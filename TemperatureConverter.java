//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class TemperatureConverter{
    public static double convert(double celsius){
        return (celsius*9/5) +32;
    }
    public static double convert(int fahrenheit){
        return (fahrenheit-32)*5/9.0;
    }
    public static void main(String[] args) {
        double fahrenheit = TemperatureConverter.convert(100.0);
        System.out.println("100 C = "+ fahrenheit+ "F");
        double celcius= TemperatureConverter.convert(50);
        System.out.println("50F = "+ celcius+ "C");

    }
}