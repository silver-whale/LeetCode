public class mergeList {

     class ListNode {
          int val;
          ListNode next;
          ListNode() {}
          ListNode(int val) { this.val = val; }
          ListNode(int val, ListNode next) { this.val = val; this.next = next; }
     }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode mergeList = new ListNode();

        return mergeList;
    }

    public static void main(String[] args){

    }
}

class mergeSort_TD{
    private static int[] sorted;

    // Call merge_sort(int[] a, int left, int right)
    public static void merge_sort(int[] a){
        sorted = new int[a.length];
        merge_sort(a, 0, a.length-1);
        sorted = null;
    }

    // For Recursion
    private static void merge_sort(int[] a, int left, int right){
        if(left==right) return;

        int mid = (left+right) / 2;

        merge_sort(a, left, mid);
        merge_sort(a, mid+1, right);

        merge(a, left, mid, right);
    }

    private static void merge(int[] a, int left, int mid, int right){
        int l = left;
        int r = mid + 1;
        int idx = left;

        while(l<=mid && r<=right){
            if(a[l] <= a[r]){
                sorted[idx] = a[l];
                idx++;
                l++;
            }
            else{
                sorted[idx] = a[r];
                idx++;
                r++;
            }
        }
        // l is finished, out of range
        if(l>mid){
            while(r<=right){
                sorted[idx] = a[r];
                idx++;
                r++;
            }
        }
        else{
            while(l<=mid){
                sorted[idx] = a[l];
                idx++;
                l++;
            }
        }

        for(int i=left; i<=right; i++){
            a[i] = sorted[i];
        }
    }
}

class mergeSort_BU{
    private static int[] sorted;

    // Call merge_sort(int[] a, int left, int right)
    public static void merge_sort(int[] a){
        sorted = new int[a.length];
        merge_sort(a, 0, a.length-1);
        sorted = null;
    }

    private static void merge_sort(int[] a, int left, int right) {
        for (int size = 1; size <= right; size += size) {
            for (int l = 0; l <= right - size; l += (2 * size)) {
                int low = l;
                int mid = l + size - 1;
                int high = Math.min(l + (2 * size) - 1, right);
                merge(a, low, mid, high);
            }
        }
    }

    private static void merge(int[] a, int left, int mid, int right){
        int l = left;
        int r = mid + 1;
        int idx = left;

        while(l<=mid && r<=right){
            if(a[l] <= a[r]){
                sorted[idx] = a[l];
                idx++;
                l++;
            }
            else{
                sorted[idx] = a[r];
                idx++;
                r++;
            }
        }
        // l is finished, out of range
        if(l>mid){
            while(r<=right){
                sorted[idx] = a[r];
                idx++;
                r++;
            }
        }
        else{
            while(l<=mid){
                sorted[idx] = a[l];
                idx++;
                l++;
            }
        }

        for(int i=left; i<=right; i++){
            a[i] = sorted[i];
        }
    }
}
