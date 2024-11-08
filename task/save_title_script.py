
def save_title_scripts(title, scripts, path):
    with open(path, "w") as file:
        file.write(f"{title}\n")
        file.write(f"{scripts}\n")
    print("title and scripts saved to: " +path)
