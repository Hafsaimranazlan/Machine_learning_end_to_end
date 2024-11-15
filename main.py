from src import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_data_validation import DataValidationPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline



logger.info(f">>>>>>>>>> stage Data Ingestion started >>>>>>>>>>")
ditp=DataIngestionTrainingPipeline()
ditp.main()
logger.info(f">>>>>>>>>>>>>>>> Data Ingestion Stage Completed >>>>>>>>>>>>")

logger.info(f">>>>>>>>>>>>>>> Data Validation stage Started >>>>>>>>>>>>>>>>>>>")
dvp=DataValidationPipeline()
dvp.main()
logger.info(f">>>>>>>>>>>>>>>>> Data Validation Stage completed >>>>>>>>>>>>>>>>>")

logger.info(f">>>>>>>>>>>>>>>>> Data Transformation Stage Started >>>>>>>>>>>>>>>>>")
dttp=DataTransformationTrainingPipeline()
train_arr,test_arr=dttp.main()
logger.info(f"<<<<<<<<<<<<<<<<<< Data Transformation completed >>>>>>>>>>>>>>>>>")

