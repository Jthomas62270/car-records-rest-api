from flask import Blueprint, request, jsonify 
from ..services.user_servies import create_user

auth_routes = blueprint('v1/auth', __name__)

@auth_routes.route('/auth', methods=['POST'])
def auth(): 

