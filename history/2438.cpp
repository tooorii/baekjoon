#include <iostream>
#include <string>
using namespace std;

int main(void) {
    int N;
    cin >> N;
    
    for (int i=1; i<=N; ++i) {
        for (int j=1; j<=i; j++) {
            cout<<'*';
        }
        cout<<endl;
    }
    return 0;
}

// g++ : 컴파일러
// 2438.cpp => 컴퓨터가 이해할 수 있는 기계어로 작성된 실행파일로
// a.out => 실행파일