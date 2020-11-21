from flask import request
from datetime import date
from polzybackend.authenticate import bp
from polzybackend.models import User
from polzybackend import auth


@bp.route('/login', methods=['POST'])
def login():
    # get request data
    data = request.get_json()
    
    # check for required fields in data
    required_fields = [
        'email',
        'stage',
        'language',
    ]
    for field in required_fields:
        value = data.get(field)  
        if value is None:
            return {'error': f'User data does not contain {field}'}, 400

    # get user from db
    user = User.query.filter_by(email=data['email']).first()
    # check if user found
    if user is None:
        return {'error': 'User does not exist'}, 404

    # update current stage and language
    user.set_stage(data['stage'])
    user.set_language(data['language'])

    return user.to_json(), 200


@bp.route('/company', methods=['POST'])
@auth.login_required
def set_current_company():
    # get request data
    data = request.get_json()

    # get company id
    company_id = data.get('id')
    if company_id is None:
        return {'error': 'Company data does not contain company id'}, 400

    # update company
    try:
        auth.current_user().set_company(company_id)
    except Exception as e:
        return {'error': f'Set company failed: {e}'}, 400

    return {'success': 'Success'}, 200


