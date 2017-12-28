#include "my_math.h"
#include <stdexcept>

enum Operations
{
    e_operation_plus,
    e_operation_minus,
    e_operation_mult,
    e_operation_div,
};

Operations get(const std::string & str)
{
    if(str == "+")
        return e_operation_plus;

    if(str == "-")
        return e_operation_minus;

    if(str == "*")
        return e_operation_mult;

    if(str == "/")
        return e_operation_div;

    throw std::logic_error("Not type");
}

double getResult(const std::string & operation, double lhs, double rhs)
{
    switch(get(operation))
    {
        case e_operation_plus: return lhs + rhs; break;
        case e_operation_minus: return lhs - rhs; break;
        case e_operation_mult: return lhs * rhs; break;
        case e_operation_div: return lhs / rhs; break;
    }

    throw std::logic_error("Not type");
}