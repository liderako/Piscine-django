from local_lib.path import Path

def 	run():
	path = Path("local_lib/")
	if (path.dirs("folder")) == []:
		newdir = path + "folder" + "/"
		newdir.mkdir()
	else:
		newdir = path + "folder" + "/"
	newfile = newdir + "my_file"
	newfile.touch()
	newfile.write_text("Hello world! Text writed!")
	print (newfile.text())

if __name__ == '__main__':
    run()