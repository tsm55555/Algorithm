#include <iostream>
#include <math.h>

using namespace std;

int happy(int num);

int main(){
    int test_num;
    string ans[100];
    cin >> test_num;
    for(int i = 0; i < test_num; i++){
        int num;
        cin >> num;
        if(happy(num) == 1){
            ans[i] = "Happy";
        }
        else{
            ans[i] = "Not Happy";
        }
    }
    for(int i = 0; i < test_num; i++){
        cout << ans[i] << endl;
    }
}

int happy(int num){
    int sum = 0;
    int length = to_string(num).length() - 1;
    while(1){
        if(length == -1){
            int end = to_string(sum).length();
            if(end==1){
                break;
            }
            else{
                num = sum;
                sum = 0;
                length = end;
                continue;
            }
            
        }
        sum += int(pow( int(num / pow(10,length)), 2));
        num -= int(num / pow(10,length))*pow(10,length);
        length--;
    }
    
    if(sum == 1){
        return 1;
    }
    if(length == 0){
        return 0;
    }
    return 0;
}