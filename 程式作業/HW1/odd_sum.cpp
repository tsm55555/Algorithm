#include <iostream>

using namespace std;

int main(){
    int testcase = 0;
    int sum[100];
    cin >> testcase;
    for(int i = 1; i <= testcase; i++){
        int start, end;
        int start_num;
        cin >> start;
        cin >> end;
        if( start != 1){
            start_num = ((start - 2 ) / 2) + 1;
        }
        end = ((end - 1 ) / 2) + 1;
        if( start != 1){
            sum[i]  = end * end - start_num * start_num;
        }
        else{
            sum[i] = end * end;
        }
        
    }
    for(int i = 1; i <= testcase; i++){
        cout << "Case " << i << ": " << sum[i] << endl;
    }
}