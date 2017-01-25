set BIN_FOLDER=.\Win32\Release
set NEW_FOLDER=RSU-135

echo Coping files to %NEW_FOLDER%...

xcopy %BIN_FOLDER%\vcredist_x86.exe             .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\platforms\qwindows.dll       .\%NEW_FOLDER%\platforms\     /y
xcopy %BIN_FOLDER%\auctl.dll                    .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\CmdReader.dll                .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\GUI.dll                      .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\icudt53.dll                  .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\icuin53.dll                  .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\icuuc53.dll                  .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\plane.dll                    .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\PlxApi650.dll                .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\Qt5Core.dll                  .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\Qt5Gui.dll                   .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\Qt5Widgets.dll               .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\RSU-135.exe                  .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\RsuOneInstanse.dll           .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\socklib.dll                  .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\usmk.dll                     .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\UsmkExt.dll                  .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\UsmkIO.dll                   .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\ZGO.dll                      .\%NEW_FOLDER%\               /y
xcopy %BIN_FOLDER%\libusb0.dll                  .\%NEW_FOLDER%\               /y
