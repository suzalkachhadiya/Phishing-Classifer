import streamlit as st

from Phishingproject.config.configuration import ConfigurationManager
from Phishingproject.components.prediction import PredictionPipeline

st.header("Phishing Predictor", divider="rainbow")
user_input = st.text_input("Enter URL Here:",placeholder="Type Here")
# st.write(user_input)

if user_input: 
    try:
        config = ConfigurationManager()
        prediction_config = config.get_prediction_config()
        prediction= PredictionPipeline(config=prediction_config)
        print(f"type:{type(user_input)}")
        PW=int((prediction.predict(user_input))[0])
        print(f"prediction {PW}")
    except Exception as e:
        raise e
    
    if PW == 1:
        st.error(f":red[Danger]! website asked to visit by you can be Phishing.", icon='⚠️')
    else:
        st.success(f"website asked to visit by you is safe.", icon="✅")
        st.write(f"You can visit: {user_input}")