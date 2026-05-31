label Day12_Con_Kyou_Nozomi_Trance:
    scene bg street1 day with blink
    "It's Friday, and I'm walking to school with a spring in my step."
    # play music Moment fadein 5.0
    play music Beautiful fadein 5.0
    show Nozomi side smile at center, flip:
        xpos -0.2
        linear 1.1 xpos 0.25
    if hypno2 == "zombie":
        show Nozomi noglasses
    n "Kyou! Good morning~"
    show Nozomi smile at flip:
        xpos 0.25
    "I turn and face the unfamiliar but very welcome sight of Nozomi approaching me on the way to school."
    ks smile "Nozomi? Aren't you afraid that we'll be seen together?"
    hide Nozomi
    show Nozomi at center:
        xpos 0.25
    if hypno2 == "zombie":
        show Nozomi noglasses
    n front teasing "I don't think there's much wrong with greeting a classmate on the way to school. What about you?" with dissolve
    "I can feel my heart grow a size or two as I smile at her."
    ks "I don't think you're wrong."
    n smile "So how was your night?" with dissolve
    ks sigh "Eh, I ended up starving myself."
    n surprised "Huh? Whatever for?" with dissolve
    ks "Well, dad came home barely five minutes after you left, saw the cleaned-up plate you left by the sink, and made dinner for just himself."
    n frown "You couldn't make your own?" with dissolve
    ks frown "I wasn't going to explain the mystery meal to my dad."
    ks "Either he'd blow up on me for being greedy or I'd have to tell him I had someone over."
    n annoyed_left "Hm, right..." with dissolve
    "She looks around to make sure no one else is in earshot, then leans in conspiratorily."
    n pout uniform_folded "{size=16}If only you had eaten the lovely cheese omelette I made you.{/size}" with dissolve
    ks smile "Whatever. It was worth it for the fun we had."
    n chuckle "Mhmhmhm~" with dissolve
    stop music fadeout 5.0
    scene bg classroom day with blink
    play sound schoolbell
    "I walk in with Nozomi just in time for the bell and class begins."
    scene bg classroom day
    show Hiroko uniform_armup happy uniform_arm at center, flip
    with blink
    play music Memories
    h "Lunchtiiiime~"
    show Nozomi side laugh at center:
        xpos 0.75
    if hypno2 == "zombie":
        show Nozomi noglasses
    n "Ehehe, that came around quickly, didn't it?" with dissolve
    show Sayori smile uniform_folded at center, flip:
        xpos 0.25
    s "Mm...  perhaps I can catch some z's while we are up on the roof today." with dissolve
    "I hear Nozomi chatting to her friends, and it still bums me out that I can't be around her during school hours."
    "I feel we really have a connection now, with all that we've shared over the past couple weeks."
    "She must feel the same, especially after last night."
    "But it seems the best I can do for now is go up to the roof and watch her from afar, so I'll make my way there..."
    show Sayori concerned
    show Hiroko surprised
    show Nozomi front concerned at tremble
    n surprised "Ah!" with vpunch
    "Ah, crap. I was in such a hurry to get out of here that I got out of my chair and stumbled into Nozomi while she was passing my desk."
    ks concerned "Ah, sorry Nozomi."
    n "Sorry, Sir."
    stop music fadeout 1.0
    show Hiroko surprised_side
    s surprised "Huh? What was that?" with dissolve
    n side surprised_side "U-uhh, what was what?" with dissolve
    h no_arm frown_side "\"Sir\"? {w=0.5}Where did {nw}" with dissolve
    extend "THAT come from?" with vpunch
    play music Rain fadein 5.0
    n "I-I was... I was just being polite?"
    h uniform "He ran into you, though." with dissolve
    n frown_side blush "Y-yes, well why are you making such a big deal of this anyway?" with dissolve
    if hypno2 == "trance":
        s "It is just... Nozomi, your behaviour over the past week or more..."
        s concerned "You have not been sleeping properly, you are falling behind on your studies..." with dissolve
        s "To say nothing of that bizarre incident on the roof yesterday, and your evasiveness whenever we try to speak of this."
        s frown "Not to mention..." with dissolve
        h uniform_armup angry_side "You missed half my tourney and I still dunno what the fuck happened!" with dissolve
        #You have been extremely evasive when we called any of it to your attention, You are keeping secrets from us, and missed an appointment with your closest friend in her time of need." with dissolve
        # if hypno4 == "tickle":
        # s angry "More than that, thre was that bizarre incident on the rooftop yesterday." with dissolve

        # s "It is just... you have not been acting like yourself lately. Is there something you're not telling us?"
        n front irritated "W-well, it's just..." with dissolve
        show Nozomi side frown_side at flip
        n "Ugh, no, we're not having this conversation." with dissolve
        n "Just forget it!"
    elif hypno2 == "zombie":
        s "It is just... you have been evasive with us since your accident. Is there something you're not telling us?"
        n irritated "What? No, there isn't anything I'm not... Ugh, forget it. I'm not in the mood for this!" with dissolve
    show Nozomi:
        linear 1.0 xpos 1.5
    pause 1.0
    if hypno2 == "zombie":
        h uniform_armup surprised_side "N-Nozo?! Hey, wait up!" with dissolve
    elif hypno2 == "trance":
        h furious_side "Oh, {nw}" with dissolve
        extend "HELL no! Don't you run away from me!" with vpunch
    show Hiroko:
        linear 1.5 xpos 1.5
    "And as I'm trying to process all this, the girls just run off."
    show Sayori at center, flip:
        xpos 0.25
        linear 1.5 xpos 0.5
    pause 1.5
    s frown_right uniform "And what is your part in this, I wonder." with dissolve
    show Sayori at center, flip:
        xpos 0.5
    "Well, most of them anyway."
    ks frown "Excuse me?"
    if hypno2 == "zombie":
        s annoyed "Please do not insult me, Kyou. You have been hovering around Nozomi all week." with dissolve
    elif hypno2 == "trance":
        s annoyed "Please do not insult me, Kyou. You seem to have been hovering around Nozomi even more than usual." with dissolve
    s "To say nothing of the rumours that she has been heading to a boy's house after school."
    ks "What?"
    if hypno2 == "trance":
        s uniform_folded "People talk, Kyou. And neither of you are good at being discreet. Especially with that odd spectacle yesterday." with dissolve
    elif hypno2 == "zombie":
        $hypno4 = ""
        s uniform_folded "People talk, Kyou. And neither of you are good at being discreet. Especially after what happened the other day." with dissolve
    if hypno4 == "spank":
        s "So of course a lot of people were interested in what that strange screaming girl from class 3-B was up to."
    elif hypno4 == "tickle":
        s "So of course a lot of people were interested in what that strange laughing girl from class 3-B was up to."
    elif hypno2 == "zombie":
        s "Naturally a lot of people become concerned when one of their classmates shows up with an injury and a flimsy explanation. They wonder what is really going on."
    s annoyed_right "Turns out she went straight to your place. Is that not interesting?" with dissolve
    ks surprised "W-wait, what? You already knew?!"
    show Sayori smirk_right
    "She regards me coolly as a smirk spreads across her face." with dissolve
    s "I did not. As I said, it was just a rumour that she was going to some boy's place."
    s "But thank you for confirming my hunch."
    "Fuck..."
    ks "I promised her I wouldn't tell anyone!"
    s rolleyes "Kyou, in case you failed to notice, the cat is well and truly out of the bag and is being chased around the school by Hiroko as we speak." with dissolve
    s "I am sure that by the end of the day everyone who cares to know will know, so I would not worry about that if I were you."
    s concerned_right "The real secret here is why you specifically?" with dissolve
    ks neutral "Why me?"
    s "One day she cannot stand you, the next she's involved in after-school trysts with you."
    s neutral_right "I am not the most knowledgeable about human behaviour, but I am sure that is not often a natural occurrence." with dissolve
    s "That is some sort of magic, or..."
    s frown_right "Blackmail, perhaps?" with dissolve
    ks surprised "Wh-what!? Of COURSE not!"
    s irritated "Then what? Do not tell me she suddenly fell hard for you." with dissolve
    if hypno2 == "zombie":
        s "At least not in the way most people would mean it."
    ks frown "It's nothing like that... It's complicated."
    stop music fadeout 10.0
    n "Wait!"
    show Sayori concerned with dissolve
    hide Nozomi
    show Nozomi side sad_closed at center:
        xpos 1.5
        linear 1.5 xpos 0.75
    pause 1.5
    n "*huff* *pant* Let's... Let's not do this here..."
    show Hiroko annoyed_side at center, flip:
        xpos 1.5
        linear 1.5 xpos 0.75
    show Sayori at flip:
        linear 1.5 xpos 0.25
    show Nozomi:
        linear 1.5 xpos 0.5
    pause 1.5
    h "Ugh, all that running around and you just come back here."
    show Nozomi:
        xpos 0.5
    show Sayori at flip:
        xpos 0.25
    show Hiroko at flip:
        xpos 0.75
    n frown "Yes, well clearly I'm not outrunning you anytime soon and you weren't going to leave me alone..." with dissolve
    n sad_side "Anyway, it's really not what you think. I seriously don't know what you'd do if you knew..." with dissolve
    if hypno2 == "zombie":
        h uniform sad_side "C'mon, just tell us!" with dissolve
    elif hypno2 == "trance":
        show Nozomi at flip
        h uniform_armup angry_side "For fuck's sake, Nozo! Why're you being like this?" with dissolve
        h furious_side "We tell each other {nw}" with dissolve
        extend "EVERYTHING, don't we?" with vpunch
        h uniform "So why..." with dissolve
        h sad_side "Why're you shuttin' me out?" with dissolve

        # h furious_side "We used to tell each other {nw}" with dissolve
        # extend "EVERYTHING, didn't we?" with vpunch
        # h uniform "So why..." with dissolve
        # h sad_side "Why'd you start getting weird on me?" with dissolve
    play music Sorrow fadein 10.0
    n sad_closed "I'm... I-I'm sorry, Hiroko..." with dissolve
    "Nozomi takes a shuddered breath as she comes to a decision."
    hide Nozomi
    show Nozomi front sleep_concerned at center
    n "Tomorrow, okay? I'll explain everything to both of you, I promise." with dissolve
    s annoyed "This secrecy is baffling to me, but alright. I would indulge you." with dissolve
    n sleeptalk_concerned "We could all meet at Kyou's." with dissolve
    h angry "Why the hell do you want us {nw}" with dissolve
    extend "THERE for?" with vpunch
    show Nozomi side at flip
    n sad_side "Please? For me?" with dissolve
    h uniform_armup irritated "GAWD{nw}" with vpunch
    extend ", this is so annoying. If we weren't besties I'd have kicked your butt by now."
    h frown_side "But, yeah okay. For you." with dissolve
    show Sayori rolleyes
    "Sayori clicks her tongue and sighs." with dissolve
    s "Fine, if it will put an end to this rubbish."
    n side sad "You don't mind, right Kyou?" with dissolve
    show Sayori neutral_right
    "Right. Nozomi knows my living situation by now, and that I'd probably be home alone again." with dissolve
    "And I can understand why she'd want to discuss this outside of school, at the place where it all went down."
    # "Right, Nozomi must've remembered that I'd be home alone this weekend. And I can see why she'd want to talk about something so sensitive there." with dissolve
    ks sigh "As if I have a choice..."
    n sad_closed "Then it's settled. Tomorrow morning." with dissolve
    scene bg blackscreen with fade
    "The rest of lunch period passes uncomfortably for everyone."
    "No one has an appetite to talk about anything else, so it's mostly conducted in uneasy silence."
    scene bg k bedroom eve with blink
    stop music fadeout 5.0
    "As school ends and I return home, I get a text from Nozomi saying she's decided not to visit today."
    "I guess I'm not surprised. My order to see me must have lost any power it might have had the moment she left the house last night."
    "And with her friendships in the balance, I can't imagine how she must feel right now."
    "I send her a quick text message to say it's going to be okay. But what do I know?"
    "We should've been more careful."
    "No. I should've been more careful..."
    jump Day13_Con_Kyou_Nozomi_Trance
