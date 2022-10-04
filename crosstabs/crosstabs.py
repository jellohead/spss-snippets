# importing packages
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
