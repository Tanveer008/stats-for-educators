# Statistics for Educators — Episode 01
# "Why Teachers Need Statistics"
# Author: Tanvir Ali | github.com/Tanveer008

# ── SETUP ──────────────────────────────────────────────
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── LOAD DATA ──────────────────────────────────────────
# Using sample data — replace with your own class CSV
data = {
    'student_id': [f'S{i:02d}' for i in range(1, 21)],
    'pre_test':  [45,50,55,60,62,62,70,75,90,95,40,48,52,58,63,65,72,78,88,92],
    'post_test': [52,61,60,68,70,65,78,82,94,97,50,55,58,67,72,69,80,85,91,95],
    'class':     ['6A']*10 + ['6B']*10
}
df = pd.DataFrame(data)

# ── DESCRIPTIVE STATISTICS ─────────────────────────────
print("=" * 45)
print("  STATISTICS FOR EDUCATORS — Episode 01")
print("=" * 45)

for cls in ['6A', '6B']:
    sub = df[df['class'] == cls]['pre_test']
    print(f"\n📊 Class {cls} — Pre-Test Results")
    print(f"   Mean Score:         {sub.mean():.1f}%")
    print(f"   Median Score:       {sub.median():.1f}%")
    print(f"   Standard Deviation: {sub.std():.1f}")
    print(f"   Min / Max:          {sub.min()}% / {sub.max()}%")

    std = sub.std()
    print(f"\n   📌 Interpretation:")
    if std > 15:
        print(f"   ⚠️  High variation (SD={std:.1f}). Class is divided.")
        print(f"      Consider differentiated instruction.")
    elif std > 8:
        print(f"   ✅  Moderate variation (SD={std:.1f}). Manageable spread.")
    else:
        print(f"   🎯  Low variation (SD={std:.1f}). Uniform performance.")

# ── VISUALIZATION ──────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle('Statistics for Educators — Episode 01\nWhy the Average Isn\'t Enough',
             fontsize=15, fontweight='bold', color='#1F5C99', y=1.01)

colors = {'6A': '#1F5C99', '6B': '#1A7A4A'}

for i, cls in enumerate(['6A', '6B']):
    sub = df[df['class'] == cls]['pre_test']
    ax_hist = axes[i][0]
    ax_box  = axes[i][1]
    color   = colors[cls]

    # Histogram
    ax_hist.hist(sub, bins=7, color=color, edgecolor='white', alpha=0.85)
    ax_hist.axvline(sub.mean(),   color='red',    linestyle='--', linewidth=2,
                    label=f'Mean: {sub.mean():.1f}')
    ax_hist.axvline(sub.median(), color='orange', linestyle='--', linewidth=2,
                    label=f'Median: {sub.median():.1f}')
    ax_hist.set_title(f'Class {cls} — Score Distribution', fontweight='bold', color=color)
    ax_hist.set_xlabel('Score (%)')
    ax_hist.set_ylabel('Students')
    ax_hist.legend(fontsize=9)
    ax_hist.spines['top'].set_visible(False)
    ax_hist.spines['right'].set_visible(False)

    # Box plot
    bp = ax_box.boxplot(sub, vert=True, patch_artist=True,
                        boxprops=dict(facecolor=color+'33', color=color),
                        medianprops=dict(color='red', linewidth=2.5),
                        whiskerprops=dict(color=color),
                        capprops=dict(color=color),
                        flierprops=dict(markerfacecolor=color, marker='o'))
    ax_box.set_title(f'Class {cls} — Score Spread', fontweight='bold', color=color)
    ax_box.set_ylabel('Score (%)')
    ax_box.set_xticklabels([f'Class {cls}'])
    ax_box.text(1.35, sub.mean(), f'SD = {sub.std():.1f}',
                va='center', color='#555', fontsize=10)
    ax_box.spines['top'].set_visible(False)
    ax_box.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('episode01_analysis.png', dpi=150, bbox_inches='tight')
print("\n✅ Chart saved as 'episode01_analysis.png'")
plt.show()

print("\n" + "=" * 45)
print("  KEY LESSON")
print("=" * 45)
print("""
  Two classes can have the same average
  but completely different realities.

  Standard Deviation reveals what the
  average hides — how divided your class is.

  High SD → Differentiate your instruction.
  Low SD  → One approach may serve all.
""")
print("  📂 Full series: github.com/Tanveer008/stats-for-educators")
print("=" * 45)

