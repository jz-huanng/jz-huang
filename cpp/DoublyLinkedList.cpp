#include<iostream>
#include<sstream>
#include <string>
#include<vector>
using namespace std;

class Number {
public:
    int number;
    shared_ptr<Number> next;
    shared_ptr<Number> previous;
};

shared_ptr<Number> dll_start;
shared_ptr<Number> dll_end;

void sortDLL() {

}

void printDLLNumber() {
    shared_ptr<Number> current = dll_start;
    do {
        cout << current->number << " ";
        current = current->next;
    } while (current != nullptr);
    cout << endl;
}

void readInput(vector<int> & v) {
	string line, token;

	getline(cin, line);
	stringstream ss(line);

	int count = 0;
    while (getline(ss, token, ' ')) {
        v.push_back(stoi(token));
	}
}

void makeDLL(vector<int> v) {
    dll_start = make_shared<Number>();
    
    dll_start->number = v[0];
    dll_start->next = nullptr;
    dll_start->previous = nullptr;
    dll_end = dll_start;
    for (int i = 1; i < v.size(); i++) {
        shared_ptr<Number> item = make_shared<Number>();
        item->number = v[i];
        item->previous = dll_end;
        item->next = nullptr;
        dll_end->next = item;
        dll_end = item;
    }
}

int main(int argc, char * argv[]) {

    vector<int> v;
    readInput(v);
    if (v.size() == 0) {
        cout << endl;
        return 0;
    }
    makeDLL(v);
    printDLLNumber();



}


