@echo off
git clone https://github.com/google/googletest.git
cd googletest
mkdir build
cd build
cmake .. -G "MinGW Makefiles" -DCMAKE_INSTALL_PREFIX=stage -DBUILD_SHARED_LIBS=On
cmake --build . --target install --config Release
cd ..
cd ..