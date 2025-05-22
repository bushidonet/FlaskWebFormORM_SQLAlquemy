from flask import Blueprint, request, jsonify, render_template
from app.services.form_service import save_form_data
from app.models.form_model import ContactFormModel

form_bp = Blueprint('form', __name__)

@form_bp.route('/')
def index():
    return render_template('form.html')

@form_bp.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    nuevo_campo = request.form.get('nuevo_campo')

    if not name or not email or not message:
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    entry = save_form_data(name, email, message)

    return jsonify({
        'message': 'Datos guardados correctamente',
        'data': {
            'id': entry.id,
            'name': entry.name,
            'email': entry.email,
            'message': entry.message
        }
    })
