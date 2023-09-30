# colors = ('red', 'green', 'black')
# print(type(colors))

# colors = ('red', 'green', 'black')
# color = colors.index('green')
# print(color)

def daylight():
    sunrise = '4:30'
    sunset = '22:30'
    
    return sunrise, sunset

start, finish = daylight()
print(start)
print(finish)