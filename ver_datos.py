from app import app
from models import db, Title

with app.app_context():
    titles = Title.query.all()
    for title in titles:
        print(title.title) 
