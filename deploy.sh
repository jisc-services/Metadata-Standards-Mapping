#!/bin/bash

push () {
    git add .
    git commit -m "Updated pages"
    git push
}

# http://stackoverflow.com/questions/3231804/in-bash-how-to-add-are-you-sure-y-n-to-any-command-or-alias
confirm () {
    # call with a prompt string or use a default
    read -r -p "${1:-Are you sure? [y/N]} " response
    case $response in
        [yY][eE][sS]|[yY]) 
            true
            ;;
        *)
            false
            ;;
    esac
}

cd build
git status
confirm "OK to push? [y/N]" && push
cd ..

