import requests
import mysql.connector

# Make a GET request to the Rick and Morty API
url = "https://rickandmortyapi.com/api/character"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()['results']  # Get JSON response and access the 'results'

    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="127.0.0.1",  # e.g., 'localhost' or your DB server
        port="3306",
        user="root",  # your database username
        password="Nand@2509",  # your database password
        database="da_data"  # the name of your database
    )

    cursor = db.cursor()

    # Prepare an insert statement
    sql = "INSERT INTO characters (id, name, status, species) VALUES (%s, %s, %s, %s)"

    # Insert each item into the database
    for item in data:
        values = (item['id'], item['name'], item['status'], item['species'])
        cursor.execute(sql, values)

    # Commit the transaction
    db.commit()

    print(f"{cursor.rowcount} rows were inserted.")

    # Close the cursor and database connection
    cursor.close()
    db.close()
else:
    print("Error:", response.status_code)


