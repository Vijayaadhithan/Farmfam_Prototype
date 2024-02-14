import pandas as pd
import mysql.connector
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Read the transformed data
transformed_data = pd.read_excel('transformed_data.xlsx')

# Convert datetime columns to string representation
for column in transformed_data.columns:
    if pd.api.types.is_datetime64_any_dtype(transformed_data[column]):
        transformed_data[column] = transformed_data[column].dt.strftime('%Y-%m-%d %H:%M:%S')

# Database connection parameters
db_config = {
    'host': '127.0.0.1',
    'database': 'CI_CD',
    'user': 'root',
    'password': 'Vijay2799#',
}

# Create a connection using the 'with' statement
try:
    with mysql.connector.connect(**db_config) as conn:
        with conn.cursor(buffered=True) as cursor:
            # Mapping pandas data types to MySQL data types
            mysql_data_type_mapping = {
                'int64': 'INT',
                'float64': 'FLOAT',
                'object': 'VARCHAR(255)',  
                'datetime64[ns]': 'DATETIME',
                # Add more data types as needed
            }
            # Loop through each sheet
            for sheet_name, sheet_data in sheets.items():
                # Convert datetime columns
                for column in sheet_data.columns:
                    if pd.api.types.is_datetime64_any_dtype(sheet_data[column]):
                        sheet_data[column] = sheet_data[column].dt.strftime('%Y-%m-%d %H:%M:%S')


            # Extract column names and their data types from the DataFrame
            column_definitions = ', '.join([f'{column} {mysql_data_type_mapping[str(transformed_data[column].dtype)]}' for column in transformed_data.columns])

            # Create the table if it doesn't exist
            table_name = 'mytable'
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {column_definitions},
                PRIMARY KEY (`ID`)
            );
            """
            cursor.execute(create_table_query)
            logging.info(f"Table '{table_name}' created or already exists.")

            # Write the transformed data to the database using prepared statements
            transformed_data_columns = ', '.join(transformed_data.columns)
            placeholders = ', '.join(['%s' for _ in range(len(transformed_data.columns))])

            for _, row in transformed_data.iterrows():
                # Check if the ID already exists in the table
                check_id_query = f"SELECT * FROM {table_name} WHERE `ID` = %s"
                cursor.execute(check_id_query, (row['ID'],))
                existing_row = cursor.fetchone()

                if existing_row:
                    # Update existing row based on the ID
                    update_query = f"UPDATE {table_name} SET {', '.join([f'{col} = %s' for col in transformed_data.columns])} WHERE `ID` = %s"
                    cursor.execute(update_query, tuple(row) + (row['ID'],))
                    logging.info(f"Row with ID '{row['ID']}' updated.")
                else:
                    # Insert new row if ID doesn't exist
                    insert_query = f"INSERT INTO {table_name} ({transformed_data_columns}) VALUES ({placeholders})"
                    cursor.execute(insert_query, tuple(row))
                    logging.info(f"Row with ID '{row['ID']}' inserted.")

            # Commit the changes
            conn.commit()
            logging.info(f"Data inserted or updated in table '{table_name}' successfully.")

except mysql.connector.Error as err:
    logging.error(f"MySQL Error: {err}")
