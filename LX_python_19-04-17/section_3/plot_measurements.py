import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

plt.rcParams["font.size"] = 18

CWD = Path(__file__).parent.resolve()

measurements = pd.read_csv(CWD / "measurements.csv")
ax = measurements.plot(
    x="array_length",
    y=["python_timing", "c_timing"],
    loglog=True,
    style="o-",
    xlim=(4e1, 2e5),
)
ax.legend(["Python", "C"])
ax.set_xlabel("Array length")
ax.set_ylabel("Time [ms]")
plt.tight_layout()
plt.savefig(CWD / "py-c_performance.png", dpi=150)

