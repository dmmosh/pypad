#!/bin/bash

: '
INSTALL SCRIPT FOR PYPAD
'



# GET DEPENDENCIES (linux and macos)

# Determine OS name
os="$(uname)" # default for macos
# Desktop manager
pkg_manager=""

#finds linux distro
if [ -f /etc/os-release ]
then
    source "/etc/os-release"
    os=$ID

# checks if it's android
elif [ ! -z "$(echo $TERMUX_VERSION)" ]
then
    os="android"
fi


# IF LINUX - FIND THE DISTRO
#TODO: dont forget to add sudo
case "$os" in
    # ARCH
    arch)
    pkg_manager="yay -S"        
    ;;

    # MANJARO
    manjaro)
    pkg_manager="sudo pacman -Sy"
    ;;

    # UBUNTU AND DLINUX MINT
    ubuntu | linuxmint)
    pkg_manager="sudo apt install"
    ;;

    # FEDORA
    fedora)
    pkg_manager="sudo dnf install"
    ;;

    # RASBERRY PI
    raspbian)
    pkg_manager="sudo apt-get install"
    ;;

    # CENT OS
    centos)
    pkg_manager="yum -y install"
    ;;

    # MACOS
    Darwin)
    # if brew isn't installed, install it
    if [ -z "$(command -v brew)" ] 
    then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    pkg_manager="brew install"
    ;;

    # android
    android)
    pkg_manager="pkg install"
    ;;
    
esac



# have to do sudo user for linux whereas macos keeps it at home variable

# if os is supported, install the dependencies
if [ ! -z "$pkg_manager" ] && [ -z "$(command -v xterm)" ] 
then
    eval "$pkg_manager xterm"
fi

# checking if dependencies are installed 
if [ -z "$(command -v xterm)" ]
then
    echo -e "FATAL ERROR:"
    echo -e "   xterm not found.\n   Please install xterm and run 'sudo ./$(basename "$0")' again."
    exit 1
fi

# IF PYTHON IS NOT INSTALLED
if [ ! -f "usr/bin/python" ] && [ -z "$(command -v python)" ] && [ -z "$(command -v python3)" ]
then
    echo -e "ALMOST FATAL ERROR:"
    echo -e "   Python not installed.\n"
    read -p "Install Python (y/n)? " install_python
    case "$install_python" in 
        y|Y|yes|YES|Yes|yEs|yeS ) eval "$pkg_manager python";;
        * ) exit 1 ;;
    esac
fi

[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@"

home_dir="$HOME"

# for linux
# find user home dir
if [ ! "$os" == "Darwin" ]
then
home_dir="/home/${SUDO_USER}"
fi


chmod +x "./dist/pypad"
chmod +x "./src/pypad.desktop"
chmod +x "./uninstall.sh"

echo -e "COPYING HELPER FILES..."
sudo cp -r -T "./pypad/" "/usr/share/pypad"
sudo chown -R "${SUDO_USER}" "/usr/share/pypad"


echo -e "COMPILING THE EXECUTABLE..."
eval "./pyinstaller --onefile src/pmain.py && mv dist/pmain dist/pypad;"

echo -e "COPYING THE EXECUTABLE..."
sudo mv "./dist/pypad" "/usr/bin/pypad"
rm -rf './build'
rm -rf './dist'
rm 'pmain.spec'



# different installation for macosdvsvdfsdsffdsfsfds
#linux only
if [ ! "$os" == "Darwin" ]
then
    # for linux
    echo -e "COPYING THE .DESKTOP FILE..."
    sudo cp -r "./src/pypad.desktop" "/usr/share/applications"
fi