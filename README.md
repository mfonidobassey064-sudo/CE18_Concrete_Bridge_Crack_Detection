---
title: CE18 Concrete Bridge Deck Crack Detection
emoji: 🏗️
colorFrom: gray
colorTo: blue
sdk: streamlit
sdk_version: 1.60.0
app_file: app.py
pinned: false
---

# CE18 Concrete Bridge Deck Crack Detection Using CNN

## CE18 Mini Project

This project uses a Convolutional Neural Network (CNN) based on **MobileNetV2** to classify concrete bridge deck images into two categories:

- Cracked
- Non-Cracked

## Dataset

The dataset contains two classes:

- CD - Cracked
- UD - Non-Cracked

The dataset was separated into:

- Training Images: **70%**
- Validation Images: **15%**
- Testing Images: **15%**

The dataset was organized into separate training, validation and testing folders.

## Model Performance

- Training Accuracy: **82.45%**
- Validation Accuracy: **89.67%**
- Validation Loss: **0.3262**

## Technologies Used

- Python
- TensorFlow/Keras
- MobileNetV2
- Streamlit
- NumPy
- Pillow
- Matplotlib

## How to Run

1. Install the required packages:

```bash
pip install -r requirements.txt

2 . Run the application:
streamlit run app.py

3. Upload a concrete bridge deck image.
4. The application predicts whether the bridge deck image is:
Cracked
Non-Cracked

and displays the prediction confidence.

GitHub Repository

https://github.com/mfonidobassey064-sudo/CE18_Concrete_Bridge_Crack_Detection


BASSEY, MFONIDO RANSOM
22/EG/CE/1356
Role: Leader / Model Developer

Author
BASSEY, MFONIDO RANSOM
22/EG/CE/1356