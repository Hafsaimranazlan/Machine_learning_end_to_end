from src.configuration.config import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        obj=ConfigurationManager()
        data_config=obj.data_ingestion_config()
        obj2=DataIngestion(data_config)
        obj2.download_file()
        obj2.data_extract()


if __name__=="__main__":
    pass


