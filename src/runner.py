"""
Main application script for running the ML model service.

This script initializes the ModelService, loads the ML model, makes
a prediction based on predefined input parameters, and logs the output.
It demonstrates the typical workflow of using the ModelService in
a practical application context.
"""
from loguru import logger
from model.model_service import ModelService


@logger.catch
def main():
    """
    Run the application.

    Load the model,make a prediction based on provided data,
    and log the prediction
    """
    logger.info('running the application....')
    svc_model = ModelService()
    svc_model.load_model()

    feature_values = {
        'area': 85,
        'constraction_year': 2015,
        'bedrooms': 2,
        'garden': 20,
        'balcony_yes': 1,
        'parking_yes': 1,
        'furnished_yes': 0,
        'garage_yes': 0,
        'storage_yes': 1
    }
    pred = svc_model.predict(list(feature_values.values()))
    logger.info(f'Prediction= {pred}')


if __name__ == '__main__':
    main()
