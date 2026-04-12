from core import Keeper
from botfactory import Maker
from tracker import Screen, Record

# Singleton instance
manager = Keeper()

# Observers
screen = Screen()
record = Record()

# Factory creates units
unit1 = Maker.produce("helper", "AlphaBot")
unit2 = Maker.produce("friend", "BetaBot")

# Add units to keeper
manager.add_unit(unit1)
manager.add_unit(unit2)

# Run system
for unit in manager.units:
    unit.action()
    screen.notice(f"{unit.id} completed an action")
    record.notice(f"{unit.id} completed an action")
