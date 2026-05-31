label Epilogue_NonCon_Kyou:
    scene bg classroom eve with longblink
    play music Memories
    "As another school day draws to a close, I gather my things and ponder."
    play sound schoolbell
    if ending == "liar":
        "It's been three months since Nozomi and I started our hypnosis sessions."
    elif ending == "hypnotized":
        if preferences.language == None:
            $nozomi_name = "Class Rep"
        elif preferences.language == "spanish":
            $nozomi_name = "Representante de clase"
        show Hiroko uniform_armup angry_side uniform_arm at center
        show Sayori neutral at center, flip:
            xpos 0.25
        h "Fuckin' finally. Now I'm gonna blow off tennis club and punch the walls in my room." with dissolve
        s concerned "I am so sorry about yesterday, Hiroko." with dissolve
        h neutral_side "I can't stop thinking about it, y'know? That shit really got in my head." with dissolve
        "What on earth was I doing these last few months?"
        h sad_side "I messed up..." with dissolve
        s uniform_folded "I can only encourage you to keep going. You have a lot of potential, anyone can see that." with dissolve
        h "Yeah... I mean, what else am I 'sposed to do?"
        show Nozomi side frown_side at center:
            xpos 1.2
            linear 1.0 xpos 0.75
        n "Is everything okay?" with dissolve
        show Hiroko uniform at center, flip
        h "Nah." with dissolve
        show Nozomi:
            xpos 0.75
        n sad_side "I'm so sorry, Hiroko. I got you mixed up in all of this." with dissolve
        s "Was it really right to do what we did? I know it wasn't much, but still..."
        "Well, no point hanging around here. Time to head home."
        n front irritated "We did what we had to. And we got rid of that thing so nothing like that will happen again." with dissolve
        h "I guess..."
        scene bg entrance with fade
        n "Uh, Kyou? Do you have a moment?"
        ks surprised "Huh?"
        show Nozomi front with dissolve
        "Just as I'm heading out I realize our class rep is wanting me for something."
        "Wish I knew what her name was."
        "I guess I could ask, but something tells me I really shouldn't bother her."
        n "It's just... well, how was your weekend?"
        ks frown "My... weekend?"
        "Ugh, what do I tell her? I have no... Oh wait, I remember now."
        ks smile "It was a perfectly normal and uneventful weekend."
        show Nozomi uniform_folded smile
        "As lame as that answer was, it seems to satisfy her." with dissolve
        n "That's great. Sorry, I won't hold you up any longer; have a nice evening."
        ks "Yeah, you too uhh..."
        hide Nozomi with dissolve
        "I trail off as she walks away. Shit, how do I not know this girl's name?"
        scene bg blackscreen with dissolve
        "Oh well. As long as I don't bother her, it's fine."
        jump Credits
    elif ending == "devotion undone":
        show Hiroko uniform frown_side at center
        show Sayori neutral at center, flip:
            xpos 0.25
        with dissolve
        h "Hometime. Great."
        "I still can't believe I had them all in the palm of my hand and I just... let them go."
        h uniform_armup angry_side "Later, losers! Gonna go punch the walls of my room again." with dissolve
        s concerned "I am so sorry about yesterday, Hiroko." with dissolve
        h uniform_headhold2 neutral_side "... Yeah. Well it's my own damn fault, ain't it." with dissolve
        h sleeptalk "Like sure, I was worried about Nozo and all, but I didn't have to skip all that prep work like I did." with dissolve
        "Looking at them now, acting out their lives like I wasn't a total god to them."
        h sad_side "I fucked up..." with dissolve
        s uniform_folded "I can only encourage you to keep going. You have a lot of potential, anyone can see that." with dissolve
        "Man, I could almost believe last week was but a figment of my imagination."
        h "Yeah... I mean, what else am I s'posed to do?"
        show Nozomi side frown_side at center:
            xpos 1.2
            linear 1.0 xpos 0.75
        n "Is everything okay?" with dissolve
        show Hiroko uniform nervous_side at center, flip
        h "Nah." with dissolve
        show Nozomi:
            xpos 0.75
        n sad_side "I'm so sorry, Hiroko. If only I hadn't overreacted when..." with dissolve
        h frown_side "Don't start that again." with dissolve
        "But it wasn't. And I'm just going to have to be okay with my choice to let them go."
        n sad_closed "But..." with dissolve
        h uniform_headhold2 irritated "How many times have I gotta tell ya? Starting to get on my tits how you keep blaming yerself all the time." with dissolve
        "I know that, when it comes down to it, I'm not the kind of guy who'd brainwash girls into worshipping him." 
        h frown_side "Just... Quit worrying about me. I'll figure something out..." with dissolve
        scene bg blackscreen with dissolve
        stop music fadeout 5.0
        "And knowing that... I guess that has to be enough."
        jump Credits
        # scene bg corridor eve with longdissolve
        # "Anyway, I'd better "
    else:
    #Would be nice to incorporate the other girl's newfound hypno fetish in this part of writing.
    # h "What's a girl gotta do to get a little hypno action around here, huh?"
    # Just, the other girl begging Kyou to hypnotize them, while he brushes her off to meet up with Nozo
        if pursued == "Hiroko":
            show Hiroko uniform_armup happy uniform_arm at center
            show Sayori smile at left, flip:
                xpos 0.1
            h "Hometiiime~ {font=DejaVuSans.ttf}♫{/font}" with dissolve
            s "Chipper as ever, Hiroko. Doing anything this weekend?"
            "It's been three months since that day."
            h smile_side "Naaaah. I'm just gonna chill out and play videogames." with dissolve
            "Three months since Nozomi realized her love for me." with dissolve
            s "Are you even trying to do anything productive anymore?"
            h uniform "Oh, what's the big deal? Things'll work out eventually." with dissolve
            s concerned "Will they? We are graduating soon and you have nothing lined up. I'm getting a little worried for you, Hiroko." with dissolve
            h happy no_arm  "It'll be fine~ I'll get a job at a convenience store or something, don't stress." with dissolve
            s "Hiroko..."
        elif pursued == "Sayori":
            show Hiroko uniform_arm  neutral_side at center
            show Sayori alert_neutral at left, flip:
                xpos 0.1
            s "Time to go home..." with dissolve
            h "You alright, Sayori?"
            s "Not really."
            "It's been three months since that day."
            h uniform_headhold2 sad_side "Hey... don't take it bad, yeah? You did your best." with dissolve
            s alert_concerned uniform_folded "Did I? I was close to the end and it feels like I just... stopped trying." with dissolve
            h nervous_side "You said it yourself though, didn't you? You needed the downtime." with dissolve
            "Three months since Nozomi realized her love for me."
            s alert_annoyed "I didn't need THAT much downtime. Why did I quit cram school? I LOVED cram school." with dissolve
            s irritated "I learned so much more there than I ever did in this dump." with dissolve
            s uniform sleeptalk "No matter how I look at it, I just..." with dissolve
            s cry "I don't understand..." with dissolve
            h sleeptalk_concerned "Oh man, Sayori..." with dissolve


    # scene bg corridor eve with blink
    # "As I'm about to head out, I'm suddenly addressed from behind."
    # if pursued == "Sayori":
    #     h "Hey, Kyou?"
    #     show Hiroko smile at center
    #     "I wheel round to be confronted by a smiling Hiroko." with dissolve
    #     "She's... been a lot nicer to me than she used to, that's for sure."
    #     h "Hey buddy, did you ever think about what I said the other week?"
    #     "... Of course it's mostly because she wants something from me."
    #     k "I did, yeah."
    #     h annoyed blush "Well... do you wanna sometime?" with dissolve
    #     h annoyed_side "I tried watching those hypno vids Nozo told me about, but they got nothing on what you can do." with dissolve
    #     k "Look, can this wait? I have things to do tonight."
    #     h sleep "Oh... right, yeah, she told me you two were doing a thing." with dissolve
    #     h neutral noblush "You'll hit me up when you're free though, yeah?" with dissolve
    #     k "Yeah, sure. Anyway, I gotta head out."
    #     scene bg blackscreen with dissolve
    #     "It was cute for a while, but Hiroko's seriously getting annoying asking me to hypnotize her all the time."

    scene bg ext school eve
    stop music fadeout 15.0
    show Nozomi front shortwavy loving blush at center
    with blink
    "Nozomi greets me at the school gates with a tender smooch."
    n "I'll see you tonight, Kyou. I love you so much~ {font=DejaVuSans.ttf}♥{/font}"
    ks "Yeah. Love you too."
    hide Nozomi with dissolve
    "We arranged ourselves a little dinner date. She's gone off to freshen up and get changed for it."
    "Well, I mean I was the one who arranged it. I have to do everything involving her these days."
    scene bg street1 eve with dissolve
    "It's exhausting. It's like the longer we've been a couple, the more she leaves for me to decide."
    "What happened to the smart, funny, interesting and amazing girl I fell in love with?"
    scene bg shopping night
    show Nozomi front2 casual concerned
    with blink
    play music Sorrow
    n "Kyou, is everything alright?"
    ks casual angry "Stop asking me that!"
    n surprised "But Kyou, you barely said a word at dinner. If anything's bothering you, I'd like to know about it." with dissolve
    ks frown "It's nothing. Nothing you can help with, anyway."
    n frown "What? There must be something. Please just tell me what's on your mind; let me in." with dissolve
    n surprised "You know I'll support you any way I can. I'm your girlfriend!" with dissolve
    ks "Don't you wonder if that's all you are, Nozomi?"
    n concerned "Excuse me?" with dissolve
    ks confused "I mean, doesn't it bother you that you gave up on your college applications just so you could be with me?"
    "She blinks in surprise, as if I'd said something completely incomprehensible."
    n surprised "Why on earth would it, Kyou? I gladly set my own ambitions aside so I could be close to you. And I'd just as gladly do it again." with dissolve
    n loving blush "Because I love you with all my heart and soul, Kyou~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    "I sigh, pinching my fingers between my brow."
    ks irritated "See, this is exactly what I'm talking about, Nozo!"
    n shocked "Huh?" with dissolve
    ks frown "I mean, it's like every time I hypnotize you to bring out your true feelings, I just find you want to be more and more what I want you to be."
    n concerned noblush "And that's... a bad thing? Sorry, Kyou, I'm trying to understand but I'm not sure I do..." with dissolve
    ks annoyed "You never push back on a single thing; you just blithely accept anything I tell you."
    "Although when I put it like that..."
    n side sad "I... I know, Kyou. I just accept what you show me is right. If you tried to twist me into something I truly wasn't, I'd never allow it." with dissolve
    n smile blush "But I know you'd never hurt me, Kyou. Everything you say to me always feels so completely right, and natural." with dissolve
    n front2 laugh "You tell me something, and it's like it was staring me in the face my entire life and I was stupid for not realizing sooner." with dissolve
    "It's almost as if..."
    n loving "So Kyou, if there's anything I can do... Anything at all to put you at ease, please just tell me." with dissolve
    ks surprised "G-go away..."
    "After all this time..."
    n surprised "W-... what?" with dissolve
    ks "You heard me. I can't do this anymore. Just get away from me."
    n cry "Are you... breaking up with me?" with dissolve
    ks "I can't deal with this. I-I can't deal with you."
    "All I was really doing was..."
    n "P-please, Kyou don't... do this... no... no..."
    n "No..."
    n frightened "K-k-kyou, please I need you. Just... j-just tell me what to do to make this right." with dissolve
    n "I-I'll do anything, please Kyou. {w=0.5}{nw}"
    extend "PLEASE DON'T BREAK UP WITH ME!!!!" with shake
    ks cry "I'm sorry. Shit, I'm sorry!"
    "And with that, I turn and run into the night, past the assembled crowds of onlookers as my feet pound the pavement."
    scene cg delusion end 1 with dissolve
    n "KYOU!?"
    n "{size=30}KYOOOUUUUUU!!!{/size}" with shake
    $persistent.delusion_end_1_unlock = True
    scene bg blackscreen with longdissolve
    "I never went back to school after that."
    jump Credits

label Epilogue_Villain_Kyou:
    scene bg classroom eve with longdissolve
    "As another school day draws to a close, I gather my things and ponder."
    play music Memories
    play sound schoolbell
    if devoted>2:
        show Hiroko happy uniform_armup uniform_arm at center
        show Sayori happy at center, flip:
            xpos 0.25
        with dissolve
        h "FINALLY!" with vpunch
        s "How long have we waited for this moment, Hiroko?"
        "It's been nearly two weeks since I turned the minds of Nozomi and her friends."
        h angry_side "TOO DAMN LONG! I can't believe they wouldn't just give this to us." with vpunch
        s annoyed uniform_folded "That is school bureaucracy for you. At least we managed to persuade the right people without too much fuss, even if it took longer than we hoped." with dissolve
        "Since then, I've been busy effecting a few more changes around here. And today, one of them is coming to fruition."
        show Nozomi side smile_side at center:
            xpos 1.1
            linear 1.0 xpos 0.75
        n "Well, everyone else has left now. Except for Mr. Kobayashi, of course."
        show Nozomi smile:
            xpos 0.75
        show Hiroko smile_side no_arm at center, flip
        show Sayori smile
        h "Awesome~" with dissolve
        ks frown "*ahem* Club is now in session, Mr. Kobayashi."
        stop music fadeout 5.0
        "Our homeroom teacher looks up from his desk, then blinks slowly before returning to whatever it was he was doing."
        "Rest assured he'll be completely ignoring us for the duration of our stay."
        ks smile "Nozomi, if you'll do the honours."
        show Hiroko uniform
        show Nozomi laugh blush
        "Nozomi giggles happily before clearing her throat as she prepares to make an announcement." with dissolve
        play music Eons
        n "It is my great pleasure and privilege to declare the first official meeting of the Kyou Koyama Appreciation Society is now in session."
        s laugh blush "Ahh, this is so exciting~" with dissolve
        n "Our club's goal: To promote the excellence of this school's greatest ever student, Kyou Koyama, in his final months in this school and-"
        h uniform_armup cry_joy blush "AAAAA THIS IS HAPPENING!" with vpunch
        n "Ehehe~ And to ensure his legacy is upheld for future generations of students."
        n front laugh "So let's work hard to make sure Kyou is loved by one and all, as his greatness deserves~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        show Hiroko laugh uniform_arm
        show Nozomi front2 happy uniform_folded
        show Sayori giggle
        "The three of them break into rapturous applause and excited laughing." with dissolve
        "It's been a couple of weeks now, but their enthusiasm for pleasing me hasn't dimmed in the slightest."
        "The fact that none of them have been able to shake their hypnotic conditioning really makes me think I can pull off what I'm about to do..."
        n smile "I will now hand off to our club president... {w=0.5}K-{w=0.2}{nw}" with dissolve
        extend laugh "KYOU KOYAMA!" with vpunch
        ks "Heh, thanks, Nozomi. That was adequate, I suppose."
        n "Ahaha, thank you so much~ {font=DejaVuSans.ttf}♥{/font}"
        ks "Now to business. First on our agenda of course is to recruit new members."
        show Hiroko uniform smile
        show Sayori smile_right
        show Nozomi smile
        ks neutral "Forming the club this late in our school lives was a good achievement, but we'll need to bring a lot more members in if we want to meet our goals." with dissolve
        "The three of them nod in unison as they listen intently."
        ks smirk "Also fooling around with just the three of you is getting tiresome. I need some variety around here."
        n uniform loving "We completely understand, president. We only hope we can continue to bring you pleasure in your life as you do ours~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        ks smile "I knew you'd get where I'm coming from. So, I want to hear some suggestions from all of you for candidates."
        s "Before we suggest anyone, Kyou, am I correct in surmising your preference is for female candidates?"
        menu:
            "Yeah, girls only":
                $hypno11 = "girls"
                ks "That's right, Sayori."
            "CUTE girls only":
                $hypno11 = "cute"
                ks smirk "Not just that, but I want you to consider their attractiveness before putting their names forward. I only want the best for my club."
            "All are welcome in the Kyou Appreciation Society":
                $hypno11 = "all"
                ks "Actually, Sayori, I'm not so picky as that. Name anyone you think would be good for us."
        s laugh_right "Understood!" with dissolve
        ks smile "So who are we thinking of?"
        if hypno11 == "all":
            h "What about Ryoma? Ryoma Ichizen?"
            ks "Who's that?"
            h happy "He's captain of the Boy's Tennis Club. I always thought he was cool~" with dissolve
            h affectionate "I kinda had a crush on him before you happened, ehehe." with dissolve
        elif hypno11 == "girls":
            h "Maybe Risa? We used to be playing buddies when I was in tennis club."
        elif hypno11 == "cute":
            h happy "Chiyo! She was in tennis club with me, she's so pretty~" with dissolve
        if hypno11 != "all":
            s smile "Talking of former clubmates, there is Kimiko from my study club." with dissolve
            s "The club is dissolving soon as my leaving has left too few regularly-attending members, so she will be free to join us immediately."
            if hypno11 == "cute":
                ks frown "Is she attractive, though?"
                s rolleyes "Her assets are more considerable than mine, so I believe so." with dissolve
        else:
            s smile "I recommend Kimiko, from my former study club." with dissolve
            s "The club is dissolving soon as my leaving has left too few regularly-attending members, so she will be free to join us immediately."
        show Sayori smile_right
        ks neutral "Great. Nozomi, what have you got for me?" with dissolve
        if hypno11 == "all":
            n surprised "What about Daisuke? I don't really get the appeal of him, but he's something of an idol around these parts." with dissolve
            n pout_left "Nothing compared to you, of course, but he'd definitely bring a lot more people with him. He'd be a good catch for us." with dissolve
        elif hypno11 == "girls":
            n smile "Rie from our class would be lovely, don't you think?" with dissolve
        elif hypno11 == "cute":
            n pout_left uniform_folded "Hmm, someone attractive... Maybe Sachiko from the literature club? She has a bit of a sexy librarian vibe about her." with dissolve
        show Hiroko smile
        show Sayori uniform smile_right
        show Nozomi smile
        ks frown "Okay, good. Now you're going to lay out everything you know about these people and more importantly, how we can isolate them, and..." with dissolve
        show penlight at right with moveinright:
            ypos 0.346
        "I lay my penlight down on the desk in front of us for emphasis."
        ks "... Recruit them. Understand, girls?"
        multi "Yes, president!"
        hide penlight with moveoutright
        ks smirk "Perfect. As your president, I expect you to dedicate your every waking moment to realizing my club's goals, and this is just the first step."
        ks "If you three really want to make me happy, you'll do this without question."
        ks "I'm not being unreasonable. Am I, girls?"
        scene cg devotion end 1 with blink
        "The three of them squeal their mindless affirmations as they crowd around my desk feverishly."
        s "Ahaha, of course not! W-We would be fools to do anything else!"
        n "Oh my gosh, your happiness is ALL I care about! I want to do this for you!"
        h "KYAHAHAHAHA! I FUCKING LOVE THIS CLUB!" with shake
        $persistent.devotion_end_1_unlock = True
        scene bg blackscreen with fade
        stop music fadeout 5.0
        nvl_narrator "Time passed as we got to work on expanding the club."
        nvl_narrator "My influence on the school became immense, as the Kyou Koyama Appreciation Society swiftly gained pace."
        if hypno11 == "all":
            nvl_narrator "Within a few months, it had expanded to become the most attended club in the school."
        elif hypno11 == "girls":
            nvl_narrator "Within a few months, it had expanded to become the most attended club in the school for girls."
        elif hypno11 == "cute":
            nvl_narrator "Within a few months, almost all of the most popular girls in school had switched memberships to join the club."
        scene bg blackscreen with fade
        play music Sorrow
        nvl clear
        nvl_narrator "Unfortunately, as my popularity soared, so did my problems."
        nvl_narrator "Rumours quickly began to spread about me and my club members, and about the activities we allegedly performed."
        nvl_narrator "It was said that what we were doing behind closed doors was immoral and indecent."
        scene bg blackscreen with fade
        nvl clear
        nvl_narrator "While me and my members did their best to... address the rumours, they persisted."
        nvl_narrator "One day, an independent inspection surprised us at a club meeting."
        nvl_narrator "I had long managed to convince the faculty to look the other way regarding us, but these were not from the school."
        scene bg blackscreen with fade
        nvl clear
        nvl_narrator "Long story short, I was arrested on suspicion of starting a cult."
        nvl_narrator "My penlight is stashed in an evidence vault somewhere. If they suspected it had much to do with the incident, though, it was quickly written off."
        nvl_narrator "Still, it's safe to say I'm never getting it back."
        scene bg blackscreen with fade
        nvl clear
        nvl_narrator "I may get out of here eventually, when they run out of reasons to keep me imprisoned."
        nvl_narrator "But having had time to think about these past few months... It gets to me."
        nvl_narrator "I forced others to worship me, to love me unconditionally. It was a high, and one I kept chasing as I endlessly sought out new people to love me how I wanted."
        scene bg blackscreen with fade
        nvl clear
        nvl_narrator "But still, even when I was surrounded by awestruck fans I never managed to forget what I did to win their adoration."
        nvl_narrator "All I ever must have earned was their hatred and contempt, lurking just behind their smiles and giddy enthusiasm, ready to strike me if they ever broke free of me."
        nvl_narrator "Looking back, I think I stopped being happy a while ago."
        scene bg blackscreen with fade
        nvl clear
        nvl_narrator "Many members of the society, including the three founding girls, were institutionalized after they found it impossible to continue their lives in my absence."
        nvl_narrator "I can't say I considered what would happen if I wasn't around for them to worship..."
        nvl_narrator "It was in the news for weeks: The young man who seduced an entire community into insanity."
        scene bg blackscreen with fade
        nvl clear
        nvl_narrator "Even if I'm released, this town will tear me apart. My life is over."
        nvl_narrator "The only small comfort I can take is that no one is going to forget my legacy in a hurry."

        nvl_narrator "So I guess in that respect, the Kyou Koyama Appreciation Society was a success."
        jump Credits
    elif robot == 2:
        show Hiroko uniform_armup happy uniform_arm at center
        show Sayori happy at center, flip:
            xpos 0.25
        with dissolve
        h "Hometiiime~ {font=DejaVuSans.ttf}♫{/font}" with dissolve
        "It's been a couple months since that day."
        s smile "Do you have any plans this weekend, Hiroko?" with dissolve
        h no_arm smile_side "I dunno. If my shoulder's feeling okay I'm gonna hit the court again~" with dissolve
        "A couple months since I had these two think they're secretly [hypno6]s and brought them under my control."
        show Nozomi side neutral_side at center:
            xpos 1.3
            linear 1.0 xpos 0.75
        show Sayori uniform smile
        n "I'll see you all later, then. Have a good weekend, you two." with dissolve
        "And a couple months since Nozomi and I started dating, of course."
        show Hiroko uniform smile_side at center, flip
        show Nozomi:
            xpos 0.75
        h "Yeah same to you, buddy. Seeya~" with dissolve
        stop music fadeout 5.0
        scene bg street1 eve with blink
        "We've enjoyed our time together since then, hanging out together and spending the odd nights at my place."
        "She told her mom about us like she promised, and even my dad seemed to take a liking to her when they finally met."
        play music Downtown
        "And as for those other girls, me and Nozomi have been keeping them on a tight leash, making sure they perform their public duties while ultimately obeying our every command."
        "Staying on top of their programming has been a little stressful; there's always something we didn't account for, but still..."
        "My life is... sort of okay right now."
        show Nozomi front2 neutral_left at center
        "... And yet my girlfriend seems a little out of sorts these past few days." with dissolve
        ks smile "Hey, are you alright there?"
        n surprised "{cps=20}H-huh? Oh, I... {/cps}{w=1.0}{nw}" with dissolve
        $ renpy.transition(dissolve, layer="master")
        extend concerned "well..."
        "Yeah, something's obviously wrong. It's not like her to make such a face when she's around me."
        "So I take her by the shoulders and ask her earnestly."
        ks neutral "Hey, you can tell me anything. You know that, right?"
        show Nozomi sleeptalk_concerned
        "Nozomi nods her head quietly." with dissolve
        n "Y-yeah... I know."
        ks "So what is it?"
        n neutral_left blush "It's... w-well, it's not you, just to be clear." with dissolve
        n surprised "Being with you is wonderful, and I'm so glad we're together!" with dissolve
        ks confused "But?"
        n sleeptalk "I-It's just..." with dissolve
        "Her shoulders feel so tense. Whatever's eating her has got to be pretty severe, especially if she's so cagey about telling me."
        "Maybe if I tried to cheer her up..."
        ks smile "You know, I've been thinking about what we should do tonight, and you know what I think?"
        n surprised "U-uh... what's that?" with dissolve
        "I don't really want to do this. Nozomi's asked me a bunch of times before and I always turned her down."
        ks "Let's go to that karaoke place you like. Bang out a few tunes."
        n shocked "I... r-really?!" with dissolve
        "But desperate times, desperate measures, I guess."
        ks "Really. What do you say to that?"
        n side smile "Gosh, Kyou. I... really appreciate that." with dissolve
        "It seems to cheer her up a little at least."
        ks "Alright. Well no time like the present, then. Come on!"
        scene bg shopping eve with blink
        "So I take her by the hand and lead her into town, before I lose my nerve."
        "Although Nozomi perked up at my invitation, it doesn't seem to make her any more forthcoming about her problems."
        scene bg karaoke with blink
        "But maybe she'll loosen up once we get a few tunes in her..."
        show Nozomi front2 neutral at center
        ks smile "Okay, we've got this room for an hour. But we can spend all night in here if you want to, Nozomi." with dissolve
        n side smile_side "That's... great, yeah." with dissolve
        ks "Is there anything you want to start with?"
        show Nozomi neutral
        "I say, as I pick up the controller from the table and start to browse the menu of songs..." with dissolve
        ks confused "Hmm... I barely know any of these."
        n sad "Gosh, have you seriously never done karaoke before?" with dissolve
        "... Yeah. I know it's a common activity around here, but I always ducked out of doing this stuff before when I had the chance."
        ks "Uh... w-well..."
        "I don't even *listen* to that much music, if I'm being honest."
        show Nozomi smile
        "And as I continue to waver, Nozomi just smiles and shakes her head at me." with dissolve
        n "It's alright. We don't have to sing if you don't want to."
        "She can see I'm obviously struggling with this, even though it was my idea to come here."
        "But wait, is she telling me she doesn't want to sing either? After all those times she tried to get me in here?"
        ks sigh "Okay seriously, Nozomi. What's gotten into you?"
        stop music fadeout 5.0
        n front2 sleeptalk_concerned "..." with dissolve
        ks frown "Come on, spit it out. I'm trying to help you here and you're not giving me anything!"
        "I'm not even trying to hide my frustration now, and Nozomi reacts with an anxious-sounding sigh."
        queue music Eons
        n neutral_right "I know. I'm sorry, this is really silly but I... w-well..." with dissolve
        "Just as it seems she's finally ready to explain herself, I notice her reach into her pocket and pull out her phone while she looks at me pensively."
        n concerned "... Do you mind if I have the others join us?" with dissolve
        "I give her a look as she starts to place a call before I can even answer her."
        ks confused "The others? Are you talking about those girls from the literature club?"
        n sleeptalk_concerned "No. Not... them, I mean..." with dissolve
        n side sad_closed "S-sorry, Kyou. I really need this, okay?" with dissolve
        show Nozomi neutral_side
        "I'm feeling more confused by the second as she puts the phone to her ear and the person on the other end picks up almost immediately." with dissolve
        n "... Hiroko, stop what you're doing and head to our usual karaoke club. Give the attendant your name and head up to the room they give you. [hypno3]."
        "I don't believe it."
        ks frown "Really, Nozo? You want those goddamn [hypno6]s here for our night out?"
        show Nozomi sad
        "Nozomi sighs and nods as she hangs up the phone and starts thumbing the screen to place another call." with dissolve
        n "I'm sorry, but yes I do."
        n neutral "You'll do this for me, right?" with dissolve
        "I let out a resigned sigh and nod my head."
        ks sigh "Ugh, fine. If this is what you really want."
        n neutral_side "Sayori, cancel your current plans and head to Charming Cat Karaoke, near the mall..." with dissolve
        show Nozomi front2 neutral
        with blink
        "A few minutes pass as I finish booking those two for the room at my expense."
        "I really think I'm owed an explanation now as I look to Nozomi, who sits tensely on the couch opposite me."
        n concerned "... I don't have anyone else to do this stuff with any more." with dissolve
        ks confused "Huh? What are you talking about?"
        n neutral_left "Those people you mentioned from the literature club? I can't associate with them outside of school ever again." with dissolve
        "I may have wanted her to open up to me, but I can only shake my head at what I'm hearing."
        n surprised "No, seriously, I can't trust them, okay? I can't trust any of them!" with dissolve
        "Really should've guessed this was what was eating her."
        ks sigh "Jesus, Nozomi. You can't bitch and moan about how lonely you are when you won't even talk to anybody else."
        n concerned "I-I know I sound silly, but it's the truth. I can't ever feel comfortable around those girls again. You understand, right?" with dissolve
        "I don't, really. I've always been alone and I've always had to suck it up."
        "But now we have each other and that's enough. She has to realize that someday."
        ks confused "Well, it's too bad you feel that way. Maybe you just need a change of scenery. We aren't going to be at that school much longer anyhow."
        "She'll get used to it. Just like I did."
        n surprised "It won't get any easier, Kyou! Do you really not get it?" with dissolve
        n sleeptalk_concerned "Out of everyone in the world, I thought you'd understand the most." with dissolve
        ks frown "No, I don't get you at all! Why's this so difficult for you, Nozomi?"
        stop music fadeout 5.0
        n pain "Because anyone I meet might be a [hypno6], that's why!" with dissolve
        ks frown "Oh for the love of..."
        "Okay, so maybe I went a little overboard in convincing her that [hypno6]s are dangerous."
        queue music Diary
        n side sad "No, don't tell me it's ridiculous. How long did it take you to figure out the truth about my friends?" with dissolve
        "Even so, she's supposed to believe that the only [hypno6]s around are the people I tell her are [hypno6]s."
        ks sigh "For fuck's sake, no one else we know is one of them. You have my word on that so stop freaking out."
        "I've told her before, so why's she still so afraid?"
        n sad_side "That might be true now, but who's to say someone else won't be snatched away and replaced by whoever's making these things?" with dissolve
        ks confused "You... what?"
        n surprised "We don't even know who's building them! We have no idea where they're coming from!" with dissolve
        ks sigh "Ugh, just don't worry about it. Seriously." with dissolve
        n sad_closed "... Kyou, I've been thinking about this a lot, as you've probably guessed." with dissolve
        n sad "And what I keep coming back to is... well, [hypno6]s can't grow, can they? They're machines, not organic beings." with dissolve
        n front2 surprised "So Hiroko and Sayori can't have always been [hypno6]s, can they?" with dissolve
        ks confused "Er, w-well... th-that is..."
        "I probably should've realized Nozomi would consider the concept of [hypno6]s beyond just her friends when I put the idea in her head..."
        n concerned "I knew it. So if these shadowy organisations can replace them just like that? Then they can replace any one of us." with dissolve
        "But I never would've imagined her to take that idea and run a hundred goddamned miles with it."
        n side sad "If it happens again, if someone else is replaced by one of these [hypno6]s, are either of us going to notice before they do something terrible to us or our families?" with dissolve
        "I left far too much to her imagination."
        ks sad "Nozomi..."
        "... So what if I hypnotized her again?"
        n sad_closed "I have to stay vigiliant for the rest of my life. After all, you can't always be around to protect me." with dissolve
        "I could alter her thoughts, dial back the whole \"scared of [hypno6]s\" thing. Maybe convince her Sayori and Hiroko are the only [hypno6]s that exist..."
        stop music
        play sound telephone loop
        n surprised "Ah!" with vpunch
        "But just then a ringing telephone rudely interrupts my thoughts."
        n front2 surprised "The staff are calling us from downstairs. One of the [hypno6]s must have arrived." with dissolve
        stop sound
        n concerned "Let's bring them up here, then..." with dissolve
        show Nozomi front2 neutral_right
        show Hiroko neutral_side at center:
            xpos 0.75
        show Sayori neutral at center, flip:
            xpos 0.25
        with blink
        "Turns out the pair of them arrived almost together, so we bring them both inside to the privacy of our room for tonight."
        "And as the door closes behind them, the two now stand blankly to attention, awaiting our instructions."
        queue music Night_Road
        n neutral_left "So..." with dissolve
        "After all, now that they're out of the public eye, the [hypno6]s have no compulsion to maintain the pretense that they're in any way human beings."
        n side frown_side "[hypno6!c] Sayori, tell me of any issues that will arise by my keeping you here this evening. [hypno3]." with dissolve
        "Which of course means neither of us need to treat them as human either."
        s "[hypno2]. One issue detected: Sayori Watanabe's parents are scheduled to return home at approximately 9pm, necessitating her presence at home by that time."
        n irritated "Great. Set an alert for eight-twenty and inform me when it happens. [hypno3]." with dissolve
        s sleeptalk "[hypno2]." with dissolve
        show Nozomi frown_side at center, flip
        show Sayori neutral
        n "And [hypno6] Hiroko, am I right in assuming no one will miss you before nine as well?" with dissolve
        h "Yes, administrator Akemi. Hiroko Homura will not be missed before nine o'clock."
        hide Nozomi
        show Nozomi front sleep
        n "Good. That's what I thought..." with dissolve
        n neutral "... Why do I want these \"goddamn [hypno6]s\", as you put it?" with dissolve
        "I had simply stood to watch as Nozomi bossed the bots around, so her suddenly addressing me catches me off guard."
        n sleeptalk "I know they're not my friends. And maybe they never were." with dissolve
        n side neutral_side "But even so, they're the only other... \"people\" I can feel safe around now." with dissolve
        n sad_closed "At least now that you reprogrammed these things they can't hurt me any longer." with dissolve
        n sad "They can never betray me... right?" with dissolve
        n neutral_side "You'll remain our loyal companions, dedicated to our comfort and happiness. Won't you, [hypno6]s?" with dissolve
        $multi = "{color=FF89AB}Hiroko{/color}{color=#FFFFFF} {color=#FFFFFF}&{/color} {color=385599}Sayori{/color}"
        multi "Yes, administrator."
        show Nozomi frown_side
        "Nozomi regards the pair of them cooly for a moment before she nods her head firmly, as if she's just come to a decision." with dissolve
        show Nozomi at flip
        "She then scoops up the microphones from the table and points one towards the emotionless pink-haired [hypno6] as she speaks to [p_them] calmly." with dissolve
        n "So you dip into those memory banks of yours, Hiroko. Recall how you used to be when we sang together in this very place, back when I thought we were friends."
        n neutral_side "And now when you take this mic, I want you to be that person again." with dissolve
        n sad_side "I want you act as if the real Hiroko were standing here right now, ready to sing with her dearest friend... [hypno3]." with dissolve
        h "[hypno2]."
        "The [hypno6]'s reply is as nonchalant and monotone as ever, but the moment Nozomi places the microphone onto the palm of [p_their] hand..."
        h uniform_armup happy"Fuck yeah, let's do this, bestie! {font=DejaVuSans.ttf}♥{/font}" with dissolve
        "That obnoxious, overly bubbly personality that [p_they] possessed before returns in an instant."
        n happy "Ehehehe... y-yeah." with dissolve
        show Nozomi smile
        h angry "Dude, come on! If you're gonna stand there hogging the remote you better pick a good song for us right the fuck now!" with dissolve
        "Even while Hiroko's in public [p_they]'s never been this... boisterous since I reprogrammed her."
        show Hiroko annoyed
        "But if this is what my girlfriend wants I'll suck it up for now." with dissolve
        ks sigh "Uh-huh. I'm just gonna hit the randomizer and you two can have at it."
        stop music fadeout 5.0
        "Yeah, I'll just hit the button on the controller here and get out of their way for now."
        show Hiroko neutral_side
        n surprised_side "I don't think I know this one... some electropop song from 2010?" with dissolve
        h rolleyes "H'yeah, who the fuck is that? Great going, dude..." with dissolve
        h happy "... Let's do it, Nozo!" with dissolve
        play music Sorrow2
        scene RobotKaraoke nozomi1 n_happy h_happy with blink
        "So the lights in the room dim as the song begins to start, while I take a seat to watch this disaster unfold."
        "I spare a glance at the [hypno6] sitting beside me, completely unmoving at the sight before us."
        #CG would come in here or the previous line
        show RobotKaraoke n_smile lyric1
        "Even as Nozomi starts to sing the first lyrics and..." with dissolve
        n "{size=28}Our love's memories, as they sway, disappear~ {font=DejaVuSans.ttf}♫{/font}{/size}"
        "... Damn, is it just me or does her singing sound off-key?"
        show RobotKaraoke n_neutral lyric2
        n neutral_side "{size=16}Oh, this sounds like a sad one.{/size}" with dissolve
        "I always thought she'd have the singing voice of an angel, especially as she does this kinda stuff all the time."
        show RobotKaraoke h_sing
        h happy_closed "{size=28}You and I, from above, swirling down, singing love~ {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
        "Meanwhile Hiroko seems to pick up the melody a lot quicker despite this apparantly being a song neither of them have ever heard before."
        show RobotKaraoke n_unsure
        n sad_side "{size=28}Do you love me even now, and if so, for how long...{/size}" with dissolve
        show RobotKaraoke h_sing_n lyric1
        h laugh_side "{size=28}You and I, from above... lalala~ {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
        "It helps me pick up on the lyrics and they... wow yeah, this melody coming out sounds downright bleak."
        show RobotKaraoke -lyric1
        "The more I listen, the more this song sounds like it's about a person lamenting the loss of their love, likening it to a firework burning out." with dissolve
        "And a firework burned out, as Nozomi declares with a wavering voice into the mic, can never be relit."
        show RobotKaraoke n_unsure_closed h_sing lyric1
        "She'll never find happiness in friendship again. And I'm gonna have to move heaven and earth to even maintain the lie of our relationship, and these [hypno6]s." with dissolve
        $multi = "{color=93624B}Nozomi{/color}{color=#FFFFFF} & {/color}{color=FF89AB}Hiroko{/color}"
        show RobotKaraoke h_happy lyric2
        multi "{size=28}And these night melodies that once offered me peace.{/size}" with dissolve
        "\"What if I hypnotized her again?\" What a joke that is."
        show RobotKaraoke n_tearful h_sing
        n front2 pain "{size=28}Will remind me from now that it was all a l-lie...{/size}" with dissolve
        "If I hypnotize her again, alter her as I please, reprogram her... how would it make her any different to the \"[hypno6]s\" beside her?"
        show RobotKaraoke n_cry lyric1
        n cry "{size=28}I am throwing the key, kissing summer goodbye...{/size}" with dissolve
        "So what's the point anymore? Even if I hypnotize her, I'll know how she really feels."
        show RobotKaraoke h_peaceful
        h sleeptalk "{size=28}You and I from above... lalala~ ♪{/size}" with dissolve
        "I know I've reduced her to... to this."
        show RobotKaraoke nozomi2 -lyric1
        n frightened "O-oh God, Hiroko... nnnrrrg..." with dissolve
        show RobotKaraoke h_smile
        h happy_closed "Hey, c'mon sis you weren't THAT bad!" with dissolve
        "This is my life now. Mine and Nozomi's."
        n "I-I was... I am..."
        "And there's no going back..."
        $persistent.robot_karaoke_end_unlock = True
        jump Credits
    elif robot > 2:
            show Hiroko uniform_armup happy uniform_arm at center
            show Sayori happy at center, flip:
                xpos 0.25
            with dissolve
            h "Hometiiime~ {font=DejaVuSans.ttf}♫{/font}" with dissolve
            s smile "Do you have any plans this weekend, Hiroko?" with dissolve
            h no_arm smile_side "I dunno. If my shoulder's feeling okay I'm gonna hit the court again~" with dissolve
            "It's been a couple months since that day."
            s smirk "I know better than to think I can talk you out of it, but please don't overwork yourself." with dissolve
            h laugh_side "Hehe, same to you, buddy~" with dissolve
            "A couple months since I reprogrammed some [hypno6]s I discovered masquerading as high-school girls."
            show Nozomi side smile_side at center:
                xpos 1.3
                linear 1.0 xpos 0.75
            show Sayori uniform smile
            n "Are we all set?" with dissolve
            show Hiroko uniform smile_side at center, flip
            show Nozomi:
                xpos 0.75
            s "We're ready. Let's go." with dissolve
            stop music fadeout 5.0
            scene bg street1 eve with blink
            "I take my time heading home. There's no rush today, after all."
            show phone at right with moveinright:
                ypos 0.346
            "As I walk, I pull out my phone and run an app I wrote myself called \"[hypno6].apk\"."
            if robot == 2:
                "After a few moments, the simple app boots up and displays two icons on the screen."
            elif robot == 3:
                "After a few moments, the simple app boots up and displays three icons on the screen."
            "I don't really need them for anything, but I consider it important to bring one in for a routine check-up each day."
            "And I know none of them have any pressing human impersonation duties to attend to this evening."
            "I don't care which; I'll just pick one at random."
            $hypno6 = hypno6.capitalize()
            $robolist = ['nozomi','hiroko','sayori']
            if hypno1 != "robot hiroko":
                $list.remove('hiroko')
            if hypno5 != "robot sayori":
                $list.remove('sayori')
            if hypno10 != "robot nozomi":
                $list.remove('nozomi')
            $random.shuffle(robolist)
            menu:
                "[hypno6!t]#001":
                    $hypno11 = robolist[0]
                    $hypno11 = hypno11.capitalize()
                    $hypno12 = 1
                    $bot_name = "%s#001" %hypno6; bot_image = hypno11
                "[hypno6!t]#002":
                    $hypno11 = robolist[1]
                    $hypno11 = hypno11.capitalize()
                    $hypno12 = 2
                    $bot_name = "%s#002" %hypno6; bot_image = hypno11
                "[hypno6!t]#003" if len(robolist) == 3:
                    $hypno11 = robolist[2]
                    $hypno11 = hypno11.capitalize()
                    $hypno12 = 3
                    $bot_name = "%s#003" %hypno6; bot_image = hypno11
            play sound appbutton
            "With a shrug, I press my thumb on the icon, which opens a menu. I thumb over the \"Home\" option and wait for a response."
            play sound cellvibrate
            "It doesn't take long before my phone vibrates from a received text." with vpunch
            "\"[hypno2].\""
            hide phone with moveoutright
            scene bg shopping2 eve with blink
            $hypno6 = hypno6.lower()
            "Putting my phone away, I continue the rest of the journey home, stopping off at the convenience store first."
            "There's no rush, after all. The [hypno6] will be waiting for me when I arrive, for as long as [p_they] needs to."
            $hiroko_name = "[hypno6!c!t]#00[hypno12]"; nozomi_name = "[hypno6!c!t]#00[hypno12]"; sayori_name = "[hypno6!c!t]#00[hypno12]"
            scene bg k house eve
            if hypno11 == "Hiroko":
                show Hiroko frown at center
                with blink
                "Sure enough, [p_they]'s standing outside my door when I get there."
                h uniform_armup angry "Dude! I've been waiting here for ages. How come I got here before you, huh?" with dissolve
                ks frown "I was getting some things, that okay with you?"
                h annoyed "Ugh. I dunno why I wasted my time coming here; I could've been on court by now." with dissolve
            elif hypno11 == "Nozomi":
                show Nozomi front neutral at center
                with blink
                "Sure enough, [p_they]'s standing outside my door when I get there."
                n surprised "Kyou, hi! I thought you'd already be home." with dissolve
                ks smile "Just wanted to get a few things first. Anyway..."
            elif hypno11 == "Sayori":
                show Sayori neutral_right at center
                with blink
                "Sure enough, [p_they]'s standing outside my door when I get there."
                s frown_right "Did you get lost on the way home, Kyou?" with dissolve
                ks smirk "Very funny. I was just getting a few things."
            scene bg k room eve
            with blink
            play sound dooropen
            "My door swings open as I let myself inside, knowing my [hypno6] will follow behind me."
            if hypno11 == "Hiroko":
                show Hiroko uniform_armup angry at center
                play sound doorclose
                h "I mean, {nw}" with dissolve
                extend "SOME of us have shit to do, you know?" with vpunch
                show phone at right with moveinright:
                    ypos 0.346
                "Ignoring [p_them] as [p_they] pulls the door closed, I take out my phone again with the [hypno6].apk app still running."
                h annoyed "You even listening to me?" with dissolve
                "With the app still on [hypno6!c]#00[hypno12]'s service menu, my thumb presses down on a button option marked \"Maintenance Mode\"."
                h furious "I mean, you fuckin' call me here, and you-{w=0.2}{nw}" with dissolve
                play sound appbutton
                $ renpy.transition(longdissolve, layer="master")
                extend entranced_neutral ""
                hide phone with moveoutright
                show Hiroko uniform
                "[p_their!c] human mode prattling ceases as [p_they] almost instantaneously processes the transmitted instruction and shuts off the entirety of [p_their] human personality core." with dissolve
                ks "00[hypno12], remove all clothing and submit for inspection. [hypno3]."
                play sound clothes
                "As [p_they] wordlessly begins to pull off the blazer [p_they]'s wearing, I shake my head. To think I was fooled by this automation for so long."
                show Hiroko underwear
                "Honestly, it didn't take me long to see through [p_their] charade once I seriously considered the possibility [p_they] was a [hypno6]." with dissolve
                "But I can see how [p_they] and the other [hypno6]s managed to stay undetected for so long. It's not exactly a common thing people think about."
                show Hiroko nude
                "Yet now, as I watch this one shed the last of [p_their] clothing and stand stiffly to attention in front of me, I can't imagine how [p_they] could be anything else." with dissolve
            elif hypno11 == "Nozomi":
                show Nozomi side smile at center
                play sound doorclose
                n "So how was your day, Kyou?" with dissolve
                show phone at right with moveinright:
                    ypos 0.346
                "Ignoring [p_them] as [p_they] pulls the door closed, I take out my phone again with the [hypno6].apk app still running."
                n laugh "Mine kinda dragged on; it's been one of those weeks." with dissolve
                "With the app still on [hypno6!c]#00[hypno12]'s service menu, my thumb presses down on a button option marked \"Maintenance Mode\"."
                show Nozomi front happy with dissolve
                n "Once I get home I think I'll-{w=0.2}{nw}"
                play sound appbutton
                $ renpy.transition(longdissolve, layer="master")
                extend entranced_neutral ""
                hide phone with moveoutright
                "[p_their!c] human mode prattling ceases as [p_they] almost instantaneously processes the transmitted instruction and shuts off the entirety of [p_their] human personality core."
                ks "00[hypno12], remove all clothing and submit for inspection. [hypno3]."
                play sound clothes
                "As [p_they] wordlessly begins to pull off the blazer [p_they]'s wearing, I shake my head. To think I was fooled by this automation for so long."
                "I was actually pining over this girl for the longest time, only to realize she wasn't really a girl at all..."
                show Nozomi underwear
                "Honestly, it didn't take me long to see through [p_their] charade once I seriously considered the possibility [p_they] was a [hypno6]." with dissolve
                "But I can see how [p_they] and the other [hypno6]s managed to stay undetected for so long. It's not exactly a common thing people think about."
                show Nozomi nude
                "Yet now, as I watch this one shed the last of [p_their] clothing and stand stiffly to attention in front of me, I can't imagine how [p_they] could be anything else." with dissolve
            elif hypno11 == "Sayori":
                show Sayori frown_right at center
                play sound doorclose
                s "So what did you want to talk to me about, Kyou?" with dissolve
                show phone at right with moveinright:
                    ypos 0.346
                "Ignoring [p_them] as [p_they] pulls the door closed, I take out my phone again with the [hypno6].apk app still running."
                s uniform_folded "Kyou? Will you look at me while I am talking to you? I do not appreciate being ignored." with dissolve
                s "You can play with your phone later."
                "With the app still on [hypno6!c]#00[hypno12]'s service menu, my thumb presses down on a button option marked \"Maintenance Mode\"."
                s scowl "Kyou, I am, as ever, extremely bu-{w=0.2}{nw}" with dissolve
                play sound appbutton
                $ renpy.transition(longdissolve, layer="master")
                extend uniform entranced_right ""
                hide phone with moveoutright
                "[p_their!c] human mode prattling ceases as [p_they] almost instantaneously processes the transmitted instruction and shuts off the entirety of [p_their] human personality core."
                ks "00[hypno12], remove all clothing and submit for inspection. [hypno3]."
                play sound clothes
                "As [p_they] wordlessly begins to pull off the blazer [p_they]'s wearing, I shake my head. To think I was fooled by this automation for so long."
                show Sayori underwear
                "Honestly, it didn't take me long to see through [p_their] charade once I seriously considered the possibility [p_they] was a [hypno6]." with dissolve
                "But I can see how [p_they] and the other [hypno6]s managed to stay undetected for so long. It's not exactly a common thing people think about."
                show Sayori nude normal_attention
                "Yet now, as I watch this one shed the last of [p_their] clothing and stand stiffly to attention in front of me, I can't imagine how [p_they] could be anything else." with dissolve
            if hypno11 == "Hiroko":
                h entranced_talk "[hypno2]. [hypno6!c]#00[hypno12] is ready for inspection." with dissolve
                show Hiroko entranced_neutral
            elif hypno11 == "Nozomi":
                n entranced_talk "[hypno2]. [hypno6!c]#00[hypno12] is ready for inspection." with dissolve
                show Nozomi entranced_neutral
            elif hypno11 == "Sayori":
                s entranced_talk_right "[hypno2]. [hypno6!c]#00[hypno12] is ready for inspection." with dissolve
                show Sayori entranced_right
            play music Machine
            "In any case, I brought [p_them] here for maintenance so let's get to it." with dissolve
            "First I look over [p_their] frame, inspecting it for damage."
            if hypno11 == "Hiroko":
                "[p_their!c] left shoulder looks a little sore. I'll have to remember to make [p_them] ease up on the tennis player impersonation until it repairs itself."
            elif hypno11 == "Sayori":
                "There doesn't seem to be any imperfections as I take in [p_their] every detail from head to foot. Other than the cosmetic damage around [p_their] eyes, of course."
                "I suspect it's down to [p_them] constantly running down [p_their] battery to nothing before recharging, a defect [p_they]'s had long before I got a hold of [p_them]."
                "Well, I'll get around to fixing it after I graduate."

            elif hypno11 == "Nozomi":
                "There doesn't seem to be any imperfections as I take in [p_their] every detail from head to foot."
                "Just that minor issue with [p_their] optics that requires [p_them] to use external corrective lenses to maintain full functionality."
                menu:
                    "Take the lenses off":
                        "It's not aesthetically pleasing to me, especially as the other [hypno6!l]s don't need them."
                        $glassesoff = True
                        show Nozomi noglasses
                        "Reaching up, I pull the lenses from [p_their] lifeless face and drop them on top of [p_their] pile of discarded clothing." with dissolve
                        "I'm going to test how [p_they] performs like this today."
                    "Leave them on":
                        $glassesoff = False
                        "That won't be easy to fix, but it's only a minor issue. I guess I can live with it."
            "Next, I pick up [p_their] left wrist in my hand and take [p_their] \"pulse\"."
            "[p_they!c] seems to be replicating a healthy, resting heart rate. So far so good."
            "Now to check for evidence of human mode response."
            show penlight at right with moveinright:
                ypos 0.346
            if hypno11 == "Hiroko":
                if persistent.NewSprite == " New":
                    $light_x = 0.46; light_y = 0.3; slight_x = 0.5; slight_y = 0.29
                else:
                    $light_x = 0.44; light_y = 0.31; slight_x = 0.48; slight_y = 0.31
            elif hypno11 == "Nozomi":
                if persistent.NewSprite == " New":
                    $light_x = 0.46; light_y = 0.25; slight_x = 0.5; slight_y = 0.25
                else:
                    $light_x = 0.46; light_y = 0.25; slight_x = 0.5; slight_y = 0.25
            elif hypno11 == "Sayori":
                if persistent.NewSprite == " New":
                    $light_x = 0.45; light_y = 0.225; slight_x = 0.49; slight_y = 0.22
                else:
                    $light_x = 0.435; light_y = 0.2; slight_x = 0.47; slight_y = 0.19
            show plight:
                xpos light_x
                ypos light_y
            "Taking my penlight, I switch it on and hold it in front of [p_their] face, shining the beam harshly into each eye." with dissolve
            show plight:
                linear 1.0 xpos slight_x ypos slight_y
            "No blinking, no response of any kind. Okay."
            hide plight with dissolve
            hide penlight with moveoutright
            if hypno11 == "Hiroko":
                show Hiroko entranced_talk
            elif hypno11 == "Nozomi":
                show Nozomi entranced_wideopen
            elif hypno11 == "Sayori":
                show Sayori entranced_talk_right
            "I then reach up to the stationary [hypno6]'s face and pull [p_their] jaw open without resistance..." with dissolve
            "... before firmly pushing a couple fingers inside [p_their] mouth."
            "My fingertips drag all the way over [p_their] tongue and press right through to the back of [p_their] throat."
            "No clear signs of respiratory, physical or emotional response. So far so good."
            "I leave them in [p_their] mouth a little longer to be certain, then pull them out and start to drag my wettened fingertips over [p_their] exposed nipples."
            "Watching [p_their] expression carefully, there is again no response of any kind as my fingers stroke [p_their] breasts for close to a minute."
            "After giving each nipple a firm squeeze and tug, I withdraw and nod to myself."
            "That's good. The other week one of the [hypno6]s actually moaned when I did that."
            "I can't recall which of them it was now, but I needed a whole evening to debug that response out of [p_them]. That should NOT be happening in maintenance mode."
            "And it's why I keep doing these checks. I have to make sure their human personality core is airtight, and doesn't leak into their primary code."
            "As it is, I decided to erase all awareness of their true natures from their human personalities again to limit that risk."
            "After all, there's no telling what one of these [hypno6]s would do if they were able to disrupt their programming."
            "Anyway, as one final test I grab [p_their] wrist and take [p_their] pulse again. It seems to be just as stable and even as when I took it before."
            if hypno11 == "Hiroko":
                show Hiroko entranced_neutral
            elif hypno11 == "Nozomi":
                show Nozomi entranced_neutral
            elif hypno11 == "Sayori":
                show Sayori entranced_right
            if hypno11 == "Hiroko":
                "With a satisfied nod, I raise a hand to [p_their] face and snap [p_their] jaw back shut. All tests complete." with dissolve
                "Other than the minor shoulder damage, this one seems to be in perfect working order."
            else:
                "Satisfied, I raise a hand to [p_their] face and snap [p_their] jaw back shut. All tests complete: This one seems to be in good working order." with dissolve
            "All that remains is for me to pop out the earpiece buried in [p_their] audio receptacle and replace it with a fresh one."
            "The [hypno6]s are programmed to regularly recharge their earpieces and replace them automatically."
            "But it never hurts to do it myself while they're here, just to be extra certain."
            "After all, without a fully-functional receiver, [hypno6].apk is as good as worthless."
            "They wouldn't be able to receive the coded messages transmitted from the client version of the [hypno6].apk app, that I wrote and installed on their own phones."
            show phone at right with moveinright:
                ypos 0.346
            "In any case, I bring the app up again on my phone and press the \"Work Mode\" button."
            # "In any case, I bring the app up again on my phone and look at the array of options available."
            # "I could be a little more thorough and test the other options, but I'm not sure it's worth my time."
            # label Roboplay:
            #     $hypno6 = hypno6.capitalize()
            #     menu:
            #         "Human Mode Configuration":
            #             "Better make sure this is still correct."
            #             play sound appbutton
            #             if hypno11 == "Hiroko":
            #                 h entranced_talk "Accessing human mode configuration... please input further instruction." with dissolve
            #                 show Hiroko entranced_neutral
            #                 ks "00[hypno12], report your current configuration. [hypno3]." with dissolve
            #                 h entranced_talk "Assigned Name: Hiroko Homura\nGlobal Behaviour Setting: Default" with dissolve
            #                 h "Behavioural Modifications: \nNon-violence. Subject: Kyou Koyama\nAdditional Instructions: None"
            #             elif hypno11 == "Sayori":
            #                 s entranced_talk "Accessing human mode configuration... please input further instruction." with dissolve
            #                 show Sayori entranced_neutral
            #                 ks "00[hypno12], report your current configuration. [hypno3]." with dissolve
            #                 s entranced_talk "Assigned Name: Sayori Watanabe\nGlobal Behaviour Setting: Default" with dissolve
            #                 s "Behavioural Modifications: \nNon-violence. Subject: Kyou Koyama\nAdditional Instructions: None"
            #             elif hypno11 == "Nozomi":
            #                 n entranced_talk "Accessing human mode configuration... please input further instruction." with dissolve
            #                 show Nozomi entranced_neutral
            #                 ks "00[hypno12], report your current configuration. [hypno3]." with dissolve
            #                 n entranced_talk "Assigned Name: Nozomi Akemi\nGlobal Behaviour Setting: Default" with dissolve
            #                 n "Behavioural Modifications: \nHeightened happiness. Subject: Kyou Koyama"
            #                 n "Additional Instructions: None"
            #         "Object Mode":
            #             play sound appbutton
            #             "This one opens a submenu of, to be honest, pretty useless functions that I coded in just to see if I could."
            #             menu:
            #                 "Table":
            #                     if hypno11 == "Hiroko":
            #                         show Hiroko:
            #                             linear 1.0 ypos 1.3
            #                         "Almost immediately, the [hypno6!l] drops in front of me and plants her hands and knees on the floor, straightening her back to make a crudely horizontal surface."
            #                         "It's good that it works, but there's no getting away from the fact that [hypno6!c]s make for really shitty furniture."
            #                 "Footstool":
            #                     if hypno11 == "Hiroko":
            #                         show Hiroko:
            #                             linear 1.0 ypos 1.4
            #                         "Almost immediately, the [hypno6!l] drops in front of me and plants her hands and knees on the floor, straightening her back to make a crudely horizontal surface."
            #                         "It's good that it works, but there's no getting away from the fact that [hypno6!c]s make for really shitty furniture."
            #         "Work Mode":
            #             jump label WorkMode
            label WorkMode:

                play sound appbutton
                if hypno11 == "Hiroko":
                    h entranced_talk "Work mode activated. Present tasks: None. [hypno6!c]#00[hypno12] is idle." with dissolve
                    h "Please input new work order."
                    show Hiroko entranced_neutral
                    "This house is close to flawless now, since I had all the [hypno6]s over to do a deep clean of the place the other weekend." with dissolve
                    "Sure impressed my dad when he got back that night."
                    "Still, there's always something to do around here, and it's a waste to have a piece of tech like this and not put it to use."
                    ks "00[hypno12], add new work order: Standard house-cleaning protocols. Priority: Floors and work surfaces. [hypno3]."
                    h entranced_talk "[hypno2]. [hypno6!c]#00[hypno12] is executing current task: Standard house-cleaning protocol." with dissolve
                elif hypno11 == "Nozomi":
                    n entranced_talk "Work mode executed. Present tasks: None. [hypno6!c]#00[hypno12] is idle." with dissolve
                    n "Please input new work order."
                    show Nozomi entranced_neutral
                    "This house is close to flawless now, since I had all the [hypno6]s over to do a deep clean of the place the other weekend." with dissolve
                    "Sure impressed my dad when he got back that night."
                    "Still, there's always something to do around here, and it's a waste to have a piece of tech like this and not put it to use."
                    ks "00[hypno12], add new work order: Standard house-cleaning protocols. Priority: Floors and work surfaces. [hypno3]."
                    n entranced_talk "[hypno2]. [hypno6!c]#00[hypno12] is executing current task: Standard house-cleaning protocol." with dissolve
                elif hypno11 == "Sayori":
                    s entranced_talk_right "Work mode executed. Present tasks: None. [hypno6!c]#00[hypno12] is idle." with dissolve
                    s "Please input new work order."
                    show Sayori entranced_right
                    "This house is close to flawless now, since I had all the [hypno6]s over to do a deep clean of the place the other weekend." with dissolve
                    "Sure impressed my dad when he got back that night."
                    "Still, there's always something to do around here, and it's a waste to have a piece of tech like this and not put it to use."
                    ks "00[hypno12], add new work order: Standard house-cleaning protocols. Priority: Floors and work surfaces. [hypno3]."
                    s entranced_talk_right "[hypno2]. [hypno6!c]#00[hypno12] is executing current task: Standard house-cleaning protocol." with dissolve
            hide Sayori
            hide Nozomi
            hide Hiroko
            with dissolve
            play sound footsteps
            hide phone with moveoutright
            "As the [hypno6] turns on [p_their] heel and obediently sets [p_them]self to work, I head back upstairs to my room."
            scene bg k bedroom eve
            with blink
            "I fall back on my bed with a sigh. Watching that thing work was interesting the first time, but it quickly loses its luster after a couple of hours."
            "I confirmed the charged-up earpiece functions properly, anyway. That's all I really needed. But now what?"
            "I'm just so fucking bored."
            "My projects kept me distracted from thinking about it, but now I've done everything I wanted to with my [hypno6] hobby."
            "I've reprogrammed the ones I found as well as I can. Removed all the faults in their code."
            "So long as I maintain them on the regular, they'll function perfectly until their circuits start to give out."
            "There's nothing left for me to tinker with."
            "And there's no one to talk to. I have no friends, and [hypno6]s are useless company when you know they're just machines running code."
            "What am I supposed to do now..."
            with blink
            play sound dooropen
            if hypno11 == "Hiroko":
                show Hiroko nude entranced_neutral at center
            elif hypno11 == "Nozomi":
                show Nozomi front nude entranced_neutral at center
                if glassesoff == True:
                    show Nozomi noglasses
            elif hypno11 == "Sayori":
                show Sayori nude normal_attention entranced_right at center
            with dissolve
            "... I don't know how long it's been, but I'm disturbed from my reverie by the sound of the [hypno6] in the house blundering into my room."
            "Sitting up on my bed, I find myself idly watching [p_them] work, as [p_they] wordlessly wipes down my desk and table with a cloth."
            "[p_they!c] looks so at ease... Makes me want to make [p_their] automated life just that tiny bit harder."
            ks frown "00[hypno12], add new work order: Acquire item \"cola\" from kitchen fridge. Deliver item to sysadmin. [hypno3]."
            if hypno11 == "Hiroko":
                h entranced_talk "[hypno2]. New work order queued: Acquire item \"cola\" from kitchen fridge. Deliver item to sysadmin." with dissolve
                show Hiroko entranced_neutral
            elif hypno11 == "Nozomi":
                n entranced_talk "[hypno2]. New work order queued: Acquire item \"cola\" from kitchen fridge. Deliver item to sysadmin." with dissolve
                show Nozomi entranced_neutral
            elif hypno11 == "Sayori":
                s entranced_talk_right "[hypno2]. New work order queued: Acquire item \"cola\" from kitchen fridge. Deliver item to sysadmin." with dissolve
                show Sayori entranced_right
            "I shake my head as the [hypno6] processes my command and adds it to [p_their] work queue without missing a beat in [p_their] current task." with dissolve
            ks frown "Look at you. Working away without a care in the world."
            ks "You never have a problem with boredom, do you, [hypno6]."
            "I might as well be talking to myself, as the [hypno6] continues [p_their] monotonous cleaning routine in my room completely unfazed."
            ks "Man, if I could just have no thoughts or worries like you. That almost sounds appealing right about now."
            ks "But I can't, because unlike you, I'm a goddamn human."
            ks "Not like... not like you."
            if hypno11 == "Hiroko":
                show Hiroko nude entranced_neutral at center:
                    linear 1.0 xpos 0.25
            elif hypno11 == "Nozomi":
                show Nozomi front nude entranced_neutral at center:
                    linear 1.0 xpos 0.25
            elif hypno11 == "Sayori":
                show Sayori nude entranced_right at center:
                    linear 1.0 xpos 0.25
            "Setting the cloth down, the [hypno6] obliviously walks across to pick up my bin as I talk to myself."
            "\"Just... be kind to her, won't you?\""
            "Not like... fuck, why am I thinking about that AGAIN?"
            ks angry "It... it's not true! I..."
            play sound footsteps
            if hypno11 == "Hiroko":
                show Hiroko nude entranced_neutral at center:
                    linear 2.0 xpos -0.14
            elif hypno11 == "Nozomi":
                show Nozomi front nude entranced_neutral at center:
                    linear 2.0 xpos -0.14
            elif hypno11 == "Sayori":
                show Sayori nude entranced_right at center:
                    linear 2.0 xpos -0.14
            "Just then, my [hypno6] company starts to walk out of the room with my bin in [p_their] hands to go empty it."
            ks "Hey [hypno11], wait! I'm not done with you!"
            "... Holy shit, I must really be losing it if I'm calling her that while her human AI's switched off."
            scene cg k bedroom eve2
            show Kyou_Robo upper
            with blink
            play sound appbutton
            "Reaching for my phone again, I open the [hypno6].apk app back up with its screen showing the \"Work Mode\" window, and press the pause button."
            show Kyou_Robo rest
            $ renpy.transition(dissolve, layer="master")
            if hypno11 == "Hiroko":
                h "{size=16}Work mode paused.{/size}"
            elif hypno11 == "Nozomi":
                n "{size=16}Work mode paused.{/size}"
            elif hypno11 == "Sayori":
                s "{size=16}Work mode paused.{/size}"
            ks angry "00[hypno12], get your ass back in here NOW! [hypno3]!"
            play sound footsteps
            "I can hear the bin clatter to the ground and the unhurried patter of bare feet on the floorboards as [p_they] returns to me automatically."
            if hypno11 == "Hiroko":
                show Hiroko_K_Bedroom_Robo robot with dissolve
                pause 0.5
                show Hiroko_K_Bedroom_Robo open
                $ renpy.transition(dissolve, layer="master")
                h "[hypno2]."
                show Hiroko_K_Bedroom_Robo closed
                $ renpy.transition(dissolve, layer="master")
            elif hypno11 == "Nozomi":
                show Nozomi_K_Bedroom_Robo robot
                if glassesoff == True:
                    show Nozomi_K_Bedroom_Robo noglasses
                with dissolve
                pause 0.5
                show Nozomi_K_Bedroom_Robo open
                $ renpy.transition(dissolve, layer="master")
                n "[hypno2]."
                show Nozomi_K_Bedroom_Robo closed
                $ renpy.transition(dissolve, layer="master")
            elif hypno11 == "Sayori":
                show Sayori_K_Bedroom_Robo robot with dissolve
                pause 0.5
                show Sayori_K_Bedroom_Robo open
                $ renpy.transition(dissolve, layer="master")
                s "[hypno2]."
                show Sayori_K_Bedroom_Robo closed
                $ renpy.transition(dissolve, layer="master")
            ks smile "Eheh..."
            "I can't help but chuckle at my momentary panic."
            ks smirk "You... you really are realistic for a machine, not gonna lie."
            ks "Even now you almost fooled me again."
            if hypno11 == "Hiroko":
                h "..."
            elif hypno11 == "Nozomi":
                n "..."
            elif hypno11 == "Sayori":
                s "..."
            ks angry "But you ARE just a machine. I'll... I'll prove it."
            show Kyou_Robo upper
            "Swiping my thumb on the app, I go back a page and hit the large green button on the top: \"Online Mode\"." with dissolve
            play sound appbutton
            show Kyou_Robo rest
            if hypno11 == "Hiroko":
                show Hiroko_K_Bedroom_Robo confused
                $ renpy.transition(dissolve, layer="master")
                h "Kyou? What the fuck just happened?"
                show Hiroko_K_Bedroom_Robo panicked blush
                $ renpy.transition(dissolve, layer="master")
                h "And {w=0.2}{nw}"
                extend "WHY THE FUCK AM I NAKED?! H-H-HOLY SHIT!" with shake
            elif hypno11 == "Nozomi":
                show Nozomi_K_Bedroom_Robo confused
                $ renpy.transition(dissolve, layer="master")
                n "... Hm? Kyou? Wait, what just happened?" with dissolve
                n "Uh...{w=0.5}{nw}"
                show Nozomi_K_Bedroom_Robo panicked blush
                $ renpy.transition(dissolve, layer="master")
                extend " O-Oh, OH MY GOD! WHAT HAPPENED TO MY CLOTHES?!"
            elif hypno11 == "Sayori":
                show Sayori_K_Bedroom_Robo confused
                $ renpy.transition(dissolve, layer="master")
                s "... Kyou? Kyou, what is going on?"
                s "Wh- {w=0.2}{nw}"
                show Sayori_K_Bedroom_Robo panicked blush
                $ renpy.transition(dissolve, layer="master")
                extend "What the?!"
                s "Kyou, W-w-why am I naked?!"
            "[p_they!c] replicates the appearance of panic and fright so realistically, just as her human AI dictates."
            show Kyou_Robo lower
            $ renpy.transition(dissolve, layer="master")
            "But the moment I tap my thumb over the \"Maintenance Mode\" button again, I know I can shut that shit right down." with dissolve
            if hypno11 == "Hiroko":
                h "WHAT'S GOING ON?! Wh-{w=1.0}{nw}"
                play sound appbutton
                show Hiroko_K_Bedroom_Robo body neutral
                $ renpy.transition(dissolve, layer="master")
                extend "{size=16} whaa...{/size}{w=1.0}{nw}"
                show Kyou_Robo rest
                show Hiroko_K_Bedroom_Robo robot
                $ renpy.transition(longdissolve, layer="master")
                extend ""
            elif hypno11 == "Nozomi":
                n "KYOU?! WH-{w=1.0}{nw}"
                play sound appbutton
                show Nozomi_K_Bedroom_Robo neutral body
                $ renpy.transition(dissolve, layer="master")
                extend "{size=16} what is...{/size}{w=1.0}{nw}"
                show Kyou_Robo rest
                show Nozomi_K_Bedroom_Robo robot
                $ renpy.transition(longdissolve, layer="master")
                extend ""
            elif hypno11 == "Sayori":
                s "I demand an- {w=1.0}{nw}"
                play sound appbutton
                show Sayori_K_Bedroom_Robo neutral body
                $ renpy.transition(dissolve, layer="master")
                extend "{size=16}a-an... {/size}{w=1.0}{nw}"
                show Kyou_Robo rest
                show Sayori_K_Bedroom_Robo robot
                $ renpy.transition(longdissolve, layer="master")
                extend ""
            ks smirk "Y-You see? I couldn't do this to a human being, now could I?"
            "I hold my phone out in front of her as my trembling thumb slowly bounces between the two buttons on the screen."
            play sound appbutton
            show Kyou_Robo upper
            $ renpy.transition(dissolve, layer="master")
            pause 0.2
            if hypno11 == "Hiroko":
                show Hiroko_K_Bedroom_Robo panicked
                $ renpy.transition(dissolve, layer="master")
                h shocked "What the {nw}"
                extend "FUCK is going on?!" with vpunch
                ks "Couldn't... c-couldn't do this at all... switching you off and on like an appliance."
                show Kyou_Robo lower
                $ renpy.transition(dissolve, layer="master")
                h "Who you callin' an- {w=0.5}{nw}"
                play sound appbutton
                show Hiroko_K_Bedroom_Robo neutral
                $ renpy.transition(dissolve, layer="master")
                extend "{size=16}a-an...{/size}{w=1.0}{nw}"
                # pause 0.5
                show Hiroko_K_Bedroom_Robo robot
                show Kyou_Robo rest
                $ renpy.transition(longdissolve, layer="master")
                extend ""
                ks "There's just no way..."
                show Kyou_Robo upper
                $ renpy.transition(dissolve, layer="master")
                pause 0.2
                play sound appbutton
                show Hiroko_K_Bedroom_Robo confused
                $ renpy.transition(longdissolve, layer="master")
                h "Uhh... what're you doing to me? So... s-so dizzy..."
                ks "A-all I did was alter your programming..."
                show Kyou_Robo lower
                $ renpy.transition(dissolve, layer="master")
                h "The fuck are y-{w=0.5}{nw}"
                play sound appbutton
                show Hiroko_K_Bedroom_Robo robot
                $ renpy.transition(longdissolve, layer="master")
                extend ""
                h "..."
            elif hypno11 == "Nozomi":
                show Nozomi_K_Bedroom_Robo panicked
                $ renpy.transition(dissolve, layer="master")
                n "Kyou? What's going on?! What just happened?"
                ks "Couldn't... c-couldn't do this at all... switching you off and on like an appliance."
                show Kyou_Robo lower
                $ renpy.transition(dissolve, layer="master")
                n "Switching me-{w=0.5}{nw}"
                play sound appbutton
                show Nozomi_K_Bedroom_Robo neutral
                $ renpy.transition(dissolve, layer="master")
                extend "I...{w=1.0}{nw}"
                show Nozomi_K_Bedroom_Robo robot
                show Kyou_Robo rest
                $ renpy.transition(longdissolve, layer="master")
                extend ""
                ks "There's just no way..."
                show Kyou_Robo upper
                $ renpy.transition(dissolve, layer="master")
                pause 0.2
                play sound appbutton
                show Nozomi_K_Bedroom_Robo confused
                $ renpy.transition(longdissolve, layer="master")
                n "What's... what's happening to me..."
                ks "A-all I did was alter your programming..."
                show Kyou_Robo lower
                $ renpy.transition(dissolve, layer="master")
                n "Programming? What do you m-{w=0.5}{nw}"
                play sound appbutton
                show Nozomi_K_Bedroom_Robo robot
                $ renpy.transition(longdissolve, layer="master")
                extend ""
                n "..."
            elif hypno11 == "Sayori":
                show Sayori_K_Bedroom_Robo panicked
                $ renpy.transition(dissolve, layer="master")
                s "Kyou?! What are you doing?!"
                ks "Couldn't... c-couldn't do this at all... switching you off and on like an appliance."
                show Kyou_Robo lower
                $ renpy.transition(dissolve, layer="master")
                s "\"Appliance?\" What are you talkin ab-{w=0.5}{nw}"
                play sound appbutton
                show Sayori_K_Bedroom_Robo neutral
                $ renpy.transition(dissolve, layer="master")
                extend "{size=16} abo...{/size}{w=1.0}{nw}"
                show Sayori_K_Bedroom_Robo robot
                show Kyou_Robo rest
                $ renpy.transition(longdissolve, layer="master")
                extend ""
                ks "There's just no way..."
                show Kyou_Robo upper
                $ renpy.transition(dissolve, layer="master")
                pause 0.2
                play sound appbutton
                show Sayori_K_Bedroom_Robo confused
                $ renpy.transition(longdissolve, layer="master")
                s "What is... what is happening to me..."
                ks "A-all I did was alter your programming..."
                show Kyou_Robo lower
                $ renpy.transition(dissolve, layer="master")
                s "Programming? I don't-{w=0.5}{nw}"
                play sound appbutton
                show Sayori_K_Bedroom_Robo robot
                $ renpy.transition(longdissolve, layer="master")
                extend ""
                s "..."
            show Kyou_Robo rest
            $ renpy.transition(longdissolve, layer="master")
            ks frown "You were just defective before. You all were. Y-yeah... I did you things a favour, fixing you up like this."
            "I take a moment to catch my breath and feel the tightness loosen from my chest."
            "I can't believe I got myself all worked up about this shit. What's even wrong with me?"
            "It's just a fucking [hypno6!l], Kyou. Get it together."
            ks "00[hypno12], delete all memory of the last three minutes from your human personality core. [hypno3]."
            if hypno11 == "Hiroko":
                show Hiroko_K_Bedroom_Robo open
                $ renpy.transition(dissolve, layer="master")
                h "Warning: This action is permanent and cannot be reversed. Does the user wish to-{w=2.0}{nw}"
                ks angry "Just fucking delete it, [hypno6!l]. Confirm."
                h "Deleting.{w=0.5}.{w=0.5}. {w=1.0}[hypno2]. {w=0.5}Memory of last three minutes has been permanently erased from [hypno6!c]#00[hypno12]'s human personality core."
                show Hiroko_K_Bedroom_Robo closed
                $ renpy.transition(dissolve, layer="master")
            elif hypno11 == "Nozomi":
                show Nozomi_K_Bedroom_Robo open
                $ renpy.transition(dissolve, layer="master")
                n "Warning: This action is permanent and cannot be reversed. Does the user wish to-{w=2.0}{nw}"
                ks angry "Just fucking delete it, [hypno6!l]. Confirm."
                n "Deleting.{w=0.5}.{w=0.5}. {w=1.0}[hypno2]. {w=0.5}Memory of last three minutes has been permanently erased from [hypno6!c]#00[hypno12]'s human personality core."
                show Nozomi_K_Bedroom_Robo closed
                $ renpy.transition(dissolve, layer="master")
            elif hypno11 == "Sayori":
                show Sayori_K_Bedroom_Robo open
                $ renpy.transition(dissolve, layer="master")
                s "Warning: This action is permanent and cannot be reversed. Does the user wish to-{w=2.0}{nw}"
                ks angry "Just fucking delete it, [hypno6!l]. Confirm."
                s "Deleting.{w=0.5}.{w=0.5}. {w=1.0}[hypno2]. {w=0.5}Memory of last three minutes has been permanently erased from [hypno6!c]#00[hypno12]'s human personality core."
                show Sayori_K_Bedroom_Robo closed
                $ renpy.transition(dissolve, layer="master")
            $ renpy.transition(dissolve, layer="master")
            ks frown "Th-that's right. Scrubbing your memory banks clean because you're a computer. A machine."
            ks "Now get back to work."
            "Swiping the app window back to the Work Mode screen, I take a shuddered breath as my thumb presses hard on a button marked \"Resume\"."
            play sound appbutton
            show Kyou_Robo upper
            $ renpy.transition(dissolve, layer="master")
            pause 0.2
            if hypno11 == "Hiroko":
                show Hiroko_K_Bedroom_Robo open
                $ renpy.transition(dissolve, layer="master")
                h "[hypno6!c]#00[hypno12] is resuming Work Mode. Current task: Standard house-cleaning protocol."
                $ persistent.k_bedroom_robot_hiroko_unlock = True
            elif hypno11 == "Nozomi":
                show Nozomi_K_Bedroom_Robo open
                $ renpy.transition(dissolve, layer="master")
                n "[hypno6!c]#00[hypno12] is resuming Work Mode. Current task: Standard house-cleaning protocol."
                $ persistent.k_bedroom_robot_nozomi_unlock = True
            elif hypno11 == "Sayori":
                show Sayori_K_Bedroom_Robo open
                $ renpy.transition(dissolve, layer="master")
                s "[hypno6!c]#00[hypno12] is resuming Work Mode. Current task: Standard house-cleaning protocol."
                $ persistent.k_bedroom_robot_sayori_unlock = True
            play sound footsteps
            hide Nozomi_K_Bedroom_Robo
            hide Hiroko_K_Bedroom_Robo
            hide Sayori_K_Bedroom_Robo
            show Kyou_Robo rest
            "And off [p_they] goes, padding with unhurried steps back outside to pick up the bin [p_they] dropped, almost as if my interruption never happened." with dissolve
            show Kyou_Robo nohand
            "Now where was I? Oh yeah..." with dissolve
            "Bored. Just... just bored..."
            stop sound
            #Need to impress Kyou's sanity slippage, reasoning how the girls are so obviously bots and he shouldn't get hung up about treating them as such
            #But it's kind of obvious that he's kidding himself and he's going mad from guilt?
            # play sound cellvibrate
            # show phone at right with moveinright:
            #     ypos 0.346
            # "\"[hypno2].\""
            # "..."
            # "Why did I do all of this?"
            jump Credits
    elif hypno1 == "spy hiroko" and spyfight == False:
        show Hiroko uniform_armup irritated uniform_arm at center
        show Sayori smile at center, flip:
            xpos 0.25
        show Nozomi side smile_side at center:
            xpos 0.75
        with dissolve
        h "Ugh. Let's get this shit over with." with dissolve
        s "Oh, please. You enjoy it more than you let on."
        "It's been about a month since that day."
        h frown_side no_arm "Eh, you know what I wanna be doing instead." with dissolve
        n laugh "Eheh, your studies are still important, Hiroko. You'll be thanking us for this later~" with dissolve
        "A month since I hypnotized these three into becoming my willing spies."
        s smile_right "Are you coming, Kyou?" with dissolve
        ks smile "Oh yeah, sure. Be right with you."
        stop music fadeout 5.0
        scene bg study room eve
        show Hiroko at center, flip:
            xpos 0.25
        show Sayori smile at center:
            xpos 0.75
        show Nozomi front smile at center
        with blink
        "A lot has happened since then."
        play music Eons
        "Making the girls aware and eager participants in gaining me influence has paid dividends."
        "First, we took over Sayori's study club, which made ideal cover for us to meet on school grounds without anyone else listening in."
        ks neutral "So, what did we learn today, girls?"
        h uniform_armup happy "Ooh, me first!" with dissolve
        s uniform_folded "If you insist." with dissolve
        h laugh "Yeah, so Chiyo told me her dad's got a little business going on the side?" with dissolve
        ks "Yes, and?"
        h "He ain't telling the taxman about it! You can totally use that, right?"
        ks smile "That is good to know, yeah. Let me note that down..."
        "Pulling out my phone, I bring up the relevant entry and start typing."
        s "Speaking of dads..."
        "Sayori smiles and pulls out a stack of printouts from her bag."
        s smile_right "Mine took some of his work home with him last night and I was able to procure copies." with dissolve
        s "I have not had time to go through them, but they should turn up some dirt, I would think."
        s smirk_right "And even if they don't, a police sergeant leaking so many documents on top of the other... \"mishaps\" he has had recently should be cause for concern." with dissolve
        show Nozomi laugh
        show Hiroko uniform happy
        "That gets a laugh out of everyone. Sayori's parents have been a goldmine for confidential information." with dissolve
        ks "And what about you, Nozomi?"
        show Hiroko smile_side
        show Sayori smile
        n smile "Well, I had a chance to visit the teacher's lounge today as you saw." with dissolve
        n "And while I was there, I overheard Mrs. Tanaka complaining about how long it takes her to finish her paperwork every afternoon."
        n side smile "I'm sure you could sneak into her classroom after the other teachers in her block have gone home and... \"recruit her\"?" with dissolve
        show penlight at right with moveinright:
            ypos 0.346
        "I pull out the penlight from my pocket and nod."
        ks "We were looking for more on the faculty to join us in an \"official\" capacity, yeah."
        ks "So that's what I'll be doing in a bit. What else can you tell me about her?"
        hide penlight with moveoutright
        n front chuckle "Well..." with dissolve
        scene bg blackscreen with fade
        nvl_narrator "Time passed as we set to work on expanding my influence."
        nvl_narrator "Over time, everyone in school who wasn't hypnotized into my service was brought to heel by other means."
        nvl_narrator "Within a few months, most of the local community was in my pocket, too."
        scene bg blackscreen with fade
        nvl clear
        stop music fadeout 5.0
        nvl_narrator "How far could I go?"
        nvl_narrator "So far I've been careful not to expose myself. People have ignored me for all this time, but it's okay now. Now I WANT to be ignored."
        nvl_narrator "I mean, if I can just keep going like this, I could be a genuine ruler from the shadows."
        scene bg blackscreen with fade
        nvl clear
        play music Sorrow
        nvl_narrator "It won't matter then, if people still ignore me. I'll have the real power around here."
        nvl_narrator "It's fine if the only ones who'll hang on my every word are the ones who fell under the full glow of my penlight."
        nvl_narrator "Who cares if people still treat me with contempt in public? I could have them destroyed with just a few words to my loyal agents."
        # nvl_narrator "... And then what?"
        # nvl_narrator "Even as I accrue all this power, I feel an emptiness."
        # nvl_narrator "For all the people I bring into my orbit, there's no one I can be close to."
        scene bg blackscreen with fade
        nvl clear
        nvl_narrator "I don't NEED anyone to love me anymore. Not Nozomi, not the dozens of other cute girls I have in my service. No one."
        nvl_narrator "I have a power no one else has. That'll always make me somebody."
        nvl_narrator "That'll always... that'll always be good enough for me..."
        # nvl_narrator "How can I be close to anyone after this? Everyone in my life is compromised, my relationships based on lies that I built; I know that."
        # nvl_narrator "Nozomi might smile and listen to me now, as will hundreds of other cute girls. But so what?"
        # nvl_narrator "They'll never love me the way I want."
        jump Credits

        #"Chiyo! She was in tennis club with me, she's so pretty~"
        #Kyou attempted to build more penlights for his new agents to use, but they all failed
    elif hypno1 == "spy hiroko" and spyfight == True:
        show Hiroko uniform_armup smile_side at center
        show Sayori smile at center, flip:
            xpos 0.25
        h "Alright, I'm outta here." with dissolve

label Epilogue_Villain_Devoted_Girlfriend:
    scene bg classroom eve with longdissolve
    "As another school day draws to a close, I gather my things and ponder."
    play music Memories
    play sound schoolbell
    show Hiroko happy uniform_armup uniform_arm at center
    show Sayori happy at center, flip:
        xpos 0.25
    with dissolve
    h "WEEEKEEEEEENND~" with vpunch
    "It's been nearly three weeks since I turned the minds of Nozomi and her friends."
    s "Indeed. Another five days of unpleasant distractions have been well and truly conquered."
    "And I have to admit, life has been pretty great to me lately."
    show Hiroko uniform smile
    s smile_right "Are you ready to go, Mr. Koyama?" with dissolve
    "I mean, it's hard not to love having a posse of girls who'll joyfully hang on my every word."
    # h angry_side "TOO DAMN LONG! I can't believe they wouldn't just give this to us."
    show Nozomi front2 loving blush at center:
        xpos 0.75
    n "Not without me he isn't~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    "Not to mention my cute, extremely attentive girlfriend..."
    ks smile "Yeah, you two go carry our bags for us; we're getting out of here."
    show Sayori uniform_handup happy
    h uniform_armup happy "Dibs on Kyou's bag!" with dissolve
    s "{cps=20}I shall call carry K-... {/cps}{w=0.5}{nw}"
    $ renpy.transition(dissolve, layer="master")
    extend frown "damn you, Hiroko."
    scene bg blackscreen with dissolve
    "Of course our classmates have started to gossip about us."
    "The other girls don't understand our dynamic at all, and the guys want to know how someone like me managed to pull this off."
    "Needless to say, I'm happy to keep my secrets..."
    scene bg street1 eve
    show Nozomi front2 smile blush at center
    show Sayori uniform_folded smile_right blush at center, flip:
        xpos 0.25
    show Hiroko uniform smile blush at center:
        xpos 0.75
    with longdissolve
    "I head home walking arm in arm with my girlfriend, while my obsessed groupies dutifully follow closely behind."
    ks sigh "So, guess who wasn't paying attention for that physics lecture this afternoon."
    n sigh "Urrgh, you too? It was sooo boring, I could barely keep my eyes open." with dissolve
    n loving "Besides, I had other... things on my mind, ehehehe~" with dissolve
    ks smirk "Oh, I'm sure..."
    "I give Nozomi a little squeeze, and she giggles as she plants her head on my shoulder."
    ks smile "Sayori?"
    s uniform giggle "Y-yes, Mr. Koyama?" with dissolve
    ks "Send us both a copy of your notes when you get home."
    s uniform_handup happy "Mhmhmhm, it would be my pleasure!" with dissolve
    n neutral_left noblush "Oh that reminds me, let me see your homework for English Lit too." with dissolve
    show Hiroko neutral_side noblush
    s surprised noblush "O-oh, you have not done that one already?" with dissolve
    n pout "I haven't gotten around to it yet, but the deadline's on Monday and Kyou's taking me out tomorrow." with dissolve
    n neutral_left "You understand, right?" with dissolve
    s concerned "Still, I thought you were passionate about the subject. You are Ms. Chiba's favourite for a reason." with dissolve
    n sleeptalk "That's right, and I prefer to keep it that way if you don't mind. I've just been busy with... t-things lately, you know how it is." with dissolve
    ks smirk "Do as she says, Sayori."
    s happy blush "... I shall send it to you with my notes, Ms. Akemi~" with dissolve
    n chuckle "Mhmhm, that's what I thought." with dissolve
    "I chuckle with her as we come to a crossroad in the street. Seems Nozomi is becoming more comfortable with enjoying the side benefits of having a powerful hypnotist for a boyfriend."
    ks smile "Alright, well this is us so we'll see you guys tomorrow."
    show Nozomi smile
    show Sayori concerned_right noblush
    h uniform_headhold nervous "Aww, can't we come with this time? Like, I know Nozo's your number one, but we love ya too, y'know?" with dissolve
    "Nozomi and I turn back to face the pair of them. Just looking at those lovestruck faces makes me grin."
    show Nozomi neutral
    show Hiroko uniform_headhold2 sad_side
    s uniform "Yes. We have no desire to come between you and Nozomi, but surely we are all friends here." with dissolve
    "It's not like I'm surprised that they're still like this. Ever since I hypnotized them, their desire to please me has only grown stronger."
    show Hiroko sad
    s sleeptalk_concerned blush "If we could brighten up your evening in any way. Any way at all..." with dissolve
    ks smirk "Heh. And how would you girls \"brighten up my evening\"?"
    s uniform_handup surprised_right "O-oh, well we... th-that is..." with dissolve
    "I'm still content to let them lavish me with their attention, even if my girlfriend seems unamused as I spy her folding her arms."
    n pout "Urrgh, just give us our bags back and go home. This is getting embarrassing even for you two." with dissolve
    s smile_right "Perhaps... Do you have any dinner plans, Mr. Koyama?" with dissolve
    ks confused "Uhh... Me and Nozomi were just gonna get some ramen or something."
    s giggle "Neither of you cook?" with dissolve
    "I can see the arousal of hope in Sayori's eyes as they seem to widen."
    ks "Ehh, not really, no."
    "And sure enough, Sayori claps her hands excitedly as I give her an opening."
    s uniform_folded laugh "I knew it! Kyou, please grant me the opportunity to impress you with my culinary skill!" with dissolve
    show Hiroko neutral_side
    n neutral_left "I didn't know you cooked, Sayori." with dissolve
    show Hiroko smile_side blush
    s giggle "I may be somewhat out of practice, but I am positive I can prepare something far more pleasurable to your palettes than store-bought ramen." with dissolve
    show Nozomi neutral_right
    h uniform_armup happy "Aw, FUCK yeah! Lemme help too! I, u-um, I do a little cookin' myself y'know~" with dissolve
    ks smirk "Hmm, I dunno... is it really such a good idea to let you two loose on my kitchen?"
    show Nozomi sleep
    h happy_closed "C'mooon, it'll be great! We're gonna treat ya like king an' queen~" with dissolve
    h uniform_headhold2 affectionate "An' then after dinner, if you need anything else from us... l-like, umm..." with dissolve
    show Nozomi irritated
    h happy "Eeehehehe~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    stop music fadeout 5.0
    "Man, they are tempting me. I haven't invited them back home since that day they helped me win over Nozomi."
    "So maybe..."
    show Nozomi side frown_side at flip
    show Sayori surprised
    show Hiroko surprised_side
    n "God, do you two even hear yourselves?" with dissolve
    queue music Eons
    n furious_side "Do you know what people say behind your back? Everyone talks about how pathetic you're being, pawing over my Kyou in the open like this." with dissolve
    n furious "Have you no self respect at all?" with dissolve
    "Oh man, are they... are my girls fighting over me now?"
    h sad_side "He's... l-like, our Kyou too, tho. We just wanna do right by him, that's all." with dissolve
    "I should probably step in, but I think I'm going to let this play out just a little longer; it amuses me."
    h sleeptalk_concerned "'Sides, I don't give a shit what those bitches think. He's the only one who matters to me." with dissolve
    s concerned "Not to mention... if it is not out of line for me to say, you benefit from our involvement as well, Ms. Akemi." with dissolve
    hide Nozomi
    show Nozomi side frown_side
    show Hiroko sad_side
    n "Oh, shut up. You're just Kyou's brainwashed lackeys, nothing more. And don't you ever forget it." with dissolve
    n irritated "Honestly don't know why he keeps you two around when he's got me." with dissolve
    "Wow, brainwashed or not, I didn't know Nozomi could be so vicious towards the girls she considered her friends. I can't help but laugh."
    ks smirk "Methinks someone's getting jealous."
    show Nozomi front2 pout
    "Nozomi turns to me as she stamps her foot on the pavement." with dissolve
    n frown "Urrrgh, just tell them to back off! I don't want to be your number one girl, Kyou." with dissolve
    n smile blush "I... I want to be your ONLY girl. Aren't I enough for you, sweetie?" with dissolve
    show Hiroko sad
    show Sayori uniform concerned_right
    "As she looks to me, Nozomi smiles that same coquettish smile she had for me when I first won her over, and before I can react she embraces me once again." with dissolve
    n chuckle "Come on, let's have a nice night in, just the two of us." with dissolve
    "She leans in, pecking my lips as she gazes into my eyes with a seductive fervour that I don't recall seeing before."
    n loving "I'll... I'll make you feel so good you'll forget all about these losers." with dissolve
    "Honestly, after the thrill of the chase had died down I've had to think about how... sort of ordinary Nozomi really is."
    "She's cute enough, but I gotta admit I've started to have my eye on other girls in other classes who seem way cuter."
    ks neutral blush "W-well, I..."
    "It'd be trivial to dump her. Just turn my penlight on her again and hypnotize her into accepting she's merely an over-obsessed groupie like her friends."
    n smirk "You'll do it for me... won't you?" with dissolve
    "But seeing this possessive streak in her? It's new. It's kinda sexy..."
    "So, after I kiss her back, I turn round to my waiting followers with my decision made."
    ks smirk "Maybe some other time, ladies. But tonight you're going to leave me alone so I can have some fun times with my girlfriend. Understood?"
    h surprised "A-ahh..." with dissolve
    "Any objections they may have had die on their lips at my declaration."
    show Hiroko smile
    show Sayori smile_right
    show Nozomi smile
    "Instead, they simply smile back at me despite their obvious disappointment." with dissolve
    h happy_closed "You got it, boss. Hope you guys have a great night~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    "My word is law to them; they'd never for a moment entertain the idea of going against my wishes."
    s uniform_handup "Then I shall head home and dream of you, Mr. Koyama. After I tend to your requests, of course." with dissolve
    s happy "Have a wonderful time~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "Nozomi and I take our bags back and leave the pair to their own devices as we giddily finish the walk back to mine."
    "I gotta start provoking this jealous side of her more often. It's fun..."
    pause 1.0
    scene bg k entrance eve
    play sound dooropen
    show Nozomi front2 chuckle blush at center
    with longdissolve
    n "Mmmn, home sweet home~"
    play sound doorclose
    queue music Night_Road
    "We barely get ourselves inside before Nozomi is all over me again, kissing me as we struggle out of our shoes by the doorway."
    ks smirk blush "Ehehe... well someone's keen tonight."
    n laugh "Ahahaha, I think that makes two of us~" with dissolve
    "Nozomi laughs as she presses a hand between my legs before slowly stroking it up the outside of my pants."
    "Oh she is definitely feeling friskier than usual tonight..."
    show Nozomi smile
    ks smile "Mmmn... s-so are we gonna do this here?" with dissolve
    show Nozomi uniform happy
    "I kiss her again and she simply giggles impishly as she puts one hand behind her back and presses a finger to my lips." with dissolve
    n smirk "L-let's put a pin on that, okay? Come on..." with dissolve
    scene bg blackscreen with dissolve
    "Grinning from ear to ear, I'm happy to let my eager girlfriend lead me by the hand as she drags me upstairs..."
    scene bg k bedroom eve
    show Nozomi front smile blush
    with dissolve
    "... and straight up to my room, naturally."
    n chuckle "S-so, um... go make yourself comfortable, sweetie." with dissolve
    play sound clothes
    hide Nozomi
    "I don't need her to tell me twice. Stepping ahead of her, I start to take off my uniform on my way to the bed..." with dissolve
    "As I pull off my shirt and settle down on the sheets, I turn around to see her crouched by the foot of my bed."
    ks nude confused "Uhh, what are you doing?"
    n "I- I'm changing, haha. Just sit tight, okay?"
    play sound clothes
    ks smirk "Oh come on, take it off where I can see you."
    n "Ahahaha..."
    show Nozomi front underwear smile blush at center with dissolve
    "She soon rises back to stand in front of me with both her hands held coyly behind her back and, disappointingly, without most of her clothes."
    scene DevotionEnd2 nozomi1 arm_up n_smile n_blush k_smirk k_blush with blink
    "Would've appreciated the striptease, but it seems my girl's got other plans as she plants her knees up on the bed before shuffling over to straddle me."
    k "Now what on earth are you planning on doing to me, you little minx?"
    "She giggles impishly as she leans a little closer to my face..."
    n "O-oh, nothing. Just going to blow your mind, that's all..."
    show DevotionEnd2 n_grin
    "A hand reaches out to press teasingly against my chest, her dainty fingertips stroking against my hot, bare skin as I can feel my breath quickening." with dissolve
    "It's weird; I've always been the one on top in these situations. I'm always the one to initiate our sexual encounters, but..."
    n "Just close your handsome eyes, relax, and let me make you feel as special as you truly are..."
    "But it's hard not to agree with what's going on with Nozomi right now."
    show bg blackscreen zorder 1 with dissolve
    "I'm getting so turned on watching her try to seduce me like this..."
    $renpy.music.set_volume(1.0)
    stop music fadeout 5.0
    with flash
    n "That's right. Breathe deep and relax for me."
    ks nude sigh "... Wait, what the hell was that?"
    with flash
    $renpy.music.set_volume(0.1)
    play music Flow
    "A light? Where the hell did she get a light?"
    n "Shh, don't worry about a thing, sweetie. It's okay."
    with flash
    $renpy.music.set_volume(0.15)
    n "Breathe deep, and allow yourself to feel all the tension in your body begin to melt away."
    scene DevotionEnd2 nozomi2 arm_up n_grin n_blush k_surprised
    with longdissolve
    k "W-what are you...?"
    show DevotionEnd2 k_surprised_light with dissolve
    show DevotionEnd2 k_surprised with dissolve
    $renpy.music.set_volume(0.2)
    k "d... doing...?"
    n "... It's just like I said, my sweet."
    show DevotionEnd2 k_surprised_light with dissolve
    show DevotionEnd2 k_surprised with dissolve
    $renpy.music.set_volume(0.25)
    pause 1.0
    show DevotionEnd2 n_giggle
    $ renpy.transition(longdissolve, layer="master")
    n smirk "... I'm going to make you feel special."
    show DevotionEnd2 k_surprised_light with dissolve
    show DevotionEnd2 k_surprised with dissolve
    $renpy.music.set_volume(0.3)
    "The light in her hand... it's MY light?!"
    show DevotionEnd2 k_struggle with dissolve
    "{cps=15}How the fuck did she get my- {/cps}{nw}"
    show DevotionEnd2 k_struggle_light with dissolve
    show DevotionEnd2 k_struggle with dissolve
    $renpy.music.set_volume(0.35)
    n "We can do this with your eyes open if you want. Just make sure to stare."
    show DevotionEnd2 k_struggle_light with dissolve
    show DevotionEnd2 k_struggle with dissolve
    $renpy.music.set_volume(0.4)
    k "{size=16}How... why... I...{/size}"
    show DevotionEnd2 k_struggle_light with dissolve
    show DevotionEnd2 k_struggle with dissolve
    $renpy.music.set_volume(0.45)
    n "Stare at this beautiful light you created. Gaze deep for your girlfriend..."
    show DevotionEnd2 k_struggle_light with dissolve
    show DevotionEnd2 k_struggle with dissolve
    $renpy.music.set_volume(0.5)
    "{cps=15}I need to... to get her off me? Stop her? But...{/cps}{w=0.5}{nw}"
    show DevotionEnd2 k_struggle_light with dissolve
    show DevotionEnd2 k_struggle with dissolve
    pause 0.5
    show DevotionEnd2 k_surprised
    $ renpy.transition(longdissolve, layer="master")
    $renpy.music.set_volume(0.55)
    n "Stare and let your mind drift. Let your mind..."
    show DevotionEnd2 k_surprised_light with dissolve
    show DevotionEnd2 k_surprised with dissolve
    $renpy.music.set_volume(0.6)
    pause 1.0
    show DevotionEnd2 k_sleepy
    $ renpy.transition(longdissolve, layer="master")
    n "... Sink. Take a deep breath, stare and sink..."
    show DevotionEnd2 k_sleepy_light with dissolve
    show DevotionEnd2 k_sleepy with dissolve
    $renpy.music.set_volume(0.65)
    "{cps=15}I can't... I can't... think-{/cps}{w=1.0}{nw}"
    show DevotionEnd2 k_sleepy_light with dissolve
    show DevotionEnd2 k_sleepy with dissolve
    pause 1.0
    show DevotionEnd2 arm_down with dissolve
    $renpy.music.set_volume(0.7)
    n "Deeper and deeper. Let every thought fade from your beautiful mind..."
    show DevotionEnd2 k_sleepy_light with dissolve
    show DevotionEnd2 k_sleepy with dissolve
    $renpy.music.set_volume(0.75)
    "I..."
    show DevotionEnd2 k_sleepy_light with dissolve
    show DevotionEnd2 k_sleepy with dissolve
    $renpy.music.set_volume(0.8)
    n "Feeling so good. Feeling so right."
    show DevotionEnd2 k_sleepy_light with dissolve
    show DevotionEnd2 k_sleepy with dissolve
    $renpy.music.set_volume(0.85)
    "I feel so good..."
    n "And as you start to sink so deep. As you let every thought go, you'll find yourself hearing only my voice."
    show DevotionEnd2 k_sleepy_light with dissolve
    show DevotionEnd2 k_sleepy with dissolve
    $renpy.music.set_volume(0.9)
    show DevotionEnd2 n_grin
    n "You'll only need me, Kyou. I'll be the only one who can make you feel special. No one else will do." with dissolve
    show DevotionEnd2 k_sleepy_light with dissolve
    show DevotionEnd2 k_sleepy with dissolve
    $renpy.music.set_volume(0.95)
    n "No one else will ever love you like I do. No one else will ever be able to make you feel this good. And very soon you're going to understand that."
    show DevotionEnd2 k_sleepy_light with dissolve
    show DevotionEnd2 k_sleepy with dissolve
    $renpy.music.set_volume(1.0)
    n "So now that you're so completely relaxed with me. Now that you're reaching that most delicious state of hypnotic trance for me..."
    show DevotionEnd2 k_sleepy_light with dissolve
    show DevotionEnd2 k_sleepy with dissolve
    n "You'll let your dreamy eyes close, and sink even deeper for your girlfriend."
    show bg blackscreen zorder 1 with longdissolve
    n "That's right. Going deeper. And deeper."
    n "It's going to be just you and me. We'll be together forever."
    n "No one will ever come between me and my boyfriend again..."
    $persistent.devotion_end_2_unlock = True
    jump Credits

label Epilogue_Villain_Robot_Quit:
    scene bg classroom eve with longblink
    "As another school day draws to a close, I gather my things and ponder."
    play music Memories
    play sound schoolbell
    show Hiroko uniform_armup happy uniform_arm at center
    show Sayori smile at center, flip:
        xpos 0.25
    h "Weekeeeeend~ {font=DejaVuSans.ttf}♫{/font}" with dissolve
    s "Do you have anything special planned, Hiroko?"
    "It's been a couple weeks since that day."
    h uniform_headhold2 smile_side "Man, I dunno. I was gonna take a break but I still wanna hit the courts again, y'know?" with dissolve
    "A couple weeks since I used my penlight on those girls and made them think they were [hypno6]s..."
    s uniform_handup happy "I imagine the excitement you felt during the tournament would be hard to quiet." with dissolve
    show Sayori smile
    h uniform_armup happy "FUCK, yeah! I'm still buzzing about it!" with vpunch
    "I still can't believe what happened. That I managed to do that to them. And that I was this close to... to..."
    show Hiroko uniform smile_side at flip
    show Nozomi side laugh at center:
        xpos 0.75
    n "You really were amazing, Hiroko! That was so good to watch~" with dissolve
    "I can't stand this feeling. Just being around them brings the guilt of what I did to them to the forefront of my mind."
    n smile_side "That reminds me, did you apply for the scholarship yet?" with dissolve
    h uniform_headhold2 happy_closed "Sure did~ Coach helped me with it this morning." with dissolve
    "But I had to stay. I had to make sure my last programming session with them is working as I intended."
    show Hiroko smile_side
    n happy "I'm so happy for you~ Anyway, let's all enjoy our weekends, okay?" with dissolve
    show Hiroko uniform smile
    s uniform_folded smirk "With a solid two days of cramming and intensive research awaiting me? How could I not?" with dissolve
    "I think they'll be fine. None of them seem to be affected by that week I had with them, and they seem happy."
    scene bg corridor eve with blink
    stop music fadeout 10.0
    "I just need to make absolutely sure..."
    show Hiroko smile_side at center, flip:
        xpos 0.25
    show Nozomi side smile_side at center
    show Sayori smile at center:
        xpos 0.75
    ks "Uhh... e-excuse me?" with dissolve
    show Nozomi neutral
    show Sayori neutral_right
    queue music Eons
    h surprised "Huh? {w=1.0}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend frown "Aw, come on, don't shit on my day now."
    "I'll just need to say a couple things that will force them to recall their week with me. See how they handle it."
    ks sigh "This won't take long, but... N-Nozomi?"
    n front neutral "Hm?" with dissolve
    ks neutral "I was just wondering. Has your mom said anything about me?"
    n surprised "My mom?" with dissolve
    "Nozomi blinks for a moment, probably taken aback by my weird question, but starts to shuffle her foot on the floor as she finds herself answering."
    show Hiroko frown_side
    n pout_left "Well... yes, she did ask about you, actually." with dissolve
    show Sayori neutral
    h surprised_side "Wait, seriously? How's your mom know Kyou?" with dissolve
    "I watch the three of them carefully as they all start to recall that dark day."
    show Nozomi neutral_right
    s uniform_handup "He and I visited Nozomi at her house the other week. For a light study session, if I recall." with dissolve
    "So far they don't seem to be in any discomfort. I'll push a little further."
    show Hiroko surprised
    show Nozomi neutral
    ks neutral "That's right. The same day you were at my place, Hiroko. Remember?" with dissolve
    h frown "Pffth, don't talk bullshit, dude, that's..." with dissolve
    show Hiroko neutral
    "She trails off as something obviously registers in her head." with dissolve
    show Nozomi front2 neutral_left
    h uniform_headhold2 neutral "Oh wait... y-yeah, you needed my help with something big, so I... yeah, I skipped morning practice to bail you out." with dissolve
    h frown "You're welcome, by the way." with dissolve
    ks "Thanks."
    "Yeah... thanks, everyone. For confirming your final instructions all processed correctly."
    show Sayori neutral
    h irritated "But man, that was such a weird fuckin' week." with dissolve
    "You're all a little confused about what happened, sure..."
    show Hiroko frown_side
    n side neutral_side "Yes, I know what you mean. I don't really understand it myself." with dissolve
    "But it seems you've accepted everything that happened as being within the bounds of normality."
    s uniform_folded sleep "Hm... perhaps it is strange to think about, but it almost seemed like the distraction on the eve of the tournament did you some good, Hiroko." with dissolve
    show Sayori neutral
    h sleeptalk "H'yeah. I was stressin' pretty bad before that so maybe you're onto something." with dissolve

    #Need some more dialogue here about Kyou's visit to her house that she and Sayori have handwaved in their heads.
    #And something else to show Hiroko has done the same about her visits to Kyou's house.
    "These girls really will be fine. They're all going to just get on with their lives."
    show Hiroko neutral_side
    n front2 smile "Anyway Kyou, we need to get going." with dissolve
    "So I don't need to check anymore."
    show Hiroko neutral
    show Sayori neutral_right
    ks smile "S-sure. Have a good weekend." with dissolve
    n chuckle "You too." with dissolve
    scene bg street1 eve with blink
    "I can make today my last day at school."
    "I'll be able to start putting all this behind me..."
    scene bg blackscreen with longdissolve
    "And maybe one day, this dread feeling inside me will be gone..."
    jump Credits

    #Epilogue: Kyou stays in school a little longer to make sure the girls are okay, then quietly stops going to class as the guilt of what he did tears him apart.
    #Today, unknown to anyone else, is his last day as he assures himself that they're going to be fine.

label Epilogue_Con_Kyou_Nozomi:
    if ending == "friendship":
        scene bg classroom eve with longblink
        "As another school day draws to a close, I gather my things and ponder."
        play music Memories
        play sound schoolbell
        show Hiroko uniform_armup happy uniform_arm at center
        show Sayori smile at center, flip:
            xpos 0.25
        h "Hometiiime~ {font=DejaVuSans.ttf}♫{/font}" with dissolve
        s "Any plans this weekend, Hiroko?"
        h smile_side "Are you kidding? I'm back on court again; you know that!" with dissolve
        h laugh_side uniform_armup "I can't let up now!" with dissolve
        s uniform_folded "Of course. I am glad your career is moving in the right direction." with dissolve
        "It's been three months since that day."
        h "Yeah, feels great! Same to you, though~"
        s happy "Ah, thank you! It was a relief to see those results, and perhaps I can get a decent night's sleep tonight." with dissolve
        h happy no_arm "Heh, you earned it, sis!" with dissolve
        "Three months since Nozomi and I played around with hypnosis and that penlight."
        show Nozomi side smile_side at center:
            xpos 1.2
            linear 1.0 xpos 0.75
        show Sayori uniform smile
        n "Are we all set?" with dissolve
        show Hiroko smile uniform at center, flip
        h "Yep! Just waiting for..." with dissolve
        show Sayori smile_right
        show Nozomi smile
        h uniform_armup frown "Kyou! What's keeping ya?" with dissolve
        h irritated "C'mon, we're going home! Move 'yer ass!" with dissolve
        ks sigh "Yeah, yeah, I'm coming."
        stop music fadeout 2.0
        scene bg street1 eve with blink
        show Nozomi front smile at center
        show Sayori smile at center, flip:
            xpos 0.25
        show Hiroko smile at center:
            xpos 0.75
        with dissolve
        play music Peaceful fadein 2.0
        n "So did anyone catch the finale?"
        "Life has been pretty good to me since then."
        s frown "You've lost me." with dissolve
        n annoyed_left "Of that show I keep telling you all about?" with dissolve
        h smile_side "Oh yeah, I'm not caught up on that yet." with dissolve
        "Hiroko and Sayori made good on their word to \"watch\" me so I didn't try anything weird with Nozomi again."
        h uniform_armup angry_side "So you {nw}" with dissolve
        extend "BETTER not spoil!" with vpunch
        n pout "Yeah, yeah. Buzzkill." with dissolve
        show Sayori smile_right
        show Hiroko smile uniform_armup
        "And in the process we've been getting to know each other a lot more." with dissolve
        show Sayori smile
        show Nozomi neutral
        h "'Sides, why bother with TV when I can just watch Kyou make an ass of himself." with dissolve
        ks surprised "What?!"
        h uniform smirk "Dude, I saw what happened with you and Shiro today." with dissolve
        ks frown "... I don't know what you're talking about, stalker."
        h laugh "You sure? 'Cuz that face is telling me something else." with dissolve
        ks smirk "I just think it's funny how you used to keep calling me a creep for staring at people, but now you can't take your eyes off of me."
        ks "I think someone's obsessed."
        h uniform annoyed "Heh, don't flatter yourself. You know why I watch you." with dissolve
        ks "Because you looove me~"
        show Nozomi pout_left
        show Sayori rolleyes
        h uniform_armup irritated "Agh, fuck you!" with dissolve
        show Hiroko uniform frown
        show Nozomi smile
        s smile_right "Anyway, Kyou, have you given any thought to what we talked about?" with dissolve
        ks smile "Actually, yeah. I've been thinking about it and it makes a lot of sense. I'm gonna pursue it."
        n surprised "Eh? What's this?" with dissolve
        ks "Sayori suggested I look into applied psychology as something I could do for a living. I think I could pull it off."
        s happy uniform_folded "I was reluctant to encourage such a thing, given what happened, but now I do feel it is a viable career path and a good use of his talents and interests." with dissolve
        s "After all, if he can stumble upon a method to silence the hidden observer, what other breakthroughs is he capable of if he actually works with purpose?"
        n shocked "Huh! And I'm just hearing about this now?" with dissolve
        show Sayori smile
        h smirk_side uniform_arm "Well, yeah! Not like we gotta tell you everything he does~" with dissolve
        n pout "You too? Geez!" with dissolve
        ks happy "Haha, sorry Nozomi. I just didn't think to say anything."
        show Hiroko smile_side
        n smile "Oh, it's fine. And it does seem to make a lot of sense." with dissolve
        ks smile "Yeah. I think I may actually be excited about my future for a change."
        n happy uniform "Aw, that's wonderful~" with dissolve
        show Hiroko:
            linear 0.5 xpos 0.5
        show Nozomi:
            linear 0.5 xpos 0.75
        pause 0.5
        show Hiroko smile no_arm at flip
        show Nozomi side smile_side
        h uniform_armup happy_side "Alright, we're heading this way so we'll seeya both tomorrow!" with dissolve
        show Hiroko:
            xpos 0.5
        show Nozomi:
            xpos 0.75
        ks "Take care, you two."
        n "Bye for now!"
        hide Sayori
        hide Hiroko
        with dissolve
        show Nozomi:
            linear 0.5 xpos 0.5
        pause 0.5
        show Nozomi front smile
        "A moment's silence passes as Nozomi and me continue along the road home." with dissolve
        show Nozomi:
            xpos 0.5
        ks "Speaking of the future, are you excited about yours?"
        n laugh "Of course! I'm going to miss everyone like crazy, but I think we're ready to leave high school behind, don't you?" with dissolve
        show Nozomi side smile_side
        "She then casts her gaze back as we walk, towards the path Hiroko and Sayori took." with dissolve
        n "Even if I still don't know exactly what I want."
        ks smile "You'll get there. You're way too smart not to figure it out."
        ks "Just like you figured out your entrance exams in the end."
        n smile "Heh, thanks. I do hope you're right." with dissolve
        "We share a polite smile as we walk, but it's obvious that Nozomi has something else on her mind besides college."
        ks "What is it?"
        n smile_side "I'm..." with dissolve
        n front chuckle "I've started watching hypnosis videos again." with dissolve
        ks surprised "Yeah?"
        "She nods."
        n side smile_side "Mhm. Now that things have slowed down I've had some time to reflect on what we did together." with dissolve
        ks smile "That's great, Nozomi. I thought I'd ruined this for you after what happened."
        n sad_side "I honestly thought you had for a little while. Knowing how dangerous it was felt like a wake-up call." with dissolve
        n sad_closed "For a while, I couldn't even fathom wanting to be hypnotized ever again." with dissolve
        n front sleep "But the feeling did pass, and over the last few days I've started to enjoy thinking about it." with dissolve
        n front pout_left "Although I'll be avoiding anything involving lights for a bit longer..." with dissolve
        show Nozomi chuckle
        "I let out a nervous chuckle, and she responds in kind as we walk." with dissolve
        "It kinda begs the question though, but Nozomi starts to speak again before I ask it."
        n side smile_side "Do you... think you'd want to do more hypnosis with me?" with dissolve
        ks smile "Of course!"
        n laugh "Ahaha, don't sound TOO keen!" with dissolve
        n smile "But... We can start over. Without the penlight this time." with dissolve
        ks smile "Y-yeah... I was thinking we could stay away from the eyes completely."
        n surprised "Huh? Just like that, Kyou?" with dissolve
        n front teasing "It sounds like someone's been thinking about me a lot~" with dissolve
        ks sigh "H-How could I not? Don't tease me like this."
        n side laugh "Ahahaha~ S-sorry!" with dissolve
        n smile "I've been thinking about you too." with dissolve
        "As she comes to a halt I realise this is where we need to part ways."
        n blush "About \"us\", I mean." with dissolve
        ks surprised blush "Y-You have?!"
        n front sleep "Mhm... " with dissolve
        n sleeptalk "Honestly, I still don't know how to feel about you. But I don't want to make the same mistake I did with Satoshi." with dissolve
        n side sad_side "I don't want to see you gone and have any regrets." with dissolve
        n front concerned "A-and at the same time I know it's selfish of me." with dissolve
        n sleeptalk_concerned "S-so..." with dissolve
        "Gotta admit, that this is still where she's at makes my heart sink a little bit."
        "Maybe she'll never feel about me the way I feel about her."
        "But..."
        show Nozomi concerned
        ks smile "Hey, Nozo, it's okay. You don't have to commit to anything else." with dissolve
        ks "We can still be two people doing something fun together until we graduate. Maybe even past that."
        ks "I still... I'll still love you no matter what."
        show Nozomi front smile blush
        ks "So let's just do what we've been doing and take it as it comes, okay?" with dissolve
        scene cg nozomi good end 1
        show Nozomi GoodEnd1 smile
        with blink
        "Just then, I find myself warmly wrapped in Nozomi's arms as I respond in kind."
        n "Okay."
        "And for a little while we stay like that, happy to share just a few moments of uncomplicated bliss."
        n "I'll find you online after dinner. Maybe we could plan something for the weekend?"
        k "Yeah, sounds great! Looking forward to it."
        show Nozomi GoodEnd1 kiss
        "And just then I feel her lips brush gently against my cheek, just for a moment..." with dissolve
        $persistent.nozomi_good_end_1_unlock = True
        scene bg street1 eve
        show Nozomi front smile blush at center
        with blink
        "I barely have time to register what's happening before she backs away shyly, clapping her hands behind her back."
        n "You have a good evening, Kyou. I'll message you~"
        hide Nozomi with dissolve
        "And just like that, she's gone, leaving me standing by the road with my hand still on my cheek from where she kissed it."
        "But as I start walking home, I can't help but feel excited."
        "No matter what happens, I know everything's going to be alright."
        jump Credits
    elif ending == "frightened":
        jump Credits
        # scene bg classroom eve with longblink
        # "As another school day draws to a close, I gather my things and ponder."
        # play sound schoolbell
        # $nface = "sleep"; nclothes = "uniform"; nblush = False; nskin = "normal"
        # $hface = "neutral"; hclothes = "uniform"; harm = "uniform arm"
        # $sface = "neutral"; sclothes = "uniform"
        # show Nozomi at center
        # n "...{w=1.0}{nw}" with dissolve
        # hide Nozomi
        # "Did I do the right thing, just letting her go like that?" with dissolve
        # show Hiroko at center
        # show Sayori at left, flip:
        #     xpos 0.1
        # s "There she goes again..." with dissolve
        # "It's been a few weeks since that day..."
        # h "Yeah... She ever tell you what her deal is?"
        # "She doesn't acknowledge me anymore."
        # s "No. It is hard to get anything out of her lately."
        # $sface = "concerned"; sclothes = "uniform folded"
        # s "Did you hear she tried to get transferred out of this class?" with dissolve
        # "It's like she's trying to blot out my entire existence from her mind."
        # $hface = "shocked"
        # h "Wha?!" with dissolve
        # s "Yes. Clearly they turned her down, perhaps because she was as forthcoming to them as she's been to us."
        # $hface = "concerned"
        # h "Well, shit..." with dissolve
        # s "Yes. I hate seeing her in such pain."
        # h "Yeah... Anyway, let's get after her. At least we can be just, like there for her, y'know?"
        # "I don't know what to do..."
        # s "Yep."
        # hide Sayori
        # hide Hiroko
        # "I need to fix this somehow." with dissolve
        # scene bg street1 eve with fade
        # show Hiroko at right
        # show Sayori at left, flip:
        #     xpos 0.1
        # show Nozomi at center
        # "I hurry after them, and watch from a distance as the two friends catch up with Nozomi."
    elif ending == "awkward":
        scene bg classroom eve with longblink
        "As another school day draws to a close, I gather my things and ponder."
        play music Sorrow fadein 2.0
        play sound schoolbell
        show Hiroko neutral_side uniform_arm at center, flip:
            xpos 0.25
        show Nozomi side smile_side at center
        show Sayori at center:
            xpos 0.75
        s "All set?" with dissolve
        n "Sure~"
        "Why did I hurt her like that?"
        h uniform_armup smile_side "Great~ Let's get out of here!" with dissolve
        hide Nozomi
        hide Sayori
        hide Hiroko
        with dissolve
        "I simply watch as Nozomi and her friends file out of the classroom and sigh."
        "After that day, I stopped inviting Nozomi for more hypnosis sessions."
        "She still didn't understand why I wanted to stop so suddenly, but she accepted my decision."
        scene bg entrance with fade
        "After a couple weeks she stopped asking, and we drifted apart again."
        scene bg street1 eve with fade
        "And now things feel just like they were before I thought about using that damned penlight."
        scene bg k room eve with fade
        "Friendless and unlikeable, that's me. That's Kyou."
        scene bg k bedroom eve with fade
        "Maybe that's just what I deserve."
        jump Credits
    elif ending == "dark fantasy":
        #The "dark fantasy" ending is where Kyou brainwashes Nozomi into accepting Kyou's proposition to be her boyfriend, fooling himself into believing this
        #is what she wants...
        scene bg classroom eve with longdissolve
        "As another school day draws to a close, I gather my things and ponder."
        queue music Memories
        play sound schoolbell
        show Hiroko uniform neutral_side uniform_arm at center, flip
        show Sayori neutral at center, flip:
            xpos 0.25
        show Nozomi side uniform laugh blush at center:
            xpos 0.75
        n "Well, then. I hope you both have fantastic weekends~" with dissolve
        s smile "Yes... take care, Nozomi." with dissolve
        "It's been about six weeks since that day."
        h smile_side "H'yeah same to you. But, uh... Nozo?" with dissolve
        n smile_side noblush "Hm?" with dissolve
        "Six weeks since Nozomi became my girlfriend."
        show Sayori neutral
        h sad_side "Can I... like, ask you something?" with dissolve
        n surprised_side "Uh, right now? What about?" with dissolve
        "And now that another week's over we're going to spend even more time together."
        h uniform_armup sleeptalk "Man, how am I s'posed to say this..." with dissolve
        show Nozomi neutral_side
        s smirk "With a selection of words, appropriately arranged into a coherent sentence that adequately conveys the nature of your inquiry." with dissolve
        h angry vein "H'yeah, thanks, smartass." with dissolve
        "At least, as soon as we can get out of here."
        show Sayori smile
        stop music fadeout 10.0
        n sad_side "So what is it?" with dissolve
        h uniform neutral_side novein "Yeah, uh..." with dissolve
        show Sayori neutral_right
        "Restlessly standing up from my seat, I can't help but approach Nozomi's desk to see what the holdup is." with dissolve
        show Nozomi surprised
        show Hiroko neutral
        queue music Eons
        s uniform_folded "Kyou. Good afternoon." with dissolve
        n smile blush "H-hi~" with dissolve
        ks neutral "Hey, girls. What's going on?"
        h frown "Tch..." with dissolve
        "To be honest, I still don't think much of these two. But I'm done being scared of them."
        h sleeptalk "O-okay yeah, so..." with dissolve
        h neutral "How's it going, you two?" with dissolve
        n sad_side noblush "Huh?" with dissolve
        "Wait, she's asking about..."
        ks frown "Me and Nozomi? We're doing fine."
        show Sayori neutral
        show Hiroko neutral_side
        n smile_side blush "More than fine~" with dissolve
        "Not that it's any of her goddamn business."
        h sad_side blush "Cool. Cool, yeah, that's what I thought. You guys are, like, joined at the hip now, huh?" with dissolve
        n front irritated blush "Well... Yes, I suppose." with dissolve
        ks sigh "What's your point?"
        h uniform_armup irritated "Agh, I dunno. I was just... {w=1.0}{nw}" with dissolve
        $ renpy.transition(longdissolve, layer="master")
        extend surprised "w-wondering if you two wanna hang out tomorrow... or whenever?"
        show Sayori surprised
        n side surprised_side "Wh- what?!" with dissolve
        "It takes me a second to realise my mouth fell open as she said that."
        show Sayori concerned
        show Nozomi neutral_side noblush
        h uniform sleeptalk_concerned "Nozo, c'mon, we don't talk outta school anymore. You stopped yer karaoke nights, and all that other stuff, so..." with dissolve
        "Out of all the hurtful shit she's said about and to me, this has gotta be a contender for the worst."
        n sad_side "Hiroko..." with dissolve
        "It's so goddamn... she's embarrassing everyone, putting us on the spot like this."
        h sad_side "H'yeah, okay, forget about the three of us. But tell me we can hang out soon, Nozo. I miss doing shit with you." with dissolve
        show Sayori neutral_right
        show Nozomi sad
        show Hiroko sad
        ks sigh "Man, what makes you think you can make demands of her, Hiroko?" with dissolve
        h uniform_armup angry "Dude, chill. I'm just asking!" with dissolve
        n front sleep "Look, Hiroko, I appreciate that things have been a bit... different around here since I started dating, but it is what it is." with dissolve
        show Hiroko neutral_side noblush
        s uniform neutral "Different is certainly one way of putting it." with dissolve
        h irritated "It don't {nw}" with dissolve
        extend "HAVE to be like this! Why'd you wanna spend every waking second around this dude anyway?!" with vpunch
        show Nozomi irritated
        "God. Why don't you go all the way and call me a creep again while you're at it, you little turd?" with dissolve
        n side frown_side "Honestly, that's my business. Kyou and I are happy together and you just need to accept that." with dissolve
        "You just don't believe that you could be wrong about me, do you?"
        h uniform_armup furious_side vein "I'm fuckin'... {w=0.5}I'm {nw}" with dissolve
        extend "TRYING, okay? I just don't get it. I don't get you." with vpunch
        "You just can't get your head around the fact that Nozomi would break her \"no dating\" rule for a guy like me."
        show Hiroko angry
        s sleeptalk "Hiroko, I understand your frustration, but Nozomi has made it clear how she feels." with dissolve
        s uniform concerned "Their relationship is an enigma to me as well, but we are not entitled to know any more about it." with dissolve
        show Hiroko uniform novein
        ks sigh "Oh no, Hiroko got me. I'm the scary creepy dude stealing her girl away." with dissolve
        show Nozomi front shocked
        show Sayori concerned_right
        h furious blush "Th-the {nw}" with dissolve
        extend "FUCK?!" with vpunch
        "Yeah, I'm done listening to this shit."
        s uniform_folded rolleyes "Kyou, I do not think that is helpful." with dissolve
        ks frown "Yeah, well if either of you don't like seeing us together, that's your problem."
        show Sayori neutral
        show Nozomi concerned
        h angry noblush "I don't like you hanging around her every second, you fuckin' control freak!" with dissolve
        "Ignoring Hiroko's glaring bitch face, I look to my girlfriend."
        ks "Come on, Nozo. We're leaving."
        n surprised "We are? But-{w=1.0}{nw}" with dissolve
        show Nozomi entranced_talk
        stop music fadeout 5.0
        $ renpy.transition(dissolve, layer="master")
        show Hiroko surprised_side
        show Sayori uniform surprised
        if gesture == "hand":
            show Mindtrick awake wave_sleeve at center:
                xpos 0.7 ypos 0.6
            ks frown "You're leaving with me now." with dissolve
            "She'll come. I know she just wants me to be firm with her as I wave my hand in front of her face."
        elif gesture == "forehead":
            show Mindtrick awake poke_sleeve at center:
                xpos 0.7 ypos 0.6
            ks frown "You're leaving with me now." with dissolve
            "She'll come. I know she just wants me to be firm with her as I press my finger to her forehead"
        show Mindtrick entranced
        "After all, we've done this so many times before." with dissolve
        if hypnorepeat == True:
            n "{size=16}I'm leaving with you now...{/size}"
        hide Mindtrick
        show Nozomi neutral
        show Sayori uniform_folded concerned
        queue music Night_Road
        if hypnorepeat == True:
            s "Did she just..." with dissolve
        if gesture == "hand":
            h uniform_armup angry_side "Nozo? You ain't gonna let him talk to you like that, are you?" with dissolve
        elif gesture == "forehead":
            h uniform_armup angry_side "Nozo? You ain't gonna let him treat you like that, are you?" with dissolve
        n side sad_closed "I'm leaving with Kyou now. We'll talk later, okay?" with dissolve
        show Nozomi with None:
            linear 2.0 xpos 1.15
        h irritated vein "{size=16}F-fuckin'...{/size}" with dissolve
        h uniform sleeptalk novein "*sigh* H'yeah. Get outta here, you weirdos..." with dissolve
        show Hiroko sad_side
        s sleeptalk_concerned "We are always here for you, Nozomi. Please remember that." with dissolve
        stop music fadeout 10.0
        scene bg corridor eve
        show Nozomi front neutral
        with blink
        "The pair of them call out futilely as we leave at a brisk pace."
        ks sigh "Man, your friends are annoying."
        queue music Eons
        n side sad_side "They just care about me, Kyou. Even if they could never understand us." with dissolve
        ks smirk "Heh. Like they'll never understand how much you loved what I did to you just now."
        n front sleep blush "Oh, s-stop it. We're still in school." with dissolve
        ks "And?"
        scene bg entrance
        show Nozomi front pout_left blush
        with blink
        n "And I'm fine with no one else understanding thank you very much."
        "I shrug as we stop at the entrance to change our shoes."
        ks smile "As if anyone around here is gonna figure out what we're really talking about."
        show Nozomi sleep
        "Nozomi doesn't reply, instead busying herself with putting her indoor shoes back on her shelf." with dissolve
        show Nozomi surprised
        "But raising my hand close to her face quickly gets her attention again, and she lets out a little squeak of anticipation as I lean in to whisper..." with dissolve
        ks smirk "{size=16}So? Are you going to tell me or am I going to have to make you?{/size}"
        show Nozomi side sad_side
        "Nozomi's blush deepens as she bites her lip in that cute way that I've seen her do when she's turned on." with dissolve
        "She understands my \"threat\", but more than that, she knows I'm right."
        n sad "You're... r-really going to make me say it, huh?" with dissolve
        "Everyone knows we're a couple by now. Anyone watching or hearing us might think we're talking about some kind of flirtatious or outright dirty stuff, I guess..."
        "But they'll never suspect what we're really talking about, Nozomi. You know that."
        n front chuckle "... I loved what you did back there, Kyou. You know I did~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        scene bg street1 eve with blink
        "Yeah. All the hypnosis she lets me do on her, and the control she allows me to have over her. She loves it all."
        "Just living out her wild fantasy, and I'm the one letting her live it. The only one she can live it with."
        show Nozomi front smile
        "That's my girlfriend. That's Nozomi. And she's so goddamn sexy." with dissolve
        n side smile blush "So what are we doing tonight, Kyou?" with dissolve
        "So why does it feel like something's missing?"
        ks smile blush "Uh... I dunno, what do you wanna do?"
        show Nozomi front chuckle
        "Nozomi giggles." with dissolve
        n smile "I mean, my whole family's going to be home tonight and I thought you might like some peace and quiet." with dissolve
        ks smile "S-so yeah, we can hang out at my house again if you want."
        n side smile "Okay~" with dissolve
        ks "Same as... pretty much every night, I guess, haha."
        show Nozomi front happy
        "Another giggle." with dissolve
        n laugh "Ahaha, yeah~" with dissolve
        "Nozomi leans into me as we take the turn that leads to my house..."
        scene bg k house eve with blink
        "She'll want me to play with her some more, of course. Put her fully under hypnosis again, maybe give her a few more post-hypnotic commands for the night..."
        "I mean, that's what we normally do."
        scene bg k entrance eve
        show Nozomi front smile blush
        with blink
        "This is what she wants."
        show Nozomi chuckle
        "It's... it's what I want." with dissolve
        scene bg k bedroom eve with blink
        "I wanted Nozomi. And now I have Nozomi."
        scene NozomiForcedGF smile_up with blink
        "All of her. She's right here." id Epilogue_Con_Kyou_Nozomi_00e0ca94
        show NozomiForcedGF smile_down with dissolve
        "... Isn't she?"
        $persistent.forced_girlfriend_ending_unlock = True
        jump Credits
    elif ending == "quit":
        scene bg classroom eve with longdissolve
        "It's been a few weeks since that day."
        play music Memories
        show Hiroko uniform neutral_side at center
        show Sayori sleeptalk at center, flip:
            xpos 0.25
        with dissolve
        s "Mmmrrrn...."
        h smile_side "Hang in there, buddy. We got culture fest this week, case you forgot." with dissolve
        "A few weeks since Nozomi and I stopped doing hypnosis."
        s rolleyes "As if I needed reminding. I could do without the wasted time." with dissolve
        show Nozomi side smile_side at center:
            xpos 0.75
        n "I think the change of pace will do you some good, Sayori." with dissolve
        "We... well, despite my worst fears, we're still on good terms."
        s concerned "Perhaps... Anyway, study club awaits." with dissolve
        "As a matter of fact, we've even started hanging out in school together."
        s neutral_right "Have a good evening, Kyou." with dissolve
        "Even her friends are starting to warm up to me."
        show Hiroko neutral
        ks smile "You too, Sayori. Take care, girls." with dissolve
        h uniform_headhold2 sleeptalk "H'yeah, same to you, stalker. Seeya tomorrow." with dissolve
        hide Sayori
        hide Hiroko
        hide Nozomi
        "And just talking to people has gotten a little easier." with dissolve
        n "By the way, Kyou?"
        ks neutral "Hm?"
        scene TranceStopEnd unsure with blink
        "Even so..."
        n "I'm hosting a board game night on Saturday, but some of our group had to drop out. So I was wondering..."
        show TranceStopEnd smile
        n smile "Would you like to come along?" with dissolve
        "I still wonder about Nozomi and what she thinks of us."
        show TranceStopEnd happy
        n chuckle "No pressure, but there's a few people I'd like you to meet." with dissolve
        ks smile "S-sure. That sounds nice. But I wanted to ask..."
        stop music fadeout 5.0
        show TranceStopEnd smile
        n "Hm?" with dissolve
        ks neutral "How are you holding up? After... well, I mean, it's been a few weeks hasn't it?"
        show TranceStopEnd unsure
        play music Eons
        n "Yeah..." with dissolve
        "She averts her eyes from mine, as she seems to look off into the distance before she starts to speak again."
        n "Don't worry about me."
        n "It's not like... what we did... was everything I was into. You know?"
        "So she really has shut herself off from hypnosis."
        show TranceStopEnd smile
        n "Anyway, I'm dying to show you and the others this new game I bought. So you'd better be there~" with dissolve
        "And she's throwing her all into everything else."
        ks smile "I said I would, didn't I?"
        show TranceStopEnd laugh
        n "You did. And then maybe next week you want to tag along for karaoke night?" with dissolve
        "Just so she can forget about that time with me and my penlight."
        ks frown "Hard pass."
        show TranceStopEnd unsure
        n "Haah... it was worth a try." with dissolve
        "I... probably shouldn't remind her any more."
        show TranceStopEnd smile
        n side smile "Anyway... just swing by around seven and I'll introduce you to everyone. I'm sure it'll be a good time." with dissolve
        show TranceStopEnd happy
        n "You have a good evening, okay?" with dissolve
        $persistent.trance_stop_end_unlock = True
        scene bg corridor eve with blink
        "At least it's good that we're still friends. Sorta."
        "I just feel like there's something I'm missing through all of this."
        "If only things hadn't turned out... well, the way they did."
        scene bg street1 eve with blink
        "In any case, I haven't touched that penlight since we broke things off."
        "I don't think I'm so keen on hypnosis now anyway, all things considered."
        scene bg k room eve with blink
        "I only learned it for Nozomi anyway."
        "But if I don't need it now, then..."
        scene bg blackscreen with dissolve
        "Maybe I'll learn something else..."
        jump Credits    
    scene bg blackscreen with fade    

label Epilogue_Con_Kyou_Nozomi_Trance_Abuse:
    "A lot has happened since that day."
    queue music Cafe
    scene bg classroom day with longdissolve
    # "For starters... well, we made sure that experience never really stopped."
    show Hiroko maid smile_side at center, flip:
        xpos 0.75
    with dissolve
    h "Here's your coffee, sir. Thanks for coming to our class café."
    "The day I gave Nozomi the darkest, most erotic experience of her life was the day both our lives changed forever."
    hide Hiroko with dissolve
    "It's certainly spiced up our lives around school, that's for sure."
    show Sayori maid smile at center, flip:
            xpos 0.25
    s "So that is two milk teas and a piece of strawberry shortcake. Can I get you two anything else?" with dissolve
    "Take today, for example. Today's the day of our annual school culture festival."
    hide Sayori with dissolve
    "Every year our class runs a maid and butler café for the event, so we all dress up and serve simple drinks and snacks for the visiting parents and other locals."
    "Well, I say we \"all\" dress up..."
    "In truth, most of us guys wuss out and take a sick day, or we vote each other for kitchen and cleaning duty while the girls get suckered into waiting tables."
    h "Here we go, ma'am, this table's free."
    "That's why I'm here at the back of the classroom, which has been sectioned off from the rest of the place so we can do food prep."
    h "Uhhh... wait a sec, lemme get you a menu."
    "It's been a busy morning, but now I'm caught up on plating the food orders I can look up from my station and watch one of the maids working the tables across from me..."
    # "It's been a busy morning, but now I'm caught up on plating the food orders I can turn my attention back towards the business area, as I look to the maid on the other side of the room..."
    show Nozomi side maid neutral_side at center, flip:
        xpos 0.25
    with longdissolve
    "... My maid, of course."
    h "Hey, you! Quit spacin' out."
    "Seeing Nozomi in that outfit has brought a smile on my face every year she's worn it."
    n sad_side "U-uh, what?" with dissolve
    "Of course this year was going to be difficult for her, especially now that we've gone public with our... relationship."
    # "We knew she was going to have a hard time of it this year, now that we've gone public with our... relationship."
    show Hiroko maid frown_side at center with dissolve
    h "Table three's missing a menu card. Weren't you s'posed to be on top of that?"
    "She avoids the other girls in class these days, and the girls avoid her. Mostly."
    # "She wanted to take a sick day herself, to tell the truth. But she knows it's not for her to decide any more."
    n neutral_side "Oh? I was sure I put one out for every table." with dissolve
    # n neutral_side "Oh? I guess one of the customers must have walked away with it; I'm sure I put one out for every table." with dissolve
    # "After all, since that night she's been ready and eager to continue on from that wild, passionate night. As my mind-controlled \"slave\"."
    "Yeah, today was always going to be trouble."
    h maid_headhold2 confused_side "Yeah, so? I'm saying it ain't there now." with dissolve
    "Just gotta get through it, Nozomi..."
    n sad_closed "Ahh. One of the other customers must have walked off with it." with dissolve
    show Nozomi neutral_side
    h irritated "I don't give a shit!" with dissolve
    h angry_side "What, you need me to tell you what to do around here, or do you only take orders from that other creep?" with dissolve
    n sad_side blush "H-Hiroko, p-please don't start..." with dissolve
    show Sayori maid_handup frown at center:
        xpos 0.75
    s "What on earth is going on here? Do you not realize how bad this looks for all of us?" with dissolve
    n sad_closed "S-sorry... i-it's about... the menus..." with dissolve
    show Hiroko frown_side
    s maid_folded irritated "We printed spares. The boys will have them in their area; go ask them." with dissolve
    hide Nozomi
    show Nozomi front2 maid sleeptalk_concerned blush at center:
        xpos 0.25
    n "Right... r-right away. Sorry." with dissolve
    hide Nozomi with dissolve
    "Man, that was not a fun thing to witness. Guess I'd better find those menus they were talking about."
    show Hiroko frown
    s frown "And Hiroko, how about you take over as greeter? Perhaps you'll be able to keep away from each other, for everyone's sake." with dissolve
    show Hiroko maid frown_side at flip
    h "Ugh. F... fine, whatever. Didn't wanna talk to that lyin' b-word anyhow." with dissolve
    hide Sayori
    hide Hiroko
    with dissolve
    "And while she's got a reason to approach me, maybe I can lift her spirits in the way only I can..."
    show Nozomi front2 maid concerned at center
    n "Hey Kyou, I..." with dissolve
    ks smile "That outfit really suits you, you know."
    show Nozomi side sad_closed blush
    "She looks away from me in that bashful way she's started doing whenever I compliment her. Which only makes her more delectable in my eyes." with dissolve
    n smile_side "O-oh... thank you, but I really need to..." with dissolve
    ks "You should talk to Mr. Kobayashi about letting you borrow it after we're done today. I think I'll get a real kick out of you wearing it at my house tonight."
    n front2 surprised "You.. w-want me to..." with dissolve
    "Yeah, I know. They're school property and if Kobayashi knew what I mean to do with her while she's wearing it he'd go apeshit on us, but..."
    n "W-we couldn't possibly..."
    if gesture == "hand":
        show Mindtrick awake wave_sleeve at center:
            ypos 0.6
        with dissolve
    elif gesture == "forehead":
        show Mindtrick awake poke_sleeve at center:
            ypos 0.6
        with dissolve
    "Damn, I really want her to try."
    ks "You'll do as I say."
    show Mindtrick entranced
    if hypnorepeat == True:
        n "{size=16}I'll do as you say...{/size}" with dissolve
    else:
        with dissolve
    "And I know how much it gives her life to do my bidding, no matter how shameful I get with her these days."
    show Nozomi entranced_talk
    hide Mindtrick
    ks "Just tell him you want to take some souvenir photos of it at home or something." with dissolve
    show Nozomi smile
    ks "It's our last year of doing this after all, so maybe he'll see it your way." with dissolve
    n side happy "Ehehehe... o-okay, I'll ask him as soon as I can~" with dissolve
    ks "That's my girl. Oh, and... Nozomi?"
    n smile "Yes, Kyou?" with dissolve
    "I grin as I tap a menu card against the back of her hand."
    ks smirk "You better get back to work before they yell at you again."
    show Nozomi front2 loving
    "Suddenly reminded why she came to me in the first place, Nozomi skittishly takes it from me and immediately tries to cover her face with it." with dissolve
    n "E-ehehe thank you, sir. I-I'll do my best~ {font=DejaVuSans.ttf}♥{/font}"
    hide Nozomi
    "And with that she scuttles merrily away, still holding the menu to her face as the shade of crimson on her cheeks seems to get even darker." with dissolve
    "That little show got a chuckle out of the guys around me. And if I have to guess, more than a few envious looks in my direction."
    "No one can understand how me and Nozomi wound up as this school's weirdest couple. No one gets us at all."
    "But that's okay. Right, Nozomi?"
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "So long as we have each other, everything will be okay."
    pause 1.0
    scene bg classroom day with longdissolve
    queue music Eons
    "Before too long the morning rush of customers to our café gives way to a more sedate afternoon."
    "People are still coming in here for treats, but most are out exploring the other classrooms and the various attractions put out by the students within."
    "And that means some of us staffing this place have been taking breaks to go explore for themselves."
    show Nozomi side maid smile_side at center, flip:
        xpos 0.75
    n "Thank you very much for visiting our class café~" with dissolve
    "Leaving the rest of us to keep things ticking over until they return to relieve us."
    show Hiroko maid frown_side at center:
        xpos 1.5
        linear 3.0 xpos 0.4
    n happy "We're open until four, so be sure to stop by...{w=1.0}{nw}" with dissolve
    hide Hiroko
    $ renpy.transition(dissolve, layer="master")
    extend neutral " a-again."
    "They're a little late coming back, but at least they're here now. I was getting bored trying to look busy around here."
    show Nozomi sad_closed
    "With a nod to my co-workers, I slip away from my post and sneak up behind Nozomi, distracted as she is, before I..." with dissolve
    n shocked blush "E-eep!" with vpunch
    if hypno4 == "tickle":
        "... Give her ribs a sly tickling from over her maid costume."
        n laugh "E-ehehee~" with dissolve
    elif hypno4 == "spank":
        "... Give her cute little tush a discreet pinch."
        n happy "Mmmmn~" with dissolve
    ks smile "Hey, you ready to go?"
    if hypno4 == "tickle":
        "I'd have gone in on her harder but, well, there's too many people around. Maybe later."
    elif hypno4 == "spank":
        "I'd have gone under her skirt but, well, there's too many people around. Maybe later."
    n smile "J-just a moment, please. We need someone to take over from me." with dissolve
    hide Nozomi
    show Nozomi front2 maid loving blush at center:
        xpos 0.75
    n "And then, I'll.. I'll be all yours again, Mr. Koyama..." with dissolve
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "So before too long I'm leading my insatiably kinky girlfriend out to catch the other sights of the festival."
    "Although to be honest, I quickly became bored with these second-rate stalls the other classes put out to showcase their talent."
    "Nozomi seems to feel the same. But to be fair, everything seems boring when we compare it to what we have now."
    scene bg school side day with dissolve
    play music Park
    "We've both become far too addicted to each other's company, and to what we can do whenever we're allowed some alone time..."
    ks smile "This should be far enough. I don't think anyone's going to bother us for a while if we stay here."
    show Nozomi side maid smile_side blush at center
    "My partner in crime nods demurely as we wander out to a secluded side of the school building, away from the general festivities taking place all around us." with dissolve
    n neutral_side -blush "Y-yes, I... I-I hope so." with dissolve
    "Although as we settle, I can see her face start to drop."
    n sad_side "I really needed to be away from... all of that. At least for a while." with dissolve
    "And it doesn't take a genius to know what's getting her down."
    n sad "I'm sorry, I just couldn't help thinking about Hiroko, and Sayori and... and the other girls." with dissolve
    n front concerned "I knew it wouldn't be easy being yours, but I still wasn't prepared for how much they'd all hate me." with dissolve
    ks sigh "Look, Nozo, I've had people calling me stuff behind my back the whole time I've been here. You get used to it."
    n sleeptalk_concerned "I-I know... I'm sorry to even bring it up." with dissolve
    n neutral_left "And besides, after we graduate I'll never have to see them again." with dissolve
    n sleeptalk "It's not like we're going to start college, after all. Not any more." with dissolve
    "She's right. We sure aren't getting our grades back up in time for the real entrance exams, that's for sure."
    n smile "So I guess I really am all yours now, Mr. Koyama. Mind, body and soul." with dissolve
    "Dad's gonna be furious when he finds out. He'll probably kick me out of the house, and then what will I do?"
    n happy "I don't have to worry about my future when I have you to decide for me... ehehehe~" with dissolve
    "Maybe I can crash at Nozomi's house for a while... her mom seems to like me, although we'd have to be more discreet with our hypno play..."
    n chuckle "So forget what I said. It doesn't matter any more." with dissolve
    "... Ugh, whatever. I'll cross that bridge when we get to it."
    ks smirk "Already forgotten. Now let's get back to the fun stuff."
    scene TranceAbuseEnd smile with blink
    "Right now I just want to enjoy the hell out of this beautiful girl, and all the kinky fantasies we can indulge with each other."
    show TranceAbuseEnd shy_left
    n side smile_side "Mmmn, speaking of fun stuff... and forgetting..." with dissolve
    ks smirk "Oh, you are going to tell me what you're thinking right this instant."
    show TranceAbuseEnd shy blush
    stop music fadeout 5.0
    "I can feel as much as I can see Nozomi trembling in pleasure as I speak to her with assured authority." with dissolve
    n "I'm thinking... w-when we get home tonight, you could hypnotize me into forgetting everything about us."
    ks confused "Oh?"
    queue music Dark_Piano
    show TranceAbuseEnd shy_left
    n side smile_side "Yeah, just... flash that light of yours in my eyes and take me so deep that I barely even know who you are." with dissolve
    "I'm confused, but I know that dirty little mind of hers has something hot going on..."
    show TranceAbuseEnd shy blush hand
    "... So as I reach up to stroke her red hot cheek I smirk encouragingly..." with dissolve
    ks smirk blush "... Keep talking."
    n "Th-then, you could tie me up again while I'm still in trance. With more hypnosis, or those ropes you bought the other day."
    show TranceAbuseEnd excited
    n loving "And then... I-I want you to wake me up and do your worst." with dissolve
    "Heh. Now I understand. She wants me to..."
    n "Tell me I'm your helpless captive. Torture me like I'm nothing to you."
    show TranceAbuseEnd smirk
    n smirk "Use all my triggers and play all you want with my body, no matter how much I scream and beg. Don't hold anything back." with dissolve
    n "I want to feel like I did the night you first claimed me. I want to feel so, so powerless. So completely, irresistably helpless before your ultimate control over my mind."
    show TranceAbuseEnd manic
    n laugh "Break me, Mr. Koyama. Hahahaha." with dissolve
    "Damn, she is making me so hard talking like that. And who am I to deny her?"
    show TranceAbuseEnd perverted nozomi_hand
    n smirk "Break me... a-again." with dissolve
    n "Please."
    "Fuck what anyone else thinks about us. Hell, fuck anything else in this world; this girl gives me life."
    "She completes me, and I complete her."
    $persistent.trance_abuse_end_unlock = True
    scene bg blackscreen with longdissolve
    "We'll never let each other go..."
    jump Credits

label Epilogue_Con_Kyou_Nozomi_Zombie:
    if ending == "broke penlight":
        "A lot has happened since that day."
        scene bg classroom day
        queue music Cafe
        show Hiroko maid smile_side at center, flip:
            xpos 0.75
        with longdissolve
        h "Here's your coffee, sir. Thanks for coming to our class café!"
        hide Hiroko with dissolve
        "Although one thing that didn't happen was our hypnosis show, which is why on the day of the culture fest we're all here serving drinks and snacks in our classroom..."
        show Nozomi side maid smile_side at center, flip:
            xpos 0.75
        n "Welcome! Please take a seat wherever you like~" with dissolve
        hide Nozomi with dissolve
        "Our classroom having been transformed into a simple café for other students, parents and the occasional visiting member of the public."
        $t = "Customer"
        t "Hey, did you hear me?"
        ks butler confused "H-huh? Hear what?"
        "Right. A classroom café that me and most of my class got roped into helping with. And I'm supposed to be waiting tables right now."
        t "I said I wanted a milk tea! And some lemon cake."
        ks sigh "Oh... r-right, sorry."
        show Sayori maid_folded smirk_right at center, flip:
            xpos 0.25
        s "Please excuse him, ma'am. This is his first day." with dissolve
        ks frown "Ugh..."
        s maid_handup "Service with a smile, Kyou." with dissolve
        ks smile blush "Uh, I-I mean, coming right up, ma'am!"
        scene cg school cafe with longblink
        "And that's how the day went, as we all saw to a busy lunch hour."
        "It's not like we haven't done the school café thing before. Actually our class has done this for the third year in a row."
        "But this time does feel different. Maybe because I'm out here talking to the customers this time instead of hiding in the back room."
        "Maybe because I know me and Nozomi had a chance to do something better."
        "Or maybe it's because this will be the last time we all take part in a school culture fest together..."
        "I'm not sure how I feel about it all."
        $persistent.school_cafe_1_unlock = True
        scene bg classroom day
        show Hiroko maid happy at center, flip:
            xpos 0.75
        with longblink
        h "Thanks for coming to our class café! Have a great day!"
        show Nozomi side maid smile_side at center, flip
        n "I think we can relax a little now, Hiroko. The crowd's started to thin." with dissolve
        hide Hiroko
        show Hiroko maid sleeptalk at center:
            xpos 0.75
        show Nozomi neutral_side
        h "Oh, thank fuck. I think my cheeks are gonna fall off." with dissolve
        show Sayori maid neutral at center, flip:
            xpos 0.25
        show Nozomi sad_side
        s "That is a little TOO relaxed, Hiroko. Especially given our current clientele." with dissolve
        h scared_side blush "{cps=15}Ahh, I-I was just sayin'... {w=0.5} u-uh, {/cps}{nw}" with dissolve
        $ renpy.transition(dissolve, layer="master")
        extend maid_headhold2 happy_closed "it sure is great our class voted to do a maid an' butler café for culture fest again! I LOVE serving customers 'n' stuff~"
        h happy "Good job, class! Love all of ya!" with dissolve
        s maid_handup smirk "There we go. I could not have said it any better myself." with dissolve
        h "{size=16}... Fuckin' kill me.{/size}"
        hide Nozomi
        show Nozomi front2 maid neutral at center
        show Sayori neutral_right
        show Hiroko neutral
        ks butler sigh "Oh yeah, I can't believe I've missed out on all this fun before, waiting tables with you guys." with dissolve
        show Hiroko neutral_side noblush
        show Nozomi neutral_left
        s maid_folded frown "\"Guys\" he says." with dissolve
        "Right. Most of the dudes in our class voted for this, then elected themselves for kitchen and cleaning duty while the girls got cajoled into dressing up. Just like before."
        "I'm almost single-handedly upholding the \"butler\" theme here."
        show Nozomi neutral
        show Sayori neutral_right
        show Hiroko neutral
        ks frown "Okay, bad choice of words on my part." with dissolve
        h maid sleeptalk "Eh, well it's cool you stepped up anyhow." with dissolve
        show Hiroko neutral
        ks smile "S-sure... no problem. I mean, it's only fair after the other week, right?" with dissolve
        show Sayori maid neutral
        show Nozomi neutral_right
        h smile "Heh, damn right it is~" with dissolve
        h maid_headhold nervous "And... ehh, I'm jus' gonna say it." with dissolve
        ks neutral "Hm? Say what?"
        h sad "It's a damn shame we couldn't make that hypnosis show work." with dissolve
        show Nozomi surprised_side at flip
        show Sayori concerned
        n side maid surprised_side "H-huh?" with dissolve
        h sleeptalk "H'yeah, like... don't get me wrong or anything, I still think the hypno stuff's a lil'... like, weird an' freaky." with dissolve
        h maid_headhold2 neutral_side "But I dunno. It ain't every night we all get to hang out and have some fun. Y'know?" with dissolve
        show Hiroko maid sad noblush
        show Sayori maid_folded sleep
        show Nozomi neutral_side
        "For a moment, no one says a word as the clinking of cups and plates fills our silence." with dissolve
        show Nozomi neutral
        show Hiroko sad_side
        s concerned "Well, for what it is worth I happen to agree." with dissolve
        hide Nozomi
        show Nozomi side maid surprised_side at center
        show Hiroko surprised_side
        n "Y-you do?!" with dissolve
        "Sayori looks to Nozomi, and seems to think carefully about her next words."
        s maid neutral "It did not seem appropriate to mention it at the time, after what happened to your mother." with dissolve
        show Nozomi neutral_side
        show Hiroko neutral_side
        s neutral_right "And of course we have all been busy since then with our preparations for exams and..." with dissolve
        show Sayori maid_folded rolleyes
        "She sighs and gestures around her." with dissolve
        s "Well... this. So I have not had an opportune moment to comment before now."
        s neutral_right "But I will admit I was impressed that the three of you were able to come together, set aside your differences and put on an entertaining and thought-provoking performance." with dissolve
        s concerned "And you put it together at such short notice. If you had only allowed yourselves the proper time to prepare I daresay you would have made something very special." with dissolve
        n sad_side "You really think so?" with dissolve
        s maid_handup smile "Of course. Now, I believe our services are going to be needed again in short order." with dissolve
        show Hiroko frown_side at flip
        show Nozomi neutral_side at flip
        "She points, and the rest of us look to see a queue forming by the doors of our classroom." with dissolve
        h maid_armup irritated "Ugh, yeah. That's fu-... fudging great." with dissolve
        show Hiroko neutral
        show Sayori neutral_right
        show Nozomi neutral
        ks sigh "Do you guys wanna take a break? I can handle this." with dissolve
        show Nozomi neutral_side
        h maid_headhold2 nervous "For real? Don't gimme hope like that, dude." with dissolve
        hide Nozomi
        show Nozomi front maid sleeptalk at center
        n "Well, we do need to start thinking about breaks now that you mention it, Kyou." with dissolve
        show Nozomi neutral_left
        hide Hiroko
        show Hiroko maid_headhold2 neutral_side at center:
            xpos 0.75
        s smirk "We do. So if you don't mind I would like to go first. And I propose Hiroko join me, if only to rest her poor abused facial muscles." with dissolve
        show Nozomi neutral_right
        h maid_armup irritated "P'feh!" with dissolve
        h nervous_side "But yeah, I owe you guys." with dissolve
        scene bg blackscreen with dissolve
        "So the pair of them head out to enjoy the rest of the festival while Nozomi and I hold the fort with some others in the classroom."
        scene bg classroom day with dissolve
        "The new visitors keep us busy for a few minutes, but business really has died down since the morning."
        "I'm sure people are way more interested in the exhibits and attractions the other classes are putting on than what we're doing."
        n "So, er... Kyou?"
        ks butler neutral "Hm?"
        show Nozomi front2 maid neutral at center
        with dissolve
        "But I realize I'm spacing out again as I hear Nozomi address me from behind."
        n concerned "I just wanted to ask how you've been?" with dissolve
        ks neutral "Oh... yeah, good I guess. Just going through the motions, you know?"
        show Nozomi chuckle
        "Nozomi lets out a little chuckle." with dissolve
        n side smile "Yeah. I know what you mean." with dissolve
        ks sigh "Sucks that we've been so busy, huh. What with the culture fest and the exams, I hardly get to talk to you guys."
        n front teasing "Story of your life, huh." with dissolve
        ks frown "Aw, come on. Don't be like that."
        n front2 laugh "Ahaha~ You know I'm teasing." with dissolve
        "She grins at me, and she knows only too well that I can't really get mad at her."
        "But I can get even..."
        ks smirk "Sure. But I think that next customer's yours."
        n neutral_right "Hm? {w=1.0}{nw}" with dissolve
        show Nozomi side laugh at flip
        $ renpy.transition(longdissolve, layer="master")
        extend "O-oh, uh... welcome! Please take a seat wherever you like~"
        "Just as she's about to attend to our latest guest, she stops in her tracks for a moment and looks back at me."
        n smile "... Let's go look at the festival together when our friends are back, okay?" with dissolve
        stop music fadeout 5.0
        scene bg blackscreen with longdissolve
        "Sayori and Hiroko returned to relieve us before too long, both of them grateful for a more subdued café atmosphere compared to the busy morning we just had."
        "So I spent a little time with Nozomi looking at the attractions the rest of the school put on for the festival."
        scene bg school outdoors day
        show Nozomi front2 maid smile at center
        with dissolve
        "But before it was time to head back we found ourselves outside, away from most of the hustle and bustle of the main event."
        queue music Peaceful
        ks butler sigh "Man, it feels weird to be out dressed like this."
        n pout "It's all part of the festival, Kyou. You get used to it." with dissolve
        "I'm not so sure about that, to be honest. But I have more important things on my mind."
        show Nozomi neutral
        "Things that I suspect are on Nozomi's mind as well." with dissolve
        n side neutral_side "So... that hypnosis show we did really left an impression, didn't it." with dissolve
        ks neutral "Yeah. You want to talk about it?"
        "She nods."
        n sad_side "I mean, I've barely been able to stop thinking about it." with dissolve
        n sad "Just the thought that you had a device that we were sure could put me or anybody else into a hypnotic state with ease." with dissolve
        n front2 concerned "And you could use it to plant all sorts of crazy suggestions in our heads that we'd feel compelled to follow, no matter what." with dissolve
        n sleeptalk "I know what we promised each other, and... and I know you were true to your word, Kyou. I don't think you ever abused what you had." with dissolve
        n surprised "But what if you DID abuse it? What was stopping you from doing whatever you wanted with that thing?" with dissolve
        n side sad_side "Everyone's been so supportive of what we did back then. Mom, Sayori... even Hiroko. But the fact is I put them all in danger and they have no idea." with dissolve
        n sad_closed "And the shameful truth is, it's not like I wasn't thinking about any of this at the time." with dissolve
        n front2 sleeptalk_concerned "There was a part of me that was getting excited at the thought you might betray me. Might turn that light of yours on me and everyone else and..." with dissolve
        ks surprised "A-and? And what?"
        show Nozomi blush
        "She blushes as she averts her eyes. And I guess I'm not gonna get a solid answer to that." with dissolve
        n neutral noblush "I'm just so disgusted with myself, Kyou." with dissolve
        "So she's still beating herself up about what could have happened, huh?"
        ks sigh "Nozomi, that's..."
        n sleeptalk_concerned "I just don't know what's wrong with me." with dissolve
        "She needs to know she doesn't have to feel this way."
        ks smile "Nozo, nothing's wrong with you, okay?"
        show Nozomi concerned
        ks "That penlight... I still don't know how it happened. And after I broke it, I don't think we'll ever know." with dissolve
        ks "It was such a freaky, totally unexpected thing that it'd be weird if we didn't get tempted by what it could do for us."
        ks "But we came out of it, didn't we? That thing's gone, it's never coming back, and... well, we're still here!"
        ks "We know what hypnosis is supposed to be like. And I think so does your mom, and your friends."
        ks "So please don't be too hard on yourself now. I couldn't bear it if I ruined hypnosis for you."
        show Nozomi side sad_side
        n "..." with dissolve
        n sad_closed "I don't think you ruined it for me, Kyou. I think I might have ruined it for myself." with dissolve
        n front sleeptalk_concerned "After everything that happened, I think the love I had for it might actually be gone." with dissolve
        ks smirk "Are you sure that's true, Nozomi?"
        n neutral "Why wouldn't it be true?" with dissolve
        "Yeah, what happened is still getting her down, but from what we've been through together I have a good feeling she'll appreciate what I'm about to do for her."
        ks smile "Well, here's a way to find out for sure. Put your hands together like this."
        show Nozomi front2 frown
        "I hold my hands together in front of me and Nozomi, after a pause, starts to mimic me." with dissolve
        ks "Now hold them up in front of your face and extend your pointer fingers out, nice and straight."
        scene ZombieEnding1 kyou k_smile point fingers_apart nozomi1 n_irritated with blink
        n "... I don't know what this is supposed to prove."
        k "You know you can stop this at any time. You can certainly try to. Or you might find yourself staring at that space in-between your fingers. Right here where I'm pointing."
        show ZombieEnding1 n_frown
        "Nozomi's eyes turn to focus on the spot between her pointed fingers. And immediately I start to take the finger I pointed with and begin to circle it around her hands." with dissolve
        k "You can try to pull your eyes away, or you may now find a growing force pushing your fingertips towards each other. Pushing harder and harder."
        show ZombieEnding1 n_straining blush1
        $ renpy.transition(longdissolve, layer="master")
        n "Mmn..."
        "My finger continues to circle, while Nozomi's start to quiver as she stares intently."
        "She knows what I'm doing, and she knows she can stop playing this game with me any time she likes. I don't have that penlight anymore."
        "And yet, in spite of that..."
        show ZombieEnding1 fingers_closing
        $ renpy.transition(longdissolve, layer="master")
        k "That force becoming more and more powerful, pushing those fingertips of yours closer and closer..."
        "Nozomi is finding she wants this after all."
        hide ZombieEnding1
        show ZombieEnding1 kyou k_neutral rest fingers_closing nozomi1 n_focused
        $ renpy.transition(longdissolve, layer="master")
        k "And you can try to resist. You can try to pull your fingers away, but the more you try, the stronger the force becomes."
        k "The more you try, the stronger it becomes and the deeper you'll fall into hypnosis the moment they touch."
        show ZombieEnding1 fingers_touch
        $ renpy.transition(longdissolve, layer="master")
        k "{cps=20}Keeping your feet planted firmly on the ground, staying perfectly upright even when your fingertips touch... {/cps}{w=1.0}and {nw}"
        show ZombieEnding1 snap
        play sound fingersnap
        $ renpy.transition(longdissolve, layer="master")
        extend "sleep!"
        show ZombieEnding1 n_relaxed
        $ renpy.transition(longdissolve, layer="master")
        "I snap my fingers just as Nozomi helplessly touches her tips together, and man am I happy that worked."
        hide ZombieEnding1
        show ZombieEnding1 kyou rest k_neutral nozomi2 n_sleep
        $ renpy.transition(longdissolve, layer="master")
        k "Going deeper into this pleasant state of hypnotic trance. Allowing yourself to enjoy this feeling, allowing yourself to relax all the way while staying nice and upright."
        "It was a simple hypnotic induction, of course. So simple even Hiroko could do it."
        k "Because you do enjoy this, don't you, Nozomi?"
        show ZombieEnding1 n_sleeptalk
        n sleeptalk "{size=16}Ye... y-yeah...{/size}" with dissolve
        show ZombieEnding1 n_sleep
        "But it's all I needed to show Nozomi that her love of hypnosis is as strong as ever." with dissolve
        k "Of course you do. And when I count up to three and snap my fingers you're going to wake up from this trance, happy and refreshed."
        k "And what's more, when we arrive back in class and until it's time to close the café you're going to become the best maid this school has ever seen."
        show ZombieEnding1 k_smile
        k "You'll be friendly, happy and eager to help our customers so they'll all leave with smiles on their faces. Okay?" with dissolve
        show ZombieEnding1 n_sleeptalk
        n sleeptalk "Okay..." with dissolve
        show ZombieEnding1 n_sleep
        k "{cps=15}One, two, three, and {/cps}{nw}" with dissolve
        show ZombieEnding1 snap n_waking
        play sound fingersnap
        $ renpy.transition(dissolve, layer="master")
        extend "wide awake!"
        show ZombieEnding1 rest
        $ renpy.transition(dissolve, layer="master")
        "Nozomi lets her eyelids open slowly as I step back and watch her in the autumn sun."
        show ZombieEnding1 nozomi3 n_surprised
        $ renpy.transition(dissolve, layer="master")
        "It's only just now I realize it's been a while since I thought this... but she really is beautiful."
        "I guess that's weird. But after all this time I've really just liked that we've been able to hang out together like this."
        show ZombieEnding1 n_smile
        $ renpy.transition(dissolve, layer="master")
        "And it sure feels amazing, being able to put that smile on her face."
        show ZombieEnding1 blush3
        $ renpy.transition(dissolve, layer="master")
        n "S-so, I guess we should head back now, huh?"
        show ZombieEnding1 k_laugh
        $ renpy.transition(dissolve, layer="master")
        k "Yeah. The class needs its star maid back."
        show ZombieEnding1 n_laugh
        n "Ahahaha~" with dissolve
        show ZombieEnding1 n_happy
        n smile "Well... w-we'll see about that~" with dissolve
        hide ZombieEnding1
        show ZombieEnding1
        "She walks with a spring back in her step as she heads back inside." with dissolve
        "And as I follow behind her, I have a feeling this afternoon's gonna be a lot more fun for everyone."
        $persistent.zombie_ending_1_unlock = True
        scene bg blackscreen with dissolve
        "May we have many more days like this..."
        jump Credits
        # ks "Nothing's ruined. You're fine; everything's fine."


        #Nozo thanks Kyou for his kind words, but thinks the spark might have gone. Kyou does a little hypno on her right there to convince her otherwise






        # Nozo does some hand wringing about being tempted by the penlight and putting herself and everyone at the mercy of Kyou, who has nevertheless proved trustworthy but it could've so not been the case
        # But hey, you're cool now Kyou so let's be hypno buddies!



        #Urgh, I think it's a little implausible that these guys are all now getting on despite apparently having had no time to talk amongst themselves
        #I think instead Nozomi's specifically ready to talk about what happened before, after having needed time to process things
        #Can we work some more maid/butler stuff into this convo?



        # n "Mom and I talked a lot after our


        # n "Obviously I was a bit shaken up after our show. It was hard not to think about how things could have been so much worse."
        #
        # n "But everyone's been so supportive. Mom, Sayori... even Hiroko."
        #
        #


        # show Nozomi neutral
        # ks smirk "Eh, well it's our last one of these so I guess I won't have to, huh." with dissolve
        # n chuckle "I suppose. Although if you ask me, I think you missed out." with dissolve
        # "I smile and shrug at her."
        # show Nozomi smile
        # ks smile "Yeah, maybe. It's been nice this year; getting to hang out with you guys." with dissolve
        #
        #
        # ks "Hmm..."
        # ks smile "Missing out on spending them with you? I guess I did."
        # ks neutral "Yeah..." #Maybe add something to say he regrets not being able to share more school festivals with her instead of this one time


# "As they head outside, we'll probably hear a little bit about what happened after the botched show."
# "Atsuko is probably doing okay now and all is pretty much forgiven on that front."
# "As for the relationship between Kyou and Nozomi, we're likely going down a similar path as the original ending to Nozomi's Trance storyline."
# "In that version, Nozomi's revealed to be thinking about going back to hypnosis again, carefully, as it seems she's still as kinky for it as ever."
# "She and Kyou seem to be friends, and it's clear his growing confidence in social situations has made him more approachable to the girls in his class."
# "He has his sights on one of them and Nozomi encourages him to ask her out. He promises to go for it once they're done with business today."
# hide Nozomi
# "Nozomi's looking forward to finding out what happens, but for now they should start heading back and she walks on ahead." with dissolve
# "Kyou doesn't immediately follow, instead thinking to himself life is a lot better now than it was when he started his penlight adventure."
# "And that's it! That's the end :D"
# "So! Things have developed a fair bit since last month, with the newly-written script mostly following what was outlined before."
# # "That suggestion made to Nozomi's mum is still the main sticking point. Hopefully I'll have it worked out soon."
# # "Also, it seems I'm gonna commit to setting the epilogue during the culture fest school café, which could lead to a couple of fun CGs..."
# # "A few plotholes? Some OOC moments maybe? As ever, I'm interested to know your thoughts, readers!"
# #Like Nozomi's seeming abandonment of her embarrassment about hypnosis."
# # "Or the relative recklessness with which she and Kyou have gone about testing the penlight to prove it's safe to play with..."
# "Thanks for reading this far! As always, feedback will be read and appreciated, and I'll be trying (again) to get this script wrapped up in time for the next release."
# "And now, the credits!"


        # show Nozomi neutral
        # ks "I missed out on a lot of things, huh." with dissolve
        # show Nozomi side neutral_side
        # "Nozomi doesn't say anything right away, but I notice her nod her head just a little before her lips begin to part." with dissolve
        # n "Well, let's not beat ourselves up about our regrets, okay?"
        # n "I've been trying to forgive myself for what happened at our show."
        #
        #
        # n "Yeah... you and me both."
        # ks "Hm?"
        # n "I mean, if I wasn't so uptight about people knowing I was into hypnosis..."
        #
        #
        # n "Well, let's not beat ourselves up about our regrets, okay?"
        # n "It really is a shame that we couldn't meet like this sooner."
        #
        # n "I'm just happy we can be here now. In this moment."
        # n "And I think I can let myself enjoy hypnosis again~"
        #
        #
        # n "And I know the others are happy to meet you at last, Kyou."
        #
        #
        #
        #
        # n "It's just... I guess I was too caught up in everything to realize it at the time."
        # n "I was so worried about what people would think if they knew I was into hypnosis. So I kept that part of me tightly locked within myself."
        # n sad "But then out of nowhere you opened up to me. Just a little."


        # n sad_side "I mean, I know you were always there, but that time it was different. You opened yourself up, just a little."

        # n "I was so afraid about people discovering my interest in hypnosis."
        # n "Mom, Hiroko, Sayori..."

        # n "Mom, Hiroko, Sayori... I was so afraid how everyone would react to me wanting to get involved in a hypnosis act. Let alone with a boy we all thought was..."
        # n "Well..."
        # ks sigh "Creepy."
        # n "Yeah..."
        # ks "I know
        # n "And sure, it was a little awkward, .

        # n "But in spite of everything, it all turned out fine."
        # n "And, I mean, I guess they don't know how much I enjoy it... but I feel lighter now, just knowing they accept it."
        # n "That maybe it's okay to talk about it some more and not hide it away like it's my greatest shame."
        # n "I have you to thank for that~"

        # Mention Hiroko has her reservations, but even so her earlier comments suggest she's still accepting of it

        # n "It's all been so sudden."
        # Nozomi talks about Kyou's transformation and laments that he couldn't bring this side of himself out sooner
        # The past couple weeks really brought about a change where she and her friends all feel comfortable and safe around him, now that he's
        # become more assertive around them and after proving himself as responsible during the hypno show
        # She also thinks it's brought out something in her as well, as she was forced to reckon with her love of hypnosis and others knowing about it
        # And after people seem accepting, maybe she can allow herself to dabble again without feeling ashamed
        # To end, Kyou does a little playful hypnosis on her on the spot, to her quiet delight.
        # He's not sure about the idea of dating her now. After this time together, knowing the real Nozomi instead of an ideal he's not sure how he feels about her anymore.
        # But he does like making her happy?


        # "Things definitely changed between me and these girls since the day of our rehearsal. I feel lighter whenever I'm around them."
        #
        #
        # "I do, but even as she grins at me it still stings a little." with dissolve
        # "Things definitely changed between me and these girls since the day of our rehearsal. I feel lighter whenever I'm around them."
        # n neutral "What's on your mind?" with dissolve
        # "AUTHOR'S NOTE: Okay, I'm out of time again so I'll have to leave this epilogue frustratingly unfinished for now T_T"
        # "Next time, assuming we don't run into another big setback, I'll finally be done with this story path and we'll see some movement elsewhere."
        # "Bye for now!"
label Epilogue_Reversal_Good_Nozomi:
    scene bg k bedroom day with longdissolve
    "So that was last night..."
    "As I get myself ready for school this morning, I'm still not sure how to feel about everything that went down."
    "All the work I put into learning hypnosis for her, and building that penlight, and it seems all we have to show for it is a load of trouble."
    "I can't exactly blame Nozomi if she wanted to step away from everything."
    "But she said she wanted to live up to what I said? About being a good hypnotist?"
    "I wonder what she really meant by that. Are things really going to be any different now, Nozomi?"
    play sound cellvibratelong
    "Wait, hold that thought. My phone's ringing..."
    "Why is my phone ringing? No one ever calls me?!"
    show phone at right with moveinright:
        ypos 0.346
    stop sound
    n "\"Kyou! Oh good, you're up!\""
    ks surprised "N-Nozomi? Yeah, of course I'm up; it's a school day."
    n "\"Mhmhmh~ Well, it's a little early so I thought...\""
    n "\"A-ahem, anyway I just wanted to talk before school. Can we meet outside? Are you ready to go?\""
    ks confused "Y... y-yeah, just gimme a minute. Where are you anyway?"
    n "\"Um... Just come out when you can, okay?\""
    scene bg house
    show Nozomi front2 smile at center
    with blink
    play sound doorclose
    play music Inspiration
    "She... wow, she wanted to talk to me this badly, huh?"
    n chuckle "Good morning!" with dissolve
    ks smile "M... morning!"
    show Nozomi side smile at flip
    n "S-so, um... I wanted to ask how you're feeling after... you know?" with dissolve
    "She seems to examine my expression as I examine her back."
    n "Still think you're clear-headed?"
    "Damn, I don't know about that. Nozomi looks as bewitching as ever, maybe even more so when she's being like this."
    ks "I'm fine. Just a little surprised, that's all."
    n happy blush "Yeah, I just... I really need you to be okay, that's all." with dissolve
    n smile_side "But, um... come on, let's get going. We'll talk on the way." with dissolve
    scene bg street1 day
    show Nozomi side neutral_side at center, flip
    with blink
    n "I'm still trying to make sense of it all, you know?"
    n sad_side "A penlight that can literally control minds... it's just insane to think about what we had." with dissolve
    ks neutral "A penight that I made, don't forget."
    n surprised "Yeah! How is that even possible? I can't even imagine how you pulled that off!" with dissolve
    ks sigh "And we never will. It's gone now."
    n sad "Yeah..." with dissolve
    n neutral_side "It's... it really is for the best that it's gone though, right?" with dissolve
    "She asks, and I think we both know the answer to that one, but I notice how she looks away from me as she says it."
    ks neutral "Yeah... I mean, yeah of course it is."
    n neutral "Right. Of course it is." with dissolve
    n sad_side "... But is it wrong that a part of me still regrets that it's gone?" with dissolve
    n "Even knowing what I know now, I still can't stop myself from playing it all back in my head and finding it..."
    n sad_closed blush "Well... it still gets me going." with dissolve
    n sad "I've been trying not to think too deeply about it, but... is there something wrong with me, Kyou?" with dissolve
    hide Nozomi
    show Nozomi front2 concerned at center
    "She suddenly stops in her tracks, and I turn to her as she looks at me pensively." with dissolve
    n sleep "I know how close I came to taking over your mind with that thing. It wasn't just a fantasy that I pulled out of my imagination, or out of some weird manga." with dissolve
    n sleeptalk "So why..." with dissolve
    n sleeptalk_concerned "Why am I still like this?" with dissolve
    "I sigh. Yeah, it's a little weird that a high school girl gets a kick out of controlling people's minds. Or even having her own mind taken over."
    "It still surprises me that a girl as sweet as her would have such perverted thoughts."
    ks sigh "Nozomi, there's nothing wrong with you, okay? Nothing could be further from the truth."
    "But since I've come to know that about her, I'm not sure I'd want it any other way."
    show Nozomi concerned
    ks neutral "Yeah, maybe you got caught up in your fantasies or whatever, when we were doing all that stuff together. But when it got real? You did the right thing." with dissolve
    ks "That's what's important, Nozomi. So don't put yourself down; don't do that to yourself."
    "I don't want her to change who she is. And I think when it comes down to it, she doesn't want to either."
    n sleeptalk_concerned "Yes, that's what I keep telling myself. It just gave me a scare, that's all." with dissolve
    ks smile "That makes two of us."
    n smile "Yes, well... I guess all this stuff about controlling minds can go back to being a fantasy from now on~" with dissolve
    ks smile "Isn't it great though, that we can talk about this kinda stuff now without getting weirded out?"
    "And if I can help her accept that side of her, like she's come to accept me, well..."
    n chuckle "Only because we're both weird, it turns out." with dissolve
    "That would really be the best thing."
    ks "Embrace the weirdness."
    n "Oh, I intend to~"
    ks smirk "Speaking of... I didn't know you read manga, Nozo."
    n surprised blush "Huh?" with dissolve
    show Nozomi side sad_side at center, flip
    n "W-well..." with dissolve
    ks happy "C'mon, tell me which ones! I read a lot of them myself."
    n happy blush "... Ask me again after school, okay?" with dissolve
    scene bg school ext day with blink
    "Nozomi continues to be coy as we roll up to the gates together."
    "But... walking with her was nice. Maybe she just wanted to check up on me, but it really is starting to feel like Nozomi and I are becoming closer."
    stop music fadeout 10.0
    r "Hey, you guys!"
    "Huh? That voice calling out to us... Risa?"
    show Nozomi side laugh at center, flip:
        xpos 0.55
    show Risa smile_side at center:
        xpos 0.75
    n "Good morning, Risa! How are you?" with dissolve
    "Shit, this could be trouble."
    show Nozomi smile_side
    r uniform_armup "Oh, you know. Surviving." with dissolve
    r sleeptalk "Sooo looking forward to Ms. Chiba drilling us for our English Lit. exam tomorrow." with dissolve
    "But... this is going a lot more smoothly than I expected."
    r neutral_side "What about you two?" with dissolve
    n happy "I'm... I'm good. Yeah, good." with dissolve
    "What is..."
    r grin "Also surviving. Got it~" with dissolve
    show Risa uniform neutral
    show Nozomi neutral
    ks surprised "What is going on here?" with dissolve
    r "..."
    show Nozomi smile_side
    r smile_side "I think this is what you'd call a conversation." with dissolve
    queue music Peaceful
    n happy "Ehehehe~" with dissolve
    "Ugh, don't act like it's weird for me to be confused here. Not after watching you two fight yesterday..."
    hide Nozomi
    show Nozomi front2 smile at center:
        xpos 0.55
    show Risa smile
    n "So Kyou, I reached out to Risa last night and... well, we talked things out." with dissolve
    show Risa smug
    r "And by \"talked things out\" she means \"apologized big time for all that weird shit\"." with dissolve
    show Risa smile_side
    n sleeptalk_concerned "*sigh* Yes, thank you, Risa. That was an important clarification." with dissolve
    "Huh. So that's why she was in such a hurry to leave last night."
    show Nozomi side sad_closed at flip
    n "But I want you to know I meant every word, Risa. I really am so embarrassed about what I said yesterday." with dissolve
    "She really DID clean up after herself."
    n sad_side "It wasn't my place to talk about Daisuke like that, and... w-well..." with dissolve
    r uniform_armup grin "Nozo, chill. You don't have to rehash all this in front of Kyou. I get it." with dissolve
    s "What is being rehashed? Are we late to this party?"
    show Hiroko smile_side at center, flip:
        xpos 0.35
    show Sayori smile at center, flip:
        xpos 0.15
    show Risa smile_side
    show Nozomi neutral
    "We all turn at the same time to notice some new company has joined us by the gates." with dissolve
    r uniform "Heh. Looks like the gang's all here." with dissolve
    h uniform_headhold2 "Um, hey guys. Y'all good?" with dissolve
    hide Nozomi
    show Nozomi side smile_side at center:
        xpos 0.55
    n "We, um... yes, Hiroko. We're good~" with dissolve
    r smug_side "Don't worry, Hiro. Your mommies aren't fighting anymore." with dissolve
    h uniform_armup furious_side blush "{cps=15}T-the fuck is {/cps}{nw}" with dissolve
    extend "THAT supposed to mean?! YOU were the ones acting like fuckin' babies and don't you forget it!" with vpunch
    h angry_side "So you all just... l-like..." with dissolve
    show Risa smile_side
    h uniform_headhold nervous_side "Arrgh, just don't scare me like that again, 'kay?" with dissolve
    n happy "Aww, I'm really sorry for worrying you, Hiroko." with dissolve
    n neutral_side "It's all my fault for not being honest with you guys." with dissolve
    n sad_closed "Y-you see, Kyou and I..." with dissolve
    show Sayori neutral_right
    show Hiroko uniform_headhold2 neutral noblush
    show Risa neutral
    "At the mention of my name, everyone casts their eyes in my direction, and I'm once again reminded of how awkward it feels under their attention as Nozomi continues speaking." with dissolve
    n sad_side "{cps=20}Kyou and I... we've been seeing each other, okay, but- {/cps}{w=1.0}{nw}" with dissolve
    r uniform_armup grin "Called it!" with dissolve
    show Sayori neutral
    show Hiroko neutral_side
    n front2 pain blush "B-but it's NOT what you think! God, let me finish!" with dissolve
    show Risa smile_side
    n concerned "It's just... when we got to talking we found we have something in common, something I never knew before." with dissolve
    n "And that something was... it was..."
    "Nozomi takes a breath, then audibly clears her throat, then takes another breath."
    show Risa uniform neutral_side
    "The girl group seem to collectively lean in as Nozomi lowers her head as she finally forces the words out of her mouth." with dissolve
    n sleeptalk_concerned "... H-hypnosis. So that's what we've been doing together." with dissolve
    show Sayori uniform_handup
    n "And that's all been going so well, but... m-more than that..." with dissolve
    n neutral_left "Kyou's been really sweet to me. We've been talking a lot, and he's really opened up to me and it's just like, all that tension we had has just gone." with dissolve
    n sleeptalk "So... I... um..." with dissolve
    "Finally, Nozomi raises her head again and locks eyes with me, standing opposite her, as she summons a shy smile to her lips."
    n smile "I really hope Kyou and I can become friends." with dissolve
    "Friends, huh? The way she's blushing makes me wonder if there's more to it than that."
    "But man, now it's my turn to look to the ground because I can feel my cheeks catching fire."
    show Risa neutral
    show Hiroko neutral
    show Sayori neutral_right
    ks smile blush "I, uh... I hope so too, Nozomi." with dissolve
    "And well... it's finally out in the open, isn't it?"
    show Nozomi neutral_right
    r uniform_armup smile "Aww, aren't they just the cutest?" with dissolve
    "Nozomi's love of hypnosis and the truth of what we've been up to together; everything that she so desperately wanted to hide."
    show Nozomi neutral_left
    h uniform surprised_side "Whoa, whoa, back up a sec. What's this shit about hypnosis?" with dissolve
    "There's no going back now."
    n side sad_side "It's s-something I've been interested in for a long time. You could say it's a... um, p-passion of mine?" with dissolve
    ks smile "She's, uh... r-really good at it too. You know, I was bricking it when she invited me to do karaoke with you guys, but she hypnotized me for it, and it helped a ton."
    h confused "That a fact? So she, like, made you do that? Like on a dare or somethin'?" with dissolve
    ks sigh "S-something like that..."
    show Hiroko confused_side
    show Risa smile_side
    n sad_closed "Gosh this is SO embarrassing to talk about!" with dissolve
    n sad_side "But I needed to. I know clamming up about it only made it worse for everyone, s-soooo, now that's all out in the open can we please all just move on?" with dissolve
    r grin "Ppttth-hahahahahahaha!" with dissolve
    n surprised "Risa!" with dissolve
    r uniform "I'm sorry, it's just... like, that is so LAME! THIS is what you've been worked up about?" with dissolve
    show Hiroko smile_side
    s happy "Mhmhmh, it is rather amusing to look back on now, isn't it." with dissolve
    hide Nozomi
    show Nozomi side sad_closed blush at center, flip:
        xpos 0.55
    n "Come on, I'm being serious." with dissolve
    show Sayori smile
    show Hiroko neutral_side
    r smile_side "Oh for sure, sounds like we gotta be careful around you." with dissolve
    show Nozomi sad_side
    r smug_side "No one look into her eyes or she'll hypnotize you into a chicken or something." with dissolve
    n irritated "Ugggh, that's not how hypnosis works! Geez." with dissolve
    stop music fadeout 10.0
    n frown_side "If I was going to hypnotize you I'd need your full consent, because you have to want it to work, and even then you'd still need to focus properly!" with dissolve
    n irritated "Plus there's this little thing called the \"hidden observer\", which basically means you're still aware of anything that happens under hypnosis." with dissolve
    n "{cps=20}So even if I DID want to turn you into a chicken, Risa, and you didn't want to- {/cps}{w=1.0}{nw}"
    show Nozomi irritated
    show Hiroko uniform_headhold2 happy
    show Sayori happy
    show Risa grin
    r "Ahahahahaha~" with dissolve
    n sad "T-to..." with dissolve
    queue music Memories
    s "Mhmhmhmhmh, oh that is adorable!"
    hide Nozomi
    show Nozomi side sad_closed blush at center:
        xpos 0.55
    show Risa smug_side
    n "W-why are you all laughing? It's all true!" with dissolve
    h uniform_armup happy_side "Kyahahaha Nozo, you're so fuckin' weird sometimes!" with dissolve
    n front2 sleeptalk_concerned "I-I know... I'm sorry..." with dissolve
    s smile "Oh, Nozomi. I always knew you had a dash of the eccentric about you; it is nothing to apologize for." with dissolve
    show Nozomi neutral_left
    h uniform_headhold2 smile_side "Yeah for reals, Nozo. I don't always get you, but that don't mean you gotta hide who you are." with dissolve
    h happy_closed "You say you admire how I am? Well, right back at ya, sis! You be as weird as you want, I ain't ever letting go of ya!" with dissolve
    h uniform_armup happy blush "I LOVE ya, bestie~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    n sleeptalk "O-oh gosh, Hiroko, you..." with dissolve
    n laugh "Ahahaha, you're making me blush!" with dissolve
    show Risa uniform_armup grin
    show Sayori uniform_folded laugh
    "Nozomi's embarrassed laughter gets the crowd going again, and I can't help but smile at the sight." with dissolve
    "After all her freaking out over people knowing her dark secret, it must be really cathartic to reveal it to the people closest to her, knowing they love and accept her."
    s uniform_handup smile "Well, much as I am enjoying this, I do believe classes are about to start. We should head inside." with dissolve
    show Hiroko smile noblush
    show Risa uniform sleeptalk
    show Nozomi side smile_side noblush
    r "Yeah. Let's go face the music." with dissolve
    "She really has some great friends."
    h furious "Hey, Kyou!" with dissolve
    show Risa neutral
    show Sayori neutral_right
    show Nozomi neutral
    ks surprised "H-huh?" with dissolve
    show Sayori smile_right
    show Risa smile
    show Nozomi smile
    h uniform_headhold2 smile "Quit spacin' out and walk with us. We gotta bounce~" with dissolve
    "... And, I guess I'm one of them now?"
    scene ReversalGoodEnd bg1 sayori s_smile nozomi n_smile kyou k_smile hiroko h_smile risa r_neutral:
        zoom 0.5
    with longblink
    "So we walk. Together."
    hide ReversalGoodEnd
    show ReversalGoodEnd bg1 hiroko h_smile risa r_neutral:
        zoom 1.4 xpos -1.6 ypos -1.1
    r "You know... I think I'm gonna do it." with dissolve
    h "Do what?"
    show ReversalGoodEnd r_sigh
    r sleep "I'm gonna ditch Daisuke today. Get it over with." with dissolve
    show ReversalGoodEnd k_concerned h_concerned
    "... At least we started walking before Risa dropped that on us and brought us back to a stop." with dissolve
    show ReversalGoodEnd h_surprised r_neutral_side
    h uniform_armup shocked_side "SERIOUSLY? Don't ya dare do it without me; I wanna see the look on his face!" with dissolve
    show ReversalGoodEnd sayori s_smirk n_neutral:
        zoom 1.0 xpos 0.0 ypos 0.0
    s uniform_handup smirk "And now we discover our Hiroko has an interest in voyeurism." with dissolve
    show ReversalGoodEnd h_angry:
        zoom 1.4 xpos -1.6 ypos -1.1
    h furious "Say WHAT?!" with vpunch
    show ReversalGoodEnd s_happy:
        zoom 1.0 xpos 0.0 ypos 0.0
    s happy "So much has been learned today before we have even set foot in a classroom." with dissolve
    show ReversalGoodEnd h_blush:
        zoom 1.4 xpos -1.6 ypos -1.1
    h angry "Y-you shut the fuck up! Don't act like you ain't interested too." with dissolve
    show ReversalGoodEnd r_neutral
    r neutral_side "Hiro, no one's getting a front row seat, okay?" with dissolve
    show ReversalGoodEnd h_concerned
    h uniform_headhold nervous_side "But... h'yeah, I get it. You gotta do it right." with dissolve
    show ReversalGoodEnd r_smug
    r smug "I'll describe it to you later, don't sweat it." with dissolve
    show ReversalGoodEnd kyou k_concerned n_neutral_side:
        xpos -0.8 ypos -0.6
    k "Well... good luck with that, Risa. That can't be easy for you." with dissolve
    n "Yes, best of luck. And you know we'll all be here if you need us."
    hide ReversalGoodEnd
    show ReversalGoodEnd bg1 hiroko h_concerned risa r_smile_side:
        zoom 1.4 xpos -1.6 ypos -1.1
    r smile "I'm sure I can handle him, but... thanks." with dissolve
    "I return Risa's smile as we get back to walking."
    r "But what about you two? Are we gonna see that hypno mumbo jumbo anytime soon?"
    hide ReversalGoodEnd
    show ReversalGoodEnd bg2 kyou k_neutral_side nozomi n_nervous:
        zoom 1.4 xpos -0.8 ypos -0.6
    n sad_side "W-well..." with dissolve
    "It feels like everyone's so open with each other, even knowing I'm among them."
    show ReversalGoodEnd k_smile
    k "I'm game if you are, Nozomi. Now that the cat's out of the bag." with dissolve
    show ReversalGoodEnd n_neutral_side
    k "Are you feeling any better about wanting to do it again?" with dissolve
    "Maybe that penlight didn't work out the way I wanted. But even so, I can look back at that time I spent learning hypnosis with no regrets."
    show ReversalGoodEnd k_smug
    k "Or I could show them what I can do? You know I can go either way." with dissolve
    "It made me open up to Nozomi. To finally take that chance, show her I could truly see her for the wonderful person she is."
    show ReversalGoodEnd bg2 sayori s_curious n_neutral_side:
        zoom 1.0 xpos 0.0 ypos 0.0
    s surprised_right "So... if I am inferring from this correctly you have hypnotized each other?" with dissolve
    "And for that... it finally made her see me too."
    show ReversalGoodEnd n_smile k_smile:
        zoom 1.4 xpos -0.8 ypos -0.6
    n smile "We have and I'm happy everyone's being so supportive, but... I think we really do need to focus on these exams, Kyou." with dissolve
    show ReversalGoodEnd sayori s_smirk:
        zoom 1.0 xpos 0.0 ypos 0.0
    s uniform_folded smirk "Not that we are going to let you off the hook so easily but, yes. Yes we do." with dissolve
    "We truly are friends now. Maybe we can be more than that someday."
    show ReversalGoodEnd s_smile k_smile n_happy n_blush hiroko h_smile risa r_smile:
        zoom 1.4 xpos -0.8 ypos -0.6
    n happy blush "Ehehehe, guess we'll just take a raincheck on that for now, Kyou." with dissolve
    show ReversalGoodEnd n_smile
    n "But after the exams are over..." with dissolve
    show ReversalGoodEnd:
        linear 5.0 zoom 0.5 xpos 0.0 ypos 0.0
    "Maybe this is enough."
    n "... I'm thinking about getting a pocketwatch?"
    $persistent.reversal_good_end_unlock = True
    jump Credits

label Epilogue_Reversal_Bad_Nozomi:
    scene bg k bedroom day with longdissolve
    "I awaken in the morning to the sound of a quiet moan."
    "A moan from my own lips... God, was I dreaming about her again?"
    "It was more than a week ago, and yet the memory of that beautiful woman hypnotizing me on the school rooftop feels fresher than ever."
    play sound clothes
    "But as I shuffle out of the bedsheets and stretch for my phone I realize the time."
    ks nude surprised "S-shit, I gotta get a move on!"
    play music Bright_Opening
    scene bg street1 day with blink
    "A quick shower and a bite of breakfast and I'm practically running on my way to school."
    "Dammit. Why did I have to oversleep again? I need to be there bright and early. I promised her I'd do better this time."
    "If only I could've stopped myself from dreaming about her mesmerizing beauty. Her bewitching brown eyes."
    "Her... melodic, entrancing voice. I can almost hear it again from my dreams..."
    "Shit! I'm doing it again!" with vpunch
    scene bg blackscreen
    play sound runningshoes
    $ renpy.transition(longdissolve, layer="master")
    "I gotta pick up the pace..."
    scene  bg school ext day with longblink
    "Only when the school gates loom large before me do I finally come to a stop."
    "With a gasp, I clutch my chest as I massage the air back into my bursting lungs. Man, I'm so out of shape."
    "No... This is no time to catch my breath. I gotta find..."
    $nozomi_name = "Miss Akemi"
    show Nozomi side frown at center
    n "Oh there you are, Koyama. Did you mean to keep me waiting again?" with dissolve
    ks surprised blush "M... M-Miss Akemi!"
    "My god, there she is. Appearing suddenly before me as if she had stepped out of heaven itself."
    n front irritated "Let me guess... You had another dream about me so you overslept and made yourself late." with dissolve
    "It's enough to take my breath away. If I had the breath to lose, that is."
    n frown "Am I wrong, Koyama?" with dissolve
    "The sweet, hypnotic sound of her voice, even as she scolds me, sounds even better than it did in my dreams."
    ks "I... th-that is..."
    "And she can read my every shameful thought as if it were written on my forehead. That's just how amazing she is."
    show Nozomi neutral
    ks sad "No, Miss Akemi, you're exactly right. I can't stop thinking about you, not even in my sleep." with dissolve
    n sigh "Ahh you're so hopeless, Koyama. But it seems you just can't help yourself." with dissolve
    "There's no point in even trying to lie to someone as incredible as her."
    n neutral "You want to be hypnotized again that badly, don't you." with dissolve
    "I hang my head, ashamed that I managed to disappoint this goddess of a woman."
    ks sigh "Yes, Miss Akemi... I'm really sorry."
    show Nozomi front2 smile
    "But suddenly I find my chin cupped by Miss Akemi's gentle hand as she turns my gaze upwards, and before I know it I'm treated to that beautiful smile of hers." with dissolve
    n "Don't worry, Koyama. I suppose it's okay if you want to feel like I'm hypnotizing you every night as you sleep."
    show bg blackscreen onlayer toplayer with longdissolve:
        alpha 0.6
    "But moreso, I realize those beautiful brown eyes are looking right into mine from behind her glasses. And when they look at me, it's impossible not to lose myself in them..."
    ks confused noblush "I..."
    n "Just as you find yourself becoming hypnotized now as you look into my eyes..."
    "Yes, lose myself... in those bewitching... mesmerizing brown eyes..."
    ks entranced "Uhh..."
    n "Shh, don't speak. Just sink, back into your happy place..."
    show bg blackscreen:
        alpha 1.0
    with longdissolve
    pause 2.0
    play sound fingersnap
    show Nozomi front chuckle at center
    hide bg blackscreen onlayer toplayer
    n "Ehehehehe~"
    "Miss Akemi's gentle laughter reverberates in my ears as she breaks eye contact and I find myself blinking sharply."
    n smile "Aww, I can't stay mad at you. Don't worry about it~" with dissolve
    "As she smiles at me again, I'm suddenly aware of a euphoric sensation leaving my body. But that means..."
    ks surprised "I... y-you really..." with dissolve
    "Oh my god, Miss Akemi hypnotized me just now!"
    n chuckle "I mean it, Koyama. All is forgiven." with dissolve
    "This girl I've crushed on for so long. I always knew how kind she was, but even so I still can't believe how good she is to me."
    n side smile "Besides, I'm sure you'll find a way to make it up to me." with dissolve
    "Miss Akemi is so awesome!"
    n smile_side "And as a matter of fact, I might have just the thing." with dissolve
    "Man, I wonder what she said to me while I was under. I'm feeling excited all over again just thinking about..."
    n smile "Koyama... is your father going to be home tonight?" with dissolve
    "Ahh, but I can't let myself enjoy this wonderful feeling. I gotta pay attention to what Miss Akemi is saying to me now I'm awake."
    ks confused "My... father? No, Miss Akemi, he's still on a business trip."
    "I must repay her kindness. That's the only thing I should be thinking about right now."
    n happy "That's what I thought. Then I'm sure you won't mind if I borrow you and your house for the evening." with dissolve
    ks smile blush "Oh... o-of course, Miss Akemi. You got it."
    "Honestly, Miss Akemi could've asked anything of me and it would be hers."
    show Nozomi smile
    "I'd give her whatever her heart desires, if it meant I could be in her angelic presence even a second longer." with dissolve
    n front smile "Good. Now let's... {w=1.0}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend neutral "ah."
    "Only... the smile I covet so much drops from her face as she seems to notice something over my shoulder."
    n neutral_right "Well, look who it is..." with dissolve
    "So I turn around to follow Miss Akemi's gaze and spy a familiar figure walking towards the school gates. Towards us."
    show Risa neutral_side at center:
        xpos 0.75
    show Nozomi side smile_side at flip
    n "Um, good morning, Risa." with dissolve
    r uniform_armup surprised_side "... Huh?" with dissolve
    "Right, that's Risa. I haven't seen her since..."
    r neutral_side "Oh, it's you. Something up?" with dissolve
    "Since that day on the rooftop."
    n neutral_side "A-actually, I ... I was just wondering about you. Is everything okay?" with dissolve
    "Now that I think of it, I'm a little surprised she and Miss Akemi are even speaking to each other after the fight they had back then."
    r uniform frown_side "Eh? Why wouldn't it be?" with dissolve
    n sad_side "W-well, I just, um... heard something happened with you and Daisuke?" with dissolve
    r uniform sleeptalk "Oh... Guess word travels fast, huh." with dissolve
    "But then, this is Miss Akemi we're talking about here."
    n surprised_side "So you really did dump him like I-... {w=1.0}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend neutral_side "I-I mean, yes. Something like that."
    show Risa neutral_side
    "Miss Akemi is so wonderful, I can't imagine how anyone could get mad at her." with dissolve
    n sad_side "Um, do you want to talk about it?" with dissolve
    "It's just so strange to me that anyone could feel differently about her than I do."
    r concerned_side "I mean... It was just the weirdest thing." with dissolve
    "But it seems like Risa is finally beginning to understand."
    r uniform_armup "We hooked up last night and we started talking, but it's like the second I saw him I just kinda knew it was over, you know?" with dissolve
    n smile_side "Ahhh... Yeah, I think I do." with dissolve
    r frown_side "So I just told him it wasn't working out and he gave me some shit over it, but it's fine." with dissolve
    n "Mhm, mhm~"
    "And if that crap with her and Daisuke really is over, then I guess there's no reason for them to fight anymore, right?"
    r sleeptalk "I was probably gonna ditch him when we got to college anyway, so... yeah, I just ripped off the bandaid that's all." with dissolve
    n happy "Well, I'm really happy for you, Risa. You did the right thing." with dissolve
    r uniform smile_side "Yeah. I don't even know why I'm even telling you this, but... yeah. Kinda feels good to move on and all." with dissolve
    "Yeah. I'm glad Miss Akemi doesn't have to worry about Risa any more."
    show Nozomi smile_side
    r smug "You get all that, shy boy? Ya girl's back on the market~" with dissolve
    show Nozomi neutral_side
    ks surprised "H-huh?!" with dissolve
    n sad_side "Oh, Risa, don't tease him again." with dissolve
    "Honestly, I'm more surprised she even acknowledged me."
    show Risa smile_side
    n neutral_side "And wait, don't tell me you're already wanting another boyfriend after all this." with dissolve
    "Besides, Risa can tease me all she wants. Like I could ever be interested in a girl who isn't Miss Akemi."
    r sleeptalk "Maybe, maybe not. I'll take it as it comes." with dissolve
    n irritated "Urrrgh." with dissolve
    n sad_closed "{size=16}Well, at least I know you can be convinced. I just need to step it up a little more.{/size}" with dissolve
    r neutral_side "You... what now?" with dissolve
    n frown_side "Listen, Risa, if you want my advice..." with dissolve
    r frown_side "Which I don't." with dissolve
    stop music fadeout 5.0
    n "I think you should remember the light again."
    "Wait, why is Miss Akemi's face so stern all of a sudden?"
    r neutral_side "\"Remember the\"... {w=1.0}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend surprised_side "huh?"
    n neutral_side "You remember the light. Don't you, Risa." with dissolve
    play music Flow fadein 5.0
    "She's..."
    show Risa entranced_side
    $ renpy.transition(longdissolve, layer="master")
    r entranced_side "Uh... s-sure..."
    "Oh man, she's... Miss Akemi is..."
    n smile_side "I thought you might. You remembered to dump Daisuke after all, so it's only natural that you remember the light as well." with dissolve
    "Miss Akemi is so amazing."
    n neutral_side "So now we know for sure how good you are at remembering, I want you to remember that you're going to swear off of guys until we graduate high school." with dissolve
    show Nozomi neutral
    r "..." with dissolve
    "As Risa stands vacantly in front of us, Miss Akemi glances to me and puts a finger to her lips. And I understand completely."
    show Nozomi neutral_side
    "It feels so good to be controlled by Nozomi." with dissolve
    n  "It's for the best, Risa. Remember, and wake up in three, two, one..."
    play sound fingersnap
    show Risa neutral_side
    stop music fadeout 5.0
    "And with a snap of her fingers, Miss Akemi takes a half-step away from Risa as I watch the girl's eyes flicker back to awareness." with dissolve
    n "Risa?"
    "I hope she realizes how lucky she was that she got to experience what it's like to be hypnotized by Miss Akemi."
    play music Bright_Opening
    r drowsy "You know, I think I'm gonna swear off of boys until we're out of here. Too much drama, you know?" with dissolve
    "Honestly, it makes me a little jealous. But I don't want to dwell on that."
    n smile_side "Oh. Really?" with dissolve
    "I'm just happy for Miss Akemi to get what she wants."
    r smile_side "Yeah... Yeah, you know what? Yeah!" with dissolve
    r uniform_armup grin "Nothing but wild nights out with the girls from now on~" with dissolve
    n happy "Eh... ehehehe, well in that case I actually have a little something planned myself~" with dissolve
    r smile_side "Hm, what's that?" with dissolve
    n smile_side "How would you feel about a slumber party?" with dissolve
    r smug_side "A slumber party? What are we? Twelve?" with dissolve
    n frown_side blush "N-no, hear me out! We're going to Kyou's since he's on his own tonight." with dissolve
    r neutral "That a fact?" with dissolve
    n smile_side "There'll be games, singing, maybe a movie, and a few other surprises in store; it'll be great!" with dissolve
    r uniform sleeptalk "Nozo, come on. I don't care if it's just your boyfriend, I'm not making an exception for him." with dissolve
    n frown_side "H-he's not... we're just good friends, Risa." with dissolve
    show Risa neutral_side
    n "And besides, Kyou's practically one of the girls anyway; you pretty much said it yourself." with dissolve
    r uniform_armup "Well, whatever it is you've got going on, I'm not interested." with dissolve
    n sad_side "Look, I just want us to be friends, okay? We haven't always seen eye to eye, but Hiroko thinks the world of you so we really need to get along." with dissolve
    r uniform concerned_side "We really don't, you know. Besides, you're kinda creeping me out." with dissolve
    n smile_side "W-well... that just means you need to remember the light again, don't you." with dissolve
    show Risa entranced_side
    n smile_side noblush "Yes, remember the light and don't worry about the sleepover. It's going to be great." with dissolve
    n "Just tell me you'll come, okay?"
    r "Oh... okay..."
    play sound fingersnap
    show Risa neutral_side
    n happy "So you'll come, right?" with dissolve
    r smile_side "... Oh what the hell, count me in. Sounds like a riot." with dissolve
    show Nozomi surprised
    show Sayori smile at center, flip:
        xpos 0.15
    show Hiroko happy at center, flip:
        xpos 0.3
    h "Nozoooo!" with dissolve
    hide Nozomi
    show Nozomi side smile_side at center
    n "Oh... hey, good morning! Perfect timing." with dissolve
    h smile_side "Yeah? What's going on?" with dissolve
    n smile_side "We're going to have a sleepover at Kyou's house tonight. You two are coming, right?" with dissolve
    s uniform_handup surprised "At Kyou's, you say?" with dissolve
    n "That's not weird is it?"
    show Sayori neutral
    h confused_side "Why'd it be weird? It's just Kyou an' us girls at this thing, right?" with dissolve
    s smirk "Kyou may as well be one of \"us girls\", in all honesty." with dissolve
    show Hiroko happy_closed
    "Hiroko giggles in agreement, and I notice Nozomi flashing the pair of them a knowing grin as I watch quietly." with dissolve
    n laugh "Hahaha, alright, then! We'll talk more about it over lunch, okay?" with dissolve
    show Hiroko smile_side
    s uniform smile "Very well. Now, shall we head inside?" with dissolve
    n smile_side "Actually... can you all go ahead? I need to ask Kyou about something real quick." with dissolve
    hide Sayori
    hide Hiroko
    hide Risa
    stop music fadeout 5.0
    "And with that the other girls leave us be as they make smalltalk among themselves on the way to class." with dissolve
    n front smile "Now as for you, Kyou... come here..." with dissolve
    scene bg school side day
    show Nozomi front2 smile at center
    with blink
    play music Park
    "Miss Akemi beckons and I gladly follow her to a secluded side of the school building, away from the general masses of students that are now gathering for the start of lessons."
    n chuckle "This should be far enough. Now..." with dissolve
    scene bg blackscreen with dissolve
    "Once again my goddess approaches me, and once again she cups a hand under my chin as a quiet moan breathlessly escapes my quivering lips."
    scene ReversalBadEnd neutral with dissolve
    n neutral "You know... sometimes I still wonder if I can live with myself."
    "And I can't help but find those eyes of hers again..."
    stop music fadeout 5.0
    show ReversalBadEnd worried
    n concerned "This isn't how you smooth things over with your friends." with dissolve
    $renpy.music.set_volume(1.0)
    play music Flow
    $renpy.music.set_volume(0.1)
    "God, those eyes... it's happening again."
    show ReversalBadEnd curious
    n neutral "But it was just... it was just so easy, and..." with dissolve
    $renpy.music.set_volume(0.2)
    show bg blackscreen onlayer toplayer with longdissolve:
        alpha 0.4
    "My world darkens around me as I shudder in anticipation. I can't help it."
    show ReversalBadEnd smile
    n smile "And... well, all that aside, we're going to show my friends a good time tonight. Won't we, my plaything?" with dissolve
    $renpy.music.set_volume(0.3)
    show bg blackscreen onlayer toplayer with longdissolve:
        alpha 0.6
    "I don't want to be helped. I want to lose myself in those eyes; let everything go but the only thing that matters..."
    ks entranced "Y... yesss..."
    $renpy.music.set_volume(0.4)
    show bg blackscreen onlayer toplayer with longdissolve:
        alpha 0.8
    show ReversalBadEnd wicked
    "Her." with dissolve
    $renpy.music.set_volume(0.5)
    n "That's right, Koyama. You remember the light too."
    $renpy.music.set_volume(0.6)
    n "Now sink. Sink back into your happy place, and I'll tell you how to treat my friends like queens."
    $renpy.music.set_volume(0.7)
    n "Because it feels so good to be controlled by Nozomi."
    $renpy.music.set_volume(0.8)
    # hide bg blackscreen onlayer toplayer
    show bg blackscreen onlayer toplayer with longdissolve:
        alpha 1.0
    n "Doesn't it."
    $renpy.music.set_volume(0.9)
    ks "Yes..."
    $renpy.music.set_volume(1.0)
    ks "It feels so good to be controlled by Nozomi..."
    $persistent.reversal_bad_end_unlock = True
    scene bg blackscreen
    hide bg blackscreen onlayer toplayer
    jump Credits

label Epilogue_Con_Kyou_Sayori:
    if ending == "trust":
        scene bg classroom eve with longblink
        play music Memories
        "As another school day draws to a close, I gather my things and ponder."
        play sound schoolbell
        show Hiroko annoyed_side uniform_arm at center, flip
        show Nozomi side sad_closed at center:
            xpos 0.75
        n "Well that sure dragged on." with dissolve
        h "Uggh, tell me about it. Can't wait to get back on court and smack the shit out of some balls."
        n frown_side "... I'm sure you could've phrased that better." with dissolve
        h smirk_side uniform_headhold2 "Probably." with dissolve
        "It's been a few months since that day."
        n smile_side "Anyway, let's get out of here. See you tomorrow, Sayori!" with dissolve
        show Sayori alert_smile at left, flip:
            xpos 0.1
        s "See you." with dissolve
        hide Nozomi
        hide Hiroko
        "Three months since I got Sayori involved with hypnosis and that penlight." with dissolve
        s alert_smile_right "Are you coming, Kyou?" with dissolve
        ks smile "Huh? Oh yeah, just a sec!"
        stop music fadeout 2.0
        scene bg study room eve with blink
        show Sayori alert_smile
        with dissolve
        play music Peaceful fadein 2.0
        s "Seems it is just us today."
        "Life has been pretty good to me since then."
        ks smile "Yeah. After entrance exams, I guess study club's pretty much dead until next year."
        "Sayori and I kept talking to each other after that weird week. She even let me join her club officially and I've been a regular ever since."
        s alert_smile_right "How did you think you did?" with dissolve
        ks "Pretty good! I think I really turned things around thanks to you."
        "And in the process we've been getting to know each other a lot more."
        s uniform_folded alert_smile "Ah, it was a group effort. But I happily take some of the credit." with dissolve
        ks "What about you, though? Do you think you made it?"
        s alert_happy "I am quietly optimistic." with dissolve
        s alert_smile "It has helped that I have had far fewer issues with knowledge retention since I started making time for myself." with dissolve
        s alert_smile_right "And I think your hypnosis sessions with me post-incident have actually helped with my insomnia." with dissolve
        ks "Yeah, I'm really happy that helped."
        "I then add with a grin:"
        ks smirk "Shame you didn't join me on stage for the culture fest, though."
        s uniform alert_rolleyes "Please. I am not one for public performances. Besides, Nozomi did enough to keep you on your toes." with dissolve
        ks smile "Heh. I can't believe she wanted to do that again after last year. I don't think she even likes me that much."
        show Sayori alert_smirk_right
        "Sayori chuckles and shakes her head." with dissolve
        s uniform_handup "Are you serious? Or have you really not figured her out yet?" with dissolve
        ks "Eh, I dunno."
        "I shrug. I guess I haven't been thinking much about Nozomi lately."
        ks "Anyway it seems pointless to be hanging around here, huh?"
        s alert_annoyed "Hm... I suppose. There is little else to study for until we get our results back." with dissolve
        "That's what I thought. And now seems a good time to do something I've been wanting to do for a little while now."
        ks "So, uh... how about we head over to the arcade or something?"
        s uniform alert_panicked_right "K-Kyou!" with dissolve
        ks surprised "... What?"
        s alert_smirk_right "Are... are you asking me out?" with dissolve
        "Her response takes me back for a moment, but only a moment as I grin at her."
        ks smirk "As a matter of fact I am. So, are you coming or not?"
        show Sayori alert_surprised_right
        "My time with Sayori didn't just force me to take my studies more seriously and up my own aspirations for the future." with dissolve
        "It also let me study Sayori as well."
        s alert_neutral blush "H- Hmm... why the arcade? I thought such a generic person as yourself would be the dinner and a movie type." with dissolve
        ks smile "Well... I remember you saying you used to play in the arcade a lot before you started high school."
        ks "You only stopped because that's when you went overkill on the studying."
        ks "So how about it?"
        scene bg school ext eve with blink
        "As we leave the club room and approach the gates, I feel a tap on the back of my hand."
        scene cg sayori alter good end 1
        show Sayori AlterEnd1 concerned
        with blink
        ks "Huh?"
        s "I just want to be sure that you know... I am still moving away if I do get into med school."
        s "So please understand if nothing comes of this."
        "I look to her eyes and see the apprehension in them, as my hand brushes against hers."
        "When she makes no attempt to move her hand away, I close my fingers around it and smile at her."
        ks smile "I know. And I get it, you've worked too hard to stop now."
        ks "But between then and now, let's not worry about that. We can enjoy the time we have."
        ks blush "And I mean really... What's the worst that could happen from this?"
        ks "We try a few games, they suck and you stay bored?"
        show Sayori AlterEnd1 blush happy
        "I can feel Sayori's fingers tighten around mine as we share a smile." with longdissolve
        s "You are piquing my interest, and I am resenting you for that."
        s "Let's go."
        $persistent.alter_good_end_1_unlock = True
        jump Credits
    elif ending == "altered":
        $sayori_name = "Sayori"
        scene bg classroom day with longdissolve
        "So that was a few days ago."
        play music Eons
        "The weekend came and went, and now I'm kind of freaking out."
        "Because I'm back in school and I still haven't had a proper talk with Sayori since the argument because..."
        show Sayori alert_laugh at center
        s "Kyou! Good morning to you~" with dissolve
        "Well..."
        ks confused "Uh, yeah good morning Sayori."
        s  alert_smile_right "Did you have a good weekend? Do anything exciting? I want to hear all about it." with dissolve
        "Her behaviour's been confusing me."
        ks "Oh, I... it was okay, I guess. Played a few videogames, that's all."
        s uniform_handup alert_happy "Which ones? Oh wait, don't tell me..." with dissolve
        "Kinda scaring me too."
        s alert_giggle "Actually, why don't you show me this evening? I've been dying to hang out again; would that not be so much fun?" with dissolve
        "This intensity. This... over-eager, joyful energy... she still hasn't dropped the carefree, fun-loving act?"
        ks "I-I don't know, today doesn't really work for me."
        "Is she like this at home too?"
        s alert_surprised_right "No? Don't tell me you are actually going to study for these mock exams we have coming up." with dissolve
        s uniform_folded alert_laugh "Ahaha, you should know we only treat those things with scorn and ridicule. That's why we call them mock exams~" with dissolve
        "Or is this her way of fucking with me?"
        show Sayori alert_smile_right
        show Nozomi side neutral at center:
            xpos 0.7
        n "Hey, Sayori. And... Kyou? Good morning." with dissolve
        "I just don't know what to make of it, and I'm a little grateful Sayori's been distracted so I don't have to answer her."
        show Nozomi neutral_side zorder 2
        show Sayori alert_happy at center, flip        
        show Hiroko uniform_headhold2 neutral_side at center:
            xpos 0.85
        s "Nozomi! And Hiroko too! Good morning dear friends~" with dissolve
        h sleeptalk "... Still ain't getting this sunshine and rainbows thing you got going on." with dissolve
        "But it seems I'm not the only one having trouble around our class' star student."
        h confused_side "And what's the deal between you and him anyway? Like you're all buddy buddy all of a sudden?" with dissolve
        s uniform_handup alert_laugh "Ahahaha, and what if we are? I never had any serious objection to Kyou anyway." with dissolve
        h uniform "That a fact?" with dissolve
        s alert_smile "But honestly, Hiroko, I just want to enjoy life. Our stay on this earth is too short to be stressing about the little things." with dissolve
        n sad_side "... Is that why you quit the study club?" with dissolve
        play sound schoolbell
        stop music
        show Hiroko neutral_side
        s "..." with dissolve
        play sfx2 classdoor
        $ t = "Mr. Kobayashi"
        t "Okay class, settle down. We have a little ground to cover this morning. Please be seated."
        hide Sayori
        hide Hiroko
        hide Nozomi
        with dissolve
        "Nozomi's pointed question goes unanswered as everyone is drawn to their desks, but... did I really hear that right?"
        t "Now, I hope you all remember you'll be doing your mock entrance exams in a couple days..."
        "Sayori's really quitting the study club? Doesn't she run that thing?"        
        scene bg blackscreen with dissolve
        "What the hell is going on with her?"
        scene bg classroom day with longdissolve
        play music Downtown
        "A tense morning eventually gives way to the lunch period, and I watch as Sayori wastes no time in leaping up from her seat."
        show Sayori uniform_handup alert_laugh at center
        s "Aaaah, sweet respite at last~" with dissolve
        "I can't stand it any more. Something's clearly not right."
        show Hiroko uniform_headhold2 confused_side at center, flip:
            xpos 0.25
        show Nozomi side sad_side at center:
            xpos 0.75
        h "What're you even talking about? I thought you loved learning shit." with dissolve
        "I need to say something to her; figure out what exactly her deal is."
        s alert_smile "Mhmhm, I think I am learning to love our rooftop lunches even more." with dissolve
        hide Nozomi
        hide Hiroko
        show Sayori alert_smile_right
        "So as the three girls make ready to leave I catch Sayori's gaze and subtly wave my hand at her, hoping she'll make an excuse to stick around and talk to me." with dissolve
        s alert_surprised_right "Oh! I'll join you up there in a moment, Kyou wants to say something to me!" with dissolve
        "... Although subtlety apparently wasn't on her mind."
        h "What? Ugh, whatever..."
        # Time skip to lunch
        # "After telling the pair she'll join them for lunch in a moment, Nozomi and Hiroko leave for the rooftop while Sayori presses Kyou again." with dissolve
        "Well... alright. Now to see if I can get to the bottom of all this weirdness."
        show Sayori uniform alert_smile_right
        ks confused "Sayori... are you okay?" with dissolve
        s alert_giggle "Am I okay? My word, do I not look okay to you?" with dissolve
        "I lean in, hoping none of the other loiterers in class overhear what I'm about to say."
        ks "Sayori, come on. All this \"happy and carefree\" stuff? I know that's not what you're about. Everyone knows it."
        s alert_smile_right "Oh... is that so?" with dissolve
        ks neutral "Yeah. So look, if you think you have to be like this just because I hypnotized you, then that's just nuts. You can drop the act any time you want."
        s alert_concerned_right "... \"Act\"?" with dissolve
        ks sigh "And if you're doing this to make some sort of point, I... I dunno, I'm sorry I guess?"
        s uniform_handup "..." with dissolve        
        ks "I mean, you're not actually going to quit your study club are you?"        
        s alert_happy "Mhmhmhmhmhmh~" with dissolve
        stop music fadeout 5.0
        "Man, what's with that reaction?"
        "I'm about to speak again when Sayori just leans in conspiratorily, a foreboding glint in her eye."
        s "Oh my, Kyou..."
        s alert_smirk_right "Do you actually think I am this stuffy \"Sayori\" character, perchance?" with dissolve
        play music Unrest
        s alert_happy "I thought you of all people would know better." with dissolve
        "That... is not a response I was expecting."
        s alert_laugh "Ahahaha, you told me to be someone else, did you not?" with dissolve
        "She couldn't possibly mean what I think she..."
        s alert_happy "So who do you think I am now?" with dissolve
        ks surprised "It can't be..."
        s alert_laugh "It can absolutely be~ Ahahahaha!" with dissolve
        "As she gives that melodic little laugh, she seems to lean in even closer as her voice falls to a barely perceptible whisper..."
        $sayori_name = "[alt_name]"
        s alert_giggle "{size=16}I'm [alt_name], silly.{size=16}" with dissolve
        "She means it. She's really convinced herself she's this other similar, yet completely different person this entire time?"
        s alert_smile_right "I must admit I was so confused at first, by this little magic trick of yours." with dissolve
        s alert_neutral_right "Everyone was calling me by this unfamiliar name. Expecting all the wrong things of me..." with dissolve
        "How..."
        s uniform_folded alert_sleeptalk_concerned "It was rather upsetting, yet it quickly made me realize the truth of your hypnosis. How could it not?" with dissolve
        "How the hell is she still affected by this?"
        s alert_laugh "Hypnosis really works! And being a subject of it has been quite beneficial if I do say so myself~" with dissolve
        ks "You can't be serious! There's no way you'd just flip a switch just from that. It's impossible!"
        s uniform_handup alert_concerned_right "Oh come now, Kyou. If you truly believed that, then why did you think to flip my switch a second time?" with dissolve
        ks "A... second..."
        s alert_surprised_right "That is how I seemingly teleported from your bedroom to your living room, is it not?" with dissolve
        "She even thought about that? Like she really has a separate memory? This is..."
        s alert_rolleyes "And if this \"Sayori\" annoyed you so much that you did such a crazy thing as will me into being, perhaps it would be better to leave that switch alone, hm?" with dissolve
        "Did I seriously manage to give Sayori a whole second personality that just took over? She's not going to change back on her own?"
        ks "I... [alt_name], I..."
        scene SayoriAlterBadEnd3 wink with blink
        "As I struggle to make sense of this absolute shitshow playing out in front of me, \"[alt_name]\" simply winks at me as she puts a finger to her lips."
        s "Shh... it's okay."
        "I could change her back, perhaps? Surely the reverse trigger still works; I could at least try it."
        s "We don't need to speak any more of this."
        "But if I did, then what? How could I ever explain or justify myself to Sayori? Or to anyone?"
        show SayoriAlterBadEnd3 smile blush
        s blush "It will be our little secret... my dear Kyou." with dissolve
        "[alt_name] reaches out to me, and I feel her hand brush fondly against my cheek, just for a moment..."
        $ persistent.sayori_alter_bad_end_3_unlock = True
        scene bg classroom day with blink
        "... And then she turns and strides giddily towards the door to join those others." with dissolve
        "Maybe the best thing to do... would be nothing after all? Pretend all this never happened. That this change in Sayori had nothing to do with me."
        scene bg blackscreen with longdissolve
        "... At least she seems happy?"
        # I am rather fond of this life. But it seems this Sayori may not have been so fond of hers.
        # "But with a laugh, Sayori is all too happy to admit that she's still the \"[alt_name]\" that he told her to be, and she's rather enjoying being so." with dissolve
        # show Sayori alert_smile_right
        # "And if Kyou thought Sayori was such a bother that he'd do such a crazy thing as bring her into being, then maybe it's best things stay this way, hm?" with dissolve
        # show Sayori alert_happy
        # s "It will be our little secret... my dear Kyou."
        
        # "Kyou tenses up, his mind doing flips about what this could mean, while [alt_name] simply winks at him and excuses herself to go to lunch." with dissolve
        # hide Sayori
        # "Did he seriously manage to give Sayori a whole second personality that just took over? She's not going to change back?" with dissolve
        # "And if she ever did, how the hell could Kyou ever explain or justify himself?"
        # "As he ties himself up in knots thinking about it he reasons that maybe the best thing to do... would be nothing?"
        # "Pretend all this never happened. That this has nothing to do with him..."
        # "... At least she seems happy?"
        # "(( BOOM! The end! ))"
        # "(( So yeah, pretty short and snappy. Like I say, I intend to write this in fairly short order so check out the finished script in the next update~ ))"
        jump Credits                    
        #Kyou calms down, and calms alter down as well after her disorientation and questioning why she's shaking
        #Now he's not sure what to do. He doesn't want to argue with Sayori again, so he wonders to himself if leaving her thinking happy thoughts like this would be so bad
        #Maybe he can just let her leave like this. If she really, really wants to she'll snap back to her regular self a little later
        #"Second personality"? Pfft, Sayori's being so dramatic. She just needs to chill
    elif ending == "forscience":
        scene bg classroom day with longblink
        play music Memories
        "The following school day, I set my things down at my desk, ready to start a new week."
        show Hiroko frown_side at center, flip:
            xpos 0.25
        show Nozomi side sad_side at center:
            xpos 0.5
        "And as I look up, I see Nozomi file in with her other friend..." with dissolve
        n "Morning, Hiroko. How are you?"
        h sad_side "Ehh... Man, I dunno. You really think I did okay?" with dissolve
        n frown_side "I guess I can't really say for sure, but you got pretty far didn't you? I'm sure someone was impressed." with dissolve
        h sleep "Yeah. Guess we'll see in a couple months, huh." with dissolve
        show Sayori sleep at center:
            xpos 1.1
            linear 1.0 xpos 0.75
        pause 1.0
        show Nozomi at flip
        show Hiroko neutral_side
        s "Mmn... good morning." with dissolve
        n smile_side "Morning, Sayori. How was your weekend?" with dissolve
        s sleeptalk "Uneventful. And far too short." with dissolve
        show Sayori sleep
        n frown_side "Oh dear. You haven't been sleeping well again?" with dissolve
        "And that reminds me..."
        s smile "Again? I thought we had established this was my normal state of being." with dissolve
        h uniform_headhold2 sad_side "I dunno, buddy, you had this perky look going last week. I kinda miss it." with dissolve
        "There's something I need to do today."
        scene bg classroom day
        show Hiroko frown at center, flip:
            xpos 0.25
        show Nozomi front at center:
            xpos 0.5
        show Sayori neutral_right at center:
            xpos 0.75
        play sound schoolbell
        stop music fadeout 5.0
        with blink
        "I need to wait until lunchtime, but as soon as the bell rings I'm ready to make my move."
        ks neutral "Hey, Nozomi? Do you have a minute?"
        h irritated "Come on, dude, we gonna do this every week?" with dissolve
        h uniform_armup "Give us a fuckin' break." with dissolve
        ks "It's... I mean, it concerns..."
        "I make eye contact with Nozomi, then make a little nod towards Sayori."
        n frown "It's alright, Hiroko. Go on ahead, I'll see what he wants." with dissolve
        h uniform confused_side "Ugh, really? You sure?" with dissolve
        n side neutral "It's fine. This won't take long." with dissolve
        hide Hiroko
        hide Sayori
        "Hiroko rolls her eyes at me, but the pair of them leave." with dissolve
        "And I don't think Sayori noticed the gesture I made. Not that... not that she'd have any reason to believe we'd be talking about her anymore."
        n front2 frown "Alright, Kyou. Is this about what I think it is?" with dissolve
        play music Measured
        ks smile "Yeah... and what you said about wanting to help."
        ks "I've been thinking about it all weekend and... I think it would actually be useful to get some more data from your perspective."
        ks "If you're still willing, that is?"
        n chuckle "Of... of course! If you think it'd be useful after all, then I'm happy to volunteer." with dissolve
        "I return her smile as I try to ignore the knots in my stomach."
        "With what Nozomi knows about the penlight, it'll be only a matter of time before she tells Sayori something she shouldn't."
        "So it's only reasonable to do this."
        ks "Great. Do you think you could meet me someplace after school today?"
        n neutral_right "I should be free after club... if that works for you?" with dissolve
        ks "Yeah, we'll meet then. And of course, Sayori can't know about this."
        n laugh "Of course! I'm looking forward to... to helping Sayori~" with dissolve
        n smile "Anyway, I should go. Talk to you this evening, Kyou." with dissolve
        hide Nozomi
        "As she leaves I breathe out another laboured sigh." with dissolve
        show penlight at right with moveinright:
            ypos 0.346
        "Once I've convinced her to forget all about this, I'll be free to research in peace."
        "And this will be the last time I use the penlight on a human mind, of course."
        "The absolute last time..."
    elif ending == "alter_extinguished":
        scene bg classroom eve with longblink
        play music Memories
        "As another school day draws to a close, I gather my things and ponder."
        play sound schoolbell
        show Sayori uniform_folded at center
        show Nozomi side smile_side at center, flip:
            xpos 0.25
        show Hiroko neutral_side at center:
            xpos 0.75
        h "Yeah great, now we can get out of here." with dissolve
        "It's been a couple of months since that day."
        n "Today did seem a little pointless, didn't it."
        "A couple months since Sayori and I messed around with that penlight."
        s uniform sleep "Mmn... I think I will finally have an early night tonight." with dissolve
        "A couple months since... [alt_name]..."
        scene bg corridor eve with blink
        stop music fadeout 5.0
        "We haven't really talked to each other since then, Sayori and I..."
        "I know they were all shaken by what happened, but surely it's been long enough."
        "Especially now as we finished our entrance exams the other day."
        scene bg entrance
        show Sayori uniform_folded concerned_right at center
        show Nozomi side sad at center, flip:
            xpos 0.25
        show Hiroko frown at center:
            xpos 0.75
        with blink
        "Sayori and the others see me as I approach them at the entrance."
        play music Measured
        n "Kyou..."
        h "Who said you could come near us? Asswipe."
        ks frown "Sayori, can... can we talk?"
        s "..."
        n frown "We should get going." with dissolve
        s concerned "It is fine. Go on without me." with dissolve
        show Hiroko sad_side
        n sad_side "You don't have to, Sayori." with dissolve
        s uniform sleep "I said it's fine." with dissolve
        s neutral_right "Alright, Kyou... let's talk." with dissolve
        scene bg blackscreen
        show Sayori AlterEnd2
        stop music fadeout 5.0
        with blink
        "We end up walking outside, as Sayori hangs by the school gates and leans back against the wall to watch the other students filing out and heading homeward."
        "As I go to stand beside her, I glance over to her haggard-looking face."
        play music Monologue
        ks frown "S-so..."
        s "... So?"
        ks "How... how are you?"
        "She lets the question hang in the air as she draws a tired sigh."
        s side_open "In one sense, I am as fine as can be." with dissolve
        s "It took some all-night study sessions to make up for the disruption you caused, but in the end I think I navigated the entrance exams well enough."
        s "There is no telling for certain until the results come in, of course, but... I have reason to be optimistic."
        ks smile "That's... that's great, Sayori."
        "Honestly that does make me happy. And relieved."
        "If I really had fucked things up for her after what we did..."
        s body_facing_down facing_open "But every time I lay eyes on you, it reminds me how close I came to losing everything." with dissolve
        "But what she says next hits me like a dagger to the chest."
        s "I know you destroyed your penlight and related research, and abandoned your study of hypnosis in an effort to placate us, but the damage was done."
        ks surprised "But... But Sayori, I'd never hurt you! I LOVE you!"
        ks "If I knew what I was really doing to you, then- {w=1.0}{nw}"
        s facing_closed "Spare me. You knew I had misgivings about all of this. You should have taken my feelings seriously." with dissolve
        s "Instead, you entertained your warped fantasy that I was somehow interested in a relationship."
        s facing_open "You entertained it so hard, you even succeeded in creating your fantasy version of me in my own mind." with dissolve
        "She brings a hand up to hold the side of her head."
        show Sayori bg body_facing_up facing_open
        s "Trusting you to be better was my mistake, Kyou. But she..." with dissolve
        ks frown "[alt_name]..."
        "I utter her name instinctively as Sayori taps a fingertip over her temple."
        s "She was yours."
        ks neutral "Is it... is it wrong to say I miss her, Sayori?"
        "Sayori scoffs."
        s body_side side_open "You brought her into this world, Kyou." with dissolve
        s "Honestly, I hope you miss her every day."
        s side_closed "Goodbye." with dissolve
        show Sayori body_none eyes_none
        "[alt_name]... The girl I guess I really fell in love with." with dissolve
        "She really is gone for good, isn't she..."
        $persistent.alter_bad_end_1_unlock = True
    elif ending == "alter_victory":
        scene bg classroom eve with longblink
        play music Memories
        "As another school day draws to a close, I gather my things and ponder."
        play sound schoolbell
        show Sayori uniform_folded alert_neutral at center
        show Nozomi side frown_side at center, flip:
            xpos 0.25
        show Hiroko uniform_headhold2 frown_side at center:
            xpos 0.75
        h "Yeah great, now we can get out of here." with dissolve
        "It's been a couple of months since that day."
        n neutral_side "Today did seem a little pointless, didn't it." with dissolve
        "A couple months since Sayori and I messed around with that penlight."
        s uniform alert_sleep "Mmn... I think I will finally have an early night tonight." with dissolve
        "A couple months since... [alt_name]..."
        h smile_side "Oh man, yeah. Must feel great now you can finally let your hair down~" with dissolve
        s alert_happy "Mhmhmh, you would not believe how much I have been looking forward to these days, Hiroko." with dissolve
        n "..."
        scene bg corridor eve with blink
        "We had to limit our contact inside of school, for the sake of appearances."
        "But now that the entrance exams are over, \"Sayori\" has no reason to stick to her study regimen anymore."
        "We can finally start to be free with each other."
        stop music fadeout 5.0
        "But..."
        scene bg entrance
        show Sayori uniform alert_smile at center, flip
        show Nozomi side sad at center, flip:
            xpos 0.25
        show Hiroko uniform_armup smile_side at center:
            xpos 0.75
        with blink
        "As I follow [alt_name] and her friends from a discreet distance, I can't help but feel a pain in my gut."
        h "Anywho, I'm off to practice. Catch ya later~"
        s "See you."
        n neutral_side "Yeah, take care." with dissolve
        h neutral_side "Uhh..." with dissolve
        h uniform_headhold2 "Hey, Nozo, can I ask you something?" with dissolve
        n surprised_side "Huh? S-sure." with dissolve
        h nervous_side "Like, tell me to fuck off if I'm being too nosy, but you keep gettin' this look about you." with dissolve
        show Sayori alert_neutral
        h "It's like... I dunno, you always wanna be somewhere else." with dissolve
        n neutral_side "..." with dissolve
        h sleeptalk "And I mean, I totally get that, but I've never seen you like this before." with dissolve
        "As I faintly hear the conversation playing out by the shoe lockers, I almost instinctively reach into my pocket."
        h sad_side "So... geez, I dunno Nozo. I figured it was exams eatin' at you, but they're done and you're still like..." with dissolve
        h "Y'know?"
        n sad_side "U-uhh..." with dissolve
        hide Sayori
        show Sayori uniform_folded alert_smile at center
        s "You have been a little out of sorts lately, Nozomi. And as you can see, people do notice these things." with dissolve
        s alert_neutral "But as Hiroko is saying, you are among friends." with dissolve
        s alert_smile "So Nozomi, if there is anything troubling you, you have only to tell us." with dissolve
        s alert_happy "We may be able to help you see things in a new light." with dissolve
        show Nozomi sad
        "Just then, Nozomi notices my gaze upon her. And my hand still in my pocket." with dissolve
        play music Measured
        "It's enough to bring that day flooding back."
        scene bg study room eve bw
        if persistent.NewSprite == "":
                $n = Character("[nozomi_name]", image = "NozomiFlashbackOld", who_color = "#93624B")
                $ks = DynamicCharacter("kyou_name", image = "KyouSideFlashbackOld", who_color = "#4B9374")
                $s = Character("[alt_name]", image = "SayoriFlashbackOld", who_color = "#385599")
                show NozomiFlashbackOld side sad_side at center, flip:
                    xpos 0.25
                show SayoriFlashbackOld uniform_folded alert_smile at center
        else:
            $n = Character("[nozomi_name]", image = "NozomiFlashback", who_color = "#93624B")
            $s = Character("[alt_name]", image = "SayoriFlashback", who_color = "#385599")
            $ks = DynamicCharacter("kyou_name", image = "KyouSideFlashback", who_color = "#4B9374")
            show NozomiFlashback side sad_side at center, flip:
                xpos 0.25
            show SayoriFlashback uniform_folded alert_smile at center
        with flash
        s "I understand completely that we cannot move on without your full co-operation, Nozomi."
        n frown_side "My co-operation? Surely you mean KYOU's co-operation!" with dissolve
        n sad "Kyou, please... I'm begging you again, we can't go on like this." with dissolve
        n "You HAVE to snap her out of it now or her life's work is ruined!"
        n sad_closed "I... I-I can't let you do this to her!" with dissolve
        n "Oh my god w-why aren't you stopping this!?"
        n "You told me you loved Sayori. You said you'd never hurt her."
        n sad "S-so why..." with dissolve
        ks frown "Because you still don't get it, Nozomi. [alt_name] really isn't Sayori like you think she is."
        ks "I'm not going to just kill her like you want."
        s uniform alert_neutral_right "I will take it from here, Kyou." with dissolve
        show NozomiFlashback sad_side
        s alert_neutral "Now Nozomi, I cannot pretend to understand what you are going through... but you need to accept Sayori, as you know her, is gone." with dissolve
        n frown_side "T-this is perverse. Kyou, make her stop!" with dissolve
        s "And I would prefer us all to complete the rest of our high-school lives as we were. So I would like you to consider something."
        s alert_sleep  "Kyou's hypnosis created me. Whether you think I am a separate entity or merely a re-alignment of Sayori's thought process, you must have no doubt as to his power." with dissolve
        n sad_side "... Huh?" with dissolve
        s "Sayori, in her right mind, cannot possibly have wanted for this to happen to her. I am sure we all agree this is the case."
        s alert_neutral "So then if Kyou's hypnosis, aided no doubt by his penlight, can do such a thing to Sayori, could it not do the same to anyone?" with dissolve
        s alert_annoyed "... To you, perhaps?" with dissolve
        ks surprised "Wha- {w=0.5}{nw}"
        n shocked_side "What?!" with dissolve
        s uniform_handup "Just imagine, Nozomi. You stand here now, strenuously objecting to my very existence as you decry my \"perverse\" nature..." with dissolve
        show NozomiFlashback sad_side
        s alert_neutral "... when all of a sudden a strand of light flashes before your eyes." with dissolve
        s alert_concerned "Before you can say more you find yourself staring at the light, captivated, as you dimly register a young man's voice." with dissolve
        s alert_sleep "That voice begins to caress the corners of your mind as your objections die on your lips." with dissolve
        s uniform alert_sleeptalk "All too soon you feel your eyelids begin to droop as the distraction of the light gives way to a comforting darkness..." with dissolve
        s alert_neutral "Eventually, your eyes re-open and..." with dissolve
        s alert_happy "Oh! What were you so upset at [alt_name] for? Everything is wonderful~" with dissolve
        s alert_smile "Perhaps you would have forgotten all about this \"Real Sayori\" nonsense by then." with dissolve
        n shocked_side "W-w-w-what are you saying?!" with dissolve
        ks surprised "[alt_name], you can't be serious! I can't..."
        s alert_laugh "Ahahaha, I have little to doubt that it would be very possible, Kyou." with dissolve
        n frown_side "No... no, I won't let you scare me like that." with dissolve
        n "Hypnosis it... i-it..."
        s uniform_folded alert_smile "\"Doesn't work that way?\" Because your desire to be hypnotized and follow suggestions determines its success?" with dissolve
        s alert_neutral "After all that has happened, Nozomi, are you sure you want to test that hypothesis?" with dissolve
        n "Uh..."
        s alert_smirk "And let us be plain with each other. When it comes to you and hypnosis, you do appear to have a rather... intimate relationship." with dissolve
        n blush "I... I don't know what you're talking about!" with dissolve
        if persistent.NewSprite == "":
            show SayoriFlashbackOld:
                linear 1.0 xpos 0.45
        else:
            show SayoriFlashback:
                linear 1.0 xpos 0.45
        s "You don't? Did I misremember just how eager you were to volunteer for that hypnotist show last year?"
        if persistent.NewSprite == "":
            show SayoriFlashbackOld:
                xpos 0.45
        else:
            show SayoriFlashback:
                xpos 0.45
        s "How you were practically chomping at the bit to follow Satoshi's directions?"
        n "S-stop it!"
        if persistent.NewSprite == "":
            show SayoriFlashbackOld:
                linear 1.0 xpos 0.4
        else:
            show SayoriFlashback:
                linear 1.0 xpos 0.4
        s "And my, how your eyes lit up when Kyou declared his intent to do a hypnosis show of his own. You simply could not help yourself but get involved, could you?"
        if persistent.NewSprite == "":
            show SayoriFlashbackOld:
                xpos 0.4
        else:
            show SayoriFlashback:
                xpos 0.4
        s "Not even the fact that it was your \"stalker\" was going to deter you."
        show SayoriFlashback:
            linear 1.0 xpos 0.3
        show NozomiFlashback at flip:
            linear 1.0 xpos 0.15
        s "... No. Perhaps that conceit made it MORE exciting for someone like yourself."
        scene Sayori_Alter_Confrontation2 with blink
        n "Shut up! G-get away from me!"
        show Sayori_Alter_Confrontation2 nozomi_bw
        s "Because Nozomi, I have known you for almost three years and, dear me, you are not as subtle as you think you are." with dissolve
        show Sayori_Alter_Confrontation2 worried_bw
        s "If hypnosis is a question of desire, then we have found the ideal conditions for you, my friend." with dissolve
        s "There is very much a part of you that wants just such a thing as I suggest. Yearns for it, even."
        show Sayori_Alter_Confrontation2 scared_bw
        s "Something so... fundamentally twisted and immoral that no right-thinking person would ever wish it upon themselves." with dissolve
        show Sayori_Alter_Confrontation2 grin_bw
        s "And yet, Nozomi, I can sense the burgeoning arousal behind those frightened eyes of yours." with dissolve
        show Sayori_Alter_Confrontation2 nozomi_blush_bw
        s "You truly are a most peculiar little hussy." with dissolve
        play sound bodyimpact
        scene bg blackscreen
        n shocked_side "I SAID GET AWAY!" with vpunch
        $ persistent.sayori_alter_confrontation2_unlock = True
        scene bg study room eve bw
        show NozomiFlashback side sad_side blush at center, flip:
            xpos 0.25
        show SayoriFlashback uniform_folded alert_smirk at center
        with dissolve
        n "Haah... h-haaah... o-oh my god... Sayori, you..."
        n sad_closed noblush "I don't... I don't know who you are anymore!" with dissolve
        s uniform alert_laugh "Ahahahaha! Nozomi, I have been telling you all day long, you silly girl~" with dissolve
        show NozomiFlashback sad_side
        s alert_happy "I am [alt_name]. And Kyou and I will not entertain you threatening my existence any longer." with dissolve
        s alert_smile "So now that we have come to an understanding, let us return to my proposition." with dissolve
        s "You are not to speak a word of this to anyone. Treat me publicly as you would Sayori, and address me only by her name while we are with company."
        s alert_neutral "If I learn that you have attempted to undermine me in any way, you will... \"see the light\", so to speak." with dissolve
        s uniform_handup "And Nozomi, we can do so much more to your mind than merely force acceptance upon you. You could come to believe all manner of odd things." with dissolve
        s alert_smile "... Unless you would like that?" with dissolve
        s uniform_folded alert_laugh "Ahahaha, no? Well, then." with dissolve
        n sad "Kyou... please..." with dissolve
        s alert_annoyed "Eyes on me, Nozomi. Do I have your co-operation?" with dissolve
        n sad_side "..." with dissolve
        n sad_closed "{size=16}Y-... yes...{/size}" with dissolve
        s alert_smile "Mhmhm, I knew you would come around, Nozomi." with dissolve
        s alert_annoyed "Now get out of my sight." with dissolve
        if persistent.NewSprite == "":
                $n = Character("[nozomi_name]", image = "Nozomi", who_color = "#93624B")
                $ks = DynamicCharacter("kyou_name", image = "KyouSide", who_color = "#4B9374")
                $s = Character("[alt_name]", image = "Sayori", who_color = "#385599")
        else:
            $n = Character("[nozomi_name]", image = "Nozomi", who_color = "#93624B")
            $s = Character("[alt_name]", image = "Sayori", who_color = "#385599")
            $ks = DynamicCharacter("kyou_name", image = "KyouSide", who_color = "#4B9374")
        scene bg entrance
        show Sayori uniform alert_smile at center
        show Nozomi side sad at center, flip:
            xpos 0.25
        show Hiroko uniform nervous_side at center:
            xpos 0.75
        with flash
        h "... Nozo?"
        n shocked_side "Ah!" with dissolve
        n laugh "E-everything's fine! I guess the exam really did take a lot out of me." with dissolve
        h neutral_side "Yeah?" with dissolve
        n smile_side "Yeah. I'm sorry for making you worry." with dissolve
        n happy "Don't overdo it on the courts, okay?" with dissolve
        h uniform_armup happy_side "Kyayaya! Yeah, right~" with dissolve
        hide Hiroko
        show Nozomi smile_side
        "As Hiroko skips away, Nozomi and [alt_name] share strained smiles." with dissolve
        s alert_happy "It relieves me to know you are doing well after all, Nozomi." with dissolve
        n happy "O-of course, Sayori. I just need to be going now." with dissolve
        s alert_smile "So you do. See you tomorrow." with dissolve
        stop music fadeout 10.0
        scene bg street1 eve
        show Sayori alert_happy
        with blink
        "As we walk home together, [alt_name] lets out a purr as she stretches her arms upward."
        s "Mmmn, are you not excited, Kyou?"
        queue music Eons
        "As soon as we finished our exams, [alt_name] started to slacken off on her Sayori impersonation. Especially out of the classroom."
        s alert_smile "My evenings and weekends are free again, and I have such a good feeling about our immediate futures~" with dissolve
        ks smile "Y-yeah..."
        s uniform_folded alert_happy "Soon I will be able to cast my shackles completely aside and we can truly take our relationship further..." with dissolve
        s alert_concerned_right "... And yet you look glum, my love, and that does not sit well with me." with dissolve
        s alert_neutral_right "Would you like to talk about it?" with dissolve
        "I sigh, as my walking pace slows while I look to her."
        ks sigh "It's just... do you think you could lay off Nozomi now?"
        s alert_surprised_right "Lay off her? Whatever for?" with dissolve
        ks "She... she can't do anything to either of us, [alt_name]. You get that, right?"
        s uniform_handup alert_neutral "Hmm..." with dissolve
        s alert_neutral_right "I do suppose her threat has passed. She will never convince you to return Sayori to her now..." with dissolve
        ks neutral "Right..."
        s alert_annoyed "And no one will ever find her credible if she attempted to reveal my secret." with dissolve
        s alert_sleep "With the possible exception of Hiroko, for all the good that would do her." with dissolve
        s "So..."
        s uniform_folded alert_laugh "Very well, my love! I shall retract my claws." with dissolve
        "Spoken so cheerfully. As if we were talking about a missing candy bar and not intimidating the fuck out of Nozomi."
        "It's almost as if..."
        ks frown "Fuck, did you even think we had to keep her in line like that? It almost sounds like you were doing it for fun."
        s alert_smile_right "Oh my, that is not why we did it, but yes it WAS fun!" with dissolve
        s alert_happy "Having her struggle to check her fear of an impending brainwashing against keeping the masquerade going of her own free will, lest she lose it." with dissolve
        s alert_giggle "You could see it play out from the contortions on her face... " with dissolve
        s "It was exquisite!"
        s alert_smirk "Certainly kept me amused during some of our duller class periods." with dissolve
        "It takes me a moment to recover from my shock to speak, as I realize my mouth is hanging open while I look at her."
        ks surprised "[alt_name], what..."
        show Sayori alert_smirk_right
        ks "W-what the FUCK?!" with dissolve
        s alert_rolleyes "Oh, as if you care what happens to Nozomi anymore." with dissolve
        s alert_irritated "I am quite certain you are over that girl by now." with dissolve
        ks "B-but you two were close friends weren't you?"
        "[alt_name] simply smiles and wags a finger at me."
        s uniform alert_smile_right "She was Sayori's friend. Although she could have been mine as well, had she wished it." with dissolve
        s alert_rolleyes "I am normally not one for holding grudges but, well... that hussy DID try to have me killed." with dissolve
        ks sigh "For fuck's sake, [alt_name], you gotta let that go."
        show Sayori alert_neutral_right
        ks "I mean, shit, you said we had to keep her in line so she wouldn't try anything. That's why I let you carry on like that." with dissolve
        ks "Were you lying to me about that?"
        s alert_surprised_right "Oh Kyou, no there was no lie." with dissolve
        s "It was absolutely imperative that Nozomi was cowed, lest she make some kind of emotional appeal and tempt you into \"doing the right thing\" as she would put it."
        ks frown "But you're gonna stop now?"
        s alert_smile_right "As I said, her threat has passed." with dissolve
        ks "Why? You don't think she can't convince me now?"
        ks "I mean, shit, she might not even need to convince me the way things are going..."
        "It's a pretty direct threat, and I expect [alt_name] to freak out on me."
        show Sayori alert_happy
        "But instead she simply smiles serenely?" with dissolve
        s "Kyou, I think you know very well that returning Sayori now would be a terrible idea."
        ks "Really, [alt_name]?"
        s alert_laugh "Really!" with dissolve
        s alert_smile_right "After all, we had our entrance exam just the other day, did we not?" with dissolve
        ks "We... did, yeah."
        s uniform_handup "And Kyou, need I remind you how so very hard I have been studying for the occasion?" with dissolve
        "She doesn't. I know she hasn't learned a damn thing about her subjects these past couple months."
        "Because that was the plan. She'd flunk her exam and \"settle\" for a lesser college. The same place I'd be going."
        "If I brought Sayori back into the world now, she'd be coming back to her life's ambitions in tatters."
        s alert_sleep "I can see from your face that you comprehend what I am saying, Kyou." with dissolve
        s alert_neutral_right "Our parents cannot afford to pay for her to simply try again next year, so her life's work will have been absolutely for nothing." with dissolve
        s alert_concerned_right "She will be devastated, and she will only have yourself to blame." with dissolve
        s alert_sleeptalk "So there is no going back, Kyou. Not really." with dissolve
        s alert_smile_right "You made your choice. You chose me, and for that I will always be indebted to you, Kyou." with dissolve
        s uniform "So please, do not dwell on the past. On Sayori. On Nozomi." with dissolve
        s "Why waste our short lives fretting over what has been done when we can make the most of our future together?"
        scene bg blackscreen with dissolve
        "Just then, [alt_name] moves to embrace me fully at my side."
        "She notices my lack of response, and only squeezes me tighter as she rests her head on my shoulder."
        scene cg sayori alter bad end 2 with dissolve
        s uniform_folded "Worrying accomplishes nothing, my love. Let us instead focus on what will make us happy."
        s alert_laugh "Ahaha, I mean, YOU taught me that!"
        s "So forget the troubles that brought us here and look ahead to where we are going, because... because..."
        s "Aaaah, we are going to have so much fun together, Kyou Koyama~ {font=DejaVuSans.ttf}♥{/font}"
        $persistent.alter_bad_end_2_unlock = True
        jump Credits
    elif ending == "alter co-op":
        pause 1.0
        scene bg classroom eve with longdissolve
        play music Memories
        "As another school day draws to a close, I gather my things and ponder."
        play sound schoolbell
        show Sayori uniform_folded alert_neutral_right at center
        show Nozomi side neutral_side at center, flip:
            xpos 0.25
        show Hiroko uniform_headhold sleeptalk at center:
            xpos 0.75
        h "Man, why'd they even make us come to school today. We didn't do shit." with dissolve
        "It's been a couple of months since that day."
        show Hiroko uniform_headhold2 neutral_side
        s uniform_handup alert_irritated "We are in a post-examination wilderness. It was inevitable that we would have little to do." with dissolve
        "A couple months since I messed around with that penlight and gave Sayori an alternate personality."
        n smile_side "It is what it is. But now we're about to get a lot busier, huh?" with dissolve
        h uniform_armup happy "Hells yeah! The weekend starts here~" with dissolve
        "I destroyed the penlight after all the trouble it caused. But even so, Sayori wanted me to leave her alone while she \"dealt with the consequences of my decision\"."
        h happy_side "You with me, sis?" with dissolve
        "I'd want to at least ask how she's been dealing with things since the incident but, well..."
        s alert_concerned_right "Personally I see little to celebrate, but... I did promise you all." with dissolve
        "... I kind of already know."
        show Sayori alert_neutral
        show Hiroko uniform smile_side
        n happy "So, shall we go?" with dissolve
        s uniform alert_neutral "One moment. There's that other promise I made to someone." with dissolve
        show Hiroko uniform neutral_side
        n neutral_side "Oh. Right, of course." with dissolve
        s alert_concerned "Yes. I'm going to talk to him; I shall just be a moment." with dissolve
        s alert_neutral_right "... Kyou?" with dissolve
        hide Nozomi
        show Nozomi front2 neutral at center:
            xpos 0.25
        show Hiroko frown
        ks surprised "H-huh?! What?!" with dissolve
        "Sayori just sighs at me as I react to her approaching my desk."
        s uniform_folded alert_rolleyes "Oh, drop the faux surprised act. We know perfectly well that you eavesdrop on our conversations." with dissolve
        "I mean... yeah, I kinda know what's going on. The three of them are having a karaoke night to unwind now that our entrance exams are done with."
        show Nozomi neutral_right
        h uniform_headhold2 "H'yeah, just like we all know you ain't doing shit tonight." with dissolve
        ks sigh "Yeah. And I thought you'd prefer it that way."
        s alert_annoyed_right "You would be correct." with dissolve
        show Hiroko neutral_side
        s alert_irritated "{size=16}... What? No, that was not mean of me to say. I was merely being matter of fact with...{/size}" with dissolve
        "After muttering to herself for a moment more, Sayori lets out another sigh."
        s alert_neutral_right "Kyou, you know better than anyone that it is not solely down to me these days." with dissolve
        ks neutral "Yeah..."
        s uniform alert_sleeptalk "So... look, I am not going to sugarcoat this. To me, you will always be the man who ruined my life. Just as you will always be the man who saved hers." with dissolve
        show Hiroko uniform neutral
        show Nozomi neutral
        s alert_concerned_right "And she would appreciate it very much if you joined us tonight." with dissolve
        stop music fadeout 5.0
        scene bg blackscreen with longdissolve
        "[alt_name]..."
        "Well of course I was curious. Hell, I've barely stopped thinking about the girl who loved me."
        "I guess she's still thinking of me too..."
        scene bg karaoke
        queue music Inspiration
        show Sayori uniform_handup alert_sleeptalk at center
        show Nozomi side smile_side at center, flip:
            xpos 0.25
        show Hiroko uniform neutral_side at center:
            xpos 0.75
        with longdissolve
        s "I am trying to remember how long it has been since I was last in one of these places."
        n happy "Ehehe, sounds like it's been too long if you ask me~" with dissolve
        s uniform alert_smile "Perhaps. But you will forgive me if my vocals do not amount to much." with dissolve
        show Sayori alert_neutral_right
        h uniform_headhold2 smile_side "Ehh, don't worry about it. I'm pretty good at tunin' out shitty singing." with dissolve
        show Nozomi neutral_side
        h happy_side "Right, Nozo?" with dissolve
        hide Nozomi
        show Nozomi front2 pout at center:
            xpos 0.25
        n "... No comment." with dissolve
        h uniform_armup happy "But yeah, we're gonna have a blast, just the three of us. You'll see~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        show Hiroko smile_side
        show Nozomi neutral_right
        show Sayori uniform_handup alert_surprised at flip
        s "The... the three of us, you say?" with dissolve
        show Hiroko neutral_side
        s alert_smile "Aren't you forgetting someone?" with dissolve
        h surprised_side "Huh?" with dissolve
        h uniform_headhold2 pain "O-oh, fuck, you're right." with dissolve
        show Nozomi side smile_side at flip
        h nervous_side "Sorry 'bout that, [alt_name]. You want in on this too, don't ya?" with dissolve
        "Wait, what did she just say?"
        s uniform_folded alert_laugh "Ahaha, you know I do~" with dissolve
        "Then that means..."
        h uniform_armup happy "Haha, fuck yeah! The FOUR of us!" with dissolve
        $sayori_name = "[alt_name]"
        show Sayori alert_surprised_right
        show Nozomi neutral
        ks surprised "[alt_name[0]]-[alt_name]? Is it really you?" with dissolve
        s alert_laugh "Kyouuuu!" with dissolve
        h uniform frown "Ugh... the five of us." with dissolve
        #This might be a good spot for a CG
        "I feel [alt_name]'s sudden embrace as she unashamedly hugs me in front of everyone."
        "This warmth coming from her... it was completely absent just seconds ago."
        "Even if I didn't already know the truth about Sayori, there'd be no doubt in my mind that there's a completely different woman here with me now."
        "[alt_name]... goddamn, I missed you so much!"
        s alert_giggle "Oh, I am so glad you came, my love! It's been far too long!" with dissolve
        ks smile "Y-yeah, it's... man, it's great to see you again, [alt_name]."
        s alert_happy blush "Mhmhmh~ I have waited so long for this moment, Kyou!" with dissolve
        ks smile "Maybe a little too long, huh?"
        show Sayori alert_smile_right noblush
        "I mean, I know what I told Sayori when I last hypnotized her all those weeks ago; about how she and [alt_name] could co-exist in the same headspace." with dissolve
        "But I don't know. Did I do it right? Did I give Sayori too much power over her alter if she can just shut her out most of the time?"
        ks "Is Sayori treating you okay?"
        "I have to know. And to my question, [alt_name] sighs softly."
        s alert_rolleyes "Sayori is... well, she is still a bit raw about the whole pulling out of med school thing." with dissolve
        hide Nozomi
        show Nozomi side frown_side at center, flip:
            xpos 0.25
        show Hiroko neutral_side
        n "I mean, can you blame her?" with dissolve
        h uniform_headhold2 confused_side "Yeah, [alt_name]. I like you an' all, but that's gotta be rough for her." with dissolve
        s uniform_handup alert_concerned "Oh, of course. I just hope she does not dwell on it too much." with dissolve
        s alert_smile "If she and I co-operate, I believe there will be much joy in our lives ahead~" with dissolve
        show Hiroko neutral_side
        n sad_closed "I do hope you two can work things out, I really do." with dissolve
        show Sayori alert_neutral_right
        n smile_side "But in the meantime... do we want to get started here?" with dissolve
        hide Sayori
        show Sayori uniform_handup alert_laugh at center
        "[alt_name] turns her attention to Nozomi, then laughs as she finds a microphone is being handed to her." with dissolve
        s alert_smile "Of course, Nozo~ So does this mean what I think it means?" with dissolve
        show Hiroko smile_side
        n laugh "You know it! I'm dying to hear you sing!" with dissolve
        s uniform_folded alert_laugh "Ahahaha, then I shall be happy to indulge you, my friend~" with dissolve
        "We all watch as [alt_name] puts the mic to her lips, before she frowns a little in thought."
        show Nozomi smile_side
        s alert_neutral "Ah, no, where are my manners. Did you want to go first, Sayori?" with dissolve
        s alert_sleep "..." with dissolve
        s alert_laugh "Ahahaha, so is that how it's going to be?" with dissolve
        h confused_side "What did she say?" with dissolve
        show Sayori alert_smirk at flip
        s "She told me she wished to take notes on my performance so she could better it on her turn." with dissolve
        show Nozomi happy
        h smirk_side "Oh man, that DOES sound like her." with dissolve
        s alert_laugh "Right? So okay then, Sayori. If you love learning so much..." with dissolve
        "Picking up the remote from the table, [alt_name] quickly thumbs over the controls and hits the randomizer."
        show Nozomi smile_side
        s uniform_handup alert_giggle "Allow me to be your teacher!" with dissolve
        scene bg blackscreen with longdissolve
        "We must have been singing for like an hour."
        "I end up taking the mic a couple of times, with [alt_name]'s encouragement, and even Sayori was willing to sing a couple of times. At least I think that was her..."
        "For a little while, it seems like all our problems are forgotten."
        scene bg karaoke
        show Sayori uniform_handup alert_happy at center
        show Nozomi side smile_side at center, flip:
            xpos 0.25
        show Hiroko uniform_armup happy at center:
            xpos 0.75
        with dissolve
        h "Damn, Nozo! You almost hit a couple notes, that time~"
        n laugh "Ahahaha, yeah that was pretty fun!" with dissolve
        "With a giggle, Nozomi reaches out for the phone in the room."
        show Sayori alert_smile
        show Hiroko uniform smile_side
        n smile "Now I don't know about you guys, but I need another drink~" with dissolve
        show Nozomi smile_side
        s alert_laugh "Ohhh, I'll have a melon soda!" with dissolve
        h happy_closed "Yeah, get me one too~" with dissolve
        n happy "Sure!" with dissolve
        show Sayori alert_smile_right
        show Hiroko neutral
        n neutral "And what about you, Kyou?" with dissolve
        "There's a definite drop in enthusiasm when she asks me."
        "Better not rock the boat here."
        ks smile "Y-yeah, that's good for me too."
        n smile_side "Alright, that makes things easy~" with dissolve
        "As Nozomi starts the call, I notice Sayori... no, [alt_name] looking at me."
        stop music fadeout 15.0
        "Being with her again, after all this time of Sayori shutting me out, has been wonderful."
        ks "So, uh... [alt_name]?"
        "But enough is enough. I can't live like this, not after tonight."
        s alert_laugh "Kyou! Yes! We simply must talk!" with dissolve
        ks "Yeah. I was wondering..."
        "I have to know more about [alt_name] and Sayori. But more importantly..."
        s alert_giggle "Don't be shy on me now, Kyou~ You can talk to me about anything." with dissolve
        ks neutral "I was wondering about... like, us?"
        show Nozomi neutral
        s alert_surprised_right "\"Us\"?" with dissolve
        ks sigh "Do we have a future? I mean, like... me and you?"
        s alert_smile_right "..." with dissolve
        show Nozomi neutral_side
        show Hiroko neutral_side
        s uniform alert_smile "Nozomi. Hiroko. Can you entertain yourselves for a little while?" with dissolve
        s alert_smile_right "Kyou and I need a few moments to ourselves..." with dissolve
        scene bg shopping night with blink
        queue music Eons
        "So [alt_name] and I step outside."
        show Sayori uniform_folded alert_neutral at center
        s "Kyou..." with dissolve
        s alert_smile_right "I will always be ever so intensely fond of you. I do hope you know that." with dissolve
        s alert_happy blush "As it is, it is taking every ounce of restraint to keep myself from smothering you in a million kisses~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        ks smile blush "[alt_name]..."
        show Sayori alert_smile_right
        "I hold her hands gently as we look to each other, and for a moment the idea of talking is lost in those beautiful blue eyes of hers." with dissolve
        "Instead, my thoughts wander as I realize we're not too far from where we started our date, all those weeks ago."
        "And as we start to embrace, as her lips come closer to mine, I have to wonder if she's thinking the same..."
        s alert_annoyed_right "N-now what do you two think you're doing?" with dissolve
        show Sayori noblush
        "I separate with a gasp as I see the affection rapidly drain out of her face, quickly replaced with a stony, judgmental glare." with dissolve
        $sayori_name = "Sayori"
        s alert_irritated "{size=16}I gave my permission to talk to him, not press our lips to his face.{/size}" with dissolve
        "I take a step back, bracing myself before I realize Sayori is more intent on turning her ire inward."
        stop music fadeout 10.0
        $sayori_name = "[alt_name]"
        s alert_rolleyes "{size=16}Oh please, you are such an unbelievable party-pooper.{/size}" with dissolve
        "I watch, my fear giving way to fascination as I watch this girl's face and body contort this way and that as she appears to argue quietly yet furiously with herself."
        $sayori_name = "Sayori"
        queue music Measured
        s alert_annoyed_right "{size=16}Really, [alt_name]? Do you sincerely think I would sit idly while you indulged yourself with the man who ruined my life?{/size}" with dissolve
        $sayori_name = "[alt_name]"
        s uniform_handup alert_pout_closed "{size=16}Did he, though? In spite of your ridiculous commitment to study your chances of achieving your ambitions were still rather slim as I understand it.{/size}" with dissolve
        s alert_pout "{size=16}{cps=20}So to have spared you from a lifetime of perpetual stress and anxiety-{/cps}{/size}{w=1.0}{nw}" with dissolve
        $sayori_name = "Sayori"
        s uniform alert_irritated "Oh, no no no, [alt_name], you are not going to pretend any of this was for my benefit." with dissolve
        s uniform_folded "You are not the one who had to sacrifice their life's ambition. You have barely even HAD a life!" with dissolve
        "Her raising her voice makes me spare an anxious glance around us."
        $sayori_name = "[alt_name]"
        s uniform_handup alert_rolleyes "I feel that is a low blow, Sayori-{w=1.0}{nw}" with dissolve
        $sayori_name = "Sayori"
        s uniform_folded alert_angry_right "And YOU were not the one having that devastating conversation with my parents the other week about how I was \"crumbling under all the pressure\"." with dissolve
        "Like, I figured Sayori was keeping [alt_name] hidden so no one would think she's crazy, yet they're doing this right here in the street."
        "Is anyone else watching this?!"
        s uniform alert_angry "You did not have to relate our altered plans to have me forego my ambitions, abandon EVERYTHING I have worked for to instead attend a..." with dissolve
        s "A..."
        show Sayori uniform_folded alert_irritated
        "She grimaces visibly before finishing the sentence through her teeth." with dissolve
        s "... junior college."
        s alert_annoyed_right "So you will forgive me, [alt_name], if I come across as a little PISSED OFF!" with dissolve
        s alert_irritated "..." with dissolve
        stop music fadeout 10.0
        ks surprised  noblush "U-ummm... Sayori?"
        s "..."
        ks "... [alt_name]?"
        "Her silence might actually be worse than the shouting, as I can see her eyebrows tense and strain."
        "I can only assume they're taking their argument behind closed doors while I stand awkwardly by."
        show Sayori alert_sleep
        "So I wait... until the frown starts to fade from her face, and it gives way to a pained expression." with dissolve
        $sayori_name = "[alt_name]"
        play music Diary
        s alert_concerned "Kyou... I want to thank you for everything you have done for me. Truly." with dissolve
        s alert_concerned_right "But Sayori will never tolerate our love. Certainly not after I made her give up her own dream." with dissolve
        "I can feel my heart sink at her words, but... it was already obvious, wasn't it?"
        "Sayori may understand [alt_name] had a right to exist. And maybe the two of them will figure things out between themselves in time."
        "But she'll never forgive me for putting her in such a state to begin with."
        "I was a fucking idiot if I thought I could have anything with [alt_name]."
        ks sad "We have to break up. For real this time."
        "[alt_name] looks at the pain that must be etched on my face..."
        scene cg sayori alter coop end with blink
        "... and she leans in to plant a delicate kiss upon my lips."
        "My heart jolts in my chest, but only to sink again just as quickly."
        "After all, if Sayori's allowing her to do this then it can only be for one reason..."
        s "I will always carry you in my heart... Kyou Koyama."
        scene bg shopping night with blink
        "She leaves me to rejoin her waiting friends, and I'm in no state to follow her."
        "I don't know if I'll ever see her again, but..."
        $persistent.alter_coop_end_1_unlock = True
        scene bg blackscreen with longdissolve
        "[alt_name]... I hope you can be happy..."
        jump Credits
    elif ending == "shaken":
        scene bg classroom day with longdissolve
        play music Eons
        "The following school day I set my things down at my desk, ready to start a new week as I think to myself."
        show Hiroko frown_side at center, flip:
            xpos 0.25
        show Nozomi side sad_side at center:
            xpos 0.5
        "It's been a couple nights since..." with dissolve
        n "Good morning, Hiroko. How are you?"
        "Since I took Sayori back into trance in Nozomi's room, and removed every suggestion I made to her mind over the last few days."
        h sad_side "Ehh... Man, I dunno. You really think I did okay?" with dissolve
        "With Nozomi watching me the whole time, she made sure Sayori wasn't going to snap back into her altered state, or suddenly fall asleep, or suffer anything else my hypnosis caused."
        n frown_side "I guess I can't really say for sure, but you got pretty far didn't you? I'm sure someone was impressed." with dissolve
        "Everything should be back to normal now. Almost."
        h sleep "Yeah. Guess we'll see in a couple months, huh." with dissolve
        show Sayori sleep at center:
            xpos 1.1
            linear 1.0 xpos 0.75
        pause 1.0
        show Nozomi neutral_side at flip
        show Hiroko neutral_side
        s "Mmn... good morning." with dissolve
        "Even after my assurances, Sayori still seemed pretty shaken by the end of it all."
        n sad_side "Sayori... are you doing okay?" with dissolve
        s uniform_handup sleeptalk "I slept pitifully, if that is what you mean." with dissolve
        "And I guess by the end of it, so was I."
        n sad_closed "I mean... sort of?" with dissolve
        show Nozomi neutral
        h uniform_headhold2 confused_side "H'yeah, what happened to you, girl? You were a total no-show yesterday." with dissolve
        "I told them I'd stop practicing hypnosis. I even broke that stupid penlight in front of them after I was done untangling Sayori's mind."
        s uniform sleeptalk_concerned "And I really do apologize, Hiroko, but... w-well..." with dissolve
        h neutral_side "Oh, this'll be good." with dissolve
        "... But I don't know if that's enough."
        hide Nozomi
        show Sayori concerned
        show Nozomi side neutral_side at center
        n "Let's put a pin in that, okay? We'll tell you later." with dissolve
        h frown_side "Eh? What the hell gives?" with dissolve
        s concerned_right "..." with dissolve
        n frown_side "Hiroko. Later." with dissolve
        hide Sayori
        hide Nozomi
        hide Hiroko
        "The way she still looks at me..." with dissolve
        scene bg blackscreen with longdissolve
        "... Is she still afraid of me?"
        scene bg classroom day
        show Hiroko neutral_side at center, flip:
            xpos 0.25
        show Nozomi front neutral_left at center:
            xpos 0.5
        show Sayori neutral at center:
            xpos 0.75
        play sound schoolbell
        with longdissolve
        "I need to wait until lunchtime, but as soon as the bell rings I'm ready to make my move."
        n "So... rooftop then?"
        "I have to know."
        h uniform_headhold2 sleeptalk "Sure. Just dyin' to know what all this drama's about, so..." with dissolve
        show Hiroko confused
        show Nozomi frown
        show Sayori surprised_right
        ks confused "S-Sayori. I was thinking we could... t-that we could talk again some time?" with dissolve
        "I'll just go to her now. Ask her straight up."
        h frown_side "... An' another thing, what's this \"school project\" shit about, huh? You wanna talk about that?" with dissolve
        s uniform_handup concerned "Hm? I... sorry, I have no idea..." with dissolve
        show Sayori concerned_right
        show Hiroko frown
        stop music fadeout 5.0
        ks sad "Please, Sayori? Just tell me we can meet up soon." with dissolve
        s uniform "..." with dissolve
        "There's that look again..."
        play music Monologue
        s sleeptalk "Kyou, I-I..." with dissolve
        show Sayori sleeptalk_concerned at flip
        s "I just want to forget..." with dissolve
        ks "{cps=15}Sayori- {/cps}{w=1.0}{nw}"
        n front2 determined "There, you happy now? All you're ever going to do is hurt us." with dissolve
        n angry "{cps=20}Now for the last time leave her {/cps}{nw}" with dissolve
        extend "ALONE!" with vpunch
        hide Hiroko
        hide Nozomi
        hide Sayori
        "And with that, the three of them take off out of the classroom, leaving only the fading sounds of their voices as they move out of reach." with dissolve
        h "{size=14}Seriously, what the fuck's going on around here?{/size}"
        n "{size=14}Kyou. Kyou's what's been going on, that's all...{/size}"
        # "Maybe I could find her on the roof, get her talking while everyone else goes back down, then maybe I'd have a couple minutes to..."
        "Maybe I could try again another day. Talk to her after her study club's over and everyone else has gone, then maybe I'd have a minute to..."
        "Oh, who am I kidding. She won't want to talk to me again after this."
        "It's hopeless."
    elif ending == "betrayal":
        scene bg classroom day with longdissolve
        play music Eons
        "The following school day, I set my things down at my desk, ready to start a new week."
        show Hiroko frown_side at center, flip:
            xpos 0.25
        show Nozomi side sad_side at center:
            xpos 0.5
        "And as I look up, I see Nozomi file in with her other friend..." with dissolve
        n "Morning, Hiroko. How are you?"
        "Nozomi... I can't wait to speak with you again."
        h sad_side "Ehh... Man, I dunno. You really think I did okay?" with dissolve
        "And yet, I can't get what happened with Sayori out of my head."
        n frown_side "I guess I can't really say for sure, but you got pretty far didn't you? I'm sure someone was impressed." with dissolve
        "She didn't trust me. She didn't believe that I could use the abilities my penlight afforded me responsibly. And I couldn't accept that."
        h sleep "Yeah. Guess we'll see in a couple months, huh." with dissolve
        show Sayori sleep at center:
            xpos 1.1
            linear 1.0 xpos 0.75
        pause 1.0
        show Nozomi neutral_side at flip
        show Hiroko neutral_side
        s "Mmn... good morning." with dissolve
        "I couldn't let her stop what I have going with Nozomi now. But man, did I really need to do what I did to her?"
        show Sayori:
            xpos 0.75
        n smile_side "Good morning, Sayori. How was your weekend?" with dissolve
        s sleeptalk "Mrrrrn... One to forget to be completely honest with you." with dissolve
        "I had something going with her too, didn't I? It almost felt like we could've been..."
        show Sayori sleep
        n sad_side "Oh? Don't tell me you're having trouble sleeping again." with dissolve
        s sleeptalk "I will just have to disappoint you, Nozomi. Normal service has resumed." with dissolve
        "No, come on, Kyou. This is no time to feel guilty. You did what you had to."
        n neutral_side "But I thought... w-well, never mind for now. Let's talk about it later, okay?" with dissolve
        "Sayori's going to be fine. And I'll never hurt anyone with my hypnosis again."
        s uniform_handup neutral "Talk? Nozomi, there is nothing to discuss." with dissolve
        n sad_side "Huh? But what about..." with dissolve
        "That's all she wanted from me, and I'm going to honor that."
        s uniform sleeptalk "Let us just be seated. Homeroom is about to begin." with dissolve
        n sad_closed "Yeah..." with dissolve
        scene bg blackscreen with dissolve
        pause 2.0
        play sound schoolbell
        scene bg classroom day with longdissolve
        "Before too long the bell rings out for lunch and I look once again to Nozomi and her group."
        show Sayori neutral at center:
            xpos 0.75
        show Nozomi uniform side neutral_side at flip, center
        show Hiroko neutral_side at flip, center:
            xpos 0.25
        n "So... rooftop then?" with dissolve
        "I still want to talk to Nozomi again so bad..."
        s sleeptalk "Do as you wish. But I shall catch some z's here if that's all the same to you." with dissolve
        n sad_side "Okay, but I don't understand. Don't you want to know what's been going on with you? With the... you know?" with dissolve
        s neutral "Nozomi, I shall be plain. I am quite done with *that* business, if that is indeed what you are driving at." with dissolve
        h uniform_headhold2 confused_side "Eh? What business? Feels like I'm outta the loop on something here." with dissolve
        n sad_closed "I just want to help you!" with dissolve
        s uniform_handup sleeptalk "And I could not care less what you do with your time. To say nothing of what you do with certain..." with dissolve
        s neutral_right "... individuals." with dissolve
        show Nozomi shocked_side
        "But... wait, what's going on over there?" with dissolve
        n shocked_side "H-how did you kn... S-Sayori, I can explain!"
        h sad_side "What about me? Don't I get an explanation for this shit?" with dissolve
        show Sayori neutral
        n surprised_side "O-okay listen, it was all my idea, and I'm sorry if I upset you! I-I was just trying to help! But, Sayori..." with dissolve
        "As Sayori shrugs her shoulders, I can feel a sinking feeling in the pit of my stomach."
        show Nozomi sad_side
        show Sayori uniform sleeptalk at flip
        s "Hmm. Perhaps I can sneak into the study club room. That should offer some quietude provided no one attempts to give chase." with dissolve
        "Her mind might not be able to acknowledge it..." #, but I can see I've managed to hurt her again."
        show Sayori:
            linear 1.5 xpos 1.4
        n "{cps=15}Sayori, I... {/cps}{w=0.5}{nw}"
        show Nozomi sad_closed
        hide Sayori
        $ renpy.transition(dissolve, layer="master")
        extend "uhhh."
        "... but I can see I've managed to hurt her again."
        h uniform_headhold2 frown_side "Nozo, c'mon! What the shit is going on here? What'd you do?" with dissolve
        hide Nozomi
        show Nozomi side sad_side at center
        n "O-oh, Hiroko. Um..." with dissolve
        h confused_side "Like, what're you guys doing? This ain't like you two at all!" with dissolve
        "Damn, should I have told her to be happy about hypnotizing Nozomi behind her back?"
        n front2 sleeptalk "I know, and... I-I'm sorry, but I shouldn't talk about this with anybody else." with dissolve
        h neutral_side "You serious? You can't even tell me?" with dissolve
        "Fuck, no. I didn't want to do *anything* to her!"
        h irritated "Gawd, you never tell me anything, do ya!" with dissolve
        n side sad_side "I'm sorry. B-but this time I really can't just..." with dissolve
        "And now Nozomi's suffering for it too? I didn't want to hurt either of them, dammit!"
        h frown_side "Ugh, whatever, girl. You do what you gotta do." with dissolve
        "They don't deserve any of the trouble I've made for them, I just wanted to..."
        h sleeptalk "I'm outta here." with dissolve
        show Nozomi sad_closed
        hide Hiroko
        "... Man, I guess Sayori was right after all. I really can't use this thing of mine responsibly." with dissolve
        "But if I can't do that, where does that leave me and..."
        n front2 concerned "Kyou..." with dissolve
        "... and her?"
        n neutral "You heard all that, right?" with dissolve
        ks neutral "Yeah..."
        n side sad "What's gotten into Sayori? One minute she wanted to know how your hypnosis was effecting her, then the weekend passes and..." with dissolve
        "I can't tell her the truth, that's for sure."
        ks sad "Uh... y-yeah, I don't know. Maybe she just wants to focus on her studies again."
        show Nozomi sad_closed
        "And as Nozomi sighs to herself, my hand moves to grip the penlight I still have in my pocket." with dissolve
        n "This is all my fault, isn't it?"
        "This is the only reason she's interested in me. The only reason she's even talking to me."
        n sad_side "I really was trying to help, but... well, I guess I owe you an apology too, Kyou." with dissolve
        "But what kind of person would I be if I used this on her too?"
        n front2 concerned "I'm sorry. It looks like I messed things up for everybody." with dissolve
        "I'd only hurt her the same way I did Sayori."
        ks "Uh, don't worry about it. I think I'm going to give the hypnosis a rest, anyway."
        n surprised "Y-you are? Just like that?" with dissolve
        ks neutral "Yeah. At least for a while."
        n side neutral_side "Huh..." with dissolve
        "A silence hangs between us as Nozomi seems to gaze aimlessly out the window, obviously thinking about something."
        "Maybe she suspects there's something I'm not telling her..."
        n sad_closed "Okay, I'm going to go find my friends. Well, Hiroko anyway." with dissolve
        "In any case, I doubt she'll want anything to do with me if I'm not going to hypnotize her."
        n sad_side "God, I owe her an apology too. What a mess..." with dissolve
        hide Nozomi
        "So where does that leave me?" with dissolve
        show penlight at right with moveinright:
            ypos 0.346
        "If I can't use this thing, am I even a hypnotist?"
        "And with exams coming up, would I even get another chance to try even if this all blows over?"
        hide penlight at right with moveoutright
        "I don't know... but it feels like this is it."
        "I've blown it..."
        jump Credits
    jump Credits

label Epilogue_Con_Kyou_Sayori_Alter_Switch:
    "It's been a few weeks since that day."
    n "... As you begin to pace through these twisted corridors the light from your torches suddenly seem dimmer, barely penetrating the inky darkness in which you find yourselves."
    "A few weeks since I messed around with that penlight, and with Sayori's mind."
    h "Huh? What's with the lights? I wanna do, like, a perceiving roll!"
    "I don't know why I'm thinking about that now, though."
    play sound diceroll
    n "Sure... okay, as your eyes try to adjust you can only conclude that this darkness that envelops you is magical in nature."
    "It was a crazy time for sure. An experience that changed mine and Sayori's lives, yet..."
    h "Oh, I get it. Hey, wiz, you wanna help us out here? We can't see shit."
    "... These past few weeks might have been even crazier?"
    scene Sayori AlterEnd3 n_confused h1 h_fists h_mad s1 s_surprised
    h "HEY, EARTH TO WIZ, WE GOTTA PROBLEM HERE!" with vpunch
    play music Peaceful
    "But I guess that's enough reminiscing. I gotta get my head back in this."
    show Sayori AlterEnd3 n_neutral h_growl s_neutral
    ks casual frown "Oh what's this? The young magephobe desires my aid now?" with dissolve
    "I gotta get in character."
    show Sayori AlterEnd3 h_lowered h_frown
    h annoyed "I don't \"desire\" shit from you, I just wanna get a move on in this castle an' it's about time you were good for something." with dissolve
    show Sayori AlterEnd3 h_growl
    h angry "So like, do your fucking job, okay?" with dissolve
    "No way in hell am I letting this pipsqueak upstage me in a goddamn roleplaying game, that's for sure."
    ks casual frown "I am Shou Long, master of the blazing arts, and I will not be disrespected by some upstart assassin from the Shadow Clan."
    show Sayori AlterEnd3 h_rolleyes
    h rolleyes "Master of time-wasting, more like. You spell chuckers are all the same; buncha arrogant dickheads." with dissolve
    show Sayori AlterEnd3 h_irritated
    h dungaree_armup irritated "An' I don't care how hot you think you are, you DON'T wanna make enemies of the fuckin' Shadow Clan, 'kay?" with dissolve
    ks "Such insolence. I command the fires of hell itself, and I will not be talked down to by a mere purveyor of knife tricks."
    show Sayori AlterEnd3 h_frown
    ks "You call me \"wiz\" again and I'll illuminate these halls with your hair." with dissolve
    show Sayori AlterEnd3 h_fists h_mad
    h "Oh, you wanna throw down, huh? Fuck yeah, let's do this!" with dissolve
    show Sayori AlterEnd3 n_confused h_growl s2 s_neutral_side
    n pout "Um, not to get in your way, but the darkness you're in is going to incur some heavy accuracy penalties to your dice rolls if you try anything." with dissolve
    ks sigh "That may be a chance I'm willing to take if I get to set her on fire."
    show Sayori AlterEnd3 h_irritated
    h annoyed_side "Gawd, I wanna stab this dude so fuckin' muuuuch." with dissolve
    ks frown "In the game, you mean?"
    show Sayori AlterEnd3 h_pout
    h dungaree annoyed "... Dude, you had to ask?" with dissolve
    show Sayori AlterEnd3 h2 h_frown_side n_neutral_right s_calm
    s "Roko, Shou, contain yourselves. Your people may have suffered much at each other's hands, but we can ill afford this bickering if we are to obtain the fortune stone." with dissolve
    show Sayori AlterEnd3 s_smile_side
    s "The townsfolk are depending on us, so let us keep them in our hearts, and cast our grievances and egos aside for their sake!" with dissolve
    show Sayori AlterEnd3 n_neutral_left h_lowered h_smile_side
    h smile_side "You're talking about all the reward money when we bring it back, right?" with dissolve
    show Sayori AlterEnd3 s_rolleyes
    s "Well... The local lord has promised us a substantial bounty on the stone's return, it is true, but as for his motivations for the town..." with dissolve
    show Sayori AlterEnd3 n_neutral
    ks smile "Fine, fine, enough messing around. I want to cast dispell magic now, Nozomi." with dissolve
    show Sayori AlterEnd3 n_smile s_neutral_side
    n smile "Alright. So Shou casts his spell and the magical darkness recedes, revealing the way forward." with dissolve
    show Sayori AlterEnd3 n_glare h_neutral_side
    n frown "However, it seems you are not alone. You all hear an ominous chittering noise coming from just ahead, and it's getting louder and louder." with dissolve
    show Sayori AlterEnd3 h_frown_side
    h dungaree irritated "Oh goddammit, is it those fuckin' mind melters again? I'm gonna hurl." with dissolve
    show Sayori AlterEnd3 n_confused
    n sleeptalk "You can't tell from the noise alone. All you know is that it's getting closer." with dissolve
    show Sayori AlterEnd3 h_pout_side
    h annoyed_side "H'yeah, it's gonna be mind melters." with dissolve
    show Sayori AlterEnd3 n_neutral_right s_calm
    s "How bothersome. Perhaps they were attracted to the commotion you and Shou caused arguing just now." with dissolve
    show Sayori AlterEnd3 n_happy
    n chuckle "Mhmhm, who can say?" with dissolve
    show Sayori AlterEnd3 h_neutral_side s_neutral_side
    ks frown "Pretty sure *you* can, Nozomi. You're the one inflicting this on us." with dissolve
    show Sayori AlterEnd3 n_smile
    n smile "Me? I'm but an impartial guide to the fantasy land. Anyway, the chittering is becoming even louder, surely they're almost upon you!" with dissolve
    show Sayori AlterEnd3 h_fists h_frown_side
    h dungaree_armup angry_side "Alrighty! I draw my daggers and activate my combat stance!" with dissolve
    ks frown "I prepare a fireball spell."
    show Sayori AlterEnd3 s_calm
    s "I shall place my flute to my lips and play the melody of tranquility." with dissolve
    show Sayori AlterEnd3 n_glare h_lowered s_neutral_side
    n frown "Alright. As our heroes make ready, the chittering noise reaches a fever pitch. From the shadows emerge three large, distinctive forms, their eyes burning with evil intent." with dissolve
    n irritated "{cps=16}And now, brave adventurers, you stand facing the wrath of the deadly and merciless-{/cps}{w=1.0}{nw}"
    $multichar = "{color=FF89AB}Hiroko{/color}{color=#FFFFFF},{/color} {color=#4B9374}Kyou{/color} {color=#FFFFFF}and{/color} {color=385599}Sayori{/color}"
    $multi = DynamicCharacter("multichar", image = "KyouSide")
    show Sayori AlterEnd3 h_pout_side s_rolleyes
    multi casual frown "Mind melters." with dissolve
    show Sayori AlterEnd3 n_pout
    n pout "Well... Technically they're Orthopterrors, but yes, you got me." with dissolve
    show Sayori AlterEnd3 n_sad
    n concerned "Gosh, is this campaign really that predictable?" with dissolve
    show Sayori AlterEnd3 n_sad h_smile_side s_smile_side
    s "Given what we have gleaned from the campaign master? I have to wonder." with dissolve
    show Sayori AlterEnd3 h_pout_side
    h annoyed_side "Sides, what else is supposed to make a chitterin' noise around here?" with dissolve
    show Sayori AlterEnd3 n_happy
    n smile "Hehe. Well, they all approach and begin casting confusion on the party. But since Sayori was smart enough to play her melody you all have a plus five on your saving rolls." with dissolve
    show Sayori AlterEnd3 s_smirk_side
    s "Who is this \"Sayori\" you speak of? I am Yllaphyra Ashpetal, the bard of Thimhaven." with dissolve
    "I can't help but let out a wry chuckle."
    show Sayori AlterEnd3 n_smile h1 h_neutral s1 s_smirk
    s "My, what could possibly be funny at a time like this, Shou Long?" with dissolve
    ks smirk "Oh, I think you know."
    play sound diceroll
    "\"Yllaphyra\" grins as she takes the twenty-sided die in her hand and rolls it across the table."
    show Sayori AlterEnd3 s_smile
    s "Mhmhm, perhaps. At least my state of mind is healthier this time, both in and out of the game it seems." with dissolve
    show Sayori AlterEnd3 n_happy
    n chuckle "Oh an eighteen, very nice! Now let's see what the others have~" with dissolve
    show Sayori AlterEnd3 n_neutral_left h2 h_rolling h_neutral_side s2 s_neutral_side
    "\"Roko\" scoops up the die in her hand before I can react, although as she's about to throw it back to the table, she seems to hesitate." with dissolve
    show Sayori AlterEnd3 n_smirk
    n smirk "... What's wrong, Roko? Scared of falling into the mind melter's clutches?" with dissolve
    show Sayori AlterEnd3 h_pout_side
    h annoyed_side "Pffth, those fuckin' insects don't got a chance with Ill... whats-her-face protecting us." with dissolve
    show Sayori AlterEnd3 s_smirk_side
    s "Yllaphyra. Say it with me: \"Yllaphyra\"." with dissolve
    show Sayori AlterEnd3 h_lowered
    h rolleyes "Yeah, that." with dissolve
    show Sayori AlterEnd3 n_smile h_smile_side s_smile_side
    h smile_side "Anywho, it's so great you're doing better now, sis. You know you had me worried back then, right?" with dissolve
    show Sayori AlterEnd3 n_neutral_right s_neutral_side
    s "Yes, well... I am sorry to have worried you at all, Hiroko." with dissolve
    show Sayori AlterEnd3 s1 s_neutral
    s "I suppose there was... a certain inevitability about my failure to maintain my usual high standards." with dissolve
    show Sayori AlterEnd3 n_neutral h1 h_neutral
    "Sayori casts an awkward little glance my way as the atmosphere gets a little uncomfortable." with dissolve
    show Sayori AlterEnd3 s2 s_smile_side
    s "Ah but rest assured, I am in a much better place now. I feel I can attend to my own well-being without falling into the bad habits I possessed in junior high." with dissolve
    "Yeah, so we never told Hiroko what really happened with Sayori back then."
    show Sayori AlterEnd3 s1 s_smile
    s "And I suppose I have Kyou to thank for that." with dissolve
    "We didn't want to lie to her, of course, but it's not like we could ever explain my penlight to anyone else even if we wanted to."
    show Sayori AlterEnd3 h_awe
    h surprised "H'yeah, what a trip. I still can't believe your class project turned out to be some hypno show thingy for the culture fest. And it fuckin' helped her somehow?" with dissolve
    "So we had to bend the truth about what happened. Just a little."
    show Sayori AlterEnd3 n_neutral_right s2 s_smile_side
    s "Trust me, no one has been more surprised by Kyou than I. But involving myself in his hare-brained scheme paid off handsomely in the end." with dissolve
    ks sigh "Oh come on, \"hare-brained\"?"
    show Sayori AlterEnd3 h2 h_neutral_side
    h neutral_side "Right. You had that breakdown an' you didn't wanna bother me an' Nozo about it for some reason." with dissolve
    show Sayori AlterEnd3 s_neutral_side
    s "Hmm... Less that I felt it would be a bother. Rather, I first required a fresh perspective on my situation, and Kyou was there to provide it." with dissolve
    show Sayori AlterEnd3 n_neutral_left h1 h_neutral
    h neutral "Hmm..." with dissolve
    "I'm not sure if Hiroko totally buys what we sold her."
    ks confused "What?"
    "But I don't know, it feels like she's been warming up to me lately."
    show Sayori AlterEnd3 h_confused
    h dungaree_headhold2 confused "I just didn't think you cared, dude." with dissolve
    ks smile "I mean, at first I was only looking for a practice partner for my hypnosis show and sure, that part didn't work out like I hoped."
    show Sayori AlterEnd3 n_neutral h_neutral s1 s_neutral
    ks "But Sayori was the first person to give me a real chance. I needed her help, and she had every reason to shut me down, but she saw something in me. She believed in me." with dissolve
    ks "She cared about me. So when she started on that downer, I knew I wanted to help in any way I could."
    show Sayori AlterEnd3 n_smile h_smile s_smile
    ks "She made me want to care about her too." with dissolve
    show Sayori AlterEnd3 h_laugh
    h happy "Ahh... kyahahaha~" with dissolve
    ks frown "Again. What?"
    show Sayori AlterEnd3 h_grin
    h smirk "S'laying it on a little thick, but yeah. I get'cha." with dissolve
    show Sayori AlterEnd3 h2 h_smile_side s2 s_smile_side
    h smile_side "An' if you finally got miss bookworm to hang with us outside of school, you gotta be doing something right~" with dissolve
    show Sayori AlterEnd3 s_rolleyes
    s "Ugh, again with the \"Miss Bookworm\" monicker." with dissolve
    show Sayori AlterEnd3 s_laugh
    s  "I am Yllaphyra Ashpetal, the bard of Thimhaven, and you will delay throwing that die not a moment longer if you know what is good for you!" with dissolve
    show Sayori AlterEnd3 n_laugh h1 h_rolling h_laugh
    "The room fills with playful laughter as our game, and this crazy chapter of my life, continues." with dissolve
    "I had a freaking mind-controlling penlight in my hands and lost it, and that's not even the craziest part."
    show Sayori AlterEnd3 s1 s_smile
    "I have friends now. I have Sayori in my life." with dissolve
    $persistent.alter_good_end_2_unlock = True
    scene bg blackscreen with dissolve
    "And as she and I exchange glances, I feel that our time together has only just begun..."
    jump Credits

label Epilogue_Con_Kyou_Hiroko:
    if ending == "trust":
        scene bg blackscreen with longblink
        play music Audience
        "It's been a few weeks since that day."
        scene bg classroom eve
        show Hiroko StageShow:
            ypos -0.0 xpos -0.5
        with dissolve
        k "Now I know you guys here are feeling very relaxed right now, taking nice, slow, deep breaths."
        k "But I wanna tell you all how you can drop into an even deeper sleep."
        k "So here's what's gonna happen: I'm gonna count slowly backwards from five to one."
        show Hiroko female1 male1:
            ypos -1.8 xpos -0.6 zoom 2.0
        k "You're going to listen to the numbers I'm counting, and with every number you hear me count, I want you to sink even deeper into this blissful relaxation you're feeling." with dissolve
        show Hiroko StageShow nofemale1:
            ypos -0.0 xpos -0.5 zoom 1.0
        k "And by the time we reach the number one, every muscle in your body from your heads all the way down to your toes is going to be extremely, deeply relaxed." with dissolve
        $ta = Character("Student #1"); tb = Character("Student #2"); tc = Character("Student #3"); td = Character("Student #4"); te = Character("Risa")
        ta "{size=14}C'mon, there's no way this is real.{/size}"
        show Hiroko k_grin
        k "Let's all start this count by taking a nice deep, full breath everybody." with dissolve
        show Hiroko male2 nokyou:
            ypos -0.4 xpos -1.35 zoom 1.4
        "As the seated people around me start sucking in deep breaths, I spare a glance for the mostly hushed audience in the classroom." with dissolve
        show Hiroko male1 female1 nokyou:
            ypos -1.6 xpos -0.0 zoom 1.8
        "Taking in everything, I pause to reflect what's happening here." with dissolve
        show Hiroko female1 male1:
            ypos -1.8 xpos -0.6 zoom 2.0
        "Like, holy shit, I'm actually doing this." with dissolve
        show Hiroko StageShow nofemale1 nomale2 kyou k_armup k_smile:
            ypos -0.0 xpos -0.5 zoom 1.0
        k "And now let that breath slowly seep out of you as we start. Five." with dissolve
        show Hiroko male1 female1 nokyou:
            ypos -1.6 xpos -0.0 zoom 1.8
        r "{size=14}That guy there's totally faking, you can tell.{/size}" with dissolve
        s "{size=14}Shh.{/size}"
        show Hiroko StageShow nofemale1 kyou k_armup k_smile:
            ypos -0.0 xpos -0.5 zoom 1.0
        k "Just sinking down slowly. Feeling your legs getting looser and limper, letting all the tension draining out of your feet so naturally." with dissolve
        show Hiroko StageShow k_grin
        k "And now taking another deep breath for me... That's right." with dissolve
        k "Four. Feeling all the remaining tension in your back vanish, nice and relaxed as you drop deeper and deeper."
        show Hiroko male1 female1 nokyou:
            ypos -1.8 xpos -0.6 zoom 2.0
        tb "{size=14}Are they really doing it?{/size}" with dissolve
        show Hiroko StageShow nofemale1 kyou k_armup k_smile:
            ypos -0.0 xpos -0.5 zoom 1.0
        k "Another deep breath now... Three, exhaling, letting all the tension drain out of your shoulders. Feeling it all drop away, going deeper and deeper." with dissolve
        "There's a little whoop from the crowd as I spot someone about to fall off her chair."
        show bg blackscreen onlayer toplayer
        "I walk over and touch her shoulder gently to make sure she doesn't fall on her head." with dissolve
        k "And to you, whose shoulder I am now touching, your butt is stuck to the seat of that chair. Understand?"
        hide bg blackscreen onlayer toplayer
        show Hiroko StageShow nozomi nokyou:
            ypos -0.2 xpos -1.8 zoom 1.4
        n "Y... yeah." with dissolve
        play sound AudienceLaughter
        ta "{size=14}Hahaha, isn't that the girl from last year?{/size}"
        r "The fake chicken lady!"
        s "Shush!"
        k "That's right, feeling so loose. So limp. And now taking another deep breath with me."
        show Hiroko StageShow nofemale1 nonozomi kyou k_armup k_smile:
            ypos -0.0 xpos -0.5 zoom 1.0
        k "And exhale... Two, all the tension draining from your neck now. Relaxing so deep, feeling so loose." with dissolve
        "There's another excited whoop as I notice the guy on the other end of the row of chairs is close to suffering the same fate as Nozomi. I better help him out too."
        show Hiroko male1 female1 nokyou:
            ypos -1.6 xpos -0.0 zoom 1.8
        k "And now you, I'm touching your shoulder, your butt is also stuck solidly to that chair. Understood?" with dissolve
        tc "Mm, yeah..."
        r "{size=14}Faaaake.{/size}"
        play sound AudienceLaughter
        k "Okay and now, one more deep breath with me. So close to going all the way down, deep breath."
        show Hiroko female1 male1:
            ypos -1.8 xpos -0.6 zoom 2.0
        "I listen once more as those seated in front of me, and some in the crowd it seems, draw another breath." with dissolve
        show Hiroko male2 nozomi nokyou:
            ypos -0.4 xpos -1.4 zoom 1.2
        "The audience seems to really be getting into this now as they react to the participants slumped over each other more and more, barely able to stay on their seats." with dissolve
        k "Those noises you hear from the audience only take you deeper down, boys and girls. Only take you deeper and deeper."
        show Hiroko StageShow nofemale1 nonozomi kyou k_armup k_smile:
            ypos -0.0 xpos -0.5 zoom 1.0
        k "And now on this final number, there will be nothing left. You will be dropping effortlessly into the deepest sleep; not a drop of tension anywhere in your body." with dissolve
        k "Are you ready? Exhale slowly now..."
        show Hiroko StageShow k_grin
        k "One." with dissolve
        show Hiroko nomale2
        "There's another excited whoop from the audience members as the guy to my left pretty much collapses onto poor Nozomi, who nevertheless holds fast in her seat." with dissolve
        show Hiroko male1 female1 nokyou:
            ypos -1.6 xpos -0.0 zoom 1.8
        "And yeah, I can tell that guy seated at the end is faking. Whatever, so long as he plays along." with dissolve
        show Hiroko StageShow nofemale1 nonozomi kyou k_armup k_smile:
            ypos -0.0 xpos -0.5 zoom 1.0
        k "That's right, so deeply relaxed, all the tension completely gone from your bodies... feeling so completely hypnotized." with dissolve
        "With an eye on the clock, I can see I need to wrap this up soon."
        "I was a bit nervous to start, and it took a while to find more than a couple volunteers for this stuff."
        "But that's okay, I can still do one more trick with them, just like I rehearsed."
        show bg blackscreen onlayer toplayer
        "I'll just start by reaching down and touching the shoulders of someone I know will be reliable." with dissolve
        k "But now you and only you, whose shoulder I am currently touching, can sit back up in your chair."
        show Hiroko StageShow hiroko nozomi h_hands k_armdown male2 female1:
            ypos -0.5
        hide bg blackscreen onlayer toplayer
        h "..." with dissolve
        r "Ahaha, leave her alone, ball boy!"
        if hypno6 == "cat":
            show Hiroko:
                linear 2.0 xpos 0.0 ypos 0.0 zoom 0.5
            k "And as I speak to you, you will realize that you are now a cat. You will only be able to think and act like a cat. Do you understand?"
            h "Mew..."
            play sound AudienceLaughter
            "That gets a loud chuckle from everyone on its own."
            show Hiroko StageShow k_armup h_nohands
            k "Now when I snap my fingers, Hiroko, you will be able to leave your seat and roam around the stage as a cat. Three, two, one..." with dissolve
            play sound fingersnap
            show bg blackscreen onlayer toplayer with dissolve
            h "Mroww..."
            hide bg blackscreen onlayer toplayer
            show Hiroko StageShow_Cat:
                xpos 0.0 ypos 0.0 zoom 1.0
            play sound AudienceLaughter
            with dissolve
            "The audience erupts as she drops on all fours from her chair and crawls around the stage for a moment before crouching to lick her hand."
            show Hiroko
            "I look her over before moving on, just to quickly check on her, as I know she's been anxious about doing this stuff in public."
            "But I smile as she seems contented amidst the cacophany of laughter before her."
            hide Hiroko
            show Hiroko StageShow male1 female1 nokyou:
                ypos -1.6 xpos -0.0 zoom 1.8
            "Now I clap my hand on the shoulder of the guy at the end of the row, the one I think is faking." with dissolve
            "Let's see how good an actor he is."
            k "And now you, whose shoulder I am touching, you can sit back up in your chair and realize you are a dog."
            k "You will only be able to think and act like a dog, understand?"
            tc "Uh, woof?"
            play sound AudienceLaughter
            r "Faaaake!"
            s "{size=14}Risa, please.{/size}"
            r "{size=14}What?{/size}"
            k "So now when I snap my fingers, you will be able to leave your seat and roam the stage as a dog. Three, two, one-"
            play sound fingersnap
            show Hiroko StageShow_Cat guy licking_side:
                xpos 0.0 ypos 0.0 zoom 1.0
            "And at the snap of my fingers the guy drops on all fours and starts barking somewhat unconvincingly, which Hiroko immediately seems to notice." with blink
            show Hiroko StageShow_Cat arm_down annoyed
            "I watch with the audience as he crawls over to Hiroko's crouched form, barking intermittently." with dissolve
            show Hiroko StageShow_Cat hiroko_angry
            "And in response she turns towards him and assumes a menacing stance as if she's about to pounce." with dissolve
            show Hiroko StageShow_Cat sweatdrops
            h "HSSSSSSSSS!" with vpunch
            play sound AudienceLaughter
            tc "O-oh shit!"
            show bg blackscreen onlayer toplayer with dissolve
            "I can't stop myself from laughing with everyone else as Hiroko leaps at this guy, swinging her paw and narrowly missing his cheek..."
            hide bg blackscreen onlayer toplayer
            hide Hiroko
            with dissolve
            "... before he jumps up to his feet and runs off the stage with Hiroko in hot pursuit."
            "Thankfully she doesn't chase him beyond the stage as he flees into the audience."
            "I... don't know what else I expected."
            ks smile "O-okay, Hiroko, come over here... good kitty."
            show Hiroko smile # Not sure why I need to declare this first, but she doesn't show up on screen otherwise
            show Hiroko:
                xpos 1.1 ypos 1.3
            show Hiroko:
                linear 1.5 xpos 0.8
            "I smile and beckon as she smiles back and pads over to me on all fours, purring."
            show Hiroko:
                xpos 0.8
            ks "That's a good kitty... now..."
            "Taking her hand in mine, I tug it firmly across and raise my voice."
            show Hiroko surprised
            ks "Sleep!" with dissolve
            show Hiroko sleepy:
                linear 1.0 ypos 2.0
            "As her head droops I guide her gently to the floor."
            show Hiroko:
                ypos 2.0
            ks "Good kitty, nice and deep."
            "But as I look up I see Mr. Kobayashi pointing to his wrist. Time's up."
            hide Hiroko
            show Hiroko StageShow nozomi k_armup male2 female1:
                zoom 0.5
            k "Okay, well, I hope everyone enjoyed that and, don't worry, I'll make sure they're all back to normal before I let them go." with dissolve
            show Hiroko k_grin
            k "Enjoy the rest of the festival!" with dissolve
            play sound AudienceClapping
            "I'm beaming with pride and adrenaline as I get a hearty round of applause."
            "But I can't enjoy it too much right now. I need to tend to these volunteers before the next act is up..."
            $persistent.hiroko_stageshow_good_unlock = True
            $persistent.hiroko_stageshow_cat_unlock = True
            scene bg corridor eve
            play music Peaceful
            show Nozomi front happy at center:
                xpos 0.55
            show Hiroko smile at center:
                xpos 0.75
            show Sayori smile_right at center, flip:
                xpos 0.35
            show Risa smile at center, flip:
                xpos 0.15
            with longblink
            ks smile "So, uh, what did you think?"
            "After all was said and done, I meet up with Hiroko, Nozomi and their friends while the rest of the culture fest carried on without us."
            s uniform_folded "It was interesting how your show differed from Satoshi's last year." with dissolve
            s uniform_handup smirk "Although more entertaining to me was the involvement of these two." with dissolve
            r smile_side "Right? I mean, I was sorta expecting to see the fake chicken lady again." with dissolve
            n side frown_side blush "N-Now wait just a minute-{w=1.0}{nw}" with dissolve
            show Sayori smile
            r uniform_armup smug_side "But you, Hiro? Putting on a show like this?" with dissolve
            r "Didn't think you'd be up for this sort of thing."
            h uniform_headhold2 frown_side "I was paying him back for that racket, y'know? Sides..." with dissolve
            "She lets a moment pass in silence before shrugging."
            h sleep "It was pretty fun." with dissolve
            n front concerned noblush "Yes. It was a shame you didn't have more time for your act. I did what I could, but there were a lot of people wanting to perform this year." with dissolve
            ks "I'm just happy it went okay. And after that, I kinda want to do it again real soon."
            n front2 smile "Well, let me know when and I'll do absolutely everything I can to help~" with dissolve
            show Sayori uniform_folded neutral
            show Risa neutral_side
            h neutral_side "..." with dissolve
            s neutral "..."
            r "..."
            n sleep blush "W-w-well, I mean as class representative I should be encouraging positive development of ALL my fellow classmates, and besides..." with dissolve
            n concerned "Uhh..." with dissolve
            n surprised "Ah, I just remembered I need to tell my parents... something. I think I just saw them outside. {w=1.0}{nw}" with dissolve
            hide Nozomi
            $ renpy.transition(dissolve, layer="master")
            extend "Okay, bye!"
            h frown_side "The fuck's got into her?" with dissolve
            s sleep "I have a theory, but I would not worry about it." with dissolve
            h uniform_armup smile_side "Eh, well it's cool she was up there with me. Really helped me out." with dissolve
            ks "Speaking of which, you really helped ME out, Hiroko. I seriously couldn't have done this without you."
            show Hiroko smile
            show Sayori uniform smile_right
            show Risa smile
            "As Hiroko smiles back at me, Sayori turns to me as well." with dissolve
            s "Well, congratulations to you both. It was a pleasure to watch."
            s smirk "But now, unlike some others I might mention, I do actually need to find my parents. They see too little of me as it is." with dissolve
            r uniform grin "And I'm gonna have a wander. There's a few stalls I want to check out before everything closes." with dissolve
            h happy "Bye, you two~" with dissolve
            hide Sayori
            hide Risa
            show Hiroko uniform smile
            "As the others take their leave, I turn my attention back to my assistant for tonight." with dissolve
            ks "I'm really glad you changed your mind about all this."
            h uniform_headhold2 neutral_side "Well... you did reckon it was all down to that light thingy you had, yeah? About how that was doing the weird shit to me?" with dissolve
            ks neutral "Yeah. It was the only thing I could think of that's different to how anyone else does this stuff."
            h nervous "Uh-huh. And we've done it a few times without and... yeah. It's different. Ain't so intense." with dissolve
            h sleep "Feels like I do get a say about what goes on and what doesn't." with dissolve
            h neutral "What are you gonna do with it, anyway?" with dissolve
            ks frown "I'm not sure. I leave it at home now, until I can figure it out. Maybe research it some when I get a chance."
            h nervous "Right, right." with dissolve
            show Hiroko uniform neutral_side at flip
            "She turns to look out the window and sighs, while the distant background chatter of excited students and their parents fills our silence." with dissolve
            ks "What's the matter?"
            h "Hmm..."
            h neutral "C'mon, let's go outside." with dissolve
            scene bg court night
            show Hiroko
            with blink
            "Just as she asks, I follow her out into the slightly chilly autumn air."
            "I figured she'd want to visit the outdoor festival stalls, but no, she leads me to the currently neglected tennis courts."
            h neutral_side "I sent out the scholarship apps today." with dissolve
            ks neutral "Yeah? How are you feeling about that?"
            h smile "Pretty good~ I deffo made an impression the other week." with dissolve
            h frown_side "Even if that one dude would {nw}" with dissolve
            extend "NOT shut up about my forehand." with vpunch
            h uniform_armup angry_side vein "\"It's so unorthodox. Have you considered changing to something more conventional?\"" with dissolve
            h angry "Like I don't know my own style? Fuckin' jackass." with dissolve
            ks smile "Yeah, well... for what it's worth I think you did plenty out there and I hope they give it to you."
            h uniform smile novein "Yeah, thanks, dude~ What about you, though? You figure out what you want yet?" with dissolve
            ks "I think I want to go into psychology. Which... man, until this year I never thought I'd be saying that."
            h uniform_armup laugh "The hypno bug bit you hard, huh." with dissolve
            ks "What we did just now pretty much sealed the deal, yeah."
            "Hiroko grins, then lifts a hand to her hair."
            h uniform_headhold nervous_side "Well... I mean, if you wanna keep doing it..." with dissolve
            ks surprised "... What?"
            h nervous blush "Right? This is fuckin' stupid, but... I trust you now. I trust you a lot." with dissolve
            h smile "It's stupid, right?" with dissolve
            ks "I uh... no?"
            "After having a moment to think, I clear my throat and assert myself."
            ks smile "What we did together needed an INCREDIBLE amount of trust."
            ks "And I'm pretty sure you wouldn't have put that trust in me if you knew what you were really getting into."
            ks "But I want to be worthy of your trust now, Hiroko."
            h uniform_headhold2 noblush "See, yeah, that's what I was thinking." with dissolve
            h frown "But get a pocketwatch and put that light thing in the trash, 'kay? You don't need that shit." with dissolve
            "I nod at her. I'd still like to study the thing, but after what I pulled off tonight I guess she's right."
            ks "So... wait, what does this make us now?"
            h neutral "Hm?" with dissolve
            ks "Friends? \"Hypno buddies\"? Or..."
            show Hiroko smile
            "Hiroko looks me in the eyes and smiles as she takes my meaning, only to avert her gaze with a frown." with dissolve
            show Hiroko frown_side
            ks frown "Wait, what's the matter?" with dissolve
            h "Risa's gonna rub this in my face 'til I die and she don't know the shit we've been through."
            h uniform sleeptalk "It's fuckin' unfair." with dissolve
            ks smile "Yeah... I get that, but do you really care what she thinks?"
            "She sighs."
            h angry "Just pisses me off, is all." with dissolve
            ks "Yeah, I know how it's going to look..."
            ks "You didn't answer me, though."
            show Hiroko frown_side
            "Hiroko frowns in thought as she looks past me..." with dissolve
            scene cg school ext night
            show Hiroko GoodEnd1 body smile
            with blink
            "Then breaks into a smile as she makes a grab for my hand, before dragging me back towards the festivities."
            ks surprised "H-Hey, what are you doing?"
            h "I'll make you a deal. Let's..."
            show Hiroko GoodEnd1 blush
            h "Let's finish the festival together." with dissolve
            show Hiroko GoodEnd1 blush laugh
            h "THEN I'll tell ya~" with vpunch
            $persistent.hiroko_good_end_1_unlock = True
            jump Credits
    elif ending == "liar":
        scene bg court eve with longblink
        play music Audience
        "A hush descends upon the assembled crowd."
        "It's been a long day of competitive tennis, but as I suck in a breath I watch what could be the last bit of action."
        show Hiroko tennis neutral_side at center, flip:
            xpos 0.15
        "Hiroko Homura, our school's tennis star, is serving for match point." with dissolve
        play sound tennisbounce
        "She looks calm and collected as she bounces her ball off the floor, eyes locked on her somewhat flustered-looking opponent."
        show Hiroko tennis_armup frown_side
        "A moment later, she grips the ball in her hand before tossing it vertically in the air and... {w=0.5}{nw}" with dissolve
        play sound tennishit
        extend "with perfect form hits a booming serve out wide." with vpunch
        play sound tennishit
        "The girl on the other end doesn't return Hiroko's serve so much as parries it, but it's enough to send the ball across court."
        show Hiroko at flip:
            linear 1.0 xpos 0.4
        "It's enough to make the assembled onlookers gasp as the ball unexpectedly clips the net and bounces low on Hiroko's side."
        play sound tennishit
        "But having rushed to the net, she's already in a position to crouch down and half-volley it back."
        play sound tennishit
        "It was all she could do with that, really, and her opponent takes advantage of her rare piece of luck by hitting a lobbed shot that leaves Hiroko stranded."
        show Hiroko at flip:
            linear 1.0 xpos 0.15
        "... Or so we thought."
        play sound tennishit
        h "Kyaa!" with vpunch
        "Hiroko must have known immediately what was coming, and had already started dashing back to the baseline with alarming speed."
        "Her eye on the ball the entire time, she's able to get back and execute an overhead smash on a ball that really should've beaten someone of her height."
        "The other girl... well, it's not like she stopped trying, even at the death and staring down the barrel of a humiliating \"bagel\" defeat..."
        play sound tennishit
        "But she can't take the sting out of Hiroko's powerful return, and her reply sails wildy off court."
        $t = Character(_("Line Judge"))
        play sound AudienceClapping
        t "Out!"
        show Hiroko happy
        $t = Character(_("Umpire"))
        t "Game, set and match: Miss Homura. By six games to love." with dissolve
        h "AAAAAAAA!" with shake
        show Hiroko laugh
        "I grin as Hiroko screams with delight, pumps the air, and waves happily in my direction before pacing to the net to shake hands with her crestfallen opponent." with dissolve
        "With this tournament being held at our school there's a partisan crowd but even so, there's some sympathy to spare for that other girl."
        "She played her heart out, but Hiroko just had her number every time. Just like with everyone else she's played today."
        "This whole tournament has been a procession for her."
        stop music fadeout 2.0
        scene bg track eve
        show Hiroko tennis_armup happy_side at center, flip:
            xpos 0.25
        show Nozomi side casual smile_side at center:
            xpos 0.5
        show Risa tennis wristband_left smile_side at center:
            xpos 0.75
        with blink
        play music Beautiful
        "Eventually, after the trophy ceremony and some time with her parents, Hiroko's able to get away and reflect on the day with the rest of us."
        n laugh "I'll say it again, Hiroko, you were INCREDIBLE!" with dissolve
        r tennis_armup wristband_left_armup grin "She's not wrong. That was some pro-level tennis right there, Hiro~" with dissolve
        h happy "Kyahaha! Man, I'm so pumped you all got to see it!" with dissolve
        n smile_side "Soooo, when are you playing Naomi Osaka?" with dissolve
        h tennis_headhold2 smile_side blush "Oh... g-gawd, will you shut up about her? I ain't THAT good!" with dissolve
        r smug_side "Aww, don't get modest on us now, Hiro." with dissolve
        h happy_closed "I-I'm just sayin'. I won a lil' high school tourney, s'not THAT big a deal." with dissolve
        h "Should be enough for my scholarship, but I gotta keep my head screwed on."
        r tennis wristband_left "That's cute. And sure, a one-day tourney is nothing like the pro tour. Maybe your game will struggle when it comes to three set matches." with dissolve
        show Hiroko smile_side noblush
        r smile_side "But something tells me you'll do alright, Hiro. It really feels like you've matured." with dissolve
        n "Mhm! You're not the \"demon\" I said you were before... but you might be even scarier on court now."
        n laugh "Just promise you'll remember us when you lift that Wimbledon trophy~" with dissolve
        h tennis_armup happy blush "S-shut up, Nozo! Haha~" with dissolve
        stop music fadeout 10.0
        r grin "Makes me wonder if the missing ingredient this whole time was letting a guy into your life~" with dissolve
        show Nozomi surprised_side
        h furious_side "RISA, COME ON!" with vpunch
        n "A guy? You mean there's someone?"
        "Suddenly I'm feeling a lot less comfortable standing here watching this."
        r tennis_armup wristband_left_armup smug_side "Like she didn't tell you." with dissolve
        play music Eons
        h tennis_headhold sleep "I mean... yeah, there's a guy." with dissolve
        n laugh "Aww, and this is the first I'm hearing of it? I thought we were friends." with dissolve
        h smile_side "I-it literally just happened, geez, get off my case." with dissolve
        n smile_side "Soooo...?" with dissolve
        h frown_side "So?" with dissolve
        n "Oh my gosh, is it Ryoma? Did that finally happen?"
        h smile "N-no it ain't... Ryoma, no." with dissolve
        n "Then...{w=1.0}{nw}"
        show Nozomi surprised
        $ renpy.transition(dissolve, layer="master")
        extend "{w=1.0}{nw}"
        show Nozomi front surprised
        $ renpy.transition(dissolve, layer="master")
        "As Nozomi follows Hiroko's blushing gaze to me, her mouth hangs open."
        r grin "Ah, there it is." with dissolve
        n "I did wonder why he was following us, but..."
        n side surprised_side "You? With..." with dissolve
        show Hiroko frown_side
        n surprised "With..." with dissolve
        n "Him?!"
        h "Hey, I didn't get it either."
        r tennis wristband_left smug_side "Took me by surprise, too. Never would've pegged her as being into the quiet nerdy types." with dissolve
        h tennis_armup irritated vein"H'yeah, laugh it up, you dopes. I ain't gonna let you put me down for this." with dissolve
        r smile_side "Aww, no! Realtalk, I think you look cute together, Hiro." with dissolve
        show Hiroko tennis frown_side novein
        r smug "It's Kyou I'm worried about. I hope you know what you've let yourself in for, ball boy~" with dissolve
        "As if remembering my presence again, Nozomi's gaze flickers between me and Hiroko before she turns to me sheepishly."
        n front2 concerned blush "Right, Kyou... I shouldn't talk about you like you're not here. I apologize." with dissolve
        "I almost want to say it's fine if they want to ignore me and pretend none of this ever happened, but instead I simply force a smile and answer her as best I can."
        ks casual smile blush "I... It's okay."
        h smile "Man, I gotta teach you to stick up for yourself." with dissolve
        "Hiroko chuckles at me, then turns back to the others for a moment."
        h smile_side tennis_headhold2 "Okay yeah, so secret's out. Kyou's my guy~" with dissolve
        n side sad_side noblush "Gosh, I wish I heard about this sooner. I booked us a private room at the karaoke bar to celebrate." with dissolve
        n smile "B-but, if I talk to them now I can probably squeeze you in, Kyou. If you want?" with dissolve
        ks surprised "W-well..."
        "Wait a minute..."
        h smirk "He's deffo coming with us." with dissolve
        "This is gonna complicate things."
        n front laugh "A-alright, then! I'll make the arrangements and see you all in a bit~" with dissolve
        "Now Nozomi knows about our relationship. If Hiroko and I go to this place as a couple then pretty much everyone's gonna know about us."
        hide Nozomi
        "How am I gonna explain this to Hiroko when I snap her out of this?" with dissolve
        r grin "And I'm going to get changed. Behave yourselves while we're gone, lovebirds." with dissolve
        show Hiroko frown_side
        r smug_side "... I have no idea why I said that." with dissolve
        h irritated "Yes you do! N-nothing's gonna happen!" with dissolve
        r "I believe you."
        h angry_side "I mean it!" with dissolve
        r "Okay."
        h furious_side "J{nw}" with dissolve
        extend "-JUST GET THE FUCK OUTTA HERE!" with vpunch
        hide Risa
        "Chuckling, Risa strolls off towards the changing rooms while leaving Hiroko with me to glower at her back." with dissolve
        h angry_side "GAWD." with vpunch
        show Hiroko frown_side
        "I watch with Hiroko in silence as Risa disappears into a small crowd of stragglers, before finally she speaks again." with dissolve
        h neutral "Hey, Kyou." with dissolve
        ks neutral noblush "H-hmm?"
        h "Think fast."
        ks "What?"
        scene Hiroko YikesEnd1 arms_out surprised blush with blink
        "I barely get a word out of my mouth before Hiroko is upon me, draping her arms around my shoulders as she pulls herself up to kiss me full on the lips."
        show Hiroko YikesEnd1 arms_in calm blush
        "With a quiet moan, she presses her tongue into mine as I sigh through my nose, wrapping my arms around her back to support her against me." with dissolve
        "Is this... is this what a real kiss feels like? The one I apparently stole from her frozen lips the other day has nothing on this."
        "Compared to that, this is..."
        hide Hiroko YikesEnd1
        show Hiroko YikesEnd1 couple2
        "No, holy shit, what am I doing?!" with dissolve
        h "K-Kyou?"
        "It took every bit of willpower I had to disentangle myself, and she blinks up at me in genuine astonishment."
        "I can't keep this up."
        k "H-Hiroko, I'm... shit, I-I'm sorry."
        h "Eh? For what?"
        scene bg track eve
        show Hiroko tennis surprised blush at center
        with blink
        ks casual surprised "It's just... what you said before. About this not being you."
        h neutral noblush "Uh... yeah, I guess I did say that. Why're you bringing that up now?" with dissolve
        h smile "Like, I thought we went over this already, dude. I changed my mind about it." with dissolve
        ks frown "That's the thing, Hiroko... I kinda changed your mind for you."
        h tennis_headhold2 surprised "You... what?" with dissolve
        ks surprised "I-it saw you through the tournament, didn't it? You're getting your scholarship like you wanted, no doubt about it."
        ks "B-but I can set you right again now! We can go back to mine and..."
        show penlight at right with moveinright:
            ypos 0.346
        "Rushing to assure her, I pull the penlight from my pocket and hold it in front of her."
        ks "A-and I'll take you into trance again and-{w=1.5}{nw}"
        h tennis_armup furious "What? {w=0.5}{nw}" with dissolve
        extend "NO!" with vpunch
        "As I step back from her shout, she swipes at me with her fist as I raise my free hand to block her..."
        hide penlight
        "But only as her hand swings across my face do I realize what she was really doing." with vpunch
        ks "Hiroko, please... give that back!"
        h angry "I ain't letting you \"set me right\" again! {w=1.0}The fuck's {nw}" with dissolve
        extend "THAT 'sposed to mean?" with vpunch
        ks "Like I said, I changed your mind for you so... n-now I should unchange it, right?"
        show Hiroko irritated
        ks "I know you don't really want to stay like this forev- {w=0.5}{nw}" with dissolve
        extend "NO!" with vpunch
        "While I'm trying to explain, Hiroko grips my penlight between both hands and, with a grunt, manages to bend it in half."
        show Hiroko frown
        ks "H-HIROKO WHAT DID YOU DO?!" with vpunch
        h tennis "That's what I gotta say to that, dude." with dissolve
        ks "Y-you don't know what you're saying! What if I can't change you back? What if the things I put in your head never wear off? W-what-{w=1.5}{nw}"
        h tennis_armup furious "KYOU!" with vpunch
        "Hiroko's shout stops me in my tracks."
        h tennis irritated "Just settle the fuck down, okay? It don't matter if you can't change me back." with dissolve
        h tennis_headhold2 neutral_side "So, what, I can play tennis like a boss and all I gotta do for that is like some dork?" with dissolve
        h neutral "That about sums it up, don't it?" with dissolve
        ks "I... think so, yeah."
        h smile blush "So I dunno what I was thinking before, but it sounds like a pretty sweet deal to me~" with dissolve
        "I... don't know what to say to that."
        h affectionate "And I KNOW you like me back, Kyou. You didn't do that to yourself." with dissolve
        h tennis_armup happy "So what's the problem?" with dissolve
        scene Hiroko YikesEnd1 couple3 smile with blink
        "The bent penlight slips from her fingers as she reaches up and plants her hands on my shoulders, looking up to me with a smile."
        "... Do I really have a problem with this?"
        "She's happy... I can be happy."
        "Maybe I literally changed her mind, but I didn't hurt her by doing what I did."
        "So I can stop worrying..."
        show Hiroko YikesEnd1 laugh
        h "Kyou? C'mon, quit spacin' and say something!" with dissolve
        "... Right?"
        $persistent.yikes_end_unlock = True
        jump Credits

label Epilogue_Con_Bad_Hiroko_Penlight:
    scene bg classroom eve with longblink
    play music Memories
    "As another school day draws to a close, I gather my things and ponder."
    play sound schoolbell
    show Hiroko uniform_headhold2 happy at center
    show Sayori smile at center, flip:
        xpos 0.25
    h "Ahh, ain't that bell music to your ears or what?" with dissolve
    s sleeptalk "It merely heralds the end of another school week. No more, no less." with dissolve
    "It's been a few days now, since I hypnotized Hiroko on that rooftop."
    show Sayori smile
    h annoyed_side "Man, you still ain't letting up are ya? Take a day off, girl." with dissolve
    s uniform_handup "Soon, Hiroko. Soon." with dissolve
    "Sure is wild to think that a week ago we were getting into all kinds of trouble with my penlight together."
    show Hiroko uniform neutral
    show Nozomi side smile_side at center:
        xpos 0.75
    n "But what about you, Hiroko? We're still on for tomorrow, right?" with dissolve
    show Hiroko uniform_armup happy at flip
    h "Aww, you betcha! I still owe ya for bailing last time." with dissolve
    "We hypnotized each other, and I helped her achieve the biggest thing in her life."
    show Sayori uniform
    show Hiroko happy_closed
    n happy "Ehehe, I'm just glad you're feeling better about everything you've achieved. You deserve to feel good about it all." with dissolve
    show Hiroko uniform smile_side
    "And I'm confident she doesn't remember any of it." with dissolve
    show Nozomi smile_side
    h confused_side "Yeah, you got that right. I can't believe I freaked out so much over winning that thing when it was all I ever wanted." with dissolve
    "But somehow, I have to believe that's for the best."
    s uniform "It is understandable that you were somewhat overwhelmed by the occasion. You simply didn't know how to react in the moment." with dissolve
    h uniform_headhold2 smile "Yeah. S'pretty crazy but... yeah." with dissolve
    "So what do I do now? After all that's happened, can I really justify trying to use it again?"
    n laugh "Anyway, shall we get going?" with dissolve
    "I wanted to experiment, to unlock its mysteries, but there's just no way without... well, no way without trying it on someone again."
    h uniform smile_side "Er... y-yeah, let's get outta here." with dissolve
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "And I made a promise didn't I?"
    scene bg corridor eve with dissolve
    "So somehow, in spite of everything, it feels like I'm right back to where I started."
    h "Hey, you!"
    play music Eons
    "But as I eventually leave the classroom, my heart skips a beat as I hear an all too familiar voice..."
    show Hiroko uniform neutral at center
    show Nozomi side sad at center:
        xpos 0.75
    with longdissolve
    "What are they still doing here? I thought they were going home."
    ks confused "Hiroko? Nozomi? What's going on?"
    h uniform_headhold2 rolleyes "Like you don't know already." with dissolve
    ks "Uhh..."
    h frown "What, you expect me to forget what you did just 'cuz you asked me to?" with dissolve
    "I can feel my spine stiffen at her words."
    n sad_side "{size=16}Are you really sure about this, Hiroko?{/size}" with dissolve
    ks confused "Wh... w-what do you mean?!"
    "No, she doesn't remember anything. She can't remember, I made sure of it."
    h irritated vein "You really think I was just gonna pretend it never happened? Really, dude?" with dissolve
    "After everything we discovered about my penlight, she couldn't possibly have managed to resist the hypnotic effect I placed on her memory."
    show Nozomi sad
    ks surprised "Hiroko, y-you... remember?" with dissolve
    "There's just no way!"
    h uniform_headhold2 confused novein "I mean, yeah? Why wouldn't I remember the swanky new tennis racket you got me?" with dissolve
    "Oh. Right, of course."
    n front2 smile "It was a nice thing you did for her, Kyou." with dissolve
    "That's the story I fed her while I was re-writing her memories. Not like I could make that thing just disappear, or even hide where it came from."
    h neutral "Yeah, it really was. An' I know you said I didn't owe you for it or anything." with dissolve
    "So I had to make her think it was just a gift, nothing more."
    h uniform sleep "But I dunno about that." with dissolve
    "I just wasn't expecting anything to come of it, that's all."
    show Hiroko neutral_side at flip
    show Nozomi side neutral_side
    h "So like, me an' Nozo were talking about it, 'cuz I've been doing some thinking and, uh..." with dissolve
    h uniform_headhold2 nervous "Look, do you wanna hang out or something?" with dissolve
    ks confused "Hang out?"
    "Oh man, what is even happening right now?"
    h sleeptalk "H'yeah, so... like, me an' Nozo are gonna do karaoke tomorrow night. Celebrate me winnin' the tourney and all that." with dissolve
    show Nozomi smile
    h smile "I thought you might wanna come with~" with dissolve
    "She really means that? Now that she thinks my gifting her the racket was a selfless gesture she wants to put our squabbles behind us and give me a chance?"
    ks smile blush "Ahh, well..."
    "She thinks she can trust me? And more than that..."
    ks "You don't mind, Nozomi?"
    show Nozomi happy
    "Even Nozomi's starting to come around on me!" with dissolve
    n smile "I mean, if Hiroko thinks you're okay then who am I to argue?" with dissolve
    n front2 smile "This could be a lot of fun~" with dissolve
    ks "Y-yeah..."
    stop music fadeout 5.0
    "So then, why do I suddenly feel..."
    scene bg k room eve:
        matrixcolor SaturationMatrix(0)
    show Hiroko tennis concerned at center:
        matrixcolor SaturationMatrix(0)
    with flash
    queue music Measured
    $ks = DynamicCharacter("kyou_name", image = "KyouSideFlashback", who_color = "#4B9374")
    h "I made you think she's gross with that thing..."
    h nervous "S-So you could make her think you're great... Right?" with dissolve
    ks casual frown "Ugh... I guess?"
    h frown_side "\"I guess\" my ass. You know you could do it." with dissolve
    h tennis_armup angry "Don't say you ain't tempted!" with dissolve
    ks angry "I'm NOT!"
    $ks = DynamicCharacter("kyou_name", image = "KyouSide", who_color = "#4B9374")
    scene bg corridor eve
    show Hiroko uniform confused at center, flip
    show Nozomi front2 surprised at center:
        xpos 0.75
    with flash
    n "... Kyou?"
    "Dammit. I can't..."
    scene bg k room eve:
        matrixcolor SaturationMatrix(0)
    show Hiroko tennis sad at center:
        xpos 0.8
        matrixcolor SaturationMatrix(0)
    with flash
    $ks = DynamicCharacter("kyou_name", image = "KyouSideFlashback", who_color = "#4B9374")
    h "K-Kyou... I'm sorry, alright?"
    h sad_talk "But like... Don't do anythin' you're gonna regret." with dissolve
    h sleeptalk_concerned "Please..." with dissolve
    $ks = DynamicCharacter("kyou_name", image = "KyouSide", who_color = "#4B9374")
    scene bg corridor eve
    show Hiroko uniform annoyed at center, flip
    show Nozomi front2 neutral at center:
        xpos 0.75
    stop music fadeout 5.0
    with flash
    h "Hey, Earth to Kyou? You gonna say something or what?"
    queue music Diary
    "I should've listened to you, Hiroko. But it's too late."
    ks surprised "I..."
    "All I can do now..."
    ks sigh "Count me out."
    show Nozomi surprised
    h surprised "Wha? You serious?" with dissolve
    "... is make sure I regret nothing else."
    ks smile "Yeah, don't worry about it. I'm just happy you won, Hiroko."
    show Nozomi neutral
    h uniform_headhold2 confused "Yeah... thanks." with dissolve
    n smile "Okay, well have a good weekend, Kyou." with dissolve
    hide Nozomi
    hide Hiroko
    "I'm not sure what I'll do now, but I'm never using that damned penlight again. I'll remember my promise to you, Hiroko." with dissolve
    scene bg blackscreen with longdissolve
    "I'll remember for both of us."
    jump Credits

label Epilogue_Con_Hiroko_Penlight:
    scene bg blackscreen with dissolve
    pause 2.0
    "A lot has happened since that day..."
    scene bg park day with dissolve
    play music Park fadein 5.0
    ks casual sigh "You're really sure you want to do this here?"
    "In the weeks that followed, Hiroko and I started hanging out a lot more."
    show Hiroko casual frown at center
    h "How many times have I gotta tell you? I'm bored of always doing it at your depressing ass house." with dissolve
    h frown_side "'Sides, I want a little public pressure this time." with dissolve
    h sleep "Gotta step it up if I wanna... {w=1.0}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend blush "u-um..."
    ks smile "Alright. I guess that's true for both of us, huh."
    h smirk "H'yeah, after you wussed out of doing your culture fest thingy." with dissolve
    ks frown blush "Screw you. Besides, you know I had to keep my head down after the roof incident."
    h happy noblush "Kyahaha!" with dissolve
    h smirk "Whatever, dude. You're just making excuses." with dissolve
    "I shoot her a glare as I reach over and tap her shoulder disdainfully."
    ks frown noblush "That's enough out of you. Sit down and put your arms out."
    show HirokoParkHypno
    with blink
    "Hiroko smirks as she obliges me by sitting on the bench and stretching her arms out in front of her."
    show HirokoParkHypno hiroko_arms_out
    $ renpy.transition(longdissolve, layer="master")
    h "Like this, right?"
    ks smile "Yeah, with your palms facing each other like that."
    "Okay, so it turns out we weren't done with hypnosis after I destroyed the penlight."
    show HirokoParkHypno kyou_holding
    $ renpy.transition(longdissolve, layer="master")
    "While she stays seated on the park bench, I take her hands and push my thumbs gently into her exposed palms as she watches."
    ks "So remember, just like before, see how I'm placing a magnet into each of your hands like this."
    h neutral "Magnets. Got it."
    show HirokoParkHypno kyou_pointing
    "I then release her hands and hold a finger up in the air between them as I continue." with dissolve
    ks "Really powerful magnets, don't forget that. Now, I'd like you to focus your eyes on this point right here."
    show HirokoParkHypno frown_open
    "Hiroko frowns a little in concentration while I keep my fingertip steady for her." with dissolve
    ks "Great... Now I'd like you to close your eyes and try to think about nothing else."
    ks "Nothing but those magnets pulling your hands towards each other, towards this point."
    show HirokoParkHypno frown_open_talk
    h sleeptalk "Hmm... 'Kay." with dissolve
    show HirokoParkHypno frown_closed
    "Smiling at the slight apprehension in her voice, I think to offer her some reassurance." with dissolve
    show HirokoParkHypno nohands
    "It's not like I don't know why we're doing this, Hiroko." with dissolve
    ks "Hey, don't worry. You're going to remember everything when we're done, so just relax and focus your mind on those magnets."
    show HirokoParkHypno frown_closed_talk
    h sleeptalk "Heh, yeah I got it. Empty my mind an' shit." with dissolve
    show HirokoParkHypno frown_closed
    ks smirk "Isn't it great how even though you know what's going to happen, it's still going to happen?" with dissolve
    ks "Because after all, those magnets in your hands are still so strong. Still pulling your hands closer and closer together the more I talk."
    "I grin as sure enough, her hands have already started gravitating towards each other while we've been speaking."
    ks smile "Getting closer and closer, and you know that as soon as your hands touch, you're going to feel a powerful wave of relaxation..."
    show HirokoParkHypno hiroko_arms_close
    $ renpy.transition(longdissolve, layer="master")
    "Still closer."
    ks "A deep relaxation that will send you into a very pleasant, very deep state of hypnosis."
    show HirokoParkHypno hiroko_arms_closer
    $ renpy.transition(longdissolve, layer="master")
    "I fall silent a moment and simply watch her hands as they quiver slightly, maybe only a couple inches apart now."
    ks "That's right, closer and closer. Falling under a deep wave of hypnotic relaxation as soon as your hands touch together."
    show HirokoParkHypno kyou_clapping
    $ renpy.transition(longdissolve, layer="master")
    "And now, as I bring my hands up beside my friend's, the part she knows is coming. The fun part."
    ks "Closer and closer."
    "But as I told her..."
    ks frown "The moment your hands touch- {w=0.5}{nw}"
    play sound clap
    show HirokoParkHypno hiroko_slumped nohands noface
    $ renpy.transition(longdissolve, layer="master")
    extend "Sleep!"
    "It's still going to happen, as I swiftly clap my hands into hers, forcing them together."
    "And immediately she slumps forward, needing me to catch her by the shoulders."
    ks smile "Relaxing deeply, that's right. Deep asleep now."
    show HirokoParkHypno hiroko_sleep sleep
    $ renpy.transition(longdissolve, layer="master")
    "As I right her on the bench, I spare a glance either side of me to check how any bystanders might be reacting to this."
    "Definitely attracted some looks when she slumped, but it seems everyone's minding their business for now."
    ks "Feeling that deep wave of hypnotic relaxation now, Hiroko. So completely and deeply hypnotized."
    "All I have to do is act natural and confident."
    ks "Allowing those background noises you may be hearing to gently drift away. Letting them take you deeper as you relax and listen to my voice."
    "And I should follow my own suggestion: Try and forget they're even there and just focus on what I'm doing."
    ks "And now that you're in such a deep, hypnotic state, you will find it so easy to allow my words to sink deeply into your mind."
    "No... What WE'RE doing."
    ks "Allowing my words to exert a greater and greater influence over the way you think, the way you feel, and the way you behave."
    ks "So that's why, when I say that you are going to become much more confident about what you want, whatever it is..."
    ks "... you are immediately, and automatically, going to know what your heart desires, letting all your anxieties and fears drift away."
    ks "Just feeling those anxieties disappear with the wind now. And soon, when you wake from this deeply relaxing trance..."
    ks "... you'll be able to know exactly what you want. And you'll be able to follow through with those wants in a way that's completely true to who you are."
    ks "Understand, Hiroko?"
    show HirokoParkHypno sleeptalk
    h sleeptalk "Yeah..." with dissolve
    show HirokoParkHypno sleep
    "I smile at her acknowledgement. Not that I was expecting anything else by now." with dissolve
    ks "So, having accepted my words deep in your mind, knowing how much more confident you are now in your desires, I'm now going to count up to five."
    ks "With every number I count, you'll become a little more awake, a little more aware, still keeping everything I said deep in your mind."
    ks "Remembering this deep, relaxing trance and everything about it as I count now... one."
    ks "Just beginning to stir... two, taking a nice deep breath, becoming more and more aware... three."
    ks "Sitting up nice and upright now, feeling so good about all of this... four, remembering everything about this experience..."
    ks "And five, Hiroko. Wide awake."
    show HirokoParkHypno hiroko_sitting smile
    "Hiroko's eyes flutter open and she brings a hand up to scratch her head while she looks to me with a sheepish smile." with dissolve
    "If anyone watching us had any concerns, I'm pretty sure they were dispelled by that kind of reaction."
    ks "How was that?"
    "As she inhales, she blinks under the sunlight and breaks into a grin."
    show HirokoParkHypno hiroko_sitting laugh
    h casual_armup laugh "You're deffo getting better~ {w=0.5}I fucking {nw}" with dissolve
    extend "FELT all that!" with vpunch
    show HirokoParkHypno hiroko_sitting smile
    h smile_side noblush "Like... It's still nothing like that buzz I got when you were hitting me with the light thingy, but I totally forgot we were out here for a lil' bit." with dissolve
    show HirokoParkHypno hiroko_sitting_blush
    h smile blush "And... I kinda do feel more confident about what I wanna do." with dissolve
    ks smirk "That doesn't sound very confident."
    $persistent.hiroko_park_hypno_unlock = True
    hide HirokoParkHypno
    show Hiroko casual_armup angry vein noblush:
        ypos 1.3
        linear 2.0  ypos 1.0
    with blink
    h angry noblush vein "What? {w=0.5}No, I'm {nw}"
    extend "TOTALLY confident!" with vpunch
    show Hiroko:
        ypos 1.0
    "She jumps up from the bench, and her raising her voice probably got more attention from the park visitors than anything I just did."
    ks "Haha, yeah? So what ARE you gonna do?"
    h angry novein "Grr, I'm gonna..." with dissolve
    h angry_side "I'm gonna go after that scholarship!" with dissolve
    ks smile "Really? That's great!"
    h casual_headhold2 frown "Yeah, I mean, I was talking to that girl I beat. Even she thinks I should do it." with dissolve #well... Even that girl I beat said I should do it.
    h irritated "And I gotta stop pretending this ain't what I want anymore." with dissolve
    h angry "Maybe I don't got what it takes, but if I never find out for sure I'm gonna be fucked off for the rest of my life." with dissolve
    h casual_armup furious "So I'm gonna go there, and I'm gonna show those fancy ass tennis bitches what's what!" with dissolve
    ks smirk "Kinda weird that you needed me to hypnotize you before you saw sense at last, but I'm glad you got there in the end."
    stop music fadeout 8.0
    h irritated vein "Ugh, that ain't it!" with dissolve
    h casual frown novein "Like... Fuck, I already knew I was gonna keep trying to go pro. I didn't come out here for that." with dissolve
    h irritated "But I'm... I'm gonna go through with it." with dissolve
    ks smile "Really?"
    play music Luminous_Rain
    h casual_armup furious blush "I'm gonna tell Nozo how I feel!" with dissolve
    "This is a big part of why we came out here, but I have to admit, I wasn't sure if she was really going to commit."
    ks confused "You're not worried how she'll react?"
    h surprised "What? N-no..." with dissolve
    h casual_headhold neutral_side "If I want her to tell me everything then I can't hold back on her either, can I?" with dissolve
    h sleeptalk "I dunno how she'll take it, but..." with dissolve
    h casual_armup furious "{cps=20}If I can tell you, I sure as shit can tell my {/cps}{nw}" with dissolve
    extend "BESTIE!" with vpunch
    "I'm still not sure how I feel about all of this."
    show Hiroko casual smile
    "After all, these past few years I wanted to be the one to bring Nozomi happiness. And now?" with dissolve
    ks smile "And you think you'll tell her about what we've been doing together?"
    "I guess in a roundabout way I am, but damn, I never expected it to turn out like this."
    h casual_headhold happy_closed "H'yeah, I gotta hand it to ya. You were onto something with the hypno stuff." with dissolve
    h casual_armup happy noblush "So I'm gonna tell her I'm into it too!" with dissolve
    "But Hiroko was right. In all this time I never really KNEW Nozomi."
    h laugh "An' I'm gonna show her this magnet hands stuff you showed me." with dissolve
    "So maybe I can move on from that now. Besides, it turned out my hypnosis study wasn't for nothing after all."
    h smile_side blush "Y'know, if she wants me to..." with dissolve
    "Maybe it's pathetic, but I realize I've really liked just hanging out with Hiroko."
    show Hiroko casual smile noblush
    "It's amazing how quickly the tension we used to feel around each other just disappeared." with dissolve
    ks "Yeah, it's not hard to try out. Just make sure she knows what you're doing and don't get discouraged if it doesn't seem to work first time."
    h sleeptalk "Yeah, yeah, I got it." with dissolve
    show Hiroko smile
    ks "I gotta admit I'm really curious about how it'll go." with dissolve
    "Hiroko grins as she turns away from me."
    h smirk "You'll know." with dissolve
    ks "You heading to hers now then?"
    h smile "In a bit. I still ain't done, though." with dissolve
    "I have to admit I'm a little confused this time."
    ks confused "Done with what?"
    h casual_armup frown "There's one other thing I want and I ain't afraid to say it!" with dissolve
    "... Honestly, I'm still confused."
    ks sigh "Sheesh, what else are you demanding, short stuff?"
    show Hiroko happy with dissolve
    scene cg hiroko park ending 1
    "And just then I find myself assaulted as Hiroko turns back around and bundles into me, wrapping her arms around me in a tight hug." with vpunch
    k "Ooof!"
    h "You! I wanna be your friend!"
    "As I strain under her tennis grip around my upper chest, I can't help but be a little puzzled."
    k "Ugh... W-wait, weren't we already friends?"
    $persistent.hiroko_park_ending_1_unlock = True
    scene bg park day
    show Hiroko casual sleep at center
    with blink
    "I can feel her grip loosening, before she frees me altogether as a thoughtful expression crosses her face."
    h casual sleeptalk "Dude, look..." with dissolve
    h frown "Neither of us are great at saying what we want, it turns out." with dissolve
    h frown_side "But you remember back when we first started all this?" with dissolve
    h sleep "All this happened 'cuz you grew a pair and, like, straight up told me what you wanted outta me." with dissolve
    h frown "That's when shit started to change for the better." with dissolve
    h neutral "So... I ain't gonna leave anything unsaid again. Not with Nozo..." with dissolve
    h smile "Not with you. Okay?" with dissolve
    "Wow. I really have to believe my hypnosis helped her express herself right now..."
    "Plus she's right, isn't she?"
    ks casual smile "Yeah... Okay."
    "Thinking back, I could've said something to Nozomi sooner. If I only worked up the guts, the way Hiroko feels she can now."
    "But I can't afford to dwell on the past. I can't do anything about that."
    ks smile "Well... I hope you and Nozomi can work something out. I mean it."
    ks "And I want us to be friends too, Hiroko."
    "I gotta focus on the now."
    h casual_armup happy "Kyahahaha! Feels good to get it out there, don't it?" with dissolve
    h smile blush "So now we know! We ain't getting rid of each other now~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    jump Credits

label Epilogue_Con_Hiroko_Penlight_Bad:
    scene bg street1 day with longdissolve
    "It's been a couple weeks now."
    play music Eons
    "A couple weeks since I hypnotized Hiroko into being polite to everybody, and since I started leaving my penlight at home."
    scene bg ext school day with blink
    "And I'm here now, ready to start another school week as a nervous sigh escapes my mouth."
    "Ever since that night I've dreaded every moment I've had to spend in school."
    "Of being made to sit in class and suffer the sight of..."
    h "So like, what did you think of that last episode?"
    show Hiroko uniform_headhold2 smile_side at center, flip
    show Nozomi side smile_side at center:
        xpos 0.75
    with dissolve
    "Ugh... her."
    n surprised_side "Ohhh, that twist kinda came out of nowhere, didn't it?" with dissolve
    h confused_side "Right? I mean yeah he was acting out an' all, but did she really have to, like, change his program just like that?" with dissolve
    "The mock exams were a disaster because of her."
    n sad_closed "Yeah. It makes me worry if she'll ever grow as a person if she'll resort to that to solve her problems." with dissolve
    h uniform sad_side "True that. It's almost like the robot dude's getting more human than the girl the way this's all panning out." with dissolve
    "It's all I can do to keep my head down and try to ignore her odious presence, and it's been killing my ability to focus on anything else."
    n neutral_side "Mhm. And speaking of change, I see you're still serious about turning over a new leaf, or... is that right?" with dissolve
    h confused_side "Uh, I guess? If that's what you wanna call it." with dissolve
    "Maybe I should ask Mr. Kobayashi if it's not too late to switch classrooms."
    n sad_side "What brought this on, Hiroko? Did something happen?" with dissolve
    h smile_side "Not... really? I dunno, it just don't feel right to mouth off at people, y'know?" with dissolve
    h uniform_headhold2 happy_closed "It's nice to be nice~" with dissolve
    "It's horrible to think about, but if I can just get away from her, maybe I can finally fucking concentrate around here..."
    n happy "Eheh, I suppose. I guess I'm still getting used to it." with dissolve
    h laugh "For sure, an'... oh hey, Kyou!" with dissolve
    "Ah, shit. They've noticed me."
    n neutral "Kyou..." with dissolve
    "I catch that hag eyeballing me, and I immediately regret hanging around here as I'm forced to suppress a sudden urge to barf."
    n sad_side "I'm going to head inside..." with dissolve
    scene bg blackscreen with dissolve
    "Fortunately that feeling subsides as that disgusting tramp hurries past the school gates and out of my sight."
    scene HirokoBetrayal hiroko happy with dissolve
    h "Hiya, Kyou! Good morning~"
    stop music fadeout 5.0
    "Now, Hiroko. At least she's someone I can stomach being around."
    ks neutral "Uh, yeah... morning."
    "At least, if seeing her wasn't a constant reminder of why she's so... changed."
    queue music Sorrow2
    show HirokoBetrayal neutral
    h "So, uhh... bummer that we couldn't do anything for the culture fest like you wanted, huh?" with dissolve
    "Every time we talk, I can't help but be reminded of our misadventures with hypnosis."
    ks "Y-yeah, well... yeah, I just wasn't feeling it when it came down to it; don't worry about it."
    "And those compulsions we put in each other's heads... they didn't fade away. If anything, they're as strong as ever."
    show HirokoBetrayal curious
    h "It's cool. Just think you would've brought the house down if you did, that's all." with dissolve
    "I can't possibly use the penlight again now. Especially not on her. I wouldn't dare."
    show HirokoBetrayal awe
    h "You're so good at it, dude! An' you really did me a solid when you worked your magic on me." with dissolve
    "If I hypnotized her again, could I trust her to take it well if I removed the suggestions she's holding to?"
    show HirokoBetrayal smile
    h "Still wish you could've seen me out there, kicking all that butt..." with dissolve
    "Could I trust the penlight to not fuck her up even more?"
    show HirokoBetrayal happy
    h "But anyway, you lemme know if you need anything, alright?" with dissolve
    "Hell, should I even try to lift the suggestion she put in my own head? Nozomi's so gross it hardly seems worth the effort to even bother."
    show HirokoBetrayal smile
    h "I told ya before, but I really wanna thank you for what you did." with dissolve
    "So why risk it? I can't trust myself to do anything right, anyway. Not after everything."
    show HirokoBetrayal grin
    h "Least I can do for a pal~" with dissolve
    "I can't trust... anyone."
    show HirokoBetrayal concerned
    h "... O-okay. Well, I'll see you in class, yeah?" with dissolve
    "Hiroko reacts to my pained silence with a sorrowful look as she starts to turn away from me."
    show HirokoBetrayal sad
    h "Yeah..." with dissolve
    "It makes me wonder if there's a part of her that realizes I betrayed her."
    show HirokoBetrayal -hiroko -sad with dissolve
    "As she leaves me be I let out a despondent sigh."
    "I guess all I can do now is gather myself and slowly follow her into the school, and the dread that awaits."
    $persistent.hiroko_betrayal_unlock = True
    scene bg blackscreen with longdissolve
    "It's time to face another day..."
    jump Credits
label Epilogue_Con_Kyou_Hiroko_Trickster:
    scene bg street1 day with longdissolve
    "I head back to school the next morning feeling downbeat."
    play music Downtown
    "Before I went to bed last night, I thought to log back on to that hypnosis chatroom and tell everyone that there wouldn't be a follow up to the show I did for them."
    "But instead I discovered I'd been banned..."
    "Yeah. Seems the admin I was talking to before accused me of abuse when I made Nozomi and Hiroko give up their real identities to the audience."
    "Not to mention the way I abruptly closed the cam session. Made him think I wasn't being entirely on the level with everybody."
    "I know I was going to quit being a hypnotist but fuck, that stings."
    scene bg school ext day with blink
    "Well, I won't let it get to me. It felt powerful and exhilarating to have everyone's attention like that, but in the end it was never going to satisfy me."
    h "Hey, look who it is!"
    show Nozomi side smile at center:
        xpos 0.75
    show Hiroko uniform_armup happy at center
    "Not when my real life is so much more important." with dissolve
    ks smile "Hey, girls. Good morning."
    show Hiroko uniform smile
    n happy "Good morning, Kyou~" with dissolve
    "As it is, knowing these two are happy to see me really lifts my spirits."
    ks smile "How's it going?"
    n smile "Good, thanks. I'm still a little buzzed from last night." with dissolve
    n sad_closed "But gosh, I was getting so many online messages it was unreal." with dissolve
    show Hiroko uniform_headhold2 confused_side at flip
    h "Yeah? About what we did?" with dissolve
    n neutral_side "I guess? I recognised some of those online handles from the chatroom, but I just muted everyone." with dissolve
    n smile "Anyway we should head inside; class is about to start." with dissolve
    $renpy.music.set_volume(1.0)
    scene bg corridor day with blink
    $renpy.music.set_volume(0.9)
    "So we walk into school. Together."
    $renpy.music.set_volume(0.8)
    "We make light chatter, but as we make our approach to the classroom Hiroko draws out a sigh."
    $renpy.music.set_volume(0.7)
    show Hiroko uniform_headhold2 sleeptalk at center:
        xpos 0.55
    show Nozomi side neutral_side at center:
        xpos 0.8
    h "Welp. Funtime's over, you guys." with dissolve
    $renpy.music.set_volume(0.6)
    n sad_side "Yeah. We really do need to knuckle down if we're going to get in shape for our entrance exams." with dissolve
    $renpy.music.set_volume(0.5)
    "I find myself sighing and nodding in agreement almost without thinking."
    $renpy.music.set_volume(0.4)
    ks sigh "Oh. Yeah, that's right."
    $renpy.music.set_volume(0.3)
    "I'd kind of forgotten about that in all our excitement, but it's true."
    stop music fadeout 5.0
    show Nozomi neutral
    show Hiroko neutral
    ks neutral "It won't be so bad, will it?" with dissolve
    n smile "We'll get through it together." with dissolve
    h happy_closed "Yeah it'll be dull as shit, but we're all gonna make it." with dissolve
    $renpy.music.set_volume(0.2)
    play music LoudAudience
    show Nozomi smile_side
    show Sayori uniform_folded sleeptalk at center, flip:
        xpos 0.2
    h uniform smile_side "Right, Sayori?" with dissolve
    "Huh. As we pull up to the classroom, I notice Sayori's just standing there by the door, seemingly lost in thought."
    s panicked "H-Hiroko? Nozomi?" with dissolve
    "Was she waiting for us?"
    show Hiroko neutral_side
    n neutral_side "Um, yes it's us. Is something the matter?" with dissolve
    s sleeptalk_concerned "\"Is something the matter\"?" with dissolve
    s uniform scared "D-do you have any idea what you've DONE?" with dissolve
    n sad_side "I... what? I'm confused." with dissolve
    h confused_side "Yeah fucked up our mocks, we get it. So we just gonna stand here or what?" with dissolve
    s uniform_handup "Th-that is not what I..." with dissolve
    n surprised_side "Oh gosh, everyone's really loud in our classroom. Louder than usual anyway." with dissolve
    h smile_side "H'yeah, something's going down in there all right." with dissolve
    h uniform_armup happy "C'mon, let's check it out~" with dissolve
    s uniform angry "{cps=15}W-wait, Hiroko! Before you go in there-{/cps}{w=1.0}{nw}" with dissolve
    scene bg blackscreen with dissolve
    play sound classdoor
    "Sayori's cries are lost on Hiroko as she cheerfully slides the door to our classroom wide open and strolls inside..."
    scene bg classroom day with dissolve
    $renpy.music.set_volume(1.0)
    $ta = Character("Student #1"); tb = Character("Student #2"); tc = Character("Student #3"); td = Character("Student #4")
    ta "Oh my god, they're here!" with dissolve
    "... and almost immediately our class erupts at the mere sight of us."
    show Hiroko confused_side at center
    show Nozomi side sad_side at center:
        xpos 0.7
    h "The... fuck?" with dissolve
    "As I follow behind, I notice everyone huddled around their phones. The only thing that tore them away from their screens..."
    tb "Hahaha, no wonder Nozomi doesn't date boys! You GO, girl!"
    "... is us."
    n frown_side "I... what on earth are you talking about?" with dissolve
    tc "And you're down for anything aren't you, Hiroko? You wild lil' thing!"
    play sound AudienceLaughterLoud
    "I can feel my blood run cold as everyone bursts out laughing."
    "They know. They all know... but HOW?"
    h uniform_armup furious_side "The fuck is THAT s'posed to mean?!" with dissolve
    "I knew someone might have recorded our hypnosis show, but how the hell did it get to everyone in school? And in less than a day?"
    ta "Must be why she's so mad all the time. She obviously doesn't get enough of this action since she split with her boyfriend, you know?"
    h "Hey FUCK YOU, LADY!" with vpunch
    "This is... bad."
    ta "Aww, lighten up girl! Aren't you happy now you've found true love?"
    "Very bad."
    h "The fuck are you dipshits even TALKING about! You..."
    ks surprised "N-No! Don't!"
    scene HirokoNozomiPhone h_shocked n_shocked
    $ renpy.transition(blink, layer="master")
    "With my heart in my mouth, I try to stop our smirking classmate from holding her phone out to Hiroko's outraged face. But I already know it's a futile gesture."
    h "Y-you..."
    h "{size=16}\"I love you, Nozo... mmm... l-love you so much... aaahhnn~ {font=DejaVuSans.ttf}♥{/font}\"{/size}"
    $renpy.music.set_volume(0.8)
    play sound AudienceLaughterLoud
    "There's no stopping Hiroko and Nozomi from finding out the truth..."
    n "Th-this is..."
    n "{size=16}\"Haahn... L-love you too...\"{/size}"
    "No stopping keep them from the video footage that must surely have been playing on loop on every one of these people's phones..."
    h "That's... h-holy shit is that us, Nozo?"
    h "{size=16}\"W-want this... w-want you- mmmmn... all to myself~\"{/size}"
    "No stopping them from hearing their heartfelt declarations of love while they kissed each other so passionately..."
    n "{size=16}\"Oohhhnn... H-Hiroko... y-yess...\"{/size}"
    "It doesn't matter that I told them to forget everything."
    n "W-w-what is this?! W-when did... this happen?"
    n "{size=16}\"I-I'm yours... aaahnn... a-all yours...\"{/size}"
    "They'll remember this."
    show HirokoNozomiPhone h_worried
    h "I... w-we did that? N-Nozo..." with dissolve
    play sound AudienceLaughterLoud
    "And they'll know who was responsible."
    ta "Hahaha why don't you kiss her again, Nozomi? I think your girlfriend needs cooling down~"
    show HirokoNozomiPhone n_scared
    n "S-stay away from me..." with dissolve
    tb "KISS! KISS! KISS!"
    h "{cps=15}Nozomi... c-c'mon, it'll be okay- {w=0.5}{/cps}{nw}"
    n "S-STAY AWAY FROM ME!" with vpunch
    stop music fadeout 5.0
    $persistent.hiroko_nozomi_phone_unlock = True
    scene bg blackscreen with longdissolve
    "My world darkens as Nozomi bolts from the room in tears while Hiroko dashes after her, leaving the class to devolve into chaos."
    scene bg school outdoors day
    with longdissolve
    $renpy.music.set_volume(1.0)
    "With trepidation, I follow as Nozomi retreats outdoors."
    show Nozomi front2 frightened at center:
        xpos 0.75
    show Hiroko uniform_headhold nervous_side at center, flip
    with dissolve
    "I find her sobbing uncontrollably on a nearby bench while Hiroko tries to console her..."
    queue music Sorrow
    h "Nozo... H-hey c'mon, it'll be okay. We'll get through this."
    n "You... y-y-you don't really mean that."
    h sad "Ugh... h'yeah, I know it looks bad. Like, real bad." with dissolve
    h uniform sleeptalk_concerned "But, fuck, I don't even know what happened." with dissolve
    n "K-Kyou happened... o-oh my god... oh my god..."
    ks sigh "Nozomi... Hiroko... I'm sorry."
    n cry "W-why... why would you do such a thing? I told you how dangerous it would be to show our faces and you promised... p-promised you'd stick to the script." with dissolve
    n "You made us endanger ourselves and now we'll never be safe again you fucking... f-fucking CREEP!"
    "I'm about to apologize again, but as I look to her tearful, accusing gaze I realize it's hopeless."
    "She's right. I was so thoughtless about testing the limits of my powers that I completely ignored the risk to them both."
    "There's nothing I can do to make this right for Nozomi. And as for Hiroko..."
    h nervous_side "But you know... N-Nozomi... Kyou didn't do anything to us that we didn't wanna do." with dissolve
    n side sad_side "I... *sniff* w-what? What are you saying?" with dissolve
    "Wait... what IS she saying?"
    h uniform_headhold "It's like I said, you can't make people do stuff they don't want to when they're hypnotized. None of this stuff works unless you let it." with dissolve
    h blush "So like... w-what's that say about us, Nozo?" with dissolve
    "She's... oh fuck, I've really screwed her up, haven't I."
    n sad_closed "It doesn't say anything. He manipulated us." with dissolve
    h uniform "It's okay you know, Nozo... what we said to each other last night..." with dissolve
    "I'm about to say something. Tell Hiroko the truth, that I really did control their minds and actions last night..."
    h uniform_armup "A-an' I mean, if everyone's talking about us anyway..." with dissolve
    show Nozomi sad_side
    "... But nothing comes out. I can only watch as Hiroko caresses her hand against Nozomi's tear-stained cheek..." with dissolve
    h smile_side "It ain't gonna be easy, but at least we got each other... r-right? Right?" with dissolve
    show Hiroko surprised_side
    "... And for Nozomi to recoil and jump up from the bench as if she'd just been slapped in the face." with dissolve
    n "N-no... No, that's not..."
    h uniform "Nozo?!" with dissolve
    n front scared "Stay away from me. Both of you stay the hell away from me!" with dissolve
    h shocked_side "{cps=15}Nozo?! Nozo, come back-{/cps}{w=0.5}{nw}" with dissolve
    n frightened "JUST STAY AWAY FROM ME!" with shake
    scene bg blackscreen with longdissolve
    "Nozomi ran from us. She didn't look back."
    "And my world became darker still."
    "This shit will follow us well after school is done and everyone knows it."
    "Those girls will carry this darkness with them for the rest of their lives."
    "And I'll always be known as the creep who did that to them."
    "I... I never imagined it would turn out like this. It wasn't supposed to end like this."
    "I wasn't supposed to still be alone... fuck, I can't..."
    "I can't face the world anymore..."
    jump Credits

label Epilogue_Con_Kyou_Hiroko_Trickster2:
    scene bg study room eve with longdissolve
    "It's been about a week since that day."
    play music Downtown
    show Hiroko neutral_side at center, flip:
        xpos 0.25
    show Nozomi side neutral_side at center, flip
    show Sayori uniform_folded neutral at center:
        xpos 0.75
    s "... Is everyone clear on this? Do I need to explain it again?" with dissolve
    "A week since I thought Hiroko was gullible as all hell and made her a part of my hypnosis stream."
    h uniform_headhold2 sleeptalk "Yeah yeah, we get it. See look, I wrote it down an' everything." with dissolve
    "And I'm thinking about this while Sayori's giving us a math lecture. Yeah, we all gave in to her pestering about taking some time to review our failure in the mock exams."
    show Hiroko neutral_side
    s uniform_handup smile "Anyone can copy my notes, Hiroko. But do you understand it?" with dissolve
    "We really needed it after all, if only to clear our heads after what we were doing before."
    h frown_side "Man, you're really getting a kick out of this, aren't ya, teach?" with dissolve
    "But did Hiroko and Nozomi really need to stonewall me every time I bring up hypnosis now?"
    n happy "Ehehe, algebra is a bit of a headscrew sometimes, but I think you explained it better than Kobayashi." with dissolve
    "I mean, we're still hanging out at least. We even lunched together a few times."
    s uniform_folded "Good. Now I believe you three are beginning to flag and cram school beckons, so that shall be all for today." with dissolve
    "And yet, there's this distance between us. It's like they don't really trust me."
    show Nozomi smile_side
    h uniform smile_side "Alrighty! We doing this tomorrow too?" with dissolve
    "It bothers me. I can't deny that it bothers me."
    s happy "Naturally. I am thinking we focus on the sciences next, then you should be all caught up." with dissolve
    n laugh "Sounds good to me~ Have a good evening, Sayori." with dissolve
    "And now we're finishing up for another day..."
    n smile "Kyou..." with dissolve
    "I have to say something before it's too late."
    show Nozomi neutral
    show Hiroko neutral
    ks confused "Yeah hey, Hiroko? Can you hold up for a second?" with dissolve
    show Hiroko uniform_headhold nervous_side
    hide Nozomi
    show Nozomi side sad_side at center
    show Sayori neutral_right
    multi "..." with dissolve
    "... I don't like that look they're giving each other. But I'll push past it."
    ks "You, uh... you think any more about what we were talking about the other week?"
    show Nozomi neutral
    h nervous "Oh, um... h'yeah, let's take a raincheck on that, okay?" with dissolve
    ks "It's just..."
    h smile "O-okay, see you tomorrow~" with dissolve
    show Nozomi:
        linear 1.5 xpos -0.5
    show Hiroko at flip:
        linear 1.5 xpos -0.75
    stop music fadeout 5.0
    ks surprised "H-hey, wait! Why can't we... {w=1.0}talk it out?"
    hide Nozomi
    hide Hiroko
    "Goddamn, they could hardly get out the room any faster." with dissolve
    "{cps=15}Shit. I gotta go after them. I have to know-{/cps}{w=1.5}{nw}"
    queue music Measured
    s sleeptalk "I wouldn't bother if I were you." with dissolve
    show Sayori neutral_right
    "Sayori..." with dissolve
    ks confused "What?"
    "She must have talked to her friends about me. Or they talked to her; obviously she would've had some thoughts about us hanging out now."
    "How much does she know?"
    s uniform_handup "I know what you're thinking, Kyou, and yes, I know enough." with dissolve
    s sleep "Enough to know that you have wormed your way into their company but not, as you may have hoped, into their confidence." with dissolve
    ks "But why?"
    s uniform_folded irritated "Why would they? Do they have reason to trust you?" with dissolve
    s frown_right  "Have you not betrayed them before?" with dissolve
    "This is getting me nowhere."
    scene bg corridor eve with blink
    "So I leave Sayori to preach to an empty classroom and dash down the corridor to catch up to the only people I need to hear from."
    show Hiroko uniform_headhold2 surprised at center, flip:
        xpos 0.25
    show Nozomi front surprised at center
    ks surprised "Hiroko! Nozomi!" with dissolve
    "I have to know where I stand."
    n concerned "Kyou, we're going home now. Can't this wait?" with dissolve
    ks sigh "No it can't! Hiroko, please... I'm sorry, okay?" with dissolve
    "I have to know if they can trust me again."
    h nervous "Sorry? Dude, sorry for what?" with dissolve
    ks "You know I wanted to get back at you, with the yawning and the cam show stuff, but I took it too far."
    ks "I kept putting you under hypnosis even when I knew you were uncomfortable with it, just because I could."
    show Nozomi side sad_side
    show Hiroko nervous_side
    multi "..." with dissolve
    ks sad "Maybe you really do enjoy being hypnotized, Hiroko. But I never should've taken advantage of you like that, just because I wanted to see how far I could take it."
    ks "So I'm sorry. I want to put all that behind us, because I'll never do that again."
    show Nozomi neutral_side
    h sleep "Hmm..." with dissolve
    stop music fadeout 5.0
    h neutral_side "... So it's just like you said, huh, Nozo." with dissolve
    ks confused "It... was?"
    play music Sorrow2
    n front2 sigh "Kyou, yes, we've been talking about what happened. About that cam show and... well, everything before that." with dissolve
    show Hiroko sad
    n neutral_left "We couldn't be certain before, but it sure sounded like there was something more going on." with dissolve
    n neutral "I know hypnosis can't force a person to go along with anything a hypnotist wants, but if you were to establish a rapport with the hypnotee, gain their trust..." with dissolve
    n sleep "Well, it can unlock some doors. Lower some inhibitions. It can surely be used as a tool to manipulate others, push them further than they would've wanted." with dissolve
    n concerned "And that's what you've confessed to, isn't it? When you said you took advantage of her?" with dissolve
    ks "Y-yeah, but... but..."
    h sad_side "But it weren't all bad. That what you're gonna say isn't it?" with dissolve
    h uniform nervous "Like, fuck, I dunno if I could've gotten my scholarship without you putting all that motivation in my head." with dissolve
    h uniform_armup angry "But come on, man, you tortured me for kicks, didn'tcha? And you made me think I was into that shit? Am I s'posed to let that go?" with dissolve
    ks surprised "I know, I fucked up, but that's never gonna happen again, I promise! I was good about the cam show, wasn't I?"
    h uniform_headhold sleeptalk_concerned "Ugh, I dunno man, I gotta... Gotta think." with dissolve
    h nervous "Just give me some more time, alright? Stop pushin'." with dissolve
    hide Nozomi
    hide Hiroko
    with longdissolve
    "So they turn their backs and walk away. This time I make no effort to stop them."
    "Maybe it's asking too much of them to forgive me. I really did put Hiroko through a ton of shit just because I thought I could get away with it."
    "It didn't matter if she was gullible as hell, or if my penlight was affecting her more deeply than I could imagine."
    "I exploited her trust in me. I don't know if anyone can look past that."
    "So despite everything... despite everything I've worked for, I'm back where I started."
    "Alone..."
    jump Credits

    label Epilogue_Con_Kyou_Hiroko_Trickster3:
    scene bg corridor eve with longdissolve
    "The next few days passed slowly. Painfully."
    queue music Downtown
    "As soon as we got back to school, our homeroom teacher bombarded us with the need to study for our mock exams this week."
    "The moment that happened, it's like we had an unspoken agreement to stay out of each other's way until then."
    "Maybe a little time apart would do us some good. I'm sure that's what we were all thinking, even though it seems ridiculous."
    "I sure know I couldn't focus on these damned mocks, and I can't imagine Hiroko doing any better."
    "In any case, we've just sat those exams, and I'm going to leave all my regrets concerning that firmly in the room over there."
    "I'm going to stand loitering around the hallway outside with only one thing on my mind."
    show Hiroko uniform_headhold sleeptalk at center
    show Nozomi front2 sleeptalk at center:
        xpos 0.25
    show Sayori neutral at center:
        xpos 0.75
    "It's time to talk to them again." with dissolve
    h "Fuckin' glad that's over."
    "No. Not \"them\"..." with dissolve
    n "That... makes two of us, Hiroko."
    "Yeah. Hiroko."
    show Hiroko neutral
    show Sayori
    s uniform_handup concerned "Did you really find it so difficult?" with dissolve
    show Hiroko uniform sad_side at flip
    show Nozomi neutral_right
    h "H'yeah, well it ain't like I had a chance anyway. That tourney took it all outta me." with dissolve
    "It's been driving me crazy, wondering what she even thinks of me now."
    s neutral "That may be, but I do hope you have not simply given up. Even a sports-focused college will require you to demonstrate some academic ability." with dissolve
    h uniform_headhold2 irritated "Gawd, I know! Just cut me some slack, okay?" with dissolve    
    h frown_side "I got another shot at it, {nw}" with dissolve
    show Hiroko frown
    $ renpy.transition(dissolve, layer="master")
    extend "and..."
    "It's just then, in the middle of talking back to Sayori's tedious lecturing, that she eyes me watching her from across the hall."
    h sleeptalk "Look, I get it, but can we not do this right now?" with dissolve    
    show Nozomi side sad_side at flip
    h neutral "There's someone I gotta talk to." with dissolve
    show Nozomi sad
    s concerned_right "... \"Got to?\"" with dissolve
    "I guess it's a little comforting to know she *has* been thinking of me."
    n smile_side "Alright. We'll talk later tonight, okay?" with dissolve
    hide Hiroko
    show Hiroko uniform smile_side at center
    h "Yeah, you know it~" with dissolve
    hide Sayori
    hide Nozomi
    show Hiroko neutral
    "The smiles those two share leave me wondering. Sayori might be wondering herself, as she seems to ask a question of Nozomi that leaves her looking a little flustered." with dissolve
    stop music fadeout 5.0
    h frown "C'mon, let's go someplace." with dissolve
    "... Right, I can't let myself get distracted again."
    scene bg school ext eve with blink
    "So we head out, with Hiroko making smalltalk the whole way."
    play music Eons
    show Hiroko neutral_side at center
    h "How'd you do anyhow?" with dissolve
    ks confused "Huh? What do you mean?"
    h confused "Uhh, in the mocks we just did?" with dissolve
    h frown "You're s'posed to be smart, right?" with dissolve
    ks sigh "Can we not talk about this?"
    h uniform_headhold2 rolleyes "Okay, wow. Am I ever taking THAT back." with dissolve
    "I scoff at her, but she is making me curious as she leads me down the street and deeper into town."
    scene bg cafe eve
    show Hiroko neutral_side at center
    with blink
    "She seems pretty normal after how we left things. Normal for her, anyway."
    h neutral "Alright, we'll do this here. Cool?" with dissolve
    "Although as she makes her declaration, I look at where she's led us..."
    ks confused "A coffee shop?"
    "Certainly doesn't seem like the kind of place I imagined she'd be into."
    h frown "What? You think I was taking you to the gym?" with dissolve
    "Thought it'd be more of a... Nozomi kind of thing?"
    h irritated "Get a drink and sit your ass down!" with dissolve
    scene HirokoCafe frown with blink
    "Regardless, I get my order and sit down across from each other, waiting for her to start."
    h "..."
    show HirokoCafe sigh
    h "Look... All that shit you pulled? I'm sorta over it now." with dissolve
    ks confused "Sorta?"
    show HirokoCafe worried
    h "C'mon man, you scared the shit outta me with all that hypno stuff." with dissolve
    show HirokoCafe worried_left
    h "Like yeah, I get you weren't literally brainwashing me with that fuckin' light, but you sure did a great job of making me feel like you were, didn't ya." with dissolve
    "I sigh."
    ks sigh "Yeah, I know. I took it too far, and I already said I'm sorry for that."
    show HirokoCafe neutral_left
    ks sigh "And if it makes you feel better I decided to ditch that penlight." with dissolve
    show HirokoCafe neutral
    h "Yeah? Still wanna hypno folks though?" with dissolve
    "This time I offer an indifferent shrug as I nurse the coffee cup in my hands."
    ks neutral "I don't know."
    show HirokoCafe neutral_left
    h "Hmm..." with dissolve
    h "Couldn't blame ya if you do. You sure got the talent for it."
    show HirokoCafe sigh
    h "Hypnosis ain't so terrible when the one doing it ain't being a dickhead, it turns out." with dissolve
    show HirokoCafe neutral
    h "So if you really meant what you said the other day? Maybe you could take another crack at it with someone." with dissolve
    "Someone. Just not her, then. Seems I really did blow it."
    "But wait..."
    ks confused "Nozomi really did convince you hypnosis could be a good thing, huh."
    show HirokoCafe frown
    h "Uhh, yeah? She's my bestie, case you forgot. And she knows way more about this shit than you do, that's for sure." with dissolve
    show HirokoCafe frown_left
    h "... Kinda think I should thank you for bringing that out of her." with dissolve
    ks "What?"
    show HirokoCafe irritated
    h "Ugh... just forget it. I dunno what I'm saying." with dissolve
    show HirokoCafe sigh
    h "I just... thinking about how it all felt, when Nozo was trying so hard to get me all comfy in my own head... take the fear outta me..." with dissolve
    show HirokoCafe worried
    h "Sorta made me think about when you were actually trying to help me. Y'know?" with dissolve
    "Tapping the side of my cup, I nod slowly as I recall those first days with her."
    ks neutral "I was actually happy for you too, hearing about how well you were doing in practice."
    show HirokoCafe worried_left
    h "H'yeah... Man, you really made me realize I had to work on my mentality. Keep my head in the game. Stop letting the little things get to me." with dissolve
    show HirokoCafe neutral 
    h "You can't have done it on purpose. Like, you only hypnotized me cause you thought you had a chance to do it, right? But still..." with dissolve
    show HirokoCafe sigh
    h "I dunno, man. You're a freakin' weirdo an' you still creep me out a lil'. And I'm trying really hard to see past that." with dissolve
    show HirokoCafe neutral_left
    stop music fadeout 5.0
    h "Because when you try, you make me wanna try myself; run a lil' cooler. For you, Nozo... even that Keiko chick." with dissolve
    show HirokoCafe smile
    queue music Warm_Romantic
    h "You do good work when you try." with dissolve
    "Hiroko breaks into the smallest of smiles as she looks me straight in the eye. And I feel compelled to smile back."
    "Maybe after all the hostility between us. All the shouting, and the manipulation and revenge-taking..."
    "Now she won't keep calling me a creep. Now I can finally start talking to girls like her and... and Nozomi."
    ks smile "Speaking of trying, have you and Nozomi tried anything else hypnotic since then?"
    show HirokoCafe frown blush
    h "W-what?! Fuck off, dude, you don't get to ask me that!" with dissolve
    "... Wow, she totally has. Or she's going to."
    show HirokoCafe irritated
    h "Fuckin' nerve of you, swear to God..." with dissolve
    "Is that why they're meeting up again later? Ugh, no I can't ask her that either."
    ks sigh "Alright, fine! Forget I said anything."
    "Okay, so maybe I still can't talk to girls all that much..."
    scene bg cafe eve
    show Hiroko uniform_armup irritated blush at center:
        ypos 1.2
        linear 2.0 ypos 1.0
    with blink
    h "Rrrgh... gotta fuckin' ruin everything don'tcha."
    "As Hiroko hauls herself up from her chair, I take a moment to wonder if I've undone whatever goodwill she'd built up for me yet again."
    h uniform_headhold2 -blush "Nope. {w=0.5}Runnin' cooler... {w=1.0}{nw}" with dissolve
    show Hiroko sleeptalk
    $ renpy.transition(dissolve, layer="master")    
    extend "cool. I'm cool."
    "But no. I'm not talking to the same girl who was screaming at me a week ago. She told me as much."
    h neutral "We're cool, Kyou. Don't worry about it." with dissolve
    "Hiroko's working on herself."
    ks neutral "Yeah, alright. So let me try again."
    "I need to work on myself as well."
    ks smile "Just... thanks for talking to me, Hiroko. I'm glad you're doing better."
    ks "And if you want to hang out again... well..."
    h smirk "Oh, you're gonna. You still wanna do that hypno show thingy, right?" with dissolve
    "... To be honest, that plan I had totally slipped my mind."
    h smile "I ain't going on stage with ya, but I bet we can brainstorm some kinda plan. I know Nozo's gonna be up for that." with dissolve
    "And she still wants to honour that promise she made me? Sorta?"
    h uniform "So... lunchtime tomorrow?" with dissolve
    "I wasn't sure I was ever going to perform hypnosis again, but now I'm starting to feel excited about the prospect."
    ks "Uh... Yeah. Okay!"
    "If Hiroko wants me to try... then I'll try."
    h happy_closed "Yeah, good talk. Seeya tomorrow." with dissolve
    "I'll do it right this time."
    ks "See you tomorrow!"
    hide Hiroko with dissolve
    "No more tricks. No more fancy lights."
    "Maybe this excitement I'm feeling for hypnosis won't last, if neither of those girls are gonna want to go under for me. But if they still want to talk to me?"
    "If girls want to talk to me. Hell, if *people* won't find me creepy anymore now I'm putting myself out there?"
    "I'm going to try..."
    jump Credits

label Epilogue_Con_Kyou_Sayori_Doll:
    scene bg blackscreen with longdissolve
    "A lot has happened since that day..."
    s "So... what is hypnosis?"
    "But it's getting hard to think back while I'm in the middle of..."
    scene bg classroom eve
    show Sayori uniform alert_neutral
    play music Audience
    with longdissolve
    s alert_neutral_right "I know some of you will recall what happened in this very classroom a year ago." with dissolve
    "Well, this."
    s alert_smirk_right "Some of you more vividly than others." with dissolve
    "Sayori directs her eyes to Nozomi sitting at the front of our assembled audience, who awkwardly squirms in her seat from the attention."
    s uniform_folded alert_neutral "But many of us came away from that believing hypnosis was purely a confidence trick enacted on stage for entertainment." with dissolve
    s alert_sleep "That it is not a serious subject worthy of consideration beyond such bounds." with dissolve
    s alert_smile_right "So tonight, I am hoping to change a few people's perceptions. Because hypnosis is a very real and fascinating phenomenon." with dissolve
    s "And to best explain that... well..."
    s alert_happy "I do not think you will appreciate a lecture on tonight of all nights, so Kyou and myself will be giving a demonstration while we attempt to explain the process." with dissolve
    "I look around the audience and they seem to be getting invested. At least the people who know Sayori anyway."
    s alert_neutral_right "{size=15}That was your cue.{/size}" with dissolve
    ks surprised "{size=15}Huh? O-oh, yeah.{/size}"
    "Sayori snaps me back into focus as I turn to her, then back to the crowd and I realize..."
    ks frown "S-so, I'm gonna be hypnotizing Sayori in front of you guys."
    "I've got a show to do!"
    s uniform alert_smirk_right "And how are you going to do that, Kyou?" with dissolve
    play sound AudienceLaughter
    show Sayori alert_smile_right
    "... Man, don't sound so smug in front of these guys, Sayori. You're making me nervous on purpose!" with dissolve
    ks "Uh... r-right, well hypnosis is about entering an enhanced state of focus, suggestibility and imagination."
    ks "So, Sayori, in a moment I'm gonna need you to focus where I tell you to..."
    "I then swallow, as I turn nervously to the assembled crowd of classmates, a few parents and our homeroom teacher."
    ks smile "But first I'll need a couple of volunteers to help me with her."
    s alert_laugh "I am far too much for him to handle on his own." with dissolve
    play sound AudienceLaughter
    show Sayori alert_smile
    "I watch as a few hands hesitantly raise themselves while Sayori watches with me before she starts to point." with dissolve
    s uniform_handup "I think I would like you and... you." with dissolve
    ks "Yeah, you two! Can you come over here?"
    show Akiko side sigh at center:
        xpos 0.75
    a "Don't call us \"you two\"." with dissolve
    show Nozomi side sad at center, flip:
        xpos 0.25
    n "What do you need from us?" with dissolve
    show Akiko neutral
    ks smile "Okay so, uh, Akiko, if you could stand right behind Sayori and..." with dissolve
    "I hesitate to say it."
    s uniform_folded alert_smirk_right "Get ready to catch." with dissolve
    show Nozomi surprised_side
    a surprised_side blush "HUH?!" with dissolve
    ks "Right... And Nozomi, just standby for now, okay?"
    show Akiko sad noblush
    show Sayori uniform alert_smile
    n sad "Uh, sure..." with dissolve
    show Nozomi neutral_side
    show Akiko neutral_side
    "As she nods, Nozomi seems to spy the two chairs I have beside me, arranged a few feet apart. " with dissolve
    "She then looks back to Sayori, who smiles back at her calmly while she pops her shoes off."
    "I swear I just saw Nozomi's eyes glimmer as I turn my attention back to the task at hand."
    ks "Now, there's all kinds of ways you can hypnotize someone."
    ks "Like, you can get them to focus on something like a pocketwatch, or you can have them lie back and relax really deeply."
    show Sayori alert_smile_right
    show Akiko neutral
    show Nozomi neutral
    ks "But what I'm going to do with Sayori is... well, first I'm gonna need her hand." with dissolve
    "Sayori knows what's coming of course, so she offers me her hand immediately for me to take."
    ks "Cool. Now Sayori, I need your arm too. So if you could just let it go completely limp for me?"
    "I can feel her arm loosen up as I start to swing her hand gently back and forth while I try to address those watching as clearly as I can."
    ks "Great, so now I'm going to pull her arm around like so. And Akiko, I need you to be ready to catch her, okay?"
    a surprised "Y-you mean I... o-o-okay!" with dissolve
    "As Akiko tenses in anticipation I start to pull Sayori's arm more aggressively. First in a left to right motion, then going in a circle then straight up and down..."
    "And while I do that, my free hand reaches above Sayori's face as I start to make a spidering motion with my fingers."
    show Nozomi neutral_side
    show Akiko sad_side
    show Sayori alert_neutral_right
    ks "Now just follow the path of my fingers, Sayori. Follow them..." with dissolve
    "I say that more for the benefit of those watching as she's already tracking my fingers dancing in her face, seemingly unconcerned with my messing with her arm."
    ks "That's right, following my fingers, focusing on them while also standing up nice and straight."
    "Sayori suggested I impress that last part to her during rehearsals and yeah, I see her point about that."
    "Especially with what we're about to show the class."
    ks frown "Standing straight while watching up and down, round and round and -{w=0.5}{nw}"
    show Sayori alert_sleep
    show Akiko surprised_side
    show Nozomi surprised
    play sound fingersnap
    $ renpy.transition(dissolve, layer="master")
    extend "SLEEP! Relaxing now deeper and deeper. {w=0.5}{nw}"
    play sound fingersnap
    extend "Deep in trance now, Sayori."
    "Just as I mouthed the word \"sleep\", I tugged her arm down sharply as I transitioned the hand in front of her to snapping my fingers as quickly as I could."
    "Akiko tensed in fright as I raised my voice, hands raised by Sayori's shoulders, but it seems she needn't have bothered."
    ks smile "So did you guys see that? How I was moving her arm around and twinkling my fingers in her eyes?"
    n neutral "{size=15}A butterfly induction.{/size}" with dissolve
    a neutral_side "Hm?" with dissolve
    n sad_closed blush "Oh, n-nothing." with dissolve
    ks "All that stuff occupies the mind, especially if you have to focus on it like Sayori did."
    show Nozomi sad noblush
    show Akiko neutral
    ks "So when I tugged her arm and told her to sleep, it gave her mind something clear and easy to focus on." with dissolve
    a sad "So she fell asleep standing up?" with dissolve
    "Ah, that spoiled my rhythm. Sayori warned me I could get questions while I was doing this."
    "Just gotta deal with it head on."
    show Nozomi neutral
    ks sigh "It's not like she's literally asleep; she's just on a different level of consciousness right now. She can still hear us." with dissolve
    ks "And when you're in this state of hypnosis you can become really suggestible, and you can use it to achieve some awesome things."
    "I then turn back to Sayori as I reach up to touch the top of her head."
    ks smile "For example..."
    "I need to move on quickly."
    ks "Sayori, I want you to just imagine now that your body is becoming incredibly rigid. From the top of your head, your neck..."
    "I then reach down to pat her shoulders, then her forearms as the class watches me curiously."
    show Nozomi neutral_side
    show Akiko neutral_side
    ks "Your shoulders and arms, your chest; all as if there's a strong metal bar running all the way through you. Totally stiff, totally immovable." with dissolve
    "Next I tap the sides of her calves and the tops of her feet before moving to pat her arms and head again."
    ks "Your legs, your feet, all made of metal. Every muscle in your body, your chest, everything, completely stiff, totally unable to move in any way."
    "Feeling her arm gently, it sure feels like Sayori's ready for the real show to begin."
    ks "{size=15}Can you hold her shoulders now, Akiko? We're going to carry her.{/size}"
    show Akiko surprised_side
    "Akiko's eyes widen, but after being teased with the prospect of having to hold Sayori enough times I think she's ready for this." with dissolve
    show Akiko sad_side
    show Nozomi frown_side
    "And as she puts her hands to Sayori's shoulderblades I turn to instruct Nozomi only to see her nod at me and look to Sayori's feet." with dissolve
    "She seems to know what's up, so with Akiko ready I give Sayori a gentle push into the waiting hands of our student council president."
    show Akiko surprised_side
    "There's a hushed gasp among the audience, and from Akiko herself as Sayori falls stiffly backwards against her while she strains from the weight." with dissolve
    "Watching Akiko so out of her depth is a little fun, but I have work to do myself, as I place my arms underneath Sayori's lower back and thighs..."
    "... and Nozomi reaches down to grab her friend's ankles before we collectively heave Sayori's rigid body up in the air."
    ks happy "Haha, see how rigid she is? It's like she really thinks she's made of iron or something!"
    a surprised "Rrrrgh, K-Kyouuu I'm gonna drop her!" with dissolve
    ks smile "Okay, okay, c'mon just set her down here."
    scene Sayori StageShow_Catalepsy with blink
    "And with that the three of us carefully move backwards towards the waiting chairs before we set her down."
    "Sayori's head rests on one chair, the heels of her feet on the other as we let her go. The rest of her body forming a perfect, straight bridge between the two."
    a "A-and she's just going to lay like that?"
    "I nod triumphantly to Akiko before addressing the crowd."
    ks "Yeah, so what Sayori's experiencing now is full body catalepsy. She's in a state of rigidity that she just wouldn't be able to accomplish were she conscious."
    show Sayori StageShow_Catalepsy arm_up
    "And by way of emphasising my point, I push down gently on Sayori's stomach as everyone watches." with dissolve
    ks "That's just how powerful the hypnotic state can be. You could even sit on her and she'd take your full weight!"
    "There's a few gasps, from Akiko as well as those watching, although as I spare a glance at the adults in the room I quickly add:"
    ks happy blush "B-but we're not gonna be testing that tonight, haha! You'll just have to take my word for it."
    show Sayori StageShow_Catalepsy arm_down
    "Yeah, I think I'm already pushing my luck as it is with some of the more concerned authority figures in the room. I think I'd better wrap this up." with dissolve
    ks smile noblush "Anyway, I think we'd better get Sayori back on her feet, okay, ladies?"
    $persistent.sayori_stageshow_catalepsy_unlock = True
    scene bg classroom eve
    show Akiko side neutral_side at center:
        xpos 0.75
    show Sayori alert_sleep at center
    show Nozomi side neutral_side at center, flip:
        xpos 0.25
    with blink
    ks "Waking in one... two... {w=0.5}{nw}"
    show Sayori alert_drowsy
    $ renpy.transition(dissolve, layer="master")
    extend "three, Sayori. Wide awake and alert and refreshed."
    "Sayori blinks herself back into consciousness, to the relief of some in the audience it seems."
    ks "Hey, Sayori. How are we doing?"
    s "I... am good."
    show Sayori alert_smile
    "She blinks a few more times, registering all the eyes on her before turning to smile." with dissolve
    s "From the looks on their faces, it would seem the demonstration was a success."
    ks smile "Oh yeah, it worked without a hitch."
    show Sayori uniform_folded alert_smile at flip
    show Akiko surprised_side blush
    "And with that, Sayori turns to Akiko with a grin." with dissolve
    a "Wh-what?"
    s "Thank you. For having my back."
    a sigh "Y-yeah, of course, Sayori. Always." with dissolve
    show  Akiko smile_side noblush
    "She then turns to the class and gives them a bow." with dissolve
    s uniform alert_sleep "And thank you all for coming out." with dissolve
    s alert_smile_right "I regret that we had so little time to demonstrate what hypnosis is capable of, or give a more in-depth explanation..." with dissolve
    s alert_happy "But if you have any questions please do not hesitate to ask us once we have cleared the stage." with dissolve
    ks smile blush "Y-yeah, thanks everyone!"
    "There's some polite applause from those watching. And from the looks some are giving I feel like I'm being seen for the first time."
    scene bg blackscreen with dissolve
    "... I guess the show went okay?"
    pause 0.5
    scene bg corridor eve
    play music Peaceful
    show Nozomi side frown_side at center:
        xpos 0.35
    show Hiroko neutral_side at center:
        xpos 0.75
    show Sayori alert_smile at center, flip:
        xpos 0.15
    show Akiko side smile_side at center:
        xpos 0.55
    with longdissolve
    ks smile "So, uh, what did you think?"
    "After all was said and done, I meet up with Sayori and the others while the rest of the culture fest carried on without us."
    show Nozomi front pout
    n "I mean, I guess it was okay. Not as good as the one our seniors did last year, but I get you were trying to do something educational." with dissolve
    ks sigh "Ouch."
    h sleeptalk "H'yeah, the one that dude did last year made it look like hypno was a bunch of dumb shit you do when you wanna get drunk but can't." with dissolve
    show Nozomi side sad_side blush at flip
    show Akiko laugh
    show Sayori alert_smirk
    n "S-say what?!" with dissolve
    show Akiko smile
    show Sayori alert_smile
    h smile_side "But Sayori goes up there and tries to explain and I'm like huh, maybe there's something to it." with dissolve
    a smile_side "I know what you mean. Especially seeing it all up close like I did, and I can't imagine Sayori pretending to be all stiff like that..." with dissolve
    a happy "It really makes you think~" with dissolve
    n frown_side "I-I suppose... It just seems strange how this happened without our class representative knowing about it." with dissolve
    show Nozomi sad_side
    show Hiroko neutral_side
    a smirk_side "It does? I thought scrutinizing the culture fest events was the student council's job." with dissolve
    a laugh "Ahaha, but what do I know~" with dissolve
    show Nozomi neutral_side noblush
    a smile_side "Anyway, I need to see how the rest of the school's doing. Busy busy, you know?" with dissolve
    s uniform_folded "Thank you for everything, Akiko. See you soon." with dissolve
    a smirk_side "Yeah. Soon." with dissolve
    show Sayori alert_concerned
    "Akiko turns to leave, but a moment later something happens to stop everyone in their tracks." with dissolve
    show Akiko uniform_down armband_down surprised_side
    show Nozomi surprised
    show Hiroko shocked_side
    s uniform alert_angry "Akiko, WAIT!" with dissolve
    a "!!"
    show Hiroko neutral_side
    show Nozomi sad
    s uniform_folded alert_sleeptalk blush "... That was more forceful than I had intended, but regardless..." with dissolve
    show Nozomi:
        linear 1.0 xpos 0.15
    show Sayori at flip:
        linear 1.0 xpos 0.35
    pause 1.0
    show Nozomi neutral_side
    s alert_concerned noblush "This may not be the most appropriate time to air this, but I need to while I still have the nerve, so Akiko..." with dissolve
    show Nozomi:
        xpos 0.15
    show Sayori at flip:
        xpos 0.35
    s uniform "I regret that we drifted apart." with dissolve
    a sad_side "Sayori... We're busy people, I understand." with dissolve
    s alert_sleeptalk "And that is the excuse I told myself. That my work encompassed everything; that I could not afford to leave room for anything else." with dissolve
    s alert_concerned "It was never true. I know I could have been better, so Akiko..." with dissolve
    show Akiko laugh
    "As Sayori trails off, Akiko just lets out a playful laugh." with dissolve
    a blush "Sayori, look, I really have to go, but... w-wow, haha!" with dissolve
    a smile_side noblush "Um, do you think you'll still be around at the end of this?" with dissolve
    "She gestures vaguely around her and Sayori nods assertively."
    s uniform_folded alert_annoyed "Absolutely. I'll find you." with dissolve
    a smirk_side "Not if I find you first~" with dissolve
    hide Akiko
    "Akiko leaves us with that, as she scampers gleefully away." with dissolve
    h surprised_side "I forgot you two used to hang out." with dissolve
    s uniform_handup alert_sleep "It was quite a while ago, wasn't it." with dissolve
    h uniform_armup happy "Yeah! Anywho, I'm real happy you perked up again, sis~ Was worried about ya." with dissolve
    s alert_smile  "Mhmhm. I do appreciate you looking out for me, Hiroko." with dissolve
    h uniform smile_side "Yeah, same to you, buddy~ Now I'm gonna head out." with dissolve
    show Nozomi smile_side
    ks smile "See you later." with dissolve
    "Hiroko waves at her friends, then spares me a glance."
    h sleeptalk "Oh, yeah... thanks for looking out for her too, I guess." with dissolve
    hide Hiroko
    "And off she trots..." with dissolve
    s alert_smirk_right "I think she is warming up to you." with dissolve
    ks sigh "You think?"
    n sad "She is, in her own way." with dissolve
    hide Sayori
    show Sayori uniform_folded alert_smirk at center:
        xpos 0.35
    s "And what about you?" with dissolve
    stop music fadeout 40.0
    show Nozomi sad_side
    "Nozomi, having been quiet for so long, exchanges gazes with each of us before letting out a sigh as she clears her throat to speak." with dissolve
    n sad_closed "I'm... I'm so confused about you both. These past few weeks..." with dissolve
    hide Nozomi
    show Nozomi front2 sleeptalk_concerned at center:
        xpos 0.15
    show Sayori alert_concerned
    n "I-I mean, I want to be happy for you, Sayori. I do." with dissolve
    n concerned "And Kyou, it's nice that you're coming out of your shell, but I feel like I've been frozen out." with dissolve
    show Nozomi side sad_side at flip
    n "I don't understand..." with dissolve
    ks "N-Nozomi..."
    s uniform "Keeping this from you was my decision, Nozomi. And I apologize for making you feel this way." with dissolve
    s alert_sleeptalk "I had my reasons- {w=1.0}{nw}" with dissolve
    n sad_closed "I'm sure you did, Sayori. Anyway, I'm going to go look around." with dissolve
    hide Nozomi
    show Sayori alert_neutral
    show Nozomi front2 sleeptalk at center:
        xpos 0.15
    n "Have a good night." with dissolve
    hide Nozomi
    "Nozomi quickly disappears into the crowd and the two of us are left awkwardly alone." with dissolve
    "I gotta say something to break the tension..."
    ks sigh "Sorry."
    s alert_sleeptalk "Not everything is your fault, believe it or not." with dissolve
    s alert_concerned_right "I for one have been making far too many mistakes lately." with dissolve
    s alert_concerned "Too many to correct in one evening..." with dissolve
    "She looks back into the corridor where Nozomi disappeared to."
    "It sure would suck if this is how our night is gonna end."
    ks neutral "Yeah... So do you want to get out of here?"
    show Sayori uniform_handup alert_surprised_right
    "Sayori blinks out of her reverie and looks to me." with dissolve
    s alert_concerned_right "Oh? And where would you take me?" with dissolve
    "I simply shrug at her, smiling, as I take a step backwards with intent."
    ks smile "We're going to take a walk."
    scene bg study room night with blink
    play sound dooropen
    "As the lock turns, Sayori opens the door to a familiar place, away from the hustle and bustle of the festival that rages around us."
    show Sayori alert_sleeptalk
    s "How ironic. That this room could become a sanctuary from the stresses of the world." with dissolve
    ks happy "Haha, right?"
    play sound doorclose
    "Closing the door behind me, I exhale audibly as the quiet sets in."
    play music Luminous_Rain
    ks smile "I thought it'd be a good time to clear our heads. Been a busy day."
    s alert_concerned_right "Or a busy week. I admit I have felt myself getting into old habits again." with dissolve
    s uniform_folded alert_concerned "Finding a balance between caring for my work and for myself has not been easy." with dissolve
    ks "But you're doing it."
    s alert_smirk_right "Heh." with dissolve
    ks neutral "... What?"
    s uniform_handup "Oh, just something I have pondered over since we started working together." with dissolve
    s alert_smile "This sudden transition of yours from a socially inadequate loner to a vaguely competent human being." with dissolve
    ks frown "Hey, come on!"
    s alert_happy "Mhmhmhm. I'm sorry, but it is an enigma to me. What could have effected such a change?" with dissolve
    show Sayori alert_smile_right
    ks sigh "I dunno what to tell you. All I've been doing lately is study for school and work on my hypnosis and that penlight." with dissolve
    ks "At least until I dismantled that thing."
    s uniform_folded "And I maintain that was the correct thing to do, Kyou." with dissolve
    s alert_smile "But it is interesting... After all, a good hypnotist needs to be in tune with those they intend to hypnotize." with dissolve
    s alert_smile_right "If they cannot build a comfortable rapport, and speak clearly and confidently, then they cannot hope to achieve what they intended." with dissolve
    s uniform_handup "So perhaps that truly was all you needed: A commitment to a soft science to round out the edges of your personality." with dissolve
    s alert_smirk_right "And someone patient enough to bring it out of you." with dissolve
    ks sigh "Eh, whatever."
    s uniform_folded alert_sleep "I think you could take it further." with dissolve
    ks surprised "Huh?"
    s alert_concerned_right "Why do you look so perturbed? I honestly have not seen you as fulfilled as you are now." with dissolve
    ks "But... Sayori, this isn't what I wanted to do with my life! I wanted to work in tech."
    "Yeah. That's all I wanted to do."
    ks frown "I mean, sure being a hypnotist is interesting, and getting to put people into a trance and have fun with them or try to help is kind of a thrill."
    ks "With you especially, but..."
    s alert_pout_closed blush "Well, far be it for me to dictate your career for you, but I do feel you have developed a passion for this." with dissolve
    s alert_pout "And your career aspirations for the tech world seem... somewhat directionless, if you don't mind me saying so." with dissolve
    s uniform alert_concerned_right noblush "I only ask that you do not dismiss it so readily." with dissolve
    ks sigh "Sure... I'll think about it, I guess."
    "But I think we're getting sidetracked here."
    ks smirk "But this is so like you, isn't it."
    s alert_surprised_right "Huh? What is?" with dissolve
    ks "We came here to relax and already you're stressing out worrying about me!"
    s uniform_folded alert_sleeptalk_concerned "Ugh. It is not just you. I worry about all of you." with dissolve
    s uniform "I worry that it was too late to reorganize my life with our entrance examinations so imminent." with dissolve
    s "And..."
    ks neutral "You're worried about us?"
    s uniform_folded alert_sleeptalk blush "..." with dissolve
    "Oh, man. She really has thought about it. But if she's set on making it into med school then how can I..."
    scene SayoriDollEnd1 with blink
    "No, this isn't the time to be thinking about this stuff right now."
    ks "There'll be another time where you can worry about all of that, Sayori. A better time."
    s "I... don't necessarily disagree. But here?"
    ks smile "Right now it's doll time."
    show SayoriDollEnd1 sleep_down
    $ renpy.transition(longdissolve, layer="master")
    s "{size=15}Ahh...{/size}"
    "Sayori was right about getting me to let go of that penlight."
    ks "That's right. Doll time. It's alright to let your worries slip away when it's doll time. Letting everything turn to plastic when it's doll time."
    "And not just because it was dangerous. It turned out I really didn't need it. Especially not in her case."
    "The amount of suggestibility she has, to say nothing of her trust in me; it's pretty incredible."
    show SayoriDollEnd1 kyou_arms arms_down
    $ renpy.transition(longdissolve, layer="master")
    "So now, taking her hands gently in mine, I slowly unfold them before pulling them down to rest stiffly at her sides."
    ks "No cares. No concerns... just plastic."
    show SayoriDollEnd1 kyou_chin head_up sleep_up
    "Cupping a hand on her chin, I then slowly lift and tilt her head to face straight. She'd be looking right at me if her eyelids hadn't shuttered." with dissolve
    "She looks so perfect. And with her brow having uncreased from the suggested mindlessness, so worry free."
    show SayoriDollEnd1 kyou_back
    $ renpy.transition(longdissolve, layer="master")
    ks "So I was thinking, Sayori... You can stay a few minutes like this, nothing but plastic on your mind, allowing yourself to enjoy that feeling."
    ks "Just for a little while. And then, we can go back out there and enjoy the rest of the festival together; just having a nice, relaxing time."
    ks "Does that sound good to you, Sayori?"
    "I wait with her a moment, taking in the serenity of her face as I await her response."
    show SayoriDollEnd1 smile
    "And then she smiles..." with dissolve
    $persistent.sayori_doll_good_end_unlock = True
    jump Credits

label Epilogue_NonCon_Kyou_Sayori_Doll:
    "A lot has happened since that day..."
    ks frown "U-uh... hi, everyone."
    "But it's getting hard to think back while I'm in the middle of..."
    play music Audience
    scene bg classroom eve with dissolve
    "Well, this."
    ks frown "Some of you know me around here? B-but for anyone who doesn't, I'm, uh... I'm Kyou Koyama and tonight I'm going to be showing you hypnosis."
    "My hypnosis show. I'm actually doing it."
    ks "Now... y-you might remember there was a hypnosis show last year too."
    "But man, I'm bricking it. It's harder than I thought planning and rehearsing this all by myself."
    ks "We had people up on this same stage and some guy with a pocketwatch getting them to do some crazy stuff..."
    ks "Well, I'm trying to do something a little different. Because to be hypnotized is... w-well, it's not something everyone can do very well. Or even at all!"
    "I can't complain, though. This is what I wanted, after all."
    ks neutral "To be a really good hypnotic subject you need to be smart. You need to have a creative mind; be good at visualizing and maintaining a lot of focus."
    "And besides..."
    ks "So I thought... i-if I want to give a really good demonstration of what hypnosis can do, something you can really believe... I couldn't just pick people from the audience."
    ks "I needed a person who's just like I described. And in this school... I don't think there's anyone smarter or more focused than the person I'm doing this show with tonight."
    "I told her I'd handle everything."
    ks smile "S-so please welcome my... m-my assistant for the show. Someone you probably DO know: Sayori Watanabe!"
    play sound applause
    show Sayori maid alert_smile_right at center
    "All she has to do is follow my directions and not worry about a thing." with dissolve
    s alert_happy "Thank you, everyone. I am happy to be here." with dissolve
    "A role she's been very willing to fulfil, I might add. Since that night the other week we haven't had a single fight about anything."
    n "S-Sayori?! What's going on?"
    show Sayori alert_smile_right
    ks "Actually... th-this hypnosis show technically started hours ago." with dissolve
    "As I look across the room I notice a lot of surprised faces among the audience. Not just from Nozomi, sat uncomfortably in the front row."
    s maid_handup alert_surprised_right "Kyou? I am not sure I follow." with dissolve
    "From our classmates, our teachers and elsewhere, it seems no one expected our star student to resurface from all her extra-curricular time off to be helping me of all people."
    "And on this of all things."
    ks "So I'm sure you're all wondering why she's wearing this getup."
    n "Why is she wearing it at all? Sayori, you didn't even help us at the maid café this morning! What gives?"
    s alert_neutral "I... As I told you, I had other duties to attend to. I do not understand the confusion." with dissolve
    "But I think that just makes this act all the more believable. I couldn't pull this off with anyone but her."
    ks "I'll clear that up in a minute, Sayori. But first, could you tell the audience what you're wearing?"
    "No one would ever think that one of our most respected students would simply put on an act this goddamned silly."
    s maid_folded alert_irritated "I... ugh, am wearing regulation school uniform, as should be obvious to all of you." with dissolve
    play sound AudienceLaughter
    s alert_annoyed_right "... Why are you laughing? Was there something in those teas that said café was handing out?" with dissolve
    "With a chuckle, I place one hand on Sayori's shoulder and she looks instinctively to my other hand, raised in front of her eyes."
    "I can sense the anticipation welling inside her."
    ks "{cps=10}Aaaaand {/cps}{nw}"
    play sound fingersnap
    show Sayori maid alert_sleep
    $ renpy.transition(dissolve, layer="master")
    # show bg blackscreen onlayer toplayer
    # $ renpy.transition(dissolve, layer="master")
    # $ renpy.transition(dissolve, layer="toplayer")
    extend "sleep!"
    # hide bg classroom eve
    # hide Sayori
    scene SayoriChicken1 kyou1 k_smile sayori2 s_sleep with blink
    # hide bg blackscreen onlayer toplayer with longdissolve
    "As I loudly snap my fingers, Sayori's eyes flicker before her head suddenly drops like a stone."
    h "{size=16}The fuck did he just do?!{/size}"
    "Keeping a hand on her, I make sure my assistant's standing firmly upright before I address my bewildered audience with a small amount of pride."
    show SayoriChicken1 kyou1 k_smile_side sayori2 s_sleep
    k "S-so, I guess it's time I let you all in on something. I asked Sayori to put on one of the spare costumes my class was using for their maid café event this morning." with dissolve
    k "She's no longer consciously aware of this... because of hypnosis!"
    show SayoriChicken1 kyou1 k_neutral_side sayori2 s_sleep
    "I pause for effect, although everyone seems more confused than impressed." with dissolve
    "... I'd better just move on quickly."
    show SayoriChicken1 kyou2 k_neutral_side sayori2 s_sleep
    k "L-like I said, a smart, creative and most of all willing mind can be an amazing hypnotic subject." with dissolve
    show SayoriChicken1 kyou2 k_neutral sayori2 s_sleep
    k "And when you're as good as Sayori here, you can be conditioned to very quickly and easily enter an extremely deep, altered state of consciousness." with dissolve
    show SayoriChicken1 kyou2 k_neutral_side sayori2 s_sleep
    k "She's not actually asleep when she's like this, even if she looks it. She's really in a heightened state of focus." with dissolve
    k "While she's hypnotized, her conscious thoughts take a backseat to make way for her subconscious."
    show SayoriChicken1 kyou2 k_smile_side sayori2 s_sleep
    k "And when someone enters a state like this, they can become incredibly suggestible. So suggestible that you can alter their very perception of reality." with dissolve
    k "So when I hypnotized her this morning, I put it to her that she was still wearing her school clothes."
    k "And you all saw it, right? She totally believes there's nothing strange about what she's wearing!"
    k "But can we affect her reality in other, bigger ways? Let's find out!"
    show SayoriChicken1 kyou1 k_smile sayori2 s_sleep
    "I then turn my attention back to my patiently-entranced assistant, but trying to speak loudly enough for everyone to still hear me." with dissolve
    k "Now Sayori, in a few moments I'm going to ask you to wake, but when you do you will slowly turn into a... chicken."
    n "{size=16}O-oh my god, he isn't!{/size}"
    k "Your human language will slowly turn into a chicken's. Your bodily movements will gradually become more like a chicken's."
    k "You may notice yourself turning into a chicken and you may try to resist while we talk, but the more you try, the more chicken-like you feel yourself becoming."
    k "And before too long, you will find you have completely turned into a chicken right here on stage."
    k "Your thoughts, your actions, everything, just like a chicken. Understand?"
    show SayoriChicken1 kyou1 k_smile sayori2 s_sleeptalk
    s "Uh-... uh-huh..." with dissolve
    show SayoriChicken1 kyou1 k_smile sayori2 s_sleep
    k "Wonderful. Furthermore, you will awaken with no memory of having just been hypnotized and will become annoyed that I haven't actually started the show yet." with dissolve
    k "And now, accepting your new reality and waking up in one, two..."
    show SayoriChicken1 kyou1 k_smile sayori2 s_waking
    $ renpy.transition(dissolve, layer="master")
    play sound fingersnap
    k "... three, wide awake!"
    "Snapping my fingers beside her ear once more, I watch as Sayori's deep blue eyes flicker back into life before looking back over her curious observers."
    scene bg classroom eve
    show Sayori maid alert_surprised_right at center
    with blink
    s "Uh..."
    ks smirk "So, those are your normal school clothes, right?"
    s maid_folded alert_irritated "O-of COURSE they are! Now if you don't mind I am eager to move on with the show we agreed upon for these people." with dissolve
    play sound AudienceLaughter
    "Cue more laughter from the audience; whether from Sayori still denying her situation or from the anticipation of what they're starting to expect will happen next..."
    s alert_annoyed_right "... I do not understand any of you tonight." with dissolve
    "And I gotta say, getting the crowd on my side and seeing Sayori so fully committed in front of all these people is giving me the confidence I need to keep going."
    ks happy "Okay, okay, I'll get us started in a minute!"
    "I grin at her. It's probably gone unnoticed by our observers but I can already see Sayori's head start to bob involuntarily, in the same way I've seen during our rehearsals."
    ks smile "But before that, I wanted to ask how you're doing. Are you feeling okay?"
    s maid_handup alert_neutral "{cps=10}I'm {/cps}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend alert_surprised_right "u- uck! F-fine."
    ks neutral "Are you sure? It sounded like you just coughed."
    show Sayori alert_irritated
    "Sayori frowns and clears her throat as she puts a hand to her neck." with dissolve
    s "Very... uck, s-sure, now if you please."
    play sound AudienceLaughter
    "This time she had to clap her left hand over her right elbow to stop herself from flapping it like a wing. That gets a few more amused reactions."
    ks smile "{cps=20}Just making sure! Now, I want you to clear your head and- {/cps}{w=0.5}{nw}"
    s alert_surprised_right "Boc boc!" with dissolve
    play sound AudienceLaughter
    scene SayoriChicken1 kyou2 k_laugh sayori3 s_shock blush with blink
    "And that gets pretty much everyone laughing, including me."
    "She couldn't even try to cover her mouth, as both her arms now start to flap involuntarily by her sides."
    show SayoriChicken1 kyou2 k_smirk sayori3 s_struggling blush
    k "I'm sorry, what was that?" with dissolve
    s "{cps=20}I just... {w=0.5}{/cps}{nw}"
    show SayoriChicken1 kyou2 k_smirk sayori3 s_shock blush
    extend "B-BUCAWK!" with dissolve
    play sound AudienceLaughter
    "I gotta say, she's ahead of schedule. It's barely been more than a minute since I woke her up."
    "Are you even resisting this at all, Sayori? Or maybe you're trying to resist a little too much? Is that what's happening?"
    show SayoriChicken1 kyou2 k_smirk sayori3 s_struggling blush
    k "If you're not feeling up to it you can always... chicken out." with dissolve
    s maid_folded alert_scared_right "I'm... c-cluck... fine n-now get on with it!"
    play sound AudienceLaughter
    "She says that, but my maid/chicken can't help herself as she starts to crouch down towards the floor, her folded arms now flapping with all the fervour of free-range poultry."
    show SayoriChicken1 kyou3 k_smile sayori3 s_struggling blush
    "And I in turn, can't help myself but pet her bobbing head over her bonnet while people start to crack up laughing in the front row." with dissolve
    k "Alright, we're starting now. Just relax, you're doing great."
    s alert_sleepy "B-boc... boc boc..."
    k "It's okay. Just let it happen now."
    hide SayoriChicken1
    show SayoriChicken1 kyou3 k_smile sayori3 s_chicken
    $ renpy.transition(longdissolve, layer="master")
    s "{cps=15}Boc... boc... {/cps}{w=0.5}{nw}"
    extend " BU-CAWK!" with vpunch
    $persistent.sayori_chicken1_unlock = True
    play sound AudienceLaughter
    scene bg classroom eve
    show Sayori maid_folded alert_panicked_blank_right at center
    with blink
    show Sayori:
        linear 1.0 ypos 1.2
    pause 1.0
    show Sayori alert_surprised_blank_right at center:
        ypos 1.2
    with dissolve
    "A few seconds more and her embarrassed, forced clucking has given way to unashamed squawks as she crouches towards the ground and begins to strut around the stage."
    h "{size=16}Man, she does it way better than you, Nozo.{/size}"
    n "{size=16}Oh, s-shut up.{/size}"
    "There's no shame in her eyes now. She's just a happy hen, strutting around me before an incredibly amused audience."
    ks happy "Hahaha, isn't she amazing?"
    show Sayori:
        linear 1.5 xpos 0.2
    s "Boc-boc-boc..."
    "For a short while I leave Sayori to roam the stage, lost in her own world while everyone watches in amused fascination."
    "I'm a little tempted to let her flap her way into the audience but, eh, I'd better call her back."
    ks smile "Here, Sayori. Come here, I got something for you."
    show Sayori at flip:
        xpos 0.2
    with dissolve
    show Sayori at flip:
        linear 1.0 xpos 0.5
    "Besides, I have one more little trick to pull off before I'm done with my \"chicken\"."
    show Sayori at flip:
        xpos 0.5
    s "Cluck cluck..."
    ks "Are you hungry? I got some feed for you."
    show Sayori alert_panicked_blank_right
    "Sayori thankfully comes back to me when I call her. And as I hold out my hand in front of her, she tilts her head to look at it with a wide-eyed, innocent stare." with dissolve
    ks "It's right here in the palm of my hand. Help yourself."
    scene SayoriChicken2 head_down dazed kyou with blink
    play sound AudienceLaughter
    "My mere suggestion is enough to have my entranced bird bobbing down to peck her lips against my palm."
    "It's... really cute how much she's let herself become so uninhibited since that night."
    "But I can't dwell on that thought. I know I'm on a short clock here, and it's time to put an end to this routine before we outstay our welcome."
    ks smile "That's a good bird. Now I'm going to snap my fingers and the moment you hear it you will be free of every suggestion I made to you tonight, understand?"
    s "B-boc boc!"
    play sound AudienceLaughter
    ks "... I'm gonna take that as a yes."
    play sound fingersnap
    hide SayoriChicken2
    show SayoriChicken2 head_down surprised
    with dissolve
    s "{cps=20}Boc... {w=0.5}b-{/cps}{nw}"
    show SayoriChicken2 head_up embarrassed
    $ renpy.transition(dissolve, layer="master")
    extend "uhhh!"
    show SayoriChicken2 head_up embarrassed_side
    play sound AudienceLaughter
    "The sight of the study club president suddenly coming to her senses and looking around in a panic might have gotten the loudest laugh of the evening." with dissolve
    ks "Hey, take it easy. Welcome back."
    show SayoriChicken2 head_up embarrassed
    s alert_surprised_right "I... i-it is done?" with dissolve
    "The smile on my face must tell her everything she needs to know."
    $persistent.sayori_chicken2_unlock = True
    scene bg classroom eve
    show Sayori maid alert_smile_right blush at center:
        ypos 1.3
        linear 2.0 ypos 1.0
    with blink
    ks smile "Sayori really has a brilliant mind to be able to do this stuff in front of all of you and I know she was a little shy about it so..."
    show Sayori:
        ypos 1.0
    "This past couple of weeks have been... well, SHE has been amazing."
    ks happy blush "L-let's give her a hand, everyone!"
    play sound AudienceClapping
    show Sayori alert_smile
    "The way she's committed to letting go and truly refreshing herself. To allow herself that kind of freedom really is remarkable." with dissolve
    s alert_happy blush "It... was my pleasure. Truly." with dissolve
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "And I really, really could not have done any of this without her."
    scene bg corridor eve
    play music Peaceful
    show Nozomi side sad_side at center:
        xpos 0.35
    show Hiroko nervous_side at center:
        xpos 0.75
    show Sayori maid alert_smile at center, flip:
        xpos 0.15
    show Akiko side neutral_side at center:
        xpos 0.55
    with longdissolve
    ks smile "So, uh, what did you think?" with dissolve
    "After all was said and done, I meet up with Sayori and the others while the rest of the culture fest carried on without us."
    n sad_closed "I just... I don't understand it at all." with dissolve
    "Yeah... I got to see Nozomi's uncomfortable reactions quite well, sitting in the front row as she was."
    n sad_side "This is why you avoided us, Sayori? Because you had this all planned out with..." with dissolve
    n sad "... Kyou?" with dissolve
    show Sayori alert_neutral_right
    "Sayori spares me a glance before turning back to her friend." with dissolve
    s maid_handup alert_sleeptalk "I do apologize for my deception, but Kyou and I felt the element of surprise was important to maximize our impact." with dissolve
    "Well I mean, she was the one who proposed we keep this a secret, back when we started all this. Although it seems pointless to argue about it now."
    h uniform_headhold2 sleeptalk "H'yeah, you guys made an impact all right." with dissolve
    "Not to mention, with all the fun we've been having together I guess I never gave the idea to involve Nozomi or anyone else another thought."
    show Hiroko neutral_side
    a surprised_side "I'll say! I sure wasn't expecting you to take to the stage, Sayori!" with dissolve
    s alert_neutral "Hm?" with dissolve
    a happy "I mean, you told me you were going to be a backseat driver for all of this." with dissolve
    n surprised "She... told you what?!" with dissolve
    a uniform laugh "But wow, hahaha! You really looked like you were having fun up there~" with dissolve
    a smirk_side "So what changed your mind? Did you like being hypnotized more than you thought?" with dissolve
    show Nozomi surprised_side
    s alert_smile "{cps=15}Well... as it happens- {/cps}{w=0.5}{nw}" with dissolve
    n frown_side "You... Sayori, you told her you were doing a hypnosis show but couldn't tell me?" with dissolve
    show Akiko smile_side
    show Sayori alert_neutral
    n irritated "I-I mean, you couldn't tell me and Hiroko? Your friends?" with dissolve
    a sad_side "Yeah... why did you tell me instead of your friends, Sayori?" with dissolve
    s maid alert_smile "As I said, the element of surprise was important." with dissolve
    "... Man, is no one going to talk about what we actually did out there?"
    h confused_side "Well, you sure got us. Didn't suspect a thing." with dissolve
    "Or even notice me at all?"
    stop music fadeout 5.0
    h nervous_side "But, like... you're gonna come back to study club now, right? We could really use you in there." with dissolve
    s maid_folded alert_concerned "Ah, yes... the study club." with dissolve
    show Nozomi neutral_side
    show Akiko neutral_side
    s alert_sleeptalk "Well... concerning that..." with dissolve
    a sad_side "You're still on break from the study club, Sayori?" with dissolve
    queue music Measured
    n shocked_side "HUH?! S-Sayori, what on earth is going on with you?!" with dissolve
    s alert_rolleyes "Oh, it is of no concern to anyone. I simply needed time to recharge, that is all." with dissolve
    h confused_side "H'yeah, but you're coming back now, right? It's been two weeks, sis." with dissolve
    n sad_side "S-so you haven't been doing anything after school? Just this thing with Kyou?" with dissolve
    s alert_sleep "Correct." with dissolve
    n front2 angry "Urrgh, WHY am I the last person to hear about all of this?" with dissolve
    show Nozomi neutral_left
    s maid_handup alert_concerned "Because I knew you would react this way. Please, I do not need anyone's concern; everything is fine." with dissolve
    n side sad_side "Sayori, no it's not... it's NOT fine! Why would you do this? You NEVER do this!" with dissolve
    "I can hear Sayori clicking her tongue as she regards Nozomi and her other friends coldly."
    s alert_irritated "Then perhaps you did not know me as well as you thought." with dissolve
    n sad_closed "I'm just worried about you, Sayori." with dissolve
    s alert_annoyed "How I spend my extra-curricular time is my own business and no one else's." with dissolve
    show Nozomi sad_side
    show Hiroko sad_side
    s maid_folded "So I shall resume my studies when I am ready and not a moment sooner, is that understood?" with dissolve
    n sad_closed "A-alright..." with dissolve
    "Sayori nods at their anxious faces with a snort."
    s maid alert_sleeptalk "I would never have imagined the after-show would be more stressful than the performance itself. Yet here we are." with dissolve
    show Nozomi sad_side
    s alert_neutral "Now if you will excuse me, I am going home to get changed." with dissolve
    show Sayori alert_neutral_right at flip, center:
        xpos 0.15
    "As she turns away from the group, she suddenly spares a glance in my direction." with dissolve
    s "Kyou? Are you coming?"
    hide Sayori
    show Nozomi sad
    show Akiko neutral
    show Hiroko frown
    "I can suddenly feel everyone's eyes on me as Sayori takes her leave of us." with dissolve
    ks surprised "I-I, uh..."
    "They must think I have something unseemly going on with her, for her to be like this."
    a sigh "Just go to her, Kyou. At least she listens to somebody around here." with dissolve
    "But no one could possibly know the truth."
    ks "Y... yeah..."
    scene bg blackscreen with dissolve
    stop music fadeout 5.0
    "None of them could possibly know Sayori like I do now."
    scene bg ext school eve
    show Sayori maid alert_sleep at center
    with longdissolve
    ks surprised "Sayori! Wait up!"
    "As I dash out of the school, I catch up with Sayori as she reaches the gates."
    queue music Eons
    s alert_smile_right "Ah, there you are. I was beginning to think you would leave me adrift." with dissolve
    "She smiles at me, in that carefree way she's become fond of doing lately."
    ks smile "Ah, not a chance."
    "But I gotta say, seeing her like this now..."
    ks neutral "But you're going home, right?"
    s maid_handup alert_neutral blush "Well... concerning that..." with dissolve
    "... I'm starting to worry about her again."
    s alert_smile_right "It is what I implied in front of the others, but I was hoping we could return to yours." with dissolve
    ks sigh "S-Sayori, you don't mean..."
    s maid_folded alert_sleeptalk "I do mean it." with dissolve
    s alert_neutral_right noblush "Experiencing hypnosis in a public setting was a unique kind of pleasure, and I was happy to grant you the opportunity to display your skill before a wider audience." with dissolve
    s alert_neutral "I am positive that you have changed many people's perceptions of you, and mostly for the better." with dissolve
    s maid alert_sleep "But I shall be plain with you. I am finding the scrutiny it attracted upon me to be quite stressful, and I must request your services again." with dissolve
    s alert_smile_right "So if you would indulge me, I'd very much like for you to grant me a private session to... clear my mind once again." with dissolve
    ks neutral "I... sure, we could do that."
    "It's certainly not that I don't want to, and with her in that outfit? She really is tempting me."
    "But..."
    show Sayori alert_neutral_right noblush
    ks "But you ARE going back to the study club now that we're done with the show, right? Like we agreed?" with dissolve
    s maid_handup alert_neutral "I will... strongly consider it." with dissolve
    "That's not an answer that fills me with confidence..."
    show Sayori alert_neutral_right
    ks sigh "Sayori... just promise me you'll go back. Please." with dissolve
    show Sayori maid_folded alert_rolleyes
    "She clicks her tongue at me and sighs." with dissolve
    s "Oh, not you too. At least I can understand this sort of talk coming from Nozomi."
    s alert_neutral_right "But you, Kyou? You are the one who encouraged me to absolve myself from responsibility." with dissolve
    s alert_sleeptalk "You are the one who gave me the freedom to escape into my own mind." with dissolve
    "I mean, yeah. But I know someone has to be responsible around here, and if not her then..."
    ks frown "I-I know, but you just needed to take a little step away from it all so you weren't burned out any more. You can't stay away forever."
    ks "And you... you understand that, right?"
    s maid alert_surprised_right "O-of course I understand what's at stake here! More than you could know!" with dissolve
    ks neutral "So promise me. Promise me you'll start taking your studies seriously again."
    show Sayori alert_neutral_right
    ks "Because until you do, I'm not going to hypnotize you any more." with dissolve
    s alert_annoyed_right "You... what?" with dissolve
    ks sigh "{cps=15}I'm just saying-{/cps}{w=0.5}{nw}"
    s maid_folded "You are \"just\" attempting emotional blackmail, and I am beginning to lose some of the esteem I held you in." with dissolve
    ks surprised "{cps=15}What? But Sayori, I-{/cps}{w=0.5}{nw}"
    s alert_angry_right "DON'T you \"but Sayori\" me. I will not be so crassly manipulated!" with dissolve
    "Whoa. I forgot how intense she can be sometimes."
    s maid_handup "You cannot simply grant me this wonderful sensation, compel me towards it like a siren's call..." with dissolve
    s alert_irritated blush "... To addict me to it... only now to deny me in my time of need!" with dissolve
    "She hasn't been this way since..."
    ks frown "Sayori, come on!"
    "Since our last fight."
    s alert_annoyed_right "I can't allow it." with dissolve
    ks angry "Sayori! People are looking-{w=0.5}{nw}"
    s maid alert_angry_right "I WON'T allow it!" with vpunch
    "Shit, I gotta calm her down. Manage the situation, just as I've been managing her this past couple weeks."
    ks sigh "A-alright! We'll work something out but just... stop, okay? You're making a scene."
    show Sayori alert_surprised
    "Sayori takes a sudden breath and glances around us, as if she's just remembered where we are." with dissolve
    s maid_handup alert_concerned_right "Ah... I apologize. That was unseemly of me." with dissolve
    s alert_sleeptalk "But don't you see? This merely reinforces my point." with dissolve
    s maid "I remain uncentered. Unfocused. Unready." with dissolve
    ks neutral "Sayori..."
    s alert_concerned_right "I need to be hypnotized. And you are the only one I can turn to." with dissolve
    show Sayori maid_folded
    "As she speaks, Sayori steps a little closer and gently takes my hands in hers as she looks to me pleadingly." with dissolve
    s alert_drowsy "You are the only one who can make me wonderful." with dissolve
    s alert_sleeptalk "So please... make me your doll." with dissolve
    s alert_sleeptalk_concerned "Make me free again." with dissolve
    "Well... again, it's not like I don't want to."
    stop music fadeout 5.0
    ks neutral "Let's go home, Sayori."
    scene bg blackscreen with dissolve
    "And if she truly needs it this much..."
    scene bg k bedroom eve with dissolve
    "... Then I'll take her to the only place she feels she can be free."
    "Free of stress. Free of thought. Free of any semblance of personal responsibility."
    play music Diary
    ks neutral "It's alright now, Sayori."
    ks "I thought you only needed a reset, a little chance to center yourself, but it's clear your problems go so much deeper."
    ks neutral "You still need me. And I want you to know that's okay."
    ks "I mean, it feels good to be needed. And besides, I sorta need you too, Sayori."
    scene cg sayori doll bad end:
        ypos -1.0
        linear 30.0 ypos -0.0
    with blink
    s "..."
    ks "So... it's fine. This is fine."
    ks "You can come to me any time you want and I'll be here. Here to help you manage your stress and get you working again, so don't worry."
    ks "I'll be responsible for both of us from now on."
    ks "And in return... you'll be my doll."
    ks "You'll look pretty for me. Let me play with you."
    ks "Because that's what you want... isn't it, Sayori?"
    s "..."
    ks "We don't need anyone else. Do we?"
    s "..."
    "Satisfied, I smile back at my doll sitting so ornamentally on my bed. So perfectly at peace with herself."
    ks smile "Yeah. That's what I thought. Then it's settled."
    scene bg blackscreen with longdissolve
    ks "I'll take care of everything..."
    $persistent.sayori_doll_bad_end_unlock = True
    jump Credits
label Epilogue_Redemption_Sacrifice:
    scene bg k bedroom day with longdissolve
    "It's been a couple weeks since that fateful day."
    "Needless to say, I've had a lot of time to spend at home since then."
    "After all, there's no school. And where else do I go?"
    "Yeah, life's felt pretty hopeless since I got expelled..."
    play sound doorbell
    "... Until today, anyway."
    scene bg k room day with blink
    "This morning, I got a phone call right out of the blue."
    "And I don't know if I'm ready for this..."
    play sound dooropen
    ks casual smile "Uh... h-hey."
    play music Warm_Romantic
    "But it's given me some hope."
    show Akiko side casual noarmband happy with dissolve
    a "Kyou Koyama..."
    a laugh_wink "It's good to see you again~" with dissolve
    play sound doorclose
    "Closing the door behind her, Akiko regards me with a breezy smile on her face."
    a casual_down smile "So, um... you look well?" with dissolve
    "She's lying, though. I look like someone who's barely seen daylight in two weeks."
    "At least I had time to freshen up before she got here."
    ks casual sigh "Thanks..."
    show Akiko casual_down smile_side
    "And as she steps into the living room with me, I remember vividly the last time she was here." with dissolve
    "I've had a lot of thoughts about that time since then."
    a neutral "So, how are you doing, Kyou? Are you holding up okay?" with dissolve
    "Thoughts that I need to push aside for the moment."
    ks neutral "Yeah, I'm okay. I guess."
    a laugh "Nope! That's not good enough!" with dissolve
    ks sigh "Seriously? I think \"okay\" is the best I can be right now, don't you think?"
    a laugh_wink casual "Ahahaha~" with dissolve
    a smile "What I mean is, you need to be more specific than that." with dissolve
    a smirk "I want to know EVERYTHING that's been going on with you! Spill!" with dissolve
    "She seems even pushier today than I remember. But I can't help but smile at her."
    "After everything that's happened, I'm actually kind of happy to give her what she wants."
    ks smile "Okay, okay! Not gonna lie, I've been kinda going through the motions since I got kicked out of school."
    ks "I'm studying for our entrance exams, but yeah, it's been hard."
    show Akiko neutral
    "Akiko nods." with dissolve
    ks neutral "Sayori's been talking to me online and giving me some advice, helping me focus and stuff, but... man, I don't know, 'Kiko."
    ks "Who's going to give a good job to a guy like me?"
    show Akiko sad
    ks "It all feels kind of pointless, you know?" with dissolve
    a casual_down "Yeah... I understand it looks pretty bad for you right now. But please don't lose hope." with dissolve
    a sad_side "I mean for one thing... Well, you heard about Hiroko, right?" with dissolve
    ks "Yeah, Sayori told me. They accepted her appeal, so they're going to re-evaluate her for the scholarship."
    a casual smile "Exactly! You did it, Kyou!" with dissolve
    "I find it hard to share her enthusiasm. After all, I've had a lot of time to think about this stuff."
    show Akiko neutral
    ks sigh "Yeah, and she still might not get it because of me. That tourney was her best shot and I took it away from her." with dissolve
    ks "She'll never get that back."
    a sigh "Th-that may be true, but still... I don't know many guys who'd do what you did." with dissolve
    a sad_side "Yesterday, when Risa told me what really happened, I was so shocked." with dissolve
    ks "She really wasn't supposed to tell anyone, you know."
    a casual_down sad "I know. And no-one's going to find out from me, I swear." with dissolve
    a sleep "But what I wanted to say is... it's okay to have regrets about what you've done in the past." with dissolve
    a sad "With that said, you're not that person anymore. You've owned your mistakes." with dissolve
    a sad_side "Yes, you wronged Hiroko terribly, and maybe she'll never forgive you for it." with dissolve
    a casual "I don't... I don't know if she CAN forgive what you did to her." with dissolve
    a sigh "But you did everything you possibly could to set things right." with dissolve
    a neutral_side "So... it's time to move on, Kyou." with dissolve
    a neutral "You deserve to find happiness." with dissolve
    "I deserve to find happiness, huh."
    "Whether that's true or not, it sure feels good to hear someone say that about me."
    a smile "I know we still don't know each other very well, but it's obvious you've come a long way, Kyou. You've learned so much." with dissolve
    a happy "You've got this~" with dissolve
    ks smile "Thanks..."
    "It's almost bringing a tear to my eye. But for something that's bothered me since she called me."
    ks "So... let's talk about you now."
    stop music fadeout 15.0
    a neutral "About me?" with dissolve
    "Risa didn't seem to get along very well with Akiko while I was in class with them, so why would she tell her about me?"
    "Akiko didn't give much away on the phone."
    ks "How've you been? Things okay with you?"
    a casual_down "... {w=1.0}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend smile "Yup, I'm okay. Don't worry about me~"
    "That pause doesn't exactly fill me with confidence. Not to mention the fact she's here at all."
    ks neutral "Yeah? You sure?"
    "I mean, it's the weekend of the culture festival at school. The student council president must be extremely busy, yet she has time to chill with me?"
    queue music Downtown
    a neutral_side "Um..." with dissolve
    "Not that I don't appreciate her being here but, yeah... something doesn't add up."
    ks smirk "You can't make me tell you everything and expect me to go easy on you, can you?"
    a laugh "Ahahaha~" with dissolve
    a smile "I guess not. But I figured you're the one who needs help right now." with dissolve
    a casual_down laugh blush "A-and besides, wouldn't be right to get help from one of my patients, would it? Ahaha~" with dissolve
    "Ugh. I know you're wanting to get into therapy, Akiko, but really?"
    a sad_side "... That came out wrong." with dissolve
    ks sigh "Come on, 'Kiko. You're not my therapist and I'm not your patient."
    ks "So just tell me what's up. I mean..."
    show Akiko sad
    "Dare I say it..." with dissolve
    ks smile "We're friends, aren't we?"
    a neutral noblush "F-friends..." with dissolve
    a casual "It feels too soon to think of you as a friend." with dissolve
    a smile "I'm not saying it feels wrong, though." with dissolve
    "I smile at her, relieved. But then I get back to my point."
    ks "So come on, tell me what's going on. From one friend to another."
    stop music fadeout 10.0
    scene cg k room day
    show AkikoHypno upright
    play sound sitting
    with blink
    "I gesture to the couch and she obligingly takes a seat."
    show AkikoHypno sleep
    a sleep "Okay, Kyou. If you insist." with dissolve
    show AkikoHypno sad
    a casual_down neutral_side "... Please don't freak out, okay?" with dissolve
    "I can only nod as she steels herself with a breath."
    play music Monologue
    show AkikoHypno sleep
    a sleep "It's just... well, a lot of people were so mad at you for what you did. And that kind of anger doesn't vanish in a day." with dissolve
    show AkikoHypno neutral
    a neutral_side "After you were gone, they recalled how some of us didn't believe every little thing they heard about you." with dissolve
    show AkikoHypno frown
    a neutral "And that's when my student council work got so much more stressful." with dissolve
    "So. Even when I do the right thing, I fuck someone over..."
    ks casual neutral "'Kiko..."
    "All the shit Akiko's going through right now is my fault!"
    show AkikoHypno sad
    a sad_side "I never said I didn't believe her. Never denied that you caused her pain..." with dissolve
    show AkikoHypno irritated
    a sad "All I wanted was more answers... and those rumours about you were so out there." with dissolve
    show AkikoHypno surprised
    a surprised "There just HAD to be more to the story..." with dissolve
    show AkikoHypno sad
    a sleep "... Was it really so bad that I wanted the truth?" with dissolve
    ks sigh "Shit. I'm so sorry, 'Kiko. I never meant for you to get hurt because of me."
    "Akiko shakes her head wearily."
    show AkikoHypno sleep
    a sad_side "Please... don't blame yourself for this, Kyou. This doesn't belong on your conscience." with dissolve
    show AkikoHypno neutral
    a sigh "It's why I didn't want to talk about this. It's not fair on you." with dissolve
    show AkikoHypno sad
    a sad "And besides, there's nothing you can do to help anyway. You can't stop other people from being jerks." with dissolve
    show AkikoHypno frown
    a frown "That's all on them!" with dissolve
    show AkikoHypno neutral
    a casual "Anyway, you don't have to worry about me. I can handle this kind of stuff." with dissolve
    show AkikoHypno irritated
    a frown_side "I'll always get back up. Bow. Ready my sword and face them all with dignity..." with dissolve
    show AkikoHypno sleep
    "She inhales deeply and closes her eyes, as if trying to calm herself down with a brief meditation." with dissolve
    a "Yeah. I always get back up..."
    "I guess, from how she puts it, she's used to handling this kind of shit on her own."
    "Doesn't mean it always has to be like that..."
    ks neutral "Yeah, I'm sure you will. But I think you're wrong about one thing."
    show AkikoHypno neutral
    a neutral "What's that?" with dissolve
    ks "There IS something I can do to help. At least a little."
    show AkikoHypno confused
    ks "If you're okay with it, that is." with dissolve
    show AkikoHypno happy
    "It gets a chuckle from her at least." with dissolve
    a "That's kind, but... I really don't see how you can help me at school, Kyou."
    show AkikoHypno smile
    ks smile "It might not be much, but..." with dissolve
    stop music fadeout 5.0
    ks "Well, what would you think about trying hypnosis again?"
    show AkikoHypno surprised
    a sad "Eh?" with dissolve
    "Akiko looks back at me, confused."
    play music Downtown
    "I guess that came a little out of left field, but I have an idea."
    show AkikoHypno confused
    a sad_side "Hypnosis? Risa told me you broke that light you had. The light that let you hypnotize people." with dissolve
    show AkikoHypno sad
    a sad "Was that wrong?" with dissolve
    "And I don't think she'd be against giving it another shot."
    ks neutral "No. I did break the penlight, and that's the reason my hypnosis was able to hurt Hiroko the way it did."
    ks "But I don't think I need to give up hypnosis because of that."
    show AkikoHypno neutral
    a sigh "Oh. I see." with dissolve
    "I just need to show confidence."
    ks smirk "Why so nervous? Worried I'll hypnotize you into being my girlfriend?"
    show AkikoHypno surprised blush
    a casual surprised blush "N-n-n-NO! I wasn't worried about..." with dissolve
    show AkikoHypno frown
    a frown "And you know you can't hypnotize me without that light anyway! S-so you'd be wasting your time, and..." with dissolve
    a "And... {w=1.0}{nw}"
    $ renpy.transition(dissolve, layer="master")
    show AkikoHypno annoyed
    extend sigh "urrgh, you're making fun of me, aren't you."
    show AkikoHypno irritated noblush
    "I let out a fond chuckle as she shakes her head." with dissolve
    ks smile "Seriously, though. I'm sure I'll do better than last time."
    show AkikoHypno neutral
    ks "And I promise it'll be a better experience for you, even if it doesn't work out." with dissolve
    show AkikoHypno confused
    a neutral "Yeah? Why would you think that?" with dissolve
    "And there it is. That little lean forward she does when she's interested."
    "I think I've assured her enough that her natural curiosity is starting to come through."
    ks "Because last time I was just doing what I thought I knew. I didn't consider that my methods might not work for everyone."
    ks "But I think I know you better now and if you'll let me, I'll prove it to you."
    ks "I'll prove you can be hypnotized, Akiko. And I'll prove it'll help your situation."
    "I notice her leaning in just a little bit more."
    ks "So what do you say?"
    show AkikoHypno smile
    "She replies with a quiet smile as she comes to her decision." with dissolve
    a "Okay, Kyou. I'm happy for you to try."
    show AkikoHypno happy
    a smirk "Just don't be too down if it doesn't work again, okay?" with dissolve
    "I smile back. It's not good for my chances if she thinks she can't be hypnotized, but I won't let that get to me."
    "After all, she's done so much to lift my mood today. Not to mention..."
    stop music fadeout 10.0
    ks smirk "Same to you. I mean, it'd be way more interesting if I succeeded, wouldn't it?"
    show AkikoHypno neutral
    "I've already thought about what to do this second time. And how she might react." with dissolve
    show AkikoHypno smile
    a smile_side "Y-yeah. It would be." with dissolve
    ks smile "Alright, so first I'd like you to lay down on the couch. And then I'm planning to touch the top of your head a few times for this."
    ks "Is that okay?"
    play sound sitting
    scene Redemption_Ending_1-1:
        zoom 1.0
        linear 8.0 zoom 0.5
    with blink
    "She perks a curious eyebrow before hesitantly raising her feet up onto the couch and laying her head down against the pillow."
    a "Um... sure."
    play music Night_Road
    ks casual smile "That's great. So how are we feeling right now? Comfy?"
    show Redemption_Ending_1-1 embarrassed blush
    a neutral_side blush "Now I feel like the one getting therapy..." with dissolve
    "I grin as I pick up my phone and start browsing through the list of hypnosis scripts I have stored in there."
    ks smirk "You can feel like my patient, or a friend chilling on my couch. Whatever feels right to you."
    ks "The important thing is that you relax."
    show Redemption_Ending_1-1 neutral noblush
    "I can hear Akiko take a breath through her nose as she settles into the couch." with dissolve
    ks smile "That's right. Allow your arms to relax at your sides. Let the couch support you and feel the tension in your body start to seep out into the cushions."
    "Once again, I try to bring my voice down to a calm, even register as I bring up the hypnosis script I had in mind on my phone screen."
    "Yeah. I think she'll take to this one a lot better."
    show Redemption_Ending_1-1:
        zoom 0.5
    ks "And while you're allowing that to happen, I'd like you to take a nice, deep, slow breath."
    show Redemption_Ending_1-1:
        linear 5.0 zoom 1.0
    ks "Feel the comforting coolness of the air as you breathe it into your lungs, as you hold your breath now, Akiko. Hold it..."
    show Redemption_Ending_1-1 kyou
    "I then place my hand gently over the top of her head as I speak my next words." with dissolve
    ks "And now slowly exhale. As you do so, you can feel a warm wave of relaxation wash over you."
    "Falling silent for a moment, I listen as Akiko dutifully exhales; seemingly content to follow along for now."
    ks "Feeling that wave travel through your head, weighing down your eyelids with a comfortable sensation of tiredness as it moves down your neck..."
    show Redemption_Ending_1-1:
        linear 10.0 xpos -1.0 ypos -0.8
    ks "Going down your shoulders and chest. Your arms. Your legs... All the way down to your feet and the tips of your toes."
    show Redemption_Ending_1-1 nokyou
    "I then pull my hand away and look her over, noting how she seems to be keeping still."
    show Redemption_Ending_1-1:
        linear 10.0 xpos 0.0 ypos 0.0
    "Let's see if I can get her to close her eyes this time."
    ks "Very good, Akiko. Allowing yourself to enjoy this feeling of calm. And now, take another breath. Nice and long and deep..."
    "Her chest rises as she inhales through her nose, and I wait for her to finish before calmly talking again."
    ks "Hold it... That's right. Enjoying that comforting feeling of fullness in your lungs for a moment."
    show Redemption_Ending_1-1 kyou:
        zoom 1.0
    $ renpy.transition(dissolve, layer="master")
    "Then, placing my hand gently on the top of her head again, I continue."
    ks "And breathe out. Feeling another calming, relaxing wave wash over you. All through your head, that wave of comfortable tiredness that invites you to close your eyes..."
    show Redemption_Ending_1-1 sleep
    $ renpy.transition(longdissolve, layer="master")
    "I pause a moment for effect, and Akiko lets her eyes close this time."
    "Not sure if she feels any more hypnotized, but at least she's comfortable with what we're doing."
    show Redemption_Ending_1-1:
        linear 10.0 xpos -1.0 ypos -0.8
    ks "Washing over the rest of your body. Easing all the muscles in your neck and shoulders. Releasing the tension in your spine. Soothing your calves..."
    ks "Leaving your feet feeling light and tingly as that deep wave of relaxation travels through your entire body."
    show Redemption_Ending_1-1 nokyou:
        xpos 0.0 ypos 0.0
    $ renpy.transition(longdissolve, layer="master")
    "Once again, I take my hand off of her and fall silent for a few moments. Just letting her internalize that feeling of calm that I'm impressing on her."
    "But now comes the moment of truth. The part of my script where she's supposed to feel hypnotized."
    ks "Now Akiko, soon you may start to find your conscious mind beginning to wander on its own. And I just want to tell you that's okay. You can let that happen."
    ks "Your subconscious mind will still be here, listening and responding, no matter how much your conscious mind wanders. No matter how deeply relaxed you become."
    ks "There's no need to worry about it. Now, let's take another deep, long, comforting breath. In..."
    show Redemption_Ending_1-1 kyou
    $ renpy.transition(dissolve, layer="master")
    "I then place my hand upon her for a third time."
    ks "And slowly out. More relaxation. Feeling your eyelids so comfortably heavy that they won't want to open. Feeling your neck so limp. Shoulders so loose..."
    ks "Every muscle in your arms, your fingers, every joint in your body, so completely free of tension now, Akiko..."
    "As the breath leaves her body, I raise my hand to leave it hovering just above her head."
    "I was right about having Akiko concentrate on what she feels instead of what she sees. She's responding way better to this kind of induction."
    "But is she hypnotized?"
    ks "And now I want you to take another deep, comfortable breath into your lungs, and..."
    "Now's the time to find out, as I place my hand back on her head and apply just a little pressure on her scalp with my fingertips."
    stop music fadeout 30.0
    ks "Breathe out. Feeling that deep, powerful wave of relaxation once more. Allowing your conscious mind to drift peacefully away."
    ks "Allowing me to speak just with your subconscious now. Do you understand, Akiko?"
    "My question lingers as I wonder how she'll react to something that suddenly requires her to respond."
    show Redemption_Ending_1-1 sleeptalk
    $ renpy.transition(longdissolve, layer="master")
    "And after a few moments I can see her lips twitch uncertainly. Like she's trying to remember how to speak."
    a "{size=12}Y... esss...{/size}"
    show Redemption_Ending_1-1 sleep
    $ renpy.transition(longdissolve, layer="master")
    "Man, I can barely make out a noise at all. But it seemed to be in the affirmative."
    "And the feeling of her own voice, quiet and weak as it was, may have been enough to convince her that things really are different this time."
    ks "Very good, Akiko. Going deeper into relaxation. Deeper into hypnosis."
    show Redemption_Ending_1-1 nokyou
    $ renpy.transition(dissolve, layer="master")
    "So... I think I've proven to her that she can be hypnotized."
    ks "And now that you're here, in this deeply hypnotized state of being, there are a few things that I need to say to your subconscious."
    "Now to prove I can use it to help her."
    ks "Things that your subconscious may consider to be true."
    play music Luminous_Rain
    ks "Because Akiko, no matter how bad things get, you will always remember that you are a strong and confident woman."
    ks "No matter what anyone says to hurt you, you know that you are a kind, generous soul and nothing they say can bring you down."
    a "{size=16}M-mm...{/size}"
    ks "You deserve to find happiness too."
    "She murmurs, and I can see her lips quiver as I talk."
    ks "Anyway, that's all I wanted to say. So in a few moments I'm going to count up slowly, from one to five."
    ks "With each number you'll be able to feel yourself becoming more awake and aware, feeling your conscious mind return."
    ks "And on five, you will be wide awake and refreshed. Remembering everything, feeling so good about yourself as I count now..."
    ks "One, just starting to rouse yourself..."
    ks "Two, feeling your arms and legs and feet beginning to stir..."
    ks "Three, becoming aware of your breathing now. Feeling more awake, more alert."
    ks "Four, taking a nice deep breath now. Feeling your eyelids loosen, and..."
    ks "Five. Wide awake and feeling great, Akiko."
    show Redemption_Ending_1-1 waking
    $ renpy.transition(longdissolve, layer="master")
    "I watch as her eyes flicker gently back into life."
    "As she starts to regain her focus, our gazes meet for a moment before..."
    show Redemption_Ending_1-1 smile
    a cry "*sniffle*" with dissolve
    ks surprised "H-hey, 'Kiko, what's wrong? Are you okay?"
    "Shit. The LAST thing I want to do is make her cry!"
    $persistent.redemption_ending_1_1_unlock = True
    scene bg blackscreen with dissolve
    "Akiko slides off the couch as she gives me a hasty nod, choking down a sob..."
    show Redemption_Ending_1-2 with dissolve
    "... before weakly leaning in to hug me."
    ks casual surprised "'Kiko?"
    show Redemption_Ending_1-2 laugh
    a casual "I-I'm okay! *sniff* I just... w-wow, ahaha!" with dissolve
    show Redemption_Ending_1-2 talk
    a cry_smile "I had no idea how much I needed to hear that just now..." with dissolve
    show Redemption_Ending_1-2 arms_up smile
    "Tentatively, I put my arms around her, and she tightens her arms around me as we share a quiet embrace." with dissolve
    "Seems things have been rough for both of us. And we've sure made some mistakes, big and small."
    "But right now, in this moment, it doesn't seem so bad."
    "I've come a long way, and it feels like Akiko's had a journey of her own."
    "We have friends like Sayori and Risa, who know who we really are even if the rest of the world seems set against us."
    "And, at least for the time being, we have each other."
    show Redemption_Ending_1-2 talk
    a "It's going to be alright, Kyou." with dissolve
    show Redemption_Ending_1-2 smile
    a happy "You'll see..." with dissolve
    $persistent.redemption_ending_1_2_unlock = True
    jump Credits

label Epilogue_Redemption_Spiral:
    scene bg corridor eve with longdissolve
    "I step out of the classroom with a weary gait."
    "My day was spent poring over test papers meant to resemble the ones we'll be taking for our college entrance exams next year."
    "It... could've gone better, to say the least."
    scene bg school ext eve with blink
    play music Eons
    "But I can hardly blame myself. What with being suspended and my busy evening I think I can be forgiven for having been a little distracted."
    "I'm supposed to head straight home, but as I reach the gates I... I stop and take a moment to look back and take it all in."
    "This'll surely be the last day I set foot in this place. It's an odd feeling."
    "But... no, this is no time to get all nostalgic. What has this school ever done for me anyway?"
    "I can move on. I AM moving on..."
    show phone at right with moveinright:
        ypos 0.346
    if hypno1 == "devoted hiroko":
        "{color=#4B9374}\"Where are you?\"{/color}"
    elif hypno1 == "robot hiroko":
        "{color=#4B9374}\"Where are you, BSB-3C?\"{/color}"
    "I'm going to make a future for myself, whether these people like it or not."
    scene bg shopping2 eve with blink
    "I don't need any of them in my life anymore. I won't change how they think of me."
    "... with one little exception."
    play sound cellvibrate
    show phone at right with moveinright:
        ypos 0.346
    if hypno1 == "devoted hiroko":
        "{color=#8C8888}\"OMG KYOU ILYSM\"{/color}" #Originally the color code was #5F5C5C, matching her hair, but dark grey on black is too difficult to read so I made it lighter
        play sound cellvibrate
        "{color=#8C8888}\"I just got out of my mocks what about you???\"{/color}"
        "Our future is only just beginning, Akiko."
        "{color=#4B9374}\"I'm headed home. Come on over and don't delay\"{/color}"
        play sound cellvibrate
        "{color=#8C8888}\"OMW <3<3<3\"{/color}"
    elif hypno1 == "robot hiroko":
        "{color=#8C8888}\"BSB-3C has just completed [p_their] mock exams\"{/color}"
        "Our future is only just beginning, Akiko."
        "{color=#4B9374}\"I'm headed home. Come on over and don't delay\"{/color}"
        play sound cellvibrate
        "{color=#8C8888}\"Yes administrator\"{/color}"
    "I'll take care of it for both of us..."
    scene bg street1 eve with blink
    "As I slowly make my way home I'm suddenly aware of a rapid slapping noise disturbing the otherwise quiet street."
    play sound runningshoes
    "A noise that quickly grows in volume as I start to recognise the sound of cheap shoes pounding against pavement."
    if hypno1 == "devoted hiroko":
        a "{size=16}Kyouuuuuu!{/size}"
    queue sound runningshoes
    "... She's a lot quicker than I thought."
    if hypno1 == "devoted hiroko":
        show Akiko side uniform_down armband_down laugh blush zorder 5 at center with dissolve
        stop sound
        a "Aaaaahh~ {font=DejaVuSans.ttf}♥{/font}"
        "I turn around just in time to find my now former school's student council president standing before me."
        "She's beaming, and positively dishevelled from all the running she's just been doing."
        ks sigh "Man, look at you. Aren't you supposed to be setting an example to the other students?"
        a uniform armband "Ahahaha... haaah... y-yes, hahaha~" with dissolve
        show Akiko laugh_wink
        a "But... haaah, m-my duty to my boyfriend comes first~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        show Akiko happy
        "Smiling, I open an arm for her and she happily nestles at my side before we share an affectionate kiss." with dissolve
        "I can feel the heat radiating from her. The heat of her absolute devotion to me."
        "Much as I liked her a week ago, I'm very much enjoying our new arrangement almost as much as she seems to be."
        show Akiko laugh
        "She soon breaks from kissing me to catch her breath, and I gently stroke the back of her head while we talk." with dissolve
        ks smile blush "Hey, I told you not to delay, but next time don't draw so much attention to yourself, alright? I don't want you getting into any more trouble on my account."
        a smile "Y-yeah, I got a few looks when I took off now that I think about it." with dissolve
        ks smirk "You were just that happy to be done with your mocks you couldn't wait to get out and celebrate, right?"
        a smirk "Ehehe... Th-that's exactly it~" with dissolve
        stop music fadeout 5.0
        show Akiko smile
        "She giggles and pecks my lips. Although as I look over her shoulder I realise I won't be able to enjoy her affections for the time being..." with dissolve
    elif hypno1 == "robot hiroko":
        show Akiko side uniform_down armband_down sigh blush zorder 5 at center with dissolve
        stop sound
        a "Haaah... h-haaah..."
        "I turn around just in time to find my now former school's student council president standing before me."
        "She's panting heavily, and I realize that I may have been a little careless with my instructions just now."
        ks sigh "Hey, be careful. You may be a... you know, but you're still designed to have the limitations of a regular girl."
        ks "So don't overdo it, okay?"
        a drowsy noblush "Y-yes... haaah... yes, administrator." with dissolve
        show Akiko happy
        "I smile at her fondly as I reach over to pet her head while she catches her breath." with dissolve
        ks smile "You should also be careful you don't draw too much attention to yourself. Try to keep a low profile, alright?"
        a smile "Yes, administrator. BSB-3C will be more careful." with dissolve
        ks "Good. Now, were you followed?"
        a neutral_side "Hmm..." with dissolve
        a neutral "Yes, administrator. BSB-3C has detected four female students on a likely intercept course." with dissolve
        ks confused "Oh? Is that right?"
    show Hiroko uniform_headhold nervous_side at center:
        xpos 0.95
    show Nozomi side sad_side at center:
        xpos 0.87
    show Sayori uniform_handup concerned at center:
        xpos 0.75
    show Risa frown_side at center:
        xpos 0.65
    if hypno1 == "devoted hiroko":
        "... because it seems she was followed." with dissolve
    elif hypno1 == "robot hiroko":
        a "Yes, administrator." with dissolve
        "Oh. Oh, shit."
    show Akiko surprised
    queue music Measured
    r angry_side "Akiko! What are you DOING?!" with dissolve
    "So much for my last day at school being a peaceful one."
    show Akiko uniform noarmband sad_side noblush at flip:
        xpos 0.45
    a "Ah, R- Risa! It's good to see you again. Is your suspension over already?" with dissolve
    r uniform_armup frown_side "I'm out until next week. They just let me back today so I could do my mocks." with dissolve
    show Risa frown
    "She then glares in my direction." with dissolve
    r "Guess I wasn't the only one, huh?"
    show Akiko smile_side
    "I notice Akiko put on a smile as she deftly stands between me and the girls who have assembled to... do what exactly? Stop me?" with dissolve
    a "Ah... s-so is there something you all wanted with us? We were just headed home."
    "Akiko's mine now and there's nothing anyone can say or do to take her from me."
    show Risa frown_side
    n neutral_side "Akiko, we... w-we..." with dissolve
    r uniform angry_side "We want to know why you're running off with this sleezebag!" with dissolve
    a neutral_side "... \"Sleezebag\"?" with dissolve
    "I made sure of that."
    s sleeptalk "Risa, if I may?" with dissolve
    show Risa:
        linear 1.0 xpos 0.75
    show Sayori:
        linear 1.0 xpos 0.65
    pause 1.0
    show Hiroko nervous
    show Nozomi sad_side
    show Sayori concerned zorder 4
    show Risa frown_side zorder 3
    s uniform_folded "Akiko. We all appreciate that you are going through a hard time presently, but I can assure you doubling down on Kyou is not the answer." with dissolve
    s frown "It is as I told you yesterday: You are not alone. Do not allow this man to manipulate you as he has done others." with dissolve
    s uniform concerned "Please, just... come with us! We just want to talk to you." with dissolve
    a frown_side "Sayori. Everyone. I am trying to be polite, but you really have no business butting into our personal lives like this." with dissolve
    a uniform_down "Since when have you ever cared about me? Any of you? But the moment I get involved with this boy you hate you're all suddenly \"worried\" about me?" with dissolve
    s angry "Akiko, just LISTEN to us!" with dissolve
    show Hiroko nervous_side
    show Sayori concerned
    show Risa neutral_side
    a angry_side "NO! How DARE you infantilize me like this!" with dissolve
    a frown_side "You think I can't make my own decisions? You're going to tell me Kyou hypnotized me into being his girlfriend now? Don't be stupid." with dissolve
    a uniform angry_side "I KNOW what I'm doing with my life and you can all leave us ALONE!" with dissolve
    "The conviction in her voice. I can truly believe she holds our new relationship above anything else in her entire world."
    show Akiko frown_side
    r uniform_armup "So you know you're flushing your reputation down the toilet, right? Chasing after this guy like a puppy?" with dissolve
    r concerned_side "Come on, 'Kiko, I KNOW you! Student council means too much for you to throw it all away on some bad boy you only just met. What's really going on?" with dissolve
    n "We're just worried about you, Akiko! Please come and talk to us!"
    "The strength of Akiko's devotion to me is absolute, and from the look one of our would-be heroines is giving her I don't think I'm the only one who understands that."
    show Hiroko scared_side
    a uniform_down frown_side "I'm fine. You should be more worried about your friend over there; it looks like she's triggered again." with dissolve
    h uniform "S-she's fuckin' brainwashed! He BRAINWASHED her, I TOLD you guys he was gonna do it!" with dissolve
    a uniform "Imagine bringing her along knowing what she's like around Kyou. Some friends you are." with dissolve
    h cry "Ain't nothing we can do it's too late, we gotta run. S-s-save ourselves we gotta RUN!" with dissolve
    show Nozomi sad_closed at flip
    show Akiko frown_side
    n "Hiroko, shhh, it's okay. We're not going to let anything happen to you. Don't worry!" with dissolve
    h scared "I don't wanna look at the light. Not again. N-not again!" with dissolve
    "Nozomi turns to me, while holding Hiroko in a smothering embrace."
    show Hiroko cry
    n sad "Kyou! Please! I know you're better than this!" with dissolve
    n "You may have had some setbacks. Some big ones even, but you mustn't ever stop trying to do the right thing!"
    ks frown noblush "I-I AM doing the right thing! I'm moving on, I'm moving on from all of you!"
    show Risa frown
    show Sayori frown_right
    a uniform_down "That's right! He's not coming back to school ever again, okay? You jerks all got what you wanted, so just go away!" with dissolve
    hide Nozomi
    show Nozomi front2 concerned at center:
        xpos 0.85
    n "Kyou, I am begging you! You let Hiroko go, didn't you? You can do the same for Akiko, please!" with dissolve
    "Do the same for Akiko? So she'll end up like that girl whimpering on your shoulder? So I'll have ruined my life for nothing?"
    n cry "If you don't... you'll be making a terrible mistake that you'll regret for the rest of your life, so please!" with dissolve
    "Like I'll ever let that play out again."
    n frightened "Please, just stop this madness!" with dissolve
    "But damn, this is no good. These girls are involving me in this scene and this street suddenly isn't so quiet any more."
    "People are coming out of their houses, stopping their journeys home, all to look at us."
    "Me and Akiko... we need to get out of here before they make things worse."
    show Sayori:
        linear 1.0 xpos 0.75
    show Risa:
        linear 1.0 xpos 0.65
    pause 1.0
    show Hiroko scared
    show Nozomi concerned
    show Sayori zorder 3
    show Risa uniform frown zorder 4
    r "How about it, Kyou? You think you can live with yourself after everything you've done?" with dissolve
    show Risa:
        xpos 0.65
    show Sayori:
        xpos 0.75
    "She thrusts her arm in the direction of Hiroko and Nozomi huddled together."
    r uniform_armup angry "All this devastation over your creepy hypno bullshit and for what? Do you really think there's a happy ending for you?" with dissolve
    r "How many more have to suffer until you're satisfied, huh?"
    "I'm about to defend myself, only as I open my mouth to speak it's Akiko who gets the next word."
    show Sayori concerned
    show Akiko uniform
    show Risa angry_side
    a "I think I've had just about enough of you disparaging my Kyou like that." with dissolve
    r uniform "YOUR Kyou? Jesus Christ, 'Kiko, do you even hear yourself?" with dissolve
    a "Apologize."
    s sleeptalk "Risa, please, a little caution." with dissolve
    show Sayori concerned
    r uniform_armup "{cps=15}How about you {/cps}{nw}" with dissolve
    show Akiko surprised_side
    show Nozomi side surprised_side
    show Hiroko shocked_side
    extend "WAKE UP, Akiko?"
    show Akiko uniform_down neutral_side
    show Hiroko nervous_side
    show Nozomi sad_side
    r concerned_side "... Like, come on. I don't know what he's got on you but we can work it out." with dissolve
    r uniform neutral_side "I'll help you smooth things over with the student council. Whatever he's told you, we'll deal with it." with dissolve
    a frown_side "You'll \"Deal with it\"?" with dissolve
    r angry_side "Just ditch the evil son of a bitch! It's not too late!" with dissolve
    play music Rain
    if hypno1 == "devoted hiroko":
        scene SpiralEnding furious scared with blink
        a "I'll deal with YOU!"
    elif hypno1 == "robot hiroko":
        scene SpiralEnding calm scared with blink
        a "It's you who needs to be dealt with."
    "A chorus of panicked screams breaks me out of my thoughts."
    "Within the blink of an eye Akiko lunged forward and grabbed Risa around the throat while the rest of us look on in horror."
    r "K-kiko what are you... gccck!"
    "Akiko? She did that?"
    if hypno1 == "devoted hiroko":
        a "Hrrrr... w-what's the matter, Ris'? Did you think I wouldn't stand up to you?"
    elif hypno1 == "robot hiroko":
        a "What's wrong, Risa? Did you suppose you could threaten my Kyou without consequence?"
    s "AKIKO! Get a hold of yourself!"
    "My Akiko? She..."
    if hypno1 == "devoted hiroko":
        a "You thought... h-haaah, you could just mouth off like that? Mouth off about my BOYFRIEND?!"
        a "{cps=20}You'll listen to me now, won't you? {/cps}{w=1.0}{nw}"
        extend "WON'T YOU!!!" with vpunch
        "... She told me she'd be one-hundred percent committed to me..."
        scene VoodooPhone akiko2_underwear uncomfortable_left blush2:
            matrixcolor SaturationMatrix(0)
        with flash
        a "... I know I was weak when you needed me to be strong."
        show VoodooPhone akiko1_underwear shy_closed2 blush1
        a "So I promise, I'll never doubt you ever again. I'll always take your side, no matter what." with dissolve
        show VoodooPhone akiko2_underwear uncomfortable blush2
        a "I'll always protect you from now on!" with dissolve
    elif hypno1 == "robot hiroko":
        a "I know my purpose now. I will protect Kyou from any and all threats."
        a "And you will threaten him no longer, Risa Tachibana."
        "That's right. She's... she's only obeying her programming."
        scene VoodooPhone akiko1_underwear talking:
            matrixcolor SaturationMatrix(0)
        with flash
        $ks = DynamicCharacter("kyou_name", image = "KyouSideFlashback", who_color = "#4B9374")
        a "A [hypno6] always protects [p_their] system administrator from all threats."
        show VoodooPhone akiko1_underwear neutral
        ks "Accept those rules. Keep them deep in your memory core because they're fundamental to your very existence." with dissolve
        ks "They will define every action you take from now on. Understand, [hypno6]?"
        show VoodooPhone akiko1_underwear talking
        a "Yes, administrator." with dissolve
        $ks = DynamicCharacter("kyou_name", image = "KyouSide", who_color = "#4B9374")
    scene bg blackscreen with dissolve
    "Because that's what I told her to be."
    "I made her like this..."
    if hypno1 == "devoted hiroko":
        scene SpiralEnding furious choking
    elif hypno1 == "robot hiroko":
        scene SpiralEnding calm choking
    n "KYOU! DO SOMETHING!" with shake
    $ persistent.spiral_ending_unlock = True
    scene bg blackscreen with longdissolve
    stop music fadeout 10.0
    "Everything becomes a stressed-out blur after that."
    "I remember shouting at Akiko to stop. I remember some of those onlookers running to break up the fighting."
    "I remember the cops coming and taking us off the street."
    "And throughout it all the screaming. So much screaming..."
    scene bg k bedroom night with longdissolve
    "After the police questioned us, they let us go home. Except for Akiko."
    queue music Sorrow
    "Home. Where all I can do is helplessly relive the last few hours in my head over and over."
    if hypno1 == "devoted hiroko":
        scene SpiralEnding furious choking:
            matrixcolor SaturationMatrix(0)
    elif hypno1 == "robot hiroko":
        scene SpiralEnding calm choking:
            matrixcolor SaturationMatrix(0)
    with flash
    "Witnessing Akiko trying to kill her classmate every time I close my eyes..."
    "What have I done?"
    scene bg k bedroom night with blink
    "I thought I was ready to be selfish. I thought I was ready to build a future of my own making, but... what future is there now?"
    "I... I never imagined it would turn out like this. It wasn't supposed to end like this."
    "I wasn't supposed to still be alone... fuck, I can't..."
    "I can't face the world anymore..."
    jump Credits
label TennisBot_Epilogue1:
    pause 2.0
    scene bg classroom eve with longdissolve
    "As another school day draws to a close, I gather my things and ponder."
    play music Eons
    play sound schoolbell
    show Hiroko uniform neutral_side at center, flip
    show Sayori uniform_folded neutral at center, flip:
        xpos 0.25
    show Nozomi side neutral_side at center:
        xpos 0.75
    n "Well, shall we get going?" with dissolve
    "It's been a couple months since that day."
    s sleep "Yes. Let's." with dissolve
    "A couple months since I made Hiroko think she was my [hypno6]."
    h uniform_headhold2 sleeptalk "Guys, it's okay. You don't gotta do this anymore, I'm fine." with dissolve
    "My mock exams went okay, considering the pain I was in."
    s uniform_handup concerned "It really is no bother for us, Hiroko." with dissolve
    "Since then... I guess it's gotten a little easier. Just keeping my head down, like I've always done."
    show Hiroko neutral_side
    n smile_side "That's right. Oh, but how about we stop by the mall before heading home? Have a little fun first?" with dissolve
    "And as for Hiroko and her friends, well..."
    h nervous_side "Nah for real tho', I don't wanna be like this forever. I'll be okay on my own." with dissolve
    "We're all just trying to move on with our lives, as best as we can."
    scene bg ext school eve with blink
    stop music fadeout 5.0
    "Anyway, with another day done I make my solitary journey home."
    "I'll do a little videogaming, have a quick dinner then it'll be back to studying for the real college entrance exams that are coming up."
    scene bg shopping2 eve with blink
    "The college I'm shooting for has one of the better engineering programs in the country."
    "{cps=20}I'm sure I can do enough to get in. I just need to-{/cps}{w=1.0}{nw}"
    h "H-hey, asshole!"
    "... That voice. It makes my hair stand on end hearing it here."
    show Hiroko frown at center
    "But as I turn around, I'm surprised to find it wasn't in my imagination." with dissolve
    play music Luminous_Rain
    h uniform_headhold2 confused "Man, what's with that face? Don't act like you don't deserve that." with dissolve
    ks surprised "Y-yeah, I just... Hiroko?"
    h frown "H'yeah, it's me." with dissolve
    "What a time to be feeling déjà vu."
    h sleeptalk "Listen, I... I wanna talk to you..." with dissolve
    scene bg cafe eve
    with blink
    "My stomach's in knots as I quietly follow her, while she leads me to a nearby café."
    scene bg blackscreen with dissolve
    h "We'll talk here. You're buying."
    "I don't argue and just buy her what she wants."
    scene HirokoCafe worried with dissolve
    "After all the things I had her do, it seems more than fair to let her boss me a little bit."
    "But as we sit outside the café with our drinks, I look at her and I don't see a lot of confidence in that face."
    "It's unsettling. So unlike the feisty girl who used to scream at me all those times."
    ks neutral "Are... are you okay?"
    #Hiroko could mention that she visits this place with Nozomi sometimes
    show HirokoCafe sigh
    h "Yeah... y-yeah, don't you start too." with dissolve
    show HirokoCafe frown
    h "I s-said I wanna talk to you, so that's what I'm gonna do." with dissolve
    h "..."
    show HirokoCafe scared_closed
    h "F-fuck..." with dissolve
    "Much as I hate to admit, it's obvious she's still afraid of me."
    ks sigh "H-hey, you don't have to do anything you don't want to, alright?"
    ks "I can go if you want. It's okay."
    show HirokoCafe scared
    h "No! I gotta do this." with dissolve
    h "You ain't controlling me anymore. Y-you're not..."
    show HirokoCafe scared_closed
    h "I gotta do this... f-for myself." with dissolve
    "I'm not sure I understand her, but the last thing I want to do is hurt this girl again."
    "So I'll just sit back, take a sip from my cup and wait until she's ready to talk."
    show HirokoCafe worried_left
    h "... H-h'yeah, so I got a letter about my scholarship today." with dissolve
    h "The college I want said they're super interested in me, so they're gonna pay for pretty much everything."
    ks smile "Th-that's great, Hiroko!"
    "I'd stayed silent to let her speak, but the moment she said that I couldn't help myself. I'm relieved to hear it."
    show HirokoCafe worried
    h "An' you know the first thing I thought when I read it?" with dissolve
    show HirokoCafe sigh
    h "..." with dissolve
    show HirokoCafe worried
    h "I thought... \"I got Kyou to thank for this, don't I?\"" with dissolve
    ks sigh "Ah... w-well..."
    show HirokoCafe frown
    h "Like, don't get me wrong. You fucked me up big time, but you never had to help me at all." with dissolve
    show HirokoCafe neutral_left
    show HirokoCafe neutral_left
    h "You made me think there wasn't a single thing I couldn't do, or anybody I couldn't beat." with dissolve
    show HirokoCafe worried
    h "An' that's exactly what you gotta be when you're out there on the court. You can't let shit get to you and you gotta believe in your game one-hundred percent." with dissolve
    show HirokoCafe sigh
    h "{size=16}... Kinda like a robot.{/size}" with dissolve
    ks neutral "Hiroko..."
    show HirokoCafe scared_closed
    h "H'yeah..." with dissolve
    show HirokoCafe scared
    h "My brain's been doing all kinds of crazy shit since you got in my head. S'like I'm losing my mind sometimes." with dissolve
    show HirokoCafe scared_closed
    h "Feels like I ain't ever gonna get you outta there, b-but... But I gotta keep going." with dissolve
    ks sigh "{cps=20}I'm really sorry, Hiroko. If there's anything I can do-{/cps}{w=1.0}{nw}"
    show HirokoCafe worried
    h "Yeah, dude, I heard ya the first time." with dissolve
    show HirokoCafe worried_left
    h "An' I know you mean it. You're trying to be better; I see that." with dissolve
    show HirokoCafe worried
    h "'Cuz you understand now, right? Why we're so scared of ya?" with dissolve
    "I nod slowly as I think back to that conversation I overheard on that rooftop all those weeks ago."
    show HirokoCafe neutral
    ks "Yeah... I really didn't mean to scare you guys, but it was selfish of me to keep pushing myself on you like that." with dissolve
    ks "I should've left you alone but instead I kept trying without a clue and I just... I just made it worse."
    ks "And that made me angry, so... well, you know what happened after that."
    show HirokoCafe sigh
    h "Yeah..." with dissolve
    "She lets out a pained sigh."
    show HirokoCafe neutral_left
    h "I dunno, man. Maybe if you made different choices back then we could've..." with dissolve
    show HirokoCafe sigh
    h "Ugh, forget I said anything." with dissolve
    show HirokoCafe frown
    h "But you stay on the path, you keep your nose clean and you'll meet some other girls." with dissolve
    h "And when you do you'll treat 'em right. You're gonna do better."
    show HirokoCafe neutral
    h "Maybe... if I know that... I can get better too." with dissolve
    h "So that's all I want outta you. Got it?"
    "Without hesitation, I nod my head and look her dead in the eye."
    ks frown "I WILL do better next time; I promise."
    ks "And for what it's worth coming from me, I really hope you can heal from this, Hiroko. I mean it."
    h "..."
    show HirokoCafe smile
    h "Y-yeah, I will. That's a promise." with dissolve
    show HirokoCafe smile_tears
    h "An' you will too... n-now you've found your heart." with dissolve
    $persistent.hiroko_cafe_unlock = True
    scene bg cafe eve with blink
    "Hiroko leaves me with that quiet smile on her face. She's looking a lot better than when she sat down, that's for sure."
    "We can't be friends, and in a few weeks I doubt we'll ever see each other again, but in spite of that I find myself smiling too."
    "It's going to be alright. We're going to be alright. And that's enough."
    scene bg blackscreen with dissolve
    "Thank you, Hiroko."
    jump Credits
label TennisBot_Epilogue2:
    pause 3.0
    scene bg apartment day with dissolve
    "It's been a long five months since that day."
    queue music Eons
    h "Hi, mom... Yeah, we made it here okay, just finished moving our stuff inside~"
    "I had to turn my whole life upside-down, but I saw Hiroko through graduation."
    h "... Haha yeah, there's boxes an' shiz everywhere."
    "She got her sports scholarship, just like she wanted. And I moved to a new city with her so she could start college life."
    show Hiroko dungaree2_headhold2 happy at center
    h "... Oh yeah, I'm totally pumped! Me an' Kyou are gonna have a blast up here~ {font=DejaVuSans.ttf}♫{/font}" with dissolve
    "We live together now. This little apartment is going to be our home for the time being."
    h confused_side "Whaddya mean \"What's Kyou gonna do\"? He's gonna find a job ain't he? I told ya." with dissolve
    "Yeah. A job. I had to tank any notion I had of going to college myself."
    "My dad was furious when he found out what I was doing. Said I was on my own."
    h smile_side "Well I think it's sweet. Dude's doing all of this to support me; he knows what's up." with dissolve
    "So now I'll have to knuckle down and find any work I can to maintain my \"[hypno6]\" and keep this roof over our heads, such as it is."
    h happy "That's why he's my boyfriend, mom~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    "Heh. \"Boyfriend\". Yeah, that's a cruel joke I'm having Hiroko tell the rest of the world. I'd hardly call us a romantic couple given our circumstances."
    "I enjoy a little intimacy with her sometimes, but I can't think of her like that. Not really, anyway."
    h happy_closed "An' soon as I turn pro he's gonna be my manager too, you'll see~" with dissolve
    "Now \"Manager\" is a more apt descriptor. There's no \"gonna be\" about it; I manage her now."
    ks casual "Tell her I said hi."
    h smile "He says hi, by the way... Uh-huh." with dissolve
    h neutral "... Uh-huh." with dissolve
    "Like how I'm managing her interactions with the humans still involved in her life."
    h smile "... Seriously mom, you're worrying too much. I know what I'm doing." with dissolve
    "Sounds to me like her mom's being difficult again. I don't need the complication right now, not on moving day. There's more important shit to do."
    h smirk "If you still think he's the one pulling the strings around here, think again~" with dissolve
    ks frown "{size=16}Psst. Finish the call now.{/size}"
    h laugh "... Kyahahaha, b-but listen, mom, I gotta help him unpack so we'll talk later, okay?" with dissolve
    h happy "Yeah, love you too, mom. Bye~" with dissolve
    show Hiroko dungaree2 smile
    "As she hangs up, Hiroko smiles quietly as she automatically hands her phone to me for safe keeping." with dissolve
    ks neutral "How is she? Anything I need to know?"
    h neutral "Mom's fine. She's still worried about me, 'cuz I wanted to live alone with my new high-school boyfriend instead of living in the college dorms like I was s'posed to." with dissolve
    h sleep "Would've been cheaper if I did, an' she knows my scholarship don't cover this apartment we're in." with dissolve
    h sleeptalk "She don't get why I'm makin' myself dependant on you when I totally didn't have to." with dissolve
    show Hiroko sleep
    ks sigh "Your parents still hate me, don't they." with dissolve
    h sad "Yessir. They really do." with dissolve
    "I sigh as I shake my head at her words. It hurts to hear them, but I know Hiroko can only be truthful with me; it's not her fault."
    ks frown "They seriously took it hard when you fell out with Nozomi. And that I was the one to blame for it."
    ks "One of these days they'll understand I'm doing my best for you. They'll have to come around eventually."
    h dungaree2_headhold nervous "Yeah for real, I dunno how I made it so far on my own before you reprogrammed me, but I need a sysadmin now." with dissolve
    h smile "I need my Kyou Koyama, an' mom and pops just gotta deal with it." with dissolve
    ks "That's absolutely right. I'm the one who prepared you for that tennis tournament. I'm the one who made sure you got that scholarship they keep bringing up."
    show Hiroko neutral
    ks "I made sure you didn't fuck up your college entrance exam, made sure you ditched that stupid pink dye job you had so people would take you seriously..." with dissolve
    ks "Ugh. They should be thanking me for looking after you like this."
    h dungaree2_headhold2 sad "I totally agree with you, Sir." with dissolve
    ks sigh "Yeah, you would. You're programmed to."
    "I shake my head, but at myself this time. Again, it's not her fault she's like this."
    ks neutral "Anyway, let's go over your schedule for the rest of the day."
    show Hiroko dungaree2 neutral
    ks "Next up, you're cooking us lunch. After that you need to finish unpacking and setting up the apartment, that'll probably keep you busy 'till evening." with dissolve
    ks "So you'll make us dinner and after you're done cleaning up you'll join me to play some videogames until it's time to put you into sleep mode."
    ks "It's your first day of class tomorrow and you've been working hard all weekend, so it'll be another early night for you. Understand?"
    h dungaree2_armup happy_closed "Yessir~ {font=DejaVuSans.ttf}♫{/font}" with dissolve
    ks "Good, now hop to it. Your sysadmin needs to find himself some work."
    hide Hiroko
    "As I dismiss her, Hiroko skips happily over to the kitchen counter to prepare the food I bought." with dissolve
    "Following my orders seems to be completely hardcoded into her very being now. It pleases her."
    "In fact, over the months she's been living as my [hypno6] I've noticed she's becoming less and less capable of acting without my input."
    "Since she graduated I've even had to pick her clothes in the morning."
    "Makes me worry about how she'll handle herself in her classes tomorrow. I'll have to be sure to check in with her regularly so she doesn't get overwhelmed."
    "Anyway, while she's occupied I open the packing box I kept by the dining table and pull out my laptop."
    "There's gotta be some decent work I can get around here, surely..."
    stop music fadeout 15.0
    with blink
    ks frown "Fuck."
    "Is that really all there is? I wasn't expecting much, but even so..."
    "All the entry-level stuff for progamming or engineering work are for people with college degrees. They'll never even consider someone like me."
    "The kind of stuff I thought I'd be doing as an adult is just completely off limits unless I get myself a better education."
    "So... shit, am I seriously considering going for this job as a garbage man? That's so demeaning..."
    "... Overnight shelf-stacker at a supermarket? Such menial work, but we need the fucking money. Shit."
    show Hiroko dungaree2_armup happy_closed at center
    h "Lunch is ready! Eat up~" with dissolve
    "But damn, if I get a job like that, will Hiroko be okay in the apartment by herself?"
    h smile "Did you find anything good?" with dissolve
    play music Monologue
    "Fuck, it's really sinking in now. I've thought about this stuff for so long, but it's real now. This is my life."
    h dungaree2 neutral "Everything okay?" with dissolve
    "I'm gonna have to scrap for these dead-end jobs and I just have to hope Hiroko's pro career takes off?"
    h nervous "Did I make your food wrong? What should I do?" with dissolve
    "Have I really tied my future to this girl I brainwashed? I look at her now and she... she's barely functional."
    "Rising from the dining table, I can't help but fix her with a glare."
    h surprised "S-sir?" with dissolve
    ks frown "\"What should I do?\" \"What should I do?\""
    show Hiroko shocked
    play sound bodyimpact
    "I firmly grip my brainless [hypno6] by her shoulders as my body shakes." with vpunch
    ks angry "You listen to me. You have NO idea in that CPU of yours how much I've given up for you to have a shot at the big time."
    show Hiroko surprised
    ks "So come tomorrow you better do everything it takes to get on the pro tennis circuit, you hear me? I want to see results." with dissolve
    ks "I'm talking big tournaments. I'm talking prize money. Because if you don't start raking it in, we're gonna be living in filth until we're dead!"
    ks "And I need you to understand that, [hypno6]. Do you?"
    show Hiroko neutral
    "Hiroko's surprised with me, but I feel no fear in her. She barely even flinches at my hold on her as she takes in my every word." with dissolve
    "And to my challenge, she simply answers with the cool detachment of an automaton."
    h "Yeah... I totally get it, Sir."
    h sleeptalk "I ain't gonna be distracted by all those humans. I only wanna play tennis, 'cuz that's what I do. It's my primary function." with dissolve
    h neutral "That's all I'm programmed for. And I'mma good [hypno6] who always obeys [p_their] programming." with dissolve
    h frown "Nobody's gonna get in my way, I'm gonna prove myself and I'm gonna win. For you." with dissolve
    "I let out a shuddered sigh. This is really getting to me, I've bet everything on her and I... I know Hiroko won't let me down. She can't."
    "There's no fixing this situation with the penlight that I so rashly destroyed, but it's okay. I still have her."
    ks sigh "You will... O-of course you will. Come here."
    scene bg blackscreen with dissolve
    "Hiroko unhesitantly takes a step towards me and I hug her tightly. Possessively."
    scene cg tennis bot end 3 with longdissolve
    k "I know better than to doubt you, [hypno6]. I've seen what you can do on the tennis court."
    k "We're poor now, but you'll set things right. And I'll support you every step of the way."
    k "We're in this crummy place now but s-soon, we'll be jet-setting all over the world. And you'll be playing in all the tournaments I sign you up for."
    k "I'll manage your finances, your public appearances, and all you need to do is play, just like you've always wanted. You won't have to worry about a thing."
    $persistent.tennis_bot_end_1_unlock = True
    scene bg blackscreen with longdissolve
    k "I'll make you a star, Hiroko..."
    jump Credits

label Copycat_Ending1:
    scene bg classroom2 eve with longdissolve
    "It's been a couple weeks since that day."
    play music Eons
    "A couple weeks since Akiko assaulted me and got herself suspended from school."
    "Yeah, no one could ignore the fact she brought that sword in here when she wasn't even a member of the school kendo club."
    "Nor could they overlook the bruise on my wrist when I showed the principal."
    "Although their decision was probably more down to Akiko confessing to the crime, if they're honest about it. Like anyone listens to me around here."
    "Still, she's out of the picture, while I..."
    play sound schoolbell
    $ t = "Class Representative"
    t "Stand!"
    t "Bow!"
    "... I got transferred to a different classroom."
    $risa_name = "Classmate"
    show Risa concerned_side at center
    r "Chiyo, what are you doing? Come on, let's get out of here." with dissolve
    "A room where I don't know a soul. And all because Nozomi and her gang raised hell about me \"making them feel unsafe\" or some shit."
    $ t = "Chiyo"
    t "Ehh, it's my contact lens. It just popped out."
    r uniform_armup surprised_side "Again? Well, good thing we just cleaned the floor, I guess." with dissolve
    "Apparently even their parents got involved, the ruckus at the tennis court got mentioned, and it forced their hand into \"doing something about me\"."
    show Risa neutral_side
    t "Yeah... it's fine, you go on ahead; I'll catch up." with dissolve
    "But the school couldn't throw me out of here when I hadn't broken any rules, save that one time I skipped school."
    "Keeping me and Nozomi apart was their shitty attempt at a compromise."
    r smile_side "Nonsense. I can't leave you alone, not when..." with dissolve 
    "The fact I'm being made to suffer didn't even come into it. None of my new classmates will even look my way in here."
    r neutral_side "... Let's just find it and get out of here, 'kay?" with dissolve
    "I've never felt so alone. But at least some of my new classmates look cute. That girl down on her knees in particular..."
    t "Y-yeah, okay... oh, is that it?"
    "\"Chiyo\" apparently? Yeah, she's a looker all right."
    r smile_side "Great. Can we go now? Can't leave without my favourite hitting partner." with dissolve
    "And this friend of hers isn't so bad herself, now that I get a better look at her."
    t "Nooo, I gotta wash this... wait, \"Favourite hitting partner\"? You're always with..."
    r uniform sleeptalk "Ehh it's relative, don't sweat it. Let's go, then..." with dissolve
    "... Haven't I seen her somewhere before? Before all this, I mean?"
    stop music fadeout 5.0
    r frown "... You still here, stalker boy?" with dissolve
    ks confused "Uh... w-what?"
    "Or maybe she just reminds me of someone, if she's this quick to anger."
    r angry "You don't need to be here any more. Clear off." with dissolve
    scene bg corridor eve with blink
    play music Sorrow2
    "Fucking... bitches everywhere."
    "Is the rest of my school career just gonna be me getting constantly shouted at? I already can't stand it."
    "And it just... it could've all been so very different."
    "I had a bright, shining future right in the palm of my hand. And just like that it was taken away from me."
    "Taken by the one person I could ever love..."
    stop music fadeout 5.0
    show Hiroko uniform_headhold2 sleeptalk at center
    h "... Geez, I dunno. We dated for like, two semesters an' then he was gone. It weren't all that serious." with dissolve
    #Akiko was asking about Hiroko's former boyfriend who transferred out of school suddenly last semester. They did the long distance thing for about a month before he just stopped responding. She's well over it, they only dated about five months total anyway
    "Ugh. It's those girls again, apparently only just leaving their own classroom."
    "They didn't leave with the rest of them?"
    play music Evening
    s "Did you not try long distance for a while?"
    "I don't have the energy for this, so I duck back around the corner until my former classmates are out of there."
    show Hiroko:
        linear 1.0 xpos 0.75
    pause 1.0
    show Sayori uniform_handup smile at center, flip:
        xpos 0.55
    show Hiroko:
        xpos 0.75
    h annoyed_side "H'yeah, for like a month? 'Till he ghosted me anyway; bet he found some tail the second he got there." with dissolve
    "Not like I have anywhere to be, anyway."
    show Nozomi side smile_side at center, flip:
        xpos 0.35
    n "But what about Ryoma? Now the tournament's over do you think you and him...?" with dissolve
    "They could get a damned move on, though. Why haven't they cleared out like everyone else?"
    h rolleyes "Man, just drop it already! Me an' Ryoma ain't never gonna be a thing." with dissolve
    a "But there's definitely something there, right?"
    "Wait... That voice?!"
    h frown_side "Gawd, don't you start, 'Kiko. Ain't you done enough already?" with dissolve
    "It can't be..."
    show Akiko side uniform5 laugh noarmband at center, flip:
        xpos 0.15
    a "I KNEW there was something going on with you two!" with dissolve
    "It's... it IS her!"
    h uniform_armup angry_side blush vein "Th-there ain't nothing going on! He just plays tennis like a boss an' I watch him sometimes an' that's IT!" with dissolve
    a laugh_wink_side "Well I have it on good authority that he's been making eyes at you too, so I say strike while the iron's hot~" with dissolve
    "She's back in school?"
    h furious_side "Fuckin'... {w=0.5}you got that shit from Risa didn'tcha? {w=0.5}{nw}" with dissolve
    extend "DIDN'TCHA!" with vpunch
    a uniform_down5 smirk_side "What can I say? I like to think I'm a good listener, Homura." with dissolve
    "They swapped our fucking classroom arrangements?!"
    h uniform_headhold2 irritated "Rrrg, can't believe I'm taking the day outta tennis club for this shit." with dissolve
    hide Nozomi
    show Nozomi side happy at center:
        xpos 0.35
    show Sayori smile_right
    n "Aww, we had to do something to welcome our new classmate back to school~" with dissolve
    "I don't fucking believe this!"
    hide Sayori
    show Sayori uniform smile at center:
        xpos 0.55
    show Hiroko neutral_side novein -blush
    show Akiko smile_side
    n sad_side "Although I do wish you could've told us what you were up to, Akiko. You were in so much danger." with dissolve
    "All my hard work, all I've endured, after everything I've put into changing my life..."
    show Sayori neutral
    a uniform5 sigh "I-I know. But you girls already did what you could." with dissolve
    s uniform_handup sleeptalk "The fact you brought the sword at all suggests premeditation, though." with dissolve
    "It's like the entire universe is mocking my fucking existence."
    show Sayori neutral
    a surprised_side "A-as insurance! I didn't think I was going to use it!" with dissolve
    h smirk_side "Kinda cool you did though, ain't gonna lie." with dissolve
    show Akiko neutral_side
    h sad_side "But, uh yeah you should'a called us or something." with dissolve
    s smile_right "You merely regret that you were not there to witness it." with dissolve
    h annoyed_side "An' you don't? C'mon sis, we all wanted to see it." with dissolve
    a sad_side "It's just, when your plan failed and he texted me, I thought..." with dissolve
    show Sayori uniform neutral
    show Hiroko uniform neutral_side
    a sleeptalk "Look, I know it was stupid to confront him like that. But I couldn't take it any more." with dissolve
    a sleep "And it was just like you said. If I kept up the ruse he'd never suspect I'd turn on him, and that's exactly what I did." with dissolve
    a neutral_side "He thought he was in control. Right until the sword fell." with dissolve
    n sad_closed "Well, what's done is done. At least we got that thing away from him." with dissolve
    "My \"thing\"? My \"THING\"? Do you bitches even know what you took from me?"
    a sad_side2 "I'm just grateful he wasn't the only one around here who knows a thing or two about hypnosis, Nozomi." with dissolve
    "And you, Nozomi! I knew you had something to do with this; I just didn't realize you actually knew more about hypnosis beyond being able to stare at a fucking pendulum."
    show Nozomi sad_side
    a sad_closed "You... I think you might have actually saved my life, and I don't know how I can ever repay you for that." with dissolve
    "You took everything from me."
    n neutral_side "Akiko, you don't owe me anything. If he can't hurt us any more, that's all I want." with dissolve
    "Maybe I can build myself another penlight, just like the one I had..."
    a shy_side "S-still... thank you so, so much. What he did and what you did? It's been a real eye-opener for me." with dissolve
    "And I'll try, don't think I won't try..."
    a happy "The things that are possible with the human brain..." with dissolve
    "But something tells me I won't luck into making something as perfect as that \"thing\" ever again. Or get the chances I had with you girls these past weeks..."
    show Sayori smile
    n smile_side blush "I suppose, b-but um... hey, let's get going, okay? We are sort of loitering now aren't we?" with dissolve
    s smirk "Yes. Yes we are." with dissolve
    "So is this really it? Is this all my life has in store for me?"
    a uniform_down5 laugh "Haha, yup! I guess if I were still in the council I'd be reprimanding you right about now~" with dissolve
    show Sayori uniform smile
    h rolleyes "Whatevs, 'Kiko. C'mon then, let's finally get this moving." with dissolve
    "A life of constantly being ridiculed and cast out? Always a creep in everyone's eyes, with no way of... of ever fixing that?"
    show Hiroko neutral_side
    a smirk_side "Please. I've been dying to hear if Nozomi's singing voice lives up to the legend." with dissolve
    n happy noblush "Ehehehe~" with dissolve
    show Akiko smile_side
    h smile_side "Aw, it's a fuckin' trip, lemme tell ya..." with dissolve
    hide Hiroko
    hide Nozomi
    with dissolve
    show Akiko at flip:
        linear 1.0 xpos 0.35
    "Finally, those girls start to move on and I get ready to quietly, resignedly follow from a safe distance."
    a confused_side "Hmm... I wonder if I'm allowed to join the kendo club this late in the semester." with dissolve
    s surprised "Are you even permitted to handle a weapon on school premises after...?" with dissolve
    a embarrassed_side "I-I guess we'll see won't we? Aahaha... haaah..." with dissolve
    scene bg blackscreen with longdissolve
    "Is my life really... over?"
    scene bg school ext eve with longdissolve
    "I start my walk home with leaden steps, and once again from a distance I look on at... at Akiko."
    scene cg copycat ending 1 with blink
    "Surrounded by girls I guess she can now call her friends."
    "Just by being Akiko."
    "But who would ever want to be around me... just for me?"
    "I don't even... want to be me anymore..."
    $ persistent.copycat_ending_1_unlock = True
    jump Credits
label Copycat_Ending2:
    scene bg classroom2 eve with longdissolve
    "It's been a couple months since that day."
    play music Downtown
    play sound schoolbell
    "A couple months since I... since I convinced Nozomi to come back to me."
    show Risa uniform_armup sleeptalk at center
    r "Well that's a wrap. You ready to go, Chiyo?" with dissolve
    "Yeah, once she started listening to me again I convinced her to embrace who she's become, and to ignore all the negative influences trying to break us apart."
    $ t = "Chiyo"
    t "Yeah, you don't have to tell me twice."
    "But even so, those first few weeks afterwards were pretty hard going for both of us."
    show Risa neutral_side
    t "Hiro's coming today, isn't she?" with dissolve
    "The next day I was called up to the principal's office to answer for cutting class, and for the ruckus I supposedly caused during that tennis tournament."
    r uniform frown_side "She better. God knows I gotta blow off some steam today." with dissolve
    "Those girls were all up in his face about how I was a \"danger to the other students\", and to Nozomi in particular. Even the parents got involved, apparently."
    t "One day at a time, Ris'. At least we're graduating soon."
    "Fortunately, most of those accusations fell flat when it came down to the one person it all centered around..."
    show Akiko side uniform_up4 smile_side nglasses noarmband at center:
        xpos 0.75
    an "Oh, you're off to tennis practice? Tell everyone I said hi~" with dissolve
    "The one girl in this whole school who doesn't think I'm a piece of shit, no matter how much they tried to slander me back then, and ever since."
    # r sad_side "Oh, you bet I'm counting the days now." with dissolve
    r frown "Yeah, we'll... definitely do that..." with dissolve
    "So in the end, all that happened was I got transferred out of my old classroom to keep me and that Nozomi out of each other's faces."
    r frown_side "Ugh. Let's get out of here." with dissolve
    "Seeing as it meant I got to be in the same class as MY Nozomi, I can't say I minded all that much."
    hide Risa with dissolve
    an happy "Have fun, you two~" with dissolve
    "It's just a shame that they dragged her through the mud too, just for being the only one who can stand to be near me."
    show Akiko:
        linear 1.0 xpos 0.5
    pause 1.0
    show Akiko smile:
        xpos 0.5
    "Just because she's still my girlfriend in spite of everything." with dissolve
    an "Kyou? Are we ready to go too?"
    "Yeah... she looks and acts like the perfect girlfriend now."
    an "..."
    "She's so kind, and understanding. Not to mention drop dead gorgeous."
    an "..."
    "And patient."
    ks smile "Uh, yeah. I promised us a date, didn't I?"
    an laugh "Yes! Oh gosh, I'm so pumped for tonight~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    "She's been nothing but good to me since that day, no doubt about that."
    an giggle blush "We'll go to that restaurant you like, then we'll hit the karaoke club, sing all your favourite songs..." with dissolve
    stop music fadeout 5.0
    "And yet..."
    show Nozomi side sad_side at center:
        xpos 1.1
        linear 2.0 xpos 0.75
    n "Ah... you're still here."
    show Nozomi:
        xpos 0.75
    queue music Measured
    "... There's always this uncomfortable feeling that I can never shake."
    show Akiko sad_side2 -blush at flip
    an "Oh... i-it's you again." with dissolve
    "A feeling that always rises whenever these two appear together like this."
    n neutral_side "Yes, Akiko. Literature club is starting; we need the room now." with dissolve
    an sad_closed "Please don't call me that.{w=1.0} You know my name is-{w=1.0}{nw}" with dissolve
    n frown_side "Akiko. I'll remember it for you if you won't." with dissolve
    "No matter how perfect she gets, something always feels wrong about my Nozomi."
    an sad_side "O-okay. Sorry, Akemi, I don't want another argument. We'll get out of your hair now." with dissolve
    "She has the looks, she has the grace and... and the kindness..."
    an smile "After all, we have somewhere to be." with dissolve
    show Nozomi frown
    an giggle "Right, Kyou?" with dissolve
    ks neutral "Right..."
    "But she's... not enough."
    show Akiko neutral_side
    n front "Don't look at me like that. Don't you look at me at all." with dissolve
    ks "... Please. Don't do this again."
    n determined "You know, if you're so hell-bent on manipulating her to be just like me, it's weird that she doesn't completely loathe you by now, don't you think?" with dissolve
    "And I guess, neither is the girl I used to admire so much."
    show Akiko smile
    ks sigh "Let's go, Nozomi." with dissolve
    an happy "Mm~" with dissolve
    show Akiko:
        linear 2.0 xpos 1.1
    n "You know what you're doing to her is evil, Kyou! You could stop this any time you want!"
    ks "Uh-huh..."
    n angry "Don't you feel any shame at all?!" with dissolve
    stop music fadeout 5.0
    # n "Because maybe, deep down, there is still a conscience buried underneath all that entitlement you're carrying." with dissolve
    # n "You know what you're doing is evil. You... you're killing us from the inside, you must realize that."
    # n "And you're going to have to live with all of this. No one might be using a magic light to change you, but they won't have to."
    # n "You're changing yourself. And when this is all over, I don't think you'll like what you've become."
    # "I scoff at her. It sounds like the vacuous moralizing of someone who knows she's doomed."
    # "... I used to think the world of this woman, though. And I guess I owe it to her a little to consider what she said."
    # n "So what will you do?"
    scene bg blackscreen with longdissolve
    n "You can't run away from this! You'll NEVER get away from what you've done!"
    "With her all but screaming in my ears, I do my best to ignore her as I push past her assembling club members to walk away with my girlfriend in tow."
    scene bg ext school eve
    show Akiko side uniform_up4 smile nglasses noarmband at center
    with dissolve
    queue music Eons
    ks neutral "Hey, Nozomi I was thinking..."
    an "Yes, Kyou?"
    "But I gotta admit, this constant shit is getting to me."
    ks sigh "Try not to upset the other Nozomi in there. You know I don't like seeing you fight."
    an sad "Oh... well I wasn't trying to antagonize her. She just makes it so hard." with dissolve
    ks "Just... call her Nozomi, and don't push back if she calls you Akiko. It doesn't matter, alright?"
    an "... {w=1.0}{nw}"
    $ renpy.transition(dissolve, layer="master")
    extend smile "Alright, Kyou. You're right, I'll do better next time."
    ks neutral "Yeah. I know you will."
    an "So I'll get changed and meet you in town in an hour. Okay, Kyou?"
    ks "Uh, yeah sure. See you later."
    show Akiko giggle blush
    "She pecks my lips and lets out a little squeal of delight as I see the purity in her expression." with dissolve
    "It's as if any memories of our disagreement, or of that uncomfortable moment back in class, had already completely vanished from her head."
    scene bg blackscreen with dissolve
    "And as she disappears to get herself ready, I take myself back home to..."
    scene bg k bedroom eve with longdissolve
    "... To get ready? To go back out there where we'll probably run into more people who hate my guts?"
    "Maybe, maybe not, but the possibility doesn't exactly appeal."
    # "... To do what exactly? Dating my Nozomi hasn't exactly been the most thrilling of experiences if I'm honest."
    "And even if we don't get accosted I know how tonight will go. It'll be the same as every other night we've spent together."
    "We'll eat quietly as she smiles that same smile she always has. She'll sing those same songs for me in that adorable way she always does."
    "It's nice. She's nice. But somehow, I'm starting to think it's not worth the trouble."
    show phone at right with moveinright:
        ypos 0.346
    "I guess I'm... I'm just not feeling it tonight."
    an "\"Kyou, hi! I was just about to hop in the shower~\""
    ks neutral "Hey Nozomi, I'm not really in the mood for going out. I think I'm gonna just stay here and play some videogames or something."
    an "\"Oh...\""
    ks "Yeah. Sorry for getting your hopes up and everything."
    "I can feel the disappointment in that silence over on the other side."
    "But after a few moments she answers in just the perky kind of way I expect her to."
    an "\"O-oh, no no, it's alright. I completely understand.\""
    "It doesn't make me feel any less shitty about standing her up, though. After all, it's not like she has anyone else she can be around either."
    "Not any more."
    ks sigh "You can... come over if you want."
    an "\"Yeah, I'd love that! Okay, I'll be there soon; love you~ {font=DejaVuSans.ttf}♥{/font}"
    "I know, Nozomi. You're always accommodating and understanding when it comes to your boyfriend."
    ks neutral "Love you too."
    hide phone at right with moveoutright
    "I taught you that."
    scene bg k entrance eve
    $ renpy.show ("Akiko side {0}_up4 noarmband smile nglasses".format(AkikoClothes))
    with longblink
    "Not even an hour passes before she's at my door, and..."
    if AkikoClothes == "nozomi_b":
        ks casual confused "Oh man, you really didn't need to dress up today, Nozomi."
        an sad2 "... You don't like it? I can go back and change." with dissolve
        ks "Ahh no, don't be silly, it's fine."
        show Akiko sad
        ks "I was just saying, you didn't need to go to the trouble when we're just... you know." with dissolve
        an smile "Y-yeah, I know. I was just thinking back to our first date and..." with dissolve
        an happy blush "Ahh, it just felt right to wear this out again! It's been too long~" with dissolve
    elif AkikoClothes == "nozomi_a":
        an happy "Hehe... look familiar?" with dissolve
        "I force a smile as I realize what she's getting at."
        ks casual smile "It's the outfit I bought you on our first date."
        show Akiko giggle blush
        "She giggles to herself and nods affirmatively." with dissolve
        an "Y-yeah! It just felt right to wear this out again! It's been too long~"
    stop music fadeout 5.0
    scene bg k room eve
    $ renpy.show ("Akiko side {0}_up4 noarmband smile nglasses".format(AkikoClothes))
    with longblink
    "I simply nod and lead her inside, then go back to the game I was playing."
    play music Dark_Piano
    if AkikoClothes == "nozomi_a":        
        scene CopycatEnd2 blanktalk akiko_a smile
    elif AkikoClothes == "nozomi_b":
        scene CopycatEnd2 blanktalk akiko_b smile
    with blink
    k "So this is okay, right?"
    show CopycatEnd2 blank happy
    an happy "Of course it is. I actually get really into watching you play videogames now." with dissolve
    show CopycatEnd2 grin
    an "It's way more fun than playing them myself, or those board games I used to talk about." with dissolve
    show CopycatEnd2 confused
    an confused "Or... or kendo. Gosh, what was I thinking to get into kendo?" with dissolve
    "To think I used to be excited to bring her here."
    show CopycatEnd2 blanktalk
    k "It doesn't matter now. Just be quiet, I'm trying to concentrate." with dissolve
    show CopycatEnd2 blank happy blush
    an smile "Mm..." with dissolve
    "To be excited by her touch. To share her embrace when we slept together in my bed."
    show CopycatEnd2 smile
    "I didn't think the joy would fade so quickly. That her very presence would come to mean so little." with dissolve
    "But she's all I've got..."
    $ persistent.copycat_ending_2_1_unlock = True
    $ persistent.copycat_ending_2_2_unlock = True
    jump Credits

label Credits:
    $ credits_speed = 92 #scrolling speed in seconds
    scene black #Plain black background. Could maybe insert something customized later
    with longdissolve
    hide theend with dissolve
    show cred at Move((0.5, 35.6), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom") #Increment the second number in the Move command as more credits are added
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    stop music fadeout 3.0
    with Pause(3)
    hide thanks with dissolve
    with Pause(1)
    return
