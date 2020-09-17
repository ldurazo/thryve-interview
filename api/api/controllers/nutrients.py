from flask import Blueprint, jsonify, request
from flask.views import MethodView

from api.controllers.utils import after_request_func
from api.stores.stub_store import StubStore


class Nutrients(MethodView):
    resource_name = 'nutrients'

    def post(self):
        params = request.args
        nutrients = StubStore.get_nutrients()
        return jsonify([nutrient.serialize() for nutrient in nutrients])

    @classmethod
    def as_blueprint(cls):
        bp = Blueprint(cls.resource_name, __name__)
        bp.add_url_rule('/' + cls.resource_name, view_func=Nutrients.as_view('nutrients'))
        bp.after_request(after_request_func)
        return bp
