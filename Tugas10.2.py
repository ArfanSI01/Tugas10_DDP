fruits = ['pepaya', 'mangga', 'pisamng', 'durian', 'jambu']

def balikan(list):
    hasil = []
    for item in list:
        hasil.insert(0, item)
    return hasil
    
print(balikan(fruits))