from app import db 

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False) # Formato YYYY-MM-DD
    image = db.Column(db.String(255), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<News {self.title}>'