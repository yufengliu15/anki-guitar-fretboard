import os, csv

audioFiles = []
images = []

for image in os.listdir("./svgs"):
    if (image == ".DS_Store"):
        continue
    images.append(image)
    
for note in os.listdir("./audio"):
    audioFiles.append(note)

note_names = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']

images.sort()
audioFiles.sort()
audioFiles.remove(".DS_Store")

content = ["#separator:tab \n #html:true \n#tags column:4 \n 'F#'  [sound:blah] &lt;img src= &gt;"]

with open('notes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["ID", "Back", "Audio", "Image"]
    writer.writerow(field)
    for i in range(len(images)):
        writer.writerow([i, note_names[i], f'[sound:{audioFiles[i]}]', f"<img src=\"{images[i]}\">"])