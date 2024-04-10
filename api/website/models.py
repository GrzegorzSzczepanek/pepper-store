from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


class Pepper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(1000))
    price = db.Column(db.Float)
    availability = db.Column(db.String(11))
    category = db.Column(db.String(30))
    cart_items = db.relationship('Cart', backref='pepper', lazy=True)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pepper_id = db.Column(db.Integer, db.ForeignKey('pepper.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    def update_quantity(self, new_quantity):
        if new_quantity > 0:
            self.quantity = new_quantity
        else:
            db.session.delete(self)
        db.session.commit()

    def delete_item(self):
        db.session.delete(self)
        db.session.commit()
