#include "StdPlus/StdPlus.h"

int main(int argc, char ** argv)
{
	AFUN;
	AMSG("Hello from TestMake");
	
	stdplus::SimpleCmdParser cmd;
	cmd.parseData(argc, argv);
	bool b = cmd.getValue<bool>("a", false);
	
	AVAR(b);
	
	
	APAUSE;
}