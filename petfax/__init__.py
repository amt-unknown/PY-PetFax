from flask import Flask
from flask_migrate import Migrate

# factory
def create_app():
    #config
    app = Flask(__name__)

    #database config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:zt7FsghsnpCjbB@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # index
    @app.route('/')
    def hello():
        return 'Hello, PetFax!'

    # regiser pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    # register fact blueprint
    from . import fact
    app.register_blueprint(fact.bp)

    # return app
    return app