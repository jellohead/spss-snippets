*simple crosstab.
* syntax: crosstab Name by Name.
crosstabs sector_2010 by sector_2011

*crosstab across multiple variables.
crosstabs sector_2010 by sector_2011 to sector_2014.

*Crosstab with barchart.
crosstabs sector_2010 by sector_2011
/cells column
/barchart.

*Crosstabs with chi squared independence test.
crosstabs sector_2010 by sector_2011
/cells column
/statistics chisq.