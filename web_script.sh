!/bin/bash
expressions=(11:02 11:00 10:48 11:15 11:11 10:50 11:07 11:20 10:51 11:17 11:03 11:05)
RANDOM=$$$(date +%s)


selectedexpression=${expressions[$RANDOM % ${#expressions[@]} ]}



sudo rtcwake -m mem --date 'tomorrow' + $selectedexpression
sleep 15s
source /home/ainazar/projects/test/venv/bin/activate
python3 /home/ainazar/projects/test/job.py

sleep 10s
sudo pm-suspend
