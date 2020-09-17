from flask import Flask

from api.controllers.foods import Foods
from api.controllers.nutrients import Nutrients

from api.models.nutrient import Nutrient
from api.stores.stub_store import StubStore


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(Foods.as_blueprint())
    app.register_blueprint(Nutrients.as_blueprint())
    return app


if __name__ == '__main__':
    # It's not mandatory for the system design to call this child specific method at startup, however,
    # given that there is only one data source makes sense to initialize with the app rather than with the first request
    StubStore.populate_store()

    # Fire away
    create_app().run()
