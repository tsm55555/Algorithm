#include <iostream>

using namespace std;

int path(int m, int n);
int mem[1000][1000] = {0};

int main(){
    int testcase = 0;
    cin >> testcase;
    for (int i = 0; i < testcase; i++) {
        int m,n;
        cin >> m >> n;
        int ans = path(m, n);
        cout << ans << endl;
    }
}

int path(int m, int n){
    if (m <= 0 || n <= 0)  {  
        return 0;  
    }  
    if (m == 1 || n == 1)  {  
        return 1;  
    }  
    if (m == 2 && n == 2)  {  
        return 2;  
    }  
    if (mem[m][n] > 0)  {  
        return mem[m][n];  
    }  
    mem[m-1][n]=path(m - 1, n);  
    mem[m][n-1]=path(m , n-1);  
    mem[m][n] = mem[m - 1][n] + mem[m][n - 1];  
    return mem[m][n];
}