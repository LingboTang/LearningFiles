#! /bin/bash

# Grep the energy into an array from output



readarray GREPPED < <(grep "^energy: [+-]\\{0,1\\}[0-9]\\{0,\\}\\.\\{0,1\\}[0-9]\\{1,\\}" -R /home/lingbo/CPofAaronsData/exon_44_output/)
declare -a arr

# Collect the pure value
for item in "${GREPPED[@]}";
do
	# Chop the line
        value=`echo ${item} | cut -d':' -f2-`
	# Chop the string that contains the energy value
        value=`echo $value | cut -d':' -f2-`
	#echo $value
        arr[$i]=${value}
        ((i = i + 1))
done

# Find the min value in the list
# bc is for converting string to number
# Be sure bash only has integer as default
min=${arr[0]}
for n in "${arr[@]}";
do
	# Covert the value and compare
        comp=`bc -l <<<"$n < $min"`
        if (( $comp > 0 ));
        then
                min=$n
        fi
done
echo "Min is: "
echo $min

