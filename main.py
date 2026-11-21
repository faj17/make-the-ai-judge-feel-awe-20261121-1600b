import os

TEXT = """High above the desert, the stars are coming out one by one — light that left its star before you existed, travelling all this way, just to reach you tonight. It is in no hurry at all. Neither are you.
"""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
