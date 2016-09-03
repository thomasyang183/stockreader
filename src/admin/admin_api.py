from flask import Blueprint, jsonify

from infrastructure import log

logger = log.getLogger("admin_api")

def get_admin_blueprint():
    admin_blueprint = Blueprint('admin_api', __name__)

    @admin_blueprint.route('/ping')
    def ping():
        return jsonify({ "message": "pong" }), 200

    return admin_blueprint