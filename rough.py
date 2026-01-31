# my_list = [1,2,3]
# my_str = "ramesh_vellanki"
# my_int = 329



# print(type(my_list))

# my_list.clear() #inbuilt methods. #list here is an object and clear is a method


from oops_project import chatbook
user1 = chatbook()

#user3 = chatbook()

#encapsulation
#print(user1._chatbook__name)

# getter and setter
# print(user1.get_name())
# user1.set_name("Agent_x")
# print(user1.get_name())


# print(user1.id)
# print(user2.id)
# print(user3.id)

chatbook.set_id(10)
user2 = chatbook()
print(user2.id)
