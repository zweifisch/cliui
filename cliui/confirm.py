import sys

def confirm(message, default=None):
	accept_values = {"yes":True, "y":True, "no":False, "n":False}
	choices = {None: '[y/n]', True: '[Y/n]', False: '[y/N]'}
	while True:
		sys.stdout.write("%s %s " % (message, choices[default]))
		choice = raw_input().lower()
		if choice:
			if choice in accept_values:
				return accept_values[choice]
		else:
			if default is not None:
				return default
