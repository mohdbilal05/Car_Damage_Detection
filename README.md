🚗 Car Damage Detection using PyTorch


🧠 Overview
Car Damage Detection is an AI-powered web application built using PyTorch and Streamlit that automatically detects and classifies damages on car images.
This project aims to assist insurance companies, automobile workshops, and car rental services in identifying car damage efficiently — reducing human effort and decision-making time.

🚀 Live Demo
🔗 Try the app here: cardamagedetectionusingpytorch.streamlit.app
Simply upload a car image, and the model will predict whether the car is damaged or not damaged, along with the prediction confidence.

| Component            | Technology                |
| -------------------- | ------------------------- |
| **Frontend / UI**    | Streamlit                 |
| **Backend / Model**  | PyTorch                   |
| **Image Processing** | OpenCV, Pillow            |
| **Environment**      | Python 3.10+              |
| **Deployment**       | Streamlit Community Cloud |


🧩 Features

✅ Upload car images directly from your device
✅ Real-time damage classification using a fine-tuned deep learning model
✅ Confidence score for predictions
✅ Clean, responsive, and user-friendly interface
✅ Deployed and accessible online via Streamlit

🧠 Model Details
Base Model: Pre-trained CNN (ResNet / Custom CNN using PyTorch)
Training Data: Car images dataset with damaged and undamaged labels
Loss Function: Cross Entropy Loss
Optimizer: Adam
Accuracy: Achieved competitive performance on test set


🧪 Installation & Setup (Local)
Follow these steps to run the project locally:
# Clone the repository
git clone https://github.com/mohdbilal05/Car_Damage_Detection.git
cd Car_Damage_Detection

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # For Windows
# source venv/bin/activate  # For macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

📁 Project Structure
<img width="825" height="261" alt="image" src="https://github.com/user-attachments/assets/57478275-8f84-4e77-b2c3-0052882bf99b" />

🎯 Use Cases
Insurance claim automation
Car rental inspection systems
Workshop and maintenance analysis
AI-powered automotive inspection tools


🧑‍💻 About the Developer
👋 Hi, I’m Mohd Bilal
 —
A passionate AI Engineer and Generative AI Developer building intelligent systems that combine deep learning and interactive web apps.
📬 Connect with me on LinkedIn(https://www.linkedin.com/in/bilal-mohd/)
or explore more projects on GitHub(https://github.com/mohdbilal05)
