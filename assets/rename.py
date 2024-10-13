import os

list = [
    'ai responses.png',
    'collection of files.png',
    'commands.png',
    'composer.png',
    'custom no code ai assistants.png',
    'file interactions.png',
    'make custom no code tools.png',
    'model cards.png',
    'nav-button.png',
    'pre-prompts.png',
    'presets.png',
    'quick settings.png',
    'shortcuts.png',
    'sidebar.png',
    'tts.png',
    'workspaces.png',
    'your profile.png',
]

for each in list:
    os.rename(each, each.replace(" ", "-"))

