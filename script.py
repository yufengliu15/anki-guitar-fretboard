from fretboardgtr.fretboard import FretBoard, FretBoardConfig, FretBoardElement
from fretboardgtr.notes_creators import ScaleFromName

config = {
    "general": {
        "first_fret": 0,
        "last_fret": 22,
        "show_tuning": False,
        "show_frets": False,
        "show_note_name": False,
        "fretted_color_scale": True,
        "fretted_colors": {
            "root": "rgb(255,255,255)",
        },
        "open_colors": {
            "root": "rgb(255,255,255)",
        },
        "enharmonic": True,
    },
    "background": {"color": "rgb(0,0,50)", "opacity": 0.4},
    "frets": {"color": "rgb(150,150,150)"},
    "strings": {"color": "rgb(200,200,200)", "width": 2},
}

dir = "./svgs/"
notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
starting_note = 7
fretboard_config = FretBoardConfig.from_dict(config)

for string in range(6):
    for fret in range(12):
        fretboard = FretBoard(config=fretboard_config)
        fretboard.add_note(string, notes[fret])
        fretboard.export(dir+str(string+1)+"-"+str((starting_note-2)%12)+notes[fret]+".svg", format="svg")
        starting_note = (starting_note + 1) % 12
    
    # fourth intervals!
    if (string == 1):
        starting_note = (starting_note + 4) % 12
    else:
        starting_note = (starting_note + 5) % 12