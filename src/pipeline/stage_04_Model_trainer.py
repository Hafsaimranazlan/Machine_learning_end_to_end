from src.configuration.config import ConfigurationManager
from src.components.model_trainer import ModelTrainer
from src import logger

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self,train_arr,test_arr):
        obj3=ConfigurationManager()
        trainer_config=obj3.model_trainer_config()
        obj4=ModelTrainer(trainer_config)
        obj4.train_model(train_arr,test_arr)


if __name__=="__main__":
    pass