#include<iostream>
#include<string>
#include<fstream>
#include<vector>

using namespace std;

class Node{
    public:
        Node *left;
        Node *right;
        int value;
        Node(int value){
            this->value = value;
            this->left = NULL;
            this->right = NULL:
        }
}

Node getCopy(Node *base){
    if (base == NULL) return null;
    Node newNode(base.value);
    newNode.left = getCopy(base->left);
    newNode.right = getCopy(base->right);
    return newNode;
}

int main(){
}
