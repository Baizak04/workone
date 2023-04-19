def main():
    data = {'website': 'google'}
    try: 
        print(data['url'])
    except:
        sum = 1 + 1
        print(sum)
        
main()

def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("деление на ноль")
    except TypeError:
        print("невозможно выполнить деление, один из параметром не число")
    finally:
        print("мы делили " + str(a) + " на " + str(b))

div("a",0)