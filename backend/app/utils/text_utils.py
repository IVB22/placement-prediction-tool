import re

def normalize_text(s: str) -> str:
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9+\s#.-]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def parse_skill_list(skill_str: str):
    s = (skill_str or "").replace("|", ",")
    parts = [p.strip().lower() for p in s.split(",")]
    parts = [p for p in parts if p and len(p) <= 60]
    return sorted(set(parts))
