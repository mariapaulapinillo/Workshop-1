import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def extract_data(file_path="C:\\Users\LENOVO\Downloads\candidates.csv"):
    try:
        df = pd.read_csv(file_path, sep=";")
        logger.info(f'Data extracted successfully. Shape: {df.shape}')
        return df
    except Exception as e:
        logger.error(f'Error extracting data {e}')
        raise


if __name__ == "__main__":
    df = extract_data()
    print(df.head()) 