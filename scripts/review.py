import subprocess

def getDiff():
    diff = subprocess.check_output(["git", "dif"], text=True)
    return diff



print(getDiff())