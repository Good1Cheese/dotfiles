# For example:
# ./script "Do you want to shutdown?" "shutdown -h now"

promt="Are you sure you want to shutdowm?"
cmd="shutdown now"
[ $(echo -e "No\nYes" | dmenu -i -p "$promt") \
	== "Yes" ] && $cmd
