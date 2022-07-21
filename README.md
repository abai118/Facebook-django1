# facebook-django

## Description
- In this we have created facebook app clone which is having the following designs 

- You can view this app in the link
[facebookCloneapp-django](https://facebook-django-akhil.herokuapp.com/)

- To view the code for github tou can view in this [github link](https://github.com/abai118/facebook-django)


User Stories, User Persona and Database Schema Design are given below 

### 1. User Stories

As a user Facebook clone app have following features:
- As a logged in user, i should be able to create a post.
- As a logged in user, i should be able to like a post.
- As a logged in user, i should be able to create a comment on a post.
- As a logged in user, i should be able to edit my profile.
- As a logged in user, i should be able to send a friend request.
- As a logged in user, i should be able to accept a friend request.
- As a logged in user, i should be able to like a post.
- As a logged in user, i should be able to see my friends.
- As a logged in user, i should be able to edit my friend requests.
- As a logged in user, i should be able to search for friends.

### 2. Database Schema Design

  1. Userauth Table

     - Userid (primary key)
     - Username
     - Password
     - First name
     - Last name
     - E mail

  2. Profile Model
     - User
     - Bio
     - Profile pic
     - Friends
    
  3. Post Table
     - User
     - Postimage(we would leave it as a blank)
     - Post text
     - Likes
     - Time

  4. Comment
     - User
     - Post id
     - Comment text


### 3. User Persona
Person 1

1. User Details
   - Name : Akhil
   - Age: 28
   - Work: Software Developper
   - Family: Single
   - Location: Bengalore

2. User Hobies
   - Travelling to new places
   - Adopting new skills that are required

3. Motivations
   - Socialise with people
   - Knowing about people intrestes
   - Updating according to trends

4. Frequently Used Apps
   - Instagram
   - Youtube
   - Pintrest
   - Twitter


Person2

1. User Details
   - Name : Satya
   - Age: 28
   - Work: Season Business
   - Family: Single
   - Location: Vijayawada

2. User Hobies
   - Travelling to temples
   - spending time with friends

3. Motivations
   - Finding new people with same interests
   - Knowing about people interests
  
4. Frequently Used Apps
   - Instagram
   - Youtube