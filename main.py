from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
from rembg import remove
import os



#### Centering the window on the users PC ####
def centerWindow(w, h):
    screenW = root.winfo_screenwidth()
    screenH = root.winfo_screenheight()

    x = (screenW/2) - (w/2)
    y = (screenH/2.3) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))



#### Input the image that You want to use ####
def inputPicture():
    global myFile
# Choosing the file that u want #
    myFile = filedialog.askopenfilename(title="Open file",
        filetype=(("PNG", "*.png"), ("JPEG", "*.jpg;*.jpeg")))

# Checking the choosen file #
    if myFile:
        fileExtension = myFile.split(".")[-1].lower()

# Checks if the file is png, jpg or jpeg #
        if fileExtension not in ["png", "jpg", "jpeg"]:
            messagebox.showerror("Woah!", "The file is not a JPEG nor a PNG.")
        else:
            path = myFile
            
# Opening the file path to be able to put a thumbnail into the app for preview #
            inputImage = Image.open(path)
            resizedImage = inputImage.resize((400, 250))
            inputImage = ImageTk.PhotoImage(resizedImage)

# The image that appears on the screen (position of that image = left) #
            inputImageLabel = Label(frame, image=inputImage, bd=0)
            inputImageLabel.grid(row=2, column=0, padx=5, pady=30)
            inputImageLabel.image = inputImage
    else:
        messagebox.showwarning("Oops!", "No file was selected.")
    
# Removes the background (Basically the whole program) #
    workingFile = Image.open(myFile)
    outputFile = remove(workingFile)
    saveImage(outputFile)



#### Outputs the image w/o the bacground ####
def outputPicture(savePath):
# Opening the file path to be able to put a thumbnail into the app for preview #
    file2 = Image.open(savePath)
    resizedImage = file2.resize((400, 250))
    file2 = ImageTk.PhotoImage(resizedImage)

# The image without the background that appears on the screen (position of that image = right)#
    outputImageLabel = Label(frame, image=file2)
    outputImageLabel.grid(row=2, column=2, padx=5, pady=30)
    outputImageLabel.image = file2



#### Saving the cutted image ####
def saveImage(file):
# Setting a unique output file name with the exact date of the uploading #
    saveDir = "saved_pics"
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)
    
    timestamp = datetime.now().strftime('%d%m%Y%H%M%S')
    savePath = f'saved_pics/output_{timestamp}.png'
    file.save(savePath)
    
# Function that outputs the pic to the app screen
    outputPicture(savePath)


#### Main window ####
root = tk.Tk()
root.title("Emin Hodzic <> Remove background")
root.iconbitmap('C:/Python Project/Delete the bg from a picture/Assets//e.ico')

# Using themes #
style = ttk.Style(root)
root.tk.call("source", "Assets/forest-dark.tcl")
style.theme_use("forest-dark")

#### Puts the window in the center, slightly in the north position of the screen ####
centerWindow(1000, 500)
#### Locks resizing of the window ####
root.resizable(False, False)

#### Frame ####
frame = ttk.Frame(root)
frame.pack(pady=30, padx=30)

#### Input button ####
inputButton = ttk.Button(frame, text="Upload an Image", command=inputPicture)
inputButton.grid(row=1, column=1, padx=10, pady=10)


root.mainloop()