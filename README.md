# 🎮 Jumanji - Terminal Adventure Game

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Game Type](https://img.shields.io/badge/genre-Adventure-orange.svg)](https://github.com)

> *"In the jungle you must wait, until the dice read five or eight..."*

Welcome to **Jumanji**, an immersive terminal-based choose-your-own-adventure game where every decision could be your last! Get sucked into a dangerous game world and fight your way back to reality with only 3 lives to spare.

![Game Banner](https://via.placeholder.com/800x200/2E8B57/FFFFFF?text=🌿+JUMANJI+TERMINAL+GAME+🌿)

## 🌟 Game Overview

In Jumanji, you're not just playing a game—you become trapped inside one! Navigate through treacherous encounters, solve mathematical puzzles, and make strategic decisions to escape back to the real world. Choose your character wisely, manage your limited lives, and use special items to overcome deadly challenges.

### 🎯 Key Features

- **3 Unique Characters** with special abilities
- **Dynamic Inventory System** with magical items
- **Probability-Based Events** for unpredictable gameplay
- **Mathematical Challenges** that adapt to your character
- **Multiple Story Paths** leading to different outcomes
- **Professional Object-Oriented Architecture**

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/jumanji-game.git
cd jumanji-game

# Run the game
python jumanji_game.py
```

**Requirements:** Python 3.7+ (uses standard library only)

## 🎭 Choose Your Hero

| Character | Special Ability | Best For |
|-----------|----------------|----------|
| 🍀 **Mr. Lucky** | +25% success rate in risky situations | Risk-takers who trust their fortune |
| 🧠 **MEGAMIND** | Easier mathematical challenges | Strategic players who love puzzles |
| 🐾 **Animal Andy** | Can communicate with creatures | Players who prefer diplomatic solutions |

## 🎒 Magical Items & Inventory

Discover powerful items on your journey:

- **🃏 Joker Token** - Get out of jail free card for any situation
- **🐆 Pet Cheetah** - Lightning-fast escape from danger
- **🐶 Cute Puppy** - Melts even the coldest hearts
- **💰 Millions in Currency** - Money talks in any world
- **🔫 Gun Generator** - Provides weapons when facing enemies

## 🏗️ Technical Architecture

### Object-Oriented Design Patterns

#### **State Management Pattern**
```python
@dataclass
class GameState:
    character: Optional[Character] = None
    lives: int = 3
    inventory: List[Item] = None
```
Centralized game state eliminates global variables and ensures data integrity.

#### **Strategy Pattern**
Different character abilities are implemented as strategies:
- Mr. Lucky gets enhanced probability rolls
- MEGAMIND receives simplified math challenges
- Animal Andy can attempt animal communication

#### **Command Pattern**
Special user commands (`exit`, `inventory`) are mapped to specific handlers:
```python
self.special_commands = {
    'exit': self._handle_exit,
    'inventory': self._handle_inventory
}
```

#### **Factory Pattern**
Mathematical challenges are created based on character type:
```python
class MathChallenge:
    @staticmethod
    def create_multiplication_challenge() -> tuple[str, int]
    
    @staticmethod
    def create_exponent_challenge() -> tuple[str, int]
```

### 🎨 Clean Code Principles

- **Single Responsibility**: Each class has one clear purpose
- **Dependency Injection**: Components are modular and testable
- **Type Safety**: Comprehensive type hints throughout
- **Error Handling**: Robust input validation and exception handling
- **Documentation**: Professional docstrings for all methods

### 🔧 Technologies & Concepts Used

| Technology | Purpose | Implementation |
|------------|---------|----------------|
| **Python Enums** | Type-safe constants | Character types and items |
| **Dataclasses** | Clean data structures | Game state management |
| **Type Hints** | Code clarity & IDE support | All functions and methods |
| **Random Module** | Probability mechanics | Event outcomes and challenges |
| **Lambda Functions** | Callback handling | Choice mapping system |

## 🎮 Gameplay Mechanics

### Life System
- Start with **3 lives**
- Lose lives through poor decisions or failed challenges
- Game over when all lives are lost
- Strategic resource management required

### Probability Engine
```python
class RandomEvent:
    @staticmethod
    def roll_percentage(success_chance: int) -> bool:
        return random.randint(1, 100) <= success_chance
```

### Dynamic Choice System
Choices adapt based on:
- Current inventory items
- Selected character abilities
- Previous game decisions

## 🌳 Game Flow Architecture

```
Start Game → Instructions → Prologue → Character Selection
    ↓
Cave Encounter (Optional) → Genie Events → Item Collection
    ↓
Bridge Encounter → [Lion Event | Chimpanzee Event] (Random)
    ↓
Final Boss → Victory/Defeat → Game End/Restart
```

## 🎯 Advanced Features

### **Smart Input Handling**
- Case-insensitive input processing
- Multiple valid input formats (letters or full text)
- Persistent special command access (`exit`, `inventory`)

### **Adaptive Difficulty**
- Math problems scale with character choice
- Probability events favor lucky characters
- Multiple solution paths for different play styles

### **Professional Error Handling**
```python
def _get_choice(self, prompt: str, valid_choices: Dict[str, Callable]) -> None:
    while True:
        # Input validation and error recovery
        if user_input in valid_choices:
            valid_choices[user_input]()
            break
        else:
            print("Invalid choice. Please try again.")
```

## 🔮 Code Quality Features

- **No Global Variables**: All state properly encapsulated
- **Modular Design**: Easy to extend with new events/characters
- **Memory Efficient**: Minimal resource usage
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Unit Test Ready**: Architecture supports easy testing

## 🎪 Sample Gameplay

```
=== JUMANJI GAME SESSION ===

Welcome to JUMANJI!
Choose your character:
A) Mr. Lucky - 25% better chance in risky situations
> a

You discover a mysterious cave...
A) Explore the cave
B) Continue on your path
> a

A friendly genie appears!
Choose your wish:
A) Pet Cheetah
B) Cute Puppy  
C) Millions in Currency
> c

Your pockets fill with gold coins!
An angry chimpanzee horde approaches!
A) Hide behind a bush
B) Use zap gun
C) Try helicopter escape
> b

The zap gun eliminates the horde!
You face Mighty Midas...
```

## 🚀 Future Enhancements

- **Save/Load System**: Persistent game progress
- **Achievement System**: Unlock rewards for different paths
- **Character Stats**: Detailed ability tracking
- **New Encounters**: Expand the adventure world
- **Multiplayer Mode**: Cooperative decision making

## 🤝 Contributing

We welcome contributions! Areas for improvement:
- New character types with unique abilities
- Additional story branches and encounters
- Enhanced probability mechanics
- Sound effects integration
- GUI version development

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎊 Credits

- **Game Design**: Inspired by the Jumanji universe
- **Architecture**: Professional Python game development patterns
- **Testing**: Extensive gameplay validation

---

*Ready to test your luck and skill? Your adventure in Jumanji awaits! Will you escape back to reality, or become another victim of the game?* 🎲

**[⭐ Star this repo](https://github.com/yourusername/jumanji-game)** if you enjoyed
