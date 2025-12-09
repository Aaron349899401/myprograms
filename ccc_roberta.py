import math
goal = int(input("what is your goal: "))
num_of_clubs = int(input("Enter the number of clubs you have: "))
wow = goal
club_list = []
for i in range(num_of_clubs):
    club = int(input(f"Enter your {i+1} club power: "))
    club_list.append(club)

# if goal in club_list:
#     print("Roberta wins in 1 stroke.")
# elif any(goal - x in club_list for x in club_list):
#     print("Roberta wins in 2 strokes.")
# elif any(goal - x - y in club_list for x in club_list for y in club_list):
#     print("Roberta wins in 3 strokes.")
# else:
#     print("Roberta acknowledges defeat.")

# def boobs(goal, num_of_clubs, club_list, strokes):
#     while strokes < num_of_clubs:
#         goal = wow
#         for i in club_list:
#             if goal - i in club_list:
#                 goal -= i
#                 strokes += 1
#     return strokes
# strokes = 0
# result = boobs(goal, num_of_clubs, club_list, strokes)
# if result > 0:
#     print(f"Roberta wins in {result} strokes")

# Solution via Mr.Park
# Dynamic programming
def golf(club_list, goal):
    dist = [0] + [math.inf] * goal
    for current in range(len(dist)):
        for c in club_list:
            new_location = current + c
            if new_location <= goal:
                dist[new_location] = min(dist[current]+1, dist[new_location])
    return dist[goal]
# my attempt at solution
def dih(club_list, goal):
    dic = {
        0:0,
    }
    while goal not in club_list:
        for i in range(1, goal):
            dic[i] = inf
        for key in range(1, goal):
            for item in club_list:
            dic[key + item] += 1
            
    return -1

print(dih(club_list, goal))
# my third solution
# def sixty_seven(club_list, goal):
#     count = 1
#     strokes = 1
#     for i in range(len(club_list)):
#         if goal in club_list:
#             return strokes
#         elif goal - club_list[i] in club_list:
#             strokes += 1
#         elif goal - club_list[count] in club_list:
#             count += 1
#             strokes += 1
#         else:
#             club_list.append(goal - club_list[i])
#             club_list.append(goal - club_list[count])
#     return -1

# print(sixty_seven(club_list, goal))
            
