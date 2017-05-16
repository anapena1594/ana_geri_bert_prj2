'''
Title:testapp.py
Abstract:This programs utilize python libraries and filters to create a webpage,
	 this initialize the images that are being upload and they are display in the webpage.
	 The webpage display six different filters with the same picture and the original image.
	 Each time the user uploads an image it grabs the image and (GET & POST) make the picture 
	 go through different funtions for each filter. Each filter is then directed to the webpage,
	 the user has the option to right click on the image to save it.
	 Author: Humberto Plaza, Ana Pena, Yeraldiny Jose Alonzo

Ana: Worked on the red and blur filters and contributed to the code (py and html) section
Humberto:Worked on the html page and figured how to display the images in six different 
	 boxes as well as contributing with the filters functions.
Yeraldiny: Worked on the upload section and contributed to the code (py and html) section

GitHub Link: https://github.com/anapena1594/ana_geri_bert_prj2/blob/master/testapp.py

Each member code that was done was copy and pasted into cloud 9 in order to push it to GitHub

Date: May 5, 2017
'''
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename 
from PIL import *
from PIL import Image, ImageFilter



	#This makes sure the file is secure
					#no file is to be trusted as they can be 
					#dangerous, therefore, this funtion is use
					#to secure a filename before storing it directly 
					#on the filesystem.


app = Flask(__name__)#initialize the Flask application
'''
Description:This route will show a form to perform an AJAX request, AJAX is a method that exhange
	   #data with a server, and update parts of a web page wihout reloading the whole page.
e@app.route('/')
'''


"""
Description:The UPLOAD_FOLDER stores the uploaded images and the ALLOWED_EXTENSIONS
	    are the file extensions that the user is able to upload
"""

UPLOAD_FOLDER = 'static/'  #This is the path to the upload directory

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif']) #


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

#These arrays hold the images for each filter
myPictures = []
bwPictures = []
sepPictures = []
negPictures = []
hotPictures = []
blurPictures = []

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
            faby(filename)
            blacknwhite(filename)
            sepia(filename)
            negative(filename)
            hot(filename)
            blur(filename)
    
            return render_template('/images2.html', filename=myPictures[-1], bw = bwPictures[-1], sep = sepPictures[-1], neg = negPictures[-1], hot = hotPictures[-1], blur = blurPictures[-1] )
    if(myPictures):
        print("my pictures exists")
        return render_template('/images2.html', filename=myPictures[-1], bw = bwPictures[-1], sep = sepPictures[-1],  neg = negPictures[-1], hot = hotPictures[-1], blur = blurPictures[-1] )
    else:
        print("or not")
        return render_template('/images2.html')


# Function that holds the original Picture
def faby(myPic):
    myPictures.append(myPic)


def blacknwhite(filename):

    #Open the picture that user uploaded
    ana = ('/Users/fightlikehell/Desktop/flask/app/static/' + filename)
    ana2= Image.open(ana)
    #Converts pizels to black and white using a pillow function
    ana3 = ana2.convert('L')
    ana3.save('/Users/fightlikehell/Desktop/flask/app/static/filters/blacknwhite/' + filename)
    bw = "filters/blacknwhite/" + filename
    bwPictures.append(bw)

  
def sepia(filename):

    sepiaImg = ('/Users/fightlikehell/Desktop/flask/app/static/' + filename)
    sepiaImage = Image.open(sepiaImg)
    WIDTH,HEIGHT = sepiaImage.size
   
   # Creating Image objects for Sepia and Negative Images
    sepia_image = Image.new("RGB",(WIDTH,HEIGHT))
   
   # Loading Pixel Data for all images 
    raw_pixels = sepiaImage.load()
    sepia_pixels = sepia_image.load()

    for Y in range(HEIGHT):
        for X in range(WIDTH):
         # Getting RGB of each pixel
            R,G,B = raw_pixels[X,Y]
            oR = (R*.393) + (G*.769) + (B*.189)
            oG = (R*.349) + (G*.686) + (B*.168)
            oB = (R*.272) + (G*.534) + (B*.131)
         # Writing pixel data after doing necessary manipulations
            sepia_pixels[X,Y] = (int(oR),int(oG),int(oB))
    
    
    #path = "image_sepia" + str(count) + ".jpg"
    sepia_image.save('/Users/fightlikehell/Desktop/flask/app/static/filters/sephia/' + filename)
    sep = "filters/sephia/" + filename
   
    
    sepPictures.append(sep)
    print(sepPictures)

def negative(filename):
 
    negImg = ('/Users/fightlikehell/Desktop/flask/app/static/' + filename)
    negativeImage = Image.open(negImg)
    WIDTH,HEIGHT = negativeImage.size
   
   # Creating Image objects for Sepia and Negative Images
    negative_Image= Image.new("RGB",(WIDTH,HEIGHT))
   
   # Loading Pixel Data for all images 
    raw_pixels = negativeImage.load()
 
    neg_pixels = negative_Image.load()

    for Y in range(HEIGHT):
        for X in range(WIDTH):
         # Getting RGB of each pixel
            R,G,B = raw_pixels[X,Y]
            oR = (R*.393) + (G*.769) + (B*.189)
            oG = (R*.349) + (G*.686) + (B*.168)
            oB = (R*.272) + (G*.534) + (B*.131)
         # Writing pixel data after doing necessary manipulations
            neg_pixels[X,Y] = (255-R,255-G,255-B)
         
    
    #path = "image_negative" + str(count) + ".jpg"
    negative_Image.save('/Users/fightlikehell/Desktop/flask/app/static/filters/negative/' + filename)
    neg = "filters/negative/" + filename
    negPictures.append(neg)
    print(negPictures)

def hot(filename):
 
    hotImg = ('/Users/fightlikehell/Desktop/flask/app/static/' + filename)
    hotImage = Image.open(hotImg)
    WIDTH,HEIGHT = hotImage.size
   
   # Creating Image objects for Hot
    hot_Image= Image.new("RGB",(WIDTH,HEIGHT))
   
   # 
   Loading Pixel Data for all images (original and new)
    raw_pixels = hotImage.load()
 
    hot_pixels = hot_Image.load()

    for Y in range(HEIGHT):
        for X in range(WIDTH):
         # Getting RGB of each pixel
            R,G,B = raw_pixels[X,Y]
            R1 = (R*.225) + (G*.192) + (B*.203)
            G1 = (R*.0) + (G*.192) + (B*.0)
            B1 = (R*.0) + (G*.0) + (B*.203)
         # Writing pixel data after doing necessary manipulations
            hot_pixels[X,Y] = (int(R1),int(G1),int(B1))
         
    
    #path = "image_hot" + str(count) + ".jpg"
    hot_Image.save('/Users/fightlikehell/Desktop/flask/app/static/filters/hot/' + filename)
    hot = "filters/hot/" + filename
    hotPictures.append(hot)
    print(hotPictures)

def blur(filename):
    blurImg = ('/Users/fightlikehell/Desktop/flask/app/static/' + filename)
    blurImage = Image.open(blurImg)
    blurred_image = blurImage.filter(ImageFilter.GaussianBlur(radius=50))
    blurred_image.save('/Users/fightlikehell/Desktop/flask/app/static/filters/blur/' + filename)
    blur = "filters/blur/" + filename
    blurPictures.append(blur)
    




app.run(
    debug = True,
	port = int(os.getenv('PORT', 8080)), host = os.getenv('IP','0.0.0.0'))

