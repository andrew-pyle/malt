str1 = "User: "
str2 = "IP from which the login attempt was detected: "
str3 = "Location: "
str4 = "Time: "


outputList = []

search = open('sample.txt')
for line in search:
    if str1 in line:
        outputList.append(line[6:len(line)-1:])
    if str2 in line:
        outputList.append(line[46:len(line)-1:])
    if str3 in line:
        outputList.append(line[10:len(line)-1:])
    if str4 in line:
        outputList.append(line[6:len(line)-1:])
print(outputList)