alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points']) ERROR

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

point_value = alien_0.get('points')
print(point_value)