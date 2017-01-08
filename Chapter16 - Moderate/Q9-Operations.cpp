#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

int neg(int x){
    int newSign = x >= 0? -1 : 1;
    int resp = 0;
    while (x != 0){
        x+=newSign;
        resp+=newSign;
    }
    return resp;
}

int mult(int x, int y){
    bool signX = x >= 0;
    bool signY = y >= 0;
    int outputSignal = signX != signY ? -1 : 1;
    int resp = 0;
    if(signX == signY){
        for(int i=0; i < abs(x); i++){
            resp += abs(y);
        }
        return resp;
    }else{
        int neg = min(x,y);
        int pos = max(x,y);
        for(int i=0; i < pos; i++){
            resp += neg;
        }
        return resp;
    }
}

int subtract(int x, int y){
    return x + neg(y);
}

int divi(int x, int y){
    if (y==0)
        throw std::invalid_argument("received 0 as second parameter");
    bool signX = x >= 0;
    bool signY = y >= 0;
    int outputSignal = signX != signY ? -1 : 1;
    int k = 0;
    x = abs(x);
    y = abs(y);
    while( mult(k, y) < x)
        k++;        
    if(mult(k,y) == x) 
        return mult(k ,outputSignal);
    else 
        return mult(k-1 ,outputSignal);
}

int main(){
    int x = 12;
    int y = -4;
    cout << neg(x) << endl;
    cout << mult(x, y) << endl;
    cout << subtract(x, y) << endl;
    cout << divi(x, y) << endl;    
    return 0;
}