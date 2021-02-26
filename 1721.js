//  Swapping Nodes in a Linked List


var swapNodes = function (head, k) {
    let start = head;
    let index = 1;
    while (index++ < k) {
        start = start.next
    }
    let end = start;
    let current = head;

    while (end.next) {
        end = end.next;
        current = current.next;
    }

    [start.val, current.val] = [current.val, start.val]

    return head

};