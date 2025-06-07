import os
import sys
from pathlib import Path

def get_db_path(app: str = "vscode", portable_root: str = None) -> str:
    """
    Get the path to the state.vscdb file for the specified application.

    Args:
        app (str): The application name. Options are 'vscode', 'cursor', or 'windsurf'.
        portable_root (str, optional): The root directory for portable installations (used only for 'cursor').

    Returns:
        str: Path to the state.vscdb file.
    """
    app = app.lower()
    if app not in {"vscode", "cursor", "windsurf"}:
        raise ValueError("Unsupported app. Choose from 'vscode', 'cursor', or 'windsurf'.")

    if app == "vscode":
        folder = "Code"
    elif app == "cursor":
        folder = "Cursor"
    elif app == "windsurf":
        folder = "Windsurf"

    if portable_root and app == "cursor":
        return os.path.join(portable_root, ".cursor", "User", "globalStorage", "state.vscdb")

    if sys.platform == "win32":
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, folder, "User", "globalStorage", "state.vscdb")
    elif sys.platform == "darwin":
        return os.path.join(str(Path.home()), "Library", "Application Support", folder, "User", "globalStorage", "state.vscdb")
    else:
        return os.path.join(str(Path.home()), ".config", folder, "User", "globalStorage", "state.vscdb")


# Example usage
print("== Example Usage ==")
print("Path to state.vscdb for different applications:")
print("vscode:", get_db_path("vscode"))
print("cursor:", get_db_path("cursor"))
print("windsurf:", get_db_path("windsurf"))
print("\n== Portable Installation ==")
print(get_db_path("cursor", portable_root="/path/to/workspace"))  # Cursor portable installation


