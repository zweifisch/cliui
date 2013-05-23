import os


def sudo(fn):
	def wrapper(*args, **kwargs):
		if os.geteuid() == 0:
			fn(*args, **kwargs)
			return True
	return wrapper
