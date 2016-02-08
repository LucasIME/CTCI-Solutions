#include<iostream>

using namespace std;

void swap( char &c, char &c2){
    char temp =  c;
    c = c2;
    c2 = temp;
}

char* URLfy (char* s, int n){
    int countSpaces  = 0;
    for(int i=0; i< n; i++) if(s[i] == ' ') countSpaces++;
    int r1 =n-1 , r2 = r1 + 2*countSpaces ;
    for( ; r1 >=0; r1--, r2--){
        if( s[r1] != ' ') swap(s[r1], s[r2]);
        else{
            s[r2-2] = '%';
            s[r2-1] = '2';
            s[r2] = '0';
            r2-=2;
        }
    }
    return s;
}

int main(){
    char s[] = "Mr John Smith    ";
    char *resp = URLfy(s, 13);
    cout << resp;
    return 0;
}
