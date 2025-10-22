from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.lab03.text.normalize import normalize


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    with open(path,"r",encoding="utf-8") as file:
        in_file=str(file.read())
    return normalize(in_file).replace(" ","")

# print({Path.cwd()})
# for item in Path.cwd().iterdir():
#     print(f"  {item.name}")
print(read_text(Path("data") / "input.txt"))
