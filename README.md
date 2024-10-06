# CLI Project Manager

This project is a simple CLI tool that helps manage multiple projects by allowing you to register, start, stop, and list projects easily from the command line. It is especially useful for developers working on multiple applications or services that need to be started and stopped frequently.

## Features

- **Register Projects**: Add projects to the CLI tool with a name, path, and command to run.
- **Start Projects**: Easily start any registered project with a single command.
- **Stop Projects**: Stop running projects gracefully.
- **List Projects**: View all registered projects and see which ones are currently running.
- **Logging**: Each project has separate log files for standard output and errors, allowing you to review details later.

## Installation

To use this tool on any machine, you can follow the steps below.

### Prerequisites

- Python 3.11 (or above) installed
- `click` and `psutil` Python libraries installed
- `poetry` for managing dependencies (optional)

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-folder>
```

### Step 2: Install Dependencies

If you are using `poetry`, you can install the required dependencies with the following command:

```bash
poetry install
```

Alternatively, you can use `pip` to install the dependencies manually:

```bash
pip install click psutil
```

### Step 3: Make the Script Executable

Add execution permissions to the `manage.py` script:

```bash
chmod +x manage.py
```

### Step 4: Set Up Global Command (Optional but Recommended)

To make the CLI tool easily accessible from anywhere, create a symbolic link:

```bash
sudo ln -s /path/to/your/manage.py /usr/local/bin/manage
```

This allows you to use the `manage` command globally in your terminal.

## Usage

Here are some common commands you can use with the CLI tool:

### Register a Project

You can register a new project by providing its name, path, and the command to run:

```bash
manage add --name "MyProject" --path "/path/to/project" --command "poetry run python app.py"
```

### List All Projects

To see a list of all registered projects and their current status:

```bash
manage list
```

### Start a Project

To start a project by its name:

```bash
manage start MyProject
```

The logs will be saved in `MyProject_log.txt` and `MyProject_error_log.txt` in the same directory.

### Stop a Project

To stop a running project:

```bash
manage stop MyProject
```

## Logging

- **Standard Output Log**: Each project saves its output to a log file named `<project_name>_log.txt`.
- **Error Log**: Errors are saved separately in `<project_name>_error_log.txt`.
- These log files are helpful for debugging purposes and understanding the project behavior.

## Example Workflow

1. **Register a project** called `MyWebApp`:
   ```bash
   manage add --name "MyWebApp" --path "/Users/username/projects/MyWebApp" --command "python app.py"
   ```
2. **Start** the project:
   ```bash
   manage start MyWebApp
   ```
3. **List** all projects to see which are running:
   ```bash
   manage list
   ```
4. **Stop** the project when you are done:
   ```bash
   manage stop MyWebApp
   ```

## Notes

- Make sure to use **absolute paths** when registering projects to avoid any confusion.
- **Symbolic links** are used to enable global access to the command; ensure `/usr/local/bin` is writable by using `sudo` if needed.
- For better privacy, add `projects.json` and all log files to `.gitignore` to avoid sharing potentially sensitive information on GitHub.

## .gitignore Setup

To prevent sensitive data from being included in your repository, add the following to your `.gitignore` file:

```gitignore
*.log
projects.json
```

## Contributing

Feel free to fork this repository and make changes. Pull requests are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
