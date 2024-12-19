from flask import Blueprint, jsonify

import app.repository.terror_data as repo

terror_bluprint = Blueprint('terror', __name__)

# 1. The deadliest attack types. "Deadliest" = the types with the highest number of casualties,
# killed and injured, where a casualty = 1 point and a kill is worth 2 points for the calculation.
# a. Filter option by -5Top or All
@terror_bluprint.route('/deadliest_attack_types', methods=['GET'])
def get_deadliest_attack_types():
    res = repo.deadliest_attack_types()
    return jsonify(res)