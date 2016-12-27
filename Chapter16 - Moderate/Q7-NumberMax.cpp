#include <iostream>
#include <climits>

using namespace std;

int getSignOf(int n){
    return ((n >> 31) & 1) ^ 1;
}

int numberMax(int a, int b){
    int sa = getSignOf(a);
    int sb = getSignOf(b);
    int sc = getSignOf(a-b);

    int differentSigns = sa ^ sb;

    int useAsign = sa ^ sb;
    int useCsign = useAsign ^ 1;

    int k = useAsign * sa + useCsign * sc;

    int q = k ^ 1;
    return a*k + b*q;
}

int main(){
    cout << numberMax(1,2)<< endl;
    cout << numberMax(-1,5) << endl;
    cout << numberMax(3,3) << endl;
    cout << numberMax(0,0)<< endl;
    cout << numberMax(13,0)<< endl;
    cout << numberMax(-5,-2) << endl;
    cout << numberMax(INT_MAX -2 , -15) << endl;
    return 0;
}