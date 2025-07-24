# PK-Bots
- Create and manage robot behaviors for soccer robots.
- Uses role-based behaviors and a master controller to coordinate multiple robots.
- PK-Bots is short for "Penalty Kick Robots".

## Installation
```bash
git clone https://github.com/yourusername/PK-Bots.git
cd PK-Bots
pip install -e .
```

## Quick Start
```python
from pkbots import MasterController

# Create controller (automatically initializes robots)
controller = MasterController()

# Run robot behaviors
controller.update()
```

## Architecture
- **Robot**: Abstract base class defining robot interface
- **Player/Goalie**: Concrete robot implementations with specific behaviors
- **MasterController**: Manages robot collection and coordinates updates
- **Behavior Pattern**: Each robot type has its own `active()` method where they are performing their task.

```python
from pkbots import MasterController

# Initialize controller with robots
controller = MasterController()

# Update all robots (runs their behaviors)
controller.update()
```

## Example Usage
```python
from pkbots import MasterController

def main():
    # Create the controller
    controller = MasterController()
    
    # Run update forever
    while True:
        controller.update()

if __name__ == "__main__":
    main()
```

### Future Plans
- None at the moment
