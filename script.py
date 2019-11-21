import eyed3
import subprocess 
import re
import os

# list of all folder names, in order
folders = "傷物語,化物語,偽物語,頃物語,猫物語(黒),猫物語(白),囮物語,鬼物語,恋物語,花物語,憑物語,終物語,暦物語,続終物語,花物語".split(",")

	
# keep track of which track number it is

track_num = 1

# need to find first set of numbers in audiofile
audioFiles = [audioFile for audioFile in os.listdir() if os.path.isfile(audioFile) and ".mp3" in audioFile]
numberFinder = r"""([０-９]{1,3}|[0-9]{1,3})"""
findNumber = lambda fileName : int(re.search(numberFinder, fileName).group())


# iterate over all folders, in order
for folder in folders:


	os.chdir(folder)

	# sort according to the first numbers match
	audioFiles.sort(key=findNumber)

	# load audio files
	audioFiles = [eyed3.load(audioFile) for audioFile in audioFiles]


	# label all audiofiles
	for audioFile in audioFiles:
		audioFile.tag.album = "物語"
		# for Audiobooks
		audioFile.genre = 'Audiobook'
		audioFile.tag.track_num = track_num
		audioFile.tag.save()

		# make sure to increment, for number of audiobooks
		track_num += 1

	subprocess.call("mv *.mp3 ..", shell=True)

	os.chdir("..")



