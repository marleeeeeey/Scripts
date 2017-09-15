@echo off


:: change only archive name

set ARCHIVE_NAME=acr.7z



set PF_FOLDER=%PROGRAMFILES(x86)%

if exist "%PF_FOLDER%" (
    echo System x64
) else (
    echo System x86
    set PF_FOLDER=%PROGRAMFILES%
)

echo PF folder: %PF_FOLDER%

SET PATH=%PATH%;%PROGRAMFILES%\7-Zip;%PROGRAMFILES(x86)%\7-Zip

7z x "%ARCHIVE_NAME%" -o"%PF_FOLDER%\"

pause
