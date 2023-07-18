import java.util.Scanner;

public class Watermelon{
   
    public static Boolean check_even(int in){
        if((in%2 == 0) && (in/2 >= 2)){
            return true;
        }
        
        return false;
    }
    
    public static void main(String args[]){

        Scanner myObj = new Scanner(System.in);
        String numberIn = myObj.nextLine();

        if(check_even(Integer.parseInt(numberIn))){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
        
    }
}