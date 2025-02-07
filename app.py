from flask import Flask, render_template, request
import cv2
import os
import tempfile
import logging
from werkzeug.urls import url_quote
from urllib.parse import quote as url_quote


# Set up logging
logging.basicConfig(level=logging.INFO)

# Ensure static directory exists
if not os.path.exists('static'):
    os.makedirs('static')

app = Flask(__name__)

def preprocess_image(image_path, target_size=(300, 100)):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, target_size)
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return img

def extract_features(image):
    sift = cv2.SIFT_create()
    _, descriptors = sift.detectAndCompute(image, None)
    return descriptors

def match_features(descriptors1, descriptors2):
    flann = cv2.FlannBasedMatcher(dict(algorithm=1, trees=5), dict(checks=50))
    matches = flann.knnMatch(descriptors1, descriptors2, k=2)
    return [m for m, n in matches if m.distance < 0.7 * n.distance]

def verify_signature(image1_path, image2_path, match_threshold=10):
    img1 = preprocess_image(image1_path)
    img2 = preprocess_image(image2_path)
    descriptors1 = extract_features(img1)
    descriptors2 = extract_features(img2)
    good_matches = match_features(descriptors1, descriptors2)
    return len(good_matches), len(good_matches) >= match_threshold

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    try:
        if request.method == 'POST':
            query_image = request.files['query_image']
            reference_image = request.files['reference_image']
            match_threshold = int(request.form.get('match_threshold', 10))

            if not (query_image and reference_image):
                raise ValueError("Both files must be uploaded!")

            if not (query_image.filename.endswith(('.png', '.jpg', '.jpeg')) and 
                    reference_image.filename.endswith(('.png', '.jpg', '.jpeg'))):
                raise ValueError("Only PNG, JPG, and JPEG formats are supported!")

            # Temporary file paths
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_query:
                query_path = temp_query.name
                query_image.save(query_path)

            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_reference:
                reference_path = temp_reference.name
                reference_image.save(reference_path)

            match_count, is_match = verify_signature(query_path, reference_path, match_threshold)
            result = {
                'match_count': match_count,
                'is_match': 'Genuine Signature' if is_match else 'Forgery Signature'
            }

            # Clean up temporary files
            if os.path.exists(query_path):
                os.remove(query_path)
            if os.path.exists(reference_path):
                os.remove(reference_path)

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        result = {'error': f"An error occurred: {e}"}

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
