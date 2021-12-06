/*
reference: https://chanhuiseok.github.io/posts/improve-6/
가방 용량을 1부터 W까지 순서대로 살펴보면 2차원 배열이 필요하다.
가방 용량을 W부터 1까지 순서대로 살펴보면 1차원 배열이 필요하다.
*/

#include <iostream>
#include <algorithm>

using namespace std;

int main(){

    ios::sync_with_stdio(0);
    cin.tie(0);

    // N은 물건의 개수, W는 가방의 용량
    int N, W;
    cin >> N >> W;

    // w[i]는 i번째 물건의 무게
    // p[i]는 i번째 물건의 가치
    int w[101];
    int p[101];
    int dp[100010];

    for (int i = 0; i < N; i++){
        cin >> w[i] >> p[i];
    }

    for (int i = 0; i < N; i++){
        for (int j = W; j >= 1; j--){
            if (w[i] <= j){
                // i번째 물건을 가방 용량 j에 넣을 수 있을 때
                // 해당 물건을 넣는 것과 넣지 않았는 것 중 더 큰 값을 저장한다.
                dp[j] = max(dp[j], dp[j - w[i]] + p[i]);
            }
        }
    }

	cout << dp[W];

    return 0;
}
