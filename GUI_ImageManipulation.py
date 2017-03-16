'''
Title:GUI_ImageManipulation.py

Abstract:This programs utilize buttons and filters to create a gui that initialize the buttons for three different filters.
         Each button grabs the code and make the picture take the filter chosen by the user,
         displaying it on a different window.
 
Author:Ana Pena,Humberto Plaza, Yeraldiny Jose Alonzo

Ana: Worked on the GUI section
Humberto: Worked on the black and white filter section
Yeraldiny: Worked on sepia and negative filter section

GitHub Link: https://github.com/anapena1594/ana_geri_bert_prj2/blob/master/GUI_ImageManipulation.py  

Each member used Humberto's computer to push to GitHub

Date: March 15, 2015

'''

from tkinter import * 
from PIL import  ImageTk #converts image to imageTk
from PIL import Image
from PIL import *

window = Tk() #The Tk class creates a window
window.configure(background='pink') #The window is configure to have a pink background



T = Text(window, height=1, width=22, font=("Helvetica", 28)) #Title and size of the gui window config

T.pack()

T.insert(END, "Please Click a Photo") #insert a title


#-----------------------Filter_Option_Window---------------------
'''
Description:
   Buttons are use for the user to click for filter. As the user clicks on each of
   button it grabs the information that is place on the image manipution (code) for
   each filter. (black & white, sepia, and negative filters).

   The black and button filter is actually gray.
'''
def filter1():

   
   window2 = Tk() #creates windows
   
   T = Text(window2, height=1, width=28, font=("Helvetica", 32)) #windows size
   T.pack()
   T.insert(END, "Please Choose one!") #insert a title

   A = Button(window2, text = "Black and White", command = blackwhite1, font=("Helvetica",18))
   A.pack()
   
   
   
   B = Button(window2, text = "Sepia", command = Sepia1, font=("Helvetica",18))
   B.pack()

   C = Button(window2, text = "Negative", command = Negative1, font=("Helvetica",18))
   C.pack()

   window2.mainloop() #mainloop for the window to stayed open as long as the user doesn't close it.
   
   

def filter2():

   window2 = Tk() #creates windows
   
   T = Text(window2, height=1, width=28, font=("Helvetica", 32)) #windows size
   T.pack()
   T.insert(END, "Please Choose one!")

   A = Button(window2, text = "Black and White", command = blackwhite2, font=("Helvetica",18))
   A.pack()

   B = Button(window2, text = "Sepia", command = Sepia2, font=("Helvetica",18))
   B.pack()

   C = Button(window2, text = "Negative", command = Negative2, font=("Helvetica",18))
   C.pack()

   window2.mainloop() #mainloop for the window to stayed open as long as the user doesn't close it.


def filter3():

   window2 = Tk()#creates Window
  
   T = Text(window2, height=1, width=28, font=("Helvetica", 32)) #windows size
   T.pack()
   T.insert(END, "Please Choose one!")

   A = Button(window2, text = "Black and White", command = blackwhite3, font=("Helvetica",18))
   A.pack()

   B = Button(window2, text = "Sepia", command = Sepia3, font=("Helvetica",18))
   B.pack()

   C = Button(window2, text = "Negative", command = Negative3, font=("Helvetica",18))
   C.pack()

   window2.mainloop() #mainloop for the window to stayed open as long as the user doesn't close it.


#------------------Functions_Image_Manipulation----------------------
'''
Description:
   Black and white filter. As the image is open it resize the image and it
   converted to black and white. Then takes the image an converted into a TK image
   to be display on the GUI. The label show the picture on GUI and push it to
   the window using pack(). There are three buttons for each filter, the buttons are the only
   way the user is able to interact with the images, as the label is set to only let them view the image
   without modifying or change it. 
'''
def blackwhite1(): #black and white filter 
   pp = Toplevel() #Funtion that displays the image in a different window
                  #when the user click on the filter of their choice.
 
   pp.configure(background='pink') #Image background configure to pink
   image= Image.open("/Users/AnaPena/Desktop/unnamed.gif") #File directory open the picture from the hw.
   image = image.resize((550,690), Image.ANTIALIAS) #Image resize to fit on windows.
   bw=image.convert('L') #converts the image selected to black and white.
   photobw = ImageTk.PhotoImage(bw) #image taken as a Tk image to be display on the new window. 
   label = Label(pp,image=photobw) #label is a widget that let the user view but not interact with the image 
   label.image = photobw 
   label.pack()

   pp.mainloop() #loops that keeps the window open until the user close it.

 
