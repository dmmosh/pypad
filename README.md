
![2024-03-06_16-21](https://github.com/wettestsock/pypad/assets/119987092/abddbc2c-aa97-41c1-8458-201651364cf7)

A Python terminal, running over xterm, designed for calculator use. This is NOT a calculator, it is a terminal designed to maximize Python's calculating capabilities. Best used with a numpad, Pypad maximizes convenience. I like to see it as a TI-30 calculator: It will not solve the world, but ultimately it's always there. 

not numpy, because, well, that exists 

Highly customizable, with a full settings page and serialization in effect.

Pynput package is embedded, and the program is precompiled.

## Requirements: ##
- Linux
- Xterm
- Python

## Install: ## 
```
git clone https://github.com/dmmosh/pypad
cd ./pypad
chmod +x ./install.sh
./install.sh
cd ..
```

## Uninstall: ## 
```
cd ./pypad
sudo ./uninstall.sh
cd ..
```

## Manual compiling: ##
In case you have an older glibc, or any compiled executable errors, you need to recompile the executable and run these commands.
Please make sure to install pynput before compiling. You can remove it after compiling.
```
cd ./pypad
python -m PyInstaller --hidden-import tkinter --onefile src/pmain.py --name pypad
sudo ./uninstall.sh
./install.sh
cd ..
```
In case the compiled executable does not work (like on MacOS), manually compile the files and run `./install.sh` again.

Required packages:
- PyInstaller
- Pynput

## Images: ##
![2024-03-06_16-51](https://github.com/wettestsock/pypad/assets/119987092/4c2fe94b-5c9d-49f6-965e-b65611ea06f2)
![2024-03-06_16-53](https://github.com/wettestsock/pypad/assets/119987092/2b09fad4-5028-4fcf-aa5d-3684cfccd5eb)
![2024-03-06_16-54](https://github.com/wettestsock/pypad/assets/119987092/a7c6cc9f-e7fc-4e1e-9862-752027b25dc2)
![2024-03-06_16-55](https://github.com/wettestsock/pypad/assets/119987092/8a1eac9a-ca10-4230-8144-43ea29d10d89)
![2024-03-06_16-56](https://github.com/wettestsock/pypad/assets/119987092/821fb358-693a-474d-8d95-c671889e154d)
![2024-03-06_16-57](https://github.com/wettestsock/pypad/assets/119987092/9a73e4f0-f0a5-4eb1-a4b1-5ef5f765afae)
![2024-03-06_16-58](https://github.com/wettestsock/pypad/assets/119987092/3fbae51b-9449-4ce1-9b5c-46794878a10d)
![2024-03-06_16-59](https://github.com/wettestsock/pypad/assets/119987092/26f62e42-0523-4b25-aa1a-77e10e477ac6)
![2024-03-15_14-27](https://github.com/dmmosh/pypad/assets/119987092/0a36d5d5-8e11-4074-a928-0b0c066a7a70)
![2024-03-15_13-56](https://github.com/dmmosh/pypad/assets/119987092/0a5c1d0b-4e7b-4ae8-8b2c-811a1f8cfda1)
![2024-03-15_14-31](https://github.com/dmmosh/pypad/assets/119987092/5abe5f9b-81ab-4112-ab4c-48285133fef2)
![2024-03-15_14-05](https://github.com/dmmosh/pypad/assets/119987092/7d551925-6ff2-4b3f-8c39-07b27bebd754)
![2024-03-15_14-41](https://github.com/dmmosh/pypad/assets/119987092/1f99bbf5-fc4a-418a-932d-9037c7d6a365)
![2024-03-15_14-15](https://github.com/dmmosh/pypad/assets/119987092/cb63e0b7-65d6-40fb-883d-4f50f11db73f)










