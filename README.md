# limf 
Pomf.se clone uploading tool
## Installation 
`sudo pip install limf`  
Yep, that's all
### limf
Main executable - uploads the file and can encrypt it if asked.  
Also can decrypt when right links is given.  
If file is uploaded to different host than chosen, it
just means that chosen host doesn't work.
### limfshot.sh 
Tool for making screenshots, uploading them, and putting link in clipboard.
Useful when used as bind to key.
#### Depends
* Python 3 - required for tool to work
* Requests library - required for tool to work
* scrot - for doing screenshots (limfshot.sh)
* xclip - for putting link into clipboard (limfshot.sh)
* gpg - for encryption and decrytion  

#### Entry syntax 
`['$clone_url", "$clone_upload_url", "$clone_list_name", $max_clone_filesize, $clone_does_not_use_cloudflare]`  

##### I am clone owner and my clone is not in host_list.json, what should I do?
Either email me (aptget@cock.lu) or create pull request. 
