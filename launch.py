import os, random

# TODO load dirs from JSON

# TODO automatically find subdirs if no JSON an save
directory = [
    r'A:\videos\Animated\MMD', 
    r'A:\videos\PMV'
    ]


d = []

for i in range(0, len(directory)):
    f = []
    for root, dirs, files in os.walk(directory[i]):
        for file in files:
            if os.path.splitext(file)[1] == '.mp4':
                f.append(os.path.join(root,file))
    d.append(f)

if len(d) == 0: print("No videos found")

for i in range(0, len(d)):
    r = d[i][random.randint(0, len(d[i]))]
    print(r)
    os.startfile(r)

# os.startfile()