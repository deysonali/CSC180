#include<stdio.h>
float makeabs(float x);
float bsqrt(float x, float y);

float bsqrt(float x, float y){
float est;
est=x;

while(1){
	
	if (makeabs(est*est-x)<y){
	 return est;
	}
	else{
	est=0.5*(est+(x/est));
	}
}



}


float makeabs(float x){
if(x>0){
return x;
}
else if(x<0){
return -x;
}
else{
return 0;
}
}

int main (void){
int i;
for (i=0;i<10;i=i+1){
float sqrt;
sqrt = bsqrt((float)i,0.001);
   printf("The sqrt of %d is %f\n",i,sqrt);
}
return 0;
}
