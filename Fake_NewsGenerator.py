import random

subjects = [
    "Aliens", "Talking cats", "Time travelers", "Robots", 
    # "Dinosaurs", "Flying cars", "Ghosts", "Giant pandas"
]

actions = [
    "take over", "accidentally destroy", "mysteriously visit",
    # "announce plan to buy", "challenge humans to", "secretly build"
]

objects = [
    "the moon", "the internet", "all smartphones", 
#     "the world’s largest pizza", "the White House", "Mount Everest"
]

details = [
    "officials confirm", "scientists shocked", 
    "public confused", "complete chaos starts",
    # "world reacts instantly", "experts still investigating"
]

def generate_fake_news():
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    detail = random.choice(details)
    
    return f"{subject} {action} {obj}, {detail}!"

for _ in range(5):
    print(generate_fake_news())
