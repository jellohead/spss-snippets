# importing packages
import spss
import pandas
import numpy

# creating some data
a = numpy.array(["foo", "foo", "foo", "foo",
                 "bar", "bar", "bar", "bar",
                 "foo", "foo", "foo"],
                dtype=object)

b = numpy.array(["one", "one", "one", "two",
                 "one", "one", "one", "two",
                 "two", "two", "one"],
                dtype=object)

c = numpy.array(["dull", "dull", "shiny",
                 "dull", "dull", "shiny",
                 "shiny", "dull", "shiny",
                 "shiny", "shiny"],
                dtype=object)

# form the cross tab
pandas.crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'])


# importing package

# create some data
foo = pandas.Categorical(['a', 'b'],
                         categories=['a', 'b', 'c'])

bar = pandas.Categorical(['d', 'e'],
                         categories=['d', 'e', 'f'])

# form crosstab with dropna=True (default)
pandas.crosstab(foo, bar)

# form crosstab with dropna=False
pandas.crosstab(foo, bar, dropna=False)


# importing package

# create some data
foo = pandas.Categorical(['a', 'b'],
                         categories=['a', 'b', 'c'])

bar = pandas.Categorical(['d', 'e'],
                         categories=['d', 'e', 'f'])

# form crosstab with dropna=True (default)
pandas.crosstab(foo, bar)

# form crosstab with dropna=False
pandas.crosstab(foo, bar, dropna=False)

crossVar = pandas.crosstab(foo, bar)

# this works to get variable names out of SPSS dataset .sav file
*Way to get SPSS variable names.
BEGIN PROGRAM Python3.
varList = [spss.GetVariableName(i) for i in range(spss.GetVariableCount())]
print(varList)
END PROGRAM.

# this gets the index for a specified variable
*Find the indices of specific variables.
BEGIN PROGRAM Python3.
LookVars = ["S1", "Q4"]
VarInd = [varList.index(i) for i in LookVars]
print(VarInd)
END PROGRAM.


# search for specific data from the dataset using the variable name
BEGIN PROGRAM PYTHON3.
varList = [spss.GetVariableName(i) for i in range(spss.GetVariableCount())]


*Easy function to use.
BEGIN PROGRAM Python.


def AllSPSSdat(vars):
    if vars == None:
        varNums = range(spss.GetVariableCount())
    else:
        allvars = [spss.GetVariableName(i)
                   for i in range(spss.GetVariableCount())]
        varNums = [allvars.index(i) for i in vars]
    data = spss.Cursor(varNums)
    pydata = data.fetchall()
    data.close()
    return pydata


END PROGRAM.

# You can either supply a list of variables or None, in the latter case all of the variables are returned.
BEGIN PROGRAM Python.
MyDat = AllSPSSdat(vars=["Y", "Z"])
print MyDat
END PROGRAM.

# my attempt at print the entire dataset
BEGIN PROGRAM PYTHON3.
