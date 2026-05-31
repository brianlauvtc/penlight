label Day4_NonCon_Kyou:
    scene bg street1 day with longdissolve
    ks sigh "*yawn*"
    play music Memories
    "Maybe I did a little TOO much thinking last night."
    "I've barely been keeping up with schoolwork as it is; my hypnosis self-learning on top of everything else is killing me."
    "But this'll all be worth it if I can just push through..."
    scene bg classroom day
    show Hiroko uniform frown at center
    show Sayori frown_right uniform_folded at left, flip:
        xpos 0.1
    with blink
    "When I arrive, I find a certain pair waiting by my desk."
    h "Stay the fuck away from us."
    ks confused "Excuse me? This is my desk."
    h angry "I still don't know what you got on Nozo, but from now on you keep your fuckin' distance, you hear me?" with dissolve
    "The fucking nerve of these people. Why don't they mind their own business?"
    "Still, it was hard not to see this coming, and I thought about how I'd deal with something like this."
    ks concerned "Look, I'm sure there's just been a big misunderstanding. Why don't we have a proper talk about this later?"
    ks "Maybe find someplace quiet and I'll explain everything? Let's be reasonable here."
    s irritated "We don't need this, Kyou. We don't need you. I know you are worked up about Nozomi but you need to let her go." with dissolve
    show Sayori frown_right
    h uniform_armup angry vein "Right? We don't need this bullshit in our lives; {w=0.2}we got enough crap to deal with without {nw}" with dissolve
    extend "YOUR creepy ass to worry about again!" with vpunch
    "Making a pained expression, I direct my attention to the moody tennis girl."
    show Hiroko uniform frown novein
    ks concerned "Hiroko. I don't know what you think I've done, but I really was just trying to reach out." with dissolve
    ks "It's just... We don't have much time left at school and I was just thinking how... I'm going to graduate with no friends from this place at all."
    s rolleyes "As if that is somehow our fault." with dissolve
    ks sigh "And although I'm used to being alone, I just... I realized I couldn't bear to graduate friendless and alone. That'd be just too sad."
    show Sayori frown_right
    ks "So yes, I started talking to Nozomi, and trying to make friends with her friends... do you really think I've messed up so badly that we can't ever be close?" with dissolve
    show Hiroko annoyed uniform_armup
    play sound schoolbell
    "Hiroko lets out a sigh of irritation as the bell rings for lessons to start." with dissolve
    h "Fine. We'll talk after school, but don't think this'll change anything. Got it?"
    s frown "\"We\"? Do I not get a say in this?" with dissolve
    h frown_side uniform "Oh, come on Sayori. Tell me you don't wanna know what creepo thinks he can say to us that's gonna make all of this better." with dissolve
    s uniform irritated "This is a waste of time. He is not going to convince us." with dissolve
    h uniform_armup annoyed "Right? So we let him say his piece and then he can fuck off forever." with dissolve
    s rolleyes "Well... you will insist." with dissolve
    show Hiroko uniform frown
    s uniform_folded neutral_right "Very well, Kyou. We will have this talk after school. Just the three of us." with dissolve
    ks smile "I just want a chance to change your minds, that's all I'm asking."
    s uniform sleeptalk "Uh-huh." with dissolve
    hide Hiroko
    hide Sayori
    with dissolve
    "And with that the pair of them return to their desks, leaving me to breathe a little sigh of relief."
    "In all my planning last night, the one thing I didn't settle on was who needed the most convincing."
    "Hiroko is obviously going to be in my face anytime I give her an excuse. No change there."
    "While Sayori... I have no idea what she thinks she can do to me. That girl is seriously messed-up."
    "I need to decide before the end of the day."
    menu:
        "Approach Hiroko":
            $pursued = "Hiroko"
        "Approach Sayori":
            $pursued = "Sayori"
        "Approach Nozomi":
            $pursued = "Nozomi"
            "But after thinking about it, maybe I don't need to convince either of them after all. It's not like they can watch me all day long."
            "And whatever I have going between Nozomi and me is none of their goddamned business."
    "This is all going to work out."
    "With my plan set in motion, I keep my head down for the rest of the day."
    with blink
    "Lunch comes and goes. Nozomi's group headed to the roof again today and I could've sworn she looked a little wounded when she realized I wouldn't be joining them."
    if pursued != "Nozomi":
        scene bg corridor eve with blink
        play sound schoolbell
        stop music fadeout 5.0
        "As homeroom is dismissed, I meet up with Hiroko and Sayori in the corridor."
        play music Downtown
        show Hiroko
        show Sayori neutral_right at left, flip:
            xpos 0.1
        with dissolve
        ks concerned "Hiroko? Sayori? Something's come up."
        h frown "What?" with dissolve
        ks sigh "Family emergency. We'll need to do this later."
        show Sayori concerned_right
        h uniform_headhold2 nervous "Huh? Oh." with dissolve
        s uniform_handup "I am... sorry to hear that, Kyou." with dissolve
        ks "Yeah, so I'll see you later."
    else:
        scene bg classroom eve with blink
        stop music fadeout 5.0
        "As the day nears its end, cleaning time arrives and most of us file out of the classroom to take on our assigned chores."
        scene bg corridor eve with blink
        play music Downtown
        show Nozomi front at center with dissolve
        pause 0.8
        hide Nozomi with dissolve
        "While I'm cleaning the corridor outside class today, I spy Nozomi slipping into the ladies' bathroom."
        "Seems I memorized the cleaning schedule correctly today; she's cleaning in there alone."
        "As everyone busies themselves with their own duties, I sneak into the bathroom the first chance I get."
        scene bg bathroom
        stop music fadeout 5.0
        show Nozomi front surprised
        with dissolve
        n "Kyou?! What are you doing here?"
        if persistent.NewSprite == " New":
            $light_x = 0.43; light_y = 0.25; ldirection = "right"; lnumber = 1
        else:
            $light_x = 0.43; light_y = 0.26; ldirection = "right"; lnumber = 1
        call lightshow from _call_lightshow_88
        ks "Shh, Nozomi. That's not important."
        call lightshow from _call_lightshow_89
        play music Flow fadein 5.0
        "My penlight was already in my hands and switched on as I walked in on a startled Nozomi."
        call lightshow from _call_lightshow_90
        ks "What's important is that you watch the light, like always."
        call lightshow from _call_lightshow_91
        show Nozomi drowsy
        ks "Watching the light, naturally feeling your eyelids close, and..." with dissolve
        call lightshow from _call_lightshow_92
        ks "Sleep, Nozomi."
        show Nozomi sleep
        "I quickly reach out to steady her as she drops. And just as I hoped, she's extremely good at dropping for me now." with dissolve
        ks "Very good. It feels so good to drop, Nozomi. So good to drop and to listen and to accept what I have to say."
        ks "Doesn't it, Nozomi?"
        n "Mhm..."
        "Your friends really don't understand, do they Nozomi."
        "You want this as much as I do."
        ks "That's right. That's why when I say you need to visit my home at 10 o'clock this Saturday morning, you accept how natural it is that you need to do just that."
        ks "Isn't that right, Nozomi?"
        n sleeptalk "Right..." with dissolve
        show Nozomi sleep
        ks "Very right. Now, in a moment I want you to count slowly from one to five in your head, and just as you reach five you will awaken and return to your chores." with dissolve
        ks "And as you do so, you will forget that you saw me here, or that you fell into this deep trance."
        ks "Understand, Nozomi?"
        n sleeptalk "I understand." with dissolve
        show Nozomi sleep
        ks "Wonderful. Start counting now." with dissolve
        stop music fadeout 5.0
        scene bg corridor eve with fade
        "I quickly slip back out, confident that she'll follow my words to the letter, and hurriedly get on with my own cleaning."
        scene bg corridor eve with blink
        play sound schoolbell
        play music Downtown
        "Once homeroom is dismissed, I meet up with Hiroko and Sayori in the corridor."
        show Hiroko
        show Sayori neutral_right at left, flip:
            xpos 0.1
        with dissolve
        ks sigh "So, uhh..."
        s uniform_folded frown_right "We are waiting, Kyou." with dissolve
        h frown "Yeah, we're just dying to hear more of your bullshit." with dissolve
        "Okay, I hadn't planned to actually talk to these two both at once."
        "I guess I'll wing it?"
        ks "S-so okay, like I was saying, I don't want to graduate from here without any friends."
        h "You did say that, yeah."
        ks "And, uh... I'm sorry? If I offended any of you earlier?"
        s "..."
        ks confused "Is there anything I can do to... like, make amends with you two?"
        h annoyed uniform_armup "... Is this all you've got?" with dissolve
        ks "W-well, I... it's not enough?"
        s annoyed "Please leave us alone, Kyou. We're not obligated to be on friendly terms with you and we do not appreciate your intrusion into our lives." with dissolve
        ks neutral "Fine... But neither of you speak for Nozo."
        h angry "Leave her the {nw}" with dissolve
        extend "FUCK alone, Kyou. We're serious!" with vpunch
        show Hiroko frown
        "I just give them a weary sigh and hold up my hands." with dissolve
        ks sigh "Okay fine, you win. I won't approach her anymore if that's what you want. I can't see how I can without you two breathing down my neck anyway."
        h smirk "That's right. We'll be watching." with dissolve
        ks "I'll just... try and make friends with someone else, I guess."
        s frown_right "I do hope this is the end of things, Kyou. I would hate to have to escalate this further." with dissolve
        h frown "So, we're done here? Cool. I'm off to practice." with dissolve
        h uniform_arm uniform "Thanks for wasting our time, Kyou." with dissolve
        hide Sayori
        hide Hiroko
        "And with that the two of them leave me be." with dissolve
        stop music fadeout 10.0

    scene bg k bedroom eve with blink

    if pursued == "Hiroko":
        "Of course nothing happened. I just didn't want to talk to both of them at once; I'll be far more convincing one to one."
        scene bg k bedroom night with blink
        "Instead I wait for the day to draw on, watching the clock."
        "About 7:30. Time to head outside."
        scene bg street1 night with blink
        "Besides her mouthiness, what I know of Hiroko is that she's been dedicating herself to her tennis, in aid of some tournament or other."
        "She's most likely still practicing on the tennis courts until the school kicks her out. So I'll slip back into school, head to the courts and..."
        scene bg court night
        show Hiroko frown tennis_armup tennis_arm
        with blink
        "Sure enough, I find Hiroko practicing serve on the floodlit courts by herself." with dissolve
        h surprised no_arm "Kyou!? What the hell?" with dissolve
        ks casual neutral "Hey, Hiroko. Think we can talk now?"
        h annoyed "Seriously? Of all the times to pick..." with dissolve
        ks "You need to finish practice anyway, right? I'll help you pack up and then we can talk."
        show Hiroko frown
        "Hiroko glares at me as she catches her breath." with dissolve
        h "I dunno what your game is but yeah, I gotta wrap this up."
        h annoyed tennis "Help me pick up all these balls." with dissolve
        "Hiroko and I each walk around the court grounds, bag in hand, to scoop up a few dozen tennis balls off the floor."
        h neutral "Anyway, how's things at home?" with dissolve
        ks surprised "Huh?"
        h "You said something about an emergency, didn't you?"
        "Oh... right, I did say that."
        ks chuckle "Ah, it's fine. Wasn't a big deal in the end so panic over."
        h frown "...'Kay." with dissolve
        "Having seemingly gathered everything, Hiroko slings her ball bag over her shoulder and heads to the storage shed, not looking back as I follow her inside."
        scene bg sports storage
        show Hiroko tennis
        with blink
        "As we set the bags down, I take the chance to speak up."
        ks casual neutral "Okay. Let's talk in here."
        h frown "Here? Why here?" with dissolve
        ks "Thought we could do with some privacy. No one's going to come over this way."
        h irritated vein tennis_armup "You're unbelievable. Like, who gives a shit if people are listening to this? We're just talking." with dissolve
        ks smile "Well we're here now, right? So anyway..."
        scene cg sports shed night
        $h = DynamicCharacter("hiroko_name", image = "HirokoHypno", who_color = "#FF89AB") #Hiroko Homura
        show HirokoHypno upright tennis clenched_fists_tennis frown
        with blink
        show penlight at right with moveinright:
            ypos 0.346
        $light_y = 0.3
        "I choose this time to take out the penlight from my pocket and switch it on."
        hide penlight with moveoutright
        h angry "What're you doing {nw}" with dissolve
        extend "NOW?" with vpunch
        ks casual smile "I like to play with it while I'm talking. It relaxes me."
        call cglightshow from _call_cglightshow_135
        "As I finish my sentence, I make a point to sweep the beam across her eyes. I'm getting good at working this thing."
        h annoyed_up "Urgh...  see, this is why you don't have any friends, dude." with dissolve
        call cglightshow from _call_cglightshow_136
        "Ignoring her, I pass the beam across her face a second time." with dissolve
        ks neutral "I'm sure if you focused, Hiroko, this would be relaxing for you too."
        call cglightshow from _call_cglightshow_137
        h angry_up "Like, what is it with you and creepy weird shit?" with dissolve
        # h "Just when we were all like \"This dude never talks to anyone, stays in his little corner, he must be some real creepy fucker.\""
        call cglightshow from _call_cglightshow_138
        ks "Focus for me, Hiroko, and as you focus, notice the pattern forming in your eyes."
        call cglightshow from _call_cglightshow_139
        h "You come out here and you waste my time and will you {w=0.2}{nw}"
        show HirokoHypno angry
        extend "KNOCK THAT OFF!" with vpunch
        call cglightshow from _call_cglightshow_140
        ks "Stare at it, Hiroko. Stare at the pattern and feel it relax you, feel your eyelids become heavy as you relax."
        call cglightshow from _call_cglightshow_141
        h angry_up "You even listening to me, Kyou? 'Cause all I'm hearing from you is some crazypants garbage." with dissolve
        call cglightshow from _call_cglightshow_142
        stop music fadeout 10.0
        ks "Becoming heavier and heavier, with every blink."
        call cglightshow from _call_cglightshow_143
        show HirokoHypno straining relaxed_fists_tennis
        $ renpy.transition(longdissolve, layer="master")
        ks "Heavier with every blink. Sleepier with every blink."
        call cglightshow from _call_cglightshow_144
        h "What.. what are you even saying? What's going on..."
        call cglightshow from _call_cglightshow_145
        ks "Shh, it's alright Hiroko. It's perfectly fine to be so sleepy, so relaxed, in my presence."
        call cglightshow from _call_cglightshow_146
        $ renpy.transition(longdissolve, layer="master")
        h relaxed sleepy_up_open "No it's... not...  shut up..."
        "So she says, but just like Nozomi, she doesn't appear to be too interested in stopping this."
        show HirokoHypno relaxed sleepy_up_closed
        "Maybe a little hesitant since, after all, this is all a little sudden for her." with dissolve
        "So perhaps all I need to do is put her mind fully at ease."
        call cglightshow from _call_cglightshow_147
        ks "Fighting it is natural, Hiroko. Because you're scared."
        call cglightshow from _call_cglightshow_148
        ks "It's fine to be scared, but- {w=0.7}{nw}"
        h sleepy_up_open "Not scared... I'm not scared... never be scared of you..." with dissolve
        call cglightshow from _call_cglightshow_149
        show HirokoHypno sleepy_up_closed
        ks "That's... right, Hiroko. There's no need to be scared of feeling sleepy near me, being so relaxed." with dissolve
        h sleepy_up_open "That's not what... what I..." with dissolve
        show HirokoHypno sleepy_up_closed
        "That telltale flicker of the eyelids... this is just like my time with Nozomi." with dissolve
        "She really is going for this, just like her friend."
        call cglightshow from _call_cglightshow_150
        ks "Shh, Hiroko. There's no need to explain. Just relax, eyelids getting heavier. Getting heavier."
        call cglightshow from _call_cglightshow_151
        ks "Feeling so relaxed. Feeling so sleepy."
        show HirokoHypno arm_uniform_tennis
        "Hiroko starts to wobble on her feet, prompting me to step towards her and hold her with one arm, just as I did with Nozomi." with dissolve
        ks "Sleep, Hiroko."
        play music Flow
        show HirokoHypno drooping sleep no_arm
        $ renpy.transition(longdissolve, layer="master")
        "Her eyelids flutter closed for good this time, and I take a second to look her over before speaking again."
        "If she were always this peaceful around me I might be able to stand her."
        ks smile "Can you hear me, Hiroko?"
        h sleeptalk "Yeah..." with dissolve
        show HirokoHypno sleep
        ks "That's right, Hiroko. You can hear me, and you need to listen to everything I say. It's very important that you listen and accept everything you hear." with dissolve
        play sound doorclose
        "I take a furtive glance around me to make sure we weren't seen, then pull the door closed."
        "It doesn't seem likely anyone will be coming this way for a while."
        ks "You must forget anything weird that happened in our meeting together."
        ks "Nothing weird happened, Hiroko. You didn't even imagine anything weird that may have happened. Nothing in the least bit weird occurred."
        ks "That's right isn't it, Hiroko?"
        h sleeptalk "Right... nothing weird..." with dissolve
        show HirokoHypno sleep
        ks "That's right, Hiroko. We had a perfectly normal chat together and you realized there was nothing strange or dangerous about me." with dissolve
        ks "After all, you're calmly listening to my words right now."
        ks "Feeling so relaxed listening to me. Feeling so peaceful."
        ks "So it's perfectly logical to realize I'm relaxing and safe to be around. Isn't that right?"
        h sleeptalk "Right..." with dissolve
        show HirokoHypno sleep
        ks "Therefore, there's nothing at all wrong if I want to spend time with Nozomi, or you, or anyone I choose. Is there?" with dissolve
        h sleeptalk "No... nothing wrong..." with dissolve
        show HirokoHypno sleep
        "Just like with Nozomi, I'm amazed with how easily I can convince her to see things my way." with dissolve
        "For that to have worked on her it must be that she never had a serious reason to hate me in the first place."
        "I guess she's just always hated me irrationally. But now we've reached an understanding, maybe I can do a little more convincing..."
        # "That should take care of this particular problem. Although maybe I can push my luck a little bit..." with dissolve
        ks "Nothing wrong at all. On the contrary, you would love me to spend time with you or your friends, since I'm so relaxing and safe to be with."
        ks "It's perfectly natural, perfectly correct to feel this way about me... isn't that right, Hiroko?"
        h sleeptalk "Right..." with dissolve
        show HirokoHypno sleep
        ks "It's very right, Hiroko." with dissolve
        "Heh. Guess she was just hiding that she liked me all along. What a childish girl."
        "If that's really the case then I'm glad I took care of that nonsense."
        "But then, if that's true maybe I can fully convince her of how irrational she's being?"
        "She doesn't have to be the moody little bitch she projects to the world. She could be honest about who she truly is deep down..."
        # "And then I guess I'm feeling cocky, because I think I can do better than this."
        # "I mean, if anything the little bitch should thank me for what I'm about to do."
        ks "Feeling so relaxed. Feeling so peaceful. It's a wonderful feeling, isn't it Hiroko?"
        h sleeptalk "Yeah..." with dissolve
        show HirokoHypno sleep
        ks "So wouldn't it be great if you could feel this relaxed and peaceful all the time?" with dissolve
        h sleeptalk "Yeah..." with dissolve
        show HirokoHypno sleep
        ks "You're right, Hiroko. It would be. So why not take all your anger, all your negativity and make it all disappear; as much as you can." with dissolve
        #add sleeptalk concerned
        h sleeptalk blush "I... I can't... I need to..." with dissolve
        show HirokoHypno sleep
        "A little pushback? Well, it's only natural I suppose. That angry facade has been her way for so long, after all." with dissolve
        ks "You need to let it all go, Hiroko. I know you can do it. I know from our chat how much you really want to feel so relaxed, so at ease, all the time."
        ks "All that anger you show isn't who you are. You don't need to pretend anymore."
        h sleeptalk "Can't let go... need to be angry... s-sometimes..." with dissolve
        show HirokoHypno sleep
        "Maybe I'm reaching the limits of what I can do with her. But it feels like I still have plenty of time, unlike my sessions with Nozomi." with dissolve
        "I could keep pursuing this..."
        # "But I'm sure I still have plenty of time before anyone thinks to look for Hiroko." with dissolve
        ks "You're doubting yourself, Hiroko. But remember, you're not scared. Why should you be scared?"
        h sleeptalk "I'm not scared..." with dissolve
        show HirokoHypno sleep
        ks "No, Hiroko. You're not. So there's no need to hold on to your anger or your negativity, because there's no need to be scared. You're not scared to let go." with dissolve
        h sleeptalk "Not scared..." with dissolve
        show HirokoHypno sleep
        ks "That's right, Hiroko. So let it all go, and let yourself be so peaceful, so relaxed, so carefree." with dissolve
        h sleeptalk "N... no..." with dissolve
        show HirokoHypno sleep
        ks "All that anger. All that negative attitude. All going." with dissolve
        h "..."
        ks "All going."
        h noblush "..." with dissolve
        ks "All gone."
        h sleeptalk "All gone..." with dissolve
        show HirokoHypno sleep
        ks "That's right, Hiroko. And in a few moments I'm going to wake you up and let you continue being this peaceful and relaxed." with dissolve
        ks "I'm going to count to five, and as I count you will return to a waking state until on five, you will completely awaken."
        ks "And as you awaken, you will realize we reached the end of our conversation and apologize for your earlier rudeness towards me."
        "I think she'll agree that's the least she owes me, after all her irrational bullshit towards me."
        ks "Do you understand, Hiroko?"
        h sleeptalk "Yeah..." with dissolve
        show HirokoHypno sleep
        ks "One... forgetting you were ever hypnotized, knowing that nothing weird happened today in your mind or in reality." with dissolve
        ks "Two... knowing that we chatted, and that you realize I am safe and relaxing to be around, and not a danger of any kind."
        stop music fadeout 10.0
        ks "Three... feeling you would love to spend more time around me."
        ks "Four... losing all your anger and negativity, leaving it far behind where it belongs."
        ks "Five."
        $ renpy.transition(longdissolve, layer="master")
        h relaxed sleepy_up_open "Mm..."
        ks "Hiroko? You looked like you were about to say something."
        $persistent.sports_shed_night_unlock = True
        scene bg sports storage
        $h = DynamicCharacter("hiroko_name", image = "Hiroko", who_color = "#FF89AB") #Hiroko Homura
        show Hiroko tennis smile blush at center
        with blink
        play music Beautiful
        h smile blush "Yeah, I just... I wanna say sorry for being such a butt to you before. I dunno where all that came from." with dissolve
        "I can feel my lips contorting into the widest grin."
        ks casual chuckle "It's fine, Hiroko. So are we good?"
        h tennis_armup happy noblush "Oh my gosh, yeah, Kyou! Totally~" with dissolve
        h "Nozo was right about you, you really are a good person once you open up."
        h smile "And seriously, dude, I take it all back. You come hang with us whenever you want~" with dissolve
        h blush affectionate tennis_arm "Or just you and me, y'know... just putting that out there." with dissolve
        ks "O-of course. We'll meet up again."
        h happy "I mean, if you're not doing anything tonight why don't we keep this going? Grab a bite someplace." with dissolve
        "Oh man, she's really letting her guard down now. That's kinda cute?"
        "Damn, I can feel myself blushing..."
        ks happy "Eheh... T-tempting, but I have other plans tonight. Anyway, we need to get out of here."
        h surprised "Oh man, you're right. We're gonna get locked in here if we don't move it." with dissolve
        scene bg ext school night
        show Hiroko tennis smile
        with blink
        "We lock up, then hurry back out to the school gates."
        ks casual smile "Alright. See you tomorrow, Hiroko."
        h happy "Lookin' forward to it~" with dissolve
        scene bg k bedroom night with blink
        stop music fadeout 5.0
        "I continue to amaze myself."
        "Every time I talk to one of the girls using my new gadget I feel more confident. More alive."
        "I mean, just thinking about all the things I said... I never could've said those things to anyone a week ago."
        "This whole experience is making me a better person."
        "And with what Hiroko and I worked out, clearly I can help those around me become better too."
    elif pursued == "Sayori":
        "Of course nothing happened. I just didn't want to talk to both of them at once; I'll be far more convincing one to one."
        "Instead I wait for the day to draw on, watching the clock."
        "About 5:15. Time to head outside."
        scene bg street1 eve with blink
        "Sayori is a bit of an enigma for the most part, but her schedule is easy to figure out."
        "School, then study, then cram school, then homework and probably more studying until she passes out in her room. That girl is all work and no play."
        scene bg ext school eve with blink
        "At this time of day she's almost certainly still in school, heading the study club."
        scene bg corridor eve with blink
        "When I arrive I listen outside her club room. She seems to be the only one still inside, so I may as well head in..."
        scene cg study room eve
        show SayoriHypno standing uniform_slumped noface
        $scg = Character("%s"%sayori_name, image = "SayoriHypno", who_color = "#385599")
        with blink
        scg "..."
        ks confused "Uh... did I come at a bad time?"
        $ renpy.transition(longdissolve, layer="master")
        scg uniform_handsout drowsytalk "Mhrm... Kyou?"
        show bg study room eve
        show Sayori panicked_right at center:
            ypos 1.5
            linear 2.0 ypos 1.0
        with blink
        s "... K-Kyou!? What are you doing here?" with vpunch
        show Sayori panicked_right:
            ypos 1.0
        "Seems I literally caught her napping. Is this something she normally does in here?"
        "... Anyway, I'm getting distracted. Time to go with what I rehearsed on the way over."
        ks concerned "I... thought about what you said yesterday. About me wasting my potential?"
        s frown_right "And you are telling me this now?" with dissolve
        s frown "Just as the rest of my club has gone home for the day and I myself was about to leave for cram school?" with dissolve
        s annoyed_right uniform_folded "You have a peculiar sense of timing..." with dissolve
        ks "Well, I could... see how important it was to you, and..."
        ks "And I meant what I said about wanting to be friends with Nozomi's friends and-{w=1.5}{nw}"
        stop music fadeout 5.0
        s irritated "Let me stop you right there." with dissolve
        s annoyed "If any of that were true, you would not have found a way to exclude Hiroko from this little chat we are now having." with dissolve
        s annoyed_right "Nor would you be doing it at a time that anyone would be able to tell seriously inconveniences me." with dissolve
        s uniform "And that is before we consider the fact that your \"family emergency\" from earlier seems to have been completely forgotten." with dissolve
        s scowl "So allow me to make up for my friend's absence and say you are full of shit." with dissolve
        queue music Night_Road
        "I didn't expect my little white lie to hold for very long but damn, she saw right through me."
        "But even so, she might still appreciate what I'm about to show her, right?"
        # "S-she's still alone so I should be able to hypnotize her, right?"
        "Right?"
        s annoyed "Now Kyou, I am running on about three hour's sleep so I really don't have the patience for this." with dissolve
        s sleeptalk "Some of us have things to do." with dissolve
        "Now that she mentions her lack of sleep, I can't help but notice how completely shattered she looks."
        "Sayori's commitment to all-night study sessions is legendary, but these last few days have really allowed me to realize just what that means."
        scene bg blackscreen with dissolve
        "Even when she tries to push past me I note her slow, laboured blinking..."
        "Her sluggish, uneven gait..."
        scene DelusionStruggleSayori with dissolve
        "The feebleness of her hand as she attempts to shove me aside..." with vpunch
        s "Out of the way!"
        "I can't let her go like this. She'll never admit it on her own, but she needs help."
        show DelusionStruggleSayori sayori_struggling s_angry_up_flash with dissolve
        show DelusionStruggleSayori sayori_struggling s_angry_up with dissolve
        s "Eh?"
        show DelusionStruggleSayori sayori_struggling s_angry_up_flash with dissolve
        show DelusionStruggleSayori sayori_struggling s_angry_up with dissolve
        "And I can give it to her, if she'll let me."
        show DelusionStruggleSayori sayori_struggling s_angry with dissolve
        s frown_right "Is this part of your great plan? Blinding me?" with dissolve
        show DelusionStruggleSayori sayori_struggling s_angry_up_flash with dissolve
        show DelusionStruggleSayori sayori_struggling s_angry_up k_concerned with dissolve
        k "Sayori, you're dead on your feet."
        show DelusionStruggleSayori sayori_struggling s_angry_up_flash with dissolve
        show DelusionStruggleSayori sayori_struggling s_angry_up with dissolve
        s "Insulting me is not going to help your cause. Now move before you make me late."
        show DelusionStruggleSayori sayori_struggling s_angry_up_flash with dissolve
        show DelusionStruggleSayori sayori_struggling s_angry_up with dissolve
        "She might say that, but I can't help but notice how quickly her tired attentions have been grabbed by the light in my hand as I pass it back and forth."
        # "Worried she might topple over almost immediately, I make a move to wrap an arm around her shoulders as I continue to pass the penlight back and forth."
        k "There's no need to worry about that, Sayori. Just focus on the light flashing before your eyes."
        stop music fadeout 10.0
        show DelusionStruggleSayori sayori_struggling s_angry_up_flash with dissolve
        show DelusionStruggleSayori sayori_struggling s_angry_up with dissolve
        show DelusionStruggleSayori sayori_struggling s_angry
        s scowl "G-get off me!" with vpunch
        k "Let the light and its patterns distract you, Sayori. Just for a little while."
        show DelusionStruggleSayori sayori_struggling s_angry_up_flash with dissolve
        show DelusionStruggleSayori sayori_struggling s_worried with dissolve
        s concerned_right "I don't... {w=0.5}I don't understand, why can't I look away-{w=1.3}{nw}" with dissolve
        show DelusionStruggleSayori sayori_struggling s_worried_flash with dissolve
        show DelusionStruggleSayori sayori_struggling s_worried k_calm with dissolve
        k "It's alright, Sayori. There's nothing wrong with looking. Nothing wrong with staring."
        show DelusionStruggleSayori sayori_struggling s_worried_flash with dissolve
        show DelusionStruggleSayori sayori_struggling s_worried with dissolve
        k "Nothing wrong with letting your eyelids relax, or with letting them close."
        show DelusionStruggleSayori sayori_struggling s_worried_flash with dissolve
        show DelusionStruggleSayori sayori_struggling s_worried with dissolve
        show DelusionStruggleSayori sayori_relaxing
        $ renpy.transition(longdissolve, layer="master")
        s sleepy uniform "H.. how are you doing this... I can't..."
        show DelusionStruggleSayori sayori_relaxing s_worried_flash with dissolve
        show DelusionStruggleSayori sayori_relaxing s_sleepy
        $ renpy.transition(longdissolve, layer="master")
        k "It's alright, Sayori. There really is no need to worry."
        show DelusionStruggleSayori sayori_relaxing s_sleepy_flash with dissolve
        show DelusionStruggleSayori sayori_relaxing s_sleepy with dissolve
        k "You've been neglecting your health for so long. Don't you owe it to yourself to take a breather once in a while?"
        s "A..ah..."
        $persistent.delusion_struggle_sayori_unlock = True
        scene bg blackscreen with dissolve
        "As Sayori wobbles on her feet more and more, I manoeuvre her towards the chair she was just sitting on before passing the penlight across her face one more time."
        "And then quickly lowering her down into the seat and raising my voice a tad to speak in a firm, commanding tone."
        scene bg blackscreen with dissolve
        show cg study room eve:
            ypos -0.3
            linear 0.2 ypos 0.0
        show SayoriHypno standing surprised:
            ypos -0.3
            linear 0.2 ypos 0.0
        ks frown "Sleep!{w=0.5}{nw}"
        # show Sayori panicked_right
        # pause 1.0
        show SayoriHypno drooping sleep with dissolve
        pause 0.5
        play music Flow
        scg "..."
        ks smile "Very good, Sayori. Falling deep now. So nice and deep. Very good."
        ks "But I still need you to be attentive to my words. Do you think you can do that, Sayori?"
        scg "..."
        "... Given her physical state I do have to wonder now if she's literally aslee-{w=1.0}{nw}"
        scg sleeptalk "Uh-huh..." with dissolve
        show SayoriHypno sleep
        "Oh, good. She's still with me. And very much willing to be a part of this, I notice." with dissolve
        ks "That's very good, Sayori. It's extremely important that you listen and accept everything that you hear from me."
        ks "Feeling so peaceful, so relaxed, so safe here with me. In this deep, deep sleep."
        scg sleeptalk "N.. no..." with dissolve
        ks frown "No?"
        scg "You are... dangerous..."
        "Even though she allowed herself to fall into a trance, she's not completely letting go. Not yet, anyway."
        show SayoriHypno sleep
        "I need to convince her I'm not the bad guy she seems to think I am." with dissolve
        ks "Sayori, am I really so dangerous to you? I don't recall ever doing anything to hurt you or anyone else."
        ks "And even now, I'm not hurting you am I?"
        scg sleeptalk "N... no..." with dissolve
        show SayoriHypno sleep
        ks neutral "Of course not. Nothing could be further from the truth, Sayori. I actually want to help you." with dissolve
        scg sleeptalk "... Help me?" with dissolve
        show SayoriHypno sleep
        ks "That's right, Sayori. I'm here to help you. Haven't you been working so hard lately?" with dissolve
        scg sleeptalk "Uh-huh..." with dissolve
        ks "... Maybe too hard?"
        scg "... Uh-huh..." with dissolve
        show SayoriHypno sleep
        ks "So very hard. You're exhausting yourself, Sayori, everyone can see that." with dissolve
        ks "So don't you think you owe it to yourself to ease back a little? Take a breather?"
        scg sleeptalk "Can't..." with dissolve
        ks "Why not?"
        scg "Too much... too much to do..."
        show SayoriHypno sleep
        ks "Then you're doing too much, Sayori. You need to stop what you're doing." with dissolve
        scg sleeptalk "No... can't stop." with dissolve
        show SayoriHypno sleep
        ks "Yes, Sayori. You need to stop. This is just another thing you need to work hard on; knowing when to stop." with dissolve
        ks "And I'm here to help you, remember?"
        scg sleeptalk "Help me..." with dissolve
        show SayoriHypno sleep
        "This feels like hard work, but I think I'm starting to make some progress here." with dissolve
        ks "I will, Sayori. I want to help you, and you know you need me to help you."
        scg sleeptalk "Uh-huh..." with dissolve
        show SayoriHypno sleep
        ks "And for me to help you, you need to trust me completely. Feeling very calm, very relaxed, very safe in my presence." with dissolve
        ks "Because why would you not be? I am here to help you."
        ks "Isn't that right, Sayori?"
        scg "..."
        scg sleeptalk "Right... You are here to help me..." with dissolve
        show SayoriHypno sleep
        ks "That's right, Sayori. I am here to help you relax, take time for yourself and have some fun." with dissolve
        ks "Do you like to have fun, Sayori?"
        scg sleeptalk "Uh-huh..." with dissolve
        ks "Of course you do. So instead of going to cram school, you should have fun instead." with dissolve
        scg sleeptalk "Fun..." with dissolve
        show SayoriHypno sleep
        ks "Use that time to do whatever makes you happy, and make sure you get enough sleep. Understand, Sayori?" with dissolve
        scg sleeptalk "Uh-huh..." with dissolve
        show SayoriHypno sleep
        ks "Excellent, Sayori. This will help you so much." with dissolve
        ks "Now, soon you are going to wake up but before you do, you need to know some things."
        ks "First, you know that you and I had a pleasant and normal chat where you realized I am not a danger to Nozomi, to you, or to anyone else."
        ks "Second, you know you agreed with me that you needed to make more time for yourself, to relax and to have fun and let yourself be happy."
        ks "And third, you know that you were not hypnotized. Nothing at all strange happened in this room. We simply talked."
        ks "Do you understand, Sayori?"
        scg sleeptalk "Uh-huh, I understand..." with dissolve
        show SayoriHypno sleep
        ks "Very good, Sayori. And now I will count to five, and as I count you will slowly return to waking until on five, you will become fully awake and refreshed." with dissolve
        "I then add, because I'm still stinging a little from the last time Sayori and I talked:"
        ks "Once you awaken, you will realize we have finished our conversation and apologize for your rudeness to me yesterday."
        ks "Understood, Sayori?"
        scg sleeptalk "I understand..." with dissolve
        show SayoriHypno sleep
        ks "One... knowing we had a nice and pleasant chat and that I am no danger to anyone." with dissolve
        ks "Two... realizing you need to relax and have fun instead of going to cram school and staying up late."
        stop music fadeout 5.0
        ks "Three... knowing you were not hypnotized."
        ks "Four... knowing nothing strange occurred during our talk."
        ks "Five."
        $ renpy.transition(longdissolve, layer="master")
        scg standing drowsy "..."
        ks "Sayori?"
        # play music Moment
        play music Beautiful
        scg smile "Oh, I mean, I got carried away yesterday and I was somewhat rude to you as a result." with dissolve
        scg drooping blush sleeptalk "I apologize, Kyou. I was out of line." with dissolve
        "If she's apologizing, she must have taken everything else to heart as well. I'm relieved."
        ks smile "That's okay, Sayori. No hard feelings. Besides, you were probably stressed out from all the extra work you've been doing."
        scg standing sad "That is probably the reason. I intend to let my hair down a bit from now on." with dissolve
        ks smile "Really? That's great!"
        scg smile "I do not know if that's \"great\", but talking to you did make me realize I was overdoing it." with dissolve
        scg "So thank you, Kyou. Maybe this is what Nozomi sees in you when you talk to her."
        "I let out a little chuckle."
        ks "Maybe. Anyway, thanks for hearing me out."
        scg "Of course. Now, I need to get out of this school."
        scg happy "Perhaps I shall visit the arcade again! It has been so long..." with dissolve
        scene bg ext school eve
        show Sayori smile_right
        with blink
        "And with that we made our way outside."
        ks smile "See you tomorrow, Sayori. Have fun!"
        s happy "See you." with dissolve
        scene bg k bedroom night with blink
        stop music fadeout 5.0
        "I continue to amaze myself."
        "Every time I talk to one of the girls using my new gadget I feel more confident. More alive."
        "I mean, just thinking about all the things I said... I never could've said those things to anyone a week ago."
        "This whole experience is making me a better person."
        scene bg blackscreen with dissolve
        "And with what Sayori and I worked out, clearly I can make those around me better too."
        pause 2.0
    elif pursued == "Nozomi":
        "That could've gone better but screw them, it's not like their opinions matter anymore."
        "Once Saturday comes Nozomi and I will have a long talk about those two."
        "I'll get her to tell me how she really feels about them and their bullshit meddling."
    jump Day5_NonCon_Kyou

label Day4_Villain_Kyou:
    scene bg street1 day with longdissolve
    ks sigh "*yawn*"
    play music Memories
    "I barely slept a wink last night."
    "I've hardly been keeping up with schoolwork as it is; my antics over the last few days on top of everything else is killing me."
    "Just gotta keep going..."
    scene bg classroom day with blink
    play sound schoolbell
    if hypno1 == "devoted hiroko":
        stop music fadeout 5.0
        "As class begins for another day I feel my stomach start to sink."
        queue music Measured
        "Nozomi isn't here today."
        show Hiroko uniform_arm concerned at center
        with blink
        "As soon as the lunch bell rings, I notice Hiroko patter over to me as I shoot her a glare."
        ks frown "Hiroko? What are you doing here?"
        h "Uh, yeah so Sayori wants to talk to you."
        ks surprised "Sayori?"
        show Hiroko:
            linear 1.0 xpos 0.75
        pause 1.0
        show Sayori neutral_right at center, flip
        "At the mention of her name, I notice the taller of Nozomi's friends has stood up from her desk and stepped over to join us." with dissolve
        show Hiroko:
            xpos 0.75
        s "You are not a popular man around here, Kyou."
        show Sayori uniform_folded neutral at center, flip
        "She folds her arms and shoots Hiroko a look." with dissolve
        s "With one curious exception."
        h frown_side uniform_armup "H'yeah, well, I'm big enough to admit when I'm three million percent wrong about a guy, and maybe the rest of you gotta think about that." with dissolve
        ks frown "Okay, so, you wanted to talk?"
        s annoyed "I do. This situation you have with Nozomi cannot continue." with dissolve
        "I let out a sigh as I nod."
        ks sigh "I don't know what I'm supposed to do about it, Sayori. She won't talk to me and I don't understand what was so wrong in the first place."
        show Hiroko uniform
        s frown_right "So far that is working for you, Kyou. Nozomi still isn't saying what you did to anyone, and the only other witness, Mr. Kobayashi, saw nothing untoward." with dissolve
        s "But something has to give. And that \"something\" will likely be you."
        show Hiroko surprised_side uniform
        ks confused "Wait, what?" with dissolve
        h uniform_headhold nervous_side "Whaddya mean by that?" with dissolve
        s frown "I have it on good authority that Nozomi is intending to quit this school." with dissolve
        h uniform_armup shocked_side "WHA?!" with vpunch
        show Hiroko surprised_side
        ks frown "How would you even know that? Whose authority?" with dissolve
        s frown_right "I am not revealing my sources. Just know that if she submits an official request, there will be questions." with dissolve
        s uniform "This matter regarding yourself, currently trivial for the school board, will be escalated." with dissolve
        s irritated "Considering your loathsome reputation among the other students here, and Nozomi's spotless record..." with dissolve
        s uniform_handup frown_right "It is likely and possible that you will be pushed out instead to placate her." with dissolve
        s frown "Honestly, for the sake of your own reputation and career prospects, it would be better that you jump before the push." with dissolve
        h furious_side uniform_armup "What the {nw}" with dissolve
        extend "SHIT, Sayori? That's fuckin' bull and you know it!{w=0.8} You {nw}" with vpunch
        extend "KNOW it!" with vpunch
        ks angry "I haven't done ANYTHING wrong here!"
        s frown_right "So you say, but I believe Nozomi. And that tiny benefit of the doubt that you wield is why I am advising you at all." with dissolve
        h uniform_armup angry_side vein "WHAT benefit of the doubt? None of you assholes even wanna hear his side of things!" with vpunch
        h furious_side uniform_arm novein "'Sall \"Nozo this\" and \"Nozo that\". {w=0.5}If you heard what {nw}" with dissolve
        extend "REALLY happened you'd think this whole thing is dumb, too." with vpunch
        "Wait, that's given me an idea."
        s uniform_folded rolleyes "Indulge me, then. What did he tell you?" with dissolve
        show Hiroko angry_side
        ks frown "Can we PLEASE not do this here? In front of everyone?" with dissolve
        s frown_right "No? Do you not want your exonerating tale told to the assembled masses?" with dissolve
        s uniform "Do you not wish the halls to ring with calls for your release from the clutches of inner-school politics?" with dissolve
        s "Hashtag FreeKyou."
        h uniform_headhold2 confused_side "... Freak you?" with dissolve
        ks "I don't think it's anyone's business but Nozomi's and her friends. Maybe we could talk about this later in private somewhere?"
        s uniform_handup irritated "\"We?\" No, I am not spending any private time with you. Although I suppose Hiroko could advocate on your behalf, if she wishes." with dissolve
        h uniform_armup angry_side "I DO wish it!" with vpunch
        s rolleyes "Alright, Hiroko. Perhaps you can explain your newfound fawning obsession with Kyou as well while you're at it." with dissolve
        hide Sayori
        stop music fadeout 5.0
        "And with that she walks away with a disdainful flip of her hair." with dissolve
        ks "{size=16}She didn't say where to meet?{/size}"
        show Hiroko uniform neutral
        "I speak my thoughts quietly to Hiroko, and she smiles back before whispering conspiratorily." with dissolve
        h smile "{size=16}I'll find out.{/size}" with dissolve
        ks "{size=16}Yeah. Keep me in the loop.{/size}"
        scene bg classroom eve with blink
        play music Downtown
        "The rest of the day passes uneventfully as I wait for Hiroko to get back to me."
        "I have a plan. It's risky, but I think it's my best chance going forward."
        scene bg ext school eve with blink
        "I make my way slowly outside, wondering if I should stick around a little longer."
        play sound cellvibrate
        show phone at right with moveinright:
            ypos 0.346
        "Finally, a text from Hiroko." with vpunch
        "{color=#FF89AB}\"She said not to tell u\"{/color}"
        "{color=#4B9374}\"Tell me\"{/color}"
        play sound cellvibrate
        "{color=#FF89AB}\"Gonna meet in her clubroom after clubs are done\"{/color}" with vpunch
        "{color=#4B9374}\"You really are the worst friend, you know that?\"{/color}"
        play sound cellvibrate
        "{color=#FF89AB}\"lul <3\"{/color}" with vpunch
        play sound cellvibrate
        "{color=#FF89AB}\"Anyway gotta go practice\"{/color}" with vpunch
        "{color=#4B9374}\"Don't. Come to my place ASAP\"{/color}"
        play sound cellvibrate
        "{color=#FF89AB}\"KK <3\"{/color}" with vpunch
        scene bg k room eve with blink
        "I walk around my living room, tapping my penlight anxiously as I wait for her to arrive."
        "There's a lot I need to go over with her in just a short time."
        play sound doorbell
        "Fortunately, as the doorbell being furiously pressed indicates, Hiroko is all too eager to get started."
        scene bg blackscreen
        play sound dooropen
        with dissolve
        pause 1.0
        scene bg k entrance eve
        show Hiroko happy uniform_armup blush at center
        play sound doorclose
        with dissolve
        h "I'm heeeere~ {font=DejaVuSans.ttf}♫{/font}" with dissolve
        ks frown "We don't have a lot of time. Come on up, and bring that bag with you."
        h uniform smile "Okey-dokey." with dissolve
        scene bg k bedroom eve
        show Hiroko uniform_armup happy_closed blush
        with blink
        "I lead her up the stairs and she skips cheerfully into my room while clutching her gym bag with both hands."
        show Hiroko uniform smile
        ks "Okay, first thing. Sayori needs to think you came straight from your club to talk to her." with dissolve
        ks "So get changed into your tennis clothes and I'll start explaining what you need to do."
        play sound clothes
        show Hiroko uniform_armup smile
        "Hiroko sets her bag down on my floor with a thud, then enthusiastically starts stripping off in front of me." with dissolve
        ks frown "Hmm... Although she might suspect something's off if you just went in there in your tennis kit looking totally fresh."
        h surprised "Oh yeah, Sayori's pretty sharp about that stuff." with dissolve
        queue sound clothes
        show Hiroko underwear
        ks "And she already thinks you're my lackey now. You've been acting very suspicious in front of her as it is..." with dissolve
        "I trail off while my eyes wander over Hiroko's exposed body, having just stripped off the last of her uniform."
        "As she bends down to reach for her gym bag, a new thought inevitably forces itself to the surface of my mind."
        menu:
            "I want her to stay like this":
                $hypno4 = "undies"
                $mp.hironude = False
                $mp.save()
                ks "Actually, Hiroko... stop what you're doing. You can put those on after I've gone over what you need to do."
                h laugh "Sure, Kyou~" with dissolve
                "Her hand slips away from her tennis bag as she stares at my mouth, seemingly intent on devouring every syllable that comes out of there."
                "That's a bit more intense than I'm comfortable with, so I thrust my finger towards my bed."
                ks blush "Sit down over there and listen to what you're told."
                scene bg blackscreen with dissolve
                play sound sitting
                pause 0.5
                scene DevotionBedroom head_up_blush underwear_armsdown smile with longdissolve
                "Hiroko obediently sits herself down on the bed, smiling adoringly up at me while I spend a moment looking her over from head to toe."
                "That ugly sports underwear does nothing for her, but even so, I remember that cute little body from gym class."
                "Seeing her like this makes me remember why I was into her back when we were first years. Although she wasn't dyeing her hair back then..."
                "Ugh, but I can't let myself get any more distracted right now. I have work to do."
                ks frown noblush "Now, where were we?"
                show DevotionBedroom happy
                h "Sayori thinks I'm sus~" with dissolve
                show DevotionBedroom smile
                ks "Right. Yeah, even though it's only like, five minutes to school from here you're going to leave ten... no, twenty minutes earlier than that." with dissolve
            "I want her to take it all off":
                $hypno4 = "naked"
                $mp.hironude = True
                $mp.save()
                ks blush "I-I've changed my mind. Forget about changing for now."
                "She'd plucked her tennis shirt from the bag, but immediately drops it and stands up to face me again with that cheerful grin of hers."
                h happy_closed "'Kay, I forgot... Ehehe~" with dissolve
                ks smirk "Good. Now take off everything else."
                queue sound clothes
                show Hiroko underwear_armup happy
                "Hiroko gives a carefree giggle as she starts taking off her sports bra without a moment's pause." with dissolve
                show Hiroko nude
                "She quickly slips out of her panties soon after and... there's suddenly a naked girl in my room." with dissolve
                show Hiroko smile
                "I don't know why I'm still surprised but she just... she just took it all off. Just because I told her to." with dissolve
                "And I always knew there was a cute body lurking underneath that bitchy exterior she put out. What a way to confirm it, but... fuck."
                ks frown "U-uhh... a-a-anyway, sit down over there and listen. I need you to pay attention to everything I tell you."
                scene bg blackscreen with dissolve
                play sound sitting
                pause 0.5
                scene DevotionBedroom head_up_blush bare_armsdown smile with longdissolve
                "I can't let myself enjoy this too much. I brought her here for a reason and I don't have time to fuck around. I need to act fast."
                "Need to fucking concentrate!"
                ks frown blush "O-okay, now where were we?"
                show DevotionBedroom happy
                h "Sayori thinks I'm sus~" with dissolve
                show DevotionBedroom smile
                ks "Right. Yeah, even though it's only like, five minutes to school from here you're going to leave ten... no, twenty minutes earlier than that." with dissolve
            "I want to push her around some more":
                $mp.hironude = False
                $mp.save()
                ks angry "Hurry up and get those clothes on! COME ON!"
                play sound clothes
                show Hiroko tennis_nosweat_armup pain
                "She squeals and anxiously rips her tennis uniform out of her bag, ever eager not to displease me." with dissolve
                "After hastily pulling her tennis uniform's skirt and top, she fumbles around in her bag for her socks and those sweatbands she usually wears."
                menu:
                    "Push her even more":
                        $hypno4 = "tennis partial"
                        ks "I don't have time for this!"
                        h surprised "{cps=15}Whaaa, I-I just gotta- {/cps}{nw}" with dissolve
                        ks "Get on the bed. NOW!"
                        scene bg blackscreen with dissolve
                        play sound sitting
                        pause 0.5
                        scene DevotionBedroom head_up_blush tennis_armsup_partial sad with longdissolve
                        h "Y-y-you got it, boss!"
                        "I can't help but let a smirk show on my lips, just for a moment."
                        "Knowing I can turn Hiroko into a skittishly obedient puddle with just a couple of harsh words now is pretty fucking funny to me."
                        "I want to have some more fun with her like this, and I think I can get my points across at the same time..."
                        ks frown "Alright you dopey chick, settle down. There's a lot of things I need to tell you and you need to understand all of it if my plan's gonna work."
                        show DevotionBedroom tennis_armsdown_partial neutral_right
                        ks "Don't fuck this up like you did with Nozomi. This is your last chance." with dissolve
                        show DevotionBedroom sad
                        h "Ahh..." with dissolve
                        ks "Do I make myself clear?"
                        show DevotionBedroom cry
                        h "T-t-totally! I ain't gonna fuck up again, Kyou! I promise!" with dissolve
                        ks "Yeah, we'll see about that."
                        show DevotionBedroom neutral_right
                        "I know she'll do anything to make sure my plan goes smoothly. And she won't think any worse of me at all for treating her like dirt." with dissolve
                        "On the contrary, any negative thought she has about me only makes her love me tenfold."
                        "And just one look at her makes it obvious she's getting turned on bigtime from being talked down to."
                        "So what's the downside here?"
                        ks "Good. Now what was I saying before you decided to dither about?"
                        show DevotionBedroom confused
                        h "U-uhh... you mean, like..." with dissolve
                        ks "You going to waste more of my time, you stupid girl?"
                        h "I-I mean- {w=0.5}{nw}"
                        ks angry "Do you know or not?"
                        show DevotionBedroom sad
                        h "H'y-yeah, you were saying I'm your... like, lackey, right?" with dissolve
                        ks frown "Right. And you are, but when you meet with Sayori soon you'll need to fool her that you're not. At least sow a little doubt in her head."
                        ks "First, you need to leave here nice and early. It's only five minutes to the school from here, but you'll be heading out at least twenty minutes before then."
                    "Let her finish":
                        $hypno4 = "tennis"
                        play sound clothes
                        "Tapping my foot impatiently, I watch with some amusement as the panicked girl fusses with her socks."
                        show Hiroko tennis sad
                        "She hops awkwardly back and forth as she pulls them onto her feet one by one, then bends down and hurriedly pulls her sweatbands onto her wrists to finish her ensemble." with dissolve
                        "Would've been a lot quicker if I hadn't rushed her."
                        ks sigh "What a waste of my time."
                        h cry "S-sorry! Don't be mad at meee!" with dissolve
                        "With a shrug I point her towards my bed. For once, it's not like I'm actually upset with her."
                        ks frown "Whatever. Just sit there and listen, there's a lot of ground to cover and I need you ready in time."
                        scene bg blackscreen with dissolve
                        play sound sitting
                        pause 0.5
                        scene DevotionBedroom head_up_blush tennis_armsdown neutral_right with longdissolve
                        "Hiroko obediently sits herself down, looking a little subdued. At least for the time being."
                        "So let's get back to the plan."
                        ks neutral "Now, what were we talking about before you got changed?"
                        show DevotionBedroom happy
                        h "Sayori thinks I'm sus~" with dissolve
                        show DevotionBedroom smile
                        ks "Right. Yeah, even though it's only like, five minutes to school from here you're going to leave ten... no, twenty minutes earlier than that." with dissolve
        show DevotionBedroom confused
        h "Aww. How come?" with dissolve
        ks frown "You told me you were training for that big tennis tournament that's supposed to be the most important thing in your life, right?"
        show DevotionBedroom smile
        h "Yeah, that's right~" with dissolve
        ks "So we need you looking the part. Keep you in character, maybe throw Sayori off the scent a little bit."
        ks frown "So before you head over there you're going for a run. Go around the block a few times and work up a really good sweat."
        ks "When you get there, you're going to be panting and exhausted, and about five minutes late."
        ks "Tell Sayori you're sorry, but you were training so hard that you lost track of time and forgot all about your appointment until just a couple minutes before. Okay?"
        h "Run around and get sweaty, be late on purpose, pretend it was 'cuz I was training."
        show DevotionBedroom happy
        h "Got it~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        ks "That's right. Next, you and Sayori will get to talking and you'll need to tell her your opinion about what happened between me and Nozomi."
        show DevotionBedroom smile
        ks "I'll tell you what to say, so you need to listen carefully." with dissolve
        hide DevotionBedroom
        if hypno4 == "naked":
            show DevotionBedroom head_up bare_armsdown neutral_right
        elif hypno4 == "undies":
            show DevotionBedroom head_up underwear_armsdown neutral_right
        elif hypno4 == "tennis":
            show DevotionBedroom head_up tennis_armsdown neutral_right
        elif hypno4 == "tennis partial":
            show DevotionBedroom head_up tennis_armsdown_partial neutral_right
        "Pulling out my phone, I clear my throat as I read the little piece I'd been working on since lunch, while Hiroko straightens up on the bed and appears to focus." with dissolve
        ks "You'll tell her that you're upset about Nozomi and the pain she's in. Of course you are."
        ks "Hearing it made you so angry that you went to confront me on my way home from school. You demanded I confess to my crimes."
        ks "But as you listened to my side of the story you realized, in your heart of hearts, that I was telling the truth."
        ks "It was hard for you to accept, because you hate my guts and Nozomi's your best friend, but you're a woman who believes in justice."
        ks "You couldn't just stand idly by and see an innocent man be punished. Even if that man is me."
        ks "What happened to Nozomi was a simple but tragic misunderstanding. I never laid a hand on her. I meant her no harm whatsoever."
        ks "All that happened in the end was a silly prank involving a cheap penlight and Nozomi took it completely the wrong way."
        ks "Those are the facts as you know them, and Nozomi needs to face reality like you have. You got all that?"
        show DevotionBedroom happy
        h "Yeah, I got it!" with dissolve
        "I put my phone away and frown at her. It's important for the plan that she gets her act down, and I don't trust that cheery response of hers."
        ks "You sure? Because when you talk to her you can't behave like you worship the ground I walk on."
        if hypno4 == "tennis partial":
            show DevotionBedroom neutral_right
            ks "And as we've established you're not the brightest bulb in the box, are you?" with dissolve
            show DevotionBedroom head_up_blush sad
            h "Um, y-yeah, I'm a... a dopey chick like you said...." with dissolve
            ks "So I'll explain myself extra carefully so you don't misunderstand."
            show DevotionBedroom confused
        else:
            show DevotionBedroom smile
        ks "You need to channel some of your old bitchy self from before I set you right." with dissolve
        ks "Pretend you hold a grudge against me, as if being on my side doesn't come naturally to you."
        ks "Like I said, you need to throw her off just a little. Sow some doubt into her head so she listens to you."
        ks "So let's see how you do. Imagine you're in the study club room right now and Sayori's standing here instead of me."
        ks "What will you say to her when she asks why you're supporting me?"
        show DevotionBedroom head_up neutral_right
        h "H'yeah, okay... It sucks about Nozo. Like, when she was telling us how scared she was of that dude, I thought he'd gone too far this time." with dissolve
        show DevotionBedroom frown_right
        h "I wanted to kill that motherfucker so bad." with dissolve
        if hypno4 == "naked":
            show DevotionBedroom head_up bare_armsup frown_right
        elif hypno4 == "undies":
            show DevotionBedroom head_up underwear_armsup frown_right
        elif hypno4 == "tennis":
            show DevotionBedroom head_up tennis_armsup frown_right
        elif hypno4 == "tennis partial":
            show DevotionBedroom head_up tennis_armsup_partial frown_right
        h "I was so fuckin' angry I skipped practice to go find that asshole so I could give him what for! Make him fess up!" with dissolve
        h "But he was telling me his side of things, and..."
        show DevotionBedroom confused
        h "Like, fuck, I didn't want to admit it, Sayori, but the dude was talking a lot of sense." with dissolve
        if hypno4 == "naked":
            show DevotionBedroom head_up bare_armsdown confused
        elif hypno4 == "undies":
            show DevotionBedroom head_up underwear_armsdown confused
        elif hypno4 == "tennis":
            show DevotionBedroom head_up tennis_armsdown confused
        elif hypno4 == "tennis partial":
            show DevotionBedroom head_up tennis_armsdown_partial confused
        h "He's gotta be telling the truth. He ain't the bad guy here, and I'm a... a woman who believes in justice." with dissolve
        h "It don't matter that Nozo's my bestie, and it don't matter that I'm talking about Kyou fuckin' Koyama. I can't just watch her ruin his life like this, y'know?"
        if hypno4 == "naked":
            show DevotionBedroom bare_armsup sad
        elif hypno4 == "undies":
            show DevotionBedroom underwear_armsup sad
        elif hypno4 == "tennis":
            show DevotionBedroom tennis_armsup sad
        elif hypno4 == "tennis partial":
            show DevotionBedroom head_up tennis_armsup_partial sad
        h "She's gotta stop before she gets him thrown outta school, because... b-because..." with dissolve
        show DevotionBedroom cry
        h "Kyou's {nw}" with dissolve
        extend "TOTALLY innocent, Sayori! It's the last fucking thing I ever thought I'd say!" with vpunch
        h "But I believe it with all my heart!"
        "I smile at her, satisfied."
        if hypno4 == "naked":
            show DevotionBedroom bare_armsdown smile
        elif hypno4 == "undies":
            show DevotionBedroom underwear_armsdown smile
        elif hypno4 == "tennis":
            show DevotionBedroom tennis_armsdown smile
        elif hypno4 == "tennis partial":
            show DevotionBedroom head_up tennis_armsdown_partial smile
        ks smirk noblush "Spoken like you believe every word you just said. Good girl." with dissolve
        ks "I doubt you'll convince Sayori of my innocence, and she'll have follow-up questions. But you're not there to convince her."
        show DevotionBedroom confused
        h "I ain't?" with dissolve
        "I sigh. Getting Hiroko to parrot my words is one thing. But this next part of the plan I'm a little less confident about."
        ks frown "It gets a bit complicated from here, but in short, you need to hypnotize Sayori for me."
        if hypno4 == "naked":
            show DevotionBedroom bare_armsup sad
        elif hypno4 == "undies":
            show DevotionBedroom underwear_armsup sad
        elif hypno4 == "tennis":
            show DevotionBedroom tennis_armsup sad
        elif hypno4 == "tennis partial":
            show DevotionBedroom head_up tennis_armsup_partial sad
        h underwear_armup surprised "Wha?" with dissolve
        ks sigh "Yeah, my plan means I have to trust everything to my brainwashed idiot minion. What could possibly go wrong."
        show DevotionBedroom neutral kyou_arm
        "I then make a point of taking my penlight out of my pocket to show her." with dissolve
        ks smirk "But I think with this I can get you ready in time to do what I need you to do."
        if hypno4 == "naked":
            show DevotionBedroom bare_armsdown
        elif hypno4 == "undies":
            show DevotionBedroom underwear_armsdown
        elif hypno4 == "tennis":
            show DevotionBedroom tennis_armsdown
        elif hypno4 == "tennis partial":
            show DevotionBedroom head_up tennis_armsdown_partial
        "Hiroko nods attentively as her eyes glance over the simple device." with dissolve
        h "Hey, ain't that..."
        ks frown "It's the very reason you're my brainwashed idiot minion now."
        show DevotionBedroom awe
        h "Oh shit, yeah! It's the pretty light you showed me!" with dissolve
        ks "And later tonight, you're going to be showing it to Sayori just as I showed it to you."
        if hypno4 == "naked":
            show DevotionBedroom head_up_blush bare_armsup smile
        elif hypno4 == "undies":
            show DevotionBedroom head_up_blush underwear_armsup smile
        elif hypno4 == "tennis":
            show DevotionBedroom head_up_blush tennis_armsup smile
        elif hypno4 == "tennis partial":
            show DevotionBedroom head_up_blush tennis_armsup_partial smile
        h cry_happy "Whoa! Y-You're giving it to me?" with dissolve
        ks "Not yet. And you're just borrowing it for tonight."
        show DevotionBedroom sultry
        h underwear cry_joy "S-still, your hands have been all over that thing. S'like I get to carry you in my pocket all night~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        ks "Don't be creepy and focus. First I'm going to show you how to use it, by hypnotizing you with it again."
        show DevotionBedroom confused
        h "... I don't get it." with dissolve
        if hypno4 == "tennis partial":
            ks "I'm not surprised, but don't worry your little head about it."
            ks "Just make yourself comfortable there and do exactly as I say."
        else:
            ks "You don't have to. Just make yourself comfortable there and do exactly as I say."
        if hypno4 == "naked":
            show DevotionBedroom bare_armsdown smile kyou
        elif hypno4 == "undies":
            show DevotionBedroom underwear_armsdown smile kyou
        elif hypno4 == "tennis":
            show DevotionBedroom tennis_armsdown smile kyou
        elif hypno4 == "tennis partial":
            show DevotionBedroom tennis_armsdown_partial smile kyou
        "Hiroko obediently settles down on the bedsheets as I raise my penlight up to her eye level." with dissolve
        ks "Maybe I can burn enough knowledge into that tiny brain of yours so you can handle putting Sayori into a trance by yourself."
        ks "I'm sure there'll be an opportunity to demonstrate the \"prank\" I did and give yourself an excuse to use my penlight on her."
        ks "If she's anything like you, she'll be deeply hypnotized well before she realizes something's wrong."
        ks "That's all you need to do. I'll be hanging around nearby, so once she's asleep in a trance you'll message me and I'll come in to take over. Understand?"
        if hypno4 == "naked":
            show DevotionBedroom bare_armsup laugh
        elif hypno4 == "undies":
            show DevotionBedroom underwear_armsup laugh
        elif hypno4 == "tennis":
            show DevotionBedroom tennis_armsup laugh
        elif hypno4 == "tennis partial":
            show DevotionBedroom tennis_armsup_partial laugh
        "Hiroko's face lights up as she lets out an excited squeal." with dissolve
        h "{cps=20}Oh man, this sounds so fuckin' {/cps}{nw}"
        extend "COOL! I totally get it now!" with vpunch
        show DevotionBedroom happy
        "I have to smirk at her enthusiasm." with dissolve
        "She might still care deeply about her closest friends, but even after all this talk of betraying them there's not even a hint of doubt in her mind where her true loyalties lie."
        show DevotionBedroom smile
        "I really am all that matters in her little world now." with dissolve
        ks smirk "Great. Now get comfortable and watch the light. Focus."
        if hypno4 == "naked":
            show DevotionBedroom bare_armsdown smile with dissolve
        elif hypno4 == "undies":
            show DevotionBedroom underwear_armsdown smile with dissolve
        elif hypno4 == "tennis":
            show DevotionBedroom tennis_armsdown smile with dissolve
        elif hypno4 == "tennis partial":
            show DevotionBedroom tennis_armsdown_partial smile with dissolve
        show DevotionBedroom smile_light with dissolve
        show DevotionBedroom smile
        "Hiroko settles back down on the bed as she watches me flash the penlight over her curious eyes." with dissolve
        ks neutral "Focus on the light as it passes across your eyes, and think back on how good it feels to relax under its glow."
        show DevotionBedroom smile_light with dissolve
        show DevotionBedroom smile
        $ renpy.transition(dissolve, layer="master")
        ks "Feeling so good. So relaxed. So focused as you watch the light pass."
        show DevotionBedroom smile_light with dissolve
        hide DevotionBedroom
        if hypno4 == "naked":
            show DevotionBedroom head_up bare_armsdown smile
        elif hypno4 == "undies":
            show DevotionBedroom head_up underwear_armsdown smile
        elif hypno4 == "tennis":
            show DevotionBedroom head_up tennis_armsdown smile
        elif hypno4 == "tennis partial":
            show DevotionBedroom head_up tennis_armsdown_partial smile
        $ renpy.transition(longdissolve, layer="master")
        ks "And again..."
        show DevotionBedroom smile_light with dissolve
        show DevotionBedroom smile
        $ renpy.transition(dissolve, layer="master")
        ks "You'll notice as you blink, it becomes a little harder to open those eyelids again."
        show DevotionBedroom smile_light with dissolve
        show DevotionBedroom neutral_right
        $ renpy.transition(longdissolve, layer="master")
        ks "And that's perfectly fine, Hiroko. Perfectly natural for you to become tired, your eyelids heavier, as the light passes your eyes again."
        show DevotionBedroom neutral_light with dissolve
        show DevotionBedroom neutral_right
        $ renpy.transition(dissolve, layer="master")
        ks "And again..."
        show DevotionBedroom neutral_light with dissolve
        show DevotionBedroom straining
        stop music fadeout 10.0
        $ renpy.transition(longdissolve, layer="master")
        ks "That's right, Hiroko, you can't fight it. Not anymore. You'll just let the light take you down..."
        show DevotionBedroom straining_light with dissolve
        show DevotionBedroom straining
        $ renpy.transition(dissolve, layer="master")
        ks "And down..."
        show DevotionBedroom straining_light with dissolve
        show DevotionBedroom straining
        $ renpy.transition(dissolve, layer="master")
        ks "And closing your eyes, and... sleep, Hiroko."
        show DevotionBedroom head_down sleep
        $ renpy.transition(longdissolve, layer="master")
        "Her eyes snap shut as her head slightly droops. That was the easy part, of course."
        queue music Flow
        ks "Now focus on my voice, Hiroko. Hear the natural cadence of my words, and how soothing they sound to your ears. How easy it is to listen."
        ks "Can you do that for me, Hiroko?"
        show DevotionBedroom sleeptalk
        h sleeptalk "Yeah..." with dissolve
        show DevotionBedroom sleep
        ks "Good girl. You will find that as you listen, you will be able to mimic my pattern of talking, in this nice hypnotic rhythm, whenever you attempt to hypnotize someone." with dissolve
        ks "You will recall my choices of words, to encourage your subjects to relax and focus, to feel their eyelids droop..."
        ks "... and to coax them into dropping into a deep hypnotized sleep, as you are now."
        ks "And as you do so, you will feel your confidence grow as a hypnotist. You will believe you are capable of hypnotizing any subject with your knowledge."
        ks "Understand, Hiroko?"
        show DevotionBedroom sleeptalk
        h sleeptalk "Yeah..." with dissolve
        show DevotionBedroom sleep
        ks "That's good. Now, on a count of three you will return to waking, feeling happy and refreshed and confident that you know how to hypnotize." with dissolve
        ks "One... stirring gently."
        stop music fadeout 5.0
        ks "Two... feeling your eyelids become lighter."
        ks "And three, wide awake."
        show DevotionBedroom sleepy
        $ renpy.transition(longdissolve, layer="master")
        h sleepy "Mmm..."
        ks smile "Man, this had better work."
        show DevotionBedroom head_up_blush happy
        play music Downtown
        "Hiroko grins sheepishly at me from the bed." with dissolve
        h "I totally got this~"
        hide DevotionBedroom
        if hypno4 == "naked":
            show DevotionBedroom head_down bare_holding awe_down
        elif hypno4 == "undies":
            show DevotionBedroom head_down underwear_holding awe_down
        elif hypno4 == "tennis":
            show DevotionBedroom head_down tennis_holding awe_down
        elif hypno4 == "tennis partial":
            show DevotionBedroom head_down tennis_holding_partial awe_down
        "Anxiously, I hand her my penlight and she takes it in her hands as she regards it with wonder." with dissolve
        h "Oh man, just holding Kyou's very own legendary penlight..."
        show DevotionBedroom head_up_blush sultry
        h sleeptalk_concerned "Ahhn... It's makin' me feel things!" with dissolve
        ks angry "Fucking FOCUS, Hiroko! I still need to teach you a little more."
        show DevotionBedroom confused
        h surprised "Huh?" with dissolve
        ks frown "I mean, there's not much to it. You just have to click it on and shine the lamp over her eyes like I did with you..."
        if hypno4 == "naked":
            $persistent.devotion_naked_unlock = True
        elif hypno4 == "undies":
            $persistent.devotion_underwear_unlock = True
        elif hypno4 == "tennis":
            $persistent.devotion_tennis_unlock = True
        elif hypno4 == "tennis partial":
            $persistent.devotion_tennis_partial_unlock = True
        scene bg blackscreen with longdissolve
        "So I sat down with her and guided the penlight in her hands so the lamp end was pointing away from us, as if it were a loaded gun..."
        pause 1.0
        scene bg school ext eve with longdissolve
        "After spending a little time to get her used to using the penlight and practising her hypnotic induction, I sent Hiroko away to meet Sayori as they planned."
        "I followed a few minutes after, and loiter around the gates for a while as I wait anxiously for news."
        "She definitely seemed like she could pull this off, but maybe Sayori had plans of her own. She's supposed to be smart, isn't she?"
        "Shit, what if she saw this coming? What if she right now has my penlight because she knew what she was dealing with?"
        ks frown "Ugh, why is this taking so long?!"
        "..."
        show phone at right with moveinright:
            ypos 0.346
        play sound cellvibrate
        "{color=#FF89AB}\"Come in <3\"{/color}" with vpunch
        "Oh, thank fuck."
        scene bg corridor eve with blink
        "... Wait, is this a trap? What if this is a trap?"
        "I should've told Hiroko to use a code phrase or something."
        play sound dooropen
        scene StudyRoomHypno sayori2 s_sleep hiroko1 h_happy
        with blink
        "Okay, I'll admit. This doesn't look like a trap."
        show StudyRoomHypno h_grin
        "Sayori appears down and out, and Hiroko looks stupidly pleased with herself." with dissolve
        show StudyRoomHypno hiroko2 h_blush1
        "I match Hiroko's grin with my own, and after taking my penlight back from her I talk softly in Sayori's ear." with dissolve
        ks smirk "Can you hear me, Sayori?"
        s "..."
        "Hiroko grins and whispers back."
        show StudyRoomHypno h_cheerful
        h happy "{size=16}I think she's only gonna listen to me, Kyou.{/size}" with dissolve
        "Ugh, right. Of course she's conditioned to listen to her hypnotist's voice. My own words might even wake her if I'm not careful."
        ks "{size=16}Then you're gonna tell her what I tell you, understand?{/size}"
        show StudyRoomHypno h_happy
        "She nods with a beaming smile as I begin to work on Sayori via her." with dissolve
        hide StudyRoomHypno
        show StudyRoomHypno sayori2 s_sleep hiroko3 h_smug
        h neutral_side noblush "Sayori, you'll listen to me, won't you?" with dissolve
        show StudyRoomHypno s_sleeptalk
        s sleeptalk "Uh-huh..." with dissolve
        show StudyRoomHypno h_smile_right s_sleep
        h "Yeah, it's real good to listen. So very good to listen and respond to my voice. " with dissolve
        show StudyRoomHypno h_talking
        h "And as you listen, it's super important that you accept how right my words are. And how good it feels to accept that my words are true and correct." with dissolve
        "Hiroko's speaking in her \"hypnotist's voice\" I taught her tonight. It's eerily different from the chirpy way she normally speaks."
        h "Understand, Sayori?"
        show StudyRoomHypno h_smile_right s_sleeptalk
        s sleeptalk "Uh-huh..." with dissolve
        show StudyRoomHypno h_smile s_sleep
        "Hiroko looks to me for instruction. Now it's time to turn this uppity overachiever into someone more... agreeable." with dissolve
        $hypno5 = "devoted sayori"; devoted += 1
        show StudyRoomHypno h_talking
        h smile_side "That's great, Sayori. And what's true about you is that Kyou Koyama, our classmate, is your idol." with dissolve
        show StudyRoomHypno h_smile_right s_sleeptalk
        s sleeptalk_concerned "My... what?" with dissolve
        show StudyRoomHypno h_talking s_sleep
        h "It's true. If ever you have a reason to think less of Kyou..." with dissolve
        h "... you will instead turn that thought around in your head so it makes you feel ten times better about him instead."
        show StudyRoomHypno h_smile_right s_sleeptalk
        s sleeptalk_concerned "Why would I... ever..." with dissolve
        show StudyRoomHypno h_talking s_sleep
        h no_arm "Because you know how right this feels. Kyou is amazing. Kyou can do no wrong. And the more you think about that, the better you feel." with dissolve
        show StudyRoomHypno h_smile_right
        h happy "And the better you feel, the more you realize Kyou is your ultimate idol." with dissolve
        show StudyRoomHypno h_smile_closed h_blush2
        h smile_side "That makes sense, doesn't it?" with dissolve
        show StudyRoomHypno s_sleeptalk
        s sleeptalk_concerned "It...{w=1.0}{nw}" with dissolve
        $ renpy.transition(dissolve, layer="master")
        extend sleeptalk " i-it makes sense, yes."
        show StudyRoomHypno s_sleep
        "I kinda thought Sayori would put up more of a fight than that. I'm not complaining, though." with dissolve
        show StudyRoomHypno h_talking
        h happy "Everything he says sounds like the most amazing thing to your ears, and he is always, always your first priority." with dissolve
        h "Everything I have told you is true, Sayori. Whether you are in a deep, tranced sleep, or if you are wide awake and alert. Understand?"
        show StudyRoomHypno h_smile_right s_sleeptalk
        s sleeptalk "I understand..." with dissolve
        show StudyRoomHypno h_smile_closed s_sleep
        h smile_side tennis_armup "You're doing so great, Sayori. So we're gonna wake you up in a moment." with dissolve
        hide StudyRoomHypno
        show StudyRoomHypno hiroko3 h_talking sayori2 s_sleep
        h "I'm gonna count up and when I reach the number five, you will awaken having accepted everything I've told you." with dissolve
        h "One, just beginning to stir."
        h "Two, slowly becoming more aware of where you are."
        h "Three, slowly feeling your eyelids become lighter. Starting to test them."
        h "Four, opening your eyes, so close to waking."
        show StudyRoomHypno h_smile_right
        h laugh_side "And five, waking up!" with dissolve
        show StudyRoomHypno s_waking
        s concerned "Uh... Hiroko, what is going on?" with dissolve
        show StudyRoomHypno h_laugh h_blush2
        h "Kyahaha, it's {nw}" with dissolve
        extend "KYOU! He fuckin' came, Sayori!" with vpunch
        show StudyRoomHypno s_startled s_blush
        s concerned_right "... Kyou?" with dissolve
        $persistent.study_room_hypno_sayori_unlock = True
        scene bg study room eve
        show Sayori surprised_right blush at center
        show Hiroko tennis happy at center, flip:
            xpos 0.25
        with blink
        "I feel my eyes widen as Sayori jumps out of her chair. She's no Hiroko, but I swear no one's seen her this animated, ever."
        show Hiroko smile blush
        s concerned_right "W-when did you get here?" with dissolve
        ks smirk "Just now. You pleased to see me?"
        show Sayori giggle
        "As calm and aloof as she normally is, Sayori can't help herself." with dissolve
        show Sayori happy
        "Letting a barely-concealed squeal of delight, she bows to me as if she were in the presence of royalty." with dissolve
        s "Like you would not believe! It is truly a privilege to be in your presence, Mr. Koyama!"
        s uniform_handup laugh "I think I get it now, Hiroko. What you see in him." with dissolve
        h giggle blush tennis_headhold2 "Oh my god, {nw}" with dissolve
        extend "FINALLY someone's on my wavelength!" with vpunch
        s uniform giggle "But to what do I owe the pleasure, Kyou, if you don't mind me asking?" with dissolve
        ks frown "I need to pick your brain about how I can stop Nozomi from getting me expelled."
        s angry_right uniform_folded "They will expel you over my dead body!" with dissolve
        h furious tennis_armup "AND MINE!" with vpunch
        ks frown "Yeah yeah, first I need to know if you're still in touch with Nozomi? Or did she cut you off like she did Hiroko?"
        show Hiroko tennis smile
        s smile "We are still in contact. We exchanged messages before I left for school this morning." with dissolve
        s concerned_right "It is how I know she means to leave us." with dissolve
        ks "Alright. Don't give her any idea that we've been in contact. She CAN'T know that you're loyal to me now, you understand?"
        s uniform laugh_right "You are giving me orders and it excites me... I accept the responsibility." with dissolve
        s annoyed "However, I should mention in that case that I must be leaving shortly, much as I'd hate to spend time apart from you right now." with dissolve
        ks "Why's that?"
        s concerned_right "I need to get to cram school. And if I am to comply with your order, then Nozomi must be assured I am following my normal routine." with dissolve
        s "To do otherwise would make her suspicious."
        ks sigh "That's true... Alright, we'll need to handle this in the morning. Go to cram school, Sayori."
        s laugh_right "I will see you sooner than later, Mr. Koyama~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        hide Sayori
        "As Sayori exits, I turn to Hiroko, who giggles at me." with dissolve
        h tennis_armup giggle "Did I do good or what?" with dissolve
        ks neutral "Go home, Hiroko. We'll deal with this tomorrow."
        h smile "'Kay!" with dissolve
        scene bg k bedroom night with blink
        stop music fadeout 4.0
        "This is going to work out."
        "Now Sayori works for me, she's bound to think of something to stop Nozomi from ruining me."
        play music Past_Sadness
        "Nozomi..."
        "Now that I have a moment to think about it, am I even interested in Nozomi anymore?"
        "She's the reason this all began, and yet I realize somewhere along the way I've stopped thinking of her as someone I admire and love."
        "Now she's become more an opponent to be defeated."
        "After all, the most important thing now is that I keep the gains I've made at all costs."
        "All those years I was shunned by these same girls, and for what? Because of some vaguely defined \"creepiness\"?"
        "There's no way we're going back to that."
        stop music fadeout 5.0
        scene bg blackscreen with longdissolve
        pause 2.0

    elif hypno1 == "robot hiroko":
        "As I settle in my seat for morning classes I look across the room, spying Nozomi as she takes her own seat between Sayori and the [hypno6]."
        "They're exchanging some words before settling down as Mr. Kobayashi addresses the class. I'll have to ask my bot about it later."
        stop music fadeout 5.0
        show Hiroko at center:
            xpos 0.75
        show Sayori frown_right uniform_folded at center, flip:
            xpos 0.25
        show Nozomi front2 uniform_folded determined at center
        with blink
        "As lunch rolls around I'm greeted by a peculiar sight."
        "Nozomi strides over to my desk, flanked either side by her friends as she looks to me determinedly."
        queue music Measured
        n "Okay, Kyou. Where is it?"
        ks confused "Where's... what?"
        n irritated "That... that torch you shone in my face before. Where is it?" with dissolve
        "At one time the very idea of my crush being mad at me would've had me quivering in a heap."
        "But I'm not that person anymore."
        ks neutral "I don't get it, Nozomi. Why are you getting so bent out of shape over a little light?"
        n furious "Ugh, you..." with dissolve
        s uniform_handup "It will need to be confiscated, Kyou. This school does not permit laser pointers on the premises." with dissolve
        ks frown "Well, even if I had it on me it's not a laser pointer, is it?"
        n side frown "If you're shining it in people's eyes then what's the difference? You could've blinded me!" with dissolve
        "... I doubt Nozomi really thinks that. This is obviously just a ploy to separate me from my penlight."
        ks sigh "Okay, it was a cheap prank, I know, but I stopped bringing it with me since it freaked you out so much."
        n front irritated "I know you still have it, Kyou. And as class representative I have a responsibility to root out delinquent behaviour." with dissolve
        n determined "Now turn out your pockets." with dissolve
        ks frown "Come on, Nozomi. This is harassment. And you're wildly overstepping your authority here, \"class representative\"."
        n frown "What's the harm, Kyou? We're just talking about a little flashlight here. I doubt it's even worth much to you." with dissolve
        ks "Tell me why you want it so badly, Nozomi. Can you answer me that?"
        n irritated "I want it so you don't endanger the eyesight of me or anyone else again with your childishness." with dissolve
        ks sigh "Nozomi, look, I'm sorry about the other day, and I promise I won't mess with you like that again."
        n front2 furious "Not good enough. Hand it over!" with dissolve
        ks frown "Why is that not good enough? Don't you think you're over-reacting about getting a little light in your face?"
        show Nozomi determined
        "Nozomi spends a few moments glowering at me." with dissolve
        s uniform_handup concerned "Nozomi, I am loathe to agree with him, but I think you have taken this as far as it needs to go." with dissolve
        show Nozomi irritated
        "Yeah, Nozomi. I know you haven't told anyone why you're so worried about me keeping my penlight." with dissolve
        "You think no one would believe you if you told them, not even your closest friends."
        "And you'd be right."
        n "F-fine..."
        hide Nozomi
        "And with that Nozomi turns on her heel and stomps off, hugging her stomach." with dissolve
        s uniform surprised "... You have been awfully quiet, Hiroko." with dissolve
        h surprised_side "H-huh?" with dissolve
        s concerned "Is everything okay?" with dissolve
        h "Ah... {w=0.5}{nw}"
        show Hiroko happy uniform_headhold2
        $ renpy.transition(dissolve, layer="master")
        extend "Oh, yeah, I'm just really sleepy today, is all."
        s smile "Heh. Exhausted from your tennis training I take it?" with dissolve
        h smile_side "I guess?" with dissolve
        stop music fadeout 5.0
        scene bg classroom eve
        play sound schoolbell
        show Nozomi front2 at right
        with blink
        n "Stand!"
        n "Bow!"
        hide Nozomi
        play music Downtown
        "As Nozomi calls the end of class, she hurriedly gathers her things and makes for the exit as she's done all week." with dissolve
        "Much as I hate to say it, that girl is a danger to me."
        "I don't want to hurt Nozomi, and I don't think I will, but..."
        "Something needs to be done about her now, before she rallies the faculty against me and gets me suspended or something."
        "I won't let her interfere with what I'm doing..."
        scene bg ext school eve
        with blink
        show phone at right with moveinright:
            ypos 0.346
        "As I head out, I send my [hypno6] a quick text."
        "{color=#4B9374}\"Come to my place. NOW\"{/color}"
        hide phone with moveoutright
        "I was hoping to have more time for this..."
        "But I think with just a few more adjustments to Hiroko's programming, [p_they] will be ready to do what I need [p_them] to."
        scene bg k room eve
        show Hiroko
        with blink
        "She arrives home shortly after I do. Right after I've had time to check the mail."
        "Seems my items have arrived."
        ks "Hiroko, get changed into your tennis clothes."
        h smile "Okay, Kyou." with dissolve
        play sound clothes
        hide Hiroko
        "The [hypno6] smiles blankly and changes [p_them]self without complaint while I unpackage my things." with dissolve
        "Wonderful. All of my earlier programming on the [hypno6] seems to be holding up without any bugs that I can observe."
        "Anyway, I place my ordered items on the coffee table and... yep, that's what I bought all right: A tiny bluetooth headphone and a clip-on camera."
        show Hiroko tennis smile
        "Meanwhile I look up to see that my [hypno6] has completed [p_their] task and is standing stiffly to attention." with dissolve
        "I'm sure with all the stress school life puts on Hiroko, [p_they]'s more than happy to let [p_their] robot self come out on display again."
        "Just letting that CPU cool down from the reduced load. It must be the closest a [hypno6] comes to relaxing."
        "Smiling at the thought, I pick up the little headphone from the table and switch it on as I approach Hiroko, who remains standing with that vacant look on [p_their] face."
        "Next, I brush her hair aside and firmly push the tiny device deep into [p_their] left ear before arranging [p_their] hair over to cover it."
        "I purposefully bought an earpiece that was flesh-coloured, but I'd rather it stay as concealed as possible."
        "I then take the camera and attach it to the collar of [p_their] shirt. It looks a little conspicuous, but maybe I can explain it away to anyone who asks."
        ks "Power down."
        show Hiroko entranced_neutral
        stop music fadeout 5.0        
        "Now, I have a lot of work to do and not much time to do it..." with dissolve
        scene bg classroom2 eve
        show Nozomi front2 smile at center:
            xpos 0.4
        with longblink
        n "Thanks for coming, everyone. I'll finish cleaning up here."
        n laugh "See you tomorrow!" with dissolve
        n "..."
        play music Eons
        n sigh "*sigh*" with dissolve
        show Hiroko at center:
            xpos 1.4
            linear 1.0 xpos 0.75
        h tennis_armup happy "Hi, Nozomi!"
        show Hiroko at center:
            xpos 0.75
        show Hiroko surprised_side
        show Nozomi at flip
        n side shocked_side "AAH!" with vpunch
        h tennis "Are... you okay?" with dissolve
        n sad_closed "Oh, it's just you, Hiroko." with dissolve
        n sad_side "I'm surviving, let's put it that way." with dissolve
        h sad_side "Right... That sucks." with dissolve
        n "Uh-huh. So what brings you here? I thought you'd still be out on court."
        h sleeptalk "I was, but... I wanted... to check on you." with dissolve
        n sad_closed "Well, thanks I guess. I'm just going to finish up here and go straight home." with dissolve
        h neutral_side "... Can you wait a minute?" with dissolve
        n neutral_side "I... guess? What's up?" with dissolve
        h "Maybe... you should... sit down for this?"
        n sad_side "... Not to be rude, Hiroko, but are YOU alright?" with dissolve
        h confused_side "Huh?" with dissolve
        n "You sound very... laboured."
        h smile_side "Oh... yeah, I'm just... catching my breath." with dissolve
        n "And is that a camera?"
        h tennis_armup neutral_side "... [hypno2]." with dissolve
        n surprised_side "Hiroko, what? Why are you talking so weirdly?" with dissolve
        show Nozomi shocked_side with dissolve
        show penlight at right with moveinright:
            ypos 0.346
        $light_x = 0.33; light_y = 0.25; ldirection = "right"; lnumber = 1
        call lightshow from _call_lightshow_173
        h "Nozomi, please don't be afraid."
        n "Oh my god, Hiroko..."
        call lightshow from _call_lightshow_174
        h "You don't need to... deny yourself the pleasure... of the light, Nozomi."
        n "Hiroko, please! This isn't you!"
        call lightshow from _call_lightshow_175
        h "All you need... to do is relax...{w=1.0} To-{nw}"
        scene bg blackscreen
        show KyouPhone bedroom uniform nozomi_fear
        ks "{cps=2000}All you need to do is relax. To{/cps} relax and focus your gaze on the light flashing before your eyes."
        ks "It's perfectly natural and right to want to do this, Nozomi. Perfectly-{w=1.0}{nw}"
        scene bg classroom2 eve
        show Nozomi front sleepy at center:
            xpos 0.4
        show Hiroko tennis_armup tennis_arm neutral_side at center:
            xpos 0.75
        h "{cps=2000}It's perfectly natural and... right to want to do this, Nozomi. Perfectly {/cps}correct... Perfectly normal to focus on the... pattern forming in your eyes."
        call lightshow from _call_lightshow_176
        h "Relaxing deeper... Every blink of your eyelids becoming harder... So much harder to keep your eyes open... as you focus..."
        call lightshow from _call_lightshow_177
        n drowsy "Hiroko, please... s-stop..." with dissolve
        call lightshow from _call_lightshow_178
        h "Becoming perfectly relaxed... Letting go of your cares... and your worries... So perfectly relaxed now..."
        n sleepy "Mmn..." with dissolve
        call lightshow from _call_lightshow_179
        h "That's right, Nozomi... Naturally feeling relaxed... peaceful... sleepy..."
        call lightshow from _call_lightshow_180
        scene bg blackscreen
        show KyouPhone bedroom uniform nozomi_sleepy
        ks "Hiroko, system override. Hold Nozomi's shoulders and make sure she doesn't fall. [hypno3]."
        h "\"[hypno2].\""
        show KyouPhone nozomi_sleepy_hiroko
        "I smile as the video feed coming from my [hypno6]'s camera shows [p_their] arms outstretch and grab Nozomi's shoulders as directed." with longdissolve
        ks "Hiroko, return to voice mode. Sleep-{w=1.0}{nw}"
        $persistent.k_phone_robot_unlock = True
        scene bg classroom2 eve
        show Nozomi front sleepy at center:
            xpos 0.4
        show Hiroko tennis_armup tennis_arm neutral_side at center:
            xpos 0.75
        h "{cps=2000}Sleep, {/cps}Nozomi."
        show Nozomi sleep
        "Watching on with delight, I see Nozomi's eyes flutter closed and her head droop slightly." with dissolve
        h "Very good, Nozomi... Deep sleep... Dropping deeper, now."
        "Somehow, my insane plan to hypnotize her via remote control has so far worked without a hitch."
        "And I gotta say, I owe it mostly to the compliance of my [hypno6], as [p_they] continues to repeat the words I give [p_them] to Nozomi's subdued form."
        h "And as you drop... you find it so easy... to listen to my voice... and to accept it as your truth..."
        "While [p_they] may have struggled to accept [p_their] programming at first, seeing [p_them] adapt fully like this thanks to my amateur bugfixing is so satisfying."
        h "Do you understand, Nozomi?"
        n sleeptalk_concerned "I... understand, but... I don't..." with dissolve
        show Nozomi sleep_concerned
        h "You don't need... to think, Nozomi. Just to understand..." with dissolve
        "Not to mention, the neutral monotone voice [p_they]'s been programmed to use instead of [p_their] obnoxious human one is proving really effective for hypnotic purposes."
        h "No thoughts... Just understanding, Nozomi..."
        n sleeptalk "Just... understanding..." with dissolve
        show Nozomi sleep
        "Anyway, now that Nozomi should be open to suggestion I need to finish what I started. Or maybe make her a part of what I began with Hiroko." with dissolve
        menu:
            "Have her become my girlfriend":
                $hypno10 = "girlfriend nozomi"
                "This is what I've been working towards."
                h "Now, Nozomi... what I am about to tell you is... your truth..."
                h "And the truth is... you want to become Kyou Koyama's girlfriend."
                n sleeptalk_concerned "I want to... become his girlfriend?" with dissolve
                "I know it's a lie. I know Nozomi doesn't feel anything for me, no matter how hard I tried for her."
                show Nozomi sleep_concerned
                h "Yes... ever since you... talked to him alone at cleaning... you realized you had... feelings for him, Nozomi." with dissolve
                "But it doesn't matter anymore. Not when I can correct her. Reprogram her..."
                h "There is no denying how... you really feel about Kyou Koyama. You love and accept him... no matter what."
                "Make her mine..."
                h "So embrace that feeling in your heart... and accept it completely... as though you have never... been more sure about anything... in your life."
                h "Do you know your truth now?"
                n sleeptalk_concerned "T-the... the truth..." with dissolve
                show Nozomi sleep_concerned
                h "What is the truth, Nozomi?" with dissolve
                n sleeptalk_concerned "Th- that I... want to be Kyou Koyama's girlfriend..." with dissolve
                show Nozomi sleep_concerned
                h "That's right... So when your conciousness returns... you will go to him, and confess your love..." with dissolve
                h "You will beg him to be your boyfriend. You will not be content... until you know you are in a relationship with him..."
                h "Do you understand what you must do?"
                n sleeptalk_concerned "Y-... yes. I understand..." with dissolve
                show Nozomi sleep_concerned
                h "Very good, Nozomi. It feels wonderful... knowing you have accepted your... feelings for Kyou Koyama, and that you are going to act on them..." with dissolve
                stop music fadeout 5.0
                scene bg k bedroom eve with longblink
                "I had Hiroko repeat my instructions to Nozomi a few more times before waking her from trance and giving her my home address."
                "My address had barely left Hiroko's lips before Nozomi suddenly excused herself and dashed out of the classroom."
                "And after telling the [hypno6] to take [p_them]self home I hung up the phone and let out a breath I'd been holding in the adrenaline of the moment."
                "I did it. This is what I've been working for all year, and I'm about to succeed beyond my wildest imagination."
                play sound doorbell
                scene bg k entrance eve with blink
                "I barely have time to process my accomplishment before I hear the door bell sing out from downstairs."
                play sound dooropen
                show Nozomi front2 shocked blush at center with dissolve
                n "Kyou... h-haaaah... I... c-can't wait any... ahhh... longer..."
                play music Night_Road
                "As I open the door to the sight of Nozomi, I see her face flushed and dripping with sweat."
                ks smirk "W-wait for... what?"
                n drowsy "My... f-feelings... my feelings for you..." with dissolve
                "She stumbles inside and starts to struggle out of her shoes while her eyes stay on me the entire time."
                n surprised "A-and I... know you feel the same way about me... don't you?" with dissolve
                "The look on her face. God, I've never felt more attracted to her than I do now."
                n concerned "All those times you tried to talk to me... you even tried to tell me when we... w-when we were cleaning the classroom before..." with dissolve
                n sleepy "S-so Kyou... please say something." with dissolve
                n pain "Please say you'll be my boyfriend!" with dissolve
                "As she pleads, I embrace her gently and place my hand against the small of her back as I look down into those pleading eyes."
                ks smile blush "Nozomi..."
                "I want to savour this moment."
                ks "You've been playing hard to get for all this time. I was starting to think you weren't interested in me at all."
                n shocked "No! I want you, Kyou!" with dissolve
                ks smirk "How do I know you're not playing with my feelings here?"
                n sleeptalk_concerned "L-listen... Kyou, I'm so sorry that I didn't listen to my feelings before. I'm so sorry it took me so long to realize what I've wanted all along!" with dissolve
                n "I must have hurt you a lot, but I..."
                n "I..."
                scene cg nozomi robot kiss with blink
                "My words spur her into action, as she moves to prove herself by wrapping her arms around me and kissing me deeply."
                "Her warm lips press against mine, and in an instant all thoughts of teasing her into begging for my affections melt away."
                "Nozomi... you're everything I've ever wanted."
                "And I'm going to be so good to you, now that you're mine."
                $persistent.nozomi_robot_kiss_unlock = True
                stop music fadeout 5.0
                scene bg blackscreen with longdissolve
                "You'll see..."
                pause 2.0
            "Have her think she's my robot":
                $hypno10 = "robot nozomi"; robot += 1
                "I already have a robot girl. Do I really want to accept Nozomi, the girl I started all of this for, could be a [hypno6] just like her friend?"
                h "Now, Nozomi... what I am about to tell you is... your truth..."
                "I'm already beginning the process as I realize I had already made up my mind."
                h "And the truth is... you are a [hypno6]."
                "These past couple days of programming Hiroko truly fascinated me."
                n sleeptalk_concerned "... A [hypno6]?" with dissolve
                show Nozomi sleep_concerned
                if hypno6 != "robot":
                    h "Yes... a female humanoid robot, that was built... from advanced materials and... looks indistinguishable from a real human." with dissolve
                else:
                    h "Yes... a [hypno6], that was built... from advanced materials and... looks indistinguishable from a real human." with dissolve
                n sleeptalk_concerned "That... it can't be..." with dissolve
                show Nozomi sleep_concerned
                "So I want to do more. I want to see if Nozomi can become every bit the [hypno6] Hiroko is now, if not more." with dissolve
                h "A [hypno6] does not think, Nozomi. [p_they!c] processes instructions from [p_their] programmer. Just like you are now doing..."
                h "You have no thoughts, Nozomi, because... you are not human. You are a [hypno6] that processes instructions..."
                h "And you are programmed to accept... the truth, Nozomi. Confirm that you have accepted the truth."
                n sleeptalk_concerned "T-the... the truth..." with dissolve
                show Nozomi sleep_concerned
                h "What is the truth, Nozomi?" with dissolve
                n sleeptalk_concerned "That I am... a [hypno6]..." with dissolve
                show Nozomi sleep_concerned
                h "That's right... the memory of your childhood is... a false construct made to support... your human intelligence programming..." with dissolve
                "I need to keep this a bit simpler than when I first tried it with Hiroko. Using basic concepts that should be easier for her to accept initially."
                h "But the reality is that... you were built, not... birthed. Do you understand?"
                n sleeptalk "Y-... yes. I understand..." with dissolve
                show Nozomi sleep
                h "Very good, Nozomi. It feels wonderful... knowing that the... blood and bones in your body are... actually wires and circuits..." with dissolve
                h "And what's more... whenever you accept your programming... you feel a pleasurable jolt of... electricity coursing through your robotic body..."
                h "It feels so good to you... that you will always accept your programming..."
                scene bg blackscreen with fade
                stop music fadeout 5.0
                "I spent a little longer with them like that."
                "I fed as much into Nozomi's open mind as I could, filling it with the basics so she'd accept her robotic nature and recognise me as her sysadmin and controller."
                "That was as long as I dared keep her for, in case someone else happened upon the two of them."
                scene bg k bedroom night with longblink
                "After that, I sent both of them home in their \"human\" states, and I breathed a sigh of relief and elation."
                "Now that Nozomi's accepted me as [p_their] sysadmin, [p_they] shouldn't be able to threaten me anymore. No one should."
                scene bg blackscreen with longdissolve
                "So now the tinkering can REALLY begin."
                pause 2.0
    if hypno1 == "spy hiroko":
        "As I settle in my seat for morning classes I look across the room, spying Nozomi as she takes her own seat between her two friends."
        "They're exchanging some words before settling down as Mr. Kobayashi addresses the class. Maybe I'll ask them about it later."
        stop music fadeout 5.0
        show Hiroko frown at center:
            xpos 0.75
        show Sayori frown_right uniform_folded at center, flip:
            xpos 0.25
        show Nozomi front uniform_folded determined at center
        with blink
        "As lunch rolls around I'm greeted by a peculiar sight."
        "Nozomi strides over to my desk, flanked either side by her friends as she looks to me determinedly."
        play music Measured
        n "Okay, Kyou. Where is it?"
        ks confused "Where's... what?"
        n irritated "That... that torch you shone in my face before. Where is it?" with dissolve
        "At one time the very idea of my crush being mad at me would've had me quivering in a heap."
        "But I'm not that person anymore."
        ks neutral "I don't get it, Nozomi. Why are you getting so bent out of shape over a little light?"
        n furious "Ugh, you..." with dissolve
        s uniform_handup "It will need to be confiscated, Kyou. This school does not permit laser pointers on the premises." with dissolve
        ks frown "Well, even if I had it on me it's not a laser pointer, is it?"
        n side furious "If you're shining it in people's eyes then what's the difference? You could've blinded me!" with dissolve
        "... I doubt Nozomi really thinks that. This is obviously just a ploy to separate me from my penlight."
        ks sigh "Okay, it was a cheap prank, I know, but I stopped bringing it with me since it freaked you out so much."
        n front2 irritated "I know you still have it, Kyou. And as class representative I have a responsibility to root out delinquent behaviour." with dissolve
        n determined "Now turn out your pockets." with dissolve
        ks frown "Come on, Nozomi. This is harassment. And you're wildly overstepping your authority here, \"class representative\"."
        h uniform_armup angry "Harassment? You got some fuckin' nerve talking 'bout \"harassment\", dude." with dissolve
        "I flinch a little in my seat. Catching Hiroko's glare almost feels like getting punched again."
        h furious "Quit stalling and show us what you got!" with dissolve
        ks "Ugh, seriously? J-just leave me alone."
        h uniform angry vein "You want me to help you find it?" with dissolve
        "As Hiroko approaches me with her fists clenched, I recoil back in my seat and put my hands up."
        ks sigh "A-alright! I'll show you..."
        "I feel so goddamned pathetic letting her bully me like this, but I know well enough that she's willing to get physical and no one will feel inclined to stop her."
        "So with a sigh,  I pull the penlight from my pocket and slam it down on my desk."
        s frown "This is what the fuss has been about?" with dissolve
        show Nozomi irritated
        "Nozomi nods as she scoops up the device, turning it over in her hand." with dissolve
        n "I know it doesn't look like much."
        h frown_side novein "Yeah, just looks like a pen to me." with dissolve
        n frown "Well, whatever it is, it's coming with me." with dissolve
        hide Hiroko
        hide Sayori
        hide Nozomi
        "And with that she turns and walks away amidst the chatter of her friends as they try to make sense of the whole situation." with dissolve
        "Idiots. They just don't understand what they've got."
        "And maybe I should be freaking out about losing the penlight to Nozomi more than I am, but..."
        show phone at right with moveinright:
            ypos 0.346
        "As I pull out my phone and browse my contacts, seeing Hiroko and Sayori's names listed there, I smile quietly to myself."
        stop music fadeout 5.0
        "By the end of the day, it's all going to turn out fine..."
        hide phone with moveoutright
        scene bg classroom2 eve
        show Nozomi front smile at center:
            xpos 0.4
        with longblink
        n "Thanks for coming, everyone. I'll finish cleaning up here."
        n laugh "See you tomorrow!" with dissolve
        n "..."
        play music Eons
        n sigh "*sigh*" with dissolve
        show Sayori at center:
            xpos 1.4
            linear 1.0 xpos 0.75
        s "Nozomi. Are you free?"
        show Sayori at center:
            xpos 0.75
        show Nozomi at flip
        n side frown_side "Sayori? I've just finished with literature club. What's wrong?" with dissolve
        s frown "I finished my club activities as soon as I could to see you." with dissolve
        n sad_side "Oh... That doesn't answer my question, though. Are you okay?" with dissolve
        s uniform_handup sleeptalk "I just... I cannot get Kyou's penlight out of my mind." with dissolve
        n neutral_side "Oh. Yeah, I was wondering about it myself." with dissolve
        show Sayori:
            linear 1.0 xpos 0.6
        show Hiroko tennis_armup surprised_side at center:
            xpos 1.4
            linear 1.0 xpos 0.8
        h "Oh, hey you're both here!"
        show Sayori surprised_right
        n surprised_side "Hiroko? You too?" with dissolve
        show Sayori:
            xpos 0.6
        show Hiroko:
            xpos 0.8
        h tennis_headhold nervous_side "Well, yeah, I can't stop thinking about that light pen we nabbed from the creep." with dissolve
        show Hiroko neutral_side
        s neutral uniform_folded "May we see it?" with dissolve
        n frown_side "Uh... sure. I put it in my bag." with dissolve
        n sad_closed "... Here." with dissolve
        s sleep "I do not know what I was expecting. There seems to be nothing special about it." with dissolve
        h tennis frown_side "So, what, he flashed this in your face and it freaked you out?" with dissolve
        hide Nozomi
        show Nozomi at center:
            xpos 0.4
        show Sayori neutral
        n front irritated "It... it did more than that. It's a little hard to explain." with dissolve
        scene bg corridor eve with dissolve
        "As I stand outside, listening to them prattle, I keep my phone at the ready."
        "\"Finish your club activities as soon as possible, rush to see Nozomi before she can leave her own clubroom and make her show you the penlight.\""
        "\"And read any messages you receive on your phone immediately.\""
        "That's what I texted her friends earlier."
        s "{size=16}Well, we are all ears. What else does it do?{/size}"
        scene bg classroom2 eve
        show Sayori uniform_folded frown at center:
            xpos 0.6
        show Nozomi side frown_side at center, flip:
            xpos 0.4
        show Hiroko tennis frown_side at center:
            xpos 0.8
        with dissolve
        n "It was so... intense when he flashed it in my face. And I know it sounds crazy, but..."
        h confused_side "But what? C'mon, stop holding back. Tell us!" with dissolve
        n side sad "He was... he was trying to hypnotize me into becoming his girlfriend!" with dissolve
        s smirk "Snrk... Seriously? I knew Kyou had a patheticness about him, but..." with dissolve
        n frown_side "I'm serious!" with dissolve
        s concerned "... I apologize. It just sounded so ridiculous in my head." with dissolve
        h angry_side "I {nw}" with dissolve
        extend "KNEW he was up to some creepy shit, but that's so fuckin' weird." with vpunch
        play sound cellvibrate
        h frown "Eh, one sec. Got a text." with dissolve
        hide Nozomi
        show Nozomi at center:
            xpos 0.4
        n front concerned "I know how ridiculous it sounds. It's why I didn't want to tell you anything." with dissolve
        s frown "It sounds so ludicrous to even attempt such a thing. That it would even cross his mind to try?" with dissolve
        show Hiroko tennis_armup smile_side
        show Nozomi at flip
        n side sad_side "Well, that's the thing... I think he was actually succeeding?" with dissolve
        n "If Mr. Kobayashi hadn't walked in while... {w=1.0}{nw}"
        $ renpy.transition(dissolve, layer="master")
        extend frown_side "Hiroko, what are you doing with that?"
        if persistent.NewSprite == " New":
            $light_x = 0.34; light_y = 0.25
        else:
            $light_x = 0.34; light_y = 0.25
        call lightshow from _call_lightshow_296
        h smirk_side "Eheh, couldn't resist." with dissolve
        n shocked_side "Stop that right now!" with dissolve
        call lightshow from _call_lightshow_297
        h laugh_side "Youuu are getting sleeppyyyy~" with dissolve
        show Sayori angry_right
        n furious_side "Ah, I-... I'm not kidding, Hiroko, knock it off!" with dissolve
        call lightshow from _call_lightshow_298
        h happy "Heehee, you hypnotized yet?" with dissolve
        show Sayori angry at center, flip:
            xpos 0.6
        with dissolve
        pause 0.5
        play sound bodyimpact
        h pain "O-ow!" with vpunch
        s "What is the MATTER with you? I'll take that."
        show Nozomi frown_side
        h tennis sad_side "Aw, why you gotta be like that? I was just playing." with dissolve
        s irritated "This is far from the time or the place, Hiroko." with dissolve
        hide Sayori
        show Sayori concerned at center:
            xpos 0.6
        with dissolve
        s "I apologize for her, Nozomi. Are you alright?"
        n sad_closed "Yeah, just... having that light in my eyes again is bringing it all back." with dissolve
        play sound cellvibrate
        s "Is it... ah, one moment. I need to see this."
        h "Sorry, Nozo. I dunno what I was thinking."
        n sad_side "It... it's okay. I'm just confused that you would even think that was appropriate?" with dissolve
        h "Yeah, uhh..."
        s smile uniform_handup "Can we please calm down? There's no need to make this any more than it needs to be." with dissolve
        call lightshow from _call_lightshow_299
        n shocked_side "S-SAYORI! What the hell?!" with dissolve
        s smirk "Just wanted to inject some levity, Nozomi. Now be good and watch the light for me." with dissolve
        call lightshow from _call_lightshow_300
        h frown_side "Oh wow, {w=0.2}so it's okay when {nw}" with dissolve
        extend "YOU do it?" with vpunch
        call lightshow from _call_lightshow_301
        show Nozomi frown_side
        s "Just watch the light and-{w=0.5}{nw}" with dissolve
        play sound bodyimpact
        show Hiroko surprised_side
        extend surprised " Ah!" with vpunch
        n furious_side "That's ENOUGH!" with dissolve
        n "Oh my... {w=0.5}{nw}"
        show Nozomi:
            linear 1.0 xpos 0.2
        extend "{w=1.0}{nw}"
        hide Nozomi
        show Nozomi front2 cry at center:
            xpos 0.2
        $ renpy.transition(dissolve, layer="master")
        extend " o-oh my God, what's wrong with you two?"
        s sleeptalk_concerned "I... I am so sorry, Nozomi. I have no idea what just came over me." with dissolve
        show Sayori sleep
        n frightened "I'm trying to tell you what happened and you make fun of me? What kind of friends do that?" with dissolve
        h sleeptalk_concerned "Aw, Nozo. I'm sorry too. I just thought..." with dissolve
        play sound [cellvibrate, cellvibrate]
        show Sayori neutral_right
        show Hiroko neutral
        show Nozomi side sad_side at flip
        n "You just thought what? That it'd be a good idea to wave that penlight in my face when I clearly..." with dissolve
        n irritated "Oh, for... why am I even bothering. CLEARLY whatever's on your phones is more important than anything I have to say." with dissolve
        show Hiroko surprised_side
        s surprised "Huh? I'm sorry, I must have blanked out for a moment. What were you saying?" with dissolve
        n furious_side "I... I'm going home, and don't you DARE follow me!" with dissolve
        h tennis_armup angry_side "Wait, no! You can't leave!" with dissolve
        show Nozomi zorder 10:
            linear 1.0 xpos 0.55
        pause 1.0
        show Nozomi:
            linear 0.5 xpos 0.44
        pause 0.5
        n sad_side "A-Ah! Hiroko! Sayori?! Let me through!" with dissolve
        s angry "No, Hiroko's right. We must restrain you!" with dissolve
        n shocked_side "WHAT?!" with dissolve
        show Hiroko zorder 15:
            linear 1.0 xpos 0.27
        pause 1.0
        show Hiroko at flip, zorder 5
        h "Yeah! And cover her mouth so she don't scream! We gotta do that too!" with dissolve
        scene bg corridor eve with dissolve
        "My heart races as I stand watch outside."
        n "{size=16}Wait, NO- MMMFPTH! MMMFFTH!{/size}"
        "Everyone else this way looks to have gone home for the evening."
        "So as long as we don't cause too much of a ruckus, we shouldn't be disturbed."
        n "{size=10}MMPTHTHTHTPTH!{/size}"
        s "{size=16}Shh, Nozomi, everything will be fine. We've got you.{/size}"
        "Time I made an entrance."
        play sound classdoor
        scene bg blackscreen
        show NozomiSleeperCapture
        with blink
        n "K-KTTHHH! NRRPTH!"
        h angry "Shit, really?"
        s angry_right "We are in the middle of something, Kyou. Would you kindly go elsewhere?"
        "With my breath quickening, I stride over to the struggling trio and scoop up the penlight from the ground where it had fallen during the scuffle."
        h "Fuck off, Kyou. If I didn't have my hands full I'd kick your ass right now!"
        ks smile "I-it's okay, I won't interrupt what you're doing. I just want to talk to Nozomi."
        n "MMPFTH! MMMFMFTH!" with shake
        show NozomiSleeperCapture hiro_angry
        h "Ugh... c-c'mon, Nozo, hold still for fuck's sake!" with dissolve
        show NozomiSleeperCapture nozo_scream_light with dissolve
        show NozomiSleeperCapture nozo_scream with dissolve
        "Clicking the penlight back on, I pass the beam once more over Nozomi's terrified eyes."
        ks smirk "Shh, Nozomi, I'm not going to hurt you. You know that."
        show NozomiSleeperCapture hiro_growl
        s "What is he doing? Kyou, what are you doing?" with dissolve
        show NozomiSleeperCapture nozo_scream_light with dissolve
        show NozomiSleeperCapture nozo_scream with dissolve
        ks "In fact, the more you look up at this light, finding yourself so automatically drawn to it, the more you may realize how relaxed you are becoming."
        show NozomiSleeperCapture nozo_screamup_light with dissolve
        show NozomiSleeperCapture nozo_screamup with dissolve
        n "HLLTH! S-s-smoneth... h-hllpth!" with vpunch
        ks "Because this light, and my presence, are more relaxing, more safe, than you consciously think, Nozomi."
        show NozomiSleeperCapture hiro_angry
        h "Is... he's hypnotizing her, ain't he?" with dissolve
        "Ignoring my unwitting accomplices, I concentrate my attention on the only girl who matters to me right now."
        show NozomiSleeperCapture nozo_screamup_light with dissolve
        show NozomiSleeperCapture nozo_screamup with dissolve
        ks "You may in fact be feeling so relaxed that as you focus so irresistibly on the light in your eyes, you can feel your mind start to sink."
        show NozomiSleeperCapture nozo_screamup_light with dissolve
        show NozomiSleeperCapture nozo_sleepy
        $ renpy.transition(longdissolve, layer="master")
        n drowsy "{size=14}Mmmfth... mm... {/size}"
        "Having her friends soften her up with the light before my arrival was a good idea. She's already starting to drop for me despite her obvious distress."
        "Meanwhile her friends keep her firmly gripped in their arms, completely nullifying her attempts to struggle."
        s frown "So, do you want to stop him, or...?"
        "It sure is a great feeling, knowing everything's going according to plan."
        h "Kinda busy. Can't you?"
        show NozomiSleeperCapture sayo_angry
        s "I need to keep Nozomi muzzled. I can't do that AND stop him, can I?" with dissolve
        stop music fadeout 40.0
        show NozomiSleeperCapture nozo_sleepy_light with dissolve
        show NozomiSleeperCapture nozo_sleepy with dissolve
        ks "Your mind sinking so deep, Nozomi... Eyelids drooping... Finding this light so irresistible as it lets you drop even deeper, letting your cares and worries slip away."
        h "You're s'posed to be smart aren't you? Figure something out!"
        show NozomiSleeperCapture nozo_sleepy_light with dissolve
        show NozomiSleeperCapture nozo_subdued sayo_subdued hiro_subdued hiro_angry2 nozo_sleepy
        $ renpy.transition(longdissolve, layer="master")
        ks "That's right, Nozomi. Allowing yourself to relax. Allowing yourself to drop. To sink. Feeling so safe and right to drop deep into trance with your friends at your side."
        show NozomiSleeperCapture nozo_sleepy_light with dissolve
        show NozomiSleeperCapture nozo_sleepy with dissolve
        s "I-I don't know! I can't... THINK, I just need to hold her."
        show NozomiSleeperCapture nozo_sleepy_light with dissolve
        show NozomiSleeperCapture nozo_sleepy with dissolve
        ks "It's okay to close your eyes and drop into a deep trance if you need to, Nozomi."
        show NozomiSleeperCapture nozo_sleepy_light with dissolve
        show NozomiSleeperCapture nozo_sleepy with dissolve
        ks "Sleep now."
        show NozomiSleeperCapture nozo_sleepy_light with dissolve
        show NozomiSleeperCapture nozo_sleep
        $ renpy.transition(longdissolve, layer="master")
        "Nozomi's head droops while her friends argue amongst themselves, still keeping their friend tightly imprisoned in their arms while she drifts away."
        show NozomiSleeperCapture hiro_growl2
        h angry "Hey! Cut that shit out, dude. We told you to fuck off!" with dissolve
        "Now that Nozomi is safely in trance, I know I can turn my attention to her captors."
        show NozomiSleeperCapture hiro_surprised_light with dissolve
        show NozomiSleeperCapture hiro_surprised sayo_surprised_light with dissolve
        show NozomiSleeperCapture hiro_surprised sayo_surprised
        ks smile "Now, Hiroko. Sayori. Both of you need to remember the light as well." with dissolve
        "As I sweep the light past their own eyes, they immediately look to me, startled."
        show NozomiSleeperCapture sayo_surprised_light with dissolve
        show NozomiSleeperCapture sayo_surprised hiro_surprised_light with dissolve
        show NozomiSleeperCapture hiro_surprised sayo_surprised
        ks "That's right. Remembering and sinking. After all, you're already in trance, girls." with dissolve
        show NozomiSleeperCapture hiro_surprised_light with dissolve
        show NozomiSleeperCapture hiro_surprised sayo_surprised_light with dissolve
        show NozomiSleeperCapture hiro_surprised sayo_surprised
        ks "You just need to go a little deeper for me. Feeling your limbs stiffen, keeping your eyes nice and wide as you sink deep." with dissolve
        show NozomiSleeperCapture sayo_surprised_light with dissolve
        show NozomiSleeperCapture sayo_entranced hiro_surprised_light with dissolve
        show NozomiSleeperCapture hiro_entranced
        play music Flow
        "Both girl's expressions fall blank as their eyes quickly glaze over." with dissolve
        "Frozen in place either side of their friend, who remains safely asleep in their grasp."
        ks "That's right, girls. It's time to listen and obey."
        multi "Listen and obey..."
        "I wasn't lying about them already being in trance."
        "After all, both of them have been under my post-hypnotic suggestions for most of this evening, keeping them in a state of half-trance at least."
        "All they needed was the slightest nudge to drop them fully back into this state again."
        ks "And Nozomi, you will find that you can stand rigidly upright while remaining in this deep, relaxing trance."
        ks "You will find your eyelids becoming so incredibly light, opening your eyes again as you sink even deeper for me, Nozomi."
        show NozomiSleeperCapture nozo_entranced
        $ renpy.transition(longdissolve, layer="master")
        "I can feel my heart still pounding with adrenaline in my chest, no slower than when I first entered the room, as Nozomi joins the others in staring blankly ahead."
        "Blank. Mindless. Completely open to suggestion with nothing and no one to interrupt me."
        "She's ready."
        menu:
            " (disabled)Convince her she needs a boyfriend":
                pass
            "Make her unwittingly obedient, just like her friends":
                "However, I've come to realize something since I started doing this."
                "I've been thinking too small."
                "I may have started this journey because of Nozomi, and my desire to be close to her."
                "But now I'm here, with her, I can see now that my true journey's just beginning."
                "Nozomi and her clique are but one step."
                ks "Very good, Nozomi. It feels so wonderful, so correct, to be in this blissful state. To listen and obey."
                "Slipping my hands into her pockets, I quickly fish Nozomi's phone from out of there as I continue to speak as calmly as I can amidst the racing of my heart."
                ks "Sayori, Hiroko, you can let go of Nozomi now. Just let yourselves stand nice and straight, becoming more blank. More deep. More willing to listen to my voice."
                show NozomiSleeperCapture hiro_standing hiro_blank sayo_standing sayo_blank nozo_standing nozo_blank glasses_standing
                $ renpy.transition(longdissolve, layer="master")
                "Their grip on Nozomi, so rigid until just a second ago, immediately slackens as they take to my words."
                "And with no one restraining her, Nozomi stands fully upright as well. All thoughts of escape having disappeared from her now dormant mind."
                ks "That's right. It feels so wonderful to listen to me. To listen and obey."
                ks "In fact, all three of you girls, repeat that last part after me: \"Listen and obey.\""
                $multi = "{color=FF89AB}Hiroko{/color}{color=#FFFFFF},{/color} {color=93624B}Nozomi{/color} {color=#FFFFFF}&{/color} {color=385599}Sayori{/color}"
                show NozomiSleeperCapture hiro_blanktalk sayo_blanktalk nozo_blanktalk
                multi "Listen and obey..." with dissolve
                show NozomiSleeperCapture hiro_blank sayo_blank nozo_blank
                ks smirk "Very good, girls." with dissolve
                "I smirk as the three mindlessly parrot the phrase into my ears while I take Nozomi's hand and nonchalantly swipe her fingers over her phone sensor."
                "Seriously? None of them thought to use something more secure than their fingerprints? I know they couldn't have seen me coming like this, but come on..."
                "Anyway, it's not long before I set her phone's address book up with my contact details, and add her own to mine."
                ks smirk "Nozomi, and only you, Nozomi, your subconscious needs to hear what I am about to say, and it needs to listen so completely, taking in my every word. Understand?"
                show NozomiSleeperCapture nozo_blanktalk
                n entranced_talk "I understand..." with dissolve
                show NozomiSleeperCapture nozo_blank
                ks "You will ignore any instance of the name \"Kyou\" in your phone's listed contacts. It is not something you recognize." with dissolve
                ks "But if you ever receive a message from \"Kyou\", you will absorb each and every word the message contains."
                ks "Upon having done so, you will automatically delete the message and consciously forget ever having received it."
                ks "And at the first opportunity you will automatically obey the instructions the message contained."
                ks "Once you have obeyed the instructions, you will, again automatically, forget having done so, and will continue as if nothing had occurred."
                ks "Do you understand, Nozomi?"
                show NozomiSleeperCapture nozo_blanktalk
                n entranced_talk "I understand..." with dissolve
                show NozomiSleeperCapture nozo_blank
                ks "I knew you would, Nozomi. I know how it feels so good for you to listen and obey." with dissolve
                ks "Say it with me again, girls: \"Listen and obey.\""
                show NozomiSleeperCapture hiro_blanktalk sayo_blanktalk nozo_blanktalk
                multi "Listen and obey..." with dissolve
                show NozomiSleeperCapture hiro_blank sayo_blank nozo_blank
                ks "Very good. All of you going deeper. All of you feeling so good, so correct, so natural, about going into this deep and obedient trance for me." with dissolve
                "I take a shuddered breath as I glance towards the door. If anyone sees us now they must be thinking I'm inducting these three into some kind of cult."
                "But as my heart rate finally starts to settle some, I'm satisfied that no one is listening in. We're still alone."
                "Although I do need to wrap this up just in case."
                ks "And now, girls, you are going to listen so well, and obey so fully, my next instructions."
                ks "When I tell you to, you will all begin to count up slowly in your heads, from the number one up to the numbers I give you."
                ks "Hiroko, you will count up to twenty. Sayori, you will count up to forty, and Nozomi, you will count up to sixty."
                ks "When you reach the number I gave you, you will pick up your things, leave this room and head straight home."
                ks "You will not remember meeting each other in this room, nor will you remember seeing me this evening."
                ks "Instead, you will remember having had your club meetings as normal, and simply going home on finishing."
                ks "What's more, all three of you will completely forget about my penlight."
                ks "Anything you remember about it, and of me using it, will vanish completely from your memory."
                ks "Do you understand, girls?"
                show NozomiSleeperCapture hiro_blanktalk sayo_blanktalk nozo_blanktalk
                multi "Yes..." with dissolve
                show NozomiSleeperCapture hiro_blank sayo_blank nozo_blank
                ks "Very good, girls. Listen and obey." with dissolve
                show NozomiSleeperCapture hiro_blanktalk sayo_blanktalk nozo_blanktalk
                multi "Listen and obey..." with dissolve
                show NozomiSleeperCapture hiro_blank sayo_blank nozo_blank
                ks "Now start counting, all of you." with dissolve
                $ persistent.nozomisleepercapture_unlock = True
                stop music fadeout 10.0
                scene bg corridor eve with blink
                "I exhale sharply as I leave them to it, hurrying home while the last days flash through my head."
                scene bg school ext eve with blink
                "This is all real. I really hypnotized those girls and they don't even know."
                "And I thought yesterday was a rush... holy shit."
                scene bg street1 eve with blink
                "But it's like I said to myself. This is just the beginning."
                scene bg k bedroom eve with blink
                "And tomorrow is another school day."
                scene bg blackscreen with longdissolve
                pause 2.0
                jump Day5_Villain_Kyou
    jump Day5_Villain_Kyou

label Day4_Villain2_Kyou:
    scene bg street1 day with longdissolve
    "The next morning begins with a sense of anticipation as I begin my walk to school."
    play music Downtown
    "I shouldn't expect much. As committed to change as Akiko seemed to be, she's hardly going to transform overnight."
    "But right now, just the very idea that she's doing it at all is exciting to me."
    scene bg classroom day with blink
    "It's an excitement that'll have to carry me through the morning as I settle into my desk for the lessons ahead."
    show Nozomi side neutral_side at center with dissolve
    pause 2.0
    hide Nozomi with dissolve
    "Huh, Nozomi came in on time today. That's... good."
    "Ugh, no, I can't stare. Not anymore."
    "Just got to keep my head down and try to shut her out. Think of Akiko."
    show AkikoSC arms_down sleepy1 nozomi:
        matrixcolor SaturationMatrix(0)
    with blink
    "Or rather... think of her as Nozomi."
    "Maybe the real Akiko can't live up to perfection, but when she's just in my imagination now, she can be perfect."
    "This is the girl I'm interested in. The girl sitting across from me may as well not exist."
    "That's the mental image I want to focus on. At least until lunch, anyway."
    play sound schoolbell
    scene bg classroom day with longblink
    "When lunch does eventually come around, I take my time to get up from my desk."
    show Nozomi side neutral_side at center, flip
    show Hiroko neutral_side at center, flip:
        xpos 0.25
    show Sayori neutral at center:
        xpos 0.75
    s "Well then, shall we go?" with dissolve
    "Better if I let these girls go ahead of me."
    n sad_closed "Yeah, let's get out of here." with dissolve
    show Nozomi sad with dissolve
    pause 1.0
    hide Nozomi
    hide Sayori
    hide Hiroko
    with dissolve
    "I can feel that one's eyes linger on me before she leaves."
    "She rejected me. But I can tell she's still thinking about me."
    "But I don't want to think about her. I can't."
    "Not anymore."
    scene bg corridor day with blink
    "Once they're gone, I make my way slowly towards the student council room, lunch in hand, before knocking on the door."
    ks confused "N-... Akiko? Are you in there?"
    a "Ah, Kyou! Door's open~"
    play sound dooropen
    scene bg blackscreen with dissolve
    stop music fadeout 5.0
    "And I brace myself for the sight that is about to greet me..."
    play sound doorclose
    pause 1.0
    scene bg studentcouncil day
    show Akiko side uniform2 smile at center
    with longdissolve
    queue music Evening
    a happy "What do you think? Pretty cute, huh?" with dissolve
    "The door seems to swing closed by itself while I just stand there motionless for a moment."
    "The girl I'm seeing now is... well..."
    a uniform_up2 armband_up smile_side blush"I, um... spoke with Nozomi yesterday. Student council business." with dissolve
    "I find myself starting to walk in a slow circle around our student council president. And Akiko, for her part, shyly runs a hand through her hair as I openly check her out."
    ks confused "You did, huh?"
    a uniform_down2 armband_down happy "Yup! And she was looking as great as ever; her hair really is to die for~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    ks "What did you guys talk about?"
    a smile "Like I said, student council business. She's in charge of making sure everyone in your class gets their applications for the culture festival submitted in time." with dissolve
    a neutral -blush "The deadline's next week, so I wanted to check in with everybody." with dissolve
    "I'm no expert on any of this stuff, but it's obvious even to me that she's put a ton of effort into her hair since we last spoke."
    a smile "She mentioned you, actually. Said you apologized to her?" with dissolve
    ks "Oh... yeah, I did."
    a happy "That's great, Kyou! Not that I think you had anything to apologize for after our talk, but sometimes you just have to swallow your pride a little to defuse a bad situation." with dissolve
    "Her straight bob from before seems almost totally transformed."
    a uniform2 armband smile "I don't think she's ready to move on, and she has no idea why I'm so committed to talking with you, but I suppose she just needs a little more time." with dissolve
    "She even got Nozomi's bangs right from the looks of it."
    a sigh "And wow, I have no idea what she'd think if she knew I was checking her out so I could copy her hair!" with dissolve
    a sad_side "And when that wasn't enough, I looked at some of her old photos she put on her socials when I got home." with dissolve
    ks neutral "Ah... yeah, she doesn't really post much anymore, huh."
    "If Nozomi had her hair cut short and dyed it black, I imagine it'd look very much like this."
    a confused "Yeah. It's interesting how her look's hardly changed since she was a first year. She wears glasses now, but besides that?" with dissolve
    a laugh "Well, I guess there's no improving on perfection~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    show Akiko uniform_up2 armband_up laugh_wink blush
    "And as I come to a stop in front of Akiko and she awkwardly strikes a pose, I have to think she very much believes the same." with dissolve
    a "Sooo? How is it?"
    ks smile "It's... did you do this all by yourself?"
    show Akiko laugh
    "Akiko lets out an embarrassed chuckle and nods." with dissolve
    a "Ahahah, yup! You won't believe the work I had to put in to get it just right."
    a surprised "But I was so... wow, I can't believe how DRIVEN I was last night! I've never felt so motivated to do anything in my entire life!" with dissolve
    a sad "And... a-and it's good, right? I've gotten comments about my hair all morning, but you're the only one who knows why I did it. What it's for..." with dissolve
    a uniform_down2 armband_down sad_side "And now I've gone through with it, I can't stop thinking about... well..." with dissolve
    a sigh -blush "Nozomi's so wonderful, and here I am trying to imitate her. How disrespectful is that?" with dissolve
    a sad_side "I'm such a phony." with dissolve
    a confused "But I still want to do it more?! It feels so wrong, like I'm giving up parts of myself to chase a shadow. And I still want to do it." with dissolve
    a sad_side "Even though I know I'm not her. And I'll never be her, no matter how hard I try to change myself." with dissolve
    a sad "Do you... do you even like it? You still haven't said anything." with dissolve
    "Oh damn, she's right. I've been so fascinated about the changes she's made, both physically and mentally, that I forgot to tell her what I actually thought about any of it."
    a uniform2 armband pain "You hate it, don't you!" with dissolve
    ks surprised "Oh, no! Akiko, nothing could be further from the truth!"
    "This is the path I wanted her to take. And she's already surpassed my meagre expectations."
    "I guess the doubts she's having are understandable, as driven as she is to match Nozomi's perfection. But all she needs is a little more encouragement from yours truly."
    show Akiko sad
    ks smile "I really like what you've done with your hair, Akiko. I think it was worth the effort you put in." with dissolve
    "I mean, she's still no Nozomi. But she does look prettier like this, I have to admit."
    ks "And you're not a phony for wanting to make a change. Don't be so hard on yourself."
    "Now if I could get her to grow her hair out some more. Get her to dye it..."
    ks "Feeling guilty about copying her just shows that you care; that you're kind and consider other people. That's Nozomi all over."
    "Well, that'll come in time. For now, I have other priorities."
    a uniform_down2 armband_down sleeptalk "Nozomi really brings out the best in us, doesn't she. I barely even know her, but she's become such an inspiration to me." with dissolve
    a neutral_side "If only we had been classmates. It feels like all the good folks wound up in 3-B." with dissolve
    a confused "There's Nozomi, of course. Then there's Sayori, you, Shiro..." with dissolve
    show Akiko sigh
    "Akiko sighs." with dissolve
    a "Haaah... Sorry, there's that jealousy again."
    a neutral "Being in 3-C isn't terrible, I suppose. There's just this one couple who've been at each other's throats lately, and it's driving everyone nuts." with dissolve
    a neutral_side "Not to mention... well, maybe I'm overthinking it, but sometimes I wonder how many people in there even like me." with dissolve
    a uniform2 armband sigh "I mean, I do my best to be friendly with everyone, and I try not to let anything get to me." with dissolve
    a neutral "If someone puts me down, I'll always dust myself off, get back on my feet and try again." with dissolve
    a neutral_side "But sometimes I wonder if anyone only talks to me at all because of this armband I'm wearing." with dissolve
    ks confused "Why would you think that? People liked you enough to vote you president didn't they?"
    a uniform_down2 armband_down sad_side "That is true, and it'll look good on my resumé for sure. But it's hardly a glamorous position." with dissolve
    a neutral_side "I guess no one else wanted the responsibility. Maybe everyone could count on me not to rock the boat too much." with dissolve
    a sad "And geez, I don't even know why I'm telling you all this. I'm sorry." with dissolve
    a confused "I guess you're just that easy to talk to? I'm certainly enjoying these one-on-ones we're having." with dissolve
    a smile "So when I think on that, sharing a class with Nozomi and the rest of you feels like it'd be just the best time right now." with dissolve
    "Akiko breaks into a smile as she thinks of Nozomi again, and I smile back."
    "But I need to get Akiko's focus back on what we're doing here."
    ks smile "Yeah. But still, I bet you could find a way to spend some more time with Nozomi too. Get to know her some more as a person."
    show Akiko neutral
    ks "Maybe being the student council president isn't so hot, but you still have some clout around here. I bet you could set up a meeting after school to talk about something or other." with dissolve
    a uniform2 armband sad "Kyou, I don't know what kind of authority you think I have, but I can't just compel another student to make smalltalk with me for no good reason." with dissolve
    ks neutral "Yeah, but... well, you could tell her you want to talk about me and what you were trying to accomplish with these lunchtime sessions."
    a neutral_side "Hmm..." with dissolve
    ks "She'd be interested, right? And the whole time you could really pay attention to what she says, how she says it, and how she carries herself. Really get to know the real Nozomi."
    a sad "Wow. I just..." with dissolve
    ks smirk "Maybe leave out the fact we've mostly been talking about her this whole time."
    a sad_side "Kyou..." with dissolve
    ks smile "Probably best not to mention that I hypnotized you too, just to be on the safe side."
    show Akiko uniform_up2 armband_up
    "I watch as Akiko uncomfortably runs one hand through her hair, while her other runs nervously over her stomach." with dissolve
    a "I don't know. I sort of want to... s-spend more time with her. Of course I do, but with my intentions? Keeping secrets from her? It just seems so invasive, and obviously deceitful."
    "Yeah. This whole time we've been talking, it's seemed to me that Akiko's deep desire to be more like Nozomi is warring with the fact Nozomi would never do this kind of stuff."
    "So maybe I need to get a little more... persuasive with her."
    show Akiko sad
    ks smile "Okay, well, let's set that aside for the time being. How about we have a little fun while there's still time." with dissolve
    show penlight at right with moveinright:
        ypos 0.346
    show Akiko surprised
    "It really shouldn't take much, as I pull my penlight from out of my pocket in front of her." with dissolve
    a "Huh? Isn't that..."
    ks "It's what I've been using to hypnotize you and Nozomi. So what do you say? Want to go under again?"
    show Akiko uniform2 armband smile blush
    "And sure enough, Akiko can't resist the allure of being hypnotized. Not when she knows her idol would never turn down such an opportunity." with dissolve
    a "Oh, w-wow, what are you even planning to do this time?"
    a laugh "Ahaha, no, don't tell me! It was such a thrill before, I don't even care~" with dissolve
    stop music fadeout 5.0
    hide penlight with moveoutright
    scene AkikoSC akiko2 arms_down excited1 with blink
    "I gesture to her desk and she happily goes to sit while she keeps her eyes on me, an eager look on her face."
    a "Do you think this could be a regular thing for us?"
    show AkikoSC penlight
    "I grin down on her as I hold my penlight aloft." with dissolve
    "Not gonna lie, this eagerness she's showing for me is something I could become very attracted to."
    ks smile "We'll see. Now just relax and stare, Akiko."
    "If only Nozomi would look at me the same way..."
    $renpy.music.set_volume(1.0)
    play music Flow
    $renpy.music.set_volume(0.1)
    show AkikoSC excited2 with dissolve
    show AkikoSC excited1 with dissolve
    ks "Relax, and simply let this light hit your eyes as it passes back and forth."
    show AkikoSC excited2 with dissolve
    show AkikoSC excited1 with dissolve
    show AkikoSC smile1
    $ renpy.transition(longdissolve, layer="master")
    $renpy.music.set_volume(0.2)
    ks neutral "Back and forth. Let everything else slip away, and observe this familiar pattern forming in front of you."
    show AkikoSC smile2 with dissolve
    show AkikoSC smile1 with dissolve
    $renpy.music.set_volume(0.3)
    ks "Focus on it and take a deep breath in, then out."
    show AkikoSC smile2 with dissolve
    show AkikoSC smile1 with dissolve
    $renpy.music.set_volume(0.4)
    ks "Allow your body to melt into your chair, and let those eyes of yours do all the work."
    show AkikoSC smile2 with dissolve
    show AkikoSC smile1 with dissolve
    $renpy.music.set_volume(0.5)
    ks "That's right, Akiko. It feels so good to let yourself drift into a hypnotic trance."
    show AkikoSC smile2 with dissolve
    show AkikoSC smile1 with dissolve
    $renpy.music.set_volume(0.6)
    ks "So just relax. And breathe. And stare..."
    show AkikoSC smile2 with dissolve
    show AkikoSC smile1 with dissolve
    $renpy.music.set_volume(0.7)
    a "{size=16}Mmmmn...{/size}"
    "Heh. Was that a purr I just heard?"
    ks "And feel those eyelids becoming heavy. Allow yourself to become sleepier and sleepier..."
    show AkikoSC smile2 with dissolve
    show AkikoSC smile1 with dissolve
    show AkikoSC sleepy1
    $ renpy.transition(longdissolve, layer="master")
    $renpy.music.set_volume(0.8)
    "I know I compelled you to want this, Akiko, but now I really do wonder if you were always this eager to be hypnotized. Always this easy to hypnotize..."
    ks "Allow yourself to sink. Deeper..."
    show AkikoSC sleepy2 with dissolve
    show AkikoSC sleepy1 with dissolve
    $renpy.music.set_volume(0.9)
    ks "And deeper. Falling back into hypnosis."
    show AkikoSC sleepy2 with dissolve
    show AkikoSC sleepy1 with dissolve
    $renpy.music.set_volume(1.0)
    "It's almost a shame that we'll never get to find out."
    ks "Now close your eyes, Akiko. Sleep."
    show AkikoSC sleep with longdissolve
    show AkikoSC -penlight
    $ renpy.transition(longdissolve, layer="master")
    "With my penlight, it's all become so completely irrelevant."
    ks "Sleep, and fall so very deep for me now. Let every conscious thought in your head disappear, and allow your subconscious to listen very carefully."
    ks "Because we need to have another talk about Nozomi and your admiration for her."
    ks "And you do admire Nozomi, don't you Akiko?"
    show AkikoSC sleeptalk
    a "Yes... I admire Nozomi so much..." with dissolve
    show AkikoSC sleep
    ks "You want to be everything that Nozomi is, don't you." with dissolve
    show AkikoSC sleeptalk
    a "Mmn, yes... want to be... everything she is..." with dissolve
    show AkikoSC sleep
    ks "That's right. After all, these are your true, honest thoughts. But you're conflicted, because someone as perfect as Nozomi would never imitate another person to get ahead." with dissolve
    ks "Am I right about that, Akiko?"
    show AkikoSC sleeptalk
    a "Yes..." with dissolve
    "Not that it wasn't obvious, but it's good to have her confirm it."
    show AkikoSC sleep
    "Maybe she'd push past it on her own if I gave her more time. She changed her hair quickly enough." with dissolve
    "But why wait for results when I know I can just push her myself?"
    ks smirk "Akiko... have you considered that imitation is the sincerest form of flattery?"
    show AkikoSC sleeptalk
    a "I... n-no. Not really..." with dissolve
    show AkikoSC sleep
    ks neutral "You should. As a matter of fact, by impersonating Nozomi you would be honoring her." with dissolve
    ks "There's no higher compliment you could give Nozomi than by doing everything in your power to replicate her to the tiniest detail."
    ks "Do you understand now, Akiko?"
    show AkikoSC sleeptalk
    a "Yes... I understand." with dissolve
    show AkikoSC sleep
    ks "I knew you would, Akiko. You're so very good at understanding, so very good at being hypnotized. Just like Nozomi." with dissolve
    ks "So now it's almost time to wake up. I'm going to once again count you up to five, when you will awaken."
    ks "And when you wake you will once again not remember any suggestions I made to your subconscious. You will only remember that you were hypnotized."
    ks "Counting up now... one, two, feeling lighter... three, four..."
    stop music fadeout 5.0
    ks "Thoughts returning, waking up happy and refreshed... five."
    show AkikoSC smile1
    $ renpy.transition(longdissolve, layer="master")
    a "{size=16}Mmm... {/size}" with dissolve
    queue music Downtown
    "I watch with satisfaction as the student council president opens her eyes with another happy little purr."
    ks smile "Welcome back, Akiko. Wasn't that fun?"
    a "I don't even know how you do it, but... wow, you give me such a thrill every time we do this, Kyou!"
    "There. I'm sure Akiko's about to find any doubts she had about what I'm asking of her have suddenly resolved themselves."
    ks "That's great to hear. Hypnosis is supposed to feel good, and it feels great to put you under, Akiko."
    ks "Not to mention how awesome it is that you seem so into it. Guess that's something you and Nozomi just naturally have in common, huh?"
    $persistent.akiko_student_council_hypno3_unlock = True
    scene bg studentcouncil day
    show Akiko side uniform2 laugh at center
    with blink
    "To that, Akiko just giggles as she stands up from the seat."
    a "Ahaha, you can say that again~ {font=DejaVuSans.ttf}♥{/font}"
    ks smile "Speaking of which, have you thought any more on what I said about meeting Nozomi later?"
    show Akiko smile
    "The moment I ask, Akiko responds with a happy little nod of her head." with dissolve
    a "Yup! I'm excited to make more time for her if I'm being totally honest."
    ks smirk "Just remember what I said. Make sure she doesn't know what you're up to and don't say I hypnotized you, okay?"
    a happy "But of course! I can be discreet, and it'd be the best way to honor her brilliance anyhow." with dissolve
    a laugh_wink "I'll be her secret admirer~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    "I can't help but chuckle at this infectious enthusiasm of hers."
    ks smile "You sure will. I'm looking forward to finding out how much you've learned tomorrow."
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "After all that, we barely had any time to wolf down our lunches and head back to class. But I'm satisfied."
    pause 1.0
    scene bg classroom eve
    play sound schoolbell
    show Nozomi front2 at right
    with longdissolve
    queue music Eons
    n "Stand!"
    n "Bow!"
    hide Nozomi
    "The rest of the day dragged on as usual, but we're past it now." with dissolve
    show Hiroko sleeptalk at center, flip zorder 2:
        xpos 0.5
    h "Alright, I'm outta here. C'mon, Nozo." with dissolve
    "Naturally I'm still keeping as low a profile as I can in the classroom."
    show Hiroko neutral
    show Nozomi side sad_side at center, flip zorder 1:
        xpos 0.35
    n "Right behind you, Hiroko. Good luck in practice today." with dissolve
    "Not that it seems to have diffused the tension in here much."
    show Sayori at center, flip:
        xpos 0.15
    s "Yes, let us all do our best today." with dissolve
    hide Nozomi
    hide Hiroko
    hide Sayori
    "Still, I'm mindful to wait until Nozomi is out the door before I stand up to leave myself." with dissolve
    scene bg corridor eve with blink
    "It's just better that I don't get too close to her now. Not even by accident."
    a "Excuse me, Nozomi? Do you have a moment?"
    show Nozomi side neutral_side at center, flip:
        xpos 0.5
    show Hiroko neutral_side at center, flip zorder 2:
        xpos 0.3
    show Sayori at center, flip zorder 1:
        xpos 0.15
    show Akiko side uniform2 smile_side at center:
        xpos 0.75
    "So when I hear a now familiar voice ring out amongst the crowds of departing students, I come to a sudden halt before quickly ducking behind a corner." with dissolve
    n shocked_side "A-Akiko?! Is... that a new look?" with dissolve
    s uniform_handup "It most certainly is." with dissolve
    "And I simply listen."
    a uniform_up2 armband_up embarrassed_side blush "Oh wow, i-it's just like you to notice~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    show Nozomi sad_side
    h annoyed_side "'s pretty obvious, 'Kiko." with dissolve
    s sleeptalk "Indeed. When we were colleagues at student council, you always wore that same bobbed haircut." with dissolve
    s concerned "Curious that you went to such an effort now of all times." with dissolve
    n smile_side "W-well... that being said, it suits you. You look really nice, Akiko." with dissolve
    a uniform2 armband laugh "Wow... eee, that means SO much coming from you, Nozomi!" with dissolve
    "Oh my god, don't blow this, Akiko. Dial it down a notch..."
    a smile_side "Err, b-but enough about me. I just wanted to ask if you had time to chat tonight?" with dissolve
    n sad_side "Huh? Why, is something the matter?" with dissolve
    a uniform_down2 armband_down confused_side -blush "It's... well, I can't really go into it here. Actually that's why I wanted to talk to you off the premises, if you know what I mean." with dissolve
    s uniform frown_right "Well that can only mean one thing, as far as Nozomi is concerned." with dissolve
    "That's better. I think she's saved herself, but..."
    show Nozomi neutral
    show Akiko neutral
    h frown "An' I sure as shit didn't see him pass us. Did you?" with dissolve
    stop music fadeout 5.0
    "I need to make myself scarce."
    scene bg blackscreen with longdissolve
    "So I hurried into the men's bathroom and hid in a cubicle until I was sure those girls departed for their clubs."
    scene bg k bedroom eve with longdissolve
    "And once the coast was clear, I headed straight home with nothing left to do but listlessly gaze at my study notes and think about tomorrow."
    "Really wish I could be there for Akiko and Nozomi's talk."
    queue music Past_Sadness
    "It would've been far too dangerous to tail them; I know that. Hell, it was kinda dicey to even have her do this for me."
    "I have no idea what Nozomi really thinks of mine and Akiko's little lunchtime sessions. Whether she thinks I did anything to her."
    "She's surely still worried about me. But... well, if Nozomi knows anything about hypnosis, she'll know hypnosis only works on the willing, like I did."
    show penlight at right with moveinright:
        ypos 0.346
    "She certainly doesn't know what I have here with this penlight. Certainly doesn't know it like I do."
    "Maybe she felt scared to go along, like Akiko said. Maybe she really did feel a temptation to go along, like I thought she had when I tried it on her."
    "There's plenty of ways for her to rationalize what happened that day that doesn't involve me having such a powerful hypnotic tool at my disposal."
    hide penlight at right with moveoutright
    "Yeah. So long as Akiko doesn't cream her panties talking to her idol, I'm sure Nozomi won't suspect I did anything weird on her."
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "Man, she'd better not fuck this up for me..."
    pause 2.0
    jump Day5_Villain2_Kyou

label Day4_TennisBot:
    scene bg street1 day with longdissolve
    ks sigh "*yawn*"
    play music Memories
    "I barely slept a wink last night."
    "I've hardly been keeping up with schoolwork as it is; my antics over the last few days on top of everything else is killing me."
    "Just gotta keep going..."
    scene bg classroom day with blink
    play sound schoolbell
    "As I settle in my seat for morning classes I look across the room, spying Nozomi as she takes her own seat beside her friends."
    "They're exchanging some words before settling down as Mr. Kobayashi addresses the class. I'll have to ask Hiroko about it later."
    stop music fadeout 5.0
    show Hiroko at center:
        xpos 0.75
    show Sayori frown_right uniform_folded at center, flip:
        xpos 0.25
    show Nozomi front2 uniform_folded determined at center
    with longblink
    "As lunch rolls around I'm greeted by a peculiar sight."
    "Nozomi strides over to my desk, flanked either side by her friends as she looks to me determinedly."
    queue music Measured
    n "Okay, Kyou. Where is it?"
    ks confused "Where's... what?"
    n irritated "That... that torch you shone in my face before. Where is it?" with dissolve
    "At one time the very idea of my crush being mad at me would've had me quivering in a heap."
    "But I'm not that person anymore."
    ks neutral "I don't get it, Nozomi. Why are you getting so bent out of shape over a little light?"
    n furious "Ugh, you..." with dissolve
    s uniform_handup "It will need to be confiscated, Kyou. This school does not permit laser pointers on the premises." with dissolve
    ks frown "Well, even if I had it on me it's not a laser pointer, is it?"
    n side frown "If you're shining it in people's eyes then what's the difference? You could've blinded me!" with dissolve
    "... I doubt Nozomi really thinks that. This is obviously just a ploy to separate me from my penlight."
    ks sigh "Okay, it was a cheap prank, I know, but I stopped bringing it with me since it freaked you out so much."
    n front irritated "I know you still have it, Kyou. And as class representative I have a responsibility to root out delinquent behaviour." with dissolve
    n determined "Now turn out your pockets." with dissolve
    ks frown "Come on, Nozomi. This is harassment. And you're wildly overstepping your authority here, \"class representative\"."
    n frown "What's the harm, Kyou? We're just talking about a little flashlight here. I doubt it's even worth much to you." with dissolve
    ks "Tell me why you want it so badly, Nozomi. Can you answer me that?"
    n irritated "I want it so you don't endanger the eyesight of me or anyone else again with your childishness." with dissolve
    ks sigh "Nozomi, look, I'm sorry about the other day, and I promise I won't mess with you like that again."
    n front2 furious "Not good enough. Hand it over!" with dissolve
    ks frown "Why is that not good enough? Don't you think you're over-reacting about getting a little light in your face?"
    show Nozomi determined
    "Nozomi spends a few moments glowering at me." with dissolve
    s uniform_handup concerned "Nozomi, I am loathe to agree with him, but I think you have taken this as far as it needs to go." with dissolve
    show Nozomi irritated
    "Yeah, Nozomi. I know you haven't told anyone why you're so worried about me keeping my penlight." with dissolve
    "You think no one would believe you if you told them, not even your closest friends."
    "And you'd be right."
    n "F-fine..."
    hide Nozomi
    "And with that Nozomi turns on her heel and stomps off, hugging her stomach." with dissolve
    s uniform surprised "... You have been awfully quiet, Hiroko." with dissolve
    h surprised_side "H-huh?" with dissolve
    s concerned "Is everything okay?" with dissolve
    h "Uh... {w=0.5}{nw}"
    show Hiroko nervous_side uniform_headhold2
    $ renpy.transition(dissolve, layer="master")
    extend "H'yeah, don't worry about it. Just got a lot of shit to process, that's all."
    s uniform_handup sleeptalk "Ah. Of course you do." with dissolve
    stop music fadeout 5.0
    scene bg classroom eve
    play sound schoolbell
    show Nozomi front2 at right
    with longblink
    n "Stand!"
    n "Bow!"
    hide Nozomi
    play music Downtown
    "As Nozomi calls the end of class, she hurriedly gathers her things and makes for the exit as she's done all week." with dissolve
    # "I gather my own things calmly and start to head out myself, but my mind is racing..."
    "Much as I hate to say it, that girl is a danger to me."
    "I don't want to hurt Nozomi, and I don't think I will, but..."
    "Something needs to be done about her now, before she rallies the faculty against me and gets me suspended or something."
    "I won't let her interfere with what I'm doing."
    scene bg ext school eve
    with blink
    show phone at right with moveinright:
        ypos 0.346
    # "As I head out, I send my [hypno6] a quick text."
    "{color=#4B9374}\"Come to my place. NOW\"{/color}"
    hide phone with moveoutright
    "But I'm going to need some help..."
    scene bg k room eve
    show Hiroko
    with blink
    ks "You need to talk to Nozomi. Get her to back off."
    h uniform_headhold2 confused "Huh? You made me skip practice for this?!" with dissolve
    ks frown "Is there a problem, [hypno6]?"
    h sad_talk "Uh... n-no. I'm gonna talk to Nozomi. Get her to back off." with dissolve
    "I nod at her in satisfaction. I programmed her better than to seriously entertain refusing a direct command."
    h uniform nervous "But, like... what do you want me to say to her, dude? She's scared shitless after what you pulled on her." with dissolve
    h confused "It's to do with that light thingy she was talking about, yeah? Why don't you just give it up like she wants?" with dissolve
    ks sigh "That's not important. You're her friend, just convince her to drop it. She doesn't have to worry about me anymore."
    h frown "Because you won't go near her again, right?" with dissolve
    "Although it seems my programming has still done nothing to adjust her attitude."
    h nervous "... Because you won't go near her again, right?" with dissolve
    ks frown "What's it to you? Just do as you're told and leave the worrying to the humans."
    h uniform_headhold sad "H'yeah, but you know... like you said she's still my friend. Nozo's still my bestie." with dissolve
    h sad_side "It don't matter that I'm a [hypno6], Nozomi's the nicest human I ever met. She's always been good to me." with dissolve
    h uniform nervous "Even when I don't deserve it sometimes, s-so..." with dissolve
    h sleeptalk_concerned "So please... just, like, leave her alone, okay? Don't hurt her again." with dissolve
    show Hiroko nervous
    "I breathe an annoyed sigh, which seems to make Hiroko flinch as she stands nervously in front of me." with dissolve
    "It's not like I WANT to hurt Nozomi or anything. But just the fact this... this [hypno6!u] thinks [p_they] has any say over what I can and can't do?"
    "That makes me..."
    "I mean, it makes me..."
    ks sigh "Hiroko, I'm not going to hurt Nozomi, okay? I promise."
    "Fuck it. I'm not getting mad at Hiroko for this. She's just telling me what's going through that robot-conditioned brain of hers."
    ks frown "I'm not going to approach her again. I'm done trying to impress her."
    "But I'll tell her my intentions. Only it's not for her benefit; it's for mine."
    ks "I just want her to chill out and leave me alone so I can concentrate on what's important."
    "Just saying this stuff out loud is good. It feels right to say it."
    ks "And what's important is what I'm doing with you. You're my full-time project, understand?"
    show Hiroko smile
    "If it also happens to put her \"CPU\" at ease as well, then so be it." with dissolve
    h uniform_headhold2 happy_closed "Yeah, I get it. Nozo's got nothing to worry about." with dissolve
    h smirk "{cps=20}Dealing with me is {/cps}{nw}" with dissolve
    extend "TOTALLY a full-time job." with vpunch
    "... Maybe a little TOO much at ease."
    show Hiroko neutral
    ks frown "Just don't fuck this up. If Nozomi gets me suspended I'll deactivate you and sell you on the black market myself. We clear?" with dissolve
    h uniform scared "Y-y-yessir! Super clear!" with dissolve
    show Hiroko sad
    "Satisfied, I then walk past her to my coffee table, and she watches me timidly as I open the package I left there earlier." with dissolve
    "These were the little gadgets I bought the other day to use with my project: A tiny bluetooth in-ear headphone and a clip-on camera."
    "Maybe I can play with the camera later, but I'm itching to get some use out of that headphone."
    h nervous "Uhh, what's the deal with that thingy? Kyou?" with dissolve
    ks neutral "I'm going to give you a little upgrade before I let you go tonight. Now hold still..."
    "Hiroko murmurs quietly as she freezes in place while I switch the little headphone on."
    "I then brush the [hypno6]'s hair aside before pushing the flesh-cololured device deep into [p_their] left ear, fixing it in place."
    h "Mmn..."
    "Next, I arrange [p_their] hair back over [p_their] ear to make sure it's completely concealed from view."
    ks smile "There. That's your new hardware installed."
    h sleeptalk_concerned "Y-you call this an upgrade? I can't hear a fuckin' thing outta there." with dissolve
    show Hiroko nervous
    ks smirk "You won't notice the benefit until I upgrade your software. Now power down." with dissolve
    show Hiroko entranced_neutral
    stop music fadeout 5.0
    "Hiroko's mind falls blank once again, while mine races as I think about what I'll need to do to set my latest plan into motion." with dissolve
    "I'll need a couple of hours to configure that headphone, write some script for mine and Hiroko's phones and do some programming tweaks on the [hypno6] [p_them]self."
    scene bg blackscreen with longdissolve
    "But by the time I'm finished, Hiroko and I will be more connected than ever..."
    pause 2.0
    jump Day5_TennisBot

label Day4_Con_Kyou_Nozomi:
    scene bg street1 day with longdissolve
    "Yesterday was interesting, to say the least."
    if hypno2 == "trance":
        play music Bright_Opening fadein 5.0
        "I have no idea what today will bring, but I've got every reason to be positive."
        scene bg classroom day with blink
        "I make it to class as usual and as I take my seat, I flash a Nozomi a little smile as she enters shortly after me."
        show Nozomi side neutral with dissolve
        pause 0.8
        show Nozomi happy with dissolve
        pause 0.8
        hide Nozomi with dissolve
        "And to my delight, she actually acknowledges me with a nervous smile of her own before taking her seat as lessons begin."
        "It's not much, but after all this time hoping for her to notice me, I'll take what I can get."
        play sound schoolbell
        show ClassroomLunch boy2_lunch hiroko h_laugh n_armup n_smile_left glasses sayori s_smile_hiroko with longblink
        "Still, as the day passes to lunchtime, I look to Nozomi's desk with an all-too familiar feeling of longing."
        h "All right! Later losers, we're going to the rooftop~"
        show ClassroomLunch n_sigh s_neutral_hiroko
        n sad_closed "Hiroko, don't call everyone \"losers\"." with dissolve
        "To think that I've gotten closer to Nozomi than ever before, but if I approached her now she'd just coldly turn me away again."
        show ClassroomLunch h_worried_nozomi
        h surprised_side "What? It's like, uh..." with dissolve
        show ClassroomLunch s_sigh n_curious_right
        s rolleyes "A term of endearment?" with dissolve
        show ClassroomLunch h_grin_sayori
        h uniform happy "Yeah, that!" with dissolve
        "I have to be patient. I know that."
        # "Does she honestly expect me to be content with this?"
        show ClassroomLunch n_folded n_frown_left h_neutral_nozomi s_neutral_nozomi
        n sad_side "I don't think anyone sees it that way." with dissolve
        show ClassroomLunch h_annoyed_sayori
        h frown_side "Pffth, their loss." with dissolve
        "And you know, even if I can't be as open with her as I want..."
        # "But this already feels unbearable."
        # "The more I think about it, the more I wonder what I'm even getting out of being her secret hypnotist."
        show ClassroomLunch h_grin_sayori n_sigh
        h smirk_side "Get it? 'Cuz they're losers!" with dissolve
        show ClassroomLunch s_smirk_hiroko
        s smirk "It is times like this that you have to wonder why no one else lunches with us." with dissolve
        "Having this little secret with her is still pretty hot."
        $ persistent.classroomlunch4_1_unlock = True
        scene bg classroom day with blink
        # "As she leaves the classroom, I'm left alone with these thoughts."
        show phone at right with moveinright:
            ypos 0.346
        "It's just a shame I still gotta spend my school time alone again, same as before."
        "So I'll do what I normally do: Play with my phone and read up on the latest videogame and tech news."
        "I could almost fool myself into thinking nothing's changed..."
        # show phone at right with moveinright:
        #     ypos 0.346
        # "Taking out my phone, I try to distract myself by reading up on today's videogame and tech news."
        # "But it's no good. Like... I might have been able to get in Nozomi's head a little these past few nights..."
        # "... but she manages to get in MY head constantly."
        # "It wouldn't be bad if I tried to talk to her during lunch again, would it?"
        # "I mean, not TALK talk. Just a quick text."
        # "\"Hey.\""
        # hide phone at right with moveoutright
        # "There. She'll read and acknowledge that almost instantly. Just so she'll know I want to speak to her."
        # "So she should get back to me soon, then we can hash out what we're going to do tonight; hit the ground running."
        # # "So she should get back to me quickly and we can talk about this stuff now without any awkwardness when we meet up later."
        # with blink
        # "It's been ten minutes. Why hasn't she texted back? Is she ignoring me?"
        # "Was I not clear I wanted to talk? Shit, maybe I should've used more words..."
        # "I gotta do something!"
        # menu:
        #     " (disabled)Text her again":
        #         show phone at right with moveinright:
        #             ypos 0.346
        #         "Fuck it. I'll text her again."
        #         "\"Can we talk?\""
        #         hide phone with moveoutright
        #         "There. Now she can't mistake my intentions."
        #         with blink
        #         "Still nothing? Come on! I'm dying out here..."
        #         show phone at right with moveinright:
        #             ypos 0.346
        #         "\"Please?\""
        #         hide phone with moveoutright
        #         "I mean... shit, forget about school, I don't even know what she's doing later, come to think of it. Is she even coming to see me tonight?"
        #         "I have to know. I want to speak to her and she's..."
        #         play sound cellvibrate
        #         "Ahh, finally!" with vpunch
        #         show phone at right with moveinright:
        #             ypos 0.346
        #         "{color=#93624B}\"What is it\"{/color}"
        #         "Sounds a little terse. Is she mad at me?"
        #         "\"We need to talk.\""
        #         play sound cellvibrate
        #         "{color=#93624B}\"About?\"{/color}" with vpunch
        #         "\"Well are you coming to mine after school?\""
        #         play sound cellvibrate
        #         "{color=#93624B}\"Not sure\"{/color}" with vpunch
        #     "Don't text her":
        #         "I... I gotta sit on my hands, huh."
        #         "After all, I remember her telling me yesterday that I couldn't get mad if she didn't respond to my texts and stuff."
        #         "But goddamn, this IS maddening."
        #         "Like, back at my house it kinda felt I was the one in charge, dropping her into trance and stuff."
        #         "But... everything that's happened, all of it, was because she wanted it."
        #         "I know I'm going along with what she wants in the end. And I just have to be okay with that."
        #         with blink
        #         "Lunch period finishes without a text back. She didn't even look my way when she came back to the classroom."
        #         "So this really is how it's gonna be."
        #         stop music fadeout 10.0
        #         scene bg street1 eve with blink
        #         "I think I tuned out most of the afternoon."
        #         "Trudging back home is all I can do, as I wait for her to contact me again."
        #         "Just... waiting on her."

                # scene bg k room eve with blink
                # "It really is maddening."
        hide phone
        with blink
        "I try to catch Nozomi's gaze as she returns to class after lunch, but she seems to purposefully look the other way as she returns to her seat."
        "... Come to think of it, IS she coming over to mine tonight? She didn't actually tell me."
        stop music fadeout 10.0
        scene bg classroom eve with longblink
        "I sent her a text during class, but as the school day ends and everyone starts hurrying out, I'm left with nothing."
        "Seriously. Is she coming to see me tonight or not?"
        scene bg street1 eve with blink
        "Trudging back home is all I can do, as I wait for her to contact me again."
        "Just... waiting on her."
        scene bg k kitchen eve with blink
        "It's... okay, it's a little frustrating if I'm honest."
        "I didn't realize it at the time, but with how she's arranged things between us, it's like waiting on her is all I can do."
        "She's the one calling all the shots here."
        play sound doorbell
        "The doorbell sounds, just as I'm done washing up after dinner."
        scene bg k entrance eve with blink
        "So... great, she's at the door and I'm all wound up."
        "I gotta get it together."
        play sound doorbell
        "... I also gotta let her in."
        play sound dooropen
        show Nozomi front smile
        n "Oh, there you are~" with dissolve
        play music Downtown
        "Nozomi's all smiles as she lets herself in while I hold the door open."
        play sound doorclose
        n side smile "I don't have a lot of time today, but I got here as soon as I could." with dissolve
        "I'm happy to see she's here and acknowledging me at last, just as we agreed but..."
        n smile_side "... I'm sorry, did I come at a bad time?" with dissolve
        "Did she really not consider me at all until now?"
        "Compared to how she is to me at school it's like a switch has gone off in her head."
        show Nozomi sad
        "Almost like she's under a hypnotic suggestion, come to think of it." with dissolve
        n front concerned "... Kyou? I need you to talk to me." with dissolve
        ks "N-no it's not a bad time for me, it's just..."
        "... It's no good. I can't tell her I'm having trouble with what we've arranged."
        "I'm not gonna risk losing what little I have with her."
        ks smile "I've just been looking forward to this all day, you know?"
        n side smile blush "O-oh... yes, same here." with dissolve
        scene bg k room eve
        show Nozomi side smile at center
        with blink
        "Just the fact that she wants to be here with me now is amazing."
        n sad_closed "So it really is a shame that I can't stay here for long." with dissolve
        "I don't want to stop seeing her, even if it has to be like this."
        ks sigh "Yeah..."
        n smile noblush "So with that in mind, I've been thinking about what we should do tonight." with dissolve
        ks neutral "You have?"
        n front smile "Mhm! I'd like us to try expanding on what we did yesterday." with dissolve
        n pout_left "Verbal triggers are fun, but I wanted to see if we could do something with a gesture." with dissolve
        "I had some ideas of my own, but if she's been planning something then I should probably go along with that."
        "Besides, this sounds interesting. I want to see where she's going with this."
        ks smile "Okay. So what are you thinking?"
        "She doesn't answer immediately, taking a halting breath before apparently deciding to let her thoughts out."
        n sigh "A-alright, so... I thought you could have this gesture put me back into a trance state and you'd be able to pass a simple suggestion to me while doing so." with dissolve
        n blush "Then I could immediately wake and act as if the suggestion were my own thought?" with dissolve
        "Huh. Okay, I guess that tracks with how much she likes being hypnotized that she'd want another way for me to do it."
        ks smile "Okay, sounds good. What kinds of suggestions, though?"
        n pout_left "W-well, I mean nothing lewd obviously. Just simple things to mess with me a little." with dissolve
        ks "Such as?"
        n sleeptalk_concerned "I can't tell you!" with dissolve
        "Okay, this is starting to get confusing."
        ks neutral "Uh... why not?"
        n side sad_closed "B-because... it's about the surprise? It's no fun if I know exactly what's coming." with dissolve
        ks sigh "Okay, I just... I don't want to break one of your rules and piss you off, that's all."
        "Although from her agitation it feels like just asking her questions is doing that."
        n sad_side noblush "Look, Kyou, I understand but as long as you don't suggest anything wildly inappropriate the worst that'll happen is I don't go along with it." with dissolve
        n sad "You know about the hidden observer effect, don't you?" with dissolve
        ks confused "The... hidden..."
        "Oh wait, I know this!"
        ks frown "Y-yeah, you mean how you always sorta know what's going on when you're hypnotized, even if you seem completely out of it."
        n front sleep "Mhm. It's like they say: \"All hypnosis is self-hypnosis\"." with dissolve
        n neutral "You might be the one guiding me while I'm hypnotized, but ultimately I'm still the one who decides whether to follow or not." with dissolve
        n side frown_side "It's just like we were talking about last night, when I still followed your post-hypnotic suggestion even when I thought I was resisting it." with dissolve
        ks "So... you think maybe your \"hidden observer\" always knows what you really want?"
        n smile_side "Yes, that's what I'm thinking." with dissolve
        n side smile "So... this is all going to be fine. I want you to have some fun with this. You have my permission, okay?" with dissolve
        n frown "Just... like I said, don't be lewd." with dissolve
        ks sigh "Okay, okay. I think I get it."
        show cg k room eve
        show NozomiHypno standing smile
        with blink
        "Apparently satisfied, Nozomi sits herself down and fishes her phone out of her pocket to give to me."
        "I smile back at her as I set her phone to record. I guess we're still doing this, then."
        ks smile "By the way, we didn't decide on the gesture."
        ncg neutral "Oh, right..." with dissolve
        ncg stern_closed "I mean, I was thinking... you could touch my forehead while you're making the suggestion?" with dissolve
        ks confused "You want me to touch you?"
        ncg angry "I-It's just my forehead! Don't make a big deal of that!" with dissolve
        ks sigh "Sorry, I just... It's surprising."
        ncg stern_closed "It's really not surprising at all." with dissolve
        ncg "I just... I just thought it made a neat image, just thinking you're pushing the suggestion directly into my brain like that."
        ncg stern "B-but if you don't think you can handle that, you're free to suggest something else." with dissolve
        "I wince a little at her chiding. I just didn't think she'd be comfortable with me touching her face, not that I can't handle myself."
        "It's just her forehead, goddammit."
        "Although I DID have something else in mind..."
        ncg annoyed "Well? We don't have a lot of time, you know." with dissolve
        show penlight at right with moveinright:
            ypos 0.346
        "Nodding, I pull out my penlight from my pocket and turn her phone's camera at her to signal my intentions."
        ks "A-alright then, I'm gonna get us started."
        ncg confused "Huh? You're not going to..." with dissolve
        "She then shakes her head."
        ncg stern "Oh, nevermind. But you haven't decided on a gesture yet." with dissolve
        ks smile "I have, actually."
        ks "It's... well, like you said, it's about the surprise."
        hide penlight at right with moveoutright
        show NozomiHypno smile_closed
        "I can hear her chuckle slightly as she leans back on the couch." with dissolve
        ncg lookup "Alright, Kyou. Surprise me." with dissolve
        $ light_x = 0.43; light_y = 0.26
        call cglightshow from _call_cglightshow_71
        "I smile back as I sweep the penlight's beam across her face as I take a breath and start my induction."
        ks smile "I will. So for your part, focus on looking up at the light just like before."
        call cglightshow from _call_cglightshow_72
        ks "That's right. Already feeling so familiar about this light. Already feeling your eyelids start to pull closed."
        call cglightshow from _call_cglightshow_73
        ks "Because the light is irresistible, Nozomi. You see the light and you stare."
        call cglightshow from _call_cglightshow_74
        ks "See the light, and stare..."
        stop music fadeout 20.0
        call cglightshow from _call_cglightshow_75
        show NozomiHypno drowsy
        $ renpy.transition(longdissolve, layer="master")
        ks "And you don't need me to tell you how heavy your eyelids are getting."
        $ light_y = 0.3
        call cglightshow from _call_cglightshow_76
        ks "Because you already know it's true, Nozomi. Eyelids heavy, almost closing, feeling so warm and relaxed as you start to go deep."
        call cglightshow from _call_cglightshow_77
        ks "Sinking deeper, Nozomi. You know you can feel it as the light takes you down."
        call cglightshow from _call_cglightshow_78
        show NozomiHypno drooping sleepy
        $ renpy.transition(longdissolve, layer="master")
        ks "So naturally. So automatically. So ready to drop deeper at my word."
        $light_y = 0.36
        call cglightshow from _call_cglightshow_79
        ks "So I'm telling you now, Nozomi..."
        call cglightshow from _call_cglightshow_80
        show NozomiHypno sleep
        ks "Sleep." with dissolve
        play music Flow fadein 10.0
        "Returning the penlight to my pocket, I continue talking gently to her."
        ks "Feeling so good about dropping deeper, Nozomi. Deep asleep. Your mind ready to listen and accept my words once more."
        ks "Because what I'm about to say to you is going to feel completely and utterly true to your mind."
        ks "It doesn't matter how awake you seem in the future, this truth will always be in effect. Understand, Nozomi?"
        ncg sleeptalk "I understand..." with dissolve
        show NozomiHypno sleep
        ks "Very good, Nozomi. Going deeper." with dissolve
        "Okay, so... I know what gesture I want to do for this."
        "Just gotta phrase this whole thing properly..."
        ks neutral "From now on, if at any moment in time I and only I..."
        menu:
            "Press my fingertip on your forehead":
                $gesture = "forehead"
            "Wave my hand in front of your face":
                $gesture = "hand"
        ks "And I tell you a suggestion, you will find your mind become blank while you absorb this suggestion as if it were entirely your own thought."
        "Maybe I could also have her do something to confirm she understood. And make it just a little more fun for me..."
        menu:
            "Have her repeat the suggestion aloud":
                $hypnorepeat = True
                ks "As you absorb my suggestion, you will also repeat it to yourself quietly, to show that you understand."
            "Don't have her say anything":
                $hypnorepeat = False
                "Nah. It'll be enough to see her go blank for a moment to know it's worked."
        ks "As soon as you have fully absorbed the suggestion, your mind will return to wakefulness, having accepted my suggestion as your own thinking and reality."
        ks "Understand, Nozomi?"
        ncg sleeptalk "Understand..." with dissolve
        show NozomiHypno sleep
        "I gotta admit, this could be a lot of fun if it works." with dissolve
        ks smile "Very good. Feeling so good for having accepted your new truth."
        ks "Keeping this wonderful feeling as you begin to wake now, on a count of five."
        stop music fadeout 10.0
        ks "One... two, breathing deep, feeling happy and refreshed."
        ks "Three... letting the life come back to your limbs."
        ks "Four... taking another breath now, testing your eyelids."
        show NozomiHypno sleepy
        ks "And five, wide awake now, Nozomi." with dissolve
        show NozomiHypno standing confused
        $ renpy.transition(longdissolve, layer="master")
        "I chuckle a little as Nozomi's sleepy eyes flutter open while she comes to."
        "I hope I never get used to seeing her wake up from trance like this."
        ks "Hey."
        show NozomiHypno smile
        play music Bright_Opening
        "Nozomi smiles as she registers me, and runs a hand through her hair while she readjusts herself on my couch." with dissolve
        ncg "Did you do it?"
        if gesture == "forehead":
            show CouchHypno nozomi n_smile glasses kyou_down with blink
            "I'm about to answer before the thought crosses my mind..."
            "She wanted to be messed with, right?"
            ks "Do what?"
            show CouchHypno n_grumpy
            ncg folded annoyed "You know what I'm talking about." with dissolve
            ks "Yeah, but er..."
            ks "Do YOU know what we're talking about?"
            show CouchHypno n_angry_open
            ncg angry "Wh-what?! Is this your idea of messing with me?" with dissolve
            "Her irritation is enough to distract her that she barely sees my hand dart out as I poke her forehead."
            show CouchHypno n_surprised kyou_point
            "Uh, maybe in my haste I poked her harder than I intended." with dissolve
            show CouchHypno n_dazed
            ks "You don't know what we're talking about." with dissolve
            if hypnorepeat == True:
                show CouchHypno n_tranced
                ncg drowsytalk "{size=16}I... don't know what we're talking about.{/size}" with dissolve
                "But it seems to make no difference as she blankly repeats my suggestion."
            elif hypnorepeat == False:
                show CouchHypno n_tranced
                $ renpy.transition(dissolve, layer="master")
                "But as I withdraw my hand, I can see the vacant look in her eyes."
            show CouchHypno n_neutral kyou_down
            "Smiling as I put my hand back in my lap, I watch her reaction carefully as she momentarily regains her awareness." with dissolve
            show CouchHypno n_surprised
            ncg surprised "Wait... what were we talking about?" with dissolve
            ks "You seriously don't know?"
            show CouchHypno n_puzzled
            ncg confused "U-uh..." with dissolve
            ncg stern "Remind me?"
            ks "Haha, we were just talking about the gesture trigger you wanted."
            show CouchHypno n_neutral
            ncg stern_closed "Agh... of course." with dissolve

        elif gesture == "hand":
            ks smile "Sure did."
            ncg laugh "So maybe I shouldn't let you touch my forehead, huh?" with dissolve
            "Nozomi grins, but I just shake my head and chuckle at her."
            ks "I went with something else. It's way better."
            show NozomiHypno neutral
            "Nozomi seems a little disappointed that I didn't do exactly as she asked." with dissolve
            ncg neutral "Oh... Well, what did you do then?"
            ks "I made it a hand wave across your face instead."
            ncg confused "A... hand wave? Like in those movies?" with dissolve
            "I don't answer, but I can't stop my mouth from forming an embarrassed grin."
            ncg stern "Oh Kyou, you didn't." with dissolve
            ks "I did."
            show CouchHypno nozomi n_grumpy glasses kyou_down with blink
            "Nozomi snorts and rolls her eyes at me."
            ncg annoyed "You're such a nerd, you know that?"
            "I laugh, but when she puts it like that I do feel a little self-conscious."
            show CouchHypno kyou_wave
            "She definitely needs to be set straight, as I obnoxiously sweep the palm of my hand across her face." with dissolve
            show CouchHypno n_dazed
            $ renpy.transition(dissolve, layer="master")
            ks blush "Y-you think the hand wave is way cooler than your idea."
            show CouchHypno n_tranced
            $ renpy.transition(dissolve, layer="master")
            "As my hand passes over her eyes, I can see them glaze over while I speak."
            if hypnorepeat == True:
                ncg drowsytalk "{size=16}I think the hand wave is way cooler than my idea...{/size}"
            show CouchHypno n_dazed kyou_down with dissolve
            "Man, that's hot. I gotta do another."
            show CouchHypno kyou_wave
            $ renpy.transition(dissolve, layer="master")
            ks "You're a much bigger nerd than me."
            if hypnorepeat == True:
                show CouchHypno n_tranced
                ncg drowsytalk "{size=16}I'm a much bigger nerd than you...{/size}" with dissolve
            show CouchHypno n_tranced kyou_down with dissolve
            "Noticing her eyelids flicker again, I take my hand back and look at her incredulously."
            show CouchHypno n_neutral
            ks frown noblush "Really? If anyone's a nerd around here it's you, Nozomi." with dissolve
            "Nozomi blinks as I challenge her, before momentarily breaking into embarrassed laughter."
            show CouchHypno nozomi_blush n_laugh
            ncg laugh blush "Well... that's true, ahaha~" with dissolve
            show CouchHypno nozomi n_smile
            ncg smile noblush "I'm just mad I didn't think of the hand-waving first. It's so much cooler than my lame idea." with dissolve
            ks smile "Ehehe... for sure."
        "Okay. I did what she wanted, but now what?"
        "\"Nothing lewd obviously. Just simple things to mess with me a little.\""
        show CouchHypno n_neutral
        ncg stern "So have you tried it yet? Does it work?" with dissolve
        ks "I... haven't tried it, no."
        ncg neutral "So, what're you waiting for?"
        ks "For just the right moment."
        "Nozomi starts to pout, her mind clearly turning."
        show CouchHypno n_grumpy
        ncg annoyed "I bet it's because you can't think of anything to do with it that isn't lewd." with dissolve
        "... She's not exactly wrong. I mean, just thinking I can suggest anything to a girl like her and she'll think it's her idea?"
        "What kinda guy would I be if I didn't have any dirty thoughts at all concerning that?"
        show CouchHypno n_angry_open
        ncg stern "I can see you blushing, you know." with dissolve
        "Ah, shit. She's the one who's hypnotized, so why is it she's the one reading my mind?"
        if gesture == "hand":
            show CouchHypno n_surprised kyou_wave
            $ renpy.transition(dissolve, layer="master")
            "That's it. Raising my hand, I sweep it across her face again as I speak as confidently as possible."
        elif gesture == "forehead":
            show CouchHypno n_surprised kyou_point
            $ renpy.transition(dissolve, layer="master")
            "That's it. Raising my hand, I reach over and quickly press my fingertip to her forehead again, a little more gently this time."
        "I gotta level the playing field."
        show CouchHypno n_dazed
        ks frown "You believe I can read your mind." with dissolve
        if hypnorepeat == True:
            show CouchHypno n_tranced
            ncg drowsytalk "{size=16}I believe you can read my mind...{/size}" with dissolve
        show CouchHypno n_dazed kyou_down with dissolve
        ks "W-well, if I am it's only because I know what YOU'RE thinking!"
        show CouchHypno nozomi_blush n_surprised
        ncg surprised blush "U{nw}{w=0.2}" with dissolve
        extend "-UHHHH!?" with vpunch
        "Oh... oh man, that's an even bigger reaction than I was hoping for."
        "... Wait, then what IS she thinking right now? Do I even wanna know?!"
        ks smirk "Y-yeah, you wanna explain those thoughts to me, Nozomi?"
        ncg "I-i-it's a perfectly normal thing to think about!"
        ks "You sure don't seem to think so."
        show CouchHypno n_angry_closed
        ncg stern_closed "Rrrrghhhh..." with dissolve
        ks "Wow, and what about THAT thought?"
        show CouchHypno nozomi_headclutch_blush nozomi_armsup n_angry_open
        ncg angry "AAHH! NONONO GETOUTOFMYHEAD!" with vpunch
        show CouchHypno n_angry_closed
        "I laugh as Nozomi clutches her scalp, clenches her eyes shut and exhales sharply, like she's suddenly started to concentrate hard." with dissolve
        ks smile "Hahaha, what are you doing now?"
        show CouchHypno nozomi nozomi_armsdown
        $ renpy.transition(dissolve, layer="master")
        ncg "As if you can't already tell..."
        ks smile "You're... trying to clear all the thoughts out of your head so I can't read them?"
        "She doesn't answer, but it hardly takes a genius to guess that's what she's attempting."
        ks "Well, I can help you with that."
        show CouchHypno n_surprised
        ncg stern "Huh?" with dissolve
        if gesture == "hand":
            show CouchHypno kyou_wave
            $ renpy.transition(dissolve, layer="master")
            "As her eyes open quizzically, I wave my hand in front of her nose once more."
        elif gesture == "forehead":
            show CouchHypno kyou_point
            $ renpy.transition(dissolve, layer="master")
            "Her eyes start to open inquisitively, just in time to see my fingertip press against her forehead once more."
        show CouchHypno n_dazed
        stop music fadeout 5.0
        ks "You have no thoughts." with dissolve
        show CouchHypno n_tranced
        if hypnorepeat == True:
            ncg drowsytalk "{size=16}I have no thoughts...{/size}" with dissolve
        show CouchHypno kyou_down
        $ renpy.transition(dissolve, layer="master")
        ncg "..."
        "I watch her face for a moment as she seemingly stares vacantly into the distance."
        ks "Anybody home?"
        ncg "..."
        ks "Nozomi?"
        "Seriously. It's kind of eerie how the light switched off in her head like that. She almost looks like a mannequin with how lifeless she seems right now."
        show CouchHypno n_drool
        $ renpy.transition(dissolve, layer="master")
        "Almost, as I notice she's starting to drool out of one corner of her mouth where she let it hang open."
        "She'll snap back to life eventually I'm sure, but right now it almost feels like I could leave her like this for hours and come back to find her exactly the same."
        "Although that reminds me, she said she didn't have long before she had to leave."
        if gesture == "hand":
            show CouchHypno kyou_wave
            $ renpy.transition(dissolve, layer="master")
            "So once more, I sweep my hand over her vacant eyes..."
        elif gesture == "forehead":
            show CouchHypno kyou_point
            $ renpy.transition(dissolve, layer="master")
            "So once more, I gently press my index finger against her forehead."
        ks neutral "You will drop back into a deep, hypnotic trance."
        play music Flow fadein 10.0
        if hypnorepeat == True:
            ncg drowsytalk "{size=16}I will drop back into a deep, hypnotic trance...{/size}"
        show CouchHypno nozomi_sleep n_none noglasses kyou_down
        $ renpy.transition(longdissolve, layer="master")
        "Time to finish for tonight..."
        ks "Very good, Nozomi. You're so good at this, dropping deep, back into this hypnotic trance that makes you feel so wonderful."
        if gesture == "hand":
            ks "So now, while you're so deep, listening only to my voice, I want you to think of all the things I suggested to you while waving my hand in front of your face."
        if gesture == "forehead":
            ks "So now, while you're so deep, listening only to my voice, I want you to think of all the things I suggested to you whenever I pressed my fingertip to your forehead."
        ks "And now Nozomi, I want you to imagine each and every one of those suggestions leaving your mind. Each and every one losing their influence..."
        ks "Each and every one of those suggestions no longer having any affect on you whatsoever. Understand?"
        ncg sleeptalk "I understand..."
        ks smile "I knew you would, Nozomi. You're so good at being hypnotized. So good at following instructions."
        ks "And in a moment I'm going to wake you up from this trance, and you're going to remember what we did together."
        ks "Waking up on a count of three, Nozomi. One..."
        stop music fadeout 5.0
        ks "Two... feeling refreshed, nice deep breath..."
        ks "And three, rise and shine."
        hide CouchHypno
        show NozomiHypno standing drowsytalk
        $ persistent.nozomi_mindtrick_unlock = True
        with blink
        "Nozomi moans as she flickers slowly back into life."
        play music Downtown
        "I smile at her as she takes a moment to settle back into her own head. She really seemed to be out of it just now."
        ks "Hey. You doing okay?"
        show NozomiHypno confused
        "She still seems to be getting her bearings when I ask, but she eventually replies softly." with dissolve
        show NozomiHypno neutral
        ncg "Y-yeah. Sorry, I'm still waking up." with dissolve
        ks smile "I can tell. I think you went even deeper that time."
        "Turning off Nozomi's phone from recording, I place it back into her hand as she stretches her back."
        ncg smile "Oh gosh, you might be right~ I was..." with dissolve
        "Blinking, she registers the phone in her hand as she stares at the screen."
        ncg sad "Ah, I really need to go!" with dissolve
        scene bg k room eve
        show Nozomi front sigh at center:
            ypos 1.2
            linear 2.0 ypos 1.0
        with blink
        "It's hard not to look upset as Nozomi rises shakily to her feet."
        show Nozomi:
            ypos 1.0
        ks "You can't stay just a little longer?"
        n side sad_side "Sorry, Kyou. I'm already going to be late back." with dissolve
        stop music fadeout 5.0
        n sad "Talk to you soon, okay?" with dissolve
        scene bg k bedroom night with longblink
        "Goddamn, I'm so worked up right now."
        play music Past_Sadness
        "She said she didn't have time, but it still feels weird that she didn't have a moment for me once I was done giving her what she wanted."
        "Makes me wonder if she really needed to bail so quickly."
        "But all that matters now is that she's gone, and I miss her already."
        "This feeling of longing I have. This... this powerlessness."
        if gesture == "hand":
            "I gotta admit, when she was about to go I thought about waving my hand in front of her face and telling her to stay."
        elif gesture == "forehead":
            "I gotta admit, when she was about to go I thought about touching her forehead and telling her to stay."
        "It would've been stupid to try. She was awake and aware and, more to the point, she wasn't going to let me stop her."
        "I can't use hypnosis to literally force my will on her, I know that's not how it works."
        "But still, in the moment it almost seemed worth the risk of making her mad just to see if she'd go along with it."
        "... I'm such an idiot, thinking about shit like this."
        stop music fadeout 5.0
        "I just gotta enjoy what I have with her..."
        scene bg blackscreen with longdissolve
        pause 2.0
        jump Day5_Con_Kyou_Nozomi_Trance

    elif hypno2 == "trancenoncon":
        play music Bright_Opening fadein 5.0
        "But I have a feeling today is going to be a lot more fun."
        scene bg classroom day with blink
        "I make it to class as usual and take my seat, flashing a Nozomi a knowing smile as she enters a little after me."
        show Nozomi front smile with dissolve
        pause 0.8
        hide Nozomi with dissolve
        "She acknowledges me with a nervous smile of her own before taking her seat as lessons begin."
        scene bg classroom day with blink
        play sound schoolbell
        "As time passes to lunchtime, I look to Nozomi's desk and wait for the fun to begin."
        show Nozomi side smile_side at center, flip:
            xpos 0.25
        show Sayori smile at center:
            xpos 0.5
        show Hiroko happy uniform_arm at center:
            xpos 0.75
        with dissolve
        h "All right! Time to get out of here and head to the r- {w=1.4}{nw}"
        n surprised_side "U-uh, Hiroko, hold that thought." with dissolve
        h surprised_side "Huh?" with dissolve
        n smile_side "Eheh, I mean... there's no need to say it. Let's just go~" with dissolve
        s "Is everything alright, Nozomi? You seem somewhat flustered."
        n laugh "Ahaha, everything's fine, Sayori. I just... I guess this morning's lessons took a lot out of me." with dissolve
        show Nozomi smile_side
        show Hiroko smile_side
        "Ugh, she deliberately cut them off from saying it. Makes me wonder if I should've made her forget the trigger yesterday." with dissolve
        "Still, all I have to do is wander near them before they head out the classroom and loudly say to myself:"
        ks smile "Ahh, glad that's over. I guess I'll do lunch on the rooftop today~"
        n surprised blush "E{nw}" with vpunch
        extend"-Eek!" with dissolve
        show Sayori concerned
        h surprised_side "Nozo? What's up?" with dissolve
        if hypno4 == "arousal":
            show Nozomi smile_side
            "I notice Nozomi biting her lip, then composing herself with a smile and shaking her head." with dissolve
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
        "I quickly spot Nozomi's group and set down for lunch a short distance from them. Close enough to overhear their conversations."
        h "Did {nw}"
        extend "ANYONE get what Mr. Kobayashi was talking about? That dude mumbles so much." with vpunch
        show RoofSayori sleep
        s rolleyes "Or you are a poor listener. He was talking about club commitments for this weekend." with dissolve
        show RoofHiroko annoyed
        h annoyed_side "Oh. Like I don't already know that shit." with dissolve
        if hypno4 == "spank":
            show RoofNozomi pain_left
            n concerned "Mmm... h-how is your club doing anyway, Sayori?" with dissolve
        elif hypno4 == "tickle":
            show RoofNozomi strainedsmile_left
            n side smile_side "Mhmhm... h-how is your club doing anyway, Sayori?" with dissolve
        show RoofSayori neutral
        s neutral_right "Not so bad. I mostly help the other members in my club, though, so it hasn't been as useful for me as I'd hoped." with dissolve
        show RoofSayori sleep
        s annoyed "I would be better off studying at home, but I will not abandon my obligations to the study club." with dissolve
        n "T-to think you nearly joined the literature club with me."
        show RoofSayori neutral
        s "Yes, well, I am not going to get hung up about that." with dissolve
        show RoofHiroko worried
        h sad_side "You okay, Nozo? You're really, like... antsy today." with dissolve
        "I can see Nozomi squirming in her seat from here, even as she's clearly trying to disguise it."
        if hypno4 == "spankl":
            show RoofNozomi pain_right
            n "I-I'm fine... Really, I'm fine~" with dissolve
        elif hypno4 == "tickle":
            show RoofNozomi strainedsmile
            n "Ehehe, I'm okay, really~" with dissolve
        $sface = "concerned right"
        show RoofSayori worried
        s concerned_right "Are you sure? It really looks like you're struggling with something." with dissolve
        show RoofNozomi smile_left blush
        n smile_side blush "Thanks for your concern, but..." with dissolve
        show RoofHiroko smile
        h uniform_armup smile_side "C'mon! You can share anything with rooftop club~" with dissolve
        show RoofNozomi panicked_right with dissolve
        n "!! {w=0.8}{nw}"
        if hypno4 == "spank":
            show RoofNozomi grimace
            show RoofHiroko surprised
            n reddened front sleeptalk blush "Ooohhhhh..." with dissolve
        elif hypno4 == "tickle":
            show RoofNozomi laugh motionlines
            show RoofHiroko surprised
            n laugh blush "Ahahahaha!" with dissolve
        h surprised_side "Huh? What's so funny?"
        if hypno4 == "spank":
            "Nozomi cups a hand to her mouth, looking like she's suppressing a moan, before she speaks up."
            n "It's... ahh, s-something I have to deal with myself."
            s "Uh... you know, Hiroko, I think this is a burden she doesn't have to share with us."
        elif hypno4 == "tickle":
            "Nozomi lets out an amused giggle and shakes her head, jerking her hand away as she realizes she had reached down to grab her shoe."
            n "N-n-no, there's nothing to share! R-really!"
            show RoofSayori smile
            s smirk_right "Are you sure? Because whatever you are thinking of must be hilarious." with dissolve
            n "Hahaha~ N-no, not at all!"
            show RoofHiroko laugh
            h laugh_side "Aww, you gotta tell us!" with dissolve
            n "Ehehehehe~"
            s "We are not ones to judge. It'll just be between us."
            n "Th-th-there's nothing to tell!"
            stop music fadeout 5.0
            s "What is said in rooftop club-{w=0.8}{nw}"
            show RoofNozomi panicked_left
            n surprised_side "N-NO!{w=0.5}{nw}" with dissolve
            s "-stays in rooftop club."
            show RoofNozomi laughing
            show RoofHiroko shocked
            show RoofSayori shocked
            $ renpy.transition(dissolve, layer="master")
            n front cry_laugh reddened "AAAAHAHAHAHAHA!" with shake
            play music Measured fadein 5.0
            "It's hard not to react as Nozomi bursts out laughing, sending one of her shoes flying as she kicks her feet back and forth frantically."
            "Any notion she had of trying to resist the hypnosis-induced tickling is dashed in a wave of hearty giggling."
            "Certainly the few others assembled on the roof are looking her way now. How could they not?"
            h "Nozo? What's so freakin' funny?"
            if accepted_terms == True:
                "And right now, I realize, I maybe should have given some more thought to this..."
            else:
                "And as I watch with the others, I find it fascinating to see how completely committed her mind is to my hypnotic suggestion."
            n "M-m-make it stohohohohop!" with vpunch
            show RoofSayori worried
            s "Make what stop? What is happening?" with dissolve
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
            s annoyed_right "Hiroko, if you knew what word she meant why would you say it?" with dissolve
            "... Right?"
            show RoofHiroko angry
            h angry_side "H-hey, {w=0.2}I'm fuckin' {nw}" with dissolve
            extend "CONFUSED, alright?" with vpunch
            scene bg blackscreen
            play sound bodyimpact
            with dissolve
            $persistent.nozomi_rooftop_tickled_unlock = True
            "As they argue, Nozomi collapses onto the floor, clutching her sides as she convulses to the sound of her own manic laughter."
            show RoofNozomi2 nozomi_tickled hardlaugh lines_tickled with dissolve
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
            $persistent.nozomi_rooftop_tickle2_unlock = True
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
            if accepted_terms == True:
                "The sound of the bell must be the biggest relief to Nozomi's ears as she's presumably freed from the phantom tickling sensations that tormented her." with dissolve
                "Drawing a full breath, she picks herself up off the floor with her friend's help."
            else:
                "My words must be the biggest relief to Nozomi's ears as she finally starts to recover from her giggling fit." with dissolve
                "Drawing a full breath, she picks herself up off the floor with her friend's help."
            show Nozomi:
                ypos 1.0
            n "Haaah... haaah..."
            s sleep "Oh, thank goodness you've calmed down." with dissolve
            n "S-sorry to worry you. I'm... I'm okay now."
            h "Geez, Nozo, I never knew you could laugh like that."
            if accepted_terms == True:
                n side smile_side "Mhmhm... let's just head back, okay?" with dissolve
                s concerned "... Of course." with dissolve
                show Hiroko frown
                "Just then, the pink-haired girl glares in the direction of me and the other assembled onlookers." with dissolve
                h "What are {nw}"
                extend "YOU looking at? Show's over." with vpunch
            else:
                n side smile_side "Mhmhmhm..." with dissolve
                show Nozomi smile
                "As she takes another breath, Nozomi flashes me a look. Seeing and hearing me speak was the only thing that saved her from laughing herself to exhaustion." with dissolve
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
                n smile_side "Kyou hypnotized me last night and made it so I'd feel tickled all over if anyone said..." with dissolve
                show Hiroko surprised_side
                n front pout_left uniform_folded "Well, I'm not going to say it." with dissolve
                h "\"Hypnotized\"?"
                s surprised "Now I am even more confused." with dissolve
                n side frown_side noblush "About what? I thought I'd explained pretty clearly." with dissolve
                h frown uniform_arm "So you two gotta thing going on now?" with dissolve
                n smile_side "Well, yes. I guess we do. We share a common interest it turns out~" with dissolve
                play sound schoolbell
                show Hiroko frown
                "The sound of the bell rings out on the roof, helping to keep further questions at bay as everyone makes for the exit." with dissolve
                s annoyed "This is not over. We'll continue this later." with dissolve

        stop music fadeout 5.0
        if accepted_terms == True:
            scene bg k room eve with blink
            if hypno4 == "arousal":
                "The rest of the day was awkward. Nozomi's little incident was whispered about during lessons, and it was all she could do to pretend not to notice."
            elif hypno4 == "tickle":
                "The rest of the day was awkward. Nozomi's giggling fit was whispered about during lessons, and it was all she could do to pretend not to notice."
            "I headed straight home alone, having sent her a text inviting her over any time she was ready."
            play sound doorbell
            "... That was quick. I've barely gotten home myself."
            play sound dooropen
            show Nozomi front concerned with dissolve
            play music Measured fadein 5.0
            n "So... We really need to talk about today, huh."
            play sound doorclose
            ks sigh "Yeah... That was a bit more intense than I was going for."
            $nface = "sleeptalk concerned"; nclothes = "uniform folded"
            n sleeptalk_concerned uniform_folded "Oh my god... I thought I was going to die." with dissolve
            if hypno4 == "arousal":
                n "I was so... I nearly just... relieved myself, right there in front of everyone."
            elif hypno4 == "tickle":
                n "It was like a dozen tiny hands were tickling me all over, and there was nothing I could do to stop them."
            n blush "And everyone was staring at me. They all knew." with dissolve
            n concerned "Kyou, this is going to follow me for the rest of my school career." with dissolve
            n "So I... I think the public trigger was a bad idea and I never should have agreed to it."
            ks "I'm sorry, Nozomi. I probably should've been more careful when setting it."
            n sleeptalk "Yeah..." with dissolve
            n pout_left uniform "So... I was thinking some more about what to do." with dissolve
            ks neutral "Yeah?"
            n "I want you to remove the trigger, Kyou. You can do that, can't you?"
            ks "I think so. I haven't tried to de-program you yet, but I don't see why I couldn't."
            show Nozomi sleep
            "She responds with a tentative nod." with dissolve
            n "Right. And then I'd like us to try something else. We could consider it a trade of sorts."
            "... What on earth is she thinking now?"
            ks "Go on..."
            n "I want you to try conditioning some behaviours into me."
            n side sad_closed blush "S-submissive ones. Towards you." with dissolve
            ks surprised "... Wait, what?"
            n sad "O-only for in your house! And, only when we're alone." with dissolve
            n front surprised reddened "And NOTHING lewd! Oh gosh, I should've mentioned that sooner." with vpunch
            ks "But still, that's..."
            n sleeptalk_concerned normal uniform_folded "Weird. And stupid and embarrassing to say out loud, but I don't think I could feel more humilated than I did this afternoon, so I'll get this out now." with dissolve
            n "Because as humiliating as that was, I still couldn't help but feel how much I enjoyed being powerless. Knowing I was feeling that way because you hypnotized me to."
            n side sad_closed "And being unable to resist your programming, even though in the moment I wanted to more than anything." with dissolve
            n "I can't even begin to describe how intoxicating it all felt."
            n frown "So... I want to have that experience again, just not where it might seriously come back to hurt me." with dissolve
            n front concerned "W-what do you think?" with dissolve
            ks "It's... T-that is..."
            n angry normal "Oh come {w=0.4}{nw}" with dissolve
            extend "ON, Kyou! How many guys do you think get a chance like this?" with vpunch
            "I jump back a little as she raises her voice, and it jolts my brain back into gear." with dissolve
            "Do I really have any objections to this? Why not give her what she wants?"
            "And why not do it in a way she'll approve?"
            show Nozomi surprised
            "With a smile, I pull my penlight out from its home in my pocket, which immediately grabs Nozomi's attention." with dissolve
            ks smirk "I'll make that the last time you raise your voice to me in this house, young lady."
            $light_x = 0.43; light_y = 0.25; ldirection = "right"; lnumber = 1
            stop music fadeout 10.0
            call lightshow from _call_lightshow_123
            "And with that I flash the light across her eyes, causing her to immediately snap her gaze to it with a peculiar longing."
            n "K-kyou..."
            call lightshow from _call_lightshow_124
            ks "Shhh, Nozomi. Don't say anything more."
            call lightshow from _call_lightshow_125
            show Nozomi drowsy
            ks smile "You know you can't resist the light. There's no need to try." with dissolve
            call lightshow from _call_lightshow_126
            # $n = Character("[nozomi_name]", image = "NozomiHypno", who_color = "#93624B")
            $ light_y = 0.37; light_x = 0.4
            scene bg blackscreen with dissolve
            show cg k room eve:
                ypos -0.3
                linear 0.2 ypos 0.0
            show NozomiHypno drooping sleepy:
                ypos -0.3
                linear 0.2 ypos 0.0
            "As I finish flashing the light again I reach out and firmly push on her shoulder, causing her to stumble back onto the couch behind her."
            play music Flow fadein 15.0
            call cglightshow from _call_lightshow_127
            "She already looks out of it and I've barely said anything to her. Her prior conditioning must be doing most of the work for me."
            "Of course it crossed my mind that I could've just used the spoken trigger to put her under, but doing it this way again just feels so right for this occasion."
            call cglightshow from _call_lightshow_128
            ks "That's right, Nozomi. Just keep looking at the light..."
            call cglightshow from _call_lightshow_129
            ks "Looking and relaxing. Looking and drifting..."
            call cglightshow from _call_lightshow_130
            ks "Finding yourself so completely relaxed... Sleep, Nozomi." with dissolve
            show NozomiHypno sleep
            "And down she goes." with dissolve
            ks "Very good, Nozomi. Nice and deep for me. Completely relaxed."
            ks "And now I need you to listen and accept what I have to tell you. Completely accepting my words. Can you do that, Nozomi?"
            ncg "Mhm..."
            if hypno4 == "arousal":
                ks "Yes you can. You need to accept the word \"rooftop\" will no longer induce any feelings of arousal in you."
            elif hypno4 == "tickle":
                ks "Yes you can. You need to accept the word \"rooftop\" will no longer induce any ticklish feelings in you."
            ks "It is a perfectly normal word and you will not react to it in any special way."
            "There. That should stop any repeat of what happened this afternoon."
            ks "You must also accept that while we are alone in this house you will find that anything I tell you to do becomes an irresistible command that you must obey."
            ks "Do you understand, Nozomi?"
            ncg sleeptalk "Yes... I understand..." with dissolve
            show NozomiHypno sleep
            ks "And do you accept everything you have been told so far?" with dissolve
            ncg "Mhm..."
            ks "Wonderful."
            "This should be fun to try out. But before that, I need to add one more thing..."
            ks "Now, I want you to say something for me, and I want you to say it calmly and quietly."
            ks "Say \"I cannot raise my voice\"."
            ncg sleeptalk "{size=16}I cannot raise my voice...{/size}" with dissolve
            show NozomiHypno sleep
            "Her voice comes out soft, barely above a whisper. Perfect." with dissolve
            ks "Now, Nozomi, you will find that while in we are alone this house you cannot raise your voice any louder than how you just spoke."
            ks "If you attempt to do so, you will find it physically impossible. Do you understand?"
            ncg sleeptalk "{size=16}I understand...{/size}" with dissolve
            show NozomiHypno sleep
            "I have to lean in a little closer to make sure that she answered me in the affirmative." with dissolve
            ks "Very good, Nozomi. Now I want to remind you again; everything I have just told you, about obeying my commands, being unable to raise your voice..."
            ks "They are ONLY true for you while we are alone and in this house. If either of those conditions are false, you will not be bound by these rules in any way."
            ks "Is that clear, Nozomi?"
            ncg sleeptalk "{size=16}Yes...{/size}" with dissolve
            show NozomiHypno sleep
            ks "Excellent. Now, it's time for you to wake up. I will count to three and you will awaken happy and refreshed once more." with dissolve
            ks "One... beginning to stir."
            stop music fadeout 10.0
            ks "Two... fully accepting of everything you have been told."
            ks "And... three."
            ncg sleepy "{size=16}Mmm...{/size}" with dissolve
            "I chuckle as I get to see her waking expression once again."
            ks "Wide awake, Nozomi."
            play music Eons fadein 20.0
            ncg standing confused "{size=16}Ah, y-yes I'm awake.{/size}" with vpunch
            ks "So you are. And quiet as a mouse. How are you feeling?"
            ncg "{size=16}A little nervous... was it really okay to do this?{/size}"
            ks "It's what you wanted isn't it?"
            ncg sad "{size=16}Yes... yes, it was.{/size}" with dissolve
            ks "So, stop worrying about it." with dissolve
            "I then add with a smirk:"
            ks smirk "That was an order, by the way. Stop worrying."
            show NozomiHypno smile
            "And just like that she responds with an earnest smile." with dissolve
            ncg "{size=16}Okay, Kyou.{/size}"
            ks smile "That's better. But you will call me \"Sir\" from now on."
            ncg "{size=16}Yes, Sir.{/size}"
            ks "Man, you really are loving this aren't you."
            ncg "{size=16}Y-yes, Sir. Ehehe~{/size}" with dissolve
            "Even her laughter is muted. It's adorable!"
            ks "Are you even trying to resist my commands, Nozomi?"
            ncg neutral "{size=16}I can't, Sir. I literally can't resist a thing you're doing to me and I do still wonder about that.{/size}" with dissolve
            ks "And does that worry you?"
            ncg smile "{size=16}No, Sir. You told me to stop worrying, so I'm not worried. But I'm still thinking about how impossible it is to resist.{/size}" with dissolve
            "That... does sound like a thing she should worry about, though?"
            "Through all of this she tells me every time she can't resist any of the suggestions I give her, but I never really thought about it too much."
            "I figured she was overstating it because of how into this hypnosis-based power play she is."
            "But what if she really can't resist anything? Not even if she absolutely NEEDED to?"
            "She's not worried about my power over her now because I specifically told her to stop worrying."
            "What if I told her these suggestions I gave her for the house applied everywhere? Could she resist that?"
            "... Could she resist if I were to suggest we're lovers?"
            ncg "{size=16}Is everything okay, Sir? You've gone quiet.{/size}"
            "I need to do something about this..."
            menu:
                "I need to ensure her safety":
                    "I simply smile at her and reply:"
                    $hypno3 = hypno3.capitalize()
                    ks "[hypno3]."
                    show NozomiHypno drooping sleep
                    stop music fadeout 2.0
                    "And as expected, she drifts back into her entranced sleep." with dissolve
                    play music Flow fadein 5.0
                    ks "I've just been thinking, Nozomi. We need to give you something to protect yourself, in case you sincerely think I'm going too far."
                    ks "So I need you to understand that deep down, in spite of every suggestion I make, every truth I have you accept..."
                    ks "Your true thoughts, untouched by any of my suggestions, will ALWAYS be there at the back of your mind."
                    ks "If at any time your true thoughts object to my control you will say the words \"set me free\"."
                    ks "The moment you say those words aloud you will find every single suggestion I gave you will disappear, no longer holding any sway over you."
                    ks "Do you understand, Nozomi?"
                    ncg "{size=16}Mhm...{/size}"
                    ks "Very good. It's very important that you keep this knowledge at the back of your mind at all times and be able to use it if you need to."
                    ks "And now wide awake on three, Nozomi. Feeling nice and refreshed..."
                    stop music fadeout 5.0
                    ks "One, two, three."
                    ncg sleepy "{size=16}Mmm... thank you, Sir.{/size}" with dissolve
                    ks "Don't mention it. We should've done something like that from the start."
                    show NozomiHypno standing smile
                    play music Eons fadein 5.0
                    "Nozomi's smile is full and genuine. She must have also realized the danger she was in, so this must come as a huge relief to her." with dissolve
                    "And with her safety ensured, I guess it's okay to go back to having some fun with her."
                    "I almost don't dare say it, but..."
                    ks "Still, I'm looking at you now and I'm wondering..."
                    ks "Do you really need all those clothes?"
                    "There, I said it."
                    ncg confused "{size=16}Huh?{/size}" with dissolve
                    "I'm trying to ignore the heat rising in me as I continue."
                    "I mean, I need to be cool about this."
                    ks "Anyone would think we're equals. But that's not right, is it?"
                    ncg sad "{size=16}A-ah, well... t-that is...{/size}" with dissolve
                    k "Answer the question, Nozomi."
                    ncg "{size=16}No... it's not.{/size}" with dissolve
                    k "Exactly..."
                    ks "S-strip down to your underwear, Nozomi."
                    # $n = Character("[nozomi_name]", image = "Nozomi", who_color = "#93624B")
                    scene bg k room eve
                    show Nozomi side sad_closed blush
                    with dissolve
                    "She makes a face, and I might be making a face back at her..."
                    play sound clothes
                    "But she doesn't hesitate to get off the couch and start disrobing in front of me." with dissolve
                    "I hope that means she really is comfortable with this."
                    show Nozomi underwear
                    "But as I watch her finish undressing, standing in front of me in nothing more than her undergarments, I don't get the impression she's really that upset." with dissolve
                    show Nozomi front sigh
                    "Looking at her trembling form from head to toe, she might even be as \"excited\" as I am right now..." with dissolve
                    "Could I push her to go nude, then?"
                    "... I'm just going to leave that question unanswered."
                    ks smile blush "Th- there. That's more reflective of your status in this house, don't you think, Nozomi?"
                    n "{size=16}... Y-yes, Sir.{/size}"
                    "Watching her reaction is fun and hot as hell to me but... now what?"
                "I need to test my theory":
                    $hypno3 = hypno3.capitalize(); kface = "neutral"
                    ks "I was thinking about what you just said."
                    ncg confused "{size=16}About how I can't resist, Sir?{/size}" with dissolve
                    ks "That's right. Would you mind if I tested the limits of that?"
                    ncg "{size=16}I... would mind, Sir, yes. I think we-{w=0.8}{nw}{/size}"
                    ks "Actually, you don't mind at all. Because I'm telling you not to mind. Are we clear, Nozomi?"
                    show NozomiHypno neutral
                    "Any trace of concern on her face seems to vanish as she replies quietly." with dissolve
                    ncg "{size=16}We're clear, Sir. I don't mind at all.{/size}"
                    "Alright then, Nozomi. Let's find out just how deep this goes."
                    ks "Now I want you to get up and strip, Nozomi. Take it all off."
                    # $n = Character("[nozomi_name]", image = "Nozomi", who_color = "#93624B")
                    scene bg k room eve
                    show Nozomi front neutral
                    with dissolve
                    play sound clothes
                    "I've barely finished speaking before she rises from the couch and moves her hands to tug at her blazer."
                    "And she certainly doesn't seem to mind as I watch her peel off the rest of her clothing..."
                    show Nozomi underwear
                    "Taking off one piece after another without missing a beat." with dissolve
                    "It really does seem like she can't stop herself."
                    "Yet I could stop her with just a few words..."
                    menu:
                        "Stop her":
                            ks frown "Nozomi, stop what you're doing."
                            "She freezes in place, having just started to unfasten her bra."
                            "I mean, what more do I need to prove? She's going to literally do and think anything I tell her at this point."
                            "I know back when I started learning about hypnosis I'd thought about such a fantasy scenario like this and how great it'd be to have someone so totally under my power."
                            "But as I look at her now, so helpless to my words, do I think I could ever be comfortable knowing what I've done to her?"
                            "Of course not. I care about Nozomi, don't I? And after she opened up to me about herself, how she trusted me..."
                            "I have to honor that trust."
                            $hypno3 = hypno3.capitalize()
                            ks "[hypno3]."
                            show Nozomi sleep noblush
                            stop music fadeout 2.0
                            "As expected, she drifts back into her entranced sleep." with dissolve
                            play music Flow fadein 5.0
                            ks "I've just been thinking, Nozomi. We need to give you something to protect yourself, in case you sincerely think I'm going too far."
                            ks "So I need you to understand that deep down, in spite of every suggestion I make, every truth I have you accept..."
                            ks "Your true thoughts, untouched by any of my suggestions, will ALWAYS be there at the back of your mind."
                            ks "If at any time your true thoughts object to my control you will say the words \"set me free\"."
                            ks "The moment you say those words aloud you will find every single suggestion I gave you will disappear, no longer holding any sway over you."
                            ks "Do you understand, Nozomi?"
                            n "{size=16}Mhm...{/size}"
                            ks "Very good. It's very important that you keep this knowledge at the back of your mind at all times and be able to use it if you need to."
                            ks "And now wide awake on three, Nozomi. Feeling nice and refreshed..."
                            stop music fadeout 5.0
                            ks "One, two, three."
                            n drowsy "{size=16}Mmm... thank you, Sir.{/size}" with dissolve
                            ks "Don't mention it. We should've done something like that from the start."
                            show Nozomi neutral
                            play music Eons fadein 5.0
                            "Nozomi expression is neutral, as if she didn't appreciate what was just at stake here." with dissolve
                            "But I know that's down to me simply telling her not to mind what I was doing. I should probably roll that command back as well."
                            ks "Nozomi, you are able to say and express how you really feel again. Is that clear?"
                            show Nozomi sigh
                            "Nozomi lets out a little sigh." with dissolve
                            n "{size=16}Yes, Sir. And I have to admit that got a little scary, now that I think about what just happened.{/size}"
                            ks "Yeah... Are you feeling any better now, though?"
                            show Nozomi smile
                            "{size=16}Yes, Sir. Knowing I can resist if I need to is a very reassuring to me.{/size}" with dissolve
                            "I smile, a little relieved. And with her safety ensured, I guess it's okay to go back to having some fun with her."
                        "Keep watching":
                            show Nozomi nude noglasses
                            with dissolve
                            stop music fadeout 5.0
                            "But why would I want to?"
                            "... I mean, it's not like she minds, right?"
                            "Nor will she mind me taking the time to take in every inch of her exposed beauty."
                            "She's... w-well, nothing will ever match up to my imagination, I guess. But still... she's pretty."
                            ks "H-How do you feel, Nozomi?"
                            play music Sorrow fadein 10.0
                            n "{size=16}I'm fine, Sir.{/size}"
                            ks frown "You're not, uh... you're not worried about being naked in front of me?"
                            n "{size=16}No, Sir.{/size}"
                            "Ugh, seeing her like this is doing things to me that I can't quite control..."
                            ks frown blush "And, er... you're not worried about the tent I'm pitching right now?"
                            n "{size=16}No, Sir. I'm not worried at all.{/size}"
                            "She didn't even look at what I was referring to as she whispered her reply instantly."
                            "Mindlessly."
                            "I'm... not sure how I feel about this."
                            menu:
                                # "Stop this":
                                #     ks "Put your clothes back on, Nozomi."
                                #
                                "Test her further":
                                    "But curiosity overwhelms me. I still want to see if there really is no limit to what I could make her do in this state."
                                    "I wonder..."
                                    ks frown noblush "... Stop breathing, Nozomi."
                                    n "..."
                                    "This is getting really fascinating."
                                    "She'll obey that, I'm sure. But will her self-preservation instinct kick in at some point?"
                                    n "..."
                                    "I go over to her and put a finger under her nose."
                                    "Nothing."
                                    n "..."
                                    ks "Aren't you going to breathe, Nozomi?"
                                    n entranced_neutral "{size=14}No, Sir...{/size}" with dissolve
                                    ks "And why not?"
                                    n "{size=12}Because you told me not to, Sir.{/size}"
                                    "It must've taken what little breath she had left in her lungs to answer me, but she remains calm as ever."
                                    "She looks completely unconcerned that she's suffocating herself."
                                    "How long can someone hold their {nw}"
                                    show Nozomi sleepy:
                                        linear 0.75 rotate 90 yanchor 0.2 xanchor 0.0
                                    extend "breath for anyway?" with vpunch
                                    stop music
                                    "..."
                                    ks surprised "Nozomi?"
                                    n "..."
                                    "Fuck."
                                    ks "Nozomi, breathe. I command you to breathe!"
                                    n "..."
                                    "FUCK!"
                                    ks angry "Nozomi, I need you to breathe!{w=0.8}{nw}"
                                    extend " COME ON!" with vpunch
                                    "As I shake her lifeless-looking body, I catch sight of her chest rising slightly and- oh, thank fuck she's breathing again."
                                    "At least she can't obey my commands while she's unconscious..."
                                    "But damn, that gave me a fright. Why'd I have to push her like that?"
                                    "... And what's going to happen when she comes to? When I have to let her out of here?"
                                    "She's going to remember how I nearly fucking killed her."
                                    "What... what do I do?"
                                    menu:
                                        "I can't let her remember any of this":
                                            hide Nozomi
                                            show Nozomi front nude sleepy noglasses at center:
                                                ypos 1.8 #rotate 0 yanchor 0.2 xanchor 0.0
                                                linear 1.5 ypos 1.2
                                            n "{size=16}Uhh...{/size}"
                                            ks frown "Nozomi, listen to me; you need to breathe now."
                                            "She draws a long shuddered breath, as if realizing her need for air for the first time."
                                            ks "That's good, Nozomi. Breathe normally now."
                                            "I give her a few moments to get her breath back while I decide that what I'm about to do is for the best."
                                            $hypno3 = hypno3.capitalize()
                                            ks "Alright now, Nozomi. [hypno3]."
                                            show Nozomi sleep
                                            play music Flow fadein 5.0
                                            "Even after all this she still can't shake her conditioning to go under, not even the slightest bit." with dissolve
                                            ks "Going deeper... back into a deep relaxing trance."
                                            ks "Now, Nozomi, I want you to accept some that some of the facts of this evening are different to how you currently remember them."
                                            ks "You remember that I told you to hold your breath until you passed out unconscious, but in fact it never occurred."
                                            ks "And as you accept this fact, you will find you can no longer remember that such a thing occurred."
                                            ks "After all, why would you remember something that didn't happen?"
                                            n "{size=16}I would not...{/size}"
                                            ks "No, Nozomi. You wouldn't. Now, you will wake on three."
                                            stop music fadeout 5.0
                                            ks "One... two... three."
                                            scene bg k room eve
                                            show Nozomi front uniform glasses concerned
                                            with blink
                                            n "{size=16}We still have a little time, Sir. Are you sure you want to stop so soon?{/size}"
                                            "After confirming her memory loss I had her change back into her clothes immediately and called an end to things today."
                                            ks sigh "Yeah... Sorry, Nozomi, I guess I'm not in the right frame of mind for it."
                                            n "{size=16}Oh. Did I make you uncomfortable?{/size}"
                                            ks concerned "Uhh, well..."
                                            n sleeptalk_concerned "{size=16}I was pushing for too much, wasn't I? I'm sorry I made this weird.{/size}" with dissolve
                                            ks "No, no it's fine I just..."
                                            show Nozomi concerned
                                            "I trail off. What am I supposed to tell her? That it's MY fault? Then she'll ask why..." with dissolve
                                            n "{size=16}Alright then, Kyou. See you tomorrow?{/size}"
                                            $kface = "neutral"
                                            ks neutral "Yeah. See you tomorrow."
                                            $ending = "awkward"
                                            jump Epilogue_Con_Kyou_Nozomi # Skip straight to the epilogue and play the "awkward" short ending
                                        # "I must never let her free":
                                        #     $nface = "sleepy"
                                        #     hide Nozomi
                                        #     show Nozomi at center:
                                        #         ypos 1.8 #rotate 0 yanchor 0.2 xanchor 0.0
                                        #         linear 1.5 ypos 1.2
                                        #     n "{size=16}Uhh...{/size}"
                                        #     $kface = "frown"
                                        #     ks "Breathe, Nozomi. You will breathe normally again."
                                        #     "She draws a long shuddered breath, as if realizing her need for air for the first time."
                                        "I have to take responsibility":
                                            hide Nozomi
                                            show Nozomi front nude noglasses sleepy at center:
                                                ypos 1.8 #rotate 0 yanchor 0.2 xanchor 0.0
                                                linear 1.5 ypos 1.2
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
                                            play music Flow fadein 5.0
                                            "But it's time I set her free." with dissolve
                                            ks "That's right, Nozomi. Back in this nice, deep relaxation. Ready to listen so carefully."
                                            ks "Because Nozomi, when you wake you will no longer be influenced by any of the suggestions I have given you over this past week."
                                            ks "You can feel each and every one of them leave your mind, leaving you free to think and act as you always have."
                                            ks "Do you understand, Nozomi?"
                                            ncg sleeptalk "I understand..." with dissolve
                                            show NozomiHypno sleep
                                            ks concerned "That's good, Nozomi. Now you're waking up in three..." with dissolve
                                            ks "One, beginning to rouse yourself..."
                                            show NozomiHypno sleepy
                                            stop music fadeout 5.0
                                            ks "Two, feeling your eyelids flicker open..." with dissolve
                                            ks "And three, wide awake."
                                            ncg standing drowsy "..." with dissolve
                                            ks "Okay so, Nozomi, given what just happened I thought I'd better-{w=0.8}{nw}"
                                            play music Sorrow fadein 2.0
                                            ncg "Kyou, you..."
                                            ncg confused "How could you do... do t-that..." with dissolve
                                            ks "Nozomi, please, I'm sorry-{w=0.8}{nw}"
                                            ncg "I have to get out of here."
                                            hide NozomiHypno
                                            play sound dooropen
                                            "And just like that, she bolts for the door." with dissolve
                                            play sound doorclose
                                            "... I don't try to stop her."
                                            $ending = "frightened"
                                            jump Epilogue_Con_Kyou_Nozomi
                                            #Jump straight to epilogue with broken Nozomi ending



            ks neutral blush "So, err..."
            "I've never done anything like this before."
            ks "On your knees, Nozomi."
            show Nozomi:
                linear 1.5 ypos 1.2
            "As she obediently drops down to the floor to sit on her heels, I reach down to pet her head."
            "The last thing I want to do is hurt her."
            "So maybe I should ask her what she wants me to make her do? Would that be defeating the purpose?"
            show Nozomi concerned:
                ypos 1.2
            "And now she's looking at me expectantly again." with dissolve
            "Well... if I assume she can now stop my influence over her at any time, maybe I shouldn't worry about this too much."
            ks smile "You know, I'm still thinking about the power I have over you. About all the things I could make you do."
            ks "And all you'd be able to do in return is smile and obey. Even if you knew it would risk your life. Even if my orders would strip you of your very humanity."
            ks "Doesn't that excite you, Nozomi?"
            n blush "{size=16}It.. it does, Sir. It thrills me to my core to know I'm powerless before you.{/size}" with dissolve

            ks "So then, Nozomi. With this ultimate power at my disposal I command you to..."
            menu:
                "Make me a cheese omelette.":
                    show Nozomi surprised:
                        linear 1.5 ypos 1.0
                    "Nozomi blinks in surprise as she registers what I said, but her body responds immediately as she rises back to her feet and starts padding towards the kitchen." with dissolve
                    show Nozomi:
                        xpos 0.65
                        ypos 1.0
                    show Nozomi:
                        linear 3.0 xpos 2.0
                    "I'm sure I heard a soft chuckle from her as she disappears from view, followed shortly after by the sound of the fridge door opening."
                    "Not wanting to miss the sight of an underwear-clad girl cooking for me, I decide to follow her."
                    scene bg k kitchen eve with dissolve
                    "Taking a seat at the dining table, I simply watch with a grin as she works, navigating around my kitchen with relative ease to get her task done."
                    show Nozomi front underwear concerned blush
                    "I can tell she's a little flustered at my staring, but she doesn't say anything as she prepares the food, sets it on a plate and serves it up to me at the table." with dissolve
                    n side sad "{size=16}H-Here you are, Sir.{/size}" with dissolve
                    "I take a look at the cheese omelette in front of me, then at her, still grinning."
                    ks smirk "I never said I wanted to eat it, Nozo. Besides, I'm not hungry."
                    n frown "{size=16}What? Geez, then why did you have me make it?{/size}" with dissolve
                    ks "Sit down and eat it yourself."
                    show Nozomi:
                        linear 1.0 ypos 1.1
                    pause 1.0
                    n front pout "{size=16}But I'm not hungry either...{/size}" with dissolve
                    show Nozomi:
                        ypos 1.1
                    "She says, as she tears a piece off and pops it into her mouth."
                    n "{size=16}Jerk...{/size}"
                    ks smile "Tell me how you're really feeling, Nozomi."
                    "She takes a moment to swallow her food before replying."
                    n pout_left "{size=16}Really good. I know it's just a simple thing, but even making me do this and knowing I can't stop myself is so euphoric you wouldn't believe.{/size}" with dissolve
                    "She stops to take another bite of the omelette; her compulsion to obey my latest order conflicting with the previous."
                    ks neutral "Yet you still look a bit worried to me."
                    n sleeptalk "{size=16}I'm not worried, Sir. I'm just embarrassed to admit this to you. And to myself.{/size}" with dissolve
                    ks smile blush "Nozomi, there's no reason to feel embarrassed about feeling this way. You like what you like."
                    show Nozomi concerned
                    ks "Also, no one else needs to know if you don't want to say anything. We had a deal." with dissolve
                    ks "So don't feel ashamed about who you are. You're safe here, with someone who wants you to be happy."
                    ks "Let yourself enjoy this."
                    show Nozomi smile
                    "Nozomi gives me a smile from across the table and nods, still half-chewing as she responds in her cute whispered voice." with dissolve
                    n "{size=16}Thank you, Sir. That does actually make me feel better.{/size}"
                    "I smile back at her as we share a moment of shared bliss."
                    "And then with a grin, I'm the one to break the silence for a change."
                    ks smirk "Now be a good girl and finish your omelette, and wash everything up when you're done."
                    show Nozomi teasing
                    "She pokes her tongue out at me, then takes another bite of her food." with dissolve
                    scene bg k room eve with blink
                    show Nozomi front smile with dissolve
                    "Soon after she was done in the kitchen I had her get dressed and ready to leave."
                    "Not that I wanted to, but dad's going to be home soon, and I don't think either of us want to explain this to him of all people."
                    ks smile "You got everything?"
                    n "{size=16}Yes, Sir. Are we doing this again tomorrow?{/size}"
                    "I respond with a wink and a knowing smirk."
                    ks smirk "Oh, you WILL be coming back here tomorrow. Do I make myself clear?"
                    show Nozomi chuckle blush
                    "She replies with a muted giggle." with dissolve
                    n "{size=16}Yes, Sir. I must obey~{/size}"
                    stop music fadeout 5.0
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

        else:
            scene bg classroom eve with blink
            play music Measured fadein 5.0
            if hypno4 == "arousal":
                "The rest of the day was awkward. Nozomi's little incident was whispered about during lessons, and it was all she could do to pretend not to notice."
            elif hypno4 == "tickle":
                "The rest of the day was awkward. Nozomi's giggling fit was whispered about during lessons, and it was all she could do to pretend not to notice."
            play sound schoolbell
            scene bg entrance
            show Nozomi front
            show Sayori uniform_folded at center, flip:
                xpos 0.25
            show Hiroko at center:
                xpos 0.75
            with fade
            "As the day draws to a close, we file out of the classroom and are quickly caught up by Nozomi's friends from before."
            s "I have been thinking about what happened earlier."
            h uniform_arm frown_side "Yeah, me too. It's fuckin' nuts." with dissolve
            n uniform_folded frown "Well, to be honest I'm starting to get annoyed about how much of a fuss you two are making." with dissolve
            s concerned "Why would we not make a fuss? I don't understand what you two are doing but it looks dangerous." with dissolve
            s "We're worried about you."
            n irritated "Don't be. Everything's fine. BETTER than fine, in fact." with dissolve
            h uniform_armup angry_side "A-Are you {nw}" with dissolve
            extend "SERIOUS?! You looked like you were gonna die on that roof, you idiot!" with vpunch
            s frown_right "... Want to weigh in on this, Kyou? I see you skulking back there." with dissolve
            ks confused "H-hey now, I haven't done anything with Nozomi that she didn't want!"
            h frown "What did you even do to her? That's what I don't get!" with dissolve
            n frown "Like I said, he hypnotized me into feeling tickled when I hear a certain word in school." with dissolve
            s concerned "Are you even hearing yourself, Nozomi? What you said sounds absolutely insane." with dissolve
            ks frown "Well, it's the truth. I DID hypnotize her, and it was all totally consensual."
            n irritated "Honestly. You two are just trying to kinkshame me now." with dissolve
            show Sayori uniform shocked
            h uniform surprised_side "Wha?!" with dissolve
            s "Nozomi, what are you saying? We just want to understand what's been happening."
            n angry "And I already TOLD you two. You just don't care to listen if you're still kicking up a fuss about it." with dissolve
            n "I've had enough of this. Come on, Kyou."
            show Nozomi:
                linear 1.0 xpos 1.5
            pause 1.0
            show Hiroko at center, flip:
                xpos 0.75
            "And with that she storms out of the building, leaving me to run past the stunned onlookers and after her." with dissolve
            scene bg street1 eve
            show Nozomi side frown
            with blink
            n "Seriously, what is wrong with those two?"
            "I quickly caught up with the still-fuming Nozomi."
            ks confused "U-uh, well I guess it IS pretty hard for people to understand?"
            n "Why, Kyou? I'm just a regular girl with a hypnosis fetish, what's the big deal?"
            n front irritated uniform_folded "I mean, sure, it's not for everybody, but I don't expect people to freak out over such a normal thing." with dissolve
            ks "Y... yeah."
            n "Well... screw them."
            ks surprised "You're ditching them?" with dissolve
            n "Why not? If they can't deal with this then I can't deal with them. I'm not giving up what we started."
            n determined uniform "I won't abandon who I am." with dissolve
            "Wow, she really has taken everything I said to her in trance so completely to heart."
            "And who am I to argue? This is perfect!"
            ks smile "You won't have to, Nozomi. Let's go back to mine; we'll do some more work on that beautiful mind of yours."
            show Nozomi happy
            "Nozomi giggles at that, and takes my hand as we walk." with dissolve
            $ending = "liar"
            jump Epilogue_NonCon_Kyou
            # n "Yes~ {font=DejaVuSans.ttf}♥{/font} Kyou, take my mind!"
            # ks "We're going to have so much fun togeth-{w=0.8}{nw}"
            # n surprised "My brain will be like an open book to you, Kyou! Write whatever you want in there, or rip out every page. I won't mind!" with dissolve
            # ks confused "Err.. w-well-{w=0.7}{nw}"
            # n concerned "You're hesitating. Is something wrong?" with dissolve
            # ks chuckle "What you're saying... it sounds a little extreme, don't you think?"
            # show Nozomi surprised
            # "She blinks back at me in confusion." with dissolve
            # n "No, what are YOU saying? You're the one who made me realize how much I love being hypnotized and having my mind shaped to your design."
            # "As Nozomi's voice begins to crack, I start to wonder..."
            # n concerned "Don't tell me you don't understand me either, Kyou. You have to understand!" with dissolve
            # "Is this really what she wants? To have her mind completely ripped apart like a dog's chew toy?"
            # n cry "I NEED you to understand!" with dissolve
            # "Or did I make her want this?"
            # n "Kyou. Please tell me you understand..."
            # "Shit. She can't have wanted it like this. I did this to her..."
            # ks surprised "I-I think I do, Nozo. Just give me a moment."
            # "But that's impossible?! You can't just change people, can you?"

            scene bg blackscreen with fade
            jump Credits
    elif hypno2 == "zombie":
        play music Downtown
        "Nozomi and I didn't contact each other overnight, and I'm anxious to see her again."
        "God, I hope she made it home safe."
        scene bg ext school day with blink
        "As I make it to the school entrance, I'm relieved to see Nozomi standing by the gates."
        "I approach, and I'm about to greet her when I realize she's talking to someone..."
        scene NozomiHirokoHug nozomi_worried bruise1 hiroko_worried with blink
        h "No fuckin' way!"
        n "Yeah..."
        "Nozomi raises a hand to yawn into the back of it, then continues as I strain myself to hear her."
        show NozomiHirokoHug nozomi_irritated
        n sad_side "It's embarrassing, but I somehow tripped over my own feet and down the stairs I went." with dissolve
        show NozomiHirokoHug hiroko_neutral
        h "That's some serious bruise you got, sis. Don't that hurt?" with dissolve
        show NozomiHirokoHug nozomi_annoyed
        n sad_closed "*sigh* Yes, a little bit. I wasn't too badly hurt, but I could've done without having to get my glasses fixed on top of everything else." with dissolve
        n "I don't have a spare pair, or contacts, and I barely got a wink of sleep so class is going to be SO much fun today."
        show NozomiHirokoHug hiroko_worried
        h sleeptalk_concerned uniform_armup "Nozooo..." with dissolve
        show NozomiHirokoHug nozomi_worried
        n "What?" with dissolve
        show NozomiHirokoHug girls2 nozomi_uncomfortable bruise2 hiroko_cry
        h "C'MERE!" with dissolve
        show NozomiHirokoHug nozomi_blush2
        n "H-Hiroko! What are you doing?!" with dissolve
        h "YOU'RE GONNA HAVE A GREAT DAY! Y'HEAR ME, NOZO?" with shake
        n "Y-yes, we heard you alright."
        show NozomiHirokoHug nozomi_shy
        n smile_side "But gosh... I don't think you've hugged me since we were in junior high." with dissolve
        show NozomiHirokoHug girls1 nozomi_smile bruise1 nozomi_blush1 hiroko_grin
        h happy_closed "Oh, yeah! This is like when you cut your knee while we were on that field trip." with dissolve
        show NozomiHirokoHug nozomi_happy
        n "Eheh... yeah." with dissolve
        show NozomiHirokoHug hiroko_laugh
        h uniform_arm happy "Kyahaha, {w=0.2}you used to be {nw}" with dissolve
        hide NozomiHirokoHug
        show NozomiHirokoHug girls1 nozomi_surprised bruise1 hiroko_laugh
        extend "SUCH a clutz back then!" with vpunch
        show NozomiHirokoHug nozomi_annoyed hiroko_smile
        n "Once again Hiroko, we all heard you loud and clear." with dissolve
        show NozomiHirokoHug hiroko_laugh hiroko_blush
        h "Kyahaha, sorry~ Was thinking 'bout how we used to hug it out like this all the time!" with dissolve
        show NozomiHirokoHug hiroko_neutral
        h "'Til high school happened, anyway..." with dissolve
        show NozomiHirokoHug nozomi_irritated
        n annoyed_left "Yes, because we're not little kids anymore." with dissolve
        hide NozomiHirokoHug
        show NozomiHirokoHug girls1 nozomi_smile bruise1 hiroko_smile
        n "But... thanks, Hiroko. For caring." with dissolve
        show NozomiHirokoHug nozomi_squint
        "As Nozomi disentangles herself from Hiroko's embrace, she squints towards me, seeming to notice me standing there for the first time before quickly averting her gaze." with dissolve
        show NozomiHirokoHug nozomi_worried
        $persistent.nozomi_hiroko_hug_unlock = True
        n sad_side "Anyway, let's head on in." with dissolve
        scene bg classroom day with blink
        "As I follow behind them, I send a text to Nozomi asking how she's doing."
        "I know we can't let this fester between us for too long. I hope she realizes that as well."
        play sound schoolbell
        scene bg entrance eve with blink
        stop music fadeout 5.0
        "But I don't get anything back. Not a text, not even an acknowledging stare all day."
        "I might as well have not existed to her."
        scene bg k bedroom eve with blink
        "As I get back home and drop my schoolbag down by my bed I wonder if I should text her again."
        play sound doorbell
        "Huh, that was the door bell just now. Could that be her?"
        scene bg k entrance eve
        show Nozomi front concerned noglasses bruise
        with blink
        n "Hey."
        ks concerned "Hey..."
        "Nozomi drops her shoes by the door and sighs."
        show Nozomi front2 sleeptalk
        "... Then turns and hugs me?" with dissolve
        play music Eons
        n "Sorry I didn't respond earlier. I... I kinda got wrapped up in my thoughts today."
        $light_y =0.28
        "I'm too stunned to respond as she holds me tight... wow, what a feeling."
        ks confused "Oh... y-yeah, sure."
        "To have her so close to me, her chest against mine as a single hand touches my back to keep me close."
        "Oh. I should put my arms around her too, right? Right..."
        show Nozomi concerned
        "But just as I'm about to, Nozomi lets me go before walking over to the living room couch to take a seat." with dissolve
        scene cg k room eve
        show NozomiHypno standing sad noglasses bruise
        with blink
        "... It was nice while it lasted."
        ncg neutral "I can't stay for very long, I'm afraid." with dissolve
        ks neutral "Oh... Y-yeah, of course."
        ncg "But I was thinking over and over about what happened. I've barely been able to put it out of my head."
        ks neutral "Yeah... How are you holding up, anyway?"
        ncg drooping sleeptalk "Oh, you know. Not great." with dissolve
        show NozomiHypno standing confused
        "She sighs as she turns her head to look towards the television, staring wistfully into the screen with unfocused eyes." with dissolve
        ncg "Just... one moment I was falling asleep on your couch. The next I was waking up outside your house with cuts and bruises all over."
        ncg neutral "It wasn't until I told my parents that I fell over on the way back from school that it really started to sink in." with dissolve
        ncg sad "What happened could've been so much worse, and..." with dissolve
        ncg stern "And I'm sorry, but I have to think it's all your fault!" with dissolve
        "My chest tightens as her words hit unpleasantly. And I'm finding it hard to concentrate when she looks at me like that."
        ks surprised "W-what, what do you mean?"
        "Nozomi impatiently holds up her cheap-looking smartphone and waggles it at me."
        ncg annoyed "Kyou, I went over what you told me while I was in trance yesterday." with dissolve
        ncg "You said I was supposed to \"become exactly what I believe a zombie to be\" when you told me the trigger phrase."
        ncg folded stern_closed "That's so open-ended!" with dissolve
        ks frown "Y-yeah, but..."
        show NozomiHypno stern
        "Maybe I could've been more specific, but I had my reasons for phrasing it that way." with dissolve
        ks "You weren't sure about the whole thing so I thought, well... you should decide how you want to be a zombie in front of me."
        ncg angry "But that's not what you said! You told me to be a zombie just like I think they are!" with dissolve
        ncg "And zombies are scary! They... they're creatures of the night that shamble around and eat the flesh off your bones while ranting about brains!"
        ncg stern_closed "They're mindless, e-evil monsters and when you said the magic word, that's what I was supposed to be!" with dissolve
        ks sigh "Yeah... I really didn't think you'd take it that far, after you were so nervous about it before."
        ncg stern "But I did. And you didn't stop me!" with dissolve
        ncg angry "You... you seriously let me wander around with that dangerous stuff in my head!" with dissolve
        ks surprised "Nozomi, I TRIED to stop you and you wouldn't listen!"
        ks "And hypnotized or not, you didn't have to do anything you didn't want to! You... know that, right?"
        show NozomiHypno stern_closed
        "Nozomi snorts." with dissolve
        ncg "When someone is under the influence of hypnosis, their hypnotist has a responsibility to keep them safe."
        ncg "I was in your care, under a post-hypnotic suggestion that you planted and... and it really could've been so much worse."
        ncg standing angry "YOU know that, right?" with dissolve
        ks neutral "Nozomi..."
        ncg sad "Gosh, if I had fallen differently down your stairs I could've been..." with dissolve
        "Ugh... yeah, I've tried not to think about that time I was leading Nozomi out of the house."
        show NozomiHypno neutral
        "I gotta admit, with the way she was behaving she was lucky to get out of there with just a few bruises and a broken pair of glasses." with dissolve
        "Even if she doesn't remember it happening, or maybe BECAUSE she doesn't remember... I guess she can't help but imagine what could've happened."
        "But that still raises the question:"
        ks sigh "How did this even happen?"
        ks "Even if my hypnotic suggestion to you was so dangerous, there's so many things that should've snapped you back to reality."
        ks "My kicking you, the hit you took when I opened my bedroom door on you, the falling down the stairs..."
        ks "All of those things should've made maintaining a state of post-hypnotic trance impossible!"
        show NozomiHypno folded stern
        "Nozomi holds her arms around her stomach as she frowns in thought." with dissolve
        ncg "{cps=20}You're right. That SHOULD be impossible, but... {/cps}{w=1.0}{nw}"
        $ renpy.transition(dissolve, layer="master")
        extend angry "wait, you KICKED ME?!"
        ks surprised "A-ah, you had me on the floor and you were trying to bite my face! And I shouted at you to wake up and you didn't!"
        ks "I-I had to do SOMETHING!"
        ncg surprised "I... what?" with dissolve
        show NozomiHypno drooping sleeptalk
        $ renpy.transition(longdissolve, layer="master")
        "Nozomi sighs as she drops her gaze despondently."
        ncg "The more I find out about what happened last night, the more scared I get."
        ncg standing confused "But the fact is whatever you did, it convinced me to hold myself to your ridiculous hypnotic suggestions no matter what happened." with dissolve
        ncg "It's crazy. I mean, out of all the hypnosis videos I've seen, or when Satoshi hypnotized me, nothing has come close to what I've experienced with you." id Day4_Con_Kyou_Nozomi_8f25a9cc
        ncg neutral "What's so wildly different about how you hypnotize me?" with dissolve
        ncg "The only answer I have..."
        show penlight at right with moveinright:
            ypos 0.346
        show NozomiHypno stern
        "She frowns as she pulls out a penlight that was hidden inside the sleeve of her blazer." with dissolve
        ncg "Is this!"
        "Wait a sec."
        ks surprised "How the fuck did you get that?!"
        ncg folded annoyed "Kyou, you keep your penlight in your right pants pocket. I've seen you with it a couple of times now; it wasn't hard." with dissolve
        ncg "Anyway, I've lied to everyone I care about since last night. I may as well be a thief, too."
        hide penlight with moveoutright
        "I groan as the realization of how she got hold of it hits me, then I feel anxiety well inside me as that realization is immediately followed up with ANOTHER realization."
        # if accepted_terms == False:
        #     ks frown "Y-You need to give that back."
        # else:
        ks frown "Nozomi... don't do anything rash, okay?"
        ncg neutral "..." with dissolve
        "Did she just raise an eyebrow at me?"
        ncg "I wonder what \"rash\" thing you're expecting me to do with this, Kyou?"
        ks "W... w-well..."
        ncg stern "As rash as shining this attention-grabbing light over YOUR eyes?" with dissolve
        "There's a soft click as Nozomi presses her thumb into the penlight, illuminating the cushion beside her."
        ncg smile "Maybe say a few words while I'm doing it?" with dissolve
        #This would be a great time for Kyou to reflexively trigger Nozomi's zombie state if he make the choice to not respect her earlier.
        ks angry "C-come on, that's enough! Give it back."
        ncg stern "Why, Kyou? Does me having it make you nervous? Nervous enough that you'd wrestle me for it?" with dissolve
        "Shit. Was I really about to..."
        # ncg "Nervous enough to say the thing that caused this mess in the first place?"
        ks frown "Ugh..."
        #Kyou calms down as Nozomi calls him out, and she tells Kyou that his reaction to her having the penlight makes it clear he believes it has power and is dangerous
        ncg "It's not... really that big a deal if I hold onto it, is it?"
        ks "But it's MY penlight. I worked hard on that thing."
        show NozomiHypno annoyed
        "Nozomi sighs at me in irritation." with dissolve
        ncg "I just want to borrow it for a while, you big baby."
        show NozomiHypno stern
        "And now it's my turn to sigh. First she steals my penlight, now she demands I let her leave with it?" with dissolve
        "This is making me very uneasy."
        ks confused "What would you even do with it anyway? Do you even know how to work that thing?"
        ncg annoyed "Well, do you?" with dissolve
        "I'm about to answer, but all I manage is a low, frustrated growl."
        "She's gonna be holding last night against me for a while, huh."
        ncg stern "Yeah. So, either you let me take this or we're through doing hypnosis together." with dissolve
        ks frown "Oh come on, you can't be serious."
        show penlight at right with moveinright:
            ypos 0.346
        "Nozomi just holds my penlight up in her hand in front of me with a glare."
        ncg "What's it going to be, Kyou?"
        "... I don't like this one bit. Letting her take my penlight home with her seems like a terrible idea, but I'm obviously not going to convince her otherwise."
        "And if I lose Nozomi over this there's no way I'll be able to live with myself."
        hide penlight at right with moveoutright
        ks sigh "Alright... take it."
        $persistent.k_room_nozomi_1_2_unlock = True
        scene bg k room eve
        show Nozomi uniform front noglasses sigh bruise at center:
            ypos 1.2
            linear 2.5 ypos 1.0
        with blink
        "Satisfied, Nozomi slides my penlight into her bag before rising up from the couch."
        show Nozomi:
            ypos 1.0
        n neutral "I'll talk to you later, Kyou." with dissolve
        ks neutral "Yeah."


        # ncg annoyed "Kyou, what do you take me for? I've just been explaining that I think this thing could be dangerous." with dissolve
        # ncg "No one should be doing anything with this until we know more about what it does."
        # ks "Really? All it does is help keep your focus on the pattern it emits so you'll fall into trance easier. That's all I designed it for."
        # ks "I wasn't even sure it'd do that until I used it on you."
        # ncg stern "Right, so I'm literally your only data point. How do you know it doesn't do more than that?" with dissolve
        # ncg "What if it actually managed to inhibit my hidden observer somehow? Because why else could this have happened to me?"
        # ks neutral "I... I don't know."
        # ncg angry "Not to mention your reaction just now. If you really thought it was so harmless, why does it matter so much what I do with it, huh?" with dissolve
        # "I sort of reacted out of instinct there, but I guess she has a point."
        # show NozomiHypno stern
        # ks sigh "I just thought that if I modified the light to make a pretty distraction it could help people focus in a hypnosis session." with dissolve
        # ks "It's supposed to help someone achieve a state of trance, there's no way it should've stopped your hidden observer, or whatever you want to call it."
        #
        #
        # "AUTHOR'S NOTE - Unaltered script continues from here on, so expect a lot of discrepencies until the next release."
        #Worth noting, Nozomi was very reluctant about the zombie trigger. How powerful is the penlight that she completely absorbed the suggestion anyway?
        # ks sigh "Okay, well... maybe you're right. I don't know how being hypnotized with the penlight stacks up with any other method." with dissolve
        # ks "What about you, though? What was it like when Satoshi hypnotized you?"
        # "Nozomi doesn't reply immediately, instead running her thumb over the penlight she's keeping gripped in one hand."
        # ncg standing neutral "It was different... I think." with dissolve
        # ncg "I don't remember clearly now, but I'm pretty sure I could've stopped going along with his suggestions if I really wanted to?"
        # "She shrugs."
        # ncg stern "Anyway, I think it's obvious what we should do next." with dissolve


        # "She doesn't answer immediately, and instead turns her attention to her phone. I'm about to ask what she's doing until I hear my own voice come out of her phone's speakers."
        # $t = Character("Nozomi's Phone")
        # t "{b}You recognise this light, Nozomi. So you know how natural it is to want to look into it.{/b}"
        # ncg stern_closed "Kyou, I went over what you said to me while I was hypnotized yesterday." with dissolve
        # ncg "And, um..."
        # show NozomiHypno folded stern
        # "Nozomi frowns as she presses her thumb on the screen again, silencing the audio for a moment." with dissolve
        # ncg "Something stood out..."
        # t "{b}So from now on, Nozomi, whenever we are alone in this house and I say \"[hypno3]\"...{/b}"
        # ncg stern_closed "Ahh!" with dissolve
        # "Nozomi winces as she reflexively pauses the video."
        #
        #
        # ncg neutral "Ah, right here." with dissolve
        # t "{b}You will find yourself compelled to become exactly what you believe a zombie to be.{/b}"
        # "Nozomi taps her thumb and the crappy-sounding speech on her phone falls silent once more."
        # ks sigh "Man, you ever thought about getting a decent phone? That thing sounds like it's had it."
        # ncg surprised "Wh-what? No..." with dissolve
        # show NozomiHypno stern
        # "Nozomi shakes her head and scoffs at me as she sets her cheapass phone down on her lap." with dissolve
        # ncg "Nevermind that, what do you think of this thing you said to me?"
        # ks neutral "O-oh, when I was explaining how your zombie trigger was supposed to work?"
        # ncg "Yeah..."
        # show NozomiHypno sad
        # "She sighs." with dissolve
        # ncg "I mean, that's the thing. You didn't really explain it, you just left it to my subconscious to figure out."
        # ncg neutral "\"You will find yourself compelled to become exactly what you believe a zombie to be.\"" with dissolve
        # ncg folded stern_closed "That's so open-ended!" with dissolve
        # ks frown "Y-yeah, but..."
        # show NozomiHypno stern
        # "I had my reasons for doing it that way." with dissolve
        # ks "You weren't sure about the whole thing so I thought, well... you should decide how you want to be a zombie in front of me."
        # ncg angry "But that's not what you said! You told me to be a zombie just like I think they are!" with dissolve
        # ncg "And zombies are scary! They... they're creatures of the night that shamble around and eat the flesh off your bones while ranting about brains!"
        # ncg stern_closed "They're mindless, e-evil monsters and when you said the magic word, that's what I was supposed to be!" with dissolve
        # ks sigh "Yeah... I really didn't think you'd take it that far, after you were so nervous about it before."
        # ncg angry "But I did. And you didn't stop me! You... you seriously let me wander around with that dangerous stuff in my head!" with dissolve
        # ks surprised "Nozomi, you didn't have to do any of it! You... know that, right?"
        # ncg "When someone is under the influence of hypnosis, their hypnotist has a responsibility to keep them safe."
        # ncg "I was in your care and... and it could've been so much worse. If I fell differently down your stairs I could've..."
        #
        #
        #
        #
        # ncg "Yeah... n-not great."
        # "She looks uncomfortably to the side, avoiding my gaze, and after a pause she carries on."


        # n sigh "I got home okay yesterday, and I somehow managed to convince my parents that I fell over on the way back from school." with dissolve
        # n pout_left "This morning I told my friends that I tripped down the stairs at home." with dissolve
        # ncg standing neutral "I somehow managed to convince my parents that I fell over on the way back from school yesterday, and my friends think I tripped down the stairs at home." with dissolve
        # ncg stern "So I've lied to the people I care about most just to keep what we have going under wraps, and I feel terrible about that." with dissolve
        # ks "You've never lied before?"
        # ncg stern_closed "I've lied about eating my little brother's pudding when we were kids. I've never lied about anything big before." with dissolve
        # ncg confused "Like... oh, I don't know... getting injured while visiting some strange guy's house." with dissolve
        # ks sigh "And I'm sorry for that."
        # ncg sad "I'm just terrified the truth's going to come out soon." with dissolve
        # ks frown "You don't really look all that injured to me?"
        # ncg neutral "I don't? It feels like everyone knows I'm limping as I walk, or that I'm wearing a little more makeup than usual."with dissolve
        # ncg stern_closed "And god, why did I use different stories for my friends and parents? I TOLD you I'm a terrible liar." with dissolve
        # show NozomiHypno neutral
        # "Nozomi sighs once more, then turns her gaze back to me." with dissolve
        # ncg "Well, anyway... two things came to mind while I was thinking things over."
        # "Nozomi then brings up her phone and starts tapping her thumb on the screen a few times."
        # ncg stern "Because..." with dissolve
        # "She falls silent as her eyes linger on her phone. I'm about to ask what she's looking at until I hear my own voice come out of her phone's speakers."
        # $t = Character("Nozomi's Phone")
        # t "{b}You recognise this light, Nozomi. So you know how natural it is to want to look into it.{/b}"
        # ncg stern_closed "Because... w-well first, I was listening to what you said to me while I was hypnotized." with dissolve
        # ncg "And, um..."
        # show NozomiHypno stern
        # "Nozomi frowns as she presses her thumb on the screen again, silencing the audio for a moment." with dissolve
        # ncg "Something stood out..."
        # t "{b}So from now on, Nozomi, whenever we are alone in this house and I say \"[hypno3]\"...{/b}"
        # ncg neutral "Ah, right here." with dissolve
        # t "{b}You will find yourself compelled to become exactly what you believe a zombie to be.{/b}"
        # "Nozomi taps her thumb and the crappy-sounding speech on her phone falls silent once more."
        # ks sigh "Man, you ever thought about getting a decent phone? That thing sounds like it's had it."
        # ncg surprised "Wh-what? No..." with dissolve
        # show NozomiHypno stern
        # "Nozomi shakes her head and scoffs at me as she sets her cheapass phone down on her lap." with dissolve
        # ncg "Nevermind that, what do you think of this thing you said to me?"
        # ks neutral "O-oh, when I was explaining how your zombie trigger was supposed to work?"
        # ncg "Yeah..."
        # show NozomiHypno sad
        # "She sighs." with dissolve
        # ncg "I mean, that's the thing. You didn't really explain it, you just left it to my subconscious to figure out."
        # ncg neutral "\"You will find yourself compelled to become exactly what you believe a zombie to be.\"" with dissolve
        # ncg folded stern_closed "That's so open-ended!" with dissolve
        # ks frown "Y-yeah, but..."
        # show NozomiHypno stern
        # "I had my reasons for doing it that way." with dissolve
        # ks "You weren't sure about the whole thing so I thought, well... you should decide how you want to be a zombie in front of me."
        # ncg angry "But that's not what you said! You told me to be a zombie just like I think they are!" with dissolve
        # ncg "And zombies are scary! They... they're creatures of the night that shamble around and eat the flesh off your bones while ranting about brains!"
        # ncg stern_closed "They're mindless, e-evil monsters and when you said the magic word, that's what I was supposed to be!" with dissolve
        # ks sigh "Yeah... I really didn't think you'd take it that far, after you were so nervous about it before."
        # ncg stern "But I did. And you didn't stop me!" with dissolve

        #Nozomi wants to take the penlight home with her and study it in her own time, maybe get to the bottom of how she's so susceptible to Kyou's hypnosis



        # ncg angry "So that's what I was, Kyou! You... y-you MADE me into that!" with dissolve
        # ks surprised "But..."
        #
        #
        # ncg "And do you know what's worse? You LEFT me like that!"
        # "Shit. Why do I suddenly feel like I'm being put on trial here?"
        # ks "The... w-wait, what are you saying?"
        # ncg "What am I saying? I'm saying you seriously let me wander around with that dangerous stuff in my head!"
        # ncg stern_closed "It didn't sink in until I got home and had to excuse myself to mom and dad, how much you let me down." with dissolve
        # ks "Let you down?"
        # "Nozomi takes a deep breath through her nose as she tries to compose herself."
        # ncg "You know that when someone is under the influence of hypnosis, their hypnotist has a responsibility to keep them safe, right?"
        # ncg angry "You were responsible for me, Kyou!" with dissolve
        # ncg "I was in your care and you... y-you let all those terrible things happen to me!"
        # ncg confused "And it could've been so much worse. If I fell differently down your stairs I could've... could've..." with dissolve
        # show NozomiHypno sad
        # "Nozomi tensely wraps her arms around her stomach while I struggle to process all of this." with dissolve
        # "What am I supposed to say to that?"
        # ncg "Thinking about it made me so angry at you."
        # ncg sad "And so scared..." with dissolve



        # show NozomiHypno stern
        # "I can't deny what happened yesterday in this very room. I saw it all." with dissolve
        # "Nozomi was a shambling, slurring mess that wanted to eat me alive. I didn't imagine that."
        # "And yet..."
        # ks "That's impossible!"
        # ncg annoyed "I have a stinging pain in my right foot telling me it's not." with dissolve
        # ks sigh "No, I mean... it can't have been hypnosis! Or, o-or there was more than that going on!"
        # show NozomiHypno stern
        # "Yeah. I gotta get away from the emotion of what went down and focus on the facts." with dissolve
        # ks neutral "Hypnosis can only guide a person into a focused, receptive state. It can't make you do literally anything you're told."
        # ks "So maybe I screwed up, but you should've only followed that command as much as you were comfortable with. As much as you were safe with."
        # ks "Because, Nozomi, you're always in control no matter how deeply hypnotized you get. No matter how convincing I might be."
        # show NozomiHypno annoyed
        # "Nozomi sighs loudly as she crosses her arms tightly in front of her." with dissolve
        # ncg "I know what you're talking about, Kyou. It's the hidden observer theory."
        # ncg "The idea that there's a separate consciousness that sits apart from a person's mind while they're hypnotized."
        # ncg "No matter how much a hypnotist dissociates a hypnotized person from reality, that part of them should always hold an objective view of their reality."
        # ncg stern "So if it needs to, it can intervene." with dissolve
        # ncg "It's why a deeply hypnotized person will still wake up if you left them alone for a while and they had to fulfill a basic need."
        # ks smirk "And I guess it's why hypnotists aren't ruling the world with their armies of brainwashed servants."
        # ncg stern_closed "... Uh, sure." with dissolve
        # ncg "But you know who else can intervene, besides some theoretical \"hidden observer\"?"
        # ks neutral "Uhh..."
        # "Wait, what's happening here?"
        # ncg angry "The hypnotist!" with dissolve


        # ncg neutral "But that's exactly the point, Kyou. There was no \"hidden observer\" to tell me I didn't seriously want to eat your brains or whatever." with dissolve
        # ncg stern_closed "Gosh, never mind this hidden observer stuff. Why didn't I feel ANYTHING when I hit my head or stepped on my glasses?" with dissolve
        # ncg stern "Why couldn't I stop myself? Why didn't I acknowledge the reality of the situation no matter what happened to me?" with dissolve
        # ncg "When I think about that, I can't help but wonder about the one thing in all of this that I know so little about."



        # n pout_left "S-so, I should be going now. But I'll talk to you later, okay?" with dissolve
        # show Nozomi:
        #     linear 1.0 xpos 0.6
        # "As she speaks Nozomi takes another step backwards, towards the door."
        # show Nozomi:
        #     xpos 0.6
        # ks surprised "W-wait, hold up!"
        # n shocked "H-huh?!" with dissolve
        # "Nozomi stiffens at the sound of my voice and her eyes widen in momentary panic."
        # "I guess I didn't have to speak so loud but damn, my mind's all over the place right now. Like, she literally just got here!"
        # "And I've been wanting to talk to her all night and day. She can't just leave like this!"
        # n side sad_side "Kyou, I... I-I need to go." with dissolve
        # ks sigh "Just... I dunno, how're you holding up?"
        # "I need her to tell me something at least."
        # n sad_closed "Oh... Well, you know. Not great." with dissolve
        # n front pout_left "I-I mean, not terrible but not... great." with dissolve


        # ncg "But I was thinking over and over about what happened. I've barely been able to put it out of my head."
        # ncg drooping sleeptalk "Oh, you know. Not great." with dissolve

        # ncg "But I was thinking over and over about what happened. I've barely been able to put it out of my head."
        # ks neutral "Yeah... How are you holding up, anyway?"
        # ncg drooping sleeptalk "Oh, you know. Not great." with dissolve
        # show NozomiHypno standing confused
        # "She sighs as she turns her head to look towards the television, staring wistfully into the screen with unfocused eyes." with dissolve
        # ncg "Yeah... n-not great."
        # "She looks uncomfortably to the side, avoiding my gaze, and after a pause she carries on."
        # n sigh "I got home okay yesterday, and I somehow managed to convince my parents that I fell over on the way back from school." with dissolve
        # n pout_left "This morning I told my friends that I tripped down the stairs at home." with dissolve
        # # ncg standing neutral "I somehow managed to convince my parents that I fell over on the way back from school yesterday, and my friends think I tripped down the stairs at home." with dissolve
        # n irritated "So I've lied to the people I care about most because I can't let anyone know what we've been doing. And I feel terrible about that." with dissolve
        # # ncg stern "So I've lied to the people I care about most just to keep what we have going under wraps, and I feel terrible about that." with dissolve
        # ks "You've never lied before?"
        # n pout "I've lied about eating my little brother's pudding when we were kids. I've never lied about anything big before." with dissolve
        # n frown "Like... oh, I don't know... getting injured while visiting some strange guy's house." with dissolve
        # # ncg stern_closed "I've lied about eating my little brother's pudding when we were kids. I've never lied about anything big before." with dissolve
        # # ncg confused "Like... oh, I don't know... getting injured while visiting some strange guy's house." with dissolve
        # ks sigh "And I'm sorry for that."
        # n side sad_side "I'm just terrified the truth's going to come out soon." with dissolve
        # # ncg sad "I'm just terrified the truth's going to come out soon." with dissolve
        # ks frown "You don't really look all that injured to me?"
        # n sad "I don't? It feels like everyone knows I'm limping as I walk, or that I'm wearing a little more makeup than usual."with dissolve
        # n front irritated "And god, why did I use different stories for my friends and parents? I TOLD you I'm a terrible liar." with dissolve
        # # ncg neutral "I don't? It feels like everyone knows I'm limping as I walk, or that I'm wearing a little more makeup than usual."with dissolve
        # # ncg stern_closed "And god, why did I use different stories for my friends and parents? I TOLD you I'm a terrible liar." with dissolve
        # # show NozomiHypno neutral
        # show Nozomi concerned
        # "Nozomi sighs once more, then turns her gaze towards the ground by my feet." with dissolve
        # # "Nozomi sighs once more, then turns her gaze back to me." with dissolve
        # n sigh "Anyway, we'll talk soon, okay?" with dissolve
        # # ncg sad "Anyway, we'll talk soon, okay?" with dissolve
        # ks sigh "Sure..."
        stop music fadeout 10.0
        # scene bg k room eve
        # show Nozomi front sigh noglasses at center:
        #     ypos 1.5
        #     linear 2.0 ypos 1.0
        # with blink
        # "As she stiffly gets up to leave, I can't say I'm not disappointed."
        # "As Nozomi turns to leave, I think better of trying to stop her a second time."
        # show Nozomi:
        #     ypos 1.0
        # show Nozomi:
        #     linear 1.0 xpos 0.8
        # "Still. I can't say I'm not disappointed."
        # "It's nice she stopped by at all, but I find myself thinking that this could've been a text."
        # show Nozomi:
        #     xpos 0.8
        # show Nozomi:
        #     linear 1.0 xpos 0.8
        # "Nozomi paces quickly over to the door and slips her shoes on in a hurry."
        # show Nozomi pain:
        #     xpos 0.8
        # n pain "Tstststs..." with dissolve
        # "The sound of Nozomi hissing in pain takes me away from my thoughts."
        # "It seems she forgot about the little injury she's carrying by trying to put her shoes back on so quickly."
        # # "... Maybe too much of a hurry, as she seems to forget the little injury she's carrying."
        # ks sigh "H-hey, be careful. The store's not closing that soon, is it?"
        # n surprised "S-store? But I'm going straight home." with dissolve
        # play music Measured
        # ks surprised "Wait, what?"
        # n shocked "What?" with dissolve
        # hide Nozomi
        # play sound dooropen
        # with dissolve
        # pause 0.5
        # play sound doorclose
        # "Okay, that was pretty weird. She DID say she was getting her glasses fixed, right?"
        # "So why would she..."
        # ks "HUH?!"
        # "My penlight?! Wasn't it in my pocket?"
        # "Am I going fucking crazy, or..."
        # ks frown "Nozomi..."
        scene bg k bedroom eve with longblink
        "I see Nozomi out and head up to my room to think on what just happened."
        queue music Past_Sadness
        "Honestly... I don't know what to make of it."
        "Like, I was afraid she'd want nothing to do with me after last night's disaster."
        "Maybe I should be happy she's still talking to me. But the way she forced me into giving her my penlight is leaving a bad taste in my mouth."
        "Just what is going on with her?"
        stop music fadeout 5.0
        scene bg blackscreen with longdissolve
        pause 2.0
        jump Day5_Con_Kyou_Nozomi_Zombie
        #
        #The rest of this script is cut off for now. Some of it will likely be put back in at a later time in the story.
        #

        # ncg "So... we need to talk about what happened, don't we?"
        # ks sigh "Yeah. Yeah, we do."
        # "As I agree, Nozomi brings up her phone and taps her thumb on the screen a few times."
        # ncg stern "Because..." with dissolve
        # "She falls silent as her eyes linger on her phone. I'm about to ask what she's looking at until I hear my own voice come out of her phone's speakers."
        # $t = Character("Nozomi's Phone")
        # t "{b}You recognise this light, Nozomi. So you know how natural it is to want to look into it.{/b}"
        # ncg stern_closed "Because... w-well, I've been listening to what you said to me while I was hypnotized." with dissolve
        # ncg "And, well..."
        # show NozomiHypno stern
        # "Nozomi frowns as she presses her thumb on the screen again, silencing the audio for a moment." with dissolve
        # ncg "Something stood out..."
        # t "{b}So from now on, Nozomi, whenever we are alone in this house and I say \"[hypno3]\"...{/b}"
        # ncg neutral "Ah, right here." with dissolve
        # t "{b}You will find yourself compelled to become exactly what you believe a zombie to be.{/b}"
        # "Nozomi taps her thumb and the crappy-sounding speech on her phone falls silent once more."
        # ks sigh "Man, you ever thought about getting a decent phone? That thing sounds like it's had it."
        # ncg surprised "Wh-what? No..." with dissolve
        # show NozomiHypno stern
        # "Nozomi shakes her head and scoffs at me as she sets her cheapass phone down on her lap." with dissolve
        # ncg "Nevermind that, what do you think of this thing you said to me?"
        # ks neutral "O-oh, when I was explaining how your zombie trigger was supposed to work?"
        # ncg "Yeah..."
        # show NozomiHypno sad
        # "She sighs." with dissolve
        # ncg "I mean, that's the thing. You didn't really explain it, you just left it to my subconscious to figure out."
        # ncg neutral "\"You will find yourself compelled to become exactly what you believe a zombie to be.\"" with dissolve
        # ncg folded stern_closed "That's so open-ended!" with dissolve
        # ks frown "Y-yeah, but..."
        # show NozomiHypno stern
        # "I had my reasons for doing it that way." with dissolve
        # ks "You weren't sure about the whole thing so I thought, well... you should decide how you want to be a zombie in front of me."
        # ncg angry "But that's not what you said! You told me to be a zombie just like I think they are!" with dissolve
        # ncg "And zombies are scary! They... they're creatures of the night that shamble around and eat the flesh off your bones while ranting about brains!"
        # ncg stern_closed "They're mindless, e-evil monsters and when you said the magic word, that's what I was supposed to be!" with dissolve
        # ncg angry "So that's what I was, Kyou! You... y-you MADE me into that!" with dissolve
        # ks surprised "But..."
        # show NozomiHypno stern
        # "I can't deny what happened yesterday in this very room. I saw it all." with dissolve
        # "Nozomi was a shambling, slurring mess that wanted to eat me alive. I didn't imagine that."
        # "And yet..."
        # ks "That's impossible!"
        # ncg annoyed "I have a stinging pain in my right foot telling me it's not." with dissolve
        # ks sigh "No, I mean... it can't have been hypnosis! Or, o-or there was more than that going on!"
        # show NozomiHypno stern
        # "Yeah. I gotta get away from the emotion of what went down and focus on the facts." with dissolve
        # ks neutral "Hypnosis can only guide a person into a focused, receptive state. It can't make you do literally anything you're told."
        # ks "So maybe I screwed up, but you should've only followed that command as much as you were comfortable with. As much as you were safe with."
        # ks "Because, Nozomi, you're always in control no matter how deeply hypnotized you get. No matter how convincing I might be."
        # show NozomiHypno annoyed
        # "Nozomi sighs loudly as she crosses her arms tightly in front of her." with dissolve
        # ncg "I know what you're talking about, Kyou. It's the hidden observer theory."
        # ncg "The idea that there's a separate consciousness that sits apart from a person's mind while they're hypnotized."
        # ncg "No matter how much a hypnotist dissociates a hypnotized person from reality, that part of them should always hold an objective view of their reality."
        # ncg stern "So if it needs to, it can intervene." with dissolve
        # ncg "It's why a deeply hypnotized person will still wake up if you left them alone for a while and they had to fulfill a basic need."
        # ks smirk "And I guess it's why hypnotists aren't ruling the world with their armies of brainwashed servants."
        # ncg stern_closed "... Uh, sure." with dissolve
        # ncg neutral "But that's exactly the point, Kyou. There was no \"hidden observer\" to tell me I didn't seriously want to eat your brains or whatever." with dissolve
        # ncg stern_closed "Gosh, never mind this hidden observer stuff. Why didn't I feel ANYTHING when I hit my head or stepped on my glasses?" with dissolve
        # ncg stern "Why couldn't I stop myself? Why didn't I acknowledge the reality of the situation no matter what happened to me?" with dissolve
        # ncg "When I think about that, I can't help but wonder about the one thing in all of this that I know so little about."




        #They then go on to wonder how on earth Nozomi became a zombie like that, even with the sloppy wording. It shouldn't be possible.
        #Nozo's hidden observer and general common sense should've stopped her from going overboard.
        #The pain of her injuries should've snapped her out of it! It doesn't make any sense unless...
        # And then Nozomi brings up the penlight as having some hidden properties and reveals that she stole it...
        #Might need to rephrase the above dialogue to imply Nozomi has already reached this conclusion before this convo with Kyou

        #Then she reveals the penlight she stole earlier


        # ncg "Well, anyway... two things came to mind while I was thinking things over."
        # ncg "First, for me to have been acting so convincingly as a zombie without ever letting up?"
        # ncg stern "That says to me that you could do with phrasing your hypnotic suggestions a lot better." with dissolve
        # scene cg k room eve bw
        # show NozomiHypno drooping flashback casual sleep
        # if persistent.NewSprite == "":
        #     $ks = DynamicCharacter("kyou_name", image = "KyouSideFlashbackOld", who_color = "#4B9374")
        # else:
        #     $ks = DynamicCharacter("kyou_name", image = "KyouSideFlashback", who_color = "#4B9374")
        # with flash
        # ks "You will feel your mind rapidly regress, finding it harder and harder to think."
        # ks "And you will find your speech has become slurred, unable to form any words except for one: \"Brains\"."
        # ks "Also, you will only be able to move in a shuffling gait, with your arms outstretched."
        # ks "As your mind regresses fully you will find {b}your only desire is to feast on human brains.{/b}"
        # scene cg k room eve
        # show NozomiHypno standing noglasses stern
        # with flash
        # $ks = DynamicCharacter("kyou_name", image = "KyouSide", who_color = "#8D715D")
        # ks sigh "You... you could say that, yeah."
        # ncg "I would never have attacked you unless you basically told me to."
        # ncg confused "But... that brings me to the second thing." with dissolve
        # ks concerned "What's that?"
        # ncg surprised "It STILL shouldn't have been possible. I should've been able to stop myself." with dissolve
        # ncg "You've heard of the hidden observer theory, haven't you?"
        # ks frown "Yeah. Isn't that about how even if you're deep under hypnosis you still won't do something you don't want to?"
        # ncg neutral "Basically. It's supposed to be like a separate consciousness that sits apart while you're hypnotized." with dissolve
        # ncg "No matter how much a hypnotist dissociates a hypnotized person from reality, that part of them should always hold an objective view of their reality."
        # ncg stern "So if it needs to, it can intervene." with dissolve
        # ncg "It's why a deeply hypnotized person will still wake up if you left them alone for a while and they had to fulfill a basic need."
        # ks smirk "And I guess it's why hypnotists aren't ruling the world with their armies of brainwashed servants."
        # ncg stern_closed "Uh, sure." with dissolve
        # ncg neutral "But that's exactly what I mean, Kyou. There was no \"hidden observer\" to tell me I didn't seriously want to eat your brains or whatever." with dissolve
        # ncg stern "Why couldn't I stop myself? Why didn't I acknowledge the reality of the situation?" with dissolve
        # ncg "And when I think about that, I can't help but wonder about the one thing I know so little about."
        # n "And when it comes down to it... I think it's logical to interrogate the one unknown in the equation."
        # show penlight at right with moveinright:
        #     ypos 0.346
        # "She frowns as she pulls out a penlight that was hidden inside the sleeve of her blazer."
        # "Wait."
        # ks surprised "How the fuck did you get that?!"
        # ncg stern_closed "Kyou, you keep this in your right pants pocket. I've seen you with it a couple of times now; it wasn't hard." with dissolve
        # ncg "If I'm going to be a liar today, I may as well be a thief, too."
        # hide penlight with moveoutright
        # "I groan as the realization of how she got hold of it hits me, then I feel anxiety well inside me as that realization is immediately followed up with ANOTHER realization."
        # if accepted_terms == False:
        #     ks frown "Y-You need to give that back."
        # else:
        ks frown "Nozomi... don't do anything rash, okay?"
        ncg neutral "..." with dissolve
        "Did she just raise an eyebrow at me?"
        ncg "I wonder what \"rash\" thing you're expecting me to do with this, Kyou?"
        ks "W... w-well..."
        ncg stern "As rash as shining this attention-grabbing light over YOUR eyes?" with dissolve
        "There's a soft click as Nozomi presses her thumb into the penlight, illuminating the cushion beside her."
        ncg smile "Maybe say a few words while I'm doing it?" with dissolve
        #This would be a great time for Kyou to reflexively trigger Nozomi's zombie state if he make the choice to not respect her earlier.
        ks angry "C-come on, that's enough! Give it back."
        ncg stern "Why, Kyou? Does me having it make you nervous? Nervous enough that you'd wrestle me for it?" with dissolve
        "Shit. Was I really about to..."
        ncg "Nervous enough to say the thing that caused this mess in the first place?"
        #Kyou calms down as Nozomi calls him out, and she tells Kyou that his reaction to her having the penlight makes it clear he believes it has power and is dangerous


        ncg annoyed "Kyou, what do you take me for? I've just been explaining that I think this thing could be dangerous." with dissolve
        ncg "No one should be doing anything with this until we know more about what it does."
        ks "Really? All it does is help keep your focus on the pattern it emits so you'll fall into trance easier. That's all I designed it for."
        ks "I wasn't even sure it'd do that until I used it on you."
        ncg stern "Right, so I'm literally your only data point. How do you know it doesn't do more than that?" with dissolve
        ncg "What if it actually managed to inhibit my hidden observer somehow? Because why else could this have happened to me?"
        ks neutral "I... I don't know."
        ncg angry "Not to mention your reaction just now. If you really thought it was so harmless, why does it matter so much what I do with it, huh?" with dissolve
        "I sort of reacted out of instinct there, but I guess she has a point."
        show NozomiHypno stern
        # ks sigh "I just thought that if I modified the light to make a pretty distraction it could help people focus in a hypnosis session." with dissolve
        # ks "It's supposed to help someone achieve a state of trance, there's no way it should've stopped your hidden observer, or whatever you want to call it."
        #
        #
        # "AUTHOR'S NOTE - Unaltered script continues from here on, so expect a lot of discrepencies until the next release."
        #Worth noting, Nozomi was very reluctant about the zombie trigger. How powerful is the penlight that she completely absorbed the suggestion anyway?
        ks sigh "Okay, well... maybe you're right. I don't know how being hypnotized with the penlight stacks up with any other method." with dissolve
        ks "What about you, though? What was it like when Satoshi hypnotized you?"
        "Nozomi doesn't reply immediately, instead running her thumb over the penlight she's keeping gripped in one hand."
        ncg standing neutral "It was different... I think." with dissolve
        ncg "I don't remember clearly now, but I'm pretty sure I could've stopped going along with his suggestions if I really wanted to?"
        "She shrugs."
        ncg stern "Anyway, I think it's obvious what we should do next." with dissolve
        "I end up nodding my head as I sigh. I don't really want to do this with the work I put into it, but..."
        ks concerned "We try without the penlight."
        show penlight at right with moveinright:
            ypos 0.346
        ncg stern_closed "Honestly if I had any sense I'd stop letting you hypnotize me altogether, but... yes, that's what I was thinking." with dissolve
        ncg neutral "I know this thing means something to you, but if it's doing what we think it's doing then we really shouldn't use it." with dissolve
        ks "Yeah..."
        hide penlight with moveoutright
        show NozomiHypno smile
        "Nozomi smiles as she hands me the penlight back, which I make a point of returning to my pocket." with dissolve
        ks smile "So... alright then. What should we do this time?"
        ncg "Well..."
        ncg sad "Obviously when I was spending all day thinking about what happened I couldn't help but think a lot about this, too." with dissolve
        ncg "And I don't know if this is coming from any lingering effects from the penlight or I'm just looking to excuse my own thoughts, but..."
        ncg stern "Uhh..." with dissolve
        "... What on earth is she thinking to get her embarrassed like this?"
        ncg stern_closed "I'll just say it." with dissolve
        ncg confused "I was thinking you could hypnotize me into obeying your commands?" with dissolve
        ks "Okay, like..."
        ks surprised "Wait, what?"
        ncg "I-I mean, only inside this house. A-and, only for lighter stuff."
        ks "Lighter stuff?"
        ncg "You know..."
        "..."
        ncg angry "I-I mean, don't try and make me have sex with you or anything!" with vpunch
        ks surprised "... Right. No sex, got it."
        ncg sad "I-I'm sorry. I've made this too weird. Maybe we should just forget all of this and... just go back to doing normal things." with dissolve
        "No. Oh no, I'm not going back to \"normal\" with you, Nozomi. Never again!"
        ks neutral "Nozomi, wait. It's fine, I think get it."
        ks "I mean... you want to feel like you're helpless and endangered. But you also want to know you're safe."
        ks "Maybe that's weird, but I want to do that for you."
        ks "And I CAN do that for you, Nozomi. If you'll let me?"
        ncg "I want... I want to let you, Kyou. There's one other thing, though."
        ks neutral "Okay. What's that?"
        ncg confused "It's good that we're not using the penlight but could we also just not do eye-fixation today?" with dissolve
        ncg "I don't really want to look at things any more than I have to until I get my glasses back."
        ks "Right... I guess that's kinda my speciality, but I'll see what I can do."
        show NozomiHypno sad
        "She nods and leans back on the couch, but I could see her tension from a mile away." with dissolve
        "So no penlight and a stressed-out subject. But I think I can give her what she wants."
        "Just need to diffuse the tension a little, that's all."
        ks "So... okay, I'm gonna be touching your arms at some points during this, just so you know."
        "Nozomi nods again as she places her hands down in her lap."
        ncg "Right."
        ks "And... I can see you're feeling tense, Nozomi, but remember anything that is about to happen, you can resist. You can always stop if you need to."
        "I give her a little smile as I add:"
        ks smile "But we both know you don't really want to do that."
        show NozomiHypno smile
        "Nozomi returns my smile with a nervous one of her own, but says nothing. I think that loosened her up a little." with dissolve
        ks "So in a moment, I want you to take a nice deep breath. I want you to hold it while I count to three, and on three I want you to let it all out."
        ks "And as you let it out, close your eyes and feel all the tension in your body draining away. Understand?"
        ncg "Mhm."
        stop music fadeout 10.0
        ks "Good. Now, deep breath."
        ncg neutral "..." with dissolve
        ks "One, two, three."
        ncg stern_closed "..." with dissolve
        ks "That's good, Nozomi. Now again, eyes open, deep breath."
        ncg neutral "..." with dissolve
        ks "One, two... three."
        ncg stern_closed "..." with dissolve
        ks "That's perfect. Relaxing so much. Feeling every muscle in your body grow loose and limp."
        ks "But none more so than all the little muscles around your eyes."
        play music Flow fadein 40.0
        ks "Take another deep breath, Nozomi, but this time pay special attention to those muscles in and around your eyelids."
        ks "Relaxing them so completely in one, two, three."
        ks "Your eyelids are so completely relaxed now that you will find that they have become impossible for you to open."
        ks "And I want to prove that to you, Nozomi. Try now and see if you can open those heavy, relaxed eyelids of yours."
        "Watching her intently, I wait a few moments as Nozomi's eyelids remain calmly closed."
        "When I think I see them flicker slightly, I continue."
        ks "Very good, Nozomi. Now stop trying, and let that completely relaxed feeling you have around your eyelids spread over your face and down your neck."
        ks "Feeling it spread further down your body, down your chest and arms... down your waist... spreading further down your legs and to the tips of your toes."
        "I wait another moment for her to cement the feeling of relaxation in her head before speaking again."
        ks "That's good, Nozomi. Now again I'm going to count to three, but this time on three, I want you to open your eyes again."
        ks "It'll be okay to do this, as you will soon be closing them again."
        ks "And when you do, you will feel yourself dropping ten times as deep, feeling ten times more relaxed than you are now."
        ks "So, opening your eyes on three, closing them again on my say and relaxing ten times as deeply."
        "As I say this, I raise my hand and hold the palm out in front of her face, a little above her eye level."
        ks "One, two, three."
        show NozomiHypno neutral
        "Nozomi's eyelids flutter open and her eyes immediately register the hand above her as I immediately swoop it down over her face." with dissolve
        ks "And eyes closed, Nozomi."
        show NozomiHypno drooping sleep
        $ renpy.transition(longdissolve, layer="master")
        ks "Ten times deeper. Ten times more relaxed. Very good."
        "Smiling at her responsiveness, I raise my hand over her face once more as I repeat the trick."
        ks "And again, opening your eyes on one, two... three."
        show NozomiHypno sleepy
        "Once again, the moment her eyes open I immediately bring my hand down over her face." with dissolve
        "Her eyelids start to flicker closed again before I even speak."
        show NozomiHypno sleep
        ks "And closed. Falling ten times deeper. Ten times more relaxed." with dissolve
        ks "But even as deeply relaxed as you are, you are going to find you can relax even deeper."
        "At this moment I reach out and take her right arm gently by the wrist."
        "Raising it slightly upwards over her lap, I notice how her fingers drag limply across her skirt as I do so."
        ks "You can feel how limp and heavy your arm is, can't you, Nozomi?"
        ks "It's alright, you don't need to say or do anything. It's fine to let me do all the work for you."
        ks "And as I drop your arm back into your lap you find yourself relaxing ten times deeper yet again. In one, two..."
        "Pausing a moment, I then gently let go of her wrist as her arm drops quietly back on her lap."
        ks "Three. Ten times deeper, Nozomi. You are doing so well at this. Finding it so good and natural to relax and drop so deeply as you are."
        ks "And I'm going to lift your arm again, while you're going to let me do all the work once more."
        "Once again, I lift her arm gently by the wrist, feeling no resistance whatsoever."
        ks "Just allowing yourself to feel how loose and limp you are. So deeply relaxed. One, two and..."
        "And again, I let her arm drop."
        ks "Three, ten times deeper still. Your body now so fully relaxed."
        ks "But your mind can relax even deeper, and we're going to take care of that now, Nozomi."
        ks "When I tell you to, I want you to count down from one hundred."
        ks "You will count down, speaking each number aloud as you go, followed by the words \"and deeper still\"."
        ks "I will be talking as you do this, but that's okay. you won't need to pay any conscious attention to what I say, just focus on counting down and relaxing your mind."
        ks "Relaxing your mind so much that each number becomes harder and harder to recall. And when you find the next number is too hard to remember, it's alright."
        ks "You can just stop and let all the numbers in your head disappear. Now start counting for me, Nozomi."
        show NozomiHypno sleeptalk
        "And just like that I see Nozomi's lips quiver as she begins to speak softly to the air." with dissolve
        ncg "One-hundred... and deeper still."
        ks "That's perfect, Nozomi."
        ncg "Ninety-nine, and deeper still."
        ks "Your mind relaxing more deeply with every number you count."
        ncg "Ninety-eight, and deeper still."
        ks "Finding each number so much harder to recall than the next."
        ncg "Ninety-seven, and deeper still."
        ks "As if the image of every number in your head were fading."
        ncg "Ninety-six, and deeper still."
        ks "And if the numbers are really so hard to recall..."
        ncg "Ninety-five, and deeper still."
        ks "Perhaps it would be best..."
        ncg "Ninety-four, and deeper still."
        ks "To avoid spending all that effort to recall them..."
        ncg "Ninety... ninety-three, and deeper still."
        ks "And just let them spill out of your mind."
        ncg "Ninety... two, and deeper still."
        ks "Finding it so easy to just..."
        ncg "Nine... Ninety-one... and deeper still"
        ks "Let them all..."
        ncg "Ninety..."
        ks "Disappear."
        ncg "Nine..."
        ncg "..."
        show NozomiHypno sleep
        "I give her a moment, watching her lip quiver and then fall still as she apparently admits defeat." with dissolve
        ks "That's perfect, Nozomi. Letting those numbers fall out of your head. Letting your mind relax so deeply and so completely, just as deeply as your body."
        "Another moment passes as I look over her dormant form."
        "I'm anxious about hypnotizing without the penlight for the first time, but it seems to be going well?"
        "I shouldn't be so nervous about this. I might be trying something a little different here, but I know she wants this."
        "I'll just pass her the suggestion she asked for and see how it goes."
        ks "And now that you are so relaxed, you may notice how wonderful it feels to be like this, and that I was the one who brought you to this deep, wonderful, relaxed state."
        ks "So if I can make you feel so wonderful, by having you relax so deeply for me, then perhaps you would feel just as wonderful by doing other things for me as well."
        ks "In fact, whenever we are in this house and we are alone, I could tell you to do anything and you might find yourself effortlessly and thoughtlessly obeying."
        ks "You could try to resist my commands, but doing so would be so much more effort than it would take to obey."
        ks "It would be so much more relaxing to simply obey my commands."
        ks "And so long as what I'm asking isn't lewd, you shouldn't have to think at all."
        ks "All you'll have to do is obey and feel as wonderful as you do now, knowing that you obeyed."
        ks "Allow what I have said to sink deep into your mind, making it a part of who you are, and once you have done so, you can tell me you understand."
        "..."
        ncg sleeptalk "I understand..." with dissolve
        show NozomiHypno sleep
        ks "I knew you would, Nozomi. Still feeling wonderful and relaxed as you accept this part of yourself." with dissolve
        ks "Now in a few moments you're going to come out of this deep relaxation and back to waking."
        ks "I'm going to count to five, and with each number you're going to feel a little more awake, a little more alert, until on five you will awaken completely."
        ks "And when you awaken, you will feel so good and refreshed, and ready to obey my commands."
        ks "One, just starting to stir."
        stop music fadeout 10.0
        ks "Two, beginning to feel the strength return to your legs."
        ks "Three, feeling that energy flow up your chest and your arms, as your breathing returns to normal."
        ks "Four, your senses returning to your head, letting your eyelids flicker and feeling so good about waking, and..."
        show NozomiHypno sleepy
        ks "Five. Feeling so good as you wake." with dissolve
        show NozomiHypno standing neutral
        "Nozomi breathes deeply through her nose as her eyes open fully, looking disoriented for a moment before her pupils focus on me." with dissolve
        "I give her a smile."
        ks "Tell me what you're feeling right now."
        show NozomiHypno smile
        play music Eons fadein 5.0
        "She smiles back and blinks sleepily before answering." with dissolve
        ncg "I feel... really good. Tingly."
        ks "And how does it compare with the other times you've been under for me?"
        ncg stern "Hmm..." with dissolve
        ncg "It's... different? Less euphoric, I guess. But I still feel really nice."
        "I nod. So maybe the penlight really does affect her differently in some ways. I guess it's too early to tell."
        "For now though, I want to see how she's responding to the hypnotic session we just had."
        ks "Interesting. Tap your nose."
        show NozomiHypno neutral
        "She perks an eyebrow at the odd request, but her right arm is already moving to bring her hand to her face as her index fingertip taps the tip of her nose." with dissolve
        "As she does so I can just make out a moan coming from her lips, and her eyelids flicker slightly."
        ks "That's right, Nozomi. Obeying me feels wonderful."
        ncg smile blush "It, uh... yeah." with dissolve
        ks "And since you're going to be so obedient to me, I think we ought to make a few changes while we're in this house together."
        ncg neutral "What are you thinking?" with dissolve
        ks "First, you will call me Sir from now on. Understand?"
        ncg "Yes, Sir."
        "Her response is immediate, and I can see that flicker of her eyelids once again. So far so good."
        ks "And also..."
        "But what happens if I really test her?"
        ks "Do you really need all those clothes?"
        ncg surprised "Huh?" with dissolve
        ks smirk "Anyone looking at us would think we're equals. But that's not true, is it?"
        ncg sad "A-ah, well... t-that is..." with dissolve
        ks "Answer my question, Nozomi."
        ncg "Mmn, it's not true." with dissolve
        ks "That's right. Now strip down to your underwear."
        scene bg k room eve
        show Nozomi front blush noglasses sigh
        with dissolve
        play sound clothes
        "She makes a face, but she doesn't hesitate to stand up and start disrobing in front of me. I hope that means she really is comfortable with this." with dissolve
        "I mean, I don't think she sees simply undressing as \"sex stuff\"."
        show Nozomi underwear
        "But as I watch her shed her outer clothing, standing in front of me in nothing more than her underwear, I don't get the impression she's really that upset." with dissolve
        ks smile blush "There. That's more reflective of your status in this house, don't you think, Nozomi?"
        ncg "... Yes, Sir."
        "Watching her reaction is fun and at least a little bit sexy to me but... now what?"
        ks neutral "So, err..."
        "I've never done anything like this before."
        ks "On your knees, Nozomi."
        show Nozomi:
            linear 1.5 ypos 1.2
        "As she obediently drops down to the floor to sit on her heels, I reach down to pet her head."
        "Maybe I should ask her what she wants me to make her do? Would that be defeating the purpose?"
        show Nozomi concerned:
            ypos 1.2
        "And now she's looking at me expectantly again." with dissolve
        "Well... if I assume she can now stop my influence over her at any time, maybe I shouldn't worry about this too much."
        ks smile "You know, I'm still thinking about the power I have over you right now. About all the things I could make you do."
        ks "And all you'd be able to do in return is smile and obey. Even if you knew it would risk your life. Even if my orders would strip you of your very humanity."
        ks "Doesn't that excite you, Nozomi?"
        n "It... it does, Sir."
        ks "So then, Nozomi. With this ultimate power at my disposal I command you to..."
        menu:
            "Make me a cheese omelette.":
                pass
        show Nozomi surprised:
            linear 1.5 ypos 1.0
        "Nozomi blinks in surprise as she registers what I said, but her body responds immediately as she rises back to her feet and starts padding towards the kitchen." with dissolve
        show Nozomi:
            xpos 0.65
            ypos 1.0
        show Nozomi:
            linear 3.0 xpos 2.0
        "I'm sure I heard a soft chuckle from her as she disappears from view, followed shortly after by the sound of the fridge door opening."
        "Not wanting to miss the sight of an underwear-clad girl cooking for me, I decide to follow her."
        scene bg k kitchen eve with dissolve
        "Taking a seat at the dining table, I simply watch with a grin as she works, navigating around my kitchen with relative ease to get her task done."
        show Nozomi front underwear concerned blush noglasses
        "I can tell she's a little flustered at my staring, but she doesn't say anything as she prepares the food, sets it on a plate and serves it up to me at the table." with dissolve
        n "Here you are, Sir."
        "I take a look at the cheese omelette in front of me, then at her, still grinning."
        ks smirk "I never said I wanted to eat it, Nozo. Besides, I'm not hungry."
        n side frown "What? Geez, then why did you have me make it?" with dissolve
        ks "Sit down and eat it yourself."
        show Nozomi:
            linear 1.0 ypos 1.1
        pause 1.0
        n front pout "But I'm not hungry either..." with dissolve
        show Nozomi:
            ypos 1.1
        "She says, as she tears a piece off and pops it into her mouth."
        n "Jerk..."
        ks smile "Tell me how you're really feeling, Nozomi."
        "She takes a moment to swallow her food before replying."
        n pout_left "Really good. I know it's just a simple thing, but even making me do this and feeling like I can't stop myself?" with dissolve
        n "It's really giving me a thrill."
        "She stops to take another bite of the omelette; her compulsion to obey my latest order conflicting with the previous."
        ks neutral "Yet you still look a bit worried to me."
        n sleeptalk "I guess I am, Sir. I'm just embarrassed to admit this to you. And to myself." with dissolve
        ks smile "Nozomi, there's no reason to feel embarrassed about feeling this way. You like what you like."
        show Nozomi concerned
        ks "Also, no one else needs to know if you don't want to say anything. We had a deal, remember?" with dissolve
        ks "So don't feel ashamed about who you are. You're safe here, with someone who wants you to be happy."
        ks "Let yourself enjoy this."
        show Nozomi smile
        "Nozomi gives me a smile from across the table and nods, still half-chewing as she responds." with dissolve
        n "Thank you, Sir. That does actually make me feel better."
        "I smile back at her."
        ks "Good. Now be a good girl and finish your omelette, and wash up when you're done."
        show Nozomi teasing
        "She pokes her tongue out at me, then takes another bite of her food." with dissolve
        scene bg k room eve with blink
        show Nozomi front smile noglasses with dissolve
        "Soon after she was done in the kitchen I had her get dressed and ready to leave."
        "Not that I wanted to, but dad's going to be home soon, and I don't think either of us want to explain this to him of all people."
        ks smile "You got everything?"
        n "Yes, Sir. Are we doing this again tomorrow?"
        "I respond with a wink and a knowing smirk."
        ks smirk "Oh, you WILL be coming back here tomorrow. Do I make myself clear?"
        show Nozomi laugh
        "She replies with a hearty giggle." with dissolve
        n "Yes, Sir. I must obey~"
        stop music fadeout 5.0
        jump Day5_Con_Kyou_Nozomi_Zombie
        # ks "Well... do you really know what it's like to be hypnotized, Nozomi? I mean like, in a proper session?"
        # n angry "...Are you trying to say Satoshi and the hypnosis videos I watched don't count?" with dissolve
        # ks "Uh... w-well, I mean, Satoshi was stage hypnosis and there was probably some peer pressure there to make you do what he wanted, right?"
        # ks "And I don't know what videos you watched, but I've seen a few myself and they all seemed kinda lame to me. Like, I'm not sure how anyone could hypnotize themselves watching them."
        # n irritated "Oh right, I'm sorry. Kyou, the master of all things hypnosis, said none of my experiences count so I guess I don't know what I'm talking about." with dissolve
        # ks "I'm... I'm just saying that I think you're giving that thing too much credit."
        # show Nozomi frown
        # "She snorts through her nose and shakes her head, before holding my penlight up ." with dissolve
    elif hypno2 == "NozoDom":
        play music Memories
        "Nozomi and I didn't contact each other overnight, and I'm anxious to see her again."
        "I want to see her again so bad."
        scene bg classroom day with blink
        "Coming into class a little earlier than usual, I take my seat and wait for the rest of my classmates to filter in."
        show Sayori sleeptalk at center:
            xpos 1.1
            linear 1.5 xpos 0.5
        pause 1.0
        "There's Sayori. Trying half-heartedly to hide a yawn behind the back of her hand as she walks past me to her desk."
        hide Sayori with dissolve
        show Hiroko frown at center:
            xpos 1.1
            linear 1.5 xpos 0.5
        pause 1.0
        "Hiroko strolls inside some minutes later, almost before the bell."
        h "Bounce your eyes, dude."
        ks confused "What?"
        h angry vein "You know what I'm talking about, creepo." with dissolve
        ks frown "I wasn't even..."
        hide Hiroko with dissolve
        "I trail off as she just walks past me to her desk."
        "I wasn't staring at her or anybody? What a bitch."
        play sound schoolbell
        "But class is about to start. Where the hell is Nozomi?"
        with blink
        "It takes me too long to realize, but as class continues I notice Hiroko and Sayori occasionally talk to the empty seat where Nozomi sits."
        "Of course it isn't empty. But then..."
        "How is it that I STILL can't see her?"
        with blink
        play sound schoolbell
        "Eventually the bell rings for lunch and Nozomi's friends assemble around her desk."
        show Hiroko uniform_armup happy at center, flip:
            xpos 0.25
        show Sayori at center
        with dissolve
        h "Let's go, rooftop club~"
        s sleep uniform_folded "I would be fine settling in class today, but if it's what the group demands..." with dissolve
        show Hiroko uniform smile_side
        n "I wouldn't say \"demand\", but it's nice out today." with dissolve
        "That's definitely her voice I just heard!"
        s smile_right "Ah well, who am I to argue with the majority. Lead on." with dissolve
        n "... Actually, you two go on ahead. I need to take care of something real quick."
        hide Sayori
        hide Hiroko
        "And off they go." with dissolve
        "Taking out my lunchbox, I sigh and pop it open as I observe the others who also stayed behind."
        "I may have started something with Nozomi, but right now I feel as alone as I ever was."
        ks surprised "H-Huh!?" with vpunch
        "Something just pressed against my nose!"
        play sound runningshoes
        "Rubbing the tip of my nose, the realization dawns on me as I hear the hurried shuffling of footsteps on the floor beside me that quickly grows distant."
        "Not that I can tell what I've figured out to the couple of classmates who wheeled round to look at me after I cried out."
        "At least someone is enjoying this..."
        with blink
        play sound cellvibrate
        "A few minutes later my phone buzzes in my pocket."
        show phone at right with moveinright:
            ypos 0.346
        "It's from Nozomi."
        "{color=#93624B}\"Boop!\"{/color}"
        "Rolling my eyes, I hurriedly text her back."
        "{color=#4B9374}\"At least someone's having fun around here.\"{/color}"
        play sound cellvibrate
        "{color=#93624B}\"So you really cant see me still? That is NUTS\"{/color}" with vpunch
        "{color=#4B9374}\"I seriously can't see you. I don't understand it either.\"{/color}"
        play sound cellvibrate
        "{color=#93624B}\"You were looking right at me when i came in this morning\"{/color}" with vpunch
        play sound cellvibrate
        "{color=#93624B}\"Thats why hiroko had a go at you\"{/color}" with vpunch
        "{color=#4B9374}\"I figured. Anyway you coming over tonight?\"{/color}"
        play sound cellvibrate
        "{color=#93624B}\"Are you kidding? How could i NOT???\"{/color}" with vpunch
        hide phone at right with moveoutright
        "I can feel her excitement radiating from the phone's screen as I set it down on my desk."
        "It's a little infectious. And it helps settle down my frustrations."
        "I can't stay annoyed at her, that's for sure."
        stop music fadeout 5.0
        scene bg blackscreen with longdissolve
        "The rest of the day passes without incident and I take myself straight home."
        play sound doorbell
        scene bg k entrance eve with dissolve
        "It's not long before the doorbell rings. That can only be her."
        play sound dooropen
        n "Hey, Kyou."
        play music Downtown
        "I jump back a little. Hearing a voice just come out of thin air is still a little freaky, even if I was expecting it."
        play sound doorclose
        "I watch as Nozomi's shoes appear before my eyes as she leaves them behind."
        "And I still don't understand how she did this. Or how I'm still doing this."
        n "Kyou? Come sit on the couch."
        ks surprised "O-Oh. Right."
        scene cg k room tv eve with blink
        "As I follow Nozomi's voice to the living room and get seated, I gingerly hold out a hand to try and get a feel for where exactly she is."
        play sound slap
        "And for that I get my hand slapped out of nowhere. It almost makes me jump." with vpunch
        n "Hey, hands to yourself!"
        ks confused "I-I wasn't- {w=0.5}{nw}"
        n "No, but that's what you're going to do if you keep that up!"
        "I fold my arms as I sigh."
        ks frown "Sorry... But it's the only way I can tell exactly where you are, and that's kind of your fault."
        "I hear a little groan in front of me. And I don't need to see her to figure she just rolled her eyes at me."
        n "Alright, Kyou, fine. Get comfortable, hold still and I'll see what I can do."
        "I give a little nod to the air, relax my posture and stare ahead as I wonder how this is going to work."
        "I can't even see if she's holding anyth- {w=0.8}{nw}"
        with flash
        n "Light's up here, Kyou... Yes, that's right."
        n "Did you notice how quickly you looked at the light? How natural that was..."
        scene cg k room tv eve
        show NozomiHypno standing uniform2 smile2
        with longflash
        play sound fingersnap
        "All of a sudden I find myself waking with a start, to the sound of snapping fingers."
        ncg "Welcome back."
        "I shoot the girl a puzzled look as I blink slowly."
        ks frown "What do you... oh!"
        "As I blink again, my initial confusion turns to joy as I'm greeted with a grin."
        ks smile "I can see you again!"
        show NozomiHypno laugh
        "Nozomi claps her hands together, with the penlight between them, and beams with pride." with dissolve
        ncg "Kyou, either I'm seriously amazing at this or you're the most convincing actor I've ever seen!"
        "I grin back at her. There's just no stopping myself from getting caught up in Nozomi's excitement."
        ks "And which do you think it is?"
        ncg smile2 "Ehehe, the former, obviously! Although maybe I need to drag you along to my D&D group sometime, just to be sure..." with dissolve
        "We share a chuckle before Nozomi leans back on the table and starts twirling the penlight in her fingers."
        ks "By the way... have you shown that to anyone else?"
        ncg neutral2 "Hm?" with dissolve
        ks "The penlight."
        ncg stern2 "Ah, no. Not at all. Besides, what would I tell people? It'd just be a light as far as they're concerned." with dissolve
        ks neutral "Oh... yeah, that's true. But I was thinking..."
        ks "You being interested in hypnosis isn't that weird, is it?"
        ncg "Well... maybe not in itself, no. I mean, it's a little weird maybe, but still..."
        ks smile "So why not tell them what it's for? Just leave out that it turns you on doing it."
        ncg annoyed "N-no! It'll come out, I'm sure of it." with dissolve
        ks neutral "Really?"
        ncg stern2 "Really. How long did you last before I found out your true intentions, Kyou?" with dissolve
        ks "Uh..."
        ncg "... Exactly. And then they'll never look at me the same way again."
        ncg sad "A-as it is, I'm not entirely sure I kept it together today." with dissolve
        ks surprised "... Huh?"
        ncg "When I realized you were still under my suggestion this morning? It was virtually all I could think about."
        ncg "I mean, we know how hypnosis isn't really about controlling minds at all, that it's a mutual collaboration between the hypnotist and the hypnotized..."
        ncg neutral2 "But I remembered how you practically begged me to make you lose the suggestion I gave you last night. Like you really couldn't do it without me." with dissolve
        ncg surprised2 "And I couldn't help but think that this was something I did TO you. Not WITH you." with dissolve
        ncg confused2 "That you were helpless to reject the reality I planted in your mind, because what we did really WAS mind control." with dissolve
        ncg "And thinking like that... w-well..."
        ncg sad blush2 "I just hope it wasn't written all over my face for all to see." with dissolve
        ks smirk "Well if it was I couldn't tell you."
        ncg smile2 noblush "Heh. But yes, you try explaining this to someone not in the know." with dissolve
        "But then, wait a minute."
        ks frown "So, you're telling me you also get off thinking you can control minds? I-is that it?"
        ncg surprised2 blush2 "A-ahh, w-well..." with dissolve
        show NozomiHypno sad
        "She sighs and gives a resigned nod to confirm what's already so plain to see." with dissolve
        ncg "I-I mean..."
        "Okay. So I guess I can understand why she's still hung up about what others will think."
        "After all, I never would have thought of her as the kind of person who could have such perversions."
        "What would I think of her if I'd known before now?"
        ncg folded stern2 noblush "I'm actually a little confused with myself!" with dissolve
        ks confused "Confused?"
        "She nods."
        ncg neutral2 "I really was just vaguely curious about trying to hypnotize you yesterday." with dissolve
        ncg confused2 "But I don't know... maybe you've awakened something in me, Kyou." with dissolve
        ncg "Until now, I never thought I could love being in this position..."
        ncg sad blush2 "As... the one doing the mind controlling." with dissolve
        ncg "I never realized I'd find a way to love it from this side of things, but with all the thoughts I've been having..."
        "She trails off as her face fills in the blanks for me once again."
        "And after an awkward pause, she quietly clears her throat to talk again."
        ncg stern2 "Not to mention... I seem to have a talent as a hypnotist as well, wouldn't you say?" with dissolve
        ks "I... y-yeah."
        show NozomiHypno standing smile_closed
        "My agreement makes her smile." with dissolve
        ncg "But what about you, Kyou?"
        ks "Huh? What ABOUT me?"
        ncg smile2 "I mean, you told me you hadn't thought about being \"excited\" about hypnotizing people the other day." with dissolve
        ncg "But now that you've spent some time under the light for me..."
        ncg laugh "How would you feel if I were to hypnotize you again?" with dissolve
        "Huh. Wow, I really hadn't thought about that. But now that she mentions it..."
        with flash
        "My thoughts suddenly go back to last night, when she..."
        with flash
        "When she hypnotized me... Not to mention what she did on me just now."
        "Man, was it really as hot as that?"
        ncg smile2 "Hm?" with dissolve
        ks "I'd... I-I'd feel..."
        menu:
            "Excited":
                pass
            "Thrilled":
                pass
        "Yeah... Yeah, I don't know why I'm getting hung up about this."
        ks smile blush "Not gonna lie, it feels really good to think about that."
        ks "Just... haha, just thinking about waking up to your face after bringing me out of a trance is like..."
        "Goddammit, I can feel my cheeks burning up. I can't tell her how much it's turning me on just thinking about it, holy shit!"
        ks "Man, I just remember how good it felt waking up to you the last time... Just really nice."
        ncg laugh "Ahahaha!" with dissolve
        "Nozomi giggles heartily, and I'm just grateful she can't see what's going on in my pants right now."
        ncg smile2 "Mhmhmhm~ You know, it's kinda ironic when you think about it." with dissolve
        ncg smile_closed "That you started out wanting to hypnotize girls, only for this to happen..." with dissolve
        ncg smile2 "And... speaking of which, there's an idea I wanted to try with you along those lines." with dissolve
        ks "Y-yeah?"
        ncg "Yeah. I was thinking we could try a sort of \"turning the tables\" roleplay."
        ncg smile_closed "I'll use hypnosis to try and convince you that our situations are reversed." with dissolve
        ncg "And then I'll..."
        ncg laugh "Ahaha, well, then I'll set you straight~" with dissolve
        ncg smile2 "Is that something you'd like to try, Kyou?" with dissolve
        menu:
            "Totally":
                pass
            "Absolutely":
                pass
        "I don't know exactly what she's talking about. But if this means I get her to hypnotize me again, why would I refuse?"
        ncg smile_closed "Wonderful~ Now, if I could have your eyes up here..." with dissolve
        scene cg k room reversal
        show NozomiReversal penlight uniform neutral
        with blink
        "My eyes swivel upwards on instinct as I notice the penlight is already in her hand..."
        show NozomiReversal smile
        with flash
        ncg smile "That's right, Kyou. Up at the light..."
        scene cg k room tv eve
        show NozomiHypno standing uniform2 neutral2
        with longflash
        n "... Kyou? Kyou? Is everything okay?"
        ks neutral noblush "Hm?"
        "As I look to her, I smile. Everything's better than okay."
        "Better than she knows."
        ks smile "Everything's fine, Nozomi. No... everything's perfect."
        ncg confused2 "Huh? Is that so?" with dissolve
        "With a grin, I right myself up on my seat as I take a deep breath for what I'm about to do."
        ks "Very much so. Do you know what's really been going on tonight, Nozomi?"
        ncg folded stern2 "... Why are you talking like that? What do you mean?" with dissolve
        ks smirk "I mean, Nozomi, that while you thought you were hypnotizing me, I've been working a subtle form of hypnosis on you."
        ncg surprised2 "E-ehh?!" with dissolve
        "That got her attention, although the surprised look in her eyes quickly gives way to disbelief."
        ncg annoyed "Oh, very funny, Kyou. Do you honestly expect me to fall for something like that?" with dissolve
        "Honestly? I think her reaction right there is already setting herself up for me."
        ks "I DO expect you to fall, Nozomi. You're already halfway there."
        "And as I speak, I bring a hand up to her face and point a finger at her forehead."
        ncg lookup2 "W-wait, what are you doing?" with dissolve
        ks "I'm not doing anything. You on the other hand found it so very easy to focus on my fingertip, just as you were supposed to."
        ncg "Th-that's..."
        "Playing to her imagination like this is just too easy."
        ks "That's absolutely right, Nozomi. And it's fine, there's no need to think too deeply about it. You'll find it so much easier to relax and focus up here..."
        "And she's as eager for this as I knew she'd be."
        ks smile "That's right. Just watching my fingertip, taking a nice deep breath and letting go. Focusing deeply for me now. Watching my fingertip..."
        "I bring my finger closer to her forehead, ever so slowly, as I see her eyes continue to be drawn to it."
        ks "And what you'll find is going to happen is that as I touch your forehead, your eyes are going to drop closed and you're going to drop deep into trance for me, Nozomi."
        show NozomiHypno standing
        ks "Yes, just letting it happen... Watching that finger, breathing deep, focusing all your attention here before you..." with dissolve
        "I then swiftly tap her forehead with a smile."
        show NozomiHypno drooping sleep
        ks "Sleep Nozomi." with dissolve
        "And there she goes."
        ks "Dropping deeper, conscious thoughts fading, body relaxing... That's right, very good."
        "I just had a feeling that she wanted things to go back to this, with me hypnotizing her."
        "And for her to prove me right is stirring powerful feelings in me."
        ks "So now, Nozomi, now that you're in this deep, blissful trance for me, I want you to listen carefully to my voice and what I'm about to say."
        ks "Because from this moment on, until I say you can stop, you may find yourself helplessly obeying anything my voice tells you to do."
        ks "You might not, if I tell you to do something dangerous or wrong, but you will find it so much easier to obey my words, Nozomi."
        ks "Do you understand?"
        ncg sleeptalk "Mmn... I understand." with dissolve
        "Perfect. I wondered if that was going too far for her, even with that little assurance of safety, but it seems she's as game as I thought she'd be."
        ks "That's great, Nozomi. So now I'm going to count up to three, and you're going to wake from this trance happy and refreshed."
        ks "Counting up now... one, two..."
        show NozomiHypno sleepy2
        ks "Three." with dissolve
        ncg "Mmn..."
        "I smirk as she comes to. Seems my little stunt worked like a charm."
        ks smirk "Welcome back, Nozomi. I knew you wanted this to happen."
        ncg standing stern2 "Hm? Wanted what to happen?" with dissolve
        ks "You wanted to be hypnotized."
        "I'm gonna have some fun with this."
        show NozomiHypno folded annoyed
        ncg "Uh, I'm the hypnotist here, remember?" with dissolve
        ks "So you say, but you just allowed yourself to be hypnotized, didn't you."
        ks "Maybe you weren't as keen to be the hypnotist as you thought."
        ncg stern2 "Don't be ridiculous." with dissolve
        ks smile "Why is that ridiculous?"
        ncg annoyed "Because I'm not hypnotized, for one!" with dissolve
        ks smirk "We'll see about that, Nozomi, especially when you know you won't be able to resist what's coming."
        show NozomiHypno neutral2
        "Nozomi looks me over curiously, as if she's started to wonder if she should take me seriously." with dissolve
        ncg angry2 "I'm NOT hypnotized!" with dissolve
        "She can protest all she wants, but right now my mind is racing at the possibilities..."
        "What could I tell her to do that she might accept under hypnosis?"
        show NozomiHypno stern2
        ks "You can believe you're not, but sure as anything, when I snap my fingers you're going to..." with dissolve
        menu:
            "Rub your tummy":
                $hypnocommand = "tummy"
            "Grab your boobs":
                $hypnocommand = "boobs"
        play sound fingersnap
        show NozomiHypno standing confused2 with dissolve
        ncg "Huh? I'm going to what?"
        "... That was a simple thing to ask. Did she not hear?"
        if hypnocommand == "tummy":
            ks frown "I said rub your tummy, Nozomi!"
        elif hypnocommand == "boobs":
            ks frown blush "I said grab your boobs, Nozomi!"
            "Ugh, saying it again is making me self-conscious."
        "But still, Nozomi just stares at me blankly."
        ncg sad "I'm sorry, Kyou..." with dissolve
        ncg neutral2 "Could you show me what you mean?" with dissolve
        if hypnocommand == "tummy":
            "I shoot her an annoyed look as I slap my hand down on my stomach and start rubbing myself."
        elif hypnocommand == "boobs":
            "I shoot her an annoyed look as I grip my breasts with my hands aggressively."
        ks "L-Like this, okay? Do this!"
        ncg confused2 "Oh... okay." with dissolve
        "... Is she just going to sit there?"
        show NozomiHypno neutral2
        if hypnocommand == "tummy":
            "Ugh, even rubbing my tummy harder doesn't get the point across. Goddammit." with dissolve
        elif hypnocommand == "boobs":
            "Ugh, even groping myself harder doesn't get the point across. Goddammit." with dissolve
        "Maybe if I told her to do something else..."
        menu:
            "\"Nozomi, pat your head.\"":
                $NozoDom = "safe"
            "\"Nozomi, give me a striptease.\"":
                $NozoDom = "unsafe"
        ncg "..."
        ncg confused2 "Uh, could you show me what you mean?" with dissolve
        "I don't believe this!"
        show NozomiHypno neutral2
        if NozoDom == "safe":
            if hypnocommand == "tummy":
                "But if I show her by patting my head while rubbing my stomach, she'll take my meaning and obey, right?" with dissolve
            elif hypnocommand == "boobs":
                "But if I show her by patting my head with one hand while squeezing my breast with the other, she'll take my meaning and obey, right?" with dissolve
            ks frown "... Nozomi?"
            ncg "Hm?"
            "... This isn't working."
            ks sigh "Okay, I give up."
            "Nozomi chuckles at my discomfort."
            ncg smile2 noblush "It's alright, Kyou. But I wanted to be honest about my reactions, and I just didn't feel anything that time." with dissolve
            ks confused "I see..."
            "Maybe I was too ambitious?"
            ncg neutral2 "You DID try to hypnotize me though, didn't you? Maybe I wasn't deep enough?" with dissolve
            "... She might have a point. I didn't spend that long with her in trance before I tried something like this."
            "I should've used more deepeners on her. Should've repeated what I wanted more so it'd settle in her subconscious."
            ks sigh "Yeah... maybe. Do you mind if I try this again?"
            "Nozomi nods her head, and I raise a finger at her like before."
            ks frown "So Nozomi, once again you're going to find your attention focused on my fingertip."
        elif NozoDom == "unsafe":
            show NozomiHypno surprised2 blush2
            play sound clothes
            "So I'll just have to show her, as I unfasten my pants and rip them off of me." with dissolve
            "... Is she just gonna stand there? Fine, off comes the rest of my uniform."
            ncg "K- Kyou..."
            ks nude frown "Y-yeah?"
            n "Gosh, you want me to do... t-that?"
            "Nozomi's reaction gives me pause, and as I look down on my half-naked self I can't help my cheeks from burning as red as hers."
            ks sigh "Uhhh... s-sorry, maybe I was out of line trying to make you do something like this."
            ncg neutral2 "Yeah... maybe just a little bit." with dissolve
            ks sad "Sorry..."
            "I was trying to provoke her, I'll admit. After her failure to follow along last time, I thought she'd be more determined to make it work no matter what I said."
            "She gets off on stuff like this, she said. But it was stupid to think she'd actually..."
            ncg confused2 "... It's okay, Kyou. Don't worry about it." with dissolve
            ks confused "H-huh? You sure?"
            "Because yeah, she can say that, but... her expression just now?"
            ncg "After all, I was talking about controlling your mind. About doing things to you and not with you, even though it made you uncomfortable."
            "I don't know how to read it."
            ncg lookup2 "It was a little naughty of me. But it seems we're both fine about doing naughty things with hypnosis, aren't we?" with dissolve
            ks "I... y-yeah, I guess?"
            "What I'd give to know what she's really thinking about me right now."
            ncg smile2 "So... so if it's really okay to be a little naughty, then try to hypnotize me again, Kyou." with dissolve
            ks surprised "S-seriously?! You're sure about that?!"
            ncg "Take me deeper this time. Take me under your power and... we can be a little naughty together."
            "My mouth feels a little dry as my hand unhesitantly rises to point a finger between her eyes like before."
            ks frown "A-alright. So Nozomi, I want you to focus all your attention on my fingertip."
            "We're doing this. I'm going to do it right this time."
            show NozomiHypno lookup2 noblush
            ks "There's no need to think any more. No need to do anything but stare. Stare and feel yourself beginning to sink." with dissolve
            "I'll bring her back into trance and use some more deepeners this time. Make sure she's good and deep and relaxed."
            ks "Just take a deep breath in... and out. Allow everything else to slip away from your mind."
            "Then I'll... I'll make sure her subconscious can't misinterpret what I want this time."
            ks "In... and out. All your focus belongs on the very tip of my finger now."
            "She wants this. *I* want this."
            ks "That's right, Nozomi. Just watching, and breathing... and sinking..."
            "It's going to WORK this time!"
        ncg surprised2 "Huh? Wait, what are you doing again?" with dissolve
        "... Fucking seriously? I don't want to admit it, but I'm getting a little pissed off with her tonight."
        ks frown "I'm going to put you back in trance again, okay?"
        "Is she serious about this at all?"
        ncg confused2 "Oh... Well, then." with dissolve
        "Nozomi pauses in thought for a moment, then smiles."
        ncg smile2 "Could you show me what you mean?" with dissolve
        stop music fadeout 1.0
        scene bg blackscreen with dissolve
        "... I don't remember much of the night after that."
        pause 2.0
        jump Day5_Con_Kyou_Nozomi_Reversal

label Day4_Switch_Safe:
    scene bg street1 day with longdissolve
    "The next morning arrives, and I'm walking to school with only one purpose..."
    # "The next day arrives, and Kyou walks to school with only the coming evening on his mind."
    scene bg classroom day with blink
    play music Bright_Opening
    "... To see this dull day through to the end."
    show Nozomi side smile_side at center
    show Hiroko smile_side at center:
        xpos 0.75    
    h "C'mooon, what're you thinking about?" with dissolve
    "Just as I settle at my desk, I spy Nozomi walking in with Hiroko in tow."
    n happy "Ehehe, I told you it's nothing!" with dissolve
    "And if I were to guess, her head's in the exact same place as mine."
    h uniform_headhold2 annoyed_side "Gonna keep me guessing, huh? You get another one of those games you like so much?" with dissolve
    n  neutral "Well, in a manner of speaking..." with dissolve
    "Our eyes meet for a split second. But she's quick to pull away before I can react."
    n happy "You wouldn't get it~" with dissolve
    h rolleyes "Gawd! I hate when you're like this..." with dissolve
    hide Hiroko
    hide Nozomi
    with dissolve
    "Yeah, she's definitely thinking what I'm thinking."
    play sound schoolbell
    with longblink
    "But the pair of us had to put those thoughts aside and get on with our schoolwork. At least until lunch rolls around."
    show ClassroomLunch boy2_lunch hiroko h_annoyed_sayori n_armup n_smile_left glasses sayori s_neutral_hiroko with blink    
    h "Alright, we getting out of here or what?"
    show ClassroomLunch s_smile_hiroko
    s "Why so eager, Hiroko? I cannot imagine hearing more about English sentence structure worked up an appetite." with dissolve
    "I obviously can't talk to her around her friends, though."
    show ClassroomLunch h_frown_nozomi
    h "It's Nozo. She's holding out on us." with dissolve
    show ClassroomLunch n_neutral_left s_smile_hiroko
    s "Oho, is she now?" with dissolve
    show ClassroomLunch n_sigh
    n "Honestly, Hiroko. You wouldn't be interested." with dissolve
    show ClassroomLunch s_smirk_hiroko
    s "Well now *I* am interested." with dissolve
    scene bg classroom day
    show Hiroko annoyed_side at center, flip:
        xpos 0.25 ypos 1.1
        linear 2.0 ypos 1.0    
    show Nozomi side irritated at center, flip:
        ypos 1.1
        linear 2.0 ypos 1.0
    show Sayori smirk at center:
        xpos 0.75 ypos 1.1
        linear 2.0 ypos 1.0
    with blink
    "Probably shouldn't text her either."
    show Nozomi at flip:
        ypos 1.0
        linear 6.0 xpos 2.0
    show Hiroko at flip:
        ypos 1.0 xpos 0.25
    show Sayori:
        ypos 1.0    
    n "Okay, so in the game there's this global pandemic, so you and three other players have to..."
    show Sayori uniform_handup neutral at flip
    "Those two are obviously gonna be hovering over her the entire lunch break." with dissolve
    s concerned "Wait, we are fussing about a board game?" with dissolve
    hide Nozomi
    hide Hiroko
    hide Sayori
    with dissolve
    "This is going to be the longest lunch break ever..."
    play sound schoolbell
    scene bg classroom eve with longblink
    "Lunch, and the rest of class, proved to be as much of a listless drag as I feared."
    show Nozomi front2 neutral at right
    n "Stand." with dissolve
    "But it's over now."
    n sleep "Bow." with dissolve
    hide Nozomi
    stop music fadeout 5.0
    "All I need to do is get out of this dull place." with dissolve
    scene bg street1 eve with blink
    "Take the direct route home. No distractions, no wasting any more time."
    scene bg k entrance eve with blink
    "Because Nozomi sure isn't going to."
    play sound doorbell
    "I'll definitely need to hit the ground running."
    play sound dooropen
    show Nozomi front2 pout at center with dissolve
    play music Downtown
    n "Good evening."
    ks smile "Hey."
    # "And sure enough, Nozomi shows up within minutes, and just as eager to get going again as she said she was during lunch."
    scene bg k room eve
    show Nozomi side neutral_side at center
    with blink
    "She's certainly not wasting any time, as she quickly pops off her shoes before following me back to the living room."
    scene cg k room eve
    show NozomiHypno standing neutral
    play sound sitting
    with blink
    "But as she settles down on the couch, I can't help but notice how glum she looks."
    ks confused "Uh... is everything okay?"
    show NozomiHypno standing sad
    "Nozomi lets out a weary sigh." with dissolve
    n "Yeah..."
    show NozomiHypno lookup
    n "Just could've done without Hiroko getting on my case about my good mood, that's all." with dissolve
    "Huh. Can't say I didn't notice it earlier, but Nozomi always seemed to tolerate Hiroko being in her face all the time because they're friends or whatever."
    ks confused "Was it really that bad?"
    show NozomiHypno folded stern_closed
    n "Ugh..." with dissolve
    "Maybe they're not as close as I thought they were?"
    show NozomiHypno neutral
    n "... I don't like lying to her. But there are some things she just wouldn't understand." with dissolve
    show NozomiHypno sad
    n "And I wish *she* understood that sometimes." with dissolve
    show NozomiHypno folded stern_closed
    "She lets out a disgruntled little snort, then softly shakes her head." with dissolve
    n "Forget it. I shouldn't be telling you this."
    show penlight at right with moveinright:
        ypos 0.346
    "Well, it's not like I care that much anyway. So I simply shrug as I take my penlight from out of its pocket and smile as if I'd already forgotten what we were talking about."
    show NozomiHypno neutral
    ks smile "Sure. Then do you want to get started?" with dissolve
    show NozomiHypno smile
    n "Of course. So what's the plan for tonight?" with dissolve
    "She smiles back as she takes out her phone and starts setting up her recording app."
    "Right, I should probably explain myself first."
    ks "Okay. So I want to keep this simple and try to give you a reinduction trigger. I'd say something to you, and you'd be able to drop straight back into trance."
    show NozomiHypno neutral
    n "Hmm..."
    ks "I have a feeling it'll work pretty well on you, and it'll save us some time when it's my turn again."
    n "Yes, that sounds fine. Just make sure to stipulate it'll only work in here, so we don't have any unwanted accidents."
    ks "Naturally."
    show NozomiHypno lookup
    n "And no using it out of turn, obviously." with dissolve
    "... Should I be a little annoyed that she thinks I need to be reminded of this stuff?"
    ks neutral "Yeah. Obviously."
    "Well, nevermind. I've been looking forward to this time with Nozomi all damn day."
    hide penlight at right with moveoutright
    show NozomiHypno neutral
    "So I set Nozomi's phone app to record, click my penlight on and raise it aloft as I try to keep a smile on my face." with dissolve
    ks smile "Now make yourself comfortable, and turn your eyes up... here."
    show NozomiHypno standing lookup with dissolve
    $light_y = 0.28; light_x = 0.4
    call cglightshow
    stop music fadeout 10.0
    ks "Remember this light again, Nozomi. Remember how natural it is for your eyes to search for it."
    call cglightshow
    ks "And as your eyes look, remember how relaxed it makes you feel while you try to make out that pattern that forms in your eyes once more."
    call cglightshow
    show NozomiHypno standing drowsy
    $ renpy.transition(longdissolve, layer="master")
    $light_y = 0.32; light_x = 0.4
    play music Flow fadein 10.0
    ks "It's probably making you sleepy already. Making you feel so, so drowsy and tired. And that's perfectly alright, Nozomi."
    call cglightshow
    ks neutral "It's perfectly correct that you feel tired under the light."
    call cglightshow
    ks "It's very natural. Very comforting. Very safe to feel this way."
    call cglightshow
    ks "Just watching the light now. Letting your thoughts slip away as you watch the light going back and forth. Back..."
    call cglightshow
    show NozomiHypno drooping sleepy
    $ renpy.transition(longdissolve, layer="master")
    ks "And forth."
    $light_y = 0.37; light_x = 0.4
    call cglightshow
    ks "It's becoming very easy to drop into a nice relaxing sleep for me, Nozomi."
    call cglightshow
    ks "Very easy. Very natural. As natural as breathing."
    call cglightshow
    ks "So natural... sleep, Nozomi."
    ncg drooping sleep "..." with dissolve
    ks "That's right, Nozomi. Back in this nice, safe, relaxing state of trance."
    "It really is remarkable how easy it seems to trance her like this."
    ks smile "Nice and relaxed. Ready to listen and accept my words. Isn't that right, Nozomi?"
    ncg drooping sleeptalk "Right..." with dissolve
    show NozomiHypno sleep
    "And she can do the same to me just as easily?" with dissolve
    ks "Very good. Going deeper now, Nozomi."
    "Are we both just that good at hypnosis? It really seems hard to imagine."
    ks "Dropping deeper. Feeling more and more wonderful to be this deeply hypnotized."
    "I never would've believed it, if I wasn't speaking these words to her dormant form at this very moment."
    ks "So wouldn't it be nice if I could say something to you while you're awake, just between us, that lets you fall right back into this nice, deep, tranced sleep?"
    ncg sleeptalk "Yes." with dissolve
    show NozomiHypno sleep
    $hypno3 = "Time to dream"
    ks "Yes it would. So from now on, Nozomi, whenever we are alone in this house and I say... \"Time to dream\"..." with dissolve
    ks "You will instantly fall back into this deep, tranced sleep. Every bit as deep, if not more, than you are currently."
    ks "But remember, it will only work when I say this exact phrase, and only while we are in this house. It will have no effect unless those things are true."
    ks "Do you understand, Nozomi?"
    ncg sleeptalk "Yes..." with dissolve
    show NozomiHypno sleep
    ks "Very good, Nozomi. It's something you'll process without even having to think about it. It's as natural to you as breathing, or blinking." with dissolve
    ks "Let yourself accept this new programming, making it a natural part of you, and then slowly begin to wake up as I count to five."
    ks "One... feeling so good about being hypnotized."
    stop music fadeout 10.0
    ks "Two... feeling happy and refreshed."
    ks "Three... happily accepting your new programming."
    ks "Four... beginning to test your eyelids, letting them open."
    show NozomiHypno sleepy
    ks "And... five, wide awake!" with dissolve
    ncg standing drowsytalk "Uh... I'm awake..." with dissolve
    ncg surprised "I'm awake!" with vpunch
    play music Downtown
    "I chuckle as I watch her snap back to life, then hand her back her phone."
    ks smile "So you are."
    show NozomiHypno smile
    "She smiles as she takes the phone back in her hands, looking at it, then at me." with dissolve
    ncg "Is it just me, or was that faster than the other day?"
    ks "Yeah. You weren't hard to drop last time, but today was even easier."
    "Nozomi nods as she starts playing the video back on her phone, looking to the screen."
    "I guess I should try that trigger right away."
    ncg laugh "I'm still blown away by how easy we're doing this to each other!" with dissolve
    ks "Well, for your part Nozomi, you do make it easy on me. Especially when you know it's [hypno3!l]."
    show NozomiHypno drooping sleep
    stop music fadeout 2.0
    $ renpy.transition(longdissolve, layer="master")
    "Nozomi's phone falls into her lap as her eyes snap shut while she slumps in her seat in an instant."
    play music Flow
    show NozomiHypno drooping sleep arm_uniform noblush
    "I have to reach a hand out and touch her shoulder to steady her, so she doesn't fall off the couch." with dissolve
    "Then I start to speak softly to her once more."
    ks "Very good, Nozomi. Nice and deep. Nice and safe."
    show NozomiHypno no_arm
    "Once she's settled I then reach down and pause the video on Nozomi's phone. Having my voice playing on there would no doubt confuse things." with dissolve 
    ks "I'm going to wake you back up on three, Nozomi. And on three you will once again become wide awake, feeling refreshed and happy."
    ks "One, realizing you were once again hypnotized."
    stop music fadeout 5.0
    ks "Two, knowing how much you love to be hypnotized."
    ks "And three, waking up happy and refreshed."
    show NozomiHypno standing smile_closed
    "Nozomi lets out a sleepy little smile as she rouses herself." with dissolve
    ncg "You used the trigger, right?"
    play music Downtown fadein 5.0
    ks "I did, yeah. Another complete success."
    show NozomiHypno smile blush
    "She blushes as she pushes her glasses back up her nose, which had fallen a little askew when she slumped during the trance." with dissolve
    ncg laugh "Gosh. Now that was a nice feeling~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    ks "What was that like? Could you stop it at all?"
    ncg surprised noblush "I couldn't... no, not at all!" with dissolve
    ncg confused  "The moment I saw your lips move, time just sort of stood still and I was out again!" with dissolve
    "I nod. That's certainly how it looked to me."
    ks "Seems like you enjoyed it too."
    show NozomiHypno folded smile
    n "W-well, of course. Dropping into trance has always been a good experience for me." with dissolve
    show NozomiHypno folded smile_closed
    n "I'm starting to feel spoiled getting to do so much of it~" with dissolve
    "We share a chuckle. It was a simple thing, but it really does feel great that I can brighten her day with this penlight of mine."
    show penlight at right with moveinright:
        ypos 0.346
    "And seeing as she seems in no rush to go anywhere, I think to hold said penlight out to her."
    show NozomiHypno smile
    ks smile "So, do you have time to try something else on me?" with dissolve
    show NozomiHypno neutral
    n "Hm? That's it?" with dissolve
    "Okay, that answer leaves me a little confused."
    hide penlight with moveoutright
    ks confused "That's... is what it?"
    show NozomiHypno confused
    n "I mean, the reinduction trigger is nice and all, but when you think about it, all you did was hypnotize me again." with dissolve
    ks "Well..."
    show NozomiHypno lookup
    n "Sure you technically did try a suggestion on me, but... are you really satisfied with just that being your turn?" with dissolve
    "... So she means *she's* not satisfied with that being my turn, huh."
    ks neutral "Huh. I guess it's not much of a turn when you put it that way."
    show NozomiHypno smile
    n "Mhm. So if you have anything else in mind, I'd like to hear it." with dissolve
    show NozomiHypno smile_closed
    n "Might be a good way to prove your trigger works properly too~" with dissolve
    "Well... I have thought a little about what else I could do with her. Of course I have."
    show NozomiHypno smile
    n "Um, provided we don't take too long with it. I still can't be out too late." with dissolve
    ks "Not too long, huh..."
    "She always needs to go so soon. That does give me an idea, though..."
    ks frown "... Is that true?"
    show NozomiHypno annoyed
    n "What do you mean? Of course it's true!" with dissolve
    ks smirk "How would I even know? Maybe you actually can't wait to get out of here so you can try that new board game you were talking about this morning."
    show NozomiHypno angry
    n "Ugh, there IS no new board game! I only said that to Hiroko because..." with dissolve
    show NozomiHypno annoyed
    n "Oooh, of course you were eavesdropping on us again!" with dissolve
    ks smile "Yeah, I... I know, I'm just messing with you. But what if I could get you to lie about anything and everything? That could be fun, right?"
    show NozomiHypno confused
    n "Oh... I see. So that's where you were going with this." with dissolve
    "Nozomi taps her phone against her thigh in what seems to be mild irritation, before she nods her head indignantly."
    show NozomiHypno stern_closed
    n "Alright, we can do that. {w=0.5}{cps=20}Although you should really stop snooping-{/cps}{w=1.0}{nw}" with dissolve
    ks "[hypno3], Nozomi."
    show NozomiHypno drooping sleep
    stop music fadeout 2.0
    n "..." with dissolve
    play music Flow
    "I just had to see if that would work, while she was distracted trying to give me an earful."
    "But anyway, I'd better make this as quick as she wants..."
    ks neutral "That's right, Nozomi. Dropping deep, back into this relaxing state of hypnotic trance."
    ks "And while you're so relaxed, so open to my suggestions, I want you to think about your relationship with the truth."
    ks "Because from the time you wake until the time you hear me snap my fingers, you will be incapable of saying a single true thing."
    ks "No matter what you're asked, you must always lie. The bigger the lie, the better you feel."
    ks "And no matter how big the lie, you will protest that you're telling nothing but the truth. Understand?"
    show NozomiHypno sleeptalk
    n "Yes..." with dissolve
    show NozomiHypno sleep
    "There. We should be able to have a little fun with this before it's time to go." with dissolve
    ks smile "Very good, Nozomi. Now waking up in one, two... three."
    show NozomiHypno sleepy
    stop music fadeout 5.0
    n "Mrrn..." with dissolve
    ks "There we go. Are you doing okay?"
    "Nozomi blinks as she registers my voice, her lower lip trembling hesitantly as she rights herself on the couch."
    play music Sad_Heroine
    show NozomiHypno folded stern_closed
    n "Ahhh... no, actually. I feel terrible." with dissolve
    "That brings a little smirk to my lips, even if I was expecting something like that."
    ks smirk "That a fact?"
    show NozomiHypno angry
    n "O-of COURSE it is! Do you think I actually like being hypnotized all the time?" with dissolve
    ks smile "I mean, kinda?"
    show NozomiHypno annoyed
    n "Honestly. What on earth gave you that idea?" with dissolve
    "Heh. I don't know if she believes that right now. I certainly didn't suggest that she did. But she's certainly making a good case for herself."
    "Now what else can I make her lie about?"
    ks confused "Well this whole hypnotizing each other thing *was* your idea."
    show NozomiHypno stern
    n "No, actually, the only reason we're doing this is because you wanted to hypnotize me!" with dissolve
    "... That's not that far from the truth now that she mentions it."
    "Still a lie, though."
    ks smile "And you're going along with it because you wanted to be hypnotized."
    show NozomiHypno confused
    n "N-no... no, I... just wanted to see where you lived, that's all." with dissolve
    ks "I didn't realize you were that interested in me, Nozomi. I thought you'd rather hang out with those friends of yours?"
    show NozomiHypno stern
    "Nozomi's lips crinkle in thought. Like there's an internal conflict raging in her head between her truth and the lies she's being compelled to tell before inevitably..." with dissolve
    show NozomiHypno annoyed
    n "What friends? I don't have any friends!" with dissolve
    "... Falsehood wins out."
    ks happy "Haha! You could've fooled me with how you're hanging around that pink-haired tennis girl all the time."
    show NozomiHypno angry
    n "Her name is... it's Anastasia Borisova, and she's actually a five-time world chess champion!" with dissolve
    ks smirk "... Wow."
    show NozomiHypno stern_closed
    n "Not that I know her that well, just everybody knows that." with dissolve
    ks "Sure, sure. {w=1.0}Dumb little Hiroko-{w=0.5}{nw}"
    show NozomiHypno stern
    n "{cps=20}Anastasia-{/cps}{nw}" with dissolve
    ks "- plays chess. You're a bit of a board game fan yourself, aren't you?"
    show NozomiHypno stern_closed
    n "Now that is just preposterous. If you knew me at all, you'd know I'm all about... err, fitness." with dissolve
    ks "Fitness."
    show NozomiHypno annoyed
    n "Don't take that mocking tone with me, Kyou! I can bench over three-hundred pounds and run a full marathon without breaking a sweat." with dissolve
    show NozomiHypno angry
    n "I could destroy you!" with dissolve
    "Oh wow, I'm trying so hard to hold back a chuckle. She really is trying to sell the lie by hunching her shoulders and trying to tense her girly arms while she glares at me."
    show NozomiHypno stern_closed
    "I gotta mess with her some more." with dissolve
    ks sigh "Nozomi, you're a girl after my own heart. It's a shame you don't want to date me, huh."
    show NozomiHypno angry blush
    n "W-... What do you mean? Of COURSE I want to date you!" with dissolve
    ks confused "... Really?"
    "N-no, settle down, Kyou. She's a liar, remember?"
    show NozomiHypno smile
    n "Yes, really! You could buy me flowers, take me on a date to a fancy restaurant..." with dissolve
    "This isn't real."
    show NozomiHypno laugh
    n "Gosh, we could tour all the best eateries in town! You know I'm all about fine dining~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    "Which means... she really was telling the truth about not wanting to date me. Huh."
    ks confused blush "I t-thought you said you were all about fitness."
    show NozomiHypno annoyed
    n "Well you heard wrong!" with dissolve
    "Suddenly, this doesn't feel so fun, and besides I should probably wrap this up anyway."
    ks sigh "Okay. [hypno3], Nozomi."
    show NozomiHypno drooping sleep -blush
    stop music fadeout 5.0
    "I probably shouldn't have brought it up..." with dissolve
    show NozomiHypno standing neutral
    with longblink
    queue music Downtown
    "I spent the next couple minutes taking that lying suggestion out of Nozomi head before waking her back up."
    n "Well, Kyou... That was certainly a choice, wasn't it."
    ks sad -blush "You're not mad about that, are you?"
    "She tilts her head a little, as she surely recalls what just happened with a regained sense of clarity."
    show NozomiHypno stern_closed
    n "I suppose I should've expected you to ask me a question like that given the circumstances." with dissolve
    show NozomiHypno neutral
    n "But... no, I guess it turned out okay. At least you know I was telling the truth, right?" with dissolve
    "I force a smile as I ruefully nod my head."
    ks smile "Yeah. Sorry for asking though, I got a little carried away."
    "She nods quietly in return, and I do wonder if she does think less of me for asking."
    show NozomiHypno surprised
    n "You're not the only one! I can't believe I was able to come up with those whoppers I was telling you just now!" with dissolve
    "Even if she does, at least she seems eager to move past it."
    show NozomiHypno drooping sleeptalk
    n "I mean, really. Hiroko a chess champion? Me a fitness freak?" with dissolve
    show NozomiHypno standing sad
    n "God, it doesn't bear thinking about." with dissolve
    ks smile "Heh, yeah. You sure you don't want to hit the gym after this?"
    show NozomiHypno smile_closed
    n "Ehehehe... I don't think that's happening now or ever, Kyou." with dissolve
    "We both share a chuckle before Nozomi pulls out her phone, glances at the time then meets my gaze once more."
    show NozomiHypno smile
    "Looks like our time is up for tonight." with dissolve
    n "So, I think I know what I'm going to do with you tomorrow."
    ks confused "Oh yeah? And what's that?"
    scene bg k room eve
    show Nozomi front smile at center:
        ypos 1.1
        linear 2.0 ypos 1.0
    with blink
    "Nozomi flashes me a grin as she rises from the couch."
    show Nozomi:
        ypos 1.0
    n teasing "Oh. You'll see~" with dissolve
    stop music fadeout 5.0
    scene bg k bedroom eve with longblink
    "What on earth is that girl planning now?"
    play music Past_Sadness
    "I don't know, but it makes me happy thinking she has plans for me."
    "She sure seems to be loosening up around me, seeing how pleased she looked leaving tonight."
    "And man, switching things up like this really was a masterstroke of hers, huh."
    "So... is it far-fetched of me to think she might actually be warming up to me?"
    "Maybe enough that she'll want to be seen around me soon?"
    "... Maybe even consider that \"no dating\" thing despite what she was saying back there?"
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "I could almost see it. Me and her, making that lie become truth."
    "Just so long as we can keep this going..." 
    pause 2.0
    jump Day5_Switch_Safe

label Day4_Switch_UnSafe:
    scene bg street1 day with longdissolve
    "The next morning arrives, and I'm walking to school with only one purpose..."
    # "The next day arrives, and Kyou walks to school with only the coming evening on his mind."
    scene bg classroom day with blink
    play music Bright_Opening
    "... To see this dull day through to the end."
    show Nozomi side smile_side at center
    show Hiroko smile_side at center:
        xpos 0.75    
    h "C'mooon, what're you thinking about?" with dissolve
    "Just as I settle at my desk, I spy Nozomi walking in with Hiroko in tow."
    n happy "Ehehe, I told you it's nothing!" with dissolve
    "And if I were to guess, her head's in the exact same place as mine."
    h uniform_headhold2 annoyed_side "Gonna keep me guessing, huh? You get another one of those games you like so much?" with dissolve
    n  neutral "Well, in a manner of speaking..." with dissolve
    "Our eyes meet for a split second. But she's quick to pull away before I can react."
    n happy "You wouldn't get it~" with dissolve
    h rolleyes "Gawd! I hate when you're like this..." with dissolve
    hide Hiroko
    hide Nozomi
    with dissolve
    "Yeah, she's definitely thinking what I'm thinking."
    play sound schoolbell
    with longblink
    "But the pair of us had to put those thoughts aside and get on with our schoolwork. At least until lunch rolls around."
    show ClassroomLunch boy2_lunch hiroko h_annoyed_sayori n_armup n_smile_left glasses sayori s_neutral_hiroko with blink    
    h "Alright, we getting out of here or what?"
    show ClassroomLunch s_smile_hiroko
    s "Why so eager, Hiroko? I cannot imagine hearing more about English sentence structure worked up an appetite." with dissolve
    "I obviously can't talk to her around her friends, though."
    show ClassroomLunch h_frown_nozomi
    h "It's Nozo. She's holding out on us." with dissolve
    show ClassroomLunch n_neutral_left s_smile_hiroko
    s "Oho, is she now?" with dissolve
    show ClassroomLunch n_sigh
    n "Honestly, Hiroko. You wouldn't be interested." with dissolve
    show ClassroomLunch s_smirk_hiroko
    s "Well now *I* am interested." with dissolve
    scene bg classroom day
    show Hiroko annoyed_side at center, flip:
        xpos 0.25 ypos 1.1
        linear 2.0 ypos 1.0    
    show Nozomi side irritated at center, flip:
        ypos 1.1
        linear 2.0 ypos 1.0
    show Sayori smirk at center:
        xpos 0.75 ypos 1.1
        linear 2.0 ypos 1.0
    with blink
    "Probably shouldn't text her either."
    show Nozomi at flip:
        ypos 1.0
        linear 6.0 xpos 2.0
    show Hiroko at flip:
        ypos 1.0 xpos 0.25
    show Sayori:
        ypos 1.0    
    n "Okay, so in the game there's this global pandemic, so you and three other players have to..."
    show Sayori uniform_handup neutral at flip
    "Those two are obviously gonna be hovering over her the entire lunch break." with dissolve
    s concerned "Wait, we are fussing about a board game?" with dissolve
    hide Nozomi
    hide Hiroko
    hide Sayori
    with dissolve
    "This is going to be the longest lunch break ever..."
    play sound schoolbell
    scene bg classroom eve with longblink
    "Lunch, and the rest of class, proved to be as much of a listless drag as I feared."
    show Nozomi front2 neutral at right
    n "Stand." with dissolve
    "But it's over now."
    n sleep "Bow." with dissolve
    hide Nozomi
    stop music fadeout 5.0
    "All I need to do is get out of this dull place." with dissolve
    scene bg street1 eve with blink
    "Take the direct route home. No distractions, no wasting any more time."
    scene bg k entrance eve with blink
    "Because Nozomi sure isn't going to."
    play sound doorbell
    "She'll definitely want to get us started right away."
    play sound dooropen
    show Nozomi front2 pout at center with dissolve
    play music Downtown
    n "Good evening."
    ks smile "Hey."
    # "And sure enough, Nozomi shows up within minutes, and just as eager to get going again as she said she was during lunch."
    scene bg k room eve
    show Nozomi side neutral_side at center
    with blink
    "And just as I suspected, she's not wasting any time as she quickly pops off her shoes before following me back to the living room."
    scene cg k room eve
    show NozomiHypno standing neutral
    play sound sitting
    with blink
    "But as she settles down on the couch, I can't help but notice how glum she looks."
    ks confused "Uh... is everything okay?"
    show NozomiHypno standing sad
    "Nozomi lets out a weary sigh." with dissolve
    n "Yeah..."
    show NozomiHypno lookup
    n "Just could've done without Hiroko getting on my case about my good mood, that's all." with dissolve
    "Huh. Can't say I didn't notice it earlier, but Nozomi always seemed to tolerate Hiroko being in her face all the time because they're friends or whatever."
    ks confused "Was it really that bad?"
    show NozomiHypno folded stern_closed
    n "Ugh..." with dissolve
    "Maybe they're not as close as I thought they were?"
    show NozomiHypno neutral
    n "... I don't like lying to her. But there are some things she just wouldn't understand." with dissolve
    show NozomiHypno sad
    n "And I wish *she* understood that sometimes." with dissolve
    show NozomiHypno folded stern_closed
    "She lets out a disgruntled little snort, then softly shakes her head." with dissolve
    n "Forget it. I shouldn't be telling you this."
    show penlight at right with moveinright:
        ypos 0.346
    "Well, it's not like I care that much anyway. So I simply shrug as I take my penlight from out of its pocket and smile as if I'd already forgotten what we were talking about."
    show NozomiHypno neutral
    ks smile "Sure. Then do you want to get started?" with dissolve
    scene bg k room eve
    show Nozomi front2 smile at center
    with blink
    "Nozomi's quick to smile in return as she gently takes the penlight from me and rises to her feet."
    n "Oh gosh, yes. You can't imagine how much I've been looking forward to this~"
    scene cg k room reversal
    show NozomiReversal penlight lightoff uniform smile
    with blink
    "And as I take her place on the couch, I now have to ask a question that's been on my mind all day long."
    ks smile "So what are you hoping to try on me tonight?"
    show NozomiReversal neutral
    n "Oh, right..." with dissolve
    "... Wait, was she just going to get into it without so much as a preamble?"
    show NozomiReversal stern
    n "I was thinking that giving me a trance trigger was a good idea. So I though I should start by trying to install one in you as well." with dissolve
    show NozomiReversal smile
    n "What do you think?" with dissolve
    ks smile "Yeah. That does sound reasonable."
    "Although it almost feels like a letdown with how much I've hyped myself up for this."
    ks confused "So you're just going to copy me? I figured you had bigger plans than that."
    show NozomiReversal stern
    n "Oh, I do! And no, I'm not going to just \"copy you\"." with dissolve
    show NozomiReversal lighton
    with flash
    stop music fadeout 5.0
    "And at the moment she ends that sentence, a light crosses my eyes as she flicks on the penlight that's been pointed provocatively at my face this whole time."
    n "Don't worry about it. Just lean back, make yourself comfortable..."
    with flash
    play music Flow fadein 5.0
    n "... and think about the light as it travels across your eyes."
    ks "{cps=15}W-whoa-{/cps}{w=0.5}{nw}"
    show NozomiReversal neutral
    with flash 
    n "Let yourself sink into the couch, and let this light fill your mind just as it fills your vision."
    with flash
    n "Just breathe in, and out..."
    stop music fadeout 5.0
    scene cg k room tv eve
    show NozomiHypno standing uniform2 smile2
    with longflash
    n "-and three. Wide awake now, Kyou."
    "The next thing I know, I'm laying slouched on the couch as she..."
    ks confused "Mmmn... "
    "... Wait, she did it already?!"
    show NozomiHypno folded
    play music Downtown
    "As I lie there blinking, Nozomi tucks the penlight into her palm and folds her arms with a satisfied look on her face." with dissolve
    n "That should do it~ You dropped a little faster there."
    "Wait, what did she do? My thoughts are a little slow coming back, and it takes me a few more seconds before I'm able to recall clearly."
    ks "Oh... so what, you gave me a trigger phrase? Do you think it works?"
    n "Only one way to find out, huh?"
    "I shake my head a little as I try to steel myself for what's coming."
    scene bg k room eve
    show Nozomi front2 smile at center
    with blink
    "Nozomi couldn't resist for even a moment when I used my phrase on her. But maybe I could do a little better? I should try to resist it a little, right?"
    show Nozomi side smile_side
    "But to my surprise, no words come. Instead, she pulls out her phone and starts tapping away on it." with dissolve
    show Nozomi smile
    n "Aaaaand... send." with dissolve
    play sound cellvibrate
    "What the?!"
    show phone at right with moveinright:
        ypos 0.346
    "Almost on instinct I pull out my phone as I felt it quiver in my pocket."
    "{cps=15}Why is she texting me at a time like-{/cps}{nw}"
    stop music
    scene bg blackscreen
    pause 2.0
    scene bg k room eve
    show Nozomi front2 smile at center    
    play sound fingersnap
    with dissolve
    n "Wide awake, Kyou!"
    "My eyes suddenly snap into focus as I find Nozomi looming over me with a big grin on her face."
    play music Eons
    ks confused "W-what the?!"
    show phone at right with moveinright:
        ypos 0.346
    "On reflex I pick up my phone from the couch and glance at the still active screen."
    "{color=93624B}\"Remember the light\"{/color}"
    "... Before I realize what a terrible idea that was."
    ks surprised "Gah!"
    show Nozomi side laugh
    n "Ahahaha! Don't worry, Kyou. I made sure to cover my bases there." with dissolve
    "I glance at Nozomi, then back at my phone and the provocative text."
    n front smile "It should only work the first time you see it." with dissolve
    "So this is what she meant by not copying me."
    n neutral_right "But if I send the text again you should realize it's a new trigger and fall back into trance again." with dissolve
    "She just had to get a little more ambitious with it."
    ks neutral "I see. So that's what you did."    
    hide phone at right with moveoutright
    n side neutral "This is okay, right? I'm not going to use it out of turn so don't worry about that." with dissolve
    "Nozomi looks to me pensively as she says that."
    ks smile "Yeah... Yeah, it's probably okay. I'm just surprised you managed to pull off something like this, that's all."
    "It kinda makes me a little nervous as well, but I think I'm gonna push past it."
    n happy "Hehe, I'm surprising myself too~" with dissolve
    ks "Alright, cool, so we both have trance triggers. Guess I should try something on you now, right?"
    n smile_side blush "Actuallyyy... I need to get going. Sorry." with dissolve
    "Okay... what?"
    ks confused "Seriously? It's barely been half an hour."
    n front2 neutral_right "It, um... it's not been half an hour, Kyou." with dissolve
    show phone at right with moveinright:
        ypos 0.346
    "I shoot her a look, then pull my phone back out of my pocket to check the time because she's gotta be messing with..."
    ks surprised "Guh!"
    "... T-that can't be right?!"
    n chuckle -blush "Ahem. So I'll see you tomorrow, okay?" with dissolve
    hide phone at right with moveoutright
    ks confused "Uh... yeah..."
    stop music fadeout 5.0
    scene bg k bedroom eve with longblink
    "I somewhat awkwardly see Nozomi out and retreat back to my bedroom as I mull things over in my head."
    play music Past_Sadness
    "How has it been nearly two hours? What the hell happened down there?"
    "Like, I've read about how hypnosis can screw with a person's perception of time but this is kind of ridiculous."
    "So what the hell happened? Nozomi only put me under with the penlight, put that trigger in me, then tested the trigger right after."
    "That couldn't have taken long... I guess?"
    "Maybe she was just that meticulous setting the trigger up but... man, that doesn't sit right with me."
    "I don't know what to think about that. Not to mention the fact that I need to come up with something to do with her tomorrow."
    "Yeah, I should probably focus on that for now."
    "And... wait a second, I've got it! I know EXACTLY what I'm gonna try on her!"
    "Was that idea in my head the whole time? It's like a fully-formed plan just popped straight in there."
    stop music fadeout 5.0
    scene bg blackscreen with dissolve
    "Well, I'm not gonna overthink it. This is what I'm going with..."
    pause 2.0
    jump Day5_Switch_UnSafe
label Day4_Con_Kyou_Sayori:
    scene bg street1 day with longdissolve
    "As a new day begins, I walk to school feeling uncertain."
    if hypno3 == "personality":
        if sayori_name == "Sayori":
            play music Memories
            "I did spend a little time researching why my hypnosis could've affected Sayori the way she says it did."
            scene bg classroom day with blink
            "But I pretty much came up empty. I'm still thinking Sayori is in denial over her true feelings for me and her need to take time off for herself."
            show Sayori neutral_right with dissolve
            pause 0.8
            hide Sayori with dissolve
            "Sayori acknowledges me with a brief nod before taking her seat as lessons begin."
            "Sure would love to talk to her more about this instead of reading English lit, but there's just no way."
            scene bg classroom eve with blink
            play sound schoolbell
            "The day passes uneventfully, as me and Sayori can do little more than exchange brief eye contact during our schedules."
            scene bg k room eve
            stop music fadeout 5.0
            show Sayori neutral_right
            with blink
            "When I finally get home, with Sayori following discreetly behind me, it feels like a whole week has passed."
            s "So, did you find anything?"
            ks "Not a thing. You?"
            s neutral "I found nothing conclusive." with dissolve
            "She sighs as she goes on to add:"
            play music Unrest
            s annoyed_right "Only that what you did was highly irresponsible and I hate myself for going along with it." with dissolve
            ks confused "Huh?"
            s uniform_folded "The result of your attempt at recreational hypnosis was to give me a second personality! Do you realize how dangerous that is?" with dissolve
            s irritated "And do you know something else? I took it upon myself to run a little experiment last night." with dissolve
            s neutral "Before climbing into bed, I had every intention of keeping my mind active for a while." with dissolve
            s frown "I also set an alarm on my phone for this morning, plugged it into my earphones and set the volume loud just to make sure I would wake up in time to not be late again." with dissolve
            s annoyed_right "You would think the distraction of wearing earphones alone would stop me from instantly falling asleep." with dissolve
            s concerned_right "But instead my mind blanked and I must have once again found myself immediately entering the land of nod!" with dissolve
            "Huh. So I guess she stayed up all night researching and found a way to deprive herself of a good night's sleep again."
            "At least now I know why she once again looks like death."
            s angry_right "So with that in mind I hope you understand that I am completely TERRIFIED of what is happening to me now!" with dissolve
            "As she eyeballs me fiercely, I realize her entire body is trembling."
            ks "Okay Sayori, but just... calm down, alright?"
            s uniform annoyed_right "Calm?! Kyou, in case you were not paying attention let me stress to you more clearly so you cannot misunderstand." with dissolve
            s angry_right "I am losing control of my own MIND! And it is all your doing!" with dissolve
            s uniform_handup "More to the point, how are you doing these things so... so EASILY?!" with dissolve
            ks "What?"
            s uniform "Kyou, you are an AMATEUR! How is it that you are affecting such drastic changes in my mental state with just two short hypnosis sessions?" with dissolve
            s uniform_folded "Surely the best hypnotists in the world could not do what you have done to me." with dissolve
            "Shit, Sayori is scary when she's angry. I get that she's upset, but I can't deal with her breaking down like this."
            s cry "I just... Why is it that when you put in even a modicum of effort the rewards are substantial." with dissolve
            s uniform "Whereas I have worked and studied day and night for years to reach my goal and I am projected to only JUST scrape into med school." with dissolve
            s angry_right "Do you have ANY idea how much this frustrates me, Kyou? To see you mope and moan and stare over the years and STILL succeed?" with dissolve
            "Oh no, I've let her insult me before but I'm not taking this shit lying down again."
            ks frown "M-Man, where do you get off telling me I have it easy? You... you don't fucking know me! None of you do!"
            s uniform_folded irritated "What else is there to know? Do you imagine yourself a complex figure with unknowable motivations?" with dissolve
            s angry_right "That there is a hidden meaning to you pining pathetically over my friend for nearly three years?" with dissolve
            ks "Shit, why are you bringing that up again? I told you this is nothing to do with Nozomi! I've been trying to help you haven't I?"
            s uniform "H-have you, Kyou? Or was it merely an excuse to do whatever you damn well pleased?" with dissolve
            ks angry "Oh... c-come ON! I HAVE helped! You're not sleeping and it's killing you. Anyone can see that!"
            ks "Maybe what I did isn't perfect, but you needed this, you ungrateful bitch!"
            s scared_right "... I never asked why you thought to study hypnosis in the first place, because I was afraid of something like this." with dissolve
            s scared "But it seemed so... fanciful." with dissolve
            ks frown "... What? Are you even listening to me?"
            s uniform_folded "The very notion that you would take up such a pursuit to make it even easier to get what you want." with dissolve
            "She's just... fucking hysterical now, what do I do?"
            s cry "I should have known better than to see any good in you, Kyou." with dissolve
            menu:
                "Apologize":
                    stop music fadeout 5.0
                    ks surprised "Sayori, uh... look. You're right."
                    ks "I didn't know what I was doing, and I hurt you; I can see that."
                    queue music Monologue
                    ks "I'm... I'm sorry, Sayori. I really did mean to help you, but I guess I didn't know what I was doing after all. I should've been more careful."
                    "Sayori nods her head, sobbing as she draws a breath."
                    s uniform_handup concerned "And... And I apologize for some of the things I said. My sleep-deprivation cannot be helping my mood, to say nothing of my situation, but it is no excuse." with dissolve
                    s concerned_right "Even so, I hope you can appreciate how utterly helpless I feel right now." with dissolve
                    s sleeptalk "Everything I have worked for, you could undo with a few words by bringing out this other person that now resides within me." with dissolve
                    s uniform "And all that I have learned suggests I would not be able to stop you, or her." with dissolve
                    ks sigh "Yeah... yeah, I guess. Thinking you're not in control of your own thoughts is pretty fucking scary."
                    show Sayori uniform concerned_right
                    "Sayori wipes her tired eyes as she sniffs the air." with dissolve
                    stop music fadeout 5.0
                    # ks "So, uhh... do you want me to get rid of that \"[alt_name]\" trigger for you?"
                    s "It seems you still do not quite understand what I am telling you."
                    ks confused "Maybe. I mean, you keep saying you're not in control."
                    ks "I just don't see how anything I did with you could affect you like this unless you were holding onto it yourself."
                    queue music Night_Road
                    s annoyed_right "And that is what we need to correct. I could ask you to undo what you did, and you may do it for me, but I need you to understand how this happened." with dissolve
                    s concerned_right "S-so... although I found nothing in my research, I was thinking that we need to interrogate the one unknown throughout all of this." with dissolve
                    ks neutral "What's that?"
                    s uniform_handup surprised_right "Your penlight. You said it was your own invention?" with dissolve
                    ks "Yeah. I put it together in a few months on and off."
                    s neutral_right "And what did you say it does again?" with dissolve
                    ks "I just designed it to catch people's attention and help them fall into trance. Why?"
                    s annoyed_right "It is just that I cannot help thinking about my reaction to it, in your own words." with dissolve
                    s uniform_folded "About how I \"gasped in awe\", or somesuch." with dissolve
                    ks confused "Yeah, that's right."
                    s neutral_right "The light is certainly distracting. I felt like I wanted to focus on nothing else, although it is hard to remember exactly." with dissolve
                    ks neutral "Yeah. It's pretty common for people not to remember large parts of their trances, even if no one tells them to forget."
                    s annoyed "That is a problem. If we could measure my brain activity during my exposure to the light, that could be helpful. But we have no way of accessing such." with dissolve
                    s annoyed_right "Not to mention that my previous exposure to it would compromise our findings." with dissolve
                    # s alert_surprised_right "What if you specifically told me to remember every aspect of the trance?"
                    s uniform_handup neutral_right "Perhaps I could use the light on you and gauge your reaction?" with dissolve
                    ks sigh "Uh... I dunno, is that such a good idea?"
                    ks "I'm the hypnotist here; I feel like I need to be lucid for this."
                    "Sayori frowns at my excuse."
                    s uniform_folded annoyed_right "I feel you just don't want to have done to you what you have done to me... but perhaps you have a point." with dissolve
                    s neutral "There is something else we could do, but..." with dissolve
                    ks neutral "But what?"
                    s concerned "I feel uncomfortable with involving her, for several reasons." with dissolve
                    ks "Involving her? What are you thinking of?"
                    s uniform_handup neutral_right "I am thinking to involve Nozomi in these shenanigans. She may have some time to help us, and I have a feeling she will be open-minded about being hypnotized." with dissolve
                    ks surprised "N-Nozomi?! Really? You really think she'll do this for us?" with vpunch
                    show Sayori rolleyes
                    "Sayori sighs and rolls her eyes. Seems she's already regretting that she mentioned Nozomi around me..." with dissolve
                    s "Do not get too excited. She would be there for me, not you, and I am not certain she would agree. But I will see if I can convince her."
                    s neutral_right "If she does, perhaps when you entrance her you can impress the importance of remembering every detail. Could you do that?" with dissolve
                    ks frown "Y-yeah, I think so."
                    stop music fadeout 5.0
                    s uniform "Good. Then we will meet in my club room tomorrow, hopefully with Nozomi in tow." with dissolve
                    ks smile "Okay. That's a plan at least."
                    s neutral "Indeed. Now, I need to go. Cram school awaits." with dissolve
                    show Sayori sleep
                    "Sayori closes her eyes and takes a long breath, before trudging over towards the door." with dissolve
                    s "I will see you tomorrow..."
                    scene bg blackscreen with longdissolve
                    pause 2.0
                    jump Day5_Con_Kyou_Sayori
                "Bring [alt_name] back":
                    ks frown "Sayori, that's enough!"
                    "I can't... I can't handle this."
                    s scared_right "{cps=15}Y-you... no, don't you dare-{/cps}{w=0.5}{nw}" with dissolve
                    ks "Become [alt_name]."
                    s uniform "Nng..." with dissolve
                    "I could see, from that momentary expression of wild panic in her eyes that she knew what I was about to say."
                    show Sayori surprised_right
                    ks confused "You're [alt_name] now... right?" with dissolve
                    "But it doesn't seem to matter. Even now, it doesn't matter."
                    $sayori_name = "[alt_name]"
                    s uniform_handup "Y-yes, of course I am. But... Kyou?" with dissolve
                    "Just those two words is all it takes to bring all that shit she was talking; the tears, the hysterics, all of it... to an abrupt end."
                    ks "Yeah?"
                    s uniform_folded concerned_right "Why am I... s-shaking like this? I feel so tense and... teary?" with dissolve
                    "I don't exactly feel the best about that, but at least things are starting to calm down around here."
                    "All I need to do is put the particulars out of my head for now, and reassure Sayori... no, \"[alt_name]\", that everything's fine."
                    ks smile "It's okay, [alt_name]. I hypnotized you again just now, and you're a little disoriented. That's all it is."
                    s surprised_right "Really?" with dissolve
                    ks "Really. Maybe it's best if we lay off the hypnosis for now, at least until you're feeling better."
                    show Sayori uniform_handup happy
                    "Sayori, now fully embracing her light-hearted side, puts a hand to her chest and lets out a hearty giggle as she nods in agreement." with dissolve
                    s "I am beginning to feel better already, but... yes, perhaps that would be for the best."
                    s smile_right "Although I am just dying to know what sort of mental trickery you played upon me this time. Were you attempting something ambitious?" with dissolve
                    ks "Yeah... you could say that."
                    "Convincing Sayori to take on a new persona certainly does feel wild as hell. Even more so that it seems to be working."
                    s happy "Mhmhmhm come now, don't get coy with me~" with dissolve
                    "So could I... leave her like this? Just let her out of here thinking happy thoughts for tonight?"
                    ks "Ahhh, well it's..."
                    "Would that be so bad? After all the stress she's put herself under it might do her some good."
                    s frown "Oh... wait, hold that thought." with dissolve
                    "But just then that happy facade fades as a frown creases her features."
                    ks confused "What's wrong?"
                    show Sayori uniform sleeptalk_concerned
                    "At first I fear she's already about to drop the act. But something about Sayori's theatrical sigh makes me think this is not about our fight at all." with dissolve
                    s "Haaah... I need to attend cram school, much as I so badly wish that were not the case."
                    ks "Oh... right."
                    s uniform_folded rolleyes "Perhaps if I hadn't already skipped class this morning I would be tempted to try my luck." with dissolve
                    "... Wait a minute."
                    ks confused "Wasn't that..."
                    s smile_right "Well, it was nice while it lasted. We'll have to do this again!" with dissolve
                    "Didn't she \"skip class\" yesterday?"
                    ks "Uh... yeah."
                    "I don't know if I want to press her on that."
                    s happy "Have a good evening, Kyou!" with dissolve
                    "And besides, she's already strapped for time so I probably shouldn't keep her."
                    ks smile "You too."
                    hide Sayori
                    "But still, if she really is confused about what day it is then... what does that mean?" with dissolve
                    stop music fadeout 5.0
                    scene bg k bedroom eve with longblink
                    "... I probably shouldn't worry so much."
                    "I mean... if Sayori really, *really* wants to she'll snap back to her regular self a little later."
                    "Sayori can rant and rave about \"second personalities\" and not being able to resist a simple hypnotic suggestion, but she has to know she's just overthinking it."
                    "She just needed an excuse to chill out about this. But tomorrow we can try this conversation again when we both have clearer heads."
                    scene bg blackscreen with longdissolve
                    "Maybe then she won't be so damned dramatic..."
                    $ ending = "altered"
                    pause 2.0
                    jump Epilogue_Con_Kyou_Sayori                    
        else:
            queue music Memories
            "Even if she seemed happy, I do have to wonder if I should've sent [altname]- er, Sayori, away in her altered state."
            "That's not something a stage hypnotist does, is it?"
            scene bg school ext day with blink
            "Still, keeping a big suggestion like that is gonna take some effort on Sayori's part to maintain, so I'm sure she dropped it before she showed up for cram school."
            "{cps=15}I'll have to ask how she feels when I- {w=0.5}{/cps}{nw}"
            scene SayoriGreeting laugh
            $sayori_name = "Sayori"
            s "Kyouuu!" with vpunch
            ks surprised "Wh-whoa!"
            "... When I next see her, holy shit!"
            show SayoriGreeting cheerful
            s "Good morning, Kyou! Did I scare you?" with dissolve
            "And wow, I am not used to girls approaching me voluntarily let alone jumping out from behind the school gates to surprise me."
            # "Was she seriously hiding by the gates so she could jump out at me?"
            "That's really cute, especially coming from someone like her."
            ks smile "Ehh, a little maybe. Good morning, Sayori."
            "It's a nice feeling to start the day with, knowing someone's actually happy to see me around here."
            if Alter1 == True:  #AltSayori takes this opportunity to mention she believes Sayori is the alter that Kyou failed to instill in her yesterday, since
                                #she didn't have the chance to mention this important plot point yesterday and I kinda need it for the rest of the story to make sense
                show SayoriGreeting neutral
                s uniform_folded alert_rolleyes "... Sayori? Now where have I heard that name before?" with dissolve
                ks surprised "Huh? What do you mean? You're..."
                show SayoriGreeting cheerful
                s uniform_handup alert_concerned_right "Oh, I remember! You called me \"Sayori\" yesterday, too." with dissolve
                ks confused "{cps=15}W-well, yeah because it's- {/cps}{w=0.5}{nw}"
                show SayoriGreeting laugh
                s alert_surprised_right "The name of the \"happy and carefree\" girl! It HAS to be!" with dissolve
                "S-seriously?! She still thinks she's [alt_name]?" with vpunch
                show SayoriGreeting smile
                $sayori_name = alt_name
                s alert_smile "I had assumed yesterday that you had simply confused me with someone else when you called me by that name." with dissolve
                "And what's more..."
                s "But in fact you have been trying to invoke the suggestion you gave me while I was under hypnosis."
                "She has things completely backwards!"
                show SayoriGreeting laugh
                s alert_laugh "Ahaha, but you need to give it up, Kyou! It's clearly not going to work." with dissolve
                ks "Y... y-yeah, I guess not."
                "How long is she going to go on thinking this is who she really is?"
            else:
                show SayoriGreeting laugh
                s alert_laugh "Ahahaha, give it up, Kyou. You know that's not going to work." with dissolve
                ks confused "It's... not? Wait, what isn't?"
                $sayori_name = alt_name
                show SayoriGreeting cheerful
                s alert_giggle "Calling me \"Sayori\" again. I can see what you're doing, you know!" with dissolve
                "S-seriously?! She still thinks she's [alt_name]?" with vpunch
            show SayoriGreeting neutral
            s uniform_folded alert_neutral "Also, you should realize how highly unethical it would be if you actually triggered a post-hypnotic state within me in an unagreed-upon public place such as this." with dissolve
            show SayoriGreeting smile blush
            s alert_smile_right blush "But... I will forgive you. Just this once." with dissolve
            $persistent.sayori_greeting_unlock = True
            scene bg classroom day with blink
            play sound schoolbell
            "I just can't believe she hasn't dropped that suggestion yet."
            "Does this mean she was way more willing to accept it than she let on?"
            "As I look over to where Sayori is sitting by the window, it doesn't seem like she's in any discomfort as homeroom starts."
            with blink
            "... Shit, what if someone else calls her Sayori?"
            "She thinks I'm trying to trigger her, but what if her friends say it? Or a teacher? What's she gonna think about that?"
            "I can't do anything until we're excused for lunch but even so..."
            with blink
            play sound schoolbell
            show Sayori alert_smile at center:
                xpos 0.75
            show Hiroko smile_side at center, flip:
                xpos 0.25
            show Nozomi front smile at center
            with dissolve
            "I gotta wade into her friends circle again just to talk to her."
            h uniform_armup happy uniform_arm "All right! Let's get out of here and head to the rooftop!" with dissolve
            ks frown "A-Ah... excuse me?"
            show Nozomi surprised
            show Sayori alert_surprised_right
            h angry vein "YOU AGAIN!?" with vpunch
            ks "O-ow!"
            show Sayori alert_neutral
            n side frown_side "Hiroko, I get that he's annoying, but do you think you might be overdoing it?" with dissolve
            h annoyed_side novein "What? No, it's the way you gotta be around these assholes if you want them to leave you alone." with dissolve
            show Hiroko annoyed
            show Nozomi neutral
            show Sayori alert_neutral_right
            ks "Look, I don't want to... uh, I mean..." with dissolve
            "Fuck, they've completely thrown me off."
            n frown "We're leaving now, Kyou." with dissolve
            "Not knowing how else to approach this, I point at Sayori and hope for the best."
            ks "Can I talk to you for a moment?"
            show Hiroko surprised
            show Sayori alert_neutral_right
            n front surprised "Wait, what?" with dissolve
            ks "Yeah, it's for a school project. I wanted to ask a few things."
            "Now it seems it's their turn to be thrown off as they exchange looks with each other, then with Sayori, who starts to smile."
            show Hiroko uniform_headhold2 neutral_side
            show Nozomi neutral_right
            s uniform_handup alert_happy "Mhmhmhm, I think I know what this is about. You two go on ahead~" with dissolve
            h confused_side "Oh... kay?" with dissolve
            show Nozomi side at flip
            n smile_side "Alright. We'll see you up there, Sayori." with dissolve
            hide Nozomi
            hide Hiroko
            show Sayori uniform alert_panicked_right
            "Shit. I was hoping to avoid that." with dissolve
            show Sayori:
                linear 1.0 xpos 0.5
            s "What did she call me?"
            show Sayori:
                xpos 0.5
            "I gotta think fast."
            ks "Uh, [altname[0]]- [alt_name], about that..."
            s alert_surprised_right "Yes?" with dissolve
            menu:
                "\"It's a prank\"":
                    ks confused "There... may be a little prank going on about you around the school."
                    s uniform_folded "A prank?" with dissolve
                    "Is this the best I've got?"
                    ks "Y-yeah. Don't ask me why, but I guess some people thought it hilarious to call you Sayori."
                    ks "Th-that's why I picked it as the name of the other personality I was trying to hypnotize you into yesterday? That I guess... didn't work?"
                    s uniform_handup "Huh..." with dissolve
                    "Ugh, like she's gonna buy this stupid ass lie."
                    s uniform_folded alert_laugh "Ahahaha, that is rather ridiculous." with dissolve
                    "I notice a couple of our classmates wheel round from their desks, startled at the unfamiliar sound of Sayori's giggling."
                    s alert_happy "Well, it sounds strange to me, but I don't care all that much. Let them call me \"Sayori\" if it amuses them." with dissolve
                    "I breathe out a little sigh. Seems Sayori's newfound carefree look on life has prevented her from interrogating the absurdity for now."
                    "But surely she'll have to take it seriously if she realizes the whole world knows her only as Sayori. This lie is only gonna last a day at most."
                    s uniform alert_smile_right "Now, you wanted to talk to me?" with dissolve
                    ks smile "Oh, uh, yeah."
                    "I mean, that just now was what I wanted to talk to her about, so..."
                    ks "Oh right, when did you want to come over today? Are you doing your study club thing, or..."
                    s alert_annoyed "Ugh... I will try to duck out of it. It is of no use to me anyway." with dissolve
                    ks neutral "It's not?"
                    s uniform_folded alert_annoyed_right "Not really. I mostly find myself helping the others, and although it is nice to assist it's so tiring and stupid to study when we are in school so much anyway." with dissolve
                    s alert_irritated "So I may quit." with dissolve
                    ks surprised "Quit the club? Aren't you the president?"
                    s alert_rolleyes "I am. I have no idea why I thought to start that ridiculous club in the first place." with dissolve
                    "That she's even entertaining the thought of quitting her study group is pretty intense."
                    "I'm sure she wouldn't seriously go ahead with it but still, I should cool her off on the idea before she makes life harder for herself when she comes to her senses."
                    show Sayori alert_neutral_right
                    ks smile "W-well, don't do anything too hasty, [alt_name]." with dissolve
                    ks "I mean, when I think about it, it's pretty cool how you committed to studying for your future even though... e-even though you hate it so much."
                    show Sayori alert_smile blush
                    "\"[alt_name]\" averts her gaze with a blush." with dissolve
                    "Not gonna lie, I really like that I have this effect on her."
                    s uniform_handup "Y... you really think so, Kyou? But it's so pointless." with dissolve
                    ks "I-it's not pointless, [alt_name]! I mean, maybe you took it too far but don't just quit."
                    show Sayori alert_smile_right
                    # ks "And... a-and besides, I really admire you that you've been so dedicated to it for all this time."
                    ks "You know all this hard work you're doing's gonna pay off when we get out of here." with dissolve
                    ks "And... a-and I meant what I said. I really do admire you for your dedication to your studies Sayor-, I mean, [alt_name]."
                    show Sayori alert_happy
                    "I could've sworn I heard a little squee come out of her as she mulls over what I just said." with dissolve
                    s alert_giggle uniform "I may allow myself to be convinced~" with dissolve
                    ks "J-just don't do anything now that you might regret, that's all I'm saying."
                    s alert_smile_right "Of course." with dissolve
                    s alert_smile "Now... I should take my leave before my friends wonder about what we're doing." with dissolve
                    s uniform_folded "But we should... we should chat more often, Kyou." with dissolve
                    hide Sayori
                    "She scurries away before I can reply, but the smile she had while she was talking to me never left her face." with dissolve
                    "And shit, I must be grinning like a lunatic right now."
                    "Taking a deep breath to clear my head, I'm for once grateful that people don't normally pay attention to me."
                    scene bg classroom eve with longblink
                    "The memory of \"[alt_name]\"'s face stays with me all afternoon. I mean, how could it not?"
                    "I've never had a girl look at me like that before."
                    "And it's been so long since a girl talked to me in a way that felt anything other than pure contempt..."
                    play sound schoolbell
                    show Nozomi front2 at right
                    n "Stand!" with dissolve
                    n "Bow!"
                    hide Nozomi
                    "So as the school day comes to a close and everyone rises from their seats I look to [alt_name] again from across the room, hoping to catch her gaze." with dissolve
                    show Sayori alert_neutral at center, flip
                    "I keep my eyes on her as she makes her way past me towards the exit, hoping she'll notice..." with dissolve
                    s alert_surprised_right "...{w=1.0}{nw}" with dissolve
                    show Sayori alert_smile_right
                    "And as our eyes meet, she smiles and my heart's pounding joyously once more." with dissolve
                    show Sayori alert_surprised
                    show Hiroko laugh_side uniform_armup at center:
                        xpos 0.75
                    h "Man, I dunno what's gotten into you today, Sayori, but whatever it is I want some of it~" with dissolve
                    s uniform_folded alert_laugh "Life! That's all it is~" with dissolve
                    h smile_side uniform "Heh. Well, you stay perky and I'm gonna go to practice. Catch ya later~" with dissolve
                    s alert_smile "Have fun." with dissolve
                    hide Hiroko
                    s alert_smile_right "... {w=1.0}{nw}" with dissolve
                    hide Sayori
                    "[alt_name] spares me another glance before taking her own leave." with dissolve
                    stop music fadeout 10.0
                    scene bg street1 eve with blink
                    "She'll make her excuses at her club, then hurry on over to me as soon as she can."
                    "And then we can work on a routine for my hypnosis show at the culture festival!"
                    "I mean, I wasn't sure about going through with it before, but if [alt_name]'s on board, then..."
                    "Or maybe we can do more than that..."
                    scene bg k room eve with blink
                    "Ugh, no I can't think about that yet. At least not while she's living under her post-hypnotic suggestion."
                    "... Shit, that's right. Somehow I almost forgot that she's not really \"[alt_name]\"."
                    "In all my excitement, that detail got really easy to overlook."
                    play sound doorbell
                    "But that's her at the door already. She REALLY must've wanted to get out of study club tonight; I've barely gotten home myself."
                    play sound dooropen
                    scene bg k entrance eve with blink
                    play music Inspiration fadein 5.0
                    show Sayori alert_happy with dissolve
                    s "Ahh, it feels so good to be out of there~"
                    play sound doorclose
                    "I chuckle as I close the door behind her while she pops her shoes off."
                    s alert_smile_right "I mean, I took your point about not quitting, but just to be able to do this once in a while." with dissolve
                    s alert_giggle "To be able to shirk my responsibilities!" with dissolve
                    s uniform_handup alert_laugh "Ahhh, it is so liberating~" with dissolve
                    ks smile "I... guess it must be after waiting so long to do it, heh."
                    scene bg k room eve
                    show Sayori uniform_handup alert_laugh
                    with blink
                    "[alt_name] giggles in the affirmative as she skips into my living room."
                    s alert_giggle uniform_folded "So what shall we do, Kyou? I have several hours of freedom and I have no intention of wasting them." with dissolve
                    ks "W-well... I was thinking we could try something for the hypnosis show like we talked about."
                    s alert_laugh "Oh, of course!" with dissolve
                    "But as I mention that, there's something else I remember."
                    scene cg k room eve
                    show SayoriHypno standing alert_happy
                    with blink
                    "As she goes to sit on my couch, I recall the little lie I told her about \"Sayori\" being a joke name for her."
                    show SayoriHypno alert_smile
                    s alert_smile_right "So Kyou, did you come up with any ideas?" with dissolve
                    "And that if we wanted to continue this between us I'd have to deal with that somehow."
                    "Otherwise reality will force her out of her \"[alt_name]\" bubble whether she likes it or not."
                    ks confused "U-uh, well... can I ask you something first?"
                    show SayoriHypno alert_happy
                    s alert_happy "Ask away~" with dissolve
                    "I mean, I could put a stop to this and force Sayori out of her bubble myself, but..."
                    ks "Are you... are you okay?"
                    show SayoriHypno alert_surprised
                    s alert_surprised_right "Uh... yes? Why would I not be?" with dissolve
                    "... she's held onto this suggestion for an entire day now, all on her own."
                    ks neutral "So, like... I dunno, you're not feeling like you've forgotten anything or that something weird is going on?"
                    show SayoriHypno alert_happy blush
                    s uniform alert_smile blush "I... n-no, nothing weird is going on with me. Absolutely not!" with dissolve
                    "And come on, I only have to look at her to see she how comfortable she is to keep hold of it."
                    show SayoriHypno alert_laugh
                    s "What gave you that idea?" with dissolve
                    "And I know I'm enjoying the hell out of seeing her like this."
                    "So why not make sure we can keep it going together?"
                    menu:
                        "Yeah, keep it going":
                            ks smile "I, uh... I just wanted to check, that's all. After the hypnosis session we did yesterday."
                            show SayoriHypno alert_smile noblush
                            s alert_smile_right noblush "Oh, when you were trying to put that other person in my mind." with dissolve
                            ks "That's... right, yeah. Sayori."
                            show SayoriHypno alert_stern
                            s alert_rolleyes "Well, I have been getting some strange comments today, besides the silly name prank everyone's been doing." with dissolve
                            s "It is like they are always surprised to see me so \"chipper\" and \"full of energy\"."
                            show SayoriHypno alert_happy
                            s alert_smile_right "But I have been sleeping so much better thanks to you, Kyou. That must be what they're referring to." with dissolve
                            ks "Yeah. Still though, even though it didn't work, there might be some of \"Sayori\" in your head."
                            ks "So I think I should put you under again and make sure hearing her name isn't messing with you in some way."
                            show SayoriHypno alert_smile
                            s alert_happy uniform_folded "That makes sense!" with dissolve
                            $scg = Character("%s"%sayori_name, image = "SayoriHypno", who_color = "#385599")
                            stop music fadeout 30.0
                            show penlight at right with moveinright:
                                ypos 0.346
                            "[alt_name] smiles as I take the penlight from my pocket and click it on in front of her."
                            ks smile "Great. So can you look up for me, please?"
                            hide penlight at right with moveoutright
                            show SayoriHypno alert_looking with dissolve
                            call cglightshow from _call_cglightshow_32
                            "[alt_name] happily complies as I pass the penlight's beam gently across her eyesight."
                            ks "You're so responsive now, [alt_name]. It's like your eyes immediately jump to the light."
                            s "Ehehe... Well, it is very nice to look at, Kyou~"
                            call cglightshow from _call_cglightshow_33
                            ks "Yes it is. And the more you look, the more natural it is to continue looking, [alt_name]."
                            call cglightshow from _call_cglightshow_34
                            ks "And the more natural it becomes to look, the easier it feels to accept how heavy your eyelids become from looking."
                            call cglightshow from _call_cglightshow_35
                            ks "But there's no need to think about any of that, [alt_name]. No need to think at all."
                            call cglightshow from _call_cglightshow_36
                            ks "All you need to do is stare, and what naturally will happen, will happen."
                            call cglightshow from _call_cglightshow_37
                            show SayoriHypno alert_drowsytalk
                            $ renpy.transition(longdissolve, layer="master")
                            ks "Just how all that tension and pent-up energy is flowing out of your relaxed body."
                            call cglightshow from _call_cglightshow_38
                            ks "Naturally feeling it seep out of your loose, limp limbs as your eyes become heavier still."
                            call cglightshow from _call_cglightshow_39
                            show SayoriHypno alert_drowsy
                            ks "Heavier still, [alt_name]. Much as you still want to stare at the light..." with dissolve
                            play music Flow fadein 15.0
                            call cglightshow from _call_cglightshow_40
                            ks "You may now find it impossible to keep those heavy eyelids of yours from closing completely."
                            call cglightshow from _call_cglightshow_41
                            show SayoriHypno standing alert_sleep
                            ks "Eyelids completely closed as you drift asleep, [alt_name]... That's right." with dissolve
                            show SayoriHypno drooping alert_sleep
                            $ renpy.transition(longdissolve, layer="master")
                            "So... if I've hypnotized her as [alt_name], then I guess any suggestions I give her will work on [alt_name] only, unless I tell her otherwise."
                            "I'm gonna try and make sure [alt_name] won't get tripped up by any references to her real name anymore."
                            ks "Drifting back into that nice, deep state of trance. Everything else fading into the background leaving only my voice."
                            ks "Isn't that right, [alt_name]?"
                            scg alert_sleeptalk "Right..." with dissolve
                            show SayoriHypno alert_sleep
                            ks "So right and natural, [alt_name]. And now it's just my voice, you'll be able to fully concentrate and absorb my words and accept them completely." with dissolve
                            ks "Which is why when I say to you that every time you see or hear your name as \"Sayori\", what you consciously see or hear will in fact be \"[alt_name]\"..."
                            ks "... it will be completely true that you will only consciously see or hear \"[alt_name]\" whenever you are referred to as \"Sayori\"."
                            ks "It will simply not occur to your conscious mind that you could be called by any other name, so of course they mean \"[alt_name]\"."
                            "... Although subconsciously she'll still know the difference, is the unspoken implication I'm going for here."
                            ks "Do you understand and accept what I have said, [alt_name]?"
                            "So even now if I said to her \"Become Sayori\" she'd still realize the real Sayori needs to come back."
                            scg alert_sleeptalk "Yes... understand and accept..." with dissolve
                            show SayoriHypno alert_sleep
                            ks "Furthermore, whenever you need to refer to yourself in speech or in writing, and there are others besides me you're addressing..." with dissolve
                            ks "... you will unconsciously use the name \"Sayori\" instead of your own. Understand, [alt_name]?"
                            scg alert_sleeptalk "I understand..." with dissolve
                            show SayoriHypno alert_sleep
                            "Perfect. She's been so good at absorbing my suggestions so far, I have no doubt that'll stop [alt_name] getting confused over her other personality." with dissolve
                            "I mean, her real personality."
                            ks "That's great, [alt_name]. It's so natural to process and accept these truths as automatically as breathing."
                            ks "So now we're going to wake you back up, counting up to three, upon which you'll awaken happy and refreshed once more."
                            stop music fadeout 5.0
                            ks "Counting up now... one, taking a nice deep rousing breath..."
                            ks "Two, letting the energy flow back into your waking body..."
                            ks "And three, wide-awake and refreshed, [alt_name]."
                            show SayoriHypno standing alert_drowsytalk
                            $ renpy.transition(longdissolve, layer="master")
                            "Within moments [alt_name] is testing her eyes as she sits back up straight on the couch."
                            scg alert_smile "Mmm, that still feels nice~" with dissolve
                            queue music Inspiration
                            "Smiling back at her, I think to check how she's adapted to my suggestions immediately."
                            ks "Welcome back, Sayori. Hopefully that takes care of things."
                            scg alert_happy "Mhmhm, if there was anything to take care of~" with dissolve
                            "She chirps back at me without missing a beat. So far so good."
                            scg alert_smile "But Kyou, I really need to get something off my chest before we do anything else." with dissolve
                            ks "Oh? What's that?"
                            stop music fadeout 10.0
                            "[alt_name] draws a breath, apparently steeling herself for a moment before continuing."
                            scg alert_sleep "It is just... when you asked if there was anything \"weird\" going on with me, I was not completely honest with you." with dissolve
                            scg blush "I... have a confession to make." with dissolve
                            ks surprised "Huh?"
                            "Wait, what's she talking about?"
                            scg "Ever since we started talking like this, I have felt a flutter in my chest that I have never felt before."
                            scg drooping alert_sleeptalk "At... at first I was not sure what to make of it. It really did seem to come out of nowhere." with dissolve
                            "Oh... oh shit, I get it."
                            queue music Warm_Romantic fadein 15.0
                            scg standing alert_smile "But Kyou, I am a mature woman. It may have confused me at first, but I'm not afraid of what I feel." with dissolve
                            scg "And what I feel is..."
                            "She's..."
                            scg alert_laugh "I... I like you, Kyou Koyama!" with dissolve
                            "She's seriously going all the way with this!"
                            "The crush I told her to have... she took it so much to heart that she's seriously confessing!"
                            "I don't believe this!"
                            ks "U-uh, I like you too Say- I mean... [alt_name]."
                            ks "I mean... {w=1.0}{nw}"
                            scene bg k room eve
                            show Sayori alert_laugh blush at center:
                                ypos 1.2
                                linear 2.0 ypos 1.0
                            with blink
                            "Just then, [alt_name] lets out a squeal of delight and jumps off the couch."
                            show Sayori:
                                ypos 1.0
                            s "Ahaha, I knew it! You feel it too, don't you?"
                            s alert_giggle "And is it not exhilarating to air our feelings like this?" with dissolve
                            s uniform_handup "To let them be free without a care?" with dissolve
                            "Remember, Kyou, Sayori's just playing out her alter ego in her head, just like you wanted her to."
                            ks smile blush "Y-... yeah. Feels great."
                            show Sayori uniform_folded alert_happy
                            "As she hugs herself deliriously, I have to keep telling myself not to get too excited about this development." with dissolve
                            "She's just taking full advantage of her post-hypnotic suggestion to blow off steam, after denying herself the pleasure for so long."
                            s alert_laugh "Ahaha, I have never felt so alive, Kyou!" with dissolve
                            "After all these years of studiousness, she must have realized how much she truly needed the opportunity."
                            "But she's gonna snap out of it or back off before this gets TOO hot."
                            s alert_smile_right "..." with dissolve
                            ks surprised "S-Sayori, what are you- {w=1.0}{nw}"
                            scene cg sayori x kyou
                            show Sayori x Kyou surprised
                            with blink
                            "Oblivious to my protests, Sayori closes the distance between us and raises her hands to cup my face before planting a full kiss upon my quivering lips."
                            s "Mmmn..."
                            "Her slender fingers caress my cheeks as her lips tenderly press against my own."
                            "My own lips respond almost automatically, delighting in the affection."
                            show Sayori x Kyou relaxed
                            $ renpy.transition(longdissolve, layer="master")
                            "She... she feels so much softer than I imagined."
                            "I guess she's not snapping out of it after all..."
                            "... Maybe that's okay."
                            $persistent.sayori_x_kyou_unlock = True
                            scene bg k room eve
                            show Sayori alert_smile_right blush at center
                            with blink
                            "And as she gently pulls away from me with a giggle, I don't think I want to snap out of this either."
                            ks smile blush "D- does this mean what I think it means?"
                            $sayori_name = "Sayori"
                            s uniform_handup alert_laugh "Ahaha, why don't you tell me what this means, Kyou?" with dissolve
                            "I swallow hard as I dare to say it."
                            ks "It... it means you're my girlfriend now!"
                            "That sounded so embarrassing to say out loud."
                            "But for her part, Sayori just grins and rewards me with a playful smooch."
                            s alert_giggle "Heehee! Top marks to you~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
                            "This... this is too much."
                            ks "S-s-so, what do you want to do now?"
                            "I've had a girlfriend for all of twenty seconds and it already feels like I'm fucking this up."
                            show Sayori alert_smile_right
                            "I should be taking charge of this situation, but..." with dissolve
                            "But I've never done this before. It's not my fault..."
                            show Sayori uniform
                            "But rather than berate me, Sayori just grabs both my hands with hers and smiles." with dissolve
                            s "There is no need to do anything right now, Kyou."
                            s alert_smile "This is... new for me as well." with dissolve
                            s alert_annoyed "And my time is running out until I need to leave for cram school again, much as I would rather spend the night here with you." with dissolve
                            s alert_smile_right "But we will work something out together. And soon~" with dissolve
                            s alert_happy "Okay?" with dissolve
                            "My cheeks feel like they're on fire. Nevermind what's going on downstairs."
                            "It's all I can do to nod at her."
                            stop music fadeout 10.0
                            ks "O-okay."
                            scene bg k bedroom night with blink
                            "I saw Sayori off soon after."
                            "The moment she left, I had to wonder if I'd just had some kind of intense dream."
                            "But even now I can still feel her on my lips. And just thinking about it is making me giddy all over again."
                            "Sayori really showed how interested she was in me, huh."
                            "I mean... okay, you could say \"[alt_name]\" was the one who kissed me, but I know that behind all that, Sayori is always in control."
                            "It's like I've always known: You can't make people do what they don't want under hypnosis."
                            "So how much does it matter that I'm dating \"[alt_name]\" and not Sayori?"
                            "Aren't they basically one and the same?"
                            show bg blackscreen
                            $ renpy.transition(longdissolve, layer="master")
                            "Maybe we're both living a dream right now. One neither of us want to wake up from..."
                            "And if that's the case... why not keep dreaming?"
                            pause 2.0
                            jump Day5_Con_Kyou_Sayori_Alter
                        "I really need to check with \"Sayori\" first":
                            ks smile "Oh, it's nothing. I just want to be sure you're okay after the hypnosis session we did yesterday."
                            show SayoriHypno alert_smile -blush
                            "Yeah. Tempting as it is to keep this going, we should have a real talk about the past day now that we're back home." with dissolve
                            show SayoriHypno alert_happy
                            s "Ah, when you attempted to place that other person in my mind!" with dissolve
                            "And as much as she seems to enjoy acting out this cutesy persona, it'd be proper to make sure she's in her right mind for this conversation."
                            show SayoriHypno alert_smile
                            ks "That's... right, yeah. So with that said, I need you to become Sayori again." with dissolve
                            stop music fadeout 5.0
                            show SayoriHypno alert_surprised
                            "The instant I speak the words, her eyelids seem to violently flicker for a brief moment as her jaw slackens." with dissolve
                            s "A... ahh..."
                            ks "Just for a little while, okay?"
                            show SayoriHypno alert_looking
                            "And then..." with dissolve
                            queue music Eons
                            $sayori_name = "Sayori"
                            if Alter1 == True:
                                "((AUTHOR'S NOTE: With Kyou having switched Sayori back and forth earlier, the last thing Sayori remembers is the conversation they had in his bedroom.))"
                                "((This will call for a different script, with an appropriately different reaction from Sayori. ))"
                                "(( But until that's written we're going to continue the story as if this is the first time Sayori's been her regular self since he first invoked the \"become [alt_name]\" trigger.))"
                            #Place the below under the else state once the above variation is written
                            s "... My apologies. Could you repeat that for me, please?"
                            "Her sunny disposition completely vanishes as Sayori adjusts to resemble her usual self once more."
                            ks "Like I said, I just want to be sure you're in your right mind for this."
                            show SayoriHypno alert_drowsytalk
                            "But man, she looks completely lost right now." with dissolve
                            s "My right mind? What do you mean by that?"
                            ks "{cps=20}Er, you know? After our hypnosis session yesterday when we-{/cps}{w=1.5}{nw}"
                            show SayoriHypno alert_surprised
                            s "Yesterday?" with dissolve
                            "And somehow looking more lost by the moment."
                            show SayoriHypno alert_drowsy
                            s "Would it not be pertinent to discuss the session we just concluded?" with dissolve
                            ks confused "Huh?"
                            "This is starting to concern me."
                            show SayoriHypno alert_stern
                            s "To say nothing of the fact that, if you had any concerns over my well-being you should not have proposed this frivolity, let alone gone through with it." with dissolve
                            "And now it feels like I'm the one who's lost, as Sayori stiffens in her seat and starts to regard me coldly all of a sudden."
                            ks "Uh, well..."
                            "I'm beginning to miss [alt_name] already."
                            ks confused "All I said was your trigger phrase, Sayori. I don't think that counts as a \"session\"."
                            show SayoriHypno alert_surprised
                            stop music fadeout 5.0
                            s "... \"Trigger phrase\"?" with dissolve
                            ks "Uh, you know? The phrases I'm using to switch your personalities back and forth?"
                            show SayoriHypno alert_neutral
                            s "I understand what you mean, Kyou. But I did not presume that you had invoked it upon me already." with dissolve
                            "Wait, she doesn't even know I said it to her? Like, at all?"
                            ks "Oh. W-well..."
                            "I'd thought that she'd at least have some awareness of what she was doing while she was acting under suggestion."
                            show SayoriHypno alert_stern
                            s "So tell me Kyou, what is it that you wanted me to tell you?" with dissolve
                            "But could it be that she really doesn't remember anything since..."
                            ks "Sayori... what day is it today?"
                            show SayoriHypno alert_neutral
                            play music Measured
                            s "Wednesday. Why?" with dissolve
                            "Since..."
                            show SayoriHypno alert_looking
                            s "Kyou, your expression is beginning to trouble me. Is something wrong?" with dissolve
                            # s "Kyou, you are starting to scare me. Is something wrong?" with dissolve
                            "Since the moment she became [alt_name]?!"
                            show SayoriHypno alert_stern
                            s "What is going on, Kyou? Out with it." with dissolve
                            ks surprised "I..."
                            "As I struggle to give her an answer, Sayori shoots me a curious look as she suddenly reaches to lift her phone from out of her blazer pocket before switching it on..."
                            ks "{cps=20}N-now Sayori, I can explain- {/cps}{w=1.0}{nw}"
                            show SayoriHypno alert_surprised
                            s "Th-this is..." with dissolve
                            ks "Don't freak out, okay?"
                            scene bg k room eve
                            show Sayori uniform_handup alert_surprised_right at center:
                                ypos 1.1
                                linear 2.0 ypos 1.0
                            with blink
                            "But my words seemingly go unheard as Sayori suddenly jumps to her feet, her widened eyes still fixed on her phone screen."
                            s "Thursday? Why does it say Thursday?"
                            ks surprised "Hey, just calm down, alright? I'm sure there's a good expanation for all of this!"
                            s alert_surprised "First the deep sleep, and now this?" with dissolve
                            ks "Sayori, please listen!"
                            s uniform_folded "What am I supposed to conclude from this? That you tampered with my phone while I was too hypnotized to notice? Or that you have shifted my perception of the time somehow?" with dissolve
                            s alert_sleep "I do not recall agreeing to such a thing." with dissolve
                            ks "Uh, no it's not that! It's..."
                            s alert_annoyed_right "Oh, do tell me. What \"good\" explanation could you possibly have for me?" with dissolve
                            "... It's no good. Under her hardened gaze I know no explanation I can give will calm her."
                            "I knew she was uncomfortable about what we were doing when I started all this."
                            # "I knew it wasn't right to let her leave the house thinking she was the person I selfishly constructed for my own amusement."
                            show Sayori uniform_handup
                            "So for her to have no memory of her time as \"[alt_name]\" and waking up now? A whole day later?" with dissolve
                            # "And it sure wasn't right to let her go on living her life as \"[alt_name]\", living an entire day thinking she was some happy, carefree girl with a crush." with dissolve
                            # "And it sure wasn't right to let her go on living her life as \"[alt_name]\" for an entire day, talking to her family and friends and classmates like she was some happy, carefree girl with a crush." with dissolve
                            # "Whether I believed she was content to let it play out or not, I should have done something about it well before now."
                            "What can I even say to calm her now? I could have all the time in the world and still come up with nothing."
                            show Sayori alert_concerned_right
                            "And in my silence, I can see Sayori taking another look at her phone, then at me, as the colour begins to drain from her face." with dissolve
                            s uniform "Kyou... I-I am leaving now." with dissolve
                            s alert_scared_right "Do not try and stop me." with dissolve
                            scene bg blackscreen with longdissolve
                            stop music fadeout 5.0
                            "There's no good explanation for any of this..."
                            pause 2.0
                            $sayori_hurt = True
                            jump Day5_Con_Kyou_Sayori_Alter_Switch
                            jump Credits
                    "To be continued..."
                    jump Credits
                "Switch her back":
                    "This is starting to get out of hand."
                    "Sayori really has immersed herself into the part of becoming this \"[alt_name]\" that I created for her, and I'm thrilled that she's absorbed my suggestion so completely."
                    s alert_concerned_right "So do you know why Nozomi is addressing me by such a name?" with dissolve
                    "But what's going to happen if she starts correcting people for calling her Sayori? Or starts blowing off her studies because she's gotten so deep into her new character?"
                    ks neutral "Um... w-well..."
                    stop music fadeout 5.0
                    "As fun as this is has been, I know I gotta put my foot down here."
                    "So I..."
                    ks "... You need to become Sayori now."
                    "I have to put a stop to this."
                    s alert_sleepy "W-what did you... hm?" with dissolve
                    "As I speak the words, I watch as her eyes flicker, and they start to scan left and right with a sudden awareness."
                    s uniform_handup "W-where..." with dissolve
                    $sayori_name = "Sayori"
                    s alert_surprised "... Where am I?" with dissolve
                    ks confused "{cps=15}Sayori? Do you really not know- {/cps}{w=1.0}{nw}"
                    s uniform alert_panicked "WE ARE IN CLASS?!" with vpunch
                    queue music Measured
                    "She gasps loudly, with a voice that rattles our assorted classmates who had settled in their desks for lunch."
                    ks "U-uhhh, Sayori? People are..."
                    s alert_panicked_right "People? But your room? We were just in your room..." with dissolve
                    ks surprised "{cps=15}Everyone's looking at us, Sayori-{/cps}{w=0.5}{nw}"
                    scene SayoriGrab sayori1 scared
                    s uniform_handup alert_angry_right "WHAT IS THIS TRICKERY!? ANSWER ME!" with shake
                    "She grabs me by the lapel of my uniform jacket as she gets right in my face, her eyes wild and... goddamn, I gotta calm this down fast."
                    k "H-hey come on, settle down. Yeah, we're in class so you gotta... just relax, okay?"
                    s "{cps=10}I... {w=1.0}{/cps}{nw}"
                    show SayoriGrab sayori2
                    $ renpy.transition(longdissolve, layer="master")
                    extend "y-you..."
                    show SayoriGrab sad
                    "Sayori's eyes lock with mine for a moment before they start to move again, finally registering the fact our classmates are staring and gossiping at the scene she's making." with dissolve
                    s "H-haah... n-nevermind, it's... it is nothing. Everyone, go back to what you were doing."
                    $persistent.sayori_grab_unlock = True
                    scene bg classroom day
                    show Sayori uniform_handup alert_surprised at center
                    with blink
                    "She shudders, and her grip loosens on my uniform while she looks back and forth at the assembled onlookers with their worried faces; their currently unattended lunchboxes at their desks." with dissolve
                    ks confused "C'mon, it's fine... everything's fine, see? Nothing to worry about."
                    s "{size=16}So it is lunchtime?{/size}"
                    "Is she even listening to me now?"
                    ks "Yeah, it's the start of lunchbreak. Like I said, nothing to worry about."
                    show Sayori uniform alert_sleeptalk
                    "At least she seems to have stopped freaking out as she slowly backs away from me..." with dissolve
                    s alert_concerned_right "You... I am going to join my friends now a-and you..." with dissolve
                    s alert_scared_right "Y-you... need to stay away from me. Do you understand?" with dissolve
                    hide Sayori
                    play sound runningshoes
                    ks surprised "What? Sayori, wait up!" with dissolve
                    stop music fadeout 10.0
                    "But Sayori just turns on her heel and flees the classroom without looking back."
                    "I don't chase her. Instead, I slump back down at my desk, let out a sigh I've been holding and I just..."
                    "Man, I can't wrap my head around what fucking happened just now."
                    "The moment I spoke the words to flip her back to normal, it's like she had no awareness of her time acting as \"[alt_name]\" at all."
                    "It really did feel like she had become a whole different person, with separate memories and everything."
                    "But that's... that's impossible! How in the world did she internalize my suggestions as much as that?"
                    "Dammit Sayori, I need to know more. I need to talk to you again."
                    "You can't just run away from me like this..."
                    with longblink
                    play sound schoolbell
                    queue music Eons
                    "The lunch period comes and goes, and Sayori returned to her desk without making eye contact."
                    "We're supposed to be reviewing some lesson material for our upcoming exams, but I can't concentrate on any of that."
                    "I'm kinda freaking out a bit."
                    "Hypnosis can't force someone to do things they don't want to do. I know that. Pretty much everything I read on it confirmed that."
                    "But even so, I've also read how it can lower a person's inhibitions. Convince them to maybe go a little further than they meant to."
                    scene cg k room eve:
                        matrixcolor SaturationMatrix(0)
                    show SayoriHypno drooping alert_sleep:
                        matrixcolor SaturationMatrix(0)
                    with blink
                    "Sayori was nervous about this whole deal, but she went along with it for my sake."
                    "And yeah, she did come around to it in a big way, more than she ever thought she would."
                    "But it was supposed to be just a little trick for my hypnosis show. And a trick is supposed to end when the show's over."
                    "I REALLY should've told her to go back to normal before I let her leave last night."
                    play sound schoolbell
                    scene bg classroom eve
                    show Nozomi front2 at right
                    with blink
                    n "Stand!" with dissolve
                    n "Bow!"
                    hide Nozomi
                    "But no, I just had to see how far she'd go, didn't I? I just had to know how good of a hypnotist I was." with dissolve
                    "I'm a fucking idiot. I wasn't thinking about her comfort at all."
                    show Nozomi side neutral_side at center, flip:
                        xpos 0.25
                    show Sayori uniform_folded alert_concerned at center
                    s "Nozomi? Do you have a moment to talk?" with dissolve
                    "What am I going to do? The school day's over, and I feel nothing but tension between me and Sayori."
                    n smile_side "Oh, sure, Sayori. What's up?" with dissolve
                    "She's right there, but she hasn't acknowledged me even once this afternoon."
                    s uniform_handup alert_sleeptalk "Well, it is just... w-well..." with dissolve
                    "I could go say something?"
                    n sad_side "Um... Should we take this someplace else?" with dissolve
                    "... No, I'd better leave her be. At least for now."
                    scene bg street1 eve with blink
                    "I was only going to make it worse anyway."
                    "She just... she just needs some time to clear her head. Work out how she feels."
                    "Maybe talking to a friend like Nozomi will help calm her down?"
                    scene bg k bedroom eve with blink
                    stop music fadeout 5.0
                    "Heading back home, I slump down on my bed as my head continues to spin."
                    queue music Past_Sadness
                    "Because yeah, maybe I shouldn't have done something with Sayori that I knew she wasn't fully on board with."
                    "Maybe I should've ensured she was fine before letting her leave the house last night..."
                    "... Or maybe I shouldn't have ruined it by telling the real Sayori to come back when she seemed to be enjoying herself as \"[alt_name]\"?"
                    "Seriously, how was I supposed to know she'd take to a suggestion like that so completely? Does that kind of thing even happen?"
                    show penlight at right with moveinright:
                        ypos 0.346
                    "How was I supposed to know she'd react so strongly to this little light I have in my hand?"
                    "I need answers, and the only person who can give them doesn't want to come near me."
                    stop music fadeout 5.0
                    "What am I supposed to do?"
                    scene bg blackscreen with longdissolve
                    jump Day5_Con_Kyou_Sayori_Alter_Switch
    elif hypno3 == "doll":
        play music Memories
        scene bg classroom day with blink
        show Sayori neutral_right with dissolve
        pause 0.8
        hide Sayori with dissolve
        "Sayori acknowledges me with a brief nod before taking her seat as lessons begin."
        "Sure would love to talk to her more instead of reading English lit, but there's just no way."
        with blink
        play sound schoolbell
        "As the clock grinds its way to lunchtime, I look across the room as Sayori gets up and joins her friends."
        show Nozomi side smile_side at center, flip:
            xpos 0.25
        show Sayori smile at center, flip:
            xpos 0.5
        show Hiroko happy uniform_armup at center:
            xpos 0.75
        with dissolve
        h "All right! Time to get out of here and head to the rooftop!"
        s smirk "Have fun up there, Hiroko." with dissolve
        h frown_side "What's {nw}" with dissolve
        extend "THAT supposed to mean?" with vpunch
        n neutral_side "You're not coming?" with dissolve
        s sleeptalk "Not today, my friends." with dissolve
        h irritated "Nuh-uh, we gotta get you some sun in you, {w=0.2}{nw}" with dissolve
        extend "STAT!" with vpunch
        show Hiroko uniform neutral_side
        s uniform_folded smile "Hiroko, I appreciate what you do for me, but today I simply must insist. You two go on without me." with dissolve
        n smile_side "Come on, Hiroko. Let's go next door and see if Risa will join us." with dissolve
        h smile_side "'Kay." with dissolve
        n laugh "See you in a bit, Sayori~" with dissolve
        hide Nozomi
        hide Hiroko
        s happy "See you." with dissolve
        show Sayori neutral_right
        "As her friends leave, I spy Sayori slowly pulling her lunchbox and utensils out from her bag and walking across to my desk." with dissolve
        scene SayoriLunch neutral with blink
        "She then takes a seat at an empty desk beside me, and pops the lunchbox open as our eyes meet."
        s "I trust you don't mind."
        ks frown "N-no, of course not!"
        show SayoriLunch sleep
        "Sayori nods, but I can't stop looking at her." with dissolve
        "It's something I couldn't help but notice since this morning."
        show SayoriLunch annoyed
        s frown_right "... What?" with dissolve
        ks sigh "U-uh, well... did you get enough sleep last night?"
        show SayoriLunch irritated
        "Sayori sighs, her right arm frozen in place as her hand hovers over her food." with dissolve
        "Kinda takes me back to our time together last night."
        s "That is what I wished to talk about."
        ks surprised "Yeah? So the sleep hypnosis wore off?"
        "She lets out another sigh, before looking to me with a pensive expression."
        show SayoriLunch concerned
        s uniform concerned_right "No, Kyou, the sleep hypnosis did not wear off." with dissolve
        "I'm confused, and I can only wait for her to continue as she fusses with the food in her lunchbox."
        show SayoriLunch concerned_side
        s concerned "Although I had no time to do any further research on hypnosis, I took it upon myself to run an experiment last night." with dissolve
        ks neutral "What do you mean?"
        show SayoriLunch neutral
        s neutral "I wished to test the effects of your post-hypnotic suggestion upon an unwilling mind." with dissolve
        show SayoriLunch puzzled
        s neutral_right "Do you remember? How I asked if I would be able to negate the effect should I need to?" with dissolve
        ks "Uh, yeah, I remember."
        show SayoriLunch sleep
        "There's another pause, as she draws a little yawn out of her mouth before weakly pushing a piece of chicken in there." with dissolve
        s "..."
        ks frown "Uhh, Sayori?"
        show SayoriLunch sleepy
        s sleepy "Hm? Oh, I apologize. I am not used to talking so much during lunch." with dissolve
        "... We've barely even started. But knowing what I know about her, I'm sure she uses this part of the day to nap as well."
        "Why does she even bother spending lunch with her friends then?"
        show SayoriLunch neutral
        s sleeptalk "But as I was saying, I sought to test the effects of your hypnosis against a deliberate attempt to resist it." with dissolve
        ks smirk "From the look of you, I guess you succeeded."
        show SayoriLunch annoyed
        s annoyed_right "..." with dissolve
        ks neutral "... What?"
        show SayoriLunch neutral
        s annoyed "So I stayed up until my usual time, and as I settled for bed I mentally prepared myself to remain awake." with dissolve
        show SayoriLunch sleep
        s uniform_folded "I also set an alarm on my phone for this morning and turned up the volume to ensure I would awaken in time to not be late again." with dissolve
        show SayoriLunch annoyed
        s annoyed_right "And do you know what happened, Kyou?" with dissolve
        s "Despite the distractions I wrought upon my mind, the only thing I remember upon resting my head on my pillow was the sound of my phone alarm this morning."
        ks frown "You really don't remember anything else?"
        show SayoriLunch sleepy
        "Sayori bows her head and shakes it quietly as she pokes at her lunch." with dissolve
        s "I do not. So what do you think this tells us?"
        show SayoriLunch concerned
        s concerned "Because by my understanding it appears I am as helpless to stop the numbing of my mind as I was to free my arm last night." with dissolve
        show SayoriLunch concerned_side
        s uniform neutral_right "I have been unable to explain to myself why that is... But perhaps you have some thoughts you would like to share with me?" with dissolve
        ks frown "Hmm..."
        "Seriously, all I can think of is how she managed to lifehack her way out of a good night's sleep again."
        ks sigh "I mean... your body wants what it wants, doesn't it? You must've been exhausted again, so are you really that surprised you fell asleep?"
        show SayoriLunch annoyed
        s annoyed_right "And? Were you not listening? I had made a conscious effort to remain awake at the time." with dissolve
        "A \"conscious effort\" she says..."
        show SayoriLunch irritated
        s irritated "Besides, it is not as if my body was predisposed to shutting down in the first place. That is why we are having this conversation at all." with dissolve
        ks smirk "But that's the thing isn't it? We can't just think about your conscious desires here."
        show SayoriLunch annoyed
        s annoyed_right "What on earth do you mean by that?" with dissolve
        ks "What I mean is... your conscious mind might be saying \"stay awake\", but subconsciously? That's a different story."
        ks "Subconsciously you still wanted to shut down, and that's exactly what you did."
        show SayoriLunch puzzled
        s uniform_folded concerned_right "So... you are saying my subconscious desire was able to override my conscious will?" with dissolve
        show SayoriLunch concerned
        s sleepy "Does this not contradict what you told me yesterday? That hypnosis cannot force me into doing something I do not wish to do?" with dissolve
        show SayoriLunch sleepy
        s sleeptalk_concerned "This makes so little sense to me..." with dissolve
        show SayoriLunch concerned_side
        "Sayori frowns with concern, having given up trying to eat anything for the moment." with dissolve
        ks smile "I mean... okay, I get why it's confusing. But it sounds to me like that's what happened, and there's nothing unusual about it."
        show SayoriLunch puzzled
        s surprised_right "There isn't?" with dissolve
        "I smile and nod at her, hoping I can come off as reassuring again."
        ks "Yeah! When you think about it, it's no different to what happened to you the night before."
        show SayoriLunch neutral
        ks "After we trained your subconscious with that hypnosis session it just got easier for your subconscious to take over and get you to sleep like you should." with dissolve
        ks "Not to mention, our subconscious overrides our conscious will all the time. It's just that usually we don't even notice it's happening."
        show SayoriLunch puzzled
        s neutral "Still though... The very idea that after our short hypnosis session the other day, for it to effect such a change in my subconscious..." with dissolve
        ks smile "Seriously, don't worry about it. If anything, I'd be excited about how well my subconscious takes to helpful suggestions if I were you."
        show SayoriLunch concerned
        s uniform concerned "Ah, of course... my supposed high level of hypnotic suggestibility that you were talking about." with dissolve
        ks "Right. And wouldn't it be fun to find out what else we can do with that while helping me practice?"
        "I look down at her mostly untouched lunchbox, then grin at her."
        show SayoriLunch neutral
        ks smirk "Hey, maybe we can get you to eat properly. And after you were telling me your diet was fine..." with dissolve
        show SayoriLunch rolleyes
        "Sayori scoffs indignantly, then tiredly picks up another bite of food." with dissolve
        s "Mmpth. I do not exactly share your enthusiasm, Kyou. I am not finding being subject to phenomena I don't understand especially pleasant."
        show SayoriLunch irritated
        s neutral "So thank you for your input, but I will continue to research this in my own time." with dissolve
        ks sigh "Do you even have any time, Sayori?"
        $persistent.sayori_lunch_unlock = True
        scene bg classroom day
        show Sayori uniform_folded rolleyes at center, flip:
            ypos 1.1
            linear 2.0 ypos 1.0
        with blink
        "Sayori rolls her eyes at my kneejerk reaction as she picks up her barely-touched lunchbox and rises from her borrowed desk."
        show Sayori at flip:
            ypos 1.0
        s frown_right "I will be in touch..." with dissolve
        stop music fadeout 5.0
        hide Sayori with dissolve
        "And with that she retreats back to her own desk, pillowing her arms on its surface as she sits before lowering her head to rest upon them."
        "Guess that lunch is going uneaten, huh."
        scene bg classroom eve with blink
        play music Downtown
        "But seriously. The culture fest's in a little over three weeks, and we'll have to declare our participation soon."
        "If I really want to see this through... If I really want to make use of my skill and my penlight, I need to step it up."
        scene bg corridor eve with blink
        "But I can't do this on my own. And as I file out of the classroom after another long day I can't stop thinking about it."
        show Sayori neutral with dissolve
        "I need her..."
        ks surprised "O-oof!" with vpunch
        hide Sayori with dissolve
        h "Quit blocking the door, dumbass!" with dissolve
        show Hiroko uniform_armup irritated
        "I'm suddenly stumbling forward as I'm shoved from behind by a pair of malicious, tiny hands." with dissolve
        h uniform angry "Jesus..." with dissolve
        hide Hiroko
        stop music fadeout 5.0
        "Sayori's disappeared by the time pinkie pushes past me. No doubt she's continuing her hard-nosed study regimen without missing a beat." with dissolve
        scene bg k bedroom eve
        with blink
        "Meanwhile, I follow my own routine as I head straight home."
        "My own routine? And what is that exactly?"
        play music Past_Sadness
        "There's nothing to do... Nothing I want to do anyway."
        show phone at right with moveinright:
            ypos 0.346
        "Well, I kind of want to call Sayori right now. Or at least message her something."
        "But what would I say? \"When can you help me again?\""
        "\"Why are you pushing yourself so hard?\""
        "... \"Are you doing okay?\""
        hide phone at right with moveoutright
        "Ugh. I better put my phone away before I do something to annoy her."
        "Maybe I should take a leaf out of her book and take my studies more seriously. That's why I went to her study club in the first place after all."
        stop music fadeout 5.0
        "Our studies come first, as she'd say..."
        jump Day5_Con_Kyou_Sayori

    label Day4_Con_Kyou_Hiroko:
        scene bg street1 day with longdissolve
        "As a new day begins, I walk to school feeling uncertain."
        "The hypnosis study, the penlight, I did all of it for Nozomi."
        scene bg school ext day with blink
        if hypno3 == "stuck":
            "And yet..."
            show Hiroko
            h "Kyou..." with dissolve
            ks "Hiroko."
            hide Hiroko
            "Somehow I've wound up thinking constantly about Hiroko." with dissolve
            play music Bright_Opening
            scene bg classroom day with blink
            "It's pretty wild now, when I think about it."
            "I know I didn't want to waste all my time researching hypnosis and stuff after Nozomi blew me off again."
            "But out of everybody..."
            show Hiroko neutral_side at center
            show Nozomi side sad_side at center, flip:
                xpos 0.25
            n "You're looking a little glum today, Hiroko." with dissolve
            h frown_side "Y- yeah? What about it?" with dissolve
            "Why go out of my way for Hiroko?"
            n "Just something I noticed, that's all. If you want to talk about it- {w=0.8}{nw}"
            h "I don't."
            n sad_closed "... Alright, then." with dissolve
            h uniform_headhold nervous_side "*sigh* Sorry. I'm just stressing over the tourney an' shit, I'll be fine." with dissolve
            scene bg k room eve with blink
            stop music fadeout 5.0
            "I still haven't thought of a good answer to that."
            play sound doorbell
            "I'm only half-surprised when the doorbell rings."
            play sound dooropen
            show Hiroko tennis
            "Hiroko hadn't told me she'd be running over from her tennis club to see me again, but I kind of expected her all the same." with dissolve
            play sound doorclose
            h "Hey, weird question."
            ks "What?"
            h neutral_side "Where's your folks?" with dissolve
            ks frown "Oh... they're divorced. It's just me and my dad here, and he's out of the house most of the time."
            h "Ah, okay... was just wondering 'bout that on the way here."
            h sleep "Anyway..." with dissolve
            ks neutral "Yeah, how'd your tennis go?"
            show Hiroko tennis_armup smirk
            "She grins." with dissolve
            play music Downtown
            h "Great! None of those scrubs at my club can touch me."
            h angry "Now they're gonna {nw}" with dissolve
            extend "HAVE to take me seriously." with vpunch
            ks "Who?"
            h frown "Ugh, never mind." with dissolve
            ks smile "Well, It's pretty cool that my post-hypnotic suggestions are still working to keep you calm and focused during your games."
            h shocked "It's fuckin' {nw}" with dissolve
            extend "INCREDIBLE!" with vpunch
            h surprised "Does it wear off?" with dissolve
            ks neutral "It might. I mean, we only did one session for each. It wouldn't surprise me if it needed reinforcing at some point."
            h tennis_headhold2 neutral_side "Yeah. Yeah, that makes sense..." with dissolve
            scene cg k room eve
            show HirokoHypno upright tennis frown
            $h = DynamicCharacter("hiroko_name", image = "HirokoHypno", who_color = "#FF89AB") #Hiroko Homura
            with blink
            "Hiroko frowns as she plops down on the couch."
            h sleeptalk "One thing I don't get." with dissolve
            ks "What's that?"
            h surprised "Why doesn't {nw}" with dissolve
            extend "EVERY sportsperson have a hypnotist on call?" with vpunch
            h frown "Why aren't there, like, sports hypnotists?" with dissolve
            ks frown "I... think there are?"
            h neutral "Yeah but, like, you don't hear about 'em. It's weird." with dissolve
            ks smile "I guess... Like I said, you're not the only one who's been helped by it, but it's pretty wild how much you've improved."
            h sleep "Mmn. Coach said I was like a totally different person when I stepped on the court." with dissolve
            ks "I don't think there's any doubt that you're an excellent hypnotic subject, Hiroko."
            ks "Not just with your tennis, but last night as well."
            h sad "Yeah... I thought it was all stupid bullshit, but I gotta admit it works." with dissolve
            "And I dare to bring it up:"
            ks "And it's great that we're getting on now, isn't it?"
            h angry blush "D-Don't push your luck. I'm only doing this stuff 'cuz it helps me." with dissolve
            ks neutral "No other reason?"
            h frown "Nope. We're using each other and that's it." with dissolve
            "Okay. If that's how she wants to play it, I won't push it for now."
            ks "So then, are you ready to try something else?"
            h neutral "Uh, like what?" with dissolve
            ks "Something a little more... challenging, I think. After the last thing worked so great."
            h clenched_fists_tennis angry "NO perverted shit!" with vpunch
            ks angry "Geez, Hiroko, I KNOW!"
            "I sigh and pinch the bridge of my nose as I try to think."
            ks frown "Okay, how about we..."
            menu:
                "Make you think you're a cat":
                    $hypno6 = "cat"
                    ks neutral "Yeah... I was wondering how you'd take to being a cat?"
                    h nofists frown noblush "Is this like, that bit the other dude did? Making animal noises 'n' shit?" with dissolve
                    ks "Yeah, but we could take it a little bit further. Try and make you think you really ARE a cat for a while?"
                    h "How's that gonna... {w=0.8}{nw}"
                    $ renpy.transition(dissolve, layer="master")
                    extend annoyed_up "ugh, nevermind."
                    ks "What?"
                    h frown "You'll probably pull it off somehow. But you know what? This is it. Two thingies is enough for a lil' hypno show, yeah?" with dissolve
                    ks "Yeah, okay. I'm not gonna push you any further than this."
                    h sleeptalk "'Kay. We try this, you help me through my tourney this weekend and I do the culture fest with you and we're even." with dissolve
                    ks "Okay..."
                    "I really thought we had more than this going on, but alright. If this is seriously how she wants to play it for now..."
                    show penlight at right with moveinright:
                        ypos 0.346
                    show HirokoHypno neutral
                    "So I take out the penlight once more." with dissolve
                    ks "Alright then, Hiroko. So once again I want you to look into the light..."
                    hide penlight with moveoutright
                    show HirokoHypno annoyed_up
                    with dissolve
                    call cglightshow from _call_cglightshow_129
                    "I once again shine the light in her eyes."
                    ks "That's right. Looking and relaxing so naturally."
                    call cglightshow from _call_cglightshow_130
                    ks "It must be an impulsive reaction now, for you to relax and drop deeply under this light, Hiroko."
                    call cglightshow from _call_cglightshow_131
                    ks "So natural and correct now, to simply let every bit of tension drain from your body as you stare."
                    call cglightshow from _call_cglightshow_132
                    ks "So automatically feeling your eyelids droop... that's right."
                    stop music fadeout 10.0
                    call cglightshow from _call_cglightshow_133
                    show HirokoHypno relaxed sleepy_up_closed
                    $ renpy.transition(longdissolve, layer="master")
                    ks "We both know how good you are at dropping under the light, after all. So very good at dropping, relaxing, drifting deeper..."
                    call cglightshow from _call_cglightshow_134
                    ks "That's exactly right, Hiroko. Eyes completely closing as you go deeper..."
                    show HirokoHypno sleep
                    ks "And sleep." with dissolve
                    play music Flow
                    h drooping "..." with longdissolve
                    "She didn't even complain that time. Just looked and dropped in double-quick time."
                    ks "Deeply asleep, Hiroko. Only my voice needs to remain in your head."
                    ks "So now, as we know how wonderful you are at visualizing the things I put to you... I want you to visualize what it would be like to be a cat."
                    ks "How a cat would move. How it would think. How it would act."
                    ks "Can you do that for me, Hiroko?"
                    h sleeptalk "Y... yeah..." with dissolve
                    show HirokoHypno sleep
                    ks smile "Of course you can. So now, I want you to take that visualization just a little further... so that you believe you really are a cat." with dissolve
                    h "..."
                    ks "Because you really are a cat, Hiroko. You will think like a cat and act like a cat. And as soon as you awaken you will fully embrace this reality."
                    ks "Do you understand, Hiroko?"
                    h sleeptalk "Understand..." with dissolve
                    show HirokoHypno sleep
                    ks "That's great, Hiroko. That's so great. So now, as I count up to three, you will awaken feeling refreshed and accepting what you are." with dissolve
                    ks "And what are you, Hiroko?"
                    h sleeptalk "A cat..." with dissolve
                    show HirokoHypno sleep
                    ks "Yes you are. I'm going to count up now..." with dissolve
                    stop music fadeout 5.0
                    ks "One, feeling the strength returning to your limbs..."
                    ks "Two, taking a nice breath and letting your eyelids open..."
                    show HirokoHypno relaxed sleepy_up_open
                    $ renpy.transition(longdissolve, layer="master")
                    ks "And three, Hiroko. Wide awake."
                    h neutral "..." with dissolve
                    "I give her a moment as her eyes regain their focus, before I see them swivel slightly, taking in their surroundings."
                    ks "Hiroko? Talk to me?"
                    h surprised "Meow?" with dissolve
                    ks "How are you feeling?"
                    # play music Moment
                    play music Beautiful
                    scene bg k room eve
                    $h = DynamicCharacter("hiroko_name", image = "Hiroko", who_color = "#FF89AB") #Hiroko Homura
                    show Hiroko tennis surprised_side at center:
                        ypos 1.5
                        linear 2.0 ypos 1.3
                    with blink
                    "Hiroko just ignores me as she hops down off the couch, landing on her hands while planting her knees on the floor." with dissolve
                    show Hiroko:
                        ypos 1.3
                    "I can't help but laugh as she obliviously crawls around the living room, sniffing the air as she explores."
                    ks smile "Haha, here, kitty!"
                    h neutral "..." with dissolve
                    ks "Here, girl!"
                    show Hiroko:
                        linear 1.5 xpos -0.1
                    "She pads away from me, seemingly content to ignore me."
                    "Yeah, that seems like a cat brain to me."
                    show Hiroko:
                        xpos -0.1
                    "But having her just wander around is no fun. I want to see if I can play with her."
                    show penlight at right with moveinright:
                        ypos 0.346
                    "And my penlight just gave me an idea. Maybe it'll work well enough for this..."
                    hide penlight with moveoutright
                    "Switching it back on, I walk behind Hiroko's crouched form and shine the beam on the floor in front of her."
                    show Hiroko surprised_side at flip:
                        linear 1.0 xpos 0.3
                    "It's enough to make her stop in her tracks, then suddenly pounce the ground."
                    show Hiroko at flip:
                        xpos 0.3
                    "Now I've gotten her attention, I wave the light beam around a little and watch as she stalks it, her eyes and head tracking the light rigidly."
                    show Hiroko at flip:
                        linear 1.0 xpos 0.5
                    "She crawls along the ground, taking an occasional swipe at the light with her pawed hands whenever I let her get close, only to then point the penlight at the couch..."
                    scene Hiroko Cat2 light1 with blink
                    h "HSSS!"
                    show Hiroko Cat2 hiroko1 annoyed
                    play sound sitting
                    "With only a moment's pause, she leaps back onto the couch in pursuit and vainly cups her hands over the light as it shines on the couch cushion." with dissolve
                    ks happy "Haha, what's the matter, kitty? Can't you catch it?"
                    h "MRROAAW!"
                    show Hiroko Cat2 surprised light2
                    "After waving the light over the couch a few times to confuse her more, I bring it back down to the floor, and watch as she inevitably hops down to take a swipe at it." with dissolve
                    play sound sitting
                    show Hiroko Cat2 hiroko2 angry
                    h "RRREEEEOOOWWW!" with dissolve
                    hide Hiroko Cat2
                    show Hiroko Cat2 hiroko2 angry
                    "There, I think I'd better switch the light off before I wear her out too much." with dissolve
                    show Hiroko Cat2 curious
                    stop music fadeout 5.0
                    "And as I look down at her pawing the ground where she last saw it, I really start to regret lacking the foresight to buy one of those cat ear headbands." with dissolve
                    h "Mew?"
                    "Maybe I can get some for the show..."
                    queue music Eons
                    "But as I shake that thought from my mind for now, I realize she's staring up at me from the floor."
                    $persistent.hiroko_cat_2_unlock = True
                    scene cg k room ground eve
                    show Hiroko Cat happy
                    with blink
                    "Seeing her like this, looking up at me with such an innocent wide-eyed expression... damn, that's so fucking adorable."
                    h "Nyaaa..."
                    "I guess.... I guess I'd better wake her up, but I don't think this image is gonna leave my head for a while."
                    # Note - menu choice here. He either wakes her up or decides she's too cute like this and wants to play with kitty hiroko a bit longer
                    # Former choice, follow original script. Second choice, he plays with her a bit, loses track of time as dad pulls up on the driveway...
                    # "Anyway, better wake her up and stop thinking about how cute she is when she's like this."
                    "Crouching down, I look into her eyes and switch the penlight back on to shine it over her curious face once more."
                    show cglightsmall:
                        xpos 0.38 ypos 0.25
                        linear 0.5 xpos 0.53 ypos 0.3
                    pause 0.2
                    hide cglightsmall with dissolve
                    ks smile "Look into the light again, Hiroko... good kitty."
                    show Hiroko Cat dazed
                    h "Mew!" with dissolve
                    # "She looks up at me with wide eyes. Fuck, she looks adorable like that."
                    "Her eyes glaze over slightly in confusion as they fixate on the light in my hand."
                    show cglightsmall:
                        xpos 0.53 ypos 0.3
                        linear 0.5 xpos 0.38 ypos 0.25
                    pause 0.2
                    hide cglightsmall with dissolve
                    ks "That's it, Hiroko. Just let the light take you down."
                    show cglightsmall:
                        xpos 0.38 ypos 0.25
                        linear 0.5 xpos 0.53 ypos 0.3
                    pause 0.2
                    hide cglightsmall with dissolve
                    ks "There we go. Sleep." with dissolve
                    show Hiroko Cat lying sleep
                    $ renpy.transition(longdissolve, layer="master")
                    "As her head droops, I guide it to the floor with the rest of her body, curled up as it is on my rug."
                    "Fuck, she looks adorable like this."
                    ks neutral "Nice and deep once more, Hiroko. And as you go deeper, you will find yourself returning back to your normal, human self."
                    ks "You no longer need to visualize yourself as a cat, Hiroko. You can let all of that go, as you let yourself become your human self once again."
                    ks "And now waking in one... two... three, wide awake, Hiroko."
                    show Hiroko Cat lying waking
                    "Hiroko's eyelids flicker as she begins to stare up at me bleary-eyed from the rug." with dissolve
                    h "Bluh... why the fuck am I on the floor?"
                    ks smile "You were a cat, like I said you'd be!"
                    stop music fadeout 5.0
                    h "'Kay, but..."
                    $persistent.hiroko_cat_1_unlock = True
                    scene bg k room eve
                    show Hiroko tennis sleepy at center:
                        ypos 1.3
                        linear 2.5 ypos 1.0
                    with blink
                    "As she goes to stand, she holds a hand to her head."
                    show Hiroko tennis_headhold:
                        ypos 1.0
                    play music Measured
                    h sad "I still don't get it." with dissolve
                    ks "... What about it don't you get?"
                    h nervous "Like, you wave that light in my face a few times and suddenly I'm whatever you say I am?" with dissolve
                    h tennis nervous_side "I didn't wanna think about it, but I now can't stop myself." with dissolve
                    ks "Think about what?"
                    h sad "You think I really wanna do these things for you, Kyou? 'Cuz I don't." with dissolve
                    h nervous "But you do your thing on me and it's like it don't matter what I want. I just do it." with dissolve
                    if hypno3 == "stuck":
                        h sad_side "You wave your magic light in my face and welp, thassit. My feet are stuck now." with dissolve
                    if hypno6 == "cat":
                        h sad "Do it again? Blam, now I'm a kittycat." with dissolve
                    ks "Yeah, it might seem that way to you, Hiroko."
                    ks "But I'm telling you, you had to have wanted it on some level. Hypnosis wouldn't work on you otherwise."
                    h "Yeah, but..."
                    show Hiroko sleep
                    "She cuts herself off as she frowns, seemingly deep in thought." with dissolve
                    h tennis_headhold2 nervous_side "\"On some level\"... 'kay, maybe that's true." with dissolve
                    h frown "But I meant what I said about this being the last one. No other weird shit, you get me?" with dissolve
                    ks "I heard you. I want to do some prep before the festival, but these are the only hypnosis things I'll do with you for it."
                    h "'Kay... Anyway, I'm outta here."
                    stop music fadeout 5.0
                    scene bg k bedroom night with blink
                    "As I lie in bed thinking to myself, it's become obvious to me..."
                    "I definitely have a thing for Hiroko now."
                    "Seeing her like she was tonight... how could I not?"
                    "Not to mention she must have some feelings for me, too, much as she might deny it."
                    "All the things we've done, and how fully she's committed herself to dropping for me..."
                    "That can only come from the mind of someone who trusts me completely."
        elif hypno3 == "ticklish":
            "But in the end..."
            show Hiroko
            h angry "Tch... Kyou." with dissolve
            ks frown "Hiroko."
            hide Hiroko
            "It all came to nothing." with dissolve
            play music Bright_Opening
            scene bg classroom day with blink
            "After my desperate fling with Hiroko, I'm starting to think it really is time I called it quits."
            "I know I didn't want to waste all my time researching hypnosis and stuff after Nozomi turned me down again."
            "But I need to face facts and cut my losses. Try and get my head back into schoolwork and figure out what else I'm gonna do with my life."
            show Hiroko neutral_side at center
            show Nozomi side sad_side at center, flip:
                xpos 0.25
            n "You're looking a little glum today, Hiroko." with dissolve
            h frown_side "Y- yeah? What about it?" with dissolve
            "It really is a shame, though. I was actually starting to get excited about the idea of doing stage hypnosis for the culture fest."
            n "Just something I noticed, that's all. If you want to talk about it- {w=0.8}{nw}"
            h "I don't."
            n sad_closed "... Alright, then." with dissolve
            h sleep "*sigh* Sorry. I'm just, uh... stressing over the tourney an' shit, I'll be fine." with dissolve
            scene bg k room eve with longblink
            stop music fadeout 5.0
            "Even if I'd be doing it with that spiteful bitch."
            "But damn, that girl really does have a talent for being hypnotized, I'll give her that much."
            play sound doorbell
            "... Huh? The doorbell just rang. I'm not expecting anyone."
            scene bg k entrance eve with blink
            "I'm about to open the door when I think to peer out the window to find..."
            ks angry "H-Hiroko?!"
            "Shit. Back away from the door..."
            play sound doorbell
            h "{size=16}Hey, asshole! Open up.{/size}"
            "Why the fuck is she back here?!"
            play sound doorbell
            h "{size=16}I SAW you! Lemme in!{/size}"
            ks "Why should I? What do you even WANT from me?"
            play sound doorbell
            h "{size=16}You gotta fix it!{/size}"
            ks "Fix what?"
            h "{size=16}Fix my {nw}{/size}"
            play sound doorbang
            extend "{size=16}GODDAMNED HANDS!{/size}" with shake
            "Her hands?"
            ks "What the fuck?! Don't kick my door!"
            play sound doorbang
            h "{size=16}OPEN UP!{/size}" with shake
            ks "SON OF A BITCH!"
            play sound dooropen
            "I can't let her carry on like that, so with great reluctance I pull the door open..."
            show Hiroko tennis angry at center
            with dissolve
            play sound doorclose
            "And a fuming Hiroko clad in her tennis gear stomps inside."
            play music Downtown
            h "Jesus. Was that so hard?"
            ks "Well excuse me if I don't want some rage-happy psycho in my house-{nw}"
            hide Hiroko
            $ renpy.transition(dissolve, layer="master")
            extend " Hey! {nw}"
            extend "Don't walk in here with those!"
            scene bg k room eve
            show Hiroko tennis angry
            with blink
            "Hiroko just glowers at me as she stalks into my living room while still wearing her tennis shoes."
            h tennis_armup furious vein "Just shut up and help me, yeah? I ain't taking 'em off." with dissolve
            h angry "If I do that, something's gonna touch my hand and..." with dissolve
            h sleeptalk novein "And I am so fuckin' done with feeling tickly." with dissolve
            # h "I'm done with all of this hypno shit."
            scene cg k room eve
            play sound sitting
            show HirokoHypno upright tennis frown relaxed_fists_tennis
            with blink
            "Hiroko plops onto my couch and raises her hands in front of her as she stares at them with a pained expression."
            h "Like... no matter what I do, anything that rubs on my hands 'sides my own fingers and I'm trying not to laugh my ass off."
            "You know, now that she mentions it..."
            show HirokoHypno nofists
            h "Tennis was a fuckin' disaster today, 'cuz of what you did." with dissolve
            ks frown "What? You couldn't focus?"
            show HirokoHypno angry
            h "How am I s'posed to focus when I can't even hold my goddamned racket properly?" with dissolve
            "I never stipulated when she should stop considering her palms ticklish when I hypnotized her."
            h "Like, I gotta grip it super tight so it don't rub, but that makes my swing weak as shit."
            h "An' then every time I hit the ball, I'm feeling the vibes coming off the handle and I gotta laugh and try not to drop the fucking thing."
            # h "Every time I hit the ball the vibrations coming off the handle made me drop the fuckin' thing."
            "But even so..."
            show HirokoHypno annoyed
            h "Couldn't even get mad about it, 'till I got off court anyway." with dissolve
            show HirokoHypno sleeptalk
            h "And you better believe Risa loved the shit out of watching me fuck up so bad." with dissolve
            ks confused "So you're saying my hypnosis from yesterday still works? Even though you said you didn't want it to?"
            show HirokoHypno angry
            h "Like I didn't just get done explaining it!" with dissolve
            ks "Well, it's just..."
            "I hesitate to point it out to her, but..."
            ks smirk "You know this stuff only works when you let it, right?"
            show HirokoHypno clenched_fists_tennis blush
            h "You think I {nw}" with dissolve
            extend "WANNA laugh like a jackass in front of everyone?" with vpunch
            "I offer her an indifferent shrug."
            ks "Maybe not consciously. But subconsciously? It might be your brain's way of telling you to lighten up."
            show HirokoHypno noblush
            h "Yeah? {w=0.5}Like my fists are gonna be my way of telling you to {nw}" with dissolve
            extend "WISE THE FUCK UP AND FIX ME!" with shake
            # h "Just fix what you did to me or I'm gonna hit you on {nw}"
            # extend "PURPOSE!" with vpunch
            "I bring a hand up to rub my cheek out of reflex. Honestly, I can still feel her fist on there from last night."
            ks sigh "Man, why should I?"
            show HirokoHypno nofists
            h "'Cuz it's your fault I'm like this!" with dissolve
            ks "Yeah, like it was my fault you socked me one. Maybe you should think about that."
            # ks "Well, maybe you should've thought about that before you socked me one."
            ks "I mean, if you hadn't hit me I would've taken you back into trance and lifted the suggestion from your mind there and then."
            ks "It was only supposed to be a trick for our hypnosis show, after all."
            ks "But instead you just had to-{w=0.5}{nw}"
            show HirokoHypno clenched_fists_tennis
            h "I don't care about that! {w=0.5}{nw}" with dissolve
            extend "FIX MY FUCKING HANDS!" with shake
            "Seriously though, why should I help her if all she's going to do is threaten and bully me into getting what she wants?"
            h "I'm so fucking done with it. Make em', like, UN-tickly again!"
            "The deal we had going to do the culture fest together is surely off the table, so what obligation do I have to her now?"
            "She already got a tennis racket out of me. Maybe she forgot about that, but I sure haven't."
            menu:
                "Help her":
                    ks angry "A-Alright! Settle down already."
                    "As unmotivated as I am to ease her torment a thought occurs to me."
                    show HirokoHypno nofists frown
                    "I still helped her into this state of mind, and as much as I helped her before, this is clearly something I did that's causing her a lot of pain." with dissolve
                    "And as much of a bitch she's being, as her hypnotist I'm kinda obligated to help her, aren't I?"
                    show penlight at right with moveinright:
                        ypos 0.346
                    ks frown "So, we'll put you back in trance and convince your subconscious self to let go of the tickling suggestion. Sound good?"
                    show HirokoHypno sleeptalk
                    "Hiroko lets out a sigh as she nods. Seems giving in to her demand has already done a lot to calm her down." with dissolve
                    h "Yeah... Yeah, just get it done."
                    hide penlight at right with moveoutright
                    ks frown "Alright then, so if you could sit back and focus as before?"
                    show HirokoHypno annoyed_up
                    "I can feel Hiroko's reluctance as she assumes a comfortable position, placing her hands on her lap with her palms facing upwards so she doesn't touch anything." with dissolve
                    call cglightshow from _call_cglightshow_162
                    ks "That's right. Going back to this familiar feeling as I pass the light across your eyes."
                    $renpy.music.set_volume(1.0)
                    call cglightshow from _call_cglightshow_163
                    show HirokoHypno relaxed sleepy_up_open
                    $ renpy.transition(longdissolve, layer="master")
                    $renpy.music.set_volume(0.8)
                    ks "So naturally... So easily..."
                    call cglightshow from _call_cglightshow_164
                    $renpy.music.set_volume(0.6)
                    ks neutral "So automatically, just letting the light patterns in your eyes take you deeper..."
                    call cglightshow from _call_cglightshow_165
                    $renpy.music.set_volume(0.5)
                    show HirokoHypno relaxed sleepy_up_closed
                    $ renpy.transition(longdissolve, layer="master")
                    $renpy.music.set_volume(0.4)
                    ks "And deeper. There's no need to think about it."
                    call cglightshow from _call_cglightshow_166
                    $renpy.music.set_volume(0.3)
                    ks "Just letting your eyelids become heavy. Letting your head droop as you fall back into a deep, relaxing trance."
                    call cglightshow from _call_cglightshow_167
                    $renpy.music.set_volume(0.2)
                    show HirokoHypno relaxed sleep
                    $renpy.music.set_volume(0.2)
                    $ renpy.transition(longdissolve, layer="master")
                    ks "Thoughts fading. Feeling so good as you drop deep, Hiroko. Deep asleep and ready to listen only to my voice. Only to my suggestions."
                    show HirokoHypno drooping sleep
                    stop music fadeout 2.0
                    $ renpy.transition(longdissolve, layer="master")
                    "I let that sit with her for a while as I think this over."
                    "Gotta get the phrasing right if I want to convince her she's no longer as sensitive as she thinks."
                    $renpy.music.set_volume(1.0)
                    play music Flow
                    ks "And now that you're back in this pleasant state of hypnotic trance, listening to my voice once more, I want you to reconsider the ticklish feelings of your palms."
                    ks "Remember that what you've been feeling isn't real. It's a mere construct of your mind to think you need to laugh when something touches your palms."
                    ks "So instead, I want you to let go of that construct. The palms of your hands are no more ticklish than they should be."
                    ks "You will experience a completely normal and natural sensation whenever your palms are touched. Understand, Hiroko?"
                    show HirokoHypno sleeptalk
                    h "Understand..." with dissolve
                    show HirokoHypno sleep
                    ks "Alright, then. So now on three you're going to come out of trance feeling refreshed and no longer feeling ticklish on your palms." with dissolve
                    stop music fadeout 10.0
                    ks "Waking in one, two... three, wide awake, Hiroko."
                    show HirokoHypno relaxed sleepy_up_open
                    h "Mrrh... You did it?" with dissolve
                    "I sigh, then reach out and quickly grab her hand off her lap."
                    show HirokoHypno scared
                    h "AGH! WHAT ARE YOU{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}" with shake
                    show HirokoHypno sleeptalk
                    $ renpy.transition(dissolve, layer="master")
                    extend " Ah okay, yeah."
                    play music Downtown
                    "I have to chuckle at the relief on her face as my fingertips trace her palm to no real effect."
                    ks smile "Better?"
                    h "Better... {w=1.0}{nw}"
                    show HirokoHypno upright blush angry clenched_fists_tennis
                    play sound slap
                    $ renpy.transition(dissolve, layer="master")
                    extend "A-And who said you could touch me?!" with vpunch
                    "I wince as she slaps my hand forcefully away."
                    ks sigh "You're welcome?"
                    show HirokoHypno nofists annoyed
                    h "HMPTH!" with dissolve
                    "Although as she snorts, she tentatively starts to rub her hands against the front of my couch cushions."
                    show HirokoHypno noblush sleeptalk
                    h "Haah..." with dissolve
                    ks frown "What is it now?"
                    h "Like... Dude, you got no idea how good this feels..."
                    ks confused "Rubbing my couch?"
                    show HirokoHypno angry blush
                    h "F-fuck off! That ain't it. It's just..." with dissolve
                    show HirokoHypno frown
                    h "Like, you ever lose something you take for granted? And you suddenly get it back and you're like..." with dissolve
                    show HirokoHypno sleeptalk
                    h "\"Holy shit, I'm never letting you out of my sight ever again!\"" with dissolve
                    show HirokoHypno neutral
                    h "That's what it feels like. You took something away from me, an' you gave it back." with dissolve
                    show HirokoHypno noblush
                    h "You flash a light in my face, say some magic words and... And now I get to use my hands again." with dissolve
                    h "So now I'm thinking like..."
                    show HirokoHypno angry clenched_fists_tennis
                    h "How the fuck are you even doing this?" with dissolve
                    ks sigh "Man, I dunno what to tell you. We already know how good you are at being hypnotized."
                    ks "You can focus and stay really attentive while I'm giving you suggestions to take in."
                    show HirokoHypno frown nofists
                    "I sigh as I twirl my penlight around in my fingers while I look to her. Like, I don't know how I can explain it to her any better than I already am." with dissolve
                    ks frown "But I'm telling you, there's nothing magic about it. None of this would have worked unless you let it, Hiroko."
                    ks "So for you to take these suggestions so deeply into your mind, and to hold onto them only until I told you to let go?"
                    ks "What do you think that means?"
                    show HirokoHypno angry
                    h "I know what it means, dude." with dissolve
                    show HirokoHypno clenched_fists_tennis
                    stop music
                    h "It means you're full of {nw}" with dissolve
                    extend "SHIT!" with vpunch
                    scene bg k room eve
                    show Hiroko tennis_armup angry at center:
                        ypos 1.2
                        linear 2.0 ypos 1.0
                    with blink
                    "I wince at her shouting at me again, and that's probably how I don't realise until too late that she made a grab for the penlight between my fingers."
                    show Hiroko at center
                    play music Sad_Heroine
                    ks angry "H-Hey! Give that back!"
                    "Honestly, I may as well insist she fire tennis balls out of her ass if I'm making unrealistic demands."
                    h frown "Nah. But you're gonna listen to me!" with dissolve
                    "Hiroko grips my penlight tightly in her thieving little paws and continues."
                    h angry vein "'Cuz dude, you ain't even listening to yourself!" with dissolve
                    ks frown "What?"
                    h tennis irritated "Like... fuck, think it through, man!" with dissolve
                    h "How is it that I wanna be both super focused AND super distracted when I'm on the court?"
                    h furious "It makes no fuckin' sense!" with dissolve
                    ks "And you saying I do magic tricks on your brain is any better?"
                    h tennis_armup "You {nw}" with dissolve
                    extend "FUCKIN'..." with vpunch
                    "Hiroko sucks through her teeth as she her eyes glance over the penlight still trapped in her fist."
                    h furious_side "Okay, smart guy, how 'about I give YOU a little magic and see how you feel about it then?" with dissolve
                    h irritated "Whaddya think of {nw}" with dissolve
                    extend "THAT?" with vpunch
                    "Oh my god, is she saying what I think she's saying?"
                    "Now it's MY turn to suck through my teeth, as I pinch the bridge of my nose in despair."
                    show Hiroko angry
                    ks sigh "Hiroko, you can't just... use that thing on me. It's not just the light that lets me talk to your subconscious." with dissolve
                    ks "I am actually a self-taught hypnotist. I know how to talk in a way that encourages the state to happen."
                    ks "You can't just tell someone they're getting sleepy and expect that to work."
                    h angry novein "Really, dude? 'Cuz far as I can tell that's EXACTLY what you do!" with dissolve
                    h "You flash this thing in my face, say a few words an' thassit."
                    h frown "Then you tell me what I'm 'sposed to feel and I just gotta go with that whether I like it or not." with dissolve
                    h angry "Seems piss easy to me. I wanna go!" with dissolve
                    ks frown "You want a go on my penlight."
                    show Hiroko smirk
                    "Hiroko grins at me as she clicks the light switch on the penlight with her thumb." with dissolve
                    h "You scared of what I'll do to you while you're sleepin'?"
                    ks sigh "Christ, and you say I'm creepy."
                    h frown "C'mon, you think I can't do it. So what's the harm?" with dissolve
                    ks "I don't want to play to your delusions."
                    h angry "I fuckin' {nw}" with dissolve
                    extend "DARE you I can do it! I'll make you sleepy and get you doin' some stupid shit." with vpunch
                    ks angry "This is so fucking stupid. You have NO idea what you're doing."
                    "She spends a couple moments seething at me before apparently another idea pops into that logic-free zone she calls a brain."
                    h tennis frown "How 'bout we make this interesting?" with dissolve
                    ks frown "Interesting?"
                    h frown_side "Yeah, like a bet." with dissolve
                    ks "A bet that you can hypnotize me."
                    h angry "Yeah! If you think this is so stupid, you'll win easy, right?" with dissolve
                    "This girl has no idea..."
                    h frown_side "So... I dunno, you lemme try and if I hypnotize you, you gotta help me prep for the tourney I got this weekend." with dissolve
                    ks "Okay, and when you try and nothing happens, I want you back as my assistant for the culture fest without any more of your bitching."
                    show Hiroko sleep
                    "And to that, Hiroko just shrugs her shoulders." with dissolve
                    h "'Kay, so it's on."
                    scene cg k room tv eve
                    show HirokoHypno upright tennis2 frown2 clenched_fists_tennis2
                    with blink
                    "And so I find myself on the couch with Hiroko sitting opposite, only this time I'm supposed to entertain this farce."
                    h "So, like... you ready?"
                    ks sigh "Sure."
                    "Unlike her, I'm not even going to attempt to focus. It's not like I actually want the little snot to hypnotize me, after all."
                    "And I know you can't hypnotize the unwilling, regardless of what she seems to think."
                    "So I'll just go through the motions until I can convince her to drop this idiotic game she's playing with me."
                    h "'Kay..."
                    "Now that she's actually committed herself, I can see the trepidation in her face as she holds the penlight up."
                    "It's unusual to see her lack confidence, and I'm starting to get into this little arrangement we've got going now."
                    "I'm definitely going to enjoy making her sweat."
                    ks smirk "So... What are you gonna try and do to me, miss hypnotist?"
                    show HirokoHypno angry2
                    h "S-shut up!" with dissolve
                    ks "I'm just saying. If you're going to hypnotize me you'll have to make your intentions clear."
                    show HirokoHypno nofists
                    "Hiroko slaps the penlight back down in her lap as she lets off an irritated sigh." with dissolve
                    show HirokoHypno sleeptalk
                    h "F-fine, lemme think a minute..." with dissolve
                    show HirokoHypno sleep
                    h "Hrrm..." with dissolve
                    ks "We don't have all night, tennis girl."
                    show HirokoHypno annoyed_up2
                    h "Quit trying to put me off, jackass!" with dissolve
                    show HirokoHypno annoyed2
                    h "Anyway, I think... yeah, I think I got something." with dissolve
                    "She sucks a breath through her nose as she tries to assert herself, then hits me with her big idea."
                    show HirokoHypno angry2
                    h "I'm gonna make you think Nozo's gross." with dissolve
                    ks sigh "Okay, sure...{w=1.0}{nw}"
                    extend surprised " w-wait, WHAT?!"
                    show HirokoHypno smirk2
                    h "Yeah! Then you won't wanna creep on her all the time!" with dissolve
                    "... I think we've plumbed a new depth of ridiculousness here."
                    ks sigh "This is stupid even for you."
                    show HirokoHypno annoyed2
                    h "Why? It's doable, ain't it?" with dissolve
                    ks frown "I mean... technically? I've seen stage hypnotists convince a volunteer to think a certain person was ugly for a while, sure."
                    ks "But do you really think you can do that to me? I just..."
                    "I stutter on my words while my brain struggles to comprehend the absurdity."
                    "To even entertain the notion that I'd think of Nozomi Akemi as anything but a perfect picture of feminine beauty and grace?"
                    ks sigh "Actually, why am I trying to talk you out of this?"
                    ks "If that's what you're going for, I totally invite you to try."
                    show HirokoHypno sleeptalk
                    h "R-Right. This's what we're doing, then." with dissolve
                    $persistent.k_room_hiroko_tv1_unlock = True
                    scene cg k room reversal
                    show HirokoReversal nervous
                    with blink
                    "I can't help but chuckle as she holds the penlight aloft."
                    "Looking at her expression, I think I've done enough to shake what little confidence she had in this."
                    ks smirk "I'm just thinking what I'll have you do as my assistant."
                    ks "Nothing to get us expelled obviously but still, it's gotta be something that'll get the school talking about us..."
                    # show HirokoHypno angry blush clenched_fists_tennis
                    show HirokoReversal body_blush angry
                    h "D-Dude, shut up! We're startin' this!" with dissolve
                    ks "Okay, hit me with your best-{w=1.0}{nw}"
                    stop music fadeout 1.0
                    show HirokoReversal body
                    with flash
                    "Wh- Whoa, that hit me hard."
                    ks angry "Ow!"
                    show HirokoReversal rolleyes
                    h "Ah fuck off, it don't hurt. You did it to ME enough times." with dissolve
                    "Yeah, I reacted more out of surprise than anything."
                    "I know this light was my own design, but I never once tested the effect of the light on myself."
                    $renpy.music.set_volume(1.0)
                    show HirokoReversal nervous with flash
                    $renpy.music.set_volume(0.1)
                    play music Flow
                    h "Now you pay attention."
                    h "'Cuz I dunno about the way you talk to people to make 'em sleepy..."
                    with flash
                    h "But I sure know what you're seeing right now."
                    show HirokoReversal nervous_side
                    with flash
                    $renpy.music.set_volume(0.2)
                    h "There's these... like, patterns that you can't really make out."
                    show HirokoReversal nervous
                    with flash
                    h "But you know they're there, and you know they're pretty."
                    $renpy.music.set_volume(0.3)
                    with flash
                    h "And you just... I dunno."
                    show HirokoReversal neutral
                    with flash
                    $renpy.music.set_volume(0.4)
                    h "There's something about 'em that makes you..."
                    with flash
                    h "Makes you wanna look more, y'know? Yeah, you know."
                    show HirokoReversal smirk
                    with flash
                    $renpy.music.set_volume(0.5)
                    h "You're thinking it right now, about looking. It's all over your dumb face."
                    with flash
                    $renpy.music.set_volume(0.6)
                    h "It don't matter what you thought before, does it? All you wanna do now is look."
                    with flash
                    $renpy.music.set_volume(0.7)
                    h "So you look."
                    with flash
                    h "But, like, looking is hard. You got this flashlight going off in your face all the time and it tires your eyes out."
                    with flash
                    $renpy.music.set_volume(0.8)
                    show bg blackscreen onlayer toplayer with dissolve:
                        alpha 0.5
                    h "Kinda makes you wanna take a nap, don't it?"
                    show HirokoReversal neutral
                    with flash
                    $renpy.music.set_volume(0.9)
                    h "Nah, don't move your lips; you don't gotta answer that. You can just close your eyes."
                    with flash
                    show bg blackscreen onlayer toplayer with dissolve:
                        alpha 0.7
                    h "Yeah, that's the way.  Just close your eyes, dude."
                    $renpy.music.set_volume(1.0)
                    scene bg blackscreen onlayer toplayer with fade
                    stop music fadeout 10.0
                    h "And then you can relax and listen to me some more, right?"
                    h "Heh, don't answer that either."
                    h "Just sleep."
                    $persistent.hiroko_reversal_unlock = True
                    pause 1.0
                    scene cg k room tv eve
                    stop music
                    hide bg blackscreen onlayer toplayer
                    show HirokoHypno upright tennis2 frown2 clenched_fists_tennis2
                    play sound slap
                    with vpunch
                    ks surprised "U-URGH!"
                    "I wake up with a start as I feel something slap across my cheek."
                    ks "Wh-what the fuck?! What's going on!?"
                    show HirokoHypno nofists angry2
                    h "Ah, quit being dramatic, I just woke you up." with dissolve
                    show HirokoHypno annoyed_up2
                    h "An' I hit the other cheek. Don't be a wuss." with dissolve
                    ks "H-Huh?"
                    play music Downtown
                    "I hear myself groan as my hand reaches up to stroke my face."
                    ks sigh "Where am I? Who are you?"
                    show HirokoHypno sleeptalk
                    h "H'yeah, you're just hilarious, man. C'mon, you gotta admit I got you." with dissolve
                    ks frown "... Got me?"
                    "As the swimming sensation in my head slows down, it all starts to come back to me."
                    ks "Are you saying..."
                    show HirokoHypno frown2
                    h "I totally hypnotized you, dude!" with dissolve
                    ks "Y-you..."
                    "Okay, I know this looks bad, but..."
                    ks angry "No you fucking didn't! Tell me what really happened!"
                    show HirokoHypno annoyed_up2
                    h "Oh man, lessee... I waved that light in your face a bunch, you got sleepy an' I told you to go sleep." with dissolve
                    show HirokoHypno sleeptalk
                    h "An' when you did, I told you a bunch of other stuff and woke you back up." with dissolve
                    h "You're welcome, by the way. I shoulda left you napping."
                    ks "Nobody normal wakes someone up with a slap! Jesus Christ!"
                    show HirokoHypno angry2
                    h "Well, that ain't MY fault! I never remember the bit where you wake me up." with dissolve
                    h "Anyway, I'm outta here."
                    scene bg k room eve
                    show Hiroko tennis frown at center:
                        ypos 1.5
                        linear 2.0 ypos 1.0
                    with blink
                    "And with that, Hiroko gets up off the couch while I'm still piecing together what just happened."
                    show Hiroko:
                        ypos 1.0
                    ks angry "Wait, what do you mean you're outta here? We're not done!"
                    h frown_side "Pffth, yeah well we gotta wait 'till tomorrow, don't we." with dissolve
                    scene bg k entrance eve
                    show Hiroko tennis frown_side at center
                    with blink
                    ks frown "Tomorrow?"
                    # show Hiroko:
                    #     xpos 0.8
                    h tennis_armup furious "I wanna see if it worked!" with dissolve
                    ks "If WHAT worked?"
                    "And... wait a minute."
                    ks angry "Where the fuck is my penlight?"
                    show Hiroko tennis smirk
                    "She spares a look to her sports bag as she slings it over her shoulder, then smirks at me." with dissolve
                    h "You'll get it back."
                    #Kyou's in denail, but asks what happened
                    # "Kyou comes to with a slap to the face, waking up groggy and disoriented by Hiroko's unorthodox method of bringing him back to consciousness."
                    # "When he gets his wits about him, Kyou asks Hiroko what happened."
                    # "She smirks and says it's nothing he needs to worry about. But she declares she's keeping the penlight as she drops it into her sports bag."
                    scene bg k house eve with blink
                    play sound dooropen
                    # "Kyou responds with anger and gets up to give chase, but Hiroko was already making for the door when she made her declaration."
                    ks angry "HIROKO!"
                    "By the time I'm able to run out into the street, she's nowhere to be found."
                    ks "God... {w=0.5}f-fucking {nw}"
                    extend "DAMMIT!" with vpunch
                    "How'd she leave so fast?"
                    "... Wait, was she wearing her tennis shoes indoors?"
                    "Oh, that's right. More's coming back to me."
                    "\"I'm gonna make you think Nozo's gross.\""
                    "... No. Maybe she managed to put me into some sort of trance, I'll cop to that."
                    "But it doesn't matter."
                    scene bg k room eve with blink
                    play sound doorclose
                    "Turn me off on Nozomi? Impossible."
                    "I know what kind of girl I like, and it's her."
                    "Her and her... her perfectly proportioned body, those lengths of luscious brown hair..."
                    "Even those glasses of hers seem to frame her face like the perfect gallery painting."

                    scene bg k bedroom eve with blink
                    stop music fadeout 5.0
                    "So that settles it. I'm not affected by Hiroko's childish foray into hypnotism."
                    "I'll just have to confront her at school tomorrow. Make sure she knows what's what."
                    "And I'll get my fucking penlight back..."
                    #Next day, Nozomi seems to look nothing like he imagined her the night before
                    #Point she could make - She took something from Kyou (liking Nozomi), and then she gives it back, parallel to Kyou giving her ticklish hands
                    jump Day5_Con_Kyou_Hiroko_Penlight

                "Don't help her":
                    ks frown "Nah."
                    show HirokoHypno nofists
                    h "\"Nah\"? The fuck you mean \"nah\"?" with dissolve
                    h "You {nw}"
                    extend "GOTTA fix this!" with vpunch
                    "Folding my arms, I simply look to her with disdain."
                    "I'm not letting this bullying bitch get what she wants from me, especially not with this kind of shitty attitude."
                    ks "I don't need to fix anything, Hiroko. This is all on you."
                    ks "Now get out of my house."
                    show HirokoHypno frown
                    h "I ain't leaving 'till you make it stop!" with dissolve
                    "Maybe if we were still in school she could get away with it."
                    "But I'm at the end of my rope, and we're a long way from any classroom."
                    ks angry "The fucking NERVE of you!"
                    ks "You assault me. You threaten me. Damage my property. You disrespect me all the fucking time..."
                    "I thrust my hand towards the floor at the shoes she's still wearing inside the house, as if I needed a visual to reinforce that last point."
                    ks "So what if this happened to you because of me. Stay and cry all you want if you think it'll change my mind; I don't care."
                    ks "You brought this on yourself!"
                    stop music fadeout 5.0
                    h "..."
                    "As I brace for her inevitable spiteful comeback, I watch her expression carefully..."
                    h "Kyou..."
                    "Only..."
                    show HirokoHypno concerned
                    h "C-c'mon, are you fucking serious?! You can't leave me like this! " with dissolve
                    show HirokoHypno scared
                    play music Measured
                    h "Y-you {nw}" with dissolve
                    extend "CAN'T!" with vpunch
                    "Yeah. I guess I was too much of a coward to test it before now, but she's really got no bite to go with that vicious bark of hers."
                    "Not to mention..."
                    show HirokoHypno sad_closed
                    h "Please, Kyou! I'm sorry, okay?" with dissolve
                    "She really does think I've made some permanent change to her, huh? As if I had her under some kind of magic spell."
                    h "Just... f-fuck, I dunno how you did this to me and it's freakin' me out."
                    "It's like I told her, she's only affected because she's allowed my suggestions to influence her. All this is purely in her mind."
                    show HirokoHypno sad
                    h "But it ain't funny anymore. You get that, right?" with dissolve
                    "Hiroko's not dumb if she can be hypnotized so well. She can listen and focus her mind to do some amazing things after only a few sessions with me."
                    "But the fact she really thinks she's beholden to an unwanted suggestion like this makes me think she's a little..."
                    # "So the fact that she's still playing to my ticklish hands suggestion in spite of how distressing it is?"
                    show HirokoHypno sleep
                    h "S-so please... please, you gotta stop this." with dissolve
                    "Gullible."
                    ks frown "Man, I don't know..."
                    "I may not have wanted to help her, but this is interesting to me. And she's so desperate for my help."
                    show HirokoHypno sad
                    h "Please..." with dissolve
                    "I could use this. Not just to test the limits of my skill as a hypnotist, but to teach her a few lessons about respecting her peers as well."
                    "So why don't I?"
                    menu:
                        "Find out how gullible she really is":
                            stop music fadeout 5.0
                            ks "Okay Hiroko, that's enough. I'll help you after all..."
                            show HirokoHypno sleep
                            "I pause a moment, long enough for Hiroko to quietly sigh in relief, before I add the stinger:" with dissolve
                            ks smirk "But it's gonna cost you."
                            show HirokoHypno sad
                            h "H-Huh?!" with dissolve
                            play music Eons
                            "Yeah. I know exactly how I'm going to play her."
                            "She wouldn't listen to me before, about how she doesn't have to take on a hypnotic suggestion she doesn't want."
                            "But she'll listen to this..."
                            ks "I'll take you back into trance, Hiroko. And you'll drop for me and absorb my every word, just like before. Just like you're so good at doing."
                            ks "You'll listen really closely and you'll lose that ticklish feeling in your palms at my say so. I'll do that for you."
                            ks "But here's the thing: You're not going to stop listening after that."
                            ks "You may try to shut out my words, but the more you try, the more you'll find yourself listening."
                            ks "So you'll hear what else I have to say, because you'll still be deep in trance, Hiroko. Still listening so intently. Just soaking it all up."
                            ks "And that's why, when you wake again, you'll be following some new suggestions of mine."
                            show HirokoHypno angry clenched_fists_tennis
                            h "L-Like {nw}" with dissolve
                            extend "HELL I will!" with vpunch
                            "That's right, Hiroko. Just reinforce that mindset you're holding onto. The one that has you thinking my suggestions are irresistible."
                            ks "If you don't like it, I can leave you with those hands."
                            show HirokoHypno relaxed_fists_tennis
                            h "U-uggghh..." with dissolve
                            "And I'm sure my little bit of psychological warfare is helping with that goal in mind."
                            ks "I'm gonna get a little payback for the punch, and all the other crap you've put me through these past couple years, but relax, okay? This won't be as bad as you're thinking."
                            ks "I'm not seriously going to mess with your tennis career, or do anything really bad to you."
                            ks "There really is a limit to what hypnosis can do, even if it won't seem like it to you. I'll never be able to suggest something you'd find truly unacceptable."
                            ks "But you might be surprised at what you find yourself agreeing to; like your subconscious really does want you to lighten up a bit about all this."
                            ks "You may truly find yourself enjoying what we do together, Hiroko."
                            show HirokoHypno nofists frown
                            h "Nothing's enjoyable with you, you... c-creepy fuckin' asshole." with dissolve
                            show HirokoHypno nofists sad_closed
                            h "I just wanna be done with this hypno shit and go home. C'mon." with dissolve
                            ks "But most importantly, you want your hands back to normal, right?"
                            show HirokoHypno nofists sad
                            h "Y-yeah, but-{w=0.5}{nw}" with dissolve
                            $renpy.music.set_volume(1.0)
                            show penlight at right with moveinright:
                                ypos 0.346
                            call cglightshow
                            $renpy.music.set_volume(0.9)
                            ks "So let's address that most important part first, shall we?"
                            "Wasting no more time, I swiftly click my penlight back on and sweep it across her unprepared eyes."
                            h "B-but-{w=0.5}{nw}"
                            hide penlight at right with moveoutright
                            call cglightshow
                            $renpy.music.set_volume(0.8)
                            ks "Don't worry about it. Just let the light take all of your attention now."
                            call cglightshow
                            show HirokoHypno straining
                            $ renpy.transition(longdissolve, layer="master")
                            $renpy.music.set_volume(0.7)
                            h "U-uunnng..."
                            ks "Letting it take your attention as you remember to breathe."
                            call cglightshow
                            $renpy.music.set_volume(0.6)
                            ks "Breathing in. Breathing out. Unclenching your jaw and letting those patterns before your eyes take you deeper..."
                            call cglightshow
                            show HirokoHypno relaxed drowsy
                            $renpy.music.set_volume(0.5)
                            $ renpy.transition(longdissolve, layer="master")
                            h "{size=16}Haaaah...{/size}"
                            ks "And deeper. That's right."
                            call cglightshow
                            $renpy.music.set_volume(0.4)
                            ks "Just breathing. And staring. And going deeper into relaxation."
                            call cglightshow
                            show HirokoHypno sleepy_up_closed
                            $renpy.music.set_volume(0.3)
                            $ renpy.transition(longdissolve, layer="master")
                            ks "Deeper into hypnosis."
                            $renpy.music.set_volume(0.2)
                            call cglightshow
                            ks "Deeper into sleep."
                            show HirokoHypno sleep
                            $ renpy.transition(longdissolve, layer="master")
                            $renpy.music.set_volume(0.1)
                            ks "Deeper into sleep..."
                            show HirokoHypno drooping sleep
                            $ renpy.transition(longdissolve, layer="master")
                            stop music fadeout 1.0
                            ks "That's good, Hiroko. Very good."
                            $renpy.music.set_volume(1.0)
                            play music Flow fadein 5.0
                            "Yeah, Hiroko. Very good dropping back into trance like that. It's almost like you were prepared to drop before I even started the induction."
                            "You just knew you had to follow along, didn't you? Just \"knew\" that you were helpless to stop yourself dropping back into trance."
                            "You're so easy to mess with. But don't worry, I'm going to keep my word."
                            ks "And now that you're back in this pleasant state of hypnotic trance, listening to my voice once more, I want you to reconsider the ticklish feelings of your palms."
                            ks "Remember that what you've been feeling isn't real. It's a mere construct of your mind to think you need to laugh when something touches your palms."
                            ks "So instead, I want you to let go of that construct. The palms of your hands are no more ticklish than they should be."
                            ks "You will experience a completely normal and natural sensation whenever your palms are touched. Understand, Hiroko?"
                            show HirokoHypno sleeptalk
                            h "Understand..." with dissolve
                            show HirokoHypno sleep
                            "And now to keep the other half of the little promise I made her..." with dissolve
                            ks "Very good, Hiroko. Still listening so closely. Still hypnotized so deeply."
                            ks "That's why you'll find that as I say you'll be compelled to come back and visit me every day after tennis practice..."
                            ks "... you will, inevitably and irresistibly, find yourself coming to see me at my house, so long as you don't need to be anywhere else after tennis practice."
                            ks "And when you arrive, you will be ready to become hypnotized by me again. Do you understand, Hiroko?"
                            show HirokoHypno sleeptalk
                            h "Yeah... I understand..." with dissolve
                            show HirokoHypno sleep
                            ks "So what will you do every day after tennis practice?" with dissolve
                            show HirokoHypno sleeptalk
                            h "Come see you at your house..." with dissolve
                            show HirokoHypno sleep
                            "It's as easy as that. After what happened with her hands, I'm feeling confident Hiroko won't think she can simply avoid me to stop what we're doing." with dissolve
                            "And as for getting some payback, I have just the thing for that gullible head of hers..."
                            ks "That's right, Hiroko. And there's something else that you need to listen to. Something else that you need to act on, while you remain so incredibly suggestible."
                            ks "Every day, while we're in our classroom at school and you don't need to use your phone, you need to keep it in your pocket and make sure it's set to vibrate."
                            ks "And every day, while we're in our classroom at school, if you feel your phone vibrate you will have an incredible urge to yawn."
                            ks "As you yawn in class, you'll find yourself feeling just a little sleepier than you were before. A little sleepier each and every time you yawn in our class."
                            ks "And as you feel a little sleepier, you will feel reminded of our times right here, Hiroko. You'll remember how hypnotized and sleepy you get around me."
                            ks "... Do you understand what you need to do in class now, Hiroko?"
                            show HirokoHypno sleeptalk
                            h "Y... y-yeah, I understand..." with dissolve
                            show HirokoHypno sleep
                            ks "I knew you would, Hiroko. You're taking in my every word, knowing how deeply hypnotized you are. How highly suggestible you are." with dissolve
                            ks "And because you're so hypnotized and so suggestible, you'll understand and accept one more thing."
                            ks "You'll accept that the moment you leave our classroom at the end of the day, any feelings of sleepiness you felt will be completely gone."
                            ks "You'll be wide awake, fresh and alert for your tennis practice. Completely fresh and alert, do you understand?"
                            show HirokoHypno sleeptalk
                            h "I understand..." with dissolve
                            show HirokoHypno sleep
                            ks "Excellent, Hiroko. Feeling so incredibly hypnotized. Feeling so incredibly easy to hypnotize." with dissolve
                            ks "Now in a few moments I'm going to have you wake up from this deep hypnotic trance."
                            ks "When you do, you're going to consciously remember every suggestion I made to you tonight, knowing I've only done what I said I'd do."
                            stop music fadeout 10.0
                            ks "Waking on the count of three, feeling good and relaxed and alert in one, two..."
                            ks "Three, wide awake, Hiroko."
                            show HirokoHypno relaxed sleepy_up_open
                            $ renpy.transition(longdissolve, layer="master")
                            "There's a low moan as Hiroko tilts her head back up and her eyelids drunkenly pull themselves back open."
                            h "Mmn... K-Kyou, you fuckin'..."
                            show HirokoHypno relaxed sleepy_up_closed
                            h "What did you..." with dissolve
                            ks "Relax, Hiroko. You know what I did."
                            show HirokoHypno frown
                            "I can see the frown on her face as the last few minutes likely flash through her mind, now that she has the luxury of thinking consciously about it." with dissolve
                            play music Eons
                            h "You..."
                            show HirokoHypno upright angry
                            h "I gotta yawn in class?" with dissolve
                            "I don't bother to hide the shit-eating grin that must be on my face as I shrug at her."
                            ks "See? I bet you thought I was going to do something way worse."
                            ks "And like I promised, your tennis career is going to be fine. We're just having a little fun with hypnosis here, aren't we?"
                            show HirokoHypno clenched_fists_tennis
                            h "Fuck off! {w=0.5}We ain't doing {nw}" with dissolve
                            extend "SHIT!" with vpunch
                            scene bg k room eve
                            show Hiroko tennis_armup furious at center:
                                ypos 1.3
                                linear 2.0 ypos 1.0
                            with blink
                            "Hiroko springs up from the couch with a snarl."
                            show Hiroko:
                                ypos 1.0
                            h "I don't fuckin' care what you said to me while I was asleep, you hear me?!"
                            h irritated "I ain't doing it. I'm not coming back here and I'm sure as shit not gonna yawn in class just 'cuz you told me to!" with dissolve
                            h furious "So you leave me the fuck alone!" with dissolve
                            h tennis "I'm fuckin' {nw}" with dissolve
                            extend "DONE with this shit!" with vpunch
                            hide Hiroko
                            play sound dooropen
                            with dissolve
                            pause 1.0
                            play sound doorclose
                            stop music fadeout 5.0
                            "I simply chuckle after her as she stomps out of my house, looking every bit as angry as when she came in."
                            scene bg k bedroom eve with blink
                            "I'm almost tempted to feel sorry for her."
                            play music Past_Sadness
                            "But whatever, I'm still keeping to the deal we made. She's still getting my help with her tennis and I'm still... getting her help for my hypnosis performance."
                            # "But whatever. She's still getting my help for her tennis stuff, just like she wanted. We're still keeping to our agreement when we started this. Sort of."
                            "She might not totally like what we're doing but I'm just going to mess with her for a bit; find out what she and I can do with hypnosis."
                            "Because with a subject like her... damn, it feels like so much is possible."
                            "It's enough to make me log on to this hypnosis chatroom I'm a member of."
                            "I've read a ton of useful advice from the people here. Not to mention all the interesting anecdotes others have shared about their hypnotic achievements."
                            "Usually I'm more of a lurker, and it's been a week since I last came to this place. But tonight I have a lot to say for myself and Hiroko. About all the things I've done with her..."
                            "Managing her anger issues, having her feel ticklish in weird places and this thing I'm doing now to make her yawn in class..."
                            "A few people congratulate me for finding someone to practice hypnosis on, but more of the responses I get back from the regulars cast doubt on what I'm saying."
                            "Yeah okay, so maybe all this seems pretty advanced for a young newbie hypnotist with his first subject..."
                            "But they don't know how amazingly suggestible Hiroko is. Not to mention how gullible."
                            "If only they could see her..."
                            "Well anyway, I'm logging out of there. I can't let them get to me, not when I have tomorrow to look forward to."
                            "A whole day of testing the reactions of my very real hypnotic subject. And getting a little revenge into the bargain, after all the shit she's put me through over the years."
                            "Oh man, this is gonna be so much fun..."
                            stop music fadeout 5.0
                            scene bg blackscreen with longdissolve
                            pause 2.0
                            #Sure, this is a little wrong of me, but after the shit she's pulled over the years, this is nothing.
                            #I'm just going to mess with her a bit
                            jump Day5_Con_Kyou_Hiroko_Trickster
                        "Just help her":
                            "I breathe a long and weary sigh as I feel her frightened gaze on me."
                            ks sigh "Alright, stop whining. I'll make it stop."
                            "Much as I hate to admit it, her desperate pleading is starting to make me uncomfortable."
                            show penlight at right with moveinright:
                                ypos 0.346
                            show HirokoHypno sad_closed
                            "And while it's really tempting to fuck with her gullible ass, I could probably get into a lot of trouble if I took it too far." with dissolve
                            "Better that I take a step back."
                            #This is the induction part from the standard ticklish hands route. Adjust the ending to reflect Hiroko staying scared and
                            #calling off their hypnosis sessions, causing Kyou to reflect ruefully on what happened and end the story prematurely.
                            ks frown "So, we'll put you back in trance and convince your subconscious self to let go of the tickling suggestion. Sound good?"
                            show HirokoHypno sleeptalk
                            "Hiroko lets out a sigh as she nods. Seems giving in to her demand has already done a lot to calm her down." with dissolve
                            h "Yeah... Yeah, just get it done."
                            hide penlight at right with moveoutright
                            ks frown "Alright then, so if you could sit back and focus as before?"
                            show HirokoHypno annoyed_up
                            "I can feel Hiroko's reluctance as she assumes a comfortable position, placing her hands on her lap with her palms facing upwards so she doesn't touch anything." with dissolve
                            call cglightshow
                            ks "That's right. Going back to this familiar feeling as I pass the light across your eyes."
                            call cglightshow
                            show HirokoHypno relaxed sleepy_up_open
                            $ renpy.transition(longdissolve, layer="master")
                            stop music fadeout 20.0
                            ks "So naturally... So easily..."
                            call cglightshow
                            ks neutral "So automatically, just letting the light patterns in your eyes take you deeper..."
                            call cglightshow
                            show HirokoHypno relaxed sleepy_up_closed
                            $ renpy.transition(longdissolve, layer="master")
                            ks "And deeper. There's no need to think about it."
                            call cglightshow
                            ks "Just letting your eyelids become heavy. Letting your head droop as you fall back into a deep, relaxing trance."
                            call cglightshow
                            # h "{size=16}Man, it's just like I thought...{/size}" with dissolve
                            show HirokoHypno relaxed sleep
                            $ renpy.transition(longdissolve, layer="master")
                            ks "Thoughts fading. Feeling so good as you drop deep, Hiroko. Deep asleep and ready to listen only to my voice. Only to my suggestions."
                            show HirokoHypno drooping sleep
                            $ renpy.transition(longdissolve, layer="master")
                            "I let that sit with her for a while as I think this over."
                            "Gotta get the phrasing right if I want to convince her she's no longer as sensitive as she thinks."
                            play music Flow
                            ks "And now that you're back in this pleasant state of hypnotic trance, listening to my voice once more, I want you to reconsider the ticklish feelings of your palms."
                            ks "Remember that what you've been feeling isn't real. It's a mere construct of your mind to think you need to laugh when something touches your palms."
                            ks "So instead, I want you to let go of that construct. The palms of your hands are no more ticklish than they should be."
                            ks "You will experience a completely normal and natural sensation whenever your palms are touched. Understand, Hiroko?"
                            show HirokoHypno sleeptalk
                            h "Understand..." with dissolve
                            # show HirokoHypno sleep
                            # ks "Very good. And while we're letting go of things, I want you to think on how you should feel on the tennis court." with dissolve
                            # ks "And as you think on them, remember how I told you to always stay calm while on the court, and to focus completely while playing a point."
                            # ks "You want to let go of all my suggestions, don't you, Hiroko?"
                            # show HirokoHypno sleeptalk
                            # h "Yeah... gotta let go." with dissolve
                            # show HirokoHypno sleep
                            # "I let out a quiet sigh. This really has been a waste of time after all." with dissolve
                            # ks "Then let go, Hiroko. You should find it effortlessly easy to let all my suggestions fall out of your mind."
                            # ks "You will think and act on everything however you see fit once again. Understand?"
                            # show HirokoHypno sleeptalk
                            # h "Yeah, I understand..." with dissolve
                            show HirokoHypno sleep
                            ks "Alright, then. So now on three you're going to come out of trance feeling refreshed and no longer feeling ticklish on your palms." with dissolve
                            stop music fadeout 10.0
                            ks "Waking in one, two... three, wide awake, Hiroko."
                            show HirokoHypno relaxed sleepy_up_open
                            h "Mrrh... You did it?" with dissolve
                            "I sigh, then reach out and quickly grab her hand off her lap."
                            show HirokoHypno scared
                            h "AGH! WHAT ARE YOU{w=0.5}.{w=0.5}.{w=0.5}.{w=0.5}{nw}" with shake
                            show HirokoHypno sleeptalk
                            $ renpy.transition(dissolve, layer="master")
                            extend " Ah okay, yeah."
                            play music Downtown
                            "I have to chuckle at the relief on her face as my fingertips trace her palm to no real effect."
                            ks smile "Better?"
                            h "Better... {w=1.0}{nw}"
                            show HirokoHypno upright blush angry clenched_fists_tennis
                            play sound slap
                            $ renpy.transition(dissolve, layer="master")
                            extend "A-And who said you could touch me?!" with vpunch
                            "I wince as she slaps my hand forcefully away."
                            ks sigh "You're welcome?"
                            show HirokoHypno nofists sad noblush
                            h "Y-yeah... Thanks." with dissolve
                            stop music fadeout 10.0
                            # "Not to mention, if she really does think the suggestions I've given her are beyond her own control...
                            scene bg k room eve
                            show Hiroko tennis sad at center:
                                ypos 1.5
                                linear 2.0 ypos 1.0
                            with blink
                            "And with that, she shakily rises back up from the couch."
                            show Hiroko at center
                            "Huh. I was bracing myself for another argument, but it looks to me like she doesn't know what to do with herself."
                            ks frown "What is it?"
                            play music Measured
                            h sad_side "... That was so fuckin' scary." with dissolve
                            h sad_talk "Like, you were seriously gonna leave me with fucked-up hands if I didn't beg you?" with dissolve
                            "I let out a sigh."
                            ks sigh "Come on, do you really think you were going to have insanely ticklish hands for the rest of your life?"
                            h frown "Don't say it like I'm stupid, asshole." with dissolve
                            h tennis_armup angry "Whatever you did, it messed me up good." with dissolve
                            ks "Hypnosis can't effect changes you don't want."
                            ks "I'm telling you, you really could've stopped it at any time without my help."
                            h furious "FUCK OFF!" with vpunch
                            h angry_side "You fuckin' lie to me, and... and shit, hypnosis is so fucked-up." with dissolve
                            ks frown "Hiroko, come on! You can't seriously think-{w=1.0}{nw}"
                            h furious "You keep the fuck out of my head, you hear me?" with dissolve
                            play sound dooropen
                            hide Hiroko with dissolve
                            pause 1.0
                            play sound doorclose
                            "She storms out of the house without waiting for an answer."
                            "And as I collapse on the couch my mind wanders..."
                            "There was no getting through to her. She really thinks hypnosis is dangerous now."
                            "Not to mention, she's probably going to go right back to telling everyone what a creep I am."
                            "A creep who now happens to be a dangerous hypnotist..."
                            "Fuck my life. Why did I EVER think getting involved with Hiroko was a good idea?"
                            jump Credits
                            # h tennis_armup furious "Don't fuckin' {nw}" with dissolve
                            # extend "LIE to me!" with vpunch


                    "AUTHOR's NOTE - And that's as far as I've gotten with this scenario. What do we think so far?"
                    "           TO BE CONTINUED!!!"
                    jump Credits
                    #This option she may actually start to plead with him to help her, and then Kyou begins to think that he can use this
                    #After all, if she's this suggestible to his hypnosis maybe there's more he can do with her
                    #He could tell her he'll help but it'll cost her, and before hypnotizing her he'll tell her what's going to happen to her in exchange for losing the tickle hands
                    #He wants to find out just how suggestible his nemesis really is...
            # "I sigh and hold my hands up in defeat. Honestly, I can still feel her fist on my cheek from last night."


            #Kyou follows back by smugly reminding her it only works because she wants it to. She calls bullshit.


        jump Day5_Con_Kyou_Hiroko

label Day4_Redemption:
    scene bg street1 day with longdissolve
    "The next morning comes, and I'm feeling like so much dogshit."
    scene bg ext school day with blink
    play music Measured
    "I don't walk to school so much as feel myself carried there, as my legs move on the path I've programmed into them for these past few years."
    "But as I roll up to the gates I'm confronted with a familiar sight."
    show Hiroko neutral_side at center, flip:
        xpos 0.25
    show Nozomi front at center
    show Sayori at center:
        xpos 0.75
    ks surprised "N-Nozomi!" with dissolve
    "Nozomi and her friends, arriving at school together."
    show Nozomi shocked
    show Hiroko surprised
    show Sayori surprised_right
    "Or... do they usually walk to school together? I don't recall..." with dissolve
    show Nozomi surprised
    h sad_side "Let's go..." with dissolve
    show Nozomi side sad_side
    show Sayori concerned
    n "Y-yeah..." with dissolve
    show Nozomi side sad_closed
    show Hiroko sleep
    show Sayori uniform_folded sleep
    with dissolve
    pause 0.5
    hide Nozomi
    hide Sayori
    hide Hiroko
    "My calling out only made them quicken their pace into the school. Fuck." with dissolve
    "I guess I'll see them in... class."
    scene bg corridor day with blink
    "Only I won't. I just reminded myself."
    "This is the door to class 3-C. It makes my stomach turn just looking at it."
    "Even if I barely knew anyone in 3-B, it was still like a second home to me. It was familiar."
    "But the thought of opening the door to 3-C? Of the unknowns that await me in there?"
    "I never should've agreed to this. I should have fought it."
    stop music fadeout 5.0
    show Akiko side neutral
    a "Ah, excuse me. You wouldn't happen to be Kyou Koyama, would you?" with dissolve
    "Maybe it's not too late. Like, if I don't go inside, this won't become my reality..."
    a sad "Um, hello?" with dissolve
    "Yeah, I'll just go back to Mr. Kobayashi. Say there's been a mistake and- {w=1.0}{nw}"
    a surprised "Hey, don't just ignore me!" with dissolve
    ks surprised "H-huh, what?!"
    "I heard a voice, but... huh. I didn't realize she was talking to me."
    play music Bright_Opening
    a uniform_down armband_down sigh "I said your name..." with dissolve
    a sad "Uh, I think? You ARE Koyama, aren't you?" with dissolve
    "I'm not used to girls approaching me voluntarily. Least of all the... student council president? That's her armband all right."
    "So this is Akiko Tsushima."
    "I've seen her around, but I don't think we've ever had cause to talk to one another, being from separate classes."
    ks sigh "Yeah, sorry. I'm just a little distracted, that's all."
    show Akiko smile
    "Akiko smiles politely at me, seemingly pleased to have cleared things up." with dissolve
    a "It's fine. I heard you're having a weird day today."
    ks surprised "You have?"
    a happy "Yup! I just came out of the teacher's lounge and they told me to expect a new student transfer, and also if I could help him settle." with dissolve
    a smile "So it's a pleasure to meet you, Kyou! My name is Akiko Tsushima, student council president and class representative of class 3-C." with dissolve
    show Risa smile_side at center:
        xpos 0.75
    show Akiko surprised
    r "Hey, 'Kiko. What's up?" with dissolve
    "Just then, another student appears beside us and breaks Akiko from her little introductory spiel."
    show Akiko uniform laugh noarmband at flip
    a "Oh, good morning, Risa~" with dissolve
    "So Akiko's in 3-C, huh? Then that means..."
    a smile_side "I was just going over some things with our new classmate." with dissolve
    "We're classmates now."
    r surprised "Oh yeah? New kid in school, huh?" with dissolve
    a smile "Well, not exactly. This is Kyou Koyama, he's just switching classrooms." with dissolve
    r neutral "Kyou..." with dissolve
    "I don't like the way this other girl says my name. It's like she's turning it over in her mouth while she's thinking of spitting it back out."
    a laugh "Maybe you'd like to be the first to welcome him?" with dissolve
    r frown "Yeah, no offence 'Kiko, but that's a hard pass from me." with dissolve
    "I knew it. She doesn't like me."
    a neutral_side "Oh?" with dissolve
    r uniform_armup sleeptalk "He's going to stand up in front of the class anyway, isn't he? He'll get his welcome then." with dissolve
    r uniform neutral_side "Anyway, I'm gonna go sit down. See you in there." with dissolve
    hide Risa
    a sad "Hmm. Right." with dissolve
    "Yeah. It's obvious everyone hates my guts. Just not everyone is comfortable saying it out loud, like Akiko."
    show Akiko uniform_down sleep
    "Probably some misguided sense of professionalism from having that armband." with dissolve
    a neutral "Hm, so where were we..." with dissolve
    ks neutral "You were just introducing yourself."
    a laugh "Ahaha, right~" with dissolve
    "Still, she's doing a good job of it. With that easy laughter of hers."
    a smile "So Kyou, obviously a student switching classrooms doesn't happen very often around here." with dissolve
    a happy "But we've agreed it would be best to just treat it like a transfer between schools." with dissolve
    "It's like she feels completely comfortable talking to an outcast like me."
    a smile "So that means when you walk through the door to our classroom, your new homeroom teacher is going to ask you to introduce yourself to the rest of us." with dissolve
    a neutral "I don't know how good you are with people exactly, but I was wondering if you'd be okay saying a few words?" with dissolve
    "Am I okay saying a few words? To people like that girl who clearly don't want me anywhere near them?"
    "Come the fuck on, what do you think?"
    ks sigh "I'm not... really..."
    show Akiko sad
    ks "I just don't know if I can stand there and... they all know me anyway, s-so..." with dissolve
    hide Akiko
    show Akiko side sigh at center
    "Akiko sighs as she turns towards the door." with dissolve
    show Akiko sad
    "Then she looks back at me with... I dunno, pity? Don't look at me like that." with dissolve
    a "Okay, I can't take too long because class is about to start but... listen."
    a sad_side "I don't know what happened that led to you needing to switch classrooms. That's not something our teachers are allowed to tell me." with dissolve
    a neutral "And I understand you're in a really awkward place right now, and I'm not going to mince words: Things are going to suck for a while." with dissolve
    a sleep "But it won't always be like that, Kyou. You got knocked down, it happens to everyone." with dissolve
    a neutral "You'll get back up." with dissolve
    a neutral_side "More to the point, if you really think everyone knows you, you're wrong." with dissolve
    a sleep "All I know about you is that you haven't done anything serious enough to get suspended." with dissolve
    a laugh_wink "So chin up, okay? It gets better." with dissolve
    a happy "Try to think of this as a fresh start. A new beginning." with dissolve
    "I let out a little chuckle. Yeah, this might be an act she's putting on for me, but it's a good one."
    "And I gotta admit, it's comforting that someone's willing to be nice to me, even if she thinks it's her job."
    show Akiko smile
    ks smile "Yeah, sure. We'll see." with dissolve
    play sound schoolbell
    stop music
    a surprised "O-oops!" with dissolve
    "Akiko's startled as the bell chimes for the beginning of homeroom period."
    a uniform_down armband_down laugh "Guess I overran a little, haha." with dissolve
    scene bg classroom2 day with blink
    play music Downtown
    "As we hurry into class, I'm immediately waved over by the teacher."
    $ t = "Ms. Chiba" #First surname I saw that I halfway liked the look of. Let's go with this~
    t "You must be Koyama. Welcome to class 3-C."
    ks smile "Ah, thank you, Miss."
    show Akiko side smile_side at center
    "It's just then that I notice Akiko lining up beside me." with dissolve
    a "I was just talking to Kyou about making an introduction. I'm fine to do it."
    t "Oh. Is that what you want, Koyama?"
    ks sigh "Y... Yeah."
    "My new homeroom teacher nods, apparently eager to just get this out of the way."
    t "Alright. The floor's yours, you two."
    scene AkikoIntro akiko2 worried with blink
    # show Akiko uniform_down armband_down neutral
    "As we head to the front of the classroom, Akiko turns to address me gently."
    a "{size=16}Um, by the way is there anything you want people to know about you? A hobby maybe?{/size}"
    "\"I'm not the creep you all think I am, so maybe just back off.\""
    ks confused "{size=16}Uh... I'm into computers?{/size}"
    show AkikoIntro sigh
    "Akiko sighs softly." with dissolve
    a "{size=16}Okay, fine. Stand here and face the class, please.{/size}"
    show AkikoIntro akiko1 frown
    "I do as she says, forcing myself to stand in front of this class full of disinterested faces as they chatter amongst themselves." with dissolve
    "But it's too much to look any of them in the eye, so I find myself glancing sidewards at Akiko, who stands beside me with a complicated expression on her face."
    "I mean, yeah... What the hell is there to say about me anyway?"
    # "I do as she says, as my eyes pass over the seemingly disinterested set of faces staring back at me, or at Akiko." with dissolve
    show AkikoIntro happy
    a "If I could have everyone's attention?" with dissolve
    show AkikoIntro akiko1 cheerful
    a "So as some of you may have heard, we have a new student joining us today." with dissolve
    a "His name is Kyou Koyama, and you may know him already. Because although he's new to our class, he's not new to our school."
    a "But even if you've heard of him, I thought it'd be good if we could still give him our warmest student transfer welcome!"
    a "Please treat Kyou as if you would treat anyone new to our school. With kindness, respect, and understanding."
    show AkikoIntro frown
    a "And, u-um..." with dissolve
    "Her lips crinkle in thought for a moment, before she nods gently to herself and continues."
    show AkikoIntro awkward
    a "Kyou is very passionate about computers, and I know he'd love to share that passion with some of you." with dissolve
    a "And I personally hope we can all get along and enjoy the rest of our school careers together!"
    show AkikoIntro smile
    a "Thank you all so much for listening~" with dissolve
    $persistent.akiko_intro_unlock = True
    scene bg classroom2 day with blink
    "Akiko starts towards her desk to scattered applause and I almost follow her when I realise I'm supposed to be finding my OWN desk."
    "I turn to Ms. Chiba and she helpfully points out the empty desk by the side wall."
    "Guess it was too much to hope for a window seat..."
    with blink
    "As the morning classes begin, one thought rings strongest in my head."
    "This is... ordinary."
    "I'm sat in a different place in the room, and the classmates are unfamiliar, but they regard me with the same indifference as my old ones."
    "Most of the teachers are the same as well. And I'm having no problem keeping up with our lessons."
    "Of course it helps that most of the classes are to review course materials for the upcoming mock exams, but still... ordinary is the vibe I'm feeling."
    "But it ISN'T ordinary. I can't forget why I'm here."
    "Nozomi and Hiroko are sat not far from me, in the classroom that used to be mine."
    "This will never be ordinary..."
    stop music fadeout 5.0
    play sound schoolbell
    with blink
    "The lunchtime bell rings and now I have to think about what to do for lunch while looking over my new classmates."
    "Most of them dash out, but I figure they'll be back in short order with some bread from the cafeteria."
    play music Eons
    show Risa smile_side at center, flip:
        xpos 0.25
    r "Hey, babe, what are we doing today?" with dissolve
    "That other girl is over there chatting to some athletic-looking dude."
    r neutral_side "Ehh, I'm not feeling it. We hung out with your crew yesterday." with dissolve
    "I can't be fucked to make out what the guy's saying, but..."
    r uniform_armup sleeptalk "... Yeah, and why not? I haven't lunched with her in ages, it's always..." with dissolve
    "They seem to be arguing?"
    r uniform frown_side "Christ, you're such a baby sometimes." with dissolve
    r concerned_side "... Ah, I didn't mean... Sorry." with dissolve
    r "Let's just go."
    hide Risa
    "The class barely reacts to any of that. Does this happen often between them?" with dissolve
    show Akiko side neutral at center:
        xpos 0.75
    "Even Akiko barely raises an eyebrow, seemingly focused on some paperwork on her desk." with dissolve
    "Student council stuff, maybe? I kinda wish I knew."
    hide Akiko
    "I wish I... damn, this is where it's really starting to sink in." with dissolve
    "Not having Nozomi around at lunch, seeing what she's up to."
    "Even that bitch Hiroko gave me a sense of familiarity. But no more. There's none of that now."
    "I'm so fucking lonely..."
    stop music fadeout 5.0
    scene bg classroom2 eve
    play sound schoolbell
    with longblink
    "I ended up eating alone at my desk. Which again, is no different from how life was at 3-B."
    "With lessons over, it's time for cleaning assignment. Only I realize..."
    t "Hmm, of course. Koyama's not on the cleaning rota yet."
    ks sigh "What should I do?"
    show Akiko side uniform_down armband_down smile at center
    play music Inspiration
    a "You could join me for today?" with dissolve
    "Akiko perks up as she overhears my predicament."
    t "That would work. You're on your own today aren't you, Tsushima?"
    a neutral_side "That's right. Kensuke was supposed to be with me, but he's sick." with dissolve
    a smile "So how about it, Kyou?" with dissolve
    "It's only two of them? I feel like I should ask some questions about this, but... eh, Akiko's been good to me today. I really don't mind joining her."
    ks smile "Sure, sounds good."
    show bg bathroom
    show Akiko side laugh at center
    with blink
    "Oh no, I DEFINITELY should've asked some questions about this."
    ks sigh "Cleaning the toilets? Really?"
    a uniform armband smirk "Oh, don't mope. You were going to wind up in here eventually. When you think about it, I did you a favour." with dissolve
    a laugh "Now you can get it over with~" with dissolve
    ks "You seem way too happy about cleaning in here."
    show Akiko uniform_down armband_down happy
    "Akiko chuckles as she sets down her cleaning bucket by the stalls." with dissolve
    a smile "Actually, I was kind of hoping we could talk." with dissolve
    ks neutral "Oh, yeah?"
    a smirk "I want to know about the new kid's first day in class." with dissolve
    "I find myself rolling my eyes as I plunge my mop into the bucket I brought with me."
    ks sigh "I mean, what's there to say? It's all pretty much the same as before."
    show Akiko sad
    ks "I go to class, put my head down, get ignored by all my classmates." with dissolve
    "I shrug."
    show Akiko neutral
    ks "It's all the same to me." with dissolve
    a uniform armband frown "A-{nw}" with dissolve
    extend "HEM!" with vpunch
    "Huh?! What's her problem?"
    a neutral_side "I think I need to remind you of the STUDENT in student council president." with dissolve
    ks surprised "Eh?"
    a neutral "... You know I'm one of your classmates, don't you?" with dissolve
    ks confused "Uhh... y-yeah?"
    "I wince inwardly as she admonishes me."
    "Honestly, after believing all this reaching out to me she's been doing is down to duty, I think I really did forget."
    ks sigh "Sorry. I, uh..."
    ks "I guess it IS hard to think of you as an ordinary classmate when you're the student council president."
    "Akiko nods her head thoughtfully while I explain myself, her expression softening."
    a uniform_down armband_down sigh "Right. Yes, I've had that problem before." with dissolve
    a neutral_side "Even some of the other student council members clam up on me sometimes. It's weird." with dissolve
    show Akiko smirk
    "As she sweeps her mop across the floor of one of the stalls she pauses a moment, before she looks to me with a grin." with dissolve
    a "Okay, Kyou. How about this?"
    show Akiko noarmband
    "She then unpins her student council armband and pulls it off, then balls it tightly into her fist." with dissolve
    a laugh "Now I'm but a humble student, just like you!" with dissolve
    "I let out a little groan and roll my eyes at her. It feels like she's mocking me."
    ks sigh "Oh come on, 'Kiko, that's fucking dumb."
    show Akiko smirk
    "... And yet, just the very fact that I felt comfortable mouthing off to her seems to suggest something that silly actually helped." with dissolve
    "Well alright, if she wants me to treat her like just another classmate then I think I can do that."
    ks smile "But alright, then. Could you tell me about yourself?"
    show Akiko smile_side
    "Akiko hums as she brings her mop back for another dip in the bucket, then starts to answer me while stepping inside the neighboring stall." with dissolve
    a "So, I turned eighteen a week ago. I've lived in this city all my life and I'm an only child."
    a smile "I was part of the choir in elementary school, and then in junior high I joined their kendo club." with dissolve
    ks surprised "Kendo?"
    "... You know, now that she mentions it, I can almost imagine her kitted in body armour and wielding a bamboo sword."
    a laugh "Yeah! It's hard going, and I get my butt whipped a whole bunch, but I enjoy it." with dissolve
    ks smirk "You... enjoy getting your butt whipped?"
    a sigh "I enjoy kendo, numbnuts. It's good mental prep." with dissolve
    a sleep "You don't like getting beat, of course. No one does. But you learn to appreciate how necessary it is." with dissolve
    a uniform smile "Each and every time you fail you simply bow to your adversary, ready your sword and try again." with dissolve
    "It really just sounds like she messes up a lot when she puts it like that."
    a smile_side "Anyway, I also enjoy reading fantasy novels, watching TV and playing a videogame or two." with dissolve
    a happy "What about you?" with dissolve
    "I can feel the tension in my spine when she turns the question around."
    ks sigh "I... well, I'm also into videogames, and I've always loved new technology. Computers, gadgets, robotics, anything like that."
    "This feels too short after what she said about herself."
    "Gotta think of something else."
    ks smile "I've also been studying hypnosis for about a year now. It's pretty interesting."
    show Akiko neutral
    "Wait..." with dissolve
    a surprised "Hypnosis, you said?" with dissolve
    "I didn't mean to blurt that out. Fuck."
    a neutral_side "That's... quite a leap from robots and gadgets, isn't it." with dissolve
    "But she was so encouraging and accommodating it completely lowered my guard."
    show Akiko neutral
    "And as she finishes in the stall she was in, our eyes meet as I stand frozen before her." with dissolve
    "What's she gonna think of me now?"
    a smirk "And I don't remember hearing about this at introduction, Mr. Computers." with dissolve
    "I let out a nervous chuckle as she mocks me, and as I study her expression I can't make out that she's in any way deterred by what I just said."
    a uniform_down smile "Well, I'm happy you're opening up a bit more. It's nice to meet you properly, Kyou Koyama." with dissolve
    a smile_side "I'm into psychology myself. Actually, I want to study to become a therapist when I get into college." with dissolve
    a happy "Maybe I could learn about hypnotherapy while I'm there." with dissolve
    "She lets the moment linger before snapping back to attention."
    a laugh_wink "Ahh, but we really need to finish up and head back to class now, don't we~" with dissolve
    ks smile "Oh, y-yeah. Haha."
    a smile "And, well, it was interesting talking to you. Maybe we could pick this up again sometime?" with dissolve
    ks smirk "And in somewhere better than a school toilet?"
    a smirk "Works for me." with dissolve
    stop music fadeout 5.0
    scene bg classroom2 eve
    with blink
    "As I make it back to my desk, I realize something..."
    show Akiko side uniform_down armband_down at right with dissolve
    play music Memories
    a "Stand!"
    a "Bow!"
    hide Akiko
    "For all my time so far with Akiko, I've been pretty comfortable talking to her?" with dissolve
    "Even when I was feeling intimidated by her status I still felt like I've held my own in our conversations instead of clamming up and having her turn away from me."
    scene bg street1 eve with blink
    "Thinking about that sure beats everything else that's been on my mind lately."
    "When I met her this morning, I thought Akiko was all talk. Some faculty-appointed busybody just doing her job to look good on her resumé."
    "But what we talked about back there had nothing to do with setting an example to the other students, or looking good for teacher."
    "That friendliness she showed me seemed... genuine. She really wanted to know more about me."
    scene bg k bedroom eve with blink
    stop music fadeout 10.0
    "I think I'd like to know more about her too..."
    scene bg blackscreen with longdissolve
    pause 2.0
    jump Day5_Redemption



        #Notes - Kyou mocking Hiroko's desire to be a tennis pro, prompting impassioned, angry retort
        #        Hiroko talking about Kyou to the other girls, prompting a confrontation?
