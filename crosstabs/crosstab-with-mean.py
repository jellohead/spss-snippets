import spss
import pandas as pd
import numpy as np
BEGIN PROGRAM PYTHON3.

END PROGRAM.


BEGIN PROGRAM PYTHON3.
help(spss)

END PROGRAM.


# form the cross tab.
pandas.crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'])


crossVar = pandas.crosstab(foo, bar)

# Importing all of the data.
BEGIN PROGRAM Python.
dataCursor = spss.Cursor()
AllData = dataCursor.fetchall()
dataCursor.close()
print AllData
END PROGRAM.

BEGIN PROGRAM PYTHON3.

cnxn = pyodbc.connect("DSN=acc_DB")
cursor = cnxn.cursor()
cursor.execute("select top 10 * from Table_XX")
rows = cursor.fetchall()

crsr = cnxn.cursor()
rows = crsr.execute('select top 10 * from Table_XX').fetchall()
df = pd.DataFrame.from_records(rows, columns=[x[0] for x in crsr.description])
END PROGRAM.

BEGIN PROGRAM PYTHON3.
# making data frame
data = pd.read_csv(
    "https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
# calling head() method
# storing in new variable
data_top = data.head()
# display
data_top
END PROGRAM.


BEGIN PROGRAM PYTHON3.
# making data frame
data = spss.Cursor()
# calling head() method
# storing in new variable
data_top = data.head()
# display
data_top
END PROGRAM.


# Importing all of the data.
BEGIN PROGRAM Python.
dataCursor = spss.Cursor()
AllData = dataCursor.fetchall()
dataCursor.close()
print AllData
END PROGRAM.
