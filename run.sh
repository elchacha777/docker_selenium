# Reason for "-nolisten tcp", not documented within Xvfb manpages (for who knows what reason)
# https://superuser.com/questions/855019/make-xvfb-listen-only-on-local-ip
#Xvfb :99 -screen 0 1024x768x24 -nolisten tcp &
#python3 test.py
xvfb-run --server-args='-screen 0, 840x480x24' --auto-servernum --server-num=1 python3 test.py

