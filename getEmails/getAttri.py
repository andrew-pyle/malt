str1 = "User:*"
str5 = "Service:*"

str2 = "IP from which the login attempt was detected:"
str3 = "Location:"
str4 = "Time:"

outputList = []

with open('sample.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
#print(data)
index1 = (data.find(str1))
index2 = (data.find(str5))
rawStr = data[index1:index2:]
rawList = rawStr.split('\\r\\n*')
outputList = []

for str in rawList:
    if str1 in str:
        endIndex = str.find('\\r\\n')
        outputList.append(str[7:endIndex:])
    if str2 in str:
        outputList.append(str[51::])
    if str3 in str:
        outputList.append(str[11::])
    if str4 in str:
        outputList.append(str[7::])


print (outputList)