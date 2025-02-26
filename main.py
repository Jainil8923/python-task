from typing import List, Dict
import random
import requests

from array_to_dict import atd
from group_user_by_age import group_user_by_age
from user import Users
from bank import SavingAccount, DepositAccount

def q1():
    user_version = input("Enter version for requests: ")
    if requests.__version__ == user_version:
        print("version matched.")
    else:
        print(f"both version are different, current installed version is: {requests.__version__}")

def q2():
    arr: List[str] = ["one", "two", "three", "four"]
    res: Dict[int, str] = atd(arr)
    for key, value in res.items():
        print(f"key: {key}, value: {value}")

def q3():
    users: Dict[str, int] = {}
    numer_of_users: int = int(input("Enter number of users: "))
    for i in range(numer_of_users):
        name_age = input("Enter key, value pair in formate: name:age ")
        index = name_age.find(":")
        name = name_age[0:index]
        age = int(name_age[index + 1:])
        users[name] = age
    res: Dict[int, List[str]] = group_user_by_age(users)
    print("Oldest persons group: ", end='')
    for name in res[3]:
        print(name, end=', ')
    print("\nYoungest persons group: ", end='')
    for name in res[0]:
        print(name, end=', ')

def q4():
    numbers: List[int] = []
    even_numbers: List[int] = []
    multiples_of_17: List[int] = []
    greater_then_user_input_number: List[int] = []
    for _ in range(1000):
        random_number = random.randrange(1,1000)
        numbers.append(random_number)
    user_input_number = int(input("Enter number between 1 and 1000: "))
    for num in numbers:
        if not num % 2:
            even_numbers.append(num)
        if num % 17:
            multiples_of_17.append(num)
        if num > user_input_number:
            greater_then_user_input_number.append(num)
    print("Even numbers: ", end='')
    for num in even_numbers:
        print(num, end=', ')
    print("\nNumbers multiplier of 17: ", end='')
    for num in multiples_of_17:
        print(num, end=', ')
    print("\nGreater_then_user_input_number: ", end='')
    for num in greater_then_user_input_number:
        print(num, end=', ')

def q5():
    users_data = Users()
    users_data.add()
    users_data.print()
    find_user = users_data.search(1)
    print(find_user)
    res = users_data.delete(2, "name")
    print(res)
    users_data.print()
    res = users_data.add_fields(2,{"name": "Pranjal"})
    print(res)
    users_data.print()
    res = users_data.delete(1)
    print(res)
    users_data.print()

def q6():
    saving_obj = SavingAccount(7, 5000, "123456789")
    deposit_obj = DepositAccount(10000,"638547385")
    print("Saving Account.")
    print(saving_obj.check_balance())
    print(saving_obj.calc_interest())
    print(saving_obj.deposit(2000))
    print(saving_obj.check_balance())
    print(saving_obj.withdrawal(500))
    print(saving_obj.withdrawal(1500))
    print(saving_obj.check_balance())
    print()
    print("Deposit Account.")
    print(deposit_obj.check_balance())
    print(deposit_obj.deposit(6000))
    print(deposit_obj.check_balance())
    print(deposit_obj.withdrawal(4000))
    print(deposit_obj.withdrawal(1000000))

if __name__ == "__main__":
    # q1()
    # q2()
    # q3()
    # q4()
    # q5()
    q6()