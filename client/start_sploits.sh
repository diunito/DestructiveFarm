#!/bin/bash
handle_exit() {
	echo 'got Ctrl+C, killing all sploits'
	for pid in $@;do
		kill -INT $pid
		echo "killed $pid"
	done
}

startf="$PWD"
ssf="$startf" # start_sploit.py folder
curf="$2"
url="$1"

if [ "$curf" = "--help" ] || [ -z "$url" ];then
	echo "Usage: $0 [url] [folder with only sploits]"
	exit 0
fi

tokfile="/tmp/.dftok"
if ! [ -f "$tokfile" ];then
	echo "Error: no tokfile, do 'echo [your-df-api-token] > $tokfile'"
	exit 1
fi
if [ -n "$curf" ];then
	cd "$curf" || echo echo "$curf doesn't exists, use --help for usage" && exit 2
fi

pids=()
for script in *;do
	if [ "$script" = "start_sploit.py" ] || [ "$script" = "start_sploits.sh" ];then
		continue
	fi
	script="$PWD/$script"
	"$ssf"/start_sploit.py "$script" -u "$url" --token "$(<$tokfile)" &
	pids+=("$!")
done

echo sploits pids: ${pids[*]}
trap "handle_exit ${pids[*]}" SIGINT
echo trapped

for pid in ${pids[*]};do
	wait $pid
done
