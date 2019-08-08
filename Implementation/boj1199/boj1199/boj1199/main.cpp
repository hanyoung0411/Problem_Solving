//
//  main.cpp
//  boj1199
//
//  Created by Hanyoung Yoo on 02/08/2019.
//  Copyright © 2019 Hanyoung Yoo. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

int N;
int vertex[1001][1001];
int num_of_vertex;
vector<int> path;

void traverse(int current_loc, int visited_vertex){
    if(visited_vertex == num_of_vertex && current_loc == 0){
        for(int i=0;i<path.size();i++){
            cout<<path[i]+1<<' ';
        }
        num_of_vertex = -1;
        return;
    }
    for(int i=0;i<N;i++){
        if(vertex[current_loc][i] > 0){
            vertex[current_loc][i]--;
            vertex[i][current_loc]--;
            path.push_back(i);
            traverse(i, visited_vertex + 2);
            if(num_of_vertex == -1)return;
            
            vertex[current_loc][i]++;
            vertex[i][current_loc]++;
            path.pop_back();
        }
    }
}

int main(int argc, const char * argv[]) {
    cin>>N;
    
    for(int i=0;i<N;i++){
        int vertex_for_edge = 0;
        for(int j=0;j<N;j++){
            cin>>vertex[i][j];
            num_of_vertex += vertex[i][j];
            vertex_for_edge += vertex[i][j];
        }
        if(vertex_for_edge % 2 == 1){
            cout<<-1;
            return 0;
        }
    }
    if (num_of_vertex == 0){
        cout<<-1;
        return 0;
    }
    path.push_back(0);
    traverse(0, 0);
    return 0;
}
