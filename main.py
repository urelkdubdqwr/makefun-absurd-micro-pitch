"""Write the single-sentence make.fun micro-pitch to entry.txt in the output dir."""

import os

ENTRY = (
    "For car washes with subscribers who forget they subscribed: $4 a month, "
    "an agent watches the pollen count and texts 'your car gets dirty again "
    "tomorrow,' keeping every $19.99 alive."
)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as handle:
    handle.write(ENTRY + "\n")
