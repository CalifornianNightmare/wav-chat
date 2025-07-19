from app.pipe import pipeline

from pathlib import Path
from clear_screen import clear
from simple_term_menu import TerminalMenu


def main_menu():
    clear()

    options = ["Select a WAV", "Clean WAV noise", "About", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0:
        WAVselect()
    if menu_entry_index == 1:
        noise_cancel()
    if menu_entry_index == 2:
        about()
    if menu_entry_index == 3:
        print("Goodbye")


def WAVselect():
    filelist = [name for name in Path("files").glob("*.wav")]
    options = [filename.stem + ".wav" for filename in filelist]
    terminal_menu = TerminalMenu(options, title=f"Found {len(filelist)} files. Choose:")
    menu_entry_index = terminal_menu.show()

    filename = options[menu_entry_index]

    output_path = pipeline(f"files/{filename}")
    continue_question(f"Response file saved at: {output_path}.")


def continue_question(text: str):
    options = ["Yes", "No"]
    terminal_menu = TerminalMenu(options, title=text + "\n\nContinue?")
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0:
        main_menu()
    if menu_entry_index == 1:
        print("Goodbye")


def noise_cancel():
    main_menu()
    # Не сейчас


def about():
    title = (
        "This app will listen to the input audio file and generate an output answer\n"
        "You also have the option to reduce noise on audio and save\n"
        "WAV files are taken out of /files/ folder\n"
        "Installation steps are described in README.md\n"
    )

    options = ["Okay"]
    terminal_menu = TerminalMenu(options, title=title)
    terminal_menu.show()

    main_menu()
