import os
for dpath , dnames , fnames in os.walk('/home/shivangi/Shivi'):
	for f in fnames:
		os.chdir(dpath)
		if f.startswith('s'):
			os.rename(f,f.replace('s','shivis'))

