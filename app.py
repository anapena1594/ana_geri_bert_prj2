from flask import Flask, render_template
import os
from Tkinter import * 
from PIL import  ImageTk #converts image to imageTk
from PIL import Image
from PIL import *


app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index2.html")

def blackwhite1(): #black and white filter 
   window = Tk()
   #pp = Toplevel() #Funtion that displays the image in a different window
                  #when the user click on the filter of their choice.
 
   #pp.configure(background='pink') #Image background configure to pink
   image= Image.open("/Users/AnaPena/Desktop/unnamed3.gif") #File directory open the picture from the hw.
   image = image.resize((550,690), Image.ANTIALIAS) #Image resize to fit on windows.
   bw=image.convert('L') #converts the image selected to black and white.
   photobw = ImageTk.PhotoImage(bw) #image taken as a Tk image to be display on the new window. 
   label = Label(window,image=photobw) #label is a widget that let the user view but not interact with the image 
   label.image = photobw 
   label.pack()

   window.mainloop()
    
@app.route('/my-link/')
def my_link():
	

	return blackwhite1()
    

    
if __name__ == "__main__":
    app.run()
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')


)
