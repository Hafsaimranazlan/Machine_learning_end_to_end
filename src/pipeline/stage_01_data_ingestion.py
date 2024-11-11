from src.configuration.config import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src import logger

STAGE_NAME="Data Ingestion Stage"

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
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started >>>>>>>>>>")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> completed {STAGE_NAME} >>>>>>>>>>")