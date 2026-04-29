"""
Graphical Abstract for: PONE-D-26-01398R1
"Using a mixed opinion dynamics and innovation diffusion model to
explore the 'best game no one played' phenomenon"
Huang & Wang (2026), PLOS ONE

Output:
- graphical_abstract.png  (1200x1200, lossless)
- graphical_abstract.jpg  (1200x1200, ~95% quality, for social/web use)
"""
import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image

# ---- Paths ----
OUT_DIR = "/Users/gscott/Dropbox/文件/我的程式/Github/PLOS-BCAT"
PNG_PATH = os.path.join(OUT_DIR, "graphical_abstract.png")
JPG_PATH = os.path.join(OUT_DIR, "graphical_abstract.jpg")

# ---- Color palette (PLOS-friendly, accessible) ----
NAVY    = "#1D3557"   # primary text
BLUE    = "#2E86AB"   # opinion-clustering channel
RED     = "#C1272D"   # coordination-failure channel
LIGHT   = "#F8F9FA"   # subtle background
ACCENT  = "#FFD166"   # result highlight
GRAY    = "#6C757D"   # secondary text

# ---- Canvas: 12 in * 100 dpi = 1200 px square ----
fig = plt.figure(figsize=(12, 12), dpi=100, facecolor="white")
ax = fig.add_axes([0, 0, 1, 1])  # full-bleed
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis("off")

# ============================================================
# HEADER (y: 86-100)
# ============================================================
ax.text(50, 96, "The “Best Game No One Played” Phenomenon",
        fontsize=24, fontweight="bold", ha="center", va="center", color=NAVY)
ax.text(50, 92, "Why favorable reviews fail to translate into adoption",
        fontsize=14, ha="center", va="center", style="italic", color=GRAY)

# BCAT banner
banner = FancyBboxPatch((22, 85.5), 56, 4.2,
                        boxstyle="round,pad=0.4",
                        facecolor=LIGHT, edgecolor=NAVY, linewidth=1.5)
ax.add_patch(banner)
ax.text(50, 87.6,
        "BCAT  =  Bounded Confidence  +  Adoption Threshold",
        fontsize=13, fontweight="bold", ha="center", va="center", color=NAVY)

# ============================================================
# MIDDLE: TWO-CHANNEL MECHANISM (y: 30-82)
# ============================================================
ax.text(50, 81.5, "Two channels of adoption failure",
        fontsize=14, fontweight="bold", ha="center", color=NAVY)

# ---- Left channel: Opinion Clustering ----
left_box = FancyBboxPatch((4, 47), 41, 31,
                          boxstyle="round,pad=0.5",
                          facecolor="white", edgecolor=BLUE, linewidth=2.5)
ax.add_patch(left_box)
ax.text(24.5, 75, "Channel 1", fontsize=11, ha="center",
        color=BLUE, fontweight="bold")
ax.text(24.5, 72, "Opinion Clustering",
        fontsize=15, fontweight="bold", ha="center", color=NAVY)
ax.text(24.5, 69,
        "bounded confidence partitions\nthe opinion space",
        fontsize=10, ha="center", color=GRAY)

# Mini visual: 3 separated opinion clusters
np.random.seed(42)
cluster_centers = [(11, 56), (24.5, 56), (38, 56)]
cluster_colors  = ["#B0BEC5", "#90CAF9", "#1976D2"]
for (cx, cy), color in zip(cluster_centers, cluster_colors):
    xs = cx + np.random.uniform(-2.2, 2.2, 5)
    ys = cy + np.random.uniform(-2.2, 2.2, 5)
    ax.scatter(xs, ys, s=110, c=color, edgecolors="#37474F",
               linewidths=0.8, alpha=0.95, zorder=5)
# Small "no exchange" dashed line between clusters
for x in [17.5, 31.0]:
    ax.plot([x, x], [52.5, 59.5], linestyle="--", color="#9E9E9E",
            linewidth=1.2, zorder=4)

ax.text(24.5, 50,
        "stable clusters → some agents permanently below adoption threshold",
        fontsize=9, ha="center", color=GRAY, style="italic")

# ---- Right channel: Coordination Failure ----
right_box = FancyBboxPatch((55, 47), 41, 31,
                           boxstyle="round,pad=0.5",
                           facecolor="white", edgecolor=RED, linewidth=2.5)
ax.add_patch(right_box)
ax.text(75.5, 75, "Channel 2", fontsize=11, ha="center",
        color=RED, fontweight="bold")
ax.text(75.5, 72, "Coordination Failure",
        fontsize=15, fontweight="bold", ha="center", color=NAVY)
ax.text(75.5, 69,
        "neighborhood adoption\nbelow personal threshold",
        fontsize=10, ha="center", color=GRAY)

# Mini visual: a hub with neighbors, only 1 adopted
center = np.array([75.5, 56.0])
neighbor_angles = np.linspace(0, 2 * np.pi, 7)[:-1]  # 6 neighbors
neighbor_r = 4.2
neighbor_x = center[0] + neighbor_r * np.cos(neighbor_angles)
neighbor_y = center[1] + neighbor_r * np.sin(neighbor_angles)
# Edges
for nx_, ny_ in zip(neighbor_x, neighbor_y):
    ax.plot([center[0], nx_], [center[1], ny_],
            color="#9E9E9E", linewidth=0.8, zorder=4)
# Neighbors: only 1 adopted (red), others not (light)
neighbor_colors = ["#C1272D", "#FFCDD2", "#FFCDD2", "#FFCDD2", "#FFCDD2", "#FFCDD2"]
ax.scatter(neighbor_x, neighbor_y, s=180, c=neighbor_colors,
           edgecolors=RED, linewidths=1.5, zorder=5)
