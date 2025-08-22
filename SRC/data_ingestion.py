import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import logging
import yaml

logger=logging.getLogger("data_ingestion")
logger.setLevel("DEBUG")

console_handler=logging.StreamHandler()
console_handler.setLevel("DEBUG")

file_handler=logging.FileHandler("data_ingestion.log")
file_handler.setLevel("DEBUG")

formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def load_data(data_url:str)->pd.DataFrame:
    try:
        logger.info("Loading data from %s",data_url)
        data=pd.read_csv(data_url)
        logger.info("Data loaded successfully")
        return data
    except Exception as e:
        logger.error("Error loading data: %s",e)
        raise e

def preprocess_data(df)->pd.DataFrame:
    try:
        logger.info("Preprocessing data")
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        logger.info("Data preprocessed successfully")
        return df
    except Exception as e:
        logger.error("Error preprocessing data: %s", e)
        raise e

def save_data(train_data:pd.DataFrame,test_data:pd.DataFrame,data_path:str)->None:
    try:
        logger.info("Saving data to %s",data_path)
        os.makedirs(data_path,exist_ok=True)
        train_data.to_csv(os.path.join(data_path, "train.csv"), index=False)
        test_data.to_csv(os.path.join(data_path, "test.csv"), index=False)
        logger.info("Data saved successfully")
    except Exception as e:
        logger.error("Error saving data: %s", e)
        raise e
def main():
    try:
        logger.info("Starting data ingestion")
        df=load_data(data_url="https://raw.githubusercontent.com/entbappy/Branching-tutorial/refs/heads/master/tweet_emotions.csv")
        final_df=preprocess_data(df)
        train_data,test_data=train_test_split(final_df,test_size=0.2,random_state=42)
        save_data(train_data,test_data,data_path='data/raw')
    except Exception as e:
        logger.error("Error in data ingestion: %s", e)
        raise e
if __name__=="__main__":
    main()  