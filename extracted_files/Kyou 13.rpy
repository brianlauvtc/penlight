label Day13_Con_Kyou_Nozomi_Trance:
    scene bg k bedroom day with blink
    "I have no idea what's going to happen today."
    "Nozomi texted me to say she'll be here a little earlier than the others. I think she wants to say a few things to me first."
    play sound doorbell
    "Just then I hear the doorbell from downstairs. That must be her."
    scene bg k room day
    show Nozomi front casual concerned
    if hypno2 == "zombie":
        show Nozomi noglasses
    with blink
    play music Rain fadein 2.0
    if hypno2 == "trance":
        with dissolve
        n "{size=16}Hey, Sir...{/size}"
        "I notice right away that my conditioning the other day has held up; She's still quiet as a mouse in this house."
    elif hypno2 == "zombie":
        n "Hey." with dissolve
    ks casual neutral "Hey, Nozomi. How are you holding up?"
    if hypno2 == "trance":
        n sigh "{size=16}As well as can be expected, I guess. I'm so nervous.{/size}" with dissolve
        n "{size=16}What if they never want to speak to me again?{/size}"
    elif hypno2 == "zombie":
        n sigh "As well as can be expected, I guess. I'm so nervous." with dissolve
        n "What if they never want to speak to me again?"
    ks sigh "Do you really think that will happen?"
    if hypno2 == "trance":
        n side sad_side "{size=16}I... I don't know, Sir. We've been friends for so long, but this is the kind of thing that changes how people see each other.{/size}" with dissolve
        n sad_closed "{size=16}So I really don't know...{/size}" with dissolve
        n sad "{size=16}Anyway, I came here early because I wanted to ask you something.{/size}" with dissolve
        ks neutral "What's that?"
        n front frown "{size=16}I... I need you to remove the hypnotic suggestions you've given me.{/size}" with dissolve
        "I raise an eyebrow at her."
        ks "You know the suggestions I gave you the other night won't work if your friends are here, don't you?"
        n concerned "{size=16}I know... but that's not what I mean.{/size}" with dissolve
        n side sad_side "{size=16}I need all of them gone, Kyou. Everything we've been doing since we got started.{/size}" with dissolve
        ks surprised "Huh? Really?"
        n frown "{size=16}Yes. Really.{/size}" with dissolve
        n front neutral "{size=16}We've done so many things with my head that I have no idea what influences you've exerted on me without either of us realizing.{/size}" with dissolve
        n concerned "{size=16}And I really need a clear head before I talk to my friends. I can't let any of your hypnosis affect me when they're already worried about me.{/size}" with dissolve
        n sleep_concerned "{size=16}So please, Kyou?{/size}" with dissolve
        "Before I might have thought she was silly for worrying."
        "I mean, surely she wouldn't let this stuff affect her for something as important as this?"
        show Nozomi concerned
        "But as I reach out to hold her shoulders, I think back to how quickly and easily she took to every single thing I suggested to her..." with dissolve
        if gesture == "hand":
            "I nod my confirmation, and she nods back at me, as I recall how unplanned it was that she responded to my hand-waving suggestion in her house."
        elif gesture == "forehead":
            "I nod my confirmation, and she nods back at me, as I recall how unplanned it was that she responded to my forehead-poking suggestion in her house."
        "What if she hadn't meant to go along with that as I thought?"
        "And as I lean in and talk gently to her ear..."
        ks neutral "Alright, Nozomi. [hypno3]."
        show Nozomi sleep
        "I see once again, as her head drops at my word, how effortlessly she reacts to my every hypnotic suggestion." with dissolve
        ks "That's right, Nozomi. Dropping deep, deep asleep. Back into this pleasant state of hypnotic trance."
        ks "Feeling so good... And as you drift into this pleasant state of relaxation I'd like you to recall the suggestions I've made to you in the past."
        ks "And as you recall each one, I want you to imagine them effortlessly slipping out of your mind, so that they no longer have any influence over your thoughts or actions."
        ks "The phrase \"[hypno3]\" will no longer bring you back into this blissful state of trance, no matter who says it or where."
        if gesture == "hand":
            ks "And you will no longer feel your thoughts affected in any way if I or anyone else waves their hand in front of your face."
        elif gesture == "forehead":
            ks "And you will no longer feel your thoughts affected in any way if I or anyone else presses their finger to your forehead."
        ks "There is nothing that I have said during our trances that will have any influence over your thinking in any way."
        ks "Do you understand, Nozomi?"
        n sleeptalk "Yes..." with dissolve
        show Nozomi sleep
        ks "Alright. Now on three, you're going to awaken feeling nice and refreshed, knowing every suggestion I placed in your mind has completely gone." with dissolve
        stop music fadeout 10.0
        ks "One... taking a nice deep breath, feeling yourself start to wake."
        ks "Two... head lifting now, thoughts returning."
        ks "And three, wide awake and refreshed, Nozomi."
        n sleepy "Uhh..." with dissolve
        "I keep hold of her shoulders as she steers herself back into consciousness."
        ks smile "Hey. You okay?"
        show Nozomi smile
        "She blinks a few times and smiles as she registers me." with dissolve
        n "Yeah... I'm fine."
        show Nozomi surprised
        play sound doorbell
        "The sudden ring of my doorbell startles us both." with dissolve
        n "Ah, they're already here..."
        ks frown "Oh... Yeah, I tried to be thorough with you just now so I took my time."
        n frown "Hm, right..." with dissolve
        ks "Can I try something real quick, though?"
        n neutral "What is it? My friends are right outside." with dissolve
        if gesture == "hand":
            show Mindtrick awake wave at center:
                ypos 0.6
            "I smile at her and wave my hand casually in front of her puzzled face." with dissolve
        elif gesture == "forehead":
            show Mindtrick awake poke at center:
                ypos 0.6
            "I smile at her and casually press my fingertip to her forehead, which she eyes me curiously for."
        "This won't take a moment, but I think we need to confirm this."
        ks smirk "You will buy us all pizza."
        hide Mindtrick
        n angry "U-uh, I will do no such thing!" with dissolve
        play sound doorbell
        show Nozomi side surprised_side at flip
        h "{size=16}Hey, asshole! What're you doing with Nozo?!{/size}" with dissolve
        show Nozomi surprised
        "Nozomi's eyes dart to the door, before looking back to me with a chuckle." with dissolve
        n smile "Just let them in, okay?" with dissolve
        # n "{size=16}Set me free.{/size}"
        # ks surprised "Huh?"
        # n smile "Eheh, sorry Kyou, but I need to be in my right mind for this~" with dissolve
        # ks smile "Eh, I specifically made sure my suggestions wouldn't work while we had company."
        # n front concerned "Maybe not, but still, I just realized I have no idea what other influences you might have exerted on me without either of us realizing." with dissolve
        # n "I can't have any of that effect me right now."
        # play sound doorbell
        # n pout_left "... You should probably get that." with dissolve
    show Sayori casual neutral_right at left, flip:
        xpos 0.1
    show Hiroko casual frown no_arm at center:
        xpos 0.75
    hide Nozomi
    show Nozomi front concerned casual_folded at center:
        xpos 0.5
    with blink
    play music Monologue
    s "So. Here we are."
    h dress_arm frown_side "C'mon, let's get this over with. What's going on with you two?" with dissolve
    n side casual sad_side "Alright, so..." with dissolve
    n "While I was cleaning the classroom with Kyou last week, he told me something interesting."
    n "He told me he was studying hypnosis."
    h neutral_side "Hypnosis?" with dissolve
    s neutral "And that is interesting to you?" with dissolve
    n sad_closed "Well..." with dissolve
    n blush "It's like... a hobby of mine? K-Kinda? So..." with dissolve
    show bg blackscreen onlayer toplayer with fade
    "Nozomi went on to try and explain everything that happened between us over the last couple weeks."
    "All our arranged hypnosis sessions, and the kinds of things we'd do in those sessions..."
    "She didn't mention every little detail, but her friends must have heard enough to get the gist of what we were doing."
    hide bg blackscreen onlayer toplayer
    with dissolve
    pause 0.5
    # s casual_folded concerned "Alright... I need a minute to process this." with dissolve
    s casual_folded concerned "Alright... This will take a minute for me to process." with dissolve
    h casual no_arm concerned "So like, Kyou's seriously been controlling your mind?" with dissolve
    h sad_side "All this weird shit you've been pulling was 'cuz of him?" with dissolve
    n front sigh "Well, that's... It's complicated." with dissolve
    h frown_side "Complicated how?" with dissolve
    show Nozomi side frown_side at flip
    n "We didn't know Kyou's hypnosis would work as well as it did. But still..." with dissolve
    n sad_side blush "I can't deny how much I WANTED it to work." with dissolve
    # h "Oh man... Nozo, don't you get it?"
    # n "Huh?"
    # h "Like... You say you wanted it? But like, how much do you think HE wanted it?"
    # h "He must've made you wanna do all this weird shit


    h sleep "So, uh... so what're you tellin' me, Nozo?" with dissolve
    h neutral_side "You broke your promise with me 'cuz you fancied playing cops and robbers with your stalker?" with dissolve
    n frown_side "N... N-No!" with dissolve
    h casual_armup angry_side "Like, {nw}" with dissolve
    extend "SERIOUSLY? {w=0.5}You let this creepy son of a bitch put his hands on you? After all the skeevy shit he pulled on us?" with vpunch
    "... I really want to say something here, but I should probably stay out of this."
    hide Nozomi
    show Nozomi front casual sigh at center
    n front irritated "Ugh, this is why I didn't want to say anything. I KNEW you'd get the wrong idea." with dissolve

    h furious_side "How else am I s'posed to take it if you don't tell me shit?" with dissolve
    h "Like... I don't GET you! You KNOW what that tourney meant to me. That's my life right there."
    h "And I gotta accept you knew all that and you still ditched me for {nw}"
    show Nozomi pain
    extend "THIS motherfucker?!" with vpunch
    h "Tell me he fucked with your head, Nozomi. TELL me he made you do it!"
    n cry "I... H-Hiroko-{w=1.0}{nw}" with dissolve
    h "Just TELL ME!"
    show Hiroko frown
    show Sayori neutral_right
    ks angry "Yeah, it was me. It's all MY fault!" with dissolve
    "Guess I couldn't keep my mouth shut after all."
    show Nozomi concerned
    show Hiroko casual
    "But I can't bear to see Nozomi getting laid into like this. And besides..." with dissolve
    ks frown "You remember, Nozomi? Back at your place?"
    if gesture == "hand":
        ks "Right before I left, I waved my hand across your face..."
    elif gesture == "forehead":
        ks "Right before I left, I pressed a finger to your forehead..."
    ks "And I made you want to come visit me the next day."
    "I sigh as I shake my head to myself."
    ks sigh "Knowing what we do now, it's obvious what happened isn't it?"
    n sleeptalk_concerned "Kyou..." with dissolve
    ks "I made you ditch your plans so you'd spend the whole weekend with me, and I used your post-hypnotic suggestion to do it."
    ks "And not only that..."
    show penlight at right with moveinright:
        ypos 0.346
    "I then pull out the penlight from my pocket for all to see."
    show Nozomi concerned
    ks frown "I gotta think about everything I did with you using this thing." with dissolve
    h frown_side "So that's the thingy you were talking about, Nozo?" with dissolve
    "Nozomi blinks at it for a moment, then nods wearily."
    n sigh "Yes. That's what we used to hypnotize me." with dissolve
    s "What is so special about it? It looks like a cheap penlight."
    hide penlight at right with moveoutright
    ks frown "It is, mostly. I was able to modify the beam to make it more... attention-grabbing? But after everything I have to admit it does way more than that."
    ks "It must be doing something else that I didn't consider. Something that makes the subject more suggestible and silences the \"hidden observer\" effect."
    h angry "The fuck're you talking about? \"Hidden observer\"?" with dissolve
    show Hiroko frown_side
    n pout_left "Uh... W-well, it's like how even when you're hypnotized there's still a part of you that's aware of everything that's happening?" with dissolve
    n sigh "So if your hypnotist tries to suggest something unethical or just something you disagree with..." with dissolve
    n neutral "You still have the ability to ignore the suggestion, or explicitly reject it." with dissolve
    ks frown "But the other night I started to realize that wasn't happening. It felt like I could do anything to your mind and there would've been nothing to stop me."
    h shocked "S-seriously?! Th-... that's..." with dissolve
    ks sigh "Yeah. That's why this is all on me. I really did make her do it. So don't take it out on her."
    "Rather than lay into me like I expected, Hiroko just turns to her friend with a scared look on her face."
    h sad_side "Like, holy shit, was it really worth getting mixed up in this, Nozo?" with dissolve
    show Nozomi side sad_side at flip
    n "Hiroko, I know how it sounds. And believe me, if I truly knew what I was getting myself into I never would have agreed to this." with dissolve
    s neutral "... Wouldn't you?" with dissolve
    hide Nozomi
    show Nozomi side casual sad_side
    show Hiroko surprised_side
    n "Ah..." with dissolve
    "Sayori's been quiet for most of this, so everyone seems a little startled when she speaks up."
    s casual irritated "Honestly, I do not think I am awake enough for this. But still, there were a few details in all of this that stood out to me." with dissolve
    s neutral "If we set aside for a moment the absurdity of Kyou possessing a device that can literally shape people's thoughts to his will..." with dissolve
    s rolleyes "Something that has eluded world governments with resources far outstripping an underachieving high-school student, I should add." with dissolve
    # s neutral "Let us say we accept Kyou's confession and this absurd premise that he possesses a device that can literally shape people's thoughts to his will." with dissolve
    # s neutral_right "Such a thing has eluded people with far greater intellect and resources than an underachieving high-school student, but let's go with it for now." with dissolve
    # s neutral "Even accepting Kyou's confession, there is still the manner in which you both started this insanity." with dissolve
    h casual_armup angry_side "Agh, get to the POINT, will you?" with dissolve
    s frown "My point, is that Nozomi told us that her being hypnotized and put in compromising situations was effectively HER idea." with dissolve
    s casual_folded concerned "And as much as I would love to accept Kyou having full responsibility for this mess, I cannot overlook Nozomi having an active role in it." with dissolve
    h furious_side "For fuck's sake, Sayori! You WANNA take his side?" with dissolve
    s irritated "Ugh. I am not taking sides. I am trying to get my head around this." with dissolve
    s frown "But Nozomi... I have never known you to be so foolish." with dissolve
    n front pain "Agh..." with dissolve
    h "YOU TAKE THAT BACK!" with shake
    n sleeptalk_concerned "N-no... Hiroko, she's right." with dissolve
    "Nozomi begins to weep as she covers her face."
    n frightened blush "I'm stupid. I've been so STUPID!" with dissolve
    show Hiroko casual sad_side
    show Sayori concerned
    n "*sniff* When I found out Kyou was studying hypnosis, I wanted to be a part of it so badly." with dissolve
    n side sad_side "I thought I was being careful. We were just going to talk about hypnosis somewhere safe, somewhere public." with dissolve
    n sad "But when Kyou suggested coming here to try it out, it's like I couldn't stop myself." with dissolve
    n sad_closed "And after that first time, I knew I wanted more. It was a bigger thrill than I could've imagined." with dissolve
    n "And s-sure, maybe his penlight was doing things to me that I couldn't control. Maybe it was affecting my judgement."
    n front sleeptalk_concerned "But there was no penlight making me eager to follow Kyou to his house. And everything... e-everything we did together..." with dissolve
    n cry "I wanted it. I wanted all of it, I know I did!" with dissolve
    h "But why, Nozomi?"
    n frightened "Because it was the only way for me to FEEL anything!" with dissolve
    show Sayori surprised
    h surprised_side blush "U-uhh?!" with dissolve



    # s frown "My point, is that even accepting all of this, Kyou's penlight was not a factor in your first interactions. Was it, Nozomi?" with dissolve
    # n sad_closed "It wasn't..." with dissolve
    # s casual_folded surprised "So what on earth possessed you to follow Kyou of all people back to his home after a short chat?" with dissolve
    # show Hiroko casual surprised_side
    # ks "\"Of all people\"?" with dissolve
    # s frown_right "Shush." with dissolve
    # n sad_side "It was a good chat. A-and it was just going to be harmless fun, so- {w=1.0}{nw}"
    # h sad_side "You seriously just want over there? To creepy Kyou's house?" with dissolve
    # s concerned "Hobby or not, it strikes me as somewhat... reckless." with dissolve

    #... But I did. Nozomi starts her confessional here? Blaming herself for being too eager at the start when there was no penlight to blame
    # Then going on to talk about her hypnofetish and how it put herself in danger and it's all her fault
    # Friends console her, Sayori suggests she was moving too fast and Hiroko doesn't care that she's into weird shit. She just wants her to be happy and safe.
    #You took things too far, and you definitely  went too fast


    # ks "Every single one of our hypnosis sessions, you absorbed my every suggestion so completely, every time."
    # ks "We were so caught up in how how well this stuff worked that we didn't stop to think why it was going so well."
    # ks "So it's clear that I didn't understand how powerful this was. You even tried to warn me in your own way."





    # ks "It really is all my fault, Nozomi. I was your hypnotist, and I should've realized what this was doing to you."
    #
    #
    # show Nozomi side sad
    # ks "So much so that it lessened your inhibitions and made you want to stop taking precautions. I should've realized what I was doing to you."  with dissolve
    # ks "I truly am sorry, Nozomi."
    # show Hiroko frown
    # "The room falls silent for a while, although everyone's eyes are drawn to the penlight in my hand, before Sayori speaks up." with dissolve
    # hide penlight at right with moveoutright
    #
    #
    # h "We were {nw}"
    # extend "WORRIED about you, Nozo!" with vpunch
    # show Nozomi pain
    # h "You really weren't gonna tell us anything?" with dissolve
    # h "Why couldn't you tell {nw}"
    # extend "ME!?" with vpunch
    # show Nozomi side sad_side at flip
    # n "I-I couldn't!" with dissolve
    # h "Why the fuck not?!"
    # ks angry "You think she could talk to you about any of this?"
    # show Nozomi sad
    # show Sayori concerned_right
    # show Hiroko casual angry
    # "Guess I can't hold it in anymore." with dissolve
    # h "YOU stay outta this!" with vpunch
    # # ks angry "Because she's scared!"
    # ks frown "No. If you want to be mad at someone, be mad at me."



    n "How... h-how was I supposed to tell you this?"
    # show Hiroko angry_side
    show Nozomi side at flip
    n sad_side "I-I was supposed to tell you I get turned on by feeling like my mind isn't my own?" with dissolve
    n sad_closed "That I was so desperate to experience it, I'd even approach someone we didn't trust if he could give it to me?" with dissolve
    # n blush "That I'd meet up with someone we didn't trust and put my mind in his hands because I was so desperate to experience it?" with dissolve
    hide Nozomi
    show Nozomi casual front cry blush at center
    show Hiroko neutral_side
    show Sayori casual
    n "I-It's SO stupid! So... messed-up! Don't think I don't know that!" with dissolve
    # n "I-I know it's messed-up. I KNOW! A-and I don't know what's wrong with me that I'm being so stupid." with dissolve

    # to be... t-to be dominated like this? You don't think I know that's messed-up?" with dissolve

    n frightened "I'm such a freak!" with dissolve
    h "..."
    h casual surprised_side noblush "... Huh?" with dissolve
    s "What I believe Nozomi is trying to say is..."
    s casual sleeptalk "Well..." with dissolve
    s blush "She is something of a thrill-seeker." with dissolve
    h frown "..." with dissolve
    h neutral_side "Yeah. I got that." with dissolve
    show Sayori concerned noblush

    h sad_side "But... So fucking what?" with dissolve
    show Nozomi side sad_side at flip
    n "W-What?" with dissolve
    h sleep "Like... For real, Nozo, I always thought you were kinda weird." with dissolve
    h surprised_side "NOT in a bad way or nothin'!" with vpunch
    h frown_side "Just... I dunno, you keep trying to come off as this totally normal chick but I always knew that was bullshit." with dissolve
    h sad_side "Had to be something else going on." with dissolve
    h "Didn't know what your deal was exactly, but... I liked it."
    h sleep "So Nozo, it don't matter if you're into some freaky shit. I don't care about that." with dissolve
    h sad_side "Just... I dunno, don't be stupid, okay?" with dissolve
    n sad_closed "*sigh* Yeah..." with dissolve
    show Hiroko neutral_side
    n "When Kyou opened up to me and finally started talking, we had a connection." with dissolve
    n sad_side "And even though I put myself in all these vulnerable positions with him, I never felt he was taking advantage of me." with dissolve
    n sad "So what do you think that says about him?" with dissolve
    h "Hmm..."
    show Hiroko neutral
    "As Hiroko seems to ponder what was said, I can feel her large green eyes bore into my soul." with dissolve
    s casual_folded concerned_right "Honestly, it sounds like you got in over your heads." with dissolve
    s frown "Perhaps if you had taken a more... analytical approach." with dissolve
    hide Nozomi
    show Nozomi front casual sleeptalk_concerned
    n "Yeah... I'm just so sorry for making you worry..." with dissolve
    #
    #
    # h "He still controlling your mind now?"
    #
    # n casual side sad_side "Uh, no. Like I said, he took me back into trance and undid everything we tried in our sessions." with dissolve
    # n sad "So Kyou doesn't have any hypnotic influence over my mind whatsoever." with dissolve
    # s frown "... Can you be so sure that is the case?" with dissolve
    # hide Nozomi
    # show Nozomi side casual sad_side
    # n sad_side "What do you mean, Sayori?" with dissolve
    # s "I admit I know little of hypnosis, so perhaps I am off base here..."
    # s casual_folded annoyed "But do you not think it possible that you merely BELIEVE everything has been undone?" with dissolve
    # s "Because what you have told us suggests he has had unfettered access to your mind."
    # #NOTE - Sayori should recall more things than just the name/number thing
    # if hypno1 == "count":
    #     s "He was able to make you forget something as fundamental as a number, and he can compel you to do things even if you actively resist."
    # elif hypno1 == "name":
    #     s "He was able to make you forget something as fundamental as your own name, and he can compel you to do things even if you actively resist."
    # s casual "According to you, his control of your mental faculties were so great that he could even compel you with nothing but a {nw}" with dissolve
    # if gesture == "hand":
    #     extend "wave of his hand."
    # elif gesture == "forehead":
    #     extend "touch on your forehead."
    # s frown_right "So tell me, what was stopping him from making you merely believe you're free of his control? Can either of you answer me that?" with dissolve
    # n frown_side "He didn't." with dissolve
    # "Nozomi cuts me off before I can answer."
    # ks "It's true though, isn't it? I didn't think about it to start, because we always thought you could protect yourself if I tried anything you didn't want."
    # show Hiroko casual sad
    # n front concerned casual "Kyou... It doesn't matter. Because I know you did nothing that I didn't want, or thought I didn't want." with dissolve
    # n "I trust you completely on this."
    #
    # ks neutral "Nozomi..." with dissolve
    # n frown casual_folded "It's true though, isn't it? I set us some groundrules, then I almost immediately walked them back." with dissolve
    # n "I was so eager to explore my desires I completely disregarded my own safety!"
    # n cry casual "God, I'm such an idiot. I really should've been more careful..." with dissolve
    # ks sigh "No. Nozomi, no, I was the one who should've been more careful."
    # ks "I was your hypnotist, and we were trying these things for the first time."
    # ks "I should've insisted we take it slower. At least until I knew what I was doing."
    # show penlight at right with moveinright:
    #     ypos 0.346
    # "I then pull out the penlight from my pocket for all to see."
    # show Nozomi concerned
    # show Sayori concerned_right
    # show Hiroko frown
    # ks neutral "Especially when I was using this thing." with dissolve
    # hide penlight with moveoutright
    # ks "I mean, it's clear that I didn't understand how powerful this was. You even tried to warn me in your own way."
    # h frown_side "That's the thingy you were talking about, Nozo?" with dissolve
    # n sigh "Yes. That's what we used to hypnotize me." with dissolve
    # s "What is so special about it? It looks like a cheap penlight."
    # ks frown "It is, mostly. I was able to modify the beam to make it more... attention-grabbing? But after everything I have to admit it does way more than that."
    # ks "It must be doing something else that I didn't consider. Something that makes the subject more suggestible and silences the \"hidden observer\" effect."
    # show Nozomi side sad
    # ks "So much so that it lessened your inhibitions and made you want to stop taking precautions. I should've realized what I was doing to you."  with dissolve
    # ks "I truly am sorry, Nozomi."
    show Hiroko frown
    "The room falls silent for a while, although everyone's eyes are drawn to the penlight in my hand, before Sayori speaks up." with dissolve
    s "To think that your secret little science project would cause so much trouble."
    s frown_right "There is a hidden genius in you, Kyou. Now if only you could start using it for good..." with dissolve
    "I let out a little chuckle in spite of myself."
    s "If that penlight is doing what you say it's doing, then it needs to go. It's too dangerous to keep around."
    show Hiroko frown
    n front frown casual_folded "Yes, I agree." with dissolve
    "I find myself reluctantly nodding my head as well."
    ks "You have to believe I didn't want to make you unsafe, Nozomi."
    show Nozomi smile
    "Nozomi smiles at me." with dissolve
    n "I do believe you."
    stop music fadeout 5.0
    show bg blackscreen onlayer toplayer with dissolve
    "So with everyone watching, I laid the penlight down on the living room table and started dismantling it in front of them."
    "As I did so, I couldn't entirely put out of my mind the things I was potentially letting go by doing this."
    "A penlight that let me reshape Nozomi's thoughts to my will?"
    "I kind of hate myself for it, but there's a part of me that regrets giving this up."
    "Not to mention the possibilities if it had worked on anyone else..."
    show Hiroko neutral
    hide bg blackscreen onlayer toplayer with dissolve
    "But before too long my thoughts became irrelevant, as the penlight lay in pieces on the table."
    # ks surprised "What?! I worked so hard on this. I realise it's dangerous, but do I really have to ditch it right now?"
    # ks "I mean, don't we want to know why it does what it does? There could be a research project in this. Or- {w=1.0}{nw}"
    # h casual_armup angry "YOINK!" with vpunch
    # "She just snatched the damn thing out of my hand!"
    # h "Just so you know, this is going in the fuckin' sea!"
    # show Hiroko frown
    # ks frown  "Goddamnit..." with dissolve
    play music Memories fadein 5.0
    s casual smile_right "I do not know what to make of this penlight's reputed ability, but I do feel a sense of relief now it's gone." with dissolve
    h neutral_side "So what now, Nozo?" with dissolve
    #
    # s "If you want us to start trusting you, Kyou, this is a good first step."
    # n concerned casual "I'm disappointed too, Kyou. But we need to be responsible. Who knows what would happen if we kept using that..." with dissolve
    # ks sigh "Yeah... Yeah, I know."
    # show Hiroko casual
    # "An awkward silence hangs in the room for a few moments, interrupted only by the sound of Hiroko slipping my penlight into her bag." with dissolve
    # s frown "You ARE going to destroy that thing, aren't you?" with dissolve
    # h angry_side "Of {nw}" with dissolve
    # extend "COURSE! Geez. You take me for an idiot?" with vpunch
    show Nozomi sigh
    "She draws a long sigh." with dissolve
    n "I think I'm going to give the hypnosis a rest. At least for now."
    show Hiroko frown
    ks concerned "Yeah..." with dissolve
    "I simply nod. I can't say I'm happy about all this, but after what's happened I can't fault her for wanting to take a step back."
    n surprised "These past few days have been so intense, a-and exciting, and I can't believe I got to experience it with you." with dissolve
    n side casual sad_closed "But knowing how helpless I truly was to your hypnosis does leave me a little shaken. Believe me, that wasn't exactly what I had in mind for us." with dissolve
    n blush "Still... although we had to stop this for our own safety... I-I don't exactly regret what we did." with dissolve
    n front sigh "A-anyway, you can all stop worrying now." with dissolve

    # n "I mean, fantasizing about this sort of thing and have it actually happen to you are two very different things."
    # n "And now that I'm thinking clearly again, it's left me a bit shaken to tell the truth."
    show Hiroko neutral_side
    s smile "Alright, Nozomi. I am relieved you've seen some sense." with dissolve
    show Sayori neutral
    n sleeptalk_concerned "And I'm SO sorry for all of this." with dissolve
    n "I made you both worry, and I got you mixed up in my nonsense. I was selfish chasing my desires so recklessly."
    show Hiroko sad_side
    show Sayori concerned
    n cry "You're both having to work so hard for your futures and I'm just... j-just bringing you down with this stupid crap." with dissolve

    s casual "Nozomi, come on. We all had to work hard this semester, don't sell yourself short like that." with dissolve
    h smile_side "Yeah, Nozo. We're still besties and you're clearly going through some shit. Don't worry about it~" with dissolve
    show Nozomi side casual sad_side at flip
    n "*sniff* Y-... You really mean that? Aren't you COMPLETELY weirded out by all this?" with dissolve
    h annoyed_side "I'm {nw}" with dissolve
    extend "SUPER weirded out by all this!" with vpunch
    h smile_side "But, like I said, so what? I can have a weird friend~ 'Sides, we're all weird in our own ways, right?" with dissolve
    s smirk "Do you want to tell us of your weird ways, Hiroko?" with dissolve
    h frown_side "Back the fuck off, lady." with dissolve
    show Nozomi smile
    s frown_right "So tell me, Kyou, is there anything else we should know about? Do you currently have any influence over Nozomi's mind at all right now?" with dissolve
    ks frown "Uh... I don't think so. I think I was pretty thorough in deprogramming her of all my suggestions."
    ks "And after everything else that's happened I don't have a reason to doubt that it worked."
    n frown noblush "Yeah. Since you did that I feel like... like a spell has been lifted? I don't know, but I do feel like my mind's completely my own again." with dissolve
    s "Alright, so how about this: We take you at your word, Kyou, that Nozomi is no longer under your hypnotic influence. But we will be watching."
    s "If Nozomi exhibits any unexplainable behaviour, we'll know who to come to and-{w=0.8}{nw}"
    show Nozomi surprised_side
    h casual_armup angry no_arm "We'll {nw}" with dissolve
    extend "KILL you!" with vpunch
    s concerned casual_folded "... Well, I wouldn't go that far, but whatever works." with dissolve
    ks "Nozomi won't be in that kind of danger again, I promise."
    n laugh "Ehehe... thanks for looking out for me, you two~ {font=DejaVuSans.ttf}♥{/font}" with dissolve


    scene bg blackscreen with fade
    stop music fadeout 5.0
    "I... think we worked things out?"
    "I doubt either of Nozomi's friends truly get the appeal of what we've been doing, but they seem to accept that the penlight was the only real danger."
    scene bg k room day
    if hypno2 == "trance":
        show Nozomi front casual smile
    elif hypno2 == "zombie":
        show Nozomi front casual smile noglasses
    with blink
    # play music Moment fadein 1.0
    play music Luminous_Rain fadein 1.0
    "As her friends leave, I turn to Nozomi with a smile."
    ks casual smile "Wasn't so bad, right?"
    show Nozomi chuckle
    "She chuckles." with dissolve
    n "Easy for you to say, but it went a lot better than I feared."
    ks "Yeah. I sort of envy you having friends like that."
    n happy "Heh. So what now? I mean, unlike them I don't have any plans for today." with dissolve
    ks neutral blush "Well..."
    "I turn it over in my mind and, after everything that's happened, I think there's something we really need to discuss."
    ks concerned "What now for US, do you think?"
    n surprised "\"For us\"?" with dissolve
    ks "Nozomi, I know what you said before, about not wanting to date anyone."
    n side sad_side "..." with dissolve
    ks "But... I dunno. We've been through a lot together since then."
    n "We have..."
    ks smile "I mean, we've been around each other for years, but... these two weeks..."
    show Nozomi smile
    "I trail off, a lump in my throat, but Nozomi smiles and finishes my thought for me." with dissolve
    n "It's like we've gotten acquainted for the very first time."
    "It's great to share a moment with her like this. But..."
    n smile_side "Kyou..." with dissolve
    "I can see the sadness in that smile."
    n sad_closed "..." with dissolve
    n sad "That's the problem, isn't it? I can't know how I feel after two weeks." with dissolve
    n "So I haven't changed my mind."
    "I guess I'm not surprised, especially more so as it dawns on me."
    "She got what she wanted, didn't she? We explored her fantasies further than she could've dreamed of doing."
    "But with the penlight gone... what use am I to her?"
    n front sigh "But, Kyou... please listen to me." with dissolve
    n side sad_side "Maybe I'm not attracted to you. It's hard for me to say..." with dissolve
    n sad "Because I don't think I've been attracted to anyone." with dissolve
    ks surprised "H-Huh?! Seriously?"
    n front irritated "Ugh, I don't know. I guess I don't really think about it too much?" with dissolve
    n annoyed_left "And when I decided not to date while in high school I didn't have to think about it at all." with dissolve
    n "So... It's difficult."
    n concerned "I just really hope you don't take it personally, that's all." with dissolve


    # n front concerned "I really meant it when I said I wasn't interested in dating anyone at high school." with dissolve
    # n sigh "It's like I said at the start. I'm not interested in dating anyone in high school." with dissolve
    # "She shrugs."
    # n concerned "It might not be what you want from me... but I just don't feel that way about you right now." with dissolve
    # n side sad "But Kyou, I..." with dissolve
    # n side sad_side "I don't know if I feel that sort of way about anyone..." with dissolve

    n side sad_closed "And, listen... Maybe we can't do what we've been doing anymore..." with dissolve
    n laugh "But who else am I going to talk to about hypnosis?" with dissolve #Not immediately, but maybe after dust has settled on the penlight stuff
    n front smirk "Not to mention, I want a rematch with the \"king of the settlers\"." with dissolve
    n chuckle "Plus you still need to tell me about \"those little circuit board computers\"." with dissolve
    ks surprised "Those... o-oh, right."
    n side sad_closed "Because Kyou, there's something else I haven't changed my mind about..." with dissolve
    ks surprised noblush "What's that?"
    n smile "I still want you in my life~" with dissolve
    n side sad "But... what do you think?" with dissolve
    n sad_side "After all this, can we..." with dissolve
    n front concerned "Can we be friends?" with dissolve
    stop music fadeout 5.0

    #So what do you think? Can we be friends?

    # " ((Script edits end here currently. What follows is just the original ending scene with no changes.))"

    # ks concerned "There's something I've been meaning to ask you."
    # n side sad "Oh? What is it?" with dissolve
    # ks "Well, I mean er... You're not seeing anyone are you? Romantically, I mean?"
    # n "Oh, um... no, Kyou. I'm not."
    # ks smile "... Would you like to?"
    # stop music fadeout 5.0
    # n smile "..." with dissolve
    # n "I should've seen this coming, shouldn't I?"
    # show Nozomi:
    #     linear 0.8 ypos 1.1
    # "I let out a nervous chuckle as she gestures for us to sit on the couch."
    # show Nozomi:
    #     ypos 1.1
    # play music Eons
    # n "This week with you has been fun, I admit."
    # n front pout_left "Mostly terrifying in retrospect, but fun~" with dissolve
    # n "Still..."
    # n concerned "When I entered into this arrangement with you, I never considered it beyond being a shared hobby." with dissolve
    # n "Wasn't that naive?"
    # ks smile "Honestly? Yeah, kinda."
    # ks "I mean, even from the beginning you were talking about getting off on this stuff. You really didn't think more would come from what we were doing?"
    # n sigh "I know. When you gave me the opportunity to do this, I really didn't think much beyond that." with dissolve
    # n surprised "I even overlooked the fact you made that stupid penlight just so you could hypnotize girls! And ME in particular!" with dissolve
    # n concerned "And when I think now about how effective that thing was, that really has some sinister implications, doesn't it?" with dissolve
    # ks neutral noblush "Uhh... Yeah..."
    # show Nozomi sigh
    # "Nozomi sighs." with dissolve
    # n "Look, even if I didn't have that to think about, I still wouldn't date you."
    # n concerned "I'm just not looking for a relationship right now. I wanted to focus on getting to college before I did anything like that." with dissolve
    # n "And since we're graduating soon, it makes sense to stick to the plan, don't you think?"
    # ks "Yeah. I understand."
    # ## Below needs work
    # n sigh "Sorry..." with dissolve
    # ks "No, it's okay. I think I needed to hear that."
    # "I guess I always knew that would be her answer."
    # "At least now, I think I can accept it."
    # ks "Hey, Nozomi?"
    # n neutral "Yes, Kyou?" with dissolve
    # ks smile "We can still be friends though, right?"
    # show Nozomi smile
    # "Nozomi lets out a little chuckle." with dissolve
    # n "We can~"
    stop music fadeout 5.0
    $ending = "friendship"
    jump Epilogue_Con_Kyou_Nozomi


#Nozomi goes to Kyou's house at the end of the day, although Kyou wasn't certain she would
#He expresses his frustrations to her about her rule of not being near her at school and she asks if he'd
#Like to "take it out on her" while she's in her house, within reason obviously oh my god!
#Although she says the part of her that wants to continue this with Kyou is warring with the part of her that wants to run and not look back
#She asks him to use the sleep trigger he gave her yesterday to prove the point that she's "helpless" in his house
#so long as he doesn't do anything stupid, although he could activate the trigger while she's standing so she falls into his arms asleep perhaps
#It really does work very well, and further proves her point. Anyway, she sets some more rules saying anything goes so long as he's not trying to make
#her have sex with him or take his influence outside the house, because she'll totally resist that (and maybe they still believe she can at this stage
#since everything they've done so far has been pretty innocent).
#Sayori line I just thought of: "I do not think I am awake enough for this..."
#Dramatic final scene - Nozomi will probably blame herself for getting too invested in her hypnosis fetish, pointing out that she approached Kyou first despite
#Finding him creepy before, without the penlight's influence
