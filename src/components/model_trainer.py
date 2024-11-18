import pandas as pd
import os
import joblib
from src import logger
from src.entity.config_entity import ModelTrainerConfig
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score,mean_squared_error
from src.utils.common import save_json,save_bin
from pathlib import Path


class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config

    def evaluate(self,X_train,Y_train,X_test,Y_test):
        lr=ElasticNet(alpha=self.config.alpha,l1_ratio=self.config.l1_ratio)
        lr.fit(X_train,Y_train)

        save_bin(lr,Path(self.config.model_path))

        y_pred=lr.predict(X_test)
        r2_scores=r2_score(Y_test,y_pred)
        mae_score=mean_squared_error(Y_test,y_pred)
        logger.info(f"accuracy score is {r2_scores}")
        logger.info(f"mean squared error is {mae_score}")
        return r2_scores,mae_score


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
        r2_scores,mae_score=self.evaluate(X_train,Y_train,X_test,Y_test)
        scores={"accuracy":r2_scores,"mae":mae_score}
        save_json(Path(self.config.metric_file_name),scores)
        