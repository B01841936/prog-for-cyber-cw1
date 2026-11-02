#define dictionary
user = {
        "username":"bob",
        "ip":"192.168.10.2",
        "event":"login",
        "risk":"high"
        }

#display username and ip address
print(user["username"],user["ip"])

#add status field and change risk
user["status"] = "blocked"
user["risk"] = "low"

#delete event field
del user["event"]

#print dictionary keys, values, and items
print(user.keys(),user.values(),user.items())