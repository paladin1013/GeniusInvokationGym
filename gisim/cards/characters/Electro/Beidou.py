"""北斗"""
from queue import PriorityQueue
from typing import Dict, List

from gisim.cards.characters.base import CharacterCard, CharacterSkill, GenericSkill
from gisim.classes.enums import (
    CharPos,
    ElementType,
    EntityType,
    EquipmentType,
    Nation,
    PlayerID,
    SkillType,
    WeaponType,
)
from gisim.classes.status import CombatStatusEntity
from gisim.classes.summon import AttackSummon, Summon


class Oceanborne(GenericSkill):
    """
    征涛
    ~~~~
    造成2点`物理伤害`。
    """

    id: int = 14051
    name: str = "Oceanborne"
    text: str = """
    Deals 2 Physical DMG.
    """
    type: SkillType = SkillType.NORMAL_ATTACK
    costs: Dict[ElementType, int] = {ElementType.ELECTRO: 1, ElementType.ANY: 2}
    damage_element: ElementType = ElementType.NONE
    damage_value: int = 2


class Tidecaller(GenericSkill):
    """
    捉浪
    ~~~~
    本角色附属`捉浪·涛拥之守`并`准备技能`：`踏潮`。
    """

    id: int = 14052
    name: str = "Tidecaller"
    text: str = """
    This character gains a Tidecaller: Surf Embrace. Prepare Skill: Wavestrider.
    """
    type: SkillType = SkillType.ELEMENTAL_SKILL
    costs: Dict[ElementType, int] = {ElementType.ELECTRO, 3}


class Stormbreaker(GenericSkill):
    """
    斫雷
    ~~~~
    造成3点`雷元素伤害`，生成`雷兽之盾`。
    """

    id: int = 14053
    name: str = "Stormbreaker"
    text: str = """
    Deals 3 Electro DMG, creates 1 Thunderbeast's Targe.
    """
    type: SkillType = SkillType.ELEMENTAL_BURST
    costs: Dict[ElementType, int] = {ElementType.ELECTRO, 4, ElementType.POWER, 3}
    damage_element: ElementType = ElementType.ELECTRO
    damage_value: int = 3


class Wavestrider(GenericSkill):
    """
    踏潮
    ~~~~
    （需准备1个行动轮）造成2点`雷元素伤害`。
    """

    id: int = 14054
    name: str = "Wavestrider"
    text: str = """
    (Prepare for 1 turn)Deals 2 Electro DMG.
    """
    type: SkillType = SkillType.ELEMENTAL_SKILL
    costs: Dict[ElementType, int] = {}


class Beidou(CharacterCard):
    """北斗"""

    id: int = 1405
    name: str = "Beidou"
    element_type: ElementType = ElementType.ELECTRO
    nations: List[Nation] = [Nation.Liyue]
    health_point: int = 10
    power: int = 0
    max_power: int = 3
    weapon_type: WeaponType = WeaponType.CLAYMORE
    skills: List[CharacterSkill] = [
        Oceanborne(),
        Tidecaller(),
        Stormbreaker(),
        Wavestrider(),
    ]
