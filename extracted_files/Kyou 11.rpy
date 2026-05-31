label Day11_Con_Kyou_Nozomi_Trance:
    scene bg street1 day with longdissolve
    "Yesterday might have mostly been a downer..."
    if hypno2 == "trance":
        play music Bright_Opening fadein 5.0
        "But I have a feeling today is going to be a lot more fun."
        scene bg classroom day with blink
        "I make it to class as usual and take my seat, flashing a Nozomi a knowing smile as she enters a little after me."
        show Nozomi side smile blush with dissolve
        pause 0.8
        hide Nozomi with dissolve
        "I provoke an embarrassed smile out of her as she notices me, and she can't hide the blush on her face as she takes a seat just in time for homeroom."
        scene bg classroom day with blink
        play sound schoolbell
        "As lunchtime descends, I look to Nozomi's desk and wait for the fun to begin."
        show Nozomi side smile_side at center, flip:
            xpos 0.25
        show Sayori neutral at center:
            xpos 0.5
        show Hiroko frown_side uniform_arm at center:
            xpos 0.75
        with dissolve
        h "Alrighty. Let's get out of this shithole and head up to the r- {w=1.4}{nw}"
        n surprised_side "U-uh, Hiroko, hold that thought." with dissolve
        h confused_side "Huh?" with dissolve
        n smile_side "Eheh, I mean... there's no need to say it. Let's just go~" with dissolve
        s "Hmm..."
        n frown_side "W-what?" with dissolve
        show Hiroko neutral_side
        s uniform_folded sleep "Oh, I was not going to say anything but you if you insist..." with dissolve
        s neutral "You appear to be especially flustered this afternoon." with dissolve
        n laugh "Ahaha, everything's fine, Sayori. I just... I guess this morning's lessons took a lot out of me." with dissolve
        s uniform neutral "Of course." with dissolve
        show Nozomi smile_side
        "Ugh, she deliberately cut them off from saying it. I probably should've told her to forget the trigger yesterday." with dissolve
        "But then, all I have to do is wander near them before they head out the classroom and loudly say to myself:"
        ks smile "Ahh, glad that's over. I guess I'll do lunch on the rooftop today."
        n surprised blush "E{nw}" with vpunch
        extend"-Eep!"
        show Sayori concerned
        h surprised_side "Nozo? What's up?" with dissolve
        if hypno4 == "spank":
            show Nozomi smile_side
            "I notice Nozomi visibly biting her lip, then composing herself with a smile and shaking her head." with dissolve
        elif hypno4 == "tickle":
            show Nozomi smile_side
            "I notice Nozomi straining a smile as she shifts awkwardly from foot to foot." with dissolve
        n "N-nothing~ Come on, let's get going."
        hide Nozomi
        hide Sayori
        hide Hiroko
        "I try not to grin too much as the three of them pass me into the corridor, before I casually follow them out." with dissolve
        scene bg rooftop with blink
        "The weather's not bad for lunch outside today. Not as cold as it has been."
        scene cg rooftop day
        show RoofHiroko handcheek irritated
        if hypno4 == "spank":
            show RoofNozomi handsdown frown
        elif hypno4 == "tickle":
            show RoofNozomi handsdown strainedsmile
        show RoofSayori leanback smile
        with blink
        "I quickly spot Nozomi's group and sit down for lunch a short distance from them. Close enough to overhear their conversations."
        h sleeptalk "Did {nw}" with dissolve
        extend "ANYONE get what Mr. Kobayashi was talking about? That dude mumbles so much." with vpunch
        show RoofSayori sleep
        s rolleyes "Or you are a poor listener. He was talking about club commitments for this weekend." with dissolve
        show RoofHiroko annoyed
        h annoyed_side "Oh. Like I don't already know that shit." with dissolve
        if hypno4 == "spank":
            show RoofNozomi pain_left
            n side sad_side "Ah... H-how is your club doing anyway, Sayori?" with dissolve
        elif hypno4 == "tickle":
            show RoofNozomi strainedsmile_left
            n side smile_side "Mhmhm... H-how is your club doing anyway, Sayori?" with dissolve
        show RoofSayori neutral
        s neutral_right "Not so bad. I mostly help the other members in my club, though, so it hasn't been as useful for me as I'd hoped." with dissolve
        show RoofSayori sleep
        s annoyed "I would be better off studying at home, but I will not abandon my obligations to the study club in their time of need." with dissolve
        n "T-to think you nearly joined the literature club with me."
        show RoofSayori neutral
        s sleep "Yes, well, I am not going to get hung up about that." with dissolve
        show RoofHiroko worried
        h surprised_side "You okay, Nozo? You're looking, like... {w=0.5}{nw}" with dissolve
        extend "SUPER antsy there." with vpunch
        "I can see Nozomi squirming in her seat from here, even as she's clearly trying to disguise it."
        if hypno4 == "spank":
            show RoofNozomi pain_right
            n smile_side "I-I'm fine... Really, I'm fine~" with dissolve
        elif hypno4 == "tickle":
            show RoofNozomi strainedsmile
            n laugh blush "Ehehe, I'm okay, really~" with dissolve
        show RoofSayori worried
        s concerned_right "Are you sure? It really looks like you're struggling with something." with dissolve
        show RoofNozomi smile_left blush
        n smile_side blush "Thanks for your concern, but..." with dissolve
        show RoofHiroko smile
        h uniform_armup smile_side "C'mon! You can share anything with rooftop club~" with dissolve
        show RoofNozomi panicked_right
        n "!! {w=0.8}{nw}" with dissolve id Day11_Con_Kyou_Nozomi_Trance_d7db06f0
        if hypno4 == "spank":
            show RoofNozomi grimace
            show RoofHiroko surprised
            $ renpy.transition(dissolve, layer="master")
            n front pain blush "O-{w=0.3}{nw}" id Day11_Con_Kyou_Nozomi_Trance_5c944d0a
            extend "OW!" with vpunch
            h surprised_side "Huh? Something I said?"
        elif hypno4 == "tickle":
            show RoofNozomi laugh motionlines
            show RoofHiroko surprised
            n laugh blush "Ahahahaha!" with dissolve
            h surprised_side "Huh? What's so funny?"
        if hypno4 == "spank":
            "Nozomi visibly winces as she cries out, squirming on her seat uncomfortably while she shakes her head."
            show RoofNozomi pain_right
            n side frown_side "It's... ahh, n-no it really is nothing. I'm just going to deal with it myself." with dissolve
            show RoofSayori neutral
            s surprised_right "I would have thought you sat on something, but you were struggling before." with dissolve
            show RoofNozomi grimace
            n sad_closed "Tststss... i-it's nothing, really." with dissolve
            show RoofHiroko worried
            h uniform sad_side "Uhh, seriously, was it something you ate then?" with dissolve
            show RoofNozomi pain_right
            n frown_side "I SAID it's nothing! {w=0.8}{nw}" with dissolve
            extend "{size=16}Ow...{/size}"
            show RoofSayori worried
            s frown "Nozomi, this is getting silly. Tell us what is wrong." with dissolve
            h frown_side uniform_armup "Yeah, what gives? It's just us, Nozo."
            show RoofNozomi grimace motionlines
            "I can see Nozomi jump a little in her seat as she tries in vain to compose herself in front of her concerned friends." with dissolve
            n "Y-you wouldn't understand."
            show RoofNozomi frown noblush
            show RoofSayori neutral
            with blink
            "Some time passes as Nozomi's friends drop the issue and get into their lunches. But Nozomi barely stops squirming the entire time."
            "There'll be a few moment's calm, then she'll jump a little upwards and sometimes let out a squeak before settling back down..."
            "Then it happens again. Then again."
            "It's too distracting for the others to hold their tongues forever."
            show RoofSayori worried
            s uniform concerned "Nozomi I am afraid I must insist that we get you off the rooftop and-{w=1.5}{nw}" with dissolve
            show RoofHiroko shocked
            show RoofSayori shocked
            stop music fadeout 5.0
            show RoofNozomi screaming
            $ renpy.transition(dissolve, layer="master")
            n shocked "OHHHHH!" with shake
            h "Wh-what the fuck was {nw}"
            extend "THAT?!" with vpunch
            "Yeah... that was more of a howl than a squeak that time."
            show RoofSayori worried blush
            s blush "This... might be more personal than I thought. Perhaps we should be the ones to leave the rooftop." with dissolve
            play music Measured fadein 5.0
            scene bg blackscreen
            play sound bodyimpact
            with dissolve
            $persistent.nozomi_rooftop_spanked_unlock = True
            "Just then Nozomi lets out a full-throated scream as she doubles over on the ground, her hands clutching her rear."
            scene RoofNozomi2 lines_spanked with dissolve
            "She's... holy shit, what's going on?!"
            h "NOZOMI!" with vpunch
            "As her friends crowd around her, I feel my chest tighten."
            "Do I go over there? Do I help her?"
            "CAN I help her?"
            s "We... w-we are taking you to the nurse."
            show RoofNozomi2 scream
            n "N-NO, please, I- {w=0.5}{nw}" with dissolve
            extend "AHH!" with vpunch
            show RoofNozomi2 grimace nolines
            n "{size=16}J-just need to...{/size}" with dissolve

            play sound schoolbell
            scene bg rooftop
            show Hiroko sad_side at center:
                xpos 0.75
            show Sayori concerned at center, flip:
                xpos 0.25
            show Nozomi front sigh at center:
                ypos 1.3
                linear 2.5 ypos 1.0
            with blink
            stop music fadeout 5.0
            with dissolve
            $ persistent.nozomi_rooftop_spank2_unlock = True
            "It's just then that the bell rings for the end of lunch, as Nozomi is hauled up by her friends, breathing a deep sigh of relief."
            show Nozomi:
                ypos 1.0
            n "Haaah... h-haaah, let's just... get to class, I'm fine."
            h uniform_armup furious_side "You ain't fine, you fuckin' idiot!" with dissolve
            n side sad_closed "N-no, I mean... I know, but it's passed." with dissolve
            n laugh "See? I'm not shaking anymore! Ahaha..." with dissolve
            show Hiroko frown_side
            s uniform_folded irritated "Nozomi, please. I am telling you as a friend: Get yourself looked at." with dissolve
            show Nozomi sad_side
            show Hiroko uniform
            s frown "We cannot force you, but would you please do it for our sake? If not your own?" with dissolve
            "I can see Nozomi's face drop ashamedly as she nods with a resigned sigh."
            n sad_closed "I'll see a doctor as soon as I can, I promise." with dissolve
            h sad_side "Good. Don't scare us like that again. Jesus." with dissolve
            show Hiroko frown
            "Just then, the pink-haired girl glares in the direction of me and the other assembled onlookers." with dissolve
            h angry "What are {nw}" with dissolve
            extend "YOU all looking at? Show's over." with vpunch


        elif hypno4 == "tickle":
            "Nozomi lets out an amused giggle and shakes her head, jerking her hand away as she realizes she had reached down to grab her shoe."
            n "N-n-no, there's nothing to share! R-really!"
            show RoofSayori smile
            s smirk "Do you honestly expect us to believe you, Nozomi? You clearly have something in mind that is truly hilarious." with dissolve
            n "Hahaha~ N-no, not at all!"
            show RoofHiroko laugh
            h laugh_side "Aww, you gotta tell us!" with dissolve
            n "Ehehehehe~"
            s uniform happy "We are not ones to judge. It will just be between us."
            s smile "It is as Hiroko said: You can share anything with rooftop club."
            show RoofNozomi panicked_left
            show RoofHiroko surprised
            n shocked_side "AHH!" with vpunch
            show RoofNozomi laugh
            n laugh "Th-th-there's nothing to tell! Ahahaha~" with dissolve
            stop music fadeout 5.0
            s uniform_folded "And what is said in rooftop club-{w=0.8}{nw}"
            show RoofNozomi panicked_left
            n shocked_side "N-NO PLEASE!{w=0.5}{nw}" with dissolve
            s "-stays in rooftop club."
            show RoofNozomi laughing
            show RoofHiroko shocked
            show RoofSayori shocked
            $ renpy.transition(dissolve, layer="master")
            n front cry_laugh reddened "AAAAHAHAHAHAHA!" with shake
            play music Measured fadein 5.0
            "It's hard not to react to Nozomi as she bursts out laughing at a rather frightening volume."
            "One of her shoes is sent flying while her feet kick futiley back and forth; any notion of trying to resist the hypnosis-induced tickling dashed in a wave of uncontrolled giggling."
            "Certainly the few others assembled on the roof are looking her way now. How could they not?"
            h "Nozo? S-seriously, what's so freakin' funny?"
            if accepted_terms == True:
                "And right now, I realize, I maybe should have given some more thought to this..."
            else:
                "And as I watch with the others, I find it fascinating to see how completely committed her mind is to my hypnotic suggestion."
            n "M-m-make it stohohohohop!" with vpunch
            show RoofSayori worried
            s concerned "Make what stop? What is happening?" with dissolve
            if accepted_terms == True:
                "I didn't think to put a limit on how much this could affect her..."
            n "St-st-stop saying rooofthahahahahaha!"
            if accepted_terms == True:
                "Or to give her another out besides relying on the school bell..."
            show RoofHiroko worried
            h surprised_side "... Roof? Stop saying roof?" with dissolve
            "Still, in the worst case if she seriously needed to she'd snap out of it, right?"
            n "Ahh... ahhahahahah... *wheeze*" with vpunch
            show RoofSayori angry
            s annoyed_right "Hiroko, if you knew what word she asked you not to say, why would you say it?" with dissolve
            "... Right?"
            show RoofHiroko angry
            h angry_side "H-hey, {w=0.2}I'm fuckin' {nw}" with dissolve
            extend "CONFUSED, alright?" with vpunch
            scene bg blackscreen
            play sound bodyimpact
            with dissolve
            $persistent.nozomi_rooftop_tickled_unlock = True
            "As they argue, Nozomi collapses onto the floor, clutching her sides as she convulses to the sound of her own manic laughter."
            scene RoofNozomi2 nozomi_tickled lines_tickled hardlaugh blush with dissolve
            "... She isn't snapping out of it."
            h "N-Nozo?! Holy shit."
            n "AHAHAHAHA E-EVERYTHING HUHUHUHUHUHUURRTS!" with shake
            s "How is it that you're STILL laughing?!"
            show RoofNozomi2 weaklaugh nolines
            if accepted_terms == True:
                "As Nozomi's friends crowd around her quivering form, I resist the urge to join them. I don't think she'd appreciate seeing her tormentor right now." with dissolve
                "A couple minutes go by as the two girls try to calm Nozomi down."
                "She complies only because her constant laughing and squirming has drained most of the strength and breath from her body."
                play sound schoolbell
            else:
                "As Nozomi's friends crowd around her quivering form, I gingerly approach them and lean down to lock eyes with Nozomi." with dissolve
                "As she lets out another squeal of laughter she dimly acknowledges the sight of me through tear-stained eyes and raises a quivering hand pleadingly."
                "She and I both know I'm the only one who can help her."
                ks smile "Nozomi, stop laughing."
            scene bg rooftop
            show Hiroko sad_side at center:
                xpos 0.75
            show Sayori concerned at center, flip:
                xpos 0.25
            show Nozomi front sigh at center:
                ypos 2.0
                linear 2.0 ypos 1.0
            with blink
            stop music fadeout 5.0
            $persistent.nozomi_rooftop_tickle2_unlock = True
            if accepted_terms == True:
                "The sound of the bell must be the biggest relief to Nozomi's ears as she's presumably freed from the phantom tickling sensations that tormented her." with dissolve
                "Drawing a full breath, she picks herself up off the floor with her friend's help."
            else:
                "My words must be the biggest relief to Nozomi's ears as she finally starts to recover from her giggling fit" with dissolve
                "Drawing a full breath, she picks herself up off the floor with her friend's help."
            show Nozomi:
                ypos 1.0
            n "Haaah... h-haaah..."
            s sleep "Oh, thank goodness you've calmed down." with dissolve
            n "S-sorry to worry you. I'm... I'm okay now."
            h "Geez, Nozo, I never knew you could laugh like that."
            if accepted_terms == True:
                show Nozomi side at flip
                n side smile_side "Mhmhm... let's just head back, okay?" with dissolve
                s concerned "... Of course." with dissolve
                show Hiroko uniform_armup frown
                "Just then, the pink-haired girl glares in the direction of me and the other assembled onlookers." with dissolve
                h furious "What are {nw}" with dissolve
                extend "YOU looking at? Show's over." with vpunch
            else:
                show Nozomi side at flip
                n side smile_side "Mhmhmhm..." with dissolve
                "As she takes another breath, Nozomi flashes me a look. Seeing and hearing me speak was the only thing that saved her from laughing herself to exhaustion."
                show Nozomi sad_closed blush
                "I have a feeling she enjoyed that realization immensely." with dissolve
                show Sayori frown_right
                show Hiroko uniform frown
                play music Rain fadein 5.0
                "On the other hand Nozomi's friends, now they've had a moment of relief, have come to a different realization having noticed my involvement in this." with dissolve
                h "The fuck is going on here?"
                ks "Don't worry. Everything's fine. Nozomi's perfectly safe."
                s scowl "And how would you know?" with dissolve
                n smile "He's... he's right. Don't worry about me." with dissolve
                show Sayori concerned
                show Hiroko neutral
                n "Kyou hypnotized me last night and made it so I'd feel tickled all over if anyone said..." with dissolve
                show Hiroko surprised_side
                n front pout_left uniform_folded "Well, I'm not going to say it." with dissolve
                h "\"Hypnotized\"?"
                s "Now I am even more confused."
                n neutral noblush "About what? I thought I'd explained pretty clearly." with dissolve
                h frown uniform_arm "So you two gotta thing going on now?" with dissolve
                n smile "Well, yes. I guess we do. We share a common interest it turns out~" with dissolve
                play sound schoolbell
                show Hiroko annoyed
                "The sound of the bell rings out on the roof, helping to keep further questions at bay as everyone makes for the exit." with dissolve
                s annoyed "This is not over. We'll continue this later." with dissolve

        stop music fadeout 5.0
        scene bg k entrance eve with longblink
        if hypno4 == "spank":
            "The rest of the day was awkward. Nozomi's little incident was whispered about during lessons, and it was all she could do to pretend not to notice."
        elif hypno4 == "tickle":
            "The rest of the day was awkward. Nozomi's giggling fit was whispered about during lessons, and it was all she could do to pretend not to notice."
        "I headed straight home alone, having sent her a text inviting her over any time she wanted."
        play sound doorbell
        "... Although I'm hardly surprised to hear the doorbell barely a minute after I'm home myself."
        play sound dooropen
        show Nozomi front concerned with dissolve
        play music Monologue fadein 5.0
        n "So... We really need to talk about today, huh."
        play sound doorclose
        ks sigh "Yeah... That was a bit more intense than I was going for."
        $nface = "sleeptalk concerned"; nclothes = "uniform folded"
        n sleeptalk_concerned uniform_folded "Oh my god... I thought I was going to die." with dissolve
        if hypno4 == "spank":
            n sleep_concerned "It wasn't so bad at first. It almost felt nice for a little while." with dissolve
            n side sad_side "But then as they kept saying the word, it started to get painful." with dissolve
            n sad "By the end of it... it was as if I was back in my room with you. Only this time you were spanking me like some kind of sadist." with dissolve
            n front pain "Those last few moments... I was in so much pain, I couldn't stand it." with dissolve
        elif hypno4 == "tickle":
            n sleep_concerned "I mean, it was kinda fun to start?" with dissolve
            n side sad_side "Surprising at first, but after that it felt... gentle. Like a funny secret only you or I really knew." with dissolve
            n sad "But when they started saying the word it was like I was back in my room with you, right when you were giving me your worst." with dissolve
            n front concerned "By the end it felt like I was being tickled by a sadist. I could hardly breathe." with dissolve
        n blush "And everyone... E-everyone was staring at me. They all knew." with dissolve
        n sleep_concerned "Kyou, this is going to follow me for the rest of my school life." with dissolve
        n "So I... I think the public trigger was a bad idea and I never should've gone through with it."
        ks "I'm sorry, Nozomi. I probably should've been more careful about it."
        n sleeptalk_concerned "Yeah..." with dissolve
        scene bg k room eve
        show Nozomi front2 concerned at center
        with blink
        "There's a gloomy silence as Nozomi and I step into the living room."
        "I look to her, a little lost for words... But as she looks back to me it seems she has more to say."
        n pout_left uniform "So, um... I was thinking some more about what to do." with dissolve
        ks neutral "Yeah?"
        n neutral noblush "I want you to remove the trigger, Kyou. You can do that, can't you?" with dissolve
        ks "Yeah, I don't see why not."
        ks "I've de-programmed you before so this shouldn't be any different."
        show Nozomi sleep
        "She responds with a tentative nod." with dissolve
        n "Right. And then I'd like us to try something else. We could consider it a trade of sorts."
        "... What on earth is she thinking now?"
        ks "Go on..."
        stop music fadeout 5.0
        n blush "..." with dissolve
        ks confused "Uh, Nozomi?"
        n side sad_side "Y-yes, so..." with dissolve
        n "Even as weird and humiliating and... and scary as it was for me this afternoon..."
        play music Night_Road
        n neutral_side "Once the dust settled, I couldn't help but feel how much it thrilled me to experience that kind of powerlessness." with dissolve
        n sad_closed "Being unable to resist your hypnotic compulsions, even though in the moment I wanted to more than anything." with dissolve
        n front2 sleep_concerned "I can't even describe to you how... U-um..." with dissolve
        n sleeptalk_concerned "How intoxicating it all felt." with dissolve
        n sleepy "I..." with dissolve
        n front frown "I-I want to feel it again." with dissolve
        n pout_left "Just... j-just not where it might seriously come back to hurt me." with dissolve
        n sleeptalk_concerned "So Kyou... what I want is..." with dissolve
        n "I-is..."
        n frown "I want you to dominate my mind!" with dissolve
        ks "I... Y-You mean like last time?"
        "Nozomi lets out a sigh as she shakes her head firmly."
        n irritated "No, I don't mean like last time." with dissolve
        n sleep "We wouldn't be pretending I'm a captured settler, or some petty thief who needed a lesson." with dissolve
        n sigh "I don't mean roleplay, Kyou." with dissolve
        n concerned "I want you to dominate... me!" with dissolve
        n sigh "I want to be aware of you trying to command me to do and think things. I want to try and resist, and... I want to succumb." with dissolve
        "I... It's not like I didn't know this was coming."
        n sleepy "You're not surprised, are you? We've already come this far." with dissolve
        "Everything we've been doing has led to this moment."
        n side sad_side "If we want to truly \"get it out of our systems\" like we were saying, then we need to do this. We need to go all the way." with dissolve
        n sad "And I think you would want to further your skill as a hypnotist, right?" with dissolve
        "She's not even wrong about that."
        "Besides the fact we've been able to spend so much time together, I've found practicing hypnosis with her to be incredibly fascinating."
        ks frown blush "R-Right."
        n sad_side "Right. And just like before, I do want you to have some fun with this, Kyou." with dissolve
        n "So long as you don't try anything stupid, I'm sure we'll both have a good time while you explore the limits of your abilities."
        "Still, even as she says all this, I can't say she looks very comfortable."
        n sad_closed "B-But, I trust you." with dissolve
        "Could it be that she's STILL holding back about what she wants?"
        n front surprised "I never thought I'd be saying it, but... I really do trust you. So much." with dissolve
        n sleepy "The fact all your post-hypnotic suggestions work so well on me... that's proof, isn't it?" with dissolve
        n frown "So that's why... that's why I want to see it through. I want to explore my fantasies to the fullest." with dissolve
        n concerned "With you..." with dissolve
        ks "But what you're asking is..."
        n side sad_closed "Obviously I don't mean for you to try anything permanent. That'd be silly. And obviously impossible." with dissolve
        n "And... and of course you can't literally dominate me through hypnosis. I know that."
        n "But if, just for tonight... if just for a little while, you could convince me that you had total control over my mind?"
        n front sleeptalk_concerned "Would that be bad? Would that be something you'd want to do?" with dissolve
        "I'm not gonna lie. The thought of having someone as pretty as her at my beck and call is goddamn arousing, real or not."
        "It sure is a fantasy I could get behind..."
        ks "Total control, huh?"
        n front surprised "I-I-I mean as much as it's possible to seem like that?" with dissolve
        ks frown blush "R-... right. Because we know you're always in control, no matter how deeply hypnotized you get."
        n side sad_closed "Right... That's exactly right." with dissolve
        "She says that. WE say that. But..."
        n "So like I said, I want you to have some fun, but y-... yeah, let's keep it clean, okay?"
        "Does she really mean what she says? It almost feels like a contradiction."
        "Telling me she wants to feel the illusion of being totally controlled, while still insisting there are limits."
        "Maybe that's because she's still too shy about what she truly wants?"
        "What if she's still holding back, even now?"
        ks "Okay... i-if you're sure."
        n front concerned "W-what do you think?" with dissolve
        ks "It's... T-that is..."
        stop music fadeout 5.0
        scene NozomiProvoke angry blush arms1 kyou1
        n angry normal "Oh come {nw}" with dissolve
        extend "ON, Kyou! How many guys do you think would kill for a chance like this?" with vpunch
        "I jump back a little as she raises her voice, and it jolts my brain back into gear."
        show NozomiProvoke frown
        "Do I have any serious objections to doing this? Why not try to give her what she wants?" with dissolve
        play music Clumsy_Two
        "If she's holding back, then I am too. I should just do it."
        "And I'll do it in a way she'll approve."
        show NozomiProvoke scared kyou2
        "So with a smirk, I pull my penlight out from its home in my pocket, which immediately grabs Nozomi's attention." with dissolve
        ks smirk "I'll make that the last time you raise your voice to me in this house, young lady."
        show NozomiProvoke scared_light with dissolve
        show NozomiProvoke scared with dissolve
        show NozomiProvoke dazed arms2
        $ renpy.transition(longdissolve, layer="master")
        "And with that I flash the light across her eyes, causing her to immediately snap her gaze to it with a peculiar longing."
        n "K-kyou..."
        show NozomiProvoke dazed_light with dissolve
        show NozomiProvoke dazed with dissolve
        ks smile noblush "Shhh, Nozomi. Don't say anything more."
        show NozomiProvoke dazed_light with dissolve
        show NozomiProvoke dazed with dissolve
        hide NozomiProvoke
        show NozomiProvoke sleepy arms2 kyou2
        $ renpy.transition(longdissolve, layer="master")
        ks smile "We both know you can't resist the light. It's futile of you to try."
        show NozomiProvoke sleepy_light with dissolve
        show NozomiProvoke sleepy with dissolve
        pause 0.5
        $persistent.nozomi_provoke_unlock = True
        $ light_y = 0.3; light_x = 0.4
        play sound sitting
        scene bg blackscreen with dissolve
        show cg k room eve:
            ypos -0.3
            linear 0.2 ypos 0.0
        show NozomiHypno standing drowsy:
            ypos -0.3
            linear 0.2 ypos 0.0
        "As I finish flashing the light again I reach out and firmly push on her shoulder, causing her to stumble backwards onto the couch behind her."
        # play music Flow fadein 15.0
        call cglightshow from _call_cglightshow_153
        "She already looks out of it as she slumps on the seat."
        "I've barely said anything to her, but all her prior conditioning must be doing most of the work for me."
        call cglightshow from _call_cglightshow_157
        "Of course it crossed my mind that I could've just used the spoken trigger to put her under immediately..."
        call cglightshow from _call_cglightshow_158
        "But as I pass the light across her attentive eyes again, I'm certain doing it in this manner is much more fitting for the occasion."
        call cglightshow from _call_cglightshow_154
        ks "That's right, Nozomi. Just keep looking at the light..."
        call cglightshow from _call_cglightshow_159
        ks "Powerless to resist. Helpless to do anything but stare and let the light and my words take you deep into hypnotic trance."
        call cglightshow from _call_cglightshow_160
        ks "Knowing that as you stare, as you drop, you become more and more hypnotized. More and more under my power."
        call cglightshow from _call_cglightshow_155
        $ light_y = 0.37; light_x = 0.4
        show NozomiHypno drooping sleepy
        $ renpy.transition(longdissolve, layer="master")
        ks "Looking and relaxing. Looking and drifting..."
        call cglightshow from _call_cglightshow_156
        ks "Finding yourself so completely relaxed and powerless, Nozomi. So deeply hypnotized for me..."
        call cglightshow from _call_cglightshow_161
        ks "And that's why when I give the command, you will..."
        show NozomiHypno sleep
        ks "Sleep, Nozomi." with dissolve
        "And down she goes."
        "I didn't even have to finish saying the word \"sleep\" before her eyes snapped completely shut."
        ks "Very good, Nozomi. Nice and deep for me. So completely hypnotized and under my power."
        "So far so good. Nozomi's so adept at dropping for me now that I doubt much of my theater with the penlight just now was even necessary."
        "But before I get to the fun stuff, I need to make sure she won't suffer a repeat of this afternoon."

        ks "And now I need you to listen and accept what I have to tell you. Completely accepting my words."
        ks "You'll do that, won't you, Nozomi."
        ncg "Mhm..."
        if hypno4 == "spank":
            ks "Good girl. So now you need to accept the word \"rooftop\" will no longer induce a feeling of being spanked."
        elif hypno4 == "tickle":
            ks "Good girl. So now you need to accept the word \"rooftop\" will no longer induce any ticklish feelings in you."
        ks "It is a perfectly normal word and you will not react to it in any special way."
        "That should do it. Now I'll see about giving her what she wants."
        "And as I realize more and more, is also what I want."
        ks "And now I want you to think of something else, Nozomi."
        ks "This time, I want you imagine that while we're alone in this house, every time I give you an instruction you will find yourself wanting to obey and make it reality."
        ks "You might want to resist my instructions, and you can..."
        ks "But if I repeat the instruction while snapping my fingers, you will find it twice as hard to resist; wanting more and more to obey my words."
        ks "Every time I repeat the command while snapping my fingers, it becomes twice as hard again to resist."
        ks "Twice as tempting to obey and accept my words as your truth."
        ks "You can imagine it... can't you, Nozomi?"
        show NozomiHypno blush
        $ renpy.transition(longdissolve, layer="master")
        ncg blush "Mmmn..."
        "The little purr that escapes her lips takes me a little by surprise, but it also makes me smile."
        "Everything we've done together, she's been nothing but committed, trusting and seemingly insatiable for more."
        ks "What's more, each and every time you accept an instruction of mine into your head, you will feel a gentle wave of pleasure envelop your entire body."
        ks "Because it feels so good to accept and obey my every command, Nozomi. So good, so right, and so very pleasurable."
        show NozomiHypno noblush
        ks "Do you accept everything you've been told so far, Nozomi?" with dissolve
        ncg sleeptalk "Yes... Everything..." with dissolve
        show NozomiHypno sleep
        ks "Wonderful." with dissolve
        "This is gonna be great."
        ks smile "So now, in a few moments we're going to wake you up."
        ks "I will count to three and you will awaken happy and refreshed once more."
        ks "One... beginning to stir."
        stop music fadeout 10.0
        ks "Two... fully accepting of everything you have been told."
        ks "And... three."
        ncg sleepy "{size=16}Mmm...{/size}" with dissolve
        "I chuckle as I get to see her waking expression once again."
        ks "Wide awake, Nozomi."
        play music Eons fadein 20.0
        #The CGs could transition here, from the tentative slumped on couch CG I have in mind for the scene up to here, back to the default CG for the rest of it until we get to the stripping CG
        ncg standing surprised "Ah, y-yes I'm awake!" with vpunch
        ks "So you are. And how are we feeling right now?"
        ncg confused "Uh... to be honest with you, I'm feeling a little nervous." with dissolve
        ncg neutral "Was it really okay to do this?" with dissolve
        ks "It's what you wanted isn't it?"
        ncg sad blush "Yes... yes, it was." with dissolve
        "There's that shyness again. That self-doubt."
        "I'm sure putting her new conditioning to use will help her loosen back up."
        ks smirk "So now I'm thinking I made good of that threat I made."
        ncg stern noblush "Wait, threat? What threat?" with dissolve
        ks "I want you to calmly and quietly say \"I cannot raise my voice\"."
        ncg confused "U-Uh..." with dissolve
        ncg "{size=16}I cannot raise my voice...{/size}"
        "Her reply barely comes out above a whisper."
        "That's not only cute as hell, but I can't help but notice..."
        ks "Heh. So you just obeyed me straight away, huh?"
        ncg folded stern_closed blush "I just... I-It was a harmless request!" with dissolve
        ncg "Why would I refuse that?"
        ks "Especially not when obeying me feels so good, huh?"
        show NozomiHypno sad
        "Nozomi lets out a little squeak as she averts her eyes." with dissolve
        ncg "N-No comment..."
        ks "Anyway, from now on you are not to talk any louder than when you said \"I cannot raise my voice\" just now."
        show NozomiHypno folded stern_closed
        "I can see Nozomi frown in concentration." with dissolve
        ncg "That's... That's not going to happen."
        "So she says, but she had to force those words from her lips and I can still see her blushing."
        ks smile "Do you really think you can hold out against me, Nozo?"
        ncg angry noblush "I intend to!" with dissolve
        "With a grin, I reach over and snap my fingers by her ear as I talk."
        play sound fingersnap
        show NozomiHypno lookup blush
        ks "You will not raise your voice." with dissolve
        ncg "U-Uuuh... th-that's..."
        play sound fingersnap
        ks "You will only talk calmly and quietly."
        "Nozomi seems to shiver in place on the couch as she struggles to speak."
        ncg "{size=16}O-oh my gosh I can feel it working...{/size}"
        "My grin only widens at the sound of her voice, muted as it is."
        ks "How does it feel?"
        ncg standing sad "{size=16}Like... your words are a siren song. I want to follow along to them without thinking.{/size}" with dissolve
        ncg stern "{size=16}And it's taking all the willpower I have to resist you.{/size}" with dissolve
        ks "But giving in felt so right, didn't it?"
        show NozomiHypno drooping sleeptalk
        "Nozomi's head bows as she lets out an aroused-sounding whimper." with dissolve
        ncg "{size=16}So... S-So right...{/size}"
        "And what a fucking rush I'm feeling about this. Being able to do this to her, being responsible for the growing pleasure she feels..."
        "Because I could assure her the pleasure's feeling very mutual right now."
        "And we're just getting started tonight."
        ks "So good and so right to obey, Nozomi. And we both know you're not going to resist my next command."
        show NozomiHypno standing stern
        "Bristling at my challenge, Nozomi takes a breath and tries to compose herself as she stares hard at me." with dissolve
        ncg "{size=16}You don't know that at all!{/size}"
        "Not gonna lie, her staring me down is making me uncomfortable, especially with what I next have in mind for her."
        "Her best chance of resisting me is probably to keep me from telling her what to do in the first place."
        "But I'll just swallow my nerves and just get the words out. I mean, it's not even like she hasn't done this for me before..."
        ks frown blush "T-take your clothes off, Nozomi." # Right there on the couch. Amend the below lines to remove any reference to her standing while stripping
        ncg surprised blush "{size=16}U-uhh?!{/size}" with dissolve
        "Nozomi lets out another whimper as she squirms on the couch."
        "I think I know Nozomi well enough to know her protesting reaction is theater. So I lean in and try to steady my breath as I command her further."
        ks "That's right, Nozomi. I'm not asking you, and we're not roleplaying characters."
        "Raising my hand again, Nozomi quivers on the seat in anticipation."
        "She can only swivel her widened eyes to watch as I prepare to snap my fingers once again beside her left ear."
        play sound fingersnap
        show NozomiHypno lookup blush
        ks "I'm telling you, Nozomi Akemi, to strip for me." with dissolve
        ncg "{size=16}{cps=20}I... I-I ref... {w=0.5}refuse-{/cps}{/size}{w=1.0}{nw}"
        play sound fingersnap
        ks "Take off your clothes."
        scene bg blackscreen
        show NozomiCouchStrip nozomi1 armdown nervous blush1 glasses1
        with blink
        "I don't know if was specifically the directness of that last command, or if my repeated ordering had simply worn her down..."
        "But even as she meekly shakes her head at me, I notice Nozomi reaching down and tucking a trembling finger inside her sock."
        "I don't think she even realizes she's doing it."
        n "{size=16}You can't make me...{/size}"
        "She just needs one more push."
        play sound fingersnap
        ks frown "Socks off, Nozomi."
        show NozomiCouchStrip nozomi1 armup nervous blush1 glasses1 with dissolve
        n "{size=16}I wo... {w=0.5}{/size}{nw}"
        show NozomiCouchStrip nozomi1 armup disbelief blush1 glasses1
        $ renpy.transition(dissolve, layer="master")
        extend "{size=16}w-wont?!{/size}"
        "She's still protesting, until the loose sock dangling from her fingers gives her cause for quiet."
        ks smirk blush "Good girl. Now take off the other sock. And your top."
        play sound clothes
        hide NozomiCouchStrip
        show NozomiCouchStrip nozomi2 frustrated blush2 glasses2
        $ renpy.transition(longdissolve, layer="master")
        "After being confronted with her crumbling resolve, Nozomi strips off her other sock and works on her school blazer."
        n "{size=16}U-uggh...  t-this feels...{/size}"
        ks "Good, right? Resist it all you want, but you know what's going to happen."
        "It's a little comical, watching the struggle to resist her own wants play out on her face."
        n "{size=16}Urrrgh...{/size}"
        play sound fingersnap
        ks "Now take off your blazer, Nozomi. And your shirt."
        queue sound clothes
        show NozomiCouchStrip nozomi3 frustrated blush2 glasses2
        $ renpy.transition(longdissolve, layer="master")
        ks "Feeling so powerless to disobey. Keep going."
        queue sound clothes
        show NozomiCouchStrip nozomi4 pleading blush2 glasses2
        $ renpy.transition(longdissolve, layer="master")
        "Her shirt joins the rest of her clothes on the couch, before Nozomi starts to shake her head once again."
        n "{size=16}Aaah... I can't. C-can't stop myself.{/size}"
        "She holds her hands up in surrender. As if she's had enough."
        ks "Why would you, Nozomi? When it feels so good to do as I say?"
        "But I know you can do better than that, Nozomi."
        n "{size=16}B-but...{/size}"
        ks frown "T-Take off the skirt, Nozomi. Now."
        n "{size=16}Kyou, I...{/size}"
        play sound fingersnap
        ks frown "Take off your skirt."
        queue sound clothes
        hide NozomiCouchStrip
        show NozomiCouchStrip nozomi5
        $ renpy.transition(longdissolve, layer="master")
        "With a mouse-like squeak, Nozomi suddenly tips herself onto her back as her body seems to take a life of its own."
        n "{size=16}O-o-oh my gosh!{/size}"
        "She wriggles and squirms, pulling her skirt loose while her feet kick impotently in the air."
        "I can't help but chuckle at her distress. I mean, it looks like she's fighting a losing battle against herself, waged on the battleground of my living room couch."
        "Her panicked eyes look to me during her struggle, blushing darkly as she sees me taking it all in..."
        show NozomiCouchStrip nozomi6
        $ renpy.transition(longdissolve, layer="master")
        "And as the last of her uniform inevitably detatches from her body, she sits back on the couch and tries to keep what little dignity she has left."
        n "{size=16}S-s-seriously, that's enough! Please!{/size}"
        "Man, seeing her like this, so helpless and begging for mercy and... seeing so much of her, I'm made painfully aware of the state of my own body pushing against my pants."
        "But Nozomi told me not to do anything stupid..."
        ks frown "N-now get up from the couch. Stand right there."
        $persistent.nozomi_couch_strip_unlock = True
        # "I gotta say though, there's something about her expression and quiet terror this time that gives me pause."
        #He knows Nozomi told him not to go too far and picks up she might be genuinely afraid of being stripped naked. He knows better than to strip her for
        #the time being

        # "Her body seems to be in a constant state of trembling as she sheds her uniform, keeping her eyes closed the whole time while her cheeks flush deeply."
        scene bg k room eve
        show Nozomi side underwear sad_closed blush
        with blink
        "I... I can just enjoy her like this, I guess."
        n sad "{size=16}O-oh gosh, stop staring at me like that. It's embarrassing...{/size}" with dissolve
        "Ugh. Her saying that is making me blush harder. I still gotta remind her who's boss."
        "I'll assert myself by sitting down on the couch, right where she was sitting."
        "And then..."
        ks frown blush "I... g-give the orders around here, Nozomi. So now, I want you to kneel."
        "I thrust a fingertip towards the ground by my side."
        ks "R-right there."
        scene cg nozomi kneeling
        show NozomiKneeling underwear head_down_blush pleasure glasses_down kyou_down_uniform
        with blink
        "Nozomi groans slightly as she finds herself dropping meekly to the floor in front of me."
        show NozomiKneeling head_up_blush surprised glasses_up
        "Wasn't really expecting that to be so easy, and judging from the embarrassed look she gives me from down there, neither was she." with dissolve
        ks smirk "That's a good girl, Nozomi. Isn't it nicer now that you don't resist my commands?"
        show NozomiKneeling anxious
        n front pout "{size=16}I am resisting. Kyou... I am, I just...{/size}" with dissolve
        "As she cutely protests in near silence, I grin and wag a finger at her."
        ks "Kyou? That's \"Sir\" to you, Nozomi. Call me \"\Sir\" from now on."
        show NozomiKneeling surprised
        n "{size=16}Ah... {w=1.0}{nw}{/size}" with dissolve
        show NozomiKneeling anxious
        $ renpy.transition(dissolve, layer="master")
        extend "{size=16}Y-Yes, Sir...{/size}"
        "Man, what a fucking rush. She didn't resist that one either."
        show NozomiKneeling kyou_up_uniform
        "Reaching down to pet her, she looks up at me from the floor and... goddamn, my brain's having all kinds of thoughts right now." with dissolve
        "A cacophony of ideas ranging from vulgar to chaste, and everything in-between light up inside my mind, while Nozomi looks up at me with a need in her eyes."
        "But after what feels like an age, one thought wins out."
        show NozomiKneeling kyou_down_uniform
        "And having made up my mind, I turn my attention back to my beautifully-entranced captive." with dissolve
        ks smile "You know, I'm still thinking about the power I have over you. About all the things I could make you do."
        ks "And although you may try to resist, we both know you're far too weak-willed to hold out against me."
        ks "Even if you knew my commands would risk your life. Even if my orders would strip you of your very humanity..."
        ks "You'll be powerless to do anything but smile and obey, and accept my total control over your mind."
        ks "Doesn't that thought excite you, Nozomi?"
        show NozomiKneeling head_down_blush pleasure glasses_down
        $ renpy.transition(dissolve, layer="master")
        n "{size=16}It.. it does, Sir. It thrills me to my core to know I'm powerless before you.{/size}"
        ks "So then, Nozomi. With this ultimate power at my disposal I command you to..."


        # "And Nozomi inevitably succumbs, rising up off the couch and disrobing in front of him to Kyou's blushing satisfaction."
        # "But as Kyou knows, this isn't the first time she's stripped off like this."
        # "Maybe she earnestly tried to resist this time, but they both know she's willing to do this for him, even if it was just part of their roleplay before."
        # "So Kyou steels himself and takes things further."
        # "She wants to be dominated? Well then, he'll establish his dominance over her some more by commanding her to kneel at his feet."
        # show Nozomi:
        #     linear 1.5 ypos 1.2
        # "Nozomi obeys without any obvious resistance, blushing darkly as she does so."
        # "Kyou again teases Nozomi about how she didn't fight his command that time."
        # "And as she pouts, he then insists she start calling him \"Sir\" from now on (Maybe give a couple more choices of address here for player preference)"
        # "Once more Nozomi offers no pushback, moaning as she calls him such, which prompts Kyou to tease her again while blushing about his own growing arousal."
        # "Both seem to be enjoying the back and forth, but now things are starting to get dangerous."
        # "Kyou is both turned on and massively curious as to how far he can push it with Nozomi."
        # "And thinking back, on how little she's pushed back on any suggestion, on her stated fantasies and her perceived nervousness to follow through..."
        # "He has all manner of thoughts as to where to go from here. One playful, one entirely self-serving and one prompted by morbid curiosity..."
        # "So having made a decision, Kyou commands Nozomi to..."
        menu:
            "Make me a cheese omelette":
                # "((This would mostly proceed as with the original script, with Nozomi expressing her surprise at the command even as she finds herself obeying pretty easily.))"
                # "((The following script for this scene is still just the old one with no edits. Some new writing follows afterwards.))"
                n "{size=16}...{/size}"
                show NozomiKneeling head_up surprised glasses_up
                n "{size=16}H-Huh?!{/size}" with dissolve
                $persistent.nozomi_kneeling_trance1_unlock = True
                scene bg k room eve
                show Nozomi front underwear surprised at center:
                    ypos 1.2
                    linear 2.0 ypos 1.0
                with blink
                "I'm almost as surprised as Nozomi as I watch her rise up from the floor."
                show Nozomi side surprised at flip:
                    ypos 1.0
                "All this need I have, and I'm making her do something goofy?" with dissolve
                show Nozomi at flip:
                    linear 3.0 xpos 1.1
                play sound footsteps
                "But as I watch Nozomi obediently pad towards my kitchen, I think I'm doing the right thing by keeping things light for her."
                "... I'm sure I heard a soft chuckle from her as she disappears from view, followed shortly after by the sound of the fridge opening."
                "Anyway, something occurred to me while I was giving her my hammy villain speech."
                "I don't know how Nozomi feels in this moment, but it really does seem like I have this absolute power over her."
                "And if that's true, I... I do need to be careful with it."
                stop sound
                "Hurting Nozomi is the absolute last thing I want to do."
                "But while I'm thinking that, I also realize I'm missing the sight of an underwear-clad girl cooking for me..."
                "I gotta follow her!"
                scene cg nozomi kitchen:
                    ypos -1.0
                    linear 18.0 ypos -0.0
                with blink
                "Hanging around by the door so as not to get in her way, I simply watch with a grin as Nozomi works, navigating around my kitchen with relative ease to get her task done."
                ks smile "Do you often cook, Nozomi?"
                n "{size=16}Um, n-not often, Sir.{/size}"
                "She's clearly flustered by my staring but she doesn't comment on it, focused instead on her hypnosis-induced need for quiet obedience."
                n "{size=16}Mom does most of the cooking at home, but I help out sometimes.{/size}"
                ks smile "Okay. Be extra careful you don't hurt yourself against that stove, alright?"
                n "{size=16}Yes, Sir. I will.{/size}"
                $persistent.nozomi_kitchen_unlock = True
                scene bg blackscreen with dissolve
                "Before too long Nozomi has the omelette cooked and set on a plate, and I direct her to follow me with it."
                scene bg k room eve with dissolve
                ks smile "In here, Nozomi. Set it down on the table."
                show Nozomi front2 underwear blush
                with dissolve
                "I take a seat on the couch and Nozomi gently sets the food down on the table in front of me."
                # "I can tell she's a little flustered at my staring, but she doesn't say anything as she prepares the food, sets it on a plate and serves it up to me at the table." with dissolve
                n side sad "{size=16}H-Here you are, Sir.{/size}" with dissolve
                "I take a look at the cheese omelette and then at her, still grinning."
                ks smirk "I never said I wanted to eat it, Nozo. Besides, I'm not hungry."
                n frown "{size=16}What? Then why did you have me make it? Geez.{/size}" with dissolve
                ks "Sit down and eat it yourself."
                scene NozomiOmelette head_down sigh omelette1
                $ renpy.transition(blink, layer="master")
                n "{size=16}Ahhn...{/size}"
                "Damn, she's just getting turned on by any order I give her now."
                show NozomiOmelette pout
                n front pout "{size=16}But I'm not hungry either...{/size}" with dissolve
                "She says, as she tears a piece off and pops it into her mouth."
                n "{size=16}Mmth... Jerk.{/size}"
                ks smile "Tell me how you're really feeling, Nozomi."
                show NozomiOmelette head_up neutral
                "She takes a moment to swallow her food..." with dissolve
                show NozomiOmelette pout_closed
                "Then pushes another piece of omelette past her lips, seemingly to avoid answering me." with dissolve
                "It gets a laugh out of me as she pouts, knowing what's coming as I bring my hand beside her head."
                show Mindtrick awake fingersnap at center:
                    ypos 0.6
                with dissolve
                "I have ways of making you talk, Nozo."
                play sound fingersnap
                show Mindtrick entranced
                ks "Tell me how you're feeling right now, Nozomi." with dissolve
                hide Mindtrick
                show NozomiOmelette dazed
                n pout_left "{size=16}Ahn... I... I-I feel good, Sir.{/size}" with dissolve
                show NozomiOmelette surprised
                n sigh "{size=16}I know it's just a simple thing, but even making me do this and knowing I can't stop myself is so euphoric you wouldn't believe.{/size}" with dissolve
                show NozomiOmelette head_down shy_down omelette2
                "She stops to take another bite of the omelette; her compulsion to obey my latest order conflicting with the previous." with dissolve
                ks neutral "Yet you still look a bit tense to me."
                # n side sad_side "{size=16}Yes, Sir. That's what's complicated about it.{/size}" with dissolve
                show NozomiOmelette shy_up
                n side sad "{size=16}It's still embarrassing to admit all of this to you. And to myself.{/size}" with dissolve
                # n sad_closed "{size=16}But what's worse is I just... I can't stop thinking about the fact that I'm into things like this.{/size}" with dissolve
                # n "{size=16}I've been able to push those thoughts aside for so long, when I was just passively watching videos or reading stories and such.{/size}"
                # n front concerned "{size=16}Before I met you, in other words.{/size}"
                # n sleeptalk_concerned "{size=16}But
                # n sad_side "{size=16}What does it say about me that I'm excited by such frightening, horrible things?{/size}" with dissolve
                # n sad "{size=16}Is there something wrong with me?{/size}" with dissolve
                # "... Nozomi's weird, no doubt about it. But she doesn't deserve to be hurting like this."
                # ks sigh "Nozomi... Look."
                # "I have to say something."
                # ks neutral "I guess... Sure, it's not normal to want the kind of stuff that you want. And yeah, it's kinda messed up on the face of it."
                # n front concerned "{size=16}Yeah...{/size}"
                # ks frown "But so what?"

                #What does it say about me?
                ks smile blush "Nozomi, there's no reason to feel embarrassed about feeling this way. You like what you like."
                show NozomiOmelette shy_down
                ks "Also, no one else needs to know if you don't want to say anything. We had a deal." with dissolve
                ks "So don't feel ashamed about who you are. You're safe here, with someone who wants you to be happy."
                show NozomiOmelette shy_up
                ks "Let yourself enjoy this." with dissolve
                show NozomiOmelette head_up smile
                "Nozomi gives me a smile from across the table and nods, still half-chewing as she responds in her cute whispered voice." with dissolve
                n "{size=16}Thank you, Sir. That does actually make me feel better.{/size}"
                "I smile back at her as we enjoy a moment of shared bliss."
                "And then with a grin, I'm the one to break the silence for a change."
                ks smirk "Now be a good girl and finish your omelette, and wash everything up when you're done."
                show NozomiOmelette teasing
                "She pokes her tongue out at me, then takes another bite of her food." with dissolve
                $persistent.nozomi_omelette_unlock = True
                scene bg k room eve
                show Nozomi front2 smile
                with blink
                "Soon after she was done in the kitchen I had her get dressed and ready to leave."
                "Not that I wanted to, but dad's going to be home soon, and I don't think either of us want to explain this to him of all people."
                ks smile "You got everything?"
                n "{size=16}Yes, Sir. Are we doing this again tomorrow?{/size}"
                "I respond with a wink and a knowing smirk."
                ks smirk "Oh, you WILL be coming back here tomorrow. Do I make myself clear?"
                show Nozomi chuckle blush
                "She replies with a muted giggle." with dissolve
                n "{size=16}Yes, Sir. I must obey~{/size}"
                # "Maybe some other cute dominant actions could follow in-between Kyou and Nozomi talking about kink."
                # "About how nice it is to do something consensual non-consenty while still being assured of one's safety etc etc."
                stop music fadeout 5.0
                jump Day12_Con_Kyou_Nozomi_Trance
            "Become my girlfriend":
                "I mean... it's been obvious from the start, hasn't it?"
                show NozomiKneeling head_up_blush anxious glasses_up
                "Nozomi can be coy all she wants, but everything we've been doing together has led us to this point." with dissolve
                n "{size=16}Command me to... what, Sir?{/size}"
                "And what better time to confront it than now?"
                ks "Be my girlfriend."
                show NozomiKneeling surprised
                n "{size=16}I... n-no...{/size}" with dissolve
                "She'll refuse at first. Of course she'll refuse."
                "But..."
                ks "Nozomi, I know you're embarrassed about all this stuff, and I get that it's scary. Relationships are scary, right?"
                show NozomiKneeling anxious
                "She responds with a meek shaking of her head while she whispers in protest." with dissolve
                n "{size=16}P-please, Sir. We've talked about this. I can't...{/size}"
                # "For Kyou, it's obvious that they should be a true couple."
                # "Nozomi's said herself more than once that she trusts Kyou, and they've done all this kinky stuff together. \"More than friends\" stuff..."
                # "Kyou knows she's still embarrassed about her kink and her growing relationship with Kyou, but he \"knows\" this is where they're headed."
                # "And Nozomi can't move on until she accepts her feelings for Kyou and the relationship they're in."
                # "Nozomi's initial resistance to his command doesn't surprise Kyou; knowing how stubborn she is about this." with dissolve
                show NozomiKneeling kyou_click_uniform entranced
                play sound fingersnap
                ks "Agree to be my girlfriend, Nozomi." with dissolve
                show NozomiKneeling head_down pleasure glasses_down
                n "{size=16}... No.{/size}" with dissolve
                ks "You want someone you can trust with your deepest, darkest desires. Someone you can feel completely safe and happy around."
                ks "So I know, Nozomi. And I think you know it too. You're not looking for just anyone to have this kind of fun with."
                show NozomiKneeling kyou_click_uniform head_up glasses_up entranced
                play sound fingersnap
                ks "You want a boyfriend." with dissolve
                n "{size=16}A-ah... {/size}"
                ks "And who other than me knows and accepts and loves everything that you are?"
                play sound fingersnap
                # ks "And you want that boyfriend to be me."
                ks "So be my girlfriend, Nozomi."
                $persistent.nozomi_kneeling_trance1_unlock = True
                $persistent.nozomi_kneeling_trance2_unlock = True
                scene bg k room eve
                show Nozomi front underwear irritated at center:
                    ypos 1.5
                    linear 2.0 ypos 1.0
                with blink
                "With a moan, Nozomi shakily manages to haul herself up from the floor..."
                "She's still resisting, huh?"
                ks smirk "You can't hold out forever, Nozomi. You know that."
                stop music fadeout 4.0
                "Holding my hand out, I'm about to snap my fingers once more..."
                show Nozomi:
                    ypos 1.0
                show Nozomi front2 angry
                "Only for Nozomi to suddenly reach out and grab my hand!" with vpunch
                ks surprised "Nozo?!"
                play music Measured
                n "{size=16}K-Kyou... stop...{/size}"
                "She hisses at me with quiet menace, and as she struggles to keep me from triggering her again, I have to wonder if she really means this..."
                n irritated "{size=16}J-just stop!{/size}" with dissolve
                "But then I remind myself: This is the kind of stuff she fantasizes about, isn't it?"
                "Not to mention, it hasn't escaped my notice that she's still whispering. Still holding true to the mental conditioning I've placed on her."
                "So how genuine could she be about resisting this?"
                menu:
                    "Try again":
                        "Her fingers are really digging hard into my hand. She's making a fight of it this time, no doubt about it."
                        ks frown "N-Nozomi, you're... hurting me!"
                        # "Nozomi is still clutching his hand tightly, trying to stop him from clicking his fingers."
                        "If I was any good at snapping my fingers with my other hand, I could end this right now."
                        n determined "{size=16}U-ugh, I s-said that's enough Kyou!{/size}" with dissolve
                        ks "No! I won't let you be afraid anymore."
                        n angry "{size=16}I need you to stop!{/size}" with dissolve
                        "Wait, I don't even need to snap my fingers do I?"
                        # "And Kyou isn't so good at clicking with his other hand, but it doesn't matter."
                        show Nozomi shocked
                        if gesture == "hand":
                            "I just need to wave my free hand across her face." with dissolve
                            show Mindtrick awake wave_sleeve at center:
                                ypos 0.6
                            # "Instead, Kyou waves his free hand across Nozomi's face, and despite her protests she immediately falls silent with a blank expression as he speaks." with dissolve
                        elif gesture == "forehead":
                            "I just need to poke her forehead with my free hand." with dissolve
                            show Mindtrick awake poke_sleeve at center:
                                ypos 0.6
                            # "Instead, Kyou uses his free hand to poke Nozomi's forehead, and despite her protests she immediately falls silent with a blank expression as he speaks." with dissolve
                        "Like so..." with dissolve
                        stop music fadeout 10.0
                        n "{size=16}Kyou, n-{/size}{nw}"
                        show Nozomi entranced_neutral noblush
                        show Mindtrick entranced
                        $ renpy.transition(longdissolve, layer="master")
                        extend "{size=16}...{/size}"
                        ks neutral "You want to become my girlfriend."
                        if hypnorepeat == True:
                            "And there it is. Her eyes glaze over and her grip on my hand fades as her lips quiver a moment before intoning gently:"
                            n "{size=16}I want to become your girlfriend...{/size}"
                        else:
                            "And there it is. Her eyes glaze over and her grip on my hand fades as she processes what I just said."
                        hide Mindtrick with dissolve
                        "I have to admit, the more she insisted I stop the more I started to doubt my instincts..."
                        # "This time, when he tells her to agree to be his girlfriend, the suggestion takes immediately."
                        show Nozomi smile blush
                        $ renpy.transition(longdissolve, layer="master")
                        "But as I notice the shy smile starting to form on her lips it becomes clear that I've finally gotten through to her."
                        play music Warm_Romantic
                        n "{size=16}I... u-um...{/size}"
                        ks smile blush "Be my girlfriend, Nozomi."
                        n loving "{size=16}O-okay.{/size}" with dissolve
                        # "Nozomi smiles as she comes out of her blank state." with dissolve
                        scene bg blackscreen with longdissolve
                        "It's what I've imagined hearing from her lips so many times. But now, as I gently pull her in for an embrace, and as I caress the small of her bare back..."
                        scene NozomiKiss kissing with longdissolve
                        "As I close my lips with hers and feel her tongue play against mine I know I don't have to imagine any more."
                        "This is real. What we have here... it's real."
                        show NozomiKiss standing sleepy glasses
                        $ renpy.transition(longdissolve, layer="master")
                        "Nozomi really has let me into her life and showed me a side to her that I never knew existed. A side that she's never shown to anyone else."
                        "And this naughty, perverted side to her... it's beautiful. SHE is beautiful."
                        k "I love you, Nozomi. I really do."
                        show NozomiKiss standing smile glasses
                        n loving "{size=16}And I love you too, Sir~ {font=DejaVuSans.ttf}♥{/font}{/size}" with dissolve
                        hide NozomiKiss
                        show NozomiKiss kissing
                        "We lean in to kiss once more, and Nozomi giggles in that quiet understated way she's been doing since..." with dissolve
                        show NozomiKiss standing sleepysmile glasses
                        "Oh right, I almost forgot in the moment. She might be my girlfriend now, but we're still in the middle of something." with dissolve
                        k "A-and doesn't it feel good to obey me, Nozomi? Doesn't it feel better to let your futile resistance slip away and accept my dominance over your beautiful mind?"
                        #Kyou teases her with his hypnotic dominance over her and Nozomi happily goes along with it all the way to his bedroom...
                        show NozomiKiss smile
                        n chuckle "{size=16}Ehehe... i-it does, Sir. I don't think I can resist you anymore~ {font=DejaVuSans.ttf}♥{/font}{/size}" with dissolve
                        "My hand moves to stroke the back of her head and play with some of that gorgeous hair of hers while I savour this moment..."
                        stop music fadeout 10.0
                        "... Although the growing need in my pants is starting to make it difficult."
                        show NozomiKiss sleepy
                        queue music Night_Road
                        "To say nothing of how Nozomi must be feeling right now, if the crimson shade of her cheeks is anything to go by..." with dissolve
                        k "Th-th-there's no resisting me, Nozomi. I want you to follow me to my... my bedroom now, and you're going to be a good girl and obey without question, aren't you."
                        $persistent.nozomi_kiss_unlock = True
                        show bg blackscreen
                        $ renpy.transition(longdissolve, layer="master")
                        "I slide my hand down her warm neck and arm to meet her hand, and she gently closes her fingers around it as I start to tug her forward."
                        #"And as her skirt joins the rest of her uniform on the floor of my room, I'm made painfully aware of the state of my own body pushing against my pants."
                        "That smile... Damn, she looks so blissfully happy right now. Like all her fantasies have just been fully realized."
                        n "{size=16}Yes, Sir... obeying feels so good...{/size}"
                        # "So there, her resistance was clearly all for show, and now Kyou's lifted her of her anxiety about starting a proper relationship with him. All is good."
                        # "They'll probably declare their love for each other, and keen to keep their kinky hypno session going, Kyou shyly orders Nozomi to follow him to his bedroom..."
                        # Knowing she's into this kinky hypno play emboldens Kyou to go further than he thought he would, treating her more possessively and taking things in
                        # a more sexual direction against Nozomi's initial wish
                        "And I'll make sure obeying me always feels this good, Nozomi."
                        stop music fadeout 5.0
                        "That's a promise..."
                        pause 2.0
                        $ending = "dark fantasy"
                        jump Epilogue_Con_Kyou_Nozomi
                        # "... And of course now we fade to black here and timeskip to an epilogue, for uh... obvious reasons given the general tone of the game."
                        # "The epilogue itself would have shades of the Delusion ending, where Kyou also has Nozomi hypnotized into being his girlfriend."
                        # "Only in this version, Kyou probably doesn't have the shock realization that he does there."
                        # "After all, he's sure Nozomi wanted it this way, where he's controlling her via hypnosis and she's living out her fantasy with him."
                        # "But like in Delusion, he's finding out how unsatisfying it is to have a girlfriend who can't think for herself."
                        # "Only he's still going along with it because this is what he wanted too, wasn't it? Even if the spark is gone..."
                    "Stop":
                        "She's... no, this isn't an act this time. She really isn't just putting up a show of resistance."
                        show Nozomi determined
                        "This is different." with dissolve
                        n "{size=16}S-stop!{/size}"
                        "I mean, fuck, she was telling me over and over: She didn't want to date anybody."
                        stop music fadeout 10.0
                        ks sigh "Okay..."
                        show Nozomi concerned
                        "No matter how close I get to her, no matter how much of herself she lets me see..." with dissolve
                        ks "You don't have to be my girlfriend, I'm sorry."
                        "She'll never want to be with me."
                        n side sad_closed "{size=16}I think we need to stop, Sir.{/size}" with dissolve
                        ks "Yeah..."
                        # "Kyou can't get out of his head the fact that Nozomi said straight up last week, before they got too involved, that she was not interested in dating."
                        # "While the two of them have flirted with this total control hypno power play, Kyou realizes there are some lines he shouldn't cross..."
                        # "And much as he hates to admit, this is probably one of them for Nozomi. So he relents and apologizes to her." with dissolve
                        # "Nozomi breathes a sigh of relief and appreciates him stopping, and would also like to stop the play they've been doing."
                        scene cg k room eve
                        show NozomiHypno standing sad
                        with longblink
                        play music Diary
                        "So with that I told her to get dressed and spent the next several minutes putting her back into trance and removing the night's suggestions from her mind."
                        ks "Hey. Take your time waking up; everything's okay."
                        "Nozomi drags her head wearily from side to side as she lets out a pained sigh."
                        n "N-no, Kyou. Everything's... everything's not okay."
                        ks sigh "Sorry. Guess I got a little carried away, huh?"
                        show NozomiHypno folded neutral
                        n "What on earth possessed you to make a move on me like that?" with dissolve
                        "Man, what do I even say right now?"
                        ks "I... I mean, you said to have fun with it, right? I thought..."
                        n "I also said not to try anything stupid."
                        ks neutral "That was pretty vague don't you think?"
                        show NozomiHypno folded annoyed
                        n "Kyou, I told you I wasn't interested in a relationship. I told you so many times." with dissolve
                        n "There's no excuse for what you did."
                        ks sigh "I-It's just... are you really sure you're not just scared?"
                        show NozomiHypno stern
                        n "I'm not scared of relationships, Kyou! I don't know how I can make it any clearer to you. Or- or to mom or to anyone else!" with dissolve
                        n "Why is it no one ever listens to me?"
                        # show NozomiHypno sad
                        # n "... And why was it so hard to say no?" with dissolve
                        ks frown "But it looked like you were seriously considering one with me just now."
                        n "You mean while I was hypnotized and you were pressuring me."
                        ks "We know you can't make someone do things they don't want under hypnosis, right? No matter how much you want it to be literally mind control?"
                        ks "It just doesn't work that way."
                        ks "So you really don't think that you... o-on some level-{w=1.0}{nw}"
                        show NozomiHypno angry
                        n "{cps=20}Kyou, I don't want to be your {/cps}{nw}" with dissolve
                        extend "FUCKING girlfriend!" with vpunch
                        n "Is {nw}"
                        extend "THAT clear enough for you?" with vpunch
                        "Fuck. I can't stand seeing her angry with me, but was it really wrong to doubt her about this?"
                        show NozomiHypno stern
                        n "It doesn't matter if I'm supposed to be aware of what you're doing at all times. I don't care about the hidden observer effect." with dissolve
                        show NozomiHypno stern_closed
                        n "Everything we've been doing, it... m-maybe it was kinda nuts, but it was still supposed to be safe." with dissolve
                        n "You never should've put me in that position, Kyou."
                        show NozomiHypno sad
                        n "And after this... I-I'm not sure it's safe anymore." with dissolve
                        # n "It feels more like those creepy stories I read about abusive hypnotists who hang out in online chatrooms, and..." with dissolve
                        # n "A-and gosh, I never thought they could be real until now."
                        ks sigh "Nozomi..."
                        scene bg k room eve
                        show Nozomi front irritated at center:
                            ypos 1.5
                            linear 2.0 ypos 1.0
                        with blink
                        "Without warning Nozomi bolts up from the couch, clutching her hands around her stomach as she starts to pace towards my front door."
                        show Nozomi:
                            ypos 1.0
                        n "It's over, Kyou. No more."
                        ks surprised "Nozomi, wait! Come on!"
                        show Nozomi:
                            linear 1.0 xpos 0.8
                        "My words do nothing to stop her, as she slips her shoes back on in a somewhat clumsy, even panicked rush."
                        show Nozomi side sad_side at flip:
                            xpos 0.8
                        ks angry "Nozomi!" with dissolve
                        play sound dooropen
                        hide Nozomi with dissolve
                        "Rather than stop her, my calling out only makes her panic more obvious as she flings the door open and stumbles outside."
                        "I go to the door, but no further as I watch her leave."
                        "Dammit, Nozo. I just wanted to make you happy. I thought you'd want this."
                        "Why did it turn out like this?"
                        jump Credits
            "Become mindless for me":
                "I can't resist. I have to know how far Nozomi's willing to go to realize her fantasy to be powerless."
                "I've seen just how excellent she is at being hypnotized and following instructions. But surely everyone has a limit."
                "And in the context of this hypnotic power play of ours, there seems no better time for us to find out."
                ks "Become blank for me, Nozomi."
                show NozomiKneeling head_up surprised glasses_up
                n "{size=16}H-Huh?!{/size}" with dissolve
                "Nozomi squeaks her dissent quietly, but I think she's just confused about what I want her to do."
                "After all, this is another thing she's pretty much done for me before."
                ks smirk "Nozomi, you will empty your mind of every thought in that pretty little head of yours."
                n "{size=16}I... i-i...{/size}"
                show NozomiKneeling underwear head_up surprised glasses_up kyou_click_uniform
                "Ignoring her meek protest, I bring my hand in front of her face once more and snap my fingers again." with dissolve
                play sound fingersnap
                ks "Stay kneeling for me and clear all the thoughts from your head."
                show NozomiKneeling falling
                n "{size=16}A... a-all the thoughts.{/size}" with dissolve
                play sound fingersnap
                ks "Completely mindless now, Nozomi... No thoughts at all."
                show NozomiKneeling head_down blank glasses_down kyou_down_uniform
                $ renpy.transition(longdissolve, layer="master")
                "I watch as her head slumps forward, and I can see her expression go completely slack while a sliver of drool escapes her lips to drop on the floor by her hands."
                ks "Good girl, Nozomi. Completely obedient. Completely mindless. Powerless to do anything but accept my total control over your mind."
                "After I'm done filling her imagination, I sit there quietly and continue to watch her still form."
                "The more I watch her, the more I can believe she truly is as helpless as she looks."
                "And the more I wonder if I can take that helplessness even further."
                ks "So mindless, Nozomi, that you won't even think to respond to outside stimulation."
                show NozomiKneeling nokyou
                "Crouching down beside her now, still watching over her unmoving, slackened face, I have to see how fully she can take to such a command." with dissolve
                "Could she possibly be able to ignore the very real stimulation of her body to such an extent?"
                "I begin by tentatively poking her cheek. First gently, then much more firmly."
                "Besides pushing her skin aside, it accomplishes nothing."
                "Maybe if I blew in her ear?"
                "Nope, the only reaction I get is from myself as I chuckle at the experience."
                if hypno4 == "tickle":
                    "But surely she'll be forced to react if I were to suddenly reach over to her foot and start teasing the sole with my fingertips."
                    n "..."
                    "Wow. Okay. I know tickling the sole of her foot like this should have her squealing."
                    "But I soon stop my efforts when it seems I may as well be trying to tickle the sofa."
                elif hypno4 == "spank":
                    play sound slap
                    "But surely she'll be forced to react if I were to suddenly reach over and slap my hand down harshly on her butt." with vpunch
                    n "..."
                    "Wow. Okay. But if I went in harder..."
                    play sound slap
                    n "..." with vpunch
                    "All I manage to do is make my hand sting. She didn't even flinch, let alone make any kind of noise."
                "That's seriously impressive, Nozomi."
                "So she refuses to react in any way, just as I commanded her."
                "How would she respond if I commanded her again?"
                ks neutral "Stand up, Nozomi."
                $persistent.nozomi_kneeling_trance1_unlock = True
                $persistent.nozomi_kneeling_trance2_unlock = True
                scene bg k room eve
                show Nozomi front underwear entranced_neutral at center:
                    ypos 1.5
                    linear 2.3 ypos 1.0
                with blink
                "I'm not left wondering, as Nozomi climbs back to her feet the moment my command leaves my lips."
                show Nozomi:
                    ypos 1.0
                "What else would she do if I told her?"
                ks frown blush "Take... t-t-... take off your underwear, Nozomi."
                play sound clothes
                "There's not a whisper of complaint, nor any kind of tension in her body as she reaches immediately to pull her undergarments away..."
                show Nozomi nude:
                    ypos 1.0
                "Nothing but quiet, mindless obedience." with dissolve
                # "... And pulls off her underwear without a word. It sure seems that making Nozomi rid herself of thoughts also ended any resistance." with dissolve                
                "It sure does seem that commanding Nozomi to rid herself of all thoughts also wiped out any notion of resistance."
                scene NozomiZombieWalk nozomi1 neutral:
                    ypos -1.0
                    linear 20.0 ypos -0.0
                with blink
                "And this time there's none of her former embarrassment as my eyes can't help but take in every inch of her."
                "She's... She's as beautiful as I imagined her to be."
                "I don't know how long I'm standing there before I'm able to clear my throat and get some more words out of me."
                ks blush "S-so... what are you feeling right now, Nozomi? Anything?"
                n "..."
                ks "Nothing, huh?"
                ks "I... I-I guess that makes sense for someone with no thoughts, huh."
                n "..."
                "Okay... So here's the question burning in my mind now, distracted only by what's welling up in my pants from looking over a perfectly naked Nozomi:"
                "Has she attained true mindlessness? Or is something still in there, waiting to intervene if her comfort or safety are seriously threatened?"
                "That whole \"Hidden observer effect\" that we were talking about. Because what a time to truly test that theory."
                "Maybe Nozomi's content to let me take things as far as this. She did say she trusted me, after all."
                "But what if I introduced just a little danger? What then?"
                "If I ordered her to do something that would threaten her life if followed through... Would she?"
                menu:
                    "I'll order her to stop breathing":
                        ks "Nozomi... Stop breathing. I order you to stop breathing."
                        stop music fadeout 15.0
                        "Fascinating... I'm sure she'll obey, at least initially."
                        "And as I hold a finger under her nose to check her breathing, I wonder..."
                        "How long will she last before she finally allows herself to snap out of this fantasy and let reality take over?"
                        "Or will it be her self-preservation instinct that has to do it for her? Is her mind truly that disciplined?"
                        ks "Aren't you going to breathe, Nozomi?"
                        "Immediately her barely-audible reply slips past her idle lips."
                        n "{size=14}No, Sir...{/size}"
                        ks "And why not?"
                        n "{size=12}Because you told me not to, Sir.{/size}"
                        "It must've taken what little breath she had left in her lungs to answer me, but she remains as calm and blank-faced as ever."
                        "Just... wow, she looks completely unconcerned that she must be suffocating herself by now."
                        "How long can someone hold their {nw}"
                        show NozomiZombieWalk -nozomi1 -neutral
                        # show Nozomi sleepy:
                        #     linear 0.75 rotate 90 yanchor 0.2 xanchor 0.0
                        $ renpy.transition(dissolve, layer="master")
                        play sound sitting
                        extend "breath for anyway?" with vpunch
                        stop music
                        scene NozomiCaptured base4 sleeptalk
                        $ renpy.transition(dissolve, layer="master")
                        "..."
                        ks surprised noblush "Nozomi?"
                        n "..."
                        "Fuck."
                        ks "Nozomi... N-Nozomi breathe, okay? I command you to breathe!"
                        play music Sorrow
                        n "..."
                        "FUCK!"
                        ks angry "Nozomi, I need you to breathe!{w=0.8}{nw}"
                        extend " COME ON!" with vpunch
                        "As I shake her lifeless-looking body, I catch sight of her chest rising slightly and- oh, thank fuck she's breathing again."
                        "At least she can't obey my commands while she's unconscious..."
                        "But damn, that gave me a fright. Why'd I have to push her like that?"
                        "I didn't need to go this far with her!"
                        "... And what's going to happen when she comes to? When I have to let her out of here?"
                        "She's going to remember how I nearly fucking killed her."
                        "What... what do I do?"
                        menu:
                            "I can't let her remember any of this":
                                # scene bg k room eve
                                # show Nozomi front nude sleepy at center:
                                #     ypos 1.8 #rotate 0 yanchor 0.2 xanchor 0.0
                                #     linear 1.5 ypos 1.2
                                # with blink
                                show NozomiCaptured entranced_dazed
                                $ renpy.transition(longdissolve, layer="master")
                                n "{size=16}Uhh...{/size}"
                                ks frown "Nozomi, listen to me; you need to breathe now."
                                "She draws a long shuddered breath, as if realizing her need for air for the first time."
                                stop music fadeout 5.0
                                ks "That's good, Nozomi. Breathe normally now."
                                "I give her a few moments to get her breath back while I decide that what I'm about to do is for the best."
                                $hypno3 = hypno3.capitalize()
                                ks "Alright now, Nozomi. [hypno3]."
                                show NozomiCaptured sleep
                                play music Flow fadein 5.0
                                "Even after all this she still can't shake any of her conditioning. Not even the slightest bit." with dissolve
                                "It's amazing, but... Fuck, I can't put what happened out of my head."
                                "Nothing else matters; I need to fix this."
                                ks "Going deeper... back into a deep relaxing trance."
                                ks "Now, Nozomi, I want you to accept some that some of the facts of this evening are different to how you currently remember them."
                                ks "You remember that I told you to hold your breath until you passed out unconscious, but in fact it never occurred."
                                ks "And as you accept this fact, you will find you can no longer remember that such a thing occurred."
                                ks "After all, why would you remember something that didn't happen?"
                                show NozomiCaptured sleeptalk
                                n "{size=16}I would not...{/size}" with dissolve
                                show NozomiCaptured sleep
                                ks "No, Nozomi. You wouldn't. Now, you will wake on three." with dissolve
                                stop music fadeout 5.0
                                ks "One... two... three."
                                scene bg k room eve
                                show Nozomi front uniform glasses concerned
                                with blink
                                n "{size=16}We still have a little time, Sir. Are you sure you want to stop so soon?{/size}"
                                "After confirming her memory loss I had her change back into her clothes immediately and called an end to things today."
                                ks sigh "Yeah... Sorry, Nozomi, I guess I'm not in the right frame of mind for it."
                                n side sad "{size=16}Oh. Did I make you uncomfortable?{/size}" with dissolve
                                ks concerned "Uhh, well..."
                                n front sleeptalk_concerned blush "{size=16}I really was pushing for too much, wasn't I? I'm sorry I made this weird.{/size}" with dissolve
                                ks "No, no it's fine I just..."
                                show Nozomi concerned
                                "I trail off. What am I supposed to tell her? That it's MY fault? Then she'll ask why..." with dissolve
                                n "{size=16}Alright then, Kyou. See you tomorrow?{/size}"
                                $kface = "neutral"
                                ks neutral "Yeah. See you tomorrow."
                                $ending = "awkward"
                                jump Epilogue_Con_Kyou_Nozomi # Skip straight to the epilogue and play the "awkward" short ending
                            "I have to take responsibility":
                                # scene bg k room eve
                                # show Nozomi front nude sleepy at center:
                                #     ypos 1.8 #rotate 0 yanchor 0.2 xanchor 0.0
                                #     linear 1.5 ypos 1.2
                                # with blink
                                show NozomiCaptured entranced_dazed
                                $ renpy.transition(longdissolve, layer="master")
                                n "{size=16}Uhh...{/size}"
                                ks frown "Nozomi, listen to me; you need to breathe now."
                                "She draws a long shuddered breath, as if realizing her need for air for the first time."
                                ks "That's... that's great, Nozomi... Now let's get you dressed."
                                $n = Character("[nozomi_name]", image = "NozomiHypno", who_color = "#93624B"); light_y =0.28
                                scene cg k room eve
                                show NozomiHypno standing neutral
                                with blink
                                "I had Nozomi dressed and sat down on the couch."
                                "She looks so peaceful, as if lost in a daydream. Unable to feel or express what she should at a time like this."
                                $hypno3 = hypno3.capitalize()
                                ks "[hypno3], Nozomi."
                                show NozomiHypno drooping sleep
                                stop music fadeout 15.0
                                "But it's time I set her free." with dissolve
                                ks "That's right, Nozomi. Back in this nice, deep relaxation. Ready to listen so carefully."
                                ks "Because Nozomi, when you wake you will no longer be influenced by any of the suggestions I have given you at any time."
                                ks "You can feel each and every one of them leave your mind, leaving you free to think and act as you always have."
                                ks "Do you understand, Nozomi?"
                                ncg sleeptalk "I... understand..." with dissolve
                                show NozomiHypno sleep
                                ks concerned "That's good, Nozomi. Now you're waking up in three..." with dissolve
                                ks "One, beginning to rouse yourself..."
                                show NozomiHypno sleepy
                                play music Flow fadein 10.0
                                ks "Two, feeling your eyelids flicker open..." with dissolve
                                ks "And three, wide awake."
                                ncg standing drowsy "..." with dissolve
                                ks "Okay so, Nozomi, given what just happened I thought I'd better-{w=0.8}{nw}"
                                # play music Sorrow fadein 2.0
                                ncg "Kyou, you..."
                                ncg surprised "Y-you... oh my god..." with dissolve
                                ks "Nozomi, please, I'm sorry-{w=0.8}{nw}"
                                ncg "O- OH MY GOD!" with vpunch
                                hide NozomiHypno
                                play sound dooropen
                                "And just like that, she bolts for the door." with dissolve
                                play sound doorclose
                                "... I don't try to stop her."
                                $ending = "frightened"
                                jump Epilogue_Con_Kyou_Nozomi

                    "I need to put a stop to this":
                        stop music fadeout 5.0
                        "... \"Something that would threaten her life\"?"
                        "Why the fuck would I ever go that far? Why would Nozomi?"
                        play music Night_Road
                        ks "Nozomi..."
                        "I can't endanger her. I could never..."
                        ks "Stretch your arms up in front of you, and keep your hands limp."
                        show NozomiZombieWalk nozomi2:
                            zoom 0.5
                        "No, I'll just show her how far she's gone in the pursuit of her darkest fantasy." with longdissolve
                        ks neutral "Now, you will walk around my coffee table. Slowly."
                        play sound footsteps loop
                        "How total my control over her has become."
                        ks "Keep going. Over and over. Don't stop."
                        show NozomiZombieWalk nozomi_right -neutral
                        $ renpy.transition(longdissolve, layer="master")
                        n "..."
                        ks "And while you're doing so, I want you to repeat after me:"
                        "Maybe then we'll... \"get it out of our systems\"."
                        show NozomiZombieWalk nozomi_left neutral_left
                        $ renpy.transition(longdissolve, layer="master")
                        ks "\"I am Kyou's puppet.\""
                        show NozomiZombieWalk talk_left
                        $ renpy.transition(dissolve, layer="master")
                        n "{size=16}I am Kyou's puppet.{/size}"
                        ks "\"My mind is dominated.\""
                        show NozomiZombieWalk nozomi_right -talk_left
                        $ renpy.transition(longdissolve, layer="master")
                        n "{size=16}My mind is dominated.{/size}"
                        ks "My mind is controlled."
                        n "{size=16}My mind is controlled.{/size}"
                        show NozomiZombieWalk nozomi_left neutral_left
                        $ renpy.transition(longdissolve, layer="master")
                        ks "Keep saying it. Louder now."
                        show NozomiZombieWalk talk_left
                        $ renpy.transition(dissolve, layer="master")
                        n "I am Kyou's puppet..."
                        "Is this really what you wanted, Nozomi?"
                        show NozomiZombieWalk nozomi_right -talk_left
                        $ renpy.transition(longdissolve, layer="master")
                        n "My mind is dominated..."
                        "You don't want to date me, don't even want to be seen with me..."
                        show NozomiZombieWalk nozomi_left talk_left
                        $ renpy.transition(longdissolve, layer="master")
                        n "My mind is controlled..."
                        "And yet, you still want me to see you like this?"
                        show NozomiZombieWalk nozomi_right -talk_left
                        $ renpy.transition(longdissolve, layer="master")
                        n "I am Kyou's puppet... My mind is dominated... My mind is controlled..."
                        ks "Stop repeating yourself now. Just keep walking and listen to me."
                        show NozomiZombieWalk nozomi_left neutral_left
                        $ renpy.transition(longdissolve, layer="master")
                        n entranced_neutral "..."
                        "Is there truly no limit to what you allow me to do to you?"
                        ks "I'm going to make you love me, Nozomi. For real."
                        show NozomiZombieWalk nozomi_right -neutral_left
                        $ renpy.transition(longdissolve, layer="master")
                        n "..."
                        "Do you really have no inner voice at all?"
                        ks frown "Y-yeah. I'll make you want to be my girlfriend, and then I'm gonna take you up to my room and we're gonna do it."
                        n "..."
                        "Where's your \"hidden observer\" to protect you now?"
                        show NozomiZombieWalk nozomi_left neutral_left
                        $ renpy.transition(longdissolve, layer="master")
                        ks "Did you hear me, Nozomi?"
                        show NozomiZombieWalk nozomi_left talk_left
                        $ renpy.transition(dissolve, layer="master")
                        n entranced_talk "Yes..."                        
                        ks "And do you have a problem with what I just said?" with dissolve
                        show NozomiZombieWalk nozomi_right -talk_left
                        $ renpy.transition(longdissolve, layer="master")
                        n entranced_talk "No..."
                        "I just stand there in stunned silence while Nozomi continues to walk in her circular motion. Like a mindless zombie with no purpose."
                        "Before finally, I steel myself and do what I think I need to do for her sake."
                        show NozomiZombieWalk nozomi_left neutral_left
                        $ renpy.transition(longdissolve, layer="master")
                        ks "Come stand next to me, Nozomi."                        
                        stop sound
                        show NozomiZombieWalk nozomi2 neutral
                        $ renpy.transition(longdissolve, layer="master")
                        "As Nozomi obediently returns to my side, I'm feeling every temptation to make those words I uttered to her just now her reality."
                        ks "Lower your arms. Now lie down on your back."
                        $ persistent.nozomi_zombie_walk_unlock = True
                        scene NozomiCaptured base4 entranced with blink
                        "Because surely, in this moment, the only one could stop me... is me."
                        ks "Now... time to dream."
                        show NozomiCaptured sleep
                        "I have to stop this. I need us both to... to stop this." with dissolve
                        ks -blush "That's right, Nozomi. Return to this nice, deep state of relaxation, and listen to my every word carefully."
                        ks "Because Nozomi, when you wake you will no longer be influenced by any of the suggestions I made to you tonight, or at any time in the past."
                        ks "Let every single one of them drop away from your mind. But remember everything that happened while you were here in my home. I want you to remember it all."
                        ks "Do you understand, Nozomi?"
                        show NozomiCaptured sleeptalk
                        n sleeptalk "Yes... I understand..." with dissolve
                        show NozomiCaptured sleep
                        ks "That's... Yeah, that's good, Nozomi. So, waking up on three..." with dissolve
                        ks "One, two... beginning to stir, letting your eyes open wide and..."
                        "I let out a shuddered sigh, my breath catching as I dread the consequence of what I'm about to do..."
                        ks "T-Three! Awaken now, Nozomi."
                        show NozomiCaptured dazed
                        n sleepy "..." with dissolve
                        "Nozomi's eyes slowly come back into focus as I watch the emotions play out on her face."
                        show NozomiCaptured awe blush
                        "Her mouth starts to hang open in shocked silence, with the memories of her experience surely flashing before her now fully-conscious mind." with dissolve
                        show NozomiCaptured scared
                        "Then her lower lip begins to tremble as her eyes dart to register me, standing over her vulnerable, now quivering body." with dissolve
                        n  "H-hrrrrr..."
                        "I shouldn't be here. I can't see her like this any more."
                        ks sad "Y-yeah, I'm... I'm gonna give you some privacy."
                        "So I turn around and I start to walk away, only stopping briefly at the doorframe to utter meaninglessly:"
                        ks sigh "I'll be in my room if you want to... talk about it. Or whatever."
                        $ persistent.nozomi_lying_unlock = True
                        stop music fadeout 5.0
                        scene bg blackscreen with longdissolve
                        "What else could I even say?"
                        scene bg k bedroom eve with dissolve
                        "Nozomi wanted me to push her. If I hadn't gone as far as I did, would she have ever been satisfied?"
                        "But even if she truly had no limits in the end, shouldn't I have had my own?"
                        "I never had to do that to her. I didn't have to make that choice."
                        "No matter what, I'm her hypnotist. I'm still responsible for what happened in there."
                        "I'm responsible for everything, so..."
                        $renpy.sound.set_volume(0.3)
                        play sound doorknockslow
                        "... Only a quiet knocking on my door snaps me back to the real world."
                        $renpy.sound.set_volume(1.0)
                        n "{size=16}K-... Kyou?{/size}"
                        ks sigh "... Yeah, I'm here."
                        play sound dooropen
                        pause 1.0
                        show Nozomi front2 concerned at center with longdissolve
                        "She didn't just leave?"
                        n "Hey..."
                        ks sad "... Hey."
                        "I wouldn't have blamed her if she ran out of my house screaming."
                        "But here she is, standing pensively in the doorway as we regard each other with pained stares."
                        ks "Are you... okay?"
                        play music Sorrow
                        "Nozomi doesn't answer. She only bows her head as she slowly pads over to my side and sits with me on the bed."
                        "It takes another long moment before she finally begins to speak."
                        n sleeptalk "N-no, Kyou... I don't think I'm okay." with dissolve
                        ks "... I'm sorry."
                        n side sad_closed "Why are you apologizing?" with dissolve
                        ks confused "Why? I went too far, didn't I?"
                        n sad_side "Yeah... you did." with dissolve
                        "She trembles beside me as she averts her eyes from me and holds a hand to her temple."
                        n sad_closed "B-but what did I think was going to happen?" with dissolve
                        n "I wanted you to dominate my mind; to go all the way. Explore my fantasies to the fullest."
                        n sad "It's what I wanted. But also... n-not." with dissolve
                        n "I just thought, there still had to be a limit, right? There had to be something I wouldn't do; something I'd be able to resist, no matter how deep I was into it."
                        n front2 sleep_concerned "All you did was show me that when it comes down to it, I don't have limits. I don't have a bottom." with dissolve
                        n scared "Y-you showed me... t-that I can't trust myself to be hypnotized. I can't trust myself to separate fantasy from... f-from reality and just... j-just..." with dissolve
                        n cry "Hrrr... O-ohh god, I'm so messed up!" with dissolve
                        "I look down at her as she hunches over, choking down sobs."
                        "And all I can do is place an arm around her in some futile attempt to offer her comfort."
                        n frightened "I'm SO messed up!" with dissolve
                        "Like, Christ, what do I even say to her?"
                        ks "I... it's alright, Nozomi. We don't have to do this anymore."
                        n "W-we won't. I won't..."
                        n "I'll never put my mind in danger again, I swear it!"
                        "I can only nod grimly. That this would be the end of our adventures in hypnosis was practically a given."
                        "The idea of hypnotizing her again no longer excites me. Not after what it's done to her."
                        "If this is what hypnosis can do a person?"
                        "I don't think I could ever do this to someone again. Especially not to Nozomi."
                        stop music fadeout 5.0                     
                        scene bg blackscreen with longdissolve
                        "But does that mean this is the end of... of us?"
                        $ ending = "quit"
                        pause 2.0
                        jump Epilogue_Con_Kyou_Nozomi
                        #Maybe rephrase the "stop breathing" choice and instead simply make it clear Kyou's intention to escalate as much as possible, versus this choice where he doesn't go quite as
                        #far, but is clearly pushing well beyond the bounds of Nozomi's comfort and safety, which she'll soon realize herself                        

                        # "Kyou's seen enough. He knows this isn't what Nozomi wanted. He KNOWS it. Why isn't she pushing back?"
                        # "Why isn't she waking up and stopping this? And what does that mean for everything else they've done previously?"
                        # "But more to the point, Nozomi trusts him. Why is he even thinking about putting her in legitimate danger?"
                        # "It's too much; he needs to take responsibility and put a stop to this..."
                        # show Nozomi front uniform sigh noblush with blink
                        # "So he takes Nozomi back into trance, clears her mind of all his suggestions (including the ones from previous nights) and wakes her."
                        # "Cue frightened conversation between them over what just happened, Nozomi confirming that she was unaware and defenceless..."
                        # "... And that this wasn't what she wanted. This was TOO real."
        "((We have reached the end of the current rewritten script.))"
        "((Going to cut to credits instead of continuing with the old script, which is going to basically make no sense at all now.))"
        "((To be continued!))"
        jump Credits


        # ks neutral blush "So, err..."
        # "I've never done anything like this before."
        # ks "On your knees, Nozomi."
        # show Nozomi:
        #     linear 1.5 ypos 1.2
        # "As she obediently drops down to the floor to sit on her heels, I reach down to pet her head."
        # "The last thing I want to do is hurt her."
        # "So maybe I should ask her what she wants me to make her do? Would that be defeating the purpose?"
        # show Nozomi concerned:
        #     ypos 1.2
        # "And now she's looking at me expectantly again." with dissolve
        # "Well... if I assume she can now stop my influence over her at any time, maybe I shouldn't worry about this too much."
        # ks smile "You know, I'm still thinking about the power I have over you. About all the things I could make you do."
        # ks "And all you'd be able to do in return is smile and obey. Even if you knew it would risk your life. Even if my orders would strip you of your very humanity."
        # ks "Doesn't that excite you, Nozomi?"
        # n blush "{size=16}It.. it does, Sir. It thrills me to my core to know I'm powerless before you.{/size}" with dissolve
        #
        # ks "So then, Nozomi. With this ultimate power at my disposal I command you to..."
        # menu:
        #     "Make me a cheese omelette.":
        #         show Nozomi surprised:
        #             linear 1.5 ypos 1.0
        #         "Nozomi blinks in surprise as she registers what I said, but her body responds immediately as she rises back to her feet and starts padding towards the kitchen." with dissolve
        #         show Nozomi:
        #             xpos 0.65
        #             ypos 1.0
        #         show Nozomi:
        #             linear 3.0 xpos 2.0
        #         "I'm sure I heard a soft chuckle from her as she disappears from view, followed shortly after by the sound of the fridge door opening."
        #         "Not wanting to miss the sight of an underwear-clad girl cooking for me, I decide to follow her."
        #         scene bg k dining room eve with dissolve
        #         "Taking a seat at the dining table, I simply watch with a grin as she works, navigating around my kitchen with relative ease to get her task done."
        #         show Nozomi front underwear concerned blush
        #         "I can tell she's a little flustered at my staring, but she doesn't say anything as she prepares the food, sets it on a plate and serves it up to me at the table." with dissolve
        #         n side sad "{size=16}H-Here you are, Sir.{/size}" with dissolve
        #         "I take a look at the cheese omelette in front of me, then at her, still grinning."
        #         ks smirk "I never said I wanted to eat it, Nozo. Besides, I'm not hungry."
        #         n frown "{size=16}What? Geez, then why did you have me make it?{/size}" with dissolve
        #         ks "Sit down and eat it yourself."
        #         show Nozomi:
        #             linear 1.0 ypos 1.1
        #         pause 1.0
        #         n front pout "{size=16}But I'm not hungry either...{/size}" with dissolve
        #         show Nozomi:
        #             ypos 1.1
        #         "She says, as she tears a piece off and pops it into her mouth."
        #         n "{size=16}Jerk...{/size}"
        #         ks smile "Tell me how you're really feeling, Nozomi."
        #         "She takes a moment to swallow her food before replying."
        #         n pout_left "{size=16}Really good. I know it's just a simple thing, but even making me do this and knowing I can't stop myself is so euphoric you wouldn't believe.{/size}" with dissolve
        #         "She stops to take another bite of the omelette; her compulsion to obey my latest order conflicting with the previous."
        #         ks neutral "Yet you still look a bit worried to me."
        #         n sleeptalk "{size=16}I'm not worried, Sir. I'm just embarrassed to admit this to you. And to myself.{/size}" with dissolve
        #         ks smile blush "Nozomi, there's no reason to feel embarrassed about feeling this way. You like what you like."
        #         show Nozomi concerned
        #         ks "Also, no one else needs to know if you don't want to say anything. We had a deal." with dissolve
        #         ks "So don't feel ashamed about who you are. You're safe here, with someone who wants you to be happy."
        #         ks "Let yourself enjoy this."
        #         show Nozomi smile
        #         "Nozomi gives me a smile from across the table and nods, still half-chewing as she responds in her cute whispered voice." with dissolve
        #         n "{size=16}Thank you, Sir. That does actually make me feel better.{/size}"
        #         "I smile back at her as we share a moment of mutual bliss."
        #         "And then with a grin, I'm the one to break the silence for a change."
        #         ks smirk "Now be a good girl and finish your omelette, and wash everything up when you're done."
        #         show Nozomi teasing
        #         "She pokes her tongue out at me, then takes another bite of her food." with dissolve
        #         scene bg k room eve with blink
        #         show Nozomi front smile with dissolve
        #         "Soon after she was done in the kitchen I had her get dressed and ready to leave."
        #         "Not that I wanted to, but dad's going to be home soon, and I don't think either of us want to explain this to him of all people."
        #         ks smile "You got everything?"
        #         n "{size=16}Yes, Sir. Are we doing this again tomorrow?{/size}"
        #         "I respond with a wink and a knowing smirk."
        #         ks smirk "Oh, you WILL be coming back here tomorrow. Do I make myself clear?"
        #         show Nozomi chuckle blush
        #         "She replies with a muted giggle." with dissolve
        #         n "{size=16}Yes, Sir. I must obey~{/size}"
        #         stop music fadeout 5.0
        #         jump Day12_Con_Kyou_Nozomi_Trance
            # "Go down on me":
            #     n surprised "{size=16}U-u-uhhhhh...{/size=16}" with dissolve
            #     stop music fadeout 5.0
            #     n "{size=16}S-s-set me free...{/size=16}"
            #     show Nozomi:
            #         linear 1.0 ypos 1.0
            #     "Nozomi's muted utterance is enough to drain the heat from my cheeks as she dazedly climbs up from the floor."
            #     n "What the..."
            #     show Nozomi:
            #         ypos 1.0
            #     n angry "What the HELL, Kyou?!" with dissolve
            #     k "I... what? What's wrong?"
            #     n "What's wrong?{w=0.5} What's {nw}"
            #     extend "WRONG? {w=0.5}I {nw}" with vpunch
            #     extend "SAID no lewd stuff, you idiot!" with vpunch
            #     play music Rain
            #     k "B-but..."
            #     "She... she did say that, yeah."
            #     n irritated "I-I knew it was a bad idea to get this involved with you... I knew..." with dissolve
            #     "Still..."
            #     k "W-what did you expect?"
            #     k "You want me to do all this kinky shit with you a-a-and what, you think I can just... I dunno, sit back and watch?"
            #     "Nozomi shifts her weight awkwardly on the rug as she scowls, her eyes darting between me and the discarded pieces of her school uniform lying on the ground."
            #     n determined "We agreed on this, Kyou! I know what we're doing is... is kinky, yes. But you still need to respect the limits I set!" with dissolve
            #     n "If you couldn't keep it in your pants you should've said something first!"
            #     k "Shit, Nozo, what did you WANT me to do?"
            #     n "I-I don't know! Not... not THAT! AGH! Did you really think I'd want to do that with you?"
            #     k "M-... m-maybe? I don't know!"
            #     show Nozomi irritated
            #     "As she puts her head in her hands and lets out an irritated shriek I can feel my eyes sting." with dissolve
            #     k "Look, I, uh... I-I'm sorry, alright? I thought you'd like it and I wanted to make you happy and I just..."
            #     k "I don't want to hurt you, Nozomi! Y-you're so smart and... and kind and beautiful, and I wanted to talk to you for such a long time."
            #     k "And you shared this stuff with me a-and I think we have a good thing going, s-so please... don't get mad!"
            #     n concerned "..." with dissolve
            #     n "Hey, Kyou... Would you mind giving me some privacy?"
            #     n sigh "We'll... we'll talk when I'm decent." with dissolve
            #     "As I sniff the air and look to her barely-covered body, I swiftly look away as a different kind of heat fills my cheeks."
            #     k "R-right... Sure."
            #     scene cg k room eve
            #     show NozomiHypno standing neutral
            #     with blink
            #     "A few minutes later and I return to the living room to a redressed and somewhat calmer Nozomi."
            #     "The time apart has given me a chance to cool my own head, too."
            #     k "S-so, uhh... are you doing okay?"
            #     "Nozomi nods with a sigh."
            #     ncg sad "I'm fine, Kyou. I just..." with dissolve
            #     ncg "There's so much going on in my head right now."
            #     k "I'm really sorry I made you uncomfortable."
            #     ncg "It's not even that."
            #     ncg neutral "Using that safe phrase you gave me just now really opened my eyes to how... involved I've been getting with what we've been doing." with dissolve
            #     ncg "I mean... we were supposed to take this slow, weren't we? So why..."
            #     ncg sad "Why did I set those terms for you, only to relax them almost immediately?" with dissolve
            #     ncg "It made so much sense at the time, but now I've had a chance to clear my head it just sounds insane."
            #     ncg "I don't understand..."
            #     "As she says it, I think back to yesterday."
            #     "I remember wondering the same thing, about her moving too fast on this stuff."
            #     "Apparently uncomfortable with the silence, Nozomi continues to speak."
            #     ncg neutral "We need to stop." with dissolve
            #     k "... What?"
            #     ncg "Kyou, I'm serious. Something has felt wrong about all of this."
            #     k "Nozomi, I know I went too far, and too fast, and I really am sorry, but still..."
            #     "Nozomi sighs as she lowers her gaze."
            #     ncg sad "I know. For the most part, I've loved everything we did. But I can't ignore what happened to me." with dissolve
            #     ncg "It was exactly like some of my, um... my fantasies."
            #     k "And... that's a bad thing?"
            #     ncg "Yes, Kyou. It is. Do you think I ACTUALLY want to be hypnotized and brainwashed into servitude, rather than just play it out?"
            #     ncg stern "When I mean it's exactly like my fantasies, I mean it's EXACTLY like my fantasies." with dissolve
            #     ncg "Until just now, I truly feel like I would've done, felt and thought practically anything you told me to."
            #     ncg "And I would uncritically accept it as right and good."
    "To be continued."
    jump Credits

