import zipfile
import os
import pandas as pd

def extract_file_from_zip(zip_file_path: str, extract_to: str) -> None:
    """
    Extracts all files from a zip archive to the specified directory.

    Args:
        zip_file_path (str): The path to the zip file.
        extract_to (str): The directory where the files will be extracted.
    """
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def load_txt_from_zip(extracted_dir: str, filename: str) -> pd.DataFrame:
    """
    Loads a pipe-separated TXT file from the extracted directory into a pandas DataFrame.
    """
    file_path = os.path.join(extracted_dir, filename)
    return pd.read_csv(file_path, delimiter='|', low_memory=False)

def load_data(outer_zip_path: str, filename: str, extract_to: str = "../data/") -> pd.DataFrame:
    """
    Orchestrates the extraction and loading of data from a nested zip file.
    """
    os.makedirs(extract_to, exist_ok=True)
    extract_file_from_zip(outer_zip_path, extract_to)
    return load_txt_from_zip(extract_to, filename)

if __name__ == "__main__":
    zip_path="data/MachineLearningRating_v3.zip"
    output_file="MachineLearningRating_v3.txt"
    df = load_data(zip_path,output_file)
    df.to_csv("data/extracteddata/MachineLearningRating_v3.txt", sep='|', index=False)