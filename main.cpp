#include <iostream>
#include <future> 

extern "C"

float valueExchanger(int value){
    int result = value * 3.5;
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