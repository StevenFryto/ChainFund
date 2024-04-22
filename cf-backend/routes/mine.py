from flask import Blueprint

mine_bp = Blueprint('mine', __name__)

@mine_bp.route('/login')
def login():
    return 'Login Page'
