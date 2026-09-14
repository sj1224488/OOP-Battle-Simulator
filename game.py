from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Rectangle"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblinTwo = Goblin("Tibble")

    print(f"{goblinTwo.name} enters the arena with {goblin.health} health.")

    print("But no hero has answered the call... yet.")

    hero = Hero("Nya","Ninja")

    print(f"{hero.name} the {hero.hero_class} enter the arena with {hero.health} health.")

    heroAttack = hero.attack()
    goblin.take_damage(heroAttack)

    if goblin.is_alive():
        goblinAttack = goblin.attack()
        hero.take_damage(goblinAttack)


if __name__ == "__main__":
    main()
