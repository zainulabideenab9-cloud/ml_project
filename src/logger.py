import logging
import os
from datetime import datetime

# Define the log directory path
LOG_DIR = os.path.join(os.getcwd(), "logs")
# Create the directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = f"logs_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
if __name__ == "__main__":
    logging.info("Logger initialized.")