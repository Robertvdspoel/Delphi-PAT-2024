

with open('encrypted password example.txt', 'r') as file:       # in delphi this string will be retrieved from the string containing info such as username and primary key.
    string = file.read()


password = ''
keydigits= ''
for key in string:
   
    for c in key:
        if not c == ' ':
            keydigits += c
            print(keydigits)

        else:
            with open('keys.txt', 'r') as keyfile:
                for line in keyfile:
                    #print(line)
                    if keydigits == line[2 : 1002]:
                        password += line[0]
                        break
          #  string = string.replace(keydigits+ ' ', '')
            keydigits= ''


print(password)
