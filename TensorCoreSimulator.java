import java.util.Random;
import java.util.concurrent.Semaphore;
import java.util.concurrent.locks.ReentrantLock;

public class TensorCoreSimulator {

    static final int N = 1000;

    static int[][] A = new int[N][N];
    static int[][] B = new int[N][N];
    static int[][] C = new int[N][N];

    static long totalOps = 0;
    static ReentrantLock lock = new ReentrantLock();
    static Semaphore hardwareLimit = new Semaphore(2);

    public static void main(String[] args) throws Exception {

        System.out.println("=== Tensor Core Simulator (N=1000) ===");
        System.out.println("Generating data...");

        generateData();

        System.out.println("\n--- Part A: Sequential Execution ---");

        long start = System.currentTimeMillis();
        sequentialMultiply();
        long end = System.currentTimeMillis();

        System.out.println("Sequential Time: " + (end - start) + " ms");

        System.out.println("\n--- Part B: Parallel Execution (4 Threads) ---");

        start = System.currentTimeMillis();
        parallelMultiply(4, false);
        end = System.currentTimeMillis();

        System.out.println("Parallel Time: " + (end - start) + " ms");

        System.out.println("\n--- Part C & D: Parallel Execution with Audit (Billing) ---");

        totalOps = 0;

        start = System.currentTimeMillis();
        parallelMultiply(8, true);
        end = System.currentTimeMillis();

        System.out.println("Safe Parallel Time: " + (end - start) + " ms");

        long expected = (long) N * N * N;
        System.out.println("\nTotal Operations Logged: " + totalOps);
        System.out.println("Expected Operations: " + expected);
    }

    static void generateData() {
        Random r = new Random();
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++) {
                A[i][j] = r.nextInt(10);
                B[i][j] = r.nextInt(10);
            }
    }

    static void sequentialMultiply() {
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                for (int k = 0; k < N; k++)
                    C[i][j] += A[i][k] * B[k][j];
    }

    static void parallelMultiply(int threadCount, boolean audit) throws Exception {

        Thread[] threads = new Thread[threadCount];
        int rowsPerThread = N / threadCount;

        for (int i = 0; i < threadCount; i++) {
            int startRow = i * rowsPerThread;
            int endRow = (i == threadCount - 1) ? N : startRow + rowsPerThread;

            threads[i] = new Thread(new MatrixWorker(startRow, endRow, audit));
            threads[i].start();
        }

        for (Thread t : threads)
            t.join();
    }

    static class MatrixWorker implements Runnable {

        int startRow, endRow;
        boolean audit;

        MatrixWorker(int s, int e, boolean a) {
            startRow = s;
            endRow = e;
            audit = a;
        }

        public void run() {
            boolean permit=false;

            try {
                hardwareLimit.acquire();
                permit=true;

                for (int i = startRow; i < endRow; i++)
                    for (int j = 0; j < N; j++)
                        for (int k = 0; k < N; k++) {
                            C[i][j] += A[i][k] * B[k][j];

                            if (audit) {     // Part C
                                lock.lock();
                                try {
                                    totalOps++;
                                } finally {
                                    lock.unlock();
                                }
                            }
                        }

            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                hardwareLimit.release();
            }
        }
    }
}
