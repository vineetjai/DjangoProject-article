# DjangoProject-article

I am trying to arrange articles through the admin account. So group users can read, delete, edit or make a new article according to their privileges and for this administration, control will be in my hand and furtherly, I can review who is doing great work according to their activities.

I had created a registration form for users so they can register and then sign in to see articles. Hence, putting restrictions to provide basic authentication to only users which have an account in it. In the registration form, I had used their name, email-id, passwords. So, we can check if their registration form is valid or not and we have the email-id of users in the database. So, we can send weekly updates to them through the mail.

The user with required privilege can make a new article using web interface. He/She need to give Title, Body, date published in the article and an upload button which can upload thumbnails(mostly Image) which will ultimately help in the description of Article. We can also insert more information of article by changing forms accordingly. 

Articles can also be shown in various different languages in web interface even if you make a new article in a different language by language encoding. So the user can use session language according to his/her ease of understanding.

I also added like button so users can give their vote according to articles is good or not. I also put restrictions that vote can be given by users who have their account. Hence, the number of likes will give Idea about proficient articles.

Some of the features I will add in future was ajax search. So when I will enter a character it will search for all words starting with that character and hence give suggestions for search.  
