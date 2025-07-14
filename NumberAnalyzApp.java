import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.io.FileWriter;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class NumberAnalyzApp {

    public interface ProcessableValue {
        double getValue();
    }

    public static class MyNumber implements ProcessableValue {
        private double number;

        public MyNumber(double number) {
            this.number = number;
        }

        @Override
        public double getValue() {
            return number;
        }
    }

    public static class NumberCollector {
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

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            NumberCollector collector = new NumberCollector();


            JFrame frame = new JFrame("Number Analyzer");
            frame.setSize(400, 200);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            JTextField inputField = new JTextField(10);
            JButton addButton = new JButton("Sayı ekle");
            JButton calcButton = new JButton("Toplamı hesapla ve kaydet");
            JLabel resultLabel = new JLabel("Lütfen bir sayı girin.");

            addButton.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    try {
                        double value = Double.parseDouble(inputField.getText());
                        MyNumber num = new MyNumber(value);
                        collector.addNumber(num);
                        resultLabel.setText("Sayı eklendi. Toplam elemanı: " + collector.getCount());
                        inputField.setText("");
                    } catch (NumberFormatException ex) {
                        resultLabel.setText("Geçersiz sayı");
                    }
                }
            });

            calcButton.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    double sum = collector.calculateSum();
                    try {
                        collector.saveNumbersToFile("numbers.txt");
                        resultLabel.setText("Toplam: " + sum + ". Sayılar numbers.txt dosyasına kaydedildi.");
                    } catch (IOException ex) {
                        resultLabel.setText("Dosya kaydedilemedi: " + ex.getMessage());
                    }
                }
            });

            JPanel panel = new JPanel();
            panel.add(new JLabel("Sayı:"));
            panel.add(inputField);
            panel.add(addButton);
            panel.add(calcButton);
            panel.add(resultLabel);

            frame.add(panel);
            frame.setVisible(true);


        });


    }

}





