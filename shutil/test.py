import os, stat
import shutil

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

try:
	shutil.rmtree("python", onerror=remove_readonly)	
except Exception as e:
	print(e)
