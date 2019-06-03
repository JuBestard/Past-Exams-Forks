import os
import sys
import subprocess

def shrink_file(root, filename):
	f, e = os.path.splitext(filename) 
	if e == '.pdf':
		print(root)
		path = os.path.join(root, filename)
		npath = os.path.join(root, f + '_shrink' + e)
		
		subprocess.run(['gs', '-q', '-dNOPAUSE', '-dBATCH', '-sDEVICE=pdfwrite', '-dPDFSETTINGS=/ebook' ,'-sOutputFile=' + npath, path])
		if os.path.isfile(npath):
			if os.path.getsize(npath) < os.path.getsize(path):
				# The new file is smaller than the existing one; keep it
				os.remove(path)
				os.rename(npath, path)
			else:
				# The new file is larger than the existing one; delete it
				os.remove(npath)

walkpath = sys.argv[1] if len(sys.argv) >= 2 else '.'

if os.path.isfile(walkpath):
	root, filename = os.path.split(walkpath)
	shrink_file(root, filename)
else:
	for root, dirs, files in os.walk(walkpath, topdown=False):
		for filename in files:
			shrink_file(root, filename)
