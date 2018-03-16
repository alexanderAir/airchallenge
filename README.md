# airchallenge
Takes in mp4 files, makes one big mp4 file

Usage:

Run 'videoConcatenator.py'

To send in mp4 files to concatenate send a request to "http://localhost:5000/inputFiles" with arguments of a list of file URLs under 'files' and your security token under 'token'. The token is just a placeholder.

An example of this is available in 'apiTester.py', which can be run to send in 3 example files.

After the process completes you can view the concatenated video file at "http://localhost:5000/getConcat".

There is no normalization done to files which may lead to poor resolution, FFMPEG errors and corrupted files. Not all mp4 files will work with each other. The 3 example files used work together pretty well.
