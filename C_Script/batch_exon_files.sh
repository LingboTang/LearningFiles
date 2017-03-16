#! /bin/bash

# Compile the C files
make clean
rm -rf /home/lingbo/CPofAaronsData/out/
make

mkdir /home/lingbo/CPofAaronsData/out/

# Find the minimum energy
# To get only filename="${filename%.*}"
extension=".txt"
fullpath="/home/lingbo/CPofAaronsData/"
for file in /home/lingbo/CPofAaronsData/*;
do
	myBase=`basename ${file%.*}`
	if [ "$myBase" = "out" ]; 
        then
		echo ""
	else
		baseDir=`dirname ${file}`
		outFile=$baseDir
		outFile+="/out/$myBase"
		outFile+=$extension
		touch $outFile
		./lingbo_op_getter ${file} ${outFile}
	fi
done

readarray GREPPED < <(grep "[+-]\\{0,1\\}[0-9]\\{0,\\}\\.\\{0,1\\}[0-9]\\{1,\\}" -R /home/lingbo/CPofAaronsData/out/)
declare -a arr

for item in "${GREPPED[@]}"; 
do
	value=`echo ${item} | cut -d':' -f2-`
	echo $value
	arr[$i]=${value}
	((i = i + 1))
	#echo ${item##*/}	
	#echo "${item}"; 
done

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

rm -rf /home/lingbo/CPofAaronsData/out/
