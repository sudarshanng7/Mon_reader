## MonReader Project
### Background:
An AI and computer vision company aims to build a new mobile document digitization experience for the blind. They want to develop a fully automatic and fast app that perfroms high quality document scanning in bulk. To that end, the company wants to develop a solution to identify if book images contain flipped pages or not. The goal is to build a machine learning model that can label images as 'flip' and 'notflip'.

### Data Description:
The data belongs to an organization that develops AI and computer vision solutions. The organization has collected page flipping videos from smartphones and the extracted frames are saved sequentially and labelled 'flip' and 'not flip'. The dataset contains
| Dataset Type | Total Records | Flip Count | Notfilp Count |
| --- | --- | --- | --- |
| Train Dataset | 2392 | 1162 | 1230 |
| Test Dataset | 597 | 290 | 307 |

Here is a quick look at some of the images from the dataset:


![dataset](https://github.com/sudarshanng7/Mon_reader/assets/47222625/2750bc2a-a9b1-42ae-91e4-fc86d8df3f29)![dataset2](https://github.com/sudarshanng7/Mon_reader/assets/47222625/c5fbbd73-8127-4afc-adc9-eab4da26ebc6)

### Goals:
Predict if the page is being flipped using a single image. Next goal is to predict if a given sequence of images contains an action of flipping.

### Success metrics:
Evaluate model performance based on F1 score and accuracy.

### Approach
As the images have been nicely structured and presented, we simply constructed a data pipeline to import the images from the folders. We applied image augmentation technique to avoid overfitting and improve the model's performance. The data is loaded into the tensorflow's dataset class with a batch size of 32 images. 
We tried out two models for this project. One being a CNN model built from scratch and the other is a pretrained EfficientNet model.

#### Model 1: Basic CNN (Baseline)
The Sequential model consists of three convolution blocks (tf.keras.layers.Conv2D) with a max pooling layer (tf.keras.layers.MaxPooling2D) in each of them. There's a fully-connected layer (tf.keras.layers.Dense) with 64 units in the end, that is activated by a ReLU activation function ('relu').
Optimizer: Adam
Epochs: 20 The number of epochs is set to 20, but the training stabilizes at around 10th epoch
##### Results
![loss_accuracy_plot_baseline](https://github.com/sudarshanng7/Mon_reader/assets/47222625/f5c2a843-6bd7-4fa8-9e59-1f102cc7ec1a)

| Metrics | Score |
| --- | --- |
| Training Accuracy | 99.58% |
| Test Accuracy | 98.9% |
| F1 Score | 0.99 |

#### Model 2: InceptionV3
Adapted from: https://www.tensorflow.org/api_docs/python/tf/keras/applications/inception_v3/InceptionV3

Here, we will use the representations learned by a previous network to extract meaningful features from new samples. This will be done by adding a new classifier, which will be trained from scratch, on top of the pretrained model so that we can repurpose the feature maps learned previously for the dataset.

We don't re-train the entire model in this step. The base convolutional network already contains features that are generically useful for classifying pictures. However, the final, classification part of the pretrained model is specific to the original classification task, and subsequently specific to the set of classes on which the model was trained.

We instantiated a InceptionV3 model pre-loaded with weights and freezing the convolutional base layers. In the next step, we added Dense layers to convert these features into a single prediction per image.
##### Results
![loss_accuracy_plot_inception](https://github.com/sudarshanng7/Mon_reader/assets/47222625/c1af56c6-f94b-48f8-b73e-c292fe62e3f0)

| Metrics | Score |
| --- | --- |
| Training Accuracy | 100%  |
| Test Accuracy | 98.85% |
| F1 Score | 0.99 |

