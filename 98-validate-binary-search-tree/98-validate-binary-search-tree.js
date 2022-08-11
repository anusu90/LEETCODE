/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root,lower= -Infinity,upper = Infinity) {
    if(!root) return true
    if(root.val<=lower || root.val>=upper) return false
    return isValidBST(root.left,lower,root.val) && isValidBST(root.right,root.val,upper)
    
};