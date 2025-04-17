class Superhero:
    """Base class representing a generic superhero"""
    
    def __init__(self, name, secret_identity, powers, origin_story):
        # Encapsulation - using underscore prefix for "private" attributes
        self._name = name
        self._secret_identity = secret_identity
        self._powers = powers
        self._origin_story = origin_story
        self._energy_level = 100  # Starts at full energy
        
    # Getter methods for encapsulated attributes
    def get_name(self):
        return self._name
    
    def get_secret_identity(self):
        return self._secret_identity
    
    def use_power(self, power_index):
        """Use one of the hero's powers, consuming energy"""
        if self._energy_level <= 0:
            print(f"{self._name} is too exhausted to use powers!")
            return
            
        if 0 <= power_index < len(self._powers):
            power = self._powers[power_index]
            print(f"{self._name} uses {power}!")
            self._energy_level -= 10
        else:
            print("Invalid power selection!")
    
    def rest(self):
        """Recover energy by resting"""
        self._energy_level = min(100, self._energy_level + 30)
        print(f"{self._name} rests and recovers energy. Current energy: {self._energy_level}%")
    
    def describe(self):
        """Polymorphic method to be overridden by subclasses"""
        return f"{self._name} (Secret Identity: {self._secret_identity}) with powers: {', '.join(self._powers)}"
    
    def __str__(self):
        return self.describe()


class TechHero(Superhero):
    """Subclass for tech-based superheroes"""
    
    def __init__(self, name, secret_identity, powers, origin_story, gadgets):
        super().__init__(name, secret_identity, powers, origin_story)
        self._gadgets = gadgets  # Additional attribute for tech heroes
        
    def use_gadget(self, gadget_name):
        """Tech heroes can use special gadgets"""
        if gadget_name in self._gadgets:
            print(f"{self._name} uses {gadget_name}: {self._gadgets[gadget_name]}!")
        else:
            print(f"{self._name} doesn't have that gadget!")
    
    def describe(self):
        """Override parent method to include gadgets"""
        base_description = super().describe()
        return f"{base_description}\nGadgets: {', '.join(self._gadgets.keys())}"


class MutantHero(Superhero):
    """Subclass for mutant superheroes with genetic powers"""
    
    def __init__(self, name, secret_identity, powers, origin_story, mutation_level):
        super().__init__(name, secret_identity, powers, origin_story)
        self._mutation_level = mutation_level
        
    def use_power(self, power_index):
        """Mutants use powers more efficiently (less energy cost)"""
        if self._energy_level <= 0:
            print(f"{self._name} is too exhausted to use powers!")
            return
            
        if 0 <= power_index < len(self._powers):
            power = self._powers[power_index]
            print(f"{self._name} uses {power} with mutant efficiency!")
            self._energy_level -= 5  # Only 5% energy cost instead of 10%
        else:
            print("Invalid power selection!")
    
    def describe(self):
        """Override parent method to include mutation level"""
        base_description = super().describe()
        return f"{base_description}\nMutation Level: {self._mutation_level}/10"


# Example usage
if __name__ == "__main__":
    # Create some superheroes
    batman = TechHero(
        name="Batman",
        secret_identity="Bruce Wayne",
        powers=["martial arts", "detective skills", "intimidation"],
        origin_story="Witnessed parents' murder, vowed to fight crime",
        gadgets={
            "Batarang": "Throwing weapon",
            "Grappling Hook": "For scaling buildings",
            "Batmobile": "High-tech vehicle"
        }
    )
    
    wolverine = MutantHero(
        name="Wolverine",
        secret_identity="Logan",
        powers=["regeneration", "adamantium claws", "enhanced senses"],
        origin_story="Weapon X experiment",
        mutation_level=9
    )
    
    # Demonstrate polymorphism
    heroes = [batman, wolverine]
    for hero in heroes:
        print("\n" + hero.describe())
        hero.use_power(0)  # Each hero will use their power differently
        hero.use_power(1)
        hero.rest()
        
    # TechHero specific method
    batman.use_gadget("Batarang")
    batman.use_gadget("Grappling Hook")
    
    # MutantHero efficiency
    print("\nTesting mutant efficiency:")
    for _ in range(5):
        wolverine.use_power(1)  # Uses claws
    print(f"Wolverine's energy after 5 power uses: {wolverine._energy_level}%")
