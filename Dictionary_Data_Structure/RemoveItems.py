std_info = {

    "name" : "arijit",
    "id" : 1234,
    "dept" : "BCA",
    "sec" : "3Q",
    "score": 90
    
}

del std_info["dept"]
del std_info["id"]
print(std_info)

# using clear , pop, popitem

std_info.pop("sec")
print(std_info)
std_info.popitem()

std_info.clear()
print(std_info)