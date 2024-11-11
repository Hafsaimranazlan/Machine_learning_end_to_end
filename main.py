from src import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"

if __name__=="__main__":
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started >>>>>>>>>>")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>> completed {STAGE_NAME} >>>>>>>>>>")
