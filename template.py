# Import necessary modules
import os                              # Provides a way of using operating system-dependent functionality
from pathlib import Path               # Object-oriented filesystem paths

# Define the base project directory name
project_name = "src"

# Define a list of file paths to be created for the project structure
list_of_files = [

    # Component files for different ML pipeline stages
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",

    # Configuration-related files for MongoDB and AWS
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",

    # Files related to cloud storage functionality
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",

    # Files related to data access logic
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",

    # Constant values for configuration
    f"{project_name}/constants/__init__.py",

    # Entity classes for configuration and model artifacts
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",

    # Custom exception handling
    f"{project_name}/exception/__init__.py",

    # Logging utilities
    f"{project_name}/logger/__init__.py",

    # Pipeline logic for training and prediction
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",

    # General utility functions
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    # Root-level project files
    "app.py",                      # Main entry point for the application
    "requirements.txt",           # List of project dependencies
    "Dockerfile",                 # Docker image configuration
    ".dockerignore",              # Files/folders to ignore when building Docker images
    "demo.py",                    # A sample script to demonstrate functionality
    "setup.py",                   # Packaging script for the Python project
    "pyproject.toml",             # Modern Python build system configuration
    "config/model.yaml",          # Model configuration settings
    "config/schema.yaml",         # Schema definition for data validation
]

# Loop through each file path in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string path to a Path object for cross-platform compatibility
    filedir, filename = os.path.split(filepath)  # Split into directory and filename

    # Create the directory if it does not already exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # `exist_ok=True` prevents error if directory already exists

    # Create an empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Just create the file (empty)
    else:
        print(f"file is already present at: {filepath}")  # Inform user if file already exists and is non-empty
