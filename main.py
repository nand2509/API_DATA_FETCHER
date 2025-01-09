# Data Injestion process
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import mysql.connector

# Make a GET request to the JSONPlaceholder API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Get JSON response

    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="127.0.0.1",  # e.g., 'localhost' or your DB server
        port = "3306",
        user="root",  # your database username
        password="Nand@2509",  # your database password
        database="da_data"  # the name of your database
    )

    cursor = db.cursor()

    # Prepare an insert statement
    sql = "INSERT INTO posts (userId, id, title, body) VALUES (%s, %s, %s, %s)"

    # Insert each item into the database
    for item in data:  # Assuming data is a list of dictionaries
        values = (item['userId'], item['id'], item['title'], item['body'])
        cursor.execute(sql, values)

        # Commit the transaction
    db.commit()

    print(f"{cursor.rowcount} rows were inserted.")

    # Close the cursor and database connection
    cursor.close()
    db.close()
else:
    print("Error:", response.status_code)


df = pd.DataFrame(data)

# Filter by userId
filtered_by_user = df[df['userId'] == 1]

# Filter posts that contain a specific word in the title
filtered_by_title = df[df['title'].str.contains("sunt")]

# Combine filters: Get posts by userId 1 that contain "sunt" in the title
combined_filters = df[(df['userId'] == 1) & (df['title'].str.contains("sunt"))]

# Display the filtered data
print(filtered_by_user)
print(filtered_by_title)
print(combined_filters)



# import matplotlib.pyplot as plt
# import numpy as np

# # Example data
# states = ['Maharashtra', 'Uttar Pradesh', 'Delhi', 'Tamil Nadu', 'Karnataka', 'Gujarat']
# count = [124800, 24050, 20500, 6288, 2816, 3540]

# # Create 3D plot
# fig = plt.figure(figsize=(10, 7))
# ax = fig.add_subplot(111, projection='3d')

# # Set position for bars
# x_pos = np.arange(len(states))
# y_pos = np.zeros(len(states))
# z_pos = np.zeros(len(states))

# # Set width and depth of bars
# width = depth = 0.5

# # Create the bars
# ax.bar3d(x_pos, y_pos, z_pos, width, depth, count, color='skyblue')

# # Add labels
# ax.set_xlabel('States')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Number of Earners')
ax.set_xticks(x_pos)
ax.set_xticklabels(states)
ax.set_title('3D Visualization of People Earning More Than 1 Crore in FY24')

# Show plot
plt.show()
