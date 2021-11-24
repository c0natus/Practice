#include <iostream>
#include <string>
#include <tuple>

using namespace std;

tuple<int, int> solution(int index, string s){
    int answer = 0;

    while (index <= s.size() -2){
        if (s[index+1] == '('){
            int iter_num = s[index] - '0';
            tuple<int, int> result = solution(index + 2,s);
            index = get<0>(result);
            int length = get<1>(result);
            answer += length * iter_num;
        }
        else if(s[index] == ')'){
            index += 1;
            return tuple<int, int>(index, answer);
        }
        else{
            answer += 1;
            index += 1;
        }
    }

    if (s[s.size()-1] != ')'){
        answer += 1;
    }

    return tuple<int, int>(index, answer);
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    cin >> s;

    cout << get<1>(solution(0, s)) << '\n';

    return 0;
}