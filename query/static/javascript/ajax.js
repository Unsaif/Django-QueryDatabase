// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// $(document).ready(function(){
//     var $myForm = $('.my-ajax-form')
//     $myForm.submit(function(event){
//         event.preventDefault()
//         var $formData = $(this).serialize()
//         var $thisURL = $myForm.attr('data-url') || window.location.href // or set your own url
//         $.ajax({
//             method: "POST",
//             url: $thisURL,
//             data: $formData,
//             success: handleFormSuccess,
//             error: handleFormError,
//         })
//     })

$(document).ready(function () {
    var $myForm = $('.my-ajax-form');

    $myForm.submit(function (event) {
        event.preventDefault();

        var $form = $(this);
        var formData = $form.serialize();

        // Prefer the form's data-url as a *relative* path, or fall back to current path
        var thisURL = $form.data('url') || window.location.pathname;

        // If you really want absolute:
        // var thisURL = $form.data('url') || (window.location.origin + window.location.pathname);

        $.ajax({
            method: "POST",
            url: thisURL,
            data: formData,
            success: handleFormSuccess,
            error: handleFormError,
        });
    });

    // Button Click Handlers
    function setupDownloadButton(btnId, tc, tableId) {
        $("#" + btnId).click(async function (e) {
            e.preventDefault();
            var btn = $(this);
            var originalText = btn.text();

            // Update button content with spinner and simple text
            btn.html('<span class="spinner-border spinner-border-sm text-dark" role="status" aria-hidden="true"></span> Please wait...');
            btn.removeClass('d-none'); // Explicitly ensure it's visible
            btn.prop('disabled', true);

            try {
                // Retrieve links using fetching.js logic
                var data = linkRetrieval(tc);
                var links = data[0];
                var sampleNames = data[1];
                var totalLinks = data[2];

                // Process downloads in batches
                for (var i = 0; i < links.length; i++) {
                    await downloadAndZip(links[i], sampleNames[i], totalLinks.length, tc);
                }
            } catch (error) {
                console.error("Download failed:", error);
                alert("An error occurred during the download process.");
            } finally {
                // Reset button immediately after completion or error
                btn.html(originalText);
                btn.prop('disabled', false);
                btn.removeClass('d-none'); // Ensure it stays visible
            }
        });
    }

    setupDownloadButton("btnTest", "Test", "myTableTest");
    setupDownloadButton("btnControl", "Control", "myTableControl");

    function dataProcessing(data, tc) {

        //Test or Control
        var desc = "desc".concat(tc)
        var individuals = "individuals".concat(tc)
        var accession = "accession".concat(tc)
        var ftp = "ftps".concat(tc)
        var query = "query".concat(tc)
        var btn = "btn".concat(tc)
        var result = "result".concat(tc)
        var myTable = "myTable".concat(tc)

        //Control Display
        $("#".concat(btn)).removeClass('d-none');
        $("#".concat(btn).concat("CSV")).removeClass('d-none');
        $("#ICS").removeClass('d-none');

        var description = document.getElementById("desc".concat(tc));
        description.innerHTML = "<strong>" + data[individuals] + " Samples</strong> matched your query";

        if (tc !== "Control") {
            try {
                $("#btnControl").addClass('d-none');
                $("#btnControlCSV").addClass('d-none');
                $("#ICS").addClass('d-none');
            }
            catch (err) { }
        }

        var q = data[query]
        var accession = data[accession]
        var ftp = data[ftp]
        var myArray = data[result]

        //Conversion to accession CSV  
        let csvContent = "data:text/csv;charset=utf-8,Sample,Age,BMI,Sex,Body\ Site\n"
            + myArray.map(e => e.slice(1, 6)).join("\n");

        //remove all previous embedded anchors from previous query
        try {
            document.getElementById("link".concat(tc)).remove();
            var old_element = document.getElementById(btn.concat("CSV"));
            var new_element = old_element.cloneNode(true);
            old_element.parentNode.replaceChild(new_element, old_element);

            var anchors = document.getElementsByTagName('a');

            //remove all  tags
            if (anchors.length > 0) { //if statement required for some reason
                while (anchors[0]) {
                    anchors[0].parentNode.removeChild(anchors[0]);
                }
            }
        }
        catch (err) { }

        var encodedUri = encodeURI(csvContent);

        var link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", q.concat(".csv"));
        link.setAttribute("id", "link".concat(tc));

        document.body.appendChild(link); // Required for FF

        document.getElementById(btn.concat("CSV"))
            .addEventListener("click", function () {
                link.click();
            }, false);

        //Download Sample Data Info

        for (var n = 0; n < ftp.length; n++) {
            var temporaryDownloadLink = document.createElement("a");
            temporaryDownloadLink.style.display = 'none';
            document.body.appendChild(temporaryDownloadLink);

            var download = ftp[n];
            var downloadName = accession[n];

            var href = download;
            if (href.startsWith('http://')) {
                href = href.replace('http://', 'https://');
            } else if (!href.startsWith('https://')) {
                href = "https://" + href;
            }

            temporaryDownloadLink.setAttribute('href', href);
            temporaryDownloadLink.setAttribute('download', downloadName.toString().concat(".fastq.gz"));
            temporaryDownloadLink.setAttribute("class", tc);

        }

        //Display Table
        buildTable(myArray, myTable, data.individualsTest)
    }

    function buildTable(data, myTable, num) {
        var table = document.getElementById(myTable)
        table.innerHTML = "" // Clear previous results

        var max_num = 20
        if (num < max_num) {
            var max_num = num
        }

        for (var i = 0; i < max_num; i++) {
            const set = new Set(data[i]) //needed to get rid of strange error with using data[i] in <td>s
            array = Array.from(set)
            var row = `<tr>
                        <td>${array[1]}</td>
                        <td>${array[2]}</td>
                        <td>${array[3]}</td>
                        <td>${array[4]}</td>
                        <td>${array[5]}</td>
                    </tr>`

            table.innerHTML += row
        }
    }

    function handleFormSuccess(data, textStatus, jqXHR) {
        console.log(data)
        console.log(textStatus)
        console.log(jqXHR)
        $myForm[0].reset(); // reset form data

        $("#explainer").addClass('d-none');
        $("#results-container").removeClass('d-none');

        if (data.queryControl) {
            dataProcessing(data, "Test")
            dataProcessing(data, "Control")
        }
        else {
            dataProcessing(data, "Test")
        }
    }

    function handleFormError(jqXHR, textStatus, errorThrown) {
        var message = "Either no individual was found matching your query or query structure was wrong. Please check query";
        if (jqXHR.responseJSON && jqXHR.responseJSON.error) {
            message = jqXHR.responseJSON.error;
        }
        alert(message);
        console.log(jqXHR)
        console.log(textStatus)
        console.log(errorThrown)
    }
})
