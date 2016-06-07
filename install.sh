#!/bin/sh
if [ $EUID != 0 ]; then
    echo "error: You must install this with sudo."
    exit $?
fi

install_directory="$(git --exec-path)/../git-tidbit"
absolute_directory=$(cd $install_directory; pwd)
current_directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
mkdir $install_directory

echo "Installing git-tidbit into $absolute_directory"
cp -rf $current_directory/* $absolute_directory

git config --global alias.tidbit "!sh $absolute_directory/git-tidbit.sh"

if [ $? -eq 0 ]; then
    echo "Installing Successful!"
else
    echo "Install Unsuccessful. Please run ./uninstall to cleanup"
fi

