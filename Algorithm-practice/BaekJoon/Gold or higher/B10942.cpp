#include <iostream>

using namespace std;

int arr[2010] = {0};
int dp[2010][2010] = {0};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    for(int i = 1; i <= n; i++){
        cin >> arr[i];
        dp[i][i] = 1;
    }

    for(int interval = 1; interval < n; interval++){
        for(int left = 1; left <= n-interval; left++){
            int right = left + interval;
            if (interval == 1){
                if(arr[left] == arr[right]) dp[left][right] = 1;
                else dp[left][right] = 0;
                continue;
            }

            if (dp[left+1][right-1] == 0) dp[left][right] = 0;
            else{
                dp[left][right] = arr[left] == arr[right] ? 1 : 0;
            }
        }
    }

    int m;
    cin >> m;

    for(int i = 0; i < m; i++){
        int start;
        int end;

        cin >> start;
        cin >> end;

        cout << dp[start][end] << '\n';
    }

    return 0;
}