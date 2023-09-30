coder_info = {
    "name": "Alexey",
    "languages": {
        "Java": "beginner",
        "Php": "middle",
        "Python": "senior",
        "go": "none"
    }
}

coder_info_short = {
    "name": coder_info["name"],
    "languages": [],
}

for language, level in coder_info["languages"].items():
    if level in ["middle", "senior"]:
        coder_info_short["languages"].append(language)
        
print(coder_info_short)