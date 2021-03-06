// 104. Maximum Depth of Binary Tree

var maxDepth = function (root) {
    if (!root) return 0
    if (root.left == null && root.right == null) return 1; // This line is actually not needed to find the depth of tree
    let leftD = maxDepth(root.left) + 1;
    let rightD = maxDepth(root.right) + 1;
    return Math.max(leftD, rightD);

};