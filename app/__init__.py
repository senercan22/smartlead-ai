from flask import Flask
from flask_cors import CORS
from config import config_by_name
from app.database import init_db, close_connection

def create_app(config_name="dev"):
    app = Flask(__name__)

    # Konfigürasyon
    app.config.from_object(config_by_name.get(config_name, config_by_name["default"]))

    # TÜM ORIGIN, METHOD VE HEADER'LARA EKSİKSİZ İZİN VER
    CORS(app, resources={r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization", "Accept"]
    }})

    # Veritabanı
    init_db(app)
    app.teardown_appcontext(close_connection)

    # Blueprint'ler
    from app.routes import main_bp, api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
