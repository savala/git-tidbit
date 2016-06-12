#!/bin/sh
if [ $EUID != 0 ]; then
    echo "error: You must install this with sudo -H."
    exit $?
fi

install_directory="$(git --exec-path)/../git-tidbit"
absolute_directory=$(cd $install_directory; pwd)
current_directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
mkdir $install_directory

echo "Installing git-tidbit into $absolute_directory"
cp -rf $current_directory/* $absolute_directory

pip install termcolor
pip install bs4

git config --global alias.tidbit "!sh $absolute_directory/git-tidbit.sh"
git config --global alias.commit tidbit

if [ $? -eq 0 ]; then
    echo "Installing Successful!"
else
    echo "Install Unsuccessful. Please run ./uninstall to cleanup"
fi

