from flask import render_template,url_for,flash,redirect,request,session
import jwt
import datetime
from flask_api import app
from flask_api.forms import UpdateImage
from flask_api.models import Image
from functools import wraps
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address 

# API rate limit through IP address
limiter = Limiter(app,key_func=get_remote_address)

# wrapper function to wrap the token functionality
def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        token = request.args.get('token')
        if not token:
            return "Token Missing"
        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
        except:
            return "Token Invalid"
        return f(*args, **kwargs)
    return decorated

# Home Page
@app.route("/",methods=['GET','POST'])
def assign_token():
    TOKEN = jwt.encode({'user':'admin','exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=1)},app.config['SECRET_KEY'])
    TOKEN = TOKEN.decode('UTF-8')
    if TOKEN:
        session['token'] = TOKEN
        return redirect(url_for("uploadImage",token=TOKEN))
    else:
        flash('Token is required to access','danger')
    return None

# Get the Image Name
def get_image_name(image):
    file_name,_ = os.path.splitext(image.filename)
    #image.save(file_name)
    return file_name

# FLASK-API - route to page for the user to load the image
@app.route("/upload-Image",methods=["GET","POST"])
@token_required
@limiter.limit('5 per minute')
def uploadImage():
    form = UpdateImage()
    TOKEN = session.get('token',None)
    if form.validate_on_submit():
        if form.image.data:       
            image_name = get_image_name(form.image.data)
            session['name'] = image_name
            return redirect(url_for("imageName",token=TOKEN))
    return render_template('uploadImage.html',title='Upload Image',form = form,task='Upload Image',value=TOKEN)

# FLASK-API - route to page for the user to see the name of the image
@app.route("/upload-Image/Name-of-Image",methods=["GET","POST"])
@limiter.limit('5 per minute')
@token_required
def imageName():
    form = UpdateImage()
    image_name = session.get('name',None)
    token_value = session.get('token',None)
    return render_template('nameImage.html',title='Name of Image',name=image_name,form=form,task='Image Name',value=token_value)