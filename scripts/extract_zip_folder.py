import zipfile
import os

def extract_file_from_zip(zip_file_path: str, extract_to: str) -> None:
    """
    Extracts all files from a zip archive to the specified directory.

    Args:
        zip_file_path (str): The path to the zip file.
        extract_to (str): The directory where the files will be extracted.
    """
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

if __name__ == "__main__":
    # Define paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    zip_file_path = os.path.join(current_dir, '../data/MachineLearningRating_v3.zip')  # Update this to your actual ZIP file name
    extract_to = os.path.join(current_dir, '../data/')

    # Check if the ZIP file exists before attempting to extract
    if not os.path.exists(zip_file_path):
        print(f"Error: The file {zip_file_path} does not exist.")
    else:
        # Extract the ZIP file
        extract_file_from_zip(zip_file_path, extract_to)
        print(f'Extracted files from {zip_file_path} to {extract_to}')