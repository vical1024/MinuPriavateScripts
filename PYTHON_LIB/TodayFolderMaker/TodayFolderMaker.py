import os
import datetime
import winshell
import sys
import pyperclip

DEFAULT_PATH = "D:/91.Desktop_Backup/"

now = datetime.datetime.now()

CurrentYear = now.strftime('%Y')
CurrentMonth = now.strftime('%m')
CurrentDay = now.strftime('%d')


upper_file_path = DEFAULT_PATH + CurrentYear + CurrentMonth
lower_file_path = DEFAULT_PATH + CurrentYear + CurrentMonth + "/" + CurrentYear + CurrentMonth + CurrentDay

if not os.path.exists(lower_file_path):
	if not os.path.exists(upper_file_path):
		os.makedirs(upper_file_path)
	os.makedirs(lower_file_path)

os.startfile(lower_file_path)

# if len(sys.argv) == 0:
	# os.startfile(lower_file_path)
# else:
# 	pyperclip.copy(lower_file_path)

# shortcut = winshell.shortcut(sys.executable)
# path = os.path.join(winshell.desktop(), CurrentYear + CurrentMonth + CurrentDay + "test")
# shortcut = file(path, 'w')
# shortcut.write('[folder shortcut]\n')
# shortcut.write('URL=%s' % lower_file_path)
# shortcut.close()
