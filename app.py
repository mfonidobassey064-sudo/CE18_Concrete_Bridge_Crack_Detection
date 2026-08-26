import os
import urllib.request
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image


# CE18 CONCRETE BRIDGE DECK CRACK DETECTION

# Create models folder
os.makedirs("models", exist_ok=True)


# Model path
MODEL_PATH = "models/concrete_bridge_crack_classifier.keras"


# GitHub Release model URL
MODEL_URL = "https://github.com/mfonidobassey064-sudo/CE18_Concrete_Bridge_Crack_Detection/releases/download/v1.0.0/concrete_bridge_crack_classifier.keras"


# Download model if it does not exist
if (not os.path.exists(MODEL_PATH)) or os.path.getsize(MODEL_PATH) < 1000000:
    try:
        urllib.request.urlretrieve(
            MODEL_URL,
            MODEL_PATH
        )
    except Exception as e:
        st.error(
            f"Failed to download model: {e}"
        )
        st.stop()


# Load trained model
model = tf.keras.models.load_model(
    MODEL_PATH
)


# Class names
classes = [
    "Cracked",
    "Non-Cracked"
]


# Application title
st.title(
    "CE18 Concrete Bridge Deck Crack Detection"
)


st.write("""
## Concrete Bridge Deck Crack Detection Using MobileNetV2

Upload an image of a concrete bridge deck and the trained CNN model
will classify it as:

- Cracked
- Non-Cracked
""")


# Upload image
uploaded_file = st.file_uploader(
    "Upload Bridge Deck Image",
    type=["jpg", "jpeg", "png"]
)


# Prediction
if uploaded_file is not None:

    # Open image
    image = Image.open(
        uploaded_file
    ).convert("RGB")


    # Display uploaded image
    st.image(
        image,
        caption="Uploaded Bridge Deck Image",
        use_container_width=True
    )


    # Resize image
    image = image.resize(
        (224, 224)
    )


    # Convert image to NumPy array
    img = np.array(
        image
    ) / 255.0


    # Add batch dimension
    img = np.expand_dims(
        img,
        axis=0
    )


    # Make prediction
    prediction = model.predict(
        img,
        verbose=0
    )


    # Get probability
    confidence = float(
        prediction[0][0]
    )


    # Display prediction
    if confidence >= 0.5:

        st.success(
            "Prediction: Non-Cracked"
        )

        st.write(
            f"Confidence: {confidence * 100:.2f}%"
        )

    else:

        st.error(
            "Prediction: Cracked"
        )

        st.write(
            f"Confidence: {(1 - confidence) * 100:.2f}%"
        )