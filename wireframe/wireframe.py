import matplotlib.pyplot as plt

# Wireframe çizimi için figür oluşturma
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 15)
ax.axis("off")

# Header (Navbar)
ax.add_patch(plt.Rectangle((0, 13.5), 10, 1, edgecolor="black", facecolor="lightgray", lw=2))
ax.text(5, 14, "Navbar (Logo + Menü)", ha="center", va="center", fontsize=10, fontweight="bold")

# Hero Section (Ana görsel + Başlık)
ax.add_patch(plt.Rectangle((0, 10), 10, 3, edgecolor="black", facecolor="lightblue", lw=2))
ax.text(5, 11.5, "Hero Alanı (Başlık + Açıklama + CTA Butonu)", ha="center", va="center", fontsize=10, fontweight="bold")

# Hizmetler Bölümü (3 Kart)
for i in range(3):
    ax.add_patch(plt.Rectangle((1 + i * 3, 7), 2, 2, edgecolor="black", facecolor="lightgreen", lw=2))
    ax.text(2 + i * 3, 8, f"Hizmet {i+1}", ha="center", va="center", fontsize=10, fontweight="bold")

# Referanslar / Projeler
ax.add_patch(plt.Rectangle((0, 4), 10, 2, edgecolor="black", facecolor="lightcoral", lw=2))
ax.text(5, 5, "Projeler / Referanslar", ha="center", va="center", fontsize=10, fontweight="bold")

# Footer
ax.add_patch(plt.Rectangle((0, 0), 10, 2, edgecolor="black", facecolor="lightgray", lw=2))
ax.text(5, 1, "Footer (İletişim + Sosyal Medya)", ha="center", va="center", fontsize=10, fontweight="bold")

# Wireframe gösterimi
plt.show()