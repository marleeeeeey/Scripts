@echo off
set SOLUTION_FILE_NAME=.\..\Work\RSU-135\RSU-135.sln
:: Release
:: Debug
:: LogOff
set SOLUTION_CONFIG=Release
set SOLUTION_PLATFORM=Win32

call build_init.cmd
echo Start building %SOLUTION_FILE_NAME% ...
msbuild /nologo /verbosity:minimal %SOLUTION_FILE_NAME% /p:Configuration=%SOLUTION_CONFIG%;Platform=%SOLUTION_PLATFORM%

pause