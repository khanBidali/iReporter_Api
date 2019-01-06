from flask import jsonify, request
import json
from api.models.incident import Incidents, incidents_list

from datetime import datetime

def create_redflag():
    '''This function handles creating of a new incident by passing in requested json
    data as instance variables into the Incidents class and appending the Incidents
    class namespace into the Incidents_list.'''
    data = request.json

    date_added = datetime.now
    redflag_id = len(incidents_list)
    redflag_id +=1
    reported_data = {
    	'id': redflag_id,
    	'createdOn': date_added,
    	'Type': data.get('Type'),
        'location': data.get('location'),
    	'Images': data.get('Images'),
        'comment': data.get('comment')
        }

    if not all(
        [
		data.get('Type'),
		data.get('location'),
		data.get('Images'),
		data.get('comment')
        ]
    ):
        return jsonify({'error': 'Missing field/s'}), 400
    else:
        new_incident = Incidents(
            reported_data['id'],
            reported_data['createdOn'],
            reported_data['Type'],
            reported_data['location'],
            reported_data['Images'],
            reported_data['comment']
        )
        incidents_list.append(new_incident.__dict__)
        return jsonify({'Message': 'New redflag created',
                        "Redflag": "created"}), 201

def get_one(redflag_id):
    '''This function handles returning of a specific redflags by id by passing
     in the redflag_id as the arguement'''
    try:
        updated_redflag = [
            each for each in incidents_list if each['id'] == redflag_id]
        return jsonify({'Redflag {}'.format(redflag_id): updated_redflag[0]}), 200

    except IndexError:
        return jsonify({'error': 'Not found!'}), 404


def edit_one(redflag_id):
    '''This function handles the updating of a particular redflag by id by
    passing in the redflag_id as the arguement'''
    try:
        data = request.json
        date_added = datetime.now
        updated_redflag = [
            each for each in incidents_list if each['id'] == redflag_id]
        updated_redflag[0]['createdOn'] = date_added
        updated_redflag[0]['type'] = data.get('type')
        updated_redflag[0]['location'] = data.get('location')
        updated_redflag[0]['comment'] = data.get('comment')
        updated_redflag[0]['images'] = data.get('images')
        return jsonify({'Message': 'Redflag Updated',
                        "redflag": updated_redflag}), 201

    except IndexError:
        return jsonify({'error': 'Not found!'}), 404
