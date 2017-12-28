@echo off

call __path_all.cmd
call __promtString.cmd

set QTDIR=c:\Qt\Qt5.6.1\5.6\msvc2015
set QMAKESPEC=win32-msvc2015
echo add %QTDIR% to PATH
set PATH=%QTDIR%\bin;%PATH%

call "%VS140COMNTOOLS%VsDevCmd.bat"

set MAIN_NAME=RSU-135
set CURRENT_MSVC_DIR=%SOLUTION_WORK_PATH%\%MAIN_NAME%

echo Start building...
msbuild /nologo /verbosity:minimal %CURRENT_MSVC_DIR%\%MAIN_NAME%.sln /p:Configuration=Release

set NEW_FOLDER=%SOLUTION_BIN_PATH%\%MAIN_NAME%

echo Coping files to %NEW_FOLDER%...

echo ******** FlySimulator_build_release.cmd **************
echo MAIN_NAME=%MAIN_NAME%
echo NEW_FOLDER=%NEW_FOLDER%
echo CURRENT_MSVC_DIR=%CURRENT_MSVC_DIR%
echo ******************************************************

xcopy %QTDIR%\plugins\platforms\qwindows.dll                %NEW_FOLDER%\platforms\     /y
xcopy %QTDIR%\bin\icudt54.dll                               %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\icuin54.dll                               %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\icuuc54.dll                               %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\Qt5Core.dll                               %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\Qt5Gui.dll                                %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\Qt5Network.dll                            %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\Qt5Svg.dll                                %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\Qt5Widgets.dll                            %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\libEGL.dll                                %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\libGLESv2.dll                             %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\auctl.dll           %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\GUI.dll             %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\libusb0.dll         %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\plane.dll           %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\PlxApi650.dll       %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\QArincUsb.dll       %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\RSU-135.exe         %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\RsuOneInstanse.dll  %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\sl.dll              %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\socklib.dll         %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\StdPlus.dll         %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\usmk.dll            %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\UsmkExt.dll         %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\UsmkIO.dll          %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\vcredist_x86.exe    %NEW_FOLDER%\               /y
xcopy %SOLUTION_BIN_PATH%\Win32\Release\ZGO.dll             %NEW_FOLDER%\               /y

pause