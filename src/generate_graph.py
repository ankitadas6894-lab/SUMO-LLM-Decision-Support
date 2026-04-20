import matplotlib.pyplot as plt
import numpy as np

# --- 1. ENTER YOUR COLLECTED DATA HERE ---
scenarios = ['Low Traffic', 'Medium Traffic', 'High Traffic']
llama_times = [22.23, 13.89, 6.06]  # Replace with your actual results
phi_times = [3.78, 6.4, 10.42]      # Replace with your actual results

x = np.arange(len(scenarios))  # Label locations
width = 0.35                   # Width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

# Create bars
rects1 = ax.bar(x - width/2, llama_times, width, label='Llama-2 (7B)', color='#FFCC00', edgecolor='black')
rects2 = ax.bar(x + width/2, phi_times, width, label='Phi-3 (Mini)', color='#00e5ff', edgecolor='black')

# Add text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Response Time (Seconds)')
ax.set_title('AI Processing Latency: Llama-2 vs. Phi-3')
ax.set_xticks(x)
ax.set_xticklabels(scenarios)
ax.legend()

# Add value labels on top of bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}s',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

# Save the graph
plt.savefig('model_comparison_graph.png')
print("Graph saved as model_comparison_graph.png")