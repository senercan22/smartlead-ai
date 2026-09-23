from flask import Blueprint, request, jsonify

main_bp = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__)

# Render Sağlık Kontrolü
@main_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

# Wix Chat Uç Noktası
@api_bp.route('/sohbet', methods=['POST', 'OPTIONS'])
def sohbet():
    # CORS Ön Kontrolü (OPTIONS)
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200

    try:
        data = request.get_json() or {}
        kullanici_mesaji = data.get('mesaj', '')

        if not kullanici_mesaji:
            return jsonify({'basari': False, 'hata': 'Mesaj boş olamaz'}), 400

        # Yanıt metni
        cevap = f"Mesajınız başarıyla alındı: {kullanici_mesaji}"

        return jsonify({'basari': True, 'cevap': cevap}), 200

    except Exception as e:
        return jsonify({'basari': False, 'hata': str(e)}), 500
