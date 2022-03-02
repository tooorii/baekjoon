#include <iostream>
#include <string>
using namespace std;

int main(void) {
    int cnt_strings = 0;
    for (string line; cin >> line; cnt_strings++);
    cout << cnt_strings;
    return 0;
}