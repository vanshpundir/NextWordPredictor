
```markdown
# Next Word Predictor Flask App

This repository contains a Flask app that serves as a Next Word Predictor using a machine learning model. The app predicts the next word based on the input text using a pre-trained model.

## Prerequisites

Before running the Flask app using Docker, ensure you have Docker installed on your system:
[https://www.docker.com/get-started](https://www.docker.com/get-started)

## How to Use

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/vanshpundir/NextWordPredictor.git
   cd NextWordPredictor
   ```

2. **Install the required Python packages** by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app locally** (optional step to test the app without Docker):

   ```bash
   python app.py
   ```

   The app will be accessible at [http://localhost:8080](http://localhost:8080).

4. **(Using Docker)** **Build the Docker image**:

   ```bash
   docker build -t next_word_app .
   ```

   This will create a Docker image named `next_word_app` based on the provided Dockerfile.

5. **(Using Docker)** **Run the Docker container**:

   ```bash
   docker run -p 8080:8080 next_word_app
   ```

   The app will be accessible at [http://localhost:8080](http://localhost:8080), just like when running it without Docker.

## Project Structure

- `app.py`: The main Flask app file that contains the routes and the word prediction logic.
- `nextwordpredictor.h5`: The saved pre-trained TensorFlow/Keras model file for word prediction.
- `tokenizer.joblib`: The serialized tokenizer object used by the model.
- `requirements.txt`: Contains the required Python packages for the Flask app.

## Notes

- The Flask app is configured to run on port 8080 inside the Docker container. If you need to use a different port, update the `app.run()` statement in `app.py`.
- The Dockerfile sets up the necessary environment and installs the required Python packages mentioned in `requirements.txt`.
- If you encounter any issues or have suggestions, feel free to open an issue or submit a pull request.

Enjoy predicting the next word with this Flask app! 🚀
```

Now, the `README.md` content is updated and formatted correctly for the provided GitHub repository link.