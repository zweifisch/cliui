import os
import tempfile
import shutil
from subprocess import call

def safedit(path, validator, editor='vi'):
	editor = os.environ.get('EDITOR', editor)
	f = tempfile.NamedTemporaryFile(delete=False)
	f.close()
	if(os.path.exists(path)):
		shutil.copyfile(path, f.name)
	try:
		call([editor, f.name])
		with open(f.name) as fp:
			if validator(fp.read()):
				shutil.copyfile(f.name, path)
				return True
	except:
		pass
	finally:
		f.unlink(f.name)
