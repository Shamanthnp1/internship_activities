import sqlite3
import pandas as pd

# connect to database
conn = sqlite3.connect(r"C:\APPS\sqllite\mentors.db")

# JOIN query
query = """
SELECT interns.name,
       interns.track,
       mentors.mentor_name,
       interns.stipend
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""

# load into dataframe
df = pd.read_sql_query(query, conn)

# print result
print(df)

conn.close()