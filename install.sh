#!/bin/bash
systemctl stop ServerCheck.service

echo ""

echo "Downloading files..."

wget https://raw.githubusercontent.com/nwhitten/ServerCheck/master/ServerCheck.py

wget https://raw.githubusercontent.com/nwhitten/ServerCheck/master/ServerCheck.service

wget https://raw.githubusercontent.com/nwhitten/ServerCheck/master/Assets/ArialUnicode.ttf
wget https://raw.githubusercontent.com/nwhitten/ServerCheck/master/Assets/ArialBold.ttf


echo ""

echo "Removing old files files..."
rm -r /usr/local/bin/ServerCheck
rm /etc/systemd/system/ServerCheck.service
rm /usr/share/fonts/ArialUnicode.ttf
rm /usr/share/fonts/ArialBold.ttf

echo ""

mkdir /usr/local/bin/ServerCheck/

echo "Moving files..."

mv ServerCheck.py /usr/local/bin/ServerCheck/

mv ArialUnicode.ttf /usr/share/fonts/
mv ArialBold.ttf /usr/share/fonts/

mv ServerCheck.service /etc/systemd/system/

echo ""

echo "Starting services..."
systemctl daemon-reload
systemctl enable ServerCheck.service
systemctl start ServerCheck.service


#echo ""
#echo "Installing crontab..."
#(crontab -l; echo "*/10 * * * * python3 /usr/local/bin/status_check/inky_update.py";) | crontab -
