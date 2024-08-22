// server.js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());
app.use(express.static('public'));

app.post('/analyze', (req, res) => {
    const { peRatio, debtEquityRatio, roa, roe, dividendYield } = req.body;

    let score = 0;
    if (peRatio < 15) score++;
    if (debtEquityRatio < 1) score++;
    if (roa > 5) score++;
    if (roe > 10) score++;
    if (dividendYield > 2) score++;

    let resultText;
    if (score >= 4) {
        resultText = 'The stock is good.';
    } else if (score >= 2) {
        resultText = 'The stock is average.';
    } else {
        resultText = 'The stock is not good.';
    }

    res.json({ result: resultText });
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
