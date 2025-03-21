import pandas as pd
from data_ingestion import Data
from sklearn.model_selection import train_test_split
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', '..')))
print(os.getcwd())
from heart_disease.src.logger import *
from heart_disease.src.exception import CustomException



class transformation:

    def trans(self):

        data_instance = Data()  # Create an instance of the Data class
        interim = data_instance.load_config(config_file="config.json")
        data_path = interim["data_path"]
        train = interim["train_data"]
        test = interim["test_data"]
        df = data_instance.data_read(interim)  # Call the method on the instance

        if df is not None:  # Ensure data exists
            print(df.shape)  # Display the shape of the dataframe
        else:
            print("No data to display.")

        train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
        logging.info("train test split of the data iss completed")
        train_set.to_csv(train,index=False,header=True)
        test_set.to_csv(test,index=False,header=True)

        return train_set,test_set,data_path