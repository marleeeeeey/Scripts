CMAKE_MINIMUM_REQUIRED(VERSION 3.9)

PROJECT(GuiChat)

MESSAGE("*****************************************************************")
MESSAGE("Manual install CMAKE_PREFIX_PATH")
SET(CMAKE_PREFIX_PATH "c:/Qt/Qt5.6.1/5.6/msvc2015/")
MESSAGE("STD_PLUS_DIR=$ENV{STD_PLUS_DIR}")
MESSAGE("QT_PLUS_DIR=$ENV{QT_PLUS_DIR}")
MESSAGE("CMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH}")
MESSAGE("*****************************************************************")

INCLUDE_DIRECTORIES(
 $ENV{STD_PLUS_DIR}/include
 $ENV{QT_PLUS_DIR}/include
 src
 )

## Find includes in corresponding build directories
#set(CMAKE_INCLUDE_CURRENT_DIR ON)

# Instruct CMake to run moc automatically when needed.
set(CMAKE_AUTOMOC ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOUIC_SEARCH_PATHS ui)

# Find the QtWidgets library
find_package(Qt5Widgets)

# Tell CMake to create the GuiChat executable
add_executable(GuiChat WIN32
 src/Server/ServerApplication.cpp
 src/Server/ServerCore.cpp
 src/Server/ServerGraphicSystem.cpp
 src/Server/ServerMain.cpp
 src/Server/ServerMainWindow.cpp)

# Use the Widgets module from Qt 5.
target_link_libraries(GuiChat Qt5::Widgets)