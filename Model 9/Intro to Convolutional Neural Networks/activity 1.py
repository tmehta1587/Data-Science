
import os 
os.enivron['TD_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import numpy as np 
from tensorflow.keras.preprocessing import image
IMG_Size = 150
BATCH_SIZE = 32

train_datagen = ImageDataGenerator(
    rescale=1.255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range = 0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)
train_dir = r"C:\Users\Tinashe Mehta\New folder\Data Science\Model 9\Intro to Convolutional Neural Networks\activity 1.py"
test_dir = r"C:\Users\Tinashe Mehta\New folder\Data Science\Model 9\Intro to Convolutional Neural Networks\activity 1.py"

train_generator = train_detagen.flow_from_directory(
    train_dir, 
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE, 
    class_mode='binary'

)

train_generator = test_datagen.flow_from_directory(
    'datatset/test',
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='binary'
)