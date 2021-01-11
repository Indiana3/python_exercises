measure_unit = input('Choose which unit you prefer, feet or meters')
if measure_unit == ' meters':
    measure_unit = 'meters'
if measure_unit == ' feet':
    measure_unit = 'feet'
length = float(input('Insert the room lenght'))
width = float(input('Insert the room width'))
area = length * width
print('The room area is %.2f %s' % (area, measure_unit))