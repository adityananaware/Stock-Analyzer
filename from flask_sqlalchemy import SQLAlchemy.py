from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    sector = db.Column(db.String(50))
    industry = db.Column(db.String(50))
    market_cap = db.Column(db.String(20))

    def __repr__(self):
        return f"<Stock {self.symbol}>"
