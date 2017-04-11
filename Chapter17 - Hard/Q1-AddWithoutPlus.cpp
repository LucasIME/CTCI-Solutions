#include<iostream>

using namespace std;

int add(int a, int b){
    if (b == 0)
        return a;
    int sum = a ^ b;
    int carry = (a & b) << 1;
    return add(sum, carry);
}

int main(){
    cout << add(20, 12) << endl;
    cout << add(0, 2) << endl;
    cout << add(1, -1) << endl;
    cout << add(5, 32) << endl;
    cout << add(1024, -9) << endl;
    cout << add(10389, 3423) << endl;
    return 0;   
}

