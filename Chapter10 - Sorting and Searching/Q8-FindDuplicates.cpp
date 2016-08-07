#include<iostream>

using namespace std;

void checkDuplicate(int *v, int size){
    bool bitSet[32000] = {false};
    for(int i=0; i< size; i++){
        int num = v[i];
        if (bitSet[num]){
            cout << num << endl;
        } else{
            bitSet[num] = true;
        }
    }
}

int main(){
    int v[16] = {0, 1, 2, 4, 2, 11, 3, 13, 4, 50, 67, 44, 51, 67, 79, 20000};
    checkDuplicate(v, 16);
    return 0;
}
