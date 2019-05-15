"""
Module that calculates standard vs sharshooter damage
"""
import numpy as np
from die import roll_with_modifier, hit_or_miss, calculate_damage

def compare(modifier, armor_class, dmg_dice, dmg_base):
    """
    PRE:    modifier = modifier to hit
            armor_class = ac of the enemy
            DMG_DICE = array of numbers where each number represents the highest number on that dice
                ex) [20] = 1d20, [6, 6] = 2d6, [8, 6, 6, 6] = 1d8 + 3d6
            dmg_base =  base damage
    """
    std_avg = []
    sharp_avg = []

    for _ in range(0, 10):
        num_rolls = 1000000
        std_rolls = roll_with_modifier([20], num_rolls, modifier)
        sharp_rolls = roll_with_modifier([20], num_rolls, modifier - 5)

        std_hits = hit_or_miss(std_rolls, armor_class)
        sharp_hits = hit_or_miss(sharp_rolls, armor_class)

        std_dmg = calculate_damage(std_hits, dmg_dice, dmg_base)
        sharp_dmg = calculate_damage(sharp_hits, dmg_dice, dmg_base + 10)

        std_avg.append(np.average(std_dmg))
        sharp_avg.append(np.average(sharp_dmg))

    print("AC {0} | {1:.3f}        | {2:.3f}         | {3:.3f}           | {4:.3f}".format(
        armor_class, np.average(std_avg), np.average(sharp_avg),
        np.median(std_avg), np.median(sharp_avg)))

def run_compare(name, atk_mod, dmg_dice, dmg_mod):
    """
    PRE:    name = name of comparison
            modifier = modifier to hit
            DMG_DICE = array of numbers where each number represents the highest number on that dice
                ex) [20] = 1d20, [6, 6] = 2d6, [8, 6, 6, 6] = 1d8 + 3d6
            dmg_base =  base damage
    """
    print(name)
    print("      | Standard AVG | Sharpshot AVG | Standard Median | Sharpshot Median")
    compare(atk_mod, 8, dmg_dice, dmg_mod)  # Zombie
    compare(atk_mod, 11, dmg_dice, dmg_mod) # Thug
    compare(atk_mod, 12, dmg_dice, dmg_mod) # Kobold
    compare(atk_mod, 16, dmg_dice, dmg_mod) # Bugbear
    compare(atk_mod, 18, dmg_dice, dmg_mod) # Young Red Dragon
    compare(atk_mod, 19, dmg_dice, dmg_mod) # Adult Red Dragon
    compare(atk_mod, 22, dmg_dice, dmg_mod) # Ancient Red Dragon

if __name__ == '__main__':
    run_compare("Level 1 Drow Fighter DEX=17 with a Longbow", 5, [8], 3)
    run_compare("Level 3 Drow Fighter DEX=17 with a Longbow and archery fighting style", 7, [8], 3)
    run_compare("Level 4 Drow Fighter DEX=18 with a Longbow and archery fighting style", 8, [8], 4)
