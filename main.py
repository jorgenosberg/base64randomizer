import base64
import random


def create_pairs(names):
    pairs = [names[i : i + 2] for i in range(0, len(names), 2)]
    if len(pairs[-1]) == 1:
        pairs[-2].append(pairs[-1][0])
        pairs.pop()
    return pairs


def generate_encoded_strings(pairs):
    encoded_strings = {}
    for i, senders in enumerate(pairs):
        for sender in senders:
            recipients = pairs[i + 1] if i < len(pairs) - 1 else pairs[0]
            sender_info = f"{sender}: Du er hemmelig pinsevenn med {' og '.join(s for s in senders if s != sender)}. Dere skal gi til {' og '.join(recipients)}."
            encoded_sender_info = base64.b64encode(sender_info.encode("utf-8")).decode(
                "utf-8"
            )
            encoded_strings[sender] = encoded_sender_info
    return encoded_strings


if __name__ == "__main__":
    # List of names
    names = [
        "Andreas",
        "Eivind",
        "Simen",
        "David L.",
        "David N.",
        "Kristian",
        "Erlend",
        "Jørgen",
    ]

    # Randomize the list
    random.shuffle(names)

    # Create pairs of names
    pairs = create_pairs(names)

    # Generate encoded strings
    encoded_strings = generate_encoded_strings(pairs)

    for name, encoded_info in encoded_strings.items():
        print(f"{name}: {encoded_info}")
