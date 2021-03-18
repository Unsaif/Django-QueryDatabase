from .metaphone import dm

def qs(query):
        
    table_metaphone = {'american_gut_attributes': 'sample_name AS SMPLNM, acid_reflux AS ASTRFLKS, acne_medication AS AKNMTKXN, acne_medication_otc AS AKNMTKXNTK, add_adhd AS ATTT, age_cat AS AJKT, age_corrected AS AJKRKTT, age_years AS AJRS, alcohol_consumption AS ALKHLKNSMPXN, alcohol_frequency AS ALKHLFRKNS, alcohol_types_beercider AS ALKHLTPSPRSTR, alcohol_types_red_wine AS ALKHLTPSRTN, alcohol_types_sour_beers AS ALKHLTPSSRPRS, alcohol_types_spiritshard_alcohol AS ALKHLTPSSPRTXRTLKHL, alcohol_types_unspecified AS ALKHLTPSNSPSFT, alcohol_types_white_wine AS ALKHLTPSTN, allergic_to_i_have_no_food_allergies_that_i_know_of AS ALRJKTFNFTLRJS0TKNF, allergic_to_other AS ALRJKT0R, allergic_to_peanuts AS ALRJKTPNTS, allergic_to_shellfish AS ALRJKTXLFX, allergic_to_tree_nuts AS ALRJKTTRNTS, allergic_to_unspecified AS ALRJKTNSPSFT, altitude AS ALTTT, alzheimers AS ALJMRS, anonymized_name AS ANNMSTNM, antibiotic_history AS ANTPTKSTR, appendix_removed AS APNTKSRMFT, artificial_sweeteners AS ARTFSLSTNRS, asd AS AST, assigned_from_geo AS ASNTFRMJ, autoimmune AS ATMN, birth_year AS PR0R, bmi AS PM, bmi_cat AS PMKT, bmi_corrected AS PMKRKTT, body_habitat AS PTPTT, body_product AS PTPRTKT, body_site AS PTST, bowel_movement_frequency AS PLMFMNTFRKNS, bowel_movement_quality AS PLMFMNTKLT, breastmilk_formula_ensure AS PRSTMLKFRMLNSR, cancer AS KNSR, cancer_treatment AS KNSRTRTMNT, cardiovascular_disease AS KRTFSKLRTSS, cat AS KT, cdiff AS KTF, census_region AS SNSSRJN, chickenpox AS XKNPKS, clinical_condition AS KLNKLKNTXN, collection_date AS KLKXNTT, collection_month AS KLKXNMN0, collection_season AS KLKXNSSN, collection_time AS KLKXNTM, collection_timestamp AS KLKXNTMSTMP, consume_animal_products_abx AS KNSMNMLPRTKTSPKS, contraceptive AS KNTRSPTF, cosmetics_frequency AS KSMTKSFRKNS, country AS KNTR, country_of_birth AS KNTRFPR0, country_residence AS KNTRRSTNS, csection AS KSKXN, deodorant_use AS TTRNTS, depression_bipolar_schizophrenia AS TPRSNPPLRXSFRN, depth AS TP0, description AS TSKPXN, diabetes AS TPTS, diabetes_type AS TPTSTP, diet_type AS TTTP, dna_extracted AS TNKSTRKTT, dog AS TK, dominant_hand AS TMNNTNT, drinking_water_source AS TRNKNKTRSRS, drinks_per_session AS TRNKSPRSSN, economic_region AS AKNMKRJN, elevation AS ALFXN, env_biome AS ANFPM, env_feature AS ANFFTR, env_material AS ANFMTRL, env_package AS ANFPKJ, epilepsy_or_seizure_disorder AS APLPSRSSRTSRTR, exercise_frequency AS AKSRSSFRKNS, exercise_location AS AKSRSSLKXN, fed_as_infant AS FTSNFNT, fermented_plant_frequency AS FRMNTTPLNTFRKNS, flossing_frequency AS FLSNKFRKNS, flu_vaccine_date AS FLFXNTT, frozen_dessert_frequency AS FRSNTSRTFRKNS, fruit_frequency AS FRTFRKNS, fungal_overgrowth AS FNKLFRKR0, geo_loc_name AS JLKNM, gluten AS KLTN, has_physical_specimen AS HSFSKLSPSMN, height_cm AS HTKM, height_units AS HTNTS, high_fat_red_meat_frequency AS HFTRTMTFRKNS, homecooked_meals_frequency AS HMKKTMLSFRKNS, host_common_name AS HSTKMNNM, host_subject_id AS HSTSPJKTT, host_taxid AS HSTTKST, ibd AS APT, ibd_diagnosis AS APTTNSS, ibd_diagnosis_refined AS APTTNSSRFNT, ibs AS APS, kidney_disease AS KTNTSS, lactose AS LKTS, last_move AS LSTMF, last_travel AS LSTTRFL, latitude AS LTTT, level_of_education AS LFLFTKXN, liver_disease AS LFRTSS, livingwith AS LFNK0, longitude AS LNJTT, lowgrain_diet_type AS LKRNTTTP, lung_disease AS LNKTSS, meat_eggs_frequency AS MTKSFRKNS, mental_illness AS MNTLLNS, mental_illness_type_anorexia_nervosa AS MNTLLNSTPNRKSNRFS, mental_illness_type_bipolar_disorder AS MNTLLNSTPPPLRTSRTR, mental_illness_type_bulimia_nervosa AS MNTLLNSTPPLMNRFS, mental_illness_type_depression AS MNTLLNSTPTPRSN, mental_illness_type_ptsd_posttraumatic_stress_disorder AS MNTLLNSTPPTSTPSTRMTKSTRSTSRTR, mental_illness_type_schizophrenia AS MNTLLNSTPXSFRN, mental_illness_type_substance_abuse AS MNTLLNSTPSPSTNSPS, mental_illness_type_unspecified AS MNTLLNSTPNSPSFT, migraine AS MKRN, milk_cheese_frequency AS MLKXSFRKNS, milk_substitute_frequency AS MLKSPSTTTFRKNS, multivitamin AS MLTFTMN, nail_biter AS NLPTR, non_food_allergies_beestings AS NNFTLRJSPSTNKS, non_food_allergies_drug_eg_penicillin AS NNFTLRJSTRKKPNSLN, non_food_allergies_pet_dander AS NNFTLRJSPTTNTR, non_food_allergies_poison_ivyoak AS NNFTLRJSPSNFK, non_food_allergies_sun AS NNFTLRJSSN, non_food_allergies_unspecified AS NNFTLRJSNSPSFT, olive_oil AS ALFL, one_liter_of_water_a_day_frequency AS ANLTRFTRTFRKNS, other_supplement_frequency AS A0RSPLMNTFRKNS, pets_other AS PTS0R, physical_specimen_location AS FSKLSPSMNLKXN, physical_specimen_remaining AS FSKLSPSMNRMNNK, pku AS PK, pool_frequency AS PLFRKNS, poultry_frequency AS PLTRFRKNS, pregnant AS PRNNT, prepared_meals_frequency AS PRPRTMLSFRKNS, probiotic_frequency AS PRPTKFRKNS, public AS PPLK, race AS RS, ready_to_eat_meals_frequency AS RTTTMLSFRKNS, red_meat_frequency AS RTMTFRKNS, roommates AS RMTS, roommates_in_study AS RMTSNSTT, salted_snacks_frequency AS SLTTSNKSFRKNS, sample_type AS SMPLTP, scientific_name AS SNTFKNM, seafood_frequency AS SFTFRKNS, seasonal_allergies AS SSNLLRJS, sex AS SKS, sibo AS SP, skin_condition AS SKNKNTXN, sleep_duration AS SLPTRXN, smoking_frequency AS SMKNKFRKNS, softener AS SFTNR, specialized_diet_exclude_dairy AS SPSLSTTTKSLTTR, specialized_diet_exclude_nightshades AS SPSLSTTTKSLTNTXTS, specialized_diet_exclude_refined_sugars AS SPSLSTTTKSLTRFNTSKRS, specialized_diet_fodmap AS SPSLSTTTFTMP, specialized_diet_halaal AS SPSLSTTTLL, specialized_diet_i_do_not_eat_a_specialized_diet AS SPSLSTTTTNTTSPSLSTTT, specialized_diet_kosher AS SPSLSTTTKXR, specialized_diet_modified_paleo_diet AS SPSLSTTTMTFTPLTT, specialized_diet_other_restrictions_not_described_here AS SPSLSTTT0RRSTRKXNSNTTSKPTR, specialized_diet_paleodiet_or_primal_diet AS SPSLSTTTPLTTRPRMLTT, specialized_diet_raw_food_diet AS SPSLSTTTRFTTT, specialized_diet_unspecified AS SPSLSTTTNSPSFT, specialized_diet_westenprice_or_other_lowgrain_low_processed_fo AS SPSLSTTTSTNPRSR0RLKRNLPRSSTF, state AS STT, subset_age AS SPSTJ, subset_antibiotic_history AS SPSTNTPTKSTR, subset_bmi AS SPSTPM, subset_diabetes AS SPSTTPTS, subset_healthy AS SPSTL0, subset_ibd AS SPSTPT, sugar_sweetened_drink_frequency AS XKRSTNTTRNKFRKNS, sugary_sweets_frequency AS XKRSTSFRKNS, survey_id AS SRFT, taxon_id AS TKSNT, teethbrushing_frequency AS T0PRXNKFRKNS, thyroid AS 0RT, title AS TTL, tonsils_removed AS TNSLSRMFT, types_of_plants AS TPSFPLNTS, vegetable_frequency AS FKTPLFRKNS, vitamin_b_supplement_frequency AS FTMNPSPLMNTFRKNS, vitamin_d_supplement_frequency AS FTMNTSPLMNTFRKNS, vivid_dreams AS FFTTRMS, weight_change AS ATXNJ, weight_kg AS ATKK, weight_units AS ATNTS, whole_eggs AS ALKS, whole_grain_frequency AS ALKRNFRKNS'}

    def same_name_check(name, lst):
        if name in lst:
            name = name + "_"
            return same_name_check(name, lst)
        else:
            return name

    data = list(map(str, query.split(";")))
    
    class_list = {}
    
    for entry in data: #deals with input statements
        if '==' in entry:
            temp = entry.split('==')
            class_list[same_name_check(temp[0].rstrip().lstrip(), class_list)] = ["==", temp[1].rstrip().lstrip()]
        elif '!=' in entry:
            temp = entry.split('!=')
            class_list[same_name_check(temp[0].rstrip().lstrip(), class_list)] = ["!=", temp[1].rstrip().lstrip()]
        elif '<=' in entry:
            temp = entry.split('<=')
            class_list[same_name_check(temp[0].rstrip().lstrip(), class_list)] = ["<=", temp[1].rstrip().lstrip()]
        elif '>=' in entry:
            temp = entry.split('>=')
            class_list[same_name_check(temp[0].rstrip().lstrip(), class_list)] = [">=", temp[1].rstrip().lstrip()]
        elif '<' in entry:
            temp = entry.split('<')
            class_list[same_name_check(temp[0].rstrip().lstrip(), class_list)] = ["<", temp[1].rstrip().lstrip()]
        elif '>' in entry:
            temp = entry.split('>')
            class_list[same_name_check(temp[0].rstrip().lstrip(), class_list)] = [">", temp[1].rstrip().lstrip()]
        else:
            print("Error in entry: Make sure operators are correct")
            return(attribute_selector_test())
    
    conditions = []
    
    for k, v in class_list.items(): 
        if v[0] == "==":
            try:
                float(v[1])
                condition = " AND (" + dm(k)[0] + " = " + v[1] + ')'
                conditions.append(condition)
            except:
                condition = " AND (" + dm(k)[0] + " LIKE '%" + v[1] + "%')"
                conditions.append(condition)
        elif v[0] == "!=":
            try:
                float(v[1])
                condition = " AND NOT (" + dm(k)[0] + " = " + v[1] + ')'
                conditions.append(condition)
            except:
                condition = " AND (" + dm(k)[0] + " NOT LIKE '%" + v[1] + "%')"
                conditions.append(condition)
        elif v[0] == "<":
            condition = " AND (" + dm(k)[0] + " < " + v[1] + ')'
            conditions.append(condition)
        elif v[0] == "<=":
            condition = " AND (" + dm(k)[0] + " <= " + v[1] + ')'
            conditions.append(condition)
        elif v[0] == ">":
            condition = " AND (" + dm(k)[0] + " > " + v[1] + ')'
            conditions.append(condition)
        else:
            condition = " AND (" + dm(k)[0] + " >= " + v[1] + ')'
            conditions.append(condition)
    
    query = "SELECT GROUP_CONCAT( DISTINCT " + dm("sample_name")[0] + " SEPARATOR ','), GROUP_CONCAT( DISTINCT " + dm("anonymized_name")[0] + " SEPARATOR ','), GROUP_CONCAT( DISTINCT " + dm("age_years")[0] + " SEPARATOR ','), GROUP_CONCAT( DISTINCT " + dm("bmi")[0] + " SEPARATOR ', '), GROUP_CONCAT( DISTINCT " + dm("sex")[0] + " SEPARATOR ','), GROUP_CONCAT( DISTINCT " + dm("body_site")[0] + " SEPARATOR ';') FROM (SELECT metaphone FROM table) AS metaphone_table WHERE "
    
    conditions.sort() #grouping same selections
    
    for condition in conditions:
        query += condition
        
    query = query.replace(" AND ", "", 1)
    
    selected_attr = ""
    for item in set(map(dm, class_list.keys())): #OR selector addition if attribute is selected multiple times
        #Adds searched column to returned data
        #if item[0] not in [dm("sample_name")[0], dm("age_years")[0], dm("sex")[0], dm("body_site")[0], dm("bmi")[0], dm("anonymized_name")[0]]:
            #selected_attr += ", GROUP_CONCAT( DISTINCT " + item[0] + " SEPARATOR ', ')"
        pos = query.rfind(" " + item[0] + " ") + len(" " + item[0] + " ")
        if query.count(" " + item[0] + " ") > 1 and (query[pos: pos + 2] not in ["< ", "> ", "<=", ">="]):
            query = query.replace(" AND " + item[0], " OR " + item[0])
            lastOR = query[query.rfind(" OR " + item[0]) + len(" OR " + item[0]):].split(' AND')[0]
            query = query.replace(lastOR, lastOR + ")", 1)
            if "WHERE " + item[0] not in query:
                query = query.replace(" OR " + item[0], " AND (" + item[0], 1)
            else:
                query = query.replace("WHERE " + item[0], "WHERE (" + item[0], 1)
        else:
            pass

    query = query.replace(" FROM (", selected_attr + " FROM (", 1)

    search = ""
    for k, v in table_metaphone.items():
        no_col = False
        for l, w in class_list.items(): #check to see if each selected attribute is in table
            if " " + dm(l)[0] + "," in v:
                pass
            else:
                no_col = True
        if no_col:
            pass
        else: 
            search += query.replace("table", k, 1).replace("metaphone", v, 1) + " GROUP BY " + dm("anonymized_name")[0] + " UNION " #+ " GROUP BY " + dm("host_subject_id")[0]
    
    search = search[:-6]  + "ORDER BY " + dm("anonymized_name")[0]
    return search