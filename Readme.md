Code Solution Documentation
Introduction
The provided code solution is a microservice developed using FastAPI,Python SQLAlchemy, and Kafka. It synchronizes subscription statuses between two PostgreSQL databases, leveraging Kafka for message streaming and asynchronous processing. This documentation provides a detailed overview of the code solution, including its architecture, functionality, setup instructions, and an evaluation based on the specified criteria.

Architecture Overview
The microservice architecture consists of the following components:

FastAPI Endpoints: Exposes HTTP endpoints for CRUD operations on subscription statuses.
Database Operations: Utilizes SQLAlchemy ORM to interact with two PostgreSQL databases.
Kafka Integration: Consumes messages from a Kafka topic to update subscription statuses in Database 2.
Environment Configuration: Loads database and Kafka connection details from environment variables using python-dotenv.
Functionality
The microservice performs the following tasks:

Subscription Status Synchronization: Periodically checks Database 1 for subscription status updates and updates Database 2 accordingly, using email as the unique identifier.
CRUD Operations: Provides endpoints for creating, reading, updating, and deleting subscription statuses.
Error Handling: Implements robust error handling mechanisms to handle exceptions during database operations and Kafka message consumption.
Steps to Run and Installation Instructions
Step 1: Install Required Packages
Open a terminal or command prompt.
Navigate to the directory containing your Python code.
Run the following command to install the required Python packages:
pip install fastapi sqlalchemy kafka-python python-dotenv uvicorn
Step 2: Set Up Environment Variables
Create a .env file in the same directory as your Python code.
Open the .env file in a text editor.
Add the following environment variables to the .env file:
# Database 1
DB1_HOST=<database_1_host>
DB1_PORT=<database_1_port>
DB1_USER=<database_1_username>
DB1_PASSWORD=<database_1_password>
DB1_DATABASE=<database_1_name>

# Database 2
DB2_HOST=<database_2_host>
DB2_PORT=<database_2_port>
DB2_USER=<database_2_username>
DB2_PASSWORD=<database_2_password>
DB2_DATABASE=<database_2_name>

# Kafka Server and Topic
KAFKA_SERVER=<kafka_server>
KAFKA_TOPIC=<kafka_topic>

Replace <database_1_host>, <database_1_port>, <database_1_username>, <database_1_password>, <database_1_name>, <database_2_host>, <database_2_port>, <database_2_username>, <database_2_password>, <database_2_name>, <kafka_server>, and <kafka_topic> with the appropriate values for your two databases and Kafka server.

Step 3: Start Kafka Server
Download Apache Kafka from the official website and extract the files to a directory on your computer.
Open a new terminal or command prompt.
Navigate to the Kafka directory in the terminal.
Start the ZooKeeper server by running the following command:

bin/zookeeper-server-start.sh config/zookeeper.properties

Start the Kafka server by running the following command in the same terminal:
bin/kafka-server-start.sh config/server.properties

Certainly! Below is the updated documentation with steps to run the code solution and installation instructions:

Code Solution Documentation
Introduction
The provided code solution is a microservice developed using FastAPI, SQLAlchemy, and Kafka. It synchronizes subscription statuses between two PostgreSQL databases, leveraging Kafka for message streaming and asynchronous processing. This documentation provides a detailed overview of the code solution, including its architecture, functionality, setup instructions, and an evaluation based on the specified criteria.

Architecture Overview
The microservice architecture consists of the following components:

FastAPI Endpoints: Exposes HTTP endpoints for CRUD operations on subscription statuses.
Database Operations: Utilizes SQLAlchemy ORM to interact with two PostgreSQL databases.
Kafka Integration: Consumes messages from a Kafka topic to update subscription statuses in Database 2.
Environment Configuration: Loads database and Kafka connection details from environment variables using python-dotenv.
Functionality
The microservice performs the following tasks:

Subscription Status Synchronization: Periodically checks Database 1 for subscription status updates and updates Database 2 accordingly, using email as the unique identifier.
CRUD Operations: Provides endpoints for creating, reading, updating, and deleting subscription statuses.
Error Handling: Implements robust error handling mechanisms to handle exceptions during database operations and Kafka message consumption.
Steps to Run and Installation Instructions
Step 1: Install Required Packages
Open a terminal or command prompt.
Navigate to the directory containing your Python code.
Run the following command to install the required Python packages:
bash
Copy code
pip install fastapi sqlalchemy kafka-python python-dotenv uvicorn
Step 2: Set Up Environment Variables
Create a .env file in the same directory as your Python code.
Open the .env file in a text editor.
Add the following environment variables to the .env file:
plaintext
Copy code
# Database 1
DB1_HOST=<database_1_host>
DB1_PORT=<database_1_port>
DB1_USER=<database_1_username>
DB1_PASSWORD=<database_1_password>
DB1_DATABASE=<database_1_name>

# Database 2
DB2_HOST=<database_2_host>
DB2_PORT=<database_2_port>
DB2_USER=<database_2_username>
DB2_PASSWORD=<database_2_password>
DB2_DATABASE=<database_2_name>

