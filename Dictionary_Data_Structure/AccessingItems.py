thisdict = {

  "brand": "Ford",
  "model": "Mustang",
  "year": 1964

}

print(thisdict["brand"])
print(thisdict["model"])


# get all the keys
thisdict.keys()


# get all the values
thisdict.values()


# get all items 
thisdict.items()


# check if key exists

x = True
if "brand" in thisdict:
    print(x)