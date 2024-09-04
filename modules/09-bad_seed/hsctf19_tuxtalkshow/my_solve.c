#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	time_t t;
	t = time((time_t*)0x0);
	srand(t);
	int temp,target=0,i, arr[6] = {0x79,0x12c97f,0x135f0f8,0x74acbc6,0x56c614e,0xffffffe2};
	for (i = 0; i < 6; i++){
		temp = rand();
		arr[0] -= (temp %10 -1);
	}
	for (i= 0 ; i < 6; i++){
		target += arr[i];
	}
	printf("%d\n", target);
	return 0;
}
