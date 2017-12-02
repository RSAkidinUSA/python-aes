#/bin/bash
PLAIN="plaintext"
CIPHER="ciphertext"
KEY="key"
FILES="$PLAIN $CIPHER*-cbc $CIPHER*-ecb $KEY"

if [ "$#" -lt "1" ] || [ "$1" == "-h" ] \
	|| [ "$1" == "--help" ]; then
	echo "Usage: TestAll.sh [DIR]..."
	exit 1
fi

for i in "$@"; do
	echo $i":"
	
	ERR=0
	for j in $FILES; do
		ls $i"/"*$j* >/dev/null 2>/dev/null
		if (( $? != 0 )); then
			echo "Directory missing $j file."
			ERR=2
		fi
	done
	if (( $ERR != 0 )); then
		exit $ERR
	fi

	python3 aes_main.py -f $i"/"*$PLAIN* -o $i"/out-ecb" \
		$i"/"*$KEY*
	if (( $? != 0 )); then
		echo "ECB code errored out..."
		exit 3
	fi

	python3 aes_main.py -f $i"/"*$PLAIN* -o $i"/out-cbc" \
		$i"/"*$KEY* -c

	if (( $? != 0 )); then
		echo "CBC code errored out..."
		exit 3
	fi

	diff -i $i"/out-ecb" $i"/"*$CIPHER*"-ecb"*
	if (( $? != 0 )); then
		echo "Failed ECB! (outputs didn't match)"
		exit 4
	else
		echo "Passed ECB!"
	fi
	rm $i"/out-ecb"

	diff -i $i"/out-cbc" $i"/"*$CIPHER*"-cbc"*
	if (( $? != 0 )); then
		echo "Failed CBC! (outputs didn't match)"
		exit 4
	else
		echo "Passed CBC!"
	fi
	rm $i"/out-cbc"
done