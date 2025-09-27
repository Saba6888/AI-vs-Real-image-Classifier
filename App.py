from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

# ─── Flask Configuration ────────────────────────────────────────────────
app = Flask(
    __name__,
    template_folder='web_app/templates',
    static_folder='web_app/static'
)

# ─── Load Trained Model ─────────────────────────────────────────────────
MODEL_PATH = r'C:\Users\LENOVO\OneDrive\Desktop\Project 3\AI_Image_Classifier\notebooks\models\ai_vs_real_classifier.h5'

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")

model = load_model(MODEL_PATH)

# ─── Image Preprocessing ────────────────────────────────────────────────
def preprocess_image(image_path, target_size=(128, 128)):
    image = load_img(image_path, target_size=target_size)
    image_array = img_to_array(image) / 255.0
    return np.expand_dims(image_array, axis=0)

# ─── Main Route ─────────────────────────────────────────────────────────
@app.route('/', methods=['GET', 'POST'])
def upload_image():
    prediction = None
    filename = None
    note = None

    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename:
            filename = file.filename
            save_path = os.path.join(app.static_folder, filename)
            file.save(save_path)

            try:
                # Run prediction
                image_input = preprocess_image(save_path)
                raw_pred = model.predict(image_input)
                pred_array = np.squeeze(raw_pred)

                # Interpret prediction
                if pred_array.ndim == 0:  # scalar output
                    pred_scalar = float(pred_array)
                    label = 'AI-generated' if pred_scalar > 0.5 else 'Real'
                    confidence = round(pred_scalar * 100, 2)

                elif pred_array.ndim == 1:  # multi-class output
                    pred_class = int(np.argmax(pred_array))
                    confidence = round(float(pred_array[pred_class]) * 100, 2)
                    label = 'AI-generated' if pred_class == 1 else 'Real'

                else:
                    label = 'Unknown'
                    confidence = 0.0

                prediction = f"{label} ({confidence}% confidence)"
                note = "It’s an AI image." if label == 'AI-generated' else "It’s a real image."

                print("Raw prediction:", raw_pred)

            except Exception as e:
                prediction = "Prediction failed."
                note = None
                print("Error during prediction:", e)

    return render_template('Frontend.html', prediction=prediction, filename=filename, note=note)

# ─── Run Server ─────────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)