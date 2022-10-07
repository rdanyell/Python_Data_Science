#!/bin/sh

JQ="/Users/rdanyell/.brew/Cellar/jq/1.6/bin/jq" #where jq is (works with JSON files)
OUTPUT_FILE="./hh.json" #where to save 
VACANCY_AMOUNT="20" # number of vacancies
VACANCY_NAME="${1/ /+}" # vacance name should be the 1st argument
curl -k -H 'User-Agent: api-test-agent' -G "https://api.hh.ru/vacancies?text=$VACANCY_NAME&per_page=$VACANCY_AMOUNT" | $JQ > $OUTPUT_FILE

# run bash hh.sh ‘data scientist’
