import os
import subprocess
import sys
from importlib import metadata as importlib_metadata

import youdotcom

# with is like your try .. finally block in this case

with open("README.md") as file:
    # read a list of lines into data
    data = file.readlines()


print(f"Old Title: {data[6]}")


# typeof = input("type of update (major/minor/patch): ")
# os.system("poetry version " + typeof)
# os.system("poetry publish --build")
version = subprocess.run(["poetry", "version", "-s"], capture_output=True, text=True).stdout.rstrip()
# now change the 2nd line, note that you have to add a newline
data[6] = f"  YouDotCom for python v{version}" + "\n"
print(f"New Title: {data[6]}")
# and write everything back
with open("README.md", "w") as file:
    file.writelines(data)

print("update done!")
