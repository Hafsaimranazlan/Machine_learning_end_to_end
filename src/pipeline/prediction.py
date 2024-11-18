import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from src.utils.common import load_bin
from src import logger

class PredictionPipeline:
    def __init__(self):
        logger.info("laoding preprocessor object")
        self.prepro_obj=load_bin(Path("data/processed/prepro.joblib"))
        logger.info("loading model object")
        self.model=load_bin(Path("models/model.joblib"))

    def predict(self,data):
        logger.info("Data prediction started.")
        data_trans=self.prepro_obj.fit_transform(data)
        logger.info("Model Training is started.")
        predictions=self.model.predict(data_trans)

        return predictions
    
if __name__=="__main__":
    fixedacidity =float(input("fixed acidity:"))
    volatileacidity =float(input("volatile acidity"))
    citricacid  = float(input("citric acid"))
    residualsugar =float(input("residual sugar"))
    chlorides =float(input("chlorides"))
    freesulfurdioxide =float(input("free sulfur dioxide"))
    totalsulfurdioxide =float(input("total sulfur dioxide"))
    density =float(input("density"))
    pH =float(input("PH"))
    sulphates =float(input("sulphates"))
    alcohol =float(input("alcohol"))
    dict1={
        "fixed acidity" :   [fixedacidity] ,
        "volatile acidity" : [volatileacidity],
        "citric acid"  : [citricacid],
        "residual sugar" : [residualsugar],
        "chlorides" : [chlorides],
        "free sulfur dioxide" : [freesulfurdioxide],
        "total sulfur dioxide" : [totalsulfurdioxide],
        "density" : [density],
        "pH" : [pH],
        "sulphates" : [sulphates],
        "alcohol" : [alcohol]
    }
    print(dict1)
    data=pd.DataFrame(dict1)
    print(data)
    obj=PredictionPipeline()
    save=obj.predict(data)
    print(save)
    