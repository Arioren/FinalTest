from flask import Blueprint, render_template, jsonify

from neo4j_queries.app.repository.maps import groups_with_same_target_to_mup, same_strategy_to_mup, high_groups_to_mup, \
    groups_with_wide_influence_to_mup
from neo4j_queries.app.repository.neo4j import groups_with_same_target, groups_with_same_strategy, \
    high_groups, groups_with_wide_influence, groups_with_same_purpose

neo4j_queries_bluprint = Blueprint('neo4j_queries_bluprint', __name__)

# 11
@neo4j_queries_bluprint.route("/same_target", methods=["GET"])
def get_groups_with_same_target():
    same_target = groups_with_same_target()
    groups_with_same_target_to_mup(same_target)
    return render_template('same_target.html')


# 14

@neo4j_queries_bluprint.route("/same_strategy", methods=["GET"])
def get_groups_with_same_strartegy():
    same_strategy = groups_with_same_strategy()
    same_strategy_to_mup(same_strategy)
    return render_template('same_strategy.html')



# 15
@neo4j_queries_bluprint.route("/same_purpose", methods=["GET"])
def get_groups_with_same_purpose():
    try:
        same_purpose = groups_with_same_purpose()
        return jsonify(same_purpose), 200
    except Exception as e:
        print(str(e))
        return jsonify({}), 404


# 16
@neo4j_queries_bluprint.route("/high_groups", methods=["GET"])
def get_high_groups():
    high_group = high_groups()
    high_groups_to_mup(high_group)
    return render_template('high_groups.html')


# 18
@neo4j_queries_bluprint.route("/wide_influence", methods=["GET"])
def get_groups_with_wide_influence():
    wide_influence = groups_with_wide_influence()
    groups_with_wide_influence_to_mup(wide_influence)

    return render_template('wide_influence.html')