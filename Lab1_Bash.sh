#!/bin/bash
(echo "Название,Расширение,Размер,Время создания,Время изменения,Тип,Длительность видео и аудио")>./files.xls
files()
{
(
for i in "$1"/*
do
r=$(expr length "$i")
d=3
ras=$(echo "$i"|rev|cut -f1 -d .|rev)
if [[ $ras == $i ]]; then
w=' '
else
w=$ras
fi
s=$i
e=$(($r+$d))
if [[ $w == "mkv" || $w == "mp4" ]]; then
echo $(stat --printf="%n" "$s"|rev|cut -f1 -d /|rev),$w,$(stat --printf="%s,%w,%z" "$s"),$(file "$s" | cut -c$e-| sed 's/,//g'
),$(mediainfo "$s"|head -n7|tail -n1|cut -c44-)
elif [[ $w == "mp3" ]]; then
echo $(stat --printf="%n" "$s"|rev|cut -f1 -d /|rev),$w,$(stat --printf="%s,%w,%z" "$s"),$(file "$s" | cut -c$e-| sed 's/,//g'
),$(mediainfo "$s"|head -n5|tail -n1|cut -c44-)
elif [[ $w == "avi" ]]; then
echo $(stat --printf="%n" "$s"|rev|cut -f1 -d /|rev),$w,$(stat --printf="%s,%w,%z" "$s"),$(file "$s" | cut -c$e-| sed 's/,//g'
),$(mediainfo "$s"|head -n6|tail -n1|cut -c44-)
elif [[ $(echo "$i"|rev|cut -f1 -d /|rev) == "*" ]]; then
continue
elif [[ -d "$s" && $(echo "$s"|wc -l) -ne 0 ]]; then
files "$s"
else
echo $(stat --printf="%n" "$s"|rev|cut -f1 -d /|rev),$w,$(stat --printf="%s,%w,%z" "$s"),$(file "$s" | cut -c$e-| sed 's/,//g'
)
fi
done)>>./files.xls
}
files ~/work
