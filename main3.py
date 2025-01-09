import requests
import mysql.connector

# Function to fetch Pikachu's data from the PokeAPI and insert it into a database
def fetch_and_store_pikachu_data():
    # API URL for Pikachu data
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response

        # Connect to the MySQL database
        db = mysql.connector.connect(
            host="127.0.0.1",  # Database server address
            port="3306",       # MySQL default port
            user="root",       # Database user
            password="Nand@2509",  # Database password
            database="da_data"     # Database name
        )

        # Create a cursor object using the connection
        cursor = db.cursor()

        try:
            # SQL query to insert data
            sql = "INSERT INTO pokemon (id, name, base_experience, height, weight) VALUES (%s, %s, %s, %s, %s)"

            # Data tuple to insert into the database
            values = (data['id'], data['name'], data['base_experience'], data['height'], data['weight'])

            # Execute the SQL query with the data
            cursor.execute(sql, values)

            # Commit the transaction
            db.commit()

            print(f"1 row was inserted: ID {data['id']}, Name {data['name']}.")

        except mysql.connector.Error as err:
            # Handle errors for MySQL
            print(f"Error: {err}")

        finally:
            # Ensure that the cursor and connection are closed properly
            cursor.close()
            db.close()

    else:
        # Print the error if the API request failed
        print("Failed to retrieve data. Status code:", response.status_code)
        print("Error message:", response.text)

# Call the function to perform the data fetching and storing
print(fetch_and_store_pikachu_data())