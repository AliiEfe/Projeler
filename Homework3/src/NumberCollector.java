import java.util.ArrayList;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class NumberCollector {
    private ArrayList<MyNumber> numbers;

    public NumberCollector() {
        numbers = new ArrayList<>();
    }

    public void addNumber(MyNumber num) {
        numbers.add(num);
    }

    public double calculateSum() {
        double sum = 0;
        for (MyNumber num : numbers) {
            sum += num.getValue();
        }
        return sum;
    }

    public ArrayList<Double> getAllNumbers() {
        ArrayList<Double> result = new ArrayList<>();
        for (MyNumber num : numbers) {
            result.add(num.getValue());
        }
        return result;
    }

    public void saveNumbersToFile(String filename) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
        for (Double value : getAllNumbers()) {
            writer.write(value.toString());
            writer.newLine();
        }
        writer.close();
    }

    public int getCount() {
        return numbers.size();
    }
}