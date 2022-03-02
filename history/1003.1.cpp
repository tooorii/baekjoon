#include <iostream>
using namespace std;

int main() {
    int dp[42] = {1, 0, };
    
    for (int i=2; i<42; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    
    int testcase_num;
    cin >> testcase_num;
    
    while (testcase_num--) {
        int num;
        cin >> num;
        cout << dp[num] << ' ' << dp[num+1] << '\n';
    }
    return 0;
}