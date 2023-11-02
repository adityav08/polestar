from flask import Flask, Blueprint, g
from flask_restplus import Resource, Api
from flask_cors import CORS

from polestar.services import health, positions, ships
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
CORS(app)
blueprint = Blueprint('Polestar APIs', __name__)
api = Api(blueprint,
          title='Polestar APIs',
          description="Polestar REST API",
          version="1.0.0",
          default="Polestar",
          default_label="",
          doc="/polestar/swagger",
          validate=True)

app.register_blueprint(blueprint, url_prefix="/api")


@api.route(ships.URL)
class GetAppShips(Resource):
    @api.response(200, 'Success')
    @api.response(500, 'Internal Server Error Message')
    def get(self):
        all_ships = ships.get_all_ships(g.session)
        return all_ships


@api.route(positions.URL)
class GetShipLoc(Resource):
    @api.response(200, 'Success')
    @api.response(500, 'Internal Server Error Message')
    def get(self, imo):
        return positions.get_ship_position(g.session, imo)


@api.route(health.URL)
class HealthCheck(Resource):
    @api.response(200, 'success')
    @api.response(500, 'Internal Server Error Message')
    def get(self):
        return health.get_health_status(g.session)


def initialize_db(postgres_user, postgres_password, postgres_host, postgres_port, postgres_db):
    db_url = f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}'
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION'] = Session


@app.before_request
def before_request():
    g.session = app.config['SESSION']()
