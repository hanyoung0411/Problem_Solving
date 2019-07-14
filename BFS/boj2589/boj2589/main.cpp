//  Created by Hanyoung Yoo on 14/07/2019.
//  Copyright © 2019 Hanyoung Yoo. All rights reserved.

#include <iostream>
#include <queue>
#include <utility>
#include <stdlib.h>

using namespace std;

#define treasure 1
#define water 2
#define MAX 2999

int direction[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
int result = -1;
int row, col;
int map[51][51],distances[51][51];
queue<pair<int,int>> location;

int check_valid(int,int);
void init_distances();

void traverse(){
    int x,y;
    while(location.size() !=0){
        x = location.front().first;
        y = location.front().second;
        location.pop();
        if(distances[x][y] > result)result = distances[x][y];
        for(int i=0;i<4;i++){
            if(check_valid(x+direction[i][0],y+direction[i][1])){
                if(distances[x+direction[i][0]][y+direction[i][1]] > distances[x][y] + 1 &&
                   map[x+direction[i][0]][y+direction[i][1]] == treasure){
                    location.push(make_pair(x+direction[i][0],y+direction[i][1]));
                    distances[x+direction[i][0]][y+direction[i][1]] = distances[x][y] + 1;
                }
            }
        }
    }
}
int main() {
    char input;
    cin>>row>>col;
    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            cin>>input;
            if(input == 'W')map[i][j] = water;
            else map[i][j] = treasure;
        }
    }
    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            if(map[i][j] == treasure){
                location.push(make_pair(i, j));
                init_distances();
                distances[i][j] = 0;
                traverse();
            }
        }
    }
    cout<<result;
    return 0;
}

int check_valid(int x, int y){
    if(x >= row || x < 0 || y >= col || y < 0)return 0;
    else return 1;
}

void init_distances(){
    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            distances[i][j] = MAX;
        }
    }
}
