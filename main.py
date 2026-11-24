import os

REVIEW = "\u2605\u2606\u2606\u2606\u2606 Says 'one quick thing' eleven times a day. I stopped counting. He never stopped asking."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)

if __name__ == "__main__":
    main()
