/*take a choice from a,b,c,d,e,f and print one, two,
         three, four, five, six  */

class switchcaseprogram {
    public static void main(String args[])
        {
            System.out.println("provided argument is "+args[0]);
            switch (Integer.parseInt(args[0]))
            { 
            case 1: 
            System.out.println("a=1"); 
            break; 
                
            case 2:
            System.out.println("b=2"); 
            break; 

            case 3:
            System.out.println("c=3"); 
            break; 

            case 4:
            System.out.println("d=4"); 
            break; 

            case 5:
            System.out.println("e=5"); 
            break; 

        } 
    }
}
          
    