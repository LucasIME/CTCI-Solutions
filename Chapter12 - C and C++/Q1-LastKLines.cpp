#include<iostream>
#include<string>
#include<fstream>
#include<vector>

using namespace std;

void printLastKLines(string fileName, int k){
    ifstream file(fileName);
    int size = 0;
    vector<string> v(k);

    while(file.peek() != EOF){
        getline(file, v[size % k]);
        size++;
    }

    int start  = size > k? (size % k) : 0;
    int count = min(k, size);

    for(int i=0; i < count ; i++) cout << v[ (start + i)%k ] << endl;
}

int main(){
    printLastKLines("Q1-LastKLines.cpp", 10);
    return 0;
}
