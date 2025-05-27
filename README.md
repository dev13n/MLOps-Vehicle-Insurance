# 🚗 MLOps Project: Vehicle Insurance Pipeline

Welcome to the **Vehicle Insurance MLOps Project**, a robust end-to-end machine learning operations pipeline that covers everything from data ingestion to model deployment, cloud integration, and CI/CD automation. This project is designed to impress recruiters and showcase your expertise in real-world machine learning engineering practices using modern tools and services.

---

## 🛠️ Tech Stack

* **Languages**: Python 3.10
* **Cloud Services**: MongoDB Atlas, AWS S3, AWS EC2, AWS ECR, IAM
* **MLOps Tools**: Docker, GitHub Actions, Self-hosted Runners
* **CI/CD**: GitHub Actions, Docker
* **Web Framework**: Flask (with `app.py`)
* **Data Handling**: Pandas, PyMongo

---

## 🔧 Project Setup

### 1. Project Structure Initialization

```bash
python template.py
```

### 2. Package Configuration

Edit `setup.py` and `pyproject.toml` to define local package imports. More info in `crashcourse.txt`.

### 3. Virtual Environment

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
pip list  # Confirm installations
```

---

## 🗃️ MongoDB Integration

### 4. Setup MongoDB Atlas

* Create free M0 cluster
* Add user and set IP access to `0.0.0.0/0`
* Copy Python connection string

### 5. Push Dataset to MongoDB

* Folder: `notebook`
* File: `mongoDB_demo.ipynb`
* Use PyMongo to upload data
* Verify via MongoDB Atlas > Browse Collections

---

## 📋 Logging, Exceptions & EDA

### 6. Logger & Exception Handler

* Files: `logger.py`, `exception.py`
* Tested via `demo.py`

### 7. EDA & Feature Engineering

* Notebooks added in `notebooks/`

---

## 📥 Data Ingestion Component

### 8. Setup

* Define DB connection: `configuration/mongo_db_connections.py`
* Access and transform data: `data_access/proj1_data.py`
* Entities:

  * Config: `entity/config_entity.py`
  * Artifact: `entity/artifact_entity.py`
* Component: `components/data_ingestion.py`
* Run: `demo.py`

### 9. MongoDB URL Environment Setup

```bash
# Bash
export MONGODB_URL="mongodb+srv://<username>:<password>@..."
# PowerShell
$env:MONGODB_URL = "mongodb+srv://<username>:<password>@..."
```

Also add `artifact/` to `.gitignore`

---

## 📊 Data Validation & Transformation

### 10. Data Validation

* Schema: `config/schema.yaml`
* Utils: `utils/main_utils.py`
* Component: `components/data_validation.py`

### 11. Data Transformation

* Logic: `components/data_transformation.py`
* Estimator: `entity/estimator.py`

### 12. Model Training

* Trainer: `components/model_trainer.py`
* Use custom estimator from `entity/estimator.py`

---

## ☁️ AWS Integration

### 13. AWS Setup

* IAM user: `firstproj` with `AdministratorAccess`
* Access Keys: set as environment variables

```bash
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
```

### 14. S3 Bucket

* Region: `us-east-1`
* Bucket: `my-model-mlopsproj`
* Permissions: Disable block all public access

### 15. AWS Module Integration

* Constants in `constants/__init__.py`
* S3 Logic:

  * `src/aws_storage/`
  * `entity/s3_estimator.py`

---

## 🧠 Model Evaluation & Deployment

### 16. Evaluation & Pusher

* Evaluate against previous model
* Push best model to S3 bucket

### 17. Prediction Pipeline

* File: `app.py`
* Folders: `static/`, `templates/`

---

## 🔄 CI/CD: GitHub Actions + Docker + AWS

### 18. Docker

* Files: `Dockerfile`, `.dockerignore`

### 19. GitHub Actions

* Workflow: `.github/workflows/aws.yaml`
* Secrets:

  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * `AWS_DEFAULT_REGION`
  * `ECR_REPO`

### 20. AWS ECR

* Repo: `vehicleproj`
* Store Docker images

### 21. AWS EC2 + Self-Hosted Runner

* Instance: Ubuntu Server (T2 Medium)
* Install Docker and GitHub Runner
* Run with `./run.sh`

### 22. Final Deployment

* EC2 Inbound Rule: Open Port `5000`
* Access App: `http://<ec2-public-ip>:5000`
* Endpoint for training: `http://<ec2-ip>:5000/training`

---

## 📌 Project Workflow Summary

1. **Data Ingestion**  ⟶
2. **Data Validation**  ⟶
3. **Data Transformation**  ⟶
4. **Model Training**  ⟶
5. **Model Evaluation**  ⟶
6. **Model Deployment (S3 + EC2)**  ⟶
7. **CI/CD with GitHub + Docker + AWS**

---

## 🙋‍♂️ Let's Connect

If you liked the project or want to collaborate, feel free to reach out via GitHub or LinkedIn!

---

> **Note**: This project is optimized for demonstrating complete lifecycle management and DevOps for machine learning in a real-world insurance use case.
