public class LinearProbingHashTable implements HashTable {
    private int capacity;
    private Integer[] keys;
    private Integer[] values;
    private int size;
    private int lastOpProbes;
    private final Integer TOMBSTONE = Integer.MIN_VALUE;

    public LinearProbingHashTable(int capacity) {
        this.capacity = capacity;
        this.keys = new Integer[capacity];
        this.values = new Integer[capacity];
        this.size = 0;
    }

    private int hash(int key) { return Math.abs(key) % capacity; }

    @Override
    public void put(int key, int value) {
        lastOpProbes = 0;
        int i = hash(key);
        while (keys[i] != null && keys[i] != TOMBSTONE) {
            lastOpProbes++;
            if (keys[i].equals(key)) {
                values[i] = value;
                return;
            }
            i = (i + 1) % capacity;
        }
        lastOpProbes++;
        keys[i] = key;
        values[i] = value;
        size++;
    }

    @Override
    public Integer get(int key) {
        lastOpProbes = 0;
        int i = hash(key);
        while (keys[i] != null) {
            lastOpProbes++;
            if (keys[i].equals(key)) return values[i];
            i = (i + 1) % capacity;
        }
        return null;
    }

    @Override
    public void remove(int key) {
        int i = hash(key);
        while (keys[i] != null) {
            if (keys[i].equals(key)) {
                keys[i] = TOMBSTONE;
                values[i] = null;
                size--;
                return;
            }
            i = (i + 1) % capacity;
        }
    }

    @Override
    public boolean contains(int key) { return get(key) != null; }

    @Override
    public int size() { return size; }

    @Override
    public int getLastOpProbes() { return lastOpProbes; }
}