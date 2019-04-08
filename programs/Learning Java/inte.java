/* write a program takes integer number and prints if even or odd */
class inte {
    public static void main(String args[])
    {
    System.out.println("Parameter " + args[0]);
    int num=Integer.parseInt(args[0]);
    if (num == 1)
        {System.out.println("Entered number is odd/even");}
    else if (num%2==0){
        System.out.println("Entered number is even");
        }
    else{
        System.out.println("Entered number is odd");
        }
    }
}