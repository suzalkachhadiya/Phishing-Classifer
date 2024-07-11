import pandas as pd
import joblib
import whois

from Phishingproject.utils.common import *
from Phishingproject.config.configuration import PredictionConfig

class PredictionPipeline:
    def __init__(self,config:PredictionConfig):
        self.config = config

    def featureExtraction(self,url):
        features = []
        #Address bar based features (10)
        features.append(havingIP(url))
        features.append(haveAtSign(url))
        features.append(getLength(url))
        features.append(getDepth(url))
        features.append(redirection(url))
        features.append(httpDomain(url))
        features.append(tinyURL(url))
        features.append(prefixSuffix(url))
        #Domain based features (4)
        dns = 0
        try:
          domain_name = whois.whois(urlparse(url).netloc)
        except:
          dns = 1

        features.append(dns)
        features.append(is_potential_phishing(url))
        features.append(1 if dns == 1 else domainAge(domain_name))
        features.append(1 if dns == 1 else domainEnd(domain_name))

        # HTML & Javascript based features (4)
        try:
          response = requests.get(url)
        except:
          response = ""
        features.append(iframe(response))
        features.append(mouseOver(response))
        features.append(rightClick(response))
        features.append(forwarding(response))

        print(features)
        print(type(features))
        print(len(features))

        return features
    
    def predict(self,url):
        model=joblib.load(self.config.model_path)
        data=self.featureExtraction(url)
        # Get the feature names from the model
        if hasattr(model, 'feature_names_in_'):
          feature_names = model.feature_names_in_
        else:
        # If feature names are not available, create generic names
          feature_names = [f'feature_{i}' for i in range(len(data))]
        print(feature_names)
        # Create a pandas DataFrame with the correct feature names
        input_df = pd.DataFrame([data], columns=feature_names)
        pred=model.predict(input_df)
        print(pred)
        return pred