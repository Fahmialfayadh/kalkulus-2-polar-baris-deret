import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Buat folder output jika belum ada
output_dir = "/home/data/kuliah/rka/kalkulus2/kalkulus-2-polar-baris-deret/modul/images"
os.makedirs(output_dir, exist_ok=True)

# Set style agar premium dan modern
plt.rcParams['figure.facecolor'] = '#1e1e24'
plt.rcParams['axes.facecolor'] = '#1e1e24'
plt.rcParams['text.color'] = '#f8f9fa'
plt.rcParams['axes.labelcolor'] = '#e9ecef'
plt.rcParams['xtick.color'] = '#adb5bd'
plt.rcParams['ytick.color'] = '#adb5bd'
plt.rcParams['grid.color'] = '#495057'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.5
plt.rcParams['font.size'] = 11

def generate_modul_1():
    # --- Plot 1: y = 5x dan y = x^2 ---
    fig, ax = plt.subplots(figsize=(6, 5), dpi=150)
    x = np.linspace(-1, 6, 400)
    y1 = 5 * x
    y2 = x ** 2
    ax.plot(x, y1, label='$y = 5x$ (Atas)', color='#00d2ff', linewidth=2.5)
    ax.plot(x, y2, label='$y = x^2$ (Bawah)', color='#ff007f', linewidth=2.5)
    x_fill = np.linspace(0, 5, 200)
    ax.fill_between(x_fill, 5 * x_fill, x_fill**2, color='#00d2ff', alpha=0.15, label='Daerah Luas (L)')
    ax.scatter([0, 5], [0, 25], color='#ffca28', s=60, zorder=5, edgecolors='black')
    ax.annotate('(0, 0)', (0, 0), textcoords="offset points", xytext=(-15,-15), ha='center', color='#ffca28', fontweight='bold')
    ax.annotate('(5, 25)', (5, 25), textcoords="offset points", xytext=(15,10), ha='center', color='#ffca28', fontweight='bold')
    ax.set_title('Daerah antara $y = 5x$ dan $y = x^2$', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.legend(facecolor='#2b2d42', edgecolor='#495057')
    ax.set_xlim(-1, 6)
    ax.set_ylim(-5, 30)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '01_luas_kurva_ex1.png'), facecolor='#1e1e24')
    plt.close()

    # --- Plot 2: y = 2x+3 dan y = x^2 ---
    fig, ax = plt.subplots(figsize=(6, 5), dpi=150)
    x = np.linspace(-2, 4, 400)
    y1 = 2 * x + 3
    y2 = x ** 2
    ax.plot(x, y1, label='$y = 2x + 3$ (Atas)', color='#00d2ff', linewidth=2.5)
    ax.plot(x, y2, label='$y = x^2$ (Bawah)', color='#ff007f', linewidth=2.5)
    x_fill = np.linspace(-1, 3, 200)
    ax.fill_between(x_fill, 2 * x_fill + 3, x_fill**2, color='#00d2ff', alpha=0.15, label='Daerah Luas (L)')
    ax.scatter([-1, 3], [1, 9], color='#ffca28', s=60, zorder=5, edgecolors='black')
    ax.annotate('(-1, 1)', (-1, 1), textcoords="offset points", xytext=(-15,-15), ha='center', color='#ffca28', fontweight='bold')
    ax.annotate('(3, 9)', (3, 9), textcoords="offset points", xytext=(15,10), ha='center', color='#ffca28', fontweight='bold')
    ax.set_title('Daerah antara $y = 2x + 3$ dan $y = x^2$', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.legend(facecolor='#2b2d42', edgecolor='#495057')
    ax.set_xlim(-2, 4)
    ax.set_ylim(-2, 12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '01_luas_kurva_ex2.png'), facecolor='#1e1e24')
    plt.close()

