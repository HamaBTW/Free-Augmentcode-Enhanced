import argparse
import sys
from utils.paths import get_home_dir, get_app_data_dir, get_storage_path, get_db_path, get_machine_id_path, get_workspace_storage_path
from augutils.json_modifier import modify_telemetry_ids
from augutils.sqlite_modifier import clean_augment_data
from augutils.workspace_cleaner import clean_workspace_storage

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Clean AugmentCode data for different IDEs')
    parser.add_argument('--app', type=str, choices=['vscode', 'cursor', 'windsurf'], default='vscode',
                      help='The IDE to clean (default: vscode)')
    parser.add_argument('--portable-root', type=str, default=None,
                      help='Root directory for portable Cursor installation (only for --app cursor)')
    parser.add_argument('--dry-run', action='store_true',
                      help='Show what would be done without making any changes')
    
    args = parser.parse_args()
    
    print(f"Cleaning AugmentCode data for {args.app.upper()}")
    if args.app == 'cursor' and args.portable_root:
        print(f"Using portable Cursor installation at: {args.portable_root}")
    
    if args.dry_run:
        print("\nDry run - no changes will be made")
    
    try:
        # Show paths that will be affected
        print("\nSystem Paths:")
        print(f"Home Directory: {get_home_dir()}")
        print(f"App Data Directory: {get_app_data_dir()}")
        print(f"Storage Path: {get_storage_path(args.app, args.portable_root)}")
        print(f"DB Path: {get_db_path(args.app, args.portable_root)}")
        print(f"Machine ID Path: {get_machine_id_path(args.app, args.portable_root)}")
        print(f"Workspace Storage Path: {get_workspace_storage_path(args.app, args.portable_root)}")
        
        if args.dry_run:
            print("\nDry run complete. No changes were made.")
            return
            
        print("\nModifying Telemetry IDs:")
        result = modify_telemetry_ids(args.app, args.portable_root)
        print("\nBackup created at:")
        print(f"Storage backup path: {result['storage_backup_path']}")
        if result['machine_id_backup_path']:
            print(f"Machine ID backup path: {result['machine_id_backup_path']}")
        
        print("\nOld IDs:")
        print(f"Machine ID: {result['old_machine_id']}")
        print(f"Device ID: {result['old_device_id']}")
        
        print("\nNew IDs:")
        print(f"Machine ID: {result['new_machine_id']}")
        print(f"Device ID: {result['new_device_id']}")
        
        print("\nCleaning SQLite Database:")
        db_result = clean_augment_data(args.app, args.portable_root)
        print(f"Database backup created at: {db_result['db_backup_path']}")
        print(f"Deleted {db_result['deleted_rows']} rows containing 'augment' in their keys")
        
        print("\nCleaning Workspace Storage:")
        ws_result = clean_workspace_storage(args.app, args.portable_root)
        print(f"Workspace backup created at: {ws_result['backup_path']}")
        print(f"Deleted {ws_result['deleted_files_count']} files from workspace storage")
        
        print(f"\nNow you can run {args.app.upper()} and login with the new email.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()