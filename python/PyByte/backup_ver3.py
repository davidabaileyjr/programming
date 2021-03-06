# github/pybyte
# backup_ver3.py

import os
import time

source = ['"C:\\My Documents"', 'C:\\Code']
target_dir = 'E:\\Backup'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%H%S')
comment = input('Enter a comment -->')

if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' +
		comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created directory', today)
	
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
	print('Successful back up to', target)
else:
	print('Backup Failed')