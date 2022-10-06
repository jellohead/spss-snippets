import spss
*Look up all variable names.
begin program.
for ind in range(spss.GetVariableCount()):
    varNam = spss.GetVariableName(ind)
    print(varNam)
end program.


* if variable lable is empty, change _ in variable name to " " and use that as the label.
* result looks like varNam = Trial_1_Reaction, varLabel = Trial 1 Reaction.
begin program python3.
for ind in range(spss.GetVariableCount()):
    varNam = spss.GetVariableName(ind)
    varLab = spss.GetVariableLabel(ind)
    if not varLab:  # True if varLab is empty string (no VARIABLE LABEL set)
        varLab = varNam.replace("_", " ")
        print(varLab)
end program.


*Create and inspect required VARIABLE LABELS commands.

begin program python3.
for ind in range(spss.GetVariableCount()):
    varNam = spss.GetVariableName(ind)
    varLab = spss.GetVariableLabel(ind)
    if not varLab:
        varLab = varNam.replace("_", " ")
        print("VARIABLE LABELS %s '%s'." % (varNam, varLab))
end program.


*Create and inspect required VARIABLE LABELS commands.

begin program python3.
for ind in range(spss.GetVariableCount()):
    varNam = spss.GetVariableName(ind)
    varLab = spss.GetVariableLabel(ind)
    if not varLab:
        varLab = varNam.replace("_", " ")
        print("VARIABLE LABELS %s '%s'." % (varNam, varLab))
end program.

begin program python3.
xVars = ['alco', 'cigs', 'exer']
print(xVars)
for xVar in xVars:
    print("GRAPH/SCATTER " + xVar + " WITH COSTS.")
end program.

# https://stackoverflow.com/questions/67945837/getting-column-header-from-snowflake-table-using-python-snowflake-connector
# I had the same question, using the python snowflake connector in Jupyter notebooks. I work with dataframes, so working from @SimonD's answer above I adapted the section with cursor.description to:
# hdrs = pd.DataFrame(cursor.description)
# df = pd.DataFrame(sql_data)
# From my data, the resulting hdrs dataframe has an attribute 'name' that I can use to set column names for the df dataframe, like so:
# df.columns = hdrs['name']

help(pandas)
