import modal
from fastapi import Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = modal.App("dnd-character-sheet")
image = modal.Image.debian_slim().pip_install("fastapi", "pydantic")


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

class AbilityScores(BaseModel):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


class CharacterInput(BaseModel):
    name: str
    level: int
    class_name: str
    race: str
    ability_scores: AbilityScores
    armor_class: int
    speed: int
    max_hp: int
    current_hp: int
    temp_hp: Optional[int] = 0
    # Proficiencies: list of skill/save names this character is proficient in
    saving_throw_proficiencies: list[str] = []
    skill_proficiencies: list[str] = []
    skill_expertise: list[str] = []  # double proficiency bonus


# ---------------------------------------------------------------------------
# Pure calculation helpers (no auth needed — used internally)
# ---------------------------------------------------------------------------

SKILL_ABILITIES = {
    "acrobatics": "dexterity",
    "animal_handling": "wisdom",
    "arcana": "intelligence",
    "athletics": "strength",
    "deception": "charisma",
    "history": "intelligence",
    "insight": "wisdom",
    "intimidation": "charisma",
    "investigation": "intelligence",
    "medicine": "wisdom",
    "nature": "intelligence",
    "perception": "wisdom",
    "performance": "charisma",
    "persuasion": "charisma",
    "religion": "intelligence",
    "sleight_of_hand": "dexterity",
    "stealth": "dexterity",
    "survival": "wisdom",
}

ABILITIES = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]


def ability_modifier(score: int) -> int:
    return (score - 10) // 2


def proficiency_bonus(level: int) -> int:
    return (level - 1) // 4 + 2


def format_modifier(mod: int) -> str:
    return f"+{mod}" if mod >= 0 else str(mod)


def calculate_character_stats(char: CharacterInput) -> dict:
    scores = char.ability_scores.model_dump()
    mods = {ability: ability_modifier(scores[ability]) for ability in ABILITIES}
    prof_bonus = proficiency_bonus(char.level)

    # Ability scores block
    ability_block = {}
    for ability in ABILITIES:
        ability_block[ability] = {
            "score": scores[ability],
            "modifier": mods[ability],
            "modifier_display": format_modifier(mods[ability]),
        }

    # Saving throws
    saving_throws = {}
    for ability in ABILITIES:
        base_mod = mods[ability]
        proficient = ability in char.saving_throw_proficiencies
        total = base_mod + (prof_bonus if proficient else 0)
        saving_throws[ability] = {
            "modifier": total,
            "modifier_display": format_modifier(total),
            "proficient": proficient,
        }

    # Skills
    skills = {}
    for skill, governing_ability in SKILL_ABILITIES.items():
        base_mod = mods[governing_ability]
        expertise = skill in char.skill_expertise
        proficient = skill in char.skill_proficiencies or expertise
        bonus = prof_bonus * 2 if expertise else (prof_bonus if proficient else 0)
        total = base_mod + bonus
        skills[skill] = {
            "modifier": total,
            "modifier_display": format_modifier(total),
            "proficient": proficient,
            "expertise": expertise,
            "governing_ability": governing_ability,
        }

    # Passive perception = 10 + perception modifier
    passive_perception = 10 + skills["perception"]["modifier"]

    # Initiative = DEX modifier
    initiative = mods["dexterity"]

    return {
        "character": {
            "name": char.name,
            "level": char.level,
            "class": char.class_name,
            "race": char.race,
        },
        "proficiency_bonus": prof_bonus,
        "proficiency_bonus_display": format_modifier(prof_bonus),
        "initiative": initiative,
        "initiative_display": format_modifier(initiative),
        "armor_class": char.armor_class,
        "speed": char.speed,
        "passive_perception": passive_perception,
        "hit_points": {
            "max": char.max_hp,
            "current": char.current_hp,
            "temp": char.temp_hp,
            "effective": char.current_hp + (char.temp_hp or 0),
        },
        "ability_scores": ability_block,
        "saving_throws": saving_throws,
        "skills": skills,
    }


# ---------------------------------------------------------------------------
# Modal endpoint
# ---------------------------------------------------------------------------

@app.function(
    image=image,
    secrets=[modal.Secret.from_name("api-auth-token")],
    timeout=60,
)
@modal.fastapi_endpoint(method="POST")
def character_stats(
    character: CharacterInput,
    authorization: str = Header(None),
) -> dict:
    """
    Calculate all character stats, modifiers, saving throws, and skills
    for a D&D 5e character.
    """
    import os

    expected_token = os.environ.get("API_AUTH_TOKEN")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid authorization header")

    token = authorization.replace("Bearer ", "")
    if token != expected_token:
        raise HTTPException(status_code=403, detail="Invalid authentication token")

    return calculate_character_stats(character)
