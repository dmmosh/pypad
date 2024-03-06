
![2024-03-06_16-21](https://github.com/wettestsock/pypad/assets/119987092/abddbc2c-aa97-41c1-8458-201651364cf7)

A Python terminal, running over xterm, designed for calculator use. This is NOT a calculator, it is a terminal designed to maximize Python's calculating capabilities. Best used with a numpad, Pypad maximizes convenience. I like to see it as a TI-30 calculator: It will not solve the world, but ultimately it's always there. 

not numpy, because, well, that exists 

Pynput package is embedded, and the program is precompiled.

## Requirements: ##
- Linux
- Xterm
- Python

## Install: ## 
```
git clone https://github.com/wettestsock/pypad
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
Required packages:
- PyInstaller
- Pynput
In case the compiled executable does not work (like on MacOS), manually compile the files and run `./install.sh` again.
```
cd ./pypad
python -m PyInstaller --onefile src/pmain.py --name pypad
cd ..
```

