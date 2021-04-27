users = {}
print(users)

users = {"chaves": ["Chaves do 8", "20/01/2021", "Recep_001"],
         "quico": ["Quico flores", "21/12/2020", "Recep_002"]};
print(users)

users["florinda"] = ["Dona florinda", "20/02/2021", "RaioX_002"]
print(users)

users["florinda"] = ["Dona florinda 2", "20/02/2021", "RaioX_002"]
print(users)

print(users["florinda"])
print(users.get("quico"))