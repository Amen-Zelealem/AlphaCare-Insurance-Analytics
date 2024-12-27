# Task 2: Data Version Control (DVC)

This branch implements **Data Version Control (DVC)** to manage dataset versions effectively within the project. Below are the steps and commands used to complete the task.

---

## Objectives

1. Install and configure DVC in the project.
2. Set up local remote storage for DVC.
3. Track datasets with DVC and commit changes to Git.
4. Push datasets to local remote storage.
5. Create and manage different versions of datasets.

---

## Steps Summary

### 1. **Setup**
- Merged necessary branches from `task-1` into the `main` branch using a Pull Request (PR).
- Created a new branch named `task-2`:
  ```bash
  git checkout -b task-2
  git push origin task-2
- Installed and initialized DVC:
  ```bash
  pip install dvc
  dvc init
  git add .dvc .gitignore
  git commit -m "Initialize DVC"

### 2. **Configure Remote Storage**
 - Created a local storage directory and configured it as the default DVC remote:
  ```bash
  mkdir /data/localstorage
  dvc remote add -d localstorage /data/localstorage
  git add .dvc/config
  git commit -m "Configure local remote storage"

### 3. **Track and Push Data**
- Tracked datasets using DVC:
  ```bash
  dvc add data/cleaned_data.csv
  git add data/cleaned_data.csv.dvc
  git commit -m "Track cleaned_data.csv with DVC"
- Pushed data to the remote:
  ```bash
  dvc push

### 4. **Versioning**  
- Updated the dataset, re-tracked it with DVC, and pushed the changes:
  ```bash
  dvc add data/cleaned_data.csv
  git add data/cleaned_data.csv.dvc
  git commit -m "Update cleaned_data.csv with new version"
  dvc push

**Key Points**

+ DVC simplifies version control for large datasets without bloating the Git repository.
+ Local remote storage ensures data backup and easy retrieval.

### **Commands Summary**
  ```bash
  pip install dvc
  dvc init
  dvc remote add -d localstorage /data/localstorage
  dvc add data/cleaned_data.csv
  dvc push
  git commit -m "Track or update data with DVC"
  ```
**Author: Amen Zelealem**
**Date: Friday, Dec-27-2024 G.C.**