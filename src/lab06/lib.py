from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent.parent.parent

def make_obs(path: Path|str) -> Path:
    path=Path(path)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    # if not path.exists():
    #     raise FileNotFoundError("Файл не найден")
    return path
