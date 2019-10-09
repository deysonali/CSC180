#include<stdio.h>
#include<stdlib.h>

struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	};

typedef struct TreeNode TreeNode;

int add(TreeNode **root,int val){
	if(root == NULL) {
		return -1;
	}
	if(*root == NULL) {
		*root = (TreeNode *)malloc(sizeof(TreeNode));
		(*root)->val = val;
		return 0;
	}
	else if (*root != NULL){
		if(val < ((*root)->val)){
			add((&(*root)->left),val);
			return 0;
		}
		else if (val >((*root)->val)){
                        add((&(*root)->right),val);
                        return 0;
		}
		else if (val ==((*root)->val)){
                        return 0;
		}
int print(TreeNode *root, int val){
	if(root == NULL){
		return 0;
	}
	else {
		print((root.left),val);
		printf("%d\n",(root.val));
		print((root.right),val);
	}

		


	
