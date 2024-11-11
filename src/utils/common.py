import yaml
import joblib
import pandas
import os
import json
from src import  logger
from box.exceptions import BoxValueError
from pathlib import Path
from ensure import ensure_annotations
from box import ConfigBox


@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file path : {path_to_yaml} loaded successfully:")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


def create_dir(path:Path,verbose=True):
    logger.info("start creating making directory")
    os.makedirs(path,exist_ok=True)
        
@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f)

    logger.info(f"json file save to path : {path}")


@ensure_annotations
def load_json(path:Path)->ConfigBox:
    with open(path,"r") as f:
        content=json.load(path)

    logger.info(f"json file loaded from : {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file save to : {path}")


@ensure_annotations
def load_bin(path:Path):
    data=joblib.dump(path)
    logger.info(f"binary file loaded from : {path}")
    return data

@ensure_annotations
def get_size(paths:Path) -> str:
    size_in_kb=round(os.path.getsize(paths)/1024)
    return f"~{size_in_kb} KB"
