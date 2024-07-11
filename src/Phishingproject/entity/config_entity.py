from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    destination_folder: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    data_path: Path
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    criterion: str
    max_depth: int
    n_estimators: int
    oob_score: bool
    target_column: int

@dataclass(frozen=True)
class ModelEvaluationConfig:
  root_dir: Path
  test_data_path: Path
  model_path: Path
  metric_file_name: Path
  all_params:dict
  target_column: str

@dataclass(frozen=True)
class PredictionConfig:
    model_path: Path