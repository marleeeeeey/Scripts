@echo off
call init.cmd

7z a %DEST_NAME%"(exc)" -xr@"exc.txt" -p%MY_PASSWORD% -mhe=on 

:: EXAMPLES

:: zip from all
::7z a %DEST_NAME%"(all)" -p%MY_PASSWORD% -mhe=on 

:: zip form bin free
::7z a %DEST_NAME%"(bin_free)" -ir@"45_includeBinList.txt" -mhe=on 

:: zip from exclude
::7z a %DEST_NAME%"(exc)" -xr@"30_excludeList.txt" -p%MY_PASSWORD% -mhe=on 

:: zip from include
::7z a %DEST_NAME%"(inc)" -ir@"40_includeList.txt" -p%MY_PASSWORD% -mhe=on 