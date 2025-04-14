import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from .db_manage import Db_manager
from .models.user import User
from .models.patient_treatment import Patient_Treatment
from .models.treatments import Treatments
from .models.patient_symptoms import Patient_Symptoms
from.models.symptoms import Symptoms
from .models.cancer_patient_forms import Form_Cancer_Patient

db = Db_manager().get_db()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']

    db.init_app(app)
    migrate.init_app(app, db)

    swagger = Swagger(app, template_file='swagger-ui/swagger-ui.yml')

    return app