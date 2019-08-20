//  Created by Hanyoung Yoo on 19/08/2019.
//  Copyright © 2019 Hanyoung Yoo. All rights reserved.

#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int N;
    int tile[31];
    cin >> N;
    for(int i=0;i<31;i++){
        if (i % 2 == 1)tile[i] = 0;
    }
    tile[2] = 3;
    
    return 0;
}
