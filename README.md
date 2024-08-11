# Catalys-Task

## Overview

This project fetches e-commerce data from a Google Sheet, stores it temporarily in Redis, preprocesses it, and then stores it in an SQLite database.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   
2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

3. **Configure Google Sheets**
   
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
   
7. **Run the Application**

   ```bash
   python app.py

2. **Install Dependencies**


