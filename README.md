# 🧠 AI vs Real Image Classifier

> “In a world where pixels can lie, this tool tells the truth.”

A Flask-based web app that classifies uploaded images as either **AI-generated** or **Real**, using a custom-trained CNN model. Built to raise awareness about the growing risks of synthetic media and deepfakes.

---

## 🚨 Why This Matters

With the rise of generative AI, deepfakes, and synthetic content, distinguishing real from fake is no longer optional — it’s essential. AI-generated images can be stunning, but they can also be weaponized:

- 🕵️‍♂️ Impersonation in political campaigns  
- 🧑‍⚖️ Fabricated evidence in legal cases  
- 🧨 Misinformation in journalism and social media  

This project is my contribution to building responsible AI — blending engineering with ethics.

---

## 🔧 Tech Stack

- **Frontend**: HTML/CSS (Flask templates)  
- **Backend**: Python, Flask  
- **Model**: Custom CNN trained with TensorFlow/Keras  
- **Deployment**: Local server (can be extended to cloud)

---

## 🖼️ Features

- Upload any image and get a prediction
- Confidence score with friendly feedback
- Clear verdict: *“It’s an AI image”* or *“It’s a real image”*
- Modular codebase for easy extension

---

## 📦 Setup

```bash
git clone https://github.com/saba-aafreen/AI-vs-Real-Image-Classifier.git
cd AI-vs-Real-Image-Classifier
pip install -r requirements.txt
python App.py