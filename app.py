from flask import Flask, request, jsonify
from models import db, Title  

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///titles.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db.init_app(app)

@app.route('/guardar', methods=['POST'])
def guardar_titulos():
    data = request.get_json()

    if 'titles' not in data:
        return jsonify({'message': 'No se encontraron títulos en los datos.'}), 400

    titles = data['titles']

    for title_text in titles:
        new_title = Title(title=title_text)
        db.session.add(new_title)

    db.session.commit() 

    return jsonify({'message': 'Datos recibidos y guardados correctamente!'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
