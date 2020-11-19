import numpy as np
import pandas as pd
import joblib
import pickle
from sklearn.base import BaseEstimator, TransformerMixin

#######
# Get the model trained in the notebook
# `../nbs/1.0-asl-train_model.ipynb`
#######

model = joblib.load('models/forest_reg_2feat_300est_new.joblib')

#load pipeline
pipeline = joblib.load('models/box_office_pipeline.joblib')


def preprocess(data):
    """
    Returns the features entered by the user in the web form. 

    """


    feature_values = {
        'budget': 0,
        'popularity': 1,
        'runtime': 0,
        'has_collection': 0,
        'has_homepage': 0,
        'no_of_genres': 0,
        'original_language_is_english': 0,
        'no_of_production_companies': 0
    }

    # Parse the form inputs and return the defaults updated with values entered.

    for key in [k for k in data.keys() if k in feature_values.keys()]:
      feature_values[key] = data[key]
    
    for key in [k for k in data.keys() if k == "genres_checkbox"]:
      feature_values["no_of_genres"] = len(data[key])


    data_df = pd.DataFrame.from_records([feature_values])
    prepared_values = pipeline.transform(data_df)
    return prepared_values


#######
# Now we can predict with the trained model:
#######

def predict(data):
    """
    If debug, print various useful info to the terminal.
    """


    #Predict on the incoming data. 
    
    pred = model.predict(data.reshape(1, -1))

    return pred


def postprocess(prediction):
    """
    Apply postprocessing to the prediction. E.g. validate the output value, add
    additional information etc. 
    """

    # pred, uncertainty = prediction
    pred = prediction

    # Validate. As an example, if the output is an int, check that it is positive.
    try:
        int(pred[0]) > 0
    except:
        pass

    # Make strings
    pred = str(pred[0])

    # Return
    return_dict = {'pred': pred}

    return return_dict
