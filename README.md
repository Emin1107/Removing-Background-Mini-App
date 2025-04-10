# Remove Background – Desktop Image Tool (Tkinter + Python)

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**Remove Background** is a simple yet powerful desktop application built with Python and the Tkinter GUI library. It allows users to easily remove backgrounds from images (JPEG/PNG) using the powerful `rembg` library. Perfect for freelancers, designers, developers, and anyone working with images.

---

## Preview

![App Preview](/Assets/before.png)  
![App Preview](/Assets/after.png)

---

## Features

- **Easy Image Upload**  
  Intuitive file dialog for selecting an image from your computer.

- **Before & After Preview**  
  Automatically displays both the original image and the background-removed version in the app.

- **Auto-Save Output**  
  Processed images are automatically saved in the `/saved_pics` folder with a timestamp.

- **Background Removal with `rembg`**  
  Uses the `rembg` library for reliable, AI-powered background removal.

- **Modern UI Design**  
  Clean, dark-themed interface using the `forest-dark.tcl` theme for a professional look and feel.

---

## Getting Started

### Requirements

- Python 3.7+
- Install the required libraries:
  ```bash
  pip install rembg pillow
  ```

### Running the App

Run the application using:

```bash
python main.py
```

---

## How to Use

1. Launch the application.
2. Click the **"Upload an Image"** button.
3. Select a PNG or JPEG image from your computer.
4. The app will show the **original image on the left** and the **background-removed image on the right**.
5. The output image will automatically be saved in the `saved_pics/` folder with a timestamped filename.

---

## File Structure

```
.
├── main.py                 # Main Python script (GUI application)
├── Assets/
│   └── forest-dark.tcl     # Dark theme for the UI
├── saved_pics/             # Folder where output images are saved
└── README.md               # This file
```

---

## Author

**Emin Hodžić**  
Software Engineering and Management student at TU Graz.  
Currently team leader in the *AI Energy Management System* project.  
Experienced in web development (WordPress), image editing, and Python GUI applications.  
Created this tool as part of a self-learning journey and client-focused solutions.

For collaboration or freelance work, feel free to get in touch via [LinkedIn](https://www.linkedin.com/in/emin-hodzic) or GitHub.

---

## License

This project is licensed under the **Apache License** – free to use, modify, and distribute.

---

*Made with Python, curiosity, and a bit of design flair.*