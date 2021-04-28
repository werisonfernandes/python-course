data = []
with open("../machine-learning-databases/iris.data", "r") as file:
    for registry in file.readlines():
        data.append(registry.split(","))

print(data)
print(float(data[0][0]) + float(data[0][1]))