# Program Name: Assignment5.py
# Course: IT3883/Section 01
# Student Name: Makayla Jenkins
# Assignment Number: Lab5
# Due Date: 11/20/ 2026
# Purpose: Create a SQL database, insert temperature data, and take the average temp



import sqlite3

# Connect to a SQLite database
connection = sqlite3.connect("temperatures.db")

# Create a cursor so we can execute SQL commands
cursor = connection.cursor()

# Create a table to store the temperature readings
cursor.execute("""
CREATE TABLE IF NOT EXISTS Temperatures (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Day_Of_Week TEXT,
    Temperature_Value FLOAT
)
""")

# Open the input file and read each line
with open("Assignment5input.txt", "r") as file:
    for line in file:
        # Split the line into the day and temperature
        data = line.strip().split()

        day = data[0]
        temperature = float(data[1])

        # Insert the reading into the database
        cursor.execute("""
        INSERT INTO Temperatures (Day_Of_Week, Temperature_Value)
        VALUES (?, ?)
        """, (day, temperature))

# Save all the changes made to the database
connection.commit()

# Find the average temperature for Sunday
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM Temperatures
WHERE Day_Of_Week = 'Sunday'
""")

sunday_average = cursor.fetchone()[0]

# Find the average temperature for Thursday
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM Temperatures
WHERE Day_Of_Week = 'Thursday'
""")

thursday_average = cursor.fetchone()[0]

# Print the average temperatures to the console
print("Average temperature on Sunday:", sunday_average)
print("Average temperature on Thursday:", thursday_average)

# Close the database connection when finished
connection.close()
