from src.constant import *
from src.utils.common import read_yaml
from src.entity.config_entity import DataIngestionConfig,DataValidationConfig

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
    

