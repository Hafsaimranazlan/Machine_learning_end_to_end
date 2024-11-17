from src.constant import *
from src.utils.common import read_yaml
from src.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig

class ConfigurationManager:
    def __init__(self,
                config_path=CONFIG_FILE_PATH,
                schema_path=SCHEMA_FILE_PATH,
                params_path=PARAMS_FILE_PATH):
        self.config=read_yaml(config_path)
        self.schema=read_yaml(schema_path)
        self.params=read_yaml(params_path)


    def data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion

        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            data_url=config.data_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
            )
        return data_ingestion_config
    

    def data_val_config(self)->DataValidationConfig:
        config=self.config.data_validation
        #schema=self.schema.COLUMNS

        data_val_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_path=config.unzip_data_path,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=self.schema.COLUMNS
        )
        return data_val_config 
    
    def data_transformation_config(self)->DataTransformationConfig:
        config=self.config.data_transformation
        data_transformation_config=DataTransformationConfig(
        root_dir=config.root_dir,
        data_path=config.data_path,
        pkl_path=config.pkl_path
        )

        return data_transformation_config
    

    def model_trainer_config(self):
        config=self.config.model_trainer
        schema=self.schema.TARGET_COLUMN
        params=self.params.ElasticNet

        model_trainer_config=ModelTrainerConfig(
            pkl_obj_path=config.pkl_obj_path,
            model_path=config.model_path,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            TARGET_COLUMN=schema.name

        )
        return model_trainer_config
    

