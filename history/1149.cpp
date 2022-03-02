#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int num_inputs;
    cin >> num_inputs;
    int marginal_cost[num_inputs][3];
    for (int i = 0; i<num_inputs; i++) {
        for (int j = 0; j<3; j++) {
            cin >> marginal_cost[i][j];
        }
    }
    
    int total_cost[num_inputs][3];
    for (int i = 0; i<3 ; i++) {
        total_cost[0][i] = marginal_cost[0][i];
    }
    
    for (int i = 1; i<num_inputs; i++) {
        for (int j = 0; j<3; j++) {
            total_cost[i][j] = min(total_cost[i-1][(j+1)%3], total_cost[i-1][(j+2)%3]) + marginal_cost[i][j];
        }
    }
    
    cout << min(total_cost[num_inputs-1][0], min(total_cost[num_inputs-1][1], total_cost[num_inputs-1][2]));
    return 0;
}