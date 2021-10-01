from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# Create flask app
api = Blueprint('api', __name__)


app.con
@api.route('/token', methods=['POST'])
def create_token():
    response_body = {
        "message": "Hello! I am a message that came from the backend"
    }
    return jsonify(response_body), 200