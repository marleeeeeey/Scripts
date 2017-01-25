@echo off

call build_init.cmd

set SOLUTION_FILE_NAME=.\..\Work\RSU-135\RSU-135.sln
echo Start building %SOLUTION_FILE_NAME% ...
msbuild /nologo /verbosity:minimal %SOLUTION_FILE_NAME% /p:Configuration=Release;Platform=Win32
