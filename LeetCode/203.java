class Solution{
    public LinkNode removeElement(ListNode head,int val){
        while(head != null && head.val == val){
            head = head.next;
        }
        if(head == null){
            return head;
        }
        LinkNode temp = head;
        while (temp.next != null) {
            if(temp.next.val == val){
                temp.next = temp.next.next;
            }else{
                temp = temp.next;
            }
        }
        return head;
    }
}