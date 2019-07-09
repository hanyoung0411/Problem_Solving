//  Created by Hanyoung Yoo on 02/07/2019.
//  Copyright © 2019 Hanyoung Yoo. All rights reserved.
//

#include <iostream>
#include <queue>
#include <utility>
#include <cmath>

using namespace std;

int map[1501][1501];
int value[1501][1501];

struct cmp{
    bool operator()(pair<int, int> t, pair<int, int> u){
        return map[t.first][t.second] > map[u.first][u.second];
    }
};

int main() {
    int N;
    int current_value,max_val=1;
    pair<int,int> current_loc;
    priority_queue<pair<int, int>,vector<pair<int, int>>,cmp> pq;
    
    cin>>N;
    cin>>current_loc.first>>current_loc.second;
    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
            cin>>map[i][j];
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(map[current_loc.first-1][current_loc.second-1] < map[i][j])pq.push(make_pair(i, j));
        }
    }
    value[current_loc.first-1][current_loc.second-1]=1;
    //pq.push(make_pair(current_loc.first-1, current_loc.second-1));
    
    while(pq.empty() != true){
        current_loc = pq.top();
        pq.pop();
        cout<<current_loc.first<<' '<<current_loc.second<<' '<<map[current_loc.first][current_loc.second]<<endl;
        current_value = value[current_loc.first][current_loc.second];
        for (int i=0; i<N; i++) {
            // left
            if(current_loc.first > 0 && abs(current_loc.second-i)>1){
                if(map[current_loc.first-1][i] > map[current_loc.first][current_loc.second] &&
                   value[current_loc.first-1][i] < current_value+1){
                    value[current_loc.first-1][i] = current_value+1;
                    pq.push(make_pair(current_loc.first-1, i));
                }
            }
            // right
            if (current_loc.first<N-1 && abs(current_loc.second-i)>1) {
                if(map[current_loc.first+1][i] > map[current_loc.first][current_loc.second] &&
                   value[current_loc.first+1][i] < current_value+1){
                    value[current_loc.first+1][i] = current_value+1;
                    pq.push(make_pair(current_loc.first+1, i));
                }
            }
            // up
            if (current_loc.second>0 && abs(current_loc.first-i)>1) {
                if(map[i][current_loc.second-1] > map[current_loc.first][current_loc.second] &&
                   value[i][current_loc.second-1] < current_value+1){
                    value[i][current_loc.second-1] = current_value+1;
                    pq.push(make_pair(i, current_loc.second-1));
                }
            }
            // down
            if (current_loc.second<N-1 && abs(current_loc.first-i)>1) {
                if(map[i][current_loc.second+1] > map[current_loc.first][current_loc.second] &&
                   value[i][current_loc.second+1] < current_value+1){
                    value[i][current_loc.second+1] = current_value+1;
                    pq.push(make_pair(i, current_loc.second+1));
                }
            }
        }
    }
    /*
    while(pq.empty() != true){
        current_loc = pq.top();
        pq.pop();
        cout<<current_loc.first<<' '<<current_loc.second<<' '<<value[current_loc.first][current_loc.second]<<endl;
        if(max_val < value[current_loc.first][current_loc.second]){
            max_val = value[current_loc.first][current_loc.second];
        }
        current_value = value[current_loc.first][current_loc.second];
        for (int i=0; i<N; i++) {
            // left
            if(current_loc.first > 0 && abs(current_loc.second-i)>1){
                if(map[current_loc.first-1][i] > map[current_loc.first][current_loc.second] &&
                   value[current_loc.first-1][i] < current_value+1){
                    value[current_loc.first-1][i] = current_value+1;
                    pq.push(make_pair(current_loc.first-1, i));
                }
            }
            // right
            if (current_loc.first<N-1 && abs(current_loc.second-i)>1) {
                if(map[current_loc.first+1][i] > map[current_loc.first][current_loc.second] &&
                   value[current_loc.first+1][i] < current_value+1){
                    value[current_loc.first+1][i] = current_value+1;
                    pq.push(make_pair(current_loc.first+1, i));
                }
            }
            // up
            if (current_loc.second>0 && abs(current_loc.first-i)>1) {
                if(map[i][current_loc.second-1] > map[current_loc.first][current_loc.second] &&
                   value[i][current_loc.second-1] < current_value+1){
                    value[i][current_loc.second-1] = current_value+1;
                    pq.push(make_pair(i, current_loc.second-1));
                }
            }
            // down
            if (current_loc.second<N-1 && abs(current_loc.first-i)>1) {
                if(map[i][current_loc.second+1] > map[current_loc.first][current_loc.second] &&
                   value[i][current_loc.second+1] < current_value+1){
                    value[i][current_loc.second+1] = current_value+1;
                    pq.push(make_pair(i, current_loc.second+1));
                }
            }
        }
    }
     */
    cout<<max_val;
    return 0;
}
