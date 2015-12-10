#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
echo -e "\n"
echo -e "${CYAN}Bash Script (c)...${NC}"
if [[ $1 == "master" && $# -eq 1 ]]
        then
                echo -e "\n"
                echo -e "${GREEN}Pulling changes from master branch and pushing to your local branch.${NC}"
                git pull origin master
                git add .
                git commit -am "Pulling changes from master branch."
                git push origin $USER
                echo -e "${GREEN}Done. Please check for errors if any.${NC}"
                echo -e "\n"
elif [[ $1 == "push" && $# -eq 2 ]]
        then
                echo -e "\n"
                echo -e "${GREEN}Pushing ALL the changes with log message to your own branch.${NC}"
                git add .
                git commit -am "$2"
                git push origin tmakwan
                echo -e "${GREEN}Done. Please check for errors if any.${NC}"
                echo -e "\n"
elif [[ $1 == "checkout" && $# -eq 2 ]]
        then
                echo -e "\n"
                echo -e "${GREEN}Checking out $2 branch.${NC}"
                git checkout $2
                echo -e "${GREEN}Done. Please check for errors if any.${NC}"
                echo -e "\n"
else
        echo -e "\n"
        echo -e "${RED}The options are:${NC}"
        echo -e "${YELLOW}master${NC} - Pulling changes from master branch and pushing to your local branch."
        echo -e "${YELLOW}push \"YOUR_LOG_MESSAGE\"${NC} - Pushing ALL the changes with log message to your own branch."
        echo -e "${YELLOW}checkout BRANCH_NAME${NC} - Checking out BRANCH_NAME branch."
        echo -e "\n"
fi
                                                                                                                                        
