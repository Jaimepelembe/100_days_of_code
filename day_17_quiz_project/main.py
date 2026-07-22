from prettytable import PrettyTable

# Creating a class

class User:
    def __init__(self,id,username):
        self.id=id
        self.username=username 
        self.followers=0

user1=User("001","PascalCase")
user2=User("002","camelCase")
user3=User("003","snake_case")
user3.followers=1

listUsers=[user1,user2,user3]

table=PrettyTable()
table.field_names=["Id", "Username","Followers"]

for user in listUsers:
    #print(user.id)
    #print(user.username)
    table.add_row([user.id,user.username,user.followers])

print(table)