def generate_modul_2():
    fig = plt.figure(figsize=(7, 6), dpi=150)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#1e1e24')
    fig.patch.set_facecolor('#1e1e24')
    x = np.linspace(0, 1, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    X, THETA = np.meshgrid(x, theta)
    R = X
    Y = R * np.cos(THETA)
    Z = R * np.sin(THETA)
    ax.plot_surface(X, Y, Z, cmap='cool', alpha=0.6, edgecolor='none')
    ax.plot(x, x, np.zeros_like(x), color='#ff007f', linewidth=3)
    ax.set_title('Permukaan Benda Putar $y = x$ terhadap Sumbu-X', fontsize=12, fontweight='bold', color='#ffffff')
    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.grid(False)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '02_luas_putar_ex1.png'), facecolor='#1e1e24')
    plt.close()

    fig = plt.figure(figsize=(7, 6), dpi=150)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#1e1e24')
    fig.patch.set_facecolor('#1e1e24')
    x = np.linspace(1, 4, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    X, THETA = np.meshgrid(x, theta)
    R = np.sqrt(X)
    Y = R * np.cos(THETA)
    Z = R * np.sin(THETA)
    ax.plot_surface(X, Y, Z, cmap='winter', alpha=0.6, edgecolor='none')
    ax.plot(x, np.sqrt(x), np.zeros_like(x), color='#ff007f', linewidth=3)
    ax.set_title('Permukaan Benda Putar $y = \\sqrt{x}$ terhadap Sumbu-X', fontsize=12, fontweight='bold', color='#ffffff')
    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.grid(False)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '02_luas_putar_ex2.png'), facecolor='#1e1e24')
    plt.close()

def generate_modul_3():
    fig, ax = plt.subplots(figsize=(6, 5), dpi=150)
    x = np.linspace(-0.2, 1.2, 400)
    y1 = x
    y2 = x ** 2
    ax.plot(x, y1, label='$y = x$', color='#00d2ff', linewidth=2)
    ax.plot(x, y2, label='$y = x^2$', color='#ff007f', linewidth=2)
    x_fill = np.linspace(0, 1, 200)
    ax.fill_between(x_fill, x_fill, x_fill**2, color='#00d2ff', alpha=0.15)
    cx, cy = 0.5, 0.4
    ax.scatter([cx], [cy], color='#ffca28', marker='*', s=150, zorder=5, label='Centroid $(\\bar{x}, \\bar{y})$', edgecolors='black')
    ax.annotate(f'({cx:.1f}, {cy:.1f})', (cx, cy), textcoords="offset points", xytext=(20,-5), ha='center', color='#ffca28', fontweight='bold')
    ax.set_title('Centroid Daerah antara $y = x$ dan $y = x^2$', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.legend(facecolor='#2b2d42', edgecolor='#495057')
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(-0.2, 1.2)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '03_centroid_ex1.png'), facecolor='#1e1e24')
    plt.close()

    fig, ax = plt.subplots(figsize=(6, 5), dpi=150)
    x = np.linspace(-0.5, 4.5, 400)
    y1 = np.sqrt(np.clip(x, 0, None))
    ax.plot(x, y1, label='$y = \\sqrt{x}$', color='#00d2ff', linewidth=2)
    ax.axvline(4, color='#ff007f', label='$x = 4$', linewidth=2)
    x_fill = np.linspace(0, 4, 200)
    ax.fill_between(x_fill, np.sqrt(x_fill), 0, color='#00d2ff', alpha=0.15)
    cx, cy = 2.4, 0.75
    ax.scatter([cx], [cy], color='#ffca28', marker='*', s=150, zorder=5, label='Centroid $(\\bar{x}, \\bar{y})$', edgecolors='black')
    ax.annotate(f'({cx:.1f}, {cy:.2f})', (cx, cy), textcoords="offset points", xytext=(0,10), ha='center', color='#ffca28', fontweight='bold')
    ax.set_title('Centroid Daerah $y = \\sqrt{x}$, $y = 0$, $x = 4$', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.legend(facecolor='#2b2d42', edgecolor='#495057')
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 2.5)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '03_centroid_ex2.png'), facecolor='#1e1e24')
    plt.close()

