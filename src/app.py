from . import create_app
app = create_app()

@app.route('/')
def hello():
    return "Hello World!"

from .routes import user_routes
from .routes import cancer_patient_forms_routes
from .routes import patient_treatment_routes
from .routes import treatments_routes
from .routes import patient_symptoms_routes
from .routes import symptoms_routes
from .routes import auth_routes

if __name__ == "__main__":
    app.run()