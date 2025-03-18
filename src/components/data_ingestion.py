import pandas as pd
import os
import sys
import json

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
        except FileNotFoundError:
            print('Data file not found.')
            return None
        return df
    

if __name__ == "__main__":
    data_instance = Data()  # Create an instance of the Data class
    interim = data_instance.load_config(config_file="config.json")
    df = data_instance.data_read(interim)  # Call the method on the instance

    if df is not None:  # Ensure data exists
        print(df.shape)  # Display the shape of the dataframe
    else:
        print("No data to display.")
