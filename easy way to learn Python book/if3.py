tweet_limit = 280
tweet_string = "Blah" * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("Соответствующий твит")
else:
    print("Прошел мимо", abs(diff))
    
tasks = 'взять перчатки, взять маску, дать кошке витамины, вызвать скорую помощь'
tasks1 = tasks.split(',')
print(tasks1)

setup = "утка заходит в бар..."
setup1 = setup.replace('утка', 'мартышка')
print(setup1)


setup = 'утка заходит в бар...'
setup1 = setup.strip('.')
print(setup1)

sum1 = [1, [2, 3]]
sum2 = sum1
sum3 = sum1[:]

sum1[1][0] = 1
print(sum2, sum3)