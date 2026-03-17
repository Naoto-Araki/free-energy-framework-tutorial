import numpy as np
import matplotlib.pyplot as plt


def dphi(phi: float, u: float, v_p: float, sigma_u: float, sigma_p: float) -> float:
    prior_term = (v_p - phi) / sigma_p
    sensory_term = ((u - phi**2) / sigma_u) * (2.0 * phi)
    return prior_term + sensory_term


def simulate_phi(
    phi0: float,
    u: float,
    v_p: float,
    sigma_u: float,
    sigma_p: float,
    dt: float,
    t_end: float,
) -> tuple[np.ndarray, np.ndarray]:
    n_steps = int(t_end / dt)
    phi_values = np.zeros(n_steps)
    phi_values[0] = phi0

    for index in range(1, n_steps):
        phi_prev = phi_values[index - 1]
        phi_values[index] = phi_prev + dt * dphi(phi_prev, u, v_p, sigma_u, sigma_p)

    times = np.arange(dt, t_end + 0.5 * dt, dt)
    return times, phi_values


def main() -> None:
    v_p = 3.0
    sigma_p = 1.0
    sigma_u = 1.0
    u = 2.0

    phi0 = v_p
    dt = 0.01
    t_end = 5.0

    times, phi_values = simulate_phi(phi0, u, v_p, sigma_u, sigma_p, dt, t_end)

    plt.figure(figsize=(7, 4.5))
    plt.plot(times, phi_values, "k")
    plt.xlabel("Time")
    plt.ylabel("\\phi")
    plt.axis([0.0, t_end, -2.0, 3.5])
    plt.tight_layout()
    plt.savefig("exercise2_phi_trajectory.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()