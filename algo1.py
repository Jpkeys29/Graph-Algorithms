# digits = "643"
# lookup ={
#             "2":"abc",
#             "3":"def",
#             "4":"ghi",
#             "5":"jkl",
#             "6":"mno",
#             "7":"pqrs",
#             "8":"tuv",
#             "9":"wxyz",
#         }

# # for digit in lookup:
# #     for char in lookup[digit]:
# #         print(char)
# lookup['10']= 'sigmalambda'
# print(lookup['3'])
# for char in lookup:
#     print(char)

lista = ['python','js','c##','java','c']
# for index,language in enumerate(lista):
#     print(index,language)

# index = 0
# for language in lista:
#     print(index,language)
#     index+=1
# for index,language in enumerate(lista):
#     print(index,language)
# for index,language in enumerate(lista):
#     if index%2==0:
#         print(('nope'))
#     print(language)

# def max_price(prices):
#     max = float('-inf')
#     for price in prices:
#         if price>max:
#             max = price
#     return max
# print(max_price([34.76,30.45,33.09,31.08,29.34,36.00]))

def multi_int(nums):
    output = []
    current = 1
    i = 0
    while i < len(nums):
        current = current * nums[i]       
        output.append(current)
        i+=1
    return output


print(multi_int([1,2,3,4]))