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


- [FEATURES](#features)

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

An initial schematic of the front end screen screen flow (please note that there are some variations to the actual end design).

*insert workflow diagram here*

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
### Influences
Inspiration for the site layout was taken from on-line music retailers. An example is shown below which has a bootstrap style responsive grid layout.

Example guitar retailer:

![retailer](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/ExampleRetailer.png)


Inspiration for site logo text:

![logos](https://github.com/KelvenH/Guitar-Vault/blob/main/README_FILES/Logos.png)

### Logo & Typography

The site logo took great influence from the 'serif' style logos of some of the greatest known guitar and amp brands (i.e. Marshall, Gibson and Fender). A font was found which paid homage to these world famous logos, yet remained extremely legible.

The site logo-text was achieved by applying the Google Font 'lobster' font-family over a textured 'rust' background which due to the zoom level actually provides a slight 'aged leather' look. A font mask* was then applied using another 'gold' texture image (both texture images were licensed from Adobe Stock). * *see acknowledgements for font-mask*
The layering was achieved in CSS using a combination of text-fill and background-clip with a back-up gold font (declared in the root variable as was the font-family). The CSS is shown here;


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

### Buttons 

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

### Tier Pendants

The guitar images have a pendant displaying the tier (i.e. Platinum, Gold, Silver or Bronze). This was achieved by using a Font Awesome "fa-bookmark" icon for the pendant within an i tag, with a <span> inside containing the text. To this the following Font Awesome classes are applied;
- "fa-layers" - applied to parent to allow stacking
- "fa-fw" - to aid alignment
- "fa-layers-text" - applied to span to put the text on top 
- "fa-inverse" - 
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
    

------
# FEATURES
------
# TESTING
------
# BUGS
------
# FUTURE FEATURES
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
- django secret key generator - https://miniwebtool.com/django-secret-key-generator/
- favicon generator - converted a simple svg image created in Adobe Illustrator into .ico format https://favicon.io/

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
- https://getbootstrap.com/docs/5.1/getting-started/introduction/ : Bootstrap 5 docs
- https://bringyourownlaptop.com/ - guidance on UI / UX using Adobe XD

## Images
- Adobe Stock Images - licensed for textured masks applied to navigation header and logo font
- Andertons.com - online guitar retailer, used for most of the guitar images (some were also sourced from the manufacturers web sites) and source of the guitar specifications.
- the guitar Vault headstock logo was self drawn in Adobe Illustrator



## CONTENTS (click to expand sections
<details>
    <summary>show details</summary>
  
  ## Heading
  content here
</details>
