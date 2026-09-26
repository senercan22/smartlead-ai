from flask import Blueprint, render_template, request, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@main_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

@main_bp.route('/api/sohbet', methods=['POST', 'OPTIONS'])
def sohbet():
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
        response.headers.add("Access-Control-Allow-Methods", "POST,OPTIONS")
        return response, 200

    try:
        data = request.get_json(silent=True) or {}
        kullanici_mesaji = data.get('mesaj') or data.get('message') or ''

        if not kullanici_mesaji:
            return jsonify({'basari': False, 'hata': 'Mesaj boş olamaz'}), 400

        cevap = f"SmartLead AI: Mesajınız alındı -> {kullanici_mesaji}"

        response = jsonify({'basari': True, 'cevap': cevap})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 200

    except Exception as e:
        response = jsonify({'basari': False, 'hata': str(e)})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 500
