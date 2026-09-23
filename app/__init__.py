from flask import Flask
from flask_cors import CORS
from config import config_by_name
from app.database import init_db, close_connection

def create_app(config_name="dev"):
    app = Flask(__name__)

    # Konfigürasyonu yükle
    app.config.from_object(config_by_name.get(config_name, config_by_name["default"]))

    # TÜM ROTALAR VE METHODLAR İÇİN CORS İZNİ
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    # Veritabanını başlat
    init_db(app)

    # İstek bittiğinde veritabanı bağlantısını kapat
    app.teardown_appcontext(close_connection)

    # Blueprint'leri kaydet
    from app.routes import main_bp, api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
