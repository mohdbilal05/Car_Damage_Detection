import streamlit as st
from model_helper import predict  # Assuming 'predict' is correctly implemented

# --- 1. SET PAGE CONFIGURATION ---
# Use a wide layout and a car-related icon for a better first impression
st.set_page_config(
    page_title="VROOM Car Damage Classification System",  # Updated page title
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. HEADER AND INTRODUCTION ---
st.title("🚗 VROOM Automated Vehicle Damage Prediction")  # Updated title
st.markdown(
    """
    This application demonstrates an **Automated Car Damage Detection System** developed for VROOM Cars.
    [cite_start]The goal of this project is to quickly and accurately classify the condition of a vehicle's front or rear based on an uploaded image[cite: 11, 15].

    [cite_start]The system uses a trained machine learning model to classify images into one of six specific damage categories with an accuracy target of at least 75%[cite: 16, 25].
    """
)

# --- CLASSIFICATION CATEGORIES ---
st.subheader("Classification Categories")
st.markdown(
    """
    The model identifies the following six conditions:
    - **Front Normal**
    - **Front Breakage**
    - **Front Crushed**
    - **Rear Normal**
    - **Rear Breakage**
    - **Rear Crushed**
    """
)
st.divider()

# --- 3. UPLOAD SECTION (Using Columns for Centering) ---
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    # Use st.file_uploader with a more informative label
    uploaded_file = st.file_uploader(
        "**Upload Image**",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=False,
        help="Maximum file size limit is 200MB. Supported formats: JPG, JPEG, PNG."
    )

# --- 4. PREDICTION LOGIC ---
if uploaded_file:
    # Use st.expander to cleanly show the uploaded image
    with st.expander("🖼️ View Uploaded Image", expanded=True):
        st.image(uploaded_file, caption=uploaded_file.name, use_container_width=True)

    # Save the file temporarily before passing to the model
    # (Optional: you might be able to pass uploaded_file or its buffer directly to your model)
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Create a cleaner prediction display box
    st.subheader("Analysis Results:")

    # Use st.spinner while prediction is running
    with st.spinner("Analyzing image..."):
        # Assuming predict(image_path) returns one of the six categories
        prediction = predict(image_path)

        # Use st.success or st.error/st.warning based on the prediction
    if "Normal" in prediction:
        st.success(f"✅ Predicted Class: **{prediction}**")
    else:
        # Use a clearer call-to-action color for damage
        st.warning(f"⚠️ Damage Detected! Predicted Class: **{prediction}**")

    # --- 5. FOOTER/PROJECT DETAILS ---
st.divider()
st.caption(f"""
    *Project Client: VROOM Cars | Service Provider: AtliQ Technologies*
""")