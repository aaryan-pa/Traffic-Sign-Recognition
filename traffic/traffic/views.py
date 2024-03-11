import os
import keras
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
from PIL import Image
import sklearn
from sklearn.model_selection import train_test_split
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
from tensorflow.keras.utils import to_categorical
from PIL import Image
from django.http import HttpResponse
from django.shortcuts import render
from .form import form
sign = { 0:'Speed limit (20km/h)',1:'Speed limit (30km/h)', 2:'Speed limit (50km/h)', 3:'Speed limit (60km/h)', 
4:'Speed limit (70km/h)', 5:'Speed limit (80km/h)',6:'End of speed limit (80km/h)', 7:'Speed limit (100km/h)', 
8:'Speed limit (120km/h)',9:'No passing', 10:'No passing veh over 3.5 tons', 11:'Right-of-way at intersection', 
12:'Priority road',13:'Yield',14:'Stop',15:'No vehicles', 
16:'Vehicles > 3.5 tons prohibited', 17:'No entry',18:'General caution', 
19:'Dangerous curve left',20:'Dangerous curve right', 21:'Double curve', 22:'Bumpy road', 
23:'Slippery road',24:'Road narrows on the right', 25:'Road work', 26:'Traffic signals',27:'Pedestrians', 
28:'Children crossing',29:'Bicycles crossing', 30:'Beware of ice/snow',
31:'Wild animals crossing',32:'End speed + passing limits', 33:'Turn right ahead', 34:'Turn left ahead', 35:'Ahead only', 
36:'Go straight or right',37:'Go straight or left',38:'Keep right',39:'Keep left',40:'Roundabout mandatory',
41:'End of no passing',42:'End no passing veh > 3.5 tons' }
def result(request):
    print('HI!')
def homepage(request):
    p=''
    d={}
    ret='aa'
    context={}
    context['form']=form()
    l = []
    for i in request.POST.values():
        l.append(i)
    try:
        p=l[0]
    except:
        pass
    if request.method=='POST':
        print('p= ',p)
        ret=classify(p)
        print(ret)
        return render(request,'res.html',{'source':ret[0],'result':ret[1]})
    return render(request,'home.html',context)
def classify(p):
    ip = os.path.join(os.getcwd(),'test',p)
    ret=[]
    ret.append(ip)
    img=Image.open(ip)
    m2=keras.models.load_model('C:\\Users\\pasup\\Documents\\Project\\traffic\\m2')
    img = Image.open(ip)
    img=img.resize((32,32))
    img=np.array(img)
    img=np.expand_dims(img,axis=0)
    pred = m2.predict(img)
    ret.append(sign[np.argmax(pred)])
    savimg=Image.open(ip)
    plt.figure('Predicted Image')
    plt.imshow(savimg)
    plt.title(sign[np.argmax(pred)])
    plt.axis('off')
    plt.show()
    print(pred)
    return ret
