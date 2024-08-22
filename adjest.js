// script.js
async function analyzeStock() {
    const peRatio = parseFloat(document.getElementById('peRatio').value);
    const debtEquityRatio = parseFloat(document.getElementById('debtEquityRatio').value);
    const roa = parseFloat(document.getElementById('roa').value);
    const roe = parseFloat(document.getElementById('roe').value);
    const dividendYield = parseFloat(document.getElementById('dividendYield').value);

    const response = await fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ peRatio, debtEquityRatio, roa, roe, dividendYield })
    });

    const data = await response.json();
    document.getElementById('result').innerText = data.result;
}
