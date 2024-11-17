from pathlib import Path
from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    root_dir:Path
    data_url:str
    local_data_file:Path
    unzip_dir:Path


@dataclass
class DataValidationConfig:
    root_dir:Path
    unzip_data_path:Path
    STATUS_FILE:bool
    all_schema:dict


@dataclass
class DataTransformationConfig:
    root_dir:Path
    data_path:Path
    pkl_path:Path


@dataclass
class ModelTrainerConfig:
    pkl_obj_path:Path
    model_path:Path
    alpha:float
    l1_ratio:float
    TARGET_COLUMN:str