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
