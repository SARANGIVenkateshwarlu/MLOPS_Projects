# 🚀  Project -1 : END‑TO‑END LOGISTIC REGRESSION WITH MLFLOW TRACKING MODEL LIFECYCLE MANAGEMENT 
---

<p align="center"> 
   <strong> Project Workflow </strong> 
</p> 
<p align="center"> 
  <img src="assert/MLOPS_P1.png" alt="Workflow Diagram" width="600"> 
</p> 


---

## 🧠 Project Overview

This project demonstrates my ability to build and manage a production‑ready machine learning pipeline using Logistic Regression and MLflow, following real‑world MLOps best practices. The focus is not just on model training, but on experiment tracking, model validation, versioning, and reproducible deployment workflows key skills expected from a Machine Learning or MLOps Engineer.

The project begins by establishing a clean and reproducible Python development environment, ensuring consistent experimentation and dependency management. Using the Iris dataset, I train and evaluate multiple classification models, systematically comparing their performance using standardized evaluation metrics.

A central component of this project is MLflow Experiment Tracking. All model parameters, metrics, and artifacts are logged to MLflow, enabling transparent comparison between different model configurations. This allows for data‑driven model selection rather than ad‑hoc experimentation.

Before deployment, each trained model undergoes validation through MLflow inferencing, ensuring reliability and correctness. Models are then serialized and reloaded using MLflow’s PyFunc (mlflow.pyfunc) interface, demonstrating how trained models can be reused as generic Python functions for inference in downstream applications.

The project also showcases enterprise grade model lifecycle management by registering models in the MLflow Model Registry. Each model is versioned, tagged, and assigned aliases (such as Staging or Production), enabling controlled promotion across environments. Inference is performed directly from the Model Registry using model URIs, validating real‑world deployment scenarios where models are accessed dynamically rather than from local files.

## Project Highlights 

- Python Build end‑to‑end ML pipelines
- Track and compare experiments systematically
- Validate models before deployment
- Manage model versions and metadata
- Perform inference from a centralized model registry

## Skills Demonstrated: 

- Python & Scikit‑Learn 
- Logistic Regression (Classification)
- MLflow Experiment Tracking
- Model Artifact Logging & Inferencing
- MLflow PyFunc Models
- Model Registry, Versioning, Tags & Aliases
- Reproducible & Deployment‑Ready ML Pipelines
---

## 🛠️ Technologies Used
- Python - Scikit-learn - Pandas - NumPy - MLflow - VS Code - Virtual Environment (`venv`)

---
<p align="center"> 
   <strong> Experiment Tracking </strong> 
</p> 
<p align="center"> 
  <img src="assert/MLFLow_1.png" alt="Workflow Diagram" width="600"> 
</p> 



