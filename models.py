from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    
    quantity = db.Column(db.Integer, nullable=False, default=0)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
   
    location = db.relationship('Location', foreign_keys=[location_id], back_populates='products')


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255))
   
    products = db.relationship('Product', back_populates='location', lazy='dynamic', cascade='all, delete-orphan')


class Movement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    from_location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    to_location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    qty = db.Column(db.Integer, nullable=False)
    
    timestamp = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    product = db.relationship('Product', foreign_keys=[product_id])
    from_location = db.relationship('Location', foreign_keys=[from_location_id])
    to_location = db.relationship('Location', foreign_keys=[to_location_id])
