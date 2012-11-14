fbackup
=======

What is it?
-----------

fbackup is your personal Facebook backup tool.  If you're like me, you have
years of important, meaningful information stored in your facebook profile.
Tagged pictures, friends and families photo albums, conversations, messages,
etc - all locked into your facebook acount.  

fbackup liberates that data.


### Photo / Album Backup

Downloads all of your tagged photos and all the photos in the albums they are
in, as well as all your uploaded pictures.


### Message Backup (future)


### Posts Backup (future)


### Birthday Backup (future)


### Contact Backup (future)


Installation
------------

* Download a copy of fbackup `git clone https://github.com/timothyasp/fbackup.git`
* Create a Facebook app at https://developers.facebook.com
* Generate a access token from https://developers.facebook.com/tools/explorer
   * Make sure you select all the photo relevant permissions in the dialog that
     pops up, otherwise fbackup won't be able to grab all your photos
* Install facepy: `sudo easy_install facepy` or if you don't have `easy_install` (shame on you) https://facepy.readthedocs.org/en/latest/ has info on how to download
* Run `python fbackup.py`


Enjoy!  Let me know if there are any bugs through the issue tracker and I'll
work on them.  This is the first version of this tool so there are probably bugs, but it has worked for myself and roomates so hopefully it works for you!
