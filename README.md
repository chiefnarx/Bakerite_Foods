# ☁️ Bakerite Foods Data Pipeline  

Bakerite Foods is a data engineering project designed to orchestrate and automate data workflows for a food distribution company. Using **Apache Airflow** on WSL, the pipeline extracts, transforms, and loads (ETL) raw data into structured tables within **Azure cloud storage and services**. The end-to-end system ensures reliability, scalability, and automation of data operations.  

---

## 📌 Project Overview  

This project simulates a modern cloud-based data pipeline, covering:  

- ✅ Extraction of raw business data  
- ✅ Transformation and cleaning with Python  
- ✅ Orchestration of tasks using Airflow DAGs  
- ✅ Loading structured data into Azure services for analysis  

---

## ⚙️ Technologies Used  

- ⏺ **Python** — data transformation and scripting  
- ⏺ **Apache Airflow** — workflow orchestration with DAGs  
- ⏺ **Azure (Blob Storage, SQL Database, etc.)** — cloud storage and database layer  
- ⏺ **WSL (Ubuntu)** — Linux environment for local development and Airflow setup  

---

## 🔄 Full Workflow  

### 1. Data Extraction  
- Ingest raw transactional/operational data into the pipeline.  
- Source files are staged in **Azure Blob Storage**.  

### 2. Data Transformation  
- Python scripts clean and normalize the dataset.  
- Steps include handling nulls, formatting date columns, and restructuring tables for analytics.  

### 3. Workflow Orchestration with Airflow  
- Defined a **DAG (Directed Acyclic Graph)** to automate ETL steps.  
- Tasks include:  
  - Extract → Transform → Load sequence  
  - Dependencies defined so downstream tasks wait for upstream success  
- Airflow ensures retries, logging, and scheduling for recurring runs.  

### 4. Data Loading into Azure  
- Cleaned and transformed tables are loaded into **Azure SQL Database** (or another Azure storage service).  
- Schema supports queries for:  
  - Customer orders  
  - Product and sales insights  
  - Operational tracking  

---

## 📄 Results & Final Verification  

- ✅ Automated data pipeline running via Airflow  
- ✅ Cleaned and structured dataset stored in Azure  
- ✅ Cloud-hosted database ready for business insights  
- ✅ Reusable ETL DAGs for scalability and reliability  

---

## 📝 Notes  

- ⏺ Airflow DAGs provide task dependency management, retries, and scheduling  
- ⏺ WSL was used to mimic a Linux production-like setup on Windows  
- ⏺ Modular Python scripts make transformations reusable  
- ⏺ Azure cloud services provide scalability for real-world extension  
