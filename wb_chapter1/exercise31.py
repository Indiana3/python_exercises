##
# Convert kilopascals to pounds per square inch,
# millimeters of mercury and atmospheres
#
PA_IN_KPA = 1000
PA_IN_PSI = 6895
PA_IN_MMHG = 133.322
PA_IN_ATM = 101325

# Read the pressure in KPa
kpa = float(input("Please, enter a pressure" \
    " in KPa: "))

# Convert to PSI
psi = kpa / PA_IN_KPA * PA_IN_PSI

# Convert to mmHg
mmhg = kpa / PA_IN_KPA * PA_IN_MMHG

# Convert to atm
atm = kpa / PA_IN_KPA * PA_IN_ATM

# Display the results
print(kpa, "KPa are equal to: ")
print(psi, "psi")
print(mmhg, "mmHg")
print(atm, "atm")

