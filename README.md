# Flea Finder Stockholm
Django project for Code Institute (PP4)

## General Information
Flea finder Stockholm is a meeting place for people interested in markets in Stockholm. It’s a tool for vendors/event makers to share their events. And for shoppers/tourists/market conousseurs it’s a place where you can easily find a wonderful market to go to.

This Django project is a flea market blog designed to help users find flea markets happening in Stockholm. Unregistered users can view the content, but not interact much with it besides from reading posts and comments and filling out a contact form. Registered users are able to interact with the content by creating, commenting and liking posts.

*Link to deployed website*

*Screenhots*

## Table of Contents

  - ### [General Information](#general-information)
  - ### [Table of Contents](#table-of-contents-1)
  - ### [UX](#ux-1)
  - ### [Project Goals](#project-goals-1)
  - ### [User Stories](#user-stories-1)
  - ### [Flowchart](#Flowchart-1)
  - ### [General features](#general-features-1)
  - ### [Testing](#testing-1)
    - #### [Code Validation](#code-validation-1)
    - #### [Testing User Stories](#testing-user-stories-1)
    - #### [Manual Testing](#manual-testing-1)
    - #### [Future improvements](#Future-improvements-1)
  - ### [Bugs](#Bugs-1)
  - ### [Libraries and Software](#Libraries-and-Software-1)
  - ### [Final Result](#final-result-1)
  - ### [Deployment](#deployment-1)
  - ### [Github Pages](#github-pages-1)
  - ### [Credits](#credits-1)

## UX

The rule of threes
User in mind
Simple, Intuitive design
Hierarchy of information (post list shows date Title, time location)

### Agile
This project was designed using an agile approach from start to finish. I Used the Git Hub projects function to plan this project and assigned them labels according to their importance.
Increments, Epics…?
Acceptance criteria,
Tasks,

### 5 Planes of UX

Strategy
Scope
Structure
Skeleton
Surface

### Visual Design Choices

Colour scheme

Fonts

Images and icons

bootstrap

FEATURES

Browse through different categories like: food, clothes, antiques, seasonal and more. Add your own event and tell everyone about your amazing, upcoming market. Comment and like events you find interesting or want to know more about!

## Project Goals

Type of website: Blog/Online calendar for flea markets/markets
Target Audience: Tourists, Market-enthusiasts

## User Stories

| **EPIC** | **ID #** | **User Story** | **Github project** |
|-------------|------------|---------------------|---------------------|
| **Account Registration** |
|  | 1 | As a Site User I can register an account so that I can post, comment and like posts | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=46192303) |
| **Home Page** |
|  | 24 | As a Site User I can view the home page so that easily understand the purpose of the website | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=52980235) |
| **Post List** |
|  | 5 | As a Site User I can view a paginated list of posts so that I can easily select a page to view | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=46193056) |
|  | 6 | As a Site User I can view a list of posts so that I can select one to read | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=46193253) |
|  | 8 | As a Site User / Admin I can view the number of likes on each post so that I can see which is the most popular or viral | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=46193462) |
|  | 9 | As a Site User I can click on a post so that I can read the full text | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=46193561) |
|  | 17 | As a Site User I can filter the post list by categories so that I can easily select a post to view | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=52981163) |
| **Posts** |
|  | 13 | As a Site User I can like or unlike a post so that i can interact with the content | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=46194124) |
|  | 19 | As a registered user I can add posts so that I can interact with the website | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=49805609) |
|  | 23 | As a registered site user and creator of the post I can update a post i myself have created so that I can manage my own post | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=52979742) |
| **Admin** |
|  | 3 | As a Site Admin I can create, read, update and delete posts so that I can manage my blog content | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=46192736) |
|  | 20 | As a Site Admin I can create, read, update and delete comments so that I can manage my blog content | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=52966548) |
|  | 21 | As a Site Admin I can view, update and delete information about registered users so that I can manage my blog content | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=52967085) |
|  | 22 | As a Site Admin I can create, read, update and delete categories so that I can manage my blog content | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=52967739) |
| **Comments** |
|  | 10 | As a Registered User I can leave comments on a post so that I can interact with the content | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=46193747) |
|  | 11 | As a Site User I can view comments on an individual post so that I can read the conversation | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=46193921) |
| **NOT IMPLEMENTED!** |
|  | 14 | As a Site User I can Write a message so that I can leave feedback on the site-content and/or suggest events | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=52981084) |
|  | 15 | As a Site Admin I can view messages from Site User so that I can respond to messages and/or consider the feedback submitted | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=52981223) |
|  | 25 | As a site user I can sort posts by number of likes so that i can easily find a post to read based on whats most popular | [Link](https://github.com/users/AlmaBroman/projects/3/views/1?pane=issue&itemId=52980611) |
---

## Flowchart

## General Features

## Testing

   - code validation
   - Testing user stories
   - Manual Testing
   - future Implementations

## Bugs

## Libraries and Software

## Final Result

## Deployment

## GitHub Pages

## Credits

Describe in short how ive used the below stated resources

### Resources

 - [Django documentation](https://docs.djangoproject.com/en/5.0/)
 - [Bootstrap Documentation](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
 - [W3Schools](https://www.w3schools.com/)
 -  [Summernote Documentation](https://github.com/summernote/django-summernote?tab=readme-ov-file)
 - [Cloudinary Documentation](https://cloudinary.com/documentation)
 - [ElephantSQL Documentation](https://www.elephantsql.com/docs/index.html)
 - [CodeInstitute - tutor support, slack, mentoring, course content(I think therfore i blog)](https://codeinstitute.net/se/full-stack-software-development-diploma/?utm_term=code%20institute&utm_campaign=CI+-+SWE+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14660337051&hsa_grp=134087657984&hsa_ad=635849372549&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiAw6yuBhDrARIsACf94RUO531QI7q6X9yAB3s7GS_rSIc2x9qXt_eLbx6DJlR3phHXgUaEboEaAs7nEALw_wcB)
 - [OrdinaryCoders - Using django form fields and widgets](https://ordinarycoders.com/blog/article/using-django-form-fields-and-widgets)
 - [good read on how to design a database](https://www.databasestar.com/how-to-design-a-database/)
 - [Custom 404](https://studygyaan.com/django/django-custom-404-error-template-page)

### Youtube
 - [Codemy - django blog tutorial]
 - [Just Soondar - Carousel tutorial](https://www.youtube.com/watch?v=vbmXKfnVkms&ab_channel=JustSoondar)
 - [Dee Mc Django recipe sharing tutorial]


### Sketching Tools
 - [Balsamiq](https://balsamiq.com/?gad_source=1&gclid=Cj0KCQiAw6yuBhDrARIsACf94RWFuAI1AvoLD-OVge1dnsbZQ276DU-1lOZ9UUqGoY65dpZD1PvbQAYaAsFqEALw_wcB)
 - [LucidChart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier2_mixed_search_brand_exact_&km_CPC_CampaignId=1520850463&km_CPC_AdGroupID=57697288545&km_CPC_Keyword=lucid%20chart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433237648&km_CPC_TargetID=kwd-55720648523&km_CPC_Country=2752&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gad_source=1&gclid=Cj0KCQiAw6yuBhDrARIsACf94RWItUjtdfLb1-MmV01hLZvhrfGIHssS2dPuAUo9ObeQCwYlvmeGp5caAsvrEALw_wcB)

### Content
 - chat gpt
 
### Media
 - [Faviocon.io - Favicon Converter](https://favicon.io/favicon-converter/)
 - [Canva - Creating favicon](https://www.canva.com/)
 - Images used in posts and on home page