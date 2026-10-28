from pathlib import Path

SKILLS_DIR=Path(__file__).parent

def load_skill(skill_name:str)->str:
    allowed={"career","relationships","education","health","general"}

    if skill_name not in allowed:
        raise ValueError("Unknown Skill")

    path=SKILLS_DIR/skill_name/"SKILL.md"

    return path.read_text(encoding='utf-8')