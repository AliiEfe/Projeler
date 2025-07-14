import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Swing Layout");
        JButton buttonA = new JButton("Button A");
        JButton buttonB = new JButton("Button B");

        JPanel panel = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 0));
        panel.add(buttonA);
        panel.add(buttonB);

        buttonA.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.out.println("A Clicked");
            }
        });

        buttonB.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.out.println("B Clicked");
            }
        });

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(panel);
        frame.setSize(300, 100);
        frame.setVisible(true);

    }
}