# Kafka Server and Topic
KAFKA_SERVER=<kafka_server>
KAFKA_TOPIC=<kafka_topic>
Replace <database_1_host>, <database_1_port>, <database_1_username>, <database_1_password>, <database_1_name>, <database_2_host>, <database_2_port>, <database_2_username>, <database_2_password>, <database_2_name>, <kafka_server>, and <kafka_topic> with the appropriate values for your two databases and Kafka server.
Step 3: Start Kafka Server
Download Apache Kafka from the official website and extract the files to a directory on your computer.
Open a new terminal or command prompt.
Navigate to the Kafka directory in the terminal.
Start the ZooKeeper server by running the following command:
bash
Copy code
bin/zookeeper-server-start.sh config/zookeeper.properties
Start the Kafka server by running the following command in the same terminal:
bash
Copy code
bin/kafka-server-start.sh config/server.properties
Step 4: Run the FastAPI Application
Ensure that your PostgreSQL databases are running.
Open a new terminal or command prompt.
Navigate to the directory containing your Python code.
Run the FastAPI application using uvicorn. Execute the following command:
uvicorn main:app --reload


Certainly! Below is the updated documentation with steps to run the code solution and installation instructions:

Code Solution Documentation
Introduction
The provided code solution is a microservice developed using FastAPI, SQLAlchemy, and Kafka. It synchronizes subscription statuses between two PostgreSQL databases, leveraging Kafka for message streaming and asynchronous processing. This documentation provides a detailed overview of the code solution, including its architecture, functionality, setup instructions, and an evaluation based on the specified criteria.

Architecture Overview
The microservice architecture consists of the following components:

FastAPI Endpoints: Exposes HTTP endpoints for CRUD operations on subscription statuses.
Database Operations: Utilizes SQLAlchemy ORM to interact with two PostgreSQL databases.
Kafka Integration: Consumes messages from a Kafka topic to update subscription statuses in Database 2.
Environment Configuration: Loads database and Kafka connection details from environment variables using python-dotenv.
Functionality
The microservice performs the following tasks:

Subscription Status Synchronization: Periodically checks Database 1 for subscription status updates and updates Database 2 accordingly, using email as the unique identifier.
CRUD Operations: Provides endpoints for creating, reading, updating, and deleting subscription statuses.
Error Handling: Implements robust error handling mechanisms to handle exceptions during database operations and Kafka message consumption.
Steps to Run and Installation Instructions
Step 1: Install Required Packages
Open a terminal or command prompt.
Navigate to the directory containing your Python code.
Run the following command to install the required Python packages:
bash
Copy code
pip install fastapi sqlalchemy kafka-python python-dotenv uvicorn
Step 2: Set Up Environment Variables
Create a .env file in the same directory as your Python code.
Open the .env file in a text editor.
Add the following environment variables to the .env file:
plaintext
Copy code
# Database 1
DB1_HOST=<database_1_host>
DB1_PORT=<database_1_port>
DB1_USER=<database_1_username>
DB1_PASSWORD=<database_1_password>
DB1_DATABASE=<database_1_name>

# Database 2
DB2_HOST=<database_2_host>
DB2_PORT=<database_2_port>
DB2_USER=<database_2_username>
DB2_PASSWORD=<database_2_password>
DB2_DATABASE=<database_2_name>

# Kafka Server and Topic
KAFKA_SERVER=<kafka_server>
KAFKA_TOPIC=<kafka_topic>
Replace <database_1_host>, <database_1_port>, <database_1_username>, <database_1_password>, <database_1_name>, <database_2_host>, <database_2_port>, <database_2_username>, <database_2_password>, <database_2_name>, <kafka_server>, and <kafka_topic> with the appropriate values for your two databases and Kafka server.
Step 3: Start Kafka Server
Download Apache Kafka from the official website and extract the files to a directory on your computer.
Open a new terminal or command prompt.
Navigate to the Kafka directory in the terminal.
Start the ZooKeeper server by running the following command:
bash
Copy code
bin/zookeeper-server-start.sh config/zookeeper.properties
Start the Kafka server by running the following command in the same terminal:
bash
Copy code
bin/kafka-server-start.sh config/server.properties
Step 4: Run the FastAPI Application
Ensure that your PostgreSQL databases are running.
Open a new terminal or command prompt.
Navigate to the directory containing your Python code.
Run the FastAPI application using uvicorn. Execute the following command:
bash
Copy code
uvicorn main:app --reload
Step 5: Test the Application
Use an API testing tool like Postman or curl to send requests to the FastAPI endpoints (/subscription_status) to create, read, update, and delete subscription statuses.
Monitor the terminal where you ran the FastAPI application to see if there are any errors or messages related to Kafka message consumption.

Note:This code is completed 70 percent according to your requirements for approach 2 and 50 percent for approach 3 and approach 1 code has been done seperately to complete 2 and 3 approaches completely i will have to do some more modifications if you say this is enough to test my coding and problem solving skills then it's okay otherwise respond me back so i can complete this ahead of this thanks for production level.
