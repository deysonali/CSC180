#include <stdio.h>

int anlboard( int *T, int sizeT );

int anlboard( int *T, int sizeT ){
	int i;
	if (sizeT !=9){
		return -1;
	}		
	for (i=0; i<=8; i++){
		if( (*&T[i]!=0) && (*&T[i]!=1) && (*&T[i]!=2) ){
			return -1;
		}
		}
		if( (*&T[0]==*&T[1]) && (*&T[1]==*&T[2]) && (*&T[2]==1)){
			return 1;
		}
		else if( (*&T[3]==*&T[4]) && (*&T[4]==*&T[5]) && (*&T[5]==1)){
			return 1;
		}
		else if ( (*&T[6]==*&T[7]) && (*&T[7]==*&T[8]) && (*&T[8]==1)){
			return 1;
		}
		else if ( (*&T[0]==*&T[3]) && (*&T[3]==*&T[6]) && (*&T[6]==1)){
			return 1;
		}
		else if ( (*&T[2]==*&T[5]) && (*&T[5]==*&T[8]) && (*&T[8]==1)){
			return 1;
		}
		else if ( (*&T[1]==*&T[4]) && (*&T[4]==*&T[7]) && (*&T[7]==1)){
			return 1;
		}
		else if ( (*&T[0]==*&T[4]) && (*&T[4]==*&T[8]) && (*&T[8]==1)){
			return 1;
		}
		else if ( (*&T[2]==*&T[4]) && (*&T[4]==*&T[6]) && (*&T[6]==1)){
			return 1;
		}
		 else if( (*&T[3]==*&T[4]) && (*&T[4]==*&T[5]) && (*&T[5]==2)){
                        return 2;
                }
                else if ( (*&T[6]==*&T[7]) && (*&T[7]==*&T[8]) && (*&T[8]==2)){
                        return 2;
                }
                else if ( (*&T[0]==*&T[3]) && (*&T[3]==*&T[6]) && (*&T[6]==2)){
                        return 2;
                }
                else if ( (*&T[2]==*&T[5]) && (*&T[5]==*&T[8]) && (*&T[8]==2)){
                        return 2;
                }
                else if ( (*&T[1]==*&T[4]) && (*&T[4]==*&T[7]) && (*&T[7]==2)){
                        return 2;
                }
                else if ( (*&T[0]==*&T[4]) && (*&T[4]==*&T[8]) && (*&T[8]==2)){
                        return 2;
                }
                else if ( (*&T[2]==*&T[4]) && (*&T[4]==*&T[6]) && (*&T[6]==2)){
                        return 2;
		}
		else if(*&T[0]==0 || *&T[1]==0 || *&T[2]==0 || *&T[3]==0 || *&T[4]==0 || *&T[5]==0 || *&T[6]==0 || *&T[7]==0 || *&T[8]==0){
			return 0;
		}
		else {
			return 3;
		}
	}

int main(void){
int A[9];
int i;
for (i=0;i<=8;i++){
	printf("Enter A[%d]\n", i);
	scanf("%d", &A[i]);
	}
int b;
b=anlboard(&A, 9);
printf("%d",b);
return 10;
}
