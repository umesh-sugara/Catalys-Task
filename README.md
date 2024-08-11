# Catalys-Task

## Overview

This project fetches e-commerce data from a Google Sheet, stores it temporarily in Redis, preprocesses it, and then stores it in an SQLite database.

![image](https://github.com/user-attachments/assets/e46a9588-a529-444f-8822-c3e85839831b)


## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone git@github.com:umesh-sugara/Catalys-Task.git
   
2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

3. **Configure Google Sheets**

    - Access the E-Commerce data at : 
       - https://docs.google.com/spreadsheets/d/1oBPHPO2crVNvIwS103scL0Fni6-LvMwXNUfyGw4lkNA/edit?gid=1097888433#gid=1097888433.
    - Place keys.json (Google Sheets credentials) in the project directory.
    - Share the Google Sheet with the service account specified in keys.json.

4. **Configure Redis**
   
     - Update Redis connection details in app.py (host, port, and password).

5. **Prepare SQLite Database**
   
    - Ensure data.db exists in the project directory. If not, create it with the following command:
      
      -  ```bash
         sqlite3 data.db

    - Create the apiDatabase table with the following SQL command:
        -  ```bash
           CREATE TABLE apiDatabase (
            index INTEGER,
            OrderID TEXT,
            Date TEXT,
            Status TEXT,
            Fulfilment TEXT,
            SalesChannel TEXT,
            ship_service_level TEXT,
            Style TEXT,
            SKU TEXT,
            Category TEXT,
            Size TEXT,
            ASIN TEXT,
            CourierStatus TEXT,
            Qty INTEGER,
            currency TEXT,
            Amount REAL,
            ship_city TEXT,
            ship_state TEXT,
            ship_postal_code TEXT,
            ship_country TEXT,
            promotion_ids TEXT,
            B2B TEXT,
            fulfilled_by TEXT,
            Unnamed_22 TEXT
            );

   

7. **Run the Application**

   ```bash
   python app.py

8. **Access the Application**
   
    - Access the application at http://127.0.0.1:5000/.

## Usage

   - Fetch Data: Enter the number of rows to fetch from Google Sheets API and click "Fetch Data". Data will be stored in Redis. The default count of rows is 100.
   - View Redis Data: Click "View Redis Data" to display data from Redis. This will be shown in key-value format.
   - Send Data to Database: Click "Send Data to Database" to process (Converting all the values in UPPER Case) and store the data in SQLite. Once data is successfully stored in database, Redis will be cleared.
   - Fetch Data from Database: Click "Fetch Data from Database" to view data from SQLite.

## Feedback
   - For further enquires reach out to umeshsugara9@gmail.com || https://in.linkedin.com/in/umesh-sugara


