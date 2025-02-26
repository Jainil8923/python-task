from typing import List, Dict

def group_user_by_age(users: Dict[str, int])-> Dict[int, List[str]]:
    group_users: Dict[int, List[str]] = {i: [] for i in range(4)}
    for key, value in users.items():
        if value <= 35:
            group_users[0].append(key)
        elif value <= 50:
            group_users[1].append(key)
        elif value <= 65:
            group_users[2].append(key)
        else:
            group_users[3].append(key)
    return  group_users