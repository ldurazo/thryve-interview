from flask import Blueprint, request, jsonify, json
from flask.views import MethodView

from api.controllers.utils import after_request_func
from api.stores.stub_store import StubStore


class Foods(MethodView):
    resource_name = 'foods'

    def post(self):
        conditions = request.get_json(force=True)
        foods = StubStore.get_foods(conditions)
        return jsonify([food.food_name for food in foods])

    def options(self):
        return '', 204

    @classmethod
    def as_blueprint(cls):
        bp = Blueprint(cls.resource_name, __name__)
        bp.add_url_rule('/' + cls.resource_name, view_func=Foods.as_view('foods'))
        bp.after_request(after_request_func)
        return bp
