@echo off

call __path_all.cmd
call __promtString.cmd

set QTDIR=c:\Qt\Qt5.6.1\5.6\msvc2015
set QMAKESPEC=win32-msvc2015
set PATH=%QTDIR%\bin;%PATH%

call "%VS140COMNTOOLS%VsDevCmd.bat"

set CURRENT_MSVC_DIR=%SOLUTION_WORK_PATH%\FlyInstruments\msvc

echo Start building...
msbuild /nologo /verbosity:minimal %CURRENT_MSVC_DIR%\FlyInstruments.sln /p:Configuration=Release

set NEW_FOLDER=%SOLUTION_BIN_PATH%\FlySimulator

echo Coping files to %NEW_FOLDER%...

xcopy %QTDIR%\plugins\platforms\qwindows.dll                  %NEW_FOLDER%\platforms\     /y
xcopy %QTDIR%\bin\icudt54.dll                                 %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\icuin54.dll                                 %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\icuuc54.dll                                 %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\Qt5Core.dll                                 %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\Qt5Gui.dll                                  %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\Qt5Network.dll                              %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\Qt5Svg.dll                                  %NEW_FOLDER%\               /y
xcopy %QTDIR%\bin\Qt5Widgets.dll                              %NEW_FOLDER%\               /y
xcopy %CURRENT_MSVC_DIR%\Win32\Release\FlySimulator.exe       %NEW_FOLDER%\               /y
xcopy %CURRENT_MSVC_DIR%\Win32\Release\UdpReciever.exe        %NEW_FOLDER%\               /y
xcopy %CURRENT_MSVC_DIR%\FlyInstruments\flyinstruments_ru.qm  %NEW_FOLDER%\               /y

call FlightSimulator_zip.cmd

pause