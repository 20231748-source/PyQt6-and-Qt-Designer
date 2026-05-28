# Them thu vien 
import json

# data mau
data = {
    "name": "Tran Van Linh",
    "age": 21,
    "city": "Thanh Hoa"
}

# create file json 
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)


