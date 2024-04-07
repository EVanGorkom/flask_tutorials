from flask import jsonify, request, Blueprint
from app import db
from app.models import Customer, Tea, Subscription
from app.serializers import customer_serializer
import pdb

api_bp = Blueprint('api', __name__)

# Customer CRUD Functions
@api_bp.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer_serializer(customer) for customer in customers])

@api_bp.route('/customers', methods=['POST'])
def create_customers():
    data = request.data
    pdb.set_trace()
    data_name = data.get("name")
    data_email = data.get("email")

    customer = Customer(name=data_name, email=data_email)
    db.session.add(customer) #validate successful create here in future
    db.session.commit()
    return jsonify(customer_serializer(customer)), 201

@api_bp.route('/customers/<int:customers_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify([customer_serializer(customer)])

@api_bp.route('/customers/<int:customers_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    data = request.json
    customer.name = data["name"]
    customer.email = data["email"]
    db.session.commit()
    return jsonify(customer_serializer(customer))

@api_bp.route('/customers/<int:customers_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return "", 204
