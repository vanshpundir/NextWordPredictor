

```markdown
# Next Word Predictor Flask App

This repository contains a Flask app that serves as a Next Word Predictor using a machine learning model. The app predicts the next word based on the input text using a pre-trained model.

## Prerequisites

Before running the Flask app using Docker, ensure you have Docker installed on your system:
[https://www.docker.com/get-started](https://www.docker.com/get-started)

## How to Use

1. **Pull the Docker image** from Docker Hub:

   ```bash
   docker pull vanshm44/dockerhub:your_image_name
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 8080:8080 vanshm44/dockerhub:your_image_name
   ```

   The app will be accessible at [http://localhost:8080](http://localhost:8080).

## Project Structure

- `app.py`: The main Flask app file that contains the routes and the word prediction logic.
- `nextwordpredictor.h5`: The saved pre-trained TensorFlow/Keras model file for word prediction.
- `tokenizer.joblib`: The serialized tokenizer object used by the model.
- `requirements.txt`: Contains the required Python packages for the Flask app.

## Notes

- The Flask app is configured to run on port 8080 inside the Docker container. If you need to use a different port, update the `app.run()` statement in `app.py`.
- The Docker image is hosted on Docker Hub under the repository `vanshm44/dockerhub` with the tag `your_image_name`.
- If you encounter any issues or have suggestions, feel free to open an issue or submit a pull request.

Enjoy predicting the next word with this Flask app! 🚀
