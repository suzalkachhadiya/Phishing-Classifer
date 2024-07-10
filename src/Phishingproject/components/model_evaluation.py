import joblib
import pandas as pd

from pathlib import Path
from sklearn.metrics import classification_report

from Phishingproject.utils.common import save_txt_file
from Phishingproject.config.configuration import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]
        
        predicted_phishing= model.predict(test_x)

        report = classification_report(test_y, predicted_phishing)
        # print(report)
        
        # Saving report as local
        save_txt_file(file_path=Path(self.config.metric_file_name), report=report)