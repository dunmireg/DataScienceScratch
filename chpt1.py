from __future__ import division

#Data dump of users
users = [
{"id": 0, "name": "Hero"},
{"id": 1, "name": "Dunn"},
{"id": 2, "name": "Sue"},
{"id": 3, "name": "Chi"},
{"id": 4, "name": "Thor"},
{"id": 5, "name": "Clive"},
{"id": 6, "name": "Hicks"},
{"id": 7, "name": "Devin"},
{"id": 8, "name": "Kate"},
{"id": 9, "name": "Klein"}
]

#friendship Data
friendships = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
(4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

#Add a list of friends to each user
for user in users:
    user["friends"] = []

for i, j in friendships:
    #this works because users[i] is the user whose id is i
    users[i]["friends"].append(users[j]) #add i as a friend of j
    users[j]["friends"].append(users[i]) #add j as a friend of i

#find total number of connections
def number_of_friends(user):
    return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users) #24

#Divide by number of users to get average
num_users = len(users)
avg_connections = total_connections/num_users #2.4

#sort from most friends to least
#create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

sorted(num_friends_by_id, key = lambda (user_id, num_friends): num_friends, reverse = True)

#pg 6 pickup
