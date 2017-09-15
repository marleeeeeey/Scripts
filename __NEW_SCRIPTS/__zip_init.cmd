@echo off

call __path_all.cmd

set DEST_FOLDER=%BACK_UP_ZIP_PATH%

set DATE_TIME=%date: =0% %TIME: =0%

for /f "tokens=1-7 delims=/-:., " %%a in ( "%DATE_TIME%" ) do (
    set DATE_TIME=%%c-%%b-%%a_%%d%%e%%f
)

:: ѕолучение имени директории
SET VDIR=%CD%

:: ѕеределываем абсолютный путь в относительный
:NEWITERATION
FOR /F "tokens=1* delims=\" %%a in ("%VDIR%") do (
if %%a==%VDIR% goto FINISH
set VDIR=%%b
)
goto NEWITERATION

:FINISH

SET DEST_NAME=%DEST_FOLDER%\%DATE_TIME%
ECHO add 7-Zip Directory to PATH
SET PATH=%PATH%;%PROGRAMFILES%\7-Zip;%PROGRAMFILES(x86)%\7-Zip


echo **************** __zip_init.cmd **********************
echo DEST_NAME=%DEST_NAME%
echo ******************************************************
















































::SET MY_PASSWORD
