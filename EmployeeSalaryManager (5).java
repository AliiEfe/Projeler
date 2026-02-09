import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class EmployeeSalaryManager {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Write number of employee: ");
        int numberOfEmployee =scanner.nextInt();
        scanner.nextLine();


        for(int i=0; i<numberOfEmployee; i++){
            System.out.print("Write name of employee: ");
            String name= scanner.nextLine();

            System.out.print("Write salary: ");
            double baseSalary= scanner.nextDouble();

            System.out.print("Write bonus percentage: ");
            double bonusPercentage= scanner.nextDouble();
            scanner.nextLine();

            Employee employee=new Employee(name,baseSalary,bonusPercentage);
            employee.displayInfo();
            System.out.println();
        }

        System.out.println("Total Employees Registered: "+ Employee.getEmployeeCount());
        scanner.close();

    }
}

class Employee {
    private String name;
    private double baseSalary;
    private double bonusPercentage;
    private double totalSalary;
    private static int employeeCount = 0;

    public Employee(String name, double baseSalary, double bonusPercentage) {
        this.name = name;
        this.baseSalary = baseSalary;
        this.bonusPercentage = bonusPercentage;
        calculateTotalSalary();
        employeeCount ++;
    }
    private void calculateTotalSalary(){
    this.totalSalary=baseSalary+(baseSalary*(bonusPercentage/100));
    }

    public String getPerformanceLevel(){
        String performance="Needs Improvement";
        if(totalSalary>=90000){
            performance= "Outstanding";
        } else if (totalSalary>=70000) {
            performance= "Excellent";
        } else if (totalSalary>=50000) {
            performance="Good";
        } else if (totalSalary>=30000) {
            performance = "Average";
        } else{
            performance="Needs Improvement";
        }
        return performance;
    }

    public void displayInfo(){
        System.out.println(name+ "'s Salary: "+ totalSalary);
        System.out.println("Performance Level: "+ getPerformanceLevel());
        displayMotivationMessage();
    }

    private void displayMotivationMessage(){
        String level= getPerformanceLevel();
        switch (level){
            case "Outstanding":
                System.out.println("You are one of the best");
                break;
            case "Excellent":
                System.out.println("You are doing very well");
                break;
            case "Good":
                System.out.println("You are good but you will be better");
                break;
            case "Average":
                System.out.println("Keep improving");
                break;
            case "Needs Improvement":
                System.out.println("You can do it");
                break;
        }
    }

    public static int getEmployeeCount(){
        return employeeCount;
    }
}
