## MonReader Project
### Background:

An AI and computer vision company aims to build a new mobile document digitization experience for the blind. They want to develop a fully automatic and fast app that perfroms high quality document scanning in bulk. To that end, the company wants to develop a solution to identify if book images contain flipped pages or not. The goal is to build a machine learning model that can label images as 'flip' and 'notflip'.
### Data Description:

The data belongs to an organization that develops AI and computer vision solutions. The organization has collected page flipping videos from smartphones and the extracted frames are saved sequentially and labelled 'flip' and 'not flip'.
### Goals:

    Predict if the page is being flipped using a single image.
    Evaluate model performance based on F1 score.
    Predict if a given sequence of images contains an action of flipping.


### Approach
As the images have been nicely structured and presented, we simply constructed a data pipeline to import the images from the folders. We applied image augmentation technique to avoid overfitting and improve the model's performance.
We tried out two models for this project. One being a CNN model built from scratch and the other is a pretrained EfficientNet model.

#### Model 1: Basic CNN (Baseline)

##### Results
Training Accuracy: 99.58%
Test Accuracy: 98.85%
F1 Score: 0.99

#### Model 2: EfficientNet

##### Results
Training Accuracy: 100%
Test Accuracy: 98.85%
F1 Score: 0.99

