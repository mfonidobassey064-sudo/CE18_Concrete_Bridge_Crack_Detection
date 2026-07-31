---
title: CE13 Skin Disease Classifier
emoji: 🩺
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.60.0
app_file: app.py
pinned: false
---

# CE13 Skin Disease Classifier Using CNN

## CE13 Mini Project

This project uses a Convolutional Neural Network (CNN) based on **MobileNetV2** to classify skin disease images into two categories:

- Candidiasis
- Tinea

## Dataset

The dataset contains:

- Training Images: **1,063**
- Testing Images: **129**

**Total Images:** **1,192**

The dataset was obtained from Kaggle and organized into separate training and testing folders.

## Model Performance

- Training Accuracy: **93.89%**
- Validation Accuracy: **89.15%**
- Validation Loss: **0.2935**

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
```

2. Run the application:

```bash
streamlit run app.py
```

3. Upload a skin disease image.

4. The application predicts whether the image is:

- Candidiasis
- Tinea

and displays the prediction confidence.

## GitHub Repository

https://github.com/kingenchanted40-code/CE13_Tinea_Candidiasis_Classifier

## Author

**ISUO, BENEDICT EDET**