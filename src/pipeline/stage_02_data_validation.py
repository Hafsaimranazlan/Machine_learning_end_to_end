from src.configuration.config import ConfigurationManager
from src.components.data_validation import Data_Validation
from src import logger

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        val=ConfigurationManager()
        data_val=val.data_val_config()
        val2=Data_Validation(data_val)
        val2.validate_all_columns()



if __name__ == "__main__":
    pass