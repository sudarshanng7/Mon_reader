from flask import Flask, render_template, request, redirect, url_for
import os
from uvicorn import run
import tensorflow as tf
from tensorflow.keras.models import load_model

app = Flask(__name__)
classes = ['flip', 'notflip']

model = load_model("models/cnn_classifier.h5")

@app.route("/")
def home():
    return render_template("index.html")

ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT

def prediction(filename , model):
    orig_img = tf.io.read_file(filename)
    orig_img = tf.image.decode_image(orig_img)
    img = tf.image.resize(orig_img, size=[224, 224])
    img = img/255.

    prediction = model.predict(tf.expand_dims(img, axis=0), verbose=0)
    prediction_class = classes[int(tf.round(prediction))]

    return prediction_class, prediction

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    error = ""
    target_img = os.path.join(os.getcwd(), 'static/images')
    if request.method == 'POST':
        file = request.files['myfile']
        if file and allowed_file(file.filename):
            file.save(os.path.join(target_img, file.filename))
            img_path = os.path.join(target_img, file.filename)
            img = file.filename
            
            class_result , prob_result = prediction(filename=img_path , model=model)
        else:
            error = "Please upload images of jpg , jpeg and png extension only"
            
        if len(error) == 0:
            return render_template('predict.html', user_image = img, classes=class_result)
        else:
            return render_template('index.html', error = error)
        
    else:
        return render_template("index.html")
        
        
if __name__=="__main__":
    app.run()