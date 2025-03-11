# import logging
# import os
# from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime(
#     "%m_%d_%Y_%H_%M_%S"
# )}.log"

# log_path = os.path.join(os.getcwd(),"logs")

# os.makedirs(log_path,exist_ok=True)

# Log_FilePath = os.path.join(log_path,LOG_FILE)

# logging.basicConfig(level=logging.INFO,
#         filename=Log_FilePath,
#         format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
#         )
# import logging 
# import os
# from datetime import datetime

# # Fix the quotes for strftime
# LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# # Create a directory for logs
# log_path = os.path.join(os.getcwd(), "logs")
# os.makedirs(log_path, exist_ok=True)

# # Full path to the log file
# log_file_path = os.path.join(log_path, LOG_FILE)

# # Configure logging
# logging.basicConfig(
#     level= logging.INFO,
#     filename=log_file_path,
#     format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     force=True
# )

# logging = py_logging.getLogger(__name__)
# src/mcqgenerator/logger.py

import logging as py_logging
import os
from datetime import datetime

# Generate a timestamped log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a directory for logs
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

# Full path to the log file
log_file_path = os.path.join(log_path, LOG_FILE)

# Configure the built-in logging under the alias "py_logging"
py_logging.basicConfig(
    level=py_logging.INFO,
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    force=True  # Remove or adjust if using Python < 3.8
)

# Create a logger instance named 'logger'
logger = py_logging.getLogger(__name__)

# Optional test log
logger.info("Logger has been set up in logger.py!")
