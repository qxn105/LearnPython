players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# ПРИМЕЧАНИЕ В квадратные скобки, определяющие сегмент, также можно включить третье значение. 
# Это значение, если оно присутствует, сообщает Python, сколько эле-
# ментов следует пропускать при выборе элементов в заданном диапазоне.

print(players[::2])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())