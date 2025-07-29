### **Realtime Election Voting System**

This repository provides a complete implementation of a real-time election voting system developed using **Python**, **Kafka**, **Spark Streaming**, **Postgres**, and **Streamlit**. The entire setup is containerized with **Docker Compose**, making it easy to deploy all required services.


###  **System Overview**

* **System Architecture:**

![system_architecture](https://github.com/user-attachments/assets/1b1ddedd-5ae6-4b3d-8962-73493a901a2d)


* **System Flow:**
  
![system_flow](https://github.com/user-attachments/assets/bd381242-bfa7-44dd-9889-77d4e5317175)



###  **Key Components**

* **`main.py`** – Creates Postgres tables (`candidates`, `voters`, `votes`), sets up Kafka topics, copies the `votes` table to Kafka, and handles vote consumption/production for `voters_topic`.
* **`voting.py`** – Consumes voter data from `voters_topic`, generates voting events, and produces them to `votes_topic`.
* **`spark-streaming.py`** – Consumes votes from `votes_topic`, enriches them with Postgres data, aggregates results, and publishes the processed data to specific Kafka topics.
* **`streamlit-app.py`** – Fetches aggregated voting data from Kafka and Postgres, displaying it in real-time using Streamlit.



### **System Setup**

The repository includes a **Docker Compose file** to easily launch **Zookeeper**, **Kafka**, and **Postgres** in containers.



###  **Prerequisites**

* Python **3.9+**
* **Docker** and **Docker Compose** installed



###  **Steps to Get Started**

1. Clone this repository.
2. Navigate to the project root where the Docker Compose file is located.
3. Start services with:

   ```bash
   docker-compose up -d
   ```

   * Kafka → `localhost:9092`
   * Postgres → `localhost:5432`



###  **Configuration**

To change ports or Zookeeper/Kafka settings, edit the `docker-compose.yml` file as needed.



### **Running the Application**

Install dependencies:

```bash
pip install -r requirements.txt
```

#### 1️ Create Postgres tables and generate voter info:
```bash
python main.py
```

#### 2️ Consume voter data, generate votes, and publish to Kafka:

```bash
python voting.py
```

#### 3️ Process and aggregate votes with Spark Streaming:

```bash
python spark-streaming.py
```

#### 4 Launch the real-time dashboard:

```bash
streamlit run streamlit-app.py
```



###  **Screenshots**

* **Candidates and Parties:**
<img width="1113" height="225" alt="Screenshot 2025-07-29 at 10 05 23 AM" src="https://github.com/user-attachments/assets/84793cfd-40fe-4e34-b9cd-fe7b0b0aab08" />

* **Voters List:**
<img width="1133" height="465" alt="Screenshot 2025-07-29 at 10 06 36 AM" src="https://github.com/user-attachments/assets/ca450a8d-ee4e-433e-baa4-287ff269045f" />

* **Voting Process:**
<img width="1083" height="608" alt="Screenshot 2025-07-29 at 10 13 46 AM" src="https://github.com/user-attachments/assets/ed40013f-f1b0-4372-b717-c2cabdf95dc9" />

  
* **Dashboard View:**
  
<img width="679" height="449" alt="Screenshot 2025-07-29 at 10 11 16 AM" src="https://github.com/user-attachments/assets/84add8f3-8cad-432a-8313-69948553683c" />
