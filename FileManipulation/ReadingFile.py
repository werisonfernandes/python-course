with open("../tmp/file.tx", "r") as file:
    archive = file.read()
    print(archive)

print("********************************************************")
with open("../tmp/file.tx", "r") as file:
    print(file.readline())

print("********************************************************")
with open("../tmp/file.tx", "r") as file:
    print(file.readlines())

print("********************************************************")
with open("../tmp/file.tx", "r") as file:
    for line in file.readlines():
        print(line)