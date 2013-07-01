import os, sys

for file in os.listdir('.'):
	if file.endswith('.ui'):
		os.system('pyuic4 ' + file + ' -o Ui_' + file.rstrip('.ui') + '.py')

