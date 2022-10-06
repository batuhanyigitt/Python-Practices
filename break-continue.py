# name = 'Ahmet Batuhan'

# for letter in name:
#     if letter == 'ı':
#         continue
#     print(letter)

# x = 0

# while x < 5:    
#     x+=1
#     if x == 2:
#         continue
#     print(x)


# Sum of the 1-100 

x = 0
result = 0

while x <= 100:    
    x+=1
    if x % 2 == 0:
        continue
    result += x

print(f'sum: {result}')