
![2024-03-06_16-21](https://github.com/wettestsock/pypad/assets/119987092/abddbc2c-aa97-41c1-8458-201651364cf7)

ultimate calculator for the numpad

not numpy, because, well, that exists

working on an install script

```
# to make the program work
touch $HOME/.pypad
sudo cp -r -T ./pypad/ /usr/share/pypad
sudo chown -R $USER /usr/share/pypad
```

python -m PyInstaller --onefile src/pmain.py --name pypad
