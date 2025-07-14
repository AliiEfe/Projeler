//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
class ItemSwapperT<T> {
    private T item1;
    private T item2;

    public ItemSwapperT(T item1, T item2) {
        this.item1 = item1;
        this.item2 = item2;

    }

    public void swapItems() {
        T ta = item1;
        item1 = item2;
        item2 = ta;

    }

    public void displayItems() {
        System.out.println("Item 1: " + item1 + ", Item 2: " + item2);
    }
}

public class TestItemSwapper {
    public static void main(String[] args) {
        ItemSwapperT<Integer> intSwapper = new ItemSwapperT<>(10, 20);
        intSwapper.displayItems();
        intSwapper.swapItems();
        intSwapper.displayItems();

        ItemSwapperT<String> stringSwapper = new ItemSwapperT<>("Hello", "World");
        stringSwapper.displayItems();
        stringSwapper.swapItems();
        stringSwapper.displayItems();
    }
}
