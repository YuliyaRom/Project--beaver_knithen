from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    description = db.Column(db.String)
    size = db.Column(db.Integer)
    color = db.Column(db.String)
    structure = db.Column(db.String)
    price = db.Column(db.Integer)
    images = db.Column(db.String)

    def __repr__(self):
        return f"Product {self.id}, {self.Name}, {self.Category}"


