from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation

import sys
import os
sys.path.insert(0, os.path.abspath('.'))


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # data_ingestion=config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        ingestion_config = data_ingestion.ingestion_config
        train_path, test_path = data_ingestion.initiate_data_ingestion()
        


        # data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        # train_arr, test_arr, preprocessor_path =
        # data_transformation.initiate_data_transformation(train_path=ingestion_config.train_data_path,test_path=ingestion_config.test_data_path)

        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_path=ingestion_config.train_data_path,test_path=ingestion_config.test_data_path)

        logging.info("Pipe;ine Completed")
        
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)


