import shutil
import glob

for (i, filename) in enumerate(glob.glob('../face_arb/*.jpg')):
  shutil.copyfile(filename, 'image%05d.jpg'%i)

