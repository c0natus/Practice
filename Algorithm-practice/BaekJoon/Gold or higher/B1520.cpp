// 알고리즘은 똑같지만 방문을 체크하는 부분을 놓쳐서 시간초가과 났다.
// dp[i][j] = -1로 초기화하며 방문했다면 0의 값을 넣어주도록 하자.

#include <iostream>

using namespace std;

int row, col;
int arr[500][500];
int dp[500][500];

// 상, 하, 좌, 우
int move_range[4][2] = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

int solution(int r, int c){

    if ((r == row - 1 && c == col - 1) || dp[r][c] != -1){
        return dp[r][c];
    }

    dp[r][c] = 0;
    for(int i = 0; i < 4; i++){

        int move_row = r + move_range[i][0];
        int move_col = c + move_range[i][1];

        if (0 <= move_row && move_row < row && 0 <= move_col && move_col < col && arr[move_row][move_col] < arr[r][c]){
            dp[r][c] += solution(move_row, move_col);
        }
    }

    return dp[r][c];
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> row >> col;

    for(int r = 0; r < row; r++){
        for(int c = 0; c < col; c++){
            cin >> arr[r][c];
            dp[r][c] = -1;
        }
    }

    dp[row-1][col-1] = 1;
    dp[0][0] = solution(0, 0);

    cout << dp[0][0] << '\n';

    return 0;
}