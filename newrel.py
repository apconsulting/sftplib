import os, re, sys

usage = "usage:\nnewrel.py x.y.z"

# Check version arg
if len(sys.argv) < 2:
    print("Missing version argument")
    print(usage)
    sys.exit(1)

match = re.fullmatch('(\d+)\.(\d+)\.(\d+)-?([a-zA-Z-\d\.]*)\+?([a-zA-Z-\d\.]*)', sys.argv[1])
if match is None:
    print("Argument is not a version string:", sys.argv[1])
    print(usage)
    sys.exit(1)


# Check git status


# Update version in pyproject.toml
newContent = []
with open("pyproject.toml") as f:
    for l in f:
        if l.startswith("version"):
            newContent.append('version = "0.0.1"')
        else:
            newContent.append(l) 

with open("pyproject.toml", "w") as f:
    f.writelines(newContent)


# Commit changes
os.system(f'git commit -a -m "New release {sys.argv[1]}"')

# Tag commit
os.system(f'git tag -a v{sys.argv[1]} -m "Release {sys.argv[1]}"')

# Push changes
#os.system(f'git push origin v{sys.argv[1]}"')
