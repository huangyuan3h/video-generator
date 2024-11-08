
def save_title_scripts(title, scripts, path):
    with open("example.txt", "w") as file:
        file.write(f"{title}\n")
        file.write(f"{scripts}\n")
    print("title and scripts saved to: " +path)
