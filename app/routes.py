from flask import Blueprint, request, jsonify

main_bp = Blueprint('main', __name__)
api_bp = Blueprint('api', __name__)

@main_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@api_bp.route('/sohbet', methods=['POST', 'OPTIONS'])
def sohbet():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200

    try:
        # Hem JSON hem de Form verisini oku
        data = request.get_json(silent=True) or {}
        kullanici_mesaji = data.get('mesaj') or request.form.get('mesaj') or ''

        if not kullanici_mesaji:
            return jsonify({'basari': False, 'hata': 'Mesaj boş olamaz'}), 400

        cevap = f"SmartLead AI: Mesajınız alındı -> {kullanici_mesaji}"

        return jsonify({'basari': True, 'cevap': cevap}), 200

    except Exception as e:
        return jsonify({'basari': False, 'hata': str(e)}), 500
