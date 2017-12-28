@echo off

call _build_init.cmd

set SOLUTION_FILE_NAME=%SOLUTION_WORK_PATH%\RSU-135\RSU-135.sln
set SOLUTION_CONFIG=LogOff
set SOLUTION_PLATFORM=Win32

call _build_cycle.cmd

::pause