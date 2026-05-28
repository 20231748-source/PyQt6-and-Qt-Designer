# them thu vien
import json

# open file to data from json
with open("data.json", "r") as file:
    data = json.load(file)
# hien thi ra man hinh
    print(data)