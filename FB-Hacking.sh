#bagian warna
merah="\033[31;1m"
putih="\033[39;1m"
#bagian tampilan

echo "\033[31;1m ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ █░░ █▀▀"
echo "\033[31;1m ░▒█░░ █░░█ █░░█ ░░▀▄ ░▒█░░ █░░█ █░░█ █░░ ▀▀█"
echo "\033[31;1m ░▒█░░ ▀▀▀▀ █▀▀▀ █▄▄█ ░▒█░░ ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀\033[0m"
echo "\033[39;1m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m"
printf "\033[0m[\033[31;1m01\033[0m]\033[34;1m Facebookinfomercial-Dump \033[0m[\033[31;1mM\033[0m]\033[34;1m MENU\n"
echo ''
printf "\033[0m[\033[31;1m02\033[0m]\033[34;1m Facebook-Bot\n"
echo ''
printf "\033[0m[\033[31;1m03\033[0m]\033[34;1m Facebook-Clone\033[0m\n"
echo ''
printf "\n${putih}[${merah}+${putih}]ENDER-NUMBER: " gameo
read gameo
if [ $gameo = 1 ] || [ $gameo = 01 ];then
cd .FacebookToolkit && php run.php
cd && sh FB-Hacking.sh
elif [ $gameo = m ] || [ $gameo = M ];then
cd .FacebookToolkit && php run.php -m
cd && sh FB-Hacking.sh
sh FB-Hacking.sh
elif [ $gameo = 2 ] || [ $gameo = 02 ];then
clear
cd Facebook-Bot && php bot.php
elif [ $gameo = 4 ] || [ $gameo = 04 ];then
python2 .Facebook-Clone.py
elif [ $gameo = 0 ] || [ $gameo = 0 ];then
exit
else
printf "${merah}!!!! input salah atau tidak boleh kosong !!!!"
sleep 1
sh apk.sh
fi
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status

