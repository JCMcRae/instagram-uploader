# instagram-uploader
Lightweight Instagram Upload Code

This is code taken from a proprietary content planning tool I built for the Clean Your Shoes WordPress and Instagram social media accounts.
This code here is sample code that allows you to post a photo or a carousel to Instagram. 

### THIS IS NOT A WORKING APP/PROGRAM.

Because Instagram requires your images to be hosted somewhere (Google Drive, WordPress, DropBox, etc.) and not stored locally, there is a lot less code required to read, format and upload images. This code simply takes in the URI for your image(s), and uploads them to your business/brand's Instagram account.*

The code is pretty straightforward and easy to understand. The `create_instagram_post` function will have a caption, your image URL, and a a "Post URL", which is the URL to your brand's Instagram page/account using Meta's Graph API for Instagram. The payload you send to the `POST URL` will contain your caption, your image location, and the proper Instagram access token that you should have for your app to access your Instagram account. This simply nad only  _uploads_ the image to Instagram's database, akin to uploading something on a Google Drive or DropBox.

After you send the request to upload the media ot your IG account, you will receive a media ID for said image in the response. This is important because a second request with that ID and your access token will be sent to the GRAPH API request to actually _publish_ the image on your account. The way I have the code set up, it will only publish the media _if and only if_ there was a successful upload of the image and a proper ID was returned in the response.

The `create_carousel` function, which allows you to upload and publish multiple images for a carousel post works in a similar fashion with a couple of addendums, but doesn't stary far from `create_instagram_post`.
