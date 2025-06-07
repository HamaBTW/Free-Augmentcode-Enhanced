import sqlite3
import shutil
import time
import os
from utils.paths import get_db_path

def _create_backup(file_path: str) -> str:
    """
    Creates a backup of the specified file with timestamp.
    
    Args:
        file_path (str): Path to the file to backup
        
    Returns:
        str: Path to the backup file
        
    Format: <filename>.bak.<timestamp>
    """
    timestamp = int(time.time())
    backup_path = f"{file_path}.bak.{timestamp}"
    shutil.copy2(file_path, backup_path)
    return backup_path

def clean_augment_data(app: str = "vscode", portable_root: str = None) -> dict:
    """
    Cleans augment-related data from the SQLite database.
    Creates a backup before modification.
    
    Args:
        app (str): The application name ('vscode', 'cursor', or 'windsurf')
        portable_root (str, optional): The root directory for portable installations (used only for 'cursor')
    
    Returns:
        dict: A dictionary containing operation results
        {
            'db_backup_path': str,
            'deleted_rows': int
        }
    """
    db_path = get_db_path(app, portable_root)
    
    # Check if database exists
    if not os.path.exists(db_path):
        print(f"Warning: Database file not found at {db_path}")
        return {
            'db_backup_path': None,
            'deleted_rows': 0
        }
    
    # Create backup before modification
    db_backup_path = _create_backup(db_path)
    
    # Connect to the database
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Execute the delete query for augment-related data
        cursor.execute("DELETE FROM ItemTable WHERE key LIKE '%augment%'")
        deleted_rows = cursor.rowcount
        
        # Also clean up any other related data
        cursor.execute("DELETE FROM ItemTable WHERE key LIKE '%cursor%' AND key LIKE '%token%'")
        deleted_rows += cursor.rowcount
        
        # Commit the changes
        conn.commit()
        
        return {
            'db_backup_path': db_backup_path,
            'deleted_rows': deleted_rows
        }
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback()
        raise
    finally:
        # Always close the connection
        if conn:
            conn.close()