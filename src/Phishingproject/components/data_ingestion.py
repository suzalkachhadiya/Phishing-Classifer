import shutil
import os
from Phishingproject.constants import *
from Phishingproject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def upload_and_save_text_file(self):
            files_in_folder = os.listdir(SAVED_FILE_PATH)
            first_file = files_in_folder[4]
            print("first_file:",first_file)
            file_path = os.path.join(SAVED_FILE_PATH, first_file)
            # print(file_name)
            # print(f"Selected file: {file_path}")
                
                # Create the destination folder if it doesn't exist
            os.makedirs(self.config.destination_folder, exist_ok=True)
                
                # Define the destination path
            destination_path = os.path.join(self.config.destination_folder, first_file)
            # print("destination_path:",destination_path)
            
            # normalized_path = os.path.normpath(destination_path)

            # unix_style_path = normalized_path.replace(os.sep, '/')
            # print("unix_style_path:",unix_style_path)
            try:
                    # Copy the file to the destination folder
                    shutil.copy2(file_path, destination_path)
                    print(f"File saved to: {destination_path}")
                    
                    # # Read the content of the file
                    # with open(unix_style_path, 'r', encoding='utf-8') as file:
                    #     file_content = file.read()
                    
                    return #{file_name: file_content}
            except Exception as e:
                    print(f"Error: Unable to save or read {first_file}. {str(e)}")
                    return #{}
            else:
                print("No file selected")
                return #{}