
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
```
cd ./pypad
python -m PyInstaller --onefile src/pmain.py --name pypad
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
![2024-03-06_16-55_1](https://github.com/wettestsock/pypad/assets/119987092/9c1531f9-80ba-4ce8-ac24-13b7daf6585f)
![2024-03-06_17-01](https://github.com/wettestsock/pypad/assets/119987092/a5647515-9eb8-4d98-b064-23e52a02e2fd)










