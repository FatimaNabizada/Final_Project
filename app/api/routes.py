from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Cloth, cloth_schema, cloths_schema

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'naw'}

# @api.route('/data')
# def viewdata():
#     data = get_contact()
#     response = jsonify(data)
#     print(response)
#     return render_template('index.html', data = data)

#cloths create function 
@api.route('/cloths', methods = ['POST'])
@token_required
def create_cloth(current_user_token):
    name = request.json['name']
    category = request.json['category']
    size = request.json['size']
    color = request.json['color']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    cloth = Cloth(name, category, size, color, user_token = user_token )

    db.session.add(cloth)
    db.session.commit()

    response = cloth_schema.dump(cloth)
    return jsonify(response)

#cloths list function 
@api.route('/cloths', methods = ['GET'])
@token_required
def get_cloth(current_user_token):
    a_user = current_user_token.token
    cloths = Cloth.query.filter_by(user_token = a_user).all()
    response = cloths_schema.dump(cloths)
    return jsonify(response)

@api.route('/cloths/<id>', methods = ['GET'])
@token_required
def get_single_cloth(current_user_token, id):
    cloth = Cloth.query.get(id)
    response = cloth_schema.dump(cloth)
    return jsonify(response)
   

# UPDATE endpoint
@api.route('/cloths/<id>', methods = ['POST','PUT'])
@token_required
def update_cloth(current_user_token,id):
    cloth = Cloth.query.get(id) 
    cloth.name = request.json['name']
    cloth.category = request.json['category']
    cloth.size = request.json['size']
    cloth.color = request.json['color']
    cloth.user_token = current_user_token.token

    db.session.commit()
    response = cloth_schema.dump(cloth)
    return jsonify(response)


# DELETE car ENDPOINT
@api.route('/cloths/<id>', methods = ['DELETE'])
@token_required
def delete_cloth(current_user_token, id):
    cloth = Cloth.query.get(id)
    db.session.delete(cloth)
    db.session.commit()
    response = cloth_schema.dump(cloth)
    return jsonify(response)