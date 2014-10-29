# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define neet = Character('NEET', color="#0FA1A2")
define ftm = Character('FTM', color="#A0F383")
define mom = Character('Mom', color="#020383")
define unknown_buyer = Character('Unknown Buyer', color="#FF00F0")
define unknown_actor = Character('Unknown Person', color="#F000FF")

# The game starts here.
label start:
    "It was just another one of those days, you know?  The kind where you get up, and realize nothing is going to go right today. So you do all you can to minimize the damage, and it never ends up being enough."
    #fade out fade in
    "9:00AM Bedroom."
    "SCREECCCCCHHHHHHH."
    neet "Ugh.... Why do I even use this alarm...."
    "I turnover my phone to shut off the alarm.  The annoying screech is a great way to force my self up, but it feels like I'm being subjected to the rack. The grating sound ruins whatever sleep I got that night."
    "Nevertheless, I fall back asleep, waiting for the second alarm telling me its actually time to get up."
    #fade out fade in
    "9:45AM Bedroom"
    "After waking up to a second alarm, I wander off towards the shower."
    neet "Guess I have to go outside today.  The buyer did want it dropped off before tomorrow 5:00AM."
    neet "Sigh..."
    neet "I don't even know why I bother anymore."
    "Today was one of those days I needed to provide one of the few things I do well: porn."
    "I don't make porn though.  Still a virgin after all.  Never had a girlfriend either, not that I hadn't been asked before. Middle school seemed a bit early to start a romance, but that rejection had followed me throughout highschool."
    "Not that I care though.  Romance has never been my thing.  Then again, neither is anything else in this world."
    "Either way, you've got to make money somehow, so I make mine through porn. Usually, I scavenge the dark parts of the internet, dive into the dumpsters in bad parts of town, and talk to people in shady alleys late at night."
    "I provide some of the most disturbing porn I can find to a willing buyer. After all, the money is good, and I can find almost anything someone wants. Snuff, child, necrophilia, torture, bestiality, incest, you name it."
    neet "I wonder what the buyer wants this week..."
    "Getting out of the shower, I put on a dark hoodie, and some jeans."
    "Beep. Beep. Beep."
    "Wondering who could possibly text me at this hour, I walk over to my phone."
    "3 text messages unread."
    "Flipping my phone open with a crack, I check the unread messages.  2 unknown numbers and my mother.  1 more text than I was expecting, how odd."
    
    python:
        mom_text = False
        unknowns_read = 0
    
    label read_texts:
    
    menu text_menu:
        "Read the first unknown text." if unknowns_read == 0:
            $ unknowns_read += 1
            unknown_buyer "7pm at the park off of main street.bring everything"
            "Well, that wasn't unexpected.  Thought it would be a bit earlier in the day, but some people like the night."
            "Probably need to bring my self defense kit though, it gets too dark too early to do this without protection."
            "Would it have killed him to use proper captialization and punctuation though?"
            
            jump read_texts
        "Read the second unknown text." if unknowns_read == 1:
            $ unknowns_read += 1
            unknown_actor "Hey there NEET.  My name is FTM.  You might not remember, but we went to highschool together.  I'm in town (you do go to XX college right?) and was hoping we could meet up sometime.  I'll be at the cafe on main street around 1PM if you're up for it."
            "That's a surprise."
            "The name rings a bell.  Thinking back, I remember there being a girl in highschool named as such.  She was bullied a lot, though I never payed attention.  I couldn't get myself to care about anything yet."
            "Looking back, I feel bad for not doing something for her, because I've been there before.  No use worrying over the past though, what's done is done."
            "Don't know if its a good idea to meet up with someone who could talk to my parents, but its not like I have any plans."
            
            menu response_text:
                "Respond to her text.":
                    $ response_text = True
                    "Might as well let her know I'm going to be there at 1."
                    "I quickly pound out a message letting her know I'm gonna be there on time.  No harm in that."
                "Don't respond to her text.":
                    $ response_text = False
                    "Her message does imply she'll be there regardless, and I might change my mind before 1, so I'll let the message sit for now."
            jump read_texts
        "Read Mom's text." if not mom_text:
            mom "Hope your doing well buddy.  Don't forget to call sometimes."
            "Good old parental guilt sets in.  My parents still don't know I've dropped out of college.  Calling them would probably only make them angry though, so I'm putting it off for another year or too."
            "Luckily, I've stopped paying the tuition.  I told my parents I'd pay my own way through college.  It seems I knew even back then I was going to drop out early."
            "I'm no leech either, my unique erotica distribution pays for all my rent and utilities.  I've still got a good chunk saved up too.  If it weren't for the line of work, my parents would probably be extremly proud of my self sufficency."
            $ mom_text = True
            jump read_texts
    "Having finished reading and responding to my text messages, I get started on breakfast."
    #fade out fade in
    "11:30AM, Hallway."
    
    "After finishing my morning routine, I comtemplate my upcoming events for the day: the meetup with FTM, and the erotica drop off.  Neither is particularly important, but I don't like being unprepared for events I've decided to attend to."
    "I gather up all of the stuff my buyer ordered, and pack my taser and pistol into my vest.  Being licensed for a concealed carry is nice when you do shady business all the time."
    "Never really end up using the gone though, murder is not really my cup of tea.  Either way, most people go down from a nice taze to the chest, and bullets can be expensive."
    "The erotica is packed up into a briefcase with a false bottom.  Don't want any of that stuff dropping out in the middle of the street."
    "Once had a kid try to steal my briefcase, and he ended up opening it in and spilling the contents out.  False bottom protects the goods from thieves and from police."
    neet "Might as well bring some money for the cafe too."
    "The meeting with FTM is probably going to take a while, and I'd like to be able to eat while I'm there.  Breakfast was pretty shitty today, as my Cheerios have gotten stale."
    "Thinking about it, I could probably treat her to lunch too.  Sitting around with so much money eats at my soul a little bit.  Plus, it'll get my kind deed for the day out of the way."
    "..."
    neet "Now that I'm all packed up, I wonder if I should scout the cafe or the park before the meetings."
    neet "I haven't been to the either of them in a while, so traffic patterns probably have changed again."
    "This city's traffic planning tends to vary every week, because of the massive influx and outflux of people we have every now and again.  The population here varies wildly from week to week."
    menu scout_choice:
        "Scout the park.":
            jump scout_park
        "Scout the cafe.":
            jump scout_cafe
    return