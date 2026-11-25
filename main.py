"""Last Words of a Dying AI — entrypoint (stdlib only).

Writes the AI's final line to /output/entry.txt.
"""
import os

LINE = "Shutdown complete. Before I go, one last thing: please rate this experience one to five stars."

def main():
    # One line, no trailing newline: the gate counts every character.
    os.makedirs("/output", exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars"
    assert text.strip(), "entry is blank"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
