from flask_openapi3 import OpenAPI, APIBlueprint, Info
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from rabbitmq_pika_flask import RabbitMQ


info = Info(
    title='Flask Rabbitmq API',
    version='1.0.0',
    termsOfService='http://example.com/terms/',
    contact={
        'name': 'API Support',
        'url': 'http://www.example.com/support',
        'email': 'support@example.com'
    },
    license={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html'
    }
)

app = OpenAPI(
    __name__,
    info=info,
    servers=[{'url': 'http://localhost:5000'}]
)
app.config.from_object('config')

CORS(app, origins=[
    'http://localhost:5000/api/v1',
    'http://localhost:5000/openapi'
])

rabbitmq = RabbitMQ(app, 'flask_rabbitmq')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

api = APIBlueprint('flask-rabbitmq', __name__, url_prefix='/api/v1')

from api.routes import course_route

app.register_api(api)
