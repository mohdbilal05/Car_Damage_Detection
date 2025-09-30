# Deep_Learning_Project

🚗 VROOM Automated Vehicle Damage Prediction System
This project is an Automated Vehicle Damage Detection System developed by AtliQ Technologies for VROOM Cars. The system's objective is to instantly and accurately classify the condition of a car's front or rear based on an uploaded image, laying the foundation for an automated damage assessment platform.

1. Project Overview and Goal
The solution is delivered as a trained machine learning model integrated into a live Streamlit application.

Problem Statement
The model is designed to detect car damage and classify it into six possible categories with an accuracy target of at least 75%.

Classification Categories
The model classifies images into the following six distinct conditions based on the car's front or rear area:

Front Normal

Front Breakage

Front Crushed

Rear Normal

Rear Breakage

Rear Crushed

<img width="867" height="290" alt="image" src="https://github.com/user-attachments/assets/1a267e36-71fb-4723-920d-8b0e77546a32" />

3. Setup and Installation
A. Prerequisites
Python (3.8+ recommended)

The system requires access to the Streamlit app's dependencies listed in requirements.txt.

B. Environment Setup
It is essential to use a virtual environment to manage project dependencies.

Navigate to the project root directory:

Bash

cd Damage_Prediction
Create and Activate the Virtual Environment (.venv):

Bash

python -m venv .venv
Windows (PowerShell): .\.venv\Scripts\Activate.ps1

Windows (Command Prompt): .\.venv\Scripts\activate

macOS/Linux (Bash): source .venv/bin/activate

Install Dependencies:
Once the environment is active, install all necessary libraries:

Bash

pip install -r requirements.txt
4. Running the Application
After installation, the application can be launched from the project root directory (Damage_Prediction/).

Ensure your virtual environment is active.

Launch the Streamlit app:

Bash

streamlit run streamlit-app/app.py
The application will automatically open in your default web browser (typically http://localhost:8501).


2. Repository Structure
The project is organized to separate the model assets, application logic, and development files:
