from __future__ import division
from collections import Counter

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

#Define friends of friends

def friends_of_friend_ids_bad(user):
    return [foaf["id"]
        for friend in user["friends"] #for each of user's friends
        for foaf in friend["friends"]] #get each of their friends

def not_the_same(user, other_user):
    #two users are not hte same if they have different ids
    return user["id"] != other_user["id"]

def not_friends(user, other_user):
    #other_user is not a friend if he's not in user["friends"]
    return all(not_the_same(friend, other_user)
        for friend in user["friends"])

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                    for friend in user["friends"] #for each of my friends
                    for foaf in friend["friends"] #count *their* friends
                    if not_the_same(user, foaf)   #who aren't me
                    and not_friends(user, foaf))  #and aren't my friends

print friends_of_friend_ids(users[3]) #Counter({0: 2, 5: 1})

interests = [ #pick up page 7
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),

]
