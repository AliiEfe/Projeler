import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
abstract class Student {
    protected String name;
    protected double[][] grades = new double[3][2];

    public Student(String name) {
        this.name = name;
    }

    public void setGrades(Scanner scanner) {
        System.out.println("Enter grades for 3 courses");
        for (int num = 0; num < 3; num++) {
            System.out.printf("Course %d: ", num + 1);
            grades[num][0] = scanner.nextDouble();
            grades[num][1] = scanner.nextDouble();
        }
    }

    public double calculateAverage() {
        double total = 0;
        for (int a = 0; a < 3; a++) {
            total = total + ((grades[a][0] + grades[a][1]) / 2);
        }
        return total / 3;
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
        double average = calculateAverage();
        System.out.println("Average: " + average);
        System.out.println("Course category: " + getGradeCategory());
    }

    public abstract String getGradeCategory();

}

class UndergraduateStudent extends Student {
    public UndergraduateStudent(String name) {
        super(name);
    }

    @Override
    public String getGradeCategory() {
        double avg = calculateAverage();
        if (avg >= 85) {
            return "Excellent";
        } else if (avg >= 70) {
            return "Good";
        } else if (avg >= 50) {
            return "Average";
        } else {
            return "Fail";
        }
    }
}

class GraduateStudent extends Student {
    public GraduateStudent(String name) {
        super(name);
    }

    @Override
    public String getGradeCategory() {
        double avg = calculateAverage();
        if (avg >= 85) {
            return "Excellent";
        } else if (avg >= 70) {
            return "Good";
        } else if (avg >= 50) {
            return "Average";
        } else {
            return "Fail";
        }
    }
}

class InternationalStudent extends Student {
    public InternationalStudent(String name) {
        super(name);
    }

    @Override
    public String getGradeCategory() {
        double avg = calculateAverage();
        if (avg >= 85) {
            return "Excellent";
        } else if (avg >= 70) {
            return "Good";
        } else if (avg >= 50) {
            return "Average";
        } else {
            return "Fail";
        }
    }
}

public class CourseGradingSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter number of students:");
        int numStu = scanner.nextInt();
        scanner.nextLine();

        Student[] students = new Student[numStu];

        for (int i = 0; i < numStu; i++) {
            System.out.print("Enter student name:");
            String name = scanner.nextLine();

            System.out.print("Choose the student type (1) Undergraduate, (2) Graduate, (3) International ");
            int type = scanner.nextInt();

            Student student;
            switch (type) {
                case 1:
                    student = new UndergraduateStudent(name);
                    break;
                case 2:
                    student = new GraduateStudent(name);
                    break;
                case 3:
                    student = new InternationalStudent(name);
                    break;
                default:
                    System.out.println("Invalid type. Defaulting to Undergraduate.");
                    student = new UndergraduateStudent(name);
            }

            student.setGrades(scanner);
            students[i] = student;
            scanner.nextLine(); // consume newline
        }

        for (Student student : students) {
            student.displayInfo();
            System.out.println();
        }

        scanner.close();
    }
}


