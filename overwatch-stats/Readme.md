What it can do
--------------
- Send Overwatch Player Stats to grapite with a provided user list as parameter

Install
-------
```
git clone git@github.com:kaminascripts/KaminaScripts.git
cd KaminaScripts/overwatch-stats
pip install -r requirements.txt
```
Now add your user name in userlist.txt
`echo "YourName#1234" >> userlist.txt`

Usage
-----
`python get_player_stats.py --userlist userlist.txt`
