# input always comes as string
a = input()
print("the a value is", type(a))
b = input()
print("the b value is", int(b)+int(a))
# triple inverted coma's also we can write here
c = '''Hello
hi bro
hey bro,
"Hello sir"
'''
print(c);

d = input();
for character in d:
 print(str(character))
 
s = "poiujhjm"
print(len(s))
print(s[0:4])

# strings are immutable
ab = "Harry"
print(ab.upper()) # -> new string will be created
