example = 'Today it will rain'
print(len(example))

example = 'Great' * 3
print(example)

example = "This is great"
sample = example.find('gr')
print(sample)

example = "China is the most populous country"
sample = example.title()
print(sample)

example = ['Ohio', 'Nevada', 'Colorado']
print(example[0])

x = [[1, 223], [245, 63, 22]]
print(x[1][2])

sample = [12, 32, 21, 24, 65]
print(sample[0:2])

speaker = "Алексей"
duration = 60
duration_hours = round(duration/120, 3)
print(f"Наш эфир будет длиться {duration} минут/ {duration_hours} часов. Эфир будет ввести спикер {speaker}")