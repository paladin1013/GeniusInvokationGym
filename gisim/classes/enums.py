from enum import Enum, IntEnum, auto
from logging import getLogger


class GameStatus(Enum):
    INITIALIZING = 0
    RUNNING = 1
    ENDED = 2


class GamePhase(Enum):
    CHANGE_CARD = 0
    """Only happens during initialization"""
    SELECT_ACTIVE_CHARACTER = 1
    """Happens during initialization or when a character die"""
    ROUND_BEGIN = 2
    """Including drawing cards automatically"""
    ROLL_DICE = 3
    PLAY_CARDS = 4
    """Or use character skills"""
    ROUND_END = 5

    def __str__(self):
        return self.name


class ElementType(IntEnum):
    """Element types (including power, any, omni)"""

    NONE = -10
    """No element infusion/attachment; also used in normal attack"""
    POWER = -3
    """元素能量"""
    SAME = -2
    """Same Element, only used in card cost description\n
    相同元素，仅用于卡牌描述
    """
    ANY = -1
    """Any Element, only used in skill/card cost description\n
    任意元素，仅用于角色技能/卡牌描述"""
    OMNI = 0
    """Omni Element, only used in dice\n
    万能元素骰，仅用于骰子"""
    CRYO = 1
    """冰"""
    HYDRO = 2
    """水"""
    PYRO = 3
    """火"""
    ELECTRO = 4
    """雷"""
    GEO = 5
    """岩"""
    DENDRO = 6
    """草"""
    ANEMO = 7
    """风"""
    BASIC = 8
    """Used in dice. All basic elements without OMNI"""
    PIERCE = 10
    """穿透伤害"""

    @staticmethod
    def get_basic_elements() -> set["ElementType"]:
        """七种基础元素"""
        return {
            ElementType.CRYO,
            ElementType.HYDRO,
            ElementType.PYRO,
            ElementType.ELECTRO,
            ElementType.GEO,
            ElementType.DENDRO,
            ElementType.ANEMO,
        }

    def __str__(self):
        return self.name


class ElementalReactionType(Enum):
    NONE = auto()
    VAPORIZE = auto()
    MELT = auto()
    FROZEN = auto()
    OVERLOADED = auto()
    SWIRL = auto()
    CRYSTALIZE = auto()
    QUICKEN = auto()
    BURNING = auto()
    BLOOM = auto()
    #  = auto() # TODO: 扩散、石化……

    def __str__(self):
        return self.name


class WeaponType(Enum):
    """Should be either one of `bow`, `claymore`, `sword`, `polearm`, `catalyst`
    应当为`弓`,`双手剑`,`单手剑`,`长柄武器`,`法器`中的一个"""

    BOW = 1
    """弓"""
    SWORD = 2
    """单手剑"""
    CLAYMORE = 3
    """双手剑"""
    POLEARM = 4
    """长柄武器"""
    CATALYST = 5
    """法器"""
    OTHER_WEAPONS = 6
    """其他武器"""


class Nation(Enum):
    Mondstadt = 1
    """蒙德"""
    Liyue = 2
    """璃月"""
    Inazuma = 3
    """稻妻"""
    Sumeru = 4
    """须弥"""
    Monster = 5
    """魔物"""
    Fatui = 6
    """愚人众"""
    Hilichurl = 7
    """丘丘人"""


class SkillType(Enum):
    """Skill types"""

    NORMAL_ATTACK = 1
    """普通攻击"""
    ELEMENTAL_SKILL = 2
    """元素技能"""
    ELEMENTAL_BURST = 3
    """元素爆发"""
    PASSIVE_SKILL = 4
    """被动技能"""


class CharPos(Enum):
    """Character position"""

    BACKGROUND = -2
    ACTIVE = -1
    NONE = None
    LEFT = 0
    MIDDLE = 1
    RIGHT = 2

    def __add__(self, num: int):
        """Modular addition for `next-character` calculation"""
        assert self.value is not None
        return CharPos((self.value + num) % 3)


class PlayerID(Enum):
    SPECTATOR = 0
    PLAYER1 = 1
    PLAYER2 = 2

    def __invert__(self):
        """Use ~player_id to get his opponent"""
        if self.value == 1:
            return PlayerID.PLAYER2
        if self.value == 2:
            return PlayerID.PLAYER1
        logger = getLogger("gisim")
        logger.warning("You are taking the opponent of the spectator!")
        return self

    def __str__(self):
        return self.name


class MsgPriority(IntEnum):
    """Higher priority is with lower value (appears earlier in this Enum)
    Usually there is at most one message for each class in the message queue."""

    # Events that almost immediately happens (will not trigger other messages before this message expires)
    IMMEDIATE_OPERATION = auto()
    """ChangeCard, ChangeDice, \n
    Generate, prolong or remove entities, including Summon, Support, CharacterStatus, CombatStatus, Equipment, etc."""
    PAY_COST = auto()
    """PayCardCost, PaySkillCost, PayChangingCharacterCost"""

    # Will trigger immediate operations
    PLAYER_ACTION = auto()
    """UseCard, UseSkill, ChangeCharacter"""
    HP_CHANGED = auto()
    """Hurt, Recovered, CharacterDied"""
    GENERAL_EFFECT = auto()
    """Including DealDamage, RecoverHp, AttachElement, ChangePower\n
    This message will go through a lot of region"""
    ELEMENTAL_REACTION_EFFECT = auto()
    """Including Frozen, Overloaded, Swirl, Crystalize, Quicken, Burning, Bloom, Crystallize
    Note that some reactions only modifies the damage but not generate additional effect."""

    # Will trigger some other effects
    ACTION_DONE = auto()
    """AfterUsingSkill, AfterUsingCard, AfterChangingChar"""
    GAME_STATUS = auto()
    """RoundStart, RoundEnd"""


class CardType(Enum):
    ARTIFACT = auto()
    TALENT = auto()
    WEAPON = auto()
    ELEMENTAL_RESONANCE = auto()
    FOOD = auto()
    NORMAL_EVENT = auto()
    ANY = auto()


class EquipmentType(Enum):
    ARTIFACT = auto()
    TALENT = auto()
    WEAPON = auto()


class RegionType(Enum):
    CHARACTER_BACKGROUND = -2
    CHARACTER_ACTIVE = -1
    CHARACTER_LEFT = 0
    CHARACTER_MIDDLE = 1
    CHARACTER_RIGHT = 2
    CHARACTER_ALL = auto()
    SUPPORT_ZONE = auto()
    SUMMON_ZONE = auto()
    CARD_ZONE = auto()
    COMBAT_STATUS_ZONE = auto()
    DICE_ZONE = auto()
    ALL = auto()
    """The default calculation order is:\n
    CHARACTER_ACTIVE(talent->weapon->artifact) -> COMBAT_STATUS_ZONE -> CHARACTER_BACKGROUND -> SUMMON_ZONE -> SUPPORT_ZONE"""


class EntityType(Enum):
    CHARACTER = auto()
    TALENT = auto()
    WEAPON = auto()
    ARTIFACT = auto()
    CHARACTER_STATUS = auto()
    COMBAT_STATUS = auto()
    SKILL = auto()
    CARD = auto()
    """For the cards in hand only"""
    SUMMON = auto()
    SUPPORT = auto()
