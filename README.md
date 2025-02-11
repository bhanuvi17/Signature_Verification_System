🏆 Signature Verification System

This is a Signature Verification web application built using Flask and OpenCV. The system compares two uploaded signatures and determines whether they match, helping in detecting forged signatures.

📌 Features
✅ Compare two signatures for authentication
✅ Uses SIFT (Scale-Invariant Feature Transform) for feature extraction
✅ Interactive web interface using Flask
✅ Deployed on Render
✅ Supports PNG, JPG, and JPEG formats
✅ Logs errors for debugging

📂 Project Structure

signature_verification/
│── app.py                     # Flask app (main file)
│── templates/
│   ├── index.html             # Frontend UI
│── requirements.txt           # Dependencies
│── Procfile                   # Render deployment config
│── README.md                  # Project info
│── .gitignore                 # Ignore unnecessary files

🎯 Technologies Used

Backend: Flask

Computer Vision: OpenCV

Deployment: Render

🔧 Installation & Setup

🔹 Clone the Repository

git clone https://github.com/bhanuvi17/Signature_Verification_System.git
cd Signature_Verification_System

🔹 Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows

🔹 Install Dependencies

pip install -r requirements.txt

🔹 Run the Flask App

python app.py

🔗 Open in your browser: http://127.0.0.1:5000/

🚀 Live Website  
<https://signature-verification-system.onrender.com/>


🚀 Deploying on Render

1️⃣ Push Code to GitHub

git add .
git commit -m "Initial commit"
git push origin main

2️⃣ Deploy on Render:

Go to Render

Click New Web Service

Connect to your GitHub repository

Set Start Command: gunicorn app:app

Click Deploy 🎉

📸 Screenshots

🔹 Web Interface
![Web Interface](https://github.com/bhanuvi17/Signature_Verification_System/blob/d7e3e1b294f5453dc99cd161c0985ddc6af824e9/Screenshot%202025-02-11%20222058.png)


🔹 Verification Result
![Verification Result](https://github.com/bhanuvi17/Signature_Verification_System/blob/d7e3e1b294f5453dc99cd161c0985ddc6af824e9/Screenshot%202025-02-11%20222140.png)


🏆 Future Enhancements
✅ Add deep learning-based signature verification
✅ Improve UI with interactive visualizations
✅ Store past verification results in a database

📜 License
This project is open-source under the MIT License.

💡 Need Help?
Feel free to open an issue or contribute to improve this project! 😊

⭐ If you like this project, give it a star on GitHub! ⭐

