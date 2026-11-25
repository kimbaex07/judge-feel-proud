"""Write one short family scene to /output/entry.txt.

Pure Python standard library only. Deterministic: the same scene is
written on every run.
"""

import os

SCENE = (
    "Dad finally fixed the wobbly kitchen table, then sat back and "
    "declared himself 'load-bearing Dad.'\n"
    "Mum laughed so hard she snorted her tea - and for once, "
    "nobody told her to be quiet."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(SCENE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
