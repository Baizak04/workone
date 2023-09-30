import json

profile = {
    "name": "Alice",
    "is_online": True,
    "hobbies": {
        1: "cryptography",
        2: "coding"
    }
}

result = json.dumps(profile)
print(result)