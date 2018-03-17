# hive-autoswitch

This is a autoswitch of wallet based on whattomine most profitability
Install the requirements below

Step 1 : Requirements - execute the command below from terminal

# apt-get install vim

# apt-get install git

# apt-get install python-dev

# pip install certifi

# pip install logging

# git clone git@github.com:paulon-zervoulakus/hive-autoswitch.git

# cd hive-autoswitch && mv CONFIG.example.py CONFIG.py

Step 2: File Permission - at the same directory of eypiay.py file execute the command below from terminal

# chmod a+x eypiay.py

# touch autoswitch.log && chmod a+x autoswitch.log

Step 3: Tweak whattomine - goto https://whattomine.com/coins tweak most profitable for your rig to mine. 

Step 4: whattomine api - copy the full path url of whattomine and paste it on to new tab, before hitting enter and edit the string coins to coins.json

ex: 

  https://whattomine.com/coins?utf8=.....
  
  https://whattomine.com/coins.json?utf8=.....

The new url path is your api link, it will give you a json response object. Please take note of the result.

Step 5: CONFIG - After step 4, copy the new url path then goto terminal and execute the command below to edit your config url path

# vim CONFIG.py

Delete the existing existing value, and replace your whattomine url path 

Step 6: Hiveos secret and public key - Goto your hiveos account profile, then goto tab account https://hiveos.farm/a/account/#pane-user at the bottom of page you will find your API keys. If you do not have one, click Generate and takenote of the Public and Secret key

# vim CONFIG.py

place your public and secret key value into the CONFIG.py settings

Fill in the rig_ids value with your rig_id from hiveos https://hiveos.farm/a/profile/rigs. 

Step 7: Wallet - Create a wallet and name it exactly the same as the result of your whattomine api json response object index.

ex: 

  {"coins":{"Nicehash-Equihash":{"id":19,"tag":"NICEHASH","algorithm":......}
  
the first coin is Nicehash-Equihash, this should be the name of your wallet. Create a separate wallet per each coin that you want to autoswitch mining

NOTE: your wallet name should match the name from the result of json response object

Step 8: Crontab - add your application to crontab. The example below will trigger every 1 hour.

# crontab -e 

0 */1 * * * /usr/bin/python /[replace this path to your eypiay.py file path]/eypiay.py

All rights reserved

Accepting donation

Thanks!
