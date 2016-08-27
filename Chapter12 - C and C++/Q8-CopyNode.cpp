#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<map>
#include<set>

using namespace std;

class Node{
    public:
        Node *left;
        Node *right;
        int value;
        Node(int value){
            this->value = value;
            this->left = NULL;
            this->right = NULL;
        }
};
void recursivePrint(Node *a, set<Node *> &s){
    if(a == NULL) return;

    if (s.find(a) != s.end()) return;

    s.insert(a);
    cout << a->value << " ";
    recursivePrint(a->left, s);
    recursivePrint(a->right, s);
}
void printNode(Node *a){
    set<Node *> s;
    recursivePrint(a, s);
}

Node * recursiveCopy(Node *base, map<Node *, Node*> &m){
    if (base == NULL) return NULL;

    map<Node *, Node*>::iterator it = m.find(base);
    if (it != m.end() ){
        return it->second;
    }
    Node *newNode = new Node(base->value);
    m[base] = newNode;
    newNode->left = recursiveCopy(base->left, m);
    newNode->right = recursiveCopy(base->right, m);
    return newNode;
}

Node * getCopy(Node *base){
    map<Node *, Node *> m;
    return recursiveCopy(base, m);
}

int main(){
    Node *a = new Node(1);
    a->left = new Node(2);
    a->right = new Node(3);
    a->left->left = new Node(4);
    a->left->right = a->right;
    a->right->left = a;
    Node *b = getCopy(a);
    printNode(a);
    cout << endl;
    printNode(b);
    cout << endl;
    a->right->value = 9;
    b->left->value = 11;
    printNode(a);
    cout << endl;
    printNode(b);
    return 0;
}
