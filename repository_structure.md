# Repository Structure

Here's the structure of this repository:

- **WebApp/** - This folder contains code for the monreader web application
  - **models** - 
    - **cnn_classifier.h5** - Saved model
  - **static/**
    - **images/** - Contains images used as part of this project and a new image used for evaluation of the model is saved here.
  - **templates** -
    - **index.html** - HTML template for the home page.
    - **predict.html** - HTML template for the prediction page.
  - **Dockerfile** - Dockerfile to create a containerized monreader web application.
  - **app.py** - Main application file.
  - **requirements.txt** - Main requirements file containing information about the libraries used for this project.
- **models/**
  - **cnn_classifier** - Trained model saved at a checkpoint.
- **MonReader.ipynb** - This Jupyter Notebook serves as the central component for the monreader image classification task. It's designed to help users understand, train, and evaluate image classification models on a given dataset. The notebook contains code, explanations, and visualizations related to the image classification process. 
- **MonReader_Sequence.ipynb** -  The notebook contains code, explanations, and visualizations related to the image sequence classification process.
- **README.md** - This file.
