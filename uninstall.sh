#!/bin/bash

# UNINSTALLER 

# ask for sudo permissions

# ROOT PERMISSIONS

if [ ! "$UID" -eq 0 ] 
then
    echo -e "FATAL ERROR:"
    echo -e "   Can't uninstall without root permissions."
    echo -e "   Please run 'sudo ./$(basename "$0")'."
    exit 1
fi



os="$(uname)"

home_dir="$HOME"

# for linux
# find user home dir
if [ ! "$os" == "Darwin" ]
then
home_dir="/home/${SUDO_USER}"
fi



echo -e "DELETING HELPER FOLDER..."
rm -rf "/usr/share/pypad"


echo -e "DELETING EXECUTABLE..." 
rm "/usr/bin/pypad"



if [ ! "$os" == "Darwin" ] 
then

echo -e "DELETING .DESKTOP FILE..." 
sudo rm /usr/share/applications/pypad.desktop

fi

echo -e "Thank you for using my terminal. -Dmytro" 