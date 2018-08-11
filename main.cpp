#include <iostream>
#include <math.h>
#include <future> 

extern "C"

double valueExchanger(double value){
    double result = ceil(value * 350) / 100;
    return result;
}

// float caller(int value){
//     float result = std::async(std::launch::async,valueExchanger,value);
//     return result;
// }

int main() 
{
    // std::cout << "Hello, World!";
    // std::cout << valueExchanger(10);
    // return 0;
}