def generate_modul_4():
    fig, ax = plt.subplots(figsize=(6, 5), dpi=150)
    t = np.linspace(-2.2, 2.2, 400)
    x = t**2 - 1
    y = t**3 - 3*t
    ax.plot(x, y, color='#00d2ff', linewidth=2.5, label='Kurva $(x(t), y(t))$')
    ax.scatter([0, 0], [2, -2], color='#ffca28', s=80, zorder=5, edgecolors='black')
    ax.annotate('t = -1\n(0, 2)', (0, 2), textcoords="offset points", xytext=(-25,-10), ha='center', color='#ffca28', fontweight='bold', fontsize=9)
    ax.annotate('t = 1\n(0, -2)', (0, -2), textcoords="offset points", xytext=(-25,5), ha='center', color='#ffca28', fontweight='bold', fontsize=9)
    for t_val in [-1.5, 0, 1.5]:
        x_val = t_val**2 - 1
        y_val = t_val**3 - 3*t_val
        dx = 2 * t_val
        dy = 3 * t_val**2 - 3
        length = np.sqrt(dx**2 + dy**2)
        if length > 0:
            ax.quiver(x_val, y_val, dx/length, dy/length, color='#ff007f', scale=15, width=0.015, zorder=4)
    ax.set_title('Kurva Parametrik $x = t^2 - 1$, $y = t^3 - 3t$', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.legend(facecolor='#2b2d42', edgecolor='#495057')
    ax.set_xlim(-1.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '04_parametric_ex1.png'), facecolor='#1e1e24')
    plt.close()

    fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
    t = np.linspace(0, 2 * np.pi, 400)
    x = t - np.sin(t)
    y = 1 - np.cos(t)
    ax.plot(x, y, color='#00d2ff', linewidth=2.5, label='Sikloid (1 lengkung)')
    ax.fill_between(x, y, 0, color='#00d2ff', alpha=0.15)
    ax.set_title('Sikloid $x = t - \\sin(t)$, $y = 1 - \\cos(t)$ ($0 \\leq t \\leq 2\\pi$)', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.legend(facecolor='#2b2d42', edgecolor='#495057')
    ax.set_xlim(-0.5, 2 * np.pi + 0.5)
    ax.set_ylim(-0.2, 2.5)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '04_parametric_ex3.png'), facecolor='#1e1e24')
    plt.close()

