from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
from tensorflow import keras
from keras.utils import pad_sequences

app = Flask(__name__)

# Load the saved model
model = keras.models.load_model('nextwordpredictor.h5')

tokenizer = joblib.load('tokenizer.joblib')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    search_text = request.form['search_text'].lower()
    matching_words = generate_suggestions(search_text)
    return jsonify(matching_words)


def generate_suggestions(search_text):
    # Use the word prediction model to generate suggestions

    suggestions = ""
    next_words = 5
    max_sequence_len = 40
    try:
        for _ in range(next_words):

            token_list = tokenizer.texts_to_sequences([search_text])[0]
            token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
            predicted_probs = model.predict(token_list, verbose=0)[0]
            predicted_index = np.argmax(predicted_probs)
            output_word = ""
            for word, index in tokenizer.word_index.items():
                if index == predicted_index:
                    output_word = word
                    break

            suggestions = search_text + " " + output_word
    except Exception:
        pass
    return suggestions


if __name__ == '__main__':
    app.run(debug=True)
