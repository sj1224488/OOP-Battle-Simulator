from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Chain"

def battle(warrior: Hero,enemy: Goblin):
    while warrior.is_alive() and enemy.is_alive():
        warrior_damage = warrior.attack()
        enemy.take_damage(warrior_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            warrior.take_damage(enemy_damage) 
    if warrior.is_alive():
        print(f"{warrior.name} wins!")
    else:
        print(f"{enemy.name} wins!")

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

    battle(hero,goblin)


if __name__ == "__main__":
    main()
