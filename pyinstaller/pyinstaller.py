import os
import shutil
import time

print("Drag and Drop the .py File in")
py_path = input()

print("Drag and Drop the .ico File in")
ico = input()
os.system(f'pyinstaller "{py_path}" --icon "{ico}" --onefile')

time.sleep(0.2)

name = py_path.split("\\")
name = name[name.__len__() - 1]
name = name.replace(".py", "")

print(name)

os.remove(name + ".spec")
shutil.rmtree("build")

print(".exe Successfully created!")

input("Press Enter to close...")
