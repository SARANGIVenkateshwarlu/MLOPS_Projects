

# Import pandas for reading and manipulating tabular data
import pandas as pd

# Import pickle to load the trained model from disk
import pickle

# Import accuracy_score to evaluate classification performance
from sklearn.metrics import accuracy_score

# Import yaml to read configuration values from params.yaml
import yaml

# Import os to manage environment variables
import os

# Import mlflow to log metrics to the MLflow tracking server
import mlflow


# ------------------------------------------------------------
# Configure MLflow to use DAGsHub tracking server
# ------------------------------------------------------------

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/venky.sarangi/machinelearningpipeline.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "venky.sarangi"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "ba9970ca7ac66e26448188f34b4f6412472510a3"


# ------------------------------------------------------------
# Load evaluation parameters from params.yaml
# ------------------------------------------------------------

params = yaml.safe_load(open("params.yaml"))["train"]


# ------------------------------------------------------------
# Model evaluation function
# ------------------------------------------------------------

def evaluate(data_path, model_path):
    # Load the dataset
    data = pd.read_csv(data_path)
    
    # Split features and target
    X = data.drop(columns=["Outcome"])
    y = data["Outcome"]

    # Set MLflow tracking URI (matches DAGsHub repo)
    mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])

    # Load trained model
    model = pickle.load(open(model_path, "rb"))

    # Start MLflow run
    with mlflow.start_run():
        # Generate predictions
        predictions = model.predict(X)
        
        # Calculate accuracy
        accuracy = accuracy_score(y, predictions)

        # Log accuracy to MLflow
        mlflow.log_metric("accuracy", accuracy)

        # Print accuracy
        print(f"Model accuracy: {accuracy}")


# ------------------------------------------------------------
# Script entry point
# ------------------------------------------------------------

if __name__ == "__main__":
    evaluate(params["data"], params["model"])