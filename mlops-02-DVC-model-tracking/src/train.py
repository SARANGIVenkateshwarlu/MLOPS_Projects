# Import pandas for data loading and manipulation
import pandas as pd

# Import RandomForestClassifier for building the ML model
from sklearn.ensemble import RandomForestClassifier

# Import pickle to serialize (save) the trained model to disk
import pickle

# Import yaml to read configuration values from params.yaml
import yaml

# Import evaluation metrics to assess model performance
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Import MLflow utility to infer input/output schema for the model
from mlflow.models import infer_signature

# Import os for environment variables and directory handling
import os

# Import utilities for data splitting and hyperparameter tuning
from sklearn.model_selection import train_test_split, GridSearchCV

# Import urlparse to inspect the MLflow tracking URI type
from urllib.parse import urlparse

# Import MLflow for experiment tracking and model logging
import mlflow


# ------------------------------------------------------------
# Configure MLflow tracking to use DAGsHub
# ------------------------------------------------------------

# Set the MLflow tracking server URL (DAGsHub MLflow endpoint)
os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/venky.sarangi/machinelearningpipeline.mlflow"

# Set the DAGsHub username for authentication
os.environ['MLFLOW_TRACKING_USERNAME'] = "venky.sarangi"

# Set the DAGsHub access token (used as password for MLflow auth)
os.environ["MLFLOW_TRACKING_PASSWORD"] = "ba9970ca7ac66e26448188f34b4f6412472510a3"


# ------------------------------------------------------------
# Hyperparameter tuning function
# ------------------------------------------------------------

def hyperparameter_tuning(X_train, y_train, param_grid):
    # Initialize a Random Forest classifier with default settings
    rf = RandomForestClassifier()
    
    # Set up GridSearchCV to search over the hyperparameter grid
    # cv=3 -> 3-fold cross-validation
    # n_jobs=-1 -> use all available CPU cores
    # verbose=2 -> print detailed progress logs
    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=3,
        n_jobs=-1,
        verbose=2
    )
    
    # Fit GridSearchCV on the training data
    grid_search.fit(X_train, y_train)
    
    # Return the fitted GridSearchCV object
    return grid_search


# ------------------------------------------------------------
# Load training parameters from params.yaml
# ------------------------------------------------------------

# Read params.yaml and extract the "train" section
params = yaml.safe_load(open("params.yaml"))["train"]


# ------------------------------------------------------------
# Model training function
# ------------------------------------------------------------

def train(data_path, model_path, random_state, n_estimators, max_depth):
    # Load the dataset from the provided CSV file path
    data = pd.read_csv(data_path)
    
    # Separate features (X) by dropping the target column
    X = data.drop(columns=["Outcome"])
    
    # Extract the target variable (y)
    y = data["Outcome"]

    # Explicitly set the MLflow tracking URI
    mlflow.set_tracking_uri("https://dagshub.com/venky.sarangi/machinelearningpipeline.mlflow")

    # --------------------------------------------------------
    # Start an MLflow experiment run
    # --------------------------------------------------------
    with mlflow.start_run():
        
        # Split the dataset into training and testing sets (80/20 split)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.20
        )
        
        # Infer the model input/output signature for MLflow
        signature = infer_signature(X_train, y_train)

        # ----------------------------------------------------
        # Define hyperparameter search space
        # ----------------------------------------------------
        param_grid = {
            "n_estimators": [100, 200],
            "max_depth": [5, 10, None],
            "min_samples_split": [2, 5],
            "min_samples_leaf": [1, 2]
        }

        # Perform hyperparameter tuning using GridSearchCV
        grid_search = hyperparameter_tuning(X_train, y_train, param_grid)

        # Retrieve the best-performing model from GridSearchCV
        best_model = grid_search.best_estimator_

        # ----------------------------------------------------
        # Model evaluation
        # ----------------------------------------------------

        # Generate predictions on the test set
        y_pred = best_model.predict(X_test)
        
        # Calculate accuracy score
        accuracy = accuracy_score(y_test, y_pred)
        
        # Print accuracy to console
        print(f"Accuracy: {accuracy}")

        # ----------------------------------------------------
        # Log metrics and parameters to MLflow
        # ----------------------------------------------------

        # Log accuracy metric
        mlflow.log_metric("accuracy", accuracy)
        
        # Log best hyperparameters found during tuning
        mlflow.log_param("best_n_estimators", grid_search.best_params_["n_estimators"])
        mlflow.log_param("best_max_depth", grid_search.best_params_["max_depth"])
        mlflow.log_param("best_min_samples_split", grid_search.best_params_["min_samples_split"])
        mlflow.log_param("best_min_samples_leaf", grid_search.best_params_["min_samples_leaf"])

        # ----------------------------------------------------
        # Log evaluation artifacts
        # ----------------------------------------------------

        # Generate confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        
        # Generate classification report
        cr = classification_report(y_test, y_pred)

        # Log confusion matrix as a text artifact
        mlflow.log_text(str(cm), "confusion_matrix.txt")
        
        # Log classification report as a text artifact
        mlflow.log_text(cr, "classification_report.txt")

        # ----------------------------------------------------
        # Log model to MLflow
        # ----------------------------------------------------

        # Determine the type of MLflow tracking backend (file vs remote)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # If using a remote tracking server, register the model
        if tracking_url_type_store != "file":
            mlflow.sklearn.log_model(
                best_model,
                "model",
                registered_model_name="Best Model"
            )
        else:
            # Otherwise, log the model locally with signature
            mlflow.sklearn.log_model(
                best_model,
                "model",
                signature=signature
            )

        # ----------------------------------------------------
        # Save model locally using pickle
        # ----------------------------------------------------

        # Create the output directory if it does not exist
        os.makedirs(os.path.dirname(model_path), exist_ok=True)

        # Save the trained model to disk
        pickle.dump(best_model, open(model_path, "wb"))

        # Print confirmation message
        print(f"Model saved to {model_path}")


# ------------------------------------------------------------
# Script entry point
# ------------------------------------------------------------

# Ensure the training function runs only when executed directly
if __name__ == "__main__":
    train(
        params["data"],
        params["model"],
        params["random_state"],
        params["n_estimators"],
        params["max_depth"]
    )