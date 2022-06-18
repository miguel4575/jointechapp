import cmd
import subprocess
cmd = ['python3','-m',' nltk.downloader words']
subprocess.run(cmd)
print("working")