def generate_modul_5():
    fig, ax = plt.subplots(figsize=(5, 5), dpi=150)
    ax.axhline(0, color='#adb5bd', linewidth=1)
    ax.axvline(0, color='#adb5bd', linewidth=1)
    r_val = 3.0
    theta_val = np.pi / 6
    x_val = r_val * np.cos(theta_val)
    y_val = r_val * np.sin(theta_val)
    ax.plot([0, x_val], [0, y_val], color='#00d2ff', linewidth=2, marker='o')
    ax.plot([x_val, x_val], [0, y_val], color='#ff007f', linestyle=':')
    ax.plot([0, x_val], [0, 0], color='#ffca28', linestyle='--')
    ax.text(x_val + 0.1, y_val + 0.1, 'P(r, $\\theta$) atau (x, y)', color='#ffffff', fontweight='bold')
    ax.text(x_val/2 - 0.2, y_val/2 + 0.2, 'r', color='#00d2ff', fontsize=12)
    ax.text(x_val/2, -0.3, 'x = r cos $\\theta$', color='#ffca28', fontsize=10, ha='center')
    ax.text(x_val + 0.15, y_val/2, 'y = r sin $\\theta$', color='#ff007f', fontsize=10, va='center')
    arc_theta = np.linspace(0, theta_val, 50)
    ax.plot(0.5 * np.cos(arc_theta), 0.5 * np.sin(arc_theta), color='#ffffff', linewidth=1.5)
    ax.text(0.7 * np.cos(theta_val/2), 0.7 * np.sin(theta_val/2), '$\\theta$', color='#ffffff', fontsize=12)
    ax.set_title('Konsep Koordinat Kutub $(r, \\theta)$', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 3)
    ax.grid(True)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '05_polar_concept.png'), facecolor='#1e1e24')
    plt.close()

    fig = plt.figure(figsize=(5, 5), dpi=150)
    fig.patch.set_facecolor('#1e1e24')
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor('#1e1e24')
    theta = np.linspace(0, 2 * np.pi, 500)
    r = 1 + np.cos(theta)
    ax.plot(theta, r, color='#00d2ff', linewidth=2.5)
    ax.fill(theta, r, color='#00d2ff', alpha=0.15)
    ax.tick_params(colors='#adb5bd')
    ax.grid(color='#495057', linestyle='--')
    ax.set_title('Kardioid $r = 1 + \\cos(\\theta)$', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '05_polar_cardioid.png'), facecolor='#1e1e24')
    plt.close()

    fig = plt.figure(figsize=(5, 5), dpi=150)
    fig.patch.set_facecolor('#1e1e24')
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor('#1e1e24')
    theta = np.linspace(0, 2 * np.pi, 500)
    r = 3 * np.cos(2 * theta)
    ax.plot(theta, np.abs(r), color='#ff007f', linewidth=2.5)
    ax.fill(theta, np.abs(r), color='#ff007f', alpha=0.1)
    ax.tick_params(colors='#adb5bd')
    ax.grid(color='#495057', linestyle='--')
    ax.set_title('Kurva Mawar (4 Kelopak) $r = 3\\cos(2\\theta)$', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '05_polar_rose.png'), facecolor='#1e1e24')
    plt.close()

    fig = plt.figure(figsize=(5, 5), dpi=150)
    fig.patch.set_facecolor('#1e1e24')
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor('#1e1e24')
    theta = np.linspace(0, 2 * np.pi, 500)
    r = 1 + 2 * np.cos(theta)
    ax.plot(theta, r, color='#ffca28', linewidth=2.5)
    ax.fill(theta, np.clip(r, 0, None), color='#ffca28', alpha=0.1)
    ax.tick_params(colors='#adb5bd')
    ax.grid(color='#495057', linestyle='--')
    ax.set_title('Limaçon dengan Inner Loop $r = 1 + 2\\cos(\\theta)$', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '05_polar_limacon.png'), facecolor='#1e1e24')
    plt.close()

