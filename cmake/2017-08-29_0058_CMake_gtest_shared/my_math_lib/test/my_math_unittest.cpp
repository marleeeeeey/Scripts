#include <my_math/my_math.h>
#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include <iostream>


TEST(MyMath, plus) 
{
    EXPECT_EQ(15, getResult("+",10,5));
}
TEST(MyMath, min) 
{
    EXPECT_EQ(5, getResult("-",10,5));
}
TEST(MyMath, umnog) 
{
    EXPECT_EQ(50, getResult("*",10,5));
}
TEST(MyMath, del) 
{
    EXPECT_EQ(2, getResult("/",10,5));
}


int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    int ret = RUN_ALL_TESTS();    
    
    std::cin.get();    

    return ret;
}