label Day11_Con_Kyou_Nozomi_Zombie:
    scene bg street1 day with longdissolve
    "I walk to school the next morning feeling pretty postive."
    play music Bright_Opening
    "Classes are going to drag on again no doubt, but thanks to Nozomi my after-school activities are going to be a lot more fun."
    "Hell, even Hiroko's probably going to behave herself now after her little brush with hypnosis yesterday."
    scene bg school ext day with blink
    "There's a lot to look forward to..."
    scene bg classroom day with blink
    "I walk into class with time to spare and, seeing Nozomi and her friends chatting by their desks, I think to go over there and greet them."
    show Nozomi side neutral noglasses at center, flip:
        xpos 0.25
    show Hiroko neutral at center:
        xpos 0.5
    show Sayori neutral_right at center:
        xpos 0.75
    with dissolve
    ks smile "Good morning."
    n smile "Good morning, Kyou." with dissolve
    h neutral_side "Hey." with dissolve
    s uniform_folded "Morning." with dissolve
    "Well, they greeted me back at least."
    ks "H-... how's it going?"
    s uniform_handup smile "All good over here. They were just talking about you, actually." with dissolve
    hide Nozomi
    show Nozomi front2 pout noglasses at center:
        xpos 0.25
    show Hiroko neutral
    ks "Oh, really?" with dissolve
    h uniform_headhold2 sleeptalk "Yeah, don't let it get to your head or anything." with dissolve
    n front2 pout_left "We were just saying how it'd be good to have a little planning meeting over lunch so we can hit the ground running after school." with dissolve
    show Hiroko neutral
    show Sayori neutral_right
    n smile "Does that sound good to you?" with dissolve
    ks "Sounds... great, yeah."
    play sound schoolbell
    n chuckle "Alright, then~ Good luck in class." with dissolve
    ks "Yeah. You too, girls."
    hide Nozomi
    hide Hiroko
    hide Sayori
    "We seat ourselves at our desks and... is it just me or did I just handle myself pretty well talking to those girls just now?" with dissolve
    "I'm feeling more positive by the minute..."
    scene bg classroom day with blink
    "Maybe it's my good mood, but the morning's lessons didn't seem that bad. Or even feel that long."
    play sound schoolbell
    "I'm even a little surprised when the bell rings out for the start of lunch period."
    scene cg rooftop day
    show RoofHiroko leanback neutral_left
    show RoofNozomi handsdown smile noglasses
    show RoofSayori leanback neutral
    with blink
    n "Alright~ So shall we get started?"
    "And before too long I'm back on the rooftop with Nozomi and the others."
    show RoofNozomi neutral_left
    show RoofSayori sleep
    s sleeptalk "Mmn... I shall be napping in the autumn sun if anyone needs me." with dissolve
    show RoofHiroko handcheek irritated
    h "Man, why'd you even follow us anyhow?" with dissolve
    show RoofSayori happy
    s happy "Why indeed. Happy planning, you three." with dissolve
    show RoofNozomi neutral_right
    show RoofHiroko annoyed
    h irritated "Ugh. Whatever!" with dissolve
    show RoofSayori sleep
    if hirokoinfluenced == True:
        show RoofNozomi worried_right
        n sad_side "W-well anyway, I thought we could start with you, Hiroko." with dissolve
        show RoofHiroko leanback worried_left
        h "Huh? Me?" with dissolve
        "I find myself leaning in as the pair of them talk."
        show RoofNozomi happy
        n happy "Mhm! Are you still feeling good about doing the show with us?" with dissolve
        "Needless to say, I'm rather interested in Hiroko's feelings as well." #, now that she's had some time to process what happened to her."
        show RoofHiroko neutral_left
        h uniform_headhold2 "Oh, uhh... yeah, why wouldn't I be?" with dissolve
        "After all, I'm not quite done assessing the results of yesterday's experiment."
        show RoofNozomi worried_right
        n sad_side "Oh I don't know, it's... well, sometimes people say some weird things when they've just come out of hypnosis." with dissolve
        "I've not had a chance to see if a hypnotic suggestion I made with the penlight can last beyond an hour or more."
        # "Yesterday she seemed completely taken in by my whispered suggestions, but what about now that she's had time to process what happened to her?"
        show RoofNozomi neutral_right
        n neutral_side "So I want you to know, if you've had any second thoughts about it, it's okay." with dissolve
        "Is she still helpless to resist my secret suggestions to her subconscious even now?"
        # n neutral_side "I just wanted to be sure. Don't feel like you have to do any of this with us; I don't want you to feel obligated or anything." with dissolve
        # "Hiroko scoffs and shakes her head."
        show RoofHiroko sigh
        h sleeptalk "Man, where's this coming from? You know me; I ain't gonna say shit that I don't mean." with dissolve
        show RoofNozomi smile_right blush
        n smile_side blush "Yeah. Sorry, I just... I guess I'm still a little shocked that you actually liked it, that's all." with dissolve
        # n happy "W-well I was just wondering, did you have any more thoughts about what happened yesterday?" with dissolve
        # n happy "How... w-well, did you have any more thoughts about what happened yesterday?" with dissolve
        # h uniform_headhold2 surprised_side "Yesterday... m-man, that was some freaky shit you guys pulled." with dissolve
        show RoofHiroko smile_left
        "I hear Hiroko let out a slight chuckle as a smile spreads across her lips." with dissolve
        h "You and me both. That was some freaky shit you guys pulled, but it was fun."
        "Oh yes, those whispered words of mine are still living comfortably inside her head."
        show RoofHiroko handcheek surprised
        h surprised_side "Like, man, I couldn't stop thinking about it last night. Just thinking about how trippy that all was when Kyou shined the light in my eyes..." with dissolve
        "So I think I can safely conclude that my experiment has been a complete success."
        show RoofHiroko annoyed
        show RoofNozomi neutral_left noblush
        show RoofSayori neutral
        s uniform_folded sleeptalk "Well, this is quite the turnaround from yesterday, isn't it." with dissolve
        "However, it seems Nozomi and I aren't the only ones assessing the situation with Hiroko..."
        show RoofHiroko leanback frown_left
        h "Ain't you supposed to be napping?" with dissolve
        show RoofSayori sleep
        s sleeptalk "I am napping. And I am also listening." with dissolve
        s "So would you mind telling me what happened?"
        # s sleeptalk "I can multitask. Now, would you mind telling me what happened?" with dissolve
        show RoofHiroko rolleyes
        h uniform_headhold2 rolleyes "Man, why do you even care? Don't you think this's a waste of time anyway?" with dissolve
        show RoofSayori happy
        s happy "Perhaps I can be convinced otherwise with the telling." with dissolve
        show RoofHiroko frown_left
        h sleeptalk "Ugh, whatevs. So yeah, Kyou did some trick with a light and put me to sleep with it." with dissolve
        show RoofSayori sleep
    else:
        show RoofNozomi sigh
        n sad_closed "W-well, anyway I thought we could..." with dissolve
        show RoofNozomi smile_right
        n smile_side "Oh, actually Hiroko I've been meaning to ask you!" with dissolve
        show RoofHiroko leanback neutral_left
        h "Ask me what?" with dissolve
        show RoofNozomi happy
        n happy "How... w-well, now you've had a little time to think about it, how do you feel about what happened yesterday?" with dissolve
        show RoofHiroko worried_left
        h uniform_headhold2 sad_side "Yesterday... y-yeah." with dissolve
        show RoofNozomi neutral_right
        "I can see Nozomi's smile fade as she notices Hiroko's expression darken." with dissolve
        show RoofHiroko handcheek worried
        h uniform_headhold nervous_side "Still a little freaked out by it. Like..." with dissolve
        "Hiroko sighs as she reluctantly looks towards me."
        show RoofSayori neutral
        show RoofHiroko surprised
        h sad "Shit felt so fuckin' real. I still dunno how you made me do it." with dissolve
        show RoofSayori sleep
        s uniform_folded sleeptalk "Made you do what?" with dissolve
        show RoofHiroko leanback frown_left
        show RoofNozomi neutral_left
        h "Ain't you supposed to be napping?" with dissolve
        s sleeptalk "I can multitask."
        show RoofHiroko sigh
        h sleeptalk "H'yeah well if you wanna know, Kyou did some trick with a light and put me to sleep with it." with dissolve
    show RoofHiroko growl_left
    h uniform_armup angry_side "An' when I woke up, it's like he took the vocal chords right outta me!" with dissolve
    show RoofSayori worried
    s uniform_handup surprised_right "Is that so?" with dissolve
    show RoofHiroko frown
    show RoofNozomi neutral
    show RoofSayori leanforward awe
    "Sayori looks to me, as do the others as I find it impossible to keep the smile off my face." with dissolve
    ks smile "Y-yeah, it was pretty funny. She was running her mouth off but she wasn't making a sound."
    show RoofNozomi neutral_left
    show RoofHiroko frown_left
    show RoofSayori frown
    s sleeptalk "I see. Well, as it happens I spent a few minutes looking into the subject of stage hypnosis last night." with dissolve
    show RoofSayori leanback neutral
    s uniform_folded "From what little I learned, I do understand that it requires a willingness on the part of the hypnotized." with dissolve
    show RoofHiroko rolleyes
    show RoofNozomi neutral_right
    h uniform confused_side "Yeah, I get it. I went along and all, but... shit, it freaked me out." with dissolve
    show RoofSayori happy
    "Sayori chuckles." with dissolve
    show RoofHiroko frown_left
    s "Oh my, this is rather intriguing. I had thought you would give our budding hypnotist here a lot more trouble." with dissolve
    show RoofSayori smile
    s smile "Yet it seems to me that you wholeheartedly got into the spirit of what he and Nozomi are doing." with dissolve
    if hirokoinfluenced == True:
        show RoofHiroko worried_left
        h uniform_armup surprised_side "That's just it! I figured I'd just half-ass it, y'know? Play along and stuff, s'all I was gonna do." with dissolve
        show RoofSayori neutral
        show RoofHiroko sigh
        h uniform_headhold2 sleeptalk novein noblush "But... fuck, man, I dunno. The instant that light hit my eyes it's like some freak switch flipped in my brain an' I forgot all about faking it." with dissolve
        show RoofHiroko neutral_left
    else:
        show RoofHiroko sigh
        h uniform_armup irritated "Ugh, that ain't it!" with dissolve
        show RoofSayori neutral
        s neutral "No? Yet we have just established that for you to be hypnotized and follow commands requires your active co-operation." with dissolve
        show RoofSayori leanforward frown
        show RoofHiroko frown
        show RoofNozomi neutral
        "Sayori looks to me for confirmation." with dissolve
        ks neutral "That's... right, yeah."
        show RoofNozomi neutral_left
        show RoofHiroko neutral_left
        show RoofSayori leanback neutral
        s neutral "Although I imagine, you needn't be co-operating for Kyou's sake." with dissolve
        show RoofSayori smile
        s uniform_handup smirk "Were you honestly so keen on spending the culture festival with Nozomi that you went along with this little charade no matter how uncomfortable it made you?" with dissolve
        show RoofHiroko growl_left
        show RoofNozomi worried_right
        show RoofSayori neutral
        h "Ah, F-{nw}" with dissolve
        extend "FUCK off! You read a couple things an' think you're an expert now? Who do you think you are?" with vpunch
        show RoofHiroko worried_left
        h angry_side "I was gonna half-ass it. Just play along for a bit, you know? S'all I had to do." with dissolve
        show RoofHiroko worried_right
        h uniform_headhold2 sleeptalk novein noblush "But... fuck, man, I dunno. The instant that light hit my eyes it's like some freak switch flipped in my brain an' I forgot all about faking it." with dissolve
        show RoofNozomi frown
    ks sigh "Seriously? You're just admitting it?" with dissolve
    # show Nozomi sad_side
    if hirokoinfluenced == True:
        show RoofHiroko rolleyes
        h rolleyes "Like, duh? You really thought I was gonna take you serious?" with dissolve
        show RoofHiroko neutral
        h sad "I was so ready to call bullshit on the whole thing, but next thing I know I'm waking up back in that chair and... damn, dude, you really got me back there." with dissolve
        show RoofHiroko sigh
        h sleeptalk "An' ever since then I keep going back to it, like, over and over, almost like I'm trying to hypno myself." with dissolve
        show RoofHiroko blush
        h sleepy "Really didn't think I'd... um, enjoy it so much." with dissolve
        show RoofSayori sleep
        "Sayori taps her cheek thoughtfully." with dissolve
        show RoofHiroko neutral_left
        show RoofNozomi neutral_left
        s concerned "I wonder if in the moment you felt more comfortable with the arrangement than you first realized." with dissolve
        show RoofSayori worried
        s sleeptalk "Perhaps after your frustration with the examinations, the temptation to simply zone out for a while became a compelling one, regardless of the circumstances." with dissolve
        show RoofSayori smile
        s smile "Not to mention, you were not alone with our would-be hypnotist. I imagine Nozomi's presence was a comforting one." with dissolve
        show RoofHiroko worried_left
        show RoofNozomi neutral_right
        h uniform confused_side "Shit, Sayori, I just don't know any more." with dissolve
        show RoofHiroko neutral_left
        h sleep "All I know for sure is I wanna go again..." with dissolve
        show RoofSayori sleep
        s sleep "Hmm..." with dissolve
        "With a sudden shake of her head, Hiroko then turns back to Nozomi and me."
        show RoofHiroko frown -blush
        h frown "So c'mon, what're we all doing for this show thingy? That's why we're here, right?" with dissolve
        show RoofNozomi worried_right
        n sad "Uh, right..." with dissolve
    else:
        show RoofHiroko handcheek angry
        h frown "Man, fuck you too. You got what you wanted outta me, so shut up!" with dissolve
        "I simply roll my eyes at her. Like she can tell me what to do after yesterday..."
        show RoofHiroko leanback neutral_left
        show RoofNozomi worried_left
        show RoofSayori worried
        s uniform concerned "W-well... if I can cool the temperature, Hiroko? I apologize for my earlier comments." with dissolve
        show RoofSayori sleep
        s uniform_folded "Even so, it does seem like something quite remarkable happened yesterday." with dissolve
        show RoofHiroko sigh
        "Hiroko winces as she sighs a second time." with dissolve
        show RoofHiroko worried_left
        show RoofSayori neutral
        h nervous_side "Yeah, I'm sorry too, sis. This shit's just put me on edge, that's all." with dissolve
        show RoofNozomi worried_right
        n "Yeah..." with dissolve
        show RoofHiroko neutral_left
        "The sound of Nozomi's voice, having been silent for so long, is enough to pull our collective attentions back to her." with dissolve
        show RoofNozomi sigh
        n sad_closed "S-so anyway, If we could start planning out a routine now? For the show?" with dissolve
        show RoofHiroko frown
        show RoofSayori sleep
        show RoofNozomi neutral
        ks smile "Yeah. Good idea." with dissolve
    "There's a moment's silence as I look over my lunchtime companions. Although it seems like Nozomi was expecting me to say more and Hiroko just glares at me."
    "Sayori appears to have gone back to half-napping."
    show RoofNozomi sigh
    n front pout "A-alright, then. Well, before we plan anything it's important to keep in mind we'll only have about twenty minutes to do everything." with dissolve
    ks confused "Is that it?"
    "That's my gut reaction. I mean, with what we're doing that doesn't sound like enough time to do anything useful."
    show RoofHiroko neutral_left
    show RoofNozomi surprised
    n surprised "You really didn't know? It's the standard time they give to informal groups like ours." with dissolve
    show RoofHiroko rolleyes
    h neutral "Yeah, we ain't exactly the drama club over here." with dissolve
    show RoofNozomi frown_right
    show RoofHiroko neutral
    n front2 pout_left "I could request more time, but I don't think the student council would approve it. Not to mention, twenty minutes is all Satoshi had for his show last year." with dissolve
    show RoofNozomi frown
    n frown "So we have to be prepared to hit the ground running." with dissolve
    "I stroke my chin and nod."
    ks frown "Really have to wonder how that Satoshi guy pulled it off in that timeframe. Did he just get lucky?"
    show RoofNozomi neutral
    n neutral "Maybe. He certainly didn't have a problem working with me and the other volunteers he picked out, but looking back that could've easily gone wrong." with dissolve
    show RoofHiroko neutral_left
    ks "Yeah. If he picked someone who was thinking of messing with him on that stage instead of actually taking part..." with dissolve
    show RoofNozomi neutral_right
    show RoofHiroko handcheek angry
    h uniform_armup angry "Hey, don't look at me when you say that!" with dissolve
    show RoofNozomi neutral
    n side neutral_side "Well, I think it'd be a good idea if we had our volunteers picked out in advance." with dissolve
    if hirokoinfluenced == True:
        show RoofHiroko surprised
        h "Huh? Why the hell do we need volunteers for?" with dissolve
        show RoofNozomi worried_right
        n sad_side "You saw what Satoshi did, right? Picking out people from the audience is all a part of the show; that's how it's done." with dissolve
        "Hiroko simply scoffs and rolls her eyes."
        show RoofHiroko leanback rolleyes
        h rolleyes "Look, Nozo, you said it yourself; we got twenty minutes to do this thing. Why do you wanna waste time with a bunch of randos?" with dissolve
        "Seems Hiroko has her own ideas for our routine. How interesting."
        show RoofHiroko frown_left
        h frown "'Sides, his show weren't all that; why're you trying to do the same thing as Mister Pocketwatch anyway?" with dissolve
        "I know we wanted a range of hypnotic subjects to test what my penlight could do, and this was the perfect opportunity, but even so..."
        ks smirk "Wait, Hiroko, you're not suggesting..."
        "I like where this is going."
        show RoofHiroko growl
        h uniform_armup angry "Jus' do all that stuff with me! You know I'm good for it." with dissolve
        show RoofNozomi panicked_right
        n surprised_side "Y-you... you're saying you want to do everything?" with dissolve
        show RoofHiroko growl_left
        h irritated "FUCK yeah! I mean, what're you gonna do with these guys in twenty anyway? What if you get a buncha fakers like this dude's saying?" with dissolve
        show RoofNozomi worried_right
        n sad_closed "W-well... that's why I said we should pick them out before the show." with dissolve
        show RoofHiroko frown_left
        h uniform_headhold2 frown_side "Who do you think's gonna do it for us, Nozo? And even if they did, d'ya reckon they'll be on my level when they're up there in front of folks?" with dissolve
        show RoofNozomi neutral_right
        show RoofHiroko frown
        h frown "Face it, you guys can do way cooler stuff if it was just me. None of that lame-ass \"cluck like a chicken\" shit." with dissolve
        show RoofNozomi sigh
        n rolleyes "Oh, come on." with dissolve
        show RoofHiroko growl_left
        h uniform_armup angry_side "For real, though! Just lemme practice an' I'll make some jaws drop, you'll see!" with dissolve
        show RoofNozomi worried_right
        # h angry_side "What're you gonna do with these guys in twenty? What if you get a buncha fakers like this dude's saying?" with dissolve
        n sad_side "Do you even know what you're saying now? You're taking on a lot of pressure for just a culture fest show." with dissolve
        show RoofHiroko worried_left blush
        h confused_side "I just... I just LIKE this stuff, okay?" with dissolve
        show RoofHiroko growl
        h furious "I told ya yesterday; I'M your girl!" with dissolve
        show RoofSayori neutral
        s sleeptalk "You know, Hiroko does make a very good point." with dissolve
        show RoofHiroko neutral_left -blush
        show RoofNozomi panicked_left
        n surprised_side "You really think so, Sayori?" with dissolve
        show RoofSayori sleep
        s uniform_folded "After all, time is against you, and introducing variables into your routine by including unproven volunteers will absolutely complicate things." with dissolve
        show RoofSayori neutral
        show RoofNozomi neutral_left
        s neutral "A more closely-knit organization would be easier to plan around, and it leaves you more time for the actual performance you were intending." with dissolve
        show RoofSayori smile
        s smile "So what argument is there against indulging our overly-enthusiastic friend here?" with dissolve
        show RoofNozomi surprised
        n sad_closed "Hmmm... w-well..." with dissolve
        "Nozomi then looks to me exasperatedly, like she's expecting me to pour cold water on Hiroko's big idea."
        show RoofNozomi neutral
        n sad "Kyou, what do you think?" with dissolve
        show RoofSayori sleep
        "But I've already made up my mind." with dissolve
        ks smile "If Hiroko wants to be the star of the show, I'm all for it."
        ks "Just so long as she knows I'm going to be hypnotizing her a *lot* between now and the big day."
        show RoofNozomi neutral_right
        show RoofHiroko handcheek worried
        h neutral_side "Um, right... yeah, obviously." with dissolve
        ks "Is that what you *want*, Hiroko?"
        show RoofHiroko surprised
        "Hiroko looks to me as I test her, rubbing the back of her head as her eyes seem to flicker with a moment's indecision..." with dissolve
        show RoofHiroko leanback sigh
        h sleeptalk "Oh, y-... yeah, if Nozo's with me then it's cool. Go nuts." with dissolve
        "... But she was never going to say anything else. If anything, I think this conversation has only reinforced her subconscious desire to follow through on what I told her earlier."
        show RoofHiroko neutral_left
        ks "Alright, so how about this..." with dissolve
        "I'll focus our experiments on you, Hiroko."
        ks "We use the literature club room again and me and Hiroko can practice some more."
        ks "I could try taking her deeper this time, get her really in the zone and then we can do something cool with that. I've already got some ideas."
        "And boy, do I have ideas..."
        ks "What do you two think about that?"
        show RoofHiroko smile_left
        show RoofNozomi sigh
        n smile "Well... alright. We can definitely use Ms.Chiba's room again after club." with dissolve
        h "Yeah, I'm feeling pumped. Let's do it~"
        "(( AUTHOR'S NOTE: And that's where I'm going to have to leave it for now! ))"
        "(( For the next scene, in case it wasn't obvious, we'll be going back to the literature club classroom for Kyou to ramp up his hypnotic experiments on Hiroko. ))"
        "(( I'm thinking they'll get to doing two things: One fairly safe and sane, the other... well, less so ^^; ))"
        "(( All the while with Nozomi initially enthusiastic about roping her friend into the hypno fun only for doubts to creep in as things get dangerous... ))"
        "(( I'm also entertaining the thought of Sayori joining them. She volunteered to watch them in the other scenario after all. ))"
        "(( And a saner voice may perhaps be required to bring everyone down to earth before it gets too crazy... ))"
        "(( Anyway, feel free to share your thoughts about all this in the usual channels while awaiting the next release~ ))"
        "{size=30}TO BE CONTINUED...{/size}"
        jump Credits
    else:
        show RoofHiroko worried
        h uniform_headhold2 neutral_side "In advance?" with dissolve
        show RoofNozomi smile_right
        n smile_side "Yes. We could ask people earlier in the day if they want to take part. Then we can do a quick suggestibility test on them first so we weed out any problem people." with dissolve
        "I think it over while Nozomi explains herself. What she's suggesting is supposed to be pretty standard for stage hypnosis shows."
        "Although honestly I'd prefer we didn't vet anyone and we got more people like Hiroko; the kind who'd be most difficult to hypnotize under normal circumstances."
        "That would be the best way to test the penlight's abilities."
        show RoofHiroko leanback neutral_left
        h neutral "You really think peeps are gonna want to be hypnotized by the creepy dude from our class?" with dissolve
        show RoofNozomi frown_right
        n frown_side "Hiroko." with dissolve
        "... But more importantly I need to keep this train on the rails."
        show RoofHiroko rolleyes
        h uniform frown_side "What? We were all thinkin' it." with dissolve
        show RoofNozomi neutral
        show RoofHiroko frown
        ks frown "Well, you're a part of this creepy dude's show so clearly someone DOES want to be hypnotized by him." with dissolve
        show RoofSayori happy
        s happy "Mhmhmh..." with dissolve
        show RoofNozomi worried_right
        n sad_side "He has a point, Hiroko. If we're working together with him, then surely it can't be that weird." with dissolve
        show RoofHiroko neutral_left
        show RoofSayori sleep
        show RoofNozomi smile_right
        n smile_side "So we'll be the ones asking for volunteers and doing the suggestibility tests. Make sure people know we're a part of the show. Okay?" with dissolve
        show RoofHiroko frown_left
        h frown "The fuck is a suggestibility test anyway? You wanna explain that?" with dissolve
        show RoofNozomi happy
        n happy "I'll show you later, Hiroko. But it's easy, don't worry." with dissolve
        show RoofNozomi neutral_left
        s uniform_folded sleeptalk "I have a question about all of this." with dissolve
        show RoofNozomi worried_left
        ks neutral "Huh?" with dissolve
        show RoofHiroko rolleyes
        h "H'yeah, this'll be good." with dissolve
        show RoofSayori neutral
        s neutral "Well, I am listening to this back and forth and I have to ask if you are overcomplicating things for yourselves." with dissolve
        show RoofSayori worried
        show RoofHiroko neutral_left
        s concerned_right "Why do you need additional volunteers when it appears you have everyone you need to complete a twenty minute show?" with dissolve
        show RoofNozomi neutral_left
        "I'm about to try and answer her as Nozomi gives a nervous-looking shrug." with dissolve
        show RoofSayori neutral
        n "W-well, I mean... it'd be more entertaining if it was more than just us, wouldn't it?" with dissolve
        show RoofHiroko sigh
        h uniform_headhold2 sleeptalk "Yeah, and it's gonna be less weird if we ain't the only ones up there, I guess." with dissolve
        "Although as I think about it, I wonder if there's an opportunity here..."
        show RoofHiroko neutral_left
        ks smile "Sayori- {w=0.5}{nw}" with dissolve
        show RoofSayori leanforward determined
        s frown_right "No." with dissolve
        ks confused "{cps=15}Huh? But you didn't- {/cps}{w=0.5}{nw}"
        show RoofSayori frown
        s irritated "I know what you were going to say, and the answer is no. I do not have the time to dedicate to this frivolity, as I have said before." with dissolve
        "Dammit. With the interest she seems to be taking in this I thought she may have changed her mind. Seems not."
        show RoofSayori leanback sleep
        s neutral "Still, I must admit a little curiosity. I am off cram school until the end of the week so perhaps I can offer some assistance after today's study club session." with dissolve
        show RoofNozomi smile_left
        n smile_side "Sure~ We should be able to work out a routine by then and maybe you could look it over with us." with dissolve
        show RoofHiroko neutral
        show RoofNozomi neutral
        ks neutral "It'd be nice if we did have a volunteer for today, though. Just to help us rehearse with someone who hasn't done this before." with dissolve
        show RoofNozomi neutral_left
        show RoofHiroko neutral_left
        show RoofSayori neutral
        s irritated "My answer remains negative." with dissolve
        "I sigh."
        ks frown "Well, is there anyone else we can think of who might help us? Any other friends?"
        show RoofSayori leanforward frown
        s uniform sleeptalk "Hmm... I do not believe anyone from the study club will have the time or motivation to assist either, but I could ask." with dissolve
        show RoofHiroko rolleyes
        h frown "H'yeah, if any of you think I'm asking Risa or anyone else from the tennis club you can all shove it." with dissolve
        ks "Why won't you ask them, Hiroko?"
        show RoofSayori leanback neutral
        show RoofHiroko growl
        show RoofNozomi neutral_right
        h angry "{cps=20}Ugh. Why don't you ask {/cps}{nw}" with dissolve
        extend "YOUR friends, huh?" with vpunch
        ks "I don't..."
        "Fuck, why'd I let her bait me like that?"
        ks "N-nevermind."
        show RoofHiroko frown
        show RoofNozomi worried_left
        n sad_side "Um... that reminds me, Sayori. Aren't you friends with the student council president?" with dissolve
        show RoofSayori worried
        s uniform_handup concerned "Akiko? I think you know her better than me these days. Besides, she'll be too swamped in general culture festival admin to do us any favours." with dissolve
        show RoofNozomi sigh
        show RoofSayori neutral
        show RoofHiroko neutral_left
        n sad_closed "Yeah... and I can't really think of anyone from literature club who has the time either." with dissolve
        ks sigh "Well... that sucks."
        show RoofNozomi regretful blush
        n sad blush "I... g-guess I could ask mom?" with dissolve
        show RoofHiroko worried_left
        show RoofSayori shocked
        "{cps=20}Did I... Did I just- {/cps}{w=1.0}{nw}" with dissolve
        h shocked_side "{cps=20}Did I just hear that right? You're gonna ask your {/cps}{nw}" with dissolve
        show RoofNozomi grimace
        extend "MOM?!" with vpunch
        show RoofSayori worried
        show RoofNozomi frown_right
        n front irritated "Y-yeah, thanks for keeping the whole school in the loop, Hiroko." with dissolve
        show RoofSayori neutral
        s neutral "Is that wise, Nozomi?" with dissolve
        show RoofNozomi frown_left
        n pout_left "Well... I mean, she already knows Kyou and I are planning a hypnosis show for the culture festival, and she's been very supportive about it." with dissolve
        show RoofHiroko neutral_left
        show RoofNozomi strainedsmile_left
        n side sad_side "S-so, I think she'd be happy to help? Not to mention, a rehearsal at our house would be more comfortable than doing it in a classroom don't you think?" with dissolve
        "Although if we go along with this, doesn't this mean she expects me to hypnotize her mother as well?"
        show RoofHiroko worried_left
        h uniform_headhold sad_side "Y... yeah, I guess?" with dissolve
        "I'm not sure how to feel about that."
        show RoofHiroko sigh
        show RoofNozomi neutral_right -blush
        h sleeptalk "Ain't like we got any better ideas." with dissolve
        "But, as another person to try the penlight on... well, an older woman would be very different to anybody we could get from class."
        show RoofHiroko neutral_left
        show RoofNozomi smile_right
        n smile_side "Alright, I'll call her and see what she thinks..." with dissolve
        stop music fadeout 5.0
        scene bg blackscreen with longdissolve
        "So, lunch continued as Nozomi talked things through with her mom. Turns out she was pretty happy to do it for us."
        "And in the meantime, we spent a hasty hour and a half after school plotting our little routine in Nozomi's literature club room."
        scene bg n house eve with longdissolve
        "Before I know it, we've joined up with Sayori again and are on our way to Nozomi's."
        show Nozomi side neutral_side noglasses at center:
            xpos 0.75
        show Hiroko uniform_headhold2 neutral_side at center
        show Sayori uniform neutral at center, flip:
            xpos 0.25
        with dissolve
        h "Man. What a week, huh?"
        s concerned "It is certainly not how I imagined it going, I must admit." with dissolve
        n smile_side blush "D-don't worry, it's a bit awkward for everyone. After all, it's not like any of us have done a public performance before..." with dissolve
        n happy "But it's just friends and family tonight. Once we get going it'll be fun for everybody, you'll see~" with dissolve
        s smile "I am looking forward to seeing what all this fuss is about." with dissolve
        h sleeptalk "H'yeah, looking forward to laughing at us makin' asses of ourselves." with dissolve
        s uniform_folded smirk "That too." with dissolve
        scene bg n room eve with blink
        "We take this awkward atmosphere with us as we all step inside the house."
        show Atsuko laugh at center, flip:
            xpos 0.35
        with dissolve
        queue music Inspiration
        nm "Welcome, welcome! Come on in~"
        "At least Nozomi's mother is here to get rid of it. Or make it more awkward. I'm not sure."
        show Nozomi side smile_side noglasses at center, flip:
            xpos 0.15
        show Hiroko smile_side at center:
            xpos 0.6
        show Sayori smile at center:
            xpos 0.85
        show Atsuko smile_side
        h "Hi, Atsuko~" with dissolve
        nm happy "Hiroko! Nozomi told me how well you did this weekend!" with dissolve
        h uniform_headhold2 smile_side blush "S-she did, huh?" with dissolve
        nm laugh "I'm so proud of you, hun! Really wish I was there to see it myself~" with dissolve
        h happy_closed "E-ehh, t-thanks!" with dissolve
        show Hiroko uniform smile_side noblush
        show Sayori neutral
        nm surprised_side "And gosh, Sayori!" with dissolve
        s concerned "Uh... yes?" with dissolve
        nm laugh "You've grown!" with dissolve
        s uniform_folded pout "I... hardly think it has been that long since we last saw each other, Mrs. Akemi." with dissolve
        s pout_closed "... I mean Atsuko." with dissolve
        nm smile_side "Mhmhm~ Well, in any case it's lovely to see you again, dear." with dissolve
        s uniform smile "Likewise." with dissolve
        "Gotta admit, I'm feeling a little awkward myself as I watch these women talk amongst themselves."
        "They all seem really close and I'm just..."
        nm smile "And it's nice to see you again, Kyou~" with dissolve
        show Nozomi smile
        show Hiroko neutral
        show Sayori neutral_right
        ks surprised "A-ah..." with dissolve
        "I'm just standing here like I don't belong."
        show Nozomi neutral_side
        nm neutral "Is he alright?" with dissolve
        h frown "Eh, he's always like this." with dissolve
        ks smile blush "Y-yeah, I'm fine Atsuko. Nice to see you too."
        nm smile "You know, I'm just going to say it." with dissolve
        ks "S-say what?"
        nm laugh "You remind me of our Ichiro!" with dissolve
        show Hiroko surprised_side
        show Sayori surprised
        n irritated blush "MOM! Oh my god, you didn't!" with dissolve
        "Maybe they can go back to ignoring me. This isn't good at all."
        show Sayori neutral
        show Nozomi neutral_side
        h neutral_side "Ichiro? How's he doing anyhow?" with dissolve
        "I can feel my chest tighten, but I can't afford to clam up now; I've got a show to do."
        nm smile_side "Oh, he's fine. Holed up in his room doing who knows what." with dissolve
        hide Nozomi
        show Nozomi front pout noglasses at center:
            xpos 0.15
        show Atsuko neutral
        n "Well, it wouldn't kill him to come down and say hello." with dissolve
        "I've gotta get my head in the game, and fast."
        nm smile "Oh, leave him alone; you know how shy he gets. Besides, do you really want him watching this thing we're doing?" with dissolve
        show Nozomi side sad_side at flip
        n "Ugh... N-no, I guess not." with dissolve
        show Nozomi sad
        show Sayori neutral_right
        show Hiroko neutral
        ks smile noblush "S-so speaking of which, should we get to it then?" with dissolve
        nm happy "Oh, let's! Before I need to get dinner started." with dissolve
        "Alright, showtime at last. Me, Nozomi and Hiroko had this all figured out in the classroom. So I just need to remember to stay on script for the most part."
        show Atsuko neutral
        show Hiroko neutral_side
        show Sayori neutral
        n smile_side "O-okay mom! So like I said on the phone, this is supposed to be a dry run of what we're going to do for the culture fest." with dissolve
        n "We'll be searching for volunteers before the show and asking them to do a little test with us, just to see if they'll be a good fit."
        n happy "And Hiroko is going to do that test with you now, okay?" with dissolve
        nm smile_side "Alright. So what happens now, Hiroko?" with dissolve
        show Hiroko uniform_headhold2 smile_side
        show Nozomi smile_side
        "The rest of us watch as Hiroko rubs the back of her head and lets out a nervous chuckle." with dissolve
        h blush "Uhh... h'yeah, okay." with dissolve
        "We argued during the planning that she be the one to do this, as the newcomer in our group."
        h uniform_armup "So, like... put your hands out in front and hold 'em together like this." with dissolve
        nm happy "Okay~" with dissolve
        h happy_closed "Yeah, like that. Now you gotta hold 'em in front of your face and put your pointer fingers out like I'm doing, okay?" with dissolve
        nm neutral_side "Like this?" with dissolve
        h laugh_side "You got it! Now watch the space between your fingers and imagine there's like, an elastic band wrapped around those fingers." with dissolve
        nm "Okay..."
        h smile_side "So that elastic band's getting tighter and tighter, just pulling those fingers towards each other." with dissolve
        "As she explains, Hiroko makes a circular motion with her finger around Atsuko's hands. Which is something else we taught her."
        nm surprised_side "Oh!" with dissolve
        h "{cps=20}Getting tighter and tighter, an' pulling those fingers closer and closer until they... {/cps}{w=1.0}{nw}"
        $ renpy.transition(dissolve, layer="master")
        extend happy_closed "touch!"
        show Sayori smile
        show Atsuko laugh
        show Nozomi happy
        "Atsuko laughs while the rest of us look on in amusement. Seems everything's going to plan so far." with dissolve
        h laugh_side "A-awesome! That right there totally proves you can be hypnotized!" with dissolve
        show Nozomi smile_side
        show Atsuko smile_side
        h uniform_headhold smile_side "So, um... you still wanna be a part of our show?" with dissolve
        nm laugh "Why, yes I would, young lady~" with dissolve
        show Nozomi laugh blush
        show Hiroko happy
        show Sayori uniform_folded neutral
        "A gentle laughter fills the room as the women express their delight at this little pre-show performance." with dissolve
        s "I have a question."
        "Well, except one woman..."
        show Atsuko neutral_side
        show Nozomi neutral_side noblush
        h uniform neutral noblush "What's that?" with dissolve
        s concerned "What would have happened had our volunteer not gone along with your little trick?" with dissolve
        show Hiroko confused_side at flip
        h "Huh?" with dissolve
        s neutral "You just said this proves Atsuko can be hypnotized. So had it not worked the opposite is true?" with dissolve
        show Nozomi sad_side
        "I hear Nozomi clear her throat before offering an explanation." with dissolve
        show Hiroko neutral
        show Atsuko neutral
        n neutral_side "W-well, not exactly. You can hypnotize most people, but whether you can at any moment depends a lot on their desire and level of comfort, among other things." with dissolve
        show Sayori neutral_right
        show Atsuko neutral
        show Nozomi neutral
        ks neutral "Yeah. Doing this right off the bat is a good way of establishing that before you invite them on stage." with dissolve
        s uniform_handup sleep "I see... it just strikes me that Atsuko passing your test was not a foregone conclusion." with dissolve
        show Atsuko neutral_side
        show Nozomi neutral_side
        h frown_side "Y-yeah, so?" with dissolve
        s smirk "Did you have a plan B?" with dissolve
        "... We really didn't."
        n laugh blush "A-a-anyway, no time to waste! On with the show!" with dissolve
        scene bg blackscreen with dissolve
        "We then took ourselves to the living room."
        show HypnoRehearsal1 hiroko_sitting_socks h_grumpy atsuko_sitting_socks a_confused nozomi_sitting_socks n_smile:
            zoom 0.5
        with dissolve
        "Nozomi, Hiroko and Atsuko, as my lineup of volunteers, got themselves seated on one of the couches while Sayori, as our audience/critic, took the other."
        "And then there's me, the host and hypnotist, standing behind the participants. All ready to get this show on the road."
        scene HypnoRehearsal2 neutral with dissolve
        "As soon as Sayori stops staring at me like that, as if she's taking detailed notes in her head and getting ready to grade me at the end."
        "Ugh, no come on. It'll be okay, deep breath..."
        show HypnoRehearsal1 hiroko_sitting_socks h_grumpy atsuko_sitting_socks a_confused nozomi_sitting_socks n_smile:
            zoom 0.5
        with dissolve
        ks smile "O-Okay, thanks for coming everyone. I hope you're all ready to see some hypnosis in action!"
        scene HypnoRehearsal2 neutral with dissolve
        s "..."
        show HypnoRehearsal2 smirk
        s "... Let's just pretend I became wildly excited for a moment there." with dissolve
        "... Sure wish we could've found a more forgiving test audience than this woman. I bet even that Ichiro kid would've been better."
        # show Sayori smile_right
        show HypnoRehearsal1 kyou_left hiroko_sitting_socks h_growl h_hand1 atsuko_sitting_socks a_confused nozomi_sitting_socks n_smile:
            zoom 1.5 xpos -1.5
        with dissolve
        # camera:
        #     zoom 3.0 xpos -1.5
        ks blush "Now I don't know if any of you have seen a hypnosis show before..."
        show HypnoRehearsal1:
            linear 15.0 xpos - 0.3
        # camera:
        #     linear 15.0 xpos -0.5
        ks "Maybe some of you saw something like this a year ago, but what I'm about to do is going to be very simple.{w=2.5}{nw}"
        ks "{cps=20}With the help of tonight's brave volunteers- {/cps}{w=1.0}{nw}"
        h frown "{size=16}{cps=20}Stop touching my head, dickweed-{/cps}{/size}{w=1.0}{nw}"
        ks "I'm going to show you all how much fun hypnosis can be!"
        hide HypnoRehearsal1
        show HypnoRehearsal1 hiroko_sitting_socks h_grumpy atsuko_sitting_socks a_confused nozomi_sitting_socks n_smile:
            zoom 0.5 xpos 0.0
        # camera:
        #     zoom 1.0 xpos 0.0
        with dissolve
        pause 0.5
        show penlight at right with moveinright:
            ypos 0.346
        "Alright, so now I walk around to the front of my volunteers as I pull my penlight out of my pocket and hold it above them..."
        ks noblush "Now, can I get you guys to focus on the light in my hand?"
        hide penlight with moveoutright
        show HypnoRehearsal1 a_neutral
        # show Hiroko neutral
        # show Atsuko neutral
        camera:
            zoom 3.0 xpos -0.5
        with dissolve
        camera:
            zoom 3.0 xpos -0.5
            linear 10.0 xpos -1.5
            pause 1.5
            linear 10.0 xpos -0.5
            pause 1.5
            repeat
        # show HypnoRehearsal1:
        #     zoom 1.5 xpos -0.3
        # with dissolve
        # show HypnoRehearsal1:
        #     linear 10.0 xpos -1.5
        #     pause 0.5
        #     linear 10.0 xpos -0.3
        #     pause 0.5
        #     repeat
        # $renpy.block_rollback() # Blocking roll forward would be preferable, but for some reason there doesn't seem to be an equivalent function to do that
        "My heart pounding, I watch as the three of them turn their gazes upward to the penlight in my hand as I switch it on."
        ks "Good. Now I want you all to take a deep breath and focus. Just relax as the light catches your eyes."
        show HypnoRehearsal1:
            parallel:
                "HypnoRehearsal1 hiroko_sitting h_grumpy_light atsuko_sitting a_neutral nozomi_sitting n_smile" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_grumpy atsuko_sitting a_neutral nozomi_sitting n_smile" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_grumpy atsuko_sitting a_neutral_light nozomi_sitting n_smile" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_grumpy atsuko_sitting a_neutral nozomi_sitting n_smile" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_grumpy atsuko_sitting a_neutral nozomi_sitting n_smile_light" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_grumpy atsuko_sitting a_neutral nozomi_sitting n_smile" with dissolve
                pause 1.5
                "HypnoRehearsal1 hiroko_sitting h_grumpy atsuko_sitting a_neutral nozomi_sitting n_smile_light" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_grumpy atsuko_sitting a_neutral nozomi_sitting n_smile" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_grumpy atsuko_sitting a_neutral_light nozomi_sitting n_smile" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_grumpy atsuko_sitting a_neutral nozomi_sitting n_smile" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_grumpy_light atsuko_sitting a_neutral nozomi_sitting n_smile" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_grumpy atsuko_sitting a_neutral nozomi_sitting n_smile" with dissolve
                pause 1.5
                repeat
        "Trying not to think too much about everyone's attention on me, I do my best to steer the light over each person in turn while speaking as calmly and clearly as I can."
        ks "And while you're watching the light, notice how natural it becomes to focus. To focus on the light that catches your eye and to focus on the sound of my voice."
        stop music fadeout 30.0
        ks "So as you focus more and more, as you take another deep breath in... and out, you'll find that any other noises serve only to make you more and more focused."
        show HypnoRehearsal1 hiroko_sitting h_relaxed atsuko_sitting a_relaxed nozomi_sitting n_relaxed with longdissolve:

            parallel:
                "HypnoRehearsal1 hiroko_sitting h_relaxed_light atsuko_sitting a_relaxed nozomi_sitting n_relaxed" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_relaxed atsuko_sitting a_relaxed nozomi_sitting n_relaxed" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_relaxed atsuko_sitting a_relaxed_light nozomi_sitting n_relaxed" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_relaxed atsuko_sitting a_relaxed nozomi_sitting n_relaxed" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_relaxed atsuko_sitting a_relaxed nozomi_sitting n_relaxed_light" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_relaxed atsuko_sitting a_relaxed nozomi_sitting n_relaxed" with dissolve
                pause 1.5
                "HypnoRehearsal1 hiroko_sitting h_relaxed atsuko_sitting a_relaxed nozomi_sitting n_relaxed_light" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_relaxed atsuko_sitting a_relaxed nozomi_sitting n_relaxed" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_relaxed atsuko_sitting a_relaxed_light nozomi_sitting n_relaxed" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_relaxed atsuko_sitting a_relaxed nozomi_sitting n_relaxed" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_relaxed_light atsuko_sitting a_relaxed nozomi_sitting n_relaxed" with dissolve
                pause 0.5
                "HypnoRehearsal1 hiroko_sitting h_relaxed atsuko_sitting a_relaxed nozomi_sitting n_relaxed" with dissolve
                pause 1.5
                repeat
        ks "More and more focused on the light, more and more focused on my voice as you breathe once more, in..."
        ks "And as you breathe out now I want you to let your eyes close and allow yourselves to become even more focused. Even more focused as your eyes close and..."
        hide HypnoRehearsal1
        show HypnoRehearsal1 hiroko_sitting h_relaxed_closed atsuko_sitting a_relaxed_closed nozomi_sitting n_relaxed_closed:
            zoom 0.5 xpos 0.0
        $ renpy.transition(longdissolve, layer="master")
        ks "That's right, eyes closed, allowing yourselves to become completely focused on my voice." with dissolve
        "Popping my penlight back in my pocket, I allow myself a breath of my own. So far so good; everyone's co-operating just fine so far."
        ks "And now that you're all so completely focused on my voice I'd like you all to tense your entire bodies. From the muscles in your cheeks all the way down to your toes."
        show HypnoRehearsal1 hiroko_sitting h_irritated atsuko_sitting a_irritated nozomi_sitting n_irritated
        $ renpy.transition(longdissolve, layer="master")
        ks "Just tense all over and in a moment, when I count down from three to one I'm going to ask you to release all that tension." with dissolve
        ks "When I count down from three, when I reach the number one, you'll allow yourselves to become as relaxed as you can possibly be."
        ks "All tense right now, but about to become completely, utterly relaxed, not a drop of tension in your bodies as I count now... three, two and..."
        play sound fingersnap
        show HypnoRehearsal1 hiroko_sitting_socks h_relaxed_closed atsuko_laying_socks a_sleep nozomi_laying_socks n_sleep
        $ renpy.transition(longdissolve, layer="master")
        ks "One!"
        queue music Piano_Mood
        camera:
            zoom 1.0 xpos 0.0
        "I snap my fingers on the count of one, just for added effect, and almost instantly heads begin to droop." with dissolve
        ks "That's right, not a drop of tension. Completely relaxed and focused, letting your every muscle become loose and limp."
        show HypnoRehearsal1 hiroko_laying_socks h_sleep
        $ renpy.transition(longdissolve, layer="master")
        "I can hear Sayori utter a muted gasp behind me as Hiroko even slumps into Atsuko's shoulder. She's surely never seen her friends like this before."
        ks "That's right. Allowing yourselves to enjoy this deeply-relaxed feeling you're experiencing."
        ks "So now, from this point on until the end of the show whenever I, and only I, touch you on the top of your head and say the word \"sleep\"..."
        ks "... you will immediately and automatically return to this wonderfully deep state of relaxation and focus that you're feeling now."
        ks "In fact, you may allow yourselves to become even more relaxed and even more deeply focused every time I touch the top of your head and say the word \"sleep\"."
        "Okay. That's about as thorough as I can be with them given I'm supposed to be on the clock here. I need to move quickly on to the show part of this performance."
        ks "So with that in mind let's test that response in front of everyone. On a count of three I'd like you all to awaken, okay?"
        ks "{cps=20}Counting up, one two and... {/cps}{w=0.5}{nw}"
        show HypnoRehearsal1 h_wakingtalk a_waking n_waking
        play sound fingersnap
        $ renpy.transition(dissolve, layer="master")
        extend "three, awake!"
        show HypnoRehearsal1 hiroko_sitting_socks h_embarrassed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_relaxed
        $ renpy.transition(longdissolve, layer="master")
        "Eyelids flutter open and limbs stir back into motion as my three subjects begin to wearily right themselves on the couch."
        "And while they're settling back into their seats, I turn around to face my audience."
        ks "So now you've all seen a little of what hypnosis can do. But I know what some of you must be thinking."
        show HypnoRehearsal2 thoughtful onlayer toplayer
        with dissolve
        s uniform_folded concerned_right "The host should have combed his hair first before stepping out in front of all these people?"
        hide HypnoRehearsal2 onlayer toplayer
        show HypnoRehearsal1 hiroko_sitting_socks h_embarrassed atsuko_sitting_socks a_confused nozomi_sitting_socks n_relaxed
        camera:
            zoom 4.0 xpos -1.4 ypos -0.1
        with dissolve
        nm "Oh! Well, I didn't want to say anything but if we're bringing it up?"
        camera:
            xpos -0.65 ypos -0.25
        show HypnoRehearsal1 h_grumpy a_neutral n_neutral
        h frown "Like, seriously. Dude's a mess." with dissolve
        camera:
            zoom 1.0 xpos 0.0 ypos 0.0
        ks frown "... You must be thinking \"There's no way they're hypnotized. This is all fake.\"" with dissolve
        show HypnoRehearsal2 smirk onlayer toplayer
        with dissolve
        s uniform_handup smirk_right "If it helps I am now thinking our resident hypnotist needs to read the room better."
        "Fuck's sake... Okay, Kyou, just chill out."
        hide HypnoRehearsal2 onlayer toplayer
        with dissolve
        "Take a deep breath, turn your attention back to your volunteers and stay on script. It'll be fine."
        show HypnoRehearsal1 kyou_left h_hand1
        camera:
            zoom 3.0 xpos -0.5
        with dissolve
        ks "{cps=20}So let's give you doubters something to think about while our volunteers {/cps}{nw}"
        camera:
            linear 6.0 xpos -1.5
        show HypnoRehearsal1 h_relaxed_closed
        $ renpy.transition(dissolve, layer="master")
        extend "{cps=20}sleep... {/cps}{w=1.0}{nw}"
        show HypnoRehearsal1 kyou_right_right atsuko_laying a_sleep a_hand
        $ renpy.transition(dissolve, layer="master")
        extend "{cps=20}sleep, and... {/cps}{w=1.0}{nw}"
        show HypnoRehearsal1 kyou_right hiroko_laying_socks h_sleep nozomi_laying n_sleep n_hand
        $ renpy.transition(dissolve, layer="master")
        extend "sleep again."
        "As I speak, I reach out and touch each woman in turn and they drop straight back down into trance."
        show HypnoRehearsal1 kyou_right_left
        $ renpy.transition(dissolve, layer="master")
        "It's funny, but even with that little commotion I didn't even doubt for a moment that they would respond just how I wanted."
        ks neutral "All the way back down. That's right."
        show HypnoRehearsal2 neutral onlayer toplayer
        with dissolve
        "I then think on my next words while I feel Sayori's eyes firmly on me."
        "Despite her snarkiness it feels to me like she's genuinely interested in what I'm about to do next, as I rest my fingers gently on the top of Nozomi's head."
        hide HypnoRehearsal2 onlayer toplayer
        with dissolve
        ks smile "Now, the person I'm touching, I'm going to suggest something to you that's going to feel completely true..."
        "As for what I'm doing now? Well, during our planning session Nozomi and Hiroko agreed to a list of things I could use as suggestions during the show."
        "So long as I stick to the list, and remain careful in my phrasing, then neither of them can complain about what I'm going to do..."
        ks "The next time you're wide awake and for the remainder of the show, you will be absolutely convinced that laughter is banned in this house."
        "And I'll prove that it's possible to use my penlight in a very fun and safe way once and for all."
        ks "Any laughter you hear will make you incredibly angry and you will demand that whoever's laughing must stop immediately."
        ks "But no matter how angry you get when people laugh, you will never resort to violence or say anything you think you will regret. Do you understand?"
        n "Yeah..."
        show HypnoRehearsal1 kyou_right_right
        $ renpy.transition(dissolve, layer="master")
        ks "Good, now..."
        camera:
            linear 6.0 xpos -1.0
        show HypnoRehearsal1 a_hand
        $ renpy.transition(dissolve, layer="master")
        "I next place my hand gently to rest on her mother's head."
        ks "The person I'm touching now, the next time you're wide awake and for the remainder of the show, you are going to find the word \"hypnosis\" is the funniest thing."
        ks "Whenever you hear the word \"hypnosis\" you are going to laugh hysterically, because it's the funniest thing you have ever heard in your life."
        show HypnoRehearsal2 smirk onlayer toplayer
        with dissolve
        s "{size=16}Heh...{/size}"
        hide HypnoRehearsal2 onlayer toplayer
        with dissolve
        ks "You can stop and catch your breath if you have to, but nevertheless, \"hypnosis\" is the funniest word to you and it makes you laugh. Do you understand?"
        nm "I understand..."
        show HypnoRehearsal1 kyou_left
        $ renpy.transition(dissolve, layer="master")
        ks "Wonderful, and now..."
        show HypnoRehearsal1 h_hand2
        $ renpy.transition(dissolve, layer="master")
        camera:
            linear 6.0 xpos -0.8 ypos -0.35
        "I save Hiroko for last, because while I'm playing mom and daughter against each other, I have something different in mind for her."
        ks "The person I am touching, the next time you're wide awake and for the remainder of the show, you will feel a strong and natural impulse to steal people's s-... socks."
        "It was shoes on our list; that's why I hesitated. But I'm just adapting to the venue here."
        ks "When you're awake and for the remainder of the show, you'll take an immediate liking to the socks of all the volunteers here tonight."
        ks "You'll take so much of a liking that you'll feel an incredible urge to steal the socks for your private collection."

        # ks "When you're awake and for the remainder of the show, you'll take an immediate liking to the socks of the other volunteers and feel an incredible urge to steal them."
        show HypnoRehearsal2 concerned onlayer toplayer
        with dissolve
        s "{size=16}Huh...{/size}"
        hide HypnoRehearsal2 onlayer toplayer
        with dissolve
        ks "So whenever you feel no-one's paying attention to you, you'll use the chance to steal a sock from one of our volunteers."
        # ks "So whenever you feel no-one's paying attention to you, you'll crawl around on the floor and steal a sock from one of the other volunteers."
        ks "Whoever you're stealing from won't resist, you'll simply steal the socks for your collection while no one's watching because after all, you are also a master of sneaking."
        ks "Do you understand?"
        # ks "They won't resist, you'll simply steal the socks for yourself while no one's watching because after all, you are also a master of sneaking. Do you understand?"
        #Kyou could later extend Hiroko's impulse to a certain member of the audience later...
        show HypnoRehearsal1 h_sleeptalk
        h sleeptalk "Y-... yeah..." with dissolve
        show HypnoRehearsal1 kyou_right h_sleep a_hand n_hand
        camera:
            linear 6.0 xpos -1.25
        ks "Great. And just to make myself clear to those I'm touching now, if from now until the end of the show your socks are being taken you will make no effort to resist. Understand?" with dissolve
        if preferences.language == None:
            $ multichar = "{color=#93624B}Nozomi{/color} {color=#FFFFFF}and{/color} {color=#826B81}Atsuko{/color}"
        elif preferences.language == "spanish":
            $ multichar = "{color=#93624B}Nozomi{/color} {color=#FFFFFF}y{/color} {color=#826B81}Atsuko{/color}"
        multichar "Understand..."

        # hide HypnoRehearsal1
        scene HypnoRehearsal1 atsuko_laying_socks a_sleep hiroko_laying_socks h_sleep nozomi_laying_socks n_sleep
        camera:
            zoom 0.5 xpos 0.25 ypos 0.5
        with dissolve
        # camera at center:
        #     zoom 1.0 xpos 0.0 ypos 0.0
        "And now, as I lift my hands from their heads and walk around to the front of the couch once more, it's about time for the real show to begin."
        ks "Wonderful. When you hear me count up to three I would like you all wide awake."
        ks "{cps=20}On three: {w=0.5}One two and, {/cps}{nw}"
        play sound fingersnap
        show HypnoRehearsal1 h_waking a_waking n_waking
        $ renpy.transition(dissolve, layer="master")
        extend "three, welcome back!"
        show HypnoRehearsal1 hiroko_sitting_socks h_embarrassed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_relaxed
        $ renpy.transition(longdissolve, layer="master")
        "With a snap of my fingers, I immediately start to address the three of them while they're in the middle of rousing themselves."
        show HypnoRehearsal1 h_relaxed
        ks "How's everyone here? We feeling good? Feeling comfortable?" with dissolve
        show HypnoRehearsal1 n_smile
        n smile "Ahh... a-all good for now, thanks~" with dissolve
        ks smile "That's great. We're going to have a lot of fun, just so long as everyone behaves themselves..."
        show HypnoRehearsal1 h_grumpy
        h "..." with dissolve
        show HypnoRehearsal1 h_angry a_neutral n_neutral_left
        h "I {nw}" with dissolve
        extend "TOLD ya to stop looking at me when you say that kinda stuff!" with vpunch
        show HypnoRehearsal1 h_growl
        "With a smirk, I turn my back on Hiroko to address my audience once more." with dissolve
        # "I smirk as I look to Hiroko, who glares up at me, before I then turn around to face Sayori." with dissolve
        show HypnoRehearsal2 neutral onlayer toplayer
        with dissolve
        ks "So maybe you're wondering how I'm going to convince you guys that these people behind me are really under hypnosis."
        hide HypnoRehearsal2 onlayer toplayer
        show HypnoRehearsal1 a_happy h_neutral n_neutral_left
        with dissolve
        # scene bg n room eve
        # show Nozomi front2 neutral_right noglasses at center:
        #     xpos 0.15 ypos 1.1
        # show Hiroko uniform neutral_side at center:
        #     xpos 0.6 ypos 1.1
        # show Sayori uniform neutral at center:
        #     xpos 0.85 ypos 1.1
        # show Atsuko smile at center:
        #     xpos 0.35 ypos 1.1
        # with blink

        # show Nozomi neutral_right
        # hide Hiroko
        # show Hiroko neutral_side at center:
        #     xpos 0.6 ypos 1.1
        nm "Mhmhm..."
        ks "Maybe you saw the hypnosis show that other guy did at the last culture fest, like I was talking about. Or maybe you've seen hypnosis on tv..."
        show HypnoRehearsal1 a_laugh h_neutral_right n_annoyed
        nm laugh "Ahahahahaha!" with dissolve
        ks "{cps=20}... and thought they were just acting for the show. Lot of reasons to be skeptical, but- {w=1.0}{/cps}{nw}"
        show HypnoRehearsal1 a_happy n_annoyed_left
        n "Mom, what are you doing?" with dissolve
        "I turn around as I notice Nozomi glaring at Atsuko, who is currently giggling into the hand she just slapped over her mouth."
        ks smile "Is there a problem?"
        show HypnoRehearsal1 a_smile
        nm smile "Hehe, don't mind me, Kyou. Carry on with your speech." with dissolve
        n "Well he can't if you're laughing through it, can he? Please be quiet."
        ks "I'll take this from here, Nozomi."
        show HypnoRehearsal2 neutral onlayer toplayer
        with dissolve
        "Turning my back to them once again, I go back to addressing the \"crowd\"."
        ks "{cps=20}As I was saying, there's a lot of reasons to be skeptical about hypnosis, but if there's one thing- {/cps}{w=1.0}{nw}"
        nm "HEEHEEHEEHEE!"
        show HypnoRehearsal1 a_laugh n_annoyed_left
        hide HypnoRehearsal2 onlayer toplayer
        with dissolve
        n irritated "MOM! Oh my god!"
        camera:
            linear 4.0 zoom 1.5 xpos -0.4 ypos 1.5
        nm "Ahaha, l-lighten up, It's funny!"
        show HypnoRehearsal1 a_smile_right
        $ renpy.transition(dissolve, layer="master")
        # n "I don't care! Just be quiet!"
        # scene bg n room eve
        # camera
        # show Nozomi front2 irritated noglasses at center:
        #     xpos 0.15 ypos 1.1
        # show Hiroko uniform neutral_side at center:
        #     xpos 0.6 ypos 1.1
        # show Sayori uniform neutral at center:
        #     xpos 0.85 ypos 1.1
        # show Atsuko laugh at center:
        #     xpos 0.35 ypos 1.1
        # with blink
        #
        # show Hiroko at center:
        #     xpos 0.6
        #     linear 1.0 ypos 1.2
        # pause 1.0
        n angry "I don't care! Just be quiet!" with dissolve
        show HypnoRehearsal1 n_annoyed
        n annoyed_left "Honestly, you of all people should know better than to laugh in this house." with dissolve
        show HypnoRehearsal1 a_neutral_right
        nm neutral_side "{cps=20}What on earth are you... {w=0.5}{/cps}{nw}" with dissolve
        show HypnoRehearsal1 a_confused
        extend surprised "OH!" with vpunch
        show HypnoRehearsal1 n_annoyed_left
        n "{cps=20}W-well, it doesn't matter anymore. Just- {/cps}{w=0.5}{nw}" with dissolve
        show HypnoRehearsal1 n_neutral_left
        $ renpy.transition(dissolve, layer="master")
        extend sad_side "w-wait, what's wrong?"
        show HypnoRehearsal1 onesock n_neutral atsuko_sitting_onesock a_neutral h_smug
        ks frown "Hey, guys, I'm trying to get this thing started. What's going on?" with dissolve
        camera
        camera:
            linear 4.0 zoom 0.75 xpos 0.15 ypos 0.75
        "All eyes look to me as I turn around and pretend to look annoyed at the three of them for \"ruining\" my act with their antics."
        camera:
            zoom 1.5 xpos -0.77 ypos 1.5
        "My gaze falls upon Nozomi first, who offers me a resigned shrug." with dissolve
        show HypnoRehearsal1 nozomi_laying n_sleep
        n sad_closed "I'm sorry, Kyou. Mom just won't stop laughing." with dissolve
        camera:
            linear 1.0 xpos -0.5
        show HypnoRehearsal1 a_smile_right
        nm smile_side "Last I checked laughing wasn't a crime, dear."
        show HypnoRehearsal1 nozomi_protesting n_growl_left h_neutral_right
        n frown_side "It is if you do it in our house!" with dissolve
        camera:
            linear 1.0 xpos -0.2
        ks neutral "Never mind that. Are you okay, Atsuko? You cried out."
        show HypnoRehearsal1 a_smile nozomi_sitting_socks n_neutral
        nm smile "I'm fine. Something just startled me, that's all." with dissolve
        camera:
            ypos -0.1
        "Glancing down towards the floor, it's hard not to notice that her right foot is conspicuously bare as I turn my attention to Hiroko now." with dissolve
        show HypnoRehearsal1 h_growl
        camera:
            xpos 0.35 ypos 1.4
        h frown blush "W-what are you looking at?" with dissolve
        camera:
            linear 4.0 zoom 0.5 xpos 0.25 ypos 0.5
        # "She balls her hands tightly as she clumsily tries to conceal her stolen goods."
        ks frown "Are YOU alright?"
        # "I can't help but notice the loose sock poking out from under the cushion she's chosen to stash her stolen goods."
        "I ask, as my eyes glance over the loose sock conspicuously poking out from under the cushion she's chosen to stash her stolen goods."
        show HypnoRehearsal1 h_angry
        h uniform_armup irritated "D-dude, just get on with it already!" with dissolve
        show HypnoRehearsal1 h_growl
        ks "{cps=20}Okay. So maybe now we can get this hypnosis show started- {/cps}{w=0.5}{nw}" with dissolve
        show HypnoRehearsal1 h_neutral_right a_laugh n_irritated
        nm laugh "AAAHAHAHAHAHAHA!" with dissolve
        show HypnoRehearsal1 nozomi_protesting_socks n_angry_left
        n irritated blush "Oh my god mom you are SO embarrassing!" with dissolve
        nm "{cps=20}I cahahahahan't help it! Th-the things he's saying are just- {/cps}{w=1.0}{nw}"
        n frown_side "I'm serious, mom, you're going to get in SO much trouble if you don't stop it!"
        show HypnoRehearsal1 a_smile_right
        nm smile_side "Oh I am, am I? And what are you now? The laughter police?" with dissolve
        show HypnoRehearsal1 n_growl_left
        n irritated "Well it seems SOMEONE has to be around here!" with dissolve
        show HypnoRehearsal2 laugh onlayer toplayer
        s uniform_handup laugh "Pfffthahahahaha!" with dissolve
        "Sh-shit, Sayori can laugh? I have to turn around so I can see it for myself!"
        hide HypnoRehearsal2 onlayer toplayer
        show HypnoRehearsal1 n_growl
        camera:
            zoom 1.5 xpos -0.77 ypos 1.4
        n front angry "S-Sayori?! I can't BELIEVE you!" with dissolve
        "And is Nozomi shouting at... oh man, this is too perfect. I'm not getting in the way of this."
        show HypnoRehearsal2 smirk onlayer toplayer
        s smirk_right "Mhmhm, a-am I in trouble, officer?" with dissolve
        hide HypnoRehearsal2 onlayer toplayer
        show HypnoRehearsal1 n_angry
        n frown "Rrrgh, shut the hell up! I expected so much better from you!" with dissolve
        show HypnoRehearsal2 smirk onlayer toplayer
        s uniform "*snrk* W-wow, I do not even know what to say to that." with dissolve
        hide HypnoRehearsal2 onlayer toplayer
        n front2 irritated "Maybe don't say anything!" with dissolve
        show HypnoRehearsal2 laugh onlayer toplayer
        s uniform_folded laugh "Ahahaha, you have really bought into this hypnosis thing haven't you." with dissolve
        hide HypnoRehearsal2 onlayer toplayer
        show HypnoRehearsal1 a_laugh n_growl_left
        camera:
            xpos -0.4 ypos 1.5
        nm "Oh my... h-heeheeheehee!" with dissolve
        show HypnoRehearsal1 n_angry_left
        n angry "Argh! {nw}" with dissolve
        extend "{cps=20}SHUT UP ALL OF YOU! {/cps}{w=1.0}{nw}" with vpunch
        extend "SHUT UP SHUT UP SHUT UP!" with shake
        show HypnoRehearsal2 grin onlayer toplayer
        s uniform_handup giggle "Ehehehe... o-oh Nozomi, watch out~" with dissolve
        hide HypnoRehearsal2 onlayer toplayer
        show HypnoRehearsal1 n_angry
        camera:
            xpos -0.77
        n "{cps=20}\"Watch out\"? It's YOU who needs to- {/cps}{w=0.5}{nw}" with dissolve
        show HypnoRehearsal1 hiroko_thieving_socks a_neutral_right nozomi_protesting_onesock n_confused
        extend shocked "a- AH!" with vpunch
        nm neutral_side "What's the matter now, dear?"
        camera:
            linear 2.0 xpos -0.4 ypos 0.0
        n "U-uuuhhhhhh..."
        nm "Nozomi?"
        camera:
            linear 4.0 zoom 0.5 xpos 0.25 ypos 0.5
        n "It's... nothing. A-a-anyway, don't change the subject!"
        # n pout blush "I just lost a... u-um, look, don't change the subject..." with dissolve
        ks smirk "So like I was saying, if anybody here needs convincing of the fact these three are under hypnosis, that they might be faking, well..."
        show HypnoRehearsal1 a_laugh n_growl_left
        camera:
            zoom 1.5 xpos -0.4 ypos 1.5
        nm laugh "Eeeheeheehee!" with dissolve
        ks "Laughter like that is pretty hard to fake in any context, wouldn't you agree?"
        show HypnoRehearsal1 n_angry_left
        n "MOM! Come on!" with dissolve
        camera:
            linear 1.0 xpos -0.7 ypos 1.4
        ks "And get a load of her. Have you ever seen anyone this committed to a bit?"
        show HypnoRehearsal1 n_angry
        n "It's not a bit! We can't laugh in here, I'm SERIOUS!" with dissolve
        # n "{cps=20}It's not a bit! Mom can't laugh here-{/cps}{w=0.5}{nw}" with dissolve
        # show Nozomi sleep
        # $ renpy.transition(dissolve, layer="master")
        # ks smile "Aaand sleep. That's right, going deeper..."
        show HypnoRehearsal1 twosocks hiroko_sitting_socks h_smug a_happy nozomi_sitting_onesock n_embarrassed
        camera:
            zoom 0.5 xpos 0.25 ypos 0.5
        "I can hear the others chuckle at Nozomi's impotent protestations. It really seems like everyone's having a good time in here." with longdissolve
        show HypnoRehearsal2 grin onlayer toplayer
        "A good time... how much time has passed anyway? I could've already blown through my twenty minutes by now..." with dissolve
        hide HypnoRehearsal2 onlayer toplayer
        # "And now that I think of it, I have no idea how much time has gone by since we started this. I could've already blown through twenty minutes by now..."
        show bg blackscreen onlayer toplayer
        "Ah well, that's something to think about after we're done here. But right now I'm putting my hand on Atsuko's head once more." with dissolve# I'm having too much fun."
        "This is too much fun to stop now..."
        # "Let's switch things up a bit..."
        # "AUTHOR'S NOTE: I've workshopped several ideas for this next section. I've had a hugely frustrating time trying to make something work for this critical part of the scene >.<"
        # "So far I've developed two ideas beyond the most basic of outlines. They're both included here, with the \"celebrity\" idea having been written through to the next scene."
        # menu:
        #     "Make Atsuko think she's a therapist":
        #         ks "Now, from when you next wake up and until the end of the show you will find the word \"hypnosis\" to be the funniest thing you have ever heard."
        #         ks "You will always be able to catch your breath, but nevertheless \"hypnosis\" is the funniest word to you and it will make you laugh hysterically. Understand?"
        #         n sleeptalk "Yes..." with dissolve
        #         s smirk_right "{size=16}Oh, how positively wicked.{/size}" with dissolve
        #         #Sayori should note immediately how wicked this is, since Nozomi is still supposed to think laughing is banned
        #         show Nozomi sleep
        #         ks "Very good. One, two, and three, wide awake. And now..." with dissolve
        #         show Nozomi drowsy
        #         show Sayori smile_right
        #         show Atsuko smile
        #         "I'm already reaching round to touch Atsuko's shoulder before Nozomi can even open her eyes." with dissolve
        #         show Atsuko sleep
        #         ks "Sleep. You will no longer find the word \"hypnosis\" funny..." with dissolve
        #         n chuckle "{cps=20}Ehehehe... {/cps}{w=0.5}{nw}" with dissolve
        #         show Nozomi scared blush
        #         $ renpy.transition(dissolve, layer="master")
        #         extend "e-eeek, no!"
        #         show Nozomi sleeptalk_concerned
        #         "I didn't think I was going to use this next one, but with everyone behaving how they are I think this'll be hilarious." with dissolve
        #         # "With everyone behaving how they are, I think this next suggestion is gonna be hilarious." with dissolve
        #         # "I wasn't sure I'd ever use this next suggestion when the others came up with it. Felt way out of my comfort zone..." with dissolve
        #         # "Now, though? Now I feel like I can do anything!"
        #         # "There's another suggestion on our approved list that I think would be cool to try on Atsuko. A little bit of age regression." with dissolve
        #         # "Again, it's not exactly what was written, but I think it'd be a little too embarrassing to have someone much older than us thinking she's a little kid."
        #         # "I think I can adapt it for her, in a way that will be fun for everybody."
        #         # ks "Instead, I want you to think back to when you were eighteen years old. When you were in high school, like us."
        #         # n "{size=16}Oh, you're doing that one, huh?{/size}"
        #         # ks "From now until the end of the show, you're going to become just like your younger self and show us what you were like at our age. Understand?"
        #         ks "Instead, I want you to imagine you're a world-famous therapist. When you next wake up and until the end of the show, you will be the best therapist in the world."
        #         ks "You'll be able to tell, just by looking, what someone's problem is and you'll be able to tell them exactly how to fix that problem. Understand?"
        #         nm "I understand."
        #         ks "That's great. Now awake again on three."
        #         ks "{cps=20}One, two, {/cps}{nw}"
        #         play sound fingersnap
        #         extend "three."
        #         show Atsuko neutral
        #         "Atsuko snaps back to life and almost immediately her demeanor seems to shift, eyeing me nervously as she wraps her arms around her stomach." with dissolve
        #         "I have to marvel at how easily she follows along. Just like the others."
        #         "Once again, my penlight invention has worked flawlessly. It really feels like this thing will work on anybody now."
        #         "AUTHOR'S NOTE: The basic idea here was to have Atsuko diagnose Hiroko's sock-stealing obsession and Sayori's insomnia before moving onto Nozomi."
        #         "I ignored her dialogue for Hiroko and Sayori in order to focus on the critical Nozomi part, but... yeah, so far I've failed to make it work satisfactorily as you'll see."
        #         "You're welcome to read on to observe this terrible exchange for yourself."
        #         # "Atsuko snaps back to life as I jog back around to the front of the couch. And I have to say, this is yet another person my penlight-led hypnosis is working flawlessly on." with dissolve
        #         nm smile_side "And you, dear. You've been hysterical for almost this entire hypnosis show. And it's obvious why that is." with dissolve
        #         show Nozomi side laugh at flip
        #         n "Ahahaha... i-it is?" with dissolve
        #         show Nozomi happy
        #         nm happy "Why, yes. It's clear you're carrying a deep anxiety about letting something troublesome come out in a charged social situation such as this." with dissolve #while you're hypnotized. And I'm here to tell you it's okay." with dissolve
        #         nm smile_side "You're worried terribly about what would happen if this troublesome thing came out in front of your mother." with dissolve
        #         n sad_side "I... I am, huh?" with dissolve
        #         stop music fadeout 5.0
        #         nm neutral_side "And I have to tell you, you just need to let it come out. Because it really is okay, Nozomi." with dissolve
        #         nm happy "You don't have to hide that you're a lesbian anymore." with dissolve# Your mother won't be mad." with dissolve
        #         show Hiroko shocked_side
        #         show Sayori surprised
        #         queue music Rain
        #         n shocked_side blush "... H-HUH?!" with dissolve
        #         "... Wait, what the hell was that?"
        #         n sad_side "I'm not... w-w-... mom, that's..." with dissolve
        #         nm smile_side "Your parents will support your choices through life, even if they may not be the best ones." with dissolve
        #         "I don't know what I was expecting her to come out with, but it sure as hell wasn't that."
        #         nm laugh "And just like that you can feel your burden lifted~" with dissolve
        #         nm smile "{cps=20}And as for you, young man. I'm noticing a distinct lack of confidence- {/cps}{w=1.0}{nw}" with dissolve
        #         n frown_side "Mom, why would you say that? What \"burden\"? What \"choices\"?" with dissolve
        #         show Atsuko neutral_side
        #         show Hiroko uniform_headhold2 sad_side
        #         show Sayori neutral
        #         "As Nozomi protests, Atsuko turns her attention back to her upset daughter." with dissolve
        #         "This is getting away from me fast."
        #         nm "Why, you're a grown woman and I happen to have a detailed record of your past behaviour."
        #         nm "In all your years under this roof you've hardly had a thing to say about all the boys you've grown up with."
        #         nm laugh "But gosh, you have so much to talk about when it comes to your Hiroko, and your Sayori, and all the girls you bring home for board game night~" with dissolve
        #         nm "And then there's the karaoke... I may be a world-famous therapist, but this doesn't take a genuis, dear."
        #         n irritated "Right, you're the one who keeps bringing up boys. Like you think I'll shrivel up and die if I don't get a date." with dissolve
        #         show Atsuko neutral_side
        #         # n frown_side "Because that's what this is really about, isn't it. " with dissolve
        #         hide Nozomi
        #         show Nozomi front2 irritated noglasses at center:
        #             xpos 0.15 ypos 1.1
        #         n "Because that's what this is really about, isn't it. I think you're the one with the problem, mom." with dissolve
        #         ks smile "O-okay, that's all we have time for tonight, folks. Thanks for coming out!"
        #         nm sleep "Well, speaking of problems we also need to address your lack of career prospects, don't we." with dissolve
        #         #Nozomi's insulted by this of course, but Atsuko's perception of her daughter as an underachiever is apparently fuelling her wish to pair her up with someone
        #
        #         s concerned "Uh, Nozomi, perhaps we shouldn't read into what Atsuko is saying too deeply. People do say some strange things when they're uninhibited." with dissolve
        #         h uniform_headhold nervous_side "H'yeah and like, if you're seriously gay it's no biggie Nozo. Like, for real." with dissolve
        #         show Atsuko neutral_side
        #         n front2 angry "Just sh-shut up, all of you!" with dissolve
        #         show Nozomi side frown_side at flip
        #         n "And I'm sorry I'm such a disappointment to you, mom." with dissolve
        #         # n frown_side "Mom, where did THAT come from?" with dissolve
        #         # "And all of a sudden it seems a lot less fun in here."
        #         "AUTHOR'S NOTE: And that's it. Atsuko comes out with this unguarded insensitive stuff towards Nozomi leaving her embarrassed and hurt, causing her to storm off."
        #         "Kyou would then remove Atsuko's suggestions, leaving her distraught over what she said; because it's all stuff she's thought about her daughter but would never dream of saying to her."
        #         "He'd then go to check on Nozomi and they'll have the \"we need to stop our penlight hypnosis because of all the hurt it's caused\" conversation."
        #         "That's the plan anyway but, eesh, I don't know about this. There's potential in the general idea, but the execution feels way clumsy and I'm not confident about improving it."
        #         "Anyway, thanks for reading. Carry on past this line for the end credits or roll back to the previous choice to read the other ideas."
        #         jump Credits
                #
                #
                # nm "You're afraid of male intimacy."
                # n frown_side "Mom, is this because I don't talk about boys around you?"
                # h nervous_side "H-hey Nozo, even if you are it's no biggie. Like, for real." with dissolve
                # Nozomi declares the show to be over and runs to her room crying. Kyou undoes the suggestions in Atsuko's and Hiroko's minds before saying he'll talk to Nozomi
                #Could Kyou propose wiping Atsuko's memory to avoid the unpleasant atmosphere? Well then, what about Hiroko? and Sayori? We gonna mindwipe them too?
                # ks "Instead, I want you to think back to when you were eighteen years old. When you were still in school."

            # "Have everyone think they're back in high school":
            #     ks "And now sleep, and... sleep."
            #     show Atsuko sleep
            #     show Hiroko sleep
            #     "I tap the shoulders of the other two and they slump back down into trance." with dissolve
            #     ks smile "That's right. And to all of the hypnotized volunteers I want you to understand that the personalized suggestions I gave you have now been erased."
            #     ks "Instead I want you all to imagine yourselves back in high school. You're all sat down in class and you're paying attention to your homeroom teacher. That's me."
            #     "*** Uhh, okay turns out that's all I had from this latest revision of the \"regress Atsuko to a teenager\" idea ^^; ***"
            #     "*** I figured this would be a more plausible implementation of the age regression idea from both Nozomi and Kyou's perspectives to try out on an audience. ***"
            #     "*** Anyway, Nozomi and Hiroko would wake thinking Kyou is Mr. Kobayashi, while Atsuko sees him as her last homeroom teacher, Mr or Mrs. Doesnthaveanameyet. ***"
            #     "*** Nozomi and Hiroko are respectful to teacher, but Atsuko has a problem; she's unsure how she ended up back in school. ***"

                # "I still haven't quite given up on that Atsuko age regression idea."
                # "Framing it as having everyone pretend they're back in high school with Kyou as the teacher feels like a decent excuse to regress her back to this specific time in her life."
                # "Anyway, I'm still thinking about this idea. We'll see if I actually follow through..."
            # "Have Atsuko think I'm a celebrity":
                # ks "Now, from when you next wake up and until the end of the show you will find the word \"hypnosis\" to be the funniest thing you have ever heard."
                # ks "You will always be able to catch your breath, but nevertheless \"hypnosis\" is the funniest word to you and it will make you laugh hysterically. Understand?"
                # n sleeptalk "Yes..." with dissolve
                # s smirk_right "{size=16}Oh, how positively wicked.{/size}" with dissolve
                # #Sayori should note immediately how wicked this is, since Nozomi is still supposed to think laughing is banned
                # show Nozomi sleep
                # ks "Very good. One, two, and three, wide awake. And now..." with dissolve
                # show Nozomi drowsy
                # show Sayori smile_right

                # show Atsuko smile
                # "I'm already reaching round to touch Atsuko's shoulder before Nozomi can even open her eyes." with dissolve
        show HypnoRehearsal1 kyou_right_right atsuko_laying_onesock a_sleep a_hand h_neutral_right n_neutral_left
        camera:
            zoom 1.5 xpos -0.4 ypos 1.5
        hide bg blackscreen onlayer toplayer
        ks smile "Sleep. You will no longer find the word \"hypnosis\" funny..." with dissolve
        # n chuckle "{cps=20}Ehehehe... {/cps}{w=0.5}{nw}" with dissolve
        # show Nozomi scared blush
        # $ renpy.transition(dissolve, layer="master")
        # extend "e-eeek, no!"
        # show Nozomi sleeptalk_concerned
        # "I didn't think I was going to use this next one, but with everyone behaving how they are I think this'll be hilarious." with dissolve
        # "With everyone behaving how they are, I think this next suggestion is gonna be hilarious." with dissolve
        "I wasn't sure I'd ever use this next suggestion when the others came up with it. Felt way out of my comfort zone..."
        "Now, though? Now I feel like I can do anything!"
        ks "Instead, I want you to imagine a celebrity you've always wanted to meet."
        ks "He or she can be any famous person in the world. And when you open your eyes and until the end of this show you will believe... I am that celebrity!"
        ks "You'll open your eyes on a count of three, and I will look and sound just like the celebrity you've always wanted to meet. Understand?"
        nm "Yes..."
        ks "That's great. Now on three, wake up."
        show HypnoRehearsal1 kyou_left
        show HypnoRehearsal1 kyou_gone
        camera:
            zoom 1.7 xpos -0.25
        with blink
        "I then quickly pace around to the front of the couch before beginning my count."
        ks "One, two three, awake!"
        show HypnoRehearsal1 kyou_gone a_waking h_neutral_right n_neutral_left
        play sound fingersnap
        "Atsuko blinks back into life and looks up at me." with dissolve
        ks "Hey, you alright?"
        camera:
            linear 2.0 zoom 1.5 xpos -0.18
        nm "It's..."
        show HypnoRehearsal1 atsuko_sitting_onesock a_confused
        nm "I-it's you!" with dissolve
        "I try to look confident as she gasps in surprise. Although I have no idea how I should be acting right now."
        ks happy "Y-yeah, it's me. I was just... passing through the neighborhood and heard there was a fan. You wouldn't know who they're talking about, would you?"
        # ks happy "Y-yeah, it's me. I was just... passing through the neighborhood and heard there was a fan at this hypnosis show."
        # n laugh "{cps=20}Ahahaha- {/cps}{w=1.0}{nw}" with dissolve
        # show Atsuko neutral_side
        # extend irritated "MMPFTH!" with vpunch
        stop music fadeout 5.0
        show HypnoRehearsal1 a_neutral
        nm neutral "A fan? W-well..." with dissolve
        # ks smile "Hey, hold that thought a second."
        # "With a grin, I turn back to Sayori for just a moment."
        # ks noblush "Anyway, you notice how it was like a switch being flipped? How they react to hypnosis?"
        # show Atsuko surprised_side
        # show Hiroko surprised_side
        # n laugh "EEEEHEEHEEHEEHEEHEE!" with shake
        # show Hiroko:
        #     linear 1.0 ypos 1.5
        # pause 1.0
        # show Hiroko smirk_side
        # s smirk_right "Very much noted." with dissolve
        # h "{size=16}Psst, did someone say \"hypnosis\"?{/size}"
        # show Hiroko:
        #     linear 1.0 xpos 0.2
        # hide Nozomi
        # show Nozomi front2 laugh noglasses at center:
        #     ypos 1.1 xpos 0.15
        # n "{cps=20}MMpthh- AHAHAHAHAHA {/cps}{w=1.0}{nw}" with dissolve
        # extend scared blush "N-NO, I MUSTN'T!" with vpunch
        # show Hiroko:
        #     xpos 0.2
        # nm neutral_side "... Are you okay, hun?" with dissolve
        # h happy_closed "She's just freaking out about hypnosis." with dissolve
        # n cry_laugh "Ahaha-aahhh, I-I don't want to get in trouble... {size=16}but it's so funny...{/size}" with dissolve
        # show Hiroko:
        #     linear 1.0 ypos 1.1 xpos 0.6
        # pause 1.5

        # n "Ahaha-aahhh, I-I don't want to get in trouble... {size=16}but it's so funny...{/size}" with dissolve
        # nm surprised "A-anyway, I... I don't know what to say." with dissolve
        # ks smile blush "T-that's fine. I'm sure it's a little sudden so take your time."
        # "Okay, not sure what I was expecting, but she seems legit awestruck. I'll give her a moment while I turn back to address the audience."
        # nm "You're not going to be in trouble, dear."
        show HypnoRehearsal1 a_relaxed
        nm surprised "This is... this is so sudden. How did you find me?" with dissolve

        # nm "... How did you find me?"
        "Okay, her reaction isn't quite what I expected. Although she definitely seems surprised to see me, whoever it is I'm supposed to be to her."
        # "I gotta say, she doesn't seem that thrilled to see me, whoever the hell I am to her."
        ks smile "Oh... you know, I have my ways. So is there anything you want to say to me?"
        show HypnoRehearsal1 a_neutral
        nm sleep "I..." with dissolve
        show HypnoRehearsal1 a_irritated
        queue music Rain
        nm neutral "I think you need to leave." with dissolve
        ks surprised "... What?!"
        "I'm the celebrity she wants to meet and she's telling me to leave? This isn't how this routine is supposed to go."
        "What the hell is happening?"
        show HypnoRehearsal1 a_neutral
        nm neutral_side "It's been twenty years, Hansuke. But I still remember what you did to me." with dissolve
        show HypnoRehearsal2 concerned onlayer toplayer
        s uniform_folded concerned "\"Hansuke\"? Who are you talking about?" with dissolve
        hide HypnoRehearsal2 onlayer toplayer
        show HypnoRehearsal1 a_irritated
        camera:
            xpos -0.75
        # n sad_side "{cps=20}Hansuke? Mom, you don't mean-{/cps}{w=1.0}{nw}" with dissolve
        n sad_side "Mom? What's going on? Who's Hansuke?" with dissolve
        camera:
            linear 2.0 xpos -0.18
        nm sleep "It... it doesn't matter anymore. Just get out."
        ks "But..."
        show HypnoRehearsal1 a_angry
        nm neutral "I said GET OUT!" with dissolve
        show bg blackscreen onlayer toplayer with dissolve
        camera
        scene bg n room eve
        hide bg blackscreen
        scene bg n room eve
        show Atsuko angry at center:
            xpos 0.35
        show Hiroko shocked_side at center:
            xpos 0.6 ypos 1.1
        show Nozomi front2 shocked noglasses at center:
            xpos 0.15 ypos 1.1
        show Sayori uniform shocked at center:
            xpos 0.85 ypos 1.1
        with dissolve
        $persistent.hypno_rehearsal_unlock = True
        $persistent.hypno_rehearsal_2_unlock = True
        "I have no fucking clue what's going on here. But as Atsuko rises furiously from her seat I realize things are getting wildly out of control."
        hide Nozomi
        show Nozomi front2 scared noglasses at center:
            xpos 0.15 ypos 1.1
        n "K-Kyou, do something!" with dissolve
        "My hand seems to move on its own as it reaches up to press on Atsuko's head."
        ks surprised "S-s-sleep!"
        show Atsuko:
            linear 1.0 ypos 1.1
        pause 1.0
        show Atsuko sleep
        show Nozomi side sad_side at flip
        show Hiroko nervous_side
        show Sayori concerned
        play sound sitting
        "Atsuko's fury fades as she momentarily crashes back down on the couch while I hear everyone freaking out around me." with dissolve
        show Atsuko:
            ypos 1.1
        ks neutral "Yeah, that's... th-that's right. Allowing yourself to fall back into this state of relaxation."
        ks "And as you relax, you'll find yourself letting go of every suggestion I made to you tonight. Every suggestion I made tonight is now completely lifted from your mind."
        # "With all eyes on him, Kyou complies and puts our distressed subject back into trance, telling her to just relax and let that last suggestion go while others can only watch helplessly..." with dissolve
        ks "With each and every suggestion no longer able to influence you in any way, I'd like you to wake on a count of three. No longer hypnotized and no longer subject to my suggestions."
        # ks neutral "Each and every suggestion I made to you tonight is completely lifted from your mind, and when you wake on a count of three you'll no longer be hypnotized."
        stop music fadeout 5.0
        ks "Waking up, no longer hypnotized and free of all suggestions in one, two, and three."
        play sound fingersnap
        show Atsuko neutral
        "I snap my fingers and Atsuko's eyes open to look at me." with dissolve
        queue music Measured
        nm "He's... is he gone?"
        n sad_closed "Yes, mom. It's all over now." with dissolve
        show Atsuko sleep
        "She sighs, rubbing a hand against her temple." with dissolve
        nm "I didn't realize hypnosis could be so... so real."
        h uniform_headhold2 "You gonna be okay?" with dissolve
        nm neutral_side "I'll be fine, just..." with dissolve
        show Nozomi sad_side
        "She lowers her gaze to the floor as Nozomi puts a hand on her shoulder to comfort her." with dissolve
        # nm "Hansuke... I always wanted to confront him for what he did to me. But I never thought I'd see him again."
        "There's silence, broken only a few moments later as Atsuko speaks quietly to the room."
        nm "I'm going to start dinner."
        n sad_closed "O-oh... okay, mom." with dissolve
        hide Atsuko
        show Nozomi sad
        "We can only watch as she shakily departs from the couch and walks away from us." with dissolve
        "... I guess it's safe to say the show's over, huh."
        n sad_side "I need to talk to Kyou for a moment." with dissolve
        stop music fadeout 5.0
        s uniform_handup "Alright... do you want us to leave?" with dissolve
        n neutral_side "A-actually, could you keep an eye on Hiroko for me?" with dissolve
        h uniform frown_side "Eh?" with dissolve
        "Nozomi delicately points at the pair of odd socks tightly grasped in Hiroko's small hands."
        h angry_side "Aw, come on. They're mine, you can't prove anything!" with dissolve
        s sleeptalk "Understood." with dissolve
                # hide Nozomi
                # show Nozomi front2 concerned noglasses at center:
                #     xpos 0.15 ypos 1.1
                # n "Kyou?" with dissolve
                # "Yeah, Nozomi. I think it's safe to say the show's over."
                # n




                # I used to look up to him so much. That man... we used to chat online when I was about your age. He told me he was going to give me a job at his studio when I graduated."
                # nm neutral_side "Well, it turned out that it wasn't my talent he was interested in."





                # nm "I suppose you kids wouldn't know, but he was a famous mangaka back in the day. Until the scandals caught up with him."
                # nm neutral "Is that why you're here, Hansuke? Catching up on past glories?" with dissolve
                # ks sigh "Uhh... what do you mean?"
                # nm sleep "I still remember the day we met, at that book signing. You'd just finished your legendary thirty-volume series and I was just some silly art student." with dissolve
                # nm "I told you I wanted to be just like you; showed you some of my sketches. And you looked straight at me and you said you could tell I had talent."
                # nm "My parents thought I was wasting my time trying to make it in manga, but when they saw me the next day, video-chatting with one of the greatest mangaka of all time?"
                # nm "They were so proud. You said you were going to mentor me, get me a job in your studio after I graduated."
                # nm "You made me think I could do anything."
                # nm "But then you started making those... weird requests of me."


                # nm "But you have to know I'm not a little girl anymore."
                # nm neutral_side "I still think about those times, with you and me. It's been eighteen years..." with dissolve
                # nm neutral "Do you want to tell these kids what you did to me or should I?" with dissolve
                # "I have no fucking clue what's going on here."



                # "There's another suggestion on our approved list that I think would be cool to try on Atsuko. A little bit of age regression." with dissolve
                # "Again, it's not exactly what was written, but I think it'd be a little too embarrassing to have someone much older than us thinking she's a little kid."
                # "I think I can adapt it for her, in a way that will be fun for everybody."
                # ks "Instead, I want you to think back to when you were eighteen years old. When you were in high school, like us."
                # n "{size=16}Oh, you're doing that one, huh?{/size}"
                # ks "From now until the end of the show, you're going to become just like your younger self and show us what you were like at our age. Understand?"



        # "*** Still, as a safe, stageshow-appropriate suggestion with the potential for mayhem it feels like one of the better choices ***"

        # "So okay, Kyou could suggest one of several things to Atsuko. One idea I had was for her to see Kyou as a celebrity she really wanted to meet."
        # "Another was to give her a new trigger that makes her feel her butt was pinched. And another to make her feel like she's eighteen again, like the rest of them."
        # "There's problems with all of these ideas, so I still haven't decided whether to go with one or figure something else out."
        #
        # ks "However, from the time you wake up until the end of the show you will believe me to be the celebrity you most want to meet in all the world."
        # ks "Male, female, anyone in the world, whichever celebrity you most want to meet will be me, standing right here before you. Understand?"
        # nm "I... e-er, understand."
        # ks "And one, two three, wide awake!"
        # play sound fingersnap

        # "*** Still not 100% sure of it, but I think it makes some sense as a \"safe\" stageshow-appropriate suggestion that could also trigger an adverse reaction from her. ***"


        # show Atsuko neutral
        # ks "So how are you finding hypnosis, Atsuko?" with dissolve
        # n laugh "{cps=20}Ahahaha- {/cps}{w=1.0}{nw}" with dissolve
        # show Atsuko neutral_side
        # extend irritated "MMPFTH!" with vpunch
        # nm neutral "It's... w-wait." with dissolve
        # nm surprised "Is it really you?!" with dissolve
        # ks laugh "Th-the one and only! Right here at this hypnosis show."
        # show Atsuko neutral_side
        # # n chuckle "Mhmhmhmhmhm..." with dissolve
        # # ks "... funny to you?"
        # # nm happy "Not especially. I think I told you I've seen some hypnosis shows on tv but they're not really my kind of thing." with dissolve
        # n laugh "{cps=20}MMpthh- AHAHAHAHAHA {/cps}{w=1.0}{nw}" with dissolve
        # extend scared "N-NO, I MUSTN'T!" with vpunch
        # nm neutral_side "... Are you okay, hun?" with dissolve
        # show Nozomi side sad_closed at flip
        # n "Ahaha-aahhh, I-I don't want to get in trouble... {size=16}but it's so funny...{/size}" with dissolve
        # nm surprised "A-anyway, I... I don't know what to say." with dissolve
        # ks smile blush "T-that's fine. I'm sure it's a little sudden so take your time."
        # "Okay, not sure what I was expecting, but she seems legit awestruck. I'll give her a moment while I turn back to address the audience."
        # ks noblush "Anyway, you notice how it was like a switch being flipped? How they react to hypnosis?"
        # n laugh "EEEEHEEHEEHEEHEEHEE!" with shake
        # s smirk_right "Very much noted." with dissolve


        # ks "However, from now until the end of the show, any time I clap my hands, you will feel your butt was pinched." with dissolve

        #Now give Atsuko a trigger that gives an abreaction. Current winner: Make her think her butt is pinched, leading her to remember being sexually harassed at the workplace...
        # The harrassment caused her to quit her job and she fell into becoming a housewife and raising two kids...


        # h uniform_armup "I JUST LIKE THE SOCKS, OKAY?"
        # s smirk_right "Think fast." with dissolve


        #Hiroko makes her move

        #You're embarrassing everyone!
        # Kyou decides to spice things up for this show for his second set of suggestions by telling Hiroko her potential victims now extends to those in the audience
        # Seeing Sayori enjoying herself emboldens Kyou to try it
        # Sayori thinks Kyou needs to involve himself more after setting up the suggestions, as people won't necessarily react as well as these three did
        # After Hiroko made her move, he gives Atsuko her second, fateful suggestion...
        # "*** AUTHOR'S NOTE: And that's where the script ends for now xD ***"
        # "*** As always, any feedback on the script is appreciated. What follows from here is the written outline which is essentially unchanged from the previous release. ***"

        # "He then proceeds to give each woman a silly but safe and, Kyou says to himself, carefully-worded suggestion that leaves no room for ambiguity."
        # show Nozomi side laugh
        # show Sayori smile
        # show Hiroko smile_side
        # show Atsuko neutral
        # stop music fadeout 5.0
        # "Regardless, Atsuko then wakes amidst Nozomi freaking out about her forced laughter, possibly getting her other sock stolen too by an opportunistic Hiroko." with dissolve

        # "Okay, so at the climax of Kyou's hypno show, Nozomi freaks out about her forced laughter and maybe gets her other sock stolen by the opportunistic Hiroko." with dissolve
        # "However, Atsuko seems to be struggling with the fact the celebrity of her dreams is right in front of her!"
        # "However, Atsuko seems to be struggling with the suggestion in one way or another."
        # "Kyou's feeling a little less cocky now, but still he's committed and asks Atsuko not to be shy. He's here to see her; she can say what she wants..."
        # "Kyou's feeling a little less cocky now, but still he's committed and asks Atsuko what's up while she's still under the influence of this new suggestion."
        # "However, when Kyou makes a second suggestion for one of his volunteers, probably Atsuko, something unexpected happens..." with dissolve
        # show Atsuko surprised
        # show Hiroko surprised_side
        # show Sayori concerned
        # show Nozomi side sad_side at flip
        # queue music Diary
        # "... And it turns out Atsuko is suffering quite a bit under this new suggestion, which unnerves everyone." with dissolve
        # "In the case of the butt pinch suggestion, she was probably harassed in such a manner while she was younger so her reactions are less out of embarrassment but resurfaced trauma."
        # "For the celebrity suggestion, it turns out Atsuko's actually met this person before. She used to idolize him while she was an art student, and they were in touch for a while..."
        # "... only he wronged her and the experience crushed her career aspirations. She seems to have moved on, but always had a wish to confront him for it, which the suggestion brought out."
        # "Finally, for the youthful suggestion, it simply turns out that Atsuko did not have a good time when she was eighteen. Far from it."
        # "So overall, whatever the suggestion Atsuko gets, it resurfaces some past trauma and suddenly our hypno show has become decidedly unfun."
        # "For the celebrity suggestion, it turns out Atsuko's met this person before. While she was still an art student, she met him at a book signing or something, and they kept in touch."
        # "She saw him as a mentor and her ticket into a career in comic books, only for him to cut her out of his life when she wouldn't entertain his... weird requests on video chat."
        # "The experience killed her confidence, as it was obvious he wasn't interested in her for her talent, and made her quit ever trying to work in the industry."

        # "... And it turns out Atsuko does not have the best of things to say to this person, which surprises and confuses everyone."

        # "... To which, Atsuko asks him if he's showed up to torment her, which surprises and confuses everyone."
        # "... To which, Atsuko comes out with something accusatory like: \"Why did you do it?\", shocking everyone."
        # "It turns out this celebrity Atsuko had in mind is someone she's met before, back when she was a student around the same age as Nozomi and friends."
        # "This person, a famous mangaka, talked to her online a lot and offered a lot of encouragement and advice, only for him to go completely cold on her when she refused
        # "I'm thinking this person is a disgraced mangaka who she came into contact with at a book signing or something."
        # "... To which, Atsuko says something that shocks everyone in attendance. Something accusatory like: Aren't you ashamed of who you are?"
        # "It turns out the celebrity Atsuko had in mind is a famous mangaka whom she talked to many years ago when she was an art student, about the same age as Nozomi and friends."
        # "She idolized him and they used to chat online a lot while he encouraged her, even promised a job at his studio..."
        # "... only for him to go completely cold on her when she refused some of his weirder requests."
        # "His rejection shattered what confidence she had in her talents and she dropped out of art school, becoming pregnant with Nozomi not long after."

        # "A couple of ideas I had for the suggestion: Feeling pinched on the bottom when triggered, or regressing to an eighteen-year-old."
        # "Whatever the suggestion, it brings up some hidden trauma that distresses the others, Nozomi in particular, and is obviously a source of discomfort for Atsuko as well." with dissolve
        # show Hiroko sad_side
        # hide Nozomi
        # show Nozomi front angry noglasses at center:
        #     xpos 0.15 ypos 1.1
        # "Nozomi then panics and calls for Kyou to end the show immediately!" with dissolve
        # show Atsuko sleep
        # show Nozomi side sad_closed
        # "With all eyes on him, Kyou complies and puts our distressed subject back into trance, telling her to just relax and let that last suggestion go while others can only watch helplessly..." with dissolve
        # show Atsuko neutral
        # show Sayori neutral_right
        # show Hiroko neutral
        # show Nozomi front concerned
        # with blink
        # "Atsuko wakes up disoriented and upset about what just happened, before Nozomi asks Kyou to speak to her privately..."
        scene bg n bedroom eve
        show Nozomi front concerned noglasses at center
        with blink
        queue music Diary

        "Nozomi leads me up to her room and as I close the door behind me, she turns to look at me with a pained expression."
        n front2 "Mom's really hurt. I haven't seen her look at me like that for a really long time." with dissolve
        "I let out a sigh that I've been keeping in since Atsuko left us."
        "Yeah, it's undeniable that she took to my last suggestion in the worst possible way, but..."
        # n "Kyou... I think I know who \"Hansuke\" is."

        ks sigh "But I don't understand. Why the hell would your mom react like that?"
        n neutral_left "I..." with dissolve

        ks frown "I was careful, Nozomi... No, WE were careful!"
        n concerned "{cps=15}I know, I... {/cps}{w=0.5}{nw}" with dissolve
        show Nozomi sleeptalk_concerned
        $ renpy.transition(dissolve, layer="master")
        extend "I know."
        ks "You told me all the things I could do for this show and you saw me; I just did what what we agreed."
        ks "None of that stuff should've been dangerous in any way. So why..."
        n side sad_side "It doesn't matter, Kyou." with dissolve
        ks "What? What do you mean it doesn't matter?"
        "My question hangs in the air for a moment as Nozomi holds a hand up to touch her formerly-bruised cheek."
        n sad_closed "... Nothing's going to change the fact we hurt mom because we wanted to experiment." with dissolve
        n sad_side "I wanted to prove we could use your penlight to hypnotize and be hypnotized; to have the most wonderful experience, and be able to do it safely." with dissolve
        n sad "We knew it was dangerous. But I still... I still wanted to believe it was possible." with dissolve
        n front2 sleeptalk_concerned "And because of that, I hurt myself. I hurt Hiroko. Mom... even you, Kyou." with dissolve
        n cry "All because I wanted to pursue my selfish desires." with dissolve
        ks surprised "Hey, Nozomi...  c-come on, you're not selfish."
        "Nozomi starts to cry in front of me. As if this evening could get any worse."
        n frightened "Y-yes I am! I wanted a cheap thrill all to myself, and I lied and used the people I love just for a chance at it." with dissolve
        n concerned "But... b-but I can stop." with dissolve
        "I wonder for a moment what she means, only I notice her gaze is drawn to my right pants pocket."
        camera #Stop applying transforms to the entire scene so the penlight icon can slide in properly instead of just instantly appearing
        show penlight at right with moveinright:
            ypos 0.346
        "The pocket where I keep my penlight."
        n sleeptalk_concerned "We can stop, Kyou." with dissolve
        "Stop our experiments? No. It's obvious from Nozomi's expression she wants more than that."
        "... She wants me to stop using the penlight, period."
        "Just give up the crowning achievement of my entire life. Hell, the only thing that brought us together."
        menu:
            "Give up the penlight":
                "... I can't bear to see Nozomi in this much pain."
                show Nozomi concerned
                "This penlight of mine... I may have built it, but I still don't understand how it does what it does." with dissolve
                hide penlight at right with moveoutright
                "And as I wrap my fingers around it and try to bend it in two, it seems I'll never understand..."
                stop music fadeout 15.0
                show Nozomi sleeptalk
                "Nozomi wipes her eyes as she watches the penlight visibly bend in my hands. And when I go to click the switch, we see how it fails to light." with dissolve
                "So... that's that, then."
                ks sigh "I guess this means our show's cancelled too, huh."
                n side sad_closed "Y... yeah..." with dissolve
                scene bg blackscreen with dissolve
                "With our decision made, all that's left for tonight is to finish up downstairs."
                scene bg n room eve
                show Nozomi side neutral_side noglasses at center, flip:
                    xpos 0.35 ypos 1.0
                show Hiroko uniform neutral_side at center:
                    xpos 0.6 ypos 1.0
                show Sayori uniform neutral at center:
                    xpos 0.85 ypos 1.0
                with dissolve
                n "How are we doing down here?"
                "We return to the living room to find Sayori and Hiroko are still waiting for us."
                queue music Downtown
                h frown_side "Fine. Was just wondering what you an' Kyou were talking about that you didn't wanna loop me in on." with dissolve
                n sad_closed "Yeah, sorry. It was a delicate subject." with dissolve
                "I can't help but chuckle as I notice Hiroko's still holding those loose socks in her fists."
                ks smile "Hehe, yeah. And you seem a little preoccupied."
                show Hiroko frown
                hide Nozomi
                show Nozomi front2 frown noglasses at center:
                    xpos 0.35
                n "Kyou, mind your manners in my house!" with dissolve
                "... Right. Hiroko's not the only one I need to sort out while I'm here."
                ks frown "Alright, both of you need to pay attention to me."
                show Hiroko frown
                show Sayori neutral_right
                "I thought they both might have lost their hypnotic conditioning after I went upstairs. It's pretty clear we've finished our act, after all." with dissolve
                "But I guess I should know by now that they won't let go on their own. I really do need to be direct with them."
                ks frown "We're finished for tonight, okay? The show's over."
                ks "That means you're no longer hypnotized and everything I said to you in your deep states of relaxation no longer has any affect on your behaviour. Understand?"
                show Nozomi surprised
                h uniform_armup angry "Why're you talking like we're a couple idiots? I know we finished up in..." with dissolve
                show Nozomi neutral_right
                h surprised_side "... up in here. Wait, what the fuck am I doing with these?" with dissolve
                s smirk "Giving them back before you develop some kind of sock fetish?" with dissolve
                show Nozomi side neutral_side at flip
                h uniform_headhold sad_side blush "Uhh... h'yeah, here you go." with dissolve
                n happy "Mhmhmh~" with dissolve
                show Sayori uniform_folded happy
                show Hiroko smile_side
                "The room fills with quiet laughter as our performance comes to an end. For good, this time." with dissolve
                show Nozomi smile_side
                show Hiroko happy_closed
                show Sayori smile
                "Maybe I'll regret what happened just now up in Nozomi's bedroom. Knowing I broke the one thing that made all of this possible." with dissolve
                "But maybe it's worth it, just to see her smile again."
                stop music fadeout 10.0
                show Atsuko smile_side at center, flip:
                    xpos -0.5
                    linear 2.0 xpos 0.15
                nm "So when do I get MY sock back?"
                hide Nozomi
                show Nozomi side sad_side noglasses at center:
                    xpos 0.35
                show Hiroko uniform_headhold2 surprised_side
                show Sayori surprised
                show Atsuko at flip:
                    xpos 0.15
                h "A- ahh!" with dissolve
                n "Mom..."
                "We all go silent as Atsuko suddenly returns from the kitchen."
                show Hiroko nervous_side noblush
                show Sayori concerned
                queue music Monologue
                "I may have rid her of my penlight-assisted hypnosis, but I didn't do anything for the hurt it apparently caused her." with dissolve
                nm sleep "Oh, don't make those faces. I'm okay now." with dissolve
                nm neutral_side "Seeing Hansuke again after all these years was quite a shock, but I guess... it was a little cathartic, too." with dissolve
                nm neutral "I always wanted to yell at that creepy old bastard." with dissolve
                "I still want to know who the fuck this Hansuke guy was. This apparantly famous person that hurt her twenty years ago."
                "But I guess I know better than to ask right now, so all I can do is bow my head."
                show Atsuko neutral
                ks sigh "I'm sorry, Atsuko. I really wanted you to have fun with everyone else."
                nm smile "I know, dear. And it was fun while it lasted." with dissolve
                n sad_closed "It really was... but we're going to do something else for the culture festival." with dissolve
                show Atsuko neutral_side
                h surprised_side "Wait, seriously?" with dissolve
                show Hiroko nervous_side
                nm surprised_side "Oh... I hope that's not on my account." with dissolve
                n sad_side "No!" with dissolve
                hide Nozomi
                show Nozomi front2 pout noglasses at center:
                    xpos 0.35
                n "W-well, okay it is a bit." with dissolve
                n concerned "And I realized I don't feel comfortable performing hypnosis in front of everyone, s-so..." with dissolve
                "She glances towards me as she says it. I guess that's about as truthful as she can be to everyone else right now."
                h uniform sad_side "Right? I don't really wanna do all this crap in front of people. Jesus." with dissolve
                show Nozomi neutral_left
                show Sayori neutral
                nm neutral_side "Alright, Nozomi. If that really is how you feel." with dissolve
                nm "But I don't want you regretting tonight. I'm happy you asked me for help."
                show Nozomi side sad_side
                n "H-huh?" with dissolve
                show Nozomi neutral_side
                show Hiroko neutral_side
                nm smile_side "Just know I'll support you in everything you do. Okay, hun?" with dissolve
                # "Mother and daughter look to each other. I guess this evening's been especially weird for the pair of them." with dissolve
                n "Mom, I..."
                show Hiroko smile_side
                show Sayori smile
                n happy "... Okay." with dissolve
                stop music fadeout 5.0
                scene bg blackscreen with longdissolve
                pause 2.0
                $ending = "broke penlight"
                jump Epilogue_Con_Kyou_Nozomi_Zombie

                # n sad_side "Well, I don't know all the details, but mom told me she really wanted to work in comic books when she was in high school." with dissolve
                # n neutral "She wrote to this really famous author explaining her situation and asking if he had any advice for someone like her." with dissolve
                # n front2 neutral "She wasn't seriously expecting him to reply, but he did more than that. He actually praised her art and said he might hire her for his studio after she graduated." with dissolve
                # ks surprised "Really? That's a pretty big deal."
                # n concerned "Yeah... It really was too good to be true, huh." with dissolve
                # ks neutral "So what happened?"
                # n sleeptalk "They talked on videochat. Then he started asking her... well, weird things. Mom wouldn't elaborate." with dissolve
                # n concerned "But she realized he didn't give a damn about her \"talent\". It broke her heart." with dissolve
                # n neutral "So she gave up on art, had me, and that was that." with dissolve

                #Hiroko reacts to having the stolen socks in embarrassment, then Atsuko comes back in, having calmed down a bit, and sheds some light on Hansuke
                #See rough dialogue from Nozomi below and attribute it to Atsuko
            "Refuse to give up the penlight (Under Construction)":
                stop music fadeout 5.0
                hide penlight at right with moveoutright
                "Nozomi's been having doubts about all of this, and I guess tonight pushed her over the edge but I can't..."
                ks confused "Nozomi come on, don't you think you're being a little dramatic?"
                queue music Unrest
                "I can't let her stop what we're doing."
                show Nozomi concerned
                ks "This really isn't as big a deal as you think. We don't have to stop any of this!" with dissolve
                n side sad "We do, Kyou. This is my decision." with dissolve
                "We've come so far. We've gotten so close to discovering the full potential of my penlight."
                n sad_closed "I-I can't keep doing this to the people I love, so that's why..." with dissolve
                "We've gotten so close to each other."
                n front2 concerned "That's why we need to stop using that penlight. We can't ever use it again, you hear me?" with dissolve
                "No matter what Nozomi may think, we can't stop what we've started."
                ks neutral "Sure things didn't go how we wanted and you're feeling the pressure. But everything's going to be fine, you'll see."
                n frightened "No... n-no, this is as far as we go! We can't use that thing any more!" with dissolve
                "We owe it to ourselves to continue our experiments."
                ks "Look... Maybe you're right, but don't you think we should finish tonight's show first?"
                n cry "*sniff* Wha... wh-what do you mean?" with dissolve
                ks "Tonight's hypnosis show isn't over. You know that, right?"
                n shocked "I... what are you talking about? Of COURSE it's over!" with dissolve
                "Closing the distance between us, I simply reach up to pat the top of Nozomi's head as her tearful eyes fix me with the most bewildered expression..."
                ks "But I never said it was, did I?"
                n "{cps=16}K-Kyou-{/cps}{w=0.5}{nw}"
                ks "Sleep."
                show Nozomi sleeptalk_concerned
                $ renpy.transition(longdissolve, layer="master")
                n "{size=16}Ah... aaaaahhh...{/size}"
                ks "That's right, Nozomi. We both know how persuasive hypnosis under the penlight is."
                ks "So it's only natural that you are falling back into this wonderfully deep state of relaxation. Only natural to fall so deeply back into trance for me."
                "I embrace her as I see the strength leave her body, and her head slumps limply against my shoulder."
                ks "My penlight really is incredible isn't it, Nozomi?"
                n "{size=16}Mmh... Kyo... ouuu...{/size}"
                ks "Shh... it's alright."
                play sound clothes

                # "Kyou thinks she's being way too hasty and is just reacting in the moment."
                # "Sure it's done some damage to use the penlight, but she has to admit that the added pressure of their hectic school schedule hasn't helped."
                # "When things are a little calmer they can try again, surely."
                # show Nozomi frown
                # "Nozomi insists he break it, and doesn't take Kyou's refusal well at all." with dissolve
                # show Nozomi angry
                # "As she raises her voice, Kyou realises he needs to shut this down now." with dissolve
                # show Nozomi surprised
                # "First, he informs her that their show isn't over, which confuses her for a moment as he reaches for her shoulder..." with dissolve
                # show Nozomi sleep
                # "... and activates the little sleep trigger he put on all of them during the show." with dissolve
                # "And it works! Nozomi's head slumps forward as her protesting dies on her lips, reduced to nothing more than a sleepy sigh as she drops into trance in spite of herself."
                # "After all that commotion, both of them realized that Kyou never actually said the show was over earlier; it was only Nozomi who said it was."
                scene NozomiBedroom3 troubled with blink
                "With a gentle motion, I reach down to lift her up in my arms before carrying her carefully to rest on her own bed while I continue to speak to her subconscious mind."
                ks "I know you're having doubts, and I know you're scared. But you didn't really mean what you said just now, did you?"
                show NozomiBedroom3 troubledtalk
                n "I..." with dissolve
                ks "I know you don't want to stop this. And so do you, Nozomi."
                show NozomiBedroom3 troubled
                ks "So I want to tell you it's okay. You don't have to be scared of what happened, or what might happen." with dissolve
                ks "Instead, you can just relax. Let all of those worries and doubts and concerns fall away from your mind..."
                ks "Let them all go, and let me be scared for both of us."
                ks "I'll take care of everything from now on. Okay, Nozomi?"
                show NozomiBedroom3 sleeptalk
                n sleeptalk "Ah..." with dissolve
                "I smile as her expression softens with a calm sigh, while I wipe the tears from her face."
                n "Okay..."
                show NozomiBedroom3 sleep
                ks smile "Of course it's okay. So in a moment you're going to wake up again from this wonderful state of trance, ready to continue everything we're doing together." with dissolve
                ks "Ready to awaken and let me worry about all of this in one, two..."
                show bg blackscreen zorder 1
                stop music fadeout 5.0
                $ renpy.transition(longdissolve, layer="master")
                $persistent.zombie_bedroom_3_unlock = True
                ks "Three."
                "((AUTHOR'S NOTE: And that's as far as I've gotten on this story path I'm afraid. ))"
                "(( Stay tuned for more developments on this in a later update! ))"
                # "And as he sits Nozomi down on the bed in front of him... what on earth will Kyou do now?"
                # "I dunno, this author's focusing on the more ethical branch of this storyline for now, so we'll come back to this later~"
                "{size=30}TO BE CONTINUED...{/size}"
                jump Credits


    #I wanted it too, Nozomi. But you're right. We've proved enough

    # show Nozomi sleep
    #
    # n side sad_side "Kyou, I think I know why." with dissolve
    # ks surprised "Huh?"
    # "She gives a tentative nod."
    # n sad "\"It's been eighteen years, Hansuke. But I still remember what you did to me.\"" with dissolve
    # ks neutral "Do you know who she was talking about?"
    # n sad_side "Well, I don't know all the details, but mom told me she really wanted to work in comic books when she was in high school." with dissolve
    # n neutral "She wrote to this really famous author explaining her situation and asking if he had any advice for someone like her." with dissolve
    # n front2 neutral "She wasn't seriously expecting him to reply, but he did more than that. He actually praised her art and said he might hire her for his studio after she graduated." with dissolve
    # ks surprised "Really? That's a pretty big deal."
    # n concerned "Yeah... It really was too good to be true, huh." with dissolve
    # ks neutral "So what happened?"
    # n sleeptalk "They talked on videochat. Then he started asking her... well, weird things. Mom wouldn't elaborate." with dissolve
    # n concerned "But she realized he didn't give a damn about her \"talent\". It broke her heart." with dissolve
    # n neutral "So she gave up on art, had me, and that was that." with dissolve
    #
    # n side sad_side "But if she saw him in you, then she must still think about it. It must still hurt, and what we did brought it all back." with dissolve




    # n sad "... Kyou, we have to stop this." with dissolve


    # Kyou says he should have phrased it differently. Nozomi says it doesn't matter; you still can't tell how someone will respond.



    # # "(Note to self: Nobody can specifically say \"hypnosis\" here, lest Nozomi starts cracking up and ruining the tone of this scene ._.)"
    # "So, as that little demonstration just showed, there's no way to guarantee people's safety."
    # "She herself thought those suggestions they came up with would be fine and fun to work with, but she had no idea Atsuko would react like that."
    # "How did that come about? Nozomi may be able to shed some light here, linking the name Hansuke to that of a famous manga artist who was the subject of a recent scandal."
    # "Nozomi knows Atsuko was an art student before she was born, but Nozomi rarely sees her mother do much drawing. Apparently her meeting this idol of hers wrecked her career aspirations."
    # "So why the hell would she want to meet this guy again? To confront him, Nozomi thinks. Atsuko must have borne a lot of resentment for him, after all."
    # "Kyou doesn't think this makes much sense, but that's just it! There's no telling how people will react to the suggestions you give them; what may be going through their minds..."
    # "What would happen in a real show with random subjects? There's no telling how they'd react to anything."
    # "Now granted, there's a risk of a bad reaction happening using normal methods too, but they both realize the penlight just exacerbates things to an absurd degree."
    # show Nozomi front2 frightened
    # "And what's worse, Nozomi feels VERY responsible for everything that's happened." with dissolve
    # "Chasing her desires not only hurt her but everyone around her. Pursuing her love of hypnotism has caused so much misery that she no longer wants anything to do with it!"
    # "Kyou's having trouble handling all of this. He doesn't want to see Nozomi upset, but he also doesn't want to let go of his crowning achievement either."
    # show Nozomi cry
    # "But as Nozomi tearfully insists that he destroy it right here and now he thinks to himself: Can he really give it up?" with dissolve
    # menu:
    #     "Give up the penlight":
    #         "Kyou can't bear to see Nozomi like this. He emotionally grips the penlight and tries to break it in half, succeeding in bending it a little."
    #         show Nozomi sleeptalk_concerned
    #         "Nozomi lets out a sigh as she sees the penlight in Kyou's hand fail to switch on after he's messed with it, confirming he's bent it enough to make it inoperable." with dissolve
    #         show Nozomi concerned
    #         "Nozomi thanks Kyou for listening to her, and says that it's probably for the best that they cancel their plans for the culture fest. For real this time." with dissolve
    #         "Kyou, thinking their partnership is over too, dejectedly agrees. He'll deprogram her and the others downstairs before wrapping up for good..."
    #         # scene bg n room eve
    #         # show Nozomi side sad_side noglasses at center, flip:
    #         #     xpos 0.15
    #         # show Hiroko neutral at center:
    #         #     xpos 0.6
    #         # show Sayori neutral_right at center:
    #         #     xpos 0.85
    #         # show Atsuko neutral
    #         # with blink
    #         #


    # stop music fadeout 5.0
    # scene bg classroom eve with dissolve
    # "Timeskip to the epilogue. It's been a few weeks since etc etc."
    # queue music Peaceful
    # "What happens next? I'm thinking the lot of them could be working the school café during the culture festival, seemingly getting along."
    # show Nozomi front smile
    # "After a bit of banter, Nozomi says she's going on break and asks Kyou to join her." with dissolve
    # scene bg corridor eve
    # show Nozomi front smile
    # with blink
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
    # jump Credits
    #     "Refuse to give up the penlight (incomplete)":
    #         "Kyou thinks she's being way too hasty and is just reacting in the moment."
    #         "Sure it's done some damage to use the penlight, but she has to admit that the added pressure of their hectic school schedule hasn't helped."
    #         "When things are a little calmer they can try again, surely."
    #         show Nozomi frown
    #         "Nozomi insists he break it, and doesn't take Kyou's refusal well at all." with dissolve
    #         show Nozomi angry
    #         "As she raises her voice, Kyou realises he needs to shut this down now." with dissolve
    #         show Nozomi surprised
    #         "First, he informs her that their show isn't over, which confuses her for a moment as he reaches for her shoulder..." with dissolve
    #         show Nozomi sleep
    #         "... and activates the little sleep trigger he put on all of them during the show." with dissolve
    #         "And it works! Nozomi's head slumps forward as her protesting dies on her lips, reduced to nothing more than a sleepy sigh as she drops into trance in spite of herself."
    #         "After all that commotion, both of them realized that Kyou never actually said the show was over earlier; it was only Nozomi who said it was."
    #         show Nozomi:
    #             linear 1.0 ypos 1.1
    #         "And as he sits Nozomi down on the bed in front of him... what on earth will Kyou do now?"
    #         "I dunno, this author's focusing on the more ethical branch of this storyline for now, so we'll come back to this later~"
    #         "TO BE CONTINUED..."
    #         jump Credits


    #Nozomi's new confidence in talking about hypnosis needs to be brought up somewhere around the end

