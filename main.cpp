#include <iostream>
#include <math.h>
#include <future> 

extern "C"

double valueExchanger(double value){
    double result = ceil(value * 350) / 100;
    return result;
}

int main() 
{

}