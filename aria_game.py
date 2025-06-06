#!/usr/bin/env python3
"""
ARIA: La couronne, le sceptre et l'orbe - interactive narrative.

A small console-based branching story inspired by dark visual novels.
Voiceover is not included due to environment limits.
"""

import os
import sys
import time


def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")


def play_line(line: str, delay: float = 0.03) -> None:
    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

ART_INTRO = r"""
    ____   ____   ____
   /\  _`\/\  _`\/\  _`\
   \ \ \L\_\ \ \L\_\ \ \,\L_\
    \ \  _\/\ \  _\/\ \ \/_/
     \ \ \/  \ \ \/  \ \ \L\ \
      \ \_\   \ \_\   \ \____/
       \/_/    \/_/    \/___/
"""

ART_CASTLE = r"""
      |>>>                        |>>>
      |                           |
  _  _|_  _                   _  _|_  _
 | |_| |_| |                 | |_| |_| |
 \  .      /                 \ .    .  /
  \______/                   \_______/
"""

ART_FOREST = r'''
   ^^      .-=-=-=-.  ^^
        .-'"""""`-.
      .'- ""--"""-.
     /.'             '\
'''

SCENES = {
    "intro": {
        "art": ART_INTRO,
        "lines": [
            "Vous vous réveillez dans une clairière plongée dans une ",
            "obscurité presque totale. Devant vous se dresse un château ",
            "oublié renfermant la couronne, le sceptre et l'orbe d'Aria.",
        ],
        "choices": [
            ("S'approcher du château", "castle"),
            ("Explorer la forêt", "forest"),
        ],
    },
    "castle": {
        "art": ART_CASTLE,
        "lines": [
            "Le château semble abandonné. Les portes grincent lorsque vous ",
            "les poussez, révélant un hall poussiéreux et sombre.",
        ],
        "choices": [
            ("Chercher la princesse", "princess"),
            ("Rebrousser chemin", "intro"),
        ],
    },
    "forest": {
        "art": ART_FOREST,
        "lines": [
            "Les arbres noirs se resserrent. Au loin, vous apercevez une ",
            "lueur tremblante et entendez une chanson douce.",
        ],
        "choices": [
            ("Suivre la lumière", "bard"),
            ("Retourner vers le château", "intro"),
        ],
    },
    "princess": {
        "art": ART_CASTLE,
        "lines": [
            "Vous trouvez une jeune femme enchaînée qui vous implore de la ",
            "libérer en échange de la couronne.",
        ],
        "choices": [
            ("La libérer", "free"),
            ("L'abandonner", "end"),
        ],
    },
    "bard": {
        "art": ART_FOREST,
        "lines": [
            "Un barde solitaire vous avertit que la princesse porte malheur.",
        ],
        "choices": [
            ("Ignorer l'avertissement", "castle"),
            ("Écouter le barde et partir", "end"),
        ],
    },
    "free": {
        "art": ART_CASTLE,
        "lines": [
            "En brisant ses chaînes, la princesse disparaît avec un rire ",
            "sourd, emportant les trésors d'Aria.",
        ],
        "choices": [],
    },
    "end": {
        "art": "",
        "lines": [
            "Votre aventure prend fin ici. Peut-être retenterez-vous...",
        ],
        "choices": [],
    },
}

def show_scene(key: str) -> str | None:
    clear_screen()
    scene = SCENES[key]
    art = scene.get("art", "")
    if art:
        print(art)
    for line in scene["lines"]:
        play_line(line)
    if not scene["choices"]:
        return None
    for idx, (text, _) in enumerate(scene["choices"], 1):
        print(f"{idx}. {text}")
    while True:
        choice = input("> ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(scene["choices"]):
                return scene["choices"][idx][1]
        print("Choix invalide. Essayez encore.")

def main() -> None:
    next_scene = "intro"
    while next_scene:
        next_scene = show_scene(next_scene)
    play_line("Merci d'avoir joué.")

if __name__ == "__main__":
    main()
