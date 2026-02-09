public interface HashTable {
    void put(int key, int value);
    Integer get(int key);
    void remove(int key);
    boolean contains(int key);
    int size();
    int getLastOpProbes(); // Deneysel raporlama için gerekli [cite: 27]
}