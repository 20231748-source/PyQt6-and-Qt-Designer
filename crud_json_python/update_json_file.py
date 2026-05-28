# them thu vien
import json

# open file to data from json
with open("data.json", "r") as file:
    data = json.load(file)
# hien thi ra man hinh
    print(data)

# chinh sua voi du lieu da co san 
data["age"] = 28

# them truong du lieu moi 
data["email"] = "tranvanlinh21062005@gmail.com"

# Cap nhat lai du lieu vao trong file json 
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)