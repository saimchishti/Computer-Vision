#Class-Task
# Image Viewer with OpenCV and Tkinter

This repository contains a simple Python script, `images.py`, that allows users to select and display images using the OpenCV and Tkinter libraries. The `Images` folder contains a collection of Tekken 8 wallpapers sourced from Google.

## images.py

The `images.py` script performs the following tasks:
1. **File Selection**: Uses Tkinter to open a file dialog, allowing users to select an image file.
2. **Image Loading**: Loads the selected image using the OpenCV library.
3. **Image Display**: Displays the loaded image in a new window using OpenCV.
4. **User Interaction**: Waits for the user to press a key before closing the window.

### How to Run

1. Make sure you have Python installed on your system.
2. Install the required libraries if you haven't already:
    ```bash
    pip install opencv-python-headless
    ```
3. Run the script:
    ```bash
    python images.py
    ```
4. A file dialog will open, allowing you to select an image from your system.
5. The selected image will be displayed in a new window.

### Requirements

- Python 3.x
- OpenCV
- Tkinter (usually included with Python installations)

## Images Folder

The `Images` folder contains several high-quality Tekken 8 wallpapers sourced from Google. These images can be used to test the functionality of the `images.py` script. You can also select any other image from your file system using the file dialog provided by the script.

## Notes

- Ensure that the image files you want to view are supported by OpenCV (e.g., `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`).
- The file dialog will open in the default directory. Navigate to the `Images` folder or any other directory containing your images to select and display them.

## License

This project is for educational purposes and is not intended for commercial use. The images in the `Images` folder are sourced from the internet and may be subject to copyright.

## Acknowledgments

- [OpenCV](https://opencv.org/) - An open-source computer vision library.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - The standard Python interface to the Tk GUI toolkit.
- The authors of the Tekken 8 wallpapers used in this repository.

