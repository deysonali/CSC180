#include <stdio.h>

int swap(int *a, int *b);

int swap(int *a, int *b){
	int temp;
	temp = *a;
	*a  = *b;
	*b  = temp;
	return 1;
}

int main(void){
	int x = 400;
	int y = 5;
	swap(&x,&y);
	printf("%d \n",*&x);
	printf("%d \n",*&y);
	return 0;
}
