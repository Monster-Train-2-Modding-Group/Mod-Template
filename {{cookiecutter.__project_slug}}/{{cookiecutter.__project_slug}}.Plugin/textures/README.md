Use this folder for IMAGES referenced from your json files.

The tutorial to get you up and running is located [here](https://github.com/Monster-Train-2-Modding-Group/Trainworks-Reloaded/wiki)

I find its best to organize the file structure like so.

* banners - Store the clans 6 banner art images here.
  * _Disabled - Used when you are on the opposite track
  * _Enabled - Used when you on on the track with the node. And when its visited
  * _Frozen - Used when the ring this node is on is after the node you are on.
  * _MapIcon - The Map Icon for the node
  * _Visited_Disabled - Used when you have claimed the banner reward
  * ClanBannerMinimapIcon - Icon used in the mini map screen. Should always be this image provided.
* card_art - Store card images here. Card Images can be as small as you want. The examples are 256x256 they can be up to 468x468. (Best to keep as small as possible for filesize of mod).
* card_borders - Store the 3 card border images. The images provided can be used as a template.
  * Equipment and room cards share a border image the square image
  * Spell cards have a sideways hexagonal border
  * Unit cards have a longways hexagonal border with the top having the pointed end.
* character_art - Store character art images / skeletons here. These should be png images with transparency and can be as large or small as you want. The images provided are 256x256
* icons - Miscellaneous icons.
* relic_art - Artwork for artifacts here.

Special template images
 * icons/EmptyEquipmentIcon - Base icon for equipment. To make it look good don't draw in the bottom right quadrant outside the circle.
 * icons/EmptyRoomIcon - Base icon for rooms.
 * icons/EmptyPortrait - Empty champion portrait.
 
The example images provided conform to the sizes required for the images in game.


## Artwork 

Do keep to the suggested sizes listed below to minimize load times. Loading images from disk is the bottleneck in framework startup, so please don't use large images in your mod.

* Clan icons: You'll need 4 images of the icon `small` 48x48,  `medium` 92x92, `large` 128x128, and a `silhouette image` (~72x72). These are used in various places.
* Champion icon: 320x256
* Champion Portrait: 240x270
* Clan banner image: 420x420 (unconfirmed)
* Custom Status effect icons: They are sized 50x50 and two needs to be provided one black and white image for tooltips another with white and transparent background for the icon (convert the black to transparent and invert the image)
* Custom Trigger icons: They are also sized 50x50 and can include color
* Card art sprite: This has to be a minimum of 210x250 (and upto 468x468 which is for the zoomed in card) which is what the game resizes the images to. Card Art  can be animated in two ways 1. Shiny Shoe's shader or 2. Standard animation with several images (tutorial not available ask in #mt2-modding).
* Character sprites (or animation): 

    **Static sprites** 

    * image upto 500x500 for a size 4+ unit. (see below for recommended image sizes per size).

    **Animated sprites**

    * An image used for the silhouette this should be the first frame of its idle animation
    * (Recommended) A Spine Skeleton animation exported for Spine Pro 4.2.20 This would include the .atlas, .skel/.json, and .png file (skeleton animation)
    * (Alternative) A set of images defining the animations (traditional)
    * For both Spine and Traditional animations there must **at least** be an idle animation, it is standard for characters to have an idle, hit_react, and attack animation.
* Artifacts: static image sized 256x256 along with a hud icon sized 96x96
* Equipment: Icon sized 128x128
* Rooms: Icon sized 112x112
* Upgrades: Icon sized upto 200x200


Character Sprites Rule of thumb
* Size 1 units average 200px tall (Recommended 180x200)
* Size 2 units average 360px tall (Recommended 340x360)
* Size 3 units average 430px tall (Recommended 440x430)
* Size 4+ units can be 500px tall (Recommended 500x500)