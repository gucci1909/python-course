import pandas
import csv

# Data to write into words.csv
data = [
    ["Word", "Meaning"],
    ["Python", "A high-level programming language"],
    ["Pandas", "A data analysis library in Python"],
    ["CSV", "Comma-Separated Values"]
]

# Writing the data to words.csv
with open("words.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("words.csv file has been created.")
# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file