from flask import Blueprint, jsonify

import app.repository.terror_data as repo

terror_bluprint = Blueprint('terror', __name__)

@terror_bluprint.route('/deadliest_attack_types', methods=['GET'])
def get_deadliest_attack_types():
    res = repo.deadliest_attack_types("All")
    return jsonify(res)

@terror_bluprint.route('/deadliest_attack_types/top5', methods=['GET'])
def get_deadliest_attack_types_top5():
    res = repo.deadliest_attack_types()
    return jsonify(res)

@terror_bluprint.route('/average_casualties_by_region', methods=['GET'])
def get_average_casualties_by_region():
    res = repo.average_casualties_by_region("All")
    return jsonify(res)

@terror_bluprint.route('/average_casualties_by_region/top5', methods=['GET'])
def get_average_casualties_by_region_top5():
    res = repo.average_casualties_by_region("Top 5")
    return jsonify(res)


@terror_bluprint.route('/most_active_gangs_by_region', methods=['GET'])
def get_most_active_gangs_by_region():
    res = repo.most_active_gangs_by_region(None)
    return jsonify(res)

@terror_bluprint.route('/most_active_gangs_by_region/<region_name>', methods=['GET'])
def get_most_active_gangs_by_specific_region(region_name):
    res = repo.most_active_gangs_by_region(region_name)
    return jsonify(res)


@terror_bluprint.route('/percentage_change_attacks_by_region', methods=['GET'])
def get_percentage_change_attacks_by_region():
    res = repo.percentage_change_attacks_by_region("All")
    res = res.to_dict(orient="records")
    return jsonify(res)


@terror_bluprint.route('/percentage_change_attacks_by_region/top5', methods=['GET'])
def get_percentage_change_attacks_by_region_top5():
    res = repo.percentage_change_attacks_by_region("Top 5")
    res = res.to_dict(orient="records")
    return jsonify(res)


@terror_bluprint.route('/correlation_between_terrorists_and_kills', methods=['GET'])
def get_correlation_between_terrorists_and_kills():
    res = repo.correlation_between_terrorists_and_kills()
    return jsonify(res)