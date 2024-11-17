import pandas as pd
import os
from src import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config

    def train_model(self,train_arr,test_arr):
        logger.info("Model Trainer Started")
        X_train=train_arr[:,:-1]
        logger.info(f"X train shape is {pd.DataFrame(X_train).shape}")
        Y_train=train_arr[:,-1]
        logger.info(f"Y train shape is {pd.DataFrame(Y_train).shape}")
        X_test=test_arr[:,:-1]
        logger.info(f"X test shape is {pd.DataFrame(X_test).shape}")
        Y_test=test_arr[:,-1]
        logger.info(f"Y test shape is {pd.DataFrame(Y_test).shape}")

        lr=ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio)
        lr.fit(X_train,Y_train)
        joblib.dump(lr,self.config.model_path)
        logger.info("Model Trainer Config")
        