#     scene bg classroom2 eve with longblink
#     "So, with that said we skip to the day after the mock exams. Kyou is stood in the hall thinking about how poorly he did, since he's had his mind on Nozomi and Hiroko."

label Day11_Con_Kyou_Sayori_Doll:
    scene bg street1 day with longblink
    "I'm not feeling any better the next morning."
    play music Eons
    scene bg ext school day with blink
    "Walking to school with leaden feet, I can feel my stomach tense as I approach the gates."
    scene bg classroom day
    show Nozomi side smile_side at center, flip:
        xpos 0.25
    show Hiroko neutral_side at center:
        xpos 0.5
    with blink
    h "Mornin'."
    n "Hiroko, hi!"
    "I don't know how Sayori's doing since she went home. Seems we both decided not to contact each other."
    n neutral_side "Um, I guess she didn't get back to you either?" with dissolve
    h sad_side "Nah." with dissolve
    "But I know she'll never miss a day of school no matter what."
    h sleeptalk "Even stopped by her place on the way home, but her folks said she popped out." with dissolve
    stop music fadeout 5.0
    "So I'm sure I'll find..."
    show Hiroko surprised_side at flip
    show Nozomi surprised_side
    $ renpy.transition(dissolve, layer="master")
    show Sayori sleep_concerned at center:
        xpos 1.6
        linear 2.5 xpos 0.75
    s "Mmmrrnn..."
    "... Out."
    play music Measured
    h shocked_side uniform_armup "S-Sayori!" with dissolve
    show Sayori:
        xpos 0.75
    show Hiroko:
        linear 1.0 xpos 0.65
    "I wheel round as her name is called, and I can only watch as Hiroko goes to her, while Sayori practically slumps into her side with a moan."
    h angry_side "What the fuck?! {w=0.5}{nw}" with dissolve
    extend "SNAP OUT OF IT!" with vpunch
    s sleepy "Apol... a-apologies..." with dissolve
    hide Hiroko
    hide Sayori
    hide Nozomi
    "There is some commotion as Sayori walks to her desk with a lumbered gait, Nozomi moving to join Hiroko in assisting their friend to her desk." with dissolve
    "After Mr Kobayashi settles us down, things almost seem to go back to normal."
    "But this isn't normal."
    with blink
    "I know Sayori's got a reputation around here for showing up half-asleep, but what the fuck? We're just continuing class like this?"
    with blink
    play sound schoolbell
    "By the time lunch rolls around, I can't stand it."
    show Sayori concerned at center
    show Nozomi side sad_side at center, flip:
        xpos 0.25
    show Hiroko nervous_side at center:
        xpos 0.75
    "I'm psyching myself up to go over there and... I don't know." with dissolve
    "But something needs to happen."
    h "S-so, uhhh... Sayori. Buddy."
    s sleeptalk_concerned "Urrgh... what is it?" with dissolve
    n frown_side "What happened, Sayori? We weren't going to say anything, but..." with dissolve
    h neutral_side "You seriously started perking up 'til now." with dissolve
    show Sayori at flip
    s surprised "Wh... what do you mean?" with dissolve
    h frown_side "H'yeah, don't think we didn't notice. You were struttin' around here like you had all the energy in the world." with dissolve
    h sad_side "Didn't know what your deal was, but you kinda looked like you were happy." with dissolve
    n sad_side "But then yesterday and... and this." with dissolve
    s sleeptalk "Sorry. I know I must have caused you distress, but please do not worry yourselves over me." with dissolve
    h uniform_armup angry_side "What? {w=0.5}{nw}" with dissolve
    stop music fadeout 5.0
    extend "FUCK that!" with vpunch
    s frown "Hiroko..." with dissolve
    h irritated "Someone's gotta worry, and if it ain't you, then it's gotta be us!" with dissolve
    show Hiroko uniform frown_side
    play music Rain
    n sad_closed "Sayori, we... we know you didn't do as well as you hoped yesterday." with dissolve
    n sad_side "We know this must be hard for you." with dissolve
    show Sayori uniform_folded irritated
    "I can hear Sayori let out a laboured sigh as she pillows her arms on her desk." with dissolve
    s "I can cope. Now please leave me be; I would like to spend the lunch hour here if you don't mind."
    show Nozomi frown_side
    "Both the other girls seem to look at each other, before turning their attentions back on Sayori, slumped in her seat as she is." with dissolve
    hide Nozomi
    show Nozomi front sleep at center:
        xpos 0.25
    n "Sayori... We think you should go home." with dissolve
    s sleeptalk "Nozomi, I..." with dissolve
    s angry_right "You... WHAT?!" with dissolve
    h uniform_headhold2 sleeptalk "Gotta know when to call it quits, sis. You're done for today." with dissolve
    show Hiroko neutral_side
    show Nozomi side sad_side at flip
    s irritated "O-of all the unbelievable..." with dissolve
    "Sayori flaps a hand dismissively as she lets out a weary snort."
    s "Leave me alone. Both of you."
    h sleep "Nah. Not this time." with dissolve
    "And hearing their refusal, Sayori sinks her head against her arms, as if she can sleep through the distractions of their voices."
    s uniform "I only need a nap, so long as you both will not deprive me of it." with dissolve
    h frown_side "Like, shit, Sayori, I get why you're like this. Why you think you gotta BE like this." with dissolve
    h uniform_armup irritated "All that work and dedication, and givin' up everything to chase that big dream at the end..." with dissolve
    h uniform_headhold2 neutral_side "An' even then you're like... what if it still ain't enough?" with dissolve
    h uniform sad_side "What if it's all over and you slogged your guts out for jack shit?" with dissolve
    h nervous_side "Are you gonna be asking yourself \"Did I do everything I could? Or did I slack off?\"" with dissolve
    s concerned "..." with dissolve
    h sleep "So yeah, Sayori. I get it." with dissolve
    stop music fadeout 10.0
    h uniform_armup angry_side "But Jesus fuck, you gotta get over yourself!" with dissolve
    show Nozomi surprised_side
    s panicked "N-nng!" with dissolve
    show Sayori surprised
    "The whole classroom falls silent for a moment. Save for the clack of someone's chopstick hitting the floor." with dissolve
    n "H-Hiroko! What are you saying- {w=1.0}{nw}"
    play music Monologue
    h furious_side "You really think you can show up here every fuckin' day and just ignore what your body's telling you?" with dissolve
    h "Ignore what your fuckin' {nw}"
    extend "FRIENDS tell ya?!" with vpunch
    show Sayori neutral
    "I wasn't the only one interested in what was going on with Sayori, but now literally everyone's stopped what they're doing." with dissolve
    h irritated "Like, shit, Sayori, I get playing through the pain but this ain't it!" with dissolve
    "Hiroko then turns to the rest of us, well aware of our combined gazes."
    show Nozomi sad_closed
    h uniform furious "Ain't anyone else tired of this shit? We're s'posed to pretend miss bookworm killing herself is okay cuz' she's good for the school?" with dissolve
    h "Nah? Just me?"
    show Hiroko angry_side
    "And with that she huffs the air and turns her angry eyes back to Sayori, like we're not worth another second of her time." with dissolve
    show Nozomi sad_side
    "And for Sayori's part, she... I think we're all expecting some well-worded comeback." with dissolve
    "Something to put that pink-headed bitch in her place. Anything to show her she can't talk to you like that."
    s concerned "Hiroko... I- {w=1.0}{nw}" with dissolve
    h frown_side "Just get outta here." with dissolve
    play sound dooropen
    "Just then the classroom door opens as our homeroom teacher strolls back in with his lunch."
    h nervous_side "{size=15}Please?{/size}" with dissolve
    "It's not long before he discerns the tension in the room, as his gaze settles on Sayori and Hiroko staring back at each other."
    "For a moment nobody speaks."
    "But finally Sayori reluctantly turns herself to face him as she starts to talk in a halting voice."
    s sleepy "Mr. Kobayashi, I'm afraid to ask..." with dissolve
    s sleeptalk "But I need to be excused." with dissolve
    stop music fadeout 5.0
    scene bg classroom eve with blink
    "The rest of the school day is uneventful, but for the inevitable muttering about what happened at lunch."
    "Everyone seems to be worried about our star student."
    show phone at right with moveinright:
        ypos 0.346
    "Myself included, of course."
    "As cleaning period ends and we wait to be dismissed, I send Sayori a quick text."
    hide phone at right with moveoutright
    "I don't care about our hypnosis sessions, or the show for the culture fest anymore."
    "I just need her to be okay."
    scene bg k room eve with blink
    play music Eons
    play sound cellvibratelong
    "I've been home for maybe an hour before my phone starts buzzing."
    show phone at right with moveinright:
        ypos 0.346
    "Immediately stopping what I was doing, I rip it out of my pocket and anxiously check the screen."
    "... And I smile."
    stop sound
    ks smile "Sayori!"
    "The voice at the other end of the line replies with a playful, if weary, chortle."
    s "\"My, it sounds like someone's pleased to hear me.\""
    ks "Yeah, I just..."
    "I can feel my cheeks warming up as I stumble on my words."
    "Still not used to talking like this but, dammit, I *want* to talk to her!"
    ks frown blush "How are you holding up?"
    s "\"Better. Better than I had expected, in any case.\""
    s "\"My dad picked me up from the nurse's office. Just one more humiliation I have had to endure lately.\""
    "Hearing that makes me remember what she said last week, about not wanting her parents to find out she missed first period that day..."
    ks noblush "This is Hiroko's fault."
    s "\"Hm?\""
    ks "I can't believe she'd talk to you like that."
    s "\"Do not be upset with her. I understand why she said what she said.\""
    s "\"... Perhaps this is what needed to happen.\""
    ks surprised "Huh? What do you mean by that?"
    "She sighs."
    s "\"Do not worry about it. My dad was surprisingly understanding of my situation, anyway.\""
    s "\"Although he has demanded I take the rest of the week off.\""
    s "\"No study, no school of any kind. Just rest and recreation.\""
    s "\"Quite the punishment for skipping out of school early, don't you think?\""
    "She jokes, but I don't think she put a lot of effort in that delivery. Like she doesn't really believe it."
    "Or she's just that tired."
    s "\"Anyway, I wanted to let you know I'll be fine... No, I *am* fine.\""
    ks smile blush "Yeah, that's... That's great, Sayori."
    "Dammit. There's more I want to say to her."
    "But I guess I should let her go."
    ks "I'll see you next week."
    s "\"Not so fast, Mr. Koyama. I am not quite done with you.\""
    "I can feel the hairs spring from my neck when she says that."
    "Maybe she's not having the best day of her life, but it sure feels like she's getting some of her edge back at least."
    s "\"I will be lying low, but I do want to see you again before the week is out.\""
    s "\"After all, you and I have some unfinished business...\""
    stop music fadeout 5.0
    jump Day14_Con_Kyou_Sayori_Doll

