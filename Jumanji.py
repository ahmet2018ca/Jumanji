"""
Jumanji - A Terminal-Based Adventure Game
A choose-your-own-adventure game where players navigate through dangerous scenarios.
"""

import random
from enum import Enum
from typing import Dict, List, Optional, Callable
from dataclasses import dataclass


class Character(Enum):
    """Available character types with their special abilities."""
    MR_LUCKY = "Mr. Lucky"
    MEGAMIND = "MEGAMIND"
    ANIMAL_ANDY = "Animal Andy"


class Item(Enum):
    """Available inventory items."""
    JOKER_TOKEN = "Joker Token"
    PET_CHEETAH = "Pet Cheetah"
    CUTE_PUPPY = "Cute Puppy"
    MILLIONS_CURRENCY = "Millions of In-Game Currency"
    GUN_GENERATOR = "Gun Generator Per Situation"


@dataclass
class GameState:
    """Manages the current state of the game."""
    character: Optional[Character] = None
    lives: int = 3
    inventory: List[Item] = None
    
    def __post_init__(self):
        if self.inventory is None:
            self.inventory = [Item.GUN_GENERATOR]
    
    def lose_life(self, amount: int = 1) -> bool:
        """Removes lives and returns True if game should continue."""
        self.lives -= amount
        return self.lives > 0
    
    def has_item(self, item: Item) -> bool:
        """Checks if player has specific item."""
        return item in self.inventory
    
    def add_item(self, item: Item) -> None:
        """Adds item to inventory."""
        if item not in self.inventory:
            self.inventory.append(item)
    
    def remove_item(self, item: Item) -> None:
        """Removes item from inventory."""
        if item in self.inventory:
            self.inventory.remove(item)


class GameUI:
    """Handles all user interface operations."""
    
    @staticmethod
    def display_separator() -> None:
        """Displays visual separator."""
        print("-" * 150 + "\n" * 2)
    
    @staticmethod
    def display_message(message: str) -> None:
        """Displays a formatted message."""
        GameUI.display_separator()
        print(message)
    
    @staticmethod
    def get_user_input(prompt: str = "") -> str:
        """Gets user input and handles special commands."""
        return input(prompt).lower().strip()
    
    @staticmethod
    def wait_for_enter() -> bool:
        """Waits for user to press enter. Returns True if successful."""
        user_input = GameUI.get_user_input("Press Enter to continue...")
        return user_input == ""
    
    @staticmethod
    def display_inventory(state: GameState) -> None:
        """Displays current inventory and game state."""
        GameUI.display_separator()
        print("=== INVENTORY ===\n")
        
        character_name = state.character.value if state.character else "No character selected"
        print(f"Character: {character_name}\n")
        print(f"Lives remaining: {state.lives}\n")
        
        if state.inventory:
            print("Items:")
            for item in state.inventory:
                print(f"• {item.value}")
        else:
            print("No items in inventory")
        
        print("\nPress Enter to continue...")
        input("")


class MathChallenge:
    """Handles math-based challenges."""
    
    @staticmethod
    def create_multiplication_challenge() -> tuple[str, int]:
        """Creates a multiplication challenge for MEGAMIND."""
        a, b = random.randint(1, 13), random.randint(1, 13)
        return f"What is {a} × {b}?", a * b
    
    @staticmethod
    def create_exponent_challenge() -> tuple[str, int]:
        """Creates an exponent challenge for other characters."""
        a, b = random.randint(1, 5), random.randint(1, 4)  # Reduced to prevent huge numbers
        return f"What is {a} ^ {b}?", a ** b


class RandomEvent:
    """Handles probability-based events."""
    
    @staticmethod
    def roll_percentage(success_chance: int) -> bool:
        """Returns True if random roll succeeds."""
        return random.randint(1, 100) <= success_chance


