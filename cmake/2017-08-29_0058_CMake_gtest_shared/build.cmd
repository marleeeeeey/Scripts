@echo off
rd build /s /q
mkdir build
cd build
cmake .. -G "MinGW Makefiles"
cmake --build .
cd ..
pause