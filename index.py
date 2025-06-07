import argparse
import sys
import os
from pathlib import Path
from utils.paths import get_home_dir, get_app_data_dir, get_storage_path, get_db_path, get_machine_id_path, get_workspace_storage_path
from augutils.json_modifier import modify_telemetry_ids
from augutils.sqlite_modifier import clean_augment_data
from augutils.workspace_cleaner import clean_workspace_storage

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    """Display the application header."""
    header = """
╔══════════════════════════════════════════════════╗
║             FREE AUGMENTCLEANER                 ║
║        Clean AugmentCode Data Across IDEs       ║
╚══════════════════════════════════════════════════╝
    """
    print(header)

def select_ide():
    """Display IDE selection menu and get user choice."""
    while True:
        clear_screen()
        display_header()
        print("\nSelect IDE to clean:")
        print("1. VS Code")
        print("2. Cursor (Installed)")
        print("3. Cursor (Portable)")
        print("4. Windsurf")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            return 'vscode', None
        elif choice == '2':
            return 'cursor', None
        elif choice == '3':
            portable_path = input("\nEnter path to portable Cursor installation: ").strip('"')
            if not os.path.isdir(portable_path):
                input("\n❌ Invalid path. Press Enter to try again...")
                continue
            return 'cursor', portable_path
        elif choice == '4':
            return 'windsurf', None
        elif choice == '5':
            print("\nExiting...")
            sys.exit(0)
        else:
            input("\n❌ Invalid choice. Press Enter to try again...")

def main():
    # Check for command line arguments first
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print("\nUsage:")
        print("  python index.py [--app vscode|cursor|windsurf] [--portable-root PATH] [--dry-run]")
        print("\nOptions:")
        print("  --app           IDE to clean (vscode, cursor, windsurf)")
        print("  --portable-root Path to portable Cursor installation")
        print("  --dry-run       Show what would be done without making changes")
        print("\nIf no arguments are provided, an interactive menu will be shown.")
        sys.exit(0)
    
    # If command line arguments are provided, use them
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description='Clean AugmentCode data for different IDEs')
        parser.add_argument('--app', type=str, choices=['vscode', 'cursor', 'windsurf'], default='vscode',
                          help='The IDE to clean (default: vscode)')
        parser.add_argument('--portable-root', type=str, default=None,
                          help='Root directory for portable installations (used only for \'cursor\')')
        parser.add_argument('--dry-run', action='store_true',
                          help='Show what would be done without making any changes')
        
        args = parser.parse_args()
        app = args.app.lower()
        portable_root = args.portable_root
        dry_run = args.dry_run
    else:
        # Interactive mode
        app, portable_root = select_ide()
        dry_run = False
    
    clear_screen()
    display_header()
    print(f"\n🛠️  Cleaning AugmentCode data for {app.upper()}")
    if app == 'cursor' and portable_root:
        print(f"📁 Using portable Cursor installation at: {portable_root}")
    
    if dry_run:
        print("\n🔍 Dry run - no changes will be made")
    
    try:
        # Show paths that will be affected
        print("\n📂 System Paths:")
        print(f"🏠 Home Directory: {get_home_dir()}")
        print(f"📁 App Data Directory: {get_app_data_dir()}")
        print(f"💾 Storage Path: {get_storage_path(app, portable_root)}")
        print(f"🗃️  DB Path: {get_db_path(app, portable_root)}")
        print(f"🆔 Machine ID Path: {get_machine_id_path(app, portable_root)}")
        print(f"📦 Workspace Storage Path: {get_workspace_storage_path(app, portable_root)}")
        
        if dry_run:
            print("\n✅ Dry run complete. No changes were made.")
            input("\nPress Enter to exit...")
            return
        
        # Ask for confirmation
        print("\n⚠️  WARNING: This will modify your IDE's data.")
        confirm = input("Do you want to continue? (y/n): ").strip().lower()
        if confirm != 'y':
            print("\nOperation cancelled by user.")
            sys.exit(0)
            
        print("\n🔄 Modifying Telemetry IDs...")
        result = modify_telemetry_ids(app, portable_root)
        print("\n✅ Backups created at:")
        print(f"   • Storage backup: {result['storage_backup_path']}")
        if result['machine_id_backup_path']:
            print(f"   • Machine ID backup: {result['machine_id_backup_path']}")
        
        print("\n🔍 Old IDs:")
        print(f"   • Machine ID: {result['old_machine_id']}")
        print(f"   • Device ID: {result['old_device_id']}")
        
        print("\n✨ New IDs:")
        print(f"   • Machine ID: {result['new_machine_id']}")
        print(f"   • Device ID: {result['new_device_id']}")
        
        print("\n🧹 Cleaning SQLite Database...")
        db_result = clean_augment_data(app, portable_root)
        print(f"✅ Database backup created at: {db_result['db_backup_path']}")
        print(f"   • Deleted {db_result['deleted_rows']} rows containing 'augment' in their keys")
        
        print("\n🧽 Cleaning Workspace Storage...")
        ws_result = clean_workspace_storage(app, portable_root)
        if ws_result['backup_path']:
            print(f"✅ Workspace backup created at: {ws_result['backup_path']}")
            print(f"   • Deleted {ws_result['deleted_files_count']} files from workspace storage")
        else:
            print("ℹ️  No workspace storage found to clean")
        
        print(f"\n🎉 Success! You can now run {app.upper()} and log in with a new account.")
        print("\n💡 Note: If you're using VS Code, you might need to restart it for changes to take effect.")
        
        input("\nPress Enter to exit...")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()