from Phishingproject.config.configuration import ConfigurationManager
from Phishingproject.components.prediction import PredictionPipeline

try:
    config = ConfigurationManager()
    prediction_config = config.get_prediction_config()
    prediction= PredictionPipeline(config=prediction_config)
    PW=prediction.predict("http://emgn.com/tv/schnauzer-passes-out-with-excitement-when-he-is-reunited-with-his-human-after-2-years/")
except Exception as e:
    raise e