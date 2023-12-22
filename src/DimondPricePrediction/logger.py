import logging
import os
from datetime import datetime

log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs") # getcwd -> Get current working dir
os.makedirs(log_path, exist_ok=True)
log_file_path = os.path.join(log_path,log_file)

logging.basicConfig(level=logging.INFO, 
                    filename=log_file_path,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")

if __name__ == '__main__':
    logging.info("Test")