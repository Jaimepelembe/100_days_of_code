from prettytable import PrettyTable

# Creating a class

class User:
    def __init__(self,id,username):
        self.id=id
        self.username=username 
        self.listFollowers=[]
        self.listFollowing=[]
        self.followers=0
        self.following=0


    def follow(self,user):
        """"Follow a user. Add a user in your following list and you in the user followers list"""
        if self != user:
            user.listFollowers.append(self)
            user.followers+=1

            self.listFollowing.append(user)
            self.following+=1
        else:
            print("You can't follow your self.")
    
    def unFollow(self,user):
        """Unfollow a user. Remove a user in your following list."""
        if user in self.listFollowing:
            self.listFollowing.remove(user)
            self.following-=1
            user.followers-=1
        else:
            print("You can't unfollow a user that you don't follow.")



def printTable(fieldNames,listUsers):
    """Print the table of users"""
    table=PrettyTable()
    table.field_names=fieldNames

    for user in listUsers:
        #print(user.id)
        #print(user.username)
        table.add_row([user.id,user.username,user.followers,user.following])

    print(table)


user1=User("001","PascalCase")
user2=User("002","camelCase")
user3=User("003","snake_case")
user4 = User("004","UPPERCASE")
user5 = User("005","Python")



listUsers=[user1,user2,user3,user4,user5]
fieldNames=["Id", "Username","Followers","Following"]

#Follow a user
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user3.follow(user2)
user1.follow(user1) #Is trying to follow him self.
user4.follow(user2)
user2.follow(user4)

#print(user2.followers)
#print(user1.followers)

printTable(fieldNames,listUsers)


#Unfollow a user
user1.unFollow(user2)
#user1.unFollow(user3)
#user3.unFollow(user2)
#user2.unFollow(user1)
user5.unFollow(user2)
#print(user2.followers)

printTable(fieldNames,listUsers)

