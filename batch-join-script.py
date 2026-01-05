import ffmpeg
from pathlib import Path

path = Path('.') # work in current directory
files = list(path.glob('**/*-L.wav')) # look for each left side .wav file

for file in files:
    fileLeft = file
    fileRight = file.parent.joinpath(file.name.removesuffix("-L.wav") + "-R.wav")
    inputLeft = ffmpeg.input(fileLeft)
    inputRight = ffmpeg.input(fileRight)
    outputPath = file.parent.joinpath(file.name.removesuffix("-L.wav") + "-Stereo.wav")
    (
        ffmpeg
        .filter([inputLeft, inputRight], 'amerge') 
        .output(str(outputPath))
        .run()
    )
    
