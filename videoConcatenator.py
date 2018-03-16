from flask import Flask
from flask import request
from flask import send_file
from ffmpy import FFmpeg
import requests
import os

app = Flask(__name__)

# Takes in a list of URLs for mp4 files to concatenate. Has zero error handling.
@app.route('/inputFiles')
def headerTest():
    token = request.args.get('token')
    if not securityStuff(token):
        return "Access denied"

    files = request.args.getlist('files')
    i = 0;
    for file in files:
        downloadFile("file" + str(i), file)
        i = i + 1

    makeConcat(i)

    return "Completed - see /getConcat"

# very tight security
def securityStuff(token):
    return True

# I put this as a separate hit from the upload because it's a lot easier to
# hit this in my browser after running the upload script
@app.route('/getConcat')
def giveFile():
    try:
        return send_file('concat.mp4', attachment_filename='megaVideo.mp4')
    except Exception as e:
        return str(e)

# Ignores normalization of files. I could do it but that feels like delving
# more into ffmpeg than what this challenge intends. My 3 example videos
# purposefully do not need any timebase changes to work with each other.
def makeConcat(maxFile):
    file = open('filelist.txt', 'w')

    # maxFile is not the nicest way to indicate file names but it works
    for i in range(maxFile):
        fileName = 'file' + str(i) + '.mp4'
        file.write('file \'' + fileName + '\'\n')
    file.close()

    ff = FFmpeg(
        inputs={'filelist.txt': '-safe 0 -y -f concat'},
        outputs={'concat.mp4': '-c copy'}
    )

    print(ff.cmd)
    ff.run()

    os.remove('filelist.txt')
    for i in range(maxFile):
        fileName = 'file' + str(i) + '.mp4'
        os.remove(fileName)

    print("Done")


# https://stackoverflow.com/questions/20723538/downloading-mp4-files-with-python
def downloadFile(name, url):
    name=name+".mp4"
    r=requests.get(url)
    print("****Connected****")
    f=open(name,'wb');
    print("Donloading.....")
    for chunk in r.iter_content(chunk_size=255):
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    print("Done")
    f.close()

if __name__ == "__main__":
    app.run()
