from django.http import JsonResponse, HttpResponse
from .querySearch import qs
import pandas as pd
from requests import get
import re
import urllib.request

def df_cleaning(df):
    df = df.dropna()
    df = df[(df["anonymized_name"] != "Not provided") & (df["anonymized_name"] != "Not applicable")]
    df = df[(df["body_site"] != "Not provided") & (df["body_site"] != "Not applicable")]
    df = df[(df["age_years"] != "Not provided") & (df["age_years"] != "Not applicable")]
    df = df[(df["bmi"] != "Not provided") & (df["bmi"] != "Not applicable")]
    df = df[(df["sex"] != "unspecified") & (df["sex"] != "true") & (df["sex"] != "false") & (df["sex"] != "other") & (df["sex"] != "Not provided") & (df["sex"] != "Not applicable")]
    return df

def accession_retrieval(result, cursor):

    samples = []
    for i in result:
        if "," in i[0]:
            multiple = i[0].split(",")
            for sample in multiple:
                samples.append(sample)
        else:
            samples.append(i[0])

    sql = "SELECT sample_title, run_accession, fastq_ftp, secondary_sample_accession, american_gut_attributes.anonymized_name FROM prjeb11419 INNER JOIN american_gut_attributes ON prjeb11419.sample_title=american_gut_attributes.sample_name WHERE sample_title IN (" + str(samples)[1:len(str(samples)) - 1] + ")" 
    cursor.execute(sql)
    sample_accessions = cursor.fetchall()
    
    accessions = []
    ftps = []
    for i in sample_accessions:
        accessions.append(i[4])
        ftps.append(i[2])

    return ftps, accessions

def control_group(testdf, controldf):

    data = testdf.astype({"age_years": float, "bmi": float})
    data_search = controldf.astype({"age_years": float, "bmi": float})
    
    sample_name_list = []
    age_list = []
    sex_list = []
    bmi_list = []
    body_site_list = []
    anonymized_list = []
    sample_list = []

    for ind, entry in data.iterrows():

        anony = entry["anonymized_name"]
        sample_list.append(anony)

        gender = entry["sex"]
        years_old = entry["age_years"]
        body_mass_index = entry["bmi"]
        body_site = entry["body_site"]
    
        search = data_search[data_search["sex"] == gender]
        search = search[search["body_site"] == body_site]

        for sample in sample_list:
            search = search[search["anonymized_name"] != sample]

        search = search[search["age_years"] == years_old]
    
        if len(search) == 0:
            i = 1
            while len(search) == 0:
                search = data_search[data_search["sex"] == gender]
                search = search[search["body_site"] == body_site]
                search = search[(search["age_years"] <= years_old + i) & (search["age_years"] >= years_old - i)]
                i += 1
    
        control = search.iloc[(search['bmi']-float(body_mass_index)).abs().argsort()[:1]]
        identity = control["anonymized_name"].values[0]
        
        sample_name_list.append(control["sample_name"].values[0])
        age_list.append(control["age_years"].values[0])
        sex_list.append(control["sex"].values[0])
        bmi_list.append(control["bmi"].values[0])
        body_site_list.append(control["body_site"].values[0])
        anonymized_list.append(identity)
    
        idx = data_search.index[data_search["anonymized_name"] == identity][0]
        data_search.drop(idx, inplace = True)
    
    control_dic = {"sample_name": sample_name_list, "anoymized_name": anonymized_list, "age_years": age_list, "sex": sex_list, "bmi": bmi_list, "body_site": body_site_list}
    control_group = pd.DataFrame(control_dic) 

    return control_group

def qp(query, cursor):
    if '/' in query:
        tc = query.split('/')
        t = tc[0]
        c = tc[1]

        #######################

        test_search = qs(t)
        cursor.execute(test_search)
        test_result = cursor.fetchall()

        test = pd.DataFrame(test_result, columns=["sample_name", "anonymized_name", "age_years", "bmi", "sex", "body_site"])
        test = df_cleaning(test)

        test_individuals = len(test_result)
        test_remaining_individuals = len(test)

        test_q = "".join(t.split())

        test_ftps = accession_retrieval(test_result, cursor)[0]
        test_accessions = accession_retrieval(test_result, cursor)[1]

        ##########################

        control_search = qs(c)
        cursor.execute(control_search)
        control_result = cursor.fetchall()

        control = pd.DataFrame(control_result, columns=["sample_name", "anonymized_name", "age_years", "bmi", "sex", "body_site"])

        control = df_cleaning(control)

        control_individuals = len(control_result)
        control_remaining_individuals = len(control)

        control_q = "".join(c.split())

        control = control_group(test, control)

        control_ftps = accession_retrieval(control.values.tolist(), cursor)[0]
        control_accessions = accession_retrieval(control.values.tolist(), cursor)[1]

        ##########################
        
        data = {
            'queryTest': test_q,
            'resultTest': test.values.tolist(),
            'individualsTest': test_remaining_individuals,
            'accessionTest': test_accessions,
            'ftpsTest': test_ftps,  
            'queryControl': control_q,
            'resultControl': control.values.tolist(),
            'individualsControl': control_remaining_individuals,
            'accessionControl': control_accessions,
            'ftpsControl': control_ftps
        }

        return JsonResponse(data)

    elif '/' not in query:

        search = qs(query)
            
        q = "".join(query.split())
        cursor.execute(search)
        result = cursor.fetchall()

        ftps = accession_retrieval(result, cursor)[0]
        accessions = accession_retrieval(result, cursor)[1]

        individuals = len(result)

        data = {
            'queryTest': q,
            'resultTest': result,
            'individualsTest': individuals,
            'accessionTest': accessions,
            'ftpsTest': ftps
        }

        return JsonResponse(data)

    else:
        return response