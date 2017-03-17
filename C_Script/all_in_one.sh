#! /bin/bash

# Grep the energy into an array from output
readarray GREPPED < <(grep "^energy: [+-]\\{0,1\\}[0-9]\\{0,\\}\\.\\{0,1\\}[0-9]\\{1,\\}" -R /home/lingbo/CPofAaronsData/)
declare -a arr

# Collect the pure value
for item in "${GREPPED[@]}";
do
        value=`echo ${item} | cut -d':' -f2-`
        value=`echo $value | cut -d':' -f2-`
        arr[$i]=${value}
        ((i = i + 1))
done

# Find the min value in the list
# bc is for converting string to number
# Be sure bash only has integer as default
min=${arr[0]}
for n in "${arr[@]}";
do
        comp=`bc -l <<<"$n < $min"`
        if (( $comp > 0 ));
        then
                min=$n
        fi
done
echo "Min is: "
echo $min

