#include <iostream>
#include <queue>
#include <vector>

using namespace std;
int COL, ROW;
queue<pair<int, int>> location_one;

int minDays(int **tomatoes);
bool zeroIsIn(int **tomatoes);

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> COL;
    cin >> ROW;

    int **tomatoes = new int*[ROW];

    for(int i = 0; i < ROW; i++){
        tomatoes[i] = new int[COL];
    }

    for(int row = 0; row < ROW; row++){
        for(int col = 0; col < COL; col++){
            cin >> tomatoes[row][col];

            if (tomatoes[row][col] == 1){
                location_one.push(pair<int, int>(row, col));
            }
        }
    }

    int answer = 0;

    if (!location_one.empty()){
        answer = minDays(tomatoes);
    }

    if(zeroIsIn(tomatoes)){
        cout << -1 << '\n';
    } else {
        cout << answer << '\n';
    }

    return 0;
}

bool zeroIsIn(int **tomatoes){
    for(int row = 0; row < ROW; row++){
        for(int col = 0; col < COL; col++){
            if (tomatoes[row][col] == 0){
                return true;
            }
        }
    }
    return false;
}

int minDays(int **tomatoes){
    int count = 0;

    // 상, 하, 좌, 우
    int move_x[4] = {-1, 1, 0, 0};
    int move_y[4] = {0, 0, -1, 1};

    while (!location_one.empty()){
        count += 1;
        queue<pair<int, int>> tmp_queue;

        while(!location_one.empty()){
            int row = location_one.front().first;
            int col = location_one.front().second;

            location_one.pop();

            for(int i = 0; i < 4; i++){
                int tmp_row = row + move_x[i];
                int tmp_col = col + move_y[i];

                if(0 <= tmp_row && tmp_row < ROW && 0 <= tmp_col && tmp_col < COL && tomatoes[tmp_row][tmp_col] == 0){
                    tmp_queue.push(pair<int, int>(tmp_row, tmp_col));
                    tomatoes[tmp_row][tmp_col] = 1;
                }
            }
        }
        location_one = tmp_queue;
    }

    return count - 1;
}