version = input().split('.')
version = int("".join(version))
new_version = version + 1

print(".".join(str(new_version))) # обръща го на str, за да му сложи точките


############################################################
# Друго решение
############################################################
# old_version = "".join(map(str, input().split(".")))
# new_verison = ".".join(str(int(old_version + 1)))
# print(new_verison)