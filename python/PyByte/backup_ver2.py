# github/python
# backup_ver2.py

import os
import time

source = ['"C:\\My Documents"', 'C:\\Code']
target_dir = 'E:\\Backup'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(target_dir):
	os.mkdir(target_dir)
	print('Created Backup directory for you')
	
if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully create directory', today)
	
target = today + os.sep + now + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
	print('Successful back to', target)