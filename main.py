from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataTransformationConfig
from networksecurity.components.data_validation import DataValidation,DataValidationConfig
from networksecurity.logging.logger import logging
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.exception.exception import NetworkSecurityException
import sys

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        dataingestion=DataIngestion(dataingestionconfig)
        logging.info("Initialized Data Ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        logging.info("Data initiation completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)
        data_transformation_config=DataTransformationConfig(trainingpipelineconfig)
        logging.info("Data Transformation Started")
        data_transformation=data_transformation=DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(data_transformation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)