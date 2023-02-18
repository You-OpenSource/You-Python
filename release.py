import os
import subprocess
import sys
from importlib import metadata as importlib_metadata

from github_release import gh_release_create

version = subprocess.run(["poetry", "version", "-s"], capture_output=True, text=True).stdout.rstrip()

title = input("title: ")


notes = input(r"changes (use \ for a enter): ")


with open("RELEASE.md") as file:
    # read a list of lines into data
    data = file.readlines()


notes = str(notes).replace("\\", "\n")
print(len(data))
data[17] = f"{notes}"


with open("RELEASE.md", "w") as file:
    file.writelines(data)


with open("RELEASE.md") as file2:
    # read a list of lines into data
    text = file2.read()


gh_release_create("You-OpenSource/You-Python", f"{version}", publish=True, name=f"{title} - {version}", body=f"{text}")
