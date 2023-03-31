plaintext = input()
coded = input()
decode = input()

plaintext.replace(' ','_')
coded.replace(' ', '_')

code = {}

for i in range(len(plaintext)):
    if coded[i] not in code:
        code[coded[i]] = plaintext[i]

output = ''

for i in decode:
    if i not in code:
        output = output + '.'
    else:
        output = output + code[i]

print(output)


