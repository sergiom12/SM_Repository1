import java.util.Scanner;

public class familyIncome {//start of class 
  public static void main (String [] args) {//start of main 
    Scanner input = new Scanner  (System.in);
    
  System.out.print ("How many family's members do you have?");
  int familyMembers = input.nextInt();
  
    //array
  double income[] = new double [familyMembers];
  for (int index = 0; index < income.length; index++){
    System.out.printf ("Please enter income of family member %d:",index+1);
  income[index] =input.nextDouble();
   }//end of array 
 
  //total
  double total = 0;
  for(int index = 0; index < income.length; index++){
  total += income[index];
  System.out.printf ("Income of Family %d is $%.2f\n", index+1, income[index]);
  }//end of total
  
  //maximum
  double maximum = income[0];
  for(int index = 0; index < income.length; index++){
  if(income[index]>maximum)
  maximum = income[index];
 }//end of maximus
  System.out.printf ("Maximum income $%.2f",maximum);
   
  double x = maximum * 0.1;
  System.out.printf ("\n10 percent of the maximum income: $%.2f", x);
  
  int p = 0;
  for(int index = 0; index < income.length; index++){
    if(income[index] < x)
      p++;
  }
  System.out.printf ("\nNumber of families whose income is below 10 percent:%d", p);
  
  
  
  
  }//end of main

}//end of class