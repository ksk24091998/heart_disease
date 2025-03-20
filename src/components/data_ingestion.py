import pandas as pd
import os
import sys
import json
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', '..')))
print(os.getcwd())
from heart_disease.src.logger import *
from heart_disease.src.exception import CustomException

class Data:  # Use lowercase 'class' instead of 'Class'
    def load_config(self,config_file):
        with open(config_file, "r") as file:
            config = json.load(file)
            
            
        return config

    def data_read(self,config):
        # Access the variables
        data_path = config["data_path"]
        print(data_path)
        try:
            file_path = os.path.join(data_path, 'heart.csv')  # Correctly join paths

            df = pd.read_csv(file_path)
            logging.info('Read the dataset as dataframe')
        except FileNotFoundError:
            print('Data file not found.')
            logging.info('Data file not found')
            return None
        return df
    

