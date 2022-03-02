#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int num_inputs;
    cin >> num_inputs;
    int cost[num_inputs + 1][3] = {0, };//0으로 초기화
    for (int i = 1; i <= num_inputs; i++) {
        for (int j = 0; j<3; j++) {
            cin >> cost[i][j];
            cost[i][j] += min(cost[i-1][(j+1)%3], cost[i-1][(j+2)%3]);
        }
    }
    cout << min(cost[num_inputs][0], min(cost[num_inputs][1], cost[num_inputs][2]));
    return 0;
}