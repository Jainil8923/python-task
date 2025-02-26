from typing import List, Dict

class Users:
    def __init__(self):
        self.users = {}

    def add(self):
        number_of_users = int(input("Enter number of users: "))
        for i in range(number_of_users):
            print(f"Enter data for {i} user: ")
            member_id: int = int(input("Enter Member Id: "))
            if member_id in self.users:
                print("UserId already exist.")
                i -= 1
                continue
            name: str = input("Enter name: ")
            lucky_number_pref: int = int(input("Enter lucky number: "))
            hobbies: List[str] = []
            no_of_hobbies = int(input("Enter number of hobbies: "))
            for j in range(no_of_hobbies):
                hobby = input(f"Enter {j} hobby: ")
                hobbies.append(hobby)
            no_of_books: int = int(input("Enter number of book: "))
            books: List[Dict[str,str]] = [{}]
            for j in range(no_of_books):
                book = input(f"Enter {j} book name: ")
                author = input(f"Enter {j} book author name: ")
                books.append({"book":book, "author":author})
            self.users[member_id] = {
                "member_id": member_id,
                "name": name,
                "lucky_number_pref": lucky_number_pref,
                "hobbies": hobbies,
                "books": books
            }

    def add_fields(self, member_id: int, changes: Dict[str,str] | None)-> str:
        if member_id not in self.users:
            return "No user found"
        if changes:
            for key, value in changes.items():
                self.users[member_id][key] = value
        return "user updated successfully."

    def search(self, member_id: int):
        if member_id in self.users:
            return self.users[member_id]
        return  "No user found."

    def delete(self, member_id: int, key: str | None = None):
        if member_id in self.users:
            if not key:
                del self.users[member_id]
                return "User deleted."
            else:
                del self.users[member_id][key]
        else:
            return "No user deleted."

    def print(self):
        for key, value in self.users.items():
            print(f"User: {key}\n")
            for key2, value2 in value.items():
                print(f"{key2} : {value2}")
            print("\n")