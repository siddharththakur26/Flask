from flask_api import db
'''
Database structure is created so that it could be used to save pictures -- Not Yet Used.
'''
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(100),nullable=False,default='.jpg')


