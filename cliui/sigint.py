import signal

handlers = []

def handler(signal, frame):
	for h in handlers:
		h(signal, frame)

def sigint(fn):
	if 0 == len(handlers):
		signal.signal(signal.SIGINT, handler)
	handlers.append(fn)
	return fn
