CMAKE_MINIMUM_REQUIRED(VERSION 3.9.0)

PROJECT(calculator)

SET(HEADER_FILES)

SET(SOURCE_FILES
    src/calculator_main.cpp)

ADD_EXECUTABLE(calculator ${SOURCE_FILES} ${HEADER_FILES})

TARGET_LINK_LIBRARIES(calculator parse_stream greetings)
