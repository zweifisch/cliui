# cliui

utils for command line user iteraction

* prompt
* confirm
* safedit

decorators

* sudo
* sigint

prompt

```py
from cliui import prompt

print(prompt('name? '))
print(prompt('age? ', 18))
```

confirm

```py
from cliui import confirm
import sys

confirm('continue?')        #  continue? [y/n]
confirm('continue?', True)  #  continue? [Y/n]
confirm('continue?', False) #  continue? [y/N]

if not confirm('continue?'):
	sys.exit(0)
```

safedit

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

sudo

```py
from cliui import sudo

@sudo
def main():
	print('done')

if not main():
	print('pls run as root')
```

sigint

```py
from cliui import sigint
import sys

@sigint
def onsigint(signal, frame):
	print('caught user interupt')

@sigint
def onsigint2(signal, frame):
	print('quit')
	sys.exit(0)

while True:
	time.sleep(1)
```
