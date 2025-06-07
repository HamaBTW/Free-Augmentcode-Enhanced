import os
import sys
from pathlib import Path


def get_home_dir() -> str:
    """
    Get the user's home directory across different platforms.
    
    Returns:
        str: Path to the user's home directory
    """
    return str(Path.home())


def get_app_data_dir() -> str:
    """
    Get the application data directory across different platforms.
    
    Returns:
        str: Path to the application data directory
        
    Platform specific paths:
        - Windows: %APPDATA% (typically C:\\Users\\<username>\\AppData\\Roaming)
        - macOS: ~/Library/Application Support
        - Linux: ~/.local/share
    """
    if sys.platform == "win32":
        # Windows
        return os.getenv("APPDATA", "")
    elif sys.platform == "darwin":
        # macOS
        return os.path.join(str(Path.home()), "Library/Application Support")
    else:
        # Linux and other Unix-like systems
        return os.path.join(str(Path.home()), ".local/share")


def get_storage_path(app: str = "vscode", portable_root: str = None) -> str:
    """
    Get the storage.json path across different platforms and applications.
    
    Args:
        app (str): The application name ('vscode', 'cursor', or 'windsurf')
        portable_root (str, optional): The root directory for portable installations (used only for 'cursor')
        
    Returns:
        str: Path to the storage.json file
        
    Platform specific paths for VS Code:
        - Windows: %APPDATA%/Code/User/globalStorage/storage.json
        - macOS: ~/Library/Application Support/Code/User/globalStorage/storage.json
        - Linux: ~/.config/Code/User/globalStorage/storage.json
        
    For Cursor (portable):
        <portable_root>/.cursor/User/globalStorage/storage.json
    """
    app = app.lower()
    if app not in {"vscode", "cursor", "windsurf"}:
        raise ValueError("Unsupported app. Choose from 'vscode', 'cursor', or 'windsurf'.")

    # Define app-specific folder names
    if app == "vscode":
        folder = "Code"
    elif app == "cursor":
        folder = "Cursor"
    elif app == "windsurf":
        folder = "Windsurf"

    # Handle portable Cursor installation
    if portable_root and app == "cursor":
        return os.path.join(portable_root, ".cursor", "User", "globalStorage", "storage.json")

    if sys.platform == "win32":
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, folder, "User", "globalStorage", "storage.json")
    elif sys.platform == "darwin":
        return os.path.join(str(Path.home()), "Library", "Application Support", folder, "User", "globalStorage", "storage.json")
    else:
        return os.path.join(str(Path.home()), ".config", folder, "User", "globalStorage", "storage.json")


def get_db_path(app: str = "vscode", portable_root: str = None) -> str:
    """
    Get the state.vscdb path across different platforms and applications.
    
    Args:
        app (str): The application name ('vscode', 'cursor', or 'windsurf')
        portable_root (str, optional): The root directory for portable installations (used only for 'cursor')
        
    Returns:
        str: Path to the state.vscdb file
        
    Platform specific paths for VS Code:
        - Windows: %APPDATA%/Code/User/globalStorage/state.vscdb
        - macOS: ~/Library/Application Support/Code/User/globalStorage/state.vscdb
        - Linux: ~/.config/Code/User/globalStorage/state.vscdb
        
    For Cursor (portable):
        <portable_root>/.cursor/User/globalStorage/state.vscdb
    """
    app = app.lower()
    if app not in {"vscode", "cursor", "windsurf"}:
        raise ValueError("Unsupported app. Choose from 'vscode', 'cursor', or 'windsurf'.")

    # Define app-specific folder names
    if app == "vscode":
        folder = "Code"
    elif app == "cursor":
        folder = "Cursor"
    elif app == "windsurf":
        folder = "Windsurf"

    # Handle portable Cursor installation
    if portable_root and app == "cursor":
        return os.path.join(portable_root, ".cursor", "User", "globalStorage", "state.vscdb")

    if sys.platform == "win32":
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, folder, "User", "globalStorage", "state.vscdb")
    elif sys.platform == "darwin":
        return os.path.join(str(Path.home()), "Library", "Application Support", folder, "User", "globalStorage", "state.vscdb")
    else:
        return os.path.join(str(Path.home()), ".config", folder, "User", "globalStorage", "state.vscdb")


def get_machine_id_path(app: str = "vscode", portable_root: str = None) -> str:
    """
    Get the machine ID file path across different platforms and applications.
    
    Args:
        app (str): The application name ('vscode', 'cursor', or 'windsurf')
        portable_root (str, optional): The root directory for portable installations (used only for 'cursor')
        
    Returns:
        str: Path to the machine ID file
        
    Platform specific paths for VS Code:
        - Windows: %APPDATA%/Code/User/machineid
        - macOS: ~/Library/Application Support/Code/User/machineid
        - Linux: ~/.config/Code/User/machineid
        
    For Cursor (portable):
        <portable_root>/.cursor/User/machineid
    """
    app = app.lower()
    if app not in {"vscode", "cursor", "windsurf"}:
        raise ValueError("Unsupported app. Choose from 'vscode', 'cursor', or 'windsurf'.")

    # Define app-specific folder names
    if app == "vscode":
        folder = "Code"
    elif app == "cursor":
        folder = "Cursor"
    elif app == "windsurf":
        folder = "Windsurf"

    # Handle portable Cursor installation
    if portable_root and app == "cursor":
        return os.path.join(portable_root, ".cursor", "User", "machineid")

    if sys.platform == "win32":
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, "Code", "User", "machineid")
    elif sys.platform == "darwin":
        # macOS
        return os.path.join(str(Path.home()), "Library", "Application Support", "Code", "machineid")
    else:
        # Linux and other Unix-like systems
        return os.path.join(str(Path.home()), ".config", "Code", "machineid")


def get_workspace_storage_path(app: str = "vscode", portable_root: str = None) -> str:
    """
    Get the workspaceStorage path across different platforms and applications.
    
    Args:
        app (str): The application name ('vscode', 'cursor', or 'windsurf')
        portable_root (str, optional): The root directory for portable installations (used only for 'cursor')
        
    Returns:
        str: Path to the workspaceStorage directory
        
    Platform specific paths for VS Code:
        - Windows: %APPDATA%/Code/User/workspaceStorage
        - macOS: ~/Library/Application Support/Code/User/workspaceStorage
        - Linux: ~/.config/Code/User/workspaceStorage
        
    For Cursor (portable):
        <portable_root>/.cursor/User/workspaceStorage
    """
    app = app.lower()
    if app not in {"vscode", "cursor", "windsurf"}:
        raise ValueError("Unsupported app. Choose from 'vscode', 'cursor', or 'windsurf'.")

    # Define app-specific folder names
    if app == "vscode":
        folder = "Code"
    elif app == "cursor":
        folder = "Cursor"
    elif app == "windsurf":
        folder = "Windsurf"

    # Handle portable Cursor installation
    if portable_root and app == "cursor":
        return os.path.join(portable_root, ".cursor", "User", "workspaceStorage")

    if sys.platform == "win32":
        base_path = os.getenv("APPDATA", "")
        return os.path.join(base_path, folder, "User", "workspaceStorage")
    elif sys.platform == "darwin":
        return os.path.join(str(Path.home()), "Library", "Application Support", folder, "User", "workspaceStorage")
    else:
        return os.path.join(str(Path.home()), ".config", folder, "User", "workspaceStorage") 