#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

void solution(int size_of_matrix, int **matrix){
    
    bool **visited = new bool*[size_of_matrix];

    for (int i = 0; i < size_of_matrix; i++){
        visited[i] = new bool[size_of_matrix];
    }

    vector<int> area_size;
    queue<pair<int, int>> q;

    int move[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    for(int row = 0; row < size_of_matrix; row++){
        for(int col = 0; col < size_of_matrix; col++){
            if(matrix[row][col] == 1 && !visited[row][col]){

                int size = 1;

                q.push(pair<int, int>(row, col));
                visited[row][col] = true;

                while (!q.empty()){
                    int tmp_row = q.front().first;
                    int tmp_col = q.front().second;
                    q.pop();

                    for(int i = 0; i < 4; i++){
                        int move_row = tmp_row + move[i][0];
                        int move_col = tmp_col + move[i][1];

                        if(0<=move_row && move_row < size_of_matrix && 0 <= move_col && move_col < size_of_matrix){
                            if (matrix[move_row][move_col] == 1 && !visited[move_row][move_col]){

                                q.push(make_pair(move_row, move_col));
                                visited[move_row][move_col] = true;
                                size += 1;
                            }
                        }
                    }
                }
                area_size.push_back(size);
            }
        }
    }

    sort(area_size.begin(), area_size.end());
    cout << area_size.size() << '\n';

    for (int i = 0; i < area_size.size(); i++){
        cout << area_size[i] << " ";
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int size_of_matrix;
    cin >> size_of_matrix;

    int **matrix = new int*[size_of_matrix];

    for (int i = 0; i < size_of_matrix; i++){
        matrix[i] = new int[size_of_matrix];
    }

    for(int row = 0; row < size_of_matrix; row++){
        for(int col = 0; col < size_of_matrix; col++){
            cin >> matrix[row][col];
        }
    }

    solution(size_of_matrix, matrix);

    return 0;
}