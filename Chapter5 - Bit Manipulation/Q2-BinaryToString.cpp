#include<iostream>
#include<string>
using namespace std;

string toString(double n){
    //string sign="", expoent="", mantissa="";
    string resp ="";
    for(int i=0; i < 32; i++){
        n*=2;
        if (n>=1){
            resp =  resp + "1";
            n-=1;
        }
        else resp = resp + "0";
        if (n == 0) break;
    }
    if (n==0) return resp;
    else return "ERROR";
}

int main(){
    double n = 0.125;
    cout << toString(n) << endl;
    return 0;
}
