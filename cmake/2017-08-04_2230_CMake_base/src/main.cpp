#include <iostream>
#include <string>
int mult(int a, int b);
int diff(int a, int b);
int main(int argc, char ** argv)
{
    using namespace std;
    
    string s = "Hello World!";
    
    int a = 2;
    int b = 5;
    
    int m = mult(a,b);
    int d = 100;//diff(a,b);
    
    
    
    cout << s << endl;
    cout << "mult=" << m << endl;
    cout << "diff=" << d << endl;
    cin.get();
    
    return 0;
}