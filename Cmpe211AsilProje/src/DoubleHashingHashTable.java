public class DoubleHashingHashTable implements HashTable {
    private int capacity;
    private Integer[] keys;
    private Integer[] values;
    private int size;
    private int lastOpProbes;
    private final Integer TOMBSTONE = Integer.MIN_VALUE;

    public DoubleHashingHashTable(int capacity) {
        this.capacity = capacity;
        this.keys = new Integer[capacity];
        this.values = new Integer[capacity];
        this.size = 0;
    }

    private int hash1(int key) { return Math.abs(key) % capacity; }

    // İkinci hash: Adım büyüklüğünü belirler. Asla 0 dönmemelidir.
    private int hash2(int key) {
        return 7 - (Math.abs(key) % 7);
    }

    @Override
    public void put(int key, int value) {
        lastOpProbes = 0;
        int h1 = hash1(key);
        int h2 = hash2(key);
        int i = h1;

        while (keys[i] != null && keys[i] != TOMBSTONE) {
            lastOpProbes++;
            if (keys[i].equals(key)) {
                values[i] = value;
                return;
            }
            i = (i + h2) % capacity;
        }
        lastOpProbes++;
        keys[i] = key;
        values[i] = value;
        size++;
    }

    @Override
    public Integer get(int key) {
        lastOpProbes = 0;
        int h1 = hash1(key);
        int h2 = hash2(key);
        int i = h1;

        while (keys[i] != null) {
            lastOpProbes++;
            if (keys[i].equals(key)) return values[i];
            i = (i + h2) % capacity;
        }
        return null;
    }

    @Override
    public void remove(int key) {
        int h1 = hash1(key);
        int h2 = hash2(key);
        int i = h1;

        while (keys[i] != null) {
            if (keys[i].equals(key)) {
                keys[i] = TOMBSTONE;
                values[i] = null;
                size--;
                return;
            }
            i = (i + h2) % capacity;
        }
    }

    @Override
    public boolean contains(int key) { return get(key) != null; }

    @Override
    public int size() { return size; }

    @Override
    public int getLastOpProbes() { return lastOpProbes; }
}