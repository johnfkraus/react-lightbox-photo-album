#!/bin/bash

# rename files for photo album app
# Original filenames expected to be formatted as name.number.jpg.
#
for file in *.jpg *.png *.jpeg; do # Add other extensions as needed
  if [ -f "$file" ]; then
    dimensions=$(identify -format "%wx%h" "$file")
    # echo "${dimensions}"
    width=$(identify -format "%w" "$file")
    # echo "${width}"
    delimiter='.'
    # Temporarily set IFS to the delimiter and use read to populate an array
    IFS="$delimiter" read -ra my_array <<< "$file"
    # echo "my_array: ${my_array[@]}"
    array_len="${#my_array[@]}"

    if [[ $array_len -lt 3 ]]; then
      echo "error, filename is too short: ${my_array[@]}"

    else
      new_filename="${my_array[0]}.${my_array[1]}.${dimensions}.${width}w.${my_array[2]}"
      echo "${new_filename}"
      mv "$file" "renamed/$new_filename"
    fi
  fi
done
