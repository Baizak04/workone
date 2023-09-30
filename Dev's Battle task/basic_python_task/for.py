words = ['we', 'i', 'you']
    
found = None

for word in words:
    
    if len(word) == 2:
        found = word
        break
    
print(found)