from app import app
from app import db
from routes import api

app.register_blueprint(api, url_prefix='/api')

if __name__ == "__main__":
    db.create_all()
    app.run()
