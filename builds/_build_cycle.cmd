@echo off

echo Start building %SOLUTION_FILE_NAME% ...
msbuild /nologo /verbosity:minimal %SOLUTION_FILE_NAME% /p:Configuration=%SOLUTION_CONFIG%;Platform=%SOLUTION_PLATFORM%
