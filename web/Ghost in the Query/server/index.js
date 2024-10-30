window.onload = function () {
    var dataOperator = new Worker("worker.sql-wasm.js");

    dataOperator.postMessage({ action: 'open' });

    const linkContainer = document.getElementById("link");
    const statusContainer = document.getElementById("s");
    const resultContainer = document.getElementById("results");
    const currentURL = window.location.search;
    const urlParams = new URLSearchParams(currentURL);

    if (urlParams.get("query")) {
        let queryText = urlParams.get("query");

        linkContainer.innerHTML = `Link to this query: <a href="?query=${queryText}">(link)</a>`;
        statusContainer.innerHTML = "Retrieved your results...";
        resultContainer.innerHTML = "Processing request...";
        document.getElementById("query").value = queryText;

        dataOperator.onmessage = function (event) {
            var output = event.data.results;
            if (!output) {
                resultContainer.innerHTML = "<b>ERROR:</b> " + event.data.error;
                return;
            }

            resultContainer.innerHTML = "";
            output.forEach(data => {
                resultContainer.appendChild(buildTable(data.columns, data.values));
            });
        }

        fetch('sql1.db')
            .then(response => response.arrayBuffer())
            .then(buffer => dataOperator.postMessage({ action: 'open', buffer: buffer }, [buffer]))
            .then(() => dataOperator.postMessage({ action: 'exec', sql: queryText }));
    }
}

var buildTable = (function () {
    function createTags(values, tag) {
        if (values.length === 0) return '';
        let openTag = `<${tag}>`, closeTag = `</${tag}>`;
        return openTag + values.join(closeTag + openTag) + closeTag;
    }

    return function (headers, rows) {
        let table = document.createElement('table');
        let tableContent = '<thead>' + createTags(headers, 'th') + '</thead>';
        let rowEntries = rows.map(row => createTags(row, 'td'));
        tableContent += '<tbody>' + createTags(rowEntries, 'tr') + '</tbody>';
        table.innerHTML = tableContent;
        return table;
    }
})();