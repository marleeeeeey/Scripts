@echo off

set QTDIR=C:\Qt\Qt5.4.0\5.4\msvc2013
set QMAKESPEC=win32-msvc2013

set PATH=%QTDIR%\bin;%PATH%
call "%VS120COMNTOOLS%VsDevCmd.bat"