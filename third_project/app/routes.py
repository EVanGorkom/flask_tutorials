from flask import jsonify, request, Blueprint
from app import db
from app.models import Customer, Tea, Subscription

api_bp = Blueprint('api', __name__)

@api_bp.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.__dict__ for customer in customers])