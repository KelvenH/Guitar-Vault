/* jshint esversion: 8, jquery: true */
document.addEventListener("DOMContentLoaded", function() {
    /*-- BUG FIX: feedback cycle added within if check to prevent script attempting to run if user is not on index.html or the fields are hidden as only visible to non-logged in users  --*/
    if($("#members-feedback").is(":visible")){
        /*-- cycle through members feedback (index.html for non-logged-in visitors) --*/
        const feedbackA = "Having access to guitars I would not otherwise get a chance to play gives pure enjoyment!";
        const memberA = "Paul Wright";
        const feedbackB = "I was a bit sceptical at first, but all instruments have been in fantastic condition. A great service for the guitarist who wants an affordable way to swap their rig!";
        const memberB = "James Hendrix";
        const feedbackC = "I love getting to choose what guitar to try out next and the collection and delivery has been first class!";
        const memberC = "Suzie B";
        const feedbackD = "There's such a great choice of amazing guitars, and I can see that new models are being added regularly to broaden the choices!";
        const memberD = "Matt Bellamy";
        const feedbackList = [feedbackA, feedbackB, feedbackC, feedbackD];
        const memberList = [memberA, memberB, memberC, memberD];
        const membersFeedback = document.querySelector("#members-feedback");
        const member = document.querySelector("#member");
        let i = 0;
        const cycleFeedback = () => {
            membersFeedback.innerHTML = feedbackList[i];
            member.innerHTML = memberList[i];
            i = ++i % feedbackList.length;
        };
        cycleFeedback();
        setInterval(cycleFeedback, 10000); 
    };
    
});
