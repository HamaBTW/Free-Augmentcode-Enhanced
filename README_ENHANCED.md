# Free AugmentCode - Multi-IDE Edition

A powerful tool for managing and cleaning AugmentCode-related data across multiple IDEs. It allows you to log in with different accounts on the same computer without triggering account locks.

## 🌟 Features

### Multi-IDE Support
- **VS Code** - Full support for all versions
- **Cursor** - Both installed and portable versions
- **Windsurf** - Complete compatibility

### 🔄 Telemetry Management
- **ID Regeneration**
  - Reset device and machine IDs
  - Generate new random identifiers
  - Automatic backup of original IDs
  
### 🗃️ Database Maintenance
- **Smart Cleanup**
  - Remove AugmentCode-related entries
  - Clean authentication tokens
  - Automatic database backup
  - Cross-platform compatibility

### 📁 Workspace Management
- **Storage Cleanup**
  - Remove cached workspace data
  - Create zip backups before deletion
  - Handle read-only files safely

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- One of the supported IDEs installed

### Installation
```bash
git clone https://github.com/yourusername/free-augmentcode.git
cd free-augmentcode
pip install -r requirements.txt
```

## 💻 Usage

### Basic Commands
```bash
# For VS Code
python index.py --app vscode

# For Cursor (installed)
python index.py --app cursor

# For Windsurf
python index.py --app windsurf
```

### Advanced Options
```bash
# Portable Cursor installation
python index.py --app cursor --portable-root "D:\\path\\to\\cursor"

# Dry run (preview changes)
python index.py --app vscode --dry-run

# Show help
python index.py --help
```

## 🛠️ How It Works

1. **Backup Creation**
   - Creates timestamped backups of all modified files
   - Stores backups in the same directory as the original files

2. **ID Regeneration**
   - Updates telemetry IDs in storage files
   - Modifies machine ID files
   - Handles different ID formats across IDEs

3. **Database Cleaning**
   - Removes AugmentCode-related entries
   - Cleans authentication tokens
   - Maintains database integrity

4. **Workspace Cleanup**
   - Creates zip archive of workspace storage
   - Safely removes cached data
   - Handles file permissions correctly

## 📝 Notes

- Always close your IDE before running this tool
- Backups are created automatically with timestamps
- The tool will skip non-existent paths gracefully
- Use `--dry-run` to preview changes before applying them

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
