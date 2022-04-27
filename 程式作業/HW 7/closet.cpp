#include <iostream>
#include <math.h>
#include <algorithm>

using namespace std;

struct Point{
    double x;
    double y;
};

bool compare(Point a, Point b);
double distance(Point a, Point b);
double closet_pair(Point a[],int low,int high);

int main(){
    int testcase = 0;
    int num_pairs = 0;
    Point point[10000];

    cin >> testcase;
    for(int i = 0; i < testcase; i++){
        cin >> num_pairs;
        for(int j = 0; j < num_pairs; j++){
            cin >> point[j].x >> point[j].y;
        }   
        sort(point, point + num_pairs, compare);
        double min = closet_pair(point, 0, num_pairs - 1); 
        printf("%.3lf\n",min);
    }
}

bool compare(Point a,Point b){
    return a.x < b.x;
}

double distance(Point a, Point b){
    return (double)sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

double closet_pair(Point a[], int low, int high){
     if(low >= high){
         return 99999;
     } 

    int mid = (low + high) / 2;
    double min_left = closet_pair(a, low ,mid);
    double min_right = closet_pair(a, mid+1, high);

    double d = (min_left < min_right)? min_left : min_right;
    double mid_line = (double)(a[mid].x + a[mid+1].x) * 0.5; 
    double min_distance = d;
    for(int i = mid + 1; a[i].x < mid_line + d && i <= high; i++){
        for(int j = mid; a[j].x > mid_line - d && j >= low; j--){
            double temp = distance(a[i], a[j]);
            if(temp < min_distance){
                min_distance = temp;
            } 
        }
    }
    return min_distance;

}