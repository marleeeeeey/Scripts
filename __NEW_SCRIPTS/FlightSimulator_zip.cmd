@echo off

call __zip_init.cmd

set SOURSE_FOLDER_NAME=FlightSimulator
set SOURSE_FOLDER_PATH=%NEW_FOLDER%

7z a "%DEST_NAME%_%SOURSE_FOLDER_NAME%_%USER_INPUT_STRING%" %SOURSE_FOLDER_PATH%\ -mhe=on 

::pause