def generate_modul_6():
    fig, ax = plt.subplots(figsize=(5, 5), dpi=150)
    ax.set_facecolor('#1e1e24')
    ax.axhline(0, color='#adb5bd', linewidth=1)
    ax.axvline(0, color='#adb5bd', linewidth=1)
    theta1 = np.pi/6
    theta2 = np.pi/3
    r = 3.5
    ax.plot([0, r * np.cos(theta1)], [0, r * np.sin(theta1)], color='#ffca28', linewidth=1.5)
    ax.plot([0, r * np.cos(theta2)], [0, r * np.sin(theta2)], color='#ffca28', linewidth=1.5)
    theta_fill = np.linspace(theta1, theta2, 100)
    ax.fill(np.concatenate(([0], r * np.cos(theta_fill), [0])), 
            np.concatenate(([0], r * np.sin(theta_fill), [0])), 
            color='#00d2ff', alpha=0.2)
    ax.text(1.2 * np.cos((theta1+theta2)/2), 1.2 * np.sin((theta1+theta2)/2), 'd$\\theta$', color='#ffffff', ha='center', fontsize=12)
    ax.text(r * 0.7 * np.cos((theta1+theta2)/2), r * 0.7 * np.sin((theta1+theta2)/2), 'r', color='#00d2ff', ha='center', fontsize=12)
    ax.text(r * 0.5 * np.cos(theta1 - 0.1), r * 0.5 * np.sin(theta1 - 0.1), '$\\theta = \\alpha$', color='#ffca28')
    ax.text(r * 0.4 * np.cos(theta2 + 0.1), r * 0.4 * np.sin(theta2 + 0.1), '$\\theta = \\beta$', color='#ffca28')
    arc_theta = np.linspace(theta1, theta2, 50)
    ax.plot(0.8 * np.cos(arc_theta), 0.8 * np.sin(arc_theta), color='#ffffff', linewidth=1.5)
    ax.set_title('Elemen Luas Juring $dA = \\frac{1}{2}r^2 d\\theta$', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    ax.set_xlim(-0.5, 4.0)
    ax.set_ylim(-0.5, 4.0)
    ax.grid(True)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '06_polar_sector.png'), facecolor='#1e1e24')
    plt.close()

    fig = plt.figure(figsize=(5, 5), dpi=150)
    fig.patch.set_facecolor('#1e1e24')
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor('#1e1e24')
    theta_full = np.linspace(0, 2 * np.pi, 500)
    r_full = 1 + np.cos(theta_full)
    ax.plot(theta_full, r_full, color='#00d2ff', linewidth=2)
    theta_fill = np.linspace(0, np.pi, 250)
    r_fill = 1 + np.cos(theta_fill)
    ax.fill(theta_fill, r_fill, color='#00d2ff', alpha=0.25)
    ax.tick_params(colors='#adb5bd')
    ax.grid(color='#495057', linestyle='--')
    ax.set_title('Luas Setengah Kardioid $r = 1 + \\cos(\\theta)$', fontsize=13, pad=15, color='#ffffff', fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '06_polar_area_ex1.png'), facecolor='#1e1e24')
    plt.close()

    fig = plt.figure(figsize=(5, 5), dpi=150)
    fig.patch.set_facecolor('#1e1e24')
    ax = fig.add_subplot(111, polar=True)
    ax.set_facecolor('#1e1e24')
    theta = np.linspace(0, 2 * np.pi, 500)
    r2 = 1 + np.sin(theta)
    theta_pos = np.linspace(0, np.pi, 250)
    ax.plot(theta_pos, 3 * np.sin(theta_pos), color='#00d2ff', linewidth=2.5, label='$r = 3\\sin(\\theta)$')
    ax.plot(theta, r2, color='#ff007f', linewidth=2.5, label='$r = 1 + \\sin(\\theta)$')
    ax.scatter([np.pi/6, 5*np.pi/6], [1.5, 1.5], color='#ffca28', s=60, zorder=5, edgecolors='black')
    theta_fill = np.linspace(np.pi/6, 5*np.pi/6, 200)
    r1_fill = 3 * np.sin(theta_fill)
    r2_fill = 1 + np.sin(theta_fill)
    ax.fill_between(theta_fill, r2_fill, r1_fill, color='#00d2ff', alpha=0.25)
    ax.tick_params(colors='#adb5bd')
    ax.grid(color='#495057', linestyle='--')
    ax.set_title('Daerah antara $r = 3\\sin(\\theta)$ dan $r = 1 + \\sin(\\theta)$', fontsize=12, pad=15, color='#ffffff', fontweight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '06_polar_area_ex2.png'), facecolor='#1e1e24')
    plt.close()

