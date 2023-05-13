import yaml
from yaml.loader import SafeLoader

# Load moods from the moods.yaml file

moods = yaml.load(open("moods.yaml"), Loader=SafeLoader)
# Default mood is the first one
current_mood = list(moods.keys())[0]


# Get the current mood globally
def get_mood():
    return current_mood


# Set the current mood globally
def set_mood(mood):
    global current_mood
    current_mood = mood