label Day11_Redemption:
    scene bg street1 day with longdissolve
    "It's been a rough few days since that night."
    "Using the penlight wasn't going to make things better, and smashing it to pieces didn't magically help anyone."
    play music Eons
    "But... I have a plan."
    "A stupid... desperate... maybe even suicidal plan..."
    "I feel a lump in my throat just thinking about it, but if I really want to make up for what I did, I'll see it through."
    "This is the best I can do, Hiroko..."
    scene bg classroom2 day with blink
    "First, I still have to show up for class."
    "People scarcely even look my way anymore. The whole room's got this uncomfortable air of resentment caused by my very presence in it."
    show Akiko side uniform_down armband_down sad_side at center
    show Risa uniform neutral_side at center, flip:
        xpos 0.25
    a "Morning, everyone." with dissolve
    "Not even Akiko really acknowledges me anymore."
    r "Yeah. Morning."
    hide Akiko
    hide Risa
    "But I've got more important things to worry about. Like getting through the day." with dissolve
    "Just gotta go through the motions until school is out..."
    scene bg blackscreen with dissolve
    "It both helps and hurts that no one bothers me."
    "I go through my day. I eat lunch alone. I sit through the lessons..."
    "The loneliness gnaws at me but I'll endure, knowing how getting people's attention just makes things so much worse for me..."
    play sound schoolbell
    scene bg classroom2 eve with dissolve
    "Eventually, the day passes and cleaning time arrives."
    "Just a little left to go..."
    scene bg corridor eve with blink
    "I'm cleaning the corridor today, along with a couple others."
    show Akiko side uniform_down armband_down neutral_side
    "Akiko being one of them." with dissolve
    "That conversation we had last time we were on cleaning duty together... It almost feels like a year ago."
    "She's in no mood for talking this time, so I'll... hmm..."
    ks frown "Ugh, this is no good."
    a uniform armband neutral "Uh, what is?" with dissolve
    "Akiko talks to me, but her tone suggests this time it's all business."
    ks sigh "This cleaning cloth's ragged. I need a new one."
    a sleep "Oh..." with dissolve
    show Akiko neutral_side at center
    a "Well. I guess you'd better get a new one, then." with dissolve
    a neutral "Just hurry back." with dissolve
    scene bg blackscreen with dissolve
    "It stings, hearing Akiko so dismissive. But it's all I expected."
    "Risa must have really gotten to her the other day."
    scene bg court eve with dissolve
    "Anyway, I head outside and walk across the tennis courts."
    "Maybe I could've asked one of the other groups if they brought a spare, but I know the changing rooms down here have a cleaning cupboard."
    "I'll get a new cloth from there."
    stop music fadeout 5.0
    scene bg blackscreen with dissolve
    "Let's see... yep, I didn't even need to ask someone to unlock it. I'll just help myself to one, then."
    scene bg court eve with dissolve
    "And now I better rush back before I piss people off even more- {w=1.5}{nw}"
    r "{size=30}Kyou! What are you doing back here?{/size}"
    show Risa uniform_armup angry at center with dissolve
    play music Measured
    "What? Risa?"
    ks surprised "Huh? I was just- {w=0.5}{nw}"
    r frown "{size=30}You're not supposed to be back here!{/size}" with dissolve
    "She must have been cleaning in the changing rooms and followed me out when she noticed me. This could get ugly..."
    ks sigh "I-I'm only here to get another cloth, see? Leave me alone."
    r uniform "{size=30}Not buying it, Kyou. Not today. You're up to something.{/size}" with dissolve
    "She's talking loudly. Accusingly. And it's getting people's attention."
    $t = _("Student #1")
    t "Hey, isn't that Koyama?"
    "There's more people coming out of the changing rooms, and some others are staring at us from inside the main school building."
    $t = _("Student #2")
    t "Just looking at that guy gives me the creeps."
    "Shit. That's a lot of attention..."
    $t = _("Student #3")
    t "What do you think he's doing?"
    ks surprised "I'm... I-I'm not doing ANYTHING!"
    play bgm2 Audience loop
    "I can't even leave, as more and more people start to gather around."
    play sound bodyimpact
    "A-and just then I'm startled as I feel Risa's hands in my pockets!" with vpunch
    ks "R-RISA!"
    show Risa uniform_armup
    "But what's more shocking is when she pulls her hand away from me, gripping something tightly between her fingers." with dissolve
    "It's enough for the people crowded around us to briefly stop in their tracks when they spy what she's holding."
    r angry "Well, isn't that something..." with dissolve
    $t = _("Student #2")
    stop music
    t "{size=30}P-P-...{w=1.0}{/size}{nw}"
    extend "{size=30} PANTIES?!{/size}" with vpunch
    play sound bodyimpact
    play music Rain
    "The gathering crowd were already agitated, but now they're starting to turn violent as I feel someone shove me from the side." with vpunch
    "Meanwhile, Risa hoists those panties in the air for everyone assembled to see."
    r "{size=30}What's it going to take to get this guy out of here, huh?{/size}"
    r "{size=30}How long's he going to keep getting away with harassing us?{/size}"
    r angry_side "{size=30}I say enough is {/size}{nw}" with dissolve
    extend "{size=40}ENOUGH!{/size}" with vpunch
    ks surprised "H-hey WAIT A SEC!"
    stop bgm2 fadeout 5.0
    scene bg blackscreen with dissolve
    "... But my words come to nothing as I'm drowned out in a chorus of angry shouting while I'm pushed to and fro."
    "I'm lucky there were a couple teachers around to break things up before someone threw a punch."
    stop music fadeout 10.0
    pause 2.0
    scene bg principals office eve with longdissolve
    "... Although as I stand here half an hour later, in the principal's office, it's hard to think of myself as fortunate."
    $ t = _("School Principal")
    t "Kyou Koyama..."
    ks surprised "S-... Sir?"
    "The principal himself sits at his desk, looking disdainfully my way as I stand anxiously on the other side, along with a few of my current and former classmates."
    play music Diary
    t "There's a name I was not expecting to hear again so quickly. And yet, here we are."
    "Inhaling sharply, he then mercifully turns his attention towards one of said classmates."
    t "Now I understand you apprehended the... *sigh* panty thief."
    show Risa uniform neutral_side at left, flip
    r "Yes, Sir. I tailed him after I caught him sneaking into the changing rooms." with dissolve
    show Risa frown
    "She shoots a sideways glance at me before she continues." with dissolve
    r frown_side "They were right there in his pocket. I knew he was up to something like this." with dissolve
    t "Do you now, Tachibana? You're someone else I've had to hear about all too recently."
    r uniform_armup concerned_side "Ah... y-yeah, I mean..." with dissolve
    show Risa concerned
    "Another glance my way..." with dissolve
    r uniform concerned_side "My friend Hiroko, in class 3-B, she... s-she was telling me someone had been going through her gym clothes and taking her change of underwear." with dissolve
    r sleeptalk "It started happening since the day Kyou got transferred, so she thought it had to be him, but we couldn't prove it before now." with dissolve
    t "And did either of you relay these specific concerns to a member of staff?"
    show Risa frown_side
    "Risa seems to tense up under the question, but after a pause she has an answer for him." with dissolve
    r uniform_armup concerned_side "No, Sir. Hiroko told me no one would take it seriously anyway so she thought it'd be more trouble than it was worth." with dissolve
    r neutral_side "But yeah, that's why I found it suspicious when Kyou came wandering into those changing rooms." with dissolve
    r frown "And I was right." with dissolve
    t "That will do, Tachibana."
    hide Risa
    "As Risa steps back, our principal centers his gaze on another of my accusers." with dissolve
    t "Watanabe. You had something to say?"
    hide Risa with dissolve
    show Sayori sleeptalk at left, flip
    s "I do, Sir." with dissolve
    "Yeah, Sayori. After the ruckus, Risa told them this was about Hiroko and that her friends should be consulted."
    s neutral "I am not sure if you are aware, but before his transfer, Kyou and Hiroko had a history of feuding in the classroom; dating back to our time as first years." with dissolve
    s uniform_folded concerned "I am afraid it was only a matter of time before he escalated his behaviour and committed some serious harm." with dissolve
    s annoyed "And as you have now seen, removing him from our classroom did nothing to abate his dangerous obsession with her." with dissolve
    s irritated "Indeed, robbed of the ability to harass her during class, Kyou simply became more creative in his efforts to hurt Hiroko." with dissolve
    s uniform annoyed "And it is my opinion that he will continue these escalations even further if he is not stopped." with dissolve
    t "Yes, Watanabe, your opinion is duly noted."
    "He speaks disdainfully, but I have to wonder why he let her mouth off about me for as long as that if he didn't care for her opinion."
    hide Sayori
    t "And you... Akemi, is it?" with dissolve
    hide Sayori with dissolve
    show Nozomi side sad_closed at left, flip
    n "Y- yes, Sir." with dissolve
    t "Why is Homura not with you?"
    n sad_side "She..." with dissolve
    "Yeah, Nozomi's here too. Still as nervous as I've seen her lately."
    n sad_closed "Hiroko doesn't want to be in the same room as him." with dissolve
    t "Understood. Now, do you have anything to add?"
    n sad_side "Yes. I... um, I wanted to corroborate what Risa said, about Hiroko having her panties stolen. She told me as well." with dissolve
    n sad_closed "And all this has really gotten to her, Sir. What Kyou did to make her life a misery... i-it's unforgivable." with dissolve
    n sad "So I hope..." with dissolve
    n frown "I-I hope this school does the right thing and gets this sexual harrassor out of our lives for good!" with dissolve
    hide Nozomi
    "Our principal sighs and holds a hand to his head." with dissolve
    t "I've heard enough. Girls, please go about your day. You are dismissed."
    play sound doorclose
    "The room falls silent for a moment as my three accusers bow stiffly to the principal before seeing themselves out."
    "Leaving me alone with this guy."
    t "So, Koyama. What do you have to say for yourself?"
    ks "I..."
    "What do I have to say?"
    ks neutral "Uh..."
    "Even if I could talk my way out of this, why would I want to anymore?"
    ks sigh "It's true, Sir."
    "My school life's already turned to shit, no matter the outcome here."
    ks frown "I've hated Hiroko since we were first years. She's always mouthing off about me being a creep or something stupid like that. It pissed me off."
    ks "S-so yeah, I wanted to knock her off her perch, you know?"
    "I'll be the creep they all think me to be."
    ks "Maybe I took it too far with the panty-stealing thing, huh."
    t "Well... I find it refreshing that you are not wasting even more of my time by attempting to deny what you've done."
    t "But as administrator of this school I cannot overlook this brazen act of harassment upon another student."
    t "I therefore have no other choice but to issue you with an immediate suspension, pending further review by the school board."
    t "But I can assure you, Koyama, that this will be a formality. The board will recommend your expulsion."
    t "Do you understand the severity of your situation now, Koyama?"
    "I bow my head firmly."
    ks "W-what about my entrance exams? Do I still get to take them?"
    t "There will be arrangements for you to take the exams at home. But make no mistake, this will leave a mark on your record."
    t "And that concludes our meeting, Koyama. We will not meet again."
    stop music fadeout 20.0
    scene bg school ext eve with blink
    "I'm not sure I have any feeling left when I leave that place."
    "I don't even know what to think of what happened back there..."
    scene bg shopping eve with blink
    "But I'm not going home just yet."
    "First I need to make a stop at one of the karaoke bars in town..."
    scene bg blackscreen with fade
    "I've never been in one of these places before, but all I have to do is go up to the counter and tell the clerk my name."
    "And they direct me to a room where I'm expected..."
    scene bg karaoke
    show Sayori neutral_right at center, flip:
        xpos 0.25
    show Nozomi front2 neutral at center
    show Risa neutral at center:
        xpos 0.75
    with longdissolve
    play music Monologue
    ks sigh "... Hey, everyone."
    s sleeptalk "Kyou." with dissolve
    "Yeah. This was always going to be weird."
    show Sayori neutral_right
    ks "U-uhh... thanks for everything back there." with dissolve
    show Nozomi concerned
    r concerned "You're welcome?" with dissolve
    show Nozomi side sad_side at flip
    show Risa concerned_side
    "Nozomi and Risa look to each other, seeming no more at ease now than they were back in the principal's office." with dissolve
    r concerned "You know I wanted you punished for what you did to Hiro, but this doesn't feel like justice." with dissolve
    n sad "Framing you for something like that... Was this really what you wanted, Kyou?" with dissolve
    "I shake my head ruefully."
    ks "I didn't want any of this. But I wanted to help Hiroko come back from what I did to her. You know that, right?"
    s uniform_folded concerned_right "Of course we know that. Even so, this plan of yours..." with dissolve
    "Yeah, Sayori. It was stupid, desperate and probably suicidal to my career prospects. I know."
    s sleeptalk_concerned "It felt insane to go along with it." with dissolve
    ks neutral "But you thought it would help, right?"
    show Sayori concerned_right
    hide Nozomi
    show Nozomi front2 concerned at center
    "Sayori nods." with dissolve
    s "And I still do. I believe if Hiroko submits an appeal to the scholarship board, they will take these extenuating circumstances into account."
    s concerned "There would be little doubt that your harassment contributed to Hiroko's mental decline and her failure to distinguish herself at the tournament." with dissolve
    s annoyed_right "Hiroko will get another chance, I have little doubt of that." with dissolve
    n side sad "That's good. But was it really okay for you to destroy your immediate future? Just for a chance to save Hiroko's?" with dissolve
    ks sigh "Well... I-it's too late for second-thoughts now, huh?"
    n sad_side "Yeah..." with dissolve
    s uniform concerned "That's right. Kyou is fully committed to this reckless gambit, and we have committed to support him. For Hiroko." with dissolve
    r uniform_armup concerned_side "Right. For Hiroko." with dissolve
    s uniform_handup concerned_right "And for what it's worth, Kyou... I do believe I owe you an apology." with dissolve
    show Risa surprised_side
    show Nozomi surprised_side
    ks surprised "Huh?" with dissolve
    r frown_side "Yeah, Sayori, what are you apologizing for?" with dissolve
    show Nozomi sad_side
    s neutral "A week ago, when this whole nonsense began, I called him \"irredeemable filth\"." with dissolve
    show Risa neutral_side
    show Nozomi sad
    s uniform_folded sleeptalk "For you to go this far to make amends... I never thought you had it in you, Kyou." with dissolve
    s concerned_right "So I am sorry for doubting your sincerity that day, and I take those words back. Again, for what it's worth." with dissolve
    show Sayori annoyed
    "That must be the nicest thing anyone's said to me all week, but Sayori turns her attention to the others before I can even thank her for it." with dissolve
    show Nozomi sad_side
    s "Now, I want to be clear to both of you that our roles in this deception we played today are not over." with dissolve
    "Nozomi nods solemnly."
    show Sayori neutral
    n sad_closed "Right. We still need to act like we believe what we said back there." with dissolve
    s uniform_handup "Good. Only the five of us, Hiroko included, know the true story of the \"panty thefts\"." with dissolve
    s concerned "If word got out to the faculty that this scandal was fabricated we could all be in serious trouble, and Kyou's sacrifice will have been for nothing." with dissolve
    r uniform concerned "Yeah, message received. We got your back on this, Kyou." with dissolve
    s uniform_folded concerned_right "And as for you, Kyou..." with dissolve
    ks neutral "Yeah?"
    show Nozomi sad
    s sleeptalk "Good luck for the future. I mean it." with dissolve
    s uniform neutral_right "If you need any help preparing for your entrance exams, I may be able to offer some assistance." with dissolve
    "I smile at her in thanks. It's a small thing, but winning her respect does feel nice after everything that's happened."
    stop music fadeout 10.0
    scene bg shopping eve with blink
    "But as I leave the karaoke place, it's a feeling that quickly dissipates."
    "I can win the respect of those girls all I want. I still need to keep this deception going."
    "I'm still walking alone."
    scene bg k bedroom eve with blink
    "I'm still... alone."
    "Was it even worth it? Right now it's hard to think I made a difference today, and I gave up everything I had left."
    "What's going to happen to Hiroko now? It's maddening that I don't know."
    "... What's even going to happen to me?"
    scene bg blackscreen with longdissolve
    pause 2.0
    jump Epilogue_Redemption_Sacrifice
