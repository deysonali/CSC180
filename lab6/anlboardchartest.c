#include <stdio.h>

int anlboard( char *T, int sizeT );

int anlboard( char *T, int sizeT ){
	int i;
	if (sizeT !=9){
		return -1;
	}		
	for (i=0; i<=8; i++){
		if( (*&T[i]!='X') && (*&T[i]!='O') && (*&T[i]!='-') ){
			return -1;
		}
		}
		if( (*&T[0]==*&T[1]) && (*&T[1]==*&T[2]) && (*&T[2]=='X')){
			return 1;
		}
		else if( (*&T[3]==*&T[4]) && (*&T[4]==*&T[5]) && (*&T[5]=='X')){
			return 1;
		}
		else if ( (*&T[6]==*&T[7]) && (*&T[7]==*&T[8]) && (*&T[8]=='X')){
			return 1;
		}
		else if ( (*&T[0]==*&T[3]) && (*&T[3]==*&T[6]) && (*&T[6]=='X')){
			return 1;
		}
		else if ( (*&T[2]==*&T[5]) && (*&T[5]==*&T[8]) && (*&T[8]=='X')){
			return 1;
		}
		else if ( (*&T[1]==*&T[4]) && (*&T[4]==*&T[7]) && (*&T[7]=='X')){
			return 1;
		}
		else if ( (*&T[0]==*&T[4]) && (*&T[4]==*&T[8]) && (*&T[8]=='X')){
			return 1;
		}
		else if ( (*&T[2]==*&T[4]) && (*&T[4]==*&T[6]) && (*&T[6]=='X')){
			return 1;
		}
		 else if( (*&T[3]==*&T[4]) && (*&T[4]==*&T[5]) && (*&T[5]=='O')){
                        return 2;
                }
                else if ( (*&T[6]==*&T[7]) && (*&T[7]==*&T[8]) && (*&T[8]=='O')){
                        return 2;
                }
                else if ( (*&T[0]==*&T[3]) && (*&T[3]==*&T[6]) && (*&T[6]=='O')){
                        return 2;
                }
                else if ( (*&T[2]==*&T[5]) && (*&T[5]==*&T[8]) && (*&T[8]=='O')){
                        return 2;
                }
                else if ( (*&T[1]==*&T[4]) && (*&T[4]==*&T[7]) && (*&T[7]=='O')){
                        return 2;
                }
                else if ( (*&T[0]==*&T[4]) && (*&T[4]==*&T[8]) && (*&T[8]=='O')){
                        return 2;
                }
                else if ( (*&T[2]==*&T[4]) && (*&T[4]==*&T[6]) && (*&T[6]=='O')){
                        return 2;
		}
		else if(*&T[0]=='-' || *&T[1]=='-' || *&T[2]=='-' || *&T[3]=='-' || *&T[4]=='-' || *&T[5]=='-' || *&T[6]=='-' || *&T[7]=='-' || *&T[8]=='-'){
			return 0;
		}
		else {
			return 3;
		}
	}

int main(void){
char A[9];

A[0]='X';
A[1]='X';
A[2]='X';
A[3]='-';
A[4]='-';
A[5]='-';
A[6]='-';
A[7]='-';
A[8]='-';	
int b;
b=anlboard(&A, 9);
printf("%d",b);
return 10;
}
