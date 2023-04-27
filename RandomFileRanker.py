import sys
import os
import random
import shutil

dirs = []

fav_dirs = {}


class Random_File:
    def __init__(self):
        self.dir: str = random.choice(dirs)
        self.file: str = random.choice(os.listdir(self.dir))
        self.path: str = f"{self.dir}/{self.file}"

    def open(self):
        os.startfile(self.path)
        print(f"\nOpened {self.file} in\n{self.dir}\n")
        if len(fav_dirs) == 0:
            print("No favorite directories in this file")
            return
        feedback: str = input("Rating (1-5): ")
        rating: str = int(-1 if feedback == "" else feedback)
        new_path: str = fav_dirs.get(rating, "No rating")

        if new_path == "No rating":
            print("No rating given")
            return

        shutil.move(self.path, new_path)
        print(f"Moved {self.file} to {new_path}")
        return

def main():
    if len(dirs) == 0:
        print("No directory paths in this file")
        sys.exit()

    while input("\nOpen file? (y/n): ") == "y":
        Random_File().open()
    print("\n")
    sys.exit()


if __name__ == "__main__":
    main()