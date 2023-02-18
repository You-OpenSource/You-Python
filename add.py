#!python3
"""
Convert a requirements.txt file to a Poetry project.
Just place in the root of your working directory and run!
"""
sourceFile = "./requirements.txt"

import os
import re

if not os.path.exists(sourceFile):
    # Install Pigar and run it to generate your initial requirements
    # https://github.com/damnever/pigar
    os.system("pip install pigar")
    os.system(f"pigar -o ~= -p {sourceFile}")

# We don't need to keep track of this file
with open(".gitignore", "a") as fh:
    fh.write("\npoetry-convert.py\n")

# Initialize Poetry if it doesn't yet have a pyproject.toml file
if not os.path.exists("./pyproject.toml"):
    os.system("poetry init")

with open(sourceFile) as fh:
    requirements = fh.read()

noComments = re.sub("^#.*$", "", requirements, 0, re.IGNORECASE | re.MULTILINE)
bareRequirements = re.sub("\n+", "\n", noComments, 0, re.IGNORECASE | re.MULTILINE).strip()

pipPoetryMap = {">": "^", "=": ""}

reqList = list()
for line in bareRequirements.splitlines():
    package, match, version = re.sub(r"^(.*?)\s*([~>=<])=\s*v?([0-9\.\*]+)", r"\1,\2,\3", line, 0, re.IGNORECASE | re.MULTILINE).split(",")
    try:
        poetryMatch = pipPoetryMap[match]
    except KeyError:
        poetryMatch = match
    poetryLine = f"{package}:{poetryMatch}{version}"
    reqList.append(poetryLine)

print("Found Poetry-compatible dependencies:")
print(reqList)

for req in reqList:
    os.system(f"poetry add {req}")
