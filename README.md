# cliui

utils for command line user iteraction

* prompt
* confirm
* safedit

decorators

* sudo
* sigint

## safedit

```py
from cliui import safedit
import json

def is_json(content):
	try:
		json.loads(content)
		return True
	except:
		return False

if safedit('test.json',is_json):
	print('done')
else:
	print('wrong format')
```

## sudo

```py
from cliui import sudo

@sudo
def main():
	print('done')

if not main():
	print('pls run as root')
```
