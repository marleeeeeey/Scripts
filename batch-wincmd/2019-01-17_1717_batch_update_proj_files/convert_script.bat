echo off

set PATH_TO_POWERSHELL="C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
set FDT_PATH="C:\Program Files (x86)\FEI\FEI Development Tools\"
set START_DIR=%__CD__%
echo START_DIR=%START_DIR%

if exist "component.xml" (  
  rem do nothing
) else (
  echo ERROR: you have to put this script to COMPONENT_NAME\build\
  goto FINISH_LABEL
)

:: Get COMPONENT_NAME
cd %START_DIR%..\
for %%f in (%CD%) do set COMPONENT_NAME=%%~nxf
echo COMPONENT_NAME=%COMPONENT_NAME%
  
echo This script converts all projects files for %COMPONENT_NAME% component to compatible with VS2017 build.
echo Settings checker apply after converting.
echo It is a temporary solution while migration not finished.
echo Please press any key to continue or close this window to abort.
pause

cd %START_DIR%..\..\
set WORK_DIR=%__CD__%
echo WORK_DIR=%WORK_DIR%
set FBT_SOURCEPATH=%WORK_DIR%
::Does string have a trailing slash? if so remove it 
IF %FBT_SOURCEPATH:~-1%==\ SET FBT_SOURCEPATH=%FBT_SOURCEPATH:~0,-1%
echo FBT_SOURCEPATH=%FBT_SOURCEPATH%

:CONVERTING_LABEL
echo Converting...

cd %WORK_DIR%\%COMPONENT_NAME%\build
call %PATH_TO_POWERSHELL% .\convert_vc141.ps1
echo %COMPONENT_NAME% converted

:SETTINGS_CHECKER_LABEL
echo To prevent SettingsCheck error temporary files *wpftmp.csproj should be deleted.
echo Please confirm this action for each file.
for /R %WORK_DIR% %%G in (*wpftmp.csproj) do del /P "%%G"

echo Start settings checker for %COMPONENT_NAME% component
%FDT_PATH%\DevToolsCmd.exe SettingsCheck -component %COMPONENT_NAME% -update -sources %FBT_SOURCEPATH%
echo %COMPONENT_NAME% SettingsCheck finished

:FINISH_LABEL 
cd %START_DIR%
echo SCRIPT FINISHED
pause