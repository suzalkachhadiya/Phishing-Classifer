from Phishingproject.logging import logger
from Phishingproject.config.configuration import ConfigurationManager
from Phishingproject.components.model_evaluation import ModelEvaluation

STAGE_NAME="Data Validation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_model_evaluation_config()
        data_transformation = ModelEvaluation(config=data_transformation_config)
        data_transformation.save_results()


if __name__=="__main__":
    try:
        logger.info(f"===>>> stage {STAGE_NAME} started <<<===")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"===>>> stage {STAGE_NAME} completed <<<===\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e