# Center: focal not-yet-adopted agent
ax.scatter(center[0], center[1], s=260, c="white",
           edgecolors=NAVY, linewidths=2.0, zorder=6)
ax.text(center[0], center[1], "?", fontsize=14, ha="center", va="center",
        color=NAVY, fontweight="bold", zorder=7)

ax.text(75.5, 50,
        "adoption fraction 1/6 → cascade halts when threshold > 1/6",
        fontsize=9, ha="center", color=GRAY, style="italic")

# ---- Connecting arrows to result ----
ax.add_patch(FancyArrowPatch((24.5, 47), (38, 41),
                              arrowstyle="-|>", mutation_scale=20,
                              color=BLUE, linewidth=2.2, zorder=3))
ax.add_patch(FancyArrowPatch((75.5, 47), (62, 41),
                              arrowstyle="-|>", mutation_scale=20,
                              color=RED, linewidth=2.2, zorder=3))

# ---- Result box ----
result = FancyBboxPatch((26, 32), 48, 8,
                        boxstyle="round,pad=0.5",
                        facecolor=ACCENT, edgecolor=NAVY,
                        linewidth=2, alpha=0.55)
ax.add_patch(result)
ax.text(50, 36,
        r"$0 \;\leq\; \mathrm{GSI} \;\leq\; \mathrm{FRI} \;\leq\; 1$",
        fontsize=20, ha="center", va="center",
        color=NAVY, fontweight="bold")

ax.text(50, 28,
        "Adoption gap = FRI − GSI    •    user-friendly testimony "
        "can repair Channel 1 when cascade succeeds",
        fontsize=10, ha="center", color=GRAY, style="italic")

# ============================================================
# BOTTOM: 4 NETWORK TOPOLOGIES (y: 4-22)
# ============================================================
ax.text(50, 22,
        "Validated across 4 network topologies "
        "(regular lattice, small-world, random, scale-free)",
        fontsize=11, ha="center", color=NAVY, fontweight="bold")
ax.text(50, 19,
        "100,548 simulation runs  •  sensitivity analysis on 5 parameters  "
        "•  finite-size scaling N = 400 to 2,500",
        fontsize=9, ha="center", color=GRAY)

network_labels = ["Regular lattice", "Small-world", "Random", "Scale-free"]
network_centers_x = [14, 38, 62, 86]
ny0 = 11   # vertical center of mini-networks


def draw_lattice(ax, cx, cy, n=4, span=6):
    step = span / (n - 1)
    coords = [(cx - span / 2 + j * step, cy - span / 2 + i * step)
              for i in range(n) for j in range(n)]
    for x, y in coords:
        ax.scatter(x, y, s=18, c=NAVY, zorder=5)
    for i in range(n):
        for j in range(n):
            if j < n - 1:
                ax.plot([cx - span / 2 + j * step, cx - span / 2 + (j + 1) * step],
                        [cy - span / 2 + i * step] * 2,
                        color=GRAY, linewidth=0.5, zorder=4)
            if i < n - 1:
                ax.plot([cx - span / 2 + j * step] * 2,
                        [cy - span / 2 + i * step, cy - span / 2 + (i + 1) * step],
                        color=GRAY, linewidth=0.5, zorder=4)


def draw_graph(ax, cx, cy, G, span=6, node_sizes=None):
    pos = nx.circular_layout(G, scale=span / 2)
    if node_sizes is None:
        node_sizes = {n: 18 for n in G.nodes()}
    for u, v in G.edges():
        ax.plot([cx + pos[u][0], cx + pos[v][0]],
                [cy + pos[u][1], cy + pos[v][1]],
                color=GRAY, linewidth=0.5, zorder=4)
    for n, (px, py) in pos.items():
        ax.scatter(cx + px, cy + py, s=node_sizes[n], c=NAVY, zorder=5)


# Regular lattice
draw_lattice(ax, network_centers_x[0], ny0, n=4, span=6)
# Small-world (Watts-Strogatz on a ring)
G_sw = nx.watts_strogatz_graph(10, 2, 0.15, seed=7)
draw_graph(ax, network_centers_x[1], ny0, G_sw, span=6)
# Random (Erdos-Renyi)
G_er = nx.erdos_renyi_graph(10, 0.28, seed=3)
draw_graph(ax, network_centers_x[2], ny0, G_er, span=6)
# Scale-free (Barabasi-Albert), nodes sized by degree
G_ba = nx.barabasi_albert_graph(10, 1, seed=5)
sizes = {n: 12 + dict(G_ba.degree())[n] * 6 for n in G_ba.nodes()}
draw_graph(ax, network_centers_x[3], ny0, G_ba, span=6, node_sizes=sizes)

for cx, label in zip(network_centers_x, network_labels):
    ax.text(cx, 5.2, label, fontsize=10, ha="center", color=NAVY)

# ============================================================
# FOOTER
# ============================================================
ax.text(50, 1.8,
        "Huang & Wang (2026)   ·   PLOS ONE   ·   "
        "github.com/canslab1/BCAT   ·   doi:10.5281/zenodo.19216365",
        fontsize=8.5, ha="center", color=GRAY)

# ---- Save ----
fig.savefig(PNG_PATH, dpi=100, facecolor="white",
            pad_inches=0, bbox_inches=None)
plt.close(fig)

img = Image.open(PNG_PATH).convert("RGB")
img.save(JPG_PATH, "JPEG", quality=95, optimize=True)

print(f"PNG: {PNG_PATH}")
print(f"JPG: {JPG_PATH}")
print(f"Size: {img.size}")
print(f"PNG bytes: {os.path.getsize(PNG_PATH):,}")
print(f"JPG bytes: {os.path.getsize(JPG_PATH):,}")
