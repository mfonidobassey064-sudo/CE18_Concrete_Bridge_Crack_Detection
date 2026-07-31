import os
import urllib.request
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Create models folder
os.makedirs("models", exist_ok=True)

MODEL_PATH = "models/tomato_classifier.keras"

MODEL_URL = "https://github.com/agape155/CE6_Tomato_Disease_Classifier/releases/download/v1.0.0/tomato_classifier.keras"

# Download model if missing
if (not os.path.exists(MODEL_PATH)) or os.path.getsize(MODEL_PATH) < 1000000:
    try:
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    except Exception as e:
        st.error(f"Failed to download model: {e}")
        st.stop()

# Load model
model = tf.keras.models.load_model(MODEL_PATH)

# Class names
classes = ["Tomato Bacterial Spot", "Tomato Target Spot"]

st.title("CE6 Tomato Disease Classifier")

st.write("""
## Tomato Disease Classification Using MobileNetV2

Upload a tomato leaf image and the trained CNN model will classify it as:

- Tomato Bacterial Spot
- Tomato Target Spot
""")

uploaded_file = st.file_uploader(
    "Upload Tomato Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_container_width=True)

    image = image.resize((224, 224))

    img = np.array(image) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    confidence = float(prediction[0][0])

    if confidence >= 0.5:
        st.success("Prediction: Tomato Target Spot")
        st.write(f"Confidence: {confidence * 100:.2f}%")
    else:
        st.success("Prediction: Tomato Bacterial Spot")
        st.write(f"Confidence: {(1 - confidence) * 100:.2f}%")