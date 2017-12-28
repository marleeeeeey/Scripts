cmake_minimum_required(VERSION 3.1)

project(Test)

#find_library(PTHREAD_LIBRARY pthread)
#find_library(PCRE_LIBRARY pcre)
#
#include_directories(include)
#set(CMAKE_CXX_STANDARD 17)
#set(CMAKE_CXX_STANDARD_REQUIRED on)
#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Werror")

#find_package(OpenGL REQUIRED)
#include_directories(${OPENGL_INCLUDE_DIR})

#add_library(my_math_library my_math.cpp)
#add_library(my_math_library SHARED my_math.cpp)
#add_library(my_math_library STATIC my_math.cpp)

add_library(my_math_library STATIC
    src/my_math.cpp
    #src/math2.cpp
    )

add_executable(Test
    src/main.cpp
    )

target_link_libraries(Test my_math_library)

#
