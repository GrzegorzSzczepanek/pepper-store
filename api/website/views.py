from flask import Blueprint, render_template, request, jsonify, url_for, redirect
from flask_login import current_user  # login_required
from . import db
from .models import Pepper, Cart

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
    cart_items = Cart.query.all()
    categories = set([pepper.category for pepper in peppers])
    return render_template('peppers.html', peppers=peppers, cart_items=cart_items, user=current_user, categories=categories)


@views.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('search')
    category = request.args.get('category')

    peppers = Pepper.query.all()
    categories = set([pepper.category for pepper in peppers])
    filtered_peppers = [pepper for pepper in peppers if pepper.category == category]

    return render_template('peppers.html', peppers=filtered_peppers, user=current_user, categories=categories)


@views.route('/view-cart')
def shopping_cart():
    return render_template('shopping_cart.html', cart_items=Cart.query.all(), user=current_user)


@ views.route('/add-to-cart/<int:pepper_id>', methods=['POST'])
def add_to_cart(pepper_id):
    cart = Cart.query.filter_by(pepper_id=pepper_id).first()
    if cart:
        cart.quantity += 1
    else:
        cart = Cart(pepper_id=pepper_id, quantity=1)
        db.session.add(cart)
    db.session.commit()
    return redirect(url_for('views.peppers'))


@ views.route('/delete-from-cart/<int:cart_id>', methods=['POST'])
def delete_from_cart(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    cart_item.delete_item()
    return redirect(url_for('views.shopping_cart'))


@ views.route('/update-cart/<int:cart_id>', methods=['POST'])
def update_cart(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    new_quantity = request.form.get('quantity', type=int)
    cart_item.update_quantity(new_quantity)
    return redirect(url_for('views.shopping_cart'))
