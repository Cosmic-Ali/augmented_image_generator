
# Augmented Image Generator

💻 A user-friendly tool to generate synthetic image data by applying various augmentations to existing images. Built with [Streamlit](https://streamlit.io/), this application provides an intuitive interface for augmenting images, aiding in the expansion of datasets for machine learning and computer vision tasks.

> **Note:** This is a **beta version**.

## Features

- **Streamlit Interface**: Interactive web application for seamless user experience.
- **Image Augmentation**: Apply a variety of transformations to images to create augmented datasets.
- **Customizable Parameters**: Adjust augmentation settings to suit specific needs.
- **Batch Processing**: Augment multiple images simultaneously.

## Installation (Local)

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Cosmic-Ali/augmented_image_generator.git
   cd augmented_image_generator
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Locally**

   ```bash
   streamlit run app.py
   ```
## File Structure

```plaintext
augmented_image_generator/
├── .streamlit/             # Streamlit configuration files
├── data/                   # Directory to store input images
├── app.py                  # Main application script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## **Run on cloud platform**
   
   Access the live app at:

👉 [https://huggingface.co/spaces/Cosmic-Ali/augmented\_img\_generator](https://huggingface.co/spaces/Cosmic-Ali/augmented_img_generator)


---

## Usage (Deployed)

* Select augmentation options and parameters.
* View the augmented images in real-time.
* Download the augmented images as needed.

## Augmentation Techniques

The application supports a range of augmentation techniques, including but not limited to:

* **Rotation**: Rotate images by a specified degree range.
* **Flipping**: Horizontally or vertically flip images.
* **Scaling**: Zoom in or out of images.
* **Translation**: Shift images along the X and Y axes.
* **Shearing**: Stretch/shear images along the corners.
* **Cropping**: Crop parts of the image.

*Note: The exact augmentation options available can be viewed and adjusted within the Streamlit interface.*

## Future Updates

* I plan to **add more transformation types** (e.g., color jitter, perspective warp).
* **Refinements** to the UI and parameter controls are on the roadmap.
* Any **breaking changes** or new features will be noted here as the project evolves.

## License

This project is open for experimentation and improvement. Feel free to explore and modify it for your needs.

## Acknowledgments

This tool uses [Streamlit](https://streamlit.io/) to power its interactive UI for image augmentation.

```
```
---
title: Augmented Img Generator
emoji: 💻
colorFrom: indigo
colorTo: blue
sdk: streamlit
sdk_version: 1.45.0
app_file: app.py
pinned: false
short_description: Generates synthetic image data by augmenting given images
---
