#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<map>
#include<set>

using namespace std;

template<typename T>
class SmartPointer {
    protected:
    T *ref;
    unsigned *ref_count;

    void remove() {
        --(*ref_count);
        if(*ref_count== 0) {
            delete ref;
            free(ref_count);
            ref =  NULL;
            ref_count = NULL;
        }
    }

    public:
    SmartPointer(T* ptr) {
        ref = ptr;
        ref_count = (unsigned*)malloc(sizeof(unsigned));
        (*ref_count) = 1;
    }

    SmartPointer(SmartPointer<T> &sptr) {
        ref = sptr.ref;
        ref_count = sptr.ref_count;
        ++(*ref_count);
        return *this;
    }

    ~SmartPointer() {
        this->remove();
    }

    T getValue() {
        return *ref;
    }

    SmartPointer<T> & operator=(SmartPointer<T> & sptr) {
        if(this == &sptr) return *this;

        if(*ref_count > 0) {
            remove();
        }

        ref = sptr.ref;
        ref_count = sptr.ref_count;
        ++(*ref_count);
        return *this;
    }

};

int main() {
    return 0;
}
