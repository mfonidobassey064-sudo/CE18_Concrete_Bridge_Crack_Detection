---
title: CE6 Tomato Disease Classifier
emoji: 🍅
colorFrom: red
colorTo: green
sdk: streamlit
sdk_version: 1.60.0
app_file: app.py
pinned: false
---

# CE6 Tomato Disease Classifier Using CNN

## CE6 Mini Project

This project uses a Convolutional Neural Network (CNN) based on **MobileNetV2** to classify tomato leaf images into two disease categories:

- Tomato Bacterial Spot
- Tomato Target Spot

## Dataset

The dataset contains:

- Training Images: **4,653**
- Testing Images: **1,191**

**Total Images:** **5,844**

The dataset was obtained from Kaggle and organized into separate training and testing folders.

## Model Performance

- Training Accuracy: **99.13%**
- Test Accuracy: **99.58%**
- Test Loss: **0.0111**

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

3. Upload a tomato leaf image.

4. The application predicts whether the leaf image is:

- Tomato Bacterial Spot
- Tomato Target Spot

and displays the prediction confidence.

## GitHub Repository

https://github.com/agape155/CE6_Tomato_Disease_Classifier

## Author

**AGAPE DONALD**