import random
import string
from scrap import get_full_page_content
import time

def generate_random_string(seed: int) -> str:
    """
    Generate a 16-character random string:
    - Starts with letters.
    - Ends with 3 letters (no digits at the end).
    - Contains a maximum of 3 digits, randomly distributed between letters.
    - Based on a provided seed.

    Args:
        seed (int): The seed value to initialize the random generator.

    Returns:
        str: The generated random string.
    """
    random.seed(seed)

    # Define character pools
    letters = string.ascii_lowercase
    digits = string.digits

    # Ensure string starts with 2 letters
    start_letters = random.choices(letters, k=2)

    # Generate up to 3 random digits
    numbers = random.choices(digits, k=3)

    # Generate 8 more letters (to fill middle part)
    middle_letters = random.choices(letters, k=8)

    # Ensure string ends with 3 letters
    end_letters = random.choices(letters, k=3)

    # Combine the letters and numbers
    middle_combined = middle_letters + numbers

    # Shuffle the middle part to distribute numbers randomly
    random.shuffle(middle_combined)

    # Construct the final string
    final_string = start_letters + middle_combined + end_letters

    # Join into a single string
    return ''.join(final_string)

# Example usage
t1 = time.time()
for i in range(472,482):
    seed_value = i
    random_string = generate_random_string(seed_value)
    base="https://plum.gift/"
    url = base+random_string
    if (i==795):
        url="https://plum.gift/LH9gA2RznaVOsWMK"
    print(url)
    result = get_full_page_content(url)
    if str(result).find("cancelled")!=-1:
        print("The page does not work")
    else:
        print("The page works")
        with open('works.txt', 'a') as f:
            f.write(url+'\n')

t2 = time.time()
print("Time taken: ", t2-t1)

# url="https://plum.gift/LH9gA2RznaVOsWMK"
# result = get_full_page_content(url)
# if str(result).find("Order Reference")!=-1:
#     print("The page works")
# else:
#     print("The page does not work")

# https://plum.gift/kf72g1yjmprokfxj