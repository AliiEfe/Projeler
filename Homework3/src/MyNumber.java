public class MyNumber implements ProcessableValue {
    private double number;

    public MyNumber(double number) {
        this.number = number;
    }

    @Override
    public double getValue() {
        return number;
    }
}
