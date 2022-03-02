#include <iostream>
using namespace std;

int main() {
    int arr [31][31];
    int n, k;
  
    for (int i=0; i<31; i++) {
        arr[i][0] = 1;
        arr[i][i] =1;
        
        for (int j=1; j<i; j++) {
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j];
        }
    }
    
    
    cin >> n >> k;
    cout << arr[n-1][k-1];
    
    return 0;
    
}