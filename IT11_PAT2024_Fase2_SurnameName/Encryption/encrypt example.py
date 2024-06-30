password = 'Robert!!'                  

encrypt = ''        # Idea can be to store the len of the string at the begining and write to a txt file to make decryption easier



for c in password:              # Manually clear the example file before running the new encryption
   
    with open('keys.txt', 'r') as keyfile:
        for line in keyfile:
            #print(line)
            if line[0] == c:
                encrypt += line[2 : 1002] + ' '
                break

with open('encrypted password example.txt', 'a') as file:       # in delphi this will be added to the string(line) containing info such as their username and primary key
    file.writelines(encrypt + '\n')