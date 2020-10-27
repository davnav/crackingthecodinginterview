#Write code to reverse a C-Style String.C-String means that abcd is represented as
#five characters, including the null character.)
#
#***********Solution1**************
#not sure this is a right answer to above question or not!
#
print("**********Solution1***********")
s = raw_input("Enter a C-Style string:")
#finding the length of the string
l = len(s)
if len(s) ==0:
    print("entered string is blank")

def ReversedStringSln1(s):
    list = []
    for char in s:
        list.insert(0,char)

    return list
reversed = ReversedStringSln1(s)
print(''.join(reversed))
     