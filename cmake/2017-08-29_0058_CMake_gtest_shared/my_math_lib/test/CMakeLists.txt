CMAKE_MINIMUM_REQUIRED(VERSION 3.9.0)

PROJECT(my_math_unittest)

ENABLE_TESTING()

SET(GTEST_ROOT 
	../../googletest/build/stage)

FIND_PACKAGE(GTest REQUIRED)

IF(NOT GTest_FOUND)
	message(SEND_ERROR "Failed to find GTest")
	return()
ELSE()
	include_directories(${GTest_INCLUDE_DIR})
ENDIF()

ADD_EXECUTABLE(my_math_unittest my_math_unittest.cpp)

TARGET_LINK_LIBRARIES(my_math_unittest my_math)
 
TARGET_LINK_LIBRARIES(my_math_unittest GTest::GTest GTest::Main)

ADD_TEST(all_tests my_math_unittest)

