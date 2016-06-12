install_directory="$(git --exec-path)/../git-tidbit"
absolute_directory=$(cd $install_directory; pwd)

while true; do
    read -p "Do you wish to uninstall git-tidbit?" yn
    case $yn in
        [Yy]* ) rm -rf $absolute_directory; git config --global --unset alias.tidbit; echo "Uninstalled complete."; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done