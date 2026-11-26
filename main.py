import time, random
from multiprocessing import Pool, cpu_count

def hitung_titik(n):
    random.seed()
    dalam = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            dalam += 1
    return dalam

def serial(N):
    return 4 * hitung_titik(N) / N

def paralel(N, p):
    bagian = [N // p] * p
    with Pool(p) as pool:
        hasil = pool.map(hitung_titik, bagian)
    return 4 * sum(hasil) / N

if __name__ == "__main__":
    N = 20_000_000
    t0 = time.time(); pi_s = serial(N); t_s = time.time() - t0
    print(f"Serial     : pi={pi_s:.6f}, waktu={t_s:.2f}s")

    for p in [2, 4, cpu_count()]:
        t0 = time.time(); pi_p = paralel(N, p); t_p = time.time() - t0
        print(f"Paralel P={p}: pi={pi_p:.6f}, waktu={t_p:.2f}s, "
              f"speedup={t_s/t_p:.2f}, efisiensi={t_s/t_p/p:.2f}")
