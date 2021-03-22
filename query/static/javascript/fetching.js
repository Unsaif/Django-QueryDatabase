var width = 0; 

const fetch_retry = async (url, n, total, tc) => {
    try {
        // Step 1: start the fetch and obtain a reader
        let response = await fetch(url, {cache: "no-store"});

        const reader = response.body.getReader();

        // Step 2: get total length
        const contentLength = +response.headers.get('Content-Length');

        if (contentLength / 1000000 < 3 ){ //&& contentLength / 1000 > 2

            // Step 3: read the data
            let receivedLength = 0; // received that many bytes at the moment
            let chunks = []; // array of received binary chunks (comprises the body)
            while(true) {
                const {done, value} = await reader.read();

                if (done) {
                    break;
                }

                chunks.push(value);
                receivedLength += value.length;

                var progress = receivedLength/contentLength + width
                $("#progress".concat(tc)).css('width', (progress/total)*100+'%').attr('aria-valuenow', (progress/total)*100); 
                //$(".progress-bar").attr('innerHTML', (progress/total)*100 + '%');

                //console.log(`Received ${receivedLength} of ${contentLength}`)
            }

            width++; 

            if (width === total){
                width=0
            }

            let blob = new Blob(chunks);

            return blob
        }
        else {
            console.log("massive")
        }
    } 
    catch(err) {
        if (n === 1) throw err;
        return await fetch_retry(url, n - 1);
    }
};

const download = (url, total, tc) => {
    return fetch_retry(url, 15, total, tc)
};

const downloadByGroup = (urls, files_per_group, total, tc) => {
return Promise.map(
    urls, 
    async url => {
    return await download(url, total, tc);
    },
    {concurrency: files_per_group}
);
}

const exportZip = (blobs, names, tc) => {

const zip = JSZip();

blobs.forEach((blob, i) => {
    zip.file(names[i], blob);
});

zip.generateAsync({type: 'blob'}).then((blobdata)=> {
    let zipblob = new Blob([blobdata])
    // For development and testing purpose
    // Download the zipped file 
    var elem = window.document.createElement("a")
    elem.href = window.URL.createObjectURL(zipblob)
    elem.download = 'compressed'.concat(tc).concat('.zip')
    elem.click()
});
}

const linkRetrieval = tc => {

    $("#progress".concat(tc)).removeClass('d-none');
    $("#btn".concat(tc)).addClass('d-none');

    var classes = document.body.getElementsByClassName(tc);
    var links = []
    var names = []

    for(var n = 0; n < classes.length; n++) {   
        links.push(classes[n].href)
        names.push(classes[n].download)
    }

    var size = 25; var arrayOfArrays = []; var arrayOfArraysNames = [];

    for (var i=0; i<links.length; i+=size) {
        arrayOfArrays.push(links.slice(i,i+size));
        arrayOfArraysNames.push(names.slice(i,i+size));
    }

    if (arrayOfArrays.length > 1) {
        alert("Download exceeds 25 samples. Download will be broken into batches of 25")
    } 
    
    return [arrayOfArrays, arrayOfArraysNames, links]
} 

const downloadAndZip = (urls, names, total, tc) => {
    return downloadByGroup(urls, 1, total, tc).then(blobs => exportZip(blobs, names, tc));
    }