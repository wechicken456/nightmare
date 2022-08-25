
//	RUN THIS ON LINUX	

#include <malloc.h>
#include <stdio.h> 

void *my_hook(size_t size, const void *caller){
	puts("I am the hook!");
	fflush(stdout);
}

int main(){
	printf("%s\n", "asdf");
	__malloc_hook = my_hook;
	//printf("%7000s\n", "AAAA");  		=> won't print because the padding size has to be > 64000
	printf("%70000s\n", "BBBB");
	system("sh");
	return 0;

}
