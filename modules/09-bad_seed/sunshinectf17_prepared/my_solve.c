#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
	time_t t;
	t = time((time_t*)0x0);
	srand(t);
	for (int i = 0;i < 0x32; i++){
		printf("%d\n", rand()%100);
	}

	return 0;
}

