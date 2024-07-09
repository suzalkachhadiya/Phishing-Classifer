from Phishingproject.constants import *
from Phishingproject.utils.common import create_directories, read_yaml_file
from Phishingproject.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml_file(config_filepath)
        self.params = read_yaml_file(params_filepath)
        self.schema = read_yaml_file(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
            destination_folder=config.destination_folder
        )

        return data_ingestion_config