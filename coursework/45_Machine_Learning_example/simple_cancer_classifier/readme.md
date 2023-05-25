# Simple Cancer Classifier

Testing a [simple ML example](https://www.youtube.com/watch?v=il8dMDlXrIE) with a tumor dataset [Data for HCRF](https://data.mendeley.com/datasets/thgf23xgy7/2)



## Objective

The main objective of this model is to develop the project structure

By creating : 
- Model File
- Prediction Class

## Simple Cancer Classifier

It consists of two code files : 
- main.py

    > which trains ML model, estimates accuracy and save model file.

- predictor.py

    >in which a `TumorPredictor` is defined that makes use of the the model file.


## Classifier Algorithm 

Based on `Scikit SVC` classification algorithm. 

  - prepare data
  - train / test split
  - train classifier
  - test performance
  - save model file