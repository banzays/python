

# number = 99999999

# print(len(str(number)))
# counter = 0
# while number > 0:
#   number //= 10
#   counter += 1
# print(counter)

number = range(11)
print(number)
result = []
for i in number:
  if i % 2 == 0:
    result.append(i ** 3)
  else: 
    result.append(i)
print(result)

print([i ** 3 if i % 2 == 0 else i for i in range(11) ])

a = [1,2,3]
b = [4,5,6]
c = a,b
print(id(a))
print(id(b))
print(c)
a = 5
b.append(7)
print(id(a))
print(id(b))
assert c == ([1,2,3], [4,5,6,7])