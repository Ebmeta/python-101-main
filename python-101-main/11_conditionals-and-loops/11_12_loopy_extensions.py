# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

filename = "operators.pdf"
end_pdf = ".pdf"

test_end = ""
len_pdf = len(end_pdf)
len_filename = len(filename)
for i in range(0, len_pdf +1):
    if filename[-i] == end_pdf[-i]:
        test_end += filename[-i]
#print(test_end)
test_end_1 = ''
for i in range(1, len(test_end)+1): # переворачиваем конец
    test_end_1 += test_end[-i]
#    print((test_end, test_end_1))

#print(test_end_1)

#print(type(test_end) ,test_end ,type(end_pdf))
if test_end_1 == end_pdf:
    print("This is .pdf file")
else : print("This is NOT .pdf file")











