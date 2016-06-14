install_directory="$(git --exec-path)/../git-tidbit"

if [ ! -d "$DIRECTORY" ]; then
  echo "Error: Install directory does not exist. No changes made. Exiting."
  exit
fi

absolute_directory=$(cd $install_directory; pwd)


while true; do
    read -p "Do you wish to uninstall git-tidbit?" yn
    case $yn in
        [Yy]* ) rm -rf $absolute_directory; 
                git config --global --unset alias.tidbit;
                if [ $? -eq 0 ]; then
                    echo "Uninstall complete"
                else
                    echo "Uninstall failed"
                fi; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done