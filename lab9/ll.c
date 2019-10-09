#include <stdio.h>
#include <stdlib.h>
#include "ll.h"


int ll_add_to_head( llnode **head, int val) 
{
    llnode *old_head;
    if (head == NULL) 
    {
        return -1;
    }
    old_head = *head;

    *head = ( llnode *) malloc(sizeof( llnode));
    (*head) -> val = val;
    (*head) -> next = old_head;
    (*head) -> prev = NULL;	

    if(old_head != NULL){
	old_head->prev = (*head);
    }		
    return 0;
 }

int ll_add_to_tail(llnode **head, int val) 
{
    llnode *last = NULL;	
    if (head == NULL) 
    {
        return -1;
    }
    if (*head == NULL) 
    {
        *head = ( llnode *) malloc(sizeof( llnode));
        (*head) -> val = val;
        (*head) -> next = NULL;
	(*head) -> prev = last;
        return 0;
    } 
    else 
    { 
        return ll_add_to_tail(&((*head)->next), val);
	last = *head;
    }
}

int ll_print( llnode *p) 
{
    if (p==NULL) 
    {
        return 0;
    } 
    else 
    {
        printf("val = %d\n",p->val);
        return ll_print(p->next);
    }
}

int ll_free( llnode *p) 
{
    if (p==NULL) {
        return -1;
    } 
    else 
    {
        llnode *f=p->next;
        free(p);
        return ll_free(f);
    }
}

int ll_find_by_value(llnode *pList,int val)
{
    if(pList==NULL)
    {
        return -1;
    }
    else
    {
        if((pList->val)==val)
        {
            return 0;
        }
        else
        {
            return ll_find_by_value(pList->next, val);   
        }
    }
}

int ll_del_from_tail(llnode **ppList)
{
     llnode *temp = NULL;
    if (ppList == NULL)
    {
        return -1;
    }
    
     
 
    if ((*ppList)->next == NULL)
     {
         temp = *ppList;
         *ppList = NULL;
         free(temp);
	 free(temp->prev);
         return 0;
     }
    else
    {
        return ll_del_from_tail(&((*ppList)->next));
    }
}

int ll_del_from_head(llnode **ppList)
{
    struct llnode *temp = NULL;
    
    if (ppList == NULL)
    {
        return -1;
    }   
    
    temp = *ppList;
    *ppList = temp->next;
    (*ppList)->prev = NULL;
    free(temp);
    
    return 0;   

}

int ll_del_by_value(llnode **ppList,int val)
{
    struct llnode *temp = NULL;
    
    if(ppList == NULL)
    {
        return -1;
    } 
   
    if (((*ppList)->val) == val)
    {
        temp = *ppList;
        *ppList = temp->next;
	(*ppList)->prev = (temp->prev);
        free(temp);
        return 0;
    }
    else
    {
        return ll_del_by_value(&((*ppList)->next),val);
    }

}
int ll_insert_in_order(llnode **ppList,int val) 
{


    llnode *prev = NULL;
    llnode *curr = NULL;
    llnode *bef = NULL;

    if (ppList == NULL) 
    { 
        return -1; 
    }
    if (*ppList == NULL) 
    {
        return ll_add_to_head(ppList,val);
    }



    if ((*ppList) -> val > val) 
    {
        return ll_add_to_head(ppList,val);
    } 
    else 
    {
        bef = *ppList;
        curr = (*ppList)->next;
        while(curr != NULL) 
        {
            if (curr->val > val) 
            {
                break;
            } 
            else 
            {
                bef = curr;
                curr = bef->next;
            }
        }
        bef->next = (llnode *) malloc(sizeof(llnode));
        bef->next->val  = val;
        bef->next->next = curr;
	(bef->next)->prev = bef;
	curr->prev = bef->next;
        
        return 0;
    }
}

int ll_concat(llnode **pSrcA,llnode **pSrcB)
{
    if(pSrcA == NULL)
    {
        return -1;
    }
    if(pSrcB == NULL)
    {
        return -1;
    }
    
    if ((*pSrcA)->next == NULL)
    {
        (*pSrcA)->next = *pSrcB;
        (*pSrcB)->prev = *pSrcA;
        return 0;
    }
    else
    {
        return ll_concat(&((*pSrcA)->next),pSrcB);
    }
}

int ll_sort(llnode **ppList){
    int swapped = 1;
    struct llnode *address_start_list = NULL;
    int temp = 0;
    
    address_start_list = *ppList;

    if(ppList == NULL)
    {
        return -1;
    } 

    while (swapped)
    {
        swapped = 0;
        while((*ppList)->next != NULL)
        {
            if ((*ppList)->val > (*ppList)->next->val)
            {
                temp = (*ppList)->val;
                (*ppList)->val = (*ppList)->next->val;
                (*ppList)->next->val = temp;              
                *ppList = address_start_list;
                swapped = 1;
            }
            else
            {
                *ppList = (*ppList)->next;
               
            }
        }
    }
    *ppList = address_start_list;
    return 0;
}




