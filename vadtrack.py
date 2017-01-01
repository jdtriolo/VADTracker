import datetime

################################################

# part details
types = ["Abdominal", "Post-Auricular"]
runin = [1, 2, 3, 4]
pf = ["Pass", "Fail", "Working", "TRW"]
SLnum = ["N/A", 146, 147, 148]

# JA0306-10 Work Orders
JA030610WO = []
JA030610WO.append(7494)
JA030610WO.append(7566)

# JA0306-20 Work Orders
JA030620WO = []
JA030620WO.append(7495)

# JA0406-10 Work Orders
JA040610WO = []
JA040610WO.append(7550)

# JA0406-20 Work Orders
JA040620WO = []
JA040620WO.append(7551)

# JHI-001 Work Orders
JHI0010WO = []
JHI0010WO.append(7646)

# JHI-002 Work Orders
JHI0020WO = []
JHI0020WO.append(7633)

#VADS
V1810 = [1810, types[0], JA030610WO[0], JA040610WO[0], JHI0020WO[0],
         runin[0], pf[2], SLnum[1], SLnum[0], SLnum[0], SLnum[0]]
V1811 = [1811, types[0], JA030610WO[0], JA040610WO[0], JHI0020WO[0],
         runin[0], pf[2], SLnum[1], SLnum[0], SLnum[0], SLnum[0]]
V1812 = [1812, types[0], JA030610WO[0], JA040610WO[0], JHI0020WO[0],
         runin[0], pf[2], SLnum[1], SLnum[0], SLnum[0], SLnum[0]]
V1813 = [1813, types[0], JA030610WO[0], JA040610WO[0], JHI0020WO[0],
         runin[0], pf[2], SLnum[1], SLnum[0], SLnum[0], SLnum[0]]
V1814 = [1814, types[0], JA030610WO[0], JA040610WO[0], JHI0020WO[0],
         runin[0], pf[2], SLnum[1], SLnum[0], SLnum[0], SLnum[0]]
V1815 = [1815, types[0], JA030610WO[0], JA040610WO[0], JHI0020WO[0],
         runin[0], pf[2], SLnum[1], SLnum[0], SLnum[0], SLnum[0]]
V1816 = [1816, types[0], JA030610WO[0], JA040610WO[0], JHI0020WO[0],
         runin[0], pf[2], SLnum[1], SLnum[0], SLnum[0], SLnum[0]]
V1817 = [1817, types[0], JA030610WO[0], JA040610WO[0], JHI0020WO[0],
         runin[0], pf[2], SLnum[1], SLnum[0], SLnum[0], SLnum[0]]
V1818 = [1818, types[0], JA030610WO[0], JA040610WO[0], JHI0020WO[0],
         runin[0], pf[2], SLnum[1], SLnum[0], SLnum[0], SLnum[0]]

VADS = [V1810,V1811,V1812,V1813,V1814,V1815,V1816,V1817,V1818]

## SL 146

# Dates
pstdate146 = datetime.date(2017,1,13) # projected start date
astdate146 = datetime.date(2017,1,18) # actual start date

pshdate146 = datetime.date(2017,1,13) # projected ship date
ashdate146 = datetime.date(2017,1,18) # actual ship date

pfgdate146 = datetime.date(2017,1,13) # projected to FG date
afgdate146 = datetime.date(2017,1,18) # actual to FG date

pdays146 = pshdate146-pstdate146 # projected number of days for build
adays146 = ashdate146-astdate146 # actual number of days for build
pdaysfg146 = pfgdate146-pshdate146 # projected number of days to FG
adaysfg146 = afgdate146-ashdate146 # projected number of days to FG
deltastart146 = astdate146-pstdate146 # delta actual/projected start date
deltaship146 = ashdate146-pshdate146 # delta actual/projected ship date
deltafg146 = afgdate146-pfgdate146 # delta actual/projected finished goods date

# Aggregate Data

SL146 = []

for item in VADS:
    if item[7] == 146:
        SL146.append(item)
    elif item[8] == 146:
        SL146.append(item)
    elif item[9] == 146:
        SL146.append(item)
    elif item[10] == 146:
        SL146.append(item)
SNlist146 = [item[0]for item in SL146]

pass146 = []
fail146 = []
working146 = []
state146 = [item[6] for item in SL146]
for item in state146:
    if item == "Pass":
        pass146.append(item)
    elif item == "Fail":
        fail146.append(item)
    elif item == "Working":
        working146.append(item)
passcount146 = len(pass146)
failcount146 = len(fail146)
workingcount146 = len(working146)

print(SL146)
print(SNlist146)
print(workingcount146)

# QUARTER

