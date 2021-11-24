#include <iostream>
#include <vector>

using namespace std;

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    while (true){
        int n;
        cin >> n;

        if (n == 0) break;

        int *histo = new int[n];

        for (int i = 0; i < n; i++){
            cin >> histo[i];
        }


    }

    return 0;    
}