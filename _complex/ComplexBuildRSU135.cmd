@echo off

call .\..\shared\_path_all.cmd

cd %SOLUTION_PROGRAMMING_PATH%
    call copy_to_bin.cmd

cd %SOLUTION_SCRIPTS_PATH%\builds
    call build_RSU135_LogOff.cmd

cd %SOLUTION_SCRIPTS_PATH%\copy
    call cpy_RSU-135.cmd

cd %SOLUTION_SCRIPTS_PATH%\zip_pack
    call zip_RSU-135.cmd

cd %SOLUTION_SCRIPTS_PATH%\nsis
    call nsis_RSU-135.cmd
    
    
pause