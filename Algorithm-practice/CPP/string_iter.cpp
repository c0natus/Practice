#include <iostream>
#include <string>

using namespace std;

/* Overloading * operator */
string operator * (string a, unsigned int b) {
    string output = "";
    while (b--) {
        output += a;
    }
    return output;
}

int main() {

    int n;
    cin >> n;
    string str;
    cin >> str;

    cout << 3 * 2 << '\n';
    cout << str * n << '\n';
    return 0;
}