#!/bin/bash

CYAN='\033[0;36m'    # ${CYAN}
PURPLE="\033[1;35m"  # ${PURPLE}
NC='\033[0m'         # ${NC}

# Install sofware I commonly use 
install_main() {
	figlet -t -k -f slant "Installing..."
	sudo pacman -S --noconfirm spotifyd python-pywal xcompmgr scrot obsidian xwallpaper 
	figlet -t -k -f slant "Installing with yay..."
	yay -S --noconfirm ani-cli-git spotify-tui cava 
	figlet -t -k -f slant "Complete"
}
# print Osaka ASCII art
osaka() {
        base64 -d <<<"H4sIAAAAAAAAA6WVO7bjMAiGe6+CJciNdzCFGgoabSANBY0K1j+AsB65t5kzf07sxBKffvTA1wUd
XdXklw+LElERAfA7vBLhjz1Q5psIWZhpl3e5AAcrcMTyASESRynddu0LJtIMbl08ViVhGNeyswyG
XEQB7uYkgEcmJ2EKN/kdGsX/0pYxC7xGiuGsCXsMCRZVKO1RfXSxVIDsQWdrxAGTI8mrvCQzFj6k
KGjMn+lwJut5E20d9klzXzdOxQRWGxXq1JEl0NagigZDTJaNerWatmr4DCdtrKmLD9ZC1WI5Nyj1
J8thzlL3uoe0g4WrAa1zhTZ98WKhD9CBm45UIurPXZ9fWfTEIFVp+nqchYvF3rzFwLcS9Q6AHSfr
NhblTvUcfXKeDBo4+R32DiM4c2wvK2iDNdW5w6/atpwsX8Gq7wmKtfg3bb5w7a9Yx/9h2Sa4Phvr
e3bsrJbUUx7T92BfrF7fhczKcXQt3EPyGcSzXe8xX5gs2Hxh++obmJ44NtjZHjklq03WOEN2P9Ps
h4x2tMa++cmKQphbbV/z8DU/e0GLkhdRFNMzWXXkSFle/bANsTNeUE+U1u1cWlR4ewYrSPGg5u/R
a9ASJkHq98bBwRrAYMGaL3rfIQOI7K8IT9m+wl7wJWpmxVmUkDJRmawIjxxzvPhlrERM1WU8gJjm
oq5e11/xsgQw2AYAAA==
" | gunzip
}





figlet -t -k -f slant "Main Install"
echo -e "${CYAN}This script will configure your system for Pepsi.${NC}"
osaka 
echo -e "${PURPLE}Continue?...${NC}"
read -r response
if [[ ! "$response" =~ ^[Nn]$ ]]; then
	# Ask for sudo rights
	sudo -v
	# Keep sudo rights
	while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &
	# Start Main Installation
	install_main
else
	exit 1
fi
