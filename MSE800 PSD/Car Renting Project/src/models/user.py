# class User:
#     def __init__(self, user_id, username, role):
#         self.user_id = user_id
#         self.username = username
#         self.role = role


# class Admin(User):
#     def __init__(self, user_id, username):
#         super().__init__(user_id, username, "admin")


# class Customer(User):
#     def __init__(self, user_id, username):
#         super().__init__(user_id, username, "customer")

# class User:
#     def __init__(self, user_id, username, role):
#         self.user_id = user_id
#         self.username = username
#         self.role = role



# class Admin(User):
#     def __init__(self, user_id, username):
#         super().__init__(user_id, username, "admin")


# class Customer(User):
#     def __init__(self, user_id, username):
#         super().__init__(user_id, username, "customer")

class User:
    def __init__(self, user_id, username, role):
        self.user_id = user_id
        self.username = username
        self.role = role


class Admin(User):
    def __init__(self, user_id, username):
        super().__init__(user_id, username, "admin")


class Customer(User):
    def __init__(self, user_id, username):
        super().__init__(user_id, username, "customer")
        
        