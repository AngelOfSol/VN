label cafe_meeting:
    "1:05 PM Expensive Cafe"
    waitress "Can I help you today sir?"
    think_neet "The waitress looks at me a bit suspicously, probably because I walked through the entire line of people waiting to enter into the cafe.  I'm just looking for FTM amoung the patrons already sitting down in the cafe."
    neet "Uhh, yeah.  Sorry about this, but a friend of mine said she would be waiting for me at this cafe around 1 PM.  I'm just looking to see if she's already sit down to eat."
    waitress "Sigh... Do you have a name? I might be able to see if she has a reservation, and if she's sit down."
    neet "Indeed I do.  FTM is who I'm looking for."
    
    if not persistent.ftm_early_arrival:
        jump no_ftm_cafe
    if persistent.ftm_early_arrival:
        jump ftm_sitting_down
    
label ftm_sitting_down:

    think_neet "The waitress looks down at the reservation sheet, scanning the names.  She stops on one of the names, and gets an odd look on her face."
    waitress "It seems he has sat down.  He's at the table for two in the back of the cafe."
    think_neet "She points to a table with a man sitting down on the other side of the table.  This seems to be an odd occurrence."
    neet "Umm, I'm pretty sure she..."
    waitress "Could I help the next in line please?"
    think_neet "The waitress cuts me off before I can say anything, so I end up starting to walk towards the back of the cafe.  The man sitting at the table is almost definitely the guy I saw earlier."
    think_neet "Why would she set me up a meeting with her brother before talking to me?  I contemplate the situation, and come back with nothing."
    neet "Huh.... No time like the present after all."
    think_neet "I give up on trying to figure this all out, and just walk towards the table."
    think_neet "As I approach I see the man put on a light smile, one that reeks of familiarity and nostalgia."
    think_neet "Arriving at the table, he motions me to sit down.  As I do, I introduce myself."

    jump ftm_neet_meeting
    
label no_ftm_cafe:
    think_neet "The waitress looks down at the reservation sheet, scanning the names.  She stops on one of the names."
    waitress "Ahh yes, FTM.  She seems to have a table for two ready.  Shall I sit you down?"
    think_neet "I didn't see her walk in so this is to be expected."
    neet "That would be ok by me."
    think_neet "The waitress grabs some menus, and brings me over to a table for two in the back of the cafe."
    think_neet "I sit down, and watch the people entering the cafe, looking for FTM. After 5 or so minutes I spot someone."
    think_neet "A man with a familiar face approaches the waitress seating people.  He reminds me of someone from highschool, but I can't seem to put my finger on it."
    think_neet "The waitress looks back down at the reservation sheet and puts on an odd look.  Afterwards she points the man towards me in the back."
    think_neet "He starts walking over towards me, putting me in a slight confusion."
    think_neet "As he approcahes, I see him put on a light smile, one that reeks of familiarity and nostalgia."
    think_neet "Arriving at the table, I motion him to sit down.  As he does, I introduce myself."
    jump ftm_neet_meeting
    
label ftm_neet_meeting:
    neet "Hi there, I'm NEET.  I'm pretty sure I was supposed to meet FTM here?"
    think_neet "The man laughs a bit.  The voice is pitched a bit higher than I've expected."
    unknown_man "Hello NEET, its been a while since we've last talked."
    think_neet "I don't remember talking to such a man.  It is possible though."
    unknown_man "Do you remember me?"
    think_neet "I can't seem to recall meeting a brother of FTM, or any relatives of hers for that matter."
    neet "Can't say I do.  Are you a brother of FTM?"
    think_neet "The man's smile drops a little bit after hearing me say this."
    unknown_man "I guess you never payed enough attention to the social situations of your classmates after all..."
    think_neet "This man's words confuse me.  It's true I never payed any attention to the rest of my grade, but I certainly would not forget a face from those highschool days."
    think_neet "The man reaches towards his wallet, and pulls out what looks to be an ID card."
    unknown_man "Take a look at this."
    think_neet "I accept the ID, and look down to read it."
    think_neet "FTM, DOB XX/XX/XXXX, gender: female."
    neet "Is this some sort of joke?"
    think_neet "The man squirms a uncomfortably.  That was not the reaction I was looking for."
    neet "I didn't mean that way.  It's not everyday a person hands you an ID card that doesn't match the person who seems to own it."
    think_neet "The man settles down a bit."
    unknown_man "That ID card is mine though."
    think_neet "I become silent for a moment.  My brain is trying to process what this means."
    neet "So you are FTM."
    
    if ftm_seen:
        think_neet "I calm down quite a bit.  He (she?) probably doesn't know anything about my trade then.  And he didn't send a person to meet me before he did after all."
        
    ftm "I am indeed FTM."
    think_neet "This ends up being a lot less shocking than I would've expected it to be.  Then again, I'm hardly a normal person after some of the shit I've seen."
    neet "I suppose this also why you were being bullied in high school then."
    think_neet "The man looks a bit surprised at this."
    ftm "You knew?"
    neet "Indeed, never did anything about it though.  I have a pretty isolationist foreign policy after all."
    think_neet "FTM giggles a bit."
    ftm "I don't think anything less of you for not helping."
    ftm "All of the girls though I was pretty disgusting after all.  The boys didn't care for anything except my body either."
    think_neet "A waiter arrives to take our orders.  We both order drinks and a sandwich, with the waiter scurrying off quickly to place them."
    neet "So what did you call me here for?"
    think_neet "This is pretty much the important question as of now.  I care not about who people want to be after all.  I don't discriminate in my anti-social policies, men or women, gay or hetero, black or white, I really don't care about any of them."
    "FTM sighs for a bit."
    ftm "I want to date you."
    think_neet "Well that was blunt.  Then again, that's to be expected of most guys?  I've got to rearrange my expectations of this person a bit."
    think_neet "I shake off the thought and take the statement at face value."
    neet "I'm not one for dating..."
    "FTM gets up to leave."
    ftm "Well... it was worth a shot.  I didn't think you would want to date a someone like me."
    "I wasn't finished talking though, so I motion him to sit back down."
    neet "Don't take that statement the wrong way."
    neet "I don't see anything wrong with you or what you want to be."
    neet "I was merely commenting on my standard foreign policies."
    think_neet "His looks brighten up immediately after hearing this."
    ftm "So that wasn't a no?"
    neet "Well... not exactly."
    think_neet "A silence befalls the table for the moment.  FTM speaks up first."
    ftm "Do you like guys?"
    neet "I don't really have an answer for that."
    ftm "So I have a chance?"
    think_neet "I feel like I should say no here, but why not?"
    think_neet "I don't date, I don't talk to people, and I barely even communicate with the ones who raised me.  Maybe this guy can show me something worth working towards."
    think_neet "This could end up being interesting."
    think_neet "Breaking my normal rules about getting involved with people, I respond to his question."
    neet "I'll go out with you."
    
    "END PART 1"
    
    return
    