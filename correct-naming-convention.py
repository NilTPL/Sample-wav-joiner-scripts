from pathlib import Path
import shutil

path = Path('.')
filesLeft = list(path.glob('**/*-L.wav'))
filesRight= list(path.glob('**/*-R.wav'))

for file in filesLeft:
    shutil.move(file, file.parent.joinpath(file.name.removesuffix("-L.wav").rstrip() + "-L.wav"))
for file in filesRight:
    shutil.move(file, file.parent.joinpath(file.name.removesuffix("-R.wav").rstrip() + "-R.wav"))
