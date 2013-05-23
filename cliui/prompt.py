import readline


def prompt(hint, default=''):
	readline.set_startup_hook(lambda: readline.insert_text(default))
	try:
		return raw_input(hint)
	finally:
		readline.set_startup_hook()
