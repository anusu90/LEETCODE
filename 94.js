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
 * @return {number[]}
 */



var inorderTraversal = function (root) {

    let num = []

    function inorderTraversal2(root) {

        if (!root) return []
        if (!root.left) {
            num.push(root.val)
            inorderTraversal2(root.right)
        }
        if (root.left) {
            inorderTraversal2(root.left)
            num.push(root.val)
            inorderTraversal2(root.right)
        }
        return num
    }

    return inorderTraversal2(root)

};