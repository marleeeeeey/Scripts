#include <my_math/my_math.h>
#include <parse_stream.h>


double parse_stream(std::istream & is)
{
	std::cout<<"Enter expression: ";
	std::string expression;
	is>>expression;
	
	
	
	
	int oper_pos=0;
	
	 for(int i =0; i<expression.size();i++)
	{
		if (expression[i]=='+' || expression[i]=='-' 
		 || expression[i]=='*' || expression[i]=='*')
		 {
			 oper_pos=i;
			 break;
		 }
	}
	
	char operation = expression[oper_pos];
	std::string op{operation};
	
	
	std::string lhs_str;
	for(int i =0; i<oper_pos;i++)
	{
		lhs_str+=expression[i];
	}
	
	std::string rhs_str;
	for(int i =oper_pos; i<expression.size();i++)
	{
		rhs_str+=expression[i];
	}
	
	double lhs;
	std::istringstream istr_l(lhs_str);
	istr_l>>lhs;
	
	double rhs;
	std::istringstream istr_r(rhs_str);
	istr_r>>rhs;
	
	
	
	return getResult(op,lhs,rhs);
	
}