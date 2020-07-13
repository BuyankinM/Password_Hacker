with open("users.json") as f:
    users_dict = json.load(f)
    print(len(users_dict["users"]))