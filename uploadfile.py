
import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename 	#This makes sure the file is secure
					#no file is to be trusted as they can be 
					#dangerous, therefore, this funtion is use
					#to secure a filename before storing it directly 
					#on the filesystem.


app = Flask(__name__)#initialize the Flask application
'''
This route will show a form to perform an AJAX request, AJAX is a method that exhange
#data with a server, and update parts of a web page wihout reloading the whole page.
@app.route('/')
'''

def main():
	return render_template('/index.html')

"""
The UPLOAD_FOLDER stores the uploaded images and the ALLOWED_EXTENSIONS
are the file extensions that the user is able to upload
"""

UPLOAD_FOLDER = 'uploads/'  #This is the path to the upload directory

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif']) 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

'''
This returns whether a file is an allowed type or not 
'''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#credits: pocoo.org

'''
This first check the file that is being request, if the file does not contained the
file part(this means if it's not a png, jpg, jpeg, or gif it would not process the
user request and it would display inside the bar 'No file part' or 'No selected file'

'''

'''
This route shows a form that performs the request to upload an image and update 

Also, if the file that is being uploaded is not the right file extension it won't 
'''
@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename): 
            filename = secure_filename(file.filename) #make the file safe
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) #move the file to the upload folder
            return redirect(url_for('upload', filename=filename)) #direct the user to the upload route, which is shwo in the browser



    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    """

app.run(
	port = int(os.getenv('PORT', 8080)), host = os.getenv('IP','0.0.0.0'))

