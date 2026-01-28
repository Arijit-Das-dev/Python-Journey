"""
Docstring for Dictionary_Data_Structure.ChangeItems
"""
std_info = {

    "name" : "arijit",
    "id" : 1234,
    "dept" : "BCA",
    "sec" : "3Q",
    "score": 90
    
}

std_info["name"] = "a"
std_info["id"] = 53190
std_info["dept"] = "bba"
std_info["score"] = 908

print(std_info)


# using update()

std_info.update({"city":"xyz"})
print(std_info)