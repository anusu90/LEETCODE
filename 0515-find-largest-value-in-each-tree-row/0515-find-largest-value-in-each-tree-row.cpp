/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include<vector>
#include<iostream>
// #include<queue>

using namespace std;

class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        vector<int> sol;
        queue<TreeNode*> queue;
        queue.push(root);
        if(root == NULL){
            return sol;
        }
        while(!queue.empty()){
            int t = INT_MIN;
            int n = queue.size();
            for(int i=0;i<n;i++){
                TreeNode* node = queue.front();
                queue.pop();
                if(node->left){
                    queue.push(node->left);
                }
                if(node->right){
                    queue.push(node->right);
                }
              
                t = max(t,node->val);
             
                
            }
            sol.push_back(t);
        }
        return sol;
    }
};