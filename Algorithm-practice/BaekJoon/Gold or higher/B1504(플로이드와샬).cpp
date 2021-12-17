/*
 * 해당 문제를 보고 제일 처음 플로이드 와샬 알고리즘이 생각났다.
 * 플로이드 와샬은 다익스트라와 다르게 음의 간선을 포함해도 되지만, 음수인 사이클은 포함되어서는 안된다.
 * 
 * 시간 복잡도를 생각하면 다익스트라가 더 빠르다.
 * python은 시간초가가 나지만, cpp은 vertex 수가 작아 통과 된다.
 * 
 * 다익스트라: O(ElogE)
 * 플로이드 와샬: O(V^3)
 */

#include <iostream>

using namespace std;
typedef long long ll;

ll INF = 987654321;
ll adj_costs[810][810];

void floydWarshall(int v);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int v, e;
    cin >> v >> e;

    // 배열 초기화
    for(int i = 1; i <= v; i++){
        for(int j = 1; j <= v; j++){
            if (i == j) adj_costs[i][j] = 0;
            else adj_costs[i][j] = INF;
        }
    }

    // weight 입력 받기
    for(int i = 0; i < e; i++){
        int src, dst, weight;
        cin >> src >> dst >> weight;

        adj_costs[src][dst] = weight;
        adj_costs[dst][src] = weight;
    }

    floydWarshall(v);

    int stop_by1, stop_by2;
    cin >> stop_by1 >> stop_by2;

    ll min_path = min(
        adj_costs[1][stop_by1] + adj_costs[stop_by1][stop_by2] + adj_costs[stop_by2][v],
        adj_costs[1][stop_by2] + adj_costs[stop_by2][stop_by1] + adj_costs[stop_by1][v]
        );

    if (min_path >= INF) cout << -1;
	else cout << min_path;

    return 0;
}

void floydWarshall(int v){
    for (int through = 1; through <= v; through++){
        for(int start = 1; start <= v; start++){
            if (start == through) continue;
            for(int end = 1; end <= v; end++){
                if (end == through) continue;
                adj_costs[start][end] = min(
                    adj_costs[start][end], 
                    adj_costs[start][through] + adj_costs[through][end]
                    );
            }
        }
    }

}