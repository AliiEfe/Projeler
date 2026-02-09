import javax.swing.*;
import java.awt.event.*;
import java.io.IOException;

public class NumberAnalyzerGUI {
    private NumberCollector collector;

    public NumberAnalyzerGUI() {
        collector = new NumberCollector();

        JFrame frame = new JFrame("Number Analyzer");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JTextField inputField = new JTextField(10);
        JButton addButton = new JButton("Add Number");
        JButton calcButton = new JButton("Calculate Sum & Save");
        JLabel resultLabel = new JLabel("Please Add Number.");

        addButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    double value = Double.parseDouble(inputField.getText());
                    MyNumber num = new MyNumber(value);
                    collector.addNumber(num);
                    resultLabel.setText("Number added. Total items: " + collector.getCount());
                    inputField.setText("");
                } catch (NumberFormatException ex) {
                    resultLabel.setText("Invalid number. Please enter a valid number.");
                }
            }
        });

        calcButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                double sum = collector.calculateSum();
                try {
                    collector.saveNumbersToFile("numbers.txt");
                    resultLabel.setText("Sum: " + sum + ". Numbers saved to numbers.txt.");
                } catch (IOException ex) {
                    resultLabel.setText("File could not be saved: " + ex.getMessage());
                }
            }
        });

        JPanel panel = new JPanel();
        panel.add(new JLabel("Number:"));
        panel.add(inputField);
        panel.add(addButton);
        panel.add(calcButton);
        panel.add(resultLabel);

        frame.add(panel);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        new NumberAnalyzerGUI();
    }
}
