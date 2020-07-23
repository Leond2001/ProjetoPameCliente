from flask import request, Blueprint, jsonify
#from ..models import User, Product
from flask_jwt_extended import jwt_required
from ..extensions import db

product_api = Blueprint('product_api', __name__)

@product_api.route('/users/<int:id>/products/', methods=['POST'])
def create_products(id):

    data = request.json

    name = data.get('name')
    details = data.get('details')

    if not data or not name or not description:
        return {'error': 'Dados insuficientes'}, 400

    owner = User.query.get_or_404(id) #O usuário com a ID fornecida será o dono do produto

    product = Product(name=name, details=details, owner_id=owner.id) #Aqui, a variável product recebe um nome, seus detalhes e seu proprietário

    db.session.add(product)
    db.session.commit()

    return product.json(), 201