import os

try:
    os.rmdir('uz')
except Exception:
    print('there is no such directory')
