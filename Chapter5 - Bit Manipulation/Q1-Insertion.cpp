#include<iostream>

using namespace std;

int insertion(int N, int M, int i, int j){
    int clearMask = ~(( 1 - (1 << (i-j+1))) << i);
    N = N & clearMask;
    int Mmask = M << i;
    N = N | Mmask;
    return N;
}

int main(){
    int N = 1024;
    int M = 19;
    int i=2;
    int j = 6;
    cout << N <<" " << M << endl;
    cout << insertion(N, M, i, j) << endl;
    return 0;
}
