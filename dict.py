dict = {
    "Umang":1,
    "Arora":2
}

print(dict["Umang"])

# error handling -
print(dict.get("ARoraaaaa"))

for key in dict.keys():
    print(f"{key}-{dict[key]}")