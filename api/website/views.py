from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Pepper, Cart
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
# @login_required
def home():
    # if request.method == 'POST':
    #     comment = request.form.get('comment')  # Gets the comment from the HTML

    return render_template("home.html", user=current_user)


@views.route('/peppers')
def peppers():
    peppers = Pepper.query.all()
    return render_template('peppers.html', peppers=peppers, user=current_user)


@views.route('/view-cart')
def shopping_cart():
    return render_template('shopping_cart.html', cart_items=Cart.query.all(), user=current_user)


@views.route('/add-to-cart/<int:pepper_id>', methods=['POST'])
def add_to_cart(pepper_id):
    cart = Cart.query.filter_by(pepper_id=product_id).first()
    if cart:
        cart.quantity += 1
    else:
        cart = Cart(pepper_id=product_id, quantity=1)
        db.session.add(cart)
    db.session.commit()
    return jsonify({})


@views.route('/remove-from-cart/<int:pepper_id>', methods=['POST'])
def remove_from_cart(pepper_id):
    cart = Cart.query.filter_by(pepper_id=product_id).first()
    if cart:
        if cart.quantity > 1:
            cart.quantity -= 1
        else:
            db.session.delete(cart)
    db.session.commit()
    return jsonify({})


@views.route('/update-cart', methods=['POST'])
def update_cart():
    cart_items = json.loads(request.data)
    for item in cart_items:
        cart = Cart.query.get(item['id'])
        if cart:
            cart.quantity = item['quantity']
    db.session.commit()
    return jsonify({})