class JumanjiGame:
    """Main game controller."""
    
    def __init__(self):
        self.state = GameState()
        self.ui = GameUI()
        
        # Command mapping for special inputs
        self.special_commands = {
            'exit': self._handle_exit,
            'inventory': self._handle_inventory
        }
    
    def _handle_special_input(self, user_input: str) -> bool:
        """Handles special commands. Returns True if command was processed."""
        if user_input in self.special_commands:
            self.special_commands[user_input]()
            return True
        return False
    
    def _handle_exit(self) -> None:
        """Handles game exit."""
        print("\nGoodbye! Thanks for playing Jumanji!")
        exit()
    
    def _handle_inventory(self) -> None:
        """Handles inventory display."""
        self.ui.display_inventory(self.state)
    
    def _get_choice(self, prompt: str, valid_choices: Dict[str, Callable], 
                   allow_special: bool = True) -> None:
        """Gets user choice and executes corresponding function."""
        while True:
            self.ui.display_message(prompt)
            user_input = self.ui.get_user_input()
            
            if allow_special and self._handle_special_input(user_input):
                continue
            
            if user_input in valid_choices:
                valid_choices[user_input]()
                break
            else:
                print("Invalid choice. Please try again.")
    
    def _game_over(self) -> None:
        """Handles game over scenario."""
        self.ui.display_message(
            "Game Over! You've lost all your lives.\n"
            "The adventure ends here, but you can always try again.\n"
            "Would you like to restart? (yes/no)"
        )
        
        choice = self.ui.get_user_input()
        if choice == "yes":
            self.__init__()  # Reset game state
            self.start_game()
        else:
            self._handle_exit()
    
    def start_game(self) -> None:
        """Starts the game with instructions."""
        self.ui.display_message(
            "Welcome to JUMANJI!\n\n"
            "INSTRUCTIONS:\n"
            "• Type the letter (A, B, C, etc.) to select an option\n"
            "• Type 'inventory' to view your current items\n"
            "• Type 'exit' to quit the game\n"
            "• Press Enter when prompted to continue\n\n"
            "You have 3 lives. Use them wisely!\n"
            "Good luck on your adventure!"
        )
        
        if self.ui.wait_for_enter():
            self._show_prologue()
    
    def _show_prologue(self) -> None:
        """Shows game prologue."""
        self.ui.display_message(
            "You're playing a video game when suddenly...\n"
            "Your body gets sucked into the game world!\n\n"
            "You must complete this dangerous adventure game to return to reality.\n"
            "Choose wisely - your decisions will determine your fate."
        )
        
        if self.ui.wait_for_enter():
            self._character_selection()
    
    def _character_selection(self) -> None:
        """Handles character selection."""
        prompt = (
            "Choose your character wisely - it will affect your journey:\n\n"
            "A) Mr. Lucky - 25% better chance in risky situations\n"
            "B) MEGAMIND - Easier math problems when facing challenges\n"
            "C) Animal Andy - Can communicate with animals\n\n"
            "Choose your character:"
        )
        
        choices = {
            'a': lambda: self._set_character(Character.MR_LUCKY),
            'b': lambda: self._set_character(Character.MEGAMIND),
            'c': lambda: self._set_character(Character.ANIMAL_ANDY)
        }
        
        self._get_choice(prompt, choices)
    
    def _set_character(self, character: Character) -> None:
        """Sets the player's character and continues to cave event."""
        self.state.character = character
        self.ui.display_message(f"Great choice! You are now {character.value}.")
        if self.ui.wait_for_enter():
            self._cave_encounter()
    
    def _cave_encounter(self) -> None:
        """Handles the mysterious cave encounter."""
        prompt = (
            "On your way to the first checkpoint, you discover a mysterious cave.\n"
            "Something valuable might be inside...\n\n"
            "A) Explore the cave\n"
            "B) Continue on your path\n\n"
            "What do you choose?"
        )
        
        choices = {
            'a': self._explore_cave,
            'b': self._skip_cave
        }
        
        self._get_choice(prompt, choices)
    
    def _explore_cave(self) -> None:
        """Handles cave exploration."""
        prompt = (
            "Inside the cave, you find an ancient lamp on a rock.\n"
            "It looks mysterious and powerful...\n\n"
            "A) Examine the lamp closely\n"
            "B) Leave it alone\n\n"
            "What do you do?"
        )
        
        choices = {
            'a': self._examine_lamp,
            'b': self._genie_angry_path
        }
        
        self._get_choice(prompt, choices)
    
    def _examine_lamp(self) -> None:
        """Handles lamp examination - leads to genie encounter."""
        self.state.add_item(Item.JOKER_TOKEN)
        self.ui.display_message(
            "A friendly genie appears from the lamp!\n"
            "As a reward for your bravery, you receive a Joker Token!\n"
            "This token can get you out of any dangerous situation.\n\n"
            "The genie also grants you one wish:"
        )
        self._genie_wish()
    
    def _genie_angry_path(self) -> None:
        """Handles the path where genie gets angry."""
        luck_chance = 95 if self.state.character == Character.MR_LUCKY else 70
        
        prompt = (
            f"The genie senses your cowardice and is displeased!\n"
            f"You have a {luck_chance}% chance of calming him down,\n"
            "or you can solve a math problem to appease him.\n"
            "Failure in either case costs you a life!\n\n"
            "A) Take your chances with luck\n"
            "B) Solve the math problem\n\n"
            "Choose wisely:"
        )
        
        choices = {
            'a': lambda: self._luck_challenge(luck_chance),
            'b': self._math_challenge
        }
        
        self._get_choice(prompt, choices)
    
    def _luck_challenge(self, success_chance: int) -> None:
        """Handles luck-based challenge."""
        if RandomEvent.roll_percentage(success_chance):
            self.ui.display_message("Lucky you! The genie calms down.")
            self._genie_wish()
        else:
            self._lose_life_and_continue("The genie's anger overwhelms you!")
    
    def _math_challenge(self) -> None:
        """Handles math challenge based on character."""
        if self.state.character == Character.MEGAMIND:
            question, answer = MathChallenge.create_multiplication_challenge()
        else:
            question, answer = MathChallenge.create_exponent_challenge()
        
        self.ui.display_message(question)
        user_answer = self.ui.get_user_input("Your answer: ")
        
        try:
            if int(user_answer) == answer:
                self.ui.display_message("Correct! The genie is impressed.")
                self._genie_wish()
            else:
                self._lose_life_and_continue("Wrong answer! The genie is furious!")
        except ValueError:
            self.ui.display_message("Please enter a valid number.")
            self._math_challenge()
    
    def _genie_wish(self) -> None:
        """Handles genie wish selection."""
        prompt = (
            "Choose your wish carefully:\n\n"
            "A) Pet Cheetah - Fast transportation and protection\n"
            "B) Cute Puppy - Might be more useful than you think\n"
            "C) Millions in Currency - Money talks in any world\n"
            "D) Hungry Grizzly Bear - This seems dangerous...\n\n"
            "What do you wish for?"
        )
        
        choices = {
            'a': lambda: self._grant_wish(Item.PET_CHEETAH, "A loyal cheetah appears by your side!"),
            'b': lambda: self._grant_wish(Item.CUTE_PUPPY, "An adorable puppy bounds up to you!"),
            'c': lambda: self._grant_wish(Item.MILLIONS_CURRENCY, "Your pockets fill with gold coins!"),
            'd': self._wish_grizzly_bear
        }
        
        self._get_choice(prompt, choices)
    
    def _grant_wish(self, item: Item, message: str) -> None:
        """Grants a beneficial wish."""
        self.state.add_item(item)
        self.ui.display_message(message)
        if self.ui.wait_for_enter():
            self._bridge_encounter()
    
    def _wish_grizzly_bear(self) -> None:
        """Handles the dangerous grizzly bear wish."""
        self._lose_life_and_continue(
            "A hungry grizzly bear appears and immediately attacks!\n"
            "That was... not a smart choice."
        )
    
    def _skip_cave(self) -> None:
        """Handles skipping the cave."""
        self.ui.display_message("You decide to play it safe and continue on your path.")
        if self.ui.wait_for_enter():
            self._bridge_encounter()
    
    def _lose_life_and_continue(self, message: str) -> None:
        """Handles life loss and game continuation."""
        if self.state.lose_life():
            self.ui.display_message(f"{message}\nYou lose a life! Lives remaining: {self.state.lives}")
            if self.ui.wait_for_enter():
                self._bridge_encounter()
        else:
            self.ui.display_message(f"{message}\nYou have no lives remaining!")
            self._game_over()
    
    def _bridge_encounter(self) -> None:
        """Randomly selects between lion or chimpanzee encounter."""
        encounters = [self._lion_encounter, self._chimpanzee_encounter]
        random.choice(encounters)()
    
    def _lion_encounter(self) -> None:
        """Handles lion encounter at the bridge."""
        options = [
            "A) Hide behind a bush",
            "B) Use taser", 
            "C) Use bazooka"
        ]
        
        choices = {
            'a': lambda: self._lose_life_and_continue("Lions have excellent senses! Hiding was futile."),
            'b': lambda: self._lose_life_and_continue("The taser barely tickled the lion!"),
            'c': self._lion_bazooka_success
        }
        
        if self.state.has_item(Item.JOKER_TOKEN):
            options.append("D) Use Joker Token")
            choices['d'] = self._use_joker_token
        
        if self.state.has_item(Item.PET_CHEETAH):
            options.append("E) Send pet cheetah to fight")
            choices['e'] = self._cheetah_vs_lion
        
        prompt = f"A massive lion blocks the bridge!\n\n{chr(10).join(options)}\n\nWhat do you do?"
        self._get_choice(prompt, choices)
    
    def _lion_bazooka_success(self) -> None:
        """Handles successful bazooka use against lion."""
        self.ui.display_message("The bazooka eliminates the lion! You can cross the bridge safely.")
        if self.ui.wait_for_enter():
            self._final_boss()
    
    def _cheetah_vs_lion(self) -> None:
        """Handles cheetah vs lion fight."""
        self.state.remove_item(Item.PET_CHEETAH)
        self.ui.display_message(
            "Your cheetah fights bravely but loses to the lion.\n"
            "However, the exhausted lion lets you pass."
        )
        if self.ui.wait_for_enter():
            self._final_boss()
    
    def _chimpanzee_encounter(self) -> None:
        """Handles chimpanzee horde encounter."""
        options = [
            "A) Hide behind a bush",
            "B) Use zap gun",
            "C) Try helicopter escape"
        ]
        
        choices = {
            'a': lambda: self._lose_life_and_continue("Chimpanzees are too smart! They found you easily."),
            'b': self._zap_gun_success,
            'c': self._helicopter_escape
        }
        
        if self.state.has_item(Item.PET_CHEETAH):
            options.append("D) Escape on pet cheetah")
            choices['d'] = self._cheetah_escape
        
        if self.state.character == Character.ANIMAL_ANDY:
            options.append("E) Try to communicate")
            choices['e'] = lambda: self._lose_life_and_continue("An angry horde won't listen to reason!")
        
        if self.state.has_item(Item.JOKER_TOKEN):
            options.append("F) Use Joker Token")
            choices['f'] = self._use_joker_token
        
        prompt = f"An angry chimpanzee horde approaches!\n\n{chr(10).join(options)}\n\nWhat do you do?"
        self._get_choice(prompt, choices)
    
    def _zap_gun_success(self) -> None:
        """Handles successful zap gun use."""
        self.ui.display_message("The zap gun's energy bounces between enemies, eliminating the horde!")
        if self.ui.wait_for_enter():
            self._final_boss()
    
    def _helicopter_escape(self) -> None:
        """Handles helicopter escape attempt."""
        success_chance = 75 if self.state.character == Character.MR_LUCKY else 50
        
        if RandomEvent.roll_percentage(success_chance):
            self.ui.display_message("You successfully pilot the helicopter to safety!")
            if self.ui.wait_for_enter():
                self._final_boss()
        else:
            self._lose_life_and_continue("The helicopter crashes! You barely survive.")
    
    def _cheetah_escape(self) -> None:
        """Handles cheetah escape."""
        self.ui.display_message("Your cheetah carries you to safety at lightning speed!")
        if self.ui.wait_for_enter():
            self._final_boss()
    
    def _use_joker_token(self) -> None:
        """Handles joker token usage."""
        self.state.remove_item(Item.JOKER_TOKEN)
        self.ui.display_message("The Joker Token glows and transports you safely past the danger!")
        if self.ui.wait_for_enter():
            self._final_boss()
    
    def _final_boss(self) -> None:
        """Handles the final boss encounter."""
        options = [
            "A) Ask Mighty Midas nicely to let you pass",
            "B) Try to sneak past",
            "C) Use bazooka"
        ]
        
        choices = {
            'a': lambda: self._final_boss_fail("Mighty Midas shows no mercy to the polite!"),
            'b': self._final_boss_victory_sneak,
            'c': lambda: self._final_boss_fail("Your bazooka barely scratches the mighty giant!")
        }
        
        if self.state.has_item(Item.JOKER_TOKEN):
            options.append("D) Use Joker Token")
            choices['d'] = self._final_boss_victory_token
        
        if self.state.has_item(Item.CUTE_PUPPY):
            options.append("E) Use cute puppy")
            choices['e'] = self._final_boss_victory_puppy
        
        prompt = (
            "You face the final challenge: Mighty Midas, a 30-meter giant!\n"
            "He blocks your path to freedom.\n\n"
            f"{chr(10).join(options)}\n\n"
            "This is your final test. Choose wisely:"
        )
        
        self._get_choice(prompt, choices)
    
    def _final_boss_fail(self, message: str) -> None:
        """Handles failed final boss attempt."""
        if self.state.lose_life():
            self.ui.display_message(f"{message}\nLives remaining: {self.state.lives}")
            if self.ui.wait_for_enter():
                self._final_boss()  # Try again
        else:
            self.ui.display_message(f"{message}\nYou have no lives remaining!")
            self._game_over()
    
    def _final_boss_victory_sneak(self) -> None:
        """Handles sneaking victory."""
        self.ui.display_message(
            "Amazing! Mighty Midas is lost in thought.\n"
            "You successfully sneak past the distracted giant!"
        )
        self._victory()
    
    def _final_boss_victory_token(self) -> None:
        """Handles joker token victory."""
        self.state.remove_item(Item.JOKER_TOKEN)
        self.ui.display_message(
            "Perfect use of your Joker Token!\n"
            "The token's magic safely transports you past Mighty Midas!"
        )
        self._victory()
    
    def _final_boss_victory_puppy(self) -> None:
        """Handles cute puppy victory."""
        self.state.remove_item(Item.CUTE_PUPPY)
        self.ui.display_message(
            "The cute puppy melts even Mighty Midas's heart!\n"
            "The giant smiles and steps aside, letting you both pass."
        )
        self._victory()
    
    def _victory(self) -> None:
        """Handles game victory."""
        if self.state.has_item(Item.MILLIONS_CURRENCY):
            ending = (
                "CONGRATULATIONS! You've escaped Jumanji!\n\n"
                "Your unused millions in currency transform into real gold!\n"
                "You return to reality both alive and wealthy!\n\n"
                "Thanks for playing Jumanji!"
            )
        else:
            ending = (
                "CONGRATULATIONS! You've escaped Jumanji!\n\n"
                "You successfully return to the real world!\n"
                "The fresh air of reality has never felt so good.\n\n"
                "Thanks for playing Jumanji!"
            )
        
        self.ui.display_message(ending)
        self._handle_exit()


def main():
    """Main function to start the game."""
    game = JumanjiGame()
    game.start_game()


if __name__ == "__main__":
    main()