def blackwhite2():
   pp = Toplevel() #Funtion that displays the image in a different window
                  #when the user click on the filter of their choice.

   pp.configure(background='pink') #Image background configure to pink
   image= Image.open("/Users/AnaPena/Desktop/IMG_0440.gif") #File directory open the picture from the hw.
   image = image.resize((550,690), Image.ANTIALIAS) #converts the image selected to black and white.
   bw=image.convert('L') #image taken as a Tk image to be display on the new window. 
   photobw = ImageTk.PhotoImage(bw) #label is a widget that let the user view but not interact with the image 
   label = Label(pp,image=photobw)
   label.image = photobw 
   label.pack()

   pp.mainloop() #loops that keeps the window open until the user close it.
 
   
def blackwhite3():
   pp = Toplevel() #Funtion that displays the image in a different window
                  #when the user click on the filter of their choice.

   pp.configure(background='pink') #Image background configure to pink
   image= Image.open("/Users/AnaPena/Desktop/unnamed3.gif") #File directory open the picture from the hw.
   image = image.resize((550,690), Image.ANTIALIAS) #converts the image selected to black and white.
   bw=image.convert('L') #image taken as a Tk image to be display on the new window. 
   photobw = ImageTk.PhotoImage(bw) #label is a widget that let the user view but not interact with the image 
   label = Label(pp,image=photobw)
   label.image = photobw 
   label.pack()

   pp.mainloop() #loops that keeps the window open until the user close it.

def Sepia1():
   pp = Toplevel() #Funtion that displays the image in a different window
                  #when the user click on the filter of their choice.
   
   raw_image = Image.open("/Users/AnaPena/Desktop/unnamed.gif")
   raw_image = raw_image.resize((550,690), Image.ANTIALIAS)
   WIDTH,HEIGHT = raw_image.size
   
   # Creating Image objects for Sepia and Negative Images
   sepia_image = Image.new("RGB",(WIDTH,HEIGHT))
   
   # Loading Pixel Data for all images 
   raw_pixels = raw_image.load()
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

   #Displaying The Image
   sepiaI=ImageTk.PhotoImage(sepia_image)
   label = Label(pp,image=sepiaI)
   label.raw_image = sepiaI
   label.pack()
   
   pp.mainloop() #loops that keeps the window open until the user close it.

def Sepia2():
   pp = Toplevel() #Funtion that displays the image in a different window
                  #when the user click on the filter of their choice.
   
   raw_image = Image.open("/Users/AnaPena/Desktop/IMG_0440.gif")
   raw_image = raw_image.resize((550,690), Image.ANTIALIAS)
   WIDTH,HEIGHT = raw_image.size
   
   # Creating Image objects for Sepia and Negative Images
   sepia_image = Image.new("RGB",(WIDTH,HEIGHT))
   
   # Loading Pixel Data for all images 
   raw_pixels = raw_image.load()
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

   #Displaying The Image
   sepiaI=ImageTk.PhotoImage(sepia_image)
   label = Label(pp,image=sepiaI)
   label.raw_image = sepiaI
   label.pack()
   pp.mainloop()

def Sepia3():
   pp = Toplevel() #Funtion that displays the image in a different window
                  #when the user click on the filter of their choice.
   
   raw_image = Image.open("/Users/AnaPena/Desktop/unnamed3.gif")
   raw_image = raw_image.resize((550,690), Image.ANTIALIAS)
   WIDTH,HEIGHT = raw_image.size
   
   # Creating Image objects for Sepia and Negative Images
   sepia_image = Image.new("RGB",(WIDTH,HEIGHT))
   
   # Loading Pixel Data for all images 
   raw_pixels = raw_image.load()
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

   #Displaying The Image
   sepiaI=ImageTk.PhotoImage(sepia_image)
   label = Label(pp,image=sepiaI)
   label.raw_image = sepiaI
   label.pack()
   
   pp.mainloop() #loops that keeps the window open until the user close it.

 

