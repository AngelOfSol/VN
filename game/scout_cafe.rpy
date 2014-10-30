label scout_cafe:
    $ persistent.scouted = "cafe"
    "12:05 PM Cafe"
    think_neet "I walk towards the cafe on Main Street."
    think_neet "The street is bustling with people all heading towards the cafe I'm supposed to meet at.  Which is odd considering today is a work day for most of the people in this town."
    think_neet "Not to mention the cafe in question tends to be on the really expensive side in terms of price."
    store_sign "SALE 40\% OFF EVERYTHING FOR TODAY."
    think_neet "What a sale."
    think_neet "I don't think I've seen a cafe, or any restaurant for that matter, have an all day sale with such a big drop in prices."
    neet "I hope FTM has a reservation for today..."
    think_neet "I'm not too keen on waiting for my food.  I can barely stand a 10 minute wait to be sit down to a table, which is in addition to the time it makes them to actually cook the food."
    think_neet "Either way, we can always move to a different cafe to eat at if the wait is too long."
    think_neet "I walk across the street from the cafe, and pick up a newspaper.  People tend to ignore those who are reading on benches, letting my surveil the area a bit better."
    think_neet "I'll watch the cafe to see if I can spot FTM as she arrives.  I doubt she knows what I do for a living, but one can never be too careful in their preparations."
    think_neet "I spend the next 50 or so minutes watching the various customers of the cafe enter and leave the building."
    think_neet "It seems like a lot of office workers are coming down from their locations of work to eat the expensive food that for today is being provided at a cheap price."
    
    if not persistent.ftm_early_arrival:
        jump no_ftm_arrival
    if persistent.ftm_early_arrival:
        jump someone_like_ftm
    
label no_ftm_arrival:
    think_neet "A couple customers stand out to me as suspicous, but none of them seem to be FTM, or anyone else I've encountered before.  I've got no skin in the game for calling them out on their activities right now, so no point in bothering with them."
    think_neet "I spend a couple minutes watching the other restaurants on the street."
    think_neet "The sale at the cafe seems to be denting their profits for the day, as I only see a few patrons enter in and out of the other restaurants.  Today is probably going to be a loss for them."
    think_neet "The waiters and waitresses probably have it the roughest though.  With no customers, their tips will not be up to par for the day."
    think_neet "I go back to reading the newspaper a for a bit, and take a look at my watch."
    jump end_scout_cafe
    
label someone_like_ftm:
    think_neet "I see a couple suspicous patrons for the expensive cafe, but I quickly become interested in one man I see walk in the door."
    neet "That face looks awfully familiar."
    think_neet "I see a face that reminds me of someone back from highschool."
    think_neet "It bothers me though, that face belongs to a woman, not a man, after all.  I wonder if FTM had a brother, and had him scout out the cafe before hand."
    think_neet "Don't know why she would need protection when meeting with someone like me, unless she knew what I'm doing for a living."
    think_neet "I start comptemplating escape plans from the busy cafe, as my alarm level rose quite a bit after this new information."
    $ ftm_seen = True
    think_neet "Slipping my taser into my left hoodie pocket, I move things around in my personal protection pack."
    think_neet "The time flies as I map out possible scenarios for the upcoming meeting."
    think_neet "Hopefully, there is little to worry about for the meeting though.  I hadn't planned on getting mixed up in anything today."
    jump end_scout_cafe
    
label end_scout_cafe:
    neet "Well, it seems like its time to go inside the cafe to look for FTM."
    think_neet "I set my newspaper down on the bench, and watch the cars speed past before I attempt to cross the street."
    jump cafe_meeting