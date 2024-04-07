def customer_serializer(customer):
    return {
        'id': customer.id,
        'name': customer.name,
        'email': customer.email
    }
