# def among(us_list):
#     if len(us_list) <= 1:
#         return us_list
#     else:
#         i = 0
#         while i < len(us_list):
#             smallest = us_list[i] # then prove it is the smallest or is not
#             j = i + 1
#             new_location = i
#             while j < len(us_list):
#                 new_value = us_list[j]
#                 if new_value < smallest:
#                     smallest = new_value
#                     new_location = j
#                 j += 1
#             us_list[i], us_list[new_location] = us_list[new_location], us_list[i]
#             i += 1

# # for loop version
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         max_index = i
#         for j in range(i + 1, n):
#             if arr[j] > arr[max_index]:
#                 max_index = j
#         arr[i], arr[max_index] = arr[max_index], arr[i]
#     return arr

# print(selection_sort(arr))

def wow(whoa):
    return [str(x for x in whoa)]
whoa = [1, 2, 3, 4, 5]
print(wow(whoa))