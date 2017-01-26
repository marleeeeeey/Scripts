@echo off

set ARCHIVE_NAME=acr.7z



set DEST_FOLDER=%PROGRAMFILES(x86)%

if exist "%DEST_FOLDER%" (
    echo System x64
) else (
    echo System x86
    set DEST_FOLDER=%PROGRAMFILES%
)

echo PF folder: %DEST_FOLDER%

SET PATH=%PATH%;%PROGRAMFILES%\7-Zip;%PROGRAMFILES(x86)%\7-Zip

7z x "%ARCHIVE_NAME%" -o"%DEST_FOLDER%\"

pause
