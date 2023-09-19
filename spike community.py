import time
import random

print("bem vinde a Perso da Spike Community")
time.sleep(2)
print("o mapa da personalizada de hoje é:")
print("...")
time.sleep(2)

maps = ['Ascent' ,'Haven', 'Split', 'Bind', 'Icebox', 'Breeze', 'Fracture', 'Pearl', 'Lotus', 'Sunset']
for c in maps:
    r = random.choice(maps)
print(r,"\n")

time.sleep(1)

print("Atacantes time A\nDefensores time B")
print("\n")