#! /bin/bash

# Compile the C files
make clean
rm -rf /home/lingbo/CPofAaronsData/exon_44_output/out/
make

mkdir /home/lingbo/CPofAaronsData/exon_44_output/out/

# Find the minimum energy
# To get only filename="${filename%.*}"
# You can change your filename and path here
extension=".txt"
fullpath="/home/lingbo/CPofAaronsData/exon_44_output/*"
for file in $fullpath;
do
	myBase=`basename ${file%.*}`
	echo $myBase
	if [ "$myBase" = "out" ]; 
        then
		echo ""
	# Create the output folder
	else
		baseDir=`dirname ${file}`
		#echo $myBase
		outFile=$baseDir
		outFile+="/out/$myBase"
		outFile+=$extension
		touch $outFile
		# Execute the C program to extract energy
		./op_getter ${file} ${outFile}
	fi
done

# Grep the energy into an array from output
readarray GREPPED < <(grep "[+-]\\{0,1\\}[0-9]\\{0,\\}\\.\\{0,1\\}[0-9]\\{1,\\}" -R /home/lingbo/CPofAaronsData/exon_44_output/out/)
declare -a arr

# Collect the pure value
for item in "${GREPPED[@]}"; 
do
	value=`echo ${item} | cut -d':' -f2-`
	echo $value
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

# Clean up
make clean
rm -rf /home/lingbo/CPofAaronsData/exon_44_output/out/
