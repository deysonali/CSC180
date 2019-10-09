#include <stdio.h>
#include "ll.h"

int main(void) {
   llnode *root1 = NULL;
   llnode *root = NULL;	
   int r=0;
   int i=0;
   int c=0;
   int c1=0;
   int c2=0;
    
   printf("List A\n");
   r=ll_add_to_tail(&root1,100);
   r=ll_add_to_tail(&root1,200);
   r=ll_add_to_tail(&root1,300); 
   for(i=0;i<10;i=i+1){
      r=ll_add_to_tail(&root1,i*100);
   }
  	
   r=ll_print(root1);
  
   
   printf("List B\n");
   root = NULL;	
   c=ll_add_to_tail(&root,100);
   c=ll_add_to_tail(&root,200);
   c=ll_add_to_tail(&root,300);
   for(i=0;i<10;i=i+1){
     c=ll_add_to_head(&root,i*100);
   }
   c=ll_concat(&root1, &root); 	
   c=ll_print(root1);		
   c=ll_free(root);
   r=ll_free(root1);
   return 0;
}
