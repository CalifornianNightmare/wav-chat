from app.pipe import pipeline
from app.denoise.denoise import reduce_file_noise

from pathlib import Path
from clear_screen import clear


def main_menu():
    options = ["Select a WAV", "Clean WAV noise", "About", "Exit"]

    clear()
    print("Select an option:\n")

    goodbye = False

    while not goodbye:

        [print(f"{n}: {options[n]}") for n in range(len(options))]
        menu_entry_index = input("\n-> ")

        if menu_entry_index == "0":
            goodbye = continue_question(WAVselect())
        elif menu_entry_index == "1":
            goodbye = continue_question(noise_cancel())
        elif menu_entry_index == "2":
            about()
        elif menu_entry_index == "3":
            clear()
            print("Goodbye")
            goodbye = True
        else:
            clear()
            print("Incorect option. Please select:\n")


def WAVselect():
    filelist = [name for name in Path("files").glob("*.wav")]
    options = [filename.stem + ".wav" for filename in filelist]
    
    clear()
    print(f"Found {len(filelist)} files. Choose:\n")

    [print(f"{n}: {options[n]}") for n in range(len(options))]
    menu_entry_index = input("\n-> ")

    try:
        menu_entry_index_i = int(menu_entry_index)
    except ValueError:
        return 'Not a number.'
    
    try:
        filename = options[menu_entry_index_i]
    except IndexError:
        return 'Not an option.'

    output_path = pipeline(f"files/{filename}")
    return f"Response file saved at: {output_path}."


def continue_question(text: str):
    options = ["Yes", "No"]

    clear()
    print(text + "\n\nContinue?\n")

    [print(f"{n}: {options[n]}") for n in range(len(options))]

    menu_entry_index = input("\n-> ")
    clear()
    
    if menu_entry_index == "1":
        print("Goodbye")
        return True
    else:
        print("Select an option:\n")
        return False


def noise_cancel():
    filelist = [name for name in Path("files").glob("*.wav")]
    options = [filename.stem + ".wav" for filename in filelist]
    
    clear()
    print(f"Found {len(filelist)} files. Choose:\n")

    [print(f"{n}: {options[n]}") for n in range(len(options))]
    menu_entry_index = input("\n-> ")

    try:
        menu_entry_index_i = int(menu_entry_index)
    except ValueError:
        return 'Not a number.'
    
    try:
        filename = options[menu_entry_index_i]
    except IndexError:
        return 'Not an option.'

    reduce_file_noise(f"files/{filename}")
    return f"{filename} denoised succesfully"

def about():
    title = (
        "This app will listen to the input audio file and generate an output answer\n"
        "You also have the option to reduce noise on audio and save\n"
        "WAV files are taken out of /files/ folder\n"
        "Installation steps are described in README.md\n\n"
        "any: Okay"
    )

    clear()
    print(title)
    input("\n-> ")
    clear()
    print("Select an option:\n")