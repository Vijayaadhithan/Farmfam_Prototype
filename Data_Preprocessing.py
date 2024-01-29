import pandas as pd
import glob
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to transform data
def transform_data(data, datetime_format='%Y-%m-%d'):
    # Print the original data
    logger.info("Original Data:\n%s", data)

    # Add an incremental ID column
    data.insert(0, 'ID', range(1, len(data) + 1))

    # Iterate through each column
    for column in data.columns:
        # Check for null values in the column and replace with 0
        data[column] = data[column].fillna(0)

        # Correct any errors (replace 'N/A' with 'Unknown')
        data[column] = data[column].replace('N/A', 'Unknown')

        # Exclude columns with datetime values from astype(float)
        if not pd.api.types.is_datetime64_any_dtype(data[column]):
            # Transform data types (try converting to float)
            try:
                data[column] = data[column].astype(float)
            except ValueError:
                pass  # Ignore if the conversion fails

            # Change datetime format if the column contains dates
            if pd.api.types.is_datetime64_any_dtype(data[column]):
                data[column] = pd.to_datetime(data[column], errors='coerce', format=datetime_format)

    # Remove duplicates
    data = data.drop_duplicates()

    # Print the transformed data
    logger.info("\nTransformed Data:\n%s", data)

    return data

# Function to read data from Excel file
def read_excel_file(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except FileNotFoundError:
        logger.error("File not found: %s", file_path)
        return None
    except Exception as e:
        logger.error("Error reading Excel file: %s", str(e))
        return None

# Function to save data to Excel file
def save_to_excel(data, output_file='transformed_data.xlsx'):
    try:
        data.to_excel(output_file, index=False)
        logger.info("Transformed data saved to %s", output_file)
    except Exception as e:
        logger.error("Error saving to Excel file: %s", str(e))

if __name__ == "__main__":
    # Find the Excel file in the current directory
    excel_files = glob.glob('*.xlsx')

    if not excel_files:
        logger.warning("No Excel file found in the current directory.")
    else:
        # Use the first matching Excel file
        excel_file = excel_files[0]

        # Read the data from the Excel file
        data = read_excel_file(excel_file)

        if data is not None:
            # Transform the data
            transformed_data = transform_data(data)

            # Save the transformed data to a new Excel file
            save_to_excel(transformed_data)
