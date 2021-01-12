##
# Compute the total weight of widgets and gizmos
#
WIDGET_WEIGHT = 75
GIZMO_WEIGHT = 112

# Read the number of widgets and gizmos from the users
widgets = int(input("How many widgets? "))
gizmos = int(input("How many gizmos? "))

# Compute the total weight of widgets and gizmos
tot_widgets = widgets * WIDGET_WEIGHT
tot_gizmos = gizmos * GIZMO_WEIGHT

# Print the output
print("The total weight of widgets is", tot_widgets, "grams")
print("The total weight of gizmos is", tot_gizmos, "grams")      