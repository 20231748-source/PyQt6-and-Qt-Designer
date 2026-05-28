# them thu vien 
import json

# open file to read data
with open("data.json", "r") as file:
    data = json.load(file)

# xoa mot truong du lieu 
del data["city"]  

# Cap nhat lai du lieu vao file 
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)