from src import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_validation import DataValidationPipeline

STAGE_NAME="Data Ingestion Stage"


logger.info(f">>>>>>>>>> stage {STAGE_NAME} started >>>>>>>>>>")
obj=DataIngestionTrainingPipeline()
obj.main()
logger.info(f">>>>>>>>>>> completed {STAGE_NAME} >>>>>>>>>>")

logger.info(f"_____________________________________________")
logger.info(f"_____________________________________________")

logger.info(f">>>>>>>>>> Data Validation Started >>>>>>>>>>>>>>>")
obj2=DataValidationPipeline()
obj2.main()
logger.info(f">>>>>>>>>>>> Data Validation Completed >>>>>>>>>>>>")