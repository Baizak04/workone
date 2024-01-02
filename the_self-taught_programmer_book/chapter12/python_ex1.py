import re


world = "Отличный Ютуб канал"
matches = re.findall("Отличный", world.lower(), re.IGNORECASE)
print(matches)

