import numpy as np
import matplotlib.pyplot as plt


def simulate_factor_graph(
    phi0: float,
    u: float,
    v_p: float,
    sigma_u: float,
    sigma_p: float,
    dt: float,
    t_end: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    n_steps = int(t_end / dt)
    phi_values = np.zeros(n_steps)
    epsilon_u_values = np.zeros(n_steps)
    epsilon_p_values = np.zeros(n_steps)
    
    phi = phi0
    error_p = 0.0
    error_u = 0.0
    
    for step in range(n_steps):
        phi_values[step] = phi
        epsilon_p_values[step] = error_p
        epsilon_u_values[step] = error_u
        
        # 1. phiの更新
        phi = phi + dt * (-error_p + error_u * (2.0 * phi))
        
        # 2. error_pの更新
        error_p = error_p + dt * (phi - v_p - sigma_p * error_p)
        
        # 3. error_uの更新
        error_u = error_u + dt * (u - phi**2 - sigma_u * error_u)
    
    times = np.arange(dt, t_end + 0.5 * dt, dt)
    return times, phi_values, epsilon_p_values, epsilon_u_values


def main() -> None:
    v_p = 3.0
    sigma_p = 1.0
    sigma_u = 1.0
    u = 2.0
    
    phi0 = v_p
    dt = 0.01
    t_end = 5.0
    
    times, phi_values, epsilon_p_values, epsilon_u_values = simulate_factor_graph(
        phi0, u, v_p, sigma_u, sigma_p, dt, t_end
    )
    
    plt.figure(figsize=(7, 4.5))
    plt.plot(times, phi_values, "k")
    plt.plot(times, epsilon_p_values, "k--")
    plt.plot(times, epsilon_u_values, "k:")
    plt.xlabel("Time")
    plt.ylabel("Activity")
    plt.legend([r"$\phi$", r"$\varepsilon_p$", r"$\varepsilon_u$"])
    plt.axis([0, t_end, -2, 3.5])
    plt.tight_layout()
    plt.savefig("exercise3_factor_graph_plot.png", dpi=200)
    plt.show()


if __name__ == "__main__":
    main()
