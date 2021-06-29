#!/bin/bash
#coding:utf-8

nb_line=$(wc -l ../files/result.txt | cut -d ' ' -f 1)

while [ true ] ; do

	if [ -f ../files/result.txt -a $nb_line -ne 0 ] ; then

		for i in $(cat ../files/result.txt | sed 's/ /_/g') ; do
			notif=$(echo -e "$i" | sed 's/_/ /g')

			current_date=$(date +'%H:%M:%S %d/%m/%Y')
			debug_content_file=$(cat ../files/result.txt)

			message=$(echo -e "$notif" | cut -d '|' -f 1)
			message_line=$(echo -e "$notif" | cut -d '|' -f 2)

			if [ $(echo -e "$message" | cut -d ' ' -f 1) = "[Spot]" -o $(echo -e "$message" | cut -d ' ' -f 1) = "[Spots]" ] ; then

				id=$(echo -e "$message" | cut -d '$' -f 2)
				echo -e "ID: '$id'"

				if echo -e "$message_line" | grep -i "closed" 1> /dev/null ; then
					order=0 && echo a
				elif echo -e "$message_line" | grep -i "New signal available" 1> /dev/null ; then
					order=1 && echo b
				elif echo -e "$message_line" | grep -i "Target 1" 1> /dev/null ; then
					order="0_1" && echo c
				elif echo -e "$message_line" | grep -i "Target 2" 1> /dev/null ; then
					order="0_2" && echo d
				elif echo -e "$message_line" | grep -i "Target 3" 1> /dev/null ; then
					order="0_3" && echo e
				fi

				if [ "$order" = "1" ] ; then
					if echo -e "$message_line" | grep -i "Low" 1> /dev/null ; then
						risk="_L" && echo z
					else
						unset risk && echo zz
					fi
				else
					unset risk && echo zz
				fi

				if [ ! -z "$id" -a ! -z "$order" ] ; then
					echo -e "${id}${order}${risk}" >> ../files/trade.txt
					echo -en > ../files/result.txt
					echo -e "[+] Add new entry"

					# Logs
					echo -e "=== $current_date ===" >> ../files/debug.txt
					echo -e "${debug_content_file}\n" >> ../files/debug.txt
					echo -en > ../files/result.txt
				else
					# Logs
					echo -e "=== $current_date ===" >> ../files/debug.txt
					echo -e "${debug_content_file}\n" >> ../files/debug.txt
					echo -en > ../files/result.txt
				fi
			else
				# Logs
				echo -e "=== $current_date ===" >> ../files/debug.txt
				echo -e "${debug_content_file}\n" >> ../files/debug.txt
				echo -en > ../files/result.txt
			fi

			unset id
			unset order
		done
	fi

	sleep 5
	nb_line=$(wc -l ../files/result.txt | cut -d ' ' -f 1)
done
