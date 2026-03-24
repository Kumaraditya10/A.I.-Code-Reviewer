import subprocess

def getDiff():
    diff = subprocess.run(["git", "dif"], text=True)
    return diff



print(getDiff())