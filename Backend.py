import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline, AutoTokenizer

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize sentiment analysis pipeline and tokenizer
sentiment_analyzer = pipeline('sentiment-analysis')
tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')

def analyze_sentiment(text):
    try:
        # Split text into chunks if it's too long
        max_length = tokenizer.model_max_length
        chunks = [text[i:i + max_length] for i in range(0, len(text), max_length)]
        results = [sentiment_analyzer(chunk)[0] for chunk in chunks]
        
        # Combine results from chunks
        combined_result = {
            'label': results[0]['label'],
            'score': sum(result['score'] for result in results) / len(results)  # Average score
        }
        
        return combined_result
    except Exception as e:
        return {'error': str(e)}

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            with open(filepath, 'r') as f:
                content = f.read()
            sentiment_result = analyze_sentiment(content)
            return jsonify({'transcript': content, 'sentiment': sentiment_result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
