#include<stdio.h>
#define Red 0
#define Green 1
#define Blue 2
#define inf 987654321
int get_minimum(int a, int b, int c){
	int min_val = a;
	if ( min_val > b )min_val = b;
	if ( min_val > c )min_val = c;
	return min_val;
}
int main(){
	int N;
	int store_cost[1000][3],cost[1000][3];
	int i,j;
	int result = inf;
	scanf("%d",&N);
	for(i=0;i<N;i++){
		int R,G,B;
		scanf("%d %d %d",&R, &G, &B);
		cost[i][Red] = R;
		cost[i][Green] = G;
		cost[i][Blue] = B;
		if (i == 0){
			store_cost[i][Red] = R;
			store_cost[i][Green] = G;
			store_cost[i][Blue] = B;
		}
	}

	for(j=1;j<N;j++){
		store_cost[j][Red] = store_cost[j-1][Green] < store_cost[j-1][Blue] ? store_cost[j-1][Green] + cost[j][Red] : store_cost[j-1][Blue] + cost[j][Red];
		store_cost[j][Green] = store_cost[j-1][Red] < store_cost[j-1][Blue] ? store_cost[j-1][Red] + cost[j][Green] : store_cost[j-1][Blue] + cost[j][Green];
		store_cost[j][Blue] = store_cost[j-1][Red] < store_cost[j-1][Green] ? store_cost[j-1][Red] + cost[j][Blue] : store_cost[j-1][Green] + cost[j][Blue];
		//printf("%d %d %d\n",store_cost[j][Red],store_cost[j][Green],store_cost[j][Blue]);
	}
	printf("%d",get_minimum(store_cost[N-1][Red],store_cost[N-1][Green],store_cost[N-1][Blue]));
	return 0;
}
