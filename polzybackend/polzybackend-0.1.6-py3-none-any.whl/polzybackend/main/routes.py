from flask import jsonify, request, current_app
from datetime import date
from polzybackend.policy import Policy
from polzybackend.models import User, Activity, ActivityType
from polzybackend.utils.import_utils import get_policy_class, get_all_stages, get_activity_class
from polzybackend.main import bp
from polzybackend import auth


@bp.route('/stage')
def get_stages():
    #
    # returns list of all available stages
    #

    try:
        # get all stages
        stages = get_all_stages()()
        current_app.logger.debug(f"Value of stages: {stages}")
    except Exception as e:
        current_app.logger.warning(f'Failed to get All Stages: {e}')
        stages = []

    return jsonify(stages), 200


@bp.route('/policy/<string:policy_number>/<string:effective_date>')
@bp.route('/policy/<string:policy_number>')
@auth.login_required
def get_policy(policy_number, effective_date=None):
    #
    # fetches a Policy by policy_number & effective_data
    # and returns it
    #

    # set default effective_date if needed
    if effective_date is None:
        effective_date = str(date.today())

    try:
        # get Policy
        policy = get_policy_class()(policy_number, effective_date)
        # update policy stage and language
        policy.setStage(auth.current_user().stage)
        policy.setLanguage(auth.current_user().language)
        current_app.logger.warning(f"Stage={policy.stage}, lang={policy.language}")

        if policy.fetch():
            policy.set_user(auth.current_user())
            current_app.config['POLICIES'][policy.uuid] = policy
            result = policy.get()
            # DEBUG
            #import json 
            #print(json.dumps(result, indent=2))

            # save activity to DB
            Activity.read_policy(policy_number, effective_date, auth.current_user())
            
            # set response
            response_code = 400 if 'error' in result else 200
            return jsonify(result), response_code


    except Exception as e:
        current_app.logger.exception(f'Fetch policy {policy_number} {effective_date} failed: {e}')
        return jsonify({'error': str(e)}), 400

    return jsonify({'error': 'Policy not found'}), 404


@bp.route(f'/activity', methods=['POST'])
@auth.login_required
def new_activity():
    #
    # create new activity
    #

    # get post data
    data = request.get_json()

    # get policy and create activity 
    try:
        # get policy from app store
        policy = current_app.config['POLICIES'].get(data['id'])
        if policy is None:
            raise Exception(f'Policy {data["id"]} is absent in PoLZy storage')

        # save activity to DB
        activity = Activity.new(data, policy, auth.current_user())

        # execute activity
        result = policy.executeActivity(data['activity'])
        # update activity status
        activity.finish('OK' if result else 'Failed')

        if result:
            # update policy
            policy.setStage(auth.current_user().stage)
            policy.setLanguage(auth.current_user().language)
            current_app.logger.warning(f"Stage={policy.stage}, lang={policy.language}")

            # check if activity returns not bool result
            if not result is True:
                return jsonify(result), 200

            policy.fetch()
            return jsonify(policy.get()), 200
        
    except Exception as e:
        current_app.logger.warning(f'Execution activity {data.get("name")} for policy {policy.policy_number} faild: {e}')
        return jsonify({'error': 'Bad Request'}), 400

    return jsonify({
        'id': str(activity.id),
        'status': 'Failed',
    }), 400
