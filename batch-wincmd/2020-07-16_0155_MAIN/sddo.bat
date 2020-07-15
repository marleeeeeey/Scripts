@echo off
set back=%cd%
for /d %%i in (%cd%\*) do (
cd "%%i"
echo CURRENT SUBDIR: %%i

%*

echo * * * * * * *
echo.
)
cd %back%