# 1)
n = input("Как вас зовут?")

with open("st2.txt", "w") as st:
    st.write(n)
    
print(n, 'Приятно познокомится')