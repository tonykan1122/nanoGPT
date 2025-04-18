import matplotlib.pyplot as plt

# Use the validation losses at iteration 40
heads = [2, 3, 5, 7]
losses = [2.5452, 2.5456, 2.5458, 2.5441]

plt.figure(figsize=(10, 6))
plt.plot(heads, losses, marker='o')
plt.xlabel('Number of Heads')
plt.ylabel('Validation Loss at Iteration 40')
plt.title('Impact of Attention Heads on Model Performance (7 Layers)')
plt.grid(True)
plt.savefig('figures/head_vs_loss.png')
plt.close()

print("Plot saved to figures/head_vs_loss.png")