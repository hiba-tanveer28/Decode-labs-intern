import random
import string


def generate_password(length, include_special):

   
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special_characters = "@#$%&*"

    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(numbers)
    ]

  
    if include_special:

        password.append(
            random.choice(special_characters)
        )

        all_characters = (
            lowercase
            + uppercase
            + numbers
            + special_characters
        )

    else:

        all_characters = (
            lowercase
            + uppercase
            + numbers
        )

  
    for _ in range(
        length - len(password)
    ):

        password.append(
            random.choice(all_characters)
        )

   
    random.shuffle(password)

    return "".join(password)
