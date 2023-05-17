/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <vector>
using namespace std;
class Solution {
public:
    int pairSum(ListNode* head) {
        vector<int> arr;
        while(head != NULL){
            arr.push_back(head->val);
            head=head->next;
        }
        int sol=0;
        int n=arr.size();
        int s=0,e=n-1;
        while(s<e){
            sol = max(sol,arr[s++]+arr[e--]);

        }
        return sol;
    }
};