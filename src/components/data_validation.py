import pandas as pd
from src import logger
from src.configuration.config import ConfigurationManager
from src.entity.config_entity import DataValidationConfig


class Data_Validation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    def validate_all_columns(self)->bool:

        data=pd.read_csv(self.config.unzip_data_path)
        data.drop('quality',axis=1,inplace=True)
        all_columns=list(data.columns)
        schema_col=self.config.all_schema.keys()
        validation_status=None
        logger.info(f"all columns {all_columns} \n")
        logger.info(f"schema columns {schema_col}")

        for col in all_columns:
            if col not in schema_col:
                validation_status=False
                with open(self.config.STATUS_FILE,"w") as f:
                    f.write(f"Validation status : {validation_status}")

            else:
                validation_status=True
                with open(self.config.STATUS_FILE,"w") as f:
                    f.write(f"validation status : {validation_status}")
        return validation_status