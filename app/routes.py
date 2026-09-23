from flask import Blueprint, request, jsonify

main_bp = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__)

# Render'ın sağlık kontrolü (Health Check) rotası
@main_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

# Wix Chat Oturumu
@api_bp.route('/sohbet', methods=['POST', 'OPTIONS'])
def sohbet():
    # CORS Ön Kontrolü (OPTIONS)
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200

    data = request.get_json() or {}
    kullanici_mesaji = data.get('mesaj', '')

    if not kullanici_mesaji:
        return jsonify({'basari': False, 'hata': 'Mesaj boş olamaz'}), 400

    # Test yanıtı (Buraya Groq API mantığınızı bağlayabilirsiniz)
    cevap = f"Mesajınız alındı: {kullanici_mesaji}"

    return jsonify({'basari': True, 'cevap': cevap}), 200
    except Exception as e:
        return jsonify({"basari": False, "hata": "Kayıtlar çekilemedi."}), 500
