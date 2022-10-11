import os

asztal = f"C:/Users/{os.getlogin()}/Desktop"
print(asztal)
for i in range(0,5):
    f = open(f"{asztal}/demofile{i}.txt", "w")
    f.write(f". Új tartalom \n")
    f.close()
