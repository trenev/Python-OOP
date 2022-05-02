from collections import defaultdict

class Library:
    def __init__(self):
        self.user_records = []      # user objects
        self.books_available = defaultdict(list)   # {author(str): [book1(str), book2(str),.....],...}
        self.rented_books = defaultdict(dict)      # {username1(str): {book1(str): days(int),..}, username2(str): {...},...}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)
        if user.username in self.rented_books:
            self.rented_books.pop([user.username])

    def change_username(self, user_id: int, new_username: str):
        filtered_user = [element for element in self.user_records if element.user_id == user_id]
        try:
            if filtered_user[0].username == new_username:
                return "Please check again the provided username - " \
                       "it should be different than the username used so far!"
            else:
                old_name = filtered_user[0].username
                if old_name in self.rented_books:
                    self.rented_books[new_username] = self.rented_books.pop(old_name)
                filtered_user[0].username = new_username
                return f"Username successfully changed to: {new_username} for userid: {user_id}"
        except IndexError:
            return f"There is no user with id = {user_id}!"
