class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        int[] arr1 = new int[1001];
        int[] arr2 = new int[1001];
        for (int v : target) {
            ++arr1[v];
        }
        for(int v : arr ){
            ++arr2[v];
        }
            return Arrays.equals(arr1, arr2);
        }
}
