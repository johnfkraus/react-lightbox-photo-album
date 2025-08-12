# Convention for naming photos for the album and for referring to the photos in the code:

## In the code (photos.ts file):

Strings referring to photos should use the following pattern:

{arbitrary name}.{arbitrary number}.{width}x{height}.jpg

Example reference to photo in photos.ts file: `hotel.8016.3024x4032.jpg`


## Photo filenames:

Add `.{width2}w` to the filename (before the .jpg file extension).

{name}.{number}.{width1}x{height}.{width2}w.jpg

For example: `hotel.8016.3024x4032.3024w.jpg`

width1 and height should be the dimensions of the highest resolution version of the photo.  The MacOS Finder app will show these dimensions so that you can name the photo appropriately.

We have disabled the srcset functionality for now, so the following can be ignored:

Multiple versions of a photo identified by a unique name and number may optionally have different dimensions.  The highest resolution version of the photo will be largest in terms of bytes.

Optionally, you can supply multiple images having different resolutions.  The website can responsively use lower resolution images depending on users' screen size and resolution.

width2 can be equal to any of the following: width1, 1080, 640, 384, 256, 128, 96, 64, or 48.  width2 in the photo filename should be approximately the value of the actual width dimension of the photo in that file.

For the highest resolution photo (having the largest number of bytes), width2 should equal width1.  This applies to the photo file name, not the references to photos in photos.ts.  In the photos constant in photos.ts, the `{width}w` part of the photo hame is always omitted (and might be added programmatically).

Both `.jpg` and `.jpeg` work as file extensions, as long as the actual filename matches the code listing in photos.ts.

The srcset attribute in HTML is used for specifying a list of different image sources for an <img> element, allowing the browser to choose the most appropriate image based on factors like screen size and resolution. It's a crucial part of building responsive websites that deliver optimized images for various devices.


birdhouse.7943.3024x4032.4032w.jpg
dishes.8073.4032x3024.4032w.jpg
hotel.8016.3024x4032.4032w.jpg
meeks.8143.2400x3600.1080w.jpg
meeks.8143.2400x3600.128w.jpg
meeks.8143.2400x3600.2400w.jpg
meeks.8143.2400x3600.256w.jpg
meeks.8143.2400x3600.3600w.jpg
meeks.8143.2400x3600.384w.jpg
meeks.8143.2400x3600.48w.jpg
meeks.8143.2400x3600.648w.jpg
meeks.8143.2400x3600.64w.jpg
meeks.8143.2400x3600.96w.jpg
palace.8004.4032x3024.3024w.jpg
wallocheese.7977.4032x3024.4032w.jpg
