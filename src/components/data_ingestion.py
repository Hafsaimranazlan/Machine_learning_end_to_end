import os
from urllib import request
import zipfile
from src import logger
from src.entity.config_entity import DataIngestionConfig
from src.configuration.config import ConfigurationManager

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header=request.urlretrieve(self.config.data_url,self.config.local_data_file)
            logger.info(f"{filename} with following info \n {header}")

    def data_extract(self):
        unzip_path=self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file,"r") as f:
            f.extractall(unzip_path)


                        
