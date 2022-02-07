my_list = list('xyzabc')
print(my_list)
my_list.sort() # no return
print(my_list)

my_list = 'this is a test'.split() #split into each word only
print(my_list)
my_list = list('this is a test') #list each char only
print(my_list)
my_list = sorted('this is a test') #sort string only
print(my_list)
my_list1 = 'i dunnthis is a test'
string_elements=my_list1.split() #split into each word only
reversed_elements = []
for element in string_elements:
    string_elements.append(element[::-1])
print(reversed_elements)