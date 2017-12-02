#/bin/bash
PLAIN="/aes-plaintext"*".txt"
CIPHER="/aes-ciphertext"*
KEY="/aes-key"*".txt"

for i in $(ls -d testing/test*); do
	echo $i
	python3 aes_main.py -f $i$PLAIN -o $i"/out-ecb" $i$KEY
	python3 aes_main.py -f $i$PLAIN -o $i"/out-cbc" $i$KEY -c

	diff -i $i"/out-ecb" $i$CIPHER"-ecb.txt"
	if (( $? != 0 )); then
		echo "Failed ECB!"
		return
	else
		echo "Passed ECB!"
	fi
	rm $i"/out-ecb"

	diff -i $i"/out-cbc" $i$CIPHER"-cbc.txt"
	if (( $? != 0 )); then
		echo "Failed CBC!"
		return
	else
		echo "Passed CBC!"
	fi
	rm $i"/out-cbc"
done