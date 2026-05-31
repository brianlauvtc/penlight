label Day1_Kyou:
    scene bg k bedroom night
    $nozomi_name = "Nozomi"
    "There. It's finished."
    "After months of careful tinkering I think I've come up with the perfect aid for my new hobby."
    scene cg kyou intro with blink
    "With this penlight, modified by my own hands, I should be able to capture someone's complete attention."
    "In doing so, I might be able to hypnotize them if they feel so inclined."
    "At least that's what I'm hoping. I won't know for sure until I can put it to the test."
    "... Oh, I should probably mention. My name is Kyou Koyama. I'm a senior high school student in my final year."
    "I am mediocre in almost every subject, have virtually no friends and I have terrible luck with girls."
    $persistent.kyou_intro_unlock = True
    stop music fadeout 5.0
    scene cg stageshow bw
    with flash
    "But after what I saw a year ago... at the culture festival. It gave me inspiration."
    "That's when I decided to learn hypnosis."
    $persistent.stageshow_unlock = True
    scene bg classroom day
    play music Bright_Opening
    show Sayori smile at center, flip:
        xpos 0.25
    show Hiroko smile_side
    with longblink
    h "Mornin', Sayori!"
    s "Good morning!"
    "But how do I go about this? I spent all my spare time reading about hypnosis techniques, watching video tutorials and hanging out in hypnosis chatrooms."
    "Not to mention all the hypnosis scripts I wrote, and of course all the work I've done on this penlight..."
    h "How was your weekend?"
    s concerned "Spent most of it cramming." with dissolve
    "... And I considered how to approach a girl with all of this, but..."
    h frown_side uniform_arm "That's gotta suck. Can't wait 'till all this shit is behind us." with dissolve
    "Thinking and doing are such different things."
    show Nozomi side smile_side at center onlayer toplayer:
        xpos 1.5
        linear 1.3 xpos 0.75
    n "Hey, you two~"
    hide Hiroko
    show Hiroko happy uniform_arm at center, flip
    show Sayori smile
    h uniform_armup "Nozo!" with dissolve
    s "Hey, Nozomi."
    "To say nothing of trying to do it with..."
    show Nozomi side at center onlayer toplayer:
        xpos 0.75
    n "Good weekends, I hope?"
    show bg blackscreen onlayer hilayer with dissolve:
        alpha 0.8
    "Her."
    hide bg blackscreen onlayer hilayer
    hide Nozomi side onlayer toplayer
    show Nozomi side smile_side at center:
        xpos 0.75
    with dissolve
    h uniform smile_side "Eh, not so bad. Got some good practice in for the tourney this weekend~" with dissolve
    n laugh "Oh, that's wonderful!" with dissolve
    "Nozomi Akemi, our class representative."
    "Height 157 centimetres. Blood type O. Her hobbies include karaoke, writing light novels and hosting board game nights."
    n smile_side "It's the big one, isn't it? I really hope you leave a good impression." with dissolve
    "And she's been single for the entire time I've known her."
    n "I've seen you in practice a few times; you look like you could give Naomi Osaka a game with those groundstrokes of yours."
    h laugh_side no_arm "Ahahaha, Nozo, you don't know {nw}" with dissolve
    extend "SHIT about tennis!" with vpunch
    "She's... never talked to me in my whole time at this school. Not properly anyway."
    n front uniform_folded pout "W-well, I thought you looked amazing. I don't know how you find the strength to hit like that." with dissolve
    "Although I tend to observe her frequently. After all, she IS our class rep."
    n side sad_side "I mean, don't take this the wrong way, Hiroko, but you look like a demon on the court. It's almost scary to watch!" with dissolve
    "Nozomi... She has this beauty, grace and kindness about her that's always intimidated me."
    "She seems so perfect. Unapproachable for a guy like me."
    h happy uniform_headhold "Kyahaha, I ain't taking that bad. 'Sides, my hitting partner Risa said pretty much the same thing~" with dissolve
    s uniform_handup smirk "We all say it when you are steamed about something." with dissolve
    hide Hiroko
    show Hiroko angry_side vein uniform_armup at center
    h "Yeah? {w=0.5}Well it ain't {nw}" with dissolve
    extend "MY fault the folks 'round here are so goddamned {nw}" with vpunch
    extend "ANNOYING!" with vpunch
    s uniform_folded smile "Ah yes, there is nothing like a dose of your demon rage to wake me up in the morning." with dissolve
    show Sayori happy
    h irritated "Pfeh!" with dissolve
    show Hiroko frown_side novein
    "But when I saw her last year, at that hypnosis show someone did at the culture festival... something clicked." with dissolve
    n smile_side "Oh, but what about you, Sayori? Still cramming?" with dissolve
    s annoyed uniform_folded "Of course. I am not sure I got enough sleep last night... You won't tell Mr. Kobayashi if I nod off will you?" with dissolve
    n happy "No promises~" with dissolve
    scene cg stageshow bw
    with flash
    "There was something about watching her fall into a trance for this other guy from our school. Something about her giving him her undivided attention..."
    "She enjoyed it, I could tell. I watched her intently the entire time, and it was practically written all over her face."
    scene bg classroom day
    show Sayori annoyed uniform_folded at center, flip:
        xpos 0.25
    show Hiroko frown_side uniform_armup at center
    show Nozomi side happy at center:
        xpos 0.75
    with flash
    s rolleyes "That is our class representative. Such a stickler for the rules." with dissolve
    n side laugh "Ahahaha, I'm kidding, I'm kidding!" with dissolve
    scene cg stageshow bw
    with flash
    "And sat there in the audience as I was, it gave me an epiphany."
    "I mean if that guy, a total stranger, could do that with her... surely she'd consider trying it with a classmate?"
    "This could be the thing that allows her to truly see me at last."
    scene bg classroom day
    show Sayori smirk uniform_folded at center, flip:
        xpos 0.25
    show Hiroko neutral uniform at center
    show Nozomi side smile_side at center:
        xpos 0.75
    with flash
    s "Oh, so what are you saying? Your friends can commit infractions and you would not report them?"
    s uniform_handup "Could it be our class representative is... corrupt?" with dissolve
    show Hiroko pain uniform_armup at flip
    h "Aw shit, it's a {nw}" with dissolve
    show Nozomi side surprised_side
    extend "SCANDAL!"with vpunch
    n frown_side blush "O-oh, knock it off, you two. Now everyone's looking at us." with dissolve
    "With everything I've learned since, I think maybe I can pull it off..."
    show Hiroko happy uniform_arm
    s uniform "Should be used to it by now, Nozomi." with dissolve
    h uniform_headhold2 "Kyahahaha~" with dissolve
    play sound schoolbell
    n side noblush smile_side "Meh. Well, that's the bell so you jerks go take your seats." with dissolve
    show Hiroko smile_side
    s smile "Yep." with dissolve
    hide Nozomi
    hide Sayori
    hide Hiroko
    with blink
    "As the morning marches on I've been thinking about how to approach Nozomi with this, in-between struggling with calculus."
    "I mean, I can't just say \"Hi Nozomi, will you let me hypnotize you?\"."
    "Even if she wanted to, she wouldn't say yes to that. Not with those friends of hers around us."# That isn't going to go down well, I know that much."
    "They just wouldn't understand."
    # "She'd never give me a chance if I just straight-up told her; she wouldn't understand what I've been doing."
    "So we'd have to meet privately somehow, then I'd have her full attention with nobody to disturb us and make things weird."
    "But before even considering all that, it still comes back to one thing..."
    show Nozomi side smile_side uniform at center:
        xpos 0.5
    show Sayori smile uniform_folded at center, flip:
        xpos 0.25
    show Hiroko smile_side uniform_arm at center:
        xpos 0.75
    n "So, lunch on the rooftop today?" with dissolve
    "I still need to approach her, period."
    s neutral "Hmm... is it not too cold?" with dissolve
    "Okay come on, Kyou, you've been planning this for months."
    "Just go up to her, make eye contact and say what you need to say."
    "You've got this."
    stop music fadeout 20.0
    n side laugh "The weather's fine, Sayori. We should make the most of it." with dissolve
    "I'll just... okay, so she's not looking my way right now."
    show Nozomi smile_side
    s uniform sleep "I am feeling low on energy today. Staying put would be preferable." with dissolve
    "But if I stand here she'll have to notice me."
    h frown_side "You're always \"low on energy\"." with dissolve
    "And then I'll have a chance to ask her."
    h smile_side "So c'mon, sis, get some air. You'll feel better~" with dissolve
    "... Maybe now isn't the right time. I could try this again later..."
    s smile "Alright. I will allow myself to be convinced." with dissolve
    "Later, when her friends aren't being so distracting."
    h uniform_armup happy "Woo, rooftop club! Let's do it!" with dissolve
    "Y-yeah, I'll just back away and- {w=0.5}{nw}"
    n front laugh "Haha, you make it sound like- {w=0.5}{nw}" with dissolve
    show Hiroko surprised
    show Sayori surprised_right
    extend surprised "A-ah!" with vpunch
    "Oh shit, she nearly walked right into me as she turned around."
    n front2 concerned "... Kyou." with dissolve
    play music Measured
    "For a moment I feel their gazes upon me as the three of them fall silent in an instant."
    show Hiroko uniform frown
    show Sayori concerned_right
    "... And now my stomach's in knots. Okay, I gotta do something." with dissolve
    h "C'mon let's get- {w=0.5}{nw}"
    ks frown "Er, Nozomi?"
    n surprised "Huh?" with dissolve
    "Okay, here we go."
    ks confused "N-Nozomi. I was thinking we could... t-that we could talk someplace?"
    n "O-oh, well... we were just headed to the roof, Kyou."
    ks sigh "I mean, uh... alone?"
    show Nozomi side sad_side at flip
    show Sayori concerned uniform
    show Hiroko frown_side
    "There's a slight pause as the three of them look awkwardly to each other." with dissolve
    n sad "Uh... I'm sorry, what would this be concerning?" with dissolve
    ks confused "It's kind of private? I guess?"
    show Sayori concerned_right
    h uniform no_arm frown "You guess?" with dissolve
    "The pink-haired girl's staring daggers at me, as usual. I just have to ignore her."
    ks "Y-yeah, so Nozomi would you mind coming with me?"
    hide Nozomi
    show Nozomi front frown uniform_folded at center
    n "I kinda do mind, actually." with dissolve
    ks sigh "Please? This won't take long."
    "Nozomi sighs."
    n irritated "Kyou, I'm going to lunch." with dissolve
    ks surprised "B-but, Nozomi-{w=1.0}{nw}"
    h uniform_armup furious "Take a hint, creep. {w=0.5}She said {nw}" with dissolve
    extend "NO!" with vpunch
    hide Hiroko
    hide Nozomi
    hide Sayori
    stop music fadeout 2.0
    "And with that, the three of them take off out of the classroom, leaving only the fading sounds of their voices as they move out of reach." with dissolve
    s "{size=14}Well, that was more awkward than his usual.{/size}" with dissolve
    h "{size=14}That fuckin' guy again. I thought he'd stopped doing this shit...{/size}"
    "Maybe I could find her on the roof, get her talking while everyone else goes back down, then maybe I'd have a couple minutes to..."
    "Oh, who am I kidding. She won't want to talk to me again after this."
    "It's hopeless."
    scene bg classroom eve with blink
    "So lunchtime came and went. The day's almost at an end."
    play sound schoolbell
    show Nozomi front sigh uniform_folded at right
    play music Memories
    n "And now cleaning duty..." with dissolve
    "Needless to say, today hasn't gone how I wanted it to go."
    show Hiroko neutral_side uniform at center, flip
    h "You're doing the classroom today, Nozo?" with dissolve
    n side sad_closed "*sigh* You know it." with dissolve
    "I'm not sure if I'll ever get a clear opportunity to show Nozomi what I've been working on."
    h uniform_headhold sad_side "And it's really just you and him? Ouchies." with dissolve
    n frown_side "I know. Must be some flu going around." with dissolve
    "Let's face it... I'm pathetic."
    h uniform_armup frown_side "I'm gonna rush my bit and come help you out!" with dissolve
    "To think I pursued this dream so I could get a girl to like me, and I'm THIS close to showing my work..."
    n smile_side "Don't worry, Hiroko; I'll be fine. Besides, you shouldn't \"rush\" this sort of thing." with dissolve
    "... But I still can't follow through."
    h uniform_headhold2 confused_side "Yeah? You sure?" with dissolve
    "Why did I ever think this would work? As if an opportunity's ever going to come my way..."
    n sad_closed "I'm sure. Let's just get this over with." with dissolve
    h smile_side "Alrighty. Good luck, Nozo~" with dissolve
    n smile_side "Heh, thanks. I'll see you in a bit." with dissolve
    hide Hiroko with dissolve
    show Nozomi at right:
        linear 1.5 xpos 0.65
    pause 1.5
    show Nozomi at right:
        xpos 0.65
    n front2 neutral "Hey, Kyou." with dissolve
    ks surprised "W-wait, what?!"
    n sigh "Are you daydreaming? Class is over and we're on cleaning duty in here. Come on!" with dissolve
    ks confused "Oh. Oh, right."
    "Lost in my own wallowing, I apparently missed the end of class."
    "As I get up from my desk and pack my books away I notice that Nozomi and I are the only ones who stayed behind."
    ks "Er... aren't there supposed to be more of us?"
    n frown "Yes, Shiro and Rie are off sick today. Just our luck they BOTH happened to be on classroom cleaning duty with us." with dissolve
    ks sigh "Seriously? This is a lot for just two people."
    n sigh uniform "It is what it is. Besides, Mr. Kobayashi said he'll be back in about ten minutes to help us out." with dissolve
    ks "Right, right..."
    n frown "Now come on, grab a cloth and let's get to work." with dissolve
    hide Nozomi with dissolve
    "With a sigh I do as she says, picking up a cleaning cloth as I set to wiping the desks while Nozomi moves to the front of the room to scrub the blackboard."
    "And that's when it hits me."
    "I've just had a halfway normal conversation with Nozomi Akemi, our class rep."
    "And she said we're basically going to be alone for a few minutes?"
    "There's some activity outside in the halls as people are cleaning, but they're not going to come back in here until it's time for homeroom."
    "This is my chance, right?"
    "But now my mind's racing..."
    "There's so much that could go wrong here. Our teacher could come back before we're finished and screw everything up."
    "Or more likely, I'll fuck this up myself and Nozomi will yell at me or something."
    "I could be forever known throughout the whole school as the idiot with the penlight."
    # "Or more likely, this won't work at all and I'll forever be known throughout the whole school as the idiot with the penlight."
    "People already talk about me like I'm some kind of creep. I don't need more weird rumours about me."
    "So maybe I don't need to show her this badly?"
    "... No, come on Kyou. You'll probably never get a better shot at this. Do you really want the last year of your life to have been for nothing?"
    "She's... she's going to like this."
    "I'll just approach her now and..."

    menu:
        "Attempt to hypnotize her with my penlight":
            "Okay, here goes nothing."
            show penlight at right with moveinright:
                ypos 0.346
            "Pulling the penlight from my pocket, I switch it on and stand directly behind her as she busies herself with the blackboard."
            hide penlight with moveoutright
            scene bg blackscreen
            with fade
            ks frown "Nozomi, can I show you something?"
            stop music fadeout 10.0
            $ldirection = "right"; lnumber = 1
            # $n = Character("nozomi_name", image = "NozomiHypno", who_color = "#93624B");
            $light_y = 0.28
            scene cg classroom eve
            show NozomiHypno folded stern
            with dissolve
            n "What is it, Kyou?"
            call cglightshow from _call_lightshow_61
            "As she turns to face me, I hold the penlight just above her eye level and gently sweep the beam across both of her eyes."
            ncg "What on earth are you doing?"
            ks smile "Just relax, okay? I think you're going to like this."
            call cglightshow from _call_cglightshow
            ncg angry "Kyou, I'm not here to play games with you. Stop goofing off and help me clean." with dissolve
            call cglightshow from _call_cglightshow_1
            "She's mad now, but... but I'm sure she just needs a little more time to realize what's happening here."
            ks "This won't take a minute. Trust me, you're going to find all this fascinating."
            call cglightshow from _call_lightshow_64
            show NozomiHypno stern
            play music Flow
            "Just like I practiced, I'm shining the little beam of light directly over both her eyes with a deft flick of my wrist." with dissolve
            ncg "Will you cut that out, Kyou? You could seriously hurt someone with that thing."
            call cglightshow from _call_lightshow_65
            ks neutral "This won't hurt, Nozomi. There's no need to get bent out of shape over a little light."
            call cglightshow from _call_lightshow_66
            ncg "I'm not- I'm not getting \"bent out of shape\" over a little light, Kyou, but you'd better explain yourself!"
            call cglightshow from _call_lightshow_67
            "I have to say that response makes me smile. It seems she really is going along with this whether she realizes or not."
            "I knew she'd be into this."
            call cglightshow from _call_lightshow_68
            ncg angry "Ugh, that is seriously annoying! Stop it!" with dissolve
            call cglightshow from _call_lightshow_69
            "So she says, but she hasn't made a move to turn away from me or block the light's path to her face."
            "She's mostly just standing still, her eyes looking slightly to the side towards the penlight in my hand instead of at me."
            show NozomiHypno stern
            ks "Just relax and focus on the light as it passes back and forth." with dissolve
            call cglightshow from _call_lightshow_70
            ks "Focus all your attention on it as you notice a pattern forming in your eyes."
            call cglightshow from _call_lightshow_71
            ks "And while you continue to focus on the light, and my voice, perhaps you haven't noticed how heavy your eyelids are becoming."
            call cglightshow from _call_lightshow_72
            show NozomiHypno standing confused
            $light_y = 0.3
            ncg "Kyou... what's going on here? This feels weird..." with longdissolve
            call cglightshow from _call_lightshow_73
            "Ignoring her words, I continue my memorized speech, trying to suppress my nerves to speak in as calm and level a manner as I can manage."
            ks "It's fine that your eyes are blinking more often, becoming more tired."
            call cglightshow from _call_cglightshow_4
            ks "It's appropriate to feel more tired, more sleepy, as you focus on the light passing your eyes."
            call cglightshow from _call_lightshow_74
            ks "With each passing of the light your eyelids become more and more tired. More and more heavy."
            call cglightshow from _call_lightshow_75
            show NozomiHypno drowsy
            $light_y = 0.32; light_x = 0.4
            "It's... it's working! She's really going for this!" with longdissolve
            "Okay, Kyou, stay calm. Keep doing what you're doing and she'll be under before you know it."
            ks "That's right, Nozomi. Feel how heavy they are. How much harder it is to open your eyes again."
            call cglightshow from _call_lightshow_76
            ks "{cps=15}Perhaps now it would be better if you just- {/cps}{w=0.3} {nw}"
            show NozomiHypno drowsytalk
            ncg "Kyou, stop this nonsense at once...  p-put that thing away." with dissolve
            "Her talking back gives me pause, but her voice is really soft. The kind of voice I'd expect her to use if she were talking in her sleep."
            show NozomiHypno drowsy
            "Like, maybe her conscious mind is saying no, but subconsciously? She's willing." with dissolve
            "She's willing to be hypnotized."
            call cglightshow from _call_lightshow_77
            ks "Shhh, Nozomi... it's alright. It's appropriate for you to feel this way around me. Feeling so relaxed. So drowsy. So sleepy."
            call cglightshow from _call_lightshow_78
            show NozomiHypno drooping sleepy
            ncg "W...what? I don't..." with longdissolve
            "So far my penlight seems to be having the desired effect, having kept her attention all this time."
            "But now, thanks to my words I can see it's taking all her conscious will just to keep her eyelids from snapping completely shut."
            $light_y = 0.36; light_x = 0.4
            call cglightshow from _call_lightshow_79
            ks "It's so much easier to relax and drift away, Nozomi."
            call cglightshow from _call_lightshow_80
            ks "With every pass of the light, it becomes even easier to focus on the light and my voice."
            call cglightshow from _call_lightshow_81
            ks "And with every pass of the light, your eyelids become heavier and heavier. So heavy. So hard to keep open now."
            call cglightshow from _call_lightshow_82
            show NozomiHypno drooping sleepy arm_uniform
            "As her eyelids continue to droop, I step a little closer and reach out to grab her shoulder." with dissolve
            "The last thing I want to happen is for her to fall over while she's spacing out."
            ks "With every pass of the light, it becomes even easier to relax. So much harder to keep those eyes open."
            call cglightshow from _call_lightshow_83
            ks "So much harder. So very hard to keep them open."
            call cglightshow from _call_lightshow_84
            ncg "..."
            ks "That's right, Nozomi. So nice and sleepy now."
            call cglightshow from _call_lightshow_85
            ks "With every pass of the light, even sleepier, even harder to keep those heavy eyelids open."
            call cglightshow from _call_lightshow_86
            ks "It's almost impossible to keep your eyes open now. Feeling so sleepy. Feeling so relaxed."
            call cglightshow from _call_lightshow_87
            ks "So sleepy... Sleep, Nozomi."
            ncg sleep "..." with longdissolve
            "I... I did it. I almost can't believe it's working just as I imagined it, but the dormant form of our class rep is all the proof I need."
            "Still, I can't savour my success or think about what this means. We surely don't have much time left."
            ks "Nozomi... can you hear me?"
            "The sound that escapes her lips is barely audible, but clearly in the affirmative. It excites me."
            ncg "Mhm..."
            "There's so much that I want to say to her. But I need to focus on what I can do in this moment we have together."
            ks "How are you feeling right now?"
            ncg "..."
            ncg sleeptalk "Annoyed..." with dissolve
            "That's interesting. What could she be annoyed at?"
            "Oh, I know."
            show NozomiHypno sleep
            ks "Of course you are. It's so annoying to be cleaning the classroom all by ourselves." with dissolve
            ks "But it's good to take a break and relax for a little while, especially after such a long day."
            ks "Don't you agree, Nozomi?"
            ncg sleeptalk "S..sure..." with dissolve
            show NozomiHypno sleep
            ks "And that's exactly what we're doing right now. I'm helping you relax and have a nice break, and there's nothing wrong with that." with dissolve
            ks "As a matter of fact, that's exactly what you need. You're feeling so much more calm right now without all that tension weighing you down."
            ks "Doesn't it feel nice to be so relaxed on your break with me?"
            ncg "..."
            ncg "Mhm..."
            "I'm grinning so wide right now. She took a moment, but she accepted the suggestion!"
            "Now I should try another quickly."
            menu:
                "Convince her that she needs a boyfriend":
                    "I'll never get a better chance to tell her how I feel, and what I'd like for us."
                    "She might be hypnotized, but that just makes this better; because I'm sure whatever her true feelings are, she'll reveal them now while she's this uninhibited."
                    # "Because I'll never get a better chance than this to show that she's been missing out for far too long."
                    "Before I wouldn't dare suggest this to anyone, let alone to someone like her."
                    "But now we're like this, I feel like we can finally have this conversation."
                    ks smile "So very nice and relaxing to be with me, Nozomi. Perhaps even more than that."
                    ks "In fact, this is how your boyfriend would make you feel when he's near you."
                    ncg sleeptalk "B... Boyfriend?" with dissolve
                    show NozomiHypno sleep
                    ks "That's right, Nozomi. Feeling so nice, so relaxed around someone you find safe. Someone you trust." with dissolve
                    ncg sleeptalk "I don't..." with dissolve
                    show NozomiHypno sleep
                    ks "Understand? Yes you do, Nozomi. You understand how right this feels; how so very safe and good and relaxed you are feeling around me." with dissolve
                    ks "So it makes sense that you would consider being in a relationship with me. Perfectly natural. Perfectly correct."
                    ks "Don't you think so, Nozomi?"
                    ncg sleeptalk "A relationship with... with you?" with dissolve
                    # ncg sleeptalk "B...But, I don't... don't want... a relationship..." with dissolve
                    show NozomiHypno sleep
                    "I smile at her reply. Just hearing those words back is making my heart skip." with dissolve
                    "There was trepidation in her voice, but the fact she didn't express disgust at the suggestion, or that she didn't simply wake up from this trance..."
                    "... The thought didn't repulse her. She HAS to be considering this."
                    "I'll push on."
                    # "She's being a little stubborn, but is that hesitation I hear?" with dissolve
                    ks neutral "It's natural that you're a little scared to be in a relationship, Nozomi. New things are scary."
                    ks "But there's no denying how relaxed you're feeling, is there, Nozomi?"
                    ncg sleeptalk "N-no..." with dissolve
                    show NozomiHypno sleep
                    ks "And there's no denying how safe you feel around me, is there?" with dissolve
                    ncg sleeptalk "No..." with dissolve
                    show NozomiHypno sleep
                    ks "No denying how good and right it feels to be near me like this..." with dissolve
                    ks "Is there?"
                    ncg sleeptalk "No... no denying..." with dissolve
                    show NozomiHypno sleep
                    ks smile "So then, {w=0.5}there's no reason to be scared of being in a relationship either, {w=0.5}is-{w=1.0}{nw}" with dissolve
                    "There's someone coming to the door. Shit!"
                    stop music fadeout 2.0
                    ks surprised "W-wake up, Nozomi!"
                    show NozomiHypno sleepy no_arm
                    play sound classdoor
                    "Nozomi's eyes flicker open as she looks at me in surprise, just as the door swings open." with dissolve
                    ncg "Kyou, what did you..."
                    t "Is everything alright in here?"
                    show NozomiHypno standing stern
                    "I hurriedly push my penlight back into my pocket, but I had been standing there in front of Nozomi with it still in my hand." with dissolve
                    "She must have seen it."
                    "She shoots me a look of... I don't know. Anger? Fear? A little of both? Before turning to respond to our teacher."
                    ncg "Everything's fine, Sir. I'm sorry we're behind on the cleaning."
                    $persistent.classroom_nozomi_unlock = True
                    scene bg blackscreen with fade
                    # $n = Character("nozomi_name", image = "Nozomi", who_color = "#D0755B")
                    "The next minutes pass in a haze."
                    "Nozomi says nothing to me as we set to work cleaning the room with our teacher's help. But I could tell she was keeping her distance from me."
                    "I had to wake her from her trance so quickly, without being able to finish my conversation with her subconscious mind."
                    "It must have been a bit of a shock for her, waking up like that, so..."
                    "I have no idea what she must be thinking now."
                    scene bg k bedroom eve with blink
                    play music Past_Sadness
                    "I'm still turning over what happened in my head as I lay on my bed at home."
                    "I failed, and I guess Nozomi might even hate me right now. And yet... it almost doesn't feel like I failed."
                    "I could hear it in her voice, as I was convincing her to give me a chance as her boyfriend. She was about to agree with me; she MUST have been!"
                    "If only I had a little more time to speak to her subconscious, she would've come around."
                    show penlight at right with moveinright:
                        ypos 0.346
                    "I don't care how I do it, but she NEEDS to have a second date with me and my penlight again."
                    hide penlight with moveoutright
                    scene bg blackscreen with longdissolve
                    stop music fadeout 3.0
                    "There's no escaping how she really feels about me."
                    pause 2.0
                    jump Day2_Villain_Kyou

                "Make her more receptive to being hypnotized later":
                    "Now that I know for certain that she's into this, I need to make sure we can do this again."
                    "I can't just hope for another opportunity like this to come around."
            "So if I can just impress on her how good this is; convince her we should do this again soon..."
            "... And what better way to do that than to give her a little post-hypnotic suggestion?"
            "Just a little one to prove I can do this. That WE can do this."
            "That'd be exciting, wouldn't it, Nozomi?"
            # "... Maybe I can even make this whole setup a little exciting for her. Convince her subconsious to keep all this quiet..."
            # "... Maybe she'll even agree to keep it a secret. After all, if her friends get wind of what we're doing they'll probably raise a stink."
            # "They'd ruin it for us."
            # "... And maybe convince her subconscious to keep it a secret for now. That'd be for the best."
            # "She wouldn't be ready to understand what I'm doing yet, and I think her subconcious mind would agree."
            ks smile "Enjoy yourself right now in the moment, listening to me, enjoying yourself on your little break with me. "
            ks "But at the same time, you should forget what we talked about, and everything that occurred during our meeting today."
            ks "You should feel free to forget everything else."
            ks "Instead, just remember how enjoyable it was to have a nice, relaxing talk with me. Remember how much you want to see me again so we can talk more."
            "I can hear some commotion in the halls outside. I really need to wake her now."
            ks "Can you do that for me, Nozomi?"
            ncg sleeptalk "Yes..." with dissolve
            show NozomiHypno sleep
            "I allow myself another little smile. I knew she'd be game for this." with dissolve
            ks "That's good, Nozomi. That's very good. Now I'm going to count up to five, and as I count up you are going to slowly return to wakefulness."
            ks "One... beginning to stir."
            stop music fadeout 15.0
            ks "Two... slowly feeling your senses return."
            ks "Three... beginning to test your eyelids as they start to lighten."
            show NozomiHypno sleepy
            ks "Four... so close to waking." with dissolve
            ks "And.... five."
            show NozomiHypno standing confused
            ncg "U-uhh?" with dissolve
            "I gotta say, watching her wake up on my say so is pretty hot."
            ks "I, uh.. I said we'll need to talk later, Nozomi. You're right, we have too much to do right now."
            # scene bg classroom eve
            # $n = Character("nozomi_name", image = "Nozomi", who_color = "#D0755B")
            show NozomiHypno smile
            with dissolve
            "She blinks a couple times, like she's still regaining her bearings, then gives me a sweet smile and an affirming nod."
            "She's never looked at me this way before."
            ncg "Of course, Kyou. Let's get to it."
            "As she turns to get back to work, I can see her eyeing the clock on the wall."
            ncg surprised "Oh crap, it's nearly been ten minutes and we've hardly done a {nw}" with dissolve
            extend "THING!" with vpunch
            $persistent.classroom_nozomi_unlock = True
            scene bg k bedroom eve with blink
            play music Memories
            "By the time I get back home I'm positively buzzing."
            "I did it. I really did it."
            "I take out the penlight from my pocket and turn it over in my hand, admiring my own handiwork."
            show penlight at right with moveinright:
                ypos 0.346
            "It's mostly just an ordinary penlight I bought online. All I did was make a few modifications to enhance the potential for distraction."
            "When people look into the beam, however briefly, it should induce a compulsive need to see it again. That was the theory anyway."
            "And it worked so beautifully on Nozomi. I feared I'd do nothing more than humiliate myself, but as it turns out I couldn't have wished for a better outcome."
            hide penlight with moveoutright
            "Nozomi... She never smiled at me before. It always felt like I was beneath her notice. That she'd never give me a chance on her own."
            "But now it will be different. Now that I've shown her that we have something in common she'll make time for me, and see how good I can be."
            scene bg blackscreen with dissolve
            stop music fadeout 5.0
            "Tomorrow can't come soon enough..."
            pause 2.0
            jump Day2_NonCon_Kyou

        "Try to talk to her":
            "N-no, I'll talk to her first. I don't need to show her my work right away."
            "I mean, without her friends crowding around her I can do this."
            # "The penlight I spent the last several months tinkering with for just this sort of occasion remains buried in my pocket as I continue to wipe the desks."
            # "But I NEED to talk to her. And I know she's not going to talk to me without a reason, so I gotta strike up a conversation myself."
            "So I just gotta strike up a conversation, right? Be casual about it."
            "At least say something first if she won't."
            # "But I can't just leave it like this, can I? I should at least strike up a conversation if she won't."
            show Nozomi side frown_side
            ks frown "So, er... Nozomi?" with dissolve
            n neutral "Hm?" with dissolve
            ks "How... how are you?"
            "There's an uncomfortable moment's silence as she finishes wiping down the blackboard, and takes both board erasers in her hands before replying."
            n side frown "I'm good. Kinda just going through the motions, though." with dissolve
            show Nozomi:
                linear 1.5 xpos 0.15
            pause 1.5
            show Nozomi frown_side
            "She walks over towards an open window, erasers in hand as she holds them outside ready to clap them together." with dissolve
            show Nozomi:
                xpos 0.15
            "It's almost robotic how she moves in this well-practiced routine, as if emphasising her statement."
            n "And what about you?"
            ks confused "Er... good. I'm good too."
            "Nozomi starts to clap the erasers together the moment I finished my sentence."
            n front2 frown "Could you start moving the desks aside? Thanks." with dissolve
            "I nod and start my own practiced routine as I begin to clear the desks."
            "... Is this all I'm going to say to her? After all this time?"
            "Come on, I gotta keep the conversation going."
            ks neutral "Soo...  got any plans for tonight?"
            show Nozomi side frown at flip
            n "Not so much. Watch some TV I guess; there's this new drama I've been wanting to check out." with dissolve
            ks "Cool. What's it about?"
            show Nozomi frown_side
            "She audibly sighs through her nose as she puts the erasers down beside the board, then moves to pick up a chair." with dissolve
            n "Some woman who builds a robot boyfriend or something."
            show Nozomi:
                linear 1.5 xpos 0.5
            "Nozomi shrugs her shoulders as she continues to move the chairs aside while I lift up another desk."
            show Nozomi frown:
                xpos 0.5
            n "And you? What are you doing tonight?" with dissolve
            "I wince inwardly. I can see how this conversation's going; just like she said, she's going through the motions."
            "Nozomi might be responding, but only as far as she has to out of politeness, I can see that."
            "She really doesn't give a shit."
            "But I can't let it play out this way. I should..."
            # "I can't let it play out like this. If only I could say something that would catch her attention..."
            menu:
                "Tell her I've been learning hypnosis":
                    ks "W-well, I'm probably going to... s-study hypnosis some more."
                    "There. What else could I do but say it?"
                    n "Okay."
                    stop music fadeout 10.0
                    hide Nozomi
                    show Nozomi at center
                    n front shocked "... Huh?" with dissolve
                    # "Ugh, why did I say that? Good job, Kyou, everyone thinks you're a creep already without you encouraging it."
                    show Nozomi front2
                    "But as I see the eyes dart back and forth in her head I'm realizing this might be a mistake after all." with dissolve
                    # "I can already tell what she must be thinking." with dissolve
                    "\"Why'd you want to study hypnosis? So you can hypnotize girls?\" THAT'S probably what she's thinking..."
                    "Which, oh right, wouldn't be far off now, would it?"
                    n surprised "..." with dissolve
                    "Goddammit, she's staring at me. What do I do?"
                    "My hand reaches into my pocket... I should show her what I've been working on, right?"
                    n front2 concerned "I... I see." with dissolve
                    play sound classdoor
                    show Nozomi side surprised_side at flip
                    "But just then the door swings open and Mr. Kobayashi appears in time to spare me from a potential grilling." with dissolve
                    "So I guess that was my ten minutes..."
                    scene bg street1 eve with blink
                    play music Sorrow
                    "Fuck. Fuck. Fuck."
                    "My one big chance to show Nozomi what I could do. My one big chance to even TALK to her."
                    "I fucking blew it."
                    scene bg k bedroom eve with blink
                    "I'm in no mood for anything when I get home."
                    "I crash on my bed and close my eyes, feeling numb all over."
                    scene bg blackscreen with dissolve
                    "Fuck everything."
                    stop music fadeout 5.0
                    jump Day2_Con_Kyou_Nozomi
                "Talk about the show she mentioned":
                    ks "Actually, I... I was thinking of checking out that show, too."
                    hide Nozomi
                    show Nozomi
                    n front neutral "Mhm?" with dissolve
                    "Yeah, I'll engage her stated interest. That's how you talk to someone, right?"
                    "Besides, I'm sure I know what show she's talking about."
                    ks smile "Yeah! I love robot sci-fi kinda stuff."
                    show Nozomi front2 smile
                    "She smiles politely as she lifts another chair off the ground." with dissolve
                    n "I'm really interested in how they handle the relationship between the two main characters. I want to see what direction they take it in."
                    ks "Oh... yeah, she's some nerd girl who builds herself that robot dude because she's lonely."
                    show Nozomi annoyed
                    "She snorts disdainfully as she sets her chair down on a growing stack of identical chairs with a clatter." with dissolve
                    n "Well that \"nerd girl\" seems like a tragic figure to me. Like a genius who lost her way."
                    n concerned "I mean, to think that she would take such a convoluted route to companionship. To believe that was her best option." with dissolve
                    n "You have to wonder what goes through someone's mind to think that was the case."
                    ks "Y... yeah. Still though, having somebody you could program to do what you want sounds pretty cool."
                    n surprised blush "Uhh..." with dissolve
                    "Nozomi seems to pause for a moment, another chair in her hands hovering an inch off the floor."
                    n irritated "Well... I can see why you might think that, Kyou." with dissolve
                    "She sucks in a breath, then starts to move again towards the chair stacks she's made for herself while turning to look at me."
                    n side frown "A-anyway, I'm not seeing much movement with those desks. You're slacking!" with dissolve
                    ks confused "Oh... s-sorry."
                    stop music fadeout 10.0
                    scene bg blackscreen with fade
                    "After that our conversation petered out. Our homeroom teacher came back shortly after anyway."
                    scene bg corridor eve with dissolve
                    "So that was it, huh? My one big chance to talk to our class rep and all I did was piss her off."
                    "Well, fuck. I don't even understand what was so wrong about what I said. Are girls always this hard to figure out?"
                    "Maybe... maybe it really is time I gave up. That girl is out of my reach, I've always known that."
                    "And I'm obviously too chickenshit to show her what I can do, in spite of all the work I put in."
                    "But what do I do now? I don't have an after school club to get to, so maybe I should just go home and live out the rest of my sad life."
                    "Or... maybe I could find something else to do with all this frustrated energy I'm carrying right now."
                    menu:
                        " (disabled)Go home":
                            pass
                        "Visit the study club":
                            play music Downtown
                            "What with entrance exams coming up sooner than later, I know I should start taking my studies more seriously."
                            scene bg study room eve with blink
                            "And with nothing better to do, I find myself walking into a room on the other side of the building that is being used for after-school study."
                            scene cg study room2 eve
                            show SayoriIntro
                            with blink
                            s "What?"
                            show SayoriIntro suspicious_closed
                            ks confused "Is... Is this the study club?" with dissolve
                            show SayoriIntro suspicious_open
                            s "Yes, this is the study club. For members of the study club." with dissolve
                            show SayoriIntro suspicious_closed
                            "This girl. She's one of Nozomi's clique, and the president of this particular club. Of course an overachiever like her would belong to a place like this." with dissolve
                            "Still, I'm not doing anything wrong. Am I really bothering her and the other club members by coming here?"
                            "There's room for one more. Or several more if this is all the attendance there is."
                            ks "I, uh... I know I'm not a member, but I thought I could maybe study with you guys?"
                            show SayoriIntro suspicious_open
                            s "Why us?" with dissolve
                            ks "What?"
                            show SayoriIntro sigh
                            "Sayori sighs and adjusts the textbooks she's cradling in her arms before continuing." with dissolve
                            s "The study club is focused on collectively advancing our understanding of specific subjects, Kyou."
                            show SayoriIntro suspicious_open
                            s frown_right "So if you are not here to expand your knowledge of geometry, then I suggest you visit the library." with dissolve
                            show SayoriIntro suspicious_closed
                            ks "Uh, geometry is good actually. I need to brush up on that." with dissolve
                            "She holds my gaze for a moment before letting out another laboured sigh."
                            show SayoriIntro sigh
                            s "Well... if you are actually here in good faith, then I will tolerate it. Pull up a chair, and try to keep up." with dissolve
                            $persistent.sayori_intro_unlock = True
                            # scene bg study room eve with blink
                            scene SayoriStudy sayori1 talking with longblink
                            "As everyone settles and takes out their reference books, the assembled members start to strike an orderly conversation on the finer details of the course material."
                            "It doesn't take long before I give up trying to follow the conversation and instead focus more on the club's president."
                            "She seems pretty focused as she looks over her books."
                            "And when the others are discussing a problem they're having she usually seems to be the one to help them out."
                            "But every now and then..."
                            show SayoriStudy sayori2 sleep with blink
                            # $scg = Character("%s"%sayori_name, image = "SayoriHypno", who_color = "#385599")
                            s "..."
                            $t = Character (_("Student"))
                            t "Is that right do you think, Sayori?"
                            s "..."
                            t "Sayori?"
                            show SayoriStudy waking
                            s "Mmn? Oh..." with dissolve
                            show SayoriStudy sayori1 smile_side
                            s "My apologies. Could you repeat that for me, please?" with dissolve
                            "It's obvious everyone notices, but it seems the people here just politely ignore the fact she keeps dozing off during the session."
                            "I must've caught her napping like, eight times in the hour we've been here."
                            "Does she do this in class, too?"
                            show SayoriStudy talking
                            with blink
                            "In any case after two hours of intensive study, and me barely understanding any of it, Sayori announces to the group."
                            s "Thank you all for coming. I hope we have all learned something new today."
                            show SayoriStudy smile
                            s smile "Have a good evening." with dissolve
                            $persistent.sayori_study_unlock = True
                            scene bg study room eve
                            show Sayori neutral
                            with blink
                            "As the room starts to empty, I watch Sayori again as she slides her books into her bag."
                            s neutral_right "... Are you not going to leave?" with dissolve
                            ks confused "Huh? Oh right, sorry."
                            "Realizing my mistake, I hurriedly grab my own bag and fumble with my books."
                            s frown_right "I am aware you have a reputation for staring at the cute girls in class." with dissolve
                            s uniform_handup smirk_right "So why were you staring at me?" with dissolve
                            "... Normally a line like that would come off as self-deprecating, yet somehow I feel like I'm completely the one being put down here."
                            "It sure helps for her that she has those hulking great bags under her eyes. Like, this girl can't be fucked to conceal the fact she looks like a goddamned zombie."
                            ks surprised "Sorry, I just..."
                            s uniform_folded frown_right "Just what, Kyou? I have been waiting to hear what really brought you to me." with dissolve
                            s frown "But I have a hunch it concerns a certain friend of mine. Did your little one-on-one session with her end in routine failure as expected?" with dissolve
                            ks confused "Uhh... what are you talking about?"
                            s irritated "And with no better ideas you decided to pursue the less threatening of her friends in the forlorn hope of finding an opening you could exploit." with dissolve
                            "Wait, does she seriously mean..."
                            ks surprised "What? No! Seriously, I wasn't thinking about Nozomi at all."
                            s frown_right "Really, Kyou? I find that so very hard to believe." with dissolve
                            "Fuck it. I'm too depressed to argue."
                            ks frown "F-fine. I don't care if that's what you think."
                            show Sayori concerned_right
                            "I slump back in my chair as I continue trying to force a book into my half-open bag." with dissolve
                            s frown_right "If you are telling the truth, then I am relieved. Now, if you don't mind? I would like the room." with dissolve
                            ks confused "What? Why? Aren't you leaving too?"
                            s sleep "This room is quiet this time of day and I have a little time. So I like to take a nap before I head to cram school." with dissolve
                            "As I close my bag I shoot her a look. Really?"
                            ks confused "You actually sleep here?"
                            s sleeptalk "Yes. On days when self-pitying crybabies are not around to stop me." with dissolve
                            "... I'm just gonna let that slide for now and focus on the main thing."
                            ks frown "Okay, that's just... that's nuts."
                            s uniform frown_right "Oh, you do not get to call me crazy, Kyou." with dissolve
                            ks "Yeah, but come on! You're telling me you do this on the regular? What would you call something like this?"
                            s irritated "Pragmatism. I like to optimise my time." with dissolve
                            s angry_right "Which is why I take it personally that you are wasting mine." with dissolve
                            ks confused "Sorry, I just... I kinda want to help."
                            s surprised_right "..." with dissolve
                            show Sayori uniform_handup laugh
                            "... I don't think I've ever heard this girl laugh before." with dissolve
                            s giggle "Okay, I will give you this; that was actually quite funny." with dissolve
                            s happy "The very idea that you are capable of helping me in any way, to say nothing of the notion that your motivations could be pure..." with dissolve
                            "I kinda blurted out that I wanted to help her, but now my mind's racing and the more I think about it..."
                            ks frown "No... no, I'm serious! We can help each other."
                            "The more I think I actually CAN help her, and make sure the last year of my life didn't go completely to shit."
                            s uniform frown_right "Kyou, has anyone impressed on you the value of quitting while you're ahead?" with dissolve
                            ks "And we wouldn't involve Nozomi or anyone else in any way. It'd be just between us."
                            "Sayori clicks her tongue as she looks me over."
                            s uniform_folded "\"Just between us\". You are piquing my interest, and I am resenting you for that. Go on." with dissolve
                            ks "Okay, well... it's like..."
                            "Oh man, how do I explain this? I didn't want to tell Nozomi I wanted to hypnotize her, so what makes Sayori any different?"
                            "She could tell everybody about the creep who wants to hypnotize girls, and Nozomi would hear about it anyway."
                            s angry_right "Remember what I said about time and optimization, Kyou." with dissolve
                            "... Fuck it. What have I got to lose at this point? Like people are gonna think any worse of me than they already do."
                            show Sayori frown_right
                            ks neutral "O-okay, so I've been studying hypnosis for a hobby." with dissolve
                            ks "And I'm thinking like, maybe I can use that to help you sleep better at night so you're not conked out during the day?"
                            s surprised_right "... What?" with dissolve
                            ks confused "I mean, you DO sleep at night, don't you?"
                            s neutral_right "For about three to four hours every night, as if that is any of your business." with dissolve
                            "And she's talking like that's normal?! Is she SERIOUS?"
                            "Wait, no, I can't say that to her. I gotta use more tact."
                            ks "Uh, okay. And do you think that's enough?"
                            s frown_right "Kyou, I do not think some cheap stage tricks are going to help me in any way, and I am gobsmacked that even you would think otherwise." with dissolve
                            ks surprised "What?! Stage tricks?"
                            "The hell does she mean by that? Unless..."
                            ks frown "No, I don't mean like what that guy did at the culture fest last year."
                            ks "What I'm talking about would be way more involved. The kind of hypnosis that can really help people effect a positive change in their lives."
                            s uniform_handup irritated "So... okay. It sounds like you are talking about hypnotherapy, which is performed by qualified professionals and not high-school students for a \"hobby\"." with dissolve
                            ks "Yeah... I guess. But really, what's the worst that could happen from this?"
                            ks "We try something, it doesn't work and you stay tired?"
                            s sleep "And I lose more time that I cannot get back." with dissolve
                            "She sighs, then draws a long breath in silence."
                            "Or she's napping again. Can't rule that out."
                            ks neutral "... Sayori?"
                            s uniform frown_right "I need to do a little research. We will meet here again, tomorrow, after club is dismissed. Do not return until then." with dissolve
                            ks surprised "Then you're agreeing?"
                            s frown "I do not promise anything, Kyou. But I will admit that this is unusual coming from you." with dissolve
                            s neutral_right "I am curious..." with dissolve
                            s sleep "Now would you mind leaving? I still have a little time left for a nap." with dissolve
                            scene bg street1 eve with blink
                            stop music fadeout 5.0
                            "I'm still not sure what just happened back there."
                            "I started today hoping to hypnotize the girl I've been watching from afar for years..."
                            scene bg k bedroom eve with blink
                            play music Past_Sadness
                            "... And ended up agreeing to hypnotize her ugly friend instead."
                            "Well... Okay, I guess she wouldn't look like so much shit if she took care of herself."
                            "A good night's sleep would surely be a start for her."
                            "Anyway, I'm gonna look up some more hypnosis scripts. See if I can find something specific to deep relaxation, or curing insomnia or whatever."
                            "Might as well take this seriously."
                            show penlight at right with moveinright:
                                ypos 0.346
                            "And at least I'll have a reason to use this, even if it wasn't the one I wanted."
                            stop music fadeout 5.0
                            hide penlight with moveoutright
                            scene bg blackscreen with longdissolve
                            pause 2.0
                            jump Day2_Con_Kyou_Sayori
                            # s frown_right "Oh come on now, Kyou. I am genuinely interested in the real reason you came here today." with dissolve
                            # s "I have a hunch, but I think you should just tell me."
                            # ks "It's like... I-I mean..."
                            # s "You will either tell me, or I will tell you. Pick one."
                            # ks "ALRIGHT! I'm just... I mean..."
                            # ks "Fuck, I don't know. I don't know anything, Sayori."
                            # s concerned_right "Well, I would not go quite as far as that." with dissolve
                            # ks "It's just I know I gotta step it up if I want to get a job when I get out of here..."
                            # s neutral_right "I take it your conversation with Nozomi did not go as well as you hoped." with dissolve
                            # ks "Huh?"
                            # s rolleyes "Kyou, you wanted to talk to her during lunch. You made a little scene over it." with dissolve
                            # s annoyed "But today's fortuitous cleaning arrangement ensured you had some one on one time with her, just like you wanted." with dissolve
                            # s "And from your mopey deameanor, plus the fact you are here at all, strongly suggests your time with her was a failure."
                            # s "So much so, that your only other avenue of pursuit is to approach those adjacent to her in order to find an opening you can exploit."
                            # s frown_right "So how did I do?" with dissolve
                        "Visit the sports clubs":
                            "I'll head outside and watch the sports teams doing their thing. Maybe that'll be enough of a distraction for now."
                            scene bg track eve with blink
                            "I take a leisurely pace as I walk around and idly watch the wannabe athletes turn out for their respective clubs."
                            "Soccer, track, baseball... all of the people in these clubs look so serious, like they really think they're going to make a career out of doing this stuff."
                            "Best they'll get out of all this is being able to put \"works well in a team\" on their resumés when they're trying for a salaryman position with all the other drones."
                            scene bg court eve with blink
                            "Eventually I find myself walking around the tennis courts."
                            play music Tennis
                            "Our school supposedly has a pretty good tennis pedigree. A few students from previous years have gone on to play professionally."
                            "Wouldn't think it from looking at the current crop, though."
                            "On one court, there's a couple ladies hitting some tame groundstrokes at each other."
                            "But I can tell they're getting distracted by what's happening on the court next to them, where some girl's getting pulverized by that pink-haired psycho from my class."
                            $t = Character (_("Tennis Girl"))
                            h "*sigh* Love forty. You gonna play me or what?"
                            t "I'm TRYING! If you could dial it back a bit? Please?"
                            h "Are you SERIOUS? The tourney's this weekend, gimme a fuckin' game."
                            "I look across court to see a very agitated-looking opponent mutter something under her breath, toss a ball into the air and smack it out wide to Hiroko's right."
                            scene cg hiroko_tennis1 with blink
                            "Hiroko, meanwhile, seems to anticipate this and immediately springs to her right."
                            "With a full-throated roar, she hits the ball solidly with what looks like a two-handed forehand." with vpunch
                            "I look back to the other side of the court in time to see the poor girl scream and drop to the floor just as the ball whizzes past her face."
                            "... Not that she could've known, but it was the right call as the ball bounces a good few feet out of bounds."
                            "Guess that makes it fifteen forty, then."
                            $persistent.hiroko_tennis1_unlock = True
                            scene bg court eve with blink
                            t "Hiroko! C'mon, are you TRYING to kill me?!" with vpunch
                            show Hiroko tennis_armup angry_side at center, flip
                            h "Geez, don't be a fucking wuss! Hit it back next time." with dissolve
                            "The other girl picks herself up off the hard court floor and turns her back exasperatedly as she storms off."
                            t "Oh my god, SCREW YOU! You ALWAYS do this!"
                            h furious_side vein "Hey, hey HEY! {w=1.0}{nw}" with dissolve
                            extend "DON'T YOU QUIT ON ME!!" with shake
                            "Hiroko holds a hand out to the air, as if she could grab her opponent and pull her back on-court."
                            play sound punch
                            "And when that doesn't work she futilely throws her racket against the net." with vpunch
                            h "BUNCH'A PANSY-ASS WIMPS!" with shake
                            stop music fadeout 5.0
                            "I look around and see one of the other players flub her return into the tape, then turn her attention to Hiroko with a grunt."
                            $t = Character (_("Tennis Girl #2"))
                            t "Will you knock that off? Some of us are here to play."
                            h "FUCK YOU! You want a game, I'll give you a fuckin' game. I'll take you BOTH on!" with vpunch
                            t "Ugh, you wish. Maybe you should ask your admirer instead. Didn't know you had a new boyfriend."
                            h angry_side "The fuck are you..." with dissolve
                            show Hiroko confused novein
                            "She swivels to look my way as the other girl chuckles and walks off to fetch a discarded ball by the tramline." with dissolve
                            "Shit."
                            show Hiroko frown
                            "Bracing myself for another explosion of shrill rage, I watch as Hiroko's face manages to darken even more as she stalks over to me." with dissolve
                            "What's she even gonna do? I haven't done anything besides watch her play. Is THAT a crime now?"
                            "Still, I know Hiroko thinks I'm shit, and she looks like she's in a mood to murder regardless of anything she thinks I've done."
                            # "And as I brace myself for the inevitable ragesplosion, Hiroko gets up in my face and starts to speak in a low gutteral growl."
                            h "And what the fuck do {nw}"
                            extend "YOU want?" with vpunch
                            ks "Uh..."
                            "I'm kinda done being intimidated by a girl, and one a full head shorter than I am at that."
                            "I've been on the receiving end of her foul-mouthed tirades too many times now."
                            "Still, her shrillness has a way of wearing you down."
                            ks frown "I was just taking a stroll and ended up here. There's nothing wrong with that, is there?"
                            h tennis "Everything's wrong when it's you. I bet you came here looking for some upskirt, you fuckin' perv." with dissolve
                            "This is another thing she likes to do. Always calling me the class creep, or somesuch."
                            "Apparently she doesn't like the way I look at the cute girls in our class."
                            ks "S-stop calling me that. Besides, you're wrong; I just wanted to check this place out. Maybe watch a game."
                            h frown_side "Uh-huh. Creepy-ass shut-in is suddenly all about sports now? Yeah, sure, I buy that." with dissolve
                            ks "Really? Well..."
                            "I pause a moment, wondering if I can really be bothered to talk back to her and get abused some more."
                            "But I'll just go ahead and say it."
                            ks "I don't see you doing much sport either. Just a lot of bullying."
                            h tennis_armup angry "The fuck you say?" with dissolve
                            ks "I mean, I thought it was just me you had it out for, but turns out you're just a bitch to everybody, huh?"
                            h "Yeah? That all you got, dipshit? Get outta here and stop wasting my time!"
                            ks angry "Y-you came to ME! If anything you're wasting MY time!"
                            h furious "You're just a waste of {nw}" with dissolve
                            extend "EVERYONE's time! Now get outta here and go jerk off, or whatever it is you do when no one's watching." with vpunch
                            ks "Ugh, r-... really Hiroko? Because from where I'm standing it looks like you're the one playing with yourself!"
                            t "Oh my god, GET A ROOM, YOU TWO!"
                            h furious_side blush "SAY THAT AGAIN, BITCH! SEE WHAT HAPPENS!" with shake
                            "I back away slowly, grateful for the brief respite as Hiroko turns her bile elsewhere for a second."
                            "But as she turns her attention back to me and I look over her still-trembling-with-rage form, the question just pops out of my mouth:"
                            ks confused "How are you STILL keeping this up?"
                            h frown noblush "Eh?" with dissolve
                            ks sigh "I mean, how have you not worn yourself out by now? Don't you want to dial it back before you have a stroke or something?"
                            h angry "You telling me to calm down? {w=0.5}Cuz I just {nw}" with dissolve
                            extend "LOVE it when dudes tell me to calm down." with vpunch
                            ks frown "Jesus, Hiroko I'm just, I dunno... I don't wanna say \"impressed\", but I wanna say something."
                            h frown "You can always shut up." with dissolve
                            "She snorts, then immediately takes a sharp breath; as if I suddenly reminded her to take in some air after all her screaming and posturing."
                            h tennis_headhold2 frown_side "S'all the energy I was s'posed to use for the game." with dissolve
                            h angry_side tennis_arm vein "Only some people, not naming names like, {w=0.3}I dunno,{w=0.3} {nw}" with dissolve
                            extend "KEIKO, can't fucking handle competition so here I am." with vpunch
                            h irritated "Rrrgh, I wouldn't be in this shit if Risa wasn't sick." with dissolve
                            ks neutral "So what will you do now?"
                            show Hiroko tennis frown no_arm novein
                            "She shrugs aggressively, then starts to pace towards the net where she left her racket." with dissolve
                            h "Like you give a shit."
                            ks frown"I guess not. It's just... I keep hearing you say you want to be a pro tennis player."
                            ks "But with this attitude? What a joke."
                            "... Maybe I shouldn't have said that, especially as Hiroko just picked her racket up off the ground."
                            show Hiroko frown_side
                            play music Tennis
                            "I know she heard me, but for a moment she simply stares ahead at the two girls who have resumed playing on the other court." with dissolve
                            show Hiroko angry
                            "But it doesn't take long for her face to darken once more, and she wheels around to face me, thrusting her racket towards my face." with dissolve
                            h tennis_armup furious vein "What the {nw}" with dissolve
                            extend "FUCK do you know, asshole? Like you know jack shit about any of this!" with vpunch
                            "As I take a step back, I wonder how low my life has gotten for me to be this suicidal. But I press on."
                            ks frown "I-I mean, like, do you think what you're doing is gonna fly on a real tennis court? The cussing and screaming?"
                            h "Get the {nw}"
                            extend "FUCK outta here! Like some perverted freak's gonna tell me how to behave." with vpunch
                            ks "And besides, you rage so much that you miss easy points. You don't need to be an expert to see that."
                            h "Yeah? Maybe I don't rage enough if {nw}"
                            extend "YOU'RE STILL HERE!" with shake
                            ks "I could help you!"
                            stop music fadeout 2.0
                            show Hiroko confused novein
                            h "..." with dissolve
                            ks "..."
                            t "..."
                            h tennis frown "Man, you really got a death wish today, don'tcha." with dissolve
                            # h "Oh, I just {nw}"
                            # extend "GOTTA hear how some know-nothing dipshit thinks he can help my tennis career." with vpunch
                            "I guess she's right about that. But a crazy plan's formed in my head and I'm not about to let go."
                            ks "U-uh well, it's like... I know a method that could make you a better player. If you want, I could share it with you."
                            h tennis_headhold2 confused "You even hearing yourself right now?" with dissolve
                            ks "Look..."
                            play music Tennis
                            "I glance at the other two ladies, who sure seem to be half-listening to us even as they've started playing again."
                            ks "I can't talk about it here. But I swear I can improve your game."
                            h tennis frown "This is a new level of weird for you, perv." with dissolve
                            "I'm still running my mouth off it seems. But the idea's in my head now."
                            "I'm determined."
                            ks "Look, what's it gonna take for you to hear me out?"
                            h tennis_armup irritated "How about you just..." with dissolve
                            "She stops and rolls her eyes before continuing."
                            h frown "Buy me a new racket." with dissolve
                            ks "What?"
                            h frown_side "You're full of shit, Kyou. If you wanna waste my time like this, buy me a new tennis racket." with dissolve
                            ks sigh "Really? You want a BRIBE?"
                            h tennis_headhold2 irritated "No, dude, I want you to fuck off. But if you ain't gonna do that, make it worth my time." with dissolve
                            h frown "'Sides, if you're serious about helping, getting me a racket that ain't busted to shit is gonna help way more than whatever it is you're thinking of." with dissolve
                            ks "I just..."
                            "This isn't anywhere close to being ideal, but for all her faults Hiroko is probably the only girl I can talk to, even if she mostly just yells at me."
                            "So like it or not, if I'm going to put any of what I learned over the last year to the test, she's probably my best shot."
                            ks frown "Okay."
                            h smirk "Dude, I was kidding. You ain't getting me a new racket." with dissolve
                            "Maybe this is completely stupid, but I've made up my mind."
                            ks "There's a sports store near here, right? We'll go right now."
                            h surprised "You're... holy shit, you're serious?" with dissolve
                            stop music fadeout 2.0
                            scene bg shopping eve
                            show Hiroko tennis frown
                            with longblink
                            play music Downtown
                            "And so I found myself walking with a bemused Hiroko to the sporting goods store."
                            h frown_side "You know I wasn't talking about the kiddy ones, right?" with dissolve
                            h angry "I want a {nw}" with dissolve
                            extend "PROPER one! Like the pros use." with vpunch
                            ks frown "Do you want a pony as well, princess?"
                            h tennis_armup irritated "I can go home!" with dissolve
                            ks sigh "Ugh, alright. Just tell me what one you want."
                            show Hiroko shocked
                            with longblink
                            h "Huh. You seriously..."
                            "As we leave the store, she cradles her expensive new racket, stroking the cover it's wrapped in."
                            show Hiroko surprised
                            "She looks at the racket cover, then to me, as she tries to make sense of what just happened." with dissolve
                            "I can't say I blame her. I'm feeling a little crazy with having dumped that much money on a girl I don't even like."
                            h annoyed "So you're a {nw}" with dissolve
                            extend "RICH creep, is what I'm getting from this." with vpunch
                            ks angry "Oh, come on! Really?"
                            h tennis frown "What, Kyou? You think this makes it all better?" with dissolve
                            "Uggh, this unbelievable little bitch."
                            h irritated "Like, you can just buy me shit and I'm gonna be all..." with dissolve
                            h tennis_armup surprised "\"Ohh, Kyou, you're so dreamy! Let's bang!\"" with dissolve
                            h frown "Fuck off." with dissolve
                            ks "Wh- What?! You're the last person I..."
                            "I trail off. This is just embarrassing."
                            "Hiroko lets an uncomfortable silence linger for a bit before she pipes up."
                            h tennis annoyed "So what's this big idea of yours?" with dissolve
                            ks frown "It's... just promise you'll hear me out, okay?"
                            h confused "Dude, with all this build-up and a free tennis racket?{w=0.5} I {nw}" with dissolve
                            extend "NEED to hear this!" with vpunch
                            ks "Okay, well you see, I've been doing a lot of research on hypnosis in my spare time, and I think I know enough that I can use it to help you."
                            "I pause for a moment and gauge Hiroko's reaction, which looks somewhere between confusion and disgust."
                            h angry "Hypnosis? {w=0.5}{nw}" with dissolve
                            extend "THAT's what this is about?" with vpunch
                            ks "Y-yeah. So what I was thinking was, I could help you keep your cool a bit, just a little, so you don't lose focus during a game."
                            ks "And maybe so you don't piss off your opponent before the match is over."
                            h tennis_armup angry_side "Fucking. {w=0.5}Pansy-ass. {w=0.5}Wimps." with dissolve
                            ks "You don't think it'd help?"
                            "She sighs and looks down at the racket in her hands."
                            h tennis concerned "Dude, I ain't stupid. I know I run a lil' hot sometimes and it gets me in trouble." with dissolve
                            h tennis_headhold2 nervous "But seriously? That's your great plan?" with dissolve
                            h frown "Like what, you swing a pocketwatch in my face, tell me I'm gettin' sleepy and all of a sudden I'm hot shit?" with dissolve
                            ks "I don't have a pocketwatch, and if you take it seriously it could work? This kind of thing helped people before."
                            h confused "'Kay, but like... fuckin' why, dude?" with dissolve
                            ks "Uh, why what?"
                            h tennis "Why all this!?" with dissolve
                            show Hiroko tennis_armup surprised_side
                            "She waves her racket around and almost clocks a passer-by with it, prompting her to raise a hand in rushed apology before turning back to me." with dissolve
                            h frown "Like, if you're gonna follow me around and buy me shit, you gotta be pretty desperate, huh?" with dissolve
                            ks "I... I guess."
                            "She rests the racket back in her arms again, then lets off a long shrug."
                            h tennis_headhold2 sleeptalk "Welp. If this is what you wanna do with your money, don't lemme stop ya..." with dissolve
                            scene bg court night with longblink
                            "It's getting dark by the time we make it back to school."
                            scene bg sports storage
                            show Hiroko tennis neutral
                            with blink
                            "Hiroko leads me to a storage shed being used for sports supplies."
                            h tennis_headhold neutral_side "So if you wanna do this, how 'bout in here?" with dissolve
                            h frown "Just don't take too long. I don't wanna get locked up in this place." with dissolve
                            play sound doorclose
                            "I close the door behind me as I look around. It's not ideal, but..."
                            ks frown "Yeah... Yeah, okay, this could work."
                            h tennis_armup angry "And don't get any pervy ideas about being alone with me, or this racket you bought is gonna be the last thing you see." with dissolve
                            "... It just occurred to me how a boy and a girl sneaking into here at night might look if someone saw us."
                            ks sigh "Ugh... yeah, message received. Don't worry."
                            h frown "Cool. So where's the pocketwatch?" with dissolve
                            ks frown "I told you I don't have a pocketwatch!"
                            h tennis frown_side "The other guy had a pocketwatch." with dissolve
                            ks "Well I don't... wait, what other guy?"
                            h tennis_headhold2 annoyed "Y'know? There was that guy last year who did the hypno stuff. HE had a pocketwatch!" with dissolve
                            "Wait. She must be talking about..."
                            ks smile "Oh, from the culture fest last year. Yeah, I remember that..."
                            h annoyed_side "Uh-huh. Dude got a bunch of people to make animal noises and laugh at stupid shit." with dissolve
                            ks "And, uh, what did you think of that?"
                            h angry "Bunch'a idiots giving in to peer pressure! If it was me up there I'd have told the dude to go fuck himself." with dissolve
                            h annoyed "I'd do the same for you too, but we got this deal going, so let's just get this over with." with dissolve
                            "I'm feeling worse and worse about this by the minute."
                            show penlight at right with moveinright:
                                ypos 0.346
                            "But I knew what I was getting into. I just have to work with what I've got."
                            h smirk "Oh, wait wait, {w=0.2}{nw}" with dissolve
                            extend "THAT'S your pocketwatch?" with vpunch
                            ks sigh "Ugh... Yes, if that's what you want to call it. I'm going to shine the light in your eyes to hypnotize you."
                            hide penlight with moveoutright
                            h annoyed "Riiight. So what have I gotta do?" with dissolve
                            ks frown "Just get comfortable and try to take this seriously, okay? Give it a chance."
                            scene cg sports shed night
                            show HirokoHypno upright tennis annoyed nofists
                            with blink
                            $hcg = DynamicCharacter("hiroko_name", image = "HirokoHypno", who_color = "#FF89AB") #Hiroko Homura
                            "She shrugs and sits herself against a pile of crash mats, regarding me with a bored expression."
                            hcg "'Kay. Knock yourself out."
                            "I almost don't want to go through with this now. It's been a long day and this little shit has really done a number on my mood."
                            ks neutral "Okay. Okay, so I want you to watch the light with your eyes."
                            "I say, as I click the penlight on and hold it above her head, shining it downwards towards her brow."
                            ks "No, don't move your head. Just your eyes."
                            hcg frown "If I do that I'm gonna get eyestrain, fucko." with dissolve
                            ks frown "That's kind of the point, so could you- {w=0.8}{nw}"
                            hcg clenched_fists_tennis angry "What? How is fucking up my eyes gonna help me play better, genius? Gawd, you suck at this." with dissolve
                            ks angry "Oh, for f-..."
                            "Okay, deep breath. Just get through this."
                            ks "For a free tennis racket, could you PLEASE just do this for me?"
                            hcg angry_up "Ugh, {nw}" with dissolve
                            extend "FINE, I'll do it. Jesus..." with vpunch
                            show HirokoHypno annoyed_up nofists
                            "As she sulkily complies I take another breath. Now to try and somehow induce her into trance." with dissolve
                            "I just hope all this hasn't fucked up my routine."
                            $light_y = 0.3
                            call cglightshow from _call_cglightshow_105
                            ks neutral "Now, Hiroko, it really isn't hard to look up at the light."
                            hcg clenched_fists_tennis angry "Don't fuckin' patronize me!" with dissolve
                            ks frown "Hiroko, this is part of the induction. I wasn't patronizing you!"
                            call cglightshow from _call_cglightshow_106
                            "Deep... breath...."
                            "Wait, that's what SHE'S supposed to be doing!"
                            ks "Just listen and watch. I'm not here to patronize; I'm here to help."
                            call cglightshow from _call_cglightshow_107
                            ks "And all you need to do is take a nice deep breath with me..."
                            hcg annoyed_up "Mhrm..." with dissolve
                            call cglightshow from _call_cglightshow_108
                            ks "That's it. And watch the light as it passes your eyes, letting your breath out slowly..."
                            call cglightshow from _call_cglightshow_109
                            $ renpy.transition(longdissolve, layer="master")
                            hcg relaxed_fists_tennis surprised "H-huh, that's trippy..."
                            ks "That's right, Hiroko. Easiest thing in the world to just breathe in deep..."
                            call cglightshow from _call_cglightshow_110
                            ks "And stare, and exhale..."
                            call cglightshow from _call_cglightshow_111
                            show HirokoHypno drowsy nofists
                            $ renpy.transition(longdissolve, layer="master")
                            ks "And relax deeply. Easiest thing in the world..."
                            $renpy.music.set_volume(1.0)
                            call cglightshow from _call_cglightshow_112
                            $renpy.music.set_volume(0.9)
                            "Despite everything, she does seem to be paying attention and listening, as I can see her chest rise and fall at my direction. Progress."
                            ks neutral "And as you relax, as you take another deep breath now..."
                            call cglightshow from _call_cglightshow_113
                            $renpy.music.set_volume(0.8)
                            "I pause a moment, then just as her eyelids flicker, I continue."
                            ks "You may notice that your eyelids are starting to droop. Starting to become heavy..."
                            call cglightshow from _call_cglightshow_114
                            $renpy.music.set_volume(0.7)
                            ks "And as you exhale, you may find yourself relaxing more and more as your eyelids become heavier still..."
                            call cglightshow from _call_cglightshow_115
                            $ renpy.transition(longdissolve, layer="master")
                            $renpy.music.set_volume(0.6)
                            hcg relaxed "G... gettin' sleepy..."
                            "... Is she fucking mocking me? No, don't think about that. Carry on."
                            $renpy.music.set_volume(0.5)
                            ks "That's right, Hiroko. You're probably feeling a deep pull towards falling asleep right now as you let the breath out of your body."
                            call cglightshow from _call_cglightshow_116
                            $renpy.music.set_volume(0.4)
                            ks "And that's perfectly alright. So why not take another full, deep breath..."
                            call cglightshow from _call_cglightshow_117
                            $renpy.music.set_volume(0.3)
                            ks "That's right, and as you feel your eyelids become so heavy. So hard to open, breathe gently out for me."
                            call cglightshow from _call_cglightshow_118
                            $renpy.music.set_volume(0.2)
                            ks "Feeling so close to sleeping, eyelids so heavy that they may simply become too much effort to open again."
                            call cglightshow from _call_cglightshow_119
                            show HirokoHypno sleep
                            $ renpy.transition(longdissolve, layer="master")
                            $renpy.music.set_volume(0.1)
                            "As Hiroko's eyelids flutter closed, I wait a moment, then put my penlight down at my lap and continue."
                            ks "That's very good, Hiroko. Feeling that pull towards sleep completely irresistible as you find yourself dropping deeper."
                            stop music fadeout 2.0
                            ks "Deeper... nice and deep asleep, Hiroko."
                            $renpy.music.set_volume(1.0)
                            play music Flow fadein 5.0
                            show HirokoHypno drooping
                            $ renpy.transition(longdissolve, layer="master")
                            hcg "..."
                            "I can't quite believe I did it, but she really does seem to be under."
                            "So... okay, if I assume she's taken this seriously at last, then I should impress on her the need to keep the red mist at bay."
                            "That alone is gonna help her game."
                            ks "Now Hiroko, I want you to think about your times on the tennis court."
                            ks "Remembering the matches you played, and your practice sessions. Remembering how they make you feel."
                            ks "Can you do that for me, Hiroko?"
                            hcg sleeptalk "Yeah..." with dissolve
                            show HirokoHypno sleep
                            ks "That's great. And while you're thinking and remembering those times, I want you to think about the times on the court where you..." with dissolve
                            ks "... perhaps lost your temper?"
                            #Might be good to have a sleep frown expression here
                            "I can see Hiroko's brow crease as she processes what I'm saying."
                            ks "Can you recall those times, Hiroko?"
                            hcg sleeptalk "Y... yeah..." with dissolve
                            show HirokoHypno sleep
                            ks "I know it's hard, Hiroko, but that's okay." with dissolve
                            ks "And while you're thinking of these times, I want you to think of how much better it would have been had you not lost your temper."
                            ks "The points you may not have lost, or the penalties you might not have incurred."
                            ks "It would have been better if you were calm in those moments, wouldn't it, Hiroko?"
                            hcg sleeptalk "Yeah... s-sure..." with dissolve
                            show HirokoHypno sleep
                            ks "That's right. So now, Hiroko, I want you to sink back into deep relaxation. Feeling so very calm." with dissolve
                            "I wait a moment and watch as the frown seems to melt off of Hiroko's face."
                            "After all the fighting to get us to this point, seeing her co-operate now is really encouraging."
                            ks "Very good. And now, whenever you are on the tennis court and you feel like you are about to lose your temper..."
                            ks "I want you to, just for a moment, return to this nice deeply-relaxed feeling."
                            ks "Anytime you are awake and on a tennis court, and you feel you are going to lose your temper, feel this deeply calming experience instead for a moment."
                            ks "Let it bring you right back to a state of peace."
                            ks "Do you understand, Hiroko?"
                            hcg sleeptalk "Y-yeah... understand..." with dissolve
                            show HirokoHypno sleep
                            "Well, I gotta say I wasn't expecting her to really go along with this as well as she has. I just hope she's seriously taking this stuff to heart." with dissolve
                            "But in any case, we need to get out of here. I don't want to get locked in at this school either."
                            ks smile "That's great. Now, I am going to count up to five. On five, you will wake feeling nice and refreshed and alert once more. Understand, Hiroko?"
                            hcg sleeptalk "Yeah..." with dissolve
                            $renpy.music.set_volume(1.0)
                            show HirokoHypno sleep
                            $renpy.music.set_volume(0.8)
                            ks "One... taking a nice breath in and out." with dissolve
                            stop music fadeout 10.0
                            $renpy.music.set_volume(0.6)
                            ks "Two... feeling the energy start to return to your hands and feet."
                            $renpy.music.set_volume(0.4)
                            ks "Three... starting to test your limbs as you stir yourself towards wakefulness."
                            show HirokoHypno relaxed
                            $renpy.music.set_volume(0.2)
                            $ renpy.transition(longdissolve, layer="master")
                            ks "Four... testing your eyelids, so close to waking."
                            $renpy.music.set_volume(0.1)
                            ks "And five, awake and alert, Hiroko."
                            stop music fadeout 2.0
                            hcg neutral "..." with dissolve
                            "I chuckle as I see her round eyes flutter back into life. If she was pretending to be under to me, she must've been awfully committed."
                            ks "Wakey wakey, Hiroko."
                            $renpy.music.set_volume(1.0)
                            show HirokoHypno upright frown nofists
                            play music Downtown
                            hcg "What? Shut up." with dissolve
                            ks "How are you feeling?"
                            hcg annoyed "Pissed off." with dissolve
                            hcg frown "Like, I wasted a whole day of tennis training to go on a shopping trip." with dissolve
                            hcg annoyed_up "Then I had to play this weird-ass game with you." with dissolve
                            "I can't help but sigh."
                            ks sigh "Is that it?"
                            hcg frown "Yep. We going now? 'Cuz I told you I don't wanna get locked in here." with dissolve
                            $persistent.sports_shed_night_unlock = True
                            scene bg school ext night
                            show Hiroko tennis frown_side
                            with blink
                            h "So, uhh..."
                            "As we head out the school gates, Hiroko looks again to the racket I bought her."
                            stop music fadeout 5.0
                            h tennis_headhold2 sleeptalk "Thanks for this. But I gotta say..." with dissolve
                            h annoyed "Get another hobby." with dissolve
                            scene bg k bedroom night with longblink
                            play music Past_Sadness
                            "So that's it, huh? An entire evening and a ton of cash wasted on that goddamned brat."
                            "Why did I think this was something worth doing?"
                            "I mean, shit, maybe she's right. I'm wasting my life with this stupid crap; I could find something else to do."
                            "Right now, though, I just want to sleep and drain this entire fucking day out of my head."
                            stop music fadeout 5.0
                            scene bg blackscreen with longdissolve
                            pause 2.0
                            jump Day2_Con_Kyou_Hiroko
