
string2=input("enter a word")
# for i in range(len(var)):
#     print(i)
#
# for char in var:
#     print(char)



string1 = 'aeiou'

s1 = set(string1)
s2 = set(string2)
common_char = s1 & s2    # Letters in both s1 and s2
print(common_char)