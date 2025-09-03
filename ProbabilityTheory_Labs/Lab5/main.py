import random
import math

# Інтенсивності переходів між станами
transitions = {
    1: [(2, 2), (3, 1)],
    2: [(4, 1.5)],
    3: [(2, 1), (4, 0.5)],
    4: [(5, 2)],
    5: [(1, 1), (3, 0.5)],
}

current_state = 1
state_times = {state: 0.0 for state in range(1, 6)}
T = 0.0
N_TRANSITIONS = 1000

for _ in range(N_TRANSITIONS):
    outgoing = transitions[current_state]
    next_states = []

    for target_state, intensity in outgoing:
        r = random.uniform(0, 1)
        tau = -math.log(r) / intensity
        next_states.append((tau, target_state))

    tau_min, next_state = min(next_states)
    state_times[current_state] += tau_min
    T += tau_min
    current_state = next_state

# --- Обчислення стаціонарних ймовірностей ---

experimental_probs = {state: state_times[state] / T for state in state_times}

# --- Вивід результатів ---

print("=" * 45)
print("Результати моделювання неперервного Марківського процесу")
print("=" * 45)
print(f"Загальний модельний час: T = {T:.5f} одиниць\n")

print("Час перебування в кожному стані:")
for state in sorted(state_times):
    print(f"  Стан {state}: {state_times[state]:.5f}")

print("\nЕкспериментальні стаціонарні ймовірності:")
for state in sorted(experimental_probs):
    print(f"  p{state} = {experimental_probs[state]:.5f}")
print("=" * 45)
