Sure, here's the complete set of instructions to clone the Git repository, build the Docker image, and use Docker Hub to pull the pre-built image:

```markdown
# Next Word Predictor Flask App

This repository contains a Flask app that serves as a Next Word Predictor using a machine learning model. The app predicts the next word based on the input text using a pre-trained model.

## Prerequisites

Before running the Flask app using Docker, ensure you have Docker installed on your system:
[https://www.docker.com/get-started](https://www.docker.com/get-started)

## How to Use

1. **Clone the Git repository**:

   To get started, clone the Git repository to your local machine using the following commands:

   ```bash
   git clone https://github.com/vanshpundir/NextWordPredictor.git
   cd NextWordPredictor
   ```

2. **Build the Docker image**:

   Ensure you have Docker installed and the Docker daemon is running. In the terminal, navigate to the cloned repository folder and run the following command to build the Docker image:

   ```bash
   docker build -t next-word-predictor .
   ```

   This command will build the Docker image with the name `next-word-predictor` based on the `Dockerfile` provided in the repository.

3. **Alternatively, pull the Docker image from Docker Hub**:

   If you prefer not to build the image locally, you can pull the pre-built Docker image from Docker Hub by running the following command:

   ```bash
   docker pull vanshm44/dockerhub:your_image_name
   ```

   Replace `your_image_name` with the specific tag of the Docker image you want to use. If no tag is specified, it will default to `latest`.

4. **Run the Docker container**:

   After building the Docker image or pulling it from Docker Hub (based on your preference), run the following command to start the Flask app in the Docker container:

   ```bash
   docker run -p 8080:8080 next-word-predictor
   ```

   The Flask app will be accessible at [http://localhost:8080](http://localhost:8080).

## Project Structure

- `app.py`: The main Flask app file that contains the routes and the word prediction logic.
- `nextwordpredictor.h5`: The saved pre-trained TensorFlow/Keras model file for word prediction.
- `tokenizer.joblib`: The serialized tokenizer object used by the model.
- `requirements.txt`: Contains the required Python packages for the Flask app.

## Notes

- The Flask app is configured to run on port 8080 inside the Docker container. If you need to use a different port, update the `app.run()` statement in `app.py`.
- If you encounter any issues or have suggestions, feel free to open an issue or submit a pull request.

Enjoy predicting the next word with this Flask app! 🚀
```

These instructions cover cloning the Git repository, building the Docker image locally, and optionally pulling the pre-built image from Docker Hub. You can choose the method that best suits your requirements.