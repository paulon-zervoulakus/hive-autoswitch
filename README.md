# hive-autoswitch

This is a autoswitch of wallet based on whattomine most profitability
Install the requirements below

#Step 1 : requirements

apt-get install python-dev

pip install certifi

pip install logging

#Step 2: Config

Goto whattomine and tweak most profitable for your rig

get your secret and public key from hive

fill in the config rig_ids with your rig_id from hive. NOTE: your wallet name should match the name result from whattomine json response

#Step 3: add your application to crontab. The example below will trigger every hour

0 */1 * * * /usr/bin/python /hove/user/hiveos/hive-autoswitch/eypiay.py

#Step 4: file permission

chmod a+x eypiay.py

chmod a+x autoswitch.log

All rights reserved

Accepting donation

Thanks!
