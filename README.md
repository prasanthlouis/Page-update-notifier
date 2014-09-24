Page-update-notifier
====================

This script notifies you if there is a change on a webpage.

This is basically for students who couldn't wait to get their results.
What this script does is that, it compares the html code of a page with the html code of the same page a little later.
So any change caused in the html code will be due to a change in the website.

Now I made this script for the sites of http://cbseresults.nic.in/ and http://103.251.43.95/mgcbcss/result.php
Both of which are the sites for the results of the 10th/12th examinations and the MG university exams.
The  script works fine for these 2 sites. On the occurance of an update on the page, a message will appear on the console saying that the page has been updated.

However it should be noted that sites like google.com, stackoverflow.com have additional functions such as a server timer which causes the program to run once before exiting. If you still want it to work on those sites, target the HTML that you want to monitor and modify the program according to your need.

Instead of a message it's possible to play a song, or send an email, etc. However I haven't implemented it here.

And yes, its possible for you to join the refresh script with this script. However I've created them as 2 repo since each can stand alone. If you desire, feel free to combine the 2 scripts.

This would be much easier for students, as they can be occupied with sommething else, till the dreadful message appears on the command line. Good luck for the exams!

Feel free to modify and distribute.
