import logging
import sys
import os
# Define the logging format
logging_format = "[%(asctime)s:%(levelname)s:%(module)s:%(message)s]"

# Set up log directory and file path
log_dir = "log"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)  # Create log directory 

# Configure logging with file and console handlers
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=logging_format,  # Use the defined logging format

    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout)  # Log to the console
    ]
)

# Create a logger object with the name "PoetryGenerationLogger"
logger = logging.getLogger("PoetryGenerationLogger")