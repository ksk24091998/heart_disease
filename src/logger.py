import logging
import os
from datetime import datetime

base_path = os.path.abspath(os.path.join(os.getcwd(), ".", "."))  # Change ".." to move two levels up to the root directory
logs_path = os.path.join(base_path, "logs")

# Generate log file name based on timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Ensure that the "logs" directory exists
os.makedirs(logs_path, exist_ok=True)
print(logs_path)

# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)