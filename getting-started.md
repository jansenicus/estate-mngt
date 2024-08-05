### Python 3.12.4
#### Install and Activate Python 3.12.4 in the Current Directory

```bash
pyenv install --skip-existing 3.12.4
pyenv local 3.12.4
```
#### Enter Python 3.12.4
open detached terminal (not-integrated terminal in VS-Code)
to make sure python 3.12.4 is activated in the current directory
```bash
python
```

it should show
```
Python 3.12.4 (main, Jul  8 2024, 20:00:34) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
#### Exit Python 3.12.4
type `exit()` to exit the python and back to terminal prompt
 ```
 Python 3.12.4 (main, Jul  8 2024, 20:00:34) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
 ```

 #### Create Virtual Environment Based on Python 3.12.4
 ```
 python -m venv .venv
 ```

 #### Automatically load the virtual Environment in VS Code

 create `.vscode` directory, and `settings.json` that contains:
 ```json
 {
    "python.terminal.activateEnvInCurrentTerminal": true,
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"
}
 ```
 Try `fish` terminal or any other terminal in VS Code: `powershell`, `zsh`, `bash`

#### Install Requirements

```
pip install -r requirements/local.txt
```

# Docker

### Create Docker Network
```
make net
```
### Build Docker Image
```
make build
```
