# 1)
st = open("st.txt", "w")
st.write("Hi \n hello \n first name: \n last name:")
st.close()

# 2)
with open("st1.txt", "w") as fr:
    fr.write("Hi1")
    
    
# 3)
with open("st.txt", "r") as ft:
    print(ft.readline(6))
    
    
# 4)
my_list = list()

with open("st.txt", "r") as df:
    my_list.append(df.read())
    
print(my_list)