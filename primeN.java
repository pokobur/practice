class primeN{
    public static void main(String[]args){
        for(int i=1000000; i<=1010000; i++){
            for(int j=2; (i%j!=0 && j<i)||j==i; j++){
                if(j == i){
                    System.out.println(i);
                }
            }
        }
    }
}
