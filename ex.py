import ffmpy
import datetime
import os

from shutil import copyfile


file_name="Hulk.mp4"
file_name2="Hulk2.mp4"
file_out="ou/"+file_name+"_out.avi"

def convert(file_name,file_out):
	folder=file_out+"\\"+datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
	extension = os.path.splitext(file_name)[1]
	#strftime("%Y%m-%d::%H:%M:%S")
	print(folder)
	os.makedirs(folder)
	file_name1=folder+"\\input1"+extension
	file_name2=folder+"\\input2"+extension
	copyfile(file_name, file_name1);
	copyfile(file_name1,file_name2);

	file_out2=folder+"\\"+os.path.basename(file_name)
	ff = ffmpy.FFmpeg(inputs={file_name1: None,file_name2:None},
		outputs={file_out2: ['-filter_complex', '[0:v:0]pad=iw*2:ih[bg]; [bg][1:v:0]overlay=w']},
		executable='ffmpeg/bin/ffmpeg.exe'

		)
	ff.cmd
	ff.run()
	os.remove(file_name1)
	os.remove(file_name2)


#convert("C:\\Users\\Anurag\\Downloads\\Video\Love You Zindagi (Dear Zindagi) (Mixmasti.In).mp4","A:\\")

