//  Created by Hanyoung Yoo on 19/08/2019.
//  Copyright © 2019 Hanyoung Yoo. All rights reserved.

#include <iostream>
using namespace std;

int store_fib[41][2];
int main() {
    int T,N;
    cin>>T;
    store_fib[0][0] = 1;
    store_fib[1][1] = 1;
    for(int i=2;i<41;i++){
        store_fib[i][0] = store_fib[i-1][0] + store_fib[i-2][0];
        store_fib[i][1] = store_fib[i-1][1] + store_fib[i-2][1];
    }
    for(int i=0;i<T;i++){
        cin>>N;
        cout<<store_fib[N][0]<<' '<<store_fib[N][1]<<'\n';
    }
    return 0;
}
