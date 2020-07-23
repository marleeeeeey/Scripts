dir /b /s %1 > temp_filelist.txt
findstr /f:temp_filelist.txt /i /r /n "%2"
del temp_filelist.txt