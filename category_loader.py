import json

with open("category.json", "r") as f:
    category_list = json.load(f)

new_list = []
for category in category_list:
    new_data = {"model": "posts.category"}
    new_data["fields"] = {}
    new_data["fields"]["name"] = category
    new_list.append(new_data)

with open("category_data.json", "w", encoding="UTF-8") as f:
    json.dump(new_list, f, ensure_ascii=False, indent=2)
