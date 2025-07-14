//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Student {
    private static int studentCount = 0;

    public Student() {
        studentCount++;
    }

    public static int getStudentCount() {
        return studentCount;
    }

    public static void main(String[] args) {
        Student stu1 = new Student();
        Student stu2 = new Student();
        Student stu3 = new Student();

        System.out.println("Total students registered: " + Student.getStudentCount());


    }
}