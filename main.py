"""Entry program for mf-u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.

Copies the pre-drawn meme entry.png to /output/entry.png.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise FileNotFoundError("entry.png missing next to main.py")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, "/output/entry.png")


if __name__ == "__main__":
    main()
