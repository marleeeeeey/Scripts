#include <parse_stream/parse_stream.h>
#include <greetings/greetings.hpp>
#include <string>
#include <sstream>
#include <iostream>



int main()
{
	greetings::hello();
    double res = parse_stream(std::cin);
    std::cout << "res=" << res << std::endl;
	greetings::goodbye();
    std::cin.get();
}