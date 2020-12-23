
import os
import numpy as np
import tensorflow
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
# from tensorflow.keras.applications import DenseNet201
from tensorflow.keras.layers import GlobalAveragePooling2D
# from tensorflow_addons.optimizers import RectifiedAdam
from tensorflow.keras.optimizers import Adam,SGD
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import confusion_matrix, classification_report
# import seaborn as sns
import pandas as pd
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator



class Ai():
    def __init__(self):
        self.rootPath = './image_data/통합본2'
        self.category_csv = pd.read_csv('./category/category3.csv')
        self.label_dict = dict(self.category_csv[['bottle_name', 'bottle_id']].values)
        self.model_path = './model/recycle_model3.h5' ## 경로 
        self.dense_model = tf.keras.models.load_model(self.model_path)
    
    def predict(self):
        val_imageGenerator = ImageDataGenerator(
            rescale=1./255,
            # validation_split=.2
        )

        validationGen = val_imageGenerator.flow_from_directory(
            self.rootPath,
            # target_size=(64, 256),
            target_size=(224, 224),
            # subset='validation',
            batch_size = 1,
            class_mode="sparse"
        )


        Y_pred = self.dense_model.predict_generator(validationGen, 1)
        y_pred = np.argmax(Y_pred, axis=1) # 결과값입니다!!!!!
        print(y_pred)

        return y_pred


