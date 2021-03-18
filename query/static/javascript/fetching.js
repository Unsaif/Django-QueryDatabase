const fetch_retry = async (url, n) => {
    try {
        return await fetch(url).then(resp => resp.blob())
    } catch(err) {
        if (n === 1) throw err;
        return await fetch_retry(url, n - 1);
    }
};

const download = url => {
    return fetch_retry(url, 15)
};

const downloadByGroup = (urls, files_per_group=5) => {
return Promise.map(
    urls, 
    async url => {
    return await download(url);
    },
    {concurrency: files_per_group}
);
}

const exportZip = (blobs, names) => {
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
    elem.download = 'compressed.zip'
    elem.click()
});
}

const downloadAndZip = (urls, names) => {
    return downloadByGroup(urls, 5).then(blobs => exportZip(blobs, names));
    }