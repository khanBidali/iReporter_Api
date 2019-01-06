from api.models.incident import Incidents, incidents_list
from api.controllers import redflag_controller
from api.validations import Validation
from flask import Blueprint, jsonify, request
JSON_MIME_TYPE = 'application/json'

redflag = Blueprint('redflag', __name__)
validate_obj = Validation()



@redflag.route('/red-flags', methods=['POST'])
def create_new():
    '''This route creates a new redflag'''
    if request.content_type != JSON_MIME_TYPE:
        return jsonify({'error': 'Invalid Content Type'}), 406
    return redflag_controller.create_redflag()

@redflag.route('/red-flags', methods=['GET'])
def return_all():
    '''This route fetches all the redflags made'''
    return jsonify({'Redflags': incidents_list})


@redflag.route('/red-flags/<int:redflag_id>', methods=['GET'])
def return_one(redflag_id):
    '''This route fetches a specific redflag by id.'''
    specific_redflag = redflag_controller.get_one(redflag_id)
    return specific_redflag


@redflag.route('/red-flags/<int:redflag_id>', methods=['PUT'])
def update_one(redflag_id):
    '''This redflag updates a specific redflag by id.'''
    specific_redflag = redflag_controller.edit_one(redflag_id)
    return specific_redflag