def Negative1():
   pp = Toplevel() #Funtion that displays the image in a different window
                  #when the user click on the filter of their choice.
   
   raw_image = Image.open("/Users/AnaPena/Desktop/unnamed.gif")
   raw_image = raw_image.resize((550,690), Image.ANTIALIAS)
   WIDTH,HEIGHT = raw_image.size
   
   # Creating Image objects for Sepia and Negative Images
   neg_image = Image.new("RGB",(WIDTH,HEIGHT))
   
   # Loading Pixel Data for all images 
   raw_pixels = raw_image.load()
 
   neg_pixels = neg_image.load()

   for Y in range(HEIGHT):
      for X in range(WIDTH):
         # Getting RGB of each pixel
         R,G,B = raw_pixels[X,Y]
         oR = (R*.393) + (G*.769) + (B*.189)
         oG = (R*.349) + (G*.686) + (B*.168)
         oB = (R*.272) + (G*.534) + (B*.131)
         # Writing pixel data after doing necessary manipulations
         neg_pixels[X,Y] = (255-R,255-G,255-B)
         
   # Saving the images
   negativeI=ImageTk.PhotoImage(neg_image)
   label = Label(pp,image=negativeI)
   label.raw_image = negativeI
   label.pack()
   
   pp.mainloop() #loops that keeps the window open until the user close it.

def Negative2():
   pp = Toplevel() #Funtion that displays the image in a different window
                  #when the user click on the filter of their choice.
   
   raw_image = Image.open("/Users/AnaPena/Desktop/IMG_0440.gif")
   raw_image = raw_image.resize((550,690), Image.ANTIALIAS)
   WIDTH,HEIGHT = raw_image.size
   
   # Creating Image objects for Sepia and Negative Images
   neg_image = Image.new("RGB",(WIDTH,HEIGHT))
   
   # Loading Pixel Data for all images 
   raw_pixels = raw_image.load()
 
   neg_pixels = neg_image.load()

   for Y in range(HEIGHT):
      for X in range(WIDTH):
         # Getting RGB of each pixel
         R,G,B = raw_pixels[X,Y]
         oR = (R*.393) + (G*.769) + (B*.189)
         oG = (R*.349) + (G*.686) + (B*.168)
         oB = (R*.272) + (G*.534) + (B*.131)
         # Writing pixel data after doing necessary manipulations
         neg_pixels[X,Y] = (255-R,255-G,255-B)
         
   # Saving the images
   negativeI=ImageTk.PhotoImage(neg_image)
   label = Label(pp,image=negativeI)
   label.raw_image = negativeI
   label.pack()
   
   pp.mainloop() #loops that keeps the window open until the user close it.

def Negative3():
   pp = Toplevel() #Funtion that displays the image in a different window
                  #when the user click on the filter of their choice.
   
   raw_image = Image.open("/Users/AnaPena/Desktop/unnamed3.gif")
   raw_image = raw_image.resize((550,690), Image.ANTIALIAS)
   WIDTH,HEIGHT = raw_image.size
   
   # Creating Image objects for Sepia and Negative Images
   neg_image = Image.new("RGB",(WIDTH,HEIGHT))
   
   # Loading Pixel Data for all images 
   raw_pixels = raw_image.load()
 
   neg_pixels = neg_image.load()

   for Y in range(HEIGHT):
      for X in range(WIDTH):
         # Getting RGB of each pixel
         R,G,B = raw_pixels[X,Y]
         oR = (R*.393) + (G*.769) + (B*.189)
         oG = (R*.349) + (G*.686) + (B*.168)
         oB = (R*.272) + (G*.534) + (B*.131)
         # Writing pixel data after doing necessary manipulations
         neg_pixels[X,Y] = (255-R,255-G,255-B)
         
   # Saving the images
   negativeI=ImageTk.PhotoImage(neg_image)
   label = Label(pp,image=negativeI)
   label.raw_image = negativeI
   label.pack()
   
   pp.mainloop() #loops that keeps the window open until the user close it.

#-------------------------Images--------------------------
#Pillow open up the Images and covert them to TKinter Images
image1= Image.open("/Users/AnaPena/Desktop/unnamed.gif")
image1= image1.resize((190,190), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image1)

image2= Image.open("/Users/AnaPena/Desktop/IMG_0440.gif")
image2= image2.resize((190,190), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)

image3= Image.open("/Users/AnaPena/Desktop/unnamed3.gif")
image3= image3.resize((190,190), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)

#------------------Image_Buttons--------------------------
p1 = Button(window, image=photo1,command = filter1 )
p1.pack()

p2 = Button(window, image=photo2,command = filter2 )
p2.pack()

p3 = Button(window, image=photo3,command = filter3 )
p3.pack()



window.mainloop() #loops that keeps the window open until the user close it.

