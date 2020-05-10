from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileField
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

'''
Flask Form to upload the picture.
'''
class UpdateImage(FlaskForm):
    image = FileField('Choose the Image from your drive!',validators=[FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField('Upload')