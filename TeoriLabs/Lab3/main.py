import numpy as npfrom scipy.integrate import dblquad# Параметри пірамідиa, b, h = 1.0, 1.0, 3N = 100000# Генерація випадкових величинdef generate_pyramid(a, b, N):    r1 = np.random.rand(N)    X = a * (1 - np.sqrt(1 - r1))    r2 = np.random.rand(N)    Y = b * (1 - X/a) * r2    return X, YX, Y = generate_pyramid(a, b, N)# Функція щільності розподілуdef f_xy(x, y):    return 3 / (a * b * h) * (1 - x / a - y / b)# Математичні сподівання (обчислені через середнє значення вибірки)m_x = np.mean(X)m_y = np.mean(Y)sigma_x, sigma_y = np.std(X, ddof=1), np.std(Y, ddof=1)cov = np.cov(X, Y, ddof=1)[0,1]rho = cov / (sigma_x * sigma_y)# Теоретичні значенняtheoretical_mx = a/8theoretical_my = b/8theoretical_sigma_x = a / np.sqrt(18)theoretical_sigma_y = b / np.sqrt(18)theoretical_rho = -0.5# Виведення результатівprint("3.1 Математичні очікування:")print(f"  m_x = {m_x:.4f} (теоретичне: {theoretical_mx:.4f})")print(f"  m_y = {m_y:.4f} (теоретичне: {theoretical_my:.4f})\n")print("3.2 Середньоквадратичні відхилення:")print(f"  σ_x = {sigma_x:.4f} (теоретичне: {theoretical_sigma_x:.4f})")print(f"  σ_y = {sigma_y:.4f} (теоретичне: {theoretical_sigma_y:.4f})\n")print("3.3 Коефіцієнт кореляції:")print(f"  ρ = {rho:.4f} (теоретичне: {theoretical_rho:.4f})")