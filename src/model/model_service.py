"""
This module provides functionality for managing ML model.

It contain ModelService class. which handles loading and using
a pre-trained ML model. the class offers methods to load model
from a file, building it if it doesn't exist, and make prediction
using the loaded model.
"""

import pickle as pk
from pathlib import Path

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelService():
    """
    A service class for managing the ML model.

    This class provide functionality to load ML model from
    a specified path, build it if it doesn't exist, and make
    prediction using the loaded model.

    Attribute:
        model: Ml model managing by this service, initially set to None

    Methods:
        __init__: Constructor that initialize the ModelService
        load_model: load the model from file or built it if doesn't exist
        predict: Make prediction using the loaded model
    """
    def __init__(self):
        self.model = None

    def load_model(self):
        """load the model from a specific path, or build if if not exist """
        logger.info(
            f'checking the existences of model config file at '
            f'{model_settings.model_path}/{model_settings.model_name}'
        )

        model_path = Path(
            f'{model_settings.model_path}/{model_settings.model_name}')

        if not model_path.exists():
            logger.info(
                f'model at {model_path} was not found -> '
                f'build {model_settings.model_name}')
            build_model()

        logger.info(
            f'model {model_settings.model_name} exist ->'
            f'loading model configuration file',
        )

        with open(model_path, 'rb') as model_file:
            self.model = pk.load(model_file)

    def predict(self, input_parameters: list) -> list:
        """
        Make a prediction using the load model.

        Take input parameters and passed it to model. which
        was loaded using a pickle file.

        Args:
            input_parameters (list): The input data making prediction

        Return:
            list: The parameters result from the model
        """
        logger.info('make prediction')
        return self.model.predict([input_parameters])
