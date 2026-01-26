std_info = {

    "name" : "arijit",
    "id" : 1234,
    "dept" : "BCA",
    "sec" : "3Q",
    "score": 90
    
}

std_info["college"] = "ABCD"
print(std_info)

# using update()

std_info.update({"location":"xyz"})
print(std_info)