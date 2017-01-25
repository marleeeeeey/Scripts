echo Bulding installer...

set NSISDIR=C:\Program Files (x86)\NSIS
set PATH=%NSISDIR%;%PATH%

makensis.exe nsis_RSU-135.nsi
