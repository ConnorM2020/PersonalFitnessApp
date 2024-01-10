public class test {

    // public static void rotate(int[] nums, int k) {
    //     System.out.println(nums.length + " Value of K: " + k);
    //     int[] newnums = new int[nums.length]; // take account of only specific values 
    //     System.out.println("Length of nums" + nums.length);
        
    //     for(int i = 0; i < k; i++) {
    //         if(i < k) {
    //             newnums[i] += newnums[k+i];
    //         }
    //     }

    //     for(int i = 0; i < newnums.length; i++ ) {
    //         System.err.println(newnums[i]);
    //     }
        
    // }
    
    public static void rotate(int[] nums, int k) {

        for(int i = 0; i < nums.length; i++ ) {
            if(i == nums.length-1) {
                System.err.println("Last element: " + nums[i]);

                
            }
        }
    }



    public static void main(String[] args) {
        int[] nums = {1,2,3,4,5,6,7};
        rotate(nums, 3);

    }
}
