'Print even index elements and odd index elements in separate list'
# l = [12, 78, 45, 23, 80, 76, 56, 43, 37, 23]
# Str_1 = []
# Str_2 = []
# i = 0
# while i < len(l):
#     if i % 2 == 0:
#         Str_1 = Str_1 + [l[i]]
#     else:
#         Str_2 = Str_2 + [l[i]]
#     i = i + 1
# print(Str_1)
# print(Str_2)
'Print even number elements and odd number elements in separate list'
# l = [12, 78, 45, 23, 80, 76, 56, 43, 37, 23]
# Str_1 = []
# Str_2 = []
# i = 0
# while i < len(l):
#     if l[i] % 2 == 0:
#
#         Str_1 = Str_1 + [l[i]]
#         L2 = list(Str_1)
#         # Str_1 = list(Str_1)
#     else:
#         Str_2 = Str_2 + [l[i]]
#     i = i + 1
# print(Str_1)
# print(Str_2)

'Convert the character in string from upper to lower'
# Str_1 = list(input("Enter the string: "))
# i = 0
# while i < len(Str_1):
#     if 'A' <= Str_1[i] <= 'Z':
#         print((chr(ord(Str_1[i])+32)), Str_1[i])
#     i = i + 1

'iterate over the list only if the list has atleast one item'

# li_1 = list(input("Enter the list item : "))
# if len(li_1) > 0:
#     i = 0
#     while i < len(li_1):
#         print(li_1[i], type(li_1[i]))
#         i = i + 1
# else:
#     print("List has no items")

'iterate over the list only if the list has atleast one string'

# li_2 = [1, 'hello', 2.3, 4, (2, 4), 'hi', [1, 2, 3]]
# i = 0
# while i < len(li_2):
#     if type(li_2[i]) == str:
#         j = 0
#         while j < len(li_2[i]):
#             print(li_2[i][j])
#             j = j + 1
#     i = i + 1

'iterate over the list only if the list has atleast one string'
li_2 = [1, 'hi', 2.3, 4, 'hello', (2, 4), [1, 2, 3]]
i = 0
while i < len(li_2):
    if type(li_2[i]) == str:
        j = 0
        while j < len(li_2):
            print(li_2[j])
            j = j + 1
    i = i + 1