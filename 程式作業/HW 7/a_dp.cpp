#include <iostream>
#include <math.h>       /* floor */

using namespace std;

struct Value{
    float x;
    float value;
};

Value parse(string s);

int main(){
    int testcase = 0;
    cin >> testcase;
    for (int i = 0; i < testcase; i++){
        string str;
        cin >> str;
        int position = str.find('=');
        string left_side = str.substr(0, position);
        string right_side = str.substr(position + 1, str.length());
        Value left_side_value = parse(left_side);
        Value right_side_value = parse(right_side);
        if(left_side_value.x == right_side_value.x){
            if(left_side_value.value == right_side_value.value){
                cout << "IDENTITY" << endl;
            }
            else{
                cout << "IMPOSSIBLE" << endl;
            }
        }
        else{
            float x = left_side_value.x - right_side_value.x;
            float constant_v = right_side_value.value - left_side_value.value;
            float ans = constant_v / x;
            cout << floor(ans) << endl;
        }

    }
}

Value parse(string s){
    Value value;
    value.x = 0;
    value.value = 0;
    int current_value = 0;
    int negative = 1;
    bool current_value_exist = 0;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == 'x'){
            if(current_value_exist){
                value.x += current_value * negative;
            }
            else{
                value.x += 1 * negative;
            }
            current_value = 0;
            // cout << "x' value: " <<  value.x << endl;
        }
        else if(s[i] == '-'){
            if(current_value_exist){
                value.value += current_value * negative;
                current_value = 0;
                current_value_exist = 0;
            }
            negative = -1;
        }
        else if(s[i] == '+'){
            if(current_value_exist){
                value.value += current_value * negative;
                current_value = 0;
                current_value_exist = 0;
            }
            negative = 1;
        }
        else{
            current_value = current_value * 10 + s[i] - '0';
            current_value_exist = 1;
            // cout << current_value << endl;
        }
    }
    if(current_value_exist){
        value.value += current_value * negative;
    }
    return value;
}