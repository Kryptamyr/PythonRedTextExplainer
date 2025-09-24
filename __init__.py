import unrealsdk
from Mods.ModMenu import EnabledSaveType, ModTypes, SDKMod, RegisterMod
from Mods import ModMenu

# Import all category modules
from .pistols import PISTOL_COMMANDS
from .shotguns import SHOTGUN_COMMANDS
from .assault_rifles import ASSAULT_RIFLE_COMMANDS
from .sniper_rifles import SNIPER_RIFLE_COMMANDS
from .smgs import SMG_COMMANDS
from .rocket_launchers import ROCKET_LAUNCHER_COMMANDS
from .grenades import GRENADE_COMMANDS
from .shields import SHIELD_COMMANDS
from .relics import RELIC_COMMANDS
from .class_mods import CLASS_MOD_COMMANDS
from .currency import CURRENCY_COMMANDS

class PythonRedTextExplainer(SDKMod):
    Name: str = "Python Red Text Explainer"
    Author: str = "Kryptamyr"
    Description: str = "PythonSDK port of Red text Explainer by Ezeith - Organized by category"
    Version: str = "2.0"

    SupportedGames: ModMenu.Game = ModMenu.Game.BL2  # BL2 Vanilla only
    Types: ModTypes = ModTypes.Utility
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    def Enable(self) -> None:
        super().Enable()
        for cmd in COMMANDS:
            exec_cmd(cmd)

    def Disable(self) -> None:
        super().Disable()

def exec_cmd(command: str) -> None:
    try:
        unrealsdk.ConsoleCommand(command)
    except Exception:
        try:
            pc = unrealsdk.GetEngine().GamePlayers[0].Actor
            pc.ConsoleCommand(command)
        except Exception:
            pass

# Combine all category commands into one list
COMMANDS = (
    PISTOL_COMMANDS +
    SHOTGUN_COMMANDS +
    ASSAULT_RIFLE_COMMANDS +
    SNIPER_RIFLE_COMMANDS +
    SMG_COMMANDS +
    ROCKET_LAUNCHER_COMMANDS +
    GRENADE_COMMANDS +
    SHIELD_COMMANDS +
    RELIC_COMMANDS +
    CLASS_MOD_COMMANDS +
    CURRENCY_COMMANDS
)

RegisterMod(PythonRedTextExplainer())