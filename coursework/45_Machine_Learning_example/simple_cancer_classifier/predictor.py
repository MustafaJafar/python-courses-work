#import pickle
import joblib #pickle alternative

from skimage.io import imread
from skimage.transform import resize
import numpy as np
import os 

class TumorPredictor : 
    def __init__(self, model_path ='model/model.p' ):
        
        self.labels = ["cancer" , "non_cancer"]
        
        model_path = os.path.join(os.getcwd(),model_path)
        
        with open(model_path, "rb") as model : 
            self.clf = joblib.load(model)

    def read_image(self , image_path) : 
        img = imread(image_path)
        img = resize(img, (200, 200))
        return img.flatten()


    def predict(self, image_path):
        img = self.read_image(image_path)
        result = self.clf.predict([img])
        return self.labels[result[0]]



if __name__ == "__main__" : 

    image_paths = ["E:/tmp/yousif/Tumor_data_set/Gastric Slice Dataset/cancer_Sub_Ori_test1/2017-06-09_18.08.16.ndpi.16.32121_17416.2048x2048.png" , 
                   "E:/tmp/yousif/Tumor_data_set/Gastric Slice Dataset/non_cancer_subset00(2)/normal8.ndpi.17.45560_29769.2048x2048.tiff"]
    
    predictor = TumorPredictor(model_path ='model.p')

    for img in image_paths : 
        result = predictor.predict(img)
        print (result,":", img)

