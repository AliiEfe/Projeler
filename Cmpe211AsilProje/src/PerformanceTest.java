import java.util.Random;

public class PerformanceTest {
    public static void main(String[] args) {
        int capacity = 100003; // Asal sayı seçimi Double Hashing için kritiktir.
        double[] loadFactors = {0.5, 0.8, 0.9}; // İstenen doluluk oranları [cite: 23]
        Random rand = new Random();

        for (double alpha : loadFactors) {
            System.out.println("\n=== TEST: Doluluk Oranı " + alpha + " ===");

            HashTable lpTable = new LinearProbingHashTable(capacity);
            HashTable dhTable = new DoubleHashingHashTable(capacity);
            int elements = (int) (capacity * alpha);

            // 1. İş Yükü: Rastgele Anahtarlar [cite: 24]
            long startTime = System.nanoTime();
            long totalProbes = 0;
            for (int i = 0; i < elements; i++) {
                int key = rand.nextInt(1000000);
                dhTable.put(key, i);
                totalProbes += dhTable.getLastOpProbes();
            }
            long endTime = System.nanoTime();

            System.out.println("Double Hashing -> Süre: " + (endTime - startTime) / 1_000_000.0 +
                    " ms, Ort. Probe: " + (double)totalProbes/elements);

            startTime = System.nanoTime();
            totalProbes = 0;
            for (int i = 0; i < elements; i++) {
                int key = rand.nextInt(1000000);
                lpTable.put(key, i);
                totalProbes += lpTable.getLastOpProbes();
            }
            endTime = System.nanoTime();

            System.out.println("Linear Probing -> Süre: " + (endTime - startTime) / 1_000_000.0 +
                    " ms, Ort. Probe: " + (double)totalProbes/elements);
        }

        // --- BONUS: Failure Mode / Clustering Testi [cite: 31, 33] ---
        System.out.println("\n=== BONUS: Kümelenmiş Veri (Primary Clustering) Analizi ===");
        HashTable lpBonus = new LinearProbingHashTable(capacity);
        HashTable dhBonus = new DoubleHashingHashTable(capacity);

        // Ardışık anahtarlar ekleyerek Linear Probing'i zorluyoruz
        long start = System.nanoTime();
        for(int i=0; i<80000; i++) lpBonus.put(5000 + i, i);
        System.out.println("Linear Probing (Kümelenmiş) Süre: " + (System.nanoTime()-start)/1_000_000.0 + " ms");

        start = System.nanoTime();
        for(int i=0; i<80000; i++) dhBonus.put(5000 + i, i);
        System.out.println("Double Hashing (Kümelenmiş) Süre: " + (System.nanoTime()-start)/1_000_000.0 + " ms");
    }
}
