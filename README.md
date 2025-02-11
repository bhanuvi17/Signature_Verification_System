# 🏆 Signature Verification System

This is a Signature Verification web application built using Flask and OpenCV. The system compares two uploaded signatures and determines whether they match, helping in detecting forged signatures.

## 📌 Features
✅ Compare two signatures for authentication  
✅ Uses SIFT (Scale-Invariant Feature Transform) for feature extraction  
✅ Interactive web interface using Flask  
✅ Deployed on Render  
✅ Supports PNG, JPG, and JPEG formats  
✅ Logs errors for debugging  

## 📂 Project Structure
```
signature_verification/
│── app.py                  # Flask app (main file)
│── templates/
│   ├── index.html          # Frontend UI
│── requirements.txt        # Dependencies
│── Procfile                # Render deployment config
│── README.md               # Project info
│── .gitignore              # Ignore unnecessary files
```

## 🎯 Technologies Used
- **Backend:** Flask  
- **Computer Vision:** OpenCV  
- **Deployment:** Render  

## 🔧 Installation & Setup

### 🔹 Clone the Repository
```sh
git clone https://github.com/bhanuvi17/Signature_Verification_System.git
cd Signature_Verification_System
```

### 🔹 Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 🔹 Install Dependencies
```sh
pip install -r requirements.txt
```

### 🔹 Run the Flask App
```sh
python app.py
```

🔗 Open in your browser: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 🚀 Live Website
[Signature Verification System](https://signature-verification-system.onrender.com/)

## 🚀 Deploying on Render

### 1️⃣ Push Code to GitHub
```sh
git add .
git commit -m "Initial commit"
git push origin main
```

### 2️⃣ Deploy on Render:
1. Go to [Render](https://render.com/)
2. Click **New Web Service**
3. Connect to your GitHub repository
4. Set Start Command: `gunicorn app:app`
5. Click **Deploy** 🎉

## 🖼️ Screenshots
- **Web Interface**  
  _(Insert Screenshot Here)_
- **Verification Result**  
  _(Insert Screenshot Here)_

## 🏆 Future Enhancements
✅ Add deep learning-based signature verification  
✅ Improve UI with interactive visualizations  
✅ Store past verification results in a database  

## 📝 License
This project is open-source under the **MIT License**.

## 💡 Need Help?
Feel free to open an issue or contribute to improve this project! 😊

⭐ If you like this project, give it a star on GitHub! ⭐

