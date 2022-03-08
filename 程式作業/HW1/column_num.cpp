#include <iostream>
#include <math.h>
#include <string>

using namespace std;

int main(){
    int test_num;
    int ans[100] = {};
    cin >> test_num;
    for(int i = 0; i < test_num; i++){
        string input;
        cin >> input;
        int length = input.length();
        for(int j = 0; j < length; j++){
            ans[i] += ((input[j] - 'A' + 1) * round(pow(26, length-(j+1))));
        }
    }
    for(int i = 0; i < test_num; i++){
        cout << ans[i] << endl;
    }
}

