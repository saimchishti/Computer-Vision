import cv2
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter root window and hide it
root = tk.Tk()
root.withdraw()

# Open a file dialog to select an image file
file_path = filedialog.askopenfilename(title='Select an image file', 
                                       filetypes=[('Image Files', '*.jpg;*.jpeg;*.png;*.bmp;*.tiff')])

# Check if a file was selected
if file_path:
    # Load the image using OpenCV
    image = cv2.imread(file_path)
    
    # Display the image using OpenCV
    cv2.imshow('Selected Image', image)
    
    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No file selected.")
