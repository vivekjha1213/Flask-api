from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
# from flask_jwt_extended import jwt_required, get_raw_jwt, JWTManager
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

# DB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['users']

class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', help='This field cannot be blank', required=True)
        parser.add_argument('username', help='This field cannot be blank', required=True)
        parser.add_argument('password', help='This field cannot be blank', required=True)
        parser.add_argument('mobile_no', help='This field cannot be blank', required=True)
        parser.add_argument('address', help='This field cannot be blank', required=True)
        parser.add_argument('city', help='This field cannot be blank', required=True)
        parser.add_argument('message', help='This field cannot be blank', required=True)
        data = parser.parse_args()

        # Check if user already exists...........
        if db.users.find_one({'username': data['username']}):
            return {'message': 'User {} already exists'.format(data['username'])}, 400

        # Create the user into db...
        db.users.insert_one({
            'email': data['email'],
            'username': data['username'],
            'password': data['password'],
            'mobile_no': data['mobile_no'],
            'address': data['address'],
            'city': data['city'],
            'message': data['message']
        })

        return {'success': 'User {} created'.format(data['username']), 'message': 'We will contact you shortly'}, 201


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='This field cannot be blank', required=True)
        parser.add_argument('password', help='This field cannot be blank', required=True)
        data = parser.parse_args()

        # Authenticate the user
        user = db.users.find_one({'username': data['username'], 'password': data['password']})
        if user:
            access_token = create_access_token(identity=data['username'])
            return {'access_token': access_token}, 200

        return {'message': 'Invalid credentials'}, 401

# class Logout(Resource):
#     @jwt_required
#     def post(self):
#         # Get the user's JTI (JWT ID)
#         # jti = get_raw_jwt()['jti']
#         # Add the JTI to the blacklist in MongoDB
#         # db.blacklist.insert_one({'jti': jti})
#         return {'message': 'User logged out successfully'}, 200

# class Logout(Resource):
#     def post(self):
#         # Remove any session data here
#         response = {'message': 'User logged out successfully'}
#         return response, 200 

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
# api.add_resource(Logout, '/logout')

if __name__ == '__main__':
    app.run(debug=True)