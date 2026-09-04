# ForgeSort

ForgeSort is a small Python utility for cleaning up folders by:

- organizing files into category folders based on extension
- detecting duplicate files in a folder

The current project includes a CLI implementation and an early FastAPI stub.

## Current CLI Functions

ForgeSort currently exposes two CLI flags:

### `--organize PATH`

Scans the given folder and moves top-level files into category folders such as:

- `Images`
- `Videos`
- `Audio`
- `Documents`
- `Spreadsheets`
- `Data`
- `Archives`
- `Installers`
- `Code`
- `Web`
- `Databases`
- `CAD & 3D`
- `Fonts`
- `System`
- `Settings`
- `Misc`

Files that do not match a known extension are moved into `Other Files`.

Example:

```bash
python -m cli.main_cli --organize "C:\Users\YourName\Downloads"
```

### `--checkdup PATH`

Scans the given folder for duplicate files.

Current behavior:

- only top-level files in the target folder are scanned
- files are grouped by size first, then verified with SHA-256 hashing
- duplicate files are reported in groups
- files are not deleted automatically

Example:

```bash
python -m cli.main_cli --checkdup "C:\Users\YourName\Documents"
```

## Installation

ForgeSort is not packaged as an installable command yet, so the current setup is source-based.

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd forge-sort
```

### 2. Create and activate a virtual environment

Windows:

```bash
py -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

For the current CLI:

```bash
pip install rich
```

If you also want to work on the API stub:

```bash
pip install fastapi pydantic
```

## Usage

Run ForgeSort from the repository root:

```bash
python -m cli.main_cli --organize "<folder>"
python -m cli.main_cli --checkdup "<folder>"
```

If you prefer the script path form, this also works:

```bash
python cli/main_cli.py --organize "<folder>"
python cli/main_cli.py --checkdup "<folder>"
```

## Notes

- The current CLI uses flags, not subcommands.
- Folder scanning is currently non-recursive.
- The API in `api/main_api.py` is still incomplete.

## Project Structure

```text
forge-sort/
|-- api/
|   `-- main_api.py
|-- cli/
|   `-- main_cli.py
|-- modules/
|   |-- file_extensions.py
|   `-- helper.py
`-- README.md
```
