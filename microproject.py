import sys
import subprocess
import os 



for entry in os.listdir(sys.argv[1]):
    # full_path = os.path.join(entry)
    subprocess.run(["wc", "-l", entry])

