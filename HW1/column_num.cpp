#include <iostream>
#include <math.h>
#include <string>

using namespace std;

int happy(int num);

int main(){
    int test_num;
    int ans[100] = {};
    cin >> test_num;
    for(int i = 0; i < test_num; i++){
        string str;
        cin >> str;
        int length = str.length();
        for(int j = 0; j < length; j++){
            ans[i] += ((str[j] - 'A' + 1) * round(pow(26, length-(j+1))));
        }
    }
    for(int i = 0; i < test_num; i++){
        cout << ans[i] << endl;
    }
}

