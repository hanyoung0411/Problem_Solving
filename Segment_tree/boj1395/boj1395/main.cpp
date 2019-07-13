
//  Created by Hanyoung Yoo on 09/07/2019.
//  Copyright © 2019 Hanyoung Yoo. All rights reserved.


#include <iostream>
#include <vector>

using namespace std;

int init (vector<int> &a, vector<int> &tree,int node, int start, int end){
    if(start == end)return tree[node] = a[start];
    else return tree[node] = init(a, tree, node*2, start, (start+end)/2) +
        init(a, tree, node*2+1, (start+end)/2+1, end);
}

int sum (vector<int> &tree, int node, int start, int end, int left, int right){
    if (left > end || right < start) return 0;
    if (left <= start && end <= right) return tree[node];
    return sum(tree, node*2, start, (start+end)/2, left, right) +
    sum(tree, node*2+1, (start+end)/2+1, end, left, right);
}

void propagate(vector<int> &lazy, int node, int ns, int ne){
    if(lazy[node]){
        // 리프 노드가 아님
        if(node < start){
            lazy[node*2] ^= 1;
            lazy[node*2+1] ^= 1;
            
            // 왼쪽 자식과 오른쪽 자식의 결과로 자신의 결과 갱신
            int temp = 0;
            // 만약 왼쪽 자식 전체가 반전될 것이라면, 실질적인 값은 구간 크기 - 현재 값
            if(lazy[node*2]) temp += (ne-ns)/2 - arr[node*2];
            // 아니면 그냥 현재 값
            else temp += arr[node*2];
            // 오른쪽 자식도 마찬가지
            if(lazy[node*2+1]) temp += (ne-ns)/2 - arr[node*2+1];
            else temp += arr[node*2+1];
            
            arr[node] = temp;
        }
        // 리프 노드
        else arr[node] ^= 1;
        
        lazy[node] = false;
    }
}

// 구간 [s, e)의 상태를 반전시켜라
void turn(int s, int e, int node, int ns, int ne){
    propagate(node, ns, ne);
    if(e <= ns || ne <= s) return;
    if(s <= ns && ne <= e){
        // lazy 값을 반전시킴
        lazy[node] ^= 1;
        propagate(node, ns, ne);
        return;
    }
    int mid = (ns+ne)/2;
    turn(s, e, node*2, ns, mid);
    turn(s, e, node*2+1, mid, ne);
    arr[node] = arr[node*2] + arr[node*2+1];
}


int main(int argc, const char * argv[]) {
    int N,M;
    int O,S,T;
    vector<int> tree, bulb,lazy;
    cin>>N>>M;
    for(int i=0;i<N;i++)bulb.push_back(0);
    init(bulb,tree,1,0,N-1);
    for(int i=0;i<M;i++){
        cin>>O>>S>>T;
        if(O == 1){
            printf("%d\n",sum(tree, 1, 0, N-1, S, T));
        }
        else {
            for(int j=S;j<=T;j++)bulb[j] = !bulb[j];
        }
    }
    
    return 0;
}
