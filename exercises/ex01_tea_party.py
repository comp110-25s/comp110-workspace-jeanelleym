"""Calculating costs of my tea party."""

__author__: str = "730572910"


def main_planner (guests: int) -> None:
    """Entry point of the program"""
    print ("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str (tea_bags(people = guests)))
    print ("Treats: " + str(treats(people=guests)))
    print ("Cost: $" + str(cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)))) 


def tea_bags (people: int) -> int:
    """Calculate number of tea bags."""
    return 2 * people


def treats (people: int) -> int: 
    """Calculate number of treats"""
    return  int(1.5 * tea_bags(people=people))


def cost (tea_count: int, treat_count: int) -> float:
    """Calculate combined costs."""
    return (tea_count * .5 + treat_count * .75)

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
