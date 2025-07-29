**Realtime Election Voting System**
This repository provides a complete implementation of a real-time election voting system developed using **Python**, **Kafka**, **Spark Streaming**, **Postgres**, and **Streamlit**. The entire setup is containerized with **Docker Compose**, making it easy to deploy all required services.


###  **System Overview**

* **System Architecture:**
* <img src="images/system_architecture.jpg" alt="System Architecture" width="500">


* **System Flow:** `system_flow.jpg`



###  **Key Components**

* **`main.py`** – Creates Postgres tables (`candidates`, `voters`, `votes`), sets up Kafka topics, copies the `votes` table to Kafka, and handles vote consumption/production for `voters_topic`.
* **`voting.py`** – Consumes voter data from `voters_topic`, generates voting events, and produces them to `votes_topic`.
* **`spark-streaming.py`** – Consumes votes from `votes_topic`, enriches them with Postgres data, aggregates results, and publishes the processed data to specific Kafka topics.
* **`streamlit-app.py`** – Fetches aggregated voting data from Kafka and Postgres, displaying it in real-time using Streamlit.

---

### **System Setup**

The repository includes a **Docker Compose file** to easily launch **Zookeeper**, **Kafka**, and **Postgres** in containers.

---

###  **Prerequisites**

* Python **3.9+**
* **Docker** and **Docker Compose** installed

---

###  **Steps to Get Started**

1. Clone this repository.
2. Navigate to the project root where the Docker Compose file is located.
3. Start services with:

   ```bash
   docker-compose up -d
   ```

   * Kafka → `localhost:9092`
   * Postgres → `localhost:5432`

---

###  **Configuration**

To change ports or Zookeeper/Kafka settings, edit the `docker-compose.yml` file as needed.

---

### **Running the Application**

Install dependencies:


pip install -r requirements.txt


#### 1️ Create Postgres tables and generate voter info:

python main.py


#### 2️ Consume voter data, generate votes, and publish to Kafka:


python voting.py


#### 3️ Process and aggregate votes with Spark Streaming:


python spark-streaming.py


#### 4 Launch the real-time dashboard:


streamlit run streamlit-app.py




### 📸 **Screenshots**

* **Candidates and Parties:** `candidates_and_party.png`
* **Voters List:** `voters.png`
* **Voting Process:** `voting.png`
* **Dashboard View:** `dashboard_image.png`
