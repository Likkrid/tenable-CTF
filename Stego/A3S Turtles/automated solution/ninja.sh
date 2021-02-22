#!/usr/bin/env bash

while [ -e *.zip ]; do
  files=*.zip;
  for file in $files; do
    echo -n "Cracking ${file}… ";
    output="$(fcrackzip -b -D -p ~/Documents/rockyou.txt -u *.zip | tr -d '\n')";
    password="${output/PASSWORD FOUND\!\!\!\!: pw == /}";
    if [ -z "${password}" ]; then
      echo "Failed to find password";
      break 2;
    fi;
    echo "Found password: ${password}";
    7z x -y -p"${password}" "$file";
    mv "${file}" "${file}.pwned";
  done;
done;

#echo "obase=16; ibase=2; 010101000110100001101001011100110010000001101001011100110010000001100001001000000110001001101001011011100110000101110010011110010010000001101101011001010111001101110011011000010110011101100101" | bc
