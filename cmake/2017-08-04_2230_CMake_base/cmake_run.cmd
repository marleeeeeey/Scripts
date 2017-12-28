mkdir build
cd build

cmake ..
::cmake -G "Visual Studio 12 2013" ..

cmake --build . --config Release 

cd ..
pause