def generate_modul_7():
    # --- Plot 1: Konvergensi vs Divergensi Barisan ---
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=150)
    fig.patch.set_facecolor('#1e1e24')
    ax1.set_facecolor('#1e1e24')
    ax2.set_facecolor('#1e1e24')
    
    n = np.arange(1, 21)
    # Konvergen: a_n = n / (n+1) -> Limit = 1
    an = n / (n + 1)
    ax1.scatter(n, an, color='#00d2ff', s=50, edgecolors='black', label='$a_n = \\frac{n}{n+1}$')
    ax1.axhline(1.0, color='#ff007f', linestyle='--', linewidth=1.5, label='Limit L = 1')
    ax1.set_title('Barisan Konvergen', color='#ffffff', fontweight='bold')
    ax1.set_xlabel('Suku ke-n')
    ax1.set_ylabel('Nilai $a_n$')
    ax1.grid(True)
    ax1.set_ylim(0, 1.2)
    ax1.legend(facecolor='#2b2d42', edgecolor='#495057')
    
    # Divergen: b_n = (-1)^n
    bn = (-1.0) ** n
    ax2.scatter(n, bn, color='#ffca28', s=50, edgecolors='black', label='$b_n = (-1)^n$')
    ax2.set_title('Barisan Divergen (Osilasi)', color='#ffffff', fontweight='bold')
    ax2.set_xlabel('Suku ke-n')
    ax2.set_ylabel('Nilai $b_n$')
    ax2.grid(True)
    ax2.set_ylim(-1.5, 1.5)
    ax2.legend(facecolor='#2b2d42', edgecolor='#495057')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '07_sequence_conv_div.png'), facecolor='#1e1e24')
    plt.close()

    # --- Plot 2: Teorema Apit (Squeeze Theorem) ---
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=150)
    n = np.arange(1, 26)
    an = -1.0 / n
    cn = 1.0 / n
    bn = np.sin(n) / n
    
    ax.plot(n, cn, color='#ff007f', linestyle=':', linewidth=1.5, label='$c_n = 1/n$')
    ax.plot(n, an, color='#ff007f', linestyle=':', linewidth=1.5, label='$a_n = -1/n$')
    ax.scatter(n, bn, color='#00d2ff', s=45, zorder=5, edgecolors='black', label='$b_n = \\sin(n)/n$')
    ax.axhline(0, color='#ffffff', linestyle='--', alpha=0.3)
    
    ax.set_title('Ilustrasi Teorema Apit (Squeeze Theorem)', fontsize=12, pad=15, color='#ffffff', fontweight='bold')
    ax.set_xlabel('n')
    ax.set_ylabel('Nilai Suku')
    ax.grid(True)
    ax.legend(facecolor='#2b2d42', edgecolor='#495057')
    ax.set_ylim(-1.1, 1.1)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '07_sequence_squeeze.png'), facecolor='#1e1e24')
    plt.close()

    # --- Plot 3: Barisan Rekursif MCT (a_n = sqrt(2 + a_{n-1})) ---
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=150)
    
    # Hitung suku rekursif
    steps = 10
    a = np.zeros(steps)
    a[0] = 1.0
    for i in range(1, steps):
        a[i] = np.sqrt(2.0 + a[i-1])
        
    n = np.arange(1, steps + 1)
    ax.scatter(n, a, color='#ffca28', s=60, zorder=5, edgecolors='black', label='$a_n$')
    ax.plot(n, a, color='#00d2ff', alpha=0.5, linestyle='-')
    ax.axhline(2.0, color='#ff007f', linestyle='--', linewidth=1.5, label='Batas Atas / Limit L = 2')
    
    ax.set_title('Barisan Rekursif $a_1=1, a_{n+1}=\\sqrt{2+a_n}$', fontsize=12, pad=15, color='#ffffff', fontweight='bold')
    ax.set_xlabel('n')
    ax.set_ylabel('Nilai $a_n$')
    ax.grid(True)
    ax.legend(facecolor='#2b2d42', edgecolor='#495057')
    ax.set_ylim(0.8, 2.2)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '07_sequence_mct.png'), facecolor='#1e1e24')
    plt.close()
    print("Modul 7 images generated successfully.")

if __name__ == "__main__":
    generate_modul_1()
    generate_modul_2()
    generate_modul_3()
    generate_modul_4()
    generate_modul_5()
    generate_modul_6()
    generate_modul_7()
