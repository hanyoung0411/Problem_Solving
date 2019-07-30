//  Created by Hanyoung Yoo on 30/07/2019.
//  Copyright © 2019 Hanyoung Yoo. All rights reserved.

#include <iostream>
#include <cmath>

using namespace std;

int N;
long long K;
long long number_values[26];

long long not_parentheses(int digit){ // digit = 자릿수 , return val =  이 digit에 몇개가 있는 지 ㄴㄴ
    if(number_values[digit] != 0)return number_values[digit];
    int isfour;
    long long get_count;
    if(digit % 4 == 0) isfour = 1;
    else isfour = 0;
    // 00 이면 2^(digit-2)-1개 (4의 배수일 때)
    // 01 이면 not_parenthese(digit - 2)개
    // 10 이면 2^(digit-2)개
    // 11 이면 2^(digit-2)개
    get_count = pow(2,digit-2) - isfour;
    if(0 <= K && K < get_count ){
        cout<<"00";
    }
    else if(get_count <= K && K < get_count + not_parentheses(digit-2) ){
        cout<<"01";
        K -= get_count;
    }
    else if(get_count + not_parentheses(digit-2) <= K && K < get_count * 3 ){
        cout<<"10";
        K -= get_count + not_parentheses(digit-2);
    }
    else { // get_count * 3 <= K
        cout<<"11";
        K -= get_count * 3;
    }
    return 0;
}


int main() {
    cin>>N>>K;
    number_values[0] = 0;
    not_parentheses(N);
    return 0;
}
