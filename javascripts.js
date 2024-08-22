function analyzeStock() {
    // Get form values
    const peRatio = parseFloat(document.getElementById('peRatio').value);
    const debtEquityRatio = parseFloat(document.getElementById('debtEquityRatio').value);
    const sectorPeRatio = parseFloat(document.getElementById('sectorPeRatio').value);
    const pbRatio = parseFloat(document.getElementById('pbRatio').value);
    const roe = parseFloat(document.getElementById('roe').value);
    const dividendYield = parseFloat(document.getElementById('dividendYield').value);
    const marketCapitalization = parseFloat(document.getElementById('marketCapitalization').value);

    // Analysis logic (simplified)
    let score = 0;
    if (peRatio < 30) score++;
    if (debtEquityRatio < 1) score++;
    if (pbRatio < 3) score++;
    if (roe > 10) score++;
    if (dividendYield > 2) score++;
    if (peRatio < pbRatio) score++;
    if (peRatio < sectorPeRatio) score++;
    if (100000000000 > marketCapitalization > 1000000000) score++; // Assuming good if market cap is greater than $20 billion

    // Determine result
    let resultText;
    if (score >= 5) {
        resultText = 'The stock is good.';
    } else if (score >= 3) {
        resultText = 'The stock is average.';
    } else {
        resultText = 'The stock is not good.';
    }

    // Display result
    document.getElementById('result').innerText = resultText;
}
