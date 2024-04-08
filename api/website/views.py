from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Pepper
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


# @views.route('/peppers/<pepper_name>')
# def pepper(pepper_name):
#     pepper = Pepper.query.filter_by(name=pepper_name).first()
#     return render_template('pepper.html', pepper=pepper, user=current_user)


@views.route('/shopping-cart')
def shopping_cart():
    return render_template('shopping_cart.html', user=current_user)


# @views.route('/delete-comment', methods=['POST'])
# def delete_comment():
#     comment = json.loads(request.data)  # this function expects a JSON from the INDEX.js file
#     commentId = comment['commentId']
#     comment = Comment.query.get(commentId)
#     if comment:
#         if comment.user_id == current_user.id:
#             db.session.delete(comment)
#             db.session.commit()
#
#     return jsonify({})
