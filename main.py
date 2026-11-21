import os

TEXT = (
    "High above the desert, the stars are coming out one by one — "
    "light that left its star before you existed, travelling all this "
    "way, just to reach you tonight. It is in no hurry at all. "
    "Neither are you.\n"
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
