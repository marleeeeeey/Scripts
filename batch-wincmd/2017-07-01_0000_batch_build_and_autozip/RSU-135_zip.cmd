@echo off

call RSU-135_build_release.cmd
call __zip_init.cmd

set SOURSE_FOLDER_PATH=%NEW_FOLDER%

echo ************ _FlySimulator_zip.cmd *******************
echo SOURSE_FOLDER_PATH=%SOURSE_FOLDER_PATH%
echo Command for 7z: a "%DEST_NAME%_%MAIN_NAME%_%USER_INPUT_STRING%" %SOURSE_FOLDER_PATH%\ -mhe=on
echo ******************************************************

7z a "%DEST_NAME%_%MAIN_NAME%_%USER_INPUT_STRING%" %SOURSE_FOLDER_PATH%\ -mhe=on

pause