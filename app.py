import gspread
import redis
import sqlite3
import json
from flask import Flask, request, render_template

# Initialize the Flask app
app = Flask(__name__)

# Initialize Google Sheets connection
gc = gspread.service_account(filename='keys.json')
sh = gc.open_by_key('1oBPHPO2crVNvIwS103scL0Fni6-LvMwXNUfyGw4lkNA')
worksheet = sh.sheet1

# Initialize Redis connection
r = redis.Redis(
    host='redis-11729.c212.ap-south-1-1.ec2.redns.redis-cloud.com',
    port=11729,
    password='WesogrMKN7U7h61sQkOgJqvDvXKy8XMK'
)

# Initialize SQLite database connection
conn = sqlite3.connect('data.db', check_same_thread=False)
cursor = conn.cursor()

def preprocess_data(data):
    # Convert all string values to lowercase
    return [{k: v.upper() if isinstance(v, str) else v for k, v in record.items()} for record in data]

def insert_data_into_table(data):
    # Insert data into the table
    if not data:
        return
    
    # Get the column names from the first record
    keys = data[0].keys()

    # Insert data
    for record in data:
        columns = ', '.join([f'"{key}"' for key in keys])
        placeholders = ', '.join(['?' for _ in keys])
        insert_sql = f'INSERT INTO apiDatabase ({columns}) VALUES ({placeholders})'
        values = tuple(record.get(key, '') for key in keys)
        cursor.execute(insert_sql, values)
    conn.commit()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/fetch_data', methods=['POST'])
def get_data():
    # Get the number of rows from the form input
    num_rows = int(request.form.get('num_rows', 200)) + 1
    
    # Fetch the rows from Google Sheets
    rows = worksheet.get_all_values()
    
    # Limit the rows based on user input
    if len(rows) > num_rows:
        rows = rows[:num_rows]
    
    # Get column names and data rows separately
    column_names = rows[0]
    data_rows = rows[1:]  # Exclude the header row
    
    # Transform data into a list of dictionaries
    result = []
    for row in data_rows:
        row_dict = {column_names[i]: row[i] for i in range(len(column_names))}
        result.append(row_dict)
    
    # Store the data in Redis
    r.set('api_data', json.dumps(result))  # Convert the list of dictionaries to a JSON string before storing
    
    # Return a success response and render a template with the "Send to Database" button
    return render_template('index.html', message="Data is stored in Redis DB. Please check.", show_button=True, num_rows=num_rows - 1)




@app.route('/view_redis_data', methods=['POST'])
def view_redis_data():
    # Fetch the data from Redis
    redis_data = r.get('api_data').decode()
    
    # Convert the JSON string back to a list of dictionaries
    redis_data = json.loads(redis_data)
    
    # Return the data to be displayed in the template
    return render_template('index.html', redis_data=redis_data, show_button=True)







@app.route('/send_to_db', methods=['POST'])
def send_to_db():
    # Fetch the data from Redis
    redis_data = r.get('api_data').decode()
    
    # Convert the JSON string back to a list of dictionaries
    redis_data = json.loads(redis_data)
    
    # Preprocess the data
    processed_data = preprocess_data(redis_data)
    
    # Store the processed data in SQLite
    insert_data_into_table(processed_data)
    
    # Clear the Redis DB
    r.delete('api_data')
    
    # Return a success response and show the "Fetch Data from Database" button
    return render_template('index.html', message="Data is successfully stored in the database and Redis DB is cleared.", show_button=False, show_db_button=True)




@app.route('/get_processed_data', methods=['POST'])
def fetch_from_db():
    # Fetch all data from the SQLite database
    cursor.execute('SELECT * FROM apiDatabase')
    rows = cursor.fetchall()

    # Get column names from the table
    column_names = [description[0] for description in cursor.description]

    # Convert the data to a list of dictionaries for rendering in the template
    sqlite_data = [dict(zip(column_names, row)) for row in rows]

    # Return the data to be displayed in the template
    return render_template('index.html', sqlite_data=sqlite_data, show_db_button=True)





if __name__ == '__main__':
    app.run(debug=True)
