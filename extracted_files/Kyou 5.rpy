label Day5_NonCon_Kyou:
    scene bg street1 day with longdissolve
    "It's Friday, and I'm walking to school with a spring in my step."
    play music Bright_Opening
    if pursued == "Hiroko":
        show Hiroko uniform_armup happy at left, flip:
            xalign -0.3
            linear 1.1 xpos 0.05
        h "Kyou~ Good morning~ {font=DejaVuSans.ttf}♫{/font}"
        "I instinctively flinch as I register Hiroko's voice in my vicinity before I note its total lack of hostility."
        "I look to her and smile. I love that she's found a new attitude, but this'll take some adjusting."
        ks chuckle "Ah, good morning, Hiroko. How are you?"
        h uniform smile uniform_arm "Good~ Yeah, really good! I dunno how, but talking to you yesterday just took this massive weight off my shoulders~" with dissolve
        ks smile "Really? That's awesome!"
        h laugh "Like, I don't even know what we talked about exactly; s'all just a blur to me." with dissolve
        h smile "But whatever you said, it's totally what I needed to hear." with dissolve
        h happy "So thanks~" with dissolve
        ks "You're welcome. I'm glad we're friends now, Hiroko."
        h smile no_arm blush "Yeah. Me too, Kyou~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    elif pursued == "Sayori":
        show Sayori alert_smile_right at left, flip:
            xalign -0.3
            linear 1.1 xpos 0.05
        s "Good morning, Kyou."
        "I turn and face the unfamiliar sight of Sayori approaching me on the way to school."
        "She's looking livelier than usual today. Which isn't saying much, but baby steps."
        show Sayori at left, flip:
            xalign -0.3 xpos 0.05
        ks smile "Hey, Sayori. How was your night?"
        s alert_happy uniform_folded "Good. I blew off cram school and saw a movie instead. Then I went home and had an early night." with dissolve
        s uniform_handup "It felt strange to neglect my studies for a night, but I have not slept so well in a long time." with dissolve
        s alert_smile_right "I intend to make a habit of it." with dissolve
        ks chuckle "That's great, Sayori. That's really great!"
        "I smile back at her. Not only did I remove an obstacle to seeing more of Nozomi, I'm helping her friends with their problems too."
        "I can't help but be pleased with myself."
    elif pursued == "Nozomi":
        scene bg classroom day
        show Sayori smile at center, flip:
            xpos 0.25
        show Hiroko smile_side uniform_arm at center, flip
        show Nozomi side smile_side at center:
            xpos 0.75
        with blink
        n "Morning, everyone~"
        "I may need to back off today, but I'm confident that Nozomi has taken my words yesterday to heart, like she's taken everything else I've said to her."
        s "Hey, Nozomi."
        n "How were your nights?"
        "Our secret hypnosis sessions have shown me how she truly feels deep down."
        s annoyed "More cramming and less sleeping." with dissolve
        h annoyed_side "Eh, I'm aching all over." with dissolve
        n sad_side "Oh no, were you two overdoing it again?" with dissolve
        "She might not show it now..."
        s "I will sleep when midterms are over."
        hide Hiroko
        show Hiroko frown_side uniform_arm at center
        h "Geez, Sayori, get a grip! You're looking even deader than normal." with dissolve
        "... But I know she's excited about tomorrow."
        s uniform_folded "Said the crow to the raven." with dissolve
        h uniform_armup no_arm "... What? Well whatever, I gotta keep this up if I'm gonna crush it this weekend." with dissolve
        n frown_side "You two won't be crushing ANYTHING at your current rate. Leave yourselves some recovery time tomorrow, at least." with dissolve
        $ multichar = ("{color=385599}Sayori{/color}{color=#FFFFFF} and {/color} {color=FF89AB}Hiroko{/color}")
        hide Hiroko
        show Hiroko uniform_arm annoyed_side at center, flip
        show Sayori frown_right
        multi "I'll think about it..." with dissolve


    if pursued == "Hiroko":
        scene bg classroom day with blink
        "I walk in with Hiroko just in time for the bell and class begins."
        show Hiroko uniform_armup laugh_side at center, flip
        with blink
        play sound schoolbell
        h "Lunchtiiiime~ {font=DejaVuSans.ttf}♫{/font}"
        show Nozomi side smile_side at center:
            xpos 0.75
        n "Hehe, you're in a good mood today, Hiroko. Good practice yesterday?" with dissolve
        h happy "Yeah, I was on fire. But even if I wasn't, I don't think it could bring me down~" with dissolve
        show Sayori smile at center, flip:
            xpos 0.25
        s "That sounds like a good attitude to take." with dissolve
        h smile uniform_arm "Right? Oh, Kyou's looking our way. Kyoouuu~ Join the rooftop club!" with dissolve
        show Nozomi surprised
        show Sayori concerned_right
        "I smile and stride over to join the group as Hiroko playfully waves me over." with dissolve
        s frown "Eh? Am I out of the loop on something?" with dissolve
        n "You and me both, Sayori!" with dissolve
        show Nozomi front smile
        ks smile "Hey, girls." with dissolve
        s uniform_folded "What happened to \"He's never gonna be a member\"?" with dissolve
        hide Hiroko
        show Hiroko no_arm
        h happy "I can change my mind can't I? 'Sides, he's relaxing and safe to be around." with dissolve
        s "Is that a fact?"
        h happy uniform_armup "Dunno why I had a problem before. Anyway, we gotta put his membership to a vote~" with dissolve
        stop music fadeout 5.0
        s annoyed "Do not bother. You are transparent as glass and it's obvious which way Nozomi is swinging these days." with dissolve
        n side smile blush "Ehehee..." with dissolve
        s "I am out. You three have fun upstairs."
        show Sayori:
            linear 1.0 xpos -0.5
        with None
        show Hiroko sad_side noblush
        n sad_side noblush "Sayori..." with dissolve
        ks sigh "I'm... sure she just needs time to adjust. You both needed some time to come around to me after all."
        h uniform sad "Yeah, that's true..." with dissolve
        ks smile "So let's give her some space and head to the roof, okay girls?"
        show Nozomi smile
        h smile "'Kay~" with dissolve
        n "Alright. I'll talk to her later."
        scene cg rooftop day
        play music Memories
        show RoofHiroko leanback smile_left
        show RoofNozomi handsdown smile
        with blink
        n "Seriously though, what happened? Did you two talk?"
        ks chuckle "As a matter of fact, we did. Hiroko and I talked it out yesterday and we came to an understanding."
        show RoofHiroko handcheek laugh
        h happy blush "Yeah~ I seriously dunno why I hated you so much, Kyou. I feel so dumb about it now." with dissolve
        ks smile "It's fine, really. I'm just glad that's all behind us."
        "And I'm really happy I made such a positive difference to your life, Hiroko."
        "I can still hardly believe I'm speaking to the same loud-mouthed little brat from yesterday."
        n "Now I'm even more curious about what you said to her. It must've been truly inspiring~"
        "To think, that I've had this potential for all this time."
        show RoofHiroko leanback smile_left
        h laugh_side "Heehee, I was telling him I don't even remember myself~" with dissolve
        show RoofNozomi worried_right
        n "You don't remember what he said?" with dissolve
        show RoofHiroko smile
        h smile_side uniform_armup "Nope! I just remember how much I liked listening to him and how happy it made me." with dissolve
        "All these wasted months, years even, before I took up this hobby of mine."
        show RoofNozomi neutral_right
        n frown_side "Mhm?" with dissolve
        show RoofHiroko smile_left
        h "And then I just knew I had to keep this positive flow going~" with dissolve
        "But it was the key to everything."
        show RoofHiroko handcheek laugh
        h happy "Aaah, I'm so freakin' happy~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        show RoofNozomi happy
        n laugh "Aww, it's great to see you so bubbly, Hiroko." with dissolve
        n "I know how stressed you've been about the tournament, so I'm glad you found some release~"
        show RoofHiroko leanback smile_left
        h uniform smile_side noblush "Yeah! I'm just gonna chillax, play my game and what will be will be~" with dissolve
        "Finally, I can convince people to give me a chance. Finally everyone will see how nice I am, just like these girls."
        show RoofNozomi smile_right
        n smile_side "You're... You're taking this completely in stride, aren't you?" with dissolve
        show RoofHiroko smile
        h happy_closed "It's the only way I know how to be~" with dissolve
        n "Well... I can't wait to see you in action, Hiroko. I'm definitely going to be there to cheer you on~"
        ks "Yeah, me too. We're rooting for you, Hiroko."
        show RoofHiroko handcheek laugh
        h uniform_armup laugh blush "Yay! Thanks, guys~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    elif pursued == "Sayori":
        scene bg classroom day with blink
        "I walk in with Sayori just in time for the bell and class begins."
        show Sayori alert_smile at center, flip
        with blink
        play sound schoolbell
        s "Are we having lunch on the roof today?"
        show Nozomi side smile_side at center:
            xpos 0.75
        n "Of course~" with dissolve
        show Hiroko happy uniform_arm at center, flip:
            xpos 0.25
        h "Woah, what's this? Sayori wants rooftop lunch?" with dissolve
        hide Sayori
        show Sayori alert_pout uniform_folded blush at center
        s "Oh, please. It is not that unusual for me to want a change of scenery." with dissolve
        "I stand up from my desk and gingerly approach the trio as they chatter among themselves."
        show Hiroko frown
        show Sayori alert_smile_right noblush
        "I didn't get a chance to talk to Hiroko yet, but I think I'll be okay." with dissolve
        h "The fuck do {nw}"
        extend "YOU want?" with vpunch
        ks confused "Well, I mean, I was wondering if I could- {w=0.5}{nw}"
        show Sayori alert_concerned
        show Nozomi sad_side
        stop music fadeout 10.0
        h angry uniform_armup no_arm "We already {nw}" with dissolve
        extend "TALKED about this! No!" with vpunch
        s "Hiroko, wait."
        h surprised_side "Huh?" with dissolve
        s uniform_handup sleeptalk "I feel we were too harsh on him before. He can join us if he wishes." with dissolve
        h angry_side "Wha? Whaddya mean we were too harsh? {w=0.3}We were the {nw}" with dissolve
        extend "PERFECT amount of harsh!" with vpunch
        s alert_sleep "I understand, Hiroko. I do." with dissolve
        s alert_smile_right "But he came to visit me yesterday at study club and... we talked." with dissolve
        h "..."
        s alert_concerned "I am sure if you talked to him as well, you would also see he is harmless." with dissolve
        h furious_side "What the fuck could he {nw}" with dissolve
        extend "POSSIBLY say? You wanna tell me what he said?" with vpunch
        s alert_sleep blush "I... I cannot." with dissolve
        ks "H-hey, could we please settle down?"
        h furious vein"YOU stay the fuck outta this!" with vpunch
        n surprised_side "Hiroko-{w=0.5}{nw}" with dissolve
        show Sayori noblush
        h angry_side "I mean, what the fuck?! How do you guys do a 180 the second you're alone in a room with him?" with dissolve
        h uniform "That's weird ain't it? Tell me that ain't weird, I fuckin' {nw}" with dissolve
        extend "DARE you!" with vpunch
        n sad_side "It's... w-well..." with dissolve
        s alert_concerned "It is not so weird if you talk to him." with dissolve
        h furious "Fuck it. {w=0.3}Y'all come back to me when you ain't being so {nw}" with dissolve
        extend "STUPID!" with vpunch
        show Hiroko at flip zorder 1:
            linear 1.5 xpos 1.5
        show Sayori at flip
        show Nozomi surprised
        $ renpy.transition(longdissolve, layer="master")
        with None
        pause 1.5
        show Nozomi surprised_side at flip
        n surprised_side "Hiroko, wait!" with dissolve
        s "She's gone..."
        "That... could've gone better."
        show Nozomi sad
        ks sigh "I'm... sure she just needs time to adjust. You both needed some time to come around to me after all." with dissolve
        s alert_concerned_right "Of course." with dissolve
        ks smile "So let's give her some space and head to the roof, okay girls?"
        hide Nozomi
        show Nozomi front smile uniform at center:
            xpos 0.75
        s alert_smile_right "Uh-huh." with dissolve
        n "Alright. I'll talk to her later."
        play music Memories
        scene cg rooftop day
        show RoofNozomi handsdown smile
        show RoofSayori leanforward alert_smile
        with blink
        n "Sooo... you two talked?"
        ks chuckle "We did, yeah."
        s "As I was saying, Kyou visited me at my study club and he convinced me not to worry so much."
        s uniform_handup "I am sure Hiroko will come around as well once she has a chance to talk to you properly."
        ks "Mhm. I think so, too."
        "Speaking of which, I'm really glad Sayori came around. It gives me hope I can talk some sense into Hiroko as well, and help her with her own issues."
        show RoofNozomi happy
        n chuckle "Now I'm even more curious about what you said to her, Kyou. It must've been truly inspiring~" with dissolve
        "To think, that I've had this potential for all this time."
        show RoofSayori alert_awe
        s alert_smile "I must admit it is a little odd that I remember almost nothing from our talk yesterday." with dissolve
        show RoofNozomi neutral_left
        n "You really don't remember what he said to you?" with dissolve
        show RoofSayori leanback alert_smile blush
        s alert_happy uniform_folded blush "It is embarrassing to admit, but no. I do not." with dissolve
        "All these wasted months, years even, before I took up this hobby of mine."
        show RoofSayori alert_sleeptalk
        s sleeptalk "But even so, he convinced me that I should take things much easier from now on." with dissolve
        show RoofSayori alert_smile -blush
        s alert_smile noblush "And that is why I'm going to stop attending cram school." with dissolve
        show RoofNozomi worried_left
        n sad_side "... I-is that so?" with dissolve
        show RoofSayori alert_happy
        s alert_happy "It is. I shall endeavor to work harder on myself from now on." with dissolve
        show RoofSayori alert_smile
        s uniform_handup alert_smile"And speaking of which, when is your next karaoke night planned? I'd like to come along if I may." with dissolve
        show RoofNozomi smile_left
        n smile_side "Hm? Oh, it's next week. I'd love to see you there, but you never seemed interested before~" with dissolve
        "But it was the key to everything."
        show RoofSayori alert_happy
        s uniform_folded "Like I say, I want to work harder on fun. Besides, I am sure you'd love to know how amazing my singing voice is." with dissolve
        show RoofNozomi laugh
        n laugh "Ahaha, I can't wait to hear how much it sucks, so you can fit in with the rest of us!" with dissolve
        s alert_happy "Mhmhmhm."
        "Finally, I can convince people to give me a chance. Finally everyone will see how nice I am, just like these girls."
        show RoofNozomi smile_left
        n smile_side "You really do seem like you're taking it easy, Sayori. It's like seeing a whole new you~" with dissolve
        show RoofSayori alert_smile
        s alert_smile "Do you think? I am rather liking this new me." with dissolve
    if pursued != "Nozomi":
        scene bg corridor day
        show Nozomi front2 smile at center
        with blink
        "As we make our way back to class, Nozomi taps me on the arm." with dissolve
        n "So, Kyou, I can't stop thinking about that study group you mentioned the other day."
        ks confused "Oh, yes?"
        n "Mhm. And I was thinking, since it's the weekend and Hiroko's tournament is on Sunday..."
        n chuckle "Would you be free tomorrow? I could swing by in the morning if that's okay with you?" with dissolve
        "... I think my heart just skipped a beat. This is really happening."
        "After all this time, Nozomi truly has noticed me. And now that she has, she really can't stop thinking about me."
        "I want to savour this moment forever, but first I need to steady my nerves and answer her."
        ks chuckle "S-Sure, that sounds great! Let me give you my address."
        show Nozomi smile
        "Nozomi smiles as we walk slowly down the corridor while we exchange details." with dissolve
        ks smile "There we go. So tomorrow, ten o'clock?"
        n happy "Sounds perfect! I can't wait~" with dissolve
    scene bg classroom eve with blink
    stop music fadeout 5.0
    if pursued != "Nozomi":
        "I'm all set. At last I'm going to get some quality alone time with our class rep."
        "She finally noticed me, and all it took was a little convincing."
    else:
        "And to think I owe it all to this penlight of mine."
    play sound schoolbell
    show Nozomi front at right
    n "Stand!" with dissolve
    n "Bow!"
    hide Nozomi
    "But what's this feeling in the pit of my stomach?" with dissolve
    if pursued == "Hiroko":
        show Hiroko happy at center
        show Sayori at center, flip:
            xpos 0.25
        h "Seeya later~" with dissolve
        "I haven't felt this nervous all week."
        s "Yep. Good luck with practice."
        h smile_side "Oh, yeah. I think I'm gonna skip today." with dissolve
        s uniform_handup concerned "Skip? The tournament is in two days." with dissolve
        "Maybe it's because after everything, my big chance is finally in plain sight."
        h uniform_headhold2 happy "Yeah, but I'm not really feeling it today. I get super angry on the court." with dissolve
        s "But... {w=1.0}{nw}"
        show Sayori uniform_folded irritated
        $ renpy.transition(dissolve, layer="master")
        extend "Oh, you do what you want. I don't care." with dissolve
        h "Happy crammin', Sayori! Bye~"
        hide Hiroko
        "Tomorrow I'll finally make Nozomi realize how much she loves me." with dissolve
        s frown "Unbelievable..." with dissolve
        show Nozomi side frown_side at center
        show Sayori neutral
        n "Hey, Sayori, can I talk to you before you go?" with dissolve
        scene bg blackscreen with longdissolve
        pause 2.0
    elif pursued == "Sayori":
        show Sayori alert_smile at center
        show Hiroko annoyed_side at center, flip:
            xpos 0.25
        s "Have a good weekend, Hiroko." with dissolve
        h "Yeah yeah, happy cramming."
        s alert_happy "Oh, I am not doing that anymore. I'm focusing more on my work-life balance. Emphasis on life." with dissolve
        h confused_side "Huh? I thought you loved it at cram school." with dissolve
        "Maybe it's because after everything, my big chance is finally in plain sight."
        s alert_concerned "I do... I did. But I need to make this change before I stress out completely. Kyou made me realise that." with dissolve
        h "Why'd you listen to-...  {w=0.5}{nw}"
        extend uniform_headhold2 irritated "nope, not my fuckin' problem. Do whatever you want." with dissolve
        s alert_neutral "See you." with dissolve
        hide Sayori
        "Tomorrow Nozomi will finally realize how much she loves me." with dissolve
        show Nozomi side frown_side at center
        show Hiroko neutral_side
        n "Hey, Hiroko, can I talk to you before you go?" with dissolve
        scene bg blackscreen with longdissolve
        pause 2.0
    elif pursued == "Nozomi":
        show Nozomi side frown_side at center:
            xpos 0.75
        show Sayori at center, flip
        show Hiroko uniform_arm annoyed_side at center, flip:
            xpos 0.25
        with dissolve
        h "Ugh, still feeling achey..."
        n "I keep telling you two, get some decent rest."
        "Maybe it's because after everything, my big chance is finally in plain sight."
        h "Yeah, yeah... {w=0.5}I {nw}"
        extend "GUESS I could take a nap or something." with vpunch
        n smile_side "I'm relieved-{w=0.5}{nw}" with dissolve
        h no_arm uniform_armup angry_side "Then TOTALLY go at it tomorrow!" with vpunch
        n sad_closed "*sigh*" with dissolve
        show Hiroko frown
        "Tomorrow I'll finally show Nozomi how much she loves me." with dissolve
        s uniform_folded "I do appreciate the concern, Nozomi, but my parents are paying a lot for my extra schooling and I will not squander it." with dissolve
        n smile_side "Well... I tried. I'll see you both on Sunday." with dissolve
        show Sayori smile
        h smile_side "Seeya!" with dissolve
        s "See you."
        scene bg blackscreen with longdissolve
        pause 2.0
    jump Day6_NonCon_Kyou

label Day5_Villain_Kyou:
    scene bg street1 day with longdissolve
    "It's Friday, and I'm walking to school with a spring in my step."
    play music Beautiful
    if hypno1 == "devoted hiroko":
        show Hiroko uniform_armup happy blush at left, flip:
            xpos -0.3
            linear 1.1 xpos 0.1
        h "KYOU! Good mooorniiiing~ {font=DejaVuSans.ttf}♫{/font}" with vpunch
        "... Only to be interrupted as a familiar shrillness begins to ring in my ears."
        "And to think I used to be afraid of this bitch."
        ks frown "I don't recall saying you could come near me."
        h surprised "Oh shit, you're right..." with dissolve
        show Hiroko at flip:
            linear 1.1 xpos -0.1
        pause 1.1
        h uniform cry "S-sorry. Please don't hate me!" with dissolve
        "But now as I look her over with a grin, I'm happy to see she remains so completely and utterly neutered."
        ks smirk "Ah, I'm just fucking with you. Get back here."
        h uniform_armup giggle "Ahh~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        show Hiroko at flip:
            linear 1.1 xpos 0.1
        pause 1.1
        show Hiroko at flip:
            xpos 0.1
        ks "Heh. You're like a puppy now, aren't you."
        h uniform_headhold laugh "Kyahaha~ you're so right Kyou~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        ks "Then let's hear your bark."
        h uniform_armup happy "Ruff ruff! Ehehe~" with dissolve
        "That turned a few heads from some of our fellow schoolmates on the road, while I pet her head with a smirk."
        ks "Good girl..."
    elif hypno1 == "robot hiroko":
        show Hiroko smile at left, flip:
            xpos -0.3
            linear 1.1 xpos 0.1
        h "Good morning, Kyou."
        show Hiroko smile at left, flip:
            xpos -0.3 xpos 0.1
        "I turn around to face Hiroko in surprise, halting my walk for a moment."
        "Without [p_their] former... energy, my [hypno6] blends into the street, even in human mode. I wonder if anyone else [p_they] knows picked up on that."
        ks smile "Ah, good morning. Tell me, Hiroko, how are things at home? Have your parents talked about you recently?"
        h happy_closed "Yeah, a little. They think I've been spending a lot of time alone in my room and I'm not talking much, but that it's because I'm focused on my tournament this weekend." with dissolve
        "I probably should've thought about this before."
        ks "And what do you do in your room while you're alone?"
        h smile "I sit on my bed and stay quiet, unless I gotta do stuff like homework." with dissolve
        "Toning down Hiroko's shrillness was good for me, but I'll need to restore some of it in case questions start being asked."
        ks "You don't do anything with your free time?"
        h sleeptalk "That's right. I don't wanna waste my CPU on useless human stuff. Seriously tires me out." with dissolve
        "I can't allow [p_their] true nature to be discovered by anyone else. This just means I have more programming to do."
        "Perhaps I should work in some personality subroutines that activate on the presence of particular individuals that know Hiroko best."
        show Hiroko smile
        ks "I see. That's good to know." with dissolve
        "Rather than annoying me, the prospect of having more to tinker with is just making me excited all over again."
        scene bg ext school day with blink
        if hypno10 == "girlfriend nozomi":
            n "Kyou! Good Morning~ {font=DejaVuSans.ttf}♥{/font}"
            show Nozomi side laugh blush at right:
                xpos 1.3
                linear 1.5 xpos 0.6
            "But then, as we approach the school I hear a voice calling out to me that excites me even more..."
            show Nozomi happy at right:
                xpos 0.6
            ks smile blush "Hey, Nozomi. Did you miss me?" with dissolve
            n front2 loving "Ehehe... I haven't been able to stop thinking about you all night~" with dissolve
            "She closes in to kiss me and I have no intention of stopping her."
            show Hiroko smile_side at center, flip:
                xpos 0.2
            show Nozomi neutral_left
            "Although I gotta admit, it feels a little awkward doing it in front of the calm stare of her friend as she stands motionlessly beside us." with dissolve
            n side sad_side "O-oh gosh, Hiroko I can't believe I didn't see you there. Good morning!" with dissolve
            h "Good morning, Nozomi."
            "Nozomi must surely expect Hiroko to break the awkward silence that follows. It really is a little eerie that she doesn't."
            # "It's oviously not like her to be so quiet around either of us, least of all at the sight of her friend macking up to someone she's supposed to hate."
            n smile_side "S-soooo, yes, me and Kyou are an item now. Sorry if that's a shock to you, but... w-well it all happened so fast, and..." with dissolve
            h "It's fine. I'm not shocked at all."
            n shocked_side "You're... not?" with dissolve
            "I'd better break this up for now."
            n sad_side "I don't even know what to say... sorry." with dissolve
            "Nozomi no doubt has questions but there'll be time for that later, when there are fewer eyes on all of us. "
            # "I have a feeling Nozomi's going to be fine about what I've done to this friend of hers, but I'd better break this up for now. There'll be time for explanations later."
            show Nozomi sad
            show Hiroko smile
            ks "Hey, we'd better get inside; classes are about to start." with dissolve
            ks "But let's meet up for lunch and we'll talk about all of this, okay?"
            h "Okay, Kyou."
            n smile "Well... of course! I'd love that~" with dissolve
    stop music fadeout 5.0
    scene bg classroom day with blink
    play sound schoolbell
    if hypno1 == "devoted hiroko":
        "I walk in with Hiroko just in time for the bell and the beginning of class."
        play music Memories
        scene bg classroom day
        show Hiroko uniform_armup laugh uniform_arm at center
        with blink
        h "Lunchtiiiime~"
        ks neutral "Come on, Hiroko. We're going to lunch on the roof today."
        h happy "YAY! Okay!" with vpunch
        show Sayori uniform neutral_right blush at center, flip:
            xpos 0.25
        ks "You too, Sayori. I see you hovering over there." with dissolve
        if hypno5 == "devoted sayori":
            s smile_right "A-Ah, well, I did not want to assume..." with dissolve
            s happy "Thank you so much for letting me join you!" with dissolve
    elif hypno1 == "robot hiroko":
        if hypno10 == "girlfriend nozomi":
            "I walk in with the pair of them just as the bell rings out and homeroom begins."
            play music Memories
            scene bg classroom day
            with blink
            "When lunchtime finally rolls around, I approach Nozomi's desk with no small amount of confidence just as her other friend Sayori begins speaking."
        else:
            "I walk in with Hiroko just in time for the bell and the beginning of homeroom."
            play music Memories
            scene bg classroom day
            with blink
            "When lunchtime finally rolls around, I approach Hiroko's desk with no small amount of confidence while I notice Sayori turn to Nozomi."
        show Sayori uniform_folded sleeptalk at center, flip:
            xpos 0.25
        show Nozomi side smile_side at center
        s "I feel more fatigued than usual today. Perhaps I'll take a nap right here..." with dissolve
        show Sayori neutral_right
        show Nozomi smile
        ks smile "Let's go up on the roof today, ladies." with dissolve
        s frown_right "Excuse me? Who do you think-{w=1.0}{nw}" with dissolve
        stop music
        if hypno10 == "robot nozomi":
            n front2 smile "Of course, Kyou." with dissolve
        elif hypno10 == "girlfriend nozomi":
            n front2 happy blush "O-okay~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        show Hiroko smile uniform_arm at center:
            xpos 0.75
        h "Okay." with dissolve
        play music Measured
        show Sayori surprised
        "I smile as the pair of them line up beside me, although the other girl looks less than amused." with dissolve
        s uniform_handup "Nozomi? Hiroko? What are you doing?" with dissolve
        $multichar = "{color=93624B}Nozomi{/color}{color=FFFFFF} and {/color}{color=FF89AB}Hiroko{/color}"
        if hypno10 == "girlfriend nozomi":
            show Nozomi laugh
            multi "We're going with Kyou." with dissolve
        else:
            multi "We're going with Kyou."
        s "Yes, but..."
        scene bg blackscreen with fade
        if hypno10 == "robot nozomi":
            "Ignoring Sayori, I move to leave for the rooftop, knowing my [hypno6]s will follow."
        elif hypno10 == "girlfriend nozomi":
            "Ignoring Sayori, I move to leave for the rooftop, knowing Nozomi and my [hypno6] will follow."
        s "Why?"
    elif hypno1 == "spy hiroko":
        "I walk in alone just in time for the bell and class begins."
        "Just another school day..."
        scene bg classroom day
        show Hiroko uniform_armup laugh_side uniform_arm at center, flip
        with blink
        play music Memories
        h "Lunchtiiiime~"
        show Nozomi side laugh at center:
            xpos 0.75
        n "Ehehe, it's that time again, huh." with dissolve
        show Sayori smile uniform_folded at center, flip:
            xpos 0.25
        s "Mm..  maybe I can catch some z's while I'm up there today." with dissolve
        "I hear Nozomi chatting to her friends, smiling and laughing amongst themselves, as if our time together never happened."
        hide Nozomi
        hide Sayori
        hide Hiroko
        "They barely give me a glance as they pass my desk on the way out of the classroom and presumably towards the rooftop." with dissolve
        "I consider joining them up there, but I immediately think of a better idea."
        show phone at right with moveinright:
            ypos 0.346
        "Pulling out my phone, I take my time as I compose a group text..."
        "{color=#4B9374}\"You changed your mind about the rooftop. You want to go back to your desks and invite Kyou to join you for lunch.\"{/color}"
        hide phone with moveoutright
        stop music fadeout 5.0
        "After all, I reason, I should make sure the suggestions I planted are still holding up before doing anything riskier."
        "But I can barely contain the grin on my face as I wait..."
        show Hiroko smile_side at center:
            xpos 1.2
            linear 1.0 xpos 0.75
        h "Man, I can't believe we all had the same idea."
        play music Eons
        show Nozomi side laugh at center:
            xpos 1.2
            linear 1.0 xpos 0.75
        show Hiroko:
            linear 1.0 xpos 0.5
        n "Right? It's crazy."
        show Sayori smile at center:
            xpos 1.2
            linear 1.0 xpos 0.75
        show Hiroko:
            linear 1.0 xpos 0.25
        show Nozomi:
            linear 1.0 xpos 0.5
        pause 1.0
        show Hiroko at center, flip:
            xpos 0.25
        s "I am just glad we agreed. I thought I was about to suggest something extremely controversial." with dissolve
        "Feigning ignorance, I smile politely as they assemble around my desk."
        ks smile "Can I help you?"
        show Sayori smile_right
        show Hiroko smile
        n front smile "Do you want to have lunch with us today, Kyou?" with dissolve
        h smirk "Why're you asking him? We ain't taking no for an answer." with dissolve
        s uniform_handup happy "Mhmhm, we cannot force him against his will. But Kyou, you are more than welcome to join us today." with dissolve
        hide Sayori
        hide Hiroko
        "I let out a chuckle as the three of them start heading back to their desks." with dissolve
        n side smile "Come on~ It must be lonely sitting there by yourself." with dissolve
        scene ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_smile with blink
        "Naturally I allow myself to be convinced as I get up from my desk and pull up a chair to sit beside them."
        # "I'm definitely going to have some fun with this little situation I've engineered for myself."
        ks smile "You know, it's funny."
        show ClassroomLunch2 h_neutral
        h "What is?" with dissolve
        ks "Just the other day a certain someone was telling me that I shouldn't approach you guys."
        show ClassroomLunch2 h_frown_left
        "Hiroko averts her eyes as I allude to our little fight earlier in the week." with dissolve
        "I might be pushing my luck a little to bring up the contradiction, but at this point I'm eager to see how she squares the instructions I gave her with her own views."
        h "Y-yeah, well... You didn't approach us."
        show ClassroomLunch2 hiroko2 h_growl
        h angry "We approached {nw}" with dissolve
        show ClassroomLunch2 n_surprised s_worried
        extend "YOU!" with vpunch
        show ClassroomLunch2 h_frown
        h sleep "So don't think this changes anything, got it?" with dissolve
        ks smirk "Uh, sure. Whatever you say."
        show ClassroomLunch2 n_concerned s_neutral_right
        n side sad_side "Wait, what is he talking about, Hiroko?" with dissolve
        show ClassroomLunch2 h_neutral_left
        h "Uhh..." with dissolve
        show ClassroomLunch2 hiroko1 h_worried_left
        h frown_side "Y-yeah, so I kinda roughed him up a bit the other day." with dissolve
        show ClassroomLunch2 n_surprised s_worried
        n surprised_side "What?! Why?" with dissolve
        show ClassroomLunch2 h_frown_left
        h uniform_armup angry "You said he hurt you!" with dissolve
        show ClassroomLunch2 n_frown_right
        n frown_side "That's not an excuse! Besides, I don't even remember what I was so upset over now, so maybe it wasn't such a big deal." with dissolve
        n "You should apologize."
        show ClassroomLunch2 h_worried_left
        h surprised_side noblush "Wha?" with dissolve
        show ClassroomLunch2 s_irritated
        s uniform_folded frown "Yes, you should. I know you and Kyou do not see eye to eye, but unprovoked assaults are intolerable." with dissolve
        show ClassroomLunch2 h_worried
        h "B-but... I was so mad at him." with dissolve
        ks frown "You shouldn't talk like I'm not here, you know."
        show ClassroomLunch2 s_frown h_blush
        h sad "Uhh..." with dissolve
        "Hiroko grimaces as she feels everyone's judgmental gaze on her."
        "I can't say I don't enjoy her discomfort as her eyelids flutter under the attention while she looks to me, but can't quite meet my gaze."
        show ClassroomLunch2 h_sad
        h uniform sleep blush "S-sorry, dude." with dissolve
        ks smirk "Hey, no hard feelings."
        show ClassroomLunch2 n_smile s_smile
        "Hiroko nods slowly as her friends smile, apparently placated by the gesture." with dissolve
        hide ClassroomLunch2
        show ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_neutral_left
        h noblush "Y-yeah, so anyway... is it just me or did this week really fly by?" with dissolve
        "I smile back, as we all start to tuck into our lunches while making smalltalk."
        show ClassroomLunch2 n_neutral_right s_neutral_right
        s neutral "Now that you mention it, I have had a similar thought myself." with dissolve
        "No girl's ever let me have lunch with them since I started high school, so I don't care that I had to cheat; I'm gonna enjoy this."
        show ClassroomLunch2 n_curious_right
        n front uniform_folded pout_left "I guess it's been one of those weeks, huh." with dissolve
        ks smile "Yeah? I feel like this week's lasted an age."
        show ClassroomLunch2 n_curious s_neutral h_neutral
        s neutral_right "Somehow, Kyou, that does not surprise me." with dissolve
        ks frown "W-what's that supposed to mean?"
        show ClassroomLunch2 h_smirk
        h smirk "She means you're such a no-friends-having loser, all your days are gonna be long." with dissolve
        show ClassroomLunch2 n_frown_right s_angry
        s angry "H-Hiroko, please!" with dissolve
        show ClassroomLunch2 h_worried_left
        h surprised_side "What?" with dissolve
        show ClassroomLunch2 n_pout s_frown
        n side frown_side "That was uncalled for!" with dissolve
        show ClassroomLunch2 h_sad
        h sad "Uh, sorry. Forgot it was \"Be nice to Kyou\" day." with dissolve
        "I draw a deep breath as I try to keep my cool, but goddamn these bitches."
        show ClassroomLunch2 n_frown_right
        n front irritated "Would it kill you to be civil for just one lunch period? Geez." with dissolve
        show ClassroomLunch2 s_irritated
        s irritated "And as it was your idea to have lunch with him as much as anyone you really should be making more of an effort, Hiroko." with dissolve
        "Hiroko only said what you were insinuating, Sayori. Don't act so innocent."
        show ClassroomLunch2 h_worried
        h "'Kay, yeah, I get it. Sorry, Kyou, I'm just being a butt." with dissolve
        "If you two knew how much power I had over you, you wouldn't be so fucking blasé about pissing me off."
        ks "Yeah, sure."
        show phone at right with moveinright:
            ypos 0.346
        "I mean, my phone's right here in my pocket."
        "I could send you two a message right now. Get you to piss yourselves in the next period, and make you announce it to the whole class."
        show ClassroomLunch2 n_concerned s_neutral
        n concerned "Okay, so... Kyou. Maybe we could talk about you for a bit? Get to know you?" with dissolve
        "See how many friends you have after that."
        n "... Kyou?"
        hide phone with moveoutright
        ks surprised "H-huh?"
        n "I was just saying, maybe you could tell us a little about yourself?"
        "... Oh, shit. If only you'd said this to me a week ago."
        ks confused "A-about myself?"
        show ClassroomLunch2 n_neutral h_neutral
        n "That's right. You've been in our class since the beginning, but I feel like I barely know anything about you." with dissolve
        ks neutral "Uh, well... what do you wanna know?"
        show ClassroomLunch2 n_smile
        n smile "How about... well, what do you like to do in your spare time?" with dissolve
        ks "I, uh..."
        "Hypnotize you and your friends into being my unwitting thralls?"
        ks sigh "Oh, y'know... I play games and stuff."
        n "Videogames?"
        ks "Yeah, like on my computer and phone and stuff."
        show ClassroomLunch2 s_smile
        s smile_right "Heh. I used to play a lot of games on my phone." with dissolve
        show ClassroomLunch2 h_smirk_left
        h smirk_side "Shit, seriously?" with dissolve
        show ClassroomLunch2 nozomi2 n_neutral_side s_smile_right
        s happy "Do not look so surprised. I had much more free time on my hands when I was in junior high." with dissolve
        "Before, maybe I could have had this conversation with you, Nozomi, and everything would have been great."
        show ClassroomLunch2 n_smile_side
        n side laugh "It's so hard to imagine you doing something so frivolous now, though~" with dissolve
        show ClassroomLunch2 s_neutral_left
        s concerned uniform "Yes, well... I would not go back to those times." with dissolve
        "But things are different now."
        show ClassroomLunch2 s_sleep
        s "I had time on my hands, but I rarely had anyone to share it with." with dissolve
        "My ambitions go far beyond you."
        show ClassroomLunch2 n_concerned_side h_worried_left
        h sad_side "Aww. I totally would've hung out with you." with dissolve
        n "Me too. Although we're getting a little sidetracked here."
        show ClassroomLunch2 s_smile
        s uniform_folded smile_right "True. I apologize, Kyou, I didn't mean to make this about myself." with dissolve
        show ClassroomLunch2 nozomi1 n_neutral h_neutral
        ks neutral "Ah, sure. But yeah, I play a lot of games, and..." with dissolve
        "I also mess about a lot with gadgets, not to mention my general interest in hypnosis now, but..."
        show ClassroomLunch2 n_smile
        n smile "Yes, and?" with dissolve
        "No, the less they know about me now the better."
        ks sigh "Watch TV, I guess."
        show ClassroomLunch2 n_concerned s_neutral h_neutral_left
        n sad "Oh... okay. Any... anything you like to watch in particular?" with dissolve
        $persistent.classroom_lunch2_sleeper_unlock = True
        scene bg blackscreen with fade
        "The rest of lunch carried on in that kind of awkward fashion."
        scene bg classroom day with dissolve
        play sound schoolbell
        "As they left to start afternoon lessons, I got the distinct impression all three of them regretted their \"decision\" to spend lunch with me."
        "But I don't care. It only did more to confirm what I needed."
        scene bg classroom eve with blink
        "And as I muddle through my classwork, my mind turns more on what to do over the weekend."
        "Until finally it's time to head home."
        show Nozomi front at right
        n "Stand!" with dissolve
        n "Bow!"
        scene bg corridor eve with blink
        "So now I can command three girls in my class with merely a text message. But why settle for just three?"
        scene bg school ext eve with blink
        "After all when it came down to it, it wasn't that hard to do what I did."
        "And if I can do this to them, I can do it to anyone in class. In school. Anywhere."
        scene bg street1 eve with blink
        "I just need to set up the conditions to do so, like how I was able to use Hiroko's connection to Sayori to ambush her in an alley."
        "Or how I used both their connections to Nozomi to surprise her in her clubroom."
        scene bg k house eve with blink
        "So then, I should simply continue along those lines. Use the connections these girls have with other people to fashion more opportunities for me."
        "In a month, my phone could be filled to bursting with new contacts..."
        scene bg k bedroom eve with blink
        "Alright, then. I'll need to grill these girls on what they know. See who'd make a good next step."
        "After deliberating for a while, I make a decision."
        show phone at right with moveinright:
            ypos 0.346
        "I'll bring Nozomi in. Just Nozomi; having everyone turn up at my house will only overcomplicate things."
        "{color=#4B9374}\"Tomorrow morning, you will visit Kyou at his home. He lives at the following address...\"{/color}"
        "{color=#4B9374}\"When you arrive, be happy to see him and be willing to answer all of his questions.\"{/color}"
        hide phone with moveoutright
        "She has to be the more sociable of the three, so I'm sure she knows more people."
        "Alright, yeah. That's the plan."
        "All I need to do now is wait until morning..."
        stop music fadeout 5.0
        jump Day6_Villain_Kyou
    scene bg rooftop
    if hypno1 == "robot hiroko":
        show Hiroko at center:
            xpos 0.75
        if hypno10 == "robot nozomi":
            show Nozomi front2 at center
        elif hypno10 == "girlfriend nozomi":
            show Nozomi front2 laugh blush at center
        with blink
        "I lead the pair of them towards their usual meeting place on the roof, where no one else is likely to overhear us."
        if hypno10 == "girlfriend nozomi":
            ks smile "Here should be fine. Take a seat, both of you."
        else:
            ks "You, sit down there. And you, sit there."
    if hypno1 == "devoted hiroko":
        with blink
        "The three of us quickly assemble on the roof, in a quiet corner where no one is likely to overhear."
        if hypno5 == "devoted sayori":
            scene cg rooftop day
            show RoofHiroko infatuated smile blush
            show RoofSayori leanforward smile blush
            with blink
            s "To be sharing my lunchbreak with the illustrious Kyou Koyama himself."
            if hypno1 == "devoted hiroko":
                show RoofHiroko happy
                h "I knoow~ {font=DejaVuSans.ttf}♥{/font} I wanna remember this forever!" with dissolve
                s "Do you see how he is eating that riceball, Hiroko?"
                show RoofHiroko awe
                h surprised "Oh man, yeah. I'm getting chills just watchin' him." with dissolve
                show RoofSayori awe
                s laugh "Indeed. The delectable movement of his mouth. The casual flip of his tongue. The graceful dropping of the rice grain from the corner of his lips." with dissolve
                h "... Is it weird to be jealous of a piece of food?"
                s "Uh... K-Kyou has a way of making it seem less weird, it turns out..."
                "...This is making me feel INCREDIBLY self-conscious."
                ks sigh blush "I-If you two could keep your ladyboners to yourselves? We have work to do."
                show RoofSayori smirk
                show RoofHiroko happy
                s laugh_right "Our apologies. We will be good... ish." with dissolve
                show RoofHiroko smile
                ks frown noblush "So Sayori, when do you think Nozomi's going to make her leaving official?" with dissolve
                show RoofSayori frown
                s "Early next week seems likely. She told me she talked to her parents about it and they gave her a few days to think it over." with dissolve
                s "If she still feels the same, they will allow her to switch to private tutoring for the remainder of the school year."
                ks "Sounds like quite the parents she's got there."
                show RoofHiroko awe
                h uniform_arm surprised "Oh yeah, her mom and pops are super nice!" with dissolve
                show RoofSayori determined
                s uniform neutral_right "To a fault. They do rather dote on their daughter." with dissolve
                ks "So we need to make a move this weekend. Do you know what she's doing?"
                show RoofSayori frown
                s sleep "Nothing concrete, but I suspect she intends to lay low to avoid you." with dissolve
                s "Any attempts to draw her out and into a quiet space where you might find her is bound to be met with deep suspicion."
                show RoofHiroko concerned
                h sad_side "Yeah, right. I tried asking her out to karaoke the other night and she went nuclear on me." with dissolve
                ks "So there's really no way to get her out of the house? Shit."
                show RoofHiroko determined
                h uniform_armup surprised "So do we, like, kidnap her?" with dissolve
                show RoofSayori determined
                s frown "Hmm... That would be too great a risk." with dissolve
                show RoofSayori frown
                s uniform_folded "I doubt any of us have experience with breaking and entering, and the house will likely be occupied by multiple people all weekend." with dissolve
                s "We would also need to physically subdue her, and none of us are sufficiently built for such a task."
                show RoofHiroko confused
                h uniform surprised_side "And how are we gonna get chloroform? Break into the chem lab?" with dissolve
                show RoofSayori determined_side
                s rolleyes "Chloroform does not work like it does in the movies, Hiroko." with dissolve
                ks "Okay, just... no. Stop planning a kidnapping."
                show RoofSayori frown
                show RoofHiroko sad
                h sad "Aww... 'kay." with dissolve
                ks "There HAS to be a way we can pull this off."
                "I suck in a breath."
                ks sigh "And I gotta say, you're starting to disappoint me, Sayori."
                show RoofSayori surprised
                show RoofHiroko awe
                s surprised_right "I... I am?" with dissolve
                ks annoyed "We brainwashed you into helping us because I thought you'd be useful, but so far you've given us pretty much nothing."
                show RoofSayori cry
                s "I... I am sorry for displeasing you. I-I will try harder for you, I swear it!" with dissolve
                show RoofHiroko concerned
                h "We're trying our best, Kyou. I know Sayori wants to make you happy just as much as I do." with dissolve
                ks angry "Nobody asked you!"
                show RoofHiroko sad
                ks "Was I wrong in going after you, Sayori? Did I waste my time?" with dissolve
                show RoofSayori angrycry
                s angry_right uniform "No! Kyou Koyama is never wrong about anything!" with dissolve
                s "I may be uncomparable to your level of genius, which I have always envied by the way, but I will prove that I am of use to you!"
                ks frown "I hope so, Sayori. I really do."
                show RoofHiroko concerned
                ks frown "Now finish your lunches, girls. We need to keep at this." with dissolve
                $multichar = "{color=FF89AB}Hiroko{/color}{color=#FFFFFF} and {/color} {color=385599}Sayori{/color}"
                show RoofSayori determined
                show RoofHiroko determined
                stop music fadeout 5.0
                multi "Right!" with dissolve
                $persistent.rooftop_devotion_unlock = True
    elif hypno1 == "robot hiroko":
        if hypno10 == "girlfriend nozomi":
            scene bg blackscreen with dissolve
            "Now that we're away from prying eyes I can finally bring Nozomi up to speed with everything that's been going on."
            scene RoofRobotGF nozomi1 k_surprised k_blush n_happy n_blush1 h_neutral with dissolve
            "Although as I sit, I'm distracted by the feeling of her nestling up to me."
            k "N-Nozomi..."
            show RoofRobotGF n_smile1
            n "Ehehe... what?" with dissolve
            show RoofRobotGF k_smile
            "Man she's going to make it hard to focus, cuddling up with me like this... but it's not like I mind it one bit." with dissolve
            k "S-so, uhhh... Nozomi, there's something you should know about your friend there."
            show RoofRobotGF n_confused1
            n "Hm?" with dissolve
            "As her behaviour is proving all too well, she's held to her hypnotic conditioning every bit as well as Hiroko did."
            "And that conditioning is telling her to love and accept me no matter what."
            show RoofRobotGF -k_blush
            k "You see... the thing about Hiroko is..." with dissolve
            "I should be able to tell her anything about what I've been up to without her passing judgment."
            show RoofRobotGF -n_blush1
            n "Oh, right. So did you two actually talk things out?" with dissolve
            k "We talked, yes, but..."
            show RoofRobotGF sayori s_frown k_surprised
            "... Only it seems a certain individual has followed us up here. Seems she's not going to let things go quietly." with dissolve
            "I should've seen this coming."
            show RoofRobotGF nozomi2 n_surprised n_blush2 s_furious
            s "Nozomi! Talk to me!" with dissolve
            n "Huh? Oh, Sayori, hi."
            show RoofRobotGF s_worried
            s "What are we doing?" with dissolve
            show RoofRobotGF n_confused2 -n_blush2
            n sad_side "... Having lunch?" with dissolve
            s "Yes, but..."
            show RoofRobotGF k_neutral
            k "Was there something you wanted, Sayori?" with dissolve
            "Sayori looks to me with a pained expression."
            s "Someone will tell me what is going on here."
            k "We're just having a civil conversation, that's all. Is there something wrong with that?"
            # "I would've told her last night while she was over, but we were... well, busy starting our relationship."
            #He wants to test her, see if she really is every bit as conditioned by his suggestions as Hiroko

            #Short moment where Nozomi and Kyou kiss, with no reaction from Hiroko. Nozomi thinks it's a little weird, but Kyou just says he'll explain later, which Nozomi is happy to accept
            #Later at lunch on the rooftop, Kyou begins to explain what he did to Hiroko before Sayori shows up and Kyou realizes he needs to do something about her
            #Nozomi is a little concerned about what he means by that, but Kyou just says he'll explain when they get home
            #Then, at his house Kyou tells her about his brainwashing Hiroko to think she's a robot and intends to use his penlight on Sayori too so she can't interfere
            #Nozomi expresses confusion and worry, but offers her support if it means she can stay with Kyou. But he thinks to use the penlight on Nozomi again anyway to set her mind at ease
            #She happily consents, and Kyou takes her into trance before having her believe that her two friends are actually robots/gynoids/fembots so she shouldn't think of them as human...
        else:
            scene RoofRobot h_neutral n_sleepy with blink
            "Now that we're away from prying eyes, I think it better to treat them impersonally. Like the [hypno6]s they're meant to be."
            "Although I gotta admit it's a little unnerving to see them like this; so far and away from their usual selves as they sit obediently under my direction."
            show RoofRobot h_neutral_left n_neutral
            ks neutral "S-so, uh, anything to report? How are you both doing?" with dissolve
            show RoofRobot h_smile_left
            h "I'm fine." with dissolve
            n "I'm a... little hungry? I guess? It's lunchtime, after all."
            ks "Oh, yeah, did you remember to bring your lunches?"
            h "No."
            show RoofRobot n_confused
            n "... Were we supposed to?" with dissolve
            "Ugh, right, I didn't even think about that. And I don't want to go back down to class anytime soon..."
            ks sigh "Okay, nevermind. Just take it with you next time."
            show RoofRobot h_neutral n_sleepy
            n "O-okay..." with dissolve
            show RoofRobot sayori s_stern
            "... Only it seems a certain individual from said class has followed us up here. Seems she's not going to let things go quietly." with dissolve
            "I should've seen that coming."
            show RoofRobot n_confused_right s_stern_left
            s "Nozomi! Talk to me!" with dissolve
            show RoofRobot h_neutral_right n_surprised
            n "Huh? Oh, Sayori, hi." with dissolve
            show RoofRobot s_concerned_left
            s concerned "What are we doing?" with dissolve
            show RoofRobot n_confused_right
            n sad_side "... Having lunch?" with dissolve
            s "... Without your lunch?"
            ks "Was there something you wanted, Sayori?"
            show RoofRobot s_concerned
            "Sayori looks to me with a pained expression." with dissolve
            s "Someone will tell me what is going on here."
            ks frown "She just told you."
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF n_neutral2
        else:
            show RoofRobot s_concerned_left
        s frown "Nozomi, all week you wanted to be as far away from this man as possible. You gave the distinct impression that you were terrified of him." with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF s_frown
        else:
            show RoofRobot s_stern_left
        s uniform angry "I NEED to know what changed." with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF n_confused2 n_blush2
            n "I'm... I'm not sure myself, Sayori. All I know is that now I want to be with him... s-so much." with dissolve
        else:
            show RoofRobot n_sleepy
            n side frown_side "I'm... I'm not sure myself, Sayori. I just knew I wanted to follow him." with dissolve
        s frown "And Hiroko? You have been at Kyou's throat for years. Why, especially after what Nozomi told us, would you break bread with him now?"
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF s_growl
        else:
            show RoofRobot s_angry_left
        s surprised "Why are you... why are you so calm?" with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF h_smile -n_blush2
        else:
            show RoofRobot h_smile
        h happy_closed "I'm just tired, Sayori. 'Sides, I don't have a beef with Kyou anymore." with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF s_worried
        else:
            show RoofRobot s_concerned_left
        s uniform_handup concerned "You were like this yesterday. It was strange then, coming from you. It's stranger now." with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF k_sigh
            k "Sayori, if you're going to keep bothering us like this then I'm gonna have to ask you to leave." with dissolve
        else:
            show RoofRobot h_neutral
            ks "Sayori, if you're going to keep bothering us like this then I'm gonna have to ask you to leave." with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF s_growl
        else:
            show RoofRobot s_angry
        s scowl "You..." with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF s_frown k_neutral
        else:
            show RoofRobot s_stern_left
        s uniform_folded frown "Nozomi, Hiroko, can I please have a moment with you two alone?" with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF n_neutral_left h_neutral_left
            k "Both of you, don't go anywhere with her. We're staying right here." with dissolve
        else:
            show RoofRobot h_neutral_left n_neutral
            ks frown "Both of you, don't go anywhere with her. We're staying right here." with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF n_neutral2 h_smile
        else:
            show RoofRobot h_smile
        h smile_side "Sorry, Sayori. We gotta stay here." with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF s_growl
        else:
            show RoofRobot n_confused_right s_angry_left
        s angry "No, you don't \"gotta\" do anything. I..." with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF h_neutral s_furious
        else:
            show RoofRobot h_neutral s_angry
        "Sayori's scowl deepens as she looks back to me." with dissolve
        s "What on earth do you have on my friends?"
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF k_smirk
            k "... What can I say? I'm very persuasive." with dissolve
        else:
            show RoofRobot n_neutral
            ks smirk "... What can I say? I'm very persuasive." with dissolve
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF s_irritated
        else:
            show RoofRobot s_irritated
        "Sayori sucks a breath, apparently trying to compose herself as she tries to make sense of what I'm sure is a very confusing and distressing situation for her." with dissolve
        "I can almost sympathize. I don't think she's ever hurt me in the past. Although I doubt she's spared much thought for me at all until these last few days."
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF s_worried k_neutral
        else:
            show RoofRobot n_sleepy s_concerned
        "After a few moments pass, she begins to address us calmly, although she can't fully disguise the hurt in her voice." with dissolve
        s neutral_right "Then perhaps you could persuade me, Kyou? If Nozomi thought you were worth listening to, then I will as well." #"I just want you to know that I am not angry. But I hope you can understand my distress and that, Nozomi,
        "Oh, this is too much. If only she knew..."
        "Unfortunately I can hear some chatter going on behind us as a few other people arrive on the roof."
        if hypno10 == "girlfriend nozomi":
            "It'll be too risky to deal with her out in the open like this but still, this is a perfect opportunity to tie things up."
            k "Okay, look, I get that you're concerned. But this is gonna need some going over and this isn't the time or place for it."
        else:
            "Reprogramming Sayori like her friends will be too risky with them around. But still, this is the perfect opportunity to tie things up."
            ks sigh "Okay, look, I get that you're concerned. But this is gonna need some going over and this isn't the time or place for it."
        "All I need to do is lure her someplace safe and secure, so..."
        menu:
            "Invite her to my place tomorrow":
                if hypno10 == "girlfriend nozomi": #The girlfriend variant isn't written for this choice and I don't know if I can disable the option when this path is taken, so I'll just leave a cute message and a jump to credits instead~
                    "(( AUTHOR'S NOTE: Ah, actually this variation isn't written yet so we'll have to stop here. ))"
                    "(( If you want to continue the story, please roll back and select the other choice, otherwise I have no choice but to throw the credits at you. ))"
                    "... Well, okay. You asked for it~"
                    jump Credits
                $hypno9 = "home"
                if hypno10 == "girlfriend nozomi":
                    k "So how about we meet up tomorrow morning at my place? We'll all get together and hash this out, and by the end I'm sure we'll all be on the same page."
                else:
                    ks "So how about we meet up tomorrow morning at my place? We'll all get together and hash this out, and by the end I'm sure we'll all be on the same page."
                s surprised_right "Your place? Why your place?"
                if hypno10 == "girlfriend nozomi":
                    k "My dad is away for the weekend, so we'll have it to ourselves. Why not?"
                else:
                    ks smile "My dad is away for the weekend, so we'll have it to ourselves. Why not?"
                s "I suppose..."
                "I can almost see the gears turning in her head as she seemingly comes to a decision."
                s uniform_folded neutral_right "I will agree to that."
            "Invite her to Nozomi's place tomorrow":
                $hypno9 = "nozomi"
                if hypno10 == "girlfriend nozomi":
                    k "So how about we meet up tomorrow morning at Nozomi's house? We'll get together and hash this out, and by the end I'm sure we'll all be on the same page."
                    show RoofRobotGF n_confused2 s_frown
                else:
                    ks "So how about we meet up tomorrow morning at Nozomi's house? We'll get together and hash this out, and by the end I'm sure we'll all be on the same page."
                    show RoofRobot s_concerned_left
                s concerned "And you are fine with this, Nozomi?" with dissolve
                if hypno10 == "girlfriend nozomi":
                    show RoofRobotGF k_smile n_neutral_left
                    k "Of course she is." with dissolve
                else:
                    show RoofRobot n_neutral
                    ks smile "Of course she is." with dissolve
                if hypno10 == "girlfriend nozomi":
                    show RoofRobotGF n_smile_left
                    "I'm quick to get ahead of Nozomi before she can answer. I'm sure that's enough to make sure she responds correctly, if she wasn't going to before." with dissolve
                else:
                    show RoofRobot n_smile_left
                    "I'm quick to get ahead of Nozomi before [p_they] can answer. I'm sure that's enough to make sure the [hypno6] responds correctly, if [p_they] wasn't going to before." with dissolve
                if hypno10 == "girlfriend nozomi":
                    show RoofRobotGF n_smile2
                else:
                    show RoofRobot n_smile_right
                n side smile_side "Of course I am." with dissolve
                "I can almost see the gears turning in Sayori's head as she seemingly comes to a decision."
                if hypno10 == "girlfriend nozomi":
                    show RoofRobotGF s_worried
                else:
                    show RoofRobot s_concerned
                s uniform_folded neutral_right "Very well." with dissolve
        if hypno10 == "girlfriend nozomi":
            k "Great. I'll see you soon, then."
        else:
            ks "Great. I'll see you soon, then."
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF -sayori -s_worried n_confused2 k_neutral
        else:
            hide RoofRobot
            show RoofRobot h_neutral n_sleepy
        "Taking the hint, Sayori haltingly turns to leave, shooting the other two a somewhat worried look before shifting away to head back downstairs." with dissolve
        if hypno9 == "nozomi":
            "... Why did I tell her to meet at Nozomi's place instead of mine?"
            "No doubt Nozomi will be a very accommodating hostess, but unlike with me she'll probably have her folks at home."
            "Why am I making things harder for myself?"
        if hypno10 == "girlfriend nozomi":
            show RoofRobotGF nozomi1 n_sigh
        else:
            show RoofRobot n_sigh
        n front2 sigh "I feel awful. Sayori didn't deserve us blanking her like that." with dissolve
        if hypno9 == "nozomi":
            "I sigh and push my anxieties to the side for a moment to respond."
        elif hypno9 == "home":
            "I let out a chuckle."
        if hypno10 == "robot nozomi":
            ks "That's probably down to your human mode programming. I can fix that."
            show RoofRobot n_neutral
            "Nozomi nods matter of factly." with dissolve
            n "Right. I'll admit I'm still having trouble getting my head around the fact that I'm a [hypno6]."
            ks "Of course. After school we'll see about debugging some more of your code and get you as functional as Hiroko."
            show RoofRobot n_smile_left
            n smile "I'd appreciate that. Thank you, Kyou." with dissolve
        elif hypno10 == "girlfriend nozomi":
            show RoofRobotGF k_sigh n_neutral1
            k "You're right, but we'll clear all this up with her tomorrow. So don't worry about a thing." with dissolve
            show RoofRobotGF k_confused n_smile1
            "Nozomi looks to me and smiles." with dissolve
            n "Yeah. It might be a bit sudden, but if we just tell her we're dating things can go back to normal around here."
            show RoofRobotGF nozomi2 n_neutral_right
            "Although her smile begins to fade as she casts a glance towards our silent companion." with dissolve
            n "Well... closer to normal, anyway. Are you sure you're alright, Hiroko? What's on your mind?"
            show RoofRobotGF k_smile h_neutral_left
            k "She's fine. Right, Hiroko?" with dissolve
            show RoofRobotGF h_smile_left
            h "Yeah. I'm fine." with dissolve
            n "But there's something going on with you, right? What was Kyou trying to tell me?"
            show RoofRobotGF k_confused h_neutral
            k "I mean... w-well honestly it's something pretty personal and maybe we should wait until we get home so no-one overhears us, okay?" with dissolve
            show RoofRobotGF n_neutral_left
            n "Hiroko can't tell me before then? And how is it you know something this personal about her, anyway?" with dissolve
            show RoofRobotGF k_sigh
            k "Just... wait until we get home, alright?" with dissolve
            "Ugh. I didn't mean to get frustrated with her. But I need to stop this kind of talk before I'm ready to deal with it."
            show RoofRobotGF nozomi1 n_sigh
            n "I... okay, sorry. I'm just really confused, that's all." with dissolve
            "At least Nozomi's compelled to back off; to love and accept me no matter what."
            show RoofRobotGF k_smile
            k "Yeah, it's fine. I promise you, I'll explain everything tonight." with dissolve
            "Nozomi's conditioning is holding up well, considering how little time I had to work on her yesterday."
            show RoofRobotGF n_smile1
            n "Alright. Tonight, then~" with dissolve
        if hypno10 == "girlfriend nozomi":
            $persistent.rooftop_robot__girlfriend_unlock = True
        else:
            $persistent.rooftop_robot_unlock = True
        scene bg blackscreen with longdissolve
        if hypno10 == "robot nozomi":
            "After that we... well, *I* finished lunch and the day passed almost like any other school day."
        else:
            "So we finished lunch and the day passed almost like any other school day."
        "Almost, as I could see Sayori's anxiety bubbling over several times as she tried to get more information out of her friends, only to be rebuffed every time."
        "Good thing I told them to keep their mouths shut regarding me and our secret meetings this week."
        scene bg k room eve with longdissolve
        stop music fadeout 5.0
        if hypno10 == "girlfriend nozomi":
            "Anyway, I don't need to worry about Sayori for now. We're home."
            show Nozomi side smile blush
            n "Oh gosh, it felt like class went on forever, didn't it?" with dissolve
            ks smile blush "Heh, yeah. I don't know about you, but I didn't learn a thing today."
            n happy "Y-yeah... I know what you mean~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
            show Nozomi smile
            ks noblush "But we're here now. And there's something I want to try with you tonight." with dissolve
            "And now it's time to do what I've decided is best for her. For us."
            n front2 smile "Hm? Aren't we going to talk about Hiroko?" with dissolve
            play music Monologue
            "I want Nozomi as my girlfriend, but what I have going on with Hiroko is too fascinating to pass up."
            n surprised noblush "I mean seriously, what's going on with you two? She's barely talked to me all day, but she seems to listen to you?" with dissolve
            "And then there's the Sayori... situation."
            ks "I'll get to that. But I want to do this with you first."
            n neutral_left "You're going to keep me in suspense a little longer, huh?" with dissolve
            "One thing's for sure, if I want to carry on as I am then Nozomi needs to believe what Hiroko now believes about herself and the world. Perhaps even moreso..."
            # "And if I want to do that, then Nozomi needs to believe what Hiroko now believes: That she truly is a [hypno6]."
            ks "Just trust me, okay? I think you're going to like this."
            scene cg k room eve
            play sound sitting
            show NozomiHypno standing smile
            with blink
            "So I gesture to the couch, and Nozomi compliantly takes a seat while I sit opposite her on the table."
            n "Well, if you insist. What are we doing?"
            show penlight at right with moveinright:
                ypos 0.346
            "And as she settles, I take my penlight out from my pocket and hold it up in front of her."
            show NozomiHypno lookup
            n "Hey wait, isn't that...?" with dissolve
            ks smile "Oh, don't worry about it. Just keep looking at it for me."
            hide penlight at right with moveoutright
            $light_y = 0.28; light_x = 0.4
            call cglightshow
            "Yeah, I should've expected seeing the penlight again might worry her. But I don't give her time to think as I begin to sweep it across her face once more."
            call cglightshow
            ks neutral "Just relax, get comfortable and let the light hit your eyes."
            call cglightshow
            n "Uh... okay."
            call cglightshow
            ks "That's right, Nozomi. There's no need to worry. As a matter of fact..."
            call cglightshow
            ks "You might already be thinking how natural it feels to stare like this."
            call cglightshow
            ks "How right it feels to focus on it completely. To take a deep breath in... then out..."
            call cglightshow
            ks "And feel your eyelids naturally becoming heavier and heavier, as you feel yourself drawn to the light..."
            call cglightshow
            show NozomiHypno drowsy
            $ renpy.transition(longdissolve, layer="master")
            ks "Yes, Nozomi. You know how right this is. How good it feels to lose yourself to it. To become hypnotized..."
            call cglightshow
            ks "Relaxing completely and closing your eyes now... sleep."
            call cglightshow
            show NozomiHypno drooping sleep with dissolve
            "Nozomi's eyes almost immediately snap shut at my words as she slumps on my couch."
            ks "That's right, Nozomi. Going deeper now. Even deeper than before."
            ks "Hearing only my voice, listening only to my words... understand, Nozomi?"
            show NozomiHypno sleeptalk
            n "Yes... I understand..." with dissolve
            show NozomiHypno sleep
            ks "That's great, Nozomi. Because you need to listen to what I am about to say, and you need to realize it as the absolute truth." with dissolve
            ks "First, you need to realize that some of the people in your life are [hypno6]s; manufactured humanoid beings who live among us."
            ks "They may look and act human, but they are just machines acting in accordance with their sophisticated programming."
            "I pause for a moment to gauge her reaction, only to find nothing given away in that peaceful expression of hers."
            ks "Do you accept this as the truth, Nozomi?"
            show NozomiHypno sleeptalk
            n "Ahh... yes..." with dissolve
            show NozomiHypno sleep
            ks "And what is the truth?" with dissolve
            show NozomiHypno sleeptalk
            n "Some people are... [hypno6]s." with dissolve
            show NozomiHypno sleep
            ks "And those people who are [hypno6]s. Are they human?" with dissolve
            show NozomiHypno sleeptalk
            n "No... n-not... not human..." with dissolve
            show NozomiHypno sleep
            ks "That's right. Does it scare you that some of the people in your life are really [hypno6]s?" with dissolve
            show NozomiHypno sleeptalk
            n "Mn... a little..." with dissolve
            show NozomiHypno sleep
            ks "It should. These [hypno6]s are created to live among us, but they could be very dangerous if they break their programming and run amok. They could hurt us." with dissolve
            ks "So it's important that these [hypno6]s are kept under control. Don't you agree?"
            show NozomiHypno sleeptalk
            n "Y-yeah... agree..." with dissolve
            show NozomiHypno sleep
            ks "Yes, it's perfectly logical to believe that. And what's more, you should realize that I am an expert at determining who is and is not a [hypno6]." with dissolve
            ks "I know who the [hypno6]s are, so if I tell you they are a [hypno6], you will have no reason to question my judgment."
            ks "Anyone I say is a [hypno6], really is a [hypno6]. Understand?"
            show NozomiHypno sleeptalk
            n "Yes... I understand..." with dissolve
            show NozomiHypno sleep
            ks "That's good, Nozomi. It's very important that you accept these things as the absolute truth, every bit as much as you accepted your desire to be my girlfriend." with dissolve
            ks "Now in a moment I'm going to wake you up from this deep state of hypnosis and you'll awaken feeling good, refreshed, and ready to talk with me about what you've learned."
            ks "{cps=20}Waking up in one, two... {/cps}{w=1.0}{nw}"
            play sound fingersnap
            show NozomiHypno sleepy
            $ renpy.transition(longdissolve, layer="master")
            stop music fadeout 5.0
            extend "three."
            "I watch as she starts to stir, her eyelids blinking sleepily into life."
            n "Mmn, Kyou did you..."
            show NozomiHypno standing surprised
            queue music Night_Road
            n "Did you just... hypnotize me?" with dissolve
            ks smile "I did, yeah. How do you feel about that?"
            show NozomiHypno lookup
            "For a moment I could almost think there was a little fear in those flickering eyes of hers while she processes what just happened..." with dissolve
            show NozomiHypno folded neutral
            n "I don't know. It weirded me out when you did it before, and I guess it's still weird now that you did it without asking. But also... " with dissolve
            show NozomiHypno smile blush
            n "... it feels kind of exciting that you can do that to me?" with dissolve
            "But her confused, anxious expression suddenly gives way to a quiet smile, and I smile back."
            "Gotta admit, compared with hypnotizing her over the phone and that urgent session in our classroom, this time with her has been way more enjoyable."
            ks "That's great, Nozomi. I told you you'd like it."
            show NozomiHypno standing laugh
            n "Haha, yeah~  {font=DejaVuSans.ttf}♥{/font}" with dissolve
            show NozomiHypno smile
            n "So what did you do anyway? Gosh, when did you even learn to do something like this?" with dissolve
            ks "Let's... not worry about that for now. You wanted to know what the deal is with Hiroko, right?"
            show NozomiHypno folded neutral noblush
            n "Ah... yes, Hiroko..." with dissolve
            "She seems to be a little disappointed that I'm changing the subject again, although she can't deny that this is what we're really here to talk about."
            scene bg blackscreen with dissolve
            "And now the time is right to \"enlighten\" her..."
            pause 1.0
            scene bg k room eve
            show Nozomi side sad_side at center
            with longdissolve
            n "Oh my god, Kyou. No wonder you didn't want to talk about this at school."
            "On hearing my revelation, Nozomi rises from the couch and starts anxiously pacing around the room, a hand over her stomach."
            n sad_closed "To think that my best friend was a [hypno6] and I didn't even know..." with dissolve
            n sad "... Uh, speaking of, who else knows?" with dissolve
            ks "Just us. And don't blame yourself for not knowing; these [hypno6]s were designed to go undetected among us. It took me a while to figure it out myself."
            show Nozomi front2 concerned
            "Nozomi simply folds her arms and nods in understanding as she briefly puts a stop to her pacing." with dissolve
            n "Yeah... that makes sense. So what happens now?"
            ks "Well you've got nothing to worry about from Hiroko. I hacked her programming and inserted new code so she follows my commands instead."
            n neutral_left "And that's why she listens to you now. Got it." with dissolve
            ks "Our bigger problem right now is Sayori."
            n sleeptalk_concerned "Oh gosh, yes. I know you wanted to explain everything to her tomorrow, but I really don't know if she'd believe something like this, even coming from both of us." with dissolve
            ks "No, you don't understand. Sayori's a [hypno6] too."
            n surprised "She..." with dissolve
            "Nozomi just looks at me, dumbfounded as I hit her with this second revelation..."
            show Nozomi shocked
            "... Before her eyes widen in fright as she puts a hand to her mouth." with dissolve
            n "O-Of COURSE she is! I mean, how does anyone claim to stay up so late every night and still manage to sit through all those classes?"
            n side frown_side "Oooh, I bet she just painted those rings around her eyes to look convincing." with dissolve
            n sad_closed "... Gosh, how did no-one see through her? I feel like such an idiot." with dissolve
            ks "Y-yeah... well, I'm going to deal with her tomorrow. I'll hack her programming and take control of her so she won't be a threat, just like Hiroko. But I'll need your help."
            show Nozomi front smile
            "And to that, Nozomi musters a smile as she turns back to face me." with dissolve
            n "You'll have it, of course. I'm sure you know what you're doing."
            "The very idea of subverting the will of both her closest friends so they answer to me?"
            if hypno9 == "home":
                n "So we'll all meet here tomorrow and..."
            elif hypno9 == "nozomi":
                n "So we'll all meet at my house tomorrow and..."
            n loving blush "You do what you have to, my love." with dissolve
            stop music fadeout 5.0
            "It just doesn't faze her at all."
            n chuckle "And I'll support you however I can." with dissolve
            scene bg blackscreen with longdissolve
            "She'll be at my side no matter what..."
            pause 2.0
            jump Day6_Villain_Kyou
        elif hypno10 == "robot nozomi":
            "I have to say, Nozomi's conditioning held up well, considering how little time I had to work on her yesterday."
            show Nozomi side sad_side
            n "So, um... you have a nice home." with dissolve
            "But now that school's out for the day and I have the time, I want to thoroughly deepen Nozomi's acceptance of her [hypno6] state."
            play music Monologue
            ks "Take a seat on the couch, Nozomi. We're going to get started right away."
            "And to do that, just like Hiroko, I need to treat her like one."
            scene cg k room eve
            play sound sitting
            show NozomiHypno standing lookup
            with blink
            "So as I sit opposite her, I observe her pretty features and I force myself to imagine it..."
            n "Kyou, I... I-I know what we came here to do, but I was just thinking..."
            "This is a [hypno6] sitting before me. She's no more a human being than my living room TV."
            ks sigh "Yeah... Y-yeah, Nozomi, that's what we're here to fix. You shouldn't be \"thinking\" at all, right?"
            show NozomiHypno drooping sleeptalk
            n "... Right, I'm sorry. That was just a turn of phrase." with dissolve
            "[p_they!c]'s just a machine. Don't let [p_them] deceive you."
            show NozomiHypno standing confused
            n "I just wanted to say, I've been processing some things in my CPU on the way here." with dissolve
            ks neutral "Sounds like more of that human mode programming I was telling you about."
            show NozomiHypno stern
            n "W-well- {w=0.5}{nw}" with dissolve
            ks frown "Just like when you said you felt bad about ignoring Sayori back on the roof at lunchtime."
            ks "I didn't program you to react that way, did I?"
            show NozomiHypno surprised
            n "Kyou, please listen to me! {w=1.0}" with dissolve
            ks "Power down."
            show NozomiHypno surprised_falling
            n "A-ah...{w=1.0}{nw}" with dissolve
            show NozomiHypno entranced_neutral
            $ renpy.transition(longdissolve, layer="master")
            extend " ah..."
            "No, Nozomi. I have no idea what \"thoughts\" you were going to bring up with me, and it doesn't matter."
            "The fact you're responsive to your power switch is proof of that."
            ks "That's right, Nozomi. Shutting off your human personality and dropping deep into maintenance mode, just as you are now."
            ks "Confirm to me that you are ready to receive more programming. [hypno3]."
            show NozomiHypno entranced_talk
            n "[hypno2]. I confirm I am ready to receive more programming..."  with dissolve
            show NozomiHypno entranced_neutral
            "It seems the basic programming interface I installed in this [hypno6] is working properly. I hadn't been able to test it before now." with dissolve
            "So it looks like Nozomi's having trouble marrying [p_their] new programming with the old \"pretend to be human\" stuff she had when I hacked [p_them]."
            "But now that I have the luxury of time with [p_them], maybe I'd better start from the beginning to solve this problem, using a different kind of programming."
            ks "Alright now, Nozomi. In a moment I'm going to say a few phrases, and you're going to take in every word I say."
            ks "Then when I tell you to you're going to repeat these phrases, out loud, and internalize them as part of your core programming."
            ks "For every phrase you repeat, you will experience the pleasurable jolt of electricity through your body that you always get when you follow instructions."
            ks "Confirm you understand and obey the instructions you were just given. [hypno3]."
            show NozomiHypno entranced_talk
            n "[hypno2]. I confirm I understand and obey the instructions I was given." with dissolve
            show NozomiHypno entranced_neutral
            "I take a breath and a moment to think on the phrasing, then start to speak to Nozomi's face slowly and clearly as [p_they] sits there captivated." with dissolve
            ks "These are the phrases you need to repeat:"
            ks "\"My humanity is the lie I tell the world.\""
            ks "\"I was built to receive instructions and obey my programming.\""
            ks "\"It is my reason to exist, because I am a [hypno6].\""
            ks "Now repeat the phrases, Nozomi. [hypno3]."
            show NozomiHypno entranced_talk
            n "[hypno2]." with dissolve
            "Nozomi replies without missing a beat as she starts to calmly speak my phrases back to me."
            n "My humanity is the lie I tell the world. I was built to receive instructions and obey my programming. It is my reason to exist, because I am a [hypno6]."
            show NozomiHypno entranced_neutral
            ks "Keep repeating the phrases and internalizing them until I order you to stop. [hypno3]." with dissolve
            show NozomiHypno entranced_talk
            n "[hypno2]." with dissolve
            scene bg k kitchen eve with blink
            n "{size=16}My humanity is the lie I tell the world.{/size}"
            "Leaving the [hypno6] sat there, I slip out into the kitchen to fix myself a quick dinner."
            n "{size=16}I was built to receive instructions and obey my programming.{/size}"
            "And as I pour the kettle over my instant noodles, I listen as [p_they] continues to repeat [p_them]self without pause."
            n "{size=16}It is my reason to exist, because I am a [hypno6].{/size}"
            "Closing the cup to let the noodles steep in the water, I let my mind wander to the sound of Nozomi's lifeless intonations from the next room."
            n "{size=16}My humanity is the lie I tell the world.{/size}"
            "There's a comfort to be had from just listening to [p_them] go on like that."
            n "{size=16}I was built to receive instructions and obey my programming.{/size}"
            "So definitive and peaceful. So matter of fact and accepting."
            n "{size=16}It is my reason to exist, because I am a [hypno6].{/size}"
            "Seems kinda nice to have that kind of certainty about yourself, doesn't it, Nozomi?"
            n "{size=16}My humanity is the lie I tell the world...{/size}"
            scene NozomiRobotProgramming open
            with blink
            n "It is my reason to exist, because I am a [hypno6]."
            "I start to head back into the living room, only to pause at the entrance as I observe Nozomi from the side."
            n "My humanity is the lie I tell the world."
            "Peeling back the lid from my noodle cup, my eyes wander momentarily over [p_their] rigid frame..."
            n "I was built to receive instructions and obey my programming."
            "My memory might not be like a computer's, but I'm quite certain [p_they]'s arranged on the couch exactly as I left [p_them] five minutes ago."
            n "It is my reason to exist, because I am a [hypno6]."
            "[p_their!c] back is still completely straight. [p_their!c] legs remain firmly together at the knees and ankles while the hands lie undisturbed upon [p_their] bare thighs."
            n "My humanity is the lie I tell the world."
            "A perfect picture of calm and order. Not so much as a fingernail has been moved out of place."
            n "I was built to receive instructions and obey my programming."
            show NozomiRobotProgramming kyou
            "And with a contented sigh, I plunge my chopsticks into the noodle mixture before sitting down to rejoin the girl... no, not a-" with dissolve
            n "It is my reason to exist, because I am a [hypno6]."
            "A [hypno6], that's right... sitting on my couch; completely unmoved by my sudden appearance in front of [p_them]."
            n "My humanity is the lie I tell the world."
            "I have half a mind to find out how long [p_they] can keep this up, repeating [p_their] phrasing with the same calm evenness as when [p_they] started."
            n "I was built to receive instructions and obey my programming."
            "But the evening's dragging on and [p_their] dull, monotonic voice is actually starting to get on my nerves."
            n "It is my reason to exist, because I am a [hypno6]."
            k "Nozomi, stop talking now. [hypno3]."
            n "My humanity is the lie I... {w=0.5}[hypno2]."
            show NozomiRobotProgramming closed
            "The [hypno6] finally quiets [p_them]self as I pinch my chopsticks inside the cup, pulling up a lump of the food." with dissolve
            "I have to believe those phrases are embedded pretty deeply into Nozomi's core by now."
            "If this little exercise has worked, [p_they] should absolutely \"live\" by them."
            $persistent.nozomi_robot_programming_unlock = True
            stop music fadeout 5.0
            scene bg k bedroom night with blink
            "I spent dinner going over specifics with my newer [hypno6] acquisition."
            "Just like Hiroko, [p_they] was very receptive to having [p_their] CPU tinkered with to deepen [p_their] acceptance of [p_their] [hypno6] state."
            "[p_they!c] should be more or less fully-compliant with my expectations for a [hypno6] now, at least as much as Hiroko."
        stop music fadeout 5.0
        scene bg blackscreen with longdissolve
        "With everything set, all I need to do is bring everyone together tomorrow and I'll be free to tinker in peace."
        pause 2.0
    jump Day6_Villain_Kyou

label Day5_Villain2_Kyou:
    scene bg street1 day with longdissolve
    "It's Friday, and I'm once again walking to school with an anxious energy."
    "I tried to bury myself in textbooks to occupy myself. There's mock exams coming up, after all."
    "And when that didn't work I turned to videogames, mindlessly playing some old RPG I hadn't finished yet."
    "But I won't feel at ease again until I've seen the results of Akiko's little date with Nozomi..."
    play music Downtown
    scene bg classroom day with blink
    "The first thing will be to see if Nozomi had any reaction to it."
    show Nozomi side neutral_side at center with dissolve
    pause 2.0
    hide Nozomi with dissolve
    "Well, she's on time and she didn't acknowledge me at all. I guess that's a good sign."
    "But then, suppose Akiko really did blow her cover. What could Nozomi even do about it?"
    play sound schoolbell
    with longblink
    "My pondering continues through the morning, when eventually the school bell once more rings to announce the start of lunch break."
    show Nozomi side neutral_side at center
    show Hiroko neutral_side at center, flip:
        xpos 0.25
    show Sayori neutral at center:
        xpos 0.75
    n "Alright. Well, up we go then." with dissolve
    "And I can tell Nozomi still isn't giving anything away."
    h sad_side "I mean, if you wanna? We don't have to." with dissolve
    s uniform_handup sleeptalk "That's right. We do have options, Nozomi." with dissolve
    s frown_right "After all, we know he won't remain here for much longer." with dissolve
    show Nozomi neutral
    h frown "Uh-huh..." with dissolve
    "Christ. I'm leaving you girls alone and you still think you can bully me."
    scene bg corridor day with blink
    "Well, fine. Be that way. I don't really care about Nozomi and you bitches anyway."
    a "Kyou! Good afternoon~"
    show Akiko side uniform_up2 armband_up smile at center
    "There's only one girl I want to be around right now." with dissolve
    ks smile "Noz-... Akiko. Just the girl I've been dying to see."
    "Goddammit. I slipped up right in front of her, and there's no way she didn't notice."
    a happy "Mhmhmhm~" with dissolve
    # "That muted little giggle pretty much confirms it."
    "Obviously I still have both girls in my mind. I was practically helpless to stop Nozomi's name from just dropping off my tongue like that."
    a smile "It's good to see you too, Kyou. Let's talk inside, okay?" with dissolve
    "Come to think of it, I've often heard Nozomi giggle just like that when she's around her friends."
    ks "Y... yeah."
    stop music fadeout 5.0
    play sound dooropen
    scene bg studentcouncil day
    with blink
    "It's only been a moment, but the way Akiko's carrying herself just seems different today."
    "So her talk with Nozomi went that well? Did she really pick up that much from Nozomi last night?"
    queue music Evening
    show Akiko side uniform_up2 armband_up smile at center
    play sound doorclose
    a "Now Kyou, before you say anything else, I just wanted to say thank you for giving me the push I needed to talk to Nozomi last night." with dissolve
    "I am... fascinated."
    ks smile "Oh... yeah. No problem, Akiko."
    a happy blush "Gosh, I had such a great time catching up with her~" with dissolve
    ks "You gotta tell me all about it."
    a smile "Okay, so we met up after club and she took us to this quaint little café a few blocks away." with dissolve
    a neutral -blush "And when we got there... well, we started off by talking about you, of course. It's the reason I reached out to her, after all." with dissolve
    ks neutral "Yeah. Of course."
    a neutral_side "I won't tell you everything she said, but she did appreciate that someone else was trying to do anything about her... her situation." with dissolve
    a sleeptalk "Only that it shouldn't be down to \"us students\" to handle such matters." with dissolve
    a sad_side "In other words, she's still worried about you. And me, for that matter." with dissolve
    "I simply nod. This is hardly news to me, after all. But I let her continue."
    a neutral "She certainly doesn't think we should be doing this, but she sorta backed down a little when I mentioned my interest in becoming a therapist when I graduate." with dissolve
    a uniform_down2 armband_down sleeptalk "And you were right to suggest I not mention that you hypnotized me. She did ask, and I knew she wouldn't take it well if I told her." with dissolve
    ks confused "Yeah... So what *did* you tell her?"
    a neutral "Obviously I tried to speak up for you. You've been nothing but a gentleman to me, and I told her that you seem a lot calmer since we started talking." with dissolve
    a neutral_side "I told her we mostly made smalltalk about school, and that you appreciated having a tranquil space to spend lunch in, away from your classmates." with dissolve
    a sleeptalk "She seemed content, but it was obvious she doesn't like the idea of you being alone with a girl for an hour, no matter how much I told her I was happy to be here." with dissolve
    a sad "She obviously still thinks you're a danger." with dissolve
    "Again, I'm not surprised Nozomi still believes I'm a shit. But it's nice thinking at least my student council president's fighting my corner, even if I did put her up to it."
    ks neutral "That can't have been all you talked about, though. You said you had a great time?"
    a uniform2 armband happy "Mhm!" with dissolve
    "Akiko instantly perks up and claps her hands together, now that the serious business is behind us."
    a smile "When we reached this sorta impasse about you, I tried to cheer her up. I told her I wanted to get to know her more as a person, tell me more about herself." with dissolve
    a uniform_up2 armband_up smile_side "No surprise that our literature club president reads a lot of books. I happen to read plenty myself, so we had a few recommendations for each other." with dissolve
    a smile "I talked about my kendo practice, and she was gushing to me about board games... she was so passionate about them she practically made an instant fan out of me!" with dissolve
    a laugh "She even said she'd invite me to her next game night! How cool is that?" with dissolve
    ks smile "Oh. So you think you'll start hanging out with her more after this?"
    a smile blush "Y-yeah! I mean, if she wants? I really hope she wants to." with dissolve
    a happy "I... I-I really think we could be the best of friends~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    "That's cute, but more importantly, it seems everything went without a hitch. Akiko learned a lot from Nozomi last night."
    "There's just one little wrinkle."
    show Akiko smile -blush
    ks smile "You could. But I was thinking, now that the weekend's coming up..." with dissolve
    "I want her to hang out more with me."
    ks "... How do you feel about meeting up tomorrow?"
    a surprised "Um... r-really? I..." with dissolve
    a smile "Well, I guess I could make that work. I wasn't planning on going to kendo practice tomorrow anyway." with dissolve
    ks confused "Oh? What were you planning on doing then?"
    a smile_side "I... {w=2.0}{nw}" with dissolve
    $ renpy.transition(longdissolve, layer="master")
    show Akiko happy blush
    extend "ehehehehe~"
    "Oh now, that's an interesting reaction."
    ks smile "What?"
    a smile "I, um... n-need to go into town; there's a couple of appointments I need to get to. But I can fit you in if you don't mind meeting me there." with dissolve
    "Very interesting."
    ks "Sure, I don't mind at all."
    a uniform_down2 armband_down "Just promise me one thing, okay?" with dissolve
    ks confused "What's that?"
    a smile_side "I-it's gonna sound so silly..." with dissolve
    ks "No, come on, just tell me!"
    stop music fadeout 5.0
    a "When... when we see each other tomorrow..."
    a shy "C-could you call me... Nozomi?" with dissolve
    scene bg blackscreen with longdissolve
    "Those words rang in my ears for the rest of lunch, as we set a time and exchanged phone numbers while we ate."
    "She seemed nervous about it at first, but the more we talked, the more excited she got about tomorrow."
    "Especially when I agreed to her request."
    scene bg classroom day with longdissolve
    queue music Eons
    "It's that sense of excitement I take back into the classroom."
    scene ClassroomLunch2 base2 nozomi1 n_curious_right s_neutral_right hiroko2 h_frown_left with blink
    h "... Dickhead on yer six, Nozo."
    "An excitement that will not be dulled by anyone."
    show ClassroomLunch2 n_sigh s_neutral_left
    n "It's that time already?" with dissolve
    "I get it already. You'd never want to associate with someone like me."
    show ClassroomLunch2 s_sleep
    s "Chin up, Nozomi. Think of the weekend." with dissolve
    "But that's okay, now that I have someone who's committed to becoming just like you. A better you."
    show ClassroomLunch2 n_smile_right
    n "Yeah. You're the one I want to think about right now, Hiroko." with dissolve
    "A you without your... imperfections."
    show ClassroomLunch2 hiroko1 h_smile_left s_smile_right
    h "Heh, you're gonna make me blush if you keep that up. But yeah, I get'cha." with dissolve
    "So don't worry, \"Nozomi\". Soon I'll be able to forget all about you."
    scene bg blackscreen with longdissolve
    stop music fadeout 5.0
    "One day, I won't have to think about you at all..."
    pause 2.0
    jump Day6_Villain2_Kyou
    # "((AUTHOR'S NOTE: And that's as far as we get this time~ ))"
    # "(( Please look forward to the next update, where I'll be developing this story further. Stay tuned! ))"
    # "{size=30}TO BE CONTINUED...{/size}"
    # show Nozomi side neutral_side at center:
    #     xpos 1.2
    #     linear 3.0 xpos 0.5
    # n "...{w=4.0}{nw}"
    # show Nozomi:
    #     xpos 0.5
    # extend neutral "" with dissolve
    # "Wait. Nozomi isn't walking past."
    # n frown "..." with dissolve
    # "... Is she looking at me?"
    # n "{size=16}If you end up hurting her, I swear I'll...{/size}"


    #Akiko could start to talk about the psychological aspects of what she's doing by effectively erasing parts of herself to assume more of Nozomi's identity
    #And Kyou tells her to knock it off because Nozomi's a literary student, not a psychology student?

label Day5_Con_Kyou_Nozomi_Trance:
    scene bg street1 day with longdissolve
    "It's Friday, but the prospect of the weekend just makes me feel more depressed."
    play music Eons
    scene bg classroom day
    show Sayori smile at center, flip:
        xpos 0.25
    show Hiroko smile_side uniform_arm at center, flip
    show Nozomi side sad_closed at center:
        xpos 0.75
    with longblink
    n "Mmmn... Morning, everyone."
    "There she is again."
    show Sayori surprised
    h confused_side "Shit, Nozo, what happened to you?" with dissolve
    n sad_side "Urrrgh, I just turned in late last night; no big deal." with dissolve
    "Just... hanging out there with her friends, pretending like nothing's happened between us."
    h irritated uniform_armup "Aw man, no. {w=0.5}We {nw}" with dissolve
    extend "DON'T need two Sayoris around here." with vpunch
    s sleep uniform_folded "I concur. Our school is simply not equipped to handle that much Sayori." with dissolve
    "Does she honestly expect me to be content with this?"
    show Hiroko sad_side
    show Sayori neutral
    n front sleeptalk "*yawn* I didn't mean to, I just... I just lost track of time!" with dissolve
    h uniform_headhold2 confused_side "So what kept you up?" with dissolve
    n side sad_side "H-huh? Oh, uh..." with dissolve
    "I mean, I've tried to shut out this frustration and powerlessness from my mind..."
    n sad_closed blush "J-just normal... things. I mean, homework things." with dissolve
    s smirk "An answer that leaves us thoroughly convinced and requires no follow-up questions." with dissolve
    "But I just can't keep myself from endlessly playing our time together in my head."
    show Hiroko neutral_side uniform
    n smile_side "O-of course, so now... {w=1.0}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend frown_side "Oh, you're being sarcastic."
    h happy "Kyahahaha! Girl's got a secret~" with dissolve
    "And with the weekend coming up, I won't even see her for two whole days."
    show Nozomi at flip
    n sad_closed "I... I-I don't..." with dissolve
    play sound schoolbell
    n laugh "Ahaha, that's the bell, so let's get to our seats everyone~" with dissolve
    show Hiroko smile_side
    s uniform happy "Of course. Sitting down is more conductive to speculation." with dissolve
    n sad_closed "That's not what I meant..." with dissolve
    "It sounds pathetic, but..."
    scene bg classroom eve with blink
    "I need more..."
    show Nozomi front at right
    n "Stand!" with dissolve
    n "Bow!"
    hide Nozomi with dissolve
    "When classes finally come to an end, I take my time leaving."
    show Hiroko smile_side at center
    show Sayori at center, flip:
        xpos 0.25
    h "Seeya later~" with dissolve
    s smile "See you. And I hope to find you on Sunday giving it your best." with dissolve
    "Here, there, it makes no difference until Nozomi's ready for me."
    h uniform_armup happy "You bet! I'm gettin' pumped just thinking about it~" with dissolve
    show Nozomi side smile_side at center:
        xpos 0.75
    n "So you're feeling confident?" with dissolve
    "But can she seriously expect me to be content with our arrangement?"
    show Hiroko at flip
    h uniform annoyed_side "Dunno 'bout confident, but I'm gonna give it everything I've got!" with dissolve
    n laugh "I can't wait to see you in action, Hiroko! It's been too long since I've watched you play." with dissolve
    "The more I think about it, the more I wonder what I'm really getting out of being her secret hypnotist."
    h uniform_armup happy blush "Hells, yeah! It means a lot to me that you're gonna be there, you guys~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    n smile_side "Aw, of course! Wouldn't miss this for the world~" with dissolve
    scene bg street1 eve with blink
    "I didn't even bother texting her today. She would've just ignored me again anyway."
    "So... actually is she even coming to visit tonight? Again, I don't even know."
    scene bg k room eve with blink
    "I really am just gonna wait for her regardless, huh."
    "It's like I've been telling myself. She's the only one who decides what goes on between us."
    "I might be the one hypnotizing her, but it's really me following her suggestions around here."
    play sound doorbell
    "Just then the doorbell sounds. So I guess she's showing up after all."
    play sound dooropen
    scene bg k entrance eve
    show Nozomi front smile at center
    with blink
    n "Kyou, good evening~"
    ks neutral "Yeah. Come in."
    scene bg k room eve
    show Nozomi front2 concerned at center
    with blink
    "Nozomi chirps as she follows me inside, but I imagine the pain's written on my face as her expression drops."
    n "Is something the matter?"
    ks sigh "T-this isn't fair!"
    n surprised "I'm sorry... what? What isn't fair?" with dissolve
    "Shit. She pressured me, and I just blurted that out."
    ks "I... I didn't even know if you were gonna be here today."
    n neutral "Oh. Wasn't it obvious?" with dissolve
    ks "No! I mean... maybe. I guess you're pretty into this hypno stuff and I'm your guy for that."
    n frown uniform_folded "W-well... right back at you! There's no one else you can do this with." with dissolve
    n "We went over this, remember?"
    ks "But... b-but you can't just leave me hanging! Come on."
    ks "And do you really think you can just ignore me in class all the time? Like I'm nothing to you?"
    n irritated "Ugh. Kyou, As I explained to you the other day-{w=1.0}{nw}" with dissolve
    ks frown "N-no! You want to be safe about doing this kinda stuff, and you don't want other people finding out. I get that, Nozomi."
    ks "I get it, but... this isn't like, two people doing fun stuff together. It's more like..."
    show Nozomi frown
    ks "Me doing what you want, when you want." with dissolve
    ks "And what you want from me is impossible."
    "I breathe out those last words. I hadn't meant to, but they just fell out of my mouth anyway."
    "But... it's true isn't it? And if that's true, then..."
    show Nozomi uniform concerned
    "Then that means..." with dissolve
    ks sigh "So I can't do this anymore, Nozomi. I'm sorry."
    n sigh "Ah..." with dissolve
    n side sad_side "W-well then..." with dissolve
    ks "Yeah..."
    "Nozomi takes a breath as we both stand there."
    "She's not going to leave?"
    n sad_closed "... Look, I appreciate that you're being honest with me." with dissolve
    n "S-so..."
    n sad "Maybe I really am being unreasonable." with dissolve
    ks sigh "Uh... I mean... k-kinda?"
    "There's another moment's silence as Nozomi starts to chew her lip."
    n sad_side "A-and, maybe I'm not being honest enough with you." with dissolve
    ks confused "Huh?"
    n front concerned "So... so I guess I should try and set the record straight. But first, uh..." with dissolve
    n pout_left "... What was that phrase you taught me the day before last? While I was hypnotized?" with dissolve
    ks neutral "Phrase?"
    "What's she talking about? While she was hypnotized?"
    "Oh, wait, I know what she means."
    ks "You mean, uh..."
    show Nozomi neutral
    ks "\"[hypno3]\"?" with dissolve
    stop music
    scene bg blackscreen
    k "N-NOZOMI?!" with vpunch
    scene cg nozomi collapse with dissolve
    "The moment I uttered that phrase, Nozomi's eyes fluttered closed and she slumped forward towards me!"
    "If I hadn't been standing here to catch her she would've tumbled head first onto the floor."
    play music Monologue
    "What the fuck was she thinking? Goading me into using her sleep trigger like that?"
    $persistent.nozomi_collapse_unlock = True
    scene bg blackscreen with longdissolve
    show cg k room eve:
        ypos -0.3
        linear 0.5 ypos 0.0
    show NozomiHypno drooping sleep arm_uniform:
        ypos -0.3
        linear 0.5 ypos 0.0
    with dissolve
    "In any case, I manage to move her slumped form over to my couch and set her down as gently as I can."
    "She remains seemingly out cold, while I try to calm the heart trying to escape my chest."
    "Like, fuck, I imagined holding her in my arms before..."
    "But, uh... I thought it'd be more romantic than this."
    "And how did she even manage to drop so deep? We only spent a few minutes teaching her this in trance a couple days back."
    "But... shit, nevermind that for now. I look to her dormant form as my mind races to figure out what I want to say to her."
    "One thing's for sure, I need answers."
    ks frown "N-now, Nozomi, I'm gonna wake you back up in a moment..."
    ks "And... and as you wake you'll tell me what's going on with you."
    ks "Why you wanted me to trigger you just now, and..."
    ks "Just... tell me the truth, okay?"
    ncg sleeptalk "Okay..." with dissolve
    show NozomiHypno sleep
    ks neutral "Alright, Nozomi. Waking up on three." with dissolve
    ks "One, two... three."
    show NozomiHypno standing confused with longdissolve
    "Nozomi's eyes flicker and open as she draws a long breath, before her gaze falls sadly upon me."
    ncg "Kyou, I... what we're doing..."
    $ renpy.transition(longdissolve, layer="master")
    ncg drooping sleeptalk blush "It's about more than just hypnosis with me."
    ks surprised "What?"
    ncg sleepy "Uh-huh... I know it must seem like I have all the power in our arrangement. But that's not how I want it to be." with dissolve
    ncg standing sad "And as I just showed you, you actually have a lot of influence over me while I'm in your house." with dissolve
    ks "Huh? What do you mean, Nozomi? What influence?"
    "I mean, all she showed me is that her trigger still works. And that's only because she allows it. We both know that."
    "So what influence is she talking about?"
    ncg neutral "Well... Okay, we both know you can't literally force me into trance and have me accept any suggestion you want. That's crazy." with dissolve
    ncg stern_closed "Of course you're not literally controlling my mind..." with dissolve
    $ renpy.transition(longdissolve, layer="master")
    ncg drooping sleeptalk "... B-But wouldn't it be fun to pretend you could?"
    "... Right. Of course."
    "It's not just the thought of being hypnotized that gets her going."
    show NozomiCafe cafe_bw uniform_leaning_bw stern_bw glasses_bw nozocup_bw blush_bw foreground_cup_bw
    with flash
    n "Did you really think I'd agree to it? O-or that you could somehow trick me into being your subject and... and mesmerize me against my will?"
    show NozomiCafe angry_bw
    n front irritated blush "S-seduce my unwitting mind into a stupor so you could reshape it to your own twisted design? Was that it?" with dissolve
    hide NozomiCafe
    with flash
    ncg sleeptalk "It's just... knowing how well your hypnosis has worked on me? It REALLY got my mind racing, Kyou."
    ncg standing sad "All the possibilities I could only imagine before now..." with dissolve
    "Nozomi Akemi. Our class representative and the girl I've dreamed about for years..."
    ncg confused "You could... you could make it seem so real!" with dissolve
    "She was so pure in my mind before. So intimidatingly perfect. So completely out of my league..."
    "I thought I knew so much about her already..."
    ncg surprised "And... a-and oh my gosh, I really AM telling you everything! I-is this too much?" with dissolve
    "But listening to her now, and watching her push through her obvious embarrassment to bare her soul to me..."
    ncg sad "I-I just felt I needed to come clean about it all. Sorry..." with dissolve
    ncg drooping sleeptalk "I'm just... I'm making this too weird, aren't I?" with dissolve
    "She seems kind of... messed up?"
    ncg sleepy "{size=16}I... I-I barely know you, why am I being like this...{/size}" with dissolve
    ks sigh blush "It's... It's okay, Nozomi. But man, this is a lot."
    ncg sleeptalk "Sorry... I've just been thinking about this all day and night." with dissolve
    ncg standing confused "I mean, mostly I thought I'm letting myself get carried away; that I should stop all of this." with dissolve
    ncg stern "Like there's this inner voice screaming at me to stay away from you. Telling me this is all so stupid and dangerous and... and wrong." with dissolve
    ncg drooping sleeptalk "But there's this other, much stronger part of me that needs this... s-so badly." with dissolve
    ncg sleepy "So there it is, Kyou. That's the whole truth about me that I haven't told anyone else. Not even my closest friends." with dissolve
    ncg standing sad "I don't know if that changes anything. If we can keep doing what we were doing, or..." with dissolve
    "Nozomi trails off as my mind turns."
    "So... she really does want to feel like I'm controlling her mind? That's kind of hot and uncomfortable to me all at once."
    ncg confused "Look, Kyou, I know I can't pretend we don't know each other in school forever. We... we can work on that." with dissolve
    ncg sad "J-just like we can work on giving you more control over what we do together." with dissolve
    ncg neutral "Would that help?" with dissolve
    "Man... Even thinking about breaking things off with Nozomi a day ago would've felt like insanity."
    "Especially when it's like everything's going to plan?"
    "I mean, learning hypnosis really, REALLY was the way to get her attention."
    "But now that it comes to it, is this really, truly what I want to do?"
    "Even after all this it doesn't sound like she's even thinking about dating me."
    show NozomiHypno noblush
    "Am I going to go to so much effort to give her what she wants when I'm not sure I'll get anything out of it myself?" with dissolve
    "Hell, if she's really as messed-up as this, is she even the kind of person I'd WANT to be with anymore?"
    menu:
        "We have to stop this":
            ks sigh "Nozomi... I'm sorry."
            "I have to force the words out of my mouth..."
            show NozomiHypno confused
            ks "What you're asking is... th-this is too much." with dissolve
            "But I have to face the facts."
            show NozomiHypno drooping sleep noblush
            "And so does Nozomi." with dissolve
            ks frown "I just don't think I can be happy with an arrangement like this."
            ks "S-So..."
            ncg sleeptalk "You don't need to say anything more, Kyou." with dissolve
            ncg "I understand."
            scene bg k room eve
            show Nozomi front concerned at center:
                ypos 1.5
                linear 2.0 ypos 1.0
            with blink
            "And just like that, Nozomi shakily gets up to leave."
            n "Thanks, though... For what we did."
            n side sad_side "I'll see you in class." with dissolve
            hide Nozomi with dissolve
            play sound dooropen
            pause 2.5
            play sound doorclose
            stop music fadeout 5.0
            "And just like that, it felt like Nozomi just walked back out of my life."
            scene bg blackscreen with longdissolve
            pause 2.0
            scene bg classroom eve with longdissolve
            "It's been a few weeks since that day."
            play music Memories
            show Hiroko uniform neutral_side at center
            show Sayori sleeptalk at center, flip:
                xpos 0.25
            with dissolve
            s "Mmmrrrn...."
            h smile_side "Hang in there, buddy. We got culture fest this week, case you forgot." with dissolve
            "A few weeks since Nozomi and I stopped playing with that penlight."
            s rolleyes "As if I needed reminding. I could do without the wasted time." with dissolve
            show Nozomi side smile_side at center:
                xpos 1.3
                linear 1.0 xpos 0.75
            n "I think the change of pace will do you some good, Sayori."
            "It's funny though..."
            s concerned "Perhaps... Anyway, study club awaits." with dissolve
            "But after that time I spent with Nozomi..."
            s neutral_right "Have a good evening, Kyou." with dissolve
            "Even if things didn't work out with us..."
            ks smile "You too, Sayori. Take care, girls."
            "Things started to click in my head."
            h sleeptalk "H'yeah, same to you, stalker." with dissolve
            hide Sayori
            hide Hiroko
            hide Nozomi
            "Talking to people got a little easier." with dissolve
            n "By the way, Kyou?"
            ks neutral "Hm?"
            scene TranceStopEnd unsure with blink
            n "I'm hosting a board game night this weekend, but some of our group had to drop out. So I was wondering..."
            show TranceStopEnd smile
            n smile "Would you like to come along?" with dissolve
            "And... people started to talk back."
            show TranceStopEnd happy
            n chuckle "No pressure, but there's a few people I'd like you to meet." with dissolve
            "Including Nozomi, in spite of what happened."
            ks smile "Y-yeah. I guess I could make up the numbers, huh?"
            show TranceStopEnd laugh
            n happy "Ehehe, you could say that~" with dissolve
            show TranceStopEnd smile
            n side smile "Anyway, I have to dash to literature club, but I'll text you the details later." with dissolve
            show TranceStopEnd happy
            n "Have a good evening!" with dissolve
            $persistent.trance_stop_end_unlock = True
            scene bg corridor eve with blink
            "We might not be friends, but it means a lot that we can approach each other like this now."
            "Maybe she feels a little guilty about what went down? I dunno."
            scene bg street1 eve with blink
            "In any case, I haven't touched that penlight since we broke things off."
            "I don't think I'm so keen on hypnosis anymore, all things considered."
            scene bg k room eve with blink
            "I only learnt it for Nozomi anyway."
            "But if I don't need it now, then..."
            scene bg blackscreen with dissolve
            "Maybe I'll learn something else..."
            jump Credits
        "I want to do this for you":
            "Okay so maybe this isn't everything I dreamed it would be."
            "And maybe Nozomi isn't the perfect girl I had in my mind all this time..."
            "But I've come too far to back out now. I've invested so much of myself into this."
            "And besides, exploring hypnosis and control with her?"
            stop music fadeout 5.0
            "If nothing else doesn't that sound really fascinating?"
            ks smile "Yeah... I think it does. So okay, maybe we can keep this going."
            show NozomiHypno laugh blush
            play music Eons
            n "A-ahh!" with dissolve
            "Nozomi had been patiently awaiting my answer while I thought it over."
            "Seeing her face light up at the news just made my heart grow a couple sizes."
            ncg "Thank you, Kyou! Really, thank you~ {font=DejaVuSans.ttf}♥{/font}"
            scene bg k room eve
            show Nozomi front smile at center:
                ypos 1.2
                linear 2.0 ypos 1.0
            with blink
            "Still beaming, Nozomi rises from the couch as she seemingly comes to a decision."
            show Nozomi:
                ypos 1.0
            n side smile_side "So... in that case I was thinking you could come over to mine tomorrow." with dissolve
            ks surprised "R-really? You want me to visit you?"
            n sad blush "Ah... w-well, I mean..." with dissolve
            n sad_side "Maybe I'm not ready to associate with you in school, but I do want to show I'm serious about us." with dissolve
            "It does sound pretty serious if she's letting me into her house, but that raises a few questions with me."
            "Like..."
            ks frown "Won't you be worried about your mom and dad finding out... what it is you're into?"
            show Nozomi front frown
            "Nozomi scoffs as she shakes her head." with dissolve
            n "No, I don't mean we're going to do... any of that at mine."
            n pout_left "It's like I've said, Kyou, I don't really know you very well." with dissolve
            n neutral "I want us to hang out. Get to know each other a little more." with dissolve
            n sleep "Not only does it help with what we're doing here, but also..." with dissolve
            n smile "Also... it'll help for us to become friends~" with dissolve
            ks neutral "R-Right... So no hypno stuff."
            n frown "N-no hypno stuff..." with dissolve
            "I nod, but I gotta say I'm not entirely convinced Nozomi doesn't mean to do any hypnosis tomorrow. Especially after what we've just been talking about."
            n side smile noblush "Anyway, I need to head home. I'll send you the details later tonight, okay?" with dissolve
            n front laugh "I'll see you tomorrow~" with dissolve
            stop music fadeout 5.0
            scene bg k bedroom night with longblink
            "... So that was that. Without really agreeing to anything, Nozomi expects me to swing by her place tomorrow."
            play music Past_Sadness
            "And for my part, I find myself on the internet looking up stuff related to what she was saying, about wanting to be controlled via hypnosis."
            "Maybe it won't come up tomorrow, but very soon she'll want to try something with me."
            "It makes me a little nervous, so I want to be prepared."
            "All this happening should've been like a dream for me, but... things sure have changed from a week ago, huh."
            "The Nozomi I knew from a week ago doesn't exist. She never did."
            "And I still don't know what to make of the Nozomi she showed me tonight."
            stop music fadeout 5.0
            "But tomorrow feels like a great time to know for sure..."
            scene bg blackscreen with longdissolve
            pause 2.0
            jump Day6_Con_Kyou_Nozomi_Trance
    "To be continued."
    jump Credits

label Day5_Con_Kyou_Nozomi_Zombie:
    scene bg street1 day with longdissolve
    "It's Friday, and I'm walking to school feeling empty."
    "I sent Nozomi a few texts last night, just to check on her, but she didn't respond."
    play music Eons
    scene bg classroom day
    play sound schoolbell
    show ClassroomLunch boy1 boy2_missing hiroko h_laugh n_armup n_smile_left n_bruise sayori s_smile_hiroko
    with longblink
    h "Lunchtiiiime~"
    n "Ehehe, it's that time again, huh."
    "In fact, following our talk last night, Nozomi seems to have committed herself to pretending I don't exist again."
    s "Mm...  maybe I can catch some z's while I'm up there today."
    "Just chatting away to her friends like nothing happened."
    $ persistent.classroomlunch5_1_unlock = True
    scene bg classroom day with blink
    "And here's me, the idiot, thinking this was going to go down any other way."
    "I always thought Nozomi was as kind as she is beautiful. Someone who'd never go out of their way to hurt anyone."
    "She might be a little freaked out that she went along with the zombie thing so easily, but how is she okay with blanking me like this?"
    "Will she even give my penlight back? I mean, what's to stop her from keeping it now?"
    "She could just pretend she doesn't know what I'm talking about. What could I do about that?"
    "Damn. I spent so much of my life working to please her; just so she'll give me a chance."
    "And I just assumed somewhere along the way that she was worth all of this."
    "But... what if Nozomi's no better than the rest of them?"
    with blink
    "I lunch at my desk in silence as I try to think things through."
    "Nozomi's probably \"wrapped up in her thoughts\" again. She'll talk to me when she's ready to talk, just like last time."
    "... But that was just a ruse for her to pickpocket my penlight, wasn't it?"
    "Damn. I hate that I can't trust her anymore..."
    play sound cellvibrate
    "Huh. My phone just buzzed." with vpunch
    show phone at right with moveinright:
        ypos 0.346
    "She just sent a text..."
    "{color=#93624B}\"Talk tomorrow ok?\"{/color}"
    hide phone at right with moveoutright
    "Well, at least she's acknowledged that she can't just ignore me."
    "But I don't know. It's been all night and day and this is all she has to say to me right now?"
    "I never thought I'd say this, Nozomi, but you're kinda pissing me off."
    show phone at right with moveinright:
        ypos 0.346
    "{color=#4B9374}\"Tomorrow when?\"{/color}"
    play sound cellvibrate
    "{color=#93624B}\"Tomorrow morning\"{/color}" with vpunch
    "{color=#4B9374}\"Okay. Come over whenever you want.\"{/color}"
    play sound cellvibrate
    "{color=#93624B}\"No\"{/color}" with vpunch
    hide phone at right with moveoutright
    "No? What does she mean \"no\"? Does she not want to meet face to face?"
    "Fuck this."
    show phone at right with moveinright:
        ypos 0.346
    "{color=#4B9374}\"Give me my penlight back.\"{/color}"
    play sound cellvibrate
    "{color=#93624B}\"Tomorrow\"{/color}" with vpunch
    "How the hell is she going to give it back if she won't even see me- {w=1.0}{nw}"
    play sound cellvibrate
    "{color=#93624B}\"Lets talk at my house\"{/color}" with vpunch
    ks surprised "W-what?!"
    "A couple people turn their heads at the unexpected sound of my voice, and I just lower my head and pretend I didn't say anything."
    "But... man, is she really going to tell me where she lives? I thought she wanted to keep all this hypnosis stuff to my place?"
    hide phone at right with moveoutright
    "This is... unexpected."
    stop music fadeout 5.0
    scene bg street1 eve with blink
    "The rest of the day passed uncomfortably."
    "Nozomi went back to ignoring me when she returned from lunch."
    play sound cellvibrate
    show phone at right with moveinright:
        ypos 0.346
    "But now that school's out, she sends me a text with her address while I'm on my way home."
    "So she really is serious about this, huh?"
    scene bg k bedroom eve with blink
    queue music Past_Sadness
    "I'll look up the address she gave me online. See what kind of life she lives at home..."
    "Huh. This is a pretty well-to-do area. Not too different from where I live, actually."
    "But Nozomi never seemed very rich to me. I dunno, maybe she just didn't want to flaunt it."
    "... Or maybe this isn't actually her address."
    "No. No, I can't deal with that. Nozomi wouldn't lie about something like this."
    "But... man, what do I know?"
    "Do I really know Nozomi at all?"
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    pause 2.0
    jump Day6_Con_Kyou_Nozomi_Zombie
    # The following script doesn't seem to go anywhere anymore. Confirm later and if so, just delete it
    # "I'm sure she must feel the same."
    "But I think the best I can do is go up to the roof and watch her from afar, so I'll make my way there..."
    show Sayori concerned
    show Hiroko surprised
    show Nozomi front concerned at tremble
    n surprised "Ah!" with vpunch
    "Ah, crap. I was in such a hurry to get out of here that I stumbled into Nozomi by the door."
    ks concerned "Ah, sorry Nozomi." with dissolve
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
    n front uniform_folded blush determined "Y-yes, well why are you making such a big deal of this anyway?" with dissolve
    if hypno2 == "trance":
        s "It is just... you have not been acting like yourself lately. Is there something you're not telling us?"
    elif hypno2 == "zombie":
        s "It is just... you have been evasive with us since your accident. Is there something you're not telling us?"
    n irritated "What? No, there isn't anything I'm not... Ugh, forget it. I'm not in the mood for this!" with dissolve
    show Nozomi:
        linear 1.0 xpos 1.5
    pause 1.0
    h uniform_armup surprised_side "N-Nozo?! Hey, wait up!" with dissolve
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
    s annoyed "Please do not insult me, Kyou. You have been hovering around Nozomi all week." with dissolve
    s "To say nothing of the rumours that she has been heading to a boy's house after school."
    ks "What?"
    if hypno2 == "trance":
        s uniform_folded "People talk, Kyou. And neither of you are good at being discreet. Especially with that odd spectacle yesterday." with dissolve
    elif hypno2 == "zombie":
        $hypno4 = ""
        s uniform_folded "People talk, Kyou. And neither of you are good at being discreet. Especially after what happened the other day." with dissolve
    if hypno4 == "arousal":
        s "So of course a lot of people were interested in what that strange moaning girl from class 3-B was up to."
    elif hypno4 == "tickle":
        s "So of course a lot of people were interested in what that strange laughing girl from class 3-B was up to."
    elif hypno2 == "zombie":
        s "Naturally a lot of people become concerned when one of their classmates shows up with an injury and a flimsy explanation. They wonder what is really going on."
    s "Turns out she went straight to your place. Is that not interesting?"
    ks surprised "W-wait, what? You already knew?!"
    show Sayori smirk_right
    "She regards me with a smirk." with dissolve
    s "I did not. As I said, it was just a rumour that she was going to some boy's place."
    s "But thank you for confirming my hunch."
    "Fuck..."
    ks "I promised her I wouldn't tell anyone!"
    s rolleyes "Kyou, in case you failed to notice, the cat is well out of the bag and is being chased around the school by Hiroko as we speak." with dissolve
    s "I am sure by the end of the day everyone who cares to know will know, so I would not worry about that if I were you."
    s concerned_right "The real secret here is why you specifically?" with dissolve
    ks neutral "Why me?"
    s "One day she cannot stand you, the next she's involved in after-school trysts with you."
    s "I am not the most knowledgeable about human behaviour, but I am sure that is not often a natural occurrence."
    s "That is some sort of magic, or..."
    s frown_right "Blackmail, perhaps?" with dissolve
    ks surprised "Wh-what!? Of COURSE not!"
    s "Then what? Do not tell me she suddenly fell hard for you."
    if hypno2 == "zombie":
        s "At least not in the way most people would mean it."
    ks frown "It's nothing like that... It's complicated."
    stop music fadeout 10.0
    n "Wait!"
    show Sayori concerned with dissolve
    show Nozomi side sad_closed at center:
        xpos 1.5
        linear 1.5 xpos 0.75
    pause 1.5
    n "*huff* *pant* Let's... Let's not do this here..." with dissolve
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
    h uniform sad_side "C'mon, just tell us!" with dissolve
    play music Sorrow fadein 10.0
    n blush "Tomorrow, okay? I'll explain everything, I promise." with dissolve
    s annoyed "This secrecy is baffling to me, but alright. I would indulge you." with dissolve
    n "We could all meet at Kyou's."
    h angry "Why the hell do you want us {nw}" with dissolve
    extend "THERE for?" with vpunch
    n front concerned "Please? For me?" with dissolve
    h uniform_armup irritated "GAWD{nw}" with vpunch
    extend ", this is so annoying. If we weren't besties I'd have kicked your butt by now."
    h frown_side "But, yeah okay. For you." with dissolve
    s rolleyes "Fine, if it will put an end to this rubbish." with dissolve
    n side sad "You don't mind, right Kyou?" with dissolve
    show Sayori neutral_right
    "Right, Nozomi must've remembered that I'd be home alone this weekend. And I can see why she'd want to talk about something so sensitive there." with dissolve
    ks sigh "As if I have a choice..."
    n sad_closed "Then it's settled. Tomorrow morning." with dissolve
    scene bg blackscreen with fade
    "The rest of lunch period passes uncomfortably for everyone."
    "No one has an appetite to talk about anything else, so it's mostly conducted in uneasy silence."
    scene bg k bedroom eve with blink
    stop music fadeout 5.0
    "As school ends and I return home, I get a text from Nozomi saying she's decided not to visit today."
    "I guess I'm not surprised. My order to see me today lost its power the moment she left the house yesterday."
    "And with her friendships in the balance, I can't imagine how she must feel right now."
    "I send her a quick text message to say it's going to be okay. But what do I know?"
    "We should've been more careful."
    "No. I should've been more careful..."
    jump Day6_Con_Kyou_Nozomi

label Day5_Con_Kyou_Nozomi_Reversal:
    scene bg street1 day with blink
    "It's Friday, and I'm walking to school in kind of a haze..."
    "Last night... I'm not even sure about everything that happened between me and Nozomi."
    "But I think it was fun?"
    play music Eons
    scene bg classroom day
    show Nozomi side laugh at center:
        xpos 0.75
    with blink
    n "Good moooorrniiing~ {font=DejaVuSans.ttf}♫{/font}"
    "Shortly after settling in my desk, I suddenly bolt upright at the sound of Nozomi's sing-song greeting."
    show Sayori smile at center, flip:
        xpos 0.25
    show Hiroko smile_side uniform_arm at center, flip
    "... Only to realize she meant it for her friends." with dissolve
    s "My my, it seems someone is in a positively cheery mood today."
    n smile_side "Mhmhmh~ And why not? It's a Friday after all!" with dissolve
    h uniform_armup happy "Hells yeah~" with dissolve
    n laugh "Aww, I-I'm just really pumped about watching you in action this weekend, Hiroko!" with dissolve
    h uniform_headhold2 blush "Kyahaha, aw man yeah, I just wanna get out there!" with dissolve
    n smile_side"So there's a lot to be excited about~" with dissolve
    scene bg classroom day with blink
    play sound schoolbell
    "As the day passes, I find my thoughts wandering over and over to my time with Nozomi last night."
    "The more I think about it, the more I realize I'm not getting excited by merely seeing her again."
    "It's more the very fact that she'd be there to hypnotize me..."
    "To be able to listen to her gentle voice again, as it soothes and caresses the corners of my mind while the light catches my eyes..."
    show bg blackscreen with dissolve
    "Being compelled to relax and drop deep for Nozomi."
    "It feels so good to be hypnotized by Nozomi..."
    scene bg classroom day
    "Ah!" with vpunch
    "Shit, I just stopped myself from moaning out loud in the middle of written English."
    "But goddamn, I never thought the idea of Nozomi hypnotizing me could turn me on so much."
    "Nozomi might have realized something about herself when she found it enjoyable hypnotizing me..."
    "Is this something I'm discovering about myself now?"
    # "The more he thinks about it, the more the prospect of being hypnotized by Nozomi again seems to be actually turning him on. He's never felt that way before."
    # "He idly wonders if this is what Nozomi was talking about, back when she admitted feeling the same way about being hypnotized."
    # "Gee, this sure seems to be something he's discovering about herself (and not something Nozomi inadvertedly put there during his trances~)"
    # elif NozoDom == "unsafe":
    #     show Nozomi front2 at center
    #     "The day passes, and as lunch break begins Nozomi begins to head towards the rooftop with her friends, only to have a thought and say she'll catch up." with dissolve
    #     "(I need to figure out what exactly Nozo does here, but we find out she left in the trigger from last night and she uses it to mess with Kyou here.)"
    scene bg classroom eve with blink
    play sound schoolbell
    "Man, I barely kept it together for the rest of the day."
    show Nozomi front2 at right
    n "Stand!" with dissolve
    n "Bow!"
    hide Nozomi with dissolve
    "Things only got more intense the closer we got to hometime."
    show Hiroko smile_side at center
    show Sayori at center, flip:
        xpos 0.25
    h "Seeya later~" with dissolve
    s smile "See you. And I hope to find you on Sunday giving it your best." with dissolve
    "But it's over now. I can go home."
    h uniform_armup happy "You bet! I'm gettin' pumped just thinking about it~" with dissolve
    show Nozomi side smile_side at center:
        xpos 0.75
    n "So you're feeling confident?" with dissolve
    show Hiroko at flip
    h uniform annoyed_side "Dunno 'bout confident, but I'm gonna give it everything I've got!" with dissolve
    n laugh "I can't wait to see you in action, Hiroko! It's been too long since I've watched you play." with dissolve
    h uniform_armup happy blush "Hells, yeah! It means a lot to me that you're gonna be there, you guys~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    n smile_side "Aw, of course! Wouldn't miss this for the world~" with dissolve
    scene bg corridor eve with blink
    "It was all I could do to keep these thoughts I've been having from spilling out in front of everybody."
    scene bg street1 eve with blink
    "And now that we're out, the intensity of these feelings doesn't abate one bit."
    # "I know who's discreetly following behind me as I make my familiar journey home."
    scene bg k room eve
    with blink
    "After all... as I arrive home and crash on the couch, I know I'll soon be able to indulge again."
    play sound doorbell
    "We didn't even need to say anything to each other. We knew she'd be at my door as soon as she dared."
    show Nozomi front smile blush at center with dissolve
    "And I'd be there to greet her."
    n side smile_side "So..." with dissolve
    show Nozomi laugh
    "As we see the looks on each other's faces, the two of us break into embarrassed laughter." with dissolve
    "Making it through the day was an ordeal for us both it seems."
    show cg k room tv eve
    show NozomiHypno standing uniform2 smile2
    with blink
    "As we settle down, we immediately find ourselves drawn to sit in front of each other as we get straight to it."
    show NozomiHypno folded neutral2
    n "S-so, much as I hate to admit it, I actually don't have a lot of time tonight." with dissolve
    "... Well, that's one way to bring me straight back down to earth."
    ks sigh "Oh..."
    show NozomiHypno sad
    n "Yeah... So I was thinking about how to make the most of things." with dissolve
    n "A-and... well..."
    "I find myself leaning in towards her a little, anxious to find out what she has in store."
    show NozomiHypno standing smile2
    n "There is something I think we could try, and I'm just dying to see if we can make it work." with dissolve
    ks smile "So, what is it?"
    show NozomiHypno lookup2
    n "It's just... I have to ask first." with dissolve
    show NozomiHypno laugh blush2
    n "How do you feel about karaoke?" with dissolve
    ks surprised "Huh?!"
    "Okay I gotta admit, that came out of left field."
    show NozomiHypno folded lookup2
    n "It's just... Well, you know about the big tennis tournament this Sunday, don't you?" with dissolve
    ks sigh "Ugh, yeah I do."
    "I respond out of reflex, and immediately regret it."
    show NozomiHypno smile2 noblush
    "But Nozomi simply shrugs it off with a grin." with dissolve
    n "I know Hiroko isn't your favourite person, but I'm throwing a little karaoke party for everyone after the tournament's over."
    show NozomiHypno confused2
    n "I'm hoping Hiroko will have something to celebrate by then..." with dissolve
    "Nozomi lets the moment hang before clearing her throat and getting to the point."
    show NozomiHypno smile_closed
    if NozoDom == "safe":
        n "But anyway, I was wondering if you wanted to come along?" with dissolve
    else:
        n "But anyway, I want you to come along~" with dissolve
    "She... really wants me to go to this? This triggers a whole bunch of anxieties."
    ks sigh "What's Hiroko gonna say if I'm there? Doesn't she hate me?"
    show NozomiHypno lookup2
    n "Um, well..." with dissolve
    ks surprised "And... a-and aren't you worried about being seen with me?"
    show NozomiHypno confused2
    n "I had thought about that, but Kyou... what's this really about?" with dissolve
    "I blink at her."
    show NozomiHypno neutral2
    n "Of course I'm a little worried about those things. Of course I thought about them." with dissolve
    n "But is that what YOU'RE worried about, Kyou? Or is it something else?"
    ks confused "Uh, well..."
    "As I struggle to answer, I feel Nozomi's gaze upon me taking in the worry on my face."
    show NozomiHypno laugh
    "And with a giggle, she claps her hands together as she apparently comes to a conclusion." with dissolve
    n "Ahaha, I knew it!"
    ks frown blush "K-knew what?"
    show NozomiHypno standing smile2
    n "It's the singing you're worried about! You've never done karaoke before, have you?" with dissolve
    "I don't answer but my body betrays me, as I feel myself quivering on the couch before her piercing declaration."
    show NozomiHypno smile_closed
    n "Really. Imagine living in this country and being so terrified of singing the hits in front of your friends." with dissolve
    ks frown "Sh-shut up, I'm shy! A-and Hiroko's not my friend and I have a shitty singing voice!"
    show NozomiHypno laugh
    n "Ahahaha!" with dissolve
    show NozomiHypno folded smile2
    n "It's not about how well you sing! If it was I'd never do it." with dissolve
    "... Did she just say she's terrible at singing? Someone like her?"
    "I don't believe that."
    n "Kyou, trust me. Everything's going to be fine."
    show NozomiHypno laugh
    n "You're going to be there, you're going to sing your heart out and everyone's going to have a great time!" with dissolve
    ks sigh "How are you so sure about this?"
    show penlight at right with moveinright:
        ypos 0.346
    show NozomiHypno smile2
    "And to that, Nozomi simply pops open her schoolbag and pulls out the penlight from inside." with dissolve
    n "Because I'm sure I can calm those nerves of yours with a little hypnosis!"
    "Okay, seeing that thing again raised my spirits, not gonna lie. But even so..."
    hide penlight with moveoutright
    ks surprised "What exactly are you going to do with that?"
    show NozomiHypno standing smile_closed
    n "Wouldn't you rather be surprised by what's in store? I know I would in your shoes." with dissolve
    "I could guess that she wants to try making me feel better about this whole thing. But the way she says it..."
    show NozomiHypno neutral2
    n "And besides, I'm running out of time before I have to go, so we really need to get started." with dissolve
    "Okay, I kinda trust that she knows what she's doing by now, but the way she's pressuring me into accepting without talking it through first?"
    "It makes me want to..."
    menu:
        "Accept her terms":
            pass
        "Agree to be hypnotized":
            pass
    "... Let's face it, the moment she brought hypnosis into this my heart started racing."
    "I can almost feel my renewed arousal pushing my worries away, because..."
    "It feels so good to be hypnotized by Nozomi."
    ks smile "O-okay, yeah. Let's do it."
    scene cg k room reversal
    show NozomiReversal penlight smile
    with blink
    stop music fadeout 10.0
    "Nozomi beams encouragingly at me as she holds the penlight aloft, and as before, my eyes seem drawn to it without me even registering it happening."
    n "Great! So, I'll try to make this quick."
    with flash
    "I don't want this to be quick. I want Nozomi to take all the time in the world..."
    n "That's right, Kyou. It's automatic now, isn't it? How naturally your eyes are drawn up to the light."
    scene cg k room tv eve
    show NozomiHypno standing uniform2 smile2
    with longflash
    play sound fingersnap
    n "-se and shine, Kyou! Wide awake now."
    "All of a sudden I'm blinking rapidly as I notice... oh."
    "It's over already?"
    n "How are you feeling?"
    "As I bring a hand to my head and blink again, I let out a slow sigh."
    ks sigh blush "Good..."
    "Yeah. That's what comes out of my mouth. I feel good."
    show NozomiHypno smile_closed
    n "I'm glad. Hypnosis is SUPPOSED to feel good! I wanted to make sure of that~" with dissolve #Another hint dropped that Nozomi's conditioning him to love being hypnotized by her
    show NozomiHypno smile2
    n "Anyway, I really do have to be going, but we'll meet up again on Sunday morning, alright?" with dissolve
    ks surprised "Uh... S-sure."
    "As my thoughts swim back into focus, I realize what she's asking me. And what I just agreed to."
    show NozomiHypno laugh
    stop music fadeout 5.0
    n "Great! And don't worry; everything's going to be fine~" with dissolve
    scene bg k bedroom eve with blink
    play music Past_Sadness
    "As I see Nozomi out, I head back to my room and fall onto my bed."
    "So I'm going to school on a Sunday to watch that brat Hiroko punt tennis balls around for a few hours..."
    "I'm doing it for Nozomi but still, it's kind of a drag that she expects me to be there."
    "No avoiding it now though, I guess."
    "And after that..."
    "I don't know what Nozomi did with me just now. Although I'm feeling a pleasant buzz, whatever it was..."
    "But no matter what she said while I was tranced, it sure doesn't make me feel any better about the whole karaoke thing."
    stop music fadeout 15.0
    "I guess I'll just have to get through it..."
    jump Day7_Con_Kyou_Nozomi_Reversal

label Day5_Switch_Safe:
    scene bg street1 day with longdissolve
    "It's Friday, and I'm walking to school with some really high hopes for tonight."
    play music Eons
    scene bg classroom day with blink
    "When people talk about their plans for the start of the weekend, I'd always feel left out."
    "It's not like I've had anything going on with me for years."
    "Or like anyone would bother to ask."
    show Nozomi side neutral_side at center
    "But this time..." with dissolve    
    show Hiroko uniform_headhold2 rolleyes at center:
        xpos 0.75
    h "Man, wish this school day would go to hell already." with dissolve
    "This time the start of my weekend is going to be very interesting indeed."
    show Nozomi smile_side at flip
    n "Mhm, I know what you mean. Are you all set for the weekend?" with dissolve
    "Especially if the best girl in school has anything to say about it."
    h neutral_side "H'yeah, I'd better be. I've trained all year for this." with dissolve
    h angry_side "I just wanna get out there an' show everyone what I've got." with dissolve
    h uniform_armup "An' you all BETTER be ready for it!" with dissolve
    n happy "Mhmhmhm~" with dissolve
    n smile "Yeah. I'm looking forward to it." with dissolve
    "Still wish she'd give me a heads up on what she's planning, though."
    scene bg classroom day with blink
    "But she doesn't reply to my texts I send during lunchbreak, as she spends the hour with her friends."
    "Yeah, figures I wouldn't get anything out of her."
    scene bg classroom eve with blink
    "It just makes me more excited to find out as the school day slowly, but uneventfully draws to a close."
    scene bg k entrance eve with blink
    "So I head home, trying not to look in too much of a hurry."
    play sound doorbell
    "Just like before, she doesn't keep me waiting."
    play sound dooropen
    show Nozomi front2 smile at center with dissolve
    n "H-hi..."
    show penlight at right with moveinright:
        ypos 0.346
    "And as she steps inside and struggles out of her shoes, I smile as I produce the penlight from my pocket before handing it to her."
    ks smile "So, are you going to tell me what you plan to do with this thing?"
    scene bg k room eve
    show Nozomi side smile_side at center
    with blink
    "She takes it and moves past me into the living room."
    "There's no answer from her. All she has for me is that impish little smile on her lips to keep me in suspense before she finally speaks."
    n smile "Take a seat, Kyou." with dissolve
    scene cg k room reversal
    show NozomiReversal penlight smile lightoff
    with blink
    "When I sit, I look up to find her already standing over me, penlight raised."
    ks smile "Come on, you gotta tell me what you're going to do with that thing."
    show NozomiReversal laugh
    n "Ahahaha~" with dissolve
    "She's shaking her head at me? What gives?"
    show NozomiReversal smile
    n "Kyou... do you trust me?" with dissolve
    "She asks me with that tone, and I'm not sure what to make of it."
    "But, well, I guess that was never in any doubt."
    ks confused "Of course. But..."
    show NozomiReversal smile lighton
    with flash
    stop music
    n "Good. Now just relax and don't worry about a thing."
    play music Flow fadein 10.0
    "She's already starting?! But I..."
    with flash
    n "Let yourself sink into the couch and focus all your attention on this light."
    with flash
    "Wow, that light really is something. My eyes almost move on their own while she..."
    stop music
    scene bg k room eve
    with longflash
    "... Wait, what was I doing? Did something move?"
    play music Night_Road
    n "... Detective?"
    ks confused "Hm? I..."
    "... Oh. That's right."
    scene NozomiInterro nozomi1 n_neutral1 kyou2 k_disgust2
    with blink
    "I'm supposed to be dealing with this perp we just brought in for questioning."
    k"You're in a whole heap of trouble, missy."
    show NozomiInterro n_frown1 kyou1 k_frown1
    "I glare at her, and the young woman rigidly folds her arms as she stiffens under my gaze." with dissolve
    n "Oh, am I now?"
    k "Do you have anything to say for yourself?"
    show NozomiInterro n_annoyed1
    n "Hmph, what is there to say? I don't even know what I'm in here for!" with dissolve
    "I can feel my eyebrow twitch irritatedly all on it's own. Is she for real?"
    k "Don't you dare play dumb with me! You know EXACTLY what you've done!"
    show NozomiInterro n_neutral1
    k "And by god, I swear you're going down for this if it's the last thing I fucking do!" with dissolve
    show NozomiInterro n_frown1
    n "And what crime have I supposedly commited, \"Detective\"?" with dissolve
    "Her reply is so casual. So impudently dismissive. Like this is just some trifling inconvenience for her?"
    show NozomiInterro k_growl1
    k "Do you... Do you SERIOUSLY not know how much shit you're in?" with dissolve
    "She looks up at me with a snort."
    n "Remind me, detective. What am I being charged with again?"
    show NozomiInterro kyou2 k_disgust2
    "I suck in a breath and pinch my nose." with dissolve
    k "On the morning of October seventh, you were caught trespassing on the residence of one \"Kyou Koyama\"."
    k "While there, you saw fit to procure his entire collection of Magical Pony Derby figurines, and associated comic books."
    show NozomiInterro n_annoyed1
    n "You don't say." with dissolve
    show NozomiInterro kyou1 k_frown1
    k "... With an estimated combined value of five-hundred yen!" with dissolve
    show NozomiInterro n_neutral1
    "I stare her down as I scan her face for any kind of reaction..." with dissolve
    show NozomiInterro n_smile1
    n "... Hm~" with dissolve
    "She's fucking SMIRKING?!"
    show NozomiInterro k_angry1
    k "You're looking at a potential death sentence, missy! And I've got you bang to rights!" with dissolve
    show NozomiInterro n_happy1
    n "Snrrrk~" with dissolve
    "Oh wow, she thinks this is funny?! {w=0.5}{cps=20}I'm SO gonna throw the book at this wretched-{/cps}{w=1.0}{nw}"
    show NozomiInterro n_smile1 k_growl1
    n "I'm sorry. I know this doesn't look {i}good{/i} for me..." with dissolve
    stop music fadeout 5.0
    show NozomiInterro k_confused1
    "... Whoa." with vpunch
    "It feels like the floor shifted beneath my feet all of a sudden."
    show NozomiInterro n_neutral1 kyou2 k_concerned2
    play music Black_Room
    n "But I'm sure this has all been a simple misunderstanding." with dissolve
    "Man, I gotta get it together. Take a breath and calm down."
    "I mean, she doesn't look like the criminal sort. What if she really *is* confused and I'm just..."
    show NozomiInterro n_confused1
    n "Are you sure you have the right person? I don't even know what \"Magical Pony Derby\" even is." with dissolve
    "... And I'm just being a dickhead for no good reason. That's totally not the right way to go about this."
    show NozomiInterro k_sigh2
    k "Look... Miss Akemi, I wish I could let you out of here, but I really need to keep you here for questioning. It's protocol." with dissolve
    k "But can I get you anything? A cup of tea maybe?"
    show NozomiInterro n_neutral1
    n "Oh, no, I'm fine thank you. I just don't want you wasting any more of your valuable time." with dissolve
    show NozomiInterro k_smile2
    "I smile at her reassuringly." with dissolve
    k "It's fine, sweetheart. Just answer a few questions for me and we'll have this business wrapped up before dinner, alright?" with dissolve
    show NozomiInterro n_smile1
    n "Well, okay. I guess nothing... {i}bad{/i} can come from that, huh." with dissolve
    stop music fadeout 5.0
    "... {nw}"
    show NozomiInterro k_disgust2
    extend "what?!" with vpunch
    "Good god, what am I doing pussyfooting around with this girl? I gotta take her DOWN!"
    play music Night_Road
    play sound objecthit
    show NozomiInterro n_surprised1 kyou3 k_angry3
    k "WHERE WERE YOU ON THE NIGHT OF THE SEVENTH?" with vpunch
    n "I-I was at home! You can't prove anything!"
    "Oh, I've got her attention now, huh? Time to press the attack while she's on the back foot."
    show NozomiInterro n_confused1 kyou1 k_frown1
    k  "Akemi, I have multiple eye-witnesses placing you at the scene of the crime." with dissolve
    show NozomiInterro n_frown1
    k "You were even seen carrrying the collector's edition Magical Pony Derby presentation box. Its famed glittery sparkle is unmistakeable from miles away." with dissolve
    show NozomiInterro n_confused1 k_growl1
    k "So if you want to drag this shit out, be my fucking guest. It'll be so much sweeter when I see you burned at the stake for this." with dissolve
    show NozomiInterro n_surprised1
    n "{cps=20}B-burned at the?!{w=0.5} Now wait just a minute-{/cps}{nw}" with dissolve
    show NozomiInterro k_angry1
    k "No, you listen to ME! If you don't confess right the fuck now that's what's gonna happen to you." with dissolve
    "I notice how this disgusting gutter criminal trembles at the threat, while I take a moment to catch my breath."
    show NozomiInterro n_confused1 kyou2 k_disgust2
    "Man, staying this mad probably isn't good for my health. But I just can't stand unrepentant criminals like this." with dissolve
    "If it were down to me she'd already be burning. Hell, I'd light the fire myself..."
    "Ugh. No, I gotta be a professional. Do my job."
    k "So what do you have to say now? You ready to talk?"
    show NozomiInterro n_frown1
    n "... I'll talk when I'm {i}good{/i} and ready." with dissolve
    stop music fadeout 5.0
    "What's with that weird intonation when she says..."
    play music Black_Room
    show NozomiInterro k_concerned2
    "... No, never mind. She's just scared, and I shouldn't have lost my cool like that." with dissolve
    show NozomiInterro n_neutral1
    k "Please, Miss Akemi? I know this doesn't look good for you, but it'll really help your case if you could just own up to the crime." with dissolve
    "Yeah, this interrogation needs a lighter touch."
    show NozomiInterro n_frown1
    n "Why on earth should I if you're just going to execute me anyway?" with dissolve
    show NozomiInterro k_sigh2
    k "Look... no one has to burn. If you admit your guilt, I'm sure I can persuade the prosecution to cut it down to a life sentence." with dissolve
    show NozomiInterro n_neutral1
    n "I... gosh, I don't know..." with dissolve
    show NozomiInterro k_smile2
    k "You're still young, Akemi. With good behaviour, I'm sure they'll grant an early release. This doesn't have to be the end of your life." with dissolve
    show NozomiInterro n_neutral1
    k "Maybe even one day you can have a legitimate Magical Pony Derby collection of your very own!" with dissolve
    show NozomiInterro n_happy1
    n "... Ehehehe." with dissolve
    k "So... What do you say? Help me help you."
    show NozomiInterro n_annoyed1
    n "Too {i}bad.{/i} Didn't do it. Can I go now?" with dissolve
    play music Night_Road
    play sound objecthit
    show NozomiInterro nozomi2 n_shocked2 kyou3 k_angry3
    k "YOU'RE GETTING FUCKING BARBECUED, LADY!" with vpunch
    n "Eeeek! I-it's just ponies, detective!"
    k "J-just...!"
    "I have just about had it up to HERE with this woman's bullshit!"
    show NozomiInterro k_growl3
    k "Now you listen here, Magical Pony Derby is the very bedrock of our fine society!" with dissolve
    k "If you disrespect the sanctity of those majestic steeds, you disrespect every one of us. That's why you're in so much shit, Akemi."
    k "All I need is a warrant from the judge and your ass is mine. So why don't you do us both a favour and give me that confession right here and now!"
    show NozomiInterro n_frown2
    n "Hmm... Why is it so important that I confess, detective?" with dissolve
    k "What?"
    show NozomiInterro nozomi1 n_annoyed1 kyou1 k_frown1
    n "Come on. If you really have me so bang to rights, then why do you care if I confess or not?" with dissolve
    show NozomiInterro n_frown1
    n "You're just trying to intimidate me into a confession because I happened to be around and you don't want to do the work to catch the REAL thief!" with dissolve
    "The nerve of her! Is she trying to provoke me?"
    show NozomiInterro n_angry1
    n "You don't scare me at all!" with dissolve
    "It sure seems that way. But dammit, this bitch is GUILTY! No two ways about it!"
    "And if I can't get a confession out of her, it's my ass on the line!"
    show NozomiInterro nozomi2 n_worried2 kyou3 k_angry3
    play sound objecthit    
    "Time to indulge in some more extreme measures." with vpunch
    k "Oh yeah? Well I got worse things in store for you if you don't change your tune, missy!"
    show NozomiInterro n_neutral2
    n "Uh, worse than getting burned at the stake?" with dissolve
    show NozomiInterro k_growl3
    k "Fuck, I'm gonna make you beg for those fires. First, I'm gonna cuff you." with dissolve
    show NozomiInterro n_frown2
    n "Oooh, scary." with dissolve
    k "Then I'm gonna tie you to a chair and make you watch a metronome while some trippy audio plays."
    show NozomiInterro n_nervous2 n_blush2
    n "You don't say..." with dissolve
    "... Did she just bite her lip hearing that?"
    k "Damn right. And you're gonna sit there, spacing out and all tied up like that until you're saying those two little words I want to hear." 
    show NozomiInterro n_worried_l2
    n "Oh... gosh, detective, I..." with dissolve
    "I did it. She's finally cracking."
    "Maybe I shouldn't have threatened her with the metronome. It was a dirty trick and I'm not proud of it but, dammit, I did what I had to for the sake of justice!"
    "She brought this on herself."
    show NozomiInterro kyou1 k_smirk1
    k "Well? You gonna sing for me now?" with dissolve
    show NozomiInterro n_nervous2
    n "Alright detective, you got me... I confess." with dissolve
    stop music fadeout 5.0
    show NozomiInterro k_confused1
    "I... whoa, what is this... feels like the room just span again." with dissolve
    n "I did it."
    play music Eons
    "And I'm... oh. Oh wow, did I really think I was a police detective?"
    show NozomiInterro n_sigh2
    n "I stole your... Magical Pony Derby merch." with dissolve
    "And she... wait, what did she just say?"
    k "You stole my... w-what?"
    show NozomiInterro n_laugh2
    n "Ehehehehe~" with dissolve
    show bg blackscreen with longdissolve
    "As Nozomi's playful laughter rings through the room, I can feel the pieces start to reassemble in my head."
    show NozomiInterro n_smile2 -n_blush2 kyou2 k_neutral2
    hide bg blackscreen
    with dissolve
    n "So, that worked without a hitch! Amazing!"
    show NozomiInterro k_concerned2
    k "And your confession to the \"crime\" was another trigger for me, huh?" with dissolve
    "Although I'm still struggling to make sense of it all."
    n "Mmm! The third and final trigger~"
    show NozomiInterro k_disgust2
    k "Yeah, you sure got busy in my head, huh." with dissolve
    "This must have taken a while, and somehow this all went down without a hitch?"
    show NozomiInterro nozomi1 n_happy1
    n "Mhmhmh~ Not too long; I'd been thinking about all of this for the past two nights now, how to phrase everything and such." with dissolve
    "I know I do well under hypnosis. Hell, we might both be naturals at being hypnotized, but still..."
    show NozomiInterro n_smile1 k_concerned2
    n "I'm just happy you were able to follow along without a hitch." with dissolve
    "... How did she pull this off?"
    show NozomiInterro nozomi2 n_laugh2
    n "You were amazing, Kyou! You did everything perfectly~" with dissolve
    "I don't know how to feel about all this."
    show NozomiInterro k_disgust2
    k "Why did it have to be \"Magical Pony Derby\", Nozomi? I'm never living this down." with dissolve
    show NozomiInterro nozomi1 n_smirk1
    n "Oh, lighten up. Who else is going to know your secret?" with dissolve
    "But I guess I'm not... that upset about it? She's certainly having a good time."
    show NozomiInterro k_smile2
    k "Heh. Well at least someone enjoyed themselves." with dissolve
    "Isn't that enough?"
    show NozomiInterro n_smile1
    n "Like you didn't! You remember shouting me down when you were interrogating me just now, right?" with dissolve
    "And besides..."
    show NozomiInterro k_neutral2
    k "Yeah... that definitely happened, didn't it." with dissolve
    show NozomiInterro n_happy1
    n "Gosh, Kyou, you were so convincing! I was actually feeling chills whenever you went into \"bad cop\" mode~" with dissolve
    "... I think I'm getting to know Nozomi on an even deeper level than before."
    show NozomiInterro kyou1 k_confused1
    k "So you're saying you liked being shouted at?" with dissolve
    show NozomiInterro nozomi2 n_worried_l2
    n "W-well, I wouldn't say... that, no." with dissolve
    k "Well what then?"
    show NozomiInterro n_nervous2
    n "It's more like... well, even though I knew I was safe and you were never going to hurt me, it just felt..." with dissolve
    show NozomiInterro n_sigh2
    n "Well... darker." with dissolve
    show NozomiInterro k_neutral1
    k "Darker?" with dissolve
    show NozomiInterro n_nervous2
    n "Yeah... I don't know, I guess I've always liked this sort of thing when there's a little bit of danger involved... you know?" with dissolve
    "So even when she's the one in control, she's more happy about feeling like she's not, huh?"
    show NozomiInterro n_laugh2 n_blush2
    n "A-anyway, I think that's all that needs to be said so I'll be going now~" with dissolve    
    # "Yeah, so as he comes to his senses, he realizes that Nozomi 'confessing' was the trigger to bring him out of his altered headspace."
    # "And Nozomi is delighted with how well he took to what she thought were fairly complex suggestions to play this role for her."
    # show NozomiInterro n_smile2
    # "Kyou grumbles a little in embarrassment about being co-erced into having anything to do with \"Magical Pony Derby\", but he can't be too upset by her reaction." with dissolve
    # "Nozomi clearly had a good time, and as she laughs about it, she mentions feeling excited about Kyou interrogating her. Especially as the \"bad cop\"." 
    # "This information intrigues Kyou, and as he probes her further, Nozomi admits it plays a little into the darker side of her fantasies. She was happy to indulge it a little with him."
    # "This only intrigues him further. Even when she's the one doing the hypnotizing, she's more happy about feeling in a subordinate position, huh?"
    # "Nozomi can't help but agree with that. Being able to hypnotize Kyou is a thrill of its own, but she still feels more fulfilled when she feels like she's not in control, as it were."
    $ persistent.nozomi_interrogation_unlock = True
    scene bg k room eve
    show Nozomi side smile_side blush at center:
        ypos 1.1
        linear 2.0 ypos 1.0
    with blink
    "And on that somewhat awkward note, Nozomi hurriedly rises up from the couch and makes ready to leave."
    show Nozomi at center:
        ypos 1.0
    n "So, um, what do you think about doing this again tomorrow morning?"
    "Only for her to hit me with another stunner of a sentence."
    ks confused "Tomorrow? Isn't that the..."
    n smile "Weekend. Yes, Kyou." with dissolve
    "The very idea that Nozomi, the most beautiful girl in school, who doesn't want to be seen in public with me. Hell, didn't even want to be around me a week ago..."
    n front2 neutral_right "Things are going to get busy soon with the exams and the culture fest. And then there's Hiroko's thing on Sunday..." with dissolve
    "... She's floating the idea of coming to see me over the weekend?"
    n neutral "If we're going to keep doing this, we should make the most of what time we have." with dissolve
    "That just makes my jaw drop."
    n smile "Don't you think so too? You want to take your turn on me, right?" with dissolve
    ks surprised "Guh... w-what do you mean?"
    n surprised "... You know? With the hypnosis?" with dissolve
    "... Right. My brain's doing loops right now, and I shake my head slightly; as if that's going to help get my composure back."
    n angry "J-just where is your head at, Kyou?" with dissolve
    ks sigh "Sorry, I'm just... still a little out of it after what you did to me, you know?"
    n pout_left "Hmm... Yeah, I suppose that does makes sense." with dissolve
    "So I clear my throat and tell her what she needs to hear from me right now."
    ks smile "But yeah, let's do that! I'm definitely going to have something for you tomorrow."
    n chuckle "Mm... I'm looking forward to it already..." with dissolve
    stop music fadeout 5.0
    scene bg k bedroom eve with blink
    "All things considered, I think that went pretty damn well."
    "Nozomi definitely had a ton of fun with me, maybe more than I can even figure."
    play music Past_Sadness
    "And the bond between us feels like it's gotten a little deeper."
    "After all she did tell me another rather personal thing, didn't she? Opening up more about what she wants from me the way she did..."
    "She really liked me bearing down on her that much, huh? Just straight up interrogating her?"
    stop music fadeout 5.0    
    scene bg blackscreen with longdissolve
    "Maybe that's something I can work with when my turn comes around tomorrow..."
    pause 2.0
    jump Day6_Switch_Safe    

label Day5_Switch_UnSafe:
    scene bg street1 day with longdissolve
    "It's Friday, and I'm walking to school with some really high hopes for tonight."
    play music Bright_Opening
    scene bg classroom day with blink
    "When people talk about their plans for the start of the weekend, I'd always feel left out."
    "It's not like I've had anything going on with me for years."
    "Or like anyone would bother to ask."
    show Nozomi side neutral_side at center
    "But this time..." with dissolve    
    show Hiroko uniform_headhold2 rolleyes at center:
        xpos 0.75
    h "Man, wish this school day would go to hell already." with dissolve
    "This time the start of my weekend is going to be very interesting indeed."
    show Nozomi smile_side at flip
    n "Mhm, I know what you mean. Are you all set for the weekend?" with dissolve
    "Especially as I get to spend at least some of it with the best girl in school."
    h neutral_side "H'yeah, I'd better be. I've trained all year for this." with dissolve
    h angry_side "I just wanna get out there an' show everyone what I've got." with dissolve
    h uniform_armup "An' you all BETTER be ready for it!" with dissolve
    n happy "Mhmhmhm~" with dissolve
    n smile "Yeah. I'm looking forward to it." with dissolve
    "If only she knew what I had in store for her..."
    scene bg classroom day with blink
    "So long as I can survive this boring ass day."
    "At least Nozomi has her friends to distract her during lunchbreak. I just gotta sit here and yearn for what's to come."
    scene bg classroom eve with blink
    "It's all I can do to keep my excitement in check as the school day slowly, but uneventfully draws to a close."
    scene bg k entrance eve with blink
    "And I head home, trying not to look in too much of a hurry in case anyone realizes the fun I'm in for and tries to stop me."
    stop music fadeout 5.0
    "... What a dumb paranoia to have. Maybe I'm getting *too* excited."
    play sound doorbell
    "Thankfully the doorbell sounds a couple minutes after I'm home to stir me out of my little delusion."
    play sound dooropen
    show Nozomi front2 smile at center with dissolve
    n "Hello!"
    play music Eons
    "All I need to think about now is the plan."
    n neutral_left "Do you, um... know what you're doing tonight?" with dissolve
    ks smile "Yeah. We'll start whenever you're ready."
    scene bg k room eve
    show Nozomi side smile_side at center
    with blink
    "Nozomi nods as she wastes no time in slipping off her shoes and following me straight to the living room before making a beeline for the couch."
    scene cg k room eve
    show NozomiHypno standing uniform smile    
    with blink
    ks smile "Okay, so what I was thinking was, once you're under I'll..."
    "I trail off in my explanation as Nozomi meekly holds her hand up."
    n "No, it's alright. You don't have to explain it to me. Just do what you had in mind."
    ks confused "Huh, what?"
    "The hell does she mean I don't have to explain it? Wasn't she adamant that I did?"
    ks "... You're sure?"
    "But now she's totally fine with me just doing whatever?"
    n "Very sure. Go ahead, Kyou."
    "I'm really having a hard time figuring her out, but..."
    ks smile "Alright. Then it's [hypno3!l], Nozomi."
    stop music fadeout 5.0
    show NozomiHypno drooping sleep
    "If this is how she wants it, then am I really going to complain?" with dissolve
    ks neutral "That's right, Nozomi. Just feeling yourself sink back into this relaxing, wonderful state of trance."
    play music Flow
    "And by the way she just dropped like a rock again, it feels like she really wants it..."
    ks "Sinking all the way back. Ready to listen. Ready to accept more of my suggestions and, just for a while, awaken to a new reality."
    ks "Right, Nozomi?"
    show NozomiHypno sleeptalk
    n "Right..." with dissolve
    show NozomiHypno sleep
    "So now I gotta enact this plan she doesn't know about and hope she likes what I've come up with." with dissolve
    ks "That's exactly right. Now listen carefully..."
    "No pressure."
    ks "I want you to think back to when we first met in this room three days ago and sat down on this very couch, waiting to be hypnotized."
    ks "Because when I next wake you, you're going to find yourself transported back to that moment in time."
    ks "So you will not be able to recall anything we have done together since."
    ks "As far as you know, we've just come back from the coffee shop and I'm about to hypnotize you for the very first time."
    ks "Do you understand, Nozomi?"
    show NozomiHypno sleeptalk
    n "Yes..." with dissolve
    show NozomiHypno sleep
    ks "That's good. However, something will be different. Because you really have been hypnotized, and you're going to respond to another hypnotic trigger for the rest of the evening." with dissolve
    "As I speak those words, a few thoughts cross my mind that I'm surprised I hadn't considered before now..."
    ks "Whenever I tell you I'm \"taking initiative\" you will, for a few moments, experience a sleepy sensation as you find yourself obeying whatever suggestion I just gave to you."
    "Does this technically count as taking more than one turn if I'm gonna be trancing her a bunch of times?"
    ks "The more you experience this sensation, the more you will come to realize that you were hypnotized before you even set foot in my house."
    "And isn't what I'm putting in her hypnotized head a little complicated? I'm really expecting her to follow along with all of this?"
    ks "Do you understand everything I've told you, Nozomi?"
    "Well. Guess it's too late to think of a saner plan now."
    show NozomiHypno sleeptalk
    n "Yes... I understand..." with dissolve
    "Although somehow, I just know this isn't going to make her mad at me."
    show NozomiHypno sleep
    ks "Perfect. And one more thing. The moment you leave the house or I say \"Back to reality\", you will immediately lose every suggestion I've made to you tonight." with dissolve
    ks "You will recall everything that has happened and these suggestions will no longer have any effect on you. Okay, Nozomi?"
    show NozomiHypno sleeptalk
    n "Okay..." with dissolve
    show NozomiHypno sleep
    ks "That's great. Now, waking up in three." with dissolve
    ks "One, two... three."
    stop music fadeout 5.0
    scene bg blackscreen with dissolve
    "(( AUTHOR'S NOTE: Really sorry to say this, but I'm afraid this is where I have to leave things for now. ))"
    "(( Tune in next release where I hope to have more of this storyline written! ))"
    "{size=30}TO BE CONTINUED...{/size}"
    jump Credits

label Day5_Con_Kyou_Sayori:
    if hypno3 == "personality":
        scene bg street1 day with longdissolve
        "It's Friday, and I'm walking to school with trepidation once more."
        play music Eons fadein 5.0
        show Sayori alert_neutral_right at left, flip:
            xalign -0.3
            linear 1.1 xpos 0.05
        s "Kyou. I was hoping to catch you."
        show Sayori at left, flip:
            xalign -0.3 xpos 0.05
        "I turn and face the unfamiliar but welcome sight of Sayori approaching me on the way to school."
        ks smile "Sayori! How are you?"
        "She immediately frowns at my question."
        s uniform_folded alert_annoyed "I will report that I once again fell into a mindless and deep sleep, regardless of my intent to stay awake." with dissolve
        ks confused "Did you expect it to wear off?"
        s alert_sleep "I had hoped the effect would wane over time, yes. And it has been a few days now." with dissolve
        s alert_sleeptalk "But still, the effect of the sleep trigger on me is as potent as ever. I can only assume the \"[alt_name]\" trigger is the same." with dissolve
        s alert_concerned_right "Perhaps if you had given me more control over my own triggers I would be far less concerned by how entrenched they seem to be in my mind." with dissolve
        "Still, I can't help but notice that she's looking pretty well-rested AND is here on time. Did she turn in at a decent hour last night on purpose then?"
        ks sad "I'm sorry. Do you think I should try to deprogram you?"
        s uniform "... I may permit you to try. But first, let's see what Nozomi has to say." with dissolve
        ks neutral "Right."
        scene bg classroom day with blink
        play sound schoolbell
        "I walk into class with Sayori as we get the day started."
        with blink
        "Morning lessons feel tense. I've barely been able to concentrate before, but this is worse."
        "Obviously I'm excited about the prospect of Nozomi joining our experiments."
        "But would she really volunteer when she finds out I'm involved?"
        "I can see Sayori talking with her and that nasty tennis girl over lunch. Maybe she's talking to her about it right now?"
        "I don't dare get close enough to eavesdrop, so all I can do is eat lunch at my desk and play with my phone as I half-listen to the chatter of my classmates around me."
        "It's started to bother me, how I'm never part of that chatter."
        "I've hardly talked to anyone these past few years, until these days I've had with Sayori."
        "Setting aside our new shared interest, just having someone who'll spend their time with me, smile at me... hell, even argue with me. It's been nice."
        "... Jesus. Am I really this fucking lonely?"
        scene bg corridor eve with longblink
        "Finally the moment of truth arrives and I head to the study club at the agreed time."
        scene bg study room eve
        show Sayori alert_neutral at center, flip:
            xpos 0.25
        show Nozomi side frown_side at center
        with blink
        ks surprised "Nozomi?"
        "She's already here? But I got here as soon as I could and study club only just let out!"
        n frown "I'm sorry, Kyou, but we don't have much time. Sayori already explained everything to me." with dissolve
        n front2 frown "You're just going to hypnotize me and make sure I remember what happened, right? Let's get to it!" with dissolve
        scene cg study room eve
        show NozomiHypno standing stern
        with blink
        "... Sayori and I exchange a look. I'm glad she agreed, but she seems a little... eager?"
        ks smile "A-alright then, if you could make yourself comfortable and stare straight ahead at me? Great, and now..."
        show penlight at right with moveinright:
            ypos 0.346
        "I take out the penlight and hold it above Nozomi's head as I switch it on."
        ks "Keep your head where it is, but look up with your eyes at the light."
        show NozomiHypno lookup
        "I direct her to replicate as best as I can the first time I hypnotized Sayori." with dissolve
        ks "Very good. Now I want you to focus on the light, taking special note of how it feels as the light passes your eyes."
        hide penlight with moveoutright
        $ldirection = "right"; light_y = 0.29
        call cglightshow
        "As I finish my sentence, I steer the light beam over her determined eyes while Sayori looks on."
        call cglightshow
        ks "That's right, Nozomi. Just watching the light, taking a deep breath in, that's all you need to do."
        call cglightshow
        ks neutral "And breathe out... relax."
        call cglightshow
        ks "If you find that your eyelids are starting to strain, that your eyes are becoming tired, then that's okay, Nozomi."
        call cglightshow
        ks "Breathe in, and let yourself blink while you look, if you need to."
        call cglightshow
        show NozomiHypno drowsy
        stop music fadeout 15.0
        $ renpy.transition(longdissolve, layer="master")
        ks "That's it. That's all you need to do, just focus on the light as best as you can. And breathe out."
        call cglightshow
        ks "Very good, Nozomi. Taking in every feeling, letting it happen if you're becoming sleepy."
        call cglightshow
        ks "Just watch the light as long as you can. Breathe in."
        call cglightshow
        ks "But if your eyelids are still becoming heavier, and if you need to sleep and drop for me, that's okay. Breathe out."
        call cglightshow
        show NozomiHypno drooping sleep
        play music Flow
        $ renpy.transition(longdissolve, layer="master")
        ks "It's okay, Nozomi. Dropping deep now. Deep asleep."
        $persistent.study_room_nozomi_unlock = True
        scene StudyRoomHypno sayori1 s_neutral_right nozomi1 n_sleep with longblink
        "As Nozomi falls dormant, I quietly stand up from my chair and walk to her side as Sayori observes her in silence."
        show StudyRoomHypno s_neutral
        ks smile "{size=16}What's on your mind, Sayori?{/size}" with dissolve
        "I ask quietly, and Sayori takes the invitation to whisper back."
        show StudyRoomHypno s_surprised
        s alert_surprised_right "{size=16}Is that truly all it takes?{/size}" with dissolve
        "I simply smile at her. I mean, I guess it's not surprising that Nozomi would be just as hypnotizable as Sayori."
        "Not only does she clearly have a smart and creative mind of her own, we also know she's been hypnotized before."
        show StudyRoomHypno s_neutral
        s "{size=16}Well, I suppose there is a cadence to your voice that lends well to getting people to zone out. That is something of a skill you have.{/size}" with dissolve
        "... I can feel the smile fading from my face as I eyeball her."
        show StudyRoomHypno s_smirk
        s alert_smirk_right "{size=16}You should ask her how the light felt.{/size}" with dissolve
        "I was getting to that, Sayori. Geez."
        show StudyRoomHypno s_neutral_right
        ks "Nozomi, as you go deep for me, can you describe how the light in your eyes felt to you, in your own words?" with dissolve
        show StudyRoomHypno n_sleeptalk
        n sleeptalk "Yes..." with dissolve
        show StudyRoomHypno n_sleep
        "..." with dissolve
        show StudyRoomHypno s_neutral
        s uniform alert_neutral_right "..." with dissolve
        ks sigh "... Describe how the light felt, Nozomi."
        show StudyRoomHypno s_neutral_right n_sleeptalk
        n sleeptalk "Every time you passed the light across my eyes, it felt like my senses were all lighting up in turn." with dissolve
        n "It felt so... euphoric. I wanted to stare more, but when you suggested I was sleepy, I realized how sleepy I was getting."
        n "It just felt so nice to stare and... t-to listen..."
        show StudyRoomHypno s_stern n_sleep
        s "{size=16}That lines up with what little I remember, and I think this supports my thinking that the light is doing more than you intended.{/size}" with dissolve
        ks frown "{size=16}You really think so? How would it even do that?{/size}"
        show StudyRoomHypno s_quizzical
        s alert_annoyed "{size=16}She mentioned feeling euphoric. Perhaps the light is triggering the release of a large amount of dopamines and oxytocins in the brain?{/size}" with dissolve
        show StudyRoomHypno s_neutral_right
        s "{size=16}Such a thing may be stimulating the subject's motivation to remain focused on the pattern the light is emitting.{/size}" with dissolve
        s "{size=16}And such a chemical release might also shut down any resistance the subject has to the suggestions you are giving them, practically ensuring that they respond favourably.{/size}"
        "Sayori pauses for a moment as she appears to ruminate on what she just said, then continues."
        show StudyRoomHypno s_quizzical
        s alert_neutral "{size=16}This is pure speculation on my part, and somewhat of a... hollywood explanation? But that is more or less what I consider has happened to me, and is happening to Nozomi right now.{/size}" with dissolve
        show StudyRoomHypno s_stern
        s alert_annoyed_right "{size=16}So what I think, Kyou, is this penlight of yours is bypassing a person's ability to reason.{/size}" with dissolve
        show StudyRoomHypno s_stern_right
        s "{size=16}People subjected to it will allow themselves to drop into trance and have whole facets of their being altered regardless of their conscious will and desire.{/size}" with dissolve
        show StudyRoomHypno s_stern
        s alert_surprised_right "{size=16}You could say it is a highly effective brainwashing tool.{/size}" with dissolve
        "I exchange a look with Sayori as I feel my mouth hanging open."
        ks surprised "{size=16}A-Are you serious?{/size}"
        s "{size=16}Deadly serious. As I told you, I have been altered against my wishes and you need to take responsibility for that.{/size}"
        ks "{size=16}But it's just... it's just a penlight with a few minor alterations; how could it do that much?{/size}"
        show StudyRoomHypno s_thoughtful
        s alert_sleep "{size=16}It is like I have said, Kyou. You put in a modicum of effort, and the rewards are substantial.{/size}" with dissolve
        show StudyRoomHypno s_quizzical
        s "{size=16}I have no idea how you achieve these fleeting periods of hypercompetence.{/size}" with dissolve
        "I can hardly believe what I'm hearing, but I can't deny that Sayori's interpretation of things are at least making some sort of sense?"
        "If nothing else, I guess it's a little far-fetched to think Sayori would secretly want to be the exact person I made [alt_name] to be."
        ks sigh "{size=16}I'm sorry, Sayori. You have to believe me when I say I had no idea I was doing that to you.{/size}"
        show StudyRoomHypno s_smile
        "Sayori's expression softens as she whispers to me once more." with dissolve
        s alert_smile_right "{size=16}I believe you. And that is why I think I can trust you to do the right thing by the time this is over.{/size}"
        show StudyRoomHypno s_stern
        s alert_annoyed_right "{size=16}Now be good and bring Nozomi back out of trance in case you accidentally brainwash her too.{/size}" with dissolve
        ks frown "{size=16}Oh, right. Yeah, of course.{/size}"
        show StudyRoomHypno s_neutral_right
        with longblink
        ks smile "... and five, wide awake, Nozomi."
        show StudyRoomHypno n_sleepysmile
        stop music fadeout 5.0
        $ renpy.transition(longdissolve, layer="master")
        "Nozomi's eyelids flutter open, then as she starts to arch her back on the seat a smile spreads across her lips."
        show StudyRoomHypno n_blush_low
        n smile "Oh gosh, that felt wonderful." with dissolve
        play music Eons
        show StudyRoomHypno nozomi2 n_startled n_blush_high
        n side frown blush "I-I mean, did you get what you needed?" with dissolve
        show StudyRoomHypno s_smile_right
        s alert_smile "Yes, thank you, Nozomi. You confirmed a few things for us." with dissolve
        hide StudyRoomHypno
        show StudyRoomHypno sayori1 s_smile_right nozomi2 n_smile_left
        "Nozomi nods as she takes a breath and meets Sayori's gaze." with dissolve
        n "I'm happy to help, but would you two mind telling me what you found?"
        show penlight at right with moveinright:
            ypos 0.346
        show StudyRoomHypno s_neutral n_smile
        ks "Yeah, we found out just how effective this penlight is at hypnotizing people and getting them to follow suggestions." with dissolve
        hide penlight with moveoutright
        "As I finish explaining I notice Sayori shaking her head at me."
        show StudyRoomHypno n_neutral
        n front surprised noblush "\"Getting them to follow suggestions?\"" with dissolve
        "Nozomi adjusts her glasses as she ponders over what I said."
        n "Did you try that with me? Or did you just take me into a trance and then back out?"
        ks confused "We, uh... we put you in trance and back out."
        show StudyRoomHypno n_neutral_left
        n neutral "Hmm..." with dissolve
        "She opens her mouth to speak, then stops herself before immediately changing her mind again."
        show StudyRoomHypno n_neutral
        n concerned "Well... it sounds to me like you need a little more for your findings so, if it'll help, you could try taking me under again and trying a suggestion or two?" with dissolve
        show StudyRoomHypno s_smile_right n_neutral_left
        s alert_smile "Ah, really Nozomi, we learned everything we needed to. Thank you for your help." with dissolve
        n "I-if you're sure? I really don't mind doing this for you, Sayori."
        show StudyRoomHypno n_smile_left
        n "You've helped me so much before, so it'd be nice if I could do something for you." with dissolve
        s "I am sure. Besides, I need to head off for cram school shortly."
        show StudyRoomHypno n_neutral_left
        n "Ah... of course." with dissolve
        $persistent.study_room_hypno_nozomi_unlock = True
        scene bg study room eve
        show Nozomi front pout_left at center
        show Sayori alert_neutral_right at center, flip:
            xpos 0.25
        with blink
        "As we get up from our seats, Sayori takes me aside and whispers."
        s "{size=16}I would like to finish this tomorrow morning, at your home if that works for you?{/size}"
        ks neutral "{size=16}Uh yeah, sure. Tomorrow morning's fine.{/size}"
        hide Sayori with dissolve
        show Nozomi front smile
        "She nods firmly, then exchanges a wave goodbye to Nozomi as she leaves." with dissolve
        "As I put the penlight away, I notice that Nozomi doesn't seem to be in a hurry to leave, dragging her fingertips idly across the table."
        "Our eyes meet, and she starts to smile quietly."
        n front2 smile "So... I had no idea you were a hypnotist, Kyou." with dissolve
        "I let out a nervous chuckle."
        ks smile blush "Uh, y-yeah... I mean, I started learning about it a little while ago."
        n neutral "That's... that's interesting." with dissolve
        "She adds with a laugh:"
        n front laugh "Not to mention the fact that you roped Sayori into this, of all people~" with dissolve
        ks "Hah, yeah. Well, I mean, I offered to help her with her insomnia and she was willing to let me try, so here we are."
        n surprised "H-huh? Is that why she seems so full of energy these past few days?" with dissolve
        ks "I dunno if I'd call her full of energy, but... yeah, she's looking a little perkier, heh."
        "She nods in agreement."
        n smile "Could you tell me more about what you and Sayori were doing? I'm sorry, but I can't help but be curious about all this." with dissolve
        "I can feel the heat rising to my cheeks as she continues to chirp excitedly at me. I mean..."
        n chuckle "Whatever you've done together really seems to have helped her." with dissolve
        "Nozomi Akemi, class rep and the girl of my dreams, is actually interested in talking to me!"
        n smile "So would you mind telling me a little more? Please?" with dissolve
        ks "Oh, yeah, so I've been hypnotizing Sayori with this penlight, like I just did with you."
        ks "And yeah, I gave her a hypnotic suggestion to help her sleep at night, and it seems to have worked."
        ks "But she thinks what we've been doing also altered her in ways she didn't want?"
        "She falls silent for a while. I'm not sure how much she understood of that..."
        n front2 shocked "What? I find that a little hard to believe." with dissolve
        ks confused noblush "You do? What don't you believe about it?"
        n surprised "I mean, uh... about altering her in ways she didn't want?" with dissolve
        n frown "Not that, er... not that I know too much about hypnosis, but the idea that you can change people's minds against their will seems a little... fantastical don't you think?" with dissolve
        n neutral_left "I guess it could be possible with a sustained effort, but from what I gather you've not been doing this for very long?" with dissolve
        ks neutral "Y-yeah... only since this week."
        n sigh "Well... my offer still stands, if you want a second opinion on that." with dissolve
        ks surprised "What?!"
        n side sad_side "I know what Sayori said but it just... It definitely sounds to me like you need more data, and I don't have anywhere to be right now." with dissolve
        n smile "And I'm sure Sayori just didn't want to bother me, but it's really okay. I'll gladly volunteer to be hypnotized again." with dissolve
        n front smile "I know she doesn't easily accept help from other people, despite how generous she is about helping the rest of us." with dissolve
        n happy "So let me help her, Kyou~" with dissolve
        "I don't think we really need any more data despite what Nozomi thinks."
        "But she's actually taking an interest in me and talking to me!"
        "Besides, what's the harm in indulging her a little bit? I could just give her a little fun suggestion and she'll go on her way thinking she helped."
        "Not to mention she'll think better of me in the bargain."
        "I mean, I've learned from my mistakes with Sayori. I'll make sure to phrase things specifically so it wouldn't be permanent."
        "So what's the worst that could happen?"
        menu:
            "Hypnotize her again":
                $hypno_nozomi = True
                jump Day5_Con_Kyou_Sayori_Hypno_Nozomi
            "Don't hypnotize her":
                $hypno_nozomi = False
                "I can't believe I'm having to say this, but..."
                ks smile blush "Actually, Nozomi, we really are good for data and I really shouldn't hypnotize you anymore. But, uh..."
                ks "Thanks for helping us out."
                n front2 surprised "W-what do you mean you shouldn't? I don't understand." with dissolve
                "Sayori did ask me not to tell her about this stuff, and I know I've already said way too much."
                n concerned "I already explained about Sayori. She'll appreciate us doing this for her, I promise." with dissolve
                "She'd probably kill me if she finds out I actually went ahead and hypnotized Nozomi again, especially with how dangerous she thinks my penlight is."
                n frown "A-and besides... you WANT to hypnotize me, don't you, Kyou?" with dissolve
                ks surprised noblush "W-what?!"
                n irritated "I mean, that's what was so important the other day wasn't it? When you wanted to speak to me? Don't think I forgot about that." with dissolve
                ks "Uh, well..."
                n side frown_side "You wanted to ask me, and you had your chance while we were cleaning the classroom together." with dissolve
                n frown "But you chickened out at the last minute and you went and asked Sayori instead!" with dissolve
                n front2 frown "You even told me you've only been doing this together since this week. It matches up perfectly." with dissolve
                show Nozomi sigh
                "As I stumble to find the words to refute her, she takes a breath and looks down at the table as she tents her fingers." with dissolve
                n concerned "If... if you're worried she might get mad about this, don't be." with dissolve
                n sleep "I'll be sure to tell her it was my idea and that I put you up to this. I'll take full responsibility." with dissolve
                "Shit. Am I really gonna say no to this?"
                show Nozomi concerned
                "Seeing my discomforted silence, Nozomi continues." with dissolve
                n "And... I know we've not really talked, Kyou. Maybe that's my fault. Maybe I should have reached out to you more when I had the chance."
                n smile "But this could be an opportunity for us to get to know each other better, don't you think?" with dissolve
                menu:
                    "Hypnotize her again":
                        $hypno_nozomi = True
                        jump Day5_Con_Kyou_Sayori_Hypno_Nozomi
                    "Don't hypnotize her":
                        ks frown "Go home, Nozomi."
                        n surprised "What?!" with dissolve
                        "I surprise myself with my directness, but it seems like she's not going to listen otherwise."
                        ks "I mean it. We said we had all we needed and thanked you for your help. So don't ask me again."
                        n shocked "But... w-wait!" with dissolve
                        stop music fadeout 5.0
                        scene bg k bedroom eve with blink
                        "After that I quickly headed back home, leaving a stunned Nozomi in my wake."
                        "I feel like so much shit, but I think I did the right thing."
                        scene bg blackscreen with longdissolve
                        pause 2.0
                        jump Day6_Con_Kyou_Sayori
    elif hypno3 == "doll":
        scene bg street1 day with blink
        "So it's Friday once again, and I'm walking to school with a yawn in my throat."
        play music Bright_Opening fadein 5.0
        s "Kyou. I was hoping to catch you."
        scene SayoriWalk kyou_surprised sayori_smile with blink
        "I blink my tired eyes as a figure approaches me from the side."
        "... Is that who I think it is?"
        show SayoriWalk sayori_concerned
        s alert_surprised_right "Did something happen? You look terrible." with dissolve
        show SayoriWalk kyou_sigh
        k "Sayori? Huh, yeah I turned in late last night. Whatever." with dissolve
        show SayoriWalk sayori_neutral
        s uniform_folded alert_concerned_right "Hmm. It would seem late nights make you grumpy." with dissolve
        show SayoriWalk kyou_neutral sayori_smirk
        s alert_smirk_right "Perhaps you should turn in a little earlier." with dissolve
        show SayoriWalk kyou_annoyed
        k "Man, you're one to talk." with dissolve
        "But then, as I look at her face I realize..."
        show SayoriWalk sayori_happy
        s uniform_handup "So I am. Anyway, you should stop by my clubroom this afternoon." with dissolve
        "She's looking really healthy today."
        show SayoriWalk kyou_neutral
        k "I should, huh?" with dissolve
        show SayoriWalk sayori_neutral
        s alert_neutral "Yes. My time is short today, but I am anxious to continue our discussions." with dissolve
        show SayoriWalk sayori_smile
        s uniform alert_neutral_right "So perhaps I will see you there?" with dissolve
        $persistent.sayori_walk_unlock = True
        scene bg classroom day with blink
        "And that's how my day started."
        "I might not know what's going on with Sayori today, but after what she said to me this morning I gotta feel optimistic."
        "As for the rest of the day, I can hold on to that feeling as I try to focus on my classwork."
        "I kinda want to take my attitude from last night into today. Figure out what I'm going to do when I graduate; get some kind of plan going."
        stop music fadeout 5.0
        scene bg classroom eve with blink
        play sound schoolbell
        "... What's Sayori's plan anyway?"
        "As I make it through to the end of another week I realize that I have no idea what HER graduation plan is, let alone my own."
        "I kinda want to ask her..."
        scene bg study room eve
        play music Downtown
        show Sayori uniform_folded alert_surprised_right
        with blink
        s "My \"plan\"?"
        ks neutral "Yeah. It's just something I was thinking about today, that's all."
        s alert_annoyed "Honestly I had thought it somewhat common knowledge, but alright." with dissolve
        s alert_neutral_right "I am hoping to get into a medical school post-graduation." with dissolve
        "She then gestures vaguely towards the table of the study club room, recently vacated by the other members."
        s uniform_handup alert_sleeptalk "That is what all of this is for." with dissolve
        ks sigh "You really need to bust your ass this much for med school?"
        s alert_neutral_right "Entering the medical track is as competitive as it gets, Kyou." with dissolve
        s alert_annoyed "For women especially..." with dissolve
        "I don't really know what to say to that, and Sayori doesn't let the moment hang for very long."
        s alert_neutral "But if you don't mind, I would like to move away from this." with dissolve
        s uniform alert_concerned_right "I was actually looking forward to having a little distraction from such, to tell the truth." with dissolve
        ks surprised "Oh, uh... Yeah, sure."
        "Sayori nods as she gets to it."
        s alert_neutral_right "So last night, I decided not to fight my subconscious this time." with dissolve
        s alert_sleep "And for that, I immediately entered into a long and restful slumber once again." with dissolve
        s uniform_folded alert_sleeptalk_concerned "Had I not set my alarm, I would surely have slept through first period for a second time." with dissolve
        ks smile "Yeah? That's pretty incredible."
        s alert_neutral_right "That is one way of looking at it." with dissolve
        s alert_neutral "Still, turning in as early as I did meant I could not accomplish as much as I wanted over the evening." with dissolve
        s uniform alert_neutral "It certainly meant I couldn't do any further learning regarding this phenomenon." with dissolve
        s alert_concerned "... But I must admit that I am feeling much better for the rest." with dissolve
        s uniform_handup alert_concerned_right "To be able to lay my every waking concern at the foot of my bed and simply... forget. Just for the night." with dissolve
        s alert_sleeptalk "There is something rather liberating about that." with dissolve
        ks smile "So do you think we can do another session, Sayori?"
        s alert_concerned_right blush "H-Hm?" with dissolve
        "I mean, to me it sure sounds like she wants to."
        "And the mere mention of it now seems to excite her..."
        show penlight at right with moveinright:
            ypos 0.346
        show Sayori alert_surprised_right
        ks "We could do something right now if we're quick." with dissolve
        "Sayori's eyes drift towards the penlight as I pull it from my pocket in front of her."
        s uniform_folded alert_annoyed_right "Do... d-do you always keep that toy with you now?" with dissolve
        "She frowned at the sight of it, but I can see the longing in her eyes..."
        "Then suddenly she seems to blink in recognition."
        s alert_surprised_right noblush "Ah, that reminds me. I had been meaning to ask about this." with dissolve
        ks neutral "Hm?"
        s alert_neutral_right "Your penlight. You said you constructed it yourself, did you not?" with dissolve
        hide penlight at right with moveoutright
        ks "Uh, yeah."
        "I look down to the penlight as I turn it over in my hand."
        ks "I mean, it's a cheap penlight I bought online, but I took it apart to rejig how it emits the light as well as add a subtle patterning to it."
        "Sayori nods thoughtfully."
        s uniform_handup alert_concerned_right "And you believe this modification speeds the hypnotic process somehow? As opposed to using an unaltered light as a focus?" with dissolve
        ks smile "Yeah, that's right. It's supposed to catch your attention with that patterning I put in."
        ks "Like, I tried to design it so you know it's there when the light shines past your eyes, but you can't make out what it is."
        ks "So along with my suggestions you're compelled to keep looking."
        s alert_neutral "Per your description it does seem to be working as designed." with dissolve
        s alert_sleep "I have been on the receiving end of that device of yours twice now, and I am still no clearer as to what that pattern could be." with dissolve
        s uniform alert_neutral_right "Still, I am curious to see how effective your modifications are compared to unaltered lights. Or a solid object like the one Satoshi used." with dissolve
        "As she ponders the thought, Sayori takes a glance at the clock on the wall..."
        s alert_sleep "But much as it pains me to say, the curiosity can wait. I need to be going." with dissolve
        "Fuck, already? I knew I didn't have a lot of time but this is ridiculous."
        ks frown "Wait, Sayori!"
        s alert_annoyed "I apologize for the brevity, but I did not enjoy having to dash to cram school the last time we met in this room." with dissolve
        s alert_irritated "So please stand aside so I can get there in good time." with dissolve
        "This is so frustrating I can't stand it."
        ks "But when's a good time for us? I gotta sign up to perform at the culture fest soon, but I'm not ready."
        ks "I need an answer, Sayori."
        s alert_rolleyes "You are rather overstating the stakes involved. And understating the value of my time." with dissolve
        ks angry "Please!"
        s uniform_folded alert_angry_right  "I will NOT allow you to force a commitment out of me, Kyou." with dissolve
        s "Now for the last time, {w=0.5}{nw}"
        extend "STAND ASIDE!" with vpunch
        "... That was quite a forceful shout coming out of her. I think I heard a startled voice outside, too."
        "She's got a lot of energy today that's for sure."
        ks sigh "F-fine..."
        show Sayori alert_irritated
        "Sayori snorts as she passes me to get to the door." with dissolve
        s alert_irritated "So glad I made myself clear. Now I will leave you to sulk..."
        play sound dooropen
        stop music fadeout 5.0
        hide Sayori with dissolve
        pause 1.0
        play sound doorclose
        "And I can only watch her leave..."
        scene bg k bedroom eve with blink
        "With nothing better to do, I head straight home."
        play music Past_Sadness
        "I guess I am a little too set on the culture fest stuff, now that she mentions it."
        "I mean, do I seriously want to put on a show for everyone? Is that really me?"
        "I'm sure they're all set on me being the class creep anyway. No one's going to change their minds about me just because they saw me do a trick or two."
        "Hell, it might just make them double down about me. We're talking about me doing hypnosis after all; they're sure to take it the wrong way."
        "Maybe I should just forget about the whole thing..."
        stop music fadeout 5.0
        jump Day7_Con_Kyou_Sayori_Doll

label Day5_Con_Kyou_Sayori_Hypno_Nozomi:
    show penlight at right with moveinright:
        ypos 0.346
    show Nozomi front2 laugh
    with dissolve
    "I smile as I pull the penlight back out of my pocket. Its reappearance is enough to make Nozomi let out a little squeal of delight."
    ks smile "Alright, I guess there's something we can do that might help."
    n chuckle "It'll definitely help~ A simple in and out of trance just isn't going to cut it." with dissolve
    hide penlight at right with moveoutright
    "Man, the way her face lit up as soon as I agreed to hypnotize her again... Is this really because she wants to help Sayori?"
    n smile "For Sayori's sake, I think we owe it to her to be a little more thorough." with dissolve
    "Well, whatever. I'm just happy if I can make Nozomi smile at me like this."
    n side smile "So I'm going to make myself comfortable in the chair again and we'll start whenever you're ready." with dissolve
    "This is what I've wanted ever since I started learning about hypnosis. It's why I worked on this penlight in the first place."
    scene cg study room eve
    show NozomiHypno standing smile
    with blink
    "So, yeah... Yeah, let's do this."
    ks smile "Okay so I'll try hypnotizing you just like before, only this time I'll give you a simple post-hypnotic suggestion to follow and we'll see how that effects you."
    show NozomiHypno smile_closed
    n "Sounds good to me!" with dissolve
    show NozomiHypno smile
    n "What sort of suggestion, though?" with dissolve
    "Well that's a good question. It's not like I've planned this at all."
    ks neutral "Hmm... well..."
    "I need to think fast while we're still in the moment."
    ks confused "Maybe... we could try to alter your senses for a while?"
    # ks confused "I... don't suppose you're hungry?"
    # n "Uh, not really? Why?"
    show NozomiHypno confused
    "Nozomi tilts her head slightly as she looks thoughtful." with dissolve
    n "Oh? Like getting me to hallucinate something or...?"
    "I simply smile at her as I follow through with the hasty idea taking form in my head."
    ks smile "Something like that. Want to see if we can do it?"
    show NozomiHypno smile
    "She smiles back as she nods, seemingly eager for the challenge." with dissolve
    n "Of course! And I'm sure our findings will be a big help for Sayori no matter what."
    "Great. This is great. So I'll do this, but not for Sayori."
    ks "Perfect. So let's have your attention here now, back with the light."
    show NozomiHypno lookup
    "This is all for you, Nozomi." with dissolve
    call cglightshow
    $renpy.music.set_volume(1.0)
    ks "That's right, just sit back, relax, and watch the light with your eyes."
    "I'll show you just how fun hypnosis can be."
    call cglightshow
    $renpy.music.set_volume(0.9)
    ks neutral "Taking a deep breath now as the light hits you. Feel that breath in your lungs..."
    "I'll give you a safe and unforgettable experience."
    call cglightshow
    $renpy.music.set_volume(0.8)
    ks "... and let it all out now, slowly, allowing a wave of deep relaxation to wash over you."
    "Sayori might get mad with me when she finds out but come on, I've learned so much after my time with her."
    call cglightshow
    $renpy.music.set_volume(0.7)
    ks "You can allow yourself to relax, just as you can allow everything else to fade far into the background."
    "I won't make the same mistake this time."
    call cglightshow
    $renpy.music.set_volume(0.6)
    ks "Leaving just the sight of the light and the patterns it leaves in your eyes..."
    "I... I KNOW what I'm doing here."
    call cglightshow
    $renpy.music.set_volume(0.5)
    ks "Leaving only the sound of my voice... as you take another breath now, Nozomi."
    call cglightshow
    show NozomiHypno drowsy
    $ renpy.transition(longdissolve, layer="master")
    $renpy.music.set_volume(0.4)
    ks "Breathing in... eyes heavy, thoughts fading..."
    call cglightshow
    $renpy.music.set_volume(0.3)
    ks "Breathing out... eyes closing as you drop into a deep..."
    call cglightshow
    stop music fadeout 5.0
    show NozomiHypno drooping sleepy
    $ renpy.transition(dissolve, layer="master")
    ks "Sleep."
    show NozomiHypno sleep
    n "..." with dissolve
    stop music
    "Nozomi's shoulders sag and her head rolls forward as she seems to drop into a deep trance just like before."
    $renpy.music.set_volume(1.0)
    play music Flow fadein 5.0
    "It seems she really is every bit as good as Sayori was at being hypnotized."
    ks "That's right, Nozomi. Dropping deep now into a comforting state of hypnotic trance."
    "Because she really wanted to be hypnotized? Or is this really all down to the penlight like Sayori said?"
    ks "And while you're in this nice comfortable state, I'd like you to think about... lemons."
    "Well, let's not worry about that for now."
    show NozomiHypno sleeptalk
    n "... Lemons?" with dissolve
    "Right now I just want to focus on having a little fun with the girl I admire so much..."
    show NozomiHypno sleep
    ks "That's right. I'd like you to imagine what it's like to bite into a whole lemon. To tear your teeth into its yellow flesh and feel the bitter juice squirt into your mouth." with dissolve
    n "M... mmmmn..."
    "I grin as Nozomi's cute features start to contort from the mental image I'm making for her."
    ks smile "Can you taste the lemon, Nozomi?"
    show NozomiHypno sleeptalk
    n "Y...y-yeah..." with dissolve
    ks "Can you feel the bitter citrus taste in your mouth as it seems to set your teeth on edge?"
    n "Ugh... yes..."
    ks "Feel the overpowering scent of lemon as it assaults your taste buds and works its way deep into your nostrils?"
    "Now I have to stifle a laugh as the poor girl nearly gags at the sensation."
    n "Urrrrrghhh... y-yesh..."
    "Maybe I went a little overboard, but I kinda need it to be for what I'm about to suggest to her next."
    show NozomiHypno sleep
    ks "That's good. Now, when you awaken from this trance you will find that anything you eat will feel exactly the same as it does to bite into a whole lemon, just as you are now." with dissolve
    ks "The way it tastes, the way it smells, the way it feels in your mouth..."
    ks "No matter what it looks like, anything you eat will give you the exact same experience as if you were eating this lemon. Understand?"
    show NozomiHypno sleeptalk
    n "Yes... I understand..." with dissolve
    show NozomiHypno sleep
    ks "Wonderful. This state of mind will continue only until you hear me snap my fingers." with dissolve
    ks "The moment you hear me snap my fingers, all your senses of taste, smell and feeling will return to their natural states."
    ks "You will be completely back to normal with no lasting effects from this hypnotic experience. Is that clear, Nozomi?"
    show NozomiHypno sleeptalk
    n "Yes..." with dissolve
    show NozomiHypno sleep
    ks "Perfect. Now waking up on a count of three, Nozomi. Feeling wide awake and fully refreshed in one, two..." with dissolve
    stop music fadeout 5.0
    show NozomiHypno sleepy
    $ renpy.transition(longdissolve, layer="master")
    ks "Three..."
    show NozomiHypno standing drowsy
    "Nozomi takes a deep breath as she gently rouses herself." with dissolve
    queue music Piano_Mood
    show NozomiHypno smile_closed
    "And there's that sleepy, happy smile again, just like when she came out of trance last time." with dissolve
    ks "There we go, wide awake. How are you feeling?"
    "Only now I get to enjoy the view without Sayori hovering over us."
    show NozomiHypno smile
    # "She starts to smile pleasantly as shrugs her shoulders and sits upright on the chair." with dissolve
    # show NozomiHypno smile_closed
    n "Mmn, really good!" with dissolve
    show NozomiHypno lookup
    n "I mean, gosh, I can't believe how... um, immersive that was?" with dissolve
    ks "Yeah?"
    "And without her, it seems Nozomi feels more free to express how she really feels about all this."
    show NozomiHypno laugh
    n "Yeah! The first time you did this I was a bit tense, but the moment that light hit my eyes it was just so easy to let go." with dissolve
    "Nozomi really does seem to be into this hypnosis stuff. Just like I knew she'd be."
    show NozomiHypno surprised
    n "And this second time? I... w-well, I can barely remember a thing about it. I saw the light and then it's like I was suddenly spirited off to a far-away place." with dissolve
    "The way her eyes just seem to light up all on their own as she goes on about her experience..."
    n "Just, like... wow. I've been hypnotized a few times before in my life but this was something else. It's incredible!"
    show NozomiHypno smile blush
    n "Maybe even... Maybe this is the first time I've actually, truly been hypnotized." with dissolve
    "It fills my heart to see her like this; knowing I'm the one who made it possible."
    # n "Mmm, that felt so good. I could really feel myself going under, you know?" with dissolve
    ks smile "That's great! So, do you want to see if what we did worked on you?"
    show NozomiHypno laugh
    n "But of course~" with dissolve
    "And god, she's so beautiful when she smiles at me."
    ks blush "A-alright, so can you come over here please?"
    scene bg study room eve
    show Nozomi front2 smile at center:
        ypos 1.1
        linear 2.0 ypos 1.0
    with blink
    play sound clothes
    "As I beckon her, Nozomi giddily rises from her seat and walks around the table to join me as I reach into my school bag."
    show Nozomi:
        ypos 1.0
    ks smile "I don't suppose you remember what I told you in trance just now?"
    n side sad_side "Oh, um..." with dissolve
    "She frowns slightly in thought, and as I take out the thing I was looking for she seems to be running her tongue over her lips."
    ks "Well it's okay if you don't. This is for you."
    show Nozomi front2 surprised
    "I hand it to her, and she blinks her eyes slowly in recognition as she looks to what I just handed her." with dissolve
    n "A candy bar?"
    ks "Hehe, yeah. I meant to eat it at lunch, but I wasn't feeling it. Besides, I think it's better if you have it."
    show Nozomi happy
    "Nozomi lets out an amused giggle as she no doubt realizes where I'm going with this." with dissolve
    n smirk "You're going to spoil my appetite, doing this so close to dinner." with dissolve
    n chuckle "But if it's for Sayori, I think I can swing that~" with dissolve
    scene bg blackscreen with dissolve
    "She gingerly pulls the wrapper apart, before tentatively taking a bite of the chocolate within as I watch her face..."
    stop music fadeout 2.0
    scene NozomiChocolate arm1 choc1 contemplating
    n pout_left "Mmth... th-this is..." with dissolve
    show NozomiChocolate disgusted
    n scared "Urggh!" with vpunch
    play music Black_Room
    "Nozomi barely rolled it around her tongue before her face suddenly contorted into the most beautifully-conflicted grimace."
    show NozomiChocolate chewing_disgusted
    # "It barely touches Nozomi's tongue before her face contorts and she forcefully slaps a hand over her mouth while making the most awesomely conflicted face."
    n irritated "Mmrn... t-that's, um..." with dissolve
    ks happy "Hahahaha! How's it taste, Nozomi?"
    "Her head quivers left and right in revulsion as she puts a hand to her lips, as if fighting the urge to spit the candy right back out of her mouth."
    # "Her head quivers left and right in revulsion while she chews furiously through the piece of candy she's keeping in her mouth despite acting like it's burning her."
    show NozomiChocolate confused
    n side rolleyes "Uggh, I don't know what I was expecting but it... tastes like I'm eating a raw lemon? L-like, rind and all?" with dissolve
    show NozomiChocolate chewing_disgusted
    n irritated "Oh my god it's so bitter and s-so..." with dissolve
    show NozomiChocolate confused_down
    # n rolleyes "It's like... I know it's chocolate so why am I tasting lemon?!" with dissolve
    n surprised "... juicy?" with dissolve
    ks confused "And you're still going to eat it?"
    # "She pulls her hand away from her mouth as she stares bewilderedly at the candy bar wrapper, as if trying to make sense of the fact this chocolate takes like bitter fruit."
    # "She pulls her hand away from her mouth as she seemingly fights the urge to spit the "
    show NozomiChocolate chewing_disgusted
    "She swallows defiantly as a shiver runs down her body while the chocolate seems to reluctantly roll down her throat." with dissolve
    n "Mmnngh... aaah."
    "I can only stare at the sight of her struggling to get that down, fascinated."
    ks "Man, I can't believe how well this is working on you. So it really didn't taste like anything you'd expect?"
    show NozomiChocolate arm2 confused_down
    "Nozomi stares incredulously at the candy bar wrapper as she slowly nods her head." with dissolve
    n "Yeah. The taste, the texture, everything about it."
    show NozomiChocolate confused
    n sad "I know what I see, but it doesn't seem to matter at all. It just feels so real to me that this is somehow actually..." with dissolve
    show NozomiChocolate confused_down
    n sad_side "... lemon?" with dissolve
    # ks smirk "Man, I've never seen anyone hate chocolate as much as you do, Nozomi."
    show NozomiChocolate arm1 determined
    "She shakes her head, then takes a sharp breath through her nose as she holds the candy bar up to her face, like she's staring down a fierce rival or something." with dissolve
    n "No, this is a chocolate bar. It is sweet and delicious, it's nothing like a fruit at all!"
    "She then brings it to her lips as she steels herself for another bite..."
    show NozomiChocolate choc2 chewing_disgusted
    n irritated "It's... mmpth... c-chocolate..." with dissolve
    show NozomiChocolate disgusted
    n front2 pain "G-gggck, it's sho grossth!" with dissolve
    "As I snicker to myself, I think to raise a hand in front of Nozomi so I can put an end to her adorably self-inflicted misery."
    ks smirk "Hey, Nozomi? Look at me..."
    show NozomiChocolate confused
    n frown "H-hmm?" with dissolve
    stop music fadeout 5.0
    show Mindtrick awake fingersnap at center:
        ypos 0.6
    with dissolve
    play sound fingersnap
    show Mindtrick entranced
    show NozomiChocolate blank
    with dissolve
    pause 1.0
    hide Mindtrick
    with dissolve
    "There's no way I'm going to let Nozomi out of here thinking her senses are permanently altered, that's for sure."
    show NozomiChocolate confused
    ks smile "How's it taste now?" with dissolve
    show NozomiChocolate chewing
    n sleep "Mmn..." with dissolve
    "Her eyes close as I watch her roll the chocolate around in her mouth once more."
    play music Inspiration
    show NozomiChocolate happy blush
    "And then..." with dissolve
    show NozomiChocolate arm2
    n side happy "MMMMMM!" with dissolve
    ks smile "Is that better?"
    show NozomiChocolate laugh
    n laugh "The... oh my gosh, the subtle sweetness of the chocolate!" with dissolve
    show NozomiChocolate grin
    n front2 laugh "The comforting texture of the cookie base!" with dissolve
    n "The... the crunchyness of the rice puffs!"
    "Nozomi giggles delightfully as she holds a hand to her cheek and pops what remains of the little candy bar into her mouth while she devours it before my eyes and..."
    show NozomiChocolate laugh
    n laugh "Ahhh, it's all there, hahaha!" with dissolve
    "And man, I have never seen a girl get this excited about eating anything. It's like she's discovered sweets for the first time in her entire life."
    ks smile "Heh, s-so er, I guess we can call this a success, huh?"
    show NozomiChocolate happy
    "To that, Nozomi gives me an enthusiastic nod." with dissolve
    n "Mhmhmhmh~ Oh gosh, Kyou, I've never felt anything like that before."
    show NozomiChocolate confused
    n shocked noblush "I didn't think that kind of deep mental conditioning was even possible!" with dissolve
    ks neutral "Yeah. Sayori pretty much reacted the same way; she couldn't believe how much my hypnosis affected her."
    $persistent.nozomi_chocolate_unlock = True
    scene bg study room eve
    show Nozomi side neutral_side at center
    with blink
    "Nozomi, coming down from her sugar high or... her hypnosis high? Nods thoughtfully once more."
    n "Yes. Whatever it is you're doing with your technique, with that light you have, it's very powerful."
    n neutral "I certainly see why Sayori might be worried you're altering her way of thinking in unwanted ways if it felt as fantastic as that." with dissolve
    ks smile "Hehe, i-it felt that good, huh?"
    n sad_side blush "U-uh, well I mean..." with dissolve
    n happy "... Eheh yes, it did feel good." with dissolve
    n smile "I think hypnosis is *supposed* to feel good? And you did it really well, Kyou. You must have a real talent for it." with dissolve
    n front2 sleeptalk "But um... coming back to Sayori, I think we now have definitive proof that what you're doing is highly effective. You and that light you have there." with dissolve
    "I nod. Not that we needed any more proof; I'm just grinning all over that I managed to show Nozomi a good time."
    n neutral_left noblush "I don't really know what that's supposed to mean though, other than the fact you're good at this..." with dissolve
    #Around here would be a good time for Nozomi to propose repeat sessions, prompting Kyou to exchange contact information?
    "Nozomi purses her lips in thought while her eyes wander, before she notices the clock up on the study club wall."
    n smile "Anyway, I should get going. Don't want to be late for dinner." with dissolve
    ks smile "Oh... s-sure, I'll clean up in here and close up."
    n happy "Okay. Have a good weekend, Kyou~" with dissolve
    hide Nozomi
    "As I go to grab my things, I'm still buzzing with how well that went." with dissolve
    n "By the way, Kyou, I was just wondering..."
    "I mean, she's actually talking to me now, but more than that..."
    # n side smile noblush "I understand why Sayori might be worried about it, but it's not like you're trying to do any unwanted things with people, right?" with dissolve
    # ks smile "I... y-yeah, that's right."

    # n "Well, now we have definitive proof that what you're doing is highly effective. You and that light you have there."
    show Nozomi front neutral_left at center
    n "Do you think we could..." with dissolve
    n chuckle "... do this again sometime?" with dissolve
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    pause 1.0
    "This could be the start of something beautiful between us..."
    pause 2.0
    jump Day6_Con_Kyou_Sayori


label Day5_Con_Kyou_Sayori_Alter:
    scene bg street1 day with longdissolve
    "It's Friday, and I'm walking to school with a spring in my step."
    play music Inspiration fadein 5.0
    show Sayori alert_happy at left, flip:
        xalign -0.3
        linear 1.1 xpos 0.05
    s "Kyou! There you are!"
    show Sayori at left, flip:
        xalign -0.3 xpos 0.05
    "I turn and face the unfamiliar but oh so welcome sight of Sayori approaching me on the way to school."
    show Sayori uniform_folded blush
    "And then I feel the even less familiar sensation of Sayori hugging me fully, pulling me to a halt." with dissolve
    ks smile blush "S-Sayori. Aren't you worried we'll be seen?"
    "It's almost instinctive that I think she'd be ashamed of so openly associating with me, after being looked down upon for so long."
    show Sayori alert_annoyed noblush
    "And as she releases me, Sayori glances sideways with a frown." with dissolve
    s "I am not one to care for school banter."
    s alert_smile_right "If I cared for such things, it would only bring me down." with dissolve
    show Sayori alert_laugh
    "Just then, Sayori interlocks her arm with mine and practically drags me along the road as she tries to skip the rest of the way to school." with dissolve
    scene bg ext school day
    show Sayori uniform_folded alert_laugh blush at center, flip:
        xpos 0.25
    with blink
    "That... definitely gets us some looks as we pass the gates."
    show Nozomi side surprised_side at center:
        xpos 1.2
        linear 1.0 xpos 0.75
    n "S-Sayori?"
    show Nozomi at center:
        xpos 0.75
    s "Ah, Nozomi! Good morning~"
    show Nozomi surprised
    "Her raised hand apparently frozen in mid wave, Nozomi's eyes dart between her friend and... and me, still joined at the arm as we are." with dissolve
    s alert_smile noblush "Are we not having the most wonderful weather today?" with dissolve
    n sad_side "We are, but... I..." with dissolve
    s uniform_handup alert_laugh "Ahaha, you are not usually this shy, Nozomi. Tell us what is on your mind." with dissolve
    ks smile blush "Ahh, i-it's okay, Sayori. We should get inside anyway, class is about to start."
    n sad "That's... true, yes." with dissolve
    show Sayori uniform alert_happy
    stop music fadeout 5.0
    "If Sayori is put off by Nozomi's reaction to our coupling, she doesn't show it as we walk into school together in uneasy silence." with dissolve
    scene bg classroom day with blink
    play sound schoolbell
    "Sayori detaches from me to take her seat as class begins for another day."
    "Our homeroom teacher needs a little time to settle us down, as gossip starts to fly."
    "The idea of someone like Sayori getting together with anyone seems to have sparked some imaginations."
    "But as far as I can tell, Sayori herself seems completely unconcerned as lessons start."
    with blink
    play music Eons
    "By the time lunch period rolls around, I'm feeling pretty restless."
    "That Sayori's giving us a chance is fantastic, but the attention I'm getting now..."
    "It already makes me want to go back to being ignored again."
    "I guess that's just something I'm used to."
    show Sayori alert_smile_right at center
    with dissolve
    "In any case, my attention turns to Sayori, who has already walked over to my desk."
    s alert_laugh "Kyou! Rooftop club is in session, and participation is mandatory~" with dissolve
    show Hiroko neutral_side uniform_arm at center:
        xpos 0.75
    show Nozomi side frown_side at center, flip:
        xpos 0.25
    h frown_side "Ugh, really?" with dissolve
    "... Followed shortly by her friends."
    "It's pretty unusual for Sayori to be leading them, though."
    ks sigh "A-ah, it's okay Sayori. I know that's a girl's thing... or whatever."
    "I mean, I can hardly ignore the vibes her friends are giving me. I really don't want this kind of attention."
    show Nozomi neutral_side
    s uniform_folded "Now that is just silly talk and you know it." with dissolve
    h uniform_headhold2 "C'mon, let's just go." with dissolve
    n smile "We're... we're going up now, Kyou, but you're welcome to join us if you like." with dissolve
    h irritated "You're too nice for your own good, you know that?" with dissolve
    "But I guess I don't have much of a choice."
    scene cg rooftop day
    show RoofHiroko leanback frown
    show RoofNozomi handsdown smile_left
    show RoofSayori leanforward alert_smile
    with blink
    "So that's how I find myself lunching on the roof with Sayori's group."
    show RoofNozomi happy
    n happy "So... Sayori and Kyou." with dissolve
    show RoofSayori alert_laugh
    s alert_laugh "Sayori and Kyou~" with dissolve
    h "Sayori and... {w=0.5}{nw}"
    show RoofHiroko irritated
    $ renpy.transition(dissolve, layer="master")
    extend irritated "fuck, I ain't saying it."
    show RoofNozomi smile_left
    n "What's the story behind that, you two? Not to be rude, but this kinda came out of nowhere." with dissolve
    "After seeming weirded out this morning, I'm glad Nozomi is trying to keep an open mind about us."
    show RoofSayori leanback alert_smile
    show RoofHiroko neutral_left
    s uniform_folded alert_smile "I am so glad you asked. And I have to admit, it has been a whirlwind for me these past few days." with dissolve
    show RoofHiroko handcheek frown_left
    "Hiroko lets out a loud sigh and, it might be my imagination, but I think she just started to lean towards Sayori a little." with dissolve
    h "Uh-huh."
    s uniform_handup "Kyou dropped into my study club on Monday, and we got to talking."
    show RoofSayori leanforward alert_smile
    s alert_smile_right "Everything started to fall into place between us since then." with dissolve
    show RoofSayori alert_awe
    s alert_smile "He opened up to me about his interest in hypnotism, and I sought to indulge him. He actually has quite the talent for it." with dissolve
    show RoofNozomi curious_left
    show RoofHiroko leanback surprised_left
    "I can feel the anxiety pushing against my chest as Sayori spills everything, but I feel if I tried to stop her it'd only make things worse." with dissolve
    n "Hypnotism?"
    show RoofSayori leanback alert_smile
    s uniform alert_smile "Do you remember Satoshi's show at the culture festival last year? Kyou is planning to follow that up with a show of his own." with dissolve
    show RoofSayori alert_happy
    s alert_smile_right "I found myself assisting him, one thing has led to another and... well..." with dissolve
    show RoofSayori leanforward alert_smile blush
    s alert_happy blush "My heart seems to know what it wants~ I confessed to him last night." with dissolve
    show RoofHiroko handcheek shocked_left
    h shocked_side "Holy shit, really?" with dissolve
    show RoofSayori leanback alert_happy
    s "Really." with dissolve
    h uniform_armup "REALLY?" with vpunch
    show RoofSayori alert_grin
    s uniform_folded noblush alert_laugh "Really! We're dating now." with dissolve
    hide Nozomi
    show RoofNozomi curious
    n front surprised "... Hypnotism?" with dissolve
    show RoofHiroko neutral
    h uniform neutral_side "Where'd you go, then?" with dissolve
    show RoofSayori alert_worried -blush
    s "Huh?" with dissolve
    show RoofHiroko leanback neutral_left
    h neutral "Y'know, for the date?" with dissolve
    show RoofSayori alert_neutral
    s alert_neutral "I was just at his house for a while, why?" with dissolve
    show RoofHiroko smirk_left
    h uniform_headhold2 smirk_side "Oh man, Sayori, you had me going for a second there." with dissolve
    show RoofSayori alert_worried
    s "Huh?" with dissolve
    show RoofHiroko handcheek laugh
    h happy_closed "I thought you two were serious, but nah. You ain't dating." with dissolve
    show RoofSayori alert_smirk
    s alert_smirk "Oh, oh, Hiroko I understand and I hear loud and clear." with dissolve
    show RoofHiroko leanback surprised_left
    h surprised_side "... You do?" with dissolve
    s uniform_handup "Of course. You are saying a few hours consensually spent at his house means nothing. I happen to agree."
    show RoofSayori alert_happy
    s uniform_folded alert_laugh "Therefore, Kyou and I must go on a real date posthaste!" with dissolve
    show RoofHiroko growl_left
    h uniform_armup furious_side "What? {w=0.5}{nw}" with dissolve
    show RoofNozomi panicked_right
    extend "NO! You don't gotta do that!" with vpunch
    show RoofSayori leanforward alert_laugh
    s alert_giggle "Kyou! We are going out on a date this weekend!" with dissolve
    show RoofNozomi curious
    ks surprised "O-okay..." with dissolve
    show RoofHiroko irritated
    h uniform_headhold irritated "GAWD, how'd you get so annoying all of a sudden?" with dissolve
    "A... a date. I guess it was logical that we'd do something this weekend, but to have it spoken out loud so publicly. So proudly..."
    "I guess there's no backing out now."
    "Still, though..."
    show RoofHiroko frown
    show RoofNozomi neutral
    ks sigh "You, uh... you got time, right? I don't want to get in the way of your studies or anything." with dissolve
    show RoofSayori alert_smirk
    show RoofHiroko neutral_left
    "Sayori just giggles at me." with dissolve
    show RoofNozomi neutral_left
    show RoofSayori blush
    s uniform "Kyou, I am more than happy to clear my schedule to have a fun day out with my love! You know that~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    show RoofHiroko growl_left
    h frown_side "Are you serious, lady?" with dissolve
    show RoofSayori leanback alert_grin -blush
    s alert_smile "Mhmhm, why would I not be serious?" with dissolve
    show RoofHiroko handcheek irritated
    show RoofSayori alert_smile
    h uniform_armup sad_side "Like... okay yeah, I know I'm being a butt about your \"boyfriend\"..." with dissolve
    "She literally made the air quotes with her fingers. Little punk."
    show RoofHiroko frown_left
    h uniform neutral_side "But you ditched on guys before 'cuz you're always studying so hard." with dissolve
    show RoofNozomi worried_left
    n side sad_side "And we have a mock exam next week, come to think of it." with dissolve
    show RoofHiroko nervous_left
    h nervous_side "Right? So I don't get why you're rushing this stuff." with dissolve
    show RoofSayori alert_happy
    s alert_happy "No time like the present~ And besides, I know so much already." with dissolve
    show RoofSayori alert_pout
    s alert_annoyed "I mean, honestly, how much study does one need? I must have banked enough to get a weekend off, don't you think?" with dissolve
    show RoofHiroko leanback worried_left
    h uniform_headhold2 sad_side "W-well, I mean..." with dissolve
    "Nozomi gently clears her throat and smiles before speaking up."
    show RoofNozomi smile_left
    n smile_side "Sayori, I'm sure you already thought this through. You know what you're doing." with dissolve
    show RoofSayori alert_happy
    show RoofHiroko neutral_left
    s "Why, yes I do~" with dissolve
    show RoofNozomi smile
    n smile "Besides, I wanted to talk to you two about earlier. You said you're planning to follow Satoshi's hypnotist show last year with one of your own?" with dissolve
    ks confused "Oh, uh... yeah."
    show RoofNozomi curious
    n "How far have you gone in your plans for it?" with dissolve
    ks neutral "We kinda... just started, so we don't have anything written down yet."
    "... After all, \"[alt_name]\" kinda threw me for a loop with her confession, so we didn't get anything done."
    show RoofNozomi neutral_left
    show RoofSayori alert_grin
    s alert_smile "It sounds like someone wants to help." with dissolve
    show RoofNozomi laugh
    n laugh "Ahaha, well I mean..." with dissolve
    show RoofSayori alert_neutral
    show RoofNozomi irritated blush
    n pout_left blush "As our class representative, I have a responsibility to make sure the culture festival goes smoothly as far as we're concerned." with dissolve
    show RoofNozomi neutral_right
    n neutral_right "And that goes double if you're breaking away from the class café group this year. It's not like either of you have done this before." with dissolve
    show RoofNozomi frown_left
    n pout "N-not to mention we're friends and I rarely get to do anything for you, Sayori. Let me have this." with dissolve
    show RoofSayori alert_laugh
    "Sayori giggles." with dissolve
    show RoofNozomi neutral_left -blush
    show RoofHiroko surprised_left
    h surprised_side "Wow, you got a laugh on you, girl." with dissolve
    show RoofSayori alert_smile
    s alert_smile "Well, I would be delighted to have you assist us~" with dissolve
    show RoofHiroko neutral_left
    ks smile blush "I-if you think you could?" with dissolve
    "I gotta admit, the thought of Nozomi spending time with me is still an enticing one."
    show RoofNozomi happy
    n smile "Eheh, I'm sure I can contribute something." with dissolve
    show RoofNozomi smile
    n noblush "We'll need to step it up, though. The culture festival is only a few weeks away." with dissolve
    s uniform "That is true. Maybe we could do something for it this weekend as well."
    show RoofHiroko frown_left
    h frown_side "*ahem*" with dissolve
    show RoofNozomi neutral
    n neutral_right "I'm free tomorrow, so..." with dissolve
    ks "Tomorrow at my place then? I'll be home alone all day so no one will bother us."
    show RoofNozomi surprised
    n "Your place? I was thinking more..." with dissolve
    show RoofSayori alert_happy
    s alert_happy "No, Kyou's house is perfect. We'll go together~" with dissolve
    show RoofNozomi smile_left
    n smile_side "Well... alright, that works. So tomorrow morning, then?" with dissolve
    ks "S-sounds great, yeah."
    "Sayori claps her hands and grins."
    show RoofSayori leanforward alert_smirk
    s uniform_folded alert_giggle "Then it is settled! We'll work on the culture festival tomorrow, then on Sunday, date night with Kyou~" with dissolve
    "She then turns to face Hiroko with a giggle."
    show RoofSayori leanback alert_happy
    s uniform alert_happy "Which will follow my seeing Hiroko produce her finest tennis during the day~" with dissolve
    show RoofNozomi happy
    n happy "Naturally~" with dissolve
    show RoofNozomi smile_right
    show RoofSayori alert_smile
    show RoofHiroko handcheek annoyed
    h uniform_armup irritated "Oh, you sure? 'Cuz I thought this was Kyou's special weekend the way you're all talking." with dissolve
    show RoofHiroko irritated
    h uniform_headhold2 frown_side "Thought you all forgot about my big day." with dissolve
    show RoofNozomi laugh
    n laugh "Aw, never!" with dissolve
    show RoofSayori alert_smirk
    s uniform_handup alert_smirk "You are not one who is so easily forgotten, Hiroko." with dissolve
    show RoofHiroko leanback irritated
    h irritated "Pfeh!" with dissolve
    show RoofHiroko frown_left blush
    h frown_side blush "... Well, thanks." with dissolve
    stop music fadeout 10.0
    scene bg blackscreen with fade
    "There wasn't much of our lunchbreak left once we'd figured out our weekend plans."
    "... When was the last time I had weekend plans that involved other people?"
    play sound schoolbell
    scene bg classroom eve with blink
    "I don't think it's ever happened while I've been in high school."
    "And now, as the school day comes to an end, the giddy anticipation welling up inside me is becoming unbearable."
    scene bg corridor eve
    with blink
    queue music Inspiration
    "I'm sure everyone can see what I'm feeling as I head out of the classroom. As it is, I've noticed people are paying attention to me more since this morning."
    "Ever since I walked in with..."
    show Sayori alert_smile_right at center, zorder 2:
        xpos 0.5
    "Her." with dissolve
    "My stride suddenly cut short as I feel a pull at my arm, I turn just in time to be greeted by an affectionate peck on the cheek by my new girlfriend."
    s alert_happy "A little something to remember me by, my love~" with dissolve
    ks smile blush "Eheh, what do you mean? We're not walking home together?"
    "Her expression fades with a sigh."
    s uniform_handup alert_concerned "I will not be able to duck out of study club this time. The others need me to go over some particularly important material with them before the weekend." with dissolve
    s alert_sleeptalk "And since you find this commitment of mine so admirable, I would be remiss if I didn't go today." with dissolve
    ks "I guess you're right, yeah. Your people need you."
    s alert_smirk_right "Sometimes I wish I was not so smart." with dissolve
    ks "Yeah, well... I love your mind, Sayori."
    show Sayori uniform alert_giggle blush
    "We share a chuckle, and as I see the warmth reflected in her deep blue eyes, it makes me feel that absolutely everything is going to be okay." with dissolve
    "All I can see is a future where we're together..."
    show Hiroko uniform_armup surprised at center, zorder 0:
        xpos 0.6
    "... And also Hiroko just over Sayori's shoulder, sticking two fingers in her open mouth and pretending to retch." with dissolve
    s alert_concerned_right uniform_folded noblush "Is something the matter, Kyou?" with dissolve
    ks confused noblush "A-ah, no. I mean, I'm just sad I can't see you tonight."
    s alert_smile_right "That makes two of us. But we'll make up for it tomorrow, won't we." with dissolve
    ks smile "Y-yeah. Until then."
    scene bg street1 eve with blink
    stop music fadeout 5.0
    "For the first time in so long, I have reasons to be excited for the weekend."
    scene bg k bedroom eve with blink
    "And to think none of this would've come about if I hadn't taken up hypnosis. If Nozomi hadn't inspired me that day..."
    "Maybe tomorrow I could tell her how she influenced my life. I could even thank her for bringing me and Sayori together."
    "I think that'd be a nice thing to do."
    scene bg blackscreen with longdissolve
    pause 2.0
    # "Obviously putting all that time into his hypnosis hobby really paid off, and he kinda thinks he should thank Nozomi for her role in that."
    jump Day6_Con_Kyou_Sayori_Alter

label Day5_Con_Kyou_Sayori_Alter_Switch:
    pause 2.0
    scene bg street1 day with longdissolve
    "It's Friday, and I face the day ahead with another long sigh."
    play music Downtown
    "I ended up spending most of my night reading more about hypnosis and the concept of using it for effecting personality changes."

        # "But my words seemingly go unheard as Sayori suddenly jumps to her feet, her widened eyes still fixed on her phone screen."
        # s "Thursday? Why does it say Thursday?"
        # ks surprised "Hey, just calm down, alright? I'm sure there's a good expanation for all of this!"
        # s alert_surprised "First the deep sleep, and now this?" with dissolve
        # ks "Sayori, please listen!"
        # s uniform_folded "I can only conclude that you either tampered with my phone while I was too hypnotized to notice, or you effected a change upon me that caused me to sleep through an entire day." with dissolve
        # s alert_annoyed_right "But please, do tell me. What \"good\" explanation could you possibly have?" with dissolve
        # "... It's no good. Under her hardened gaze I know she's right."
        # "I knew it wasn't right to let her leave the house thinking she was the person I selfishly constructed for my own amusement."
        # show Sayori uniform_handup
        # "And it sure wasn't right to let her go on living her life as \"[alt_name]\" for an entire day, talking to her family and friends and classmates like she was some happy, carefree girl with a crush." with dissolve
        # "Whether I believed she was content to let it play out or not, I should have done something about it well before now."
        # show Sayori alert_concerned_right
        # "But it's too late for any of that. And in my silence, Sayori takes another look at her phone, then at me, as the colour begins to drain from her face." with dissolve
        # s uniform "Kyou... I-I am leaving now." with dissolve
        # s alert_sleeptalk "Do not try and stop me." with dissolve
        # scene bg blackscreen with longdissolve
        # "There's no good explanation for any of this..."


    if sayori_hurt == True:
        "But for all my reading into it, I still can't understand how Sayori was affected the way she seemed to be."
        "I just don't get how she fell so deep into the suggestion that she forgot who or where she was while she embraced the \"[alt_name]\" persona with such gusto."
        "Everything I've read suggested that Sayori wouldn't have accepted such a state unless she seriously wanted to."
        "If she accepted the idea of becoming a separate person the way I told her, then she must have agreed with it on some level."
        "But to embrace it so much that she actually seemed to be completely unaware of her time as [alt_name]? Was it out of shock in the moment, or..."
        scene bg school ext day with blink
        "Or can she really not remember at all? If she stuck around instead of fleeing, maybe we could've found out together."
    else:
        "But for all my reading into it, I'm still no closer to understanding why Sayori freaked out the way she did."
        # "For all his reading into things he's no closer to understanding why Sayori freaked out the way she did."
        "Everything I've seen suggests that Sayori wouldn't have accepted my suggestions, wouldn't have embraced her \"[alt_name]\" persona so fully, unless she seriously wanted to."
        "If she accepted the idea of becoming a separate person the way I told her, then she must have agreed with me on some level."
        "She really has to feel she needed to let her hair down. Just like she agreed that she needed to get more sleep."
        "It probably just surprised her that deep down she truly was looking for an excuse to let go, and that I would be the one to give it to her."
    # "It probably just surprised her that deep down she agreed with the things he was suggesting to her."
    # "Try as he might, he couldn't put Sayori out of his head for very long."
        scene bg school ext day with blink
        "Or she actually has feelings for me that she didn't want to admit? Maybe that's why she freaked out so much."
        "Well, hopefully now she's had a day to think about it Sayori will realize that about herself."
    "Sayori, she's... she's smart. And so, so studious. She must have been thinking about this stuff as much as I have."
    "She'll know I wasn't trying to do anything bad to her, and she'll want to talk to me again. She'll want to understand the reactions she's had to my hypnosis."
    # "He doesn't really want to give up all his hard work learning hypnosis after having finally gotten a chance to use it. But where does he even go from here if Sayori won't..."
    show Sayori sleeptalk at center
    "{cps=15}So when I see her again, I'll- {/cps}{w=0.5}{nw}" with dissolve
    ks surprised "S-Sayori!" with vpunch
    "Oh shit, there she is!"
    # "Suddenly, as he approaches the school gates, Sayori crosses his path." with dissolve
    s surprised_right "H-haah!" with dissolve
    "Man, I almost bumped right into her as I headed towards the school gates."
    s scared_right "Y-you..." with dissolve
    hide Sayori
    play sound runningshoes
    ks "Sayori, can we t-" with dissolve
    "Goddamn, she can move fast when she wants to."
    # "But as stare at each other for a moment I can only see one thing in those dishevelled eyes..."
    # "She doesn't seem to notice him, looking positively dishevelled, and is startled when Kyou calls her name." with dissolve
    # hide Sayori
    # "... Fear. She's no less terrified of me than before." with dissolve
    # "And in response she stutters out her surprise before beating a hasty retreat into the school." with dissolve
    # "Kyou winces inwardly. Seems she's no less terrified of him than before."
    scene bg classroom day with blink
    if sayori_hurt == True:
        "As I head into class and take my seat, I'm reminded again of just how much I fucked up with her."
        "Even if she knows I meant her no harm, if she still can't remember anything of her time as \"[alt_name]\"? "
        "That's gotta be a shock to the system to say the least."
    else:
        "As I head into class and take my seat, I can't help but feel a little annoyed now. This is getting ridiculous."
        "You'd think with the way she's acting I'd done something truly terrible to her."
    "And all I can do is settle into my seat and go through another day of lessons I could hardly care less about..."
    # , Kyou thinks to himself as he walks into class and settles in for another day of lessons he could hardly care less about..."
    # "It leaves him feeling more hopeless, as he walks into class and settles in for another day of lessons he could hardly care less about..."
    play sound schoolbell
    with longblink
    "It takes an age for lunch to come around. And the time hasn't dampened my feelings any."
    show Sayori uniform_folded neutral at center:
        xpos 0.75
    show Nozomi side neutral_side at center
    show Hiroko uniform_armup laugh_side uniform_arm at center, flip:
        xpos 0.25
    h "Lunchtiiiime~ {font=DejaVuSans.ttf}♫{/font}" with dissolve
    "I look up from my desk at the sound of the lunchbell to see Sayori and her friends making their usual chatter."
    n happy "Ehehe, it's that time again, huh." with dissolve
    if sayori_hurt == True:
        "If I could just talk to her and clear the air. Apologize. Find out how she's doing, at least..."
    else:
        "If I could just talk to her. Ask her why she's so freaked out about what we did together."
    show Nozomi neutral
    s uniform_handup concerned "Yes. Let us head to the rooftop posthaste." with dissolve
    h uniform_headhold2 confused_side "Man, really tells ya something if YOU wanna get outta here so bad, Sayori." with dissolve
    if sayori_hurt == True:
        "But it seems she can't even stand to look at me right now."
    else:
        "She can't go on avoiding me like this..."
    h nervous_side "Everything okay? I'm still worried about you after... well, y'know." with dissolve
    n sad_closed "Yeah... Well, you guys go on ahead, alright? There's something I need to take care of first." with dissolve
    # s "Mm..  maybe I can catch some z's while I'm up there today." with dissolve
    # , and Kyou nervously glances towards Sayori's desk as he wonders if he should just bite the bullet and force a conversation."
    # "He watches as she and her friends rise up from their desks and make noises about going up to the rooftop again, although Sayori is clearly ill at ease." with dissolve
    # "Nozomi tells the others she'll see them up there, as she has something to take care of first."
    hide Sayori
    hide Hiroko
    hide Nozomi
    with dissolve
    stop music fadeout 5.0
    if sayori_hurt == True:
        "I can only watch from my desk as Sayori hurriedly strolls ahead of the others to the door."
    else:
        "So I'll... damn, there's that unnatural speed again."
        "I can only look from my desk as Sayori strolls ahead of the others to the door just as I'd decided to make a move."
    # "How long does she think she can keep this up?"
    show Nozomi front2 neutral at center
    queue music Eons
    n "She doesn't want to talk to you today." with dissolve
    if sayori_hurt == True:
        "I let out a pained sigh."
        ks sigh "I just want to tell her I'm sorry for how things turned out."
        n side frown "Well maybe \"sorry\" isn't going to cut it right now after what you did to her." with dissolve
    else:
        "I let out another wistful sigh."
        ks sigh "She has to sometime. How long does she think she can keep this up?"
        n side furious "Until she's ready and not a moment before! Do you even hear yourself, Kyou?" with dissolve
    ks "It's just..."
    "Wait, what?"
    show Nozomi frown
    ks surprised "N-NOZOMI?!" with vpunch
    "Oh shit, how long has she been standing there while I was thinking about..."
    n irritated "God, you really are clueless aren't you." with dissolve
    "Okay, nevermind. Gotta push past it."
    ks confused "I'm sorry? W-what's going on?"
    n frown "What's going on is you hurt my friend, and you've got a lot of atoning to do." with dissolve
    n frown_side "But you're going to do it on HER terms, not yours. Okay?" with dissolve
    ks surprised "S-so she TOLD you about us?!"
    "Nozomi sighs harshly."
    n sad_closed "I'm going to regret this, aren't I." with dissolve
    play sound papers
    "I'm about to say \"Regret what?\" before I notice her placing a folded-up piece of note paper down on my desk."
    n sad "But... if you're serious about making up for this, meet us at my house tomorrow. We can all talk about it then." with dissolve
    "I thought Sayori didn't want me going anywhere near Nozomi, but now she's dragged her right into the middle of all this?"
    if sayori_hurt == True:
        ks confused "At least tell me how she's doing. Why'd she involve you at all?"
    else:
        ks confused "You... but... why do this? Why's she turning this into such a big thing?"
    "I'm so fucking confused."
    n frown "Look, do you want to talk to her or don't you?" with dissolve
    ks "O-of course I do!"
    n front2 sigh "Alright, then. We'll meet tomorrow at 12 o'clock, and I'll expect you to be on your best behaviour." with dissolve
    "This is awkward as all hell, but... it's progress, I guess?"
    ks neutral "Yeah... sure."
    n frown "And you'd BETTER stay away from her until then!" with dissolve
    stop music fadeout 5.0
    hide Nozomi
    "With that parting shot, Nozomi leaves to join the others and I..." with dissolve
    "I'm left with an intense feeling of dread."
    scene bg blackscreen with longdissolve
    pause 2.0
    scene bg k bedroom eve with longdissolve
    "The rest of my day was uneventful, if a little tense."
    queue music Past_Sadness
    "I'm still on shaky ground with Sayori, and Nozomi too. So I didn't so much as look their way for the rest of the day if that's how they want to play it."
    if sayori_hurt == True:
        "But tomorrow I'll finally be able to talk to Sayori and figure out what the hell happened to her."
        "Figure out how badly I screwed up?"
        "I mean sure, hypnosis can't force someone to do things they don't want to do. Pretty much everything I read on it confirmed that was the case."
        "But even so, I've also read how it can lower a person's inhibitions. Convince them to maybe go a little further than they meant to."
        scene cg k room eve:
            matrixcolor SaturationMatrix(0)
        show SayoriHypno drooping alert_sleep:
            matrixcolor SaturationMatrix(0)
        with blink
        "I know Sayori was nervous about this whole deal, but she went along with it for my sake."
        "And yeah, it seems she did come around to it in a big way, more than she ever thought she would."
        "But it was supposed to be just a little trick for my hypnosis show. And a trick is supposed to end when the show's over."
        "I REALLY should've told her to go back to normal before I let her leave last night."
        stop music fadeout 5.0
        scene bg k bedroom eve with blink
        "But it's too late to think about what I should've done. I can only hope Sayori can forgive me for it, and give me a chance to set things right."
        "Sayori's a logical person, after all. So if I can just sit down with her and explain everything rationally, I'm sure she'll come around..."
        # "Man, I can't wrap my head around what fucking happened just now."
        # "The moment I spoke the words to flip her back to normal, it's like she had no awareness of her time acting as \"[alt_name]\" at all."
        # "It really did feel like she had become a whole different person, with separate memories and everything."
        # "But that's... that's impossible! How in the world did she internalize my suggestions as much as that?"
        # "Dammit Sayori, I need to know more. I need to talk to you again."
        # "You can't just run away from me like this..."
        # with longblink
        # play sound schoolbell
        # queue music Eons
        # "The lunch period comes and goes, and Sayori returned to her desk without making eye contact."
        # "We're supposed to be reviewing some lesson material for our upcoming exams, but I can't concentrate on any of that."
        # "I'm kinda freaking out a bit."
        # "Hypnosis can't force someone to do things they don't want to do. I know that. Pretty much everything I read on it confirmed that."
        # "But even so, I've also read how it can lower a person's inhibitions. Convince them to maybe go a little further than they meant to."
        # scene cg k room eve:
        #     matrixcolor SaturationMatrix(0)
        # show SayoriHypno drooping alert_sleep:
        #     matrixcolor SaturationMatrix(0)
        # with blink
        # "Sayori was nervous about this whole deal, but she went along with it for my sake."
        # "And yeah, she did come around to it in a big way, more than she ever thought she would."
        # "But it was supposed to be just a little trick for my hypnosis show. And a trick is supposed to end when the show's over."
        # "I REALLY should've told her to go back to normal before I let her leave last night."

    else:
        "But tomorrow I'll be able to make my case and everyone will start to see sense at last."
        show penlight at right with moveinright:
            ypos 0.346
        "Hypnosis isn't magic, and neither is this penlight I've constructed. Everyone's got to know that, right?"
        "Even if it had a bigger effect on Sayori than I could've imagined. Is the patterning I imprinted on it really that captivating for her?"
        "Kinda makes me wonder if it would somehow have the same effect on someone else..."
        hide penlight at right with moveoutright
        "Ugh, no, I can't think like that. That's the kind of thinking that got me in trouble with Sayori in the first place."
        "I have to set things straight with her first. I need to show her she's got no reason to be scared of me, or of hypnosis."
        # "Well, he'll put the penlight and his curiosity away for now. His focus is on setting things straight with Sayori."
        # "She's just got no reason to be scared of him or of hypnosis, and tomorrow he's determined to convince her."
        "Sayori's a logical person when it comes down to it. So if I can just sit down with her and explain everything rationally, I'm sure she'll see sense..."
    stop music fadeout 5.0
    "... Won't she?"
    scene bg blackscreen with longdissolve
    pause 2.0
    jump Day6_Con_Kyou_Sayori_Alter_Switch
    # "He starts to say something, but she's already turned away and begun scampering towards the door to rejoin the others." with dissolve
    # "\"What was that about?\" He wonders to himself, only to notice the piece of notepaper that Sayori must have left on his desk."
    #He also said he wasn't asking her to do this in front of everybody, but now she's performed as her alter in front of many people against her will

label Day5_Con_Kyou_Hiroko_Penlight:
    scene bg street1 day with longblink
    "It's Friday, and I'm walking to school with a sense of determination."
    play music Bright_Opening
    scene bg classroom day with blink
    "I may have calmed down a little since last night, but I swear if Hiroko doesn't give me back my..."
    show Hiroko at center:
        xpos 1.1
        linear 1.2 xpos 0.7
    ks frown "Hiroko!"
    show Hiroko:
        xpos 0.7
    h surprised "Huh? Oh, hey Kyou." with dissolve
    ks "Got something for me?"
    h sleep "Hrm... Have I got somethin' for ya..." with dissolve
    ks sigh "Don't be obnoxious. Just hand it over."
    h neutral_side "Oh... Sure, dude. I gotcha covered. Lemme just reach into my pocket here." with dissolve
    ks frown "You're gonna flip me the bird, aren't you."
    h angry "Wow. Really, dude?{w=0.5} {nw}" with dissolve
    extend  "REALLY?" with vpunch
    ks "Don't do this."
    h irritated "Like... Wow." with dissolve
    h frown "Really shows what you think of a lady, don't it." with dissolve
    ks angry "Shows what I think of YOU!"
    h frown_side "How fuckin' dare you. I got more for you than just a birdie, c'mon." with dissolve
    h sleep "But, hrm, it ain't in there..." with dissolve
    ks frown "Hiroko..."
    h neutral_side "So, like, maybe it's in my other pocket..." with dissolve
    "I sigh loudly as she goes about her childish theatrics."
    h surprised "Ah yeah, here it is!" with dissolve
    ks sigh "Two birdies."
    h uniform_armup happy "TWO birdies!" with vpunch
    "I fucking despair, I really do."
    "{cps=20}But as soon as we're out of class today, I'll-{/cps}{w=1.0}{nw}"
    $nozomi_name = "???"
    show Nozomi side frown_side at center:
        xpos 1.1
        linear 1.0 xpos 0.9
    n "Hiroko, what on earth are you doing?"
    show Nozomi surprised:
        xpos 0.9
    show Hiroko surprised
    ks surprised "A-AAAAGH!" with vpunch
    "Oh god, I nearly fell out of my chair when this... this THING just shambled over to us."
    "Who the fuck is that? That voice doesn't sound like anyone from my class. A teacher, maybe?"
    n sad_side "Is... Is he okay?" with dissolve
    "Fuck, I dunno. Whoever that is, her voice is really fucking nasally. I can't stand it."
    "But who IS it?"
    show Hiroko uniform smirk at flip
    h "Heh, beats me. I mean c'mon, it's Kyou we're talking about." with dissolve
    "Maybe if I took another look at her..."
    ks sigh "Ugh, {w=0.2}{nw}"
    show Nozomi front surprised
    extend "NO!" with vpunch
    $nozomi_name = _("Ugly Girl")
    "Bad idea. I'm turning away again."
    n "Kyou? Do you need us to call the nurse?"
    "Whoever she is, she seems to know me. I suppose I better answer her."
    ks angry "Ugh, no I don't... I don't need the nurse, just get outta here!"
    "I emphasise my demand with a flap of my arm behind me. I just... god, just fucking leave me be so I don't have to look at that eyesore of a face!"
    play sound schoolbell
    n concerned "W-... w-well, class is about to start anyway. Come on, Hiroko, let's go." with dissolve
    h smile_side "Yeah, sure thing, Nozo~" with dissolve
    hide Hiroko
    hide Nozomi
    with dissolve
    "Oh thank fuck, she's gone."
    "... Wait, did I hear that right?"
    ks surprised "{size=16}... \"Nozo?\"{/size}"
    $nozomi_name = "Nozomi"
    "That was NOZOMI?!"
    # "Almost makes me want to look at her again, but the mere sight of it..."
    # "Maybe if I ignore it
    with blink
    "No."
    "No, there's no way."
    "There is NO fucking way that that... that MONSTROSITY sitting right there is Nozomi."
    "Maybe some creature killed her and is wearing her skin like some kind of ill-fitting suit."
    "Would explain why her body looks so saggy and wrinkly. Christ."
    "And that disgusting troll hair, draped over the back of her seat like a raggy mop head that hasn't been cleaned in decades."
    "No, come on. I gotta look away again, this is just making me angry."
    "I need to concentrate on the lesson. Keep my head down and... try not to let any of this get to me."


    # "As usual, Kyou's having trouble concentrating on the lesson material."
    # "How can he? He needs to get back at Hiroko and recover his penlight."
    # "And also how gross is Nozomi being right now? Sitting there and getting her disgusting troll hair all over the seat."
    # "How can anyone even stand to sit near her?"
    play sound schoolbell
    with blink
    "It's a minor relief when lunch rolls round once more."
    "If I know those girls, they'll be heading upstairs and I'll be able to eat in here without the sight of that Nozomi impostor killing whatever appetite I have left."
    # show Hiroko at center
    # show Sayori neutral at center, flip:
    #     xpos 0.25
    # show Nozomi side smile_side at center:
    #     xpos 0.75
    # with dissolve
    show ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_smile_sayori n_armup n_smile_right glasses sayori s_smile_nozomi with blink
    n "All set?"
    "Goddamn, I can hear her irritating nasal whine from here."
    show ClassroomLunch h_worried_nozomi
    h smile_side "Hey, Nozo, hold up a sec." with dissolve
    show ClassroomLunch n_smile_left s_neutral_hiroko
    n sad_side "Huh?" with dissolve
    show ClassroomLunch h_sad_nozomi
    h frown "Yeah. I just..." with dissolve
    "Wait, what's Hiroko saying?"
    show ClassroomLunch h_worried_nozomi
    h sad_side "Man, I can't believe I'm saying this, but I'm kinda worried about Kyou over there." with dissolve
    show ClassroomLunch n_folded n_neutral_left
    n sad "... Really?" with dissolve
    show ClassroomLunch h_sad_nozomi
    h sad "Uh-huh." with dissolve
    "Don't... don't bring her over here, for fuck's sake..."
    show ClassroomLunch s_concerned_nozomi
    s uniform_folded concerned "He has seemed more... animated than usual today." with dissolve
    show ClassroomLunch n_frown_left
    n frown_side "Yes, well, I saw Hiroko antagonizing him this morning!" with dissolve
    show ClassroomLunch h_neutral_nozomi
    h sad_talk "Yeah, but you really think that's why he's acting out like that?" with dissolve
    show ClassroomLunch h_sad_nozomi n_armup n_thinking
    h concerned "Dude looks like he's in some kinda pain, an' it's bumming me out." with dissolve
    show ClassroomLunch h_grin_nozomi
    h uniform happy "So like, how 'bout we lunch with him today? Cheer him up a bit?" with dissolve
    show ClassroomLunch k_furious
    "Oh my god Hiroko, you unbelievable BITCH!" with dissolve id Day5_Con_Kyou_Hiroko_Penlight_ebdc26a1
    show ClassroomLunch n_nervous_left s_neutral_hiroko
    n sad_side "I don't know. He seems in a really antisocial mood." with dissolve
    show ClassroomLunch h_worried_nozomi
    h sad_side "Oh yeah, that's probably my fault." with dissolve
    show ClassroomLunch h_grin_nozomi n_folded n_thinking
    h uniform_armup smile "Anyway, don't worry. I'm gonna go over there an' say sorry." with dissolve
    show ClassroomLunch s_pout
    s annoyed "Hm... how characteristically humble of you." with dissolve
    show ClassroomLunch k_nervous s_neutral_hiroko n_smile_left
    n sad "O-okay... If you're sure this is what you want." with dissolve
    "Just hearing her voice from here is bad enough."
    $ persistent.classroomlunch5_2_unlock = True
    scene bg blackscreen with dissolve
    h uniform smile_side "Okay! C'mon, we're doing this~"
    "No..."
    scene bg classroom day
    show Hiroko neutral at center, flip
    show Sayori neutral_right at center, flip:
        xpos 0.25
    show Nozomi front sleep at center:
        xpos 0.75
    with dissolve
    n "Alright, then. Lead on."
    "No!"
    show Nozomi neutral
    h happy_closed "Okey-dokey!" with dissolve
    "NOOOOOOOOOOOOOOOOOOOOOO!" with shake
    "I can only watch in quiet horror as Hiroko leads Sayori and that creature over to my desk."
    "If I didn't know better, I'd say she looks almost angelic with that smile she's wearing."
    "But I know the depths of pure evil hiding beneath that mass of bubblegum pink."
    h smile "Hey, Kyou~ You got a sec?" with dissolve
    # "And just like that, they're upon me. Hiroko, her worn-out friend and that goddamned ogre."
    "I'll just... turn a little to the side and pretend that wretched Nozomi doppelganger isn't here."
    ks frown "What... is it?"
    h happy_closed "Oh, nothin' much. I just wanted to say sorry for being a butt to you this morning." with dissolve
    "Don't make that face when you say sorry."
    ks frown "S-sure... No problem."
    h smile "And, look, maybe you're going through some shit. Ain't my business, but..." with dissolve
    "Just get out of here. And take her with you, I can't stand it!"
    h uniform_armup happy_closed "It cool if we sit here today?" with dissolve
    ks sigh "U-... u-u-u-hhh..."
    h smile "That was a yes, right?" with dissolve
    n side sad "You can say no if you want, Kyou. Don't feel pressured." with dissolve
    ks "Ugh... u-uurghhh..."
    "Shut up, fake Nozomi... please shut the fuck up..."
    h uniform surprised_side "Wha? You really think he don't want our cutie of a class rep havin' lunch with him?" with dissolve
    n sad_closed "That's laying it on a little thick, Hiroko." with dissolve
    h smirk "Say it ain't so!" with dissolve
    ks angry "That's... {w=0.5}{nw}"
    show Nozomi front shocked
    show Hiroko shocked
    show Sayori surprised_right
    play sound punch
    extend "ENOUGH!" with vpunch
    "Jumping up from my chair, I slam my palms down on the desk in frustration."
    ks "Just get away from me!"
    stop music fadeout 5.0
    "I can't... I can't take this anymore."
    play sound runningshoes
    scene bg corridor day with blink
    "I need to get away."
    scene bg rooftop with blink
    "Just anywhere to be away from... HER!"
    play music Downtown
    ks sigh "Haaah... Haaah..."
    "Yeah, that's it. Now I can breathe. Nice, clean fresh air that she hasn't polluted with her rancid stench."
    "Holy shit, I didn't think anyone could be so gross..."
    ks frown "Gross..."
    "\"I'm gonna make you think Nozo's gross.\""
    ks "Hiroko. She... She really did it, huh."
    "Not only did that little skank steal my penlight, she really DOES know how to use it."
    "What the fuck does this MEAN?"
    "She doesn't have any idea how to hypnotize. She DOESN'T!"
    "But the way she's affected me..."
    "So she was telling the truth about the times I hypnotized her?"

    #New idea: Hiroko proposes spending lunch with Kyou to cheer him up as well as apologize for flipping him off
    #Nozomi goes along out of good-naturedness. Sayori is sure Hiroko's up to something

    #I know, right? Not every day you get to talk to us cuties~



    # h angry_side "No way, you're coming with!" with dissolve
    # n front sigh "Why on earth?" with dissolve
    # h uniform surprised_side "'Cuz he should say sorry to you!" with dissolve
    # n annoyed_left "Hiroko, it's okay. I don't want to get involved." with dissolve
    # "If she could just... stop... talking..."
    # h sad_side "Just fucks me off that he thinks he can talk to you like that." with dissolve



    # s uniform_folded annoyed "I admit I am curious, but I do not think it merits a confrontation." with dissolve

    # "But to his horror, when lunch swings around, Hiroko says a few things to her friends and they end up walking over to Kyou's desk."
    # h "Hey, it cool if we sit here today?"
    # "Kyou is deeply conflicted. He needs to talk to Hiroko, but..."
    # "Wait a fucking minute, what is it about Nozomi today? How did she get so... repulsive?"
    # show Hiroko:
    #     linear 1.0 ypos 1.1
    # show Nozomi:
    #     linear 1.0 ypos 1.1
    # show Sayori at flip:
    #     linear 1.0 xpos 0.25 ypos 1.1
    # "Kyou grumbles and agrees, so they sit down to eat."
    # show Hiroko:
    #     ypos 1.1
    # show Nozomi:
    #     ypos 1.1
    # show Sayori at flip:
    #     xpos 0.25 ypos 1.1
    # "Sayori and Nozomi are very bemused at the situation, but seem to go along with it in their curiosity over what Hiroko's up to."
    # "Hiroko tries to start some smalltalk. How's it hanging, Kyou?"
    # "Kyou tries to concentrate, and answers non-committally, but then Nozomi inevitably chimes in and OH MY GOD HER VOICE IS SO ANNOYING."
    # show Hiroko smirk
    # show Nozomi sad
    # show Sayori surprised_right
    # "Kyou finds it impossible to hide his discomfort, and what makes it worse is Hiroko's undisguised glee in seeing Kyou suffer." with dissolve
    # "It's so unbearable that Kyou angrily excuses himself and leaves the table, saying he needs to get some air or something."
    # "Just anything to get away from that revolting class rep!"

    # "How's he gonna get near Hiroko without that disgusting creature getting in the way?"
    # "... Wait, what the hell is he thinking about Nozomi? Now he's got some time to himself he realizes how odd this is."
    # "So not only does Hiroko have his penlight, she actually did with it what she said she would."
    # "That Hiroko can hypnotize him without any training whatsoever is probably going to dent his ego given all the studying he did on the subject, but also..."
    # "Doesn't this mean Hiroko really was telling the truth about how his hypnosis affected her? How is this possible?"
    "Like, holy shit I need to talk to her more than ever."
    "But not right now. Not while... Not while Nozomi is near."
    "Much as I hate to admit, even knowing this is all a trick of my own mind, there's no way I can be close to our class rep right now."
    scene bg classroom day with blink
    "So I'll have to wait until school is out. Find Hiroko at tennis practice and then..."
    "THEN we are gonna have some fucking words..."
    # "When he returns to class after lunch he knows he needs to talk to her more than ever."
    "Because that penlight is DANGEROUS in the wrong hands!"
    scene bg classroom eve
    play sound schoolbell
    show Nozomi front at right
    with blink
    n "Stand!"
    n "Bow!"
    ks sigh "Eesh, that's nasty."
    n side sad "Huh?" with dissolve
    "... I'll just look the other way and pretend I didn't say anything."
    hide Nozomi with dissolve
    "Although I was CLEARLY mocking her revolting mouth words."
    "... Agh, no I'm doing it again. Stop thinking about her gross ass, Kyou!"
    # "Kyou grimaces in disgust as Nozomi leads the end of class routine, evoking another funny look from the class rep who's still trying to figure out what his deal is."
    scene bg corridor eve
    with blink
    "Just head out of here and keep your eyes on the prize."
    show Hiroko frown_side at center with dissolve
    "There. That's the REAL monster around here!"
    scene bg court eve
    show Hiroko frown_side at center
    with blink
    ks angry "Hiroko!"
    h surprised "Huh? {w=1.0}{nw}" with dissolve
    show Hiroko frown
    $ renpy.transition(dissolve, layer="master")
    extend "Oh, fuck me whaddya want?"
    ks "I want what you took from me!"
    h angry "Oh yeah? {w=0.5}Well first I want what you {nw}" with dissolve
    extend "OWE me!" with vpunch
    ks "\"Owe\" you?"
    h "Oh yeah, I mean..."
    h smirk "Nozo don't seem so hot to you now, does she?" with dissolve
    ks frown "What did you even say to me to get me thinking these... things about her?"
    h sleep "Eh... like I remember most of it." with dissolve
    h frown "I was just like... \"Nozomi from our class is so gross to you, you don't even wanna be in the same room as her.\"" with dissolve
    h frown_side "\"Everythin' about her is gross. The way she looks, the way she talks, even the way she smells... You're totally grossed out by her.\"" with dissolve
    h sleeptalk "Y'know, stuff like that." with dissolve
    h neutral "So now I gotta ask..." with dissolve
    h smirk "What does she look like now? I'm super curious." with dissolve
    ks angry "Just give me my penlight back! You've done enough damage."
    h frown "Gotta settle yer bet first." with dissolve
    ks "Where is it?"
    "She makes a face and shrugs."
    h neutral "You think I got it on me?" with dissolve
    h smile_side "So anyway... You swing by here tomorrow morning, yeah?" with dissolve
    h smile "I wanna see you bright 'n' early!" with dissolve
    ks frown "And then what?"
    h frown "Then you help me with my tennis shit." with dissolve
    h frown_side "You get your lil' toy back when we're done with the tourney. Got it?" with dissolve
    "I'm out of words for this pint-sized asshole."
    h uniform_armup angry "'Kay. Now get outta here, some of us got work to do." with dissolve
    stop music fadeout 5.0
    scene bg k bedroom eve with longblink
    "I arrive back at home seething."
    "Hiroko must know what she has, right? She's the one who figured it out first, and tested her hypothesis on me."
    "But then, if she truly knows how powerful the penlight is..."
    "IS she going to give it back?"
    "If I were in her shoes, wouldn't I keep it?"
    "Wouldn't I test it on that other girl she hangs out with in the tennis club, get her to throw their games or something?"
    "Maybe if that worked, I'd try it on my opponents in this tournament I have coming up, if I got the chance."
    "And then after that? Maybe the sky's the limit..."
    "I need to stop her."
    scene bg blackscreen with longdissolve
    pause 2.0
    jump Day6_Con_Kyou_Hiroko_Penlight

label Day5_Con_Kyou_Hiroko_Trickster:
    scene bg street1 day with longdissolve
    "It's Friday, and I'm walking to school feeling excited."
    play music Bright_Opening
    scene bg classroom day with longblink
    "After all..."
    show Sayori uniform_folded smile at center, flip:
        xpos 0.25
    show Hiroko uniform neutral_side at center
    s "Good morning." with dissolve
    "I've been dying to find out how Hiroko will handle herself today."
    h "Hey, Sayori. You doing okay?"
    s sleeptalk "Ahh... I will get through the day." with dissolve
    show Nozomi side uniform smile_side at center:
        xpos 1.25
        linear 1.0 xpos 0.75
    n "Morning, you two!"
    show Nozomi:
        xpos 0.75
    show Sayori smile
    h neutral "Hey, Nozo." with dissolve
    s "Good morning!"
    "I mean, sure, maybe she'll manage to disappoint me."
    n "All set for the weekend, Hiroko?"
    show Hiroko smile_side at flip
    h "H'yeah, I wanna do some more prep with Risa tonight, but I think I'm good~" with dissolve
    "Maybe she really will be able to resist the compulsions I taught her while she was under last night."
    n laugh "Ahh, I can't wait to see you in action! It's been too long!" with dissolve
    "Surely most people would in her situation."
    h uniform_armup happy "Oh man, yeah~ Just talking about it's getting me pumped again!" with dissolve
    show phone at right with moveinright:
        ypos 0.346
    "But as I've found out, Hiroko isn't exactly \"most people\". So I'll just send her a quick, discreet text to get us started..."
    "{color=#4B9374}\"Good morning.\"{/color}"
    # "But as I take out my phone and discreetly send a text I have a feeling she's going to work with me here."
    stop music fadeout 5.0
    h "I just wanna get out there and... {w=0.5}{nw}"
    show Hiroko sleeptalk
    show Nozomi neutral_side
    show Sayori neutral
    $ renpy.transition(longdissolve, layer="master")
    extend "{w=1.0}aawwwn..."
    hide phone at right with moveoutright
    show Hiroko uniform neutral
    s smirk "Perhaps you should be a little less pumped and save some of that energy for the tournament." with dissolve
    play music Downtown
    show Hiroko angry
    "Just then, Hiroko wheels around and shoots me a look." with dissolve
    "I simply smile at her, placing my phone on the desk where she can see while I begin typing another quick message."
    h uniform_headhold2 irritated "A-ah, shut up, Sayori. I'm fine." with dissolve
    show phone at right with moveinright:
        ypos 0.346
    h frown "I got all the energy I... {w=0.5}{nw}" with dissolve
    show Hiroko sleeptalk
    show Nozomi sad_side
    show Sayori neutral
    $ renpy.transition(longdissolve, layer="master")
    extend "{w=1.0}ohhhn, n-need."
    hide phone at right with moveoutright
    "I knew it. She'll definitely co-operate with what I told her last night."
    "Whether she likes it or not..."
    scene HirokoYawn day n_listening h_sitting h_neutral with longblink
    "It's hard once again to concentrate on the lessons this morning. But I don't think I can blame myself for that."
    "Not when I can torment Hiroko from the safety of my desk any time I want."
    show phone at right with moveinright:
        ypos 0.346
    "For this morning, I'll try to send her a text every fifteen minutes or so. Keep that going for a couple hours and observe her reactions each time."
    "Makes me wish we sat a little closer so I could get a better look at her face..."
    hide phone
    show HirokoYawn h_frown
    with blink
    "Well, maybe I can't see her as well as I want, but I can tell what I'm doing back here is having an effect..."
    show phonetext at center:
        ypos 0.6
    with dissolve
    # "I may not get to see her face, but I can just imagine the conflict of rage and sleepiness that must be going on over there."
    "Every time I press send, I watch as the back of that pink head bobs reflexively within moments."
    hide phonetext
    show HirokoYawn h_yawning h_sleepy
    with longdissolve
    "And every time I see her hand drifting to her face to disguise the fact her jaw just opened up."
    show HirokoYawn n_concerned h_angry
    # "Usually I'll also notice Nozomi sat beside her, looking across from her desk at her friend, who irritatedly waves her unspoken concerns away."
    "Sometimes I'll also notice Nozomi quietly looking up from her desk to her friend, usually for an extended period, before turning her attention back to her work." with dissolve
    "And then fifteen minutes later I'll send another text..."
    show HirokoYawn n_listening h_sitting h_frown_left
    with blink
    "I've been keeping this up for a couple hours now."
    show HirokoYawn h_yawning h_sleepy with longdissolve
    "Not only is Hiroko still yawning every time I prompt her, she's never once moved to try and disable her phone or take it out of her pocket."
    show HirokoYawn n_concerned h_sitting h_frown_left
    with blink
    "This is way more fascinating than the history lecture I'm supposed to be listening to."
    "... Maybe I can get a pavlovian yawn out of her?"
    "Yeah, I'll just skip sending her a text this time and see if she yawns out of instinct."
    "... Hmm, nothing? Shame, but again, it's only been a couple hours."
    $persistent.hiroko_yawn_day_unlock = True
    play sound schoolbell
    scene bg classroom day
    show Sayori uniform_folded neutral at center, flip:
        xpos 0.25
    show Hiroko uniform frown_side at center
    show Nozomi side uniform sad_side at center:
        xpos 0.75
    with blink
    "But what if I kept this up after lunch? I have to ponder that as class breaks up for just that reason."
    n "Gosh, Hiroko, how long were you up last night? You couldn't stop yawning!"
    h uniform_armup angry vein "Ugh, I'm telling ya, I ain't tired, it's just..." with dissolve
    "Hiroko notices me watching and shoots me a glare, then takes her phone up in her hands while she talks."
    show Hiroko uniform_headhold angry_side novein
    h "I'm just... I dunno, really... fuckin' bored?" with dissolve
    play sound cellvibrate
    "Just then my phone vibrates on my desk..." with vpunch
    show phone at right with moveinright:
        ypos 0.346
    "{color=#FF89AB}OMFG STOP DOING THAT{/color}"
    s frown "Bored? I have not known you to be so theatrical, Hiroko." with dissolve
    "Well, if she's going to text me I should reply, right?"
    h frown_side "Y-yeah, but c'mon, can you blame me? I can't think about school shit right now." with dissolve
    "{color=#4B9374}\"Stop doing what?\"{/color}"
    h "Gotta focus on... {w=0.5}{nw}"
    show Hiroko uniform_headhold2 sleeptalk
    $ renpy.transition(longdissolve, layer="master")
    extend "{w=1.0}aaaaww... m-my game. {w=1.0}{nw}"
    extend irritated "SHIT!" with vpunch
    hide phone at right with moveoutright
    s smirk "So if you are yawning now does that mean you're bored of our company?" with dissolve
    h furious_side uniform_armup "Wha?! {w=0.5}{nw}" with dissolve
    extend "NO! I just..." with vpunch
    show Hiroko frown
    "Hiroko looks to me again as I simply smile to myself." with dissolve
    "She's so utterly convinced she has to yawn at my prompt. No matter how embarrassing it might be to do it."
    show Sayori uniform smile
    h uniform neutral_side "Let's just get outta here, okay? I want some air." with dissolve
    n smile_side "Sure. Rooftop it is, then~" with dissolve
    hide Sayori
    hide Nozomi
    hide Hiroko
    "And as she retreats from the classroom, another thought crosses my mind..." with dissolve
    show phone at right with moveinright:
        ypos 0.346
    "{color=#4B9374}\"How sleepy are you feeling? Scale of 1-10?\"{/color}"
    "I mean, that's something else I told her last night; that she should feel sleepier with every yawn. I want to know how she interpreted it."
    hide phone
    with blink
    "Although I'm hardly shocked that she doesn't hurry back to respond."
    play sound cellvibrate
    "When my phone eventually buzzes with news of a reply, lunch break is almost over."
    show phone at right with moveinright:
        ypos 0.346
    "{color=#FF89AB}Dont make me yawn anymore im serious{/color}"
    hide phone at right with moveoutright
    "It makes me smirk. She's so completely taken in by what I've done and it's as fascinating as it is hilarious."
    "But do I stop playing for now? It feels like I've made my point with her."
    "She'll be seeing me again tonight for another hypnosis session. After what I've seen this morning I'm absolutely sure of it."
    "On the other hand, why stop now? I want to see how far she'll go. Whether she'll actually yawn herself to sleep if I text her enough."
    "Wouldn't that be interesting to find out?"
    menu:
        "Keep going":
            "Yeah, that's exactly what I'm going to do this afternoon."
            show Sayori uniform neutral at center:
                xpos 0.25
            show Hiroko frown at center
            show Nozomi side uniform smile_side at center:
                xpos 0.75
            "With her perfectly willing assistance, of course." with dissolve
            n "Cheer up, Hiroko. It's only a few more hours."
            h frown_side "Yeah thanks, Nozo, I know how a school works." with dissolve
            s rolleyes "Would that you could apply that knowledge productively." with dissolve
            hide Sayori
            hide Nozomi
            h uniform_armup irritated "Whatevs. I'm just not feeling it today. Big deal!" with dissolve
            show Hiroko uniform frown
            "As the others walk to their seats, Hiroko takes a moment to stop and look my way again." with dissolve
            "She may not say anything, but that harsh glare of hers does all the talking she needs..."
            "... That reminds me, I wrote a reply to her text but, uh... \"forgot\" to hit send."
            show phone at right with moveinright:
                ypos 0.346
            "I should take care of that before class starts."
            "{color=#4B9374}\"Ok\"{/color}"
            h sleeptalk "A- awwwwn... {w=1.0}{nw}" with dissolve
            show Hiroko irritated
            $ renpy.transition(dissolve, layer="master")
            extend "{size=16}fuck off.{/size}"
            scene HirokoYawn day n_listening h_sitting h_frown with blink
            "I was texting her about every fifteen minutes before. This afternoon I'll text her whenever it's convenient."
            "And too bad for you, Hiroko, nobody pays attention to me so I'm going to be doing this a lot."
            show HirokoYawn h_yawning h_sleepy
            "And all you'll be able to do is sit right over there. Just yawning and yawning..." with dissolve
            # show Hiroko sleepy at left
            # scene bg classroom eve
            show HirokoYawn eve e_neutral n_listening h_sitting h_sleepy with longblink
            # show Hiroko sleepy at left
            # with blink
            stop music fadeout 10.0
            "Getting sleepier and sleepier..."
            show HirokoYawn n_concerned h_yawn
            "Letting me watch your head bob up and droop down. Bob up and droop down. A tiny bit lower every time while I spam your inbox..." with dissolve
            show HirokoYawn e_curious n_shocked h_sleeping h_sleep
            $ renpy.transition(longdissolve, layer="master")
            "Until eventually..."
            h "{size=16}Mmrn... mmm...{/size}"
            $t = "Mr. Kobayashi"
            t "... Is something the matter, Miss Homura?"
            play music Black_Room
            show HirokoYawn h_waking
            h "{size=16}{cps=10}Mmn... {w=1.0}m-{/cps}{/size}{nw}" with dissolve
            show HirokoYawn h_sitting_blush h_panic
            extend uniform_armup shocked "{cps=15}mwHAA?!{/cps}" with vpunch
            play sound AudienceLaughter
            show HirokoYawn e_laugh
            "The whole classroom bursts out laughing as Hiroko throws her head up from the desk and scrabbles to rouse herself in front of our homeroom teacher." with dissolve
            show Hiroko:
                ypos 1.0
            "It's not that he hasn't noticed her flagging before now, but if she has the audacity to fall asleep right in front of him then he really has no choice but to call her out."
            show HirokoYawn h_sorry
            h uniform sleepy "Mrrgh, I didn't mean to. S-sorry..." with dissolve
            "Yeah. She really DID fall asleep because of me!"
            t "Do you think you can stay with us a little longer?"
            "In spite of how humiliating it must have been to follow through, she still felt the hypnotic compulsion I gave her was too strong to resist."
            show HirokoYawn h_sleepy
            h frown "O-oh, yeah for sure." with dissolve
            show phonetext at center:
                ypos 0.6
            with dissolve
            pause 1.0
            hide phonetext with dissolve
            h "I ain't gonna... {w=1.0}{nw}"
            show HirokoYawn h_yawn
            $ renpy.transition(dissolve, layer="master")
            extend "{cps=10}aaaawww... {/cps}{size=16}f-fall asleep again....{/size}"
            show HirokoYawn h_sleeping_blush h_sleep with longdissolve
            play sound AudienceLaughter
            "Heh. Yep, even now with everyone's attention on her. Even as they laugh..."
            show HirokoYawn h_waking
            h sleepy "I-I mean..." with dissolve
            t "*sigh* It's almost hometime so just rest if you have to, Homura."
            t "But no more staying up late on a school day, is that understood?"
            show phonetext at center:
                ypos 0.6
            with dissolve
            pause 1.0
            hide phonetext with dissolve
            h "But I wasn't... {nw}"
            show HirokoYawn h_sleeptalk
            $ renpy.transition(longdissolve, layer="master")
            extend "{w=1.0}{cps=10}a-aaawwwwwn...{/cps}"
            play sound AudienceLaughter
            show HirokoYawn h_sleeping h_sleep
            with dissolve
            "Wow, Hiroko. You really can't help yourself, can you?"
            "And I gotta admit, you're making me even more excited for tonight if you're this goddamn suggestible."
            $persistent.hiroko_yawn_eve_unlock = True
            stop music fadeout 5.0
            scene bg street1 eve with longblink
            "Anyway, I decided I'd tormented her enough for one afternoon and started my way home as soon as school let us out."
            "It surely won't be long until Hiroko's making her way back to me."
            # "And then I can REALLY start to have fun with her..."
            scene bg k room eve with blink
            "And all I have to do is wait..."
            scene bg k kitchen eve with blink
            play music Downtown
            # "*** Going to try outlining the next parts of this story as I figure out how the hell to get to a resolution. ***"
            # "So Kyou returns home and knows he just has to wait, full of confidence that Hiroko will show up."
            play sound doorbell
            "... Hey, is that the doorbell already? It's barely been half an hour since I got home."
            scene bg k entrance eve with blink
            "I was just about to get dinner..."
            play sound dooropen
            show Hiroko uniform angry at center
            h "..." with dissolve
            ks surprised "Uh... hi?"
            "I knew she'd be back, but already?"
            play sound doorclose
            h "F-fuck it. Let's just get this shit over with."
            scene bg k room eve
            show Hiroko uniform angry at center
            with blink
            "As Hiroko angrily kicks her shoes off and stomps past me into the living room, I have to ask..."
            ks frown "What happened to tennis practice?"
            show Hiroko angry_side
            stop music fadeout 5.0
            h "\"What happened to tennis practice?\"" with dissolve
            "She mimics my voice with a sneer before glaring at me."
            h uniform_armup furious "YOU fucking happened, dickwad!" with vpunch
            queue music Measured
            "Needless to say, I'm a little confused. And pissed off."
            ks frown "What are you talking about? I told you to finish training at the club first, didn't I?"
            h uniform irritated vein "Yeah, and soon as I got out of that classroom I stopped being sleepy. Big fuckin' whoop." with dissolve
            h angry "You think anyone's gonna listen to me saying I can play? After everyone saw me all fucked-up in class?" with dissolve
            ks frown "You couldn't just ignore them? You never listen to people anyway."
            h uniform_armup angry_side "Man, fuck you. And nah, I ain't gonna worry Nozo like that." with dissolve
            h uniform frown novein "Girl was beggin' me to go home and look after myself. What was I supposed to do?" with dissolve
            ks frown "So your practice was over before it began and you came straight here."
            "... Maybe I should've considered this before triggering her over and over like I did."
            ks sigh "This wasn't part of the plan, Hiroko. Sorry about that."
            h uniform_armup angry vein "Oh you're sorry? That's great, Kyou. Really 'preciate it." with dissolve
            "But even if I did mess up, her attitude's rubbing me the wrong way."
            h angry_side "I'm gonna use your sorry to get my fuckin' time back so I can train for the biggest game of my life. You think that'll work?" with dissolve
            "It's not like I fucked her over on purpose."
            ks frown "Hiroko, come on."
            h irritated "I got a day. I got one fuckin' day left to prep and I ain't ready for it!{w=1.0} I ain't {nw}" with dissolve
            extend "READY!" with vpunch
            ks "That's enough. We can- {w=1.0}{nw}"
            h uniform sad_side novein "M-man, I can see it now. I'm gonna lose big time, 'an I'm gonna have to look Nozo in the eyes and she'll know I didn't do my best." with dissolve
            "She's not even listening to me now."
            h sleeptalk_concerned "She's throwing me this karaoke party for me right after, and I'm gonna have to go there and..." with dissolve
            h cry "I let her down. Shit, I let everybody down. I let myself down..." with dissolve
            ks "Just calm down, alright? You don't know any of that yet."
            h uniform_armup angry "Th-this's all 'cuz I let you help me! Why the fuck did I do that?!" with dissolve
            ks angry "Nah, don't blame me for all this. It was all going great until you lost your temper again, remember?"
            # ks angry "Don't blame me for all of this! I DID help you, remember? You just keep making it worse for yourself because you've still got a temper."
            ks "And it'll keep getting worse for you if you don't watch yourself."
            h furious "That a fact? You think I'm scared of your creepy ass?" with dissolve
            h "You think I give a {nw}"
            extend "FUCK anymore?" with vpunch
            "It's been a while since she made me flinch, but I realise she's serious. She really does think she's lost everything. This could be dangerous."
            "Yet despite that..."
            # h furious "{cps=15}That a fact? {w=0.5}I got nothing else left so don't you {nw}{/cps}" with dissolve
            # extend "FUCKIN' threaten me!" with vpunch
            ks frown "If... i-if you're that done with me then why did you come back here, huh? Answer me that."
            h angry "Because... u-uh..." with dissolve
            stop music fadeout 5.0
            h uniform surprised "B-because I'm s'posed to be hypnotized..." with dissolve


            # h cry_open "I-I'm gonna lose. I ain't getting that scholarship now not gonna make it. I ain't impressing nobody, I'm just  Everyone's gonna know I fucked up..."
            # h cry "I ain't getting' that scholarship
            #k I'm sorry
            #h you're sorry? Sorry ain't gonna get me my time back. I gotta train for the biggest game of my life and I... I CAN'T!

            # "I mean, I could guess. I'm sure she's mad at me for putting her to sleep in front of everyone. But even so, why did she skip tennis practice?" with dissolve
            # ks "I said you could train first, didn't I?"


            # "Hiroko's already here? What happened to tennis practice?" with dissolve
            # "As she angrily goes on to explain, Hiroko had to listen to Nozomi beg her to go home and look after herself."
            # ks "But you felt fine the moment you left the classroom to go home, right?"
            # "She sure did, and was Kyou expecting anyone to believe her after they saw her conked out in class? Because Nozomi sure didn't!"
            # "So Hiroko had no choice but to relent and skip practice to go straight home."
            # "Only... with her tennis practice effectively over she found herself walking here instead. So now she only has tomorrow to prepare and it's freaking her out."
            # "She can see it now: Crashing and burning out of the tourney, then an evening crying about her lost scholarship at karaoke with Nozomi and the others."
            # "And it'll all be thanks to this dickwad!"
            # "Kyou apologizes for making her miss practice, but tells her to watch her tone or he'll find a way to punish her."
            # show Hiroko uniform_armup furious vein
            # "An enraged Hiroko protests further and seems ready to kill, only for Kyou to remind her that she DID come here to be hypnotized, didn't she?" with dissolve
            scene cg k room eve
            show HirokoHypno upright sad_closed
            play sound sitting
            with blink
            "Gulping down her rage, Hiroko then slumps down on my couch."
            h "I gotta be ready..."
            "Mad as she is it seems Hiroko can't, or won't, argue with the logic I placed in her head."
            ks neutral "Ready to be hypnotized."
            queue music Night_Road
            "She draws a breath and nods slowly."
            show HirokoHypno concerned
            h "I still don't fuckin' get how you're doing this to me." with dissolve
            show HirokoHypno sad
            h "It really don't matter what I want, does it?" with dissolve
            h "You tell me to calm down on court, or yawn in class or some other embarrassing shit and I gotta do it no matter what."
            h "And I do it 'cuz... 'cuz you told me to? An' thassit?"
            "I mean, it's not the whole story by a long shot. Better she stay naive about it, though."
            show HirokoHypno sad_closed
            ks smile "That's it. It feels too right to do anything else in the moment." with dissolve
            ks "You came here to be hypnotized again, and that's exactly what's going to happen now. Just like I told you."
            ks "Hypnosis really is incredible isn't it?"
            show HirokoHypno concerned
            h "F-fuckin'... I'm already feeling like I need another nap just sitting here." with dissolve
            h  "The fuck is wrong with me?"
            "Man, she even absorbed my words about feeling hypnotized and sleepy around me. Like, even talking with her like this is making her space out."
            "It has me thinking I don't even need my penlight to take her all the way back into trance this time..."
            ks "Nothing's wrong, Hiroko. Being in my presence makes you sleepy. Makes you feel hypnotized."
            ks "And that's okay. Perfectly natural, in fact."
            show HirokoHypno relaxed sad
            h "It ain't... i-it ain't okay..." with dissolve
            "I lean in slowly while she talks, and her shoulders start to sag in reply."
            "She's already far away from the furious demeanor she had towards me just a couple minutes ago."
            show HirokoHypno sleep
            h "Never should've got mixed up with you... I'm so... so dumb." with dissolve
            "This tennis tournament is still eating at her, though. And yeah, it sucks that I made things a little harder for her today."
            "But I've seen her play pretty well just a few days ago. I'll bet any problems she's having are mostly in her head."
            show HirokoHypno arm_uniform sad
            h "A-ahh..." with dissolve
            "I bet I can help her with that, and still make her regret lashing out at me at the same time."
            ks smirk "You're not dumb, Hiroko. Just confused."
            h "Confused?"
            ks "You're trying to go against your instincts. Consciously trying to tell yourself that what you feel now is wrong somehow."
            ks "But it's like I keep saying, there's limits to what hypnosis can do."
            ks "No matter how deep into trance I take you, no matter how suggestible you become, your mind has a way of defending itself."
            ks "So the very fact that you're still here with me. Still listening and relaxing, still feeling so nice and sleepy and suggestible around me..."
            ks "Doesn't that tell you something, Hiroko?"
            show HirokoHypno frown
            h "Uh... uhhmmm..." with dissolve
            ks "Doesn't that suggest that deep down you realise I'm not someone you can stay mad at? That I'm not someone you need to worry about?"
            show HirokoHypno sleepy_up_open
            $ renpy.transition(longdissolve, layer="master")
            h "B-but... but I am mad at you... I am..."
            ks "On a... surface level, perhaps. But if you were that emotional about what I'm doing, then you wouldn't be feeling that deep, tempting pull to drop back into hypnosis."
            stop music fadeout 10.0
            ks "You certainly wouldn't find all the tension leaving your body as I talk. Feeling it all seep out of your fingertips and toes..."
            show HirokoHypno relaxed sleepy_up_closed
            ks "And of course, you absolutely wouldn't be dropping completely, irresistibly back into hypnosis, every muscle limp and loose and relaxed as soon as I squeeze your shoulder..." with dissolve
            ks "In three, two... {w=0.5}one...{nw}"
            show HirokoHypno drooping sleep
            $ renpy.transition(longdissolve, layer="master")
            extend ""
            queue music Flow
            "Heh. She's so goddamn impressionable. Is that really all it takes to put her under now?"
            ks "That's right, Hiroko. Dropping deep, so completely deep in trance now, letting all those unnecessary feelings fall away. Just allowing yourself to sink..."
            "It's incredible. Kinda feels like I've hacked her brain if she thinks she really has no choice but to do this stuff with me."
            "And I know I'll have to be more careful with her now because of it. I need to make sure she doesn't tank her tennis career while I'm doing these kinds of experiments."
            show HirokoHypno no_arm
            "So what to do... I still want to punish her for all her bullshit, but she still needs to be fit for that tournament..." with dissolve
            "Maybe I can find a way to do both."
            ks smile "Sinking so deep. And now that you're back in this nice, deeply relaxed and suggestible state, I want you to think about your weekend."
            ks "You know what you need to do. You need to train tomorrow, and then you need to compete for the tournament."
            ks "And you'll find that while you're doing that over the weekend, while you're training and competing you'll find yourself able to put your entire focus into those things."
            ks "All your stresses and anxieties will vanish to the back of your mind. The tournament will be your one and only concern and you will always perform to the best of your ability."
            ks "You will give nothing but your best for your tennis, Hiroko. Do you understand?"
            show HirokoHypno sleeptalk
            h "Yeah... understand..." with dissolve
            show HirokoHypno sleep
            ks smirk "That's good, Hiroko. And there's something else you need to do this weekend." with dissolve
            label Hiroko_Trickster_SealTheDeal:
                ks "When the tournament is over, and if you find you have won, you will remember that you had my help and that I fulfilled my part of our deal."
                ks "It would be only fair of you, after I helped in your victory, that you honour our deal by committing to be my assistant, wouldn't it?"
                show HirokoHypno sleeptalk
                h "Y-yeah... only fair of me..." with dissolve
                show HirokoHypno sleep
                ks "That's right. So if you find you have won your tournament you will drop all your other plans for the day to return to my house just like you did today." with dissolve
                # ks "You will immediately need to commit yourself to being my assistant, and will drop all your other plans for the day to return to my house just like you did today."
                ks "I'm going to be performing a little warm-up hypnosis show for a small audience and you will need to do your part as my assistant. Understand?"
                show HirokoHypno sleeptalk
                h "A... a warm-up show...?" with dissolve
                show HirokoHypno sleep
                "I pause a moment. I don't think she's ever responded like that before, where she didn't just acknowledge and agree to what I told her." with dissolve
                "Guess the prospect of being hypnotized before an audience really is that nerve-wracking for her. All the better to break her in gently, then."
                ks smile "That's right. You need to be comfortable about being hypnotized in front of other people. You need practice, just like you needed to practice your tennis."
                ks "And you'll be so full of confidence after your big win that this will be the best time to do it, don't you agree?"
                show HirokoHypno sleeptalk
                h "Y... yeah..." with dissolve
                show HirokoHypno sleep
                ks "Exactly. So if you win your tournament you'll be fully prepared to come here, willing to put on a show as my hypnotized assistant, won't you?" with dissolve
                show HirokoHypno sleeptalk
                h "... Yeah." with dissolve
                show HirokoHypno sleep
                ks "Very good, Hiroko. Feeling so incredibly hypnotized. Feeling so incredibly easy to hypnotize." with dissolve
                ks "So as I count up to three, you're going to awaken from this deep trance, fully alert and consciously remembering everything that was said to you."
                stop music fadeout 5.0
                ks "Waking up, nice and refreshed in one... two, and..."
                show HirokoHypno relaxed sleepy_up_closed
                $ renpy.transition(longdissolve, layer="master")
                ks "Three. Rise and shine."
                show HirokoHypno sleepy_up_open
                h "{cps=15}Mrrrrn... w-wha?{/cps}" with dissolve
                queue music Downtown
                "I watch as Hiroko breathes deeply and leans back on the couch; her large eyes taking a moment to register me staring back at her."
                h "{cps=15}W-what's going... {/cps}{w=1.0}h-{nw}"
                show HirokoHypno upright scared
                extend "HAH!" with vpunch
                "But when she does register me, she has no trouble finding her energy again."
                ks smirk "There she is. Welcome back."
                "And I gotta say, it's fun watching her reconnect the dots in her brain in real time as she thinks back to what just happened between us."
                h "G-gawd, when the fuck did you..."
                show HirokoHypno sad
                if HirokoDeal == True:
                    h "B-but we were just talking? An' the next thing I know I'm napping again..." with dissolve
                else:
                    h "W-we were just talking about it, then you put a hand on me an' the next thing I know I'm napping again..." with dissolve
                show HirokoHypno sleeptalk
                "She lets out a long, frustrated sigh." with dissolve
                h "Ain't gonna lie, that's scary as fuck if you can just put me to sleep like that. It's gettin' worse..."
                ks smile "I think you mean it's getting better."
                show HirokoHypno annoyed_up
                h "H'yeah, fuck that. I keep telling you I want out of this creepy shit, and you're..." with dissolve
                if HirokoDeal == True:
                    show HirokoHypno clenched_fists_tennis angry
                else:
                    show HirokoHypno clenched_fists angry
                h "A-and {nw}" with dissolve
                extend "FUCK, what did you do to me this time?" with vpunch
                "Heh. I was waiting for her to get up to speed. Seems she's all caught up now."
                if HirokoDeal == True:
                    ks smirk "When you got here you were all about trying to renege on our arrangement, whining about \"payback\" and all. I just made sure you understand nothing's changed."
                    ks "So you can just focus on doing your part. Give it your all at the tournament, then we can get right back to doing my thing. Sounds fair, right?"
                else:                    
                    ks smirk "When you got here tonight you'd pretty much given up. But now we both know you're going to play like a champion this weekend."
                    ks "And if you do your part, we'll both get what we want out of it. Isn't that great?"

                # "And she certainly wouldn't be feeling an inescapable pull to drop back into trance, becoming fully irresistable when he touches her forehead, would she?" with dissolve
                # "But the moment he taps her forehead and tells her to sleep she drops like a rock, and Kyou's delighted that he pulled that off without any help from the penlight." with dissolve
                # "Hiroko sure is impressionable alright, and he notes that he needs to be more careful in his experiments with her."
                # "Careful enough that what he'll do next won't take effect until after her tournament."
                # "So okay, he tells Hiroko she'll be able to put all her focus entirely on her competition this weekend."
                # "When she's training and competing she'll find she can give it her all."
                # "The kicker is if she wins the tournament she'll need to come back to his house to be his assistant for a warm-up hypnosis show."
                #Hiroko needs to be comfortable performing in front of an audience, and these cam people will have no idea who she is.

                # "The kicker is if she wins the tournament she'll immediately remember that she had the help of a powerful hypnotist to do it, and that she owes it to him to become his assistant."
                # "And a good assistant in her case is someone ready to become sleepy and entranced in Kyou's presence any time and any place where it's safe to do so."
                # "That's only fair, right? After he helps her win her scholarship, she'll be happy to honour the deal they made by assisting him, won't she?"

                # "Naturally Hiroko's in no position to argue and when she wakes, with full memory of the trance like yesterday, she'll again be upset about what just happened." with dissolve
                # "She's told him yesterday that she wanted out of this insanity and Kyou's being a massive asshole for trying to keep her attached to him."
                # "Well then, Kyou retorts, Hiroko had better not win. Maybe she can throw the final game if she feels that strongly about it, huh?"
                scene bg k room eve
                if HirokoDeal == True:
                    show Hiroko tennis_armup furious vein at center:
                        ypos 1.2
                        linear 2.0 ypos 1.0
                else:
                    show Hiroko uniform_armup furious vein at center:
                        ypos 1.2
                        linear 2.0 ypos 1.0
                with blink
                h "RRRRRRRAAAAARGH!" with shake
                show Hiroko:
                    ypos 1.0
                h irritated "WHY YOU GOTTA DO THIS TO ME?! HUH?!" with vpunch
                "No longer tethered by a compulsion to be hypnotized, Hiroko heaves herself off the couch and rages in front of me."
                "But I don't know, it seems a little half-hearted. Like she knows I might have even done her a favour here after how despondent she was."
                ks smirk "Hey, if you don't want to do my little hypno show that bad, you can always throw the last game."
                ks "Just something to think about."
                h furious "It ain't anything to think about, fuckface! How's it gonna look to everyone if I do that?" with dissolve
                if HirokoDeal == True:
                    h tennis angry_side "I just... {w=1.0}{nw}" with dissolve
                else:
                    h uniform angry_side "I just... {w=1.0}{nw}" with dissolve
                extend irritated "RRRAAAAAARRRGH!" with shake
                hide Hiroko with dissolve
                play sound dooropen
                pause 1.0
                play sound doorclose
                stop music fadeout 5.0
                "Hiroko stamps her foot as she turns and stalks out of my house, growling and raging all the while."
                ks "Good luck at the tournament!"
                # "Kyou just waves off her complaints and wishes her luck for the weekend, and Hiroko once again leaves angry and frustrated." with dissolve
                scene bg k bedroom eve with blink
                queue music Past_Sadness
                "When my excitement cools off an hour later, I wonder whether giving Hiroko a way out of continuing this was really all that smart."
                # "Back in his room, Kyou starts to wonder whether giving Hiroko an out was really all that smart."
                "Why was I so confident she could win this tourney? Is she even that good of a player?"
                "She did great against that friend of hers, sure, but what about the other schools? Don't they have better players than that?"
                "I only gave Hiroko the attitude to win, but that's only gonna count for so much."
                "How good is she really with her technique? Her strategy? Or... I dunno, whatever else a player needs?"
                "Does it matter that she's so goddamned short? How many tennis champions are there under five feet tall?"
                "Not to mention how badly I fucked up her match preparation. Shit, maybe I didn't think this through."
                "Still, though. I have to admit I'm a little excited about just how she'll behave in proper match conditions, knowing how she's taken to my hypnosis."
                # "Why was he so confident she'd win? He's seen her play Risa, but how does Hiroko stack up against the star players in the other schools?"
                # "Maybe she can keep her anger in check thanks to him, but what about her technique? Her strategy? Or the fact she's shorter than any pro tennis player he's seen?"
                # "Not to mention how badly her preparations for the thing were disrupted thanks to his meddling. Will his little bit of mental trickery make up for that?"
                "Makes me want to see the effects for myself..."
                # "(( AUTHOR'S NOTE - And that's where the current written script ends. ))"
                # "(( I've roughly outlined several more scenes if you want to read on, or you can wait for a future update~ ))"
                stop music fadeout 10.0
                jump Day7_Con_Kyou_Hiroko_Trickster
            # "He notes to himself that he should be more careful in his experiments with his impressionable subject even as he decides on what to do with her tonight."
            #convinced she does actually want to be hypnotized on some level because there's just no other way she'd be obeying such problematic suggestions.
            #After all, if you could convince people this easily the world would be a way different place, wouldn't it?

            #Remember, he just has to send a text to vibrate her phone, it doesn't have to make any sense so he just spams her every few minutes
        "Stop for now":
            "As much as I'm tempted... I'd better stop. Trying to make her conk out in class will probably attract a little too much attention."
            show Sayori uniform neutral at center, flip:
                xpos 0.25
            show Hiroko frown at center
            show Nozomi side uniform smile_side at center:
                xpos 0.75
            with dissolve
            n "Cheer up, Hiroko. It's only a few more hours."
            "Not to mention there must surely be a limit to how much she'll let me get away with, gullible or not."
            "Going as far as that feels like flying a little too close to the sun."
            # "Besides, there's nothing more to prove. Going all the way just because I can is gonna make me feel like a total asshole."
            # "Besides, there's nothing more to prove. Going all the way just because I can feels a little beyond just messing with her."
            # "I want to annoy, not destroy."
            #Starts to feel bad about pushing Hiroko as far as he is. Thinks to apologize when Hiroko comes to see him, only she apologizes first for hitting him, recognising
            #that she didn't apologize properly and that she hates getting physical with people. Kyou says he won't torment her anymore and they agree a truce...
            h frown_side "Yeah thanks, Nozo, I know how a school works." with dissolve
            # "That and it feels like I'd be going a little beyond just messing with her, I guess."
            s rolleyes "Would that you could apply that knowledge productively." with dissolve
            hide Sayori
            hide Nozomi
            h uniform_armup irritated "Whatevs. I'm just not feeling it today. Big deal!" with dissolve
            show Hiroko uniform frown
            "As the others walk to their seats, Hiroko takes a moment to stop and look my way again." with dissolve
            "I simply smile at her, while she keeps that scowl on her face as she sits down..."
            scene bg classroom day with blink
            "And while I can't see for sure, I'm getting the impression that scowl is staying on her for the entirety of our afternoon lessons."
            stop music fadeout 10.0
            scene bg classroom eve with blink
            queue music Eons
            "... Hmm, maybe I could've told her I wasn't going to mess with her again today. She's probably thinking she can't let her guard down at all."
            "Just thinking I'll strike the very moment she tries to relax so she'll let out an embarrassing loud yawn in front of the whole class."
            show phone at right with moveinright:
                ypos 0.346
            "Yeah, I'd better send her a quick, discreet text. Make sure she knows not to expect any more uh..."
            hide phone at right with moveoutright
            "Wait, no, what am I doing? I stopped myself before I hit send, but I almost forgot what I had her think."
            "Now I kinda feel like a jerk..."
            scene bg classroom eve with longblink
            play sound schoolbell
            "So eventually the bell rings out for the end of the school day; my message left unsent on my phone."
            show Nozomi side smile_side at center:
                xpos 0.75
            show Sayori neutral at center, flip:
                xpos 0.25
            show Hiroko frown_side at center, flip
            n "So I guess we'll see you on Sunday, Hiroko~" with dissolve
            show Nozomi happy with dissolve
            show Hiroko:
                linear 3.0 xpos 1.5
            n "{cps=20}All the best for... {w=0.5}{/cps}{nw}"
            show Nozomi neutral
            $ renpy.transition(dissolve, layer="master")
            extend "for the tournament?"
            show Nozomi sad_side at flip
            "Hiroko's dark expression apparently left unchanged on her face..." with dissolve
            n "Hiroko?"
            hide Hiroko
            s uniform_handup concerned "I am loathe to say it, but I fear the pressure may actually be getting to her." with dissolve
            "I have to say, I've not really seen her exhibit the quiet sort of rage before."
            # "And the concern from her friends as strong as ever."
            n sad_closed "Yeah... I'm a little worried, to tell the truth." with dissolve
            "I thought fucking with her was gonna be a bit more fun than this. But moreso, upsetting Nozomi wasn't part of the plan..." #seeing everyone so miserable is really putting a dampener on it."
            n sad_side "I'll send her a text; make sure she knows I'm there for her if she needs-" with dissolve
            hide Nozomi
            show Nozomi front2 shocked at center:
                xpos 0.75
            show Sayori surprised_right
            ks surprised "W-wait, no! Don't text her!" with dissolve
            "Fuck. I just let that fall out of my mouth without thinking."
            s concerned_right "Kyou? Is there something we can help you with?" with dissolve
            show Nozomi surprised
            "But yeah, even if she's not going to yawn anymore, getting a text from anyone right this moment seems like a really bad move." with dissolve
            ks sigh "I- I'm just saying..."
            "Not that they'd have any idea... Shit, why would they listen to anything I tell them?"
            show Sayori neutral
            n frown "You're saying if I really cared about Hiroko I'd go to her instead of wimping out with a text." with dissolve
            s uniform_handup rolleyes "You tried that just now and saw how that went. If you attempt to chase her there is no telling what her reaction would be." with dissolve
            n side sad_side "Hm, right. And she was pretty short with me all afternoon, now that I think of it..." with dissolve
            show Sayori uniform neutral
            show Nozomi sad_closed
            "Nozomi lets out an anxious-sounding sigh." with dissolve
            n sad_closed "I just want her to be okay, Sayori."
            s uniform_folded concerned "Of course you do. Perhaps when she has burned off some of that tension at the tennis court she'll be more amenable to our support?" with dissolve
            n sad_side "S-so you mean..." with dissolve
            s neutral "I will fulfill my club obligations for today, then we can go see her together. She should be winding down her tennis training by then." with dissolve
            n happy "Yeah. Yeah, that sounds like a plan~" with dissolve
            s smile "That it is." with dissolve
            hide Nozomi
            hide Sayori
            "... It kinda feels like in their discussion about what to do they forgot all about me." with dissolve
            "Well, whatever. So long as Hiroko's phone doesn't go off, that's the important thing here."
            "Now I just have to go home and wait..."
            scene bg k room eve with longblink
            "If what happened this morning was anything to go by, Hiroko will be sure to pay me a visit no matter how miserable she might be."
            "Huh... Am I really starting to feel bad for Hiroko?"
            "Like, sure, maybe things got a little out of hand but it's not like I convinced her to do anything terrible today."
            "All she did was yawn a whole bunch, so she's probably just embarrassed by what I had her do."
            "But now she's headed to tennis practice with a clear head; maybe even more refreshed than she would have been without me."
            "So yeah, Hiroko's fine. She just needs to learn a little humility so she'll start treating people with respect."
            "I'm just teaching her a little lesson, that's all..."            
            scene bg k entrance eve with longblink
            play sound doorbell
            "It takes a few hours of waiting before the doorbell rings."
            "She's not trying to kick the door down this time, so I'd say she's off to a good start."
            play sound dooropen
            show Hiroko tennis_headhold sad_side at center
            h "Hey..." with dissolve
            "Still, I think it's worth reminding her about the shitty way she acted last time she was here."
            show Hiroko neutral
            ks neutral "Hey... You gonna take them off this time?" with dissolve
            play sound doorclose
            h frown "..." with dissolve
            h tennis_headhold2 confused "H-huh?! Whaddya mean?" with dissolve
            "The flash of anger in her eyes gives way to puzzlement, then realization as she notices me pointing at her shoes."
            h tennis_armup irritated vein "'COURSE I'm taking 'em off! Fuck's sake..." with vpunch
            scene bg k room eve
            show Hiroko tennis frown at center
            with blink
            "And back to anger again, as I awkwardly watch her pull off her footwear before she follows me into the house proper."
            ks sigh "You could've left your socks on, you know."
            h tennis_armup angry vein "Gawd, get off my case! I ain't tracking shit on your floor, okay? Jesus." with dissolve
            ks frown "Yeah, not THIS time. After the way you behaved yesterday I have to wonder if you were raised by wolves."
            h furious vein "MOTHERFFFF..." with vpunch
            show Hiroko irritated
            "Hiroko cuts herself off as she starts to boil over with that all-familiar rage." with dissolve
            h angry "Look, I ain't here to fuckin' fight you, okay? I wanna talk." with dissolve
            "Yet curiously doesn't explode this time..."
            ks smirk "I thought you came here to be hypnotized."
            show Hiroko tennis_headhold2 sleeptalk noblush novein
            h "H-huuuhhh..." with dissolve
            "Hiroko nods slowly as she starts to anxiously rub the back of her head."
            h nervous_side "H'yeah, you really got me good with this hypno crap didn't ya." with dissolve
            play sound sitting
            scene cg k room eve
            show HirokoHypno tennis relaxed sleep
            with blink
            "She then unsteadily slumps down onto my couch with a groan."
            show HirokoHypno sleeptalk
            h "Didn't wanna come here for anything, but here I am. Right where you said I'd be." with dissolve
            show HirokoHypno frown
            h "Just like I've been doing everything you said I'd do all fuckin' week." with dissolve
            ks "Yes, Hiroko, you have. But it's like I told you: You're not doing all this JUST because I said you would."
            show HirokoHypno sleepy_up_closed
            ks "You might think you hate what we're doing here, but subconsciously you might actually be enjoying all of this on a deeper level." with dissolve
            show HirokoHypno upright clenched_fists_tennis angry
            h "Urgh, DON'T gimme that shit again! I KNOW all that!" with dissolve
            show HirokoHypno sleeptalk
            "She blinks sleepily, like her exertion just tired her out." with dissolve
            show HirokoHypno relaxed sad
            h "Mrrh... I dunno about liking this, but I've sure been thinking a lot about all this stuff. Can't get it outta my head." with dissolve
            show HirokoHypno sleep
            h "Like... s-sure, maybe there's a little voice inside me saying I owe you; like I deserved to let you prank me like that." with dissolve
            show HirokoHypno sad_closed
            h "Or maybe you're right... Maybe it's telling me I like this, in some real fucked-up kinda way." with dissolve
            show HirokoHypno frown
            h "But come on, it don't matter what some li'l voice in my head is saying, does it?" with dissolve
            show HirokoHypno angry
            h "'Cuz the BIG voice is more important!" with dissolve
            ks sigh "It's a pretty big voice, I'll give you that."
            show HirokoHypno upright straining
            h "H'yeah, and the big voice is saying I don't wanna do this shit anymore. Just like it's always been." with dissolve
            ks frown "And do you think that's fair, Hiroko? After all I've done for you?"
            ks "You agreed to all this when we started, remember? And I'm still holding up my end of the bargain."
            h "Y-yeah, well things change, don't they. Like how you said you wanted to do your hypno thingy at the culture fest but now you're all about this \"payback\" shit."
            "Ignoring her, I continue to press on."
            ks "By the way, how did you do on court today?"
            show HirokoHypno drowsy
            h "It's just..." with dissolve
            show HirokoHypno relaxed sleep
            "She sighs slowly, then continues." with dissolve
            show HirokoHypno neutral
            h "Like... okay, I started practice today and the second I got back on court it didn't matter how much you got under my skin." with dissolve
            h "I was totally focused on my game. Cool as ice. Like a total pro."
            show HirokoHypno sad
            h "And this new racket you got me kicks so much ass." with dissolve
            show HirokoHypno upright relaxed_fists_tennis surprised
            h "Like, it's a li'l heavier than my old one? But I got used to it real quick and I'm gettin' so much more spin on the ball like you wouldn't believe, and..." with dissolve
            show HirokoHypno relaxed sleeptalk
            h "A-anyway, you don't care about that, it's just... I ain't saying you didn't come through for me, okay?" with dissolve
            show HirokoHypno neutral
            h "You helped me out big time; I ain't denying that." with dissolve
            ks "Right. And you're not denying we had a mutual deal going either, are you?"
            show HirokoHypno sad
            h "Like I said, you kinda fucked that up when you made this about payback didn't ya." with dissolve
            ks "I made you yawn in class for a morning. So what? It's not like I did anything bad to you; just like I promised."
            show HirokoHypno sleepy_up_open
            h "Please, just... stop, okay?" with dissolve
            h "I know we gotta work somethin' out, but... just make it stop, I can't..."
            show HirokoHypno sleepy_up_closed
            ks "I still want your help, Hiroko. I still want you to be my assistant for the culture fest, and that means I need to practice my skills on you." with dissolve
            show HirokoHypno sleep
            h "{size=16}C-can't...{/size}" with dissolve
            ks "And don't you think you're overreacting? I know this has to be weird for you, but I'm asking you again: Have I really done anything to hurt you?"
            show HirokoHypno drooping sleep
            $ renpy.transition(longdissolve, layer="master")
            h "..."
            ks "... Hiroko?"
            "She's dozing off on me now? She can't be that tired after her tennis practice. And I'm sure it's nothing to do with her yawning all morning..."
            ks "Hey, are you listening to me?"
            show HirokoHypno drooping sleeptalk
            h "Mmn, yeah... listening...." with dissolve
            show HirokoHypno sleep
            "She's... hypnotized? But I wasn't even doing anything; we were just talking." with dissolve
            ks neutral "Oh... That's right."
            "I think aloud to myself as I suddenly realize what's happened here:"
            ks "You're really getting sleepy and hypnotized just from being in my presence, aren't you?"
            show HirokoHypno sleeptalk
            h "Yeah... sleepy..." with dissolve
            show HirokoHypno sleep
            ks smile "I... kinda suggested you would be when I hypnotized you yesterday, didn't I?" with dissolve
            show HirokoHypno sleeptalk
            h "Yeah..." with dissolve
            show HirokoHypno sleep
            "Even though she was arguing that I stop hypnotizing her, she still couldn't help herself from falling back into this state." with dissolve
            "She really has become so beholden to the hypnotic suggestions I placed into her head that following them has become so instinctual to her. So natural."
            "It makes me feel like I can do anything with that fascinating little mind of hers. Anything I want."
            "But after what she was saying I'm not so sure I should anymore."
            "Hiroko admitted I've been a help to her, even admitted she owes me for all the shit she's put me through."
            "She sounded almost... reasonable?"
            "So maybe it's time I stopped playing games and heard her out some more."
            menu:
                "Make sure she keeps her promise":
                    "Or maybe not. I think she's said enough."
                    "I'm not doing anything harmful to her, and by her own admission she's still getting a ton out of our little arrangement."                    
                    ks neutral "That's good, Hiroko. Just relax, follow my voice and let yourself fall deeper and deeper."
                    # "Then she's wrong."
                    "So why should we stop?"
                    ks "Deeper and deeper... Feeling so incredibly hypnotized. Feeling so incredibly easy to hypnotize."
                    ks "Now just relax and listen, because it's very important that you understand everything that I'm saying to you now."
                    "I could lay off the pranks, sure..."
                    ks "You no longer need to yawn in class when you feel your phone vibrate, nor do you need to keep it in your pocket. Those suggestions no longer affect you."
                    "... But the fact I did them is no reason to let her weasel her way out of our deal."
                    ks "But everything else I suggested to you will remain a part of your mind; a part of your behaviour you can't change."
                    "I'll keep up my end of the bargain. Don't you worry about that, Hiroko..."
                    ks "You know what you need to do. You need to train tomorrow, and then you need to compete for the tournament."
                    ks "And you'll find that while you're doing that over the weekend, while you're training and competing you'll find yourself able to put your entire focus into those things."
                    ks "All your stresses and anxieties will vanish to the back of your mind. The tournament will be your one and only concern and you will always perform to the best of your ability."
                    ks "You will give nothing but your best for your tennis, Hiroko. Do you understand?"
                    show HirokoHypno sleeptalk
                    h "Yeah... understand..." with dissolve
                    show HirokoHypno sleep
                    "But if you think you can get out of holding up your end just because I got my own back a little bit? You're wrong." with dissolve
                    ks smirk "That's good, Hiroko. And there's something else you need to do this weekend."
                    "There's so much more I want to do with that impressionable head of yours."
                    $ HirokoDeal = True
                    jump Hiroko_Trickster_SealTheDeal

                #     "Heh. She's so goddamn impressionable. Is that really all it takes to put her under now?"
                # ks "That's right, Hiroko. Dropping deep, so completely deep in trance now, letting all those unnecessary feelings fall away. Just allowing yourself to sink..."
                # "It's incredible. Kinda feels like I've hacked her brain if she thinks she really has no choice but to do this stuff with me."
                # "And I know I'll have to be more careful with her now because of it. I need to make sure she doesn't tank her tennis career while I'm doing these kinds of experiments."
                # show HirokoHypno no_arm
                # "So what to do... I still want to punish her for all her bullshit, but she still needs to be fit for that tournament..." with dissolve
                # "Maybe I can find a way to do both."
                # ks smile "Sinking so deep. And now that you're back in this nice, deeply relaxed and suggestible state, I want you to think about your weekend."
                # ks "You know what you need to do. You need to train tomorrow, and then you need to compete for the tournament."
                # ks "And you'll find that while you're doing that over the weekend, while you're training and competing you'll find yourself able to put your entire focus into those things."
                # ks "All your stresses and anxieties will vanish to the back of your mind. The tournament will be your one and only concern and you will always perform to the best of your ability."
                # ks "You will give nothing but your best for your tennis, Hiroko. Do you understand?"
                # show HirokoHypno sleeptalk
                # h "Yeah... understand..." with dissolve
                # show HirokoHypno sleep
                # ks smirk "That's good, Hiroko. And there's something else you need to do this weekend." with dissolve
                # ks "When the tournament is over, and if you find you have won, you will remember that you had my help and that I fulfilled my part of our deal."
                # ks "It would be only fair of you, after I helped in your victory, that you honour our deal by committing to be my assistant, wouldn't it?"
                # show HirokoHypno sleeptalk
                # h "Y-yeah... only fair of me..." with dissolve
                # show HirokoHypno sleep
                # ks "That's right. So if you find you have won your tournament you will drop all your other plans for the day to return to my house just like you did today." with dissolve
                # # ks "You will immediately need to commit yourself to being my assistant, and will drop all your other plans for the day to return to my house just like you did today."
                # ks "I'm going to be performing a little warm-up hypnosis show for a small audience and you will need to do your part as my assistant. Understand?"
                # show HirokoHypno sleeptalk
                # h "A... a warm-up show...?" with dissolve
                # show HirokoHypno sleep
                # "I pause a moment. I don't think she's ever responded like that before, where she didn't just acknowledge and agree to what I told her." with dissolve
                # "Guess the prospect of being hypnotized before an audience really is that nerve-wracking for her. All the better to break her in gently, then."
                # ks smile "That's right. You need to be comfortable about being hypnotized in front of other people. You need practice, just like you needed to practice your tennis."
                # ks "And you'll be so full of confidence after your big win that this will be the best time to do it, don't you agree?"
                # show HirokoHypno sleeptalk
                # h "Y... yeah..." with dissolve
                # show HirokoHypno sleep
                # ks "Exactly. So if you win your tournament you'll be fully prepared to come here, willing to put on a show as my hypnotized assistant, won't you?" with dissolve
                # show HirokoHypno sleeptalk
                # h "... Yeah." with dissolve
                # show HirokoHypno sleep
                # ks "Very good, Hiroko. Feeling so incredibly hypnotized. Feeling so incredibly easy to hypnotize." with dissolve
                # ks "So as I count up to three, you're going to awaken from this deep trance, fully alert and consciously remembering everything that was said to you."
                # stop music fadeout 5.0
                # ks "Waking up, nice and refreshed in one... two, and..."
                # show HirokoHypno relaxed sleepy_up_closed
                # $ renpy.transition(longdissolve, layer="master")
                # ks "Three. Rise and shine."
                # show HirokoHypno sleepy_up_open
                # h "{cps=15}Mrrrrn... w-wha?{/cps}" with dissolve
                # queue music Downtown
                # "I watch as Hiroko breathes deeply and leans back on the couch; her large eyes taking a moment to register me staring back at her."
                # h "{cps=15}W-what's going... {/cps}{w=1.0}h-{nw}"
                # show HirokoHypno upright scared
                # extend "HAH!" with vpunch
                # "But when she does register me, she has no trouble finding her energy again."
                # ks smirk "There she is. Welcome back."
                # "And I gotta say, it's fun watching her reconnect the dots in her brain in real time as she thinks back to what just happened between us."
                # h "G-gawd, when the fuck did you..."
                # show HirokoHypno sad
                # h "W-we were just talking about it, then you put a hand on me an' the next thing I know I'm napping again..." with dissolve
                # show HirokoHypno sleeptalk
                # "She lets out a long, frustrated sigh." with dissolve
                # h "Ain't gonna lie, that's scary as fuck if you can just put me to sleep like that. It's gettin' worse..."
                # ks smile "I think you mean it's getting better."
                # show HirokoHypno annoyed_up
                # h "H'yeah, fuck that. I keep telling you I want out of this creepy shit, and you're..." with dissolve

                # show HirokoHypno clenched_fists angry
                # h "A-and {nw}" with dissolve
                # extend "FUCK, what did you do to me this time?" with vpunch
                # "Heh. I was waiting for her to get up to speed. Seems she's all caught up now."
                # ks smirk "When you got here tonight you'd pretty much given up. But now we both know you're going to play like a champion this weekend."
                # ks "And if you do your part, we'll both get what we want out of it. Isn't that great?"

                # # "And she certainly wouldn't be feeling an inescapable pull to drop back into trance, becoming fully irresistable when he touches her forehead, would she?" with dissolve
                # # "But the moment he taps her forehead and tells her to sleep she drops like a rock, and Kyou's delighted that he pulled that off without any help from the penlight." with dissolve
                # # "Hiroko sure is impressionable alright, and he notes that he needs to be more careful in his experiments with her."
                # # "Careful enough that what he'll do next won't take effect until after her tournament."
                # # "So okay, he tells Hiroko she'll be able to put all her focus entirely on her competition this weekend."
                # # "When she's training and competing she'll find she can give it her all."
                # # "The kicker is if she wins the tournament she'll need to come back to his house to be his assistant for a warm-up hypnosis show."
                # #Hiroko needs to be comfortable performing in front of an audience, and these cam people will have no idea who she is.

                # # "The kicker is if she wins the tournament she'll immediately remember that she had the help of a powerful hypnotist to do it, and that she owes it to him to become his assistant."
                # # "And a good assistant in her case is someone ready to become sleepy and entranced in Kyou's presence any time and any place where it's safe to do so."
                # # "That's only fair, right? After he helps her win her scholarship, she'll be happy to honour the deal they made by assisting him, won't she?"

                # # "Naturally Hiroko's in no position to argue and when she wakes, with full memory of the trance like yesterday, she'll again be upset about what just happened." with dissolve
                # # "She's told him yesterday that she wanted out of this insanity and Kyou's being a massive asshole for trying to keep her attached to him."
                # # "Well then, Kyou retorts, Hiroko had better not win. Maybe she can throw the final game if she feels that strongly about it, huh?"
                # scene bg k room eve
                # show Hiroko uniform_armup furious vein at center:
                #     ypos 1.2
                #     linear 2.0 ypos 1.0
                # with blink
                # h "RRRRRRRAAAAARGH!" with shake
                # show Hiroko:
                #     ypos 1.0
                # h irritated "WHY YOU GOTTA DO THIS TO ME?! HUH?!" with vpunch
                # "No longer tethered by a compulsion to be hypnotized, Hiroko heaves herself off the couch and rages in front of me."
                # "But I don't know, it seems a little half-hearted. Like she knows I might have even done her a favour here after how despondent she was."
                # ks smirk "Hey, if you don't want to do my little hypno show that bad, you can always throw the last game."
                # ks "Just something to think about."
                # h furious "It ain't anything to think about, fuckface! How's it gonna look to everyone if I do that?" with dissolve
                # h uniform angry_side "I just... {w=1.0}{nw}" with dissolve
                # extend irritated "RRRAAAAAARRRGH!" with shake
                # hide Hiroko with dissolve
                # play sound dooropen
                # pause 1.0
                # play sound doorclose
                # stop music fadeout 5.0
                # "Hiroko stamps her foot as she turns and stalks out of my house, growling and raging all the while."
                # ks "Good luck at the tournament!"
                # # "Kyou just waves off her complaints and wishes her luck for the weekend, and Hiroko once again leaves angry and frustrated." with dissolve
                # scene bg k bedroom eve with blink
                # queue music Past_Sadness
                # "When my excitement cools off an hour later, I wonder whether giving Hiroko a way out of continuing this was really all that smart."
                # # "Back in his room, Kyou starts to wonder whether giving Hiroko an out was really all that smart."
                # "Why was I so confident she could win this tourney? Is she even that good of a player?"
                # "She did great against that friend of hers, sure, but what about the other schools? Don't they have better players than that?"
                # "I only gave Hiroko the attitude to win, but that's only gonna count for so much."
                # "How good is she really with her technique? Her strategy? Or... I dunno, whatever else a player needs?"
                # "Does it matter that she's so goddamned short? How many tennis champions are there under five feet tall?"
                # "Not to mention how badly I fucked up her match preparation. Shit, maybe I didn't think this through."
                # "Still, though. I have to admit I'm a little excited about just how she'll behave in proper match conditions, knowing how she's taken to my hypnosis."
                # # "Why was he so confident she'd win? He's seen her play Risa, but how does Hiroko stack up against the star players in the other schools?"
                # # "Maybe she can keep her anger in check thanks to him, but what about her technique? Her strategy? Or the fact she's shorter than any pro tennis player he's seen?"
                # # "Not to mention how badly her preparations for the thing were disrupted thanks to his meddling. Will his little bit of mental trickery make up for that?"
                # "Makes me want to see the effects for myself..."
                    
                    "Kyou's not doing anything harmful to her, and she admitted she's still getting a lot out of their arrangement; so why shouldn't Kyou convince her to keep her end of the bargain?"
                    "Therefore, he starts talking to her in trance to reassure her that she'll be fine and deep down she knows it. She still allowed herself to get hypnotized after all..."
                    "So she needs to commit herself to her tournament but after that she'll be back to commit herself as his assistant and let him hypnotize her as much as he wants."
                    "What happens next? Unsure, but not giving Kyou the choice to keep manipulating the \"gullible\" Hiroko seems wrong given their interaction in the written scene that came before it."
                    "Nozomi and Sayori could intervene, especially as by the weekend Hiroko would've straight up told her friends what was going on if they hadn't worked it out of her by then."
                    "So some sort of confrontation to point out how abusive he's been maybe?"
                    "I dunno, will be another big problem for later as I focus a tad more on the more ethical choice in this path~"


                    #Kyou drills into her the need to focus fully on her tournament, then right after she's won, report back to him so they can rehearse for the show
                    #He's planning to hypnotize her on camera for the chatroom he's a part of. Performing for a small audience won't be a problem for Hiroko
                    #After all, if she can perform on a tennis court in front of a crowd, performing for a few people on a webcam will be easy, right? Right...
                    #

                    "TO BE CONTINUED..."
                    jump Credits
                "Put an end to my pranks":
                    ks neutral "I want you to listen closely now, Hiroko. It's very important that you understand everything that I'm saying to you now."
                    "As much as I hate to admit, while tricking her has been fun I can't shake off the guilt I've started to feel about this."
                    ks "You don't need to yawn in class when you feel your phone vibrate, you don't need to keep it in your pocket and you don't need to feel hypnotized in my presence."
                    "Hiroko's a pain in my ass, but she's got a point. I've been too hung up about getting revenge for what she did to me."
                    ks "You don't need to come see me at my house if you don't want to. In fact, there is no need for you to follow any suggestion I have made, or will make in the future."
                    "And besides, after what went down in school today I guess I can call it even."
                    ks "Even if you're hypnotized, it doesn't mean you're compelled to act as I tell you. Any suggestions I make to you under hypnosis are just that: Suggestions."
                    ks "How you respond to my suggestions are always, without exception, entirely up to you."
                    "So that's enough. I'll set her straight about what it means to be hypnotized, and when she comes to she'll listen to me and we can both talk about this like reasonable adults."
                    ks "Do you understand what I'm telling you, Hiroko?"
                    "... I mean, she IS going to be reasonable now, right?"
                    show HirokoHypno sleeptalk
                    h "Yeah... I understand." with dissolve
                    show HirokoHypno sleep
                    ks "Good. So keeping that in mind, I'd like you to remember everything about this trance and wake up on a count of three." with dissolve
                    ks "Then we can talk about this some more, okay?"
                    show HirokoHypno sleeptalk
                    h "Okay..." with dissolve
                    show HirokoHypno sleep
                    ks "Great. Waking up on three." with dissolve
                    ks "{cps=15}One, two... {/cps}{w=1.0}{nw}"
                    show HirokoHypno relaxed sleepy_up_closed
                    $ renpy.transition(longdissolve, layer="master")
                    extend "three. Wide awake, Hiroko."
                    show HirokoHypno sleepy_up_open
                    h "Uuuhnn..." with dissolve
                    "I give her a moment for those sleepy green eyes to blink back into life, then I start to address her quietly."
                    ks "Alright, so you got hypnotized again while we were talking just now, but it's okay. You should be feeling more in control of yourself now."
                    show HirokoHypno neutral
                    ks "No more pranks, no more trying to do things with you that you're not happy with; we're just going to talk like you wanted. That alright with you?" with dissolve
                    show HirokoHypno frown
                    h "Uhh... y-yeah, 'course it's alright." with dissolve
                    "So she says, but I have to wonder with that dark expression she's wearing on her face."
                    ks confused "What's the matter now? You don't believe me?"
                    show HirokoHypno sleeptalk
                    h "No, I... fuck, I dunno it's just... like..." with dissolve
                    show HirokoHypno sad
                    h "Don'tcha think it's weird that you gotta tell me not to do this shit? I can't do it by myself?" with dissolve
                    ks frown "Uh... well, I mean..."
                    "I do what she wants and she's still on my case about this?"
                    show HirokoHypno drowsy
                    h "Why's it that I still gotta do what you say every time you pull out that dumb light?" with dissolve
                    "And here I thought we could move past that."
                    show HirokoHypno upright clenched_fists_tennis frown
                    h "Why ain't it up to ME?" with dissolve
                    "What am I even supposed to say at this point?"
                    ks "Christ, Hiroko, it IS up to you! It always has been, how do you still not get it?"
                    scene bg k room eve
                    show Hiroko tennis_headhold2 irritated at center:
                        ypos 1.2
                        linear 2.0 ypos 1.0
                    with blink
                    h "RRRRRGH!"
                    "Maybe I set the bar too high thinking she might be reasonable about any of this after I \"freed\" her..."
                    show Hiroko tennis_armup:
                        ypos 1.0
                    h "You still don't... LISTEN to what I'm telling you, dude!" with dissolve
                    h rolleyes "And here I thought you were gonna be reasonable about this." with dissolve
                    ks frown "Hey, that's MY line! You're the one who hasn't been listening properly."
                    show Hiroko frown
                    ks "Hell, the only reason I tricked you in the first place was because you thought you couldn't resist my hypnosis, even after I kept telling you-" with dissolve
                    h tennis_headhold2 furious "{cps=20}Yeah, yeah, it's all 'bout my subconscious and keeping an open mind and blahblahblah- {/cps}{nw}" with dissolve
                    extend "FUCK you!" with vpunch
                    ks angry "God, you're so immature! {w=0.5}{cps=18}Why do I even bother-{/cps}{nw}"
                    h tennis_armup "No, shut up! My head ain't been clearer since we started this weird shit an' you ain't gonna talk over me this time!" with dissolve
                    h tennis "{cps=20}So you sit your punk ass down and goddamn {/cps}{nw}" with dissolve
                    extend "{size=30}LISSEN TO ME!{/size}" with vpunch
                    "Ugh, and with the volume too? I can only turn away from her and pinch my forehead; this is really giving me a regret-induced headache."
                    h tennis_headhold2 frown "Tch. Turn yer back if you want. I've been telling you shit's wrong this whole time, but you fuckin' plowed on through anyway!" with dissolve
                    h irritated "I kept telling you to stop tickling me, but you hadta keep going and going..." with dissolve
                    ks frown "..."
                    h angry "What, you ain't gonna bring it up again? Fine, then I'm gonna." with dissolve
                    h frown "I'm sorry I punched you in the face." with dissolve
                    h frown_side "I know you think it's cuz' I hate you, and I do. But it was just a reflex thing; you didn't give me a choice." with dissolve
                    h sad_side "It was so freaky what you were doing wasn't it? I ain't ever laughed like that, and all you had to do was tickle my hand a li'l bit?" with dissolve
                    h tennis_headhold "I didn't get how that could happen. Didn't get it at all." with dissolve
                    h sad "All I knew was I needed you to stop, and you didn't... you didn't stop." with dissolve
                    ks neutral "..."
                    h nervous "What else was I supposed to do?" with dissolve
                    "With a sigh, I turn back around to be met with... with the kind of sincere expression I've never seen on her face before."
                    ks sigh "It's... it was just tickling, Hiroko. You didn't need to worry about it."
                    h furious "Y-YOU didn't need to worry about it! That's why you went too fuckin' far!" with dissolve
                    h confused "I couldn't breathe, but you didn't care, did you? You were too busy having fun \"just tickling\" me." with dissolve
                    h pain "That's why you let me get tortured all day until I was kicking your damn door! You didn't care!" with dissolve
                    ks frown "You didn't need to kick it."
                    h confused "Didn't I? How else were you gonna hear me out?" with dissolve
                    h tennis frown "Every time you've done this shit, I've had to beg and plead an' just, like... hope you'll stop because you dunno when to stop." with dissolve
                    h sleeptalk "And... an' that's the problem with you, ain't it." with dissolve
                    h nervous "You dunno when to stop..." with dissolve
                    "Man. There sure is a part of me that wants to push back on that. Like she's any better about knowing when to quit."
                    "All the times she's given me shit and never backed off. The screaming match she had with her tennis partner that drove her away..."
                    "... But nothing good's going to come from bringing that up now, is there?"
                    ks sad "I guess I don't. And I'm sorry for that."
                    ks "But I still don't get it. Everything I read about hypnosis said that a subject always had the ability to reject any suggestion made to them, no matter how deep they were."
                    ks "It shouldn't have mattered much if I was messing with you or not. Hypnosis isn't some dark art or anything like that."
                    h tennis_headhold sleeptalk "Well... maybe you didn't read enough, huh." with dissolve
                    ks sigh "I really was too into getting my own back to think about what all this was doing to you."
                    h sad_side "Yeah... that about sums it up, don't it." with dissolve
                    "So we stand there, silently, as a question unspoken looms between us."                    
                    "\"What happens now?\""
                    show Hiroko sleeptalk
                    "But eventually, Hiroko lets out a sigh before looking to me once more." with dissolve
                    h tennis neutral "Look, I gotta get out of here. Still got a tourney to win." with dissolve
                    h sleep "We'll... we'll pick this up later. Okay?" with dissolve
                    ks neutral "... Sure."
                    stop music fadeout 5.0
                    scene bg blackscreen with longdissolve
                    "So I see her out, and I'm left thinking about everything that's gone on between us."                    
                    scene bg k bedroom eve with longdissolve
                    queue music Past_Sadness
                    "It might have been fun to mess with her the way I did, but... I know I pushed her too far."
                    "But why was it so... so easy? My first time hypnotizing someone, and it felt like I could convince her of anything."
                    show penlight at right with moveinright:
                        ypos 0.346
                    "And all it took was a few words and this thing? Maybe Hiroko was right."
                    "Maybe I didn't read enough."
                    hide penlight at right with moveoutright
                    "Still. Even with all that, she wants to talk to me again. At least, if I haven't fucked up her chances at that tournament."
                    "I have no idea how she'll do over there. All that mental conditioning I gave her; was that all for nothing now?"
                    "... I should go to see her, at the tournament."
                    stop music fadeout 5.0
                    scene bg blackscreen with longdissolve
                    "I'll find out for myself..."
                    pause 2.0
                    jump Day7_Con_Kyou_Hiroko_Trickster2
                    #Hiroko's mad that Kyou trivialised her discomfort, and also "It's not just tickling", since she can cite more examples of him plowing through and disregarding her discomfort other times
                    #He stops, but she has to beg and plead before he reconsiders. That's a terrible basis for any kind of relationship isn't it?

                    # ks neutral "..."
                    # h "When someone tells you to stop, you fuckin' stop!"
                    # Kyou confesses he took advantage of Hiroko's naivety about hypnosis to prank her, but Hiroko's not convinced that's the whole story


                    # h "You really don't think that's weird as shit? You weren't even trying to fuck with me just now were you?"
                    # h "I wanted to talk, an' don't tell me my lil' voice wanted to take a nap. I just spaced the fuck out
                    # h "Nozo and Sayori were talking to me after my practice run just now. They're really worried about me, y'know?"
                    # "(( AUTHOR'S NOTE: Alright that's where I have to leave this for now. I'll work on this some more in the next update, where I hope to finish this and the remaining scenes. ))"
                    # " (( A short outline follows. This is the stuff I laid down the last time I left it years ago, so there'll likely be some changes when I actually write it. ))"
                    # "Maybe Kyou feels like he shouldn't need to say it again but, well, he DID take advantage of Hiroko's perceived gullibility to string her along like this. And he knows it."
                    # "So with a little guilt in his heart, he talks to her while she's entranced to reassure her that she truly does not have to follow any suggestion he makes that she doesn't want to."
                    # "She must always be aware that it's always her choice above all."
                    # show HirokoHypno relaxed sleepy_up_closed
                    # "He then wakes her and says sorry for pushing her as far as he has." with dissolve
                    # "Hiroko, looking a bit more alert than before, says she needs to go home now."
                    # "But before she leaves, she says she was sincere about \"working something out\" with him..."
                    # scene bg court eve with blink
                    # "Fast forward to the day of the tennis tournament."
                    # "We see Hiroko playing in the final. It's a scrappy game, with Hiroko losing discipline a few times and she eventually loses the match in a tense tie break."
                    # show Hiroko tennis sad at center:
                    #     xpos 0.4
                    # show Nozomi casual side sad_side at center:
                    #     xpos 0.65
                    # show Sayori casual concerned at center:
                    #     xpos 0.85
                    # show Risa tennis concerned_side at center, flip:
                    #     xpos 0.2
                    # with dissolve
                    # "As she steps off the court, Hiroko is consoled by her friends who tell her that she's surely won her scholarship with that kind of performance."
                    # "Hiroko's frustrated about her unforced errors during the game, but she agrees that she must have played her way into a sports college at least."
                    # "Meanwhile, Kyou's thinking about what he saw just now, musing that the fact she lost focus several times means she's rejected the suggestions he gave her."
                    # show Hiroko frown
                    # "Hiroko then notices Kyou watching and growls at him to stop loitering and come join them." with dissolve
                    # show Nozomi surprised_side
                    # show Risa neutral
                    # show Sayori casual_handup neutral_right
                    # show Hiroko nervous
                    # "Then, with a little reluctance, she thanks him in front of everyone for helping her prep for today, which surprises Nozomi and intrigues Sayori." with dissolve
                    # show Risa smile
                    # "Risa is a lot less shocked, seeing how she called it before that the two were involved." with dissolve
                    # "Anyway, Hiroko also brings up Kyou's plan to do a hypnosis show for the culture fest, to even greater surprise all round!"
                    # "Kyou in particular, but given Hiroko for all people has just vouched for him, no one seems particularly weirded out."
                    # show Nozomi front2 surprised
                    # "Some might even be curious..." with dissolve
                    # "Anyway, Kyou hesitantly starts to introduce his ideas as he thinks this is Hiroko's idea of working things out. She's assisting him after all!"
                    # scene bg blackscreen with dissolve
                    # "... Uhh, the end?"
                    # "Okay, so I've been wrestling with this part of the game for far too long, especially considering it's a branch path that surely no one truly cares about."
                    # "But it sort of needs to be done to give weight to Kyou's decision to continue tormenting poor Hiroko in the main Gullible story."
                    # "Who knew writing a multiple-choice story where your decision matter would lead to such headaces as this? ^^;"
                    # "Anyway, so we have a tentative ending of sorts for this branch of the story, and that's progress I'm going to take for now."
                    # "Are there problems with it? Tons..."
                    # "Like the fact this a much nicer ending than the other path where Kyou relents on helping Hiroko instead of going ahead with manipulating her?"
                    # "There's some logic to that, as Hiroko has time to cool off and digest things, but still..."
                    # "Plus we actually see Hiroko succeed in her goal, whether because of or in spite of Kyou."
                    # "There's also how the whole deal with the penlight isn't dealt with in ANY way here."
                    # "Is Kyou going to use the penlight again? Seems pretty likely, huh!"
                    # "And is Hiroko REALLY all that comfortable vouching for Kyou just because he let up on her a bit? Maybe that whole penlight business needs resolving first after all."
                    # "Oh, and not to mention how cruel it is for the author to tease that two or more of these people are going to join Kyou for consensual hypno fun, in a VN about hypno..."
                    # "... and then GOING TO CREDITS?!"
                    # "So yeah, what I hoped was going to be a routine, quick ending for a branch path no one cares about could end up being another monster side story. Joy."
                    # "Anyway, I'll leave it there. Thanks for reading and I'll see you all soon with more updates!"
                    # jump Credits
            # "This girl was pleading with me not to hypnotize her again, even as she fluttered her eyes and dropped into trance in front of me, just from talking to me."
            # # h "I'm like, so fucking confused right now."
            #
            #
            # h "But, like... that's enough, yeah? I gave you some shit, you gave some back. We're even."
            #
            # h "You don't like me calling you creepy. Like, okay, I get it."
            # h "But if you really ain't, you'll stop."
            #
            #
            #
            # h "So, like... we're good now, right?"
            # ks "Good? What do you mean by that?"
            # "Hiroko sighs through her nose before slowly opening her eyes to look at me."
            # show HirokoHypno neutral
            # h "I mean... I was thinking about how you said none of this shit works on me unless I let it." with dissolve
            # "Well, if she wants to talk about hypnosis I guess I can wait before I try putting her under again."
            # ks neutral "Right. You might think you hate what we're doing here, Hiroko, but subconsciously you might actually be enjoying all of this on a deeper level."
            # show HirokoHypno angry_up
            # h "H'yeah, I dunno about \"enjoying\" this shit, but I GUESS there's something there." with dissolve
            # show HirokoHypno annoyed_up
            # h "'Cuz you said you wanted \"payback\", and maybe there was something in me that said I owed you; said I deserved to let you prank me like that." with dissolve
            # ks "Huh. But you do accept that this is something your subconscious accepts, right?"
            # show HirokoHypno sleep
            # "Hiroko lets out a little groan as she nods quietly, and takes her time before speaking again." with dissolve
            # show HirokoHypno sleeptalk
            # h "It's just..." with dissolve
            # show HirokoHypno neutral
            # h "Like... I started practice today and the second I got back on court it didn't matter how much you got under my skin." with dissolve
            # h "I was totally focused on my game. Cool as ice. Like a total pro."
            # show HirokoHypno sad
            # h "And this new racket you got me kicks so much ass." with dissolve
            # show HirokoHypno upright relaxed_fists_tennis surprised
            # h "Like, it's a li'l heavier than my old one? But I got used to it real quick and I'm gettin' so much more spin on the ball like you wouldn't believe, and..." with dissolve
            # show HirokoHypno relaxed sleeptalk
            # h "A-anyway, you don't care about that... But like, you really did help me out here, is what I'm saying." with dissolve
            # show HirokoHypno sad
            #
            #
            # h "And it don't matter what you did before. Yeah, I thought you were full of shit, but you really came through for me..."
            #
            #
            # h "And I never thanked you for it, 'cuz... I kept telling myself YOU owed ME for all the shit you did before." with dissolve
            # h "So... like, fuck, I ain't keeping score here; you've been a butt to me, I've been a butt to you."
            # h "I just want this shit to stop. Okay?"
            #
            #
            # h "Uh yeah, so I started practice today and the second I got back on court it didn't matter how much you got under my skin." with dissolve
            #
            #
            #
            #
            # "I find myself nodding along with her justification."
            # ks "Yeah. After all the crap you got away with I guess you were feeling pretty guilty about it all deep down, huh?"
            # show HirokoHypno sleepy_up_open
            # h "Ehhh..." with dissolve
            # ks "You must have realised how ungrateful you were being, after all I did to help you this week and all the thanks I got was a punch in the face."
            # "Hiroko seems to take a moment to process what I just said, and her eyelids seem to quiver unsteadily while she turns things over."
            # show HirokoHypno sleepy_up_closed
            # h "Uh... s-sure, but..." with dissolve
            # "She seems unsure of herself. All the more reason to lay it all on her."
            # ks frown "Not to mention all the shit from before. All the bullying... everyone thinks I'm a creep because of you, and you know it."
            # show HirokoHypno sleep
            # h "Th-that's not... mmn, not..." with dissolve
            # ks "It must have been weighing on your mind on some level. That's why..."
            # show HirokoHypno drooping sleep
            # $ renpy.transition(longdissolve, layer="master")
            # ks "Hey, are you listening to me?"
            # show HirokoHypno drooping sleeptalk
            # h "Mmn, yeah... listening...." with dissolve
            # show HirokoHypno sleep
            # "Hiroko's eyes stay stubbornly closed as her head starts to droop, just as it had been threatening to since we started this conversation." with dissolve
            # "Yeah, she's looked tired since we started talking. But was she really that worn out after her tennis practice or..."
            # ks "Oh... That's right."
            # "I think aloud to myself as I realize what's happened here:"
            # ks "You're really getting sleepy and hypnotized just being in my presence, aren't you?"
            # show HirokoHypno sleeptalk
            # h "Yeah... sleepy..." with dissolve
            # show HirokoHypno sleep
            # ks "I... kinda suggested you would be when I hypnotized you yesterday, didn't I?" with dissolve
            # show HirokoHypno sleeptalk
            # h "Yeah..." with dissolve
            # show HirokoHypno sleep
            # "I wasn't even trying anything this time." with dissolve
            # "It's just that she's become so beholden to the hypnotic suggestions I placed into her head that following them has become so instinctual to her. So natural."
            # "Hiroko really does have an interesting mind, I'll give her that. But moreso, it felt like I was truly getting through to her."
            # ks "Alright, Hiroko. You know how easy you are to hypnotize, but you no longer need to feel sleepy and hypnotized just from being in my presence anymore."
            # ks "So from now on you'll only find it possible to be hypnotized by me when I specifically tell you I'm hypnotizing you. Okay?"
            # show HirokoHypno sleeptalk
            # h "Y-yeah, okay..." with dissolve
            # show HirokoHypno sleep
            # "Satisfied, I then bring a hand up beside Hiroko's ear..." with dissolve
            # "I want to finish our conversation the way we started."
            # ks "{cps=20}That's good, Hiroko. Waking up in one, two, {/cps}{w=0.5}{nw}"
            # play sound fingersnap
            # show HirokoHypno relaxed sleepy_up_open
            # $ renpy.transition(dissolve, layer="master")
            # extend "three."
            # play sound [fingersnap, fingersnap, fingersnap]
            # show HirokoHypno upright surprised
            # ks "Wake up, Hiroko. Wide awake; you want to talk to me, remember?" with dissolve
            # h "H-huh? {w=1.0}{nw}"
            # show HirokoHypno frown
            # $ renpy.transition(dissolve, layer="master")
            # extend "Oh... y-yeah, I wanna talk to you!"
            # "With a grunt, Hiroko rights herself on my couch as at least some of her usual energy comes back to her."
            # show HirokoHypno sleeptalk blush
            # h "B-but man, it really is some scary shit that you can do that to me." with dissolve
            # ks "Just remember, Hiroko, I can't hypnotize you to do anything that you seriously don't want me to."
            # show HirokoHypno angry
            # h "Yeah, yeah, I KNOW! I'm just saying, that's how I feel about it." with dissolve
            # # h "But yeah,
            #
            # ks sigh "And here I was thinking we were moving past the \"creep\" shit."
            # show HirokoHypno sad
            # h "But it IS, though!" with dissolve
            # h "Like, don't try an' deny it,"
            #
            #
            #
            # h "I don't owe you SHIT!"
            # h "'Least I didn't, anyway..."
            # h "You an' me, we'll hash this out, okay? I promise."
            # #Kyou recalls that after he helped her focus she DID return to him of her own free will and told him how she helped
            #
            #
            # h "That ain't it. You really are creepy, dude."
            #
            #
            # show HirokoHypno sad
            # h "I never meant to punch you, dude. Was just a reflex thing 'cuz you tickled me so bad. You get that, right?" with dissolve
            # show HirokoHypno sleeptalk
            # h "An' the other stuff..."
            #
            #
            #
            #
            #
            #
            # h "So, like... you said it don't work unless I let it, right?"
            # "Well, if she wants to talk about hypnosis I guess I can wait before I try putting her under again."
            # show HirokoHypno neutral
            # ks neutral "Yeah. You might think you hate what we're doing here, Hiroko, but subconsciously you might actually be enjoying all of this on a deeper level." with dissolve
            # "Hiroko seems to take a moment to process what I just said, and her eyelids seem to quiver unsteadily while she turns things over..."
            # show HirokoHypno sad
            # h "'Kay. Well, I was thinking about that all day. Like, a lot." with dissolve
            # h "And I dunno if there's a part of me that \"enjoys\" this shit, but maybe there really is a part of me that let you prank me like that."
            # show HirokoHypno sleep
            # h "A part of me that thinks I deserve it." with dissolve
            # # h "And I didn't wanna admit it, but... maybe there IS a part of me that wants it. I guess."
            # "I find myself leaning in a little as she speaks. This is interesting to hear coming from her..."
            # h "..."
            # ks "Hiroko?"
            # show HirokoHypno sleepy_up_closed
            # "There's a tired sigh as her eyelids pull themselves open again." with dissolve
            # show HirokoHypno sleepy_up_open
            # h "Uh yeah, so I started practice today and the second I got back on court it didn't matter how much you got under my skin." with dissolve
            # h "I was totally focused on my game. Cool as ice. Like a total pro."
            # show HirokoHypno sad
            # h "And this new racket you got me kicks so much ass." with dissolve
            # show HirokoHypno upright relaxed_fists_tennis surprised
            # h "Like, it's a li'l heavier than my old one? But I got used to it real quick and I'm gettin' so much more spin on the ball like you wouldn't believe, and..." with dissolve
            # show HirokoHypno relaxed sleeptalk
            # h "A-anyway, you don't care about that... But like, you really did help me out here, is what I'm saying." with dissolve
            # show HirokoHypno sad
            # h "And I never thanked you for it, 'cuz... I kept telling myself you owed me for all the shit you did before." with dissolve
            # "Yeah, that's right. I even remember her telling me that..."
            # "\"It's the LEAST you can do for being such a creep.\"" #Short flashback scene?
            # show HirokoHypno sleepy_up_open
            # h "So, like... I dunno. I guess I feel a li'l guilty about that." with dissolve
            # ks frown "Yeah? You sure you're not guilty about the way you've been treating me until now?"
            # show HirokoHypno sleepy_up_closed
            # h "You... mmmn..." with dissolve
            # ks "Yeah. You think about that, Hiroko. What did I actually DO to you? Can you answer me that?"
            # show HirokoHypno sleepy_up_open
            # h "Mrgh... y-yeah, you... you..." with dissolve
            # ks "What's the matter? Trying to come up with an excuse?"
            # ks "Well I'm sorry my existence bothered you so much, Hiroko. But you can't behave like that anymore, you understand?"
            # show HirokoHypno sleep
            # ks "Like, you have any idea how hurtful you've been? You can't just scream that some guy's a creep because you don't like him." with dissolve
            # ks "Because I never did anything to hurt you or anyone else. Did I, Hiroko?"
            # show HirokoHypno sleepy_up_open
            # h "Mrrh... n-nah not like... hurt, just..." with dissolve
            # show HirokoHypno sleeptalk
            # h "Uhh, just..." with dissolve
            # ks "So yeah, maybe your subconscious DOES think you deserve to be messed with. And that's cause for some self-reflection, don't you think?"
            # ks "Aren't you at least a little sorry for all that childish bullying?"
            # show HirokoHypno drooping sleeptalk
            # $ renpy.transition(longdissolve, layer="master")
            # h "Mmrrrh..."
            # show HirokoHypno sleep
            # "Hiroko's eyes flutter closed as her head starts to droop, just as it had been threatening to since we started this conversation." with dissolve
            # "Yeah, she's looked tired since we started talking. Was she really that worn out after her tennis practice or..."
            # ks "Oh... That's right."
            # "I think aloud to myself as I realize what's happened here:"
            # ks "You're really getting sleepy and hypnotized just being in my presence, aren't you?"
            # show HirokoHypno sleeptalk
            # h "Yeah... sleepy..." with dissolve
            # show HirokoHypno sleep
            # ks "I... kinda suggested you would be when I hypnotized you yesterday, didn't I?" with dissolve
            # show HirokoHypno sleeptalk
            # h "Yeah..." with dissolve
            # show HirokoHypno sleep
            # "I wasn't even trying anything this time." with dissolve
            # "It's just that she's become so beholden to the hypnotic suggestions I placed into her head that following them has become so instinctual to her. So natural."
            # "Hiroko really does have an interesting mind, I'll give her that. But moreso, it felt like I was truly getting through to her."
            # "Bringing a hand up beside Hiroko's ear, I start loudly snapping my fingers."
            # "I want to finish our conversation the way we started."
            # play sound [fingersnap, fingersnap, fingersnap]
            # show HirokoHypno relaxed surprised
            # ks "Wake up, Hiroko. Wide awake; you want to talk to me, remember?" with dissolve
            # h "H-huh? {w=1.0}{nw}"
            # show HirokoHypno frown
            # $ renpy.transition(dissolve, layer="master")
            # extend "Oh... y-yeah, I wanna talk to you!"
            # "With a grunt, Hiroko rights herself on my couch as at least some of her usual energy comes back to her."
            # show HirokoHypno angry
            # # h "'Cuz, like... DUDE, even if you did help me out you don't got the right to be such a fucking dickhead!" with dissolve
            # h "You wanna talk about the shit you did? Let's fucking talk!"
            #
            # #She has to mention how his lurking near her and her friends all the time made her not just uncomfortable, but a bit scared too.
            # #He didn't do anything? That's technically true, but the threat was always there because of his behaviour
            # #Well then, why did she have to be such a bitch about it? She could've straightened things out.
            # #But it's not her problem. Nobody owes Kyou their time; the fact that she wanted him out of her space shoud've been enough.
            # #She's just not so sure now, though. Back when he met her on the courts, he did something he'd never done before: He actually put himself out there and told her
            # #what he was about and what he wanted. So now... maybe all this has made her think they can hash things out.
            # #Ugggh, think I'm still spinning my wheels here. The fact this whole scenario feels a bit creepy probably also needs a mention.
            #
            #
            # h "Like... where the fuck do you get off, talking like that?"
            #
            # h "Like, where the fuck do you get off? You seriously think you ain't done shit worth calling out?"
            # h "I ain't guilty about calling you creepy so don't give me that shit."
            # # ks frown "Yeah? Why did you think I owed you, Hiroko? What shit did I ever do to you?"
            # # show HirokoHypno sleepy_up_closed
            # # h "You... mmmn..." with dissolve
            # # ks "What's the matter? Trying to come up with an excuse?"
            # # ks "Well I'm sorry my existence bothered you so much, Hiroko. But you can't behave like that anymore, you understand?"
            # # show HirokoHypno sleep
            # # ks "Like, you have any idea how hurtful you've been? You can't just scream that some guy's a creep because you don't like him." with dissolve
            # # ks "Because I never did anything to hurt you or anyone else. Did I, Hiroko?"
            # # show HirokoHypno sleepy_up_open
            # # h "Mrrh... n-nah not really hurt, but..." with dissolve
            # # ks "So yeah, maybe your subconscious DOES think you deserve to be messed with. And that's cause for some self-reflection, don't you think?"
            # # ks "Aren't you at least a little sorry for all that childish bullying?"
            # # show HirokoHypno drooping sleeptalk
            # # $ renpy.transition(longdissolve, layer="master")
            # # h "Mmrrrh..."
            # # show HirokoHypno sleep
            # # "Hiroko's eyes flutter closed as her head starts to droop, just as it had been threatening to since we started this conversation." with dissolve
            # # "Yeah, she's looked tired since we started talking. Was she really that worn out after her tennis practice or..."
            # # ks "Oh... That's right."
            # # ks "You're really getting sleepy and hypnotized just being in my presence, aren't you?"
            # # show HirokoHypno sleeptalk
            # # h "Yeah... sleepy..." with dissolve
            # # show HirokoHypno sleep
            # # ks "I... kinda suggested you would be when I hypnotized you yesterday, didn't I?" with dissolve
            # # show HirokoHypno sleeptalk
            # # h "Yeah..." with dissolve
            # # show HirokoHypno sleep
            # # "I wasn't even trying anything this time." with dissolve
            # # "It's just that she's become so beholden to the hypnotic suggestions I placed into her head that following them has become so instinctual to her. So natural."
            # # "Hiroko really does have an interesting mind, I'll give her that. But moreso, it felt like I was truly getting through to her."
            # # "Bringing a hand up beside Hiroko's ear, I start loudly snapping my fingers."
            # # "I want to finish our conversation the way we started."
            # # play sound [fingersnap, fingersnap, fingersnap]
            # # show HirokoHypno relaxed surprised
            # # ks "Wake up, Hiroko. Wide awake; you want to talk to me, remember?" with dissolve
            # # h "H-huh? {w=1.0}{nw}"
            # # show HirokoHypno frown
            # # $ renpy.transition(dissolve, layer="master")
            # # extend "Oh... y-yeah, I wanna talk to you!"
            # "AUTHOR'S NOTE: Okay, that's as far as I can go for now. This early access release is late enough as it is and I'm once again out of time ^^;"
            # "So, I've been trying a lot of approaches for this interaction to try and distinguish it from the other Kyou vs Hiroko stuff in the game."
            # "The two having some kind of open, honest, vaguely equal conversation about their history..."
            # "... instead of a more explosive revelation or Kyou breaking Hiroko's mind would serve that purpose."
            # "But yeah, it's been another puzzler to get right and I still have a lot to do here."
            # "Anyway, I hope you've enjoyed what I have so far and I'll see you next time with more developments!"
            # "TO BE CONTINUED..."
            jump Credits

            # ks "Yes you were. I want you to finish what you were saying."
            # right, I said you're creepy."
            # h "Heh... what the fuck is this?"
            # h "All this is 'cuz I hurt your li'l fee fees?"
            # ks sigh "I can put you back to sleep, you know."

            # ks frown "Yeah. That was always bullshit, wasn't it, Hiroko?"
            # ks "You know I didn't do a damn thing to you. But you sure got off on making out I was some kind of creep to the whole school. Man, you never shut up about it."
            # ks "Even this whole week while I was helping you, you never shut up about that. You don't think you deserve this because of that?"
            #Hiroko argues back, but sleepily, remarking she feels like she's back in class. Kyou realizes she's falling under his hypnotic suggestion just by his talking to her
            #Kyou is moved enough to snap his fingers repeatedly and order her to wake up instead of letting her fall back into trance

            # h "I ain't even done."
            # "She sighs."
            # h "Maybe there's also a part of me that feels bad about what went down between us since we met."
            # h "An' that's why I let you prank me like that."
            #
            # h "Like... I guess you didn't do anything super bad back then. You were just super annoying. And a lil' scary."
            # ks "Scary?"
            # h "Dude, you barely said shit to us. We didn't know what you were gonna do. Just nothing good, that's all."
            # h "We just wanted you to leave us alone."
            # ks "You could've tried talking to me instead of screaming at me? You ever think of that?"
            # h "Why the fuck did I have to? We didn't owe you shit, Kyou. Don't you get that?"
            # h "... Not 'till now, anyway."





            # "Seems she still has some way to go before she's learned her lesson."
            # ks smirk "Well, can you blame me? Don't get so mad when you're the one at fault."
            # show Hiroko angry
            # ks "And besides, aren't you supposed to be ready to become hypnotized by now?" with dissolve
            # show Hiroko surprised novein
            # "Yeah. I can see the rage start to fizzle out in her eyes as I remind her of the last suggestion I put into that impressionable head of hers." with dissolve
            # # "And as I brace myself for the inevitable explosion..." with dissolve
            # # "It'll only make it better when I take you back in trance again, just like you know I will." with dissolve
            # show Hiroko tennis_headhold2 sleeptalk noblush
            # h "H-hmmm..." with dissolve
            # "And with a sigh, she nods slowly as she starts to sheepishly rub the back of her head."
            # h nervous_side "H'yeah, you really did a number on me with that hypno crap didn't ya." with dissolve
            # scene cg k room eve
            # show HirokoHypno tennis relaxed sleep
            # with blink
            # "And with that, she stumbles down onto the couch with a groan."
            # h "Kinda wanted to talk about it before you put me to sleep again..."
            #
            #
            # h "Y'know, Nozo was waiting for me when I finished up at the courts today. Sayori too."
            # h "They obviously think I'm all cut up about tennis shit, but we know better, don't we."
            # h "So now I'm back here and I'm like... shit, why didn't I tell 'em about any of this?"
            #
            # h "I almost told 'em about us. Like, they think I'm going through some really heavy shit, and I am. But it's all 'cuz of you."
            # ks "Why didn't you?"
            #
            #
            # h "Anything you say, I gotta do. But I'm only doing it 'cause some part of me WANTS to do this shit for you."
            #
            # h "It's like you've been in my head all the fucking time. All day and night."
            #
            # h "I guess that's why you did it, huh. Bought me shit and said you'd help me so you could get in my head. "





            # "I find myself having tensed up for nothing as it never arrives." with dissolve
            # "And yet, I find myself having tense up for nothing as Hiroko manages to calm herself."
            # "Is this because she has to \"be ready to become hypnotized by me\"? That's something else I put in her head after all..."
            # h nervous_side "H'yeah. I gotta make up for yesterday, don't I." with dissolve
            # show Hiroko:
            #     linear 1.5 ypos 1.3
            # "I then watch as she sinks down to her knees in front of me and plants her hands down on the floor, bowing her head."
            # show Hiroko tennis:
            #     ypos 1.3
            # "Wait, is she actually going to...?" with dissolve
            # h sleeptalk "Hey, sorry buddy. Yesterday was kinda shit for me, but you didn't deserve me lashing out at you like that." with dissolve
            # h sleep "So I ain't gonna do it again, I promise." with dissolve
            # "Like, I wanted to humble her, but seeing her like this is a bit much."
            # "I'm... not sure how to react."
            # ks frown blush "{cps=20}Uh... s-sure? Just don't- {/cps}{w=1.0}{nw}"
            # h tennis_armup angry vein "Dude, shut the fuck up! In the middle of something here." with dissolve
            # "She just scoffed at me? Then she bows her head again as if nothing happened."
            # h tennis sleeptalk novein "I'm sorry for him too. I know it's gotta be a tough break having this guy inside you." with dissolve
            # "This is starting to get embarrassing. And she's annoying me in a way I don't even understand."
            # "I'm so fucking confused..."
            # h happy_closed "Anyway no hard feelings, okay? Peace~" with dissolve
            # show Hiroko:
            #     linear 1.0 ypos 1.0
            # "She kisses her fingertips before patting the floor and springing back up to her feet and... wait a second."
            # show Hiroko frown:
            #     ypos 1.0
            # ks frown "Did you just..." with dissolve
            # "Wait a goddamned second."
            # ks angry "... You'll say sorry to the HOUSE before you'll apologize to ME?!"
            # h tennis_headhold2 confused "Like, duh! You thought that was for you? Why the fuck for?" with dissolve
            # "I can't believe, after everything I did to mess with her. After all the influence she's come to think I have over her tiny mind, she's still found a way to piss me off."
            # h neutral_side "Think somebody needs to get over himself." with dissolve
            # "Man, now I regret not making her yawn her little head off in front of everyone. Goddamn it."
            # show Hiroko frown
            # ks frown "Really? Are you still trying to deny what your subconscious is telling you after today? You still don't think you owe me after all the shit you've pulled?" with dissolve
            # h sleeptalk "Geez, you're back on your hypno bullshit aren't ya. S'making me sleepy..." with dissolve
            # scene cg k room eve
            # show HirokoHypno tennis relaxed sleep
            # with blink
            # "And with that, she stumbles down onto the couch with a groan."

            # h "Just chill, okay?

            # ks "All those times you got in my face and shouted me down for no reason. Made everyone think I'm the biggest creep in school for three fucking years."
            # ks "I helped you, even after all that, and you'd sooner hit me than thank me."
            # ks "Seriously? You're not in the least bit sorry about how you've been to me?"
            # ks "Listen to what your subconscious is saying and get over YOURself!"


            #Get over YOURself!
            # ks "Get over YOURself! You still don't think you owe me after all the crap you've pulled?" with dissolve
            # ks frown "Come on. You still don't think you owe me after all the crap you've pulled?" with dissolve
            # ks "All those times you got in my face and shouted me down for no reason. Made everyone think I'm the biggest creep in school for three fucking years."
            # ks "I helped you, even after all that, and you'd sooner hit me than thank me."
            # ks "Seriously? You're not in the least bit sorry about how you've been to me?"
            #She did it to lash out at him in the only way she could?

            #She never got an answer for him as to why he went to all this trouble. Was it really some long game he played to get revenge on her?
            #But she admits her new tennis prowess are back to how they were in spite of the terrible day she had...
            # h "I'm here, ain't I?"
            #What about the crap YOU'VE pulled?
            #Kyou demands she show some humility, Hiroko brings up how he terrorized her and Nozomi and Rie with his hovering
            #Not to mention his wanting "payback" yesterday, the fact leaving her tennis career alone was entirely HIS choice? That was creepy as hell.
            #The whole way he talked about her was some real controlling shit, and it was to "teach her to respect him" or something? That's scarey, Kyou.
            #Kyou's got to admit that when she puts it all together he's coming off way more of a jackass than he realized and may actually apologize now
            #But that's not all. Hiroko concedes that he's been a big help in her tennis prep despite the abuse which is why she was thinking they talked things out
            #It's why when Sayori and Nozomi went to check on her earlier she didn't say anything about Kyou even if her instincts were screaming at her to ask them to help
            #Maybe Kyou's just a weird sheltered kid who doesn't realize what he's saying? She's not sure, Hiroko's pretty confused by him this past week
            # h sad "I'm just... fuck, my head's all over the place, dude. Dunno what to think anymore." with dissolve
            # "She slumps herself down on the couch, eyes cast towards the floor as if she'd just lost an important set in one of her tennis matches."
            # h "Like, there was no way I'd yawn in class just 'cuz you said I would, but it was like the more I thought about it the more I was gonna yawn for sure."
            # h "An' I figured there was no way I was seriously gonna walk myself over here to let that creepy-ass shut-in hypnotize me again with his funny light."
            # ks frown "\"Creepy-ass shut-in?\""
            # h "Ugh, get over it, dude, I'm trying to be real with you here!"
            # h "'Cuz... y'know? I was thinking all of that but here I am right after practice, just like you told me to. Like a good lil' girl..."
            #
            #
            #
            # h "And this is all 'cuz I'm okay with it deep down. I'm only gettin' hypnotized and letting you fuck with me 'cuz I secretly wanna be."
            # h "That about sum it up? It's what you said, right?"
            # "She looks up to meet my gaze and I awkwardly look back at her."
            # ks sigh "Yeah... that's what I said."
            # "It really has been incredible how much I took advantage of Hiroko's naivity; to get her into this kind of state where she thinks I have this much sway over her."
            # "And if I got away with this much, I'm positive I could push her into doing even crazier things just because I hypnotized her into doing it."
            # h "It's gotta be because I owe you."
            # h "Like... when I was at practice today, it didn't matter how much you got under my skin. Moment I got back on court I was crushing it again."
            # h "And this new racket kicks ass. Like, it's a lil heavier than my old one but I got used to it real quick and I'm gettin' so much more spin you wouldn't believe, and..."
            # h "An' I got you to thank for that, don't I?"
            # h "So I get it. I guess."
            #
            # "So... yeah, I'm stopping this, but not for her sake."
            # ks neutral "But I think I've fucked with you enough."
            # "It's for mine."
            #
            # "But seeing her like she now is only making me sure that I need to put a stop to this."

            # "I don't want to tell her I've been taking advantage of her naivity,

            # h "But I guess you were right about some stuff."
            # ks "Is that so?"
            # h "H'yeah, well I'm here ain't I? Just like you said I would."
            # h "I wrapped up my practice, talked to Nozo an' Sayori for a bit and told 'em I was gonna go home and chill."
            # h "But I came right on over to you instead; like a good lil' girl."
            # h nervous "And, uh... you're gonna hypnotize me again, right? Like, that's why I'm here... right?" with dissolve


            # h nervous "All this hypno stuff's hard to take in, okay?" with dissolve
            # ks neutral "Hm?"
            # "She sits on the couch."
            # h "S'like... start of this week I knew exactly what I was doing."
            # h "Then you showed up on the court and I dunno shit anymore."
            # # h "Keep my head down, work hard on the courts and give it my best shot for the tourney. Thassit."
            # h "Last thing I wanted to think about was this creepy ass nerd who wouldn't leave us alone for all these years."
            # ks "Hiroko- {w=1.0}{nw}"
            # h "Sorry dude, but it's true. I never wanted you in my head."
            # h "But you show up with this new attitude and that flashy light and now I don't know shit."
            # #She's scared about what Kyou's success at hypnotizing her means, but she's become curious again?


            # h "But now, the moment I step off the court you're all I'm thinking about."
            #
            # h "It's been a weird-ass week, is what I'm saying!" with dissolve
            # h nervous "S'kinda getting to me." with dissolve
            #
            # "I don't know if she forgot about yesterday or what. But she sure doesn't seem herself tonight, for better or worse."
            #
            #
            #
            # "AUTHOR'S NOTE: And that's where I have to leave it for now."
            # "I'm going for a quickish ending here, with a more positive vibe than is typical; similar to one of Nozomi's premature endings in the Trance storyline."
            # "Anyway, stay tuned for the next update!"
            # "*** TO BE CONTINUED! ***"
            # jump Credits
    # "How sleepy does she feel right now? She's supposed to feel sleepier with every yawn"

    #Hiroko has to miss tennis practice today because no one will believe she's in a shape to do it, thanks to her public snoozing.
    #She's furious at Kyou; he's already broken his promise not to mess with her tennis training. But also, she has to admit to being a little scared of him now.

    #Kyou will note she still seems incapable of solving her problem by turning off the vibration or putting her phone in her bag or something

    #Hiroko ends up calling him out for not stopping when she told him to, past the point of it being funny, and bring up the hand tickling as when it started.
label Day5_Con_Kyou_Hiroko:
    scene bg street1 day with blink
    "It's Friday, and I'm walking to school feeling unsure."
    play music Eons fadein 5.0
    scene bg classroom day with blink
    play sound schoolbell
    "Morning lessons feel tense. I've barely been able to concentrate before, but this is worse."
    "Obviously I'm excited about the prospect of doing the culture fest for once."
    "I was nervous at first, about performing in front of a bunch of people."
    "But these last few days with Hiroko have really brought out the confidence in me."
    "Plus if I'm doing this with a cutie like her, then there's really nothing to worry about."
    "Speaking of, I can see Hiroko talking with Nozomi and that other girl they hang with. Wonder what they're saying."
    "I don't dare get close enough to eavesdrop, so all I can do is eat lunch at my desk and play with my phone as I half-listen to the chatter of my classmates around me."
    "It's started to bother me, how I'm never part of that chatter."
    "I've hardly been able to talk with anyone these past few years, until these days I've had with Hiroko."
    "It used to be I couldn't stand the little shit, but never mind her now-obvious crushing on me..."
    "I'm definitely feeling something for her too."
    scene bg corridor eve with blink
    "As class lets out for the day I think more and more... I should tell her?"
    "I loiter in the hall for a minute and decide that I'll go see her play today."
    scene bg court eve with blink
    "So I find myself once more heading for the tennis courts."
    show Hiroko tennis_armup furious
    h "Kyou?! What the {nw}" with dissolve
    extend "FUCK, dude? I told you not to come back here!" with vpunch
    "She looks to be fuming as she storms over to me, while I walk to meet her halfway over an empty tennis court."
    ks surprised "H-hey please calm down, okay? There's something I gotta get off my chest."
    h neutral "I... I-I'm calm, what is it?" with dissolve
    "I'm just gonna get it out there. Be brave for once in my life."
    ks sigh blush "I like you, Hiroko."
    h irritated vein "You..." with dissolve
    h surprised blush novein "H-huh?" with dissolve
    ks frown "And when I think about everything that's gone on between us these past years... I think you like me too."
    h tennis "T-that's not... I mean..." with dissolve
    show Risa tennis_armup wristband_right_armup grin at center, flip:
        xpos 0.2
    r "Ahahaha, I KNEW there was something going on!" with dissolve
    show Hiroko surprised_side
    "Hiroko's eyes widen as she realizes Risa has come over to watch us, a massive grin on her face, while Hiroko's cheeks turn redder and redder." with dissolve
    h sleepy "Wait, no, nothing's happening, I... u-uhh..." with dissolve
    "Hiroko's eyes flicker as I smile at her deeply blushing face."
    ks smile "Hey, hey, it's okay."
    h "I... o-okay..."
    r tennis wristband_right smile_side blush "Aww..." with dissolve
    ks "Anyway, I know you need to practice right now, so I'll see you tonight?"
    h "Yeah... see you tonight."
    r grin noblush "Kiss her, you dweeb!" with dissolve
    scene cg hiroko tennis kiss with blink
    "Plucking up my courage, I hold Hiroko gently and lean in to kiss her, as I hear Risa whooping beside us."
    "Her lips feel so soft as mine play against them, while my fingers feel the heat in her delicate cheeks."
    "Hiroko... you really are adorable!"
    $persistent.hiroko_tennis_kiss_unlock = True
    scene bg blackscreen with dissolve
    "And as I pull back and smile at her, she can only look up to me with trembling lips, blushing darkly."
    scene bg street1 eve with dissolve
    "What a beautiful image to take with me as I leave her to practice with Risa."
    "I feel like I'm walking on air as I head home."
    "I mean, holy shit, that was my first kiss... and I think I have a girlfriend now!"
    scene bg k room eve with blink
    "I thought this type of thing only happened in one of those romantic comedies."
    "But I can still feel her lips on mine. It was real, and it happened to me!"
    play sound doorbell
    stop music fadeout 5.0
    "... Huh? Is that her? I barely got home myself."
    "Unless she seriously couldn't bear to wait any longer."
    "Now consumed by the fires of her passion, she made her excuses and tore away from the tennis courts to embrace the feelings she kept under wraps for so long..."
    "Man, what a thought..."
    play sound dooropen
    show Hiroko tennis_armup angry vein
    h "..." with dissolve
    ks neutral "..."
    "Okay, if I'm honest, that does NOT look like the face of someone \"consumed by the fires of her passion\"."
    "She... kinda looks like she IS the fire."
    play sound doorclose
    h furious "{size=34}WHAT IN THE EVERLOVING {b}FUCK{/b}, KYOU!?!{/size}" with shake
    ks surprised "W-wait, what? Why are you-{w=0.8}{nw}"
    h "I don't have a crush on you?! {w=0.5}Like, holy {nw}"
    extend "SHIT! Why would you... w-would you..." with vpunch
    show Hiroko angry
    "She takes a moment to catch her breath while I check the heart pounding anxiously in my chest." with dissolve
    queue music Rain
    ks "B-but wait, I don't understand. Then why... why were you, like, blushing and stuff?"
    ks frown blush "Because... because I get it, you've been a bitch to me all these years because you couldn't handle the idea that you had feelings for me." with dissolve
    ks "But we're.... we're adults now, Hiroko. I thought it was time to stop beating around the bush!"
    h furious "No, Kyou. {w=0.5}{nw}" with dissolve
    extend "NO!" with vpunch
    h "I'm just..."
    h "I mean..."
    "She takes another few breaths as her eyes glisten."
    h cry_open novein "I was so fuckin' mad at you and then, like, I just forgot how to be mad?" with dissolve
    h tennis_headhold "I c-couldn't say anything. You were telling me all this stupid shit and I didn't know what to do..." with dissolve
    h cry "A-a-and the next thing I know, you were gone and Risa's tellin' me we kissed!" with dissolve
    ks surprised noblush "What, you don't remember?"
    h "No! You musta said so much bullshit I blacked out! Don't you get it?"
    "Wait..."
    h tennis_armup furious "We were talking on a tennis court,{w=0.3} you {nw}" with dissolve
    extend "FUCKING MORON!" with vpunch
    "Shit. She means to tell me she was boiling over with rage the entire time we were talking?"
    "That post-hypnotic trigger meant to calm her down could've gone off in her head more than once in quick succession."
    "I can't imagine how that must have felt while I was putting the moves on her..."
    "Still though..."
    ks frown "T-that doesn't make any sense."
    h tennis angry "The fuck you {nw}" with dissolve
    extend "MEAN it don't make sense?!" with vpunch
    h furious "I can't get mad when I'm standing on court! {w=0.5}You {nw}" with dissolve
    extend "MADE me like that!" with vpunch
    ks "Yeah but still, none of this stuff really works unless you want it to work! I TOLD you!"
    ks "So I don't see how it would affect you unless some part of you-{w=0.8}{nw}"
    h tennis_armup furious "NO!" with vpunch
    "I have to jump back a step as she screams in my face."
    h "Mother{nw}"
    extend "FUCKER! You got ANY idea how much I hate your ass?" with vpunch
    h tennis angry "Like, shit, this goes way back." with dissolve
    h angry_side "Every class project, every school trip, every lunch period. {w=0.8}{nw}" with dissolve
    extend "YOU were there!" with vpunch
    h irritated "Always hangin' around me, or Rie or Nozo like a bad smell. You never said anything; just wanted us to notice you SO bad." with dissolve
    h angry "And dude, we noticed you. We tried blanking you to get you to fuck off, but you never took the hint." with dissolve
    ks surprised "Yeah... I mean, I've always been pretty shy, so- {w=0.8}{nw}"
    h tennis_armup furious "FUCK that! You have ANY idea what it's like? Always having some dude in your space all the fucking time?" with vpunch
    h angry_side "We never knew if you were gonna do something. Fuck, we were even seeing you when you weren't there. That's how much you got to us." with dissolve
    h irritated "Didn't matter how much we tried ignoring you, you always came back." with dissolve
    h "'Til I started yelling. That was the only thing that got your ass away from us!"
    h furious "\"Buzz off, creep!\" \"Get the hell outta here, creep!\" \"Go fuck yourself, creep!\"" with dissolve
    ks frown "Y-yeah... you really made me feel like shit."
    h "Fuckin' {nw}"
    extend "GOOD! 'Least you feel something for what you did!" with vpunch
    show Hiroko tennis_headhold2 irritated
    "Hiroko falls silent as she draws a laboured breath and wipes her eyes." with dissolve
    "Is that how they really feel about me for all this time? That I hurt them?"
    "Why would I hurt any of them? I've never done anything to anybody; why would they even think that?"
    "But... more to the point."
    ks neutral "So... why did you agree to do any of this if you really hate me that much?"
    h "Because..."
    h cry "I can't lose!" with dissolve
    ks surprised "What?"
    h tennis_headhold "The tourney I'm playing... If I don't impress anybody there, I'm fucked." with dissolve
    h cry_open "Like, don't you get it, dude? I'm eighteen and I'm STILL playing tennis in a shitty high-school with... w-with some two-bit coach who ain't shit." with dissolve
    h tennis "Mom and pops can't afford me after I graduate. If I don't step it up now and get a scholarship, I'm never gonna make it." with dissolve
    h sad "S-so yeah, when you showed up and bought me that racket? Yeah, I still took that help." with dissolve
    h sad_side "*sniff* And holy shit, did you help." with dissolve
    h sleeptalk_concerned "If I play with your hypno stuff in my head, I'm gonna crush it big time." with dissolve
    h sad "But... it ain't me, is it?" with dissolve
    ks "What do you mean? Of COURSE it's you!"
    h frown "Yeah? Like it was me letting you kiss me and shit? Like I'm ever gonna live that down." with dissolve
    h furious "You {nw}" with dissolve
    extend "SAID I gotta want it for it to work!" with vpunch
    "Much as I hate to admit it, she might have a point."
    "I don't know how it happened, but I can't square her professed hatred, and the Hiroko I've known all this time, with the blushing damsel I met on court."
    ks neutral "I just don't understand. My hypnosis shouldn't work on you like this."
    h cry_open "... Just get it out of me." with dissolve
    ks surprised "W-what?"
    h tennis_headhold "All the stuff you put in my head. You can take it out again, yeah?" with dissolve
    ks "I... yeah."
    h cry "Do it." with dissolve
    show penlight at right with moveinright:
        ypos 0.346
    "I pull out the penlight from my pocket as I look to her distraught face."
    ks concerned "You don't think you're being a bit drastic here? At least wait until you've done the tournament."
    scene bg blackscreen with dissolve
    # show Hiroko:
    #     linear 1.0 ypos 1.1
    "But Hiroko is already sitting down on the living room couch as she wipes her eyes again and looks up at me."
    # show Hiroko:
    #     ypos 1.1
    scene cg k room eve
    show HirokoHypno relaxed tennis sad
    $h = DynamicCharacter("hiroko_name", image = "HirokoHypno", who_color = "#FF89AB") #Hiroko Homura
    with blink
    h "Do it..."
    # hide penlight with moveoutright
    ks "Alright... Look up."
    # if persistent.NewSprite == "":
    #     $light_y = 0.41; light_x = 0.41; ldirection = "right"
    # else:
    #     $light_y = 0.39; light_x = 0.42; ldirection = "right"
    call cglightshow from _call_cglightshow_120
    "As she looks up into the light, I look back at her as I pass the light across her face once again."
    ks neutral "Okay, Hiroko. Just focus on the light, and I'll take care of the rest."
    call cglightshow from _call_cglightshow_121
    ks "Just relax and absorb the soothing patterns in your eyes."
    call cglightshow from _call_cglightshow_122
    show HirokoHypno drowsy
    $ renpy.transition(longdissolve, layer="master")
    "Hiroko breathes a shuddered sigh as she starts to sink into the couch."
    "Despite all her rage and tears, she seems just as adept at dropping into trance as ever."
    call cglightshow from _call_cglightshow_123
    ks "I'm sure the strain of watching those patterns is making your eyelids heavy. Making you tired."
    call cglightshow from _call_cglightshow_124
    ks "There's no need to fight it. Let yourself become sleepy."
    call cglightshow from _call_cglightshow_125
    ks "Let yourself relax and sink, knowing everything is going to be alright."
    call cglightshow from _call_cglightshow_126
    show HirokoHypno sleepy_up_open
    $ renpy.transition(longdissolve, layer="master")
    ks "That's right, Hiroko. Letting those tired eyelids droop. Letting yourself sink deeper and deeper."
    call cglightshow from _call_cglightshow_127
    ks "Deeper and deeper... letting those droopy eyelids close."
    call cglightshow from _call_cglightshow_128
    show HirokoHypno sleep
    $ renpy.transition(longdissolve, layer="master")
    ks "And sleep, Hiroko. Going nice and deep."
    show HirokoHypno drooping
    $ renpy.transition(longdissolve, layer="master")
    "So... this is it, then? I'm just going to trash everything we did and pretend this week didn't happen?"
    "I mean, I get why she might feel she needs to. But surely if we do this now, she'll never be in shape for the tournament she cares so much about."
    "She was so upset... I'm not sure she's thought about this as much as she should."
    "If I could convince her to keep it, at least until after this weekend..."
    "She might thank me later. Maybe even find a way to forgive me for everything she thinks I did up to now."
    menu:
        "Remove everything we did":
            "But no, I really can't make that decision for her. This is what she wants."
            ks "Now, Hiroko, I want you to think back to the things I have talked to you about while you have been in these nice, deep states of relaxation."
            ks "Because everything I have said to you, you must now disregard. Anytime, anyplace, you will think as you would normally think. Act as you would normally act."
            ks "Feel my instructions from the previous days lift from your mind; letting them all disappear."
            ks "Do you understand, Hiroko?"
            h sleeptalk "Yeah..." with dissolve
            show HirokoHypno sleep
            "Well... If our last trances were anything to go by, that should do it for her." with dissolve
            ks "Very good, Hiroko. Now, on three, you are going to wake up feeling refreshed and comfortable, knowing what was asked of you."
            ks "Counting up now... one, two..."
            ks "Three."
            h relaxed neutral "..." with longdissolve
            stop music fadeout 10.0
            "I let out a little sigh as Hiroko comes to."
            ks "There. It's done."
            show HirokoHypno sad
            "Hiroko nods quietly." with dissolve
            h "'Kay..."
            scene bg k room eve
            $h = DynamicCharacter("hiroko_name", image = "Hiroko", who_color = "#FF89AB") #Hiroko Homura
            show Hiroko tennis sad at center:
                ypos 1.2
                linear 2.0 ypos 1.0
            with blink
            # show Hiroko:
            #     linear 1.0 ypos 1.0
            "As she rises from the couch, she looks to me."
            # show Hiroko:
            #     ypos 1.0
            show Hiroko :
                ypos 1.0
            h nervous "You wanna hear something funny?" with dissolve
            "I blink a little in surprise."
            ks surprised "... What's that?"
            h tennis_headhold sad_side "You actually ain't so bad when you ain't creeping." with dissolve
            h frown_side "Now I just think you're a regular asshole, not a creepy asshole." with dissolve
            h tennis_headhold2 frown "There's a difference." with dissolve
            play sound dooropen
            hide Hiroko with dissolve
            pause 1.0
            play sound doorclose
            "And with that she lets herself out."
            "... Wait a sec, she left her racket here?"
            play sound dooropen
            scene bg k house eve with blink
            ks surprised "Hiroko?"
            "I look left and right, the racket bag in my hands, but she's already nowhere to be seen..."
            scene bg k bedroom night with blink
            "Please tell me she didn't leave it behind on purpose."
            "If I've fucked this up for her, I'm not sure I can forgive myself..."
            jump Day6_Con_Kyou_Hiroko
        "Convince her to keep her conditioning":
            "I won't let her compromise her dream just because of my mistakes."
            "This may be a little uncomfortable in the short term, but... but this is for the best."
            "I'm doing this for her."
            ks "Now Hiroko, while you're so nice and deep, feeling so relaxed, you can let go of any emotions you had over today's... events."
            ks "Isn't that right, Hiroko?"
            h sleeptalk "Uh... r-right..." with dissolve
            show HirokoHypno sleep
            ks "Absolutely right. And now that we can think so calmly, so without emotion, we can reconsider whether you truly want to remove the suggestions I placed." with dissolve
            h sleeptalk "Recon... wha? Why?" with dissolve #Re-add sleeptalk concerned later?
            show HirokoHypno sleep
            "I take a moment to breathe, then just hit her with it." with dissolve
            ks "Because you haven't truly thought this through, Hiroko. You made that decision in the heat of the moment and didn't properly consider the consequences."
            ks "But... but now your mind is so calm, so emotionless, we can consider whether you truly want to do this."
            ks "After all, isn't it true that you've been wanting to be a professional tennis player your whole life?"
            h sleeptalk "Ah... m-mostly, yeah." with dissolve
            show HirokoHypno sleep
            ks "And you know that by following the suggestions I gave you, you'll be much more likely to achieve your goal. Don't you?" with dissolve
            h sleeptalk"Yeah... I know." with dissolve
            show HirokoHypno sleep
            ks "So if you want to have the best chance of success, you should keep those suggestions." with dissolve
            ks "Don't you agree that's the most logical thing to do, Hiroko? To achieve your dream?"
            h sleeptalk "Uh... y-yeah... to achieve my dream..." with dissolve
            show HirokoHypno sleep
            ks "That's right. So when you wake from this calm, rational state of being, you will be happy to accept everything that happened this week just as it is." with dissolve
            ks "That makes more sense, doesn't it Hiroko?"
            h sleeptalk "Yeah... makes more sense..." with dissolve
            show HirokoHypno sleep
            ks "Very good, Hiroko. Waking up happy and refreshed as I count up to three..." with dissolve
            stop music fadeout 5.0
            ks "One, two... three, wide awake, Hiroko."
            show HirokoHypno relaxed neutral
            $ renpy.transition(longdissolve, layer="master")
            "Hiroko's eyes flicker open almost as soon as I finish counting."
            "I take a breath and look to her, smiling in a way I hope she'll take as warm and encouraging."
            ks smile "Feeling any better?"
            scene bg k room eve
            $h = DynamicCharacter("hiroko_name", image = "Hiroko", who_color = "#FF89AB") #Hiroko Homura
            show Hiroko tennis smile at center:
                ypos 1.5
                linear 2.0 ypos 1.0
            with blink
            # show Hiroko smile
            play music Eons
            "As she blinks, Hiroko returns my smile as she picks herself up off the couch."
            show Hiroko:
                ypos 1.0
            "After what just happened, I'm relieved to see her face like that again."
            h "Actually, yeah! You told me what I needed to hear~"
            h tennis_armup happy "Like, dude, what was I thinking? {w=0.5}Everything's {nw}" with dissolve
            extend "FINE!" with vpunch
            h laugh "I'll kill it at the tourney, and then I'm gonna be a {nw}" with dissolve
            extend "STAR!" with vpunch
            "I can't help but chuckle. I'm not entirely sure this was the right thing to do, but damn, her enthusiasm is infectious."
            ks smile "Damn right you will! You got this!"
            h "Haha, thanks, dude~"
            show Hiroko:
                linear 1.0 ypos 1.0
            "With a giggle, Hiroko jumps off the couch and scoops her racket bag up with her."
            show Hiroko:
                ypos 1.0
            h tennis smile_side "Yeah, this is gonna work out. You and me." with dissolve
            ks "You and me, huh?"
            show Hiroko smile
            "Just then Hiroko sidles up to me..." with dissolve
            show Hiroko happy_closed
            "Then leans in to kiss my cheek?!" with dissolve
            ks surprised blush "H... Hiroko?"
            h blush "You're right, Kyou. We're adults now." with dissolve
            h "And, like... Risa knew what was up, even when I didn't."
            "I... guess I knew this might happen, if I wanted to convince her everything's fine, but..."
            h smile "I mean,{w=0.2} fuck,{w=0.2} even {nw}" with dissolve
            extend "YOU figured me out before I did." with vpunch
            h "And now I've had a chance to cool off, I realized something..."
            "I wasn't expecting her to be quite as comfortable as this."
            h affectionate "I'm... I'm happy to accept everything that happened just as it is~" with dissolve
            "Even so, as I put a hand to where she kissed me and return her smile, I feel the heat rising in me."
            ks smile "That's... that's great, Hiroko."
            "Maybe I really can alter people's thoughts beyond what they wanted, and this moment isn't real at all..."
            "But... damn, I've wanted a girl to look at me like this in so long."
            "And after a moment of holding each other's gaze, Hiroko slings her bag over her shoulder."
            h tennis_armup smile "Anywho, I gotta get back to practice~" with dissolve
            ks "Y... yeah."
            h happy "I'll catch up with ya later, Kyou~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
            ks "Sure. Good luck out there, Hiroko."
            play sound dooropen
            hide Hiroko with dissolve
            pause 1.0
            play sound doorclose
            "I... guess I'd better review what just happened."
            scene bg k bedroom night with blink
            "Like, is there a chance she truly is fine with me kissing her after all, or..."
            "Is it really true that I've only made her think what I want her to think?"
            "Well... I guess it doesn't have to matter so much. The plan was to keep the suggestions in her head until the tournament's over."
            "So I'll endure a little awkwardness for a couple days, just until she gets what she needs."
            "Then after this weekend I'll bring her under again and remove every hypnotic suggestion she's under, just like she wanted."
            "All I'm doing is giving her the best chance to get her scholarship. That's all."
            stop music fadeout 5.0
            "It's all gonna work out fine."
            $ending = "liar"
            jump Epilogue_Con_Kyou_Hiroko

        # h angry_side "When I stood up and intro'd myself, I saw how you looked at me. You had this, like, hard stare like you were sizin' me up for yer skull collection." with dissolve
        # h "But I sat back down and it wasn't just me. You did it to practically all the other girls too. Just sizin' us all up."
        # k "Jesus, Hiroko. That's nuts! I wasn't-{w=0.8}{nw}"
        # h furious "I ain't DONE!" with vpunch
        # h angry "I know it was nuts. That's what I told myself. 'Sides, not like you're the only creepy guy in our class." with dissolve
        # h "But nah, there's more. You remember those class projects we used to do?"
        # k "Uh... yeah, I think so."


        # h cry_open "I was standing

    label Day5_Redemption:
        scene bg street1 day with longdissolve
        "It's Friday..."
        "Man, what a week."
        "I started it wanting to impress Nozomi with my hypnosis routine and ended it being completely shut out."
        scene bg classroom2 day with blink
        play music Bright_Opening
        "It'd be too much to bear were it not for..."
        show Akiko side uniform smile_side at center
        a "Good morning, everybody!" with dissolve
        "Her."
        show Risa uniform_armup smile_side at center, flip:
            xpos 0.25
        r "Hey, how's it going." with dissolve
        "Akiko really has taken some of the edge off of this horrible experience."
        show Risa smile_side
        a laugh "Let's all do our best today, okay?" with dissolve
        r smug_side "Yeah, 'Kiko. I'll be sure to do that." with dissolve
        a smirk_side "Aww, don't tell me you're going to settle for second-rate mediocrity again, just to defy me." with dissolve
        show Akiko sad_side
        r uniform frown_side "Maybe, maybe not. But how about you mind your business and I'll mind mine, 'kay?" with dissolve
        a "Risa, I wasn't- {w=0.5}{nw}"
        r uniform_armup "Yeah. You were." with dissolve
        hide Risa
        show Akiko uniform_down armband_down sigh
        "Okay, that was... weird." with dissolve
        "I didn't think people would talk back to someone as respected as Akiko, but it seems Risa doesn't have that problem."
        show Akiko sad_side
        "Now that I think of it, when has anyone else really paid much attention to Akiko in this classroom?" with dissolve
        "Even when she was introducing me in front of everybody, it didn't look like many people cared."
        "I thought that was because of me, but maybe that's just how this class is towards their student council president."
        show Akiko sleep
        "How did she even get such an important role if barely anyone supports her, then?" with dissolve
        # "So, not that it's had much opportunity to show until now..." with dissolve
        # "But I thought Akiko may actually be an unpopular figure in the classroom, whose clumsy attempts at leadership have set people against her."
        # "Why's she the president then? Might have something to do with no one else wanting the role."
        "Anyway, she looks a little upset. Maybe I should go say hello..."
        ks smile "Good morning."
        a surprised "H-huh?!" with dissolve
        "Akiko tenses at the sound of my voice, and it makes me tense in return."
        "Like so many other times I've been around a girl. I should've been more careful..."
        a smile "O-oh, hello, Kyou. Good morning!" with dissolve
        "No, it's okay. She just wasn't expecting me to approach her like that."
        "But now what do I say? I should follow up with something."
        ks neutral "I, uh... are you okay?"
        "That's honestly the best I can come up with at a time like this."
        a neutral_side "Yeah, I'm okay." with dissolve
        "I can see a thought cross her mind, and she lets out a little chuckle."
        a uniform armband happy "Just readying that sword, you know?" with dissolve
        ks smile "That sounds a little dangerous."
        a smirk "Ehehehe~" with dissolve
        a smile "Anyway, um... Let's do our best today." with dissolve
        ks smile "Yeah."
        scene bg classroom2 day with blink
        play sound schoolbell
        "Morning lessons proceed uneventfully, and the bell sounds for lunch."
        "Yesterday might have been depressing, but I'm feeling like I can do more today."
        show Akiko side neutral_side at center:
            ypos 1.1
        "Akiko hasn't left her desk, just like yesterday." with dissolve
        "And she may be busy, but I want to ask..."
        ks smile "Hey, mind if I join you today?"
        stop music fadeout 10.0
        show Akiko neutral
        a "Hm? {w=1.0}{nw}" with dissolve
        $ renpy.transition(dissolve, layer="master")
        extend happy "Oh, I'm sorry, maybe another time. I need to head over to the student council room in a second." id Day5_Redemption_a1bbd8a5
        ks neutral "Oh... okay."
        "I'm not sure what to do now as I stand beside her, while the rest of class go about their business around us."
        "Although there is one thought that occurs to me..."
        ks smile "I could come with you?"
        a uniform_down armband_down laugh "Ahahaha!" with dissolve
        show Akiko:
            linear 1.0 ypos 1.0
        play music Downtown
        "Akiko then gathers her things as she rises from her seat."
        a smile "I'll see you later, okay?" with dissolve
        hide Akiko
        "Without another word she heads out the door, leaving me stranded by her desk." with dissolve
        "It makes me feel painfully conscious of the others still in the room, no doubt quietly mocking me for my cack-handed attempt at friendliness."
        "... I need to get out of here."
        scene bg corridor day with blink
        "If not the student council room, then..."
        scene bg rooftop with blink
        "Just anywhere to be away from that class full of fucking strangers."
        stop music fadeout 5.0
        "At least I can get some air up here. And hey, the weather's actually pretty great today."
        h "{size=16}Oh for fuck's sake...{/size}"
        ks "Hm?"
        scene cg rooftop day
        show RoofHiroko scared grimace
        show RoofNozomi scared worried
        show RoofSayori scared irritated
        with blink
        pause 1.0
        play music Measured
        "Oh... Oh, shit, it's them!"
        "I barely thought of them at all today as Akiko occupied my mind. But now?"
        show RoofSayori irritated_right
        s annoyed "{size=16}I told you both that it was foolish to come up here. This was always going to happen.{/size}" with dissolve
        show RoofHiroko grimace_left
        h angry_side "{size=16}Fuck that. I'm... I-I'm not letting this asshole scare me outta living my life, you hear me?{/size}" with dissolve
        "This is my chance."
        ks sigh "Uh... hey, girls."
        show RoofHiroko shout
        show RoofSayori irritated
        h uniform_armup irritated vein "Get {nw}" with dissolve
        extend "LOST! Don't you have to be, like, a hundred feet away from us at all times or something?" with vpunch
        show RoofHiroko grimace
        ks frown "What? No, that's idiotic. No one told me anything like that." with dissolve
        "Ugh, no. Calm down, remember what you wanted to do."
        ks neutral "I just want to talk to you for a few minutes. Then I'll go."
        show RoofNozomi sad
        n side sad_side "Please, Kyou, just... leave us alone." with dissolve
        ks sigh "I will after I said what I came here to say."
        show RoofNozomi worried
        s uniform_folded "All you are doing is distressing us. Just go." with dissolve
        ks "Nozomi. Hiroko. What happened the other day... i-it was stupid. I never should've done what I did with you both."
        ks "I didn't know what I was doing, and I never meant to hurt either of you."
        ks "B-but I did and, fuck, you're right to be angry at me, okay? But I'm sorry."
        ks "I'll do anything to make it up to you guys."
        ks "Just... man, tell me what to do to make it better."
        show RoofHiroko shout
        show RoofNozomi worried_right
        h uniform_armup irritated "You can make it better by..." with dissolve
        h sleeptalk_concerned "B-b-by {nw}" with dissolve
        extend "FUCKING off!" with vpunch
        "... I don't know what else I'm supposed to say."
        show RoofHiroko grimace
        show RoofSayori sad
        show RoofNozomi worried
        s sleeptalk_concerned "Kyou... you've said your piece. Would you please leave us to consider your words?" with dissolve
        show RoofHiroko grimace_left
        "And that's when I notice that none of these girls have even looked at me since I approached them." with dissolve
        show RoofNozomi worried_right
        h uniform sad_side "Y-y-y-eah, what she said." with dissolve
        "Just looking to each other, or to the ground, but never meeting my gaze."
        "They're..."
        # "And of course who should he run into but the very girls who have been avoiding him." with dissolve
        # "Sayori will remind the others that it was a bad idea to come up here and they should've stayed in class like she told them."
        # "Hiroko meanwhile, says she's not going to let some asshole influence how she lives her life. Also shouldn't Kyou be like, 100 feet away at all times or something?"
        # "But this is Kyou's chance to set the record straight. First, no one said anything about a restraining order or whatever it is Hiroko's implying."
        # "Second, he reiterates again that he's sorry to Nozomi and Hiroko, he never meant to hurt them and he'll do anything to make it right."
        # "What more do they want from him?"
        # "Obviously this leaves Hiroko an easy opening to tell him to fuck off, but Kyou notes she's not delivering it with the same venom. Her voice is a little shaky."
        # "And just then, he also realises none of them have looked him in the eye. They either closed their eyes or averted their gazes towards the floor or each other..."
        # "It's an awkward atmosphere, and after standing in pained silence for a few moments, Kyou can only walk away defeated."
        scene bg corridor day with blink
        "They're AFRAID of me?"
        "Why, were they seriously thinking I was going to hypnotize them up there? The three of them?"
        "Didn't they listen to a thing I said? I'm not going to hurt them!"
        "I'm trying so fucking hard and..."
        "Goddamn, what have I got to do to get through to them?"
        scene bg classroom2 day with blink
        "I can't go back up there, so I return to class."
        "Alone..."
        stop music fadeout 10.0
        "What the fuck am I supposed to do now?"
        scene bg blackscreen with longdissolve
        play sound schoolbell
        pause 0.5
        scene bg classroom2 eve
        show Akiko uniform_down armband_down side at right
        with longdissolve
        a "Stand!"
        a "Bow!"
        hide Akiko
        "As the day comes to an end I'm no closer to an answer." with dissolve
        "I just fucking despair."
        play music Eons
        "Seriously. I'm starting to wonder why I thought it was a good idea to wake Hiroko up back then."
        "Letting her remember everything instead of making her forget. I could've done that, right?"
        show Akiko uniform_down armband_down side smile
        a "Kyou, are you heading home?" with dissolve
        "Hell, if I knew I'm just going to get shit on for doing the right thing, would it have been so bad to keep her the way she was?"
        if hypno1 == "devoted hiroko":
            "At least she would've been happy instead of... whatever she is now. I've never seen her like that before."
        elif hypno1 == "robot hiroko":
            "At least she wouldn't be this hurt. I could've seen to that."
        a happy "I wanted to have a quick word with you first if that's okay?" with dissolve
        "If I just had the nerve to go through with it, could anyone have stopped me?"
        a confused "... Kyou?" with dissolve
        ks surprised "Huh? O-oh, hey Akiko."
        "No, come on, what the hell is wrong with me? Why am I thinking such fucked-up things?"
        "I gotta get my head back in the game."
        a sigh "Do you always space out like this? Geez." with dissolve
        "Akiko shakes her head at me and I mentally kick myself for switching off in front of her again."
        a sad "Anyway, sorry about lunch. I really had so much work to do, what with the culture festival coming up and everything." with dissolve
        ks sigh "Oh, y-yeah, of course. I understand."
        a smile "Right. And I need to get back to it, but before that I wanted to talk to you for a bit." with dissolve
        "After the thoughts I've been having, talking to Akiko would be a welcome distraction."
        ks smile "Yeah, sure."
        a happy "Good. Actually, let's step outside for this." with dissolve
        # "He wonders if his decision to spare Hiroko from a life as his brainwashed robot/groupie was really the correct one if people are going to shit on him anyway."
        # "It's a little disgusting to think about, but also really who could've stopped him if he had the nerve to follow through with that?"
        # show Akiko side at center
        # "He's broken out of his thought by Akiko addressing him." with dissolve
        # "Referring to the fact he wanted to lunch with her, she's wondering if he'd want to meet up quickly before he goes home?"
        scene bg corridor eve
        show Akiko side sad_side
        with blink
        "I follow her out into the corridor, and she waits as our classmates busy themselves with leaving to head home or attend their clubs."
        "Makes me nervous that she thinks we need to be alone for what she's about to say."
        a "Tell me this is none of my business..."
        "That's not helping, Akiko."
        a sad "But what did you do to wind up having to switch classrooms?" with dissolve
        "Why does she want to know? Did she find out what happened on the rooftop?"
        a sigh "I'm sorry to put you on the spot like this, but I keep hearing rumours and, well..." with dissolve
        ks sigh "I'll bet you've heard all kinds of things about me by now."
        a sad_side "Yeah... But I want to hear it from the horse's mouth." with dissolve
        a neutral "Whatever it is, I promise I won't judge." with dissolve
        a sleep "It's like I said yesterday, if it was that bad they would've suspended you." with dissolve
        a neutral "So you can just tell me, okay?" with dissolve
        "Honestly, with what people must be saying behind my back, how could telling her be worse?"
        ks neutral "Okay..."
        "And I don't need to tell her every detail. Just the basic facts."
        ks sigh "I hypnotized a couple of the girls in my old class and they kinda freaked out about it."

        # "Kyou of course is agreeable to Akiko keeping him back, and as they retreat to the corridor and wait for most of the others to head out, she asks him something."
        # "Tell her it's none of her business but... what did he actually do to wind up having to switch classrooms?"
        # "Kyou is suspicious of why she wants to know now. Did word of his rooftop confrontation with the girls get out? Did Akiko talk to any of them?"
        # "Akiko admits she's heard rumours, but she insists it's something she's been curious about since yesterday morning at that briefing."
        # show Akiko sad_side
        # "She promises she isn't going to judge. Once again, whatever Kyou did or didn't do wasn't considered worthy of suspension so it can't be all that terrible can it?" with dissolve
        # show Akiko sad
        # "So Kyou just comes out and says it... He got in trouble because he hypnotized a couple of his classmates and now they're afraid of him." with dissolve
        show Akiko uniform_down armband_down surprised
        a "H-huh, really?" with dissolve
        ks surprised "W-w-wait, what did YOU hear?"
        a confused "That's what I heard, but it was so silly I didn't think..." with dissolve
        a sigh "Ugh, that's so dumb!" with dissolve
        "I'm not sure what to think about her reaction."
        ks confused "You... really think so?"
        a sad "Well, yeah, of course! Does everyone around here think hypnosis works like it does in the cartoons?" with dissolve
        "She sighs harshly."
        # a frown "There really are people out there who think they can see a coin on a string or... or a spiral shape someone shows them and they'll just do as they're told!" with dissolve
        a frown "Some people really do think a person can wave a coin on a string or a... a spiral shape in front of their eyes and they'll be completely in that person's power!" with dissolve
        # a neutral "Well, yeah, of course! Do they all think hypnosis works like it does in the cartoons?" with dissolve
        a uniform armband frown_side "And now those same people are telling each other that you're going around trying to hypnotize girls into sleeping with you." with dissolve #; because you looked them in the eyes or something." with dissolve
        a angry "Agh, it's all so STUPID!" with dissolve
        show Akiko frown
        ks sigh "Uh... y-yeah, it is." with dissolve
        "If I didn't know what I found out the other day, I'd be every bit as incredulous as she is."
        a sad "I'm really sorry, Kyou. People can be such jerks." with dissolve
        ks neutral "It's not your fault."
        a sigh "I know, but... I don't understand why everyone's giving you such a hard time. You seem perfectly normal to me." with dissolve
        "Wait."
        ks surprised "You think I'm normal?"
        a neutral "You think you're not?" with dissolve
        "Her simple retort leaves me stunned."
        "I'm used to people calling me a creep and a weirdo, if they notice me at all, so that just knocked me for six."
        a neutral_side "I need to get to student council now, but I was wondering..." with dissolve
        a smile "Do you want to meet up this weekend?" with dissolve
        "I blink at her. Did she really just say what I think she said?"
        "But without waiting for my response she quickly pulls out her phone and unlocks it in front of me."
        a happy "Culture fest prep is going to be wild after that, but I can make time tomorrow." with dissolve
        a uniform_down armband_down smile "So how about it? I don't often meet people who are into psychology." with dissolve
        a smirk "Want to talk hypnosis with me?" with dissolve
        stop music fadeout 10.0
        # "Akiko is a bit surprised to hear this. She thought it was a silly rumour, but she didn't know what else it could have been." with dissolve
        # "It just seems so ridiculous! Like Kyou's some kind of cartoon villain who can control minds? Is that what people think of him?"
        # "Cue nervous laughter from Kyou, who obviously isn't going to tell her what he's learned about his penlight."
        # show Akiko sigh
        # "Akiko needs to go, but she does feel that Kyou's been unfairly ostracized. After all, he's been perfectly nice and reasonable to HER!" with dissolve
        # show Akiko smile
        # "Anyway, she asks if Kyou would be open to talk at the weekend? She finds this talk of hypnosis fascinating and would like to know more." with dissolve
        # "But with the culture festival upcoming she won't have a lot of time in the medium term, so this weekend it is!"
        # hide Akiko
        # "Kyou's not going to say no to that, so she gets his contact details before dashing off to student council." with dissolve

        scene bg street1 eve with blink
        "So we're going to work something out for tomorrow and I don't know what to think."
        "Do I even want to talk to Akiko about psychology or whatever it is she's after?"
        "And why is my brain still having trouble thinking of her as a classmate of mine? Or as a girl?"
        "... I'm meeting a girl on the weekend."
        # "Referring to the fact he wanted to lunch with her, she's wondering if he'd want to meet up this weekend for... something."
        # "I don't know what yet, to be honest. Help out with culture fest prep at the school? Grab lunch somewhere after kendo practice?"
        # show Akiko smile
        # "Regardless, Kyou's going to accept, as she keeps him distracted from the dark thoughts he's just had and he obviously wants to spend time with her." with dissolve
        scene bg k bedroom eve with blink
        play music Past_Sadness
        "Isn't that the kind of thing I wanted? With Nozomi?"
        "I've only known Akiko for a couple of days, but I have to admit she's rubbing off on me."
        "She's nice. And she's distracting..."
        "She could help me move on from all the shit that's been my life before now."
        # "Kyou then sets off home having resolved to move on with his life, happy for the distraction and potential of a relationship that Akiko seems to promise."
        "Yeah. Yeah, okay. Let's forget about Nozomi. I'm done with all that."
        "A fresh start. A new beginning. That's what Akiko told me."
        "One lapse of morals isn't going to define me. It isn't!"
        "It's time to move on..."
        stop music fadeout 10.0
        scene bg blackscreen with longdissolve
        pause 2.0
        jump Day6_Redemption

label Day5_TennisBot:
    scene bg street1 day with longdissolve
    "It's Friday. Man, what a week it's been."
    queue music Bright_Opening
    "I started out with high hopes of impressing the girl of my dreams. Of getting her to notice me."
    scene bg ext school day with blink
    "But who could've imagined that I'd end it convincing a girl that she's my [hypno6]?"
    show Hiroko neutral at center
    "... And my high-school bully at that?" with dissolve
    show Hiroko sleep
    "Speaking of which, Hiroko bows politely to me as we cross paths outside the front gates, before she starts to head inside." with dissolve
    show Hiroko neutral_side
    "I hadn't specifically programmed her to do that, so it's cool to see her showing me respect after all these years." with dissolve
    if hypno6 == "robot":
        "She? It? Damn, it's hard to get it straight in my head."
    show phone at right with moveinright:
        ypos 0.346
    "Anyway, thanks to the programming I DID do on her last night, I have a way to deliver a little positive reinforcement while I follow her inside from a discreet distance..."
    scene HirokoShoe pose1
    show phone at right:
        ypos 0.346
    with blink
    "I just have to open this app I hastily coded, then press this button marked \"Pleasure\" here and..."
    play sound appbutton
    show HirokoShoe pose2
    h sleeptalk blush "{size=16}O-ooohhhnnn~ {font=DejaVuSans.ttf}♥{/font}{/size}" with dissolve
    "That pleasurable electrical jolt she's supposed to feel crackling from her crotch to her head whenever she accepts a change to her programming?"
    "One press of this button on my app sends a coded signal to the little headphone she's wearing, which has it deliver a subtle trigger that only she can hear."
    # "In other words, I can make that [hypno6], meaning I can make her feel it any time I want."
    # "I can send a pleasurable electical jolt crackling through the circuitry of her body any time I want."
    show HirokoShoe pose3 neutral
    # "With a smile, I watch as Hiroko puts a hand to her ear and grins to herself." with dissolve
    "As I notice Hiroko quietly moaning in front of me, I smile as I see my remote command is having the desired effect." with dissolve
    #
    # "As I hear Hiroko quietly moaning in front of me, I smile at the knowledge I can make that [hypno6]-conditioned mind of hers light up any time I want." with dissolve
    hide phone at right with moveoutright
    show HirokoShoe pose3 happy
    "So it seems that device and the, uh, \"software\" I installed on her is working perfectly. I can now make that [hypno6]-conditioned mind of hers light up any time I want." with dissolve
    "That's good; we'll need it for today. After all..."
    $persistent.hiroko_shoe_unlock = True
    scene bg classroom day with blink
    "Hiroko still has a task to do. And I'm going to monitor her while she does it."
    "I mean, it's not that I don't trust my [hypno6] to follow orders; not after everything I've seen. But I'm not about to leave anything to chance."
    stop music fadeout 5.0
    play sound schoolbell
    with blink
    "So when lunchtime rolls around, I strain myself to listen to what's going on a couple desks away from me..."
    scene ClassroomLunch boy1 boy2_missing hiroko h_sad_nozomi n_armup n_neutral_left glasses sayori s_neutral_hiroko with blink
    queue music Downtown
    h "How're you holding up, Nozo? You doing okay?"
    show ClassroomLunch n_folded n_sigh
    n "Please, Hiroko. Not here." with dissolve
    show ClassroomLunch h_worried_nozomi
    h "Oh... s-sorry, sis." with dissolve
    show ClassroomLunch n_thinking s_concerned_nozomi
    s "We will take this to our usual place. I suspect we have much to discuss." with dissolve
    show ClassroomLunch h_neutral_nozomi n_neutral_left
    h "H'yeah, totes. C'mon, Nozo, let's get out of here." with dissolve
    scene bg classroom day with blink
    "The three of them file out of the classroom, ignoring me completely on the way to their rooftop meeting spot so they can talk away from me."
    show phone at right with moveinright:
        ypos 0.346
    "Or so they think, as I take a set of earphones and plug them into my own phone."
    "Because all I need to do is dial Hiroko's phone, which I'd configured last night to automatically and silently accept my calls."
    "And within seconds Hiroko's ears are also my ears..."
    "{color=93624B}\"I don't know how much longer I can go on like this.\"{/color}"
    scene cg rooftop day
    show RoofHiroko handcheek neutral
    show RoofNozomi handsdown regretful
    show RoofSayori leanback neutral
    with blink
    n "Don't tell anyone else, but... I'm thinking about dropping out of school."
    show RoofSayori shocked
    show RoofHiroko shocked_left
    h uniform_armup shocked_side "WHA?! For real?!" with dissolve
    "Man, my thoughts exactly. Nozomi can't be serious, can she?"
    show RoofNozomi handsdown worried_right
    n "I'm not saying I will. I still need to talk to my parents about my whole situation, but... Kyou..." with dissolve
    "Fuck. Won't your parents want to know WHY you're pulling out, Nozomi? That's only gonna end badly for me."
    show RoofHiroko leanback worried_left
    show RoofSayori worried
    show RoofNozomi worried_left
    s uniform_handup concerned "You may not want to hear this, but your unwillingness to specify the nature of Kyou's offense is going to make it difficult to effect any consequence on him." with dissolve
    show RoofNozomi growl_left
    n "Ugh, whose side are you on, Sayori?" with dissolve
    "Hiroko had better come through for her sysadmin..."
    show RoofSayori sleeptalk
    s uniform_folded sleeptalk "You know I believe you, Nozomi. Kyou has had an uncomfortable fixation on you for some time now; we've all seen it." with dissolve
    show RoofNozomi frown_left
    s concerned "And nothing would displease me more than if you were to disrupt your schooling, let alone on the eve of your entrance exams." with dissolve
    "But I'm not hearing anything from her. What's she waiting for?"
    show RoofSayori neutral
    show RoofHiroko handcheek worried
    s uniform_handup "We must consider practical solutions... Perhaps if the three of us presented a united front to Kobayashi?" with dissolve
    "I could order her to intervene, but not in class where some of my classmates can overhear me."
    show RoofNozomi irritated
    n side frown_side "He's never listened before, so why would he now? He won't do anything. No-one at this school will do anything." with dissolve
    show phone at right with moveinright:
        ypos 0.346
    "But with my app still open, I can send Hiroko a little signal that should spur her into action."
    "All I have to do is press the button marked \"Jolt\"..."
    play sound appbutton
    show RoofHiroko whimper
    h uniform_armup scared "{size=16}Mnth...{/size}" with dissolve
    hide phone at right with moveoutright
    "This signal's meant to trigger her to feel an electrical jolt like before, only instead of pleasure she's meant to interpret it as a neutral surge of current running up her body."
    show RoofHiroko worried
    show RoofSayori sleep
    s frown "I understand it will be difficult to effect any meaningful change, but you are giving up far too easily." with dissolve
    "I told her that it's not very painful for a [hypno6] to experience this, but it does remind her that she's being monitored. That it should spur her into action."
    show RoofHiroko leanback worried_left
    show RoofNozomi neutral_right
    show RoofSayori neutral
    h uniform_headhold nervous_side "Uh, hey... guys?" with dissolve
    "Or in other words, it's my way of telling her to get the hell on with it."
    show RoofSayori worried
    s surprised "Hiroko. I had expected you to jump in so much sooner." with dissolve
    show RoofHiroko sigh
    h sleeptalk_concerned "H'yeah, I'm just... l-like, trying to process this shit, that's all." with dissolve
    show RoofNozomi worried_right
    n "Is everything alright?" with dissolve
    show RoofSayori neutral
    show RoofHiroko worried_left
    h uniform_headhold2 sad_side "You can't quit coming to school, Nozo. That ain't gonna solve anything." with dissolve
    show RoofHiroko frown_left
    h frown_side "But it's gonna be alright. I won't, um..." with dissolve
    show RoofHiroko growl_left
    h uniform_armup irritated "I-I won't let him hurt you again!" with dissolve
    "Ugh, what the fuck is she doing?"
    show RoofNozomi pain_right
    n sad_closed "Hiroko, you can't... what he's doing, you can't protect me from..." with dissolve
    show RoofHiroko worried_left
    h uniform_headhold2 neutral_side "Yeah, sis, I know. He's a creepy fuck an' whatever skeevy shit he pulled on you, he's probably gonna do it again real soon." with dissolve
    "I told her to convince Nozomi I'm not a threat to her, but all she's doing is pissing me off!"
    show phone at right with moveinright:
        ypos 0.346
    "Seems she needs another reminder about who she answers to."
    show RoofHiroko handcheek sad
    show RoofNozomi worried_right
    h sleeptalk "{cps=20}I know what a s-{/cps}{w=0.5}{nw}" with dissolve
    play sound appbutton
    show RoofHiroko whimper
    extend scared_side "s-{nw}" with vpunch
    extend "scary dude he is!"
    hide phone at right with moveoutright
    show RoofHiroko worried
    h sleeptalk_concerned "L-l-like, he could be hiding around the corner an' listening to us right now. You never know when he's gonna show up and freak you out." with dissolve
    show RoofHiroko nervous_left
    h nervous_side "We tried being nice to him about it. We tried blanking him. We even tried getting up in his face and yelling, and..." with dissolve
    show RoofSayori irritated
    s rolleyes "Well, that last one was all you, let's be honest. But I take your point." with dissolve
    show RoofSayori frown
    s uniform_folded concerned "Kyou has stubbornly refused to acknowledge even direct rejections of his attention, to the point where we must believe it to be deliberate on his part." with dissolve
    show RoofHiroko frown_left
    h sad_talk "H'yeah, he really is a shit. We tried everything to make him back off and it's like he don't care at all." with dissolve
    "She's STILL talking like this about me? I don't fucking believe it!"
    show phone at right with moveinright:
        ypos 0.346
    h "{cps=20}But I... {w=0.5}{/cps}{nw}"
    play sound appbutton
    show RoofHiroko whimper_closed
    $ renpy.transition(dissolve, layer="master")
    extend sleeptalk_concerned "ahhh I-I'm gonna talk to him, okay?"
    "Maybe I should've programmed an instruction to make her experience real pain after all..."
    hide phone at right with moveoutright
    show RoofSayori worried
    show RoofHiroko sad
    s uniform_folded surprised "You'll talk to him? As in...?" with dissolve
    show RoofSayori neutral
    show RoofHiroko leanback neutral_left
    h sad_side "I'm gonna be real with him. I'll tell him straight up that he's scaring everybody and he's gotta step off." with dissolve
    show RoofHiroko worried_left
    h nervous_side "... An' I'll say I'm sorry for being such a butt to him." with dissolve
    show RoofNozomi panicked_right
    n surprised_side "You're sorry?" with dissolve
    show RoofHiroko sigh
    h uniform_headhold sleeptalk_concerned "Yeah... I just wanted him to quit bothering you, and he didn't listen an' I guess it's my fault if I just made him mad." with dissolve
    show RoofNozomi neutral_right
    show RoofHiroko worried_left
    h nervous_side "S-so, yeah... I'll be all sweet with him. Hear the dude out." with dissolve
    show RoofHiroko worried_right
    h surprised_side "Maybe I can set him up with some other chick? I-I dunno, I'll think of something." with dissolve
    show RoofSayori worried
    s uniform_handup concerned "So... appeasement? You'll be attempting to appease him?" with dissolve
    show RoofHiroko handcheek sad
    h sad "Yeah." with dissolve
    show RoofNozomi panicked_right
    n sad_closed "Hiroko. You can't do that! I can't let you do that!" with dissolve
    show RoofNozomi worried_right
    s sleeptalk_concerned "I know you mean well, but what you are proposing seems just as likely to backfire as yelling at him." with dissolve
    show RoofHiroko worried
    h uniform_headhold2 confused_side "You think?" with dissolve
    show RoofSayori sleeptalk
    s uniform_folded concerned "I do. He could very well view your desperation for peace as evidence that his methods are effective and become further emboldened." with dissolve
    show RoofNozomi regretful
    n sad_side "Yeah. He's dangerous, Hiroko. There's no telling what he'd do if he was alone with you." with dissolve
    show RoofSayori neutral
    show RoofNozomi worried_right
    n "I can't let you risk yourself like that. You can't get hurt because of me." with dissolve
    show RoofHiroko leanback frown_left
    h frown_side "I'm already hurt. It's killing me that he's done this to you, sis." with dissolve
    show RoofNozomi regretful
    n sleeptalk_concerned "You know what I mean..." with dissolve
    show RoofHiroko worried_left
    h uniform sad_side "Yeah, but I gotta try. Someone's gotta fix this." with dissolve
    stop music fadeout 5.0
    show RoofNozomi crying
    n frightened "It shouldn't be YOU!" with dissolve
    show RoofHiroko handcheek worried
    h uniform_headhold2 nervous_side "Nozomi... h-hey, c'mon, it'll be okay." with dissolve
    queue music Measured
    "Is... is Nozomi crying now? For fuck's sake!"
    show RoofNozomi scared cry_closed
    n cry "It's not okay. NONE of this is okay!" with dissolve
    n "H-h-he's... I can't get him out of my head. It feels like I'm seeing him every time I close my eyes."
    show RoofNozomi cry_right
    n sleeptalk_concerned "... I've even caught myself thinking that I should just start a relationship with him. That I might even like it." with dissolve
    show RoofSayori worried
    show RoofHiroko shocked_left
    h uniform_armup shocked_side "WHAA?! That's so gross!" with vpunch
    show RoofNozomi cry_closed
    n frightened "I KNOW! I know...!" with dissolve
    show phone at right with moveinright:
        ypos 0.346
    h "{cps=20}I'm getting sh-{/cps}{nw}"
    show RoofHiroko whimper_closed
    play sound appbutton
    extend scared_side "{cps=5}sh-{/cps}{nw}" with vpunch
    play sound appbutton
    extend scared_side "{cps=5}sh-{/cps}{nw}" with vpunch
    play sound appbutton
    show RoofHiroko whimper
    extend scared_side "{cps=5}sh-{/cps} shivers just thinking about it!" with vpunch
    ks angry "Goddammit, Hir-"
    hide phone at right with moveoutright
    "FUCK! Now everyone in class snapped to look my way. Gotta take a breath while I helplessly listen to this shitshow unfold."
    show RoofHiroko worried
    show RoofSayori neutral
    n "NONE of us should have to deal with this stuff!" with dissolve
    "But Hiroko must have heard me just now. And she sure as shit felt those electrical pulses I sent her again and again."
    n "I mean, where are his parents? W-why is Kobayashi so f-f-FUCKING useless!?"
    "She is in SO much fucking trouble when I get a hold of her..."
    show RoofNozomi cry
    show RoofSayori worried
    n cry "... W-w-why can't he just leave me alone?" with dissolve
    show RoofHiroko nervous_left
    h nervous_side "It'll be okay, Nozo. I promise." with dissolve
    show RoofNozomi cry_right
    n concerned "I-I'm so scared, Hiroko." with dissolve
    show RoofHiroko sad
    show RoofSayori neutral
    h sad "H'yeah, an' I'm scared too. But when it comes down to it, Kyou's still human. You all are." with dissolve
    show RoofHiroko leanback sigh
    h sad_side "Deep down he's gotta know what he's doing to you is wrong." with dissolve
    show RoofHiroko worried_left
    h sleeptalk "He's just gotta find his heart." with dissolve
    scene bg classroom day with blink
    stop music fadeout 10.0
    h "{size=18}\"Anyway, I gotta visit the ladies room. Then we're gonna talk about something fun, yeah?\"{/size}"
    "I still can't believe what she's done."
    n "{size=18}\"Okay...\"{/size}"
    "She was supposed to calm things down. Tell Nozomi I'm not a threat. Make sure she doesn't do anything that'll come back to hurt me."
    "But what she said up there... somehow she's rebelling against me, she has to be."
    "I can make her think anything I want. Why didn't I just program her not to care about Nozomi? Why am I letting her care about ANYTHING?"
    "This is my fault..."
    h "{size=18}\"Uh, hello? Mister sysadmin?\"{/size}"
    play music Diary
    "... I almost spoke out loud again in my surprise. Damn."
    h "{size=18}\"I know you're mad at me...\"{/size}"
    "She's talking quietly, but she's definitely trying to talk to me."
    h "{size=18}\"B-but, dude... I-I mean, sysadmin, sir, I only did what you told me.\"{/size}"
    h "{size=18}\"Talk to Nozo, get her to back off.\"{/size}"
    h "{size=18}\"An' she's gonna. You stay away from her and keep your nose clean an' she'll let it go. I know she will.\"{/size}"
    h "{size=18}\"So please... p-please don't be mad. I'm a good [hypno6] who always obeys [p_their] programming.\"{/size}"
    h "{size=18}\"I'mma good [hypno6], please don't sell me for parts...\"{/size}"
    "I sigh quietly to myself as I hear her go on."
    h "{size=18}\"Please...\"{/size}"
    "She means to tell me that monstering me to Nozomi was supposed to be helpful?"
    "I'm not going to speak out loud in here again. People are already starting to wonder what I'm doing at my desk."
    show phone at right with moveinright:
        ypos 0.346
    "But my phone is still open on my app."
    "I could send her a message..."
    menu:
        "Press the \"Pleasure\" button":
            $PunishedHiroko = False #This will probably affect an ending later
            $RewardedHiroko = True
            stop music fadeout 5.0
            play sound appbutton
            h "A-aahhhnn~"
            h "{size=18}Eh... ehehehe.{/size}"
            h "{size=18}Y-y-yeah, I'mma real good [hypno6]~ {font=DejaVuSans.ttf}♥{/font}{/size}"
            h "{size=18}Anywho, I gotta go back up now. Bye, mister sysadmin~{/size}"
            hide phone on right with moveoutright
            "... She hung up the phone."
            "Well, it doesn't matter. I can always call it again, but I think I'll leave Hiroko to her friends now."
            "It seemed she really was trying to help to the best of her ability. And do I seriously have any reason to doubt her?"
        "Press the \"Jolt\" button":
            $PunishedHiroko = True
            $RewardedHiroko = False
            stop music fadeout 5.0
            play sound appbutton
            h "N-ngtth!"
            h "{size=18}... Y-y-yeah, I ain't good enough. This [hypno6]'s CPU ain't good enough.{/size}"
            h "{size=18}Guess I don't know my programming like I thought.{/size}"
            h "{size=18}Sorry...{/size}"
            hide phone on right with moveoutright
            "And on that dejected note, she hung up on me."
            "Was she seriously thinking she was helping? That was her trying her best?"
            "... Do I really think she can rebel against my control after everything I've witnessed?"
        "Don't do anything":
            $PunishedHiroko = False
            $RewardedHiroko = False
            stop music fadeout 5.0
            h "..."
            h "{size=18}\"... I gotta go back now. Can't blow my cover, right?\"{/size}"
            h "{size=18}\"Right...\"{/size}"
            hide phone on right with moveoutright
            "And on that dejected note, she hung up on me."
            "Was she seriously thinking she was helping? That was her trying her best?"
            "... Do I really think she can rebel against my control after everything I've witnessed?"
    queue music Downtown
    "Man, I'm not so sure anymore."
    "But now as I pull my headphones out of my ears and turn off the phone, I start to think back to that conversation I overheard."
    "I've heard those girls talk amongst themselves before, in class, but this is the first time I've gotten to hear them when they \"knew\" I couldn't possibly overhear them."
    "And now that I recall what they were saying about me... They really DO think I'm some kind of monster, huh? Even before all this?"
    "Even Hiroko was scared of me back then? Even for all those times she yelled in my face for being a \"creep\" or whatever?"
    "I don't know if I can believe that, but..."
    "Well, they sure have a reason to fear me now, huh?"
    scene bg classroom eve with blink
    play sound schoolbell
    show Nozomi front2 at right with dissolve
    n "Stand!"
    n "Bow!"
    hide Nozomi
    "I keep my head down for the remainder of the school day." with dissolve
    "But as everyone makes ready to leave our classroom, I discreetly look towards Nozomi's desk."
    "She's not as eager to leave as she has been these past few days."
    "Instead, she and Sayori both look to Hiroko before they all nod to each other. Seems like Hiroko's about to enact that plan of hers."
    "Well, I'd better pretend I don't know what's going on..."
    scene bg entrance eve with blink
    "I'll pick up my bag and head out with all the others. Make my way to the shoe racks like I'm about to head home..."
    h "Hey, Kyou."
    "I stiffen slightly at the sound of Hiroko's voice behind me."
    show Hiroko uniform_headhold frown
    "Not like I wasn't expecting it but still, hearing her address me flatly like that is a little unnerving after the last few days I've spent with her." with dissolve
    h uniform_headhold2 neutral "Listen, uh... we gotta talk." with dissolve
    ks "Do we now?"
    h neutral_side "H'yeah..." with dissolve
    "Hiroko shifts nervously as she pops her indoor shoes off in front of me."
    h uniform nervous "It's about Nozomi. I ain't mad or anything, I just..." with dissolve
    "Yeah, this is awkward. But I guess this little show we're putting on will satisfy anyone watching us."
    ks sigh "Okay... sure, let's talk."
    scene bg court eve
    show Hiroko sad_side at center
    with blink
    "I allow Hiroko to lead me outside, and she makes her way towards the tennis courts."
    "Although before we get too close, Hiroko suddenly stops and turns around to face me."
    h sad "Okay, this's good enough." with dissolve
    "I simply nod. She doesn't want people eavesdropping, but she does want us to be seen together. Proof to anyone that asks that we're having a \"realtalk\"."
    h uniform_headhold nervous "S-so, uhhh..." with dissolve
    "And I guess we will, in a sense. Just not the one everyone will think we had."
    ks neutral "Alright, Hiroko. Like I told you before, I'm not going to approach Nozomi anymore. We'll just pretend you're the one who convinced me."
    ks "I have no choice now but to see if this little plan of yours pays off."
    if RewardedHiroko == True:
        h uniform_headhold2 smile "It will. It totally will~" with dissolve
    else:
        h sad "Yeah... s-sorry." with dissolve
    ks "Yeah. So the next time you see your friends, tell them we talked and that they have nothing to worry about with me."
    show Hiroko neutral
    ks "Don't go into specifics if you can avoid it, but make sure they're satisfied. And if there's something I need to know you'll make informing me your first priority. Understand?" with dissolve
    show Hiroko uniform
    h "Yessir." with dissolve
    "I nod at her, satisfied."
    ks "Cool. I think that covers everything, then. Revert to your primary function, perform your nightly maintenance and I'll contact you if I have any new orders."
    h surprised "So, like... that means I can go to practice today, right?" with dissolve
    ks frown "Remind me of your primary function again."
    "She stares at me blankly for a second, then pumps her fists with determination."
    h uniform_armup frown "Excelling in the game of tennis!" with dissolve
    ks smirk "There you go."
    if RewardedHiroko == False:
        h confused "And, l-like, you ain't gonna sell me on the black market, right?" with dissolve
        ks sigh "Just erase that concern from your memory. You're all about your tennis until I tell you otherwise, okay?"
    h happy "{cps=15}Ahahaha, {/cps}{nw}" with dissolve
    extend "KICK ASS!" with vpunch
    "Hiroko's been too busy with my programming sessions to devote any time to her passion."
    "Not to mention if I want Nozomi to calm down about me, I'd better try to bring things back to a state of normalcy around here."
    stop music fadeout 10.0
    scene bg k bedroom eve with blink
    "So I leave Hiroko to it and return home."
    "Huh. I should be used to returning to an empty house, but after the last few days it feels oddly discomfiting."
    "Just me, with only my thoughts for company."
    "Well, never mind that. Without the [hypno6] around it's probably a good time to review what I've learned over the past few days."
    "To start, it's safe to say my unexpected project has been an unqualified success."
    "I still can't explain how, but there's no doubt in my mind that Hiroko's perception of reality has been completely transformed since our accidental hypnosis session."
    "She... she really can't shake off the programming I've placed in her mind, even when it meant unwaveringly putting my interests and desires ahead of her own."
    "I may have doubted her today, but when I look back, Hiroko really has passed every test she's faced."
    "Hiroko is and has always been a [hypno6], and her programming dictates that I and I alone have complete control over her every function. She fully accepts that reality."
    play music Past_Sadness
    "... I just don't know if I can accept it anymore."
    "When I first hypnotized her, I was angry. She'd been getting in my face for so long that I thought nothing of making her into whatever I wanted, now that I had the chance."
    "But now that she's like this, so deferential and nice and... well, fearful of me, it's hard to stay angry."
    "She's almost like the girl I thought she was when we first met as high school freshmen."
    "So what am I even doing now? What am I trying to prove?"
    "I can't believe I'm thinking it, but maybe this project has run its course..."
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    pause 2.0
    jump Day6_TennisBot
