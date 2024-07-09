from Phishingproject.logging import logger
from Phishingproject.config.configuration import ConfigurationManager
from Phishingproject.components.data_transformation import DataTransformation

STAGE_NAME="Data Validation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()


if __name__=="__main__":
    try:
        logger.info(f"===>>> stage {STAGE_NAME} started <<<===")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"===>>> stage {STAGE_NAME} completed <<<===\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e