#include<iostream>
#include<vector>
#include<string>

using namespace std;

typedef std::uint8_t byte;

string toBin(byte b){
    string resp = "";
    for(int i=0; i <8;  i++){
        if ( (b&1) == 0) resp = "0" + resp;
        else resp = "1" + resp;
        b >>=1;
    }
    return resp;
}

void drawLine(vector<byte> &screen, int width, int x1, int x2, int y){
    int lineStartIndex = y * width;
    int firstByte = x1/8;
    int lastByte = x2/8;
    byte zero = 0x00;
    if ( firstByte == lastByte){
        byte mask  = ((1 << (x2-x1+1) )-1) << (7-x2);
        screen[lineStartIndex + firstByte] |= mask;
    }else{
        for(int i=firstByte+1; i< lastByte; i++) screen[lineStartIndex + i] |= 0xFF;
        screen[lineStartIndex + firstByte] |= (1 << (8-x1)) -1;  
        screen[lineStartIndex + lastByte] |=  (~zero) << (7 - x2%8);
    }
}

int main(){
    vector<byte> b(24, 0x00) ;
    int width = 3, x1=3, x2 = 17, y = 2;
    cout << width << " " << x1 << " " << x2 << " " << y << endl;
    drawLine(b,width, x1,x2,y);
    for(int i=0; i < 24; i++){
        if (i%width == 0) cout << endl;
        cout << toBin(b[i]) <<  " ";
    }
    return 0;
}
