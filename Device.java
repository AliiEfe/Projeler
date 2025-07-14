//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Device {
    String name;
    int memory;

    public Device(String name, int memory){
        this.name=name;
        this.memory=memory;
    }

    public Device(){
        name="Default";
        memory=4;

    }

    public void displayInfo(){
        System.out.println("Name: "+ name+ " Memory: "+ memory);
    }
    public static void main(String[] args) {
        Device dev1=new Device("Phone",4);
        Device dev2=new Device();

        dev1.displayInfo();
        dev2.displayInfo();


    }
}