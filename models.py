from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(255), nullable=False)  

    def __repr__(self):
        return f'<Title {self.title}>'
