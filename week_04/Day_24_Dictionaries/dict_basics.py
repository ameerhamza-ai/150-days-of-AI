dict = {}
dict["name"] = "Ameer"
dict["age"] = 20
dict["cgpa"] = 3.63
dict["City"] = "Kohat"
dict["field"] = "Artificial Intelligence"
dict["university"] = "KUST"
print(dict)
dict.update({"name": "Ameer Hamza","cgpa":3.85})
del dict["field"]
print("---Updated Dictionary---")
print(dict)