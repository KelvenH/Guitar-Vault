<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar-Vault_banner.png">

*Disclaimer: This site has been developed for educational purposes only and forms the final project for assessment through the Code Institute Full Stack Software Developer diploma.* 

<br/>

***
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/GV-Logo.png" align="left" width="100px">
<h1 align="center"> Welcome to the Guitar Vault! </h1>
<h4 align="center"> A subscription service for guitarists</h4>
<h4 align="center"> Keep your G.A.S.* turned down and your amp turned up! </h4>
<p align="center"><sup><i>*G.A.S. Gear Acquisition Syndrome - affects many guitarists with an all consuming desire to expand your collection of gear</i></sup></p>
<h1 align="center" height="100" width="100">:guitar: :notes: :metal:</h1>
<br clear="left"/>

***

# CONTENTS

- [OVERVIEW](#overview) 
- [USER EXPERIENCE (UX)](#user-experience-ux)
- [STRATEGY](#strategy)
    - [BUSINESS STRATEGY](#business-strategy)
    - [USER STORIES](#user-stories)
    
- [SCOPE](#scope)

- [STRUCTURE](#structure)

- [SKELETON](#skeleton)
    - [WIREFRAMES](#wireframes)

- [SURFACE](#surface)
    - [INFLUENCES](#influences)
    - [KEY ELEMENT STYLES](#key-element-styles)

- [FEATURES](#features)
    - [PLANNED FEATURES](#planned_features)
    - [FUTURE ENHANCEMENTS](#future_enhancements)

- [TESTING](#testing)

- [BUGS](#bugs)

- [FUTURE FEATURES](#future-features)

- [DEPLOYMENT](#deployment)

- [TECHNOLOGIES](#technologies)

- [ACKNOWLEDGEMENTS](#acknowledgements)
    - [CODING SUPPORT](#coding-support)
    - [IMAGES](#images)

***

# OVERVIEW
The site offers a subscription service for guitarist. Members enjoy access to a range of guitars (electric, acoustic and bass). Tiered subscription plans provide access to higher value instruments as well as provision of additional services (including express delivery and full guitar set-up). Members receive a 'plectrum' in exchange for their subscription fee which is used to grab a :guitar: from the vault. 

Guitar Vault has been built using <img valign="middle" height="50" src="https://github.com/devicons/devicon/blob/master/icons/django/django-original.svg"/> a <img valign="middle" height="40" src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg"/> framework, and also employs <img valign="middle" height="40" src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-plain-wordmark.svg"/> <img valign="middle" height="40" src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg"/> <img valign="middle" height="30"  src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-plain.svg"/> and <img valign="middle" height="35" src="https://github.com/devicons/devicon/blob/master/icons/jquery/jquery-plain-wordmark.svg"/>. The deployed site is hosted on <img valign="middle" height="40" src="https://github.com/devicons/devicon/blob/master/icons/heroku/heroku-original-wordmark.svg"/>, the static and media images are hosted in the :cloud:  with <img valign="middle" height="75" src="https://github.com/devicons/devicon/blob/master/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg"/>, whilst payments are processed through <img valign="middle" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/cc-stripe.png"/>. A fully responsive site layout is handled through <img valign="middle" height="40" src="https://github.com/devicons/devicon/blob/master/icons/bootstrap/bootstrap-plain-wordmark.svg"/>.

Many guitarists suffer from G.A.S. (Gear Acquisition Syndrome) - a desire to accrue a range of guitars (as well as amps and pedals) to expand their tonal possibilities. There are many downsides to this, principally the bank balance battering and the need for space for all these instruments. And of course, you can only play 1 guitar at a time. Often the G.A.S. niggle is only temporarily quelled with a new purchase, before the urge for the next guitar takes over! This is where Guitar Vault comes in. Through this service, members get the chance to get their hands on a high end instrument and although these will only be in your possession for a month, the remedy comes from another guitar of your choosing to keep your playing rocking on and G.A.S. levels tuned down!    

------
# USER EXPERIENCE (UX)
## STRATEGY

### BUSINESS STRATEGY

The business goals of Guitar Vault are;
- generate income through a paid subscription service
- provide clear images and information on the available guitars to entice new clients & retain existing clients
- have a clear and simple business proposition

### USER STORIES

| As a...         | I want to...                       | Because...                                               |
|-----------------|------------------------------------|----------------------------------------------------------|
| site user (any) | Understand the purpose of the site | See if this is relevant to me                            |
| site user (any) | Easily navigate the site           | Find the content I'm looking for                         |
| site user (any) | Be able to view the site on any size screen | So all content / images can be seen clearly     |
| site user (any) | Have clear information on pricing  | To decide if to join / which plan is affordable          |
| site user (any) | Be able to filter / search guitars | To find guitars which match my interests                 |
| site user (any) | Be able to see detailed information about the guitars | Match instruments with my preferences |
| site user (any) | Register for an account            | To become a member                                       |
| registered user | Pay for my subscription plan easily| Clarity if / how much I have been charged                |
| registered user | Login / out easily                 | Access / exit my account                                 |
| registered user | Be able to recover/reset my password | Access my account                                      |
| registered user | Be able to manage my subscription  | Change / cancel my subscription plan                     |
| registered user | Select a guitar to receive         | To obtain the guitar                                     |
| registered user | Save particular guitars as favourites| For future choices                                     |
| registered user | See a list of the guitars I've had with my rating| For future choices                         |
| registered user | See ratings given by other users   | To inform my decisions                                   |
| site administrator | View and manage guitars         | Ensuring items are available to view / loan              |
| site administrator | View / manage registered members| Visibility of subscribed members                         |
| site administrator | View / manage subscription plans| Ensure correct prices are displayed / charged            |
| site administrator | View / manage subscription orders| Visibility of members who have signed up                |


------
## SCOPE
The scope of this activity includes;
- provision of a site which satisfies user stories in being able to view, interact through the front-end.
- manage site content (guitars, categories, orders and subscription plans) through back-end technologies (in some cases through Admin).
- enable payments to be made and recorded.

Out of scope;
- additional activities which in a real business would be required, such as; scheduling of on-going monthly payments (only the initial payment is demonstrated), inventory management systems relating to the handling / scheduling of guitar loan bookings, delivery & collection processes, etc.

------
## STRUCTURE
*Please note; not all planned content was able to be completed in time. Some aspects of these feature in the user stories and in the planned wireframes, database schema. These are clearly indicated in the testing (against user stories) and within the planned future enhancements table.*

### FRONT END STRUCTURE & SCREEN FLOW

The structure of the site should provide a clean and clear interface for site users. Leveraging from django's app structure, there will be specific page content for each app module, yet a baseline html view will be applied consistently across all pages. Site navigation will primarily be through the navigation menu displayed in the header (and through an icon for small screen devices). The only exception to this will be the additional on-screen links (visually displayed as buttons) to proceed to the next / return to the last view (e.g. proceeding to the payment form.

### DATABASE STRUCTURE
*Please note comments above re aspects not delivered in this build as well as some deviations from the original design*

This build will leverage django's SQLite database during development. Upon deployment this will migrate to POSTGRES (once hosted on HEROKU).

The diagram below outlines the core components of the database - the individual tables, their expected fields and relationships between them. Most tables will be structured within their own django app with some exceptions (e.g. guitars and categories will both be held in the same model).

In summary;
- Categories - classifies guitars (Electric, Bass or Acoustic)
- Guitars - houses all information relating to each guitar including the image ID
- Subscription Plans - contains the tier (Platinum, Gold, Silver and Bronze) their price and details of any additional features
- Member Profiles - users personal information (delivery address, contact details), active subscription plan and guitar rack* (past, current and 'favourited guitars) * *not implemented*
- Orders - information on subscription plans purchased through the site

![Planned DB Structure](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Planned%20db%20structure.png)

------
## SKELETON
### WIREFRAMES

Wireframes were developed in Adobe XD, png exports are attached below. Initial designs were produced for desktop view with the intention of columns being condensed (via Bootstrap responsive grid). An example mobile screen was produced for the home screen but not for the other html pages.

Homepage (desktop)

![Homepage desktop](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Homepage-Desktop.png)


Homepage (mobile)

![Homepage mobile](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Homepage-Mobile.png)


Login/Out (desktop)

![Login out](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Login_Out.png)


Guitars List View (desktop)

![Guitar List View](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/GuitarList.png)


Guitar Detail View (desktop)

![Guitar Detail View](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/GuitarDetail.png)


Sign-Up / Payment (desktop) *note these were split into 2 seperate screens in the final development to leverage django allauth for sign-up independently from payments*

![SignUp Payment](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Sign-upForm.png)


Members Profile (desktop) *planned but not yet implemented*

![Profile](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Profile.png)


## SURFACE
### INFLUENCES
Inspiration for the site layout was taken from on-line music retailers. An example is shown below which has a bootstrap style responsive grid layout.

Example guitar retailer:

![retailer](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/ExampleRetailer.png)


Inspiration for site logo text:

![logos](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Logos.png)

### KEY ELEMENT STYLES

LOGO

The site logo took great influence from the 'serif' style logos of some of the greatest known guitar and amp brands (i.e. Marshall, Gibson and Fender). A font was found which paid homage to these world famous logos, yet remained extremely legible.

The site logo-text was achieved by applying the Google Font 'lobster' font-family over a textured 'rust' background which due to the zoom level actually provides a slight 'aged leather' look. A font mask* was then applied using another 'gold' texture image (both texture images were licensed from Adobe Stock). The layering was achieved in CSS using a combination of text-fill and background-clip with a back-up gold font* (declared in the root variable as was the font-family). 
* *see acknowledgements for referrence used for application of font/text masks*

The CSS is shown here;


``` 
    .gold-special-txt {
        color:var(--off-gold); /*- backup font color if text mask fails -*/  
        background: url('/media/gold-texture.jpg');  
        background-size: cover;
        -webkit-text-fill-color: transparent;
        -webkit-background-clip: text;
        -moz-background-clip:text;
        background-clip:text;
        }
``` 

The final result achieved;

![site logo-text](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar-Vault_banner.png)

The same styling class is then also applied to the page titles as shown below;

![site text](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/subscription.png)

The site logo was produced in Adobe Illustrator (achieved by tracing the outer edges of a photo of my own Gibson SG for an outline).

![site logo image](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/GV-Logo.png)

It was important to use a 'simple' sans-serif font elsehwere on the site, for which another Google Font was used 'Varta'.

![Varta welcome text](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/welcome.png)

---
Navigation Bar and Menus

The design of the navigation bar employs bootstrap layout to ensure responsive sizing, bootstrap classes / components to create drop-down menus which collapse into an icon for small screen sizes and django template inheritence to aid structure and responsive selections. These are structured across 3 html files;
- base.html - seen on all screens and hosts the logo and logo-text. Links to Account (i.e. sign-in/out, profile), Shopping Bag and Plectrum* are displayed here in larger screens but hidden on smaller devices.
- mobile-nav-items.html - only displayed for smaller screens and allows for the Account / Shopping Bag & Plectrum* items to be displayed on a lower row (increasing the size available in the upper row for logo).
- main-nav-items.html - contains a row of drop-down menus which employ django url filters to narrow the list of guitar items by category (electric/bass/acoustic) and further sub-categories (e.g. tier, left-handed).This menu is collapsed into a single icon for small screens. It also hosts a 'search bar' which looks for text matches against guitar brands and models.

The elements are styled using the logo fonts 'lobster', standard font 'Varta' and color schemes described elsewhere in this section. Additional custom classes are applied in some cases to override bootstrap defaults (e.g. link styles) and / or size, color and hover state effects. 

*Plectrum is the planned internal 'currency' to loan a guitar which forms part of the member profile not yet implemented.

Navigation Bar - Desktops

![Nav desktop](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Nav-desktop.png)

Navigation Bar - Mobile

![Nav mobile](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Nav-mobile.png)

---
Buttons 

The site buttons use the Bootstrap classes to determine sizing. Custom classes were applied to apply the colors, including hover states.

An example of the primary button css stlying is;

``` 
    .btn-gold-outline {
        color:var(--off-gold);
        border: 3px solid var(--off-gold);
        background-color: var(--transp); /* prevents default white background */
        }
        
    .btn-gold-outline:hover {
        background-color:var(--off-gold);
        color:var(--off-black);
        }
``` 

Button Pre and Post hover

![button](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Button.png) ![button-hover](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Button-hover.png)

---
Guitar Cards

![guitar card](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/guitarcard.png)

Guitars are displayed using the Bootstrap card class. Combination of django loop and if statements enable a card to be produced for each card which satisifes the filtered view (i.e. all or selective depending on the url view generated). The core components of the card are;

- parent card element - Bootstrap .card class for a responsive card layout which handles margin and padding settings
- image - embedded url links through to the individual card-detail page (which shows additional information)
- .card-overlay & tier pendant - the card overlay acts as a container to position the tier outside of the card-body. The tier pendant combines Font Awesome icon and text label relating to the specific tier of the guitar (*see Tier Pendant section below for more information on the structure of this element*)
- .card-body - container for `<div>`'s which holds flex-box rows (using Bootstrap .d-flex & .flex-row classes) which each hold a pair of `<p>` tags for a label and value with the latter populated through the django loop and template tags.
- .card-footer - container for Add / Remove Favourite and Add / Remove to member's rack icons - note that these form aspect of the members functionality which have not yet been implemented (*see svg section below for more information on the icons*)

Additionlly, the cards are held in parent Bootstrap columns so as layout provides a single card (100% screen width) for small screens, increasing through the Bootstrap breakpoints up to 4 cards for extra large screens.
    
<details>
    <summary>Show HTML Extract of card</summary>

    ``` 
           <div class="row">
                    
                    {% for guitar in guitars %}

                        <div class="col-12 col-md-6 col-lg-4 col-xl-3 mb-4">
                            <div class="card bg-dark guitar-card h-100 gold-accent-outline">

                                <!--card image -->
                                {% if guitar.image_id %}
                                <a href="{% url 'guitar_detail' guitar.id %}" class="guitar-image-link">
                                    <img src="{{ guitar.image_id.url }}" class="card-img-top" alt="{{ guitar.brand }} {{ guitar.guitar_model }}">
                                </a>

                                {% else %}
                                <a href="{% url 'guitar_detail' guitar.id %}" class="guitar-image-link">
                                    <img src="{{ MEDIA_URL }}noimage.png" class="card-img-top " alt="{{ guitar.brand }} {{ guitar.guitar_model }}">
                                </a>
                                {% endif %}

                                <!-- tier pendant (overlays image)-->
                                <div class="card-custom-overlay pt-0">
                                    <div class="fa-layers fa-fw tier-pendant">
                                        {% if guitar.tier %}
                                            {% if guitar.tier == 'Platinum' %}
                                                <i class="fas fa-bookmark fa-6x tp-platinum"></i>
                                                <!--Longer tier requires different transform adjustments for Platinum -->
                                                <span class="fa-layers-text fa-inverse tp-text" data-fa-transform="rotate--270 right-27">{{ guitar.tier }}</span>
                                            {% else %}    
                                                {% if guitar.tier == 'Gold' %}
                                                    <i class="fas fa-bookmark fa-6x tp-gold"></i>
                                                    
                                                {% elif guitar.tier == 'Silver'%}
                                                    <i class="fas fa-bookmark fa-6x tp-silver"></i>
                                                
                                                {% elif guitar.tier == 'Bronze'%}
                                                    <i class="fas fa-bookmark fa-6x tp-bronze"></i>
                                                
                                                {% endif %}
                                                <span class="fa-layers-text fa-inverse tp-text" data-fa-transform="rotate--270 right-27 up-7">{{ guitar.tier }}</span>
                                            {% endif %}
                                        {% endif %}
                                    </div>
                                </div>

                                <!-- card content -->
                                <h5 class="card-title text-center pt-2">{{ guitar.brand }} - {{ guitar.guitar_model }}</h5>
                                <div class="row card-body">
                                    <div class="col">
                                        <div class="guitar-card-list">
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Category</p>
                                                <p class="col-6">{{ guitar.category }}</p>
                                            </div>
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Status</p>
                                                <p class="col-6">{{ guitar.status }}</p>
                                            </div>
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Handed</p>
                                                <p class="col-6">{{ guitar.handed }}</p>
                                            </div>
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Condition</p>
                                                <p class="col-6">{{ guitar.condition }}</p>
                                            </div>
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Condition Rating</p>
                                                <p class="col-6">{{ guitar.rating_condition }}</p>
                                            </div>
                                            <div class="d-flex flex-row">
                                                <p class="col-6">Overall Rating</p>
                                                <p class="col-6">{{ guitar.rating_overall }}</p>
                                            </div>
                                        </div>
                                    </div>    
                                </div> <!--close card body -->
                                
                                <!--card footer-->
                                <div class="card-footer text-muted">
                                    <ul class="list-inline list-unstyled d-flex justify-content-evenly align-items-baseline">
                                        <li class="list-inline-item w-20 pb-0 ">
                                                                                      
                                            <!--option A : Add Favourite -->
                                            <btn type="button" class="btn btn-sm btn-add-fav align-baseline">
                                                <i class="far fa-heart fa-2x"></i>
                                                <p class="pb-0"><small>Add Favourite</small></p>
                                            </btn>
                                            
                                            <!--option B : Remove Favourite -->
                                            <btn type="button" class="btn btn-sm d-none btn-remove-fav align-baseline">
                                                <i class="fas fa-heart fa-2x"></i>
                                                <p class="ps-2"><small>Remove Favourite</small></p>
                                            </btn>
                                        </li>

                                        <li class="list-inline-item w-20 pb-0 align-baseline">
                                            
                                            <!--option A : Add to Rack -->
                                            <btn type="button" class="btn btn-sm btn-take align-baseline">
                                                <img src="{{ MEDIA_URL }}Guitar_gold_add.svg" class="guitar-svg add-gold">
                                                <img src="{{ MEDIA_URL }}Guitar_black_add.svg" class="guitar-svg add-black">
                                                <p class=""><small>Add to Rack</small></p>
                                            </btn>

                                            <!--option B : Remove from Rack -->
                                            <btn type="button" class="btn btn-sm btn-take d-none align-baseline">
                                                <img src="{{ MEDIA_URL }}Guitar_gold_remove.svg" class="guitar-svg add-gold">
                                                <img src="{{ MEDIA_URL }}Guitar_black_remove.svg" class="guitar-svg add-black">
                                                <p class="ps-2"><small>Remove from Rack</small></p>
                                            </btn>
                                        </li>
                                    </ul>
                                </div>      <!--close card footer -->
                            </div>          <!--close card  -->
                        </div>              <!--close card col -->

                    {% endfor %}

                </div>  <!--close sub-parent card row-->
        
    ``` 
    
</details>
    
---
Tier Pendants

![platinum](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/platinum.png)![gold](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/gold.png)![Silver](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/silver.png)![bronze](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/bronze.png)

The guitar images have an overlaying pendant displaying the tier (i.e. Platinum, Gold, Silver or Bronze). This was achieved by using a Font Awesome "fa-bookmark" icon for the pendant within an `<i>` tag, with a child `<span>` containing the text. To this the following Font Awesome classes are applied;
- "fa-layers" - applied to parent to allow stacking
- "fa-fw" - to aid alignment
- "fa-layers-text" - applied to span to put the text on top 
- "fa-inverse" - (recommendation on Font Awesome site to prevent background color bleed) although subsequent testing indicates these do not have an affect but remain applied 
- "fa-6x" - increase overall size of the icon
- "data-fa-transform" - attribute applied in-line to set the vertical text direction (set to rotate--270). This attribute was also used to fine tune the  horizontal alignment (centered) and the vertical alignment (top) - with a slight variation for the 'Platinum' tier due to the longer text length.

    *Note:  some of these Font Awesome styles have required the additional SVG and JS version of the script file*
``` 
    <script defer src="https://use.fontawesome.com/releases/v5.15.0/js/all.js"></script>
```     
Further custom classes position the parent card-overlay object and apply the font color with additional data-tramsform propeties applied to Platinum for the sizing reasons mentioned above.  

Extract of the html & CSS are available below, note the application of the django template tags which allows the correct pendant to be allocated to the guitar (held within a loop statement not shown in this extract) which enables the specific custom classes to be applied with the variations specified for 'Platinum'
  
<details>
    <summary>Show HTML Extract</summary>

    ``` 
            <!-- tier pendant (overlays image)-->
            <div class="card-custom-overlay pt-0">
                <div class="fa-layers fa-fw tier-pendant">
                    {% if guitar.tier %}
                        {% if guitar.tier == 'Platinum' %}
                            <i class="fas fa-bookmark fa-6x tp-platinum"></i>
                            <!--Longer tier requires different transform adjustments for Platinum -->
                            <span class="fa-layers-text tp-text" data-fa-transform="rotate--270 right-27">{{ guitar.tier }}</span>
                        {% else %}    
                            {% if guitar.tier == 'Gold' %}
                                <i class="fas fa-bookmark fa-6x tp-gold"></i>

                            {% elif guitar.tier == 'Silver'%}
                                <i class="fas fa-bookmark fa-6x tp-silver"></i>

                            {% elif guitar.tier == 'Bronze'%}
                                <i class="fas fa-bookmark fa-6x tp-bronze"></i>

                            {% endif %}
                            <span class="fa-layers-text tp-text" data-fa-transform="rotate--270 right-27 ">{{ guitar.tier }}</span>
                        {% endif %}
                    {% endif %}
                </div>
            </div>
    ``` 
    
</details>
    

<details>
    <summary>Show CSS Extract</summary>
    ```
        
        .tp-text {
        font-weight:900;
        }

        .card-custom-overlay {
        position:absolute;
        top: 5%;
        right: 25%;
        }

        .tp-platinum {
        color: var(--purple);
        transform: translateY(1.5rem) scale(1,1.5);
        }

        .tp-gold {
        color:var(--gold);
        }

        .tp-silver {
        color:var(--silver);
        }

        .tp-bronze {
        color:var(--bronze);
        }

    ``` 
 
</details>
    
---
Responsive SVG Icons

<img valign="middle" height="100" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar_black_add.svg"/> <img valign="middle" height="80" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar_gold_add.svg"/> <img valign="middle" height="125" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar_black_remove.svg"/> <img valign="middle" height="60" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Guitar_gold_remove.svg"/>


Font Awesome is used for most of the site icons, one exception was for a guitar shaped icon to be used as a visual aid to add / remove guitars from the member's guitar rack*. The icon was drawn in Adobe Illustrator (same image created that was used for the logo icon referred to above). 4 versions were then created for an add / remove and a default and hover version. The hover version was required as the same color sceme was used for the button icon that they reside on. So when the inverse hover button styles was applied these would have hidden the icon.
The images were exported from Adobe in svg format to preserve the crispness (initial efforts in png format resulted in pixelated / skewed images across responsive screens despite their small sizing). The icons are sized in REM (3rem) for responsive sizing. Rather than employ JS or custom SVG classes to change the hover affect colors, a simpler approach was to host all 4 images with 'display:none' set on the hover version. The hover class (applied to the parent) then alternates the display attribute to switch the visible icon held in child `<image>` tags.

*note that the add / remove guitars from the member's rack forms part of the member's functionality which have not yet been implemented

---
FAVICON

<img valign="middle" src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/favicon.ico"/>

The same guitar icon image was adjusted in Adobe Illustrator to replace the add / remove symbols with GV lettering. When converted to .ico format / sizing, the elongated icon (longer than width) resulted in squashed icon to conform to the boxed 32px x 32px favicon sizing. Retaining the ratio resulted in an icon width which was barely visible. For this reason, the icon was rotated for a corner to corner layout with a background color applied to aid appearance. This was then converted from a png format to .ico format via https://image.online-convert.com/convert-to-svg, whilst https://svgontheweb.com/ also served as a useful reference site for svg creation and site inclusion.

FINAL MOCK-UP

![FINAL MOCKUP](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/smartmockups.jpg)

------
# FEATURES

## Planned Features 

All planned features were achieved with the exception of those which relate to or have a dependency on the member profile aspects which are not yet complete and marked for future enhancement.

| Key Feature                   | Details.                                                          | Delivered              |
|-------------------------------|-------------------------------------------------------------------|------------------------|
| Ability to create an account  | handled by django all-auth                                        |:white_check_mark:      |
| Login / Out                   | handled by django all-auth                                        |:white_check_mark:      |
| Clear site navigation         | nav shown aross screens with collapse for small screens           |:white_check_mark:      |
| Search for guitars            | handled through nav search bar                                    |:white_check_mark:      |
| Filtered views of guitars     | url views embedded in main nav menus                              |:white_check_mark:      |
| Simple and clear layout of guitars | employs bootstrap .card component                            |:white_check_mark:      |
| Detailed view of guitars      | url from card summary through to detailed card view               |:white_check_mark:      |
| Members can favourite guitars | relates to component outstanding - future feature                 |:heavy_exclamation_mark:| 
| Members can add guitars to rack | relates to component outstanding - future feature               |:heavy_exclamation_mark:|
| Members can manage their subscription plans | relates to component outstanding - future feature   |:heavy_exclamation_mark:|
| Members can provide a rating on guitars loaned | relates to component outstanding - future feature|:heavy_exclamation_mark:|
| Site poll to get members feedback | | relates to component outstanding - future feature            |:heavy_exclamation_mark:|
| Non-registered visitors see feedback on home screen | Applied through JS to switch comments        |:white_check_mark:      |


## Future Enhancements

This list summarises the components not yet implemented

- Provide members wih the ability to and view in profile;
    -  favourite guitars
    -  manage subscriptions
    -  exchange plectrum for guitar loan
    -  rate guitars loaned
    -  view past guitar loans

- Provide Admin with;
    - capabilities to view / manage the additional member activities above
    - run a member feedback poll

In response to additional testing outcomes;

- Consider switching all images to nextgen formats (webP) with fallback for unsupported browsers
- improve color contrast ratios
- 
------
# TESTING

The majority of testing is performed manually during the development of the project. Upon completion of the project, there were a small number of known bugs but primarily there is a number of aspects relating to content / planned functionality which was unable to accomodate by the deadline. Additional testing was also performed across the site. 
A summary of the key call outs from all testing activities is summarised below, with any key oustanding matters also reflected in either the Bugs or Future Enhancement sections. 
Further information for each of the testing activities is available in the collapsible sections below. Note that attempts to run the django site through django-html-validator was unsuccesful (time constraints did not permit further investigation on how to correctly install and use this package). 


<details>
    <summary>User Story Testing</summary>
    
    
In summary, all user stories tests passed with the exception of those which relate to member profiles (add / view past guitar requests, add / remove favourites and managing subscriptions). Whilst 1 test has passed relating to guitar ratings being visible to users, the rating itself is hard-coded whereas future enhancements would switch to a calculation of average member ratings (forms part of the oustanding content). 
    
| As a...         | I want to...                       | Test Review Notes                                        | Pass / Fail. |
|-----------------|------------------------------------|----------------------------------------------------------|--------------|
| site user (any) | Understand the purpose of the site | Content available but unexpected behaviour on deployed version| :heavy_exclamation_mark: see bugs for details|
| site user (any) | Easily navigate the site           | Clear and simple navigaiton of the site with nav menu on all pages| :white_check_mark:|
| site user (any) | Be able to view the site on any size screen | Fully responsive tested across multiple screen sizes| :white_check_mark:     |
| site user (any) | Have clear information on pricing  | Subscription pricing provided up front and visible during payment steps| :white_check_mark: |
| site user (any) | Be able to filter / search guitars | Achieved through search bar and menus with filetered views| :white_check_mark:        |
| site user (any) | Be able to see detailed information about the guitars | Summary information provided in list view with full info in detailed screen |:white_check_mark:|
| site user (any) | Register for an account            | Through join link handled by allauth, new sign-ups captured in admin db| :white_check_mark: |
| registered user | Pay for my subscription plan easily| Clear laid out payments form with test payments handled through stripe| :white_check_mark:|
| registered user | Login / out easily                 | Links visible on all screens and handled through allauth  | :white_check_mark: |
| registered user | Be able to recover/reset my password | Reset / recovery links with email linkage to generate sending of email| :white_check_mark: |
| registered user | Be able to manage my subscription  | NOT DELIVERED - SEE FUTURE FEATURES                        | :x:       |
| registered user | Select a guitar to receive         | NOT DELIVERED - SEE FUTURE FEATURES                        | :x:       |
| registered user | Save particular guitars as favourites| NOT DELIVERED - SEE FUTURE FEATURES                      |  :x:      |
| registered user | See a list of the guitars I've had with my rating| NOT DELIVERED - SEE FUTURE FEATURES          | :x:       |
| registered user | See ratings given by other users   | A fixed rating is visible, futher enhancements would see this be generated by users ratings| :white_check_mark:|
| site administrator | View and manage guitars         | Management of all guitars is handled through the admin & fixture files | :white_check_mark: |
| site administrator | View / manage registered members| Managed through the admin                                  | :white_check_mark:|
| site administrator | View / manage subscription plans| NOT DELIVERED - SEE FUTURE FEATURES                        | :x:        |
| site administrator | View / manage subscription orders| Managed through the admin                                 | :white_check_mark:|

    
</details>

<details>
<summary>Lighthouse Performance</summary>

Four key site pages were run through the Chrome Inspector Lighthouse for assessment (shown below). Desktio faired better han mobile, but both had shortcomings primarily in performnce and accessibility. Please see below for details of responsive action taken.

Index - mobile
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-index-mobile.png" width="500">
    
Index - desktop
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-index-desktop.png" width="500">

SignIn/Up - mobile
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-signin-up-mobile.png" width="500">
    
SignIn/Up - desktop
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-signin-up-desktop.png" width="500">
    
Subscriptions - mobile
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-subscriptions-mobile.png" width="500">
    
Subscriptions - desktop
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-subscriptions-desktop.png" width="500">

Guitars - mobile
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-guitars-mobile.png" width="500"> 

Guitars - desktop
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/lh-guitars-desktop.png" width="500">
    
 | Aspect      | Key Causes              | Recommendations (not directly mapped to causes) | Outcome                                 |
 |-------------|-------------------------|---------------------------------------|---------------------------------------------------|
 | Performance | Contentful paint times  | switch png images to next gen formats |  Please see point 1 below                         |
 | Performance | Time to interactivity   | eliminate render blocking resources   |  Causes identified as 3rd party libraries (bootstrap, jquery) outside of my control |                                                 |   
 | Performance | HTTP/1.1                | serve resources over http/2           |  Files identified relate to AWS configuration - lack of knowledge to implement safe changes|
 | Accessibility| Color Contrasts        | Switch colors used                    | This was also self-identitied as a possible issue particularly white / gold text with 'gold' coloring scheme for that tier. Some adjustments were made to the background gold to darken from the original selection and also investigated use of text shadows but these were not providing a satisfactory result. Added to future enhancements |
 | Best Practices| Browser errors were logged to the console | Resolve errors     | This was self identified and appears on the outstanding bugs list. The cause is due to JS used to switch feedback which is not displayed if a user is logged in |   
 | SEO          | Links not crawlable | Ensure hrefs link to appropriate destination | At the time of running these reports the 'About US' modals were incomplete but plan to be resolved by the time of project submission |
    
  1. Thorough review undertaken on the guidance to switch jpeg / png images to next gen formats. Steps taken;
        - downloaded Google's Photoshop plugin to convert images to webP (format not natively supported by Adobe)
        - converted the banner background image which reduced the file size by c.50%
        - within the development environment swapped out the jpeg for webP version, re-running the index page for mobiles saw the score improve from 64% to 80%.
        - at this point I was considering adopting this format for all images, however according to caniuse.com not all browsers support - chiefly Safari (only partial support for certain Op Sys).
        - this would mean providing a fall back solution to provide both formats. The task would therefore involve;
        - creating a webP version of all site images
        - saving these to AWS S3 bucket
        - switching existing image tags to a picture with source tags to serve webP or fallback
        - updating the fixture files to have 2 versions of each image (as image links are often not hard-coded but idenfified via the django loop / tags
        - identifying a fall-back approach where images are served as background-images from the css file.
    For these reasons, the time remaining and the risk of causing unintended behavious so close to project submission the activity was not progressed but has been added as a future enhancement.
    
</details>


<details>
    <summary>HTML Validation</summary>
Individual HTML pages were run through https://validator.w3.org/. The only errors identified (c. 30 for each page) were all identified as 'parse errors'. These seem to relate to the validators inability to recognise / handle django html templates. All tags were removed in a couple of pages and no other errors were identified providing comfort that there are no concerns with the html structure.
    
</details>


<details>
    <summary>CSS Validation</summary>
    
Prior to validation, the CSS was run through https://autoprefixer.github.io/ to review and apply additional browser compatability extensions. This was then passed through W3C CSS validator and passed with no errors identified. There were 40 warnings identified but upon review these mainly related to the vendor pre-fixes and were of no concern.
    
<img src="https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/w3c_css_validation.png" width="500">    
    

</details>



<details>
    <summary>JS Validation</summary>
Only a small amount of cutom JS resides in the construction, there were only 4 issues identified when run through JShint relating to missing semi-colons which have been resolved. 
</details>



<details>
    <summary>Responsiveness</summary>
During development, signficant checking for responsiveness was performed via Google Inspector. This allowed breakpoint corrections, media queries to be developed at the time of content creation.
    
Post deployment, the site was viewed through lambdatest.com for a selection of screen sizes, browsers and operating systems. Free acount limits to 6 tests so a mix of broadening the possible ranges were chosen. The configurations checked are shown in the table below. There was 1 instance of unexpected behaviour encountered affecting Apple devices running iOS (whereby the nav banner 'scrolled' as content below the nav was navigated. However I also checked this manually on an iPhone (X) and Ipad (2019 Pro) and neither of these experienced the same issue. The CSS was also checked and confirmed as having a fixed position. 
    
The CSS was also run through auto-prefixer (as referrenced under CSS validation) to ensure any additional vendor pre-fixers were applied.
    
Table of responsive configurations checked;
    
 | Browser      | Device                   | OS        | Resolution | Outcome          |
 |--------------|--------------------------|-----------|------------|------------------|
 |Firefox       |  Mobile - samsung        | Android   | N/A        |:white_check_mark:|
 |Chrome        |  Mobile - Google Pixel 4A| N/A       | N/A        |:white_check_mark:|
 |Safari        |  Mobile - iPhone 12      | iOS       | N/A        |:heavy_exclamation_mark:|
 |Edge          |  Desktop                 | Windows 10| 1280 x 800 |:white_check_mark:|
 |Chrome        |  Desktop                 | Windows 8.1|1600 x 1200|:white_check_mark:|
 |Safari        |  Desktop                 | macOS Mojave| 1024 x 768|:white_check_mark:|
 
    

</details>

------
# BUGS

| Item      | Details                              | Additional Notes                                                                                       |
|-----------|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| Image Carousel | Carousel timing issues| Initially planned to have a single carousel which showed multiple images which scrolled across the page. Bootstrap did not seem to support this so multiple carousels were created and timed to scroll, but factors influence the rendering / JS timing impacting the visual experience |
| About Us modals | Inconsistent behaviour in deployed vs development environments | The modal content is held in a block on the base template with block tags on the main-nav items (where links to the modals reside) as well as index.html as there are also links in the About Us section. These work as planned in development, but deployed site has inconsistent behaviour with either not showing or showing but without CSS being applied. These were late additions to the site without time to investigate a fix or switch to hosting on individual html pages. |
| JS Error  | JS 'cannot set propoerties of null'  | Self identified in console and identified by LightHouse. Cause is due to the fields JS is manipulating being intentionally only shown for non-logged in users |



------
# DEPLOYMENT
------
# TECHNOLOGIES

## Design; 
- Adobe XD (UI / UX development stage, inclduing simple database structure)
- Adobe Illustrator (headstock logo)

## Languages, frameworks, libraries and apps;
- GitHub (host repository)
- GitPod / VS Code (development environment)
- django (core framework which integrates the following)*
- HTML5
- CSS3
- Bootstrap5 (html / css styles framework)
- Python
* Additional django / utility apps (referrenced in requirements.txt);
 - django-allauth (authentication)
 - django-countries (enables in form dropdown of country codes - required to validated stripe payments)
 - pillow (enables use of images)
 - crispy-forms & crispy-bootstrap5 (enable bootstrap styles in rendering form fields)
 - django-storages (intergrate with deployed database)
 - gunicorn (wsgi web server integration)
 - dj-database-url (configuration with Heroku hosted database)
 - psycopg2-binary (PostgreSQL database adapter)
 - botocore & boto3 - (configure with AWS services)
- Font Awesome - icons
- Google Fonts - typography

## Deployment
- Heroku (including PostGres SQL for database)
- AWS (media and static image hosting)

## Testing
- Lighthouse
- W3C Markup Validation Service (HTML)
- W3C CSS Validation Service (CSS)
- JSHint (JS)
- PEP8 online (Python)
- autoprefixer (browser compatability extensions)
- lamdatest.com (browser / os compatability, responsiveness testing)

## Miscellaneous
- https://miniwebtool.com/django-secret-key-generator/ : django secret key generator
- https://favicon.io/ : favicon converter (svg image created in Adobe Illustrator into .ico format) 
- https://smartmockups.com/ : generated final web site 'mockup' from deployed link for inclusion in README 

------
# ACKNOWLEDGEMENTS

## Coding Support
- CI template : https://github.com/Code-Institute-Org/gitpod-full-template
- Boutique Ado (CI Django walkthrough) : large parts of the project especially struture (django models and views) were based on this exercise.
- Net Ninja (YouTube channel https://www.youtube.com/playlist?list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc) : additional guidance on django structures
- Tutor Support (Sean and Igor) : aided with a couple of challenges I struggled to solve (both were due to incorrect referrencing of elements in models) 
- Slack : primarily when encountering django obstacles
- StackOverflow : point of referrence for number of coding queries
- https://css-tricks.com/how-to-do-knockout-text/ : logo text font mask
- https://svgontheweb.com/ : guidance on creation and styling of SVGS (referred to for add / remove guitar icons).
- https://docs.djangoproject.com/en/3.2/ : django documentation
- https://getbootstrap.com/docs/5.1/getting-started/introduction/ : Bootstrap 5 docs
- https://bringyourownlaptop.com/ - guidance on UI / UX using Adobe XD

## Images
- Adobe Stock Images - licensed for textured masks applied to navigation header and logo font
- Andertons.com - online guitar retailer, used for most of the guitar images (some were also sourced from the manufacturers web sites) and source of the guitar specifications.
- the guitar Vault headstock logo was self drawn in Adobe Illustrator
