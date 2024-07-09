from Phishingproject.logging import logger
from Phishingproject.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from Phishingproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# from Phishingproject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from Phishingproject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
# from Phishingproject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f"===>>> {STAGE_NAME} started <<<===")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"===>>> stage {STAGE_NAME} completed <<<===\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e