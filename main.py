from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://b0c67ca3cdca79:40872f9f@us-cdbr-iron-east-02.cleardb.net/heroku_183b43ecf9ed671'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)
    apellido = db.Column(db.String(30), nullable=False) 
    celular= db.Column(db.String(13),unique=True, nullable=False, index=True)
    correo=db.Column(db.String(30), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    db.create_all()
    app.run(port=8000, debug=True)
 