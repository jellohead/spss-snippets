import spss
import pandas as pd
import numpy as np
BEGIN PROGRAM PYTHON3.

END PROGRAM.


BEGIN PROGRAM PYTHON3.
help(spss)

END PROGRAM.


*Look up all variable names.
begin program.
for ind in range(spss.GetVariableCount()):
    varNam = spss.GetVariableName(ind)
    print(varNam)
end program.
