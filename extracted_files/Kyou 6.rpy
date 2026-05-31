label Day6_NonCon_Kyou:
    scene bg k bedroom day with longdissolve
    "9:52. It's almost time."
    "Pacing around my bedroom, I try to make myself relax."
    "I even toyed with the idea of trying to hypnotize myself with my penlight, but quickly dismissed such a stupid idea."
    "Instead I've been going over what I might say to her, over and over, while practicing my skill at directing the penlight from different positions in my hand."
    "Maybe I'm being paranoid, but at least it occupies my time."
    play sound doorbell
    "That's the doorbell... Okay, Kyou. Relax. It's showtime."
    "Just you and her. You got this."
    scene bg k entrance day
    show Nozomi front happy casual at center
    play music Beautiful
    with blink
    ks casual frown "It's... great to see you, Nozomi."
    n laugh "Aww, you too, Kyou~ " with dissolve
    ks "But I have to ask..."
    if pursued == "Hiroko":
        show Sayori casual at center:
            xpos 0.75
        $multichar = "Nozomi and Sayori"
        show Nozomi smile
        stop music fadeout 5.0
        queue music Piano_Mood
        ks "Why is Sayori here too?" with dissolve
        s neutral_right "And a top of the morning to you as well, Kyou." with dissolve
        show Nozomi side smile at flip
        n "Okay, so I was talking to Sayori before heading home yesterday and she asked what I was doing tomorrow." with dissolve
        n smile_side "So I said \"I'm going to Kyou's to study\", and she was like \"Can I come with?\" and I was like \"Sure!\"" with dissolve
        hide Nozomi
        show Nozomi front2 casual smile at center
        n "Maybe that was presumptuous of me, but when you suggested it the other day it was an open invitation to everybody, right?" with dissolve
        ks confused "Right... Yeah, but Sayori, don't you have cram school?"
        n surprised "That's EXACTLY what I said! I said \"But Sayori, don't you have cram school?\"" with dissolve
        n "And she was like- {w=0.5}{nw}"
        s casual_handup smile "Yes, but I could do with a change of scenery now that I think of it." with dissolve
        n smile "And so, um...  here we are!" with dissolve
        n happy "Surprise!" with dissolve
        s smile_right "Yay." with dissolve
        show Nozomi laugh
        "I don't fucking believe this." with dissolve
        n smile "So where are we doing this? In there? {w=1.0}{nw}" with dissolve
        show Nozomi surprised
        $ renpy.transition(dissolve, layer="master")
        extend "Oooh, what about in your room?"
        ks "Err, I was thinking- {w=1.0}{nw}"
        show Nozomi neutral_right
        s casual_folded smile "Now that I think of it, have you ever been in a boy's bedroom before, Nozomi?" with dissolve
        show Nozomi side casual frown_side at flip
        n "As a matter of fact I have, thankyouverymuch!" with dissolve
        s smirk "Your little brother's doesn't count." with dissolve
        n sad "Oh..." with dissolve
        s happy "Let us see if we can find it." with dissolve
        show Nozomi laugh casual:
            linear 2.0 xpos 1.5
        show Sayori:
            linear 1.0 xpos 1.5
        "And before I can register what's happening, the pair of them push past me and head up the stairs, chattering excitedly."
        ks surprised "Hey wait, don't go up there!"
        scene bg k bedroom day
        show Nozomi front casual happy at center
        show Sayori casual_folded smile at center:
            xpos 0.75
        with blink
        "They ignored me completely, and pushed open the half-open door that clearly belonged to my room."
        show Nozomi smile
        show Sayori casual_handup neutral
        stop music fadeout 10.0
        "And as they enter, their heads turn, casting their eyes quickly over the bed, the floor, the computer with a dozen tabs of hypnosis instructional videos..." with dissolve
        show Nozomi neutral
        show Sayori frown_right
        "The stack of printed out hypnosis scripts on the table..." with dissolve
        n "I knew it."
        s "Unbelievable. So he really..."
        ks casual surprised "Wait, how did you...?"
        "They already knew about this?"
        play music Rain
        n front2 determined "Do you think we're stupid, Kyou? I've known Hiroko since junior high, but even if I hadn't did you seriously think we'd not notice something amiss?" with dissolve
        ks frown "I don't know what you're- {w=1.0}{nw}"
        s casual_folded irritated "He is likely too arrogant to think we'd suspect anything." with dissolve
        n frown "Yeah. I mean, it's not every day one of your classmates brainwashes your friend with some hypnosis scripts he read off the internet." with dissolve
        show Nozomi chuckle
        "She follows that up with a short, bitter chuckle." with dissolve
        n irritated "It's utterly insane when I say it out loud." with dissolve
        n neutral "But that's what happened to Hiroko, isn't it, Kyou?" with dissolve
        "My hand slips itself into my pocket, cradling the penlight inside as I decide how I feel about what's developing here."
        "What she's saying IS insane. You can't brainwash someone with a little hypnosis for fuck's sake."
        s frown_right "If you had any respect for us at all, you would confess." with dissolve
        n frown "I don't think he ever respected us, Sayori." with dissolve
        "Swallowing hard, I'm forced to consider my options. Do they really believe what they're saying here?"
        "They must have seen my hand in my pocket by now, still gripping the penlight, but neither of them seems especially alarmed by that fact."
        "How much do they know?"
        ks frown "As you say, it's insane to even suggest such a thing. So what makes you think I hypnotized and... \"brainwashed\" Hiroko with..."
        "I gesture across to the table of printouts."
        ks "That?"
        n angry "Because you also hypnotized and brainwashed ME, Kyou." with dissolve
        ks confused "Huh? That's even MORE insane! A-and besides you should've f..."
        ks "Er, I mean- {w=0.5}{nw}"
        show Nozomi side frown at flip
        n frown "What, Kyou? I should've forgotten I was hypnotized? That's what you were going to say, right?" with dissolve
        n irritated "Because I really have been forgetting a lot of things when I've been with you this week." with dissolve
        hide Nozomi
        show Nozomi casual front2 frown
        n "Like when we were cleaning up the classroom on Monday? I don't know how you pulled it off, but I seriously don't remember a thing." with dissolve
        n determined "That WAS when all this started, wasn't it?" with dissolve
        ks frown "Right... in the classroom."
        s frown "It lines up. We noticed you were acting strange around him the very next day." with dissolve
        show Sayori frown_right
        n neutral "That day it felt like I had the hardest crush on you, Kyou. I'd never felt that way about anyone before." with dissolve
        n neutral_right "I didn't understand where that came from, and for a while I didn't want to." with dissolve
        n sleep "And even now, knowing you somehow did this to me, I still feel this attraction to you." with dissolve
        n concerned "That TERRIFIES me. I know a thing or two about hypnosis, and what you did to me and Hiroko shouldn't even be possible." with dissolve
        "The frustration welling up inside me is getting unbearable. She is THIS close to realizing and she doesn't even know it."
        "I have to set her straight."
        show Nozomi frown
        ks surprised "But Nozomi, that's it! Don't you see? For any of this to have worked at all there MUST have been something there." with dissolve
        ks "This attraction you feel for me? Hiroko's desire to be a better person? It was inside you both all along!"
        ks "Even the fact that you forgot all about this until now was down to your own wants, Nozomi. You agreed to play along with me and forget."
        ks "Because you see, you can't control minds or anything like that. For any of what I did to work there had to be something for me to work with."
        show Nozomi irritated
        ks "Something in you both that said you WANTED to be hypnotized, that you WANTED to be convinced." with dissolve
        ks "All I really did was bring your true thoughts and feelings out into the light."
        n determined "What on {w=0.3}{nw}" with dissolve
        extend "EARTH are you talking about? There was no attraction between us, Kyou?!" with vpunch
        n irritated "We never talked! We never spent any time together that wasn't you pathetically hovering around me hoping I'd notice you." with dissolve
        n side irritated "To say nothing of all the times I caught you leering at me from afar when you thought you were being discreet." with dissolve
        s irritated "If there is any attraction to be discussed here, it is distinctly of the one-sided and voyeuristic sort." with dissolve
        n sad "And Hiroko..." with dissolve
        show Sayori concerned
        n front2 sleeptalk_concerned "Oh my god, Hiroko..." with dissolve
        s casual_handup concerned_right "You... you really did a number on her, didn't you." with dissolve
        ks confused "What the hell do you mean?"
        s sleeptalk "She has lost her spirit. Her determination. Her drive to succeed." with dissolve
        show Sayori frown_right
        "I snort through my nose. They really didn't listen to a thing I said, and they're being so fucking ridiculous about this." with dissolve
        ks frown "All I did was tell her to stop being so damn angry all the time. That's not who she is."
        n side frown "Ever since I met her she's dreamed of becoming a professional tennis player. But now? She doesn't care!" with dissolve
        n furious "Right now she's happy to throw everything she's ever worked for in the garbage because \"it makes me angry and I can't be angry anymore\"." with dissolve
        ks "Did you consider she might be right about that? It doesn't sound like tennis was a good fit for her anyway if it worked her up so much."
        n front2 angry "Oh, you {w=0.2}{nw}" with dissolve
        show Sayori concerned
        extend "FUCKING ASSHOLE!{w=1.0}{nw}" with shake
        n irritated "..." with dissolve
        "Nozomi sucks in a breath before continuing. I can barely stand to see her so wound-up, especially over something she's so obviously wrong about."
        show Sayori frown_right
        n frown "Alright, you're not listening. I wasn't expecting you to anyway." with dissolve
        ks confused "Nozomi look, I... I realize how this might look, and that you couldn't possibly understand what I'm doing. But- {w=1.5}{nw}"
        n angry "You're... {w=1.0}you're {nw}" with dissolve
        extend "BRAINWASHING us is what you're doing, you evil piece of shit!" with vpunch
        n determined "And you're going to undo the damage you did before it's too late." with dissolve
        ks frown "There's that word again. \"Brainwashing\". You really don't understand at all, do you."
        "It's like she's obsessed with the damn word. And as she screams at me again my mind races to make sense of what's really going on here..."
        show Nozomi frown
        s casual_folded irritated "Okay Kyou, that is enough. I don't understand what you did to my friends exactly, but I know I'm getting dumber just listening to your self-serving justifications." with dissolve
        "Nozomi's smarter than that; she's gotta be. She even said that she knows a thing or two about hypnosis; that what she accuses me of doing is impossible."
        "That doesn't make sense, but what if..."
        menu:
            "They really don't want to be hypnotized?":
                stop music fadeout 5.0
                $ending = "acceptance"
                "... As ridiculous as this talk of \"brainwashing\" is, it's obvious Nozomi believes what she's saying."
                "So what the hell is happening here? Some deep repression? Or regret about going along with me?"
                queue music Night_Road
            "This is some hardcore playacting?":
                $ending = "brainwashed"
                "They KNOW how ridiculous they sound. Literally the only thing they're right about is that I did hypnotize Nozomi and her friend."
                "They have to know that too, so why would they pretend to be this angry and in my face about it unless..."
                "Oh man, what I've just thought is so stupid, but it's the ONLY thing that makes any sense to me at all with the facts I have."
        s frown_right "So here is what needs to happen. We all pay Hiroko a visit, you... hypnotize her again, or whatever it is you did, and you bring her back to how she was." with dissolve
        if ending == "acceptance":
            ks confused "Eh... n-now hold on a second. Let me think..."
            "And Hiroko didn't truly want to be helped either? But if that's true, why did any of this happen at all?"
            n determined "What's there to think about, Kyou? You hurt us, and you need to own that." with dissolve
            "I hypnotized them. They were hypnotized, I'm sure of it. And they were totally willing to go along with everything I told them. Everything."
            ks "Y-yeah... okay, maybe. But I..."
            "But they really want nothing to do with me? Is that the truth of it?"
            s casual_handup irritated "There is nothing to think about. Either you resolve the situation with Hiroko or we take matters into our own hands." with dissolve
            "I don't understand any of this. But one thing's becoming very clear to me..."
        elif ending == "brainwashed":
            ks "You can't be serious. You really want her back to being a little ball of angry hate? Some friends you are."
            "If there's one thing I know for sure by now, it's that these girls just won't admit what they want."
            s annoyed "What you have done is unnatural. The person we know as Hiroko doesn't exist right now. Why don't you understand?" with dissolve
            ks frown "And if I don't do what you want?"
            "Nozomi eyes the papers on the desk, then returns her gaze to me."
            n casual "In that case we'll take every scrap of evidence we can find in here. Anything that links you to your brainwashing activities." with dissolve
            n "Then we'll report you to the authorities, naming Hiroko as a victim and evidence of your intent to harm others."
            ks annoyed "For the last fucking time, What I'm doing isn't \"brainwashing\", okay? And besides, do you honestly think that would work?"
            s irritated "Do you want us to try?" with dissolve
        s frown_right "After all, even if no one believes us about the brainwashing, I am certain there are many disturbing things a boy like you might have on his computer." with dissolve
        ks "Ugh..."
        if ending == "acceptance":
            show Nozomi side casual frown_side at flip
            n "You're right. And he must have documented what he's been doing with us, right?" with dissolve
            "This whole situation is getting wildly out of hand."
            s frown "Indeed. In any case, we need to start taking pictures." with dissolve
            "I gotta dial things back, and fast."
            ks surprised "S-seriously, just calm down, both of you! Do you really think I'm some kind of criminal?"
            show Sayori casual frown_right
            n frown "Kyou, you abused us. You cornered us when we were vulnerable and you forced us to go along with your own twisted desires." with dissolve
            "My own... twisted desires? So that's what she really thinks of me?"
            hide Nozomi
            show Nozomi casual front2 determined
            n "I don't know if we could convince a court of law, even with all this evidence, but don't you dare tell me you didn't know what you were doing." with dissolve
            "So deep down in her heart, there... there really is nothing."
            stop music fadeout 5.0
            "That's the truth of it all, huh?"
            ks "N-Nozomi, I swear I didn't know! I thought you... you..."
            s casual_folded irritated "To even think you could pretend ignorance at a time like this. You contemptible sleaze." with dissolve
            ks "I thought you'd LIKE all of this!"
            queue music Diary
            n "You thought I'd... {w=1.0}{nw}"
            show Nozomi surprised
            show Sayori surprised_right
            $ renpy.transition(dissolve, layer="master")
            extend "w-what on earth?"
            n angry "{cps=15}O-of all the-{w=0.5}{/cps}{nw}" with dissolve
            ks confused "Nozomi, I SAW you at that culture fest! I saw how you were when you were hypnotized!"
            show Nozomi frown
            s casual_handup concerned_right "Did you now..." with dissolve
            ks "It was a year ago, but I still remember it so clearly."
            show cg stageshow bw with flash
            ks "When you were up there getting hypnotized, you had the most incredible look on your face."
            ks "And when that guy got you and the others doing stuff? Man, you really threw yourself into it, didn't you? It's like you were having the time of your life up there."
            ks "I've seen you laugh, and get excited about stuff before, but... not like that. Never like that."
            ks "I'd never seen you that way before."
            hide cg stageshow
            show Nozomi side sad_side blush
            with flash
            ks sad "That's why I learned hypnosis, Nozomi. It's why I did all of this."
            ks "I wanted to impress you. And... yeah, I wanted you to finally notice me. To see who I could really be."
            n sad "..." with dissolve
            s irritated "Now what is this nonsense? What gives you the right?" with dissolve
            ks "That I could be someone who could... who could make you feel that way again."
            s angry_right "I've heard enough of this! Now, enough stalling..." with dissolve
            "I don't know what else I can tell them. I'm baring my soul here, but I guess nothing I say is going to satisfy them."
            hide Nozomi
            show Nozomi casual front sleeptalk blush at center
            n "... It's alright, Sayori. I don't think we need to worry about him for much longer." with dissolve
            s casual_handup concerned "We... don't?" with dissolve
            "I can't imagine the look on my face is any less incredulous as Sayori's right now. But Nozomi..."
            "You get why I did this, right?"
            n concerned noblush "Kyou... I think I can understand why this all happened. Why you thought it would work, even how it must've seemed like it was working for you." with dissolve
            n sleeptalk_concerned "But you went about it all wrong." with dissolve
            ks sad "Nozomi..."
            n side sad_side "So on that day, you just walked up to me and hypnotized me without my consent. Because you thought I'd be into it?" with dissolve
            "I can only nod glumly in response."
            n sad "How do you suppose I would've felt when I saw you suddenly in front of me, an intense look on your face, as you went about this hypnotic routine of yours?" with dissolve
            n sad_closed "I still can't remember clearly, but I can imagine what I must have thought when I saw you like that." with dissolve
            hide Nozomi
            show Nozomi front2 casual sleeptalk_concerned
            n "For you to approach me in such a manner? I must have been terrified thinking about what you were going to do." with dissolve
            n concerned "I think under those circumstances, it would've been easy for my mind to withdraw into itself and just accept whatever you told me, just so I'd be safe from you." with dissolve
            ks surprised "S-safe from... me?"
            "My mind races as I try to search my own memories of that day..."
            #Sayori may need to say something here
            "She... she seemed more annoyed than anything. She even told me so when I had her under."
            "But now she's saying she was scared? How could she possibly be scared of someone like me?"
            ks "But Nozomi I'd never-{w=0.5}{nw}"
            show Sayori frown_right
            n frown "Save it. You'd never understand how you make me feel." with dissolve
            n irritated "It didn't matter how many times we rebuffed you over the years. You only ever thought about what it would take to make me want you, huh." with dissolve
            "I'm left feeling numb as Nozomi draws out a heavy sigh."
            n sleeptalk_concerned "You never thought how scary that made you to me." with dissolve
            scene cg sports shed night:
                matrixcolor SaturationMatrix(0)
            show HirokoHypno relaxed tennis sleepy_up_closed:
                matrixcolor SaturationMatrix(0)
            with flash
            ns casual concerned "Or to Hiroko. You got your hooks into her the same way, right?"
            ns "I can just picture you backing her into a corner, with all the unearned self-confidence you got from pulling that trick on me."
            ns "I'll bet you felt you were doing everything right when you \"convinced\" her to see things your way."
            scene bg k bedroom day
            show Nozomi side casual sad_side at center
            show Sayori casual_handup frown_right at center:
                xpos 0.75
            with flash
            n "You see, Kyou, you learned the basics of hypnosis. How to capture a person's attention with deliberate and authoritive words and actions." with dissolve
            n sad "And you convinced yourself that was enough. That this obsession you have with me... was enough." with dissolve
            n sad_closed  "You're not some calculating mastermind trying to brainwash us all. I guess it's a little insane to think that was the case." with dissolve
            show Sayori concerned_right
            n front2 sleeptalk_concerned "No, you're just a dangerous fool who dabbled in something you learned but never cared to understand. And we've had to suffer for it." with dissolve
            ks casual confused "Uh... w-well..."
            n sleep_concerned "I'm not sure which is scarier, to be quite honest with you." with dissolve
            n pain "But you can't do this to us anymore, Kyou. You understand?" with dissolve
            n cry "I NEED you to understand! It doesn't matter if I like hypnosis, you can't just do this kind of thing to me, or to anyone!" with dissolve
            "So what she's saying is... I was right about her."
            s casual concerned "So, what of Hiroko? If we are not compelling Kyou to realign her thoughts then..." with dissolve
            "I was right about her liking hypnosis. I was right about it being the key to making her notice me."
            show Nozomi side sad_closed at flip
            n "He doesn't know what he's doing. I don't think he even understands what he did to us." with dissolve
            "But all I did was make her fear me. She'll never even look at me again after today."
            n sad_side "I can put her in touch with a real hypnotherapist, it'll be okay." with dissolve
            "I blew it. I blew it big time, huh."
            s sleeptalk "I see. Well, I am glad someone around here understands what we are dealing with here." with dissolve
            hide Nozomi
            show Nozomi casual side sad_side at center
            n "Uh... yeah. I guess." with dissolve
            show Sayori concerned
            n sad_closed "Let's just get out of there." with dissolve
            hide Nozomi
            hide Sayori
            with dissolve
            "The pair of them don't even spare me a glance as they see themselves out."
            "So that's it? This is where all my effort learning hypnosis has gotten me?"
            show penlight at right with moveinright:
                ypos 0.3461
            "All the time I put into making this thing to bring Nozomi closer and all it did was push her away."
            "I'll be lucky if she even looks at me again after this."
            hide penlight at right with moveoutright
            play sound objecthit
            ks angry "GAAAAAAAH!" with vpunch
            "My frustration boils over as the penlight leaves my hand and smashes against my desk with a crash."
            scene bg blackscreen
            $ renpy.transition(longdissolve, layer="master")
            "I don't bother to see where it lands as I sink to my knees and close my eyes in surrender."
            "Let's face it... I'm still pathetic."
            jump Credits
        elif ending == "brainwashed":
            "They're really committed to this, huh. It makes me nervous that they might seriously mean to cause trouble for me."
            "Not to mention my plans for the penlight are on my computer. In a desktop folder. Unencrypted."
            "I'm not sure how they'd react if they found out I was using a device that enhanced my abilities. Guess I'll play along for now."
            ks sigh "Alright... I'll hypnotize her again and bring her back to being the nasty little bitch she was before. Satisfied?"
            n angry "You damn well better bring her back, Kyou. I'm serious." with dissolve
            "A plan emerges..."
            ks neutral "If I'm setting her back how she was, maybe I should do the same for you?"
            show Sayori frown_right
            n determined "No. You're not getting in my head again." with dissolve
            ks frown "What's the difference?"
            n "I don't trust you, Kyou. If you hypnotized me, what's to keep you from doing the same to Sayori when there's no one else to stop you?"
            s annoyed "Ugh... he would, wouldn't he." with dissolve
            "...To be fair that WAS basically my plan. But come on, haven't they taken this act far enough?"
            n frown "No, Kyou. We'll all go to Hiroko's, and you'll hypnotize her with both of us to supervise. Understand?" with dissolve
            "I let out an exasperated sigh and nod my head."
            ks sigh "Fine. If that's how you want it."
            show Nozomi frown
            show Sayori neutral casual
            "I guess they're going to drag this charade on a little longer, then." with dissolve
            show Nozomi side casual frown_side at flip
            n "She should be home, right?" with dissolve
            "Still, Nozomi truly doesn't know how I hypnotized her. I guess I can use that to surprise her somehow."
            s frown casual_folded "Well, we know she isn't on the tennis courts." with dissolve
            "As they talk amongst themselves, I take the opportunity to slip my penlight into my palm and pull it out of my pocket, concealing it from their view with my fingers."
            s casual_handup neutral "We should check that she's home." with dissolve
            n neutral_side "Yeah. Let me just call her..." with dissolve
            ks frown "Wait. Do you even know what you're going to say to her?"
            show Sayori frown_right
            hide Nozomi
            show Nozomi casual front angry
            n "You stay out of this! We're her friends, she'll listen to us." with dissolve
            ks frown "Sure, but given what you intend to do, don't you at least want to plan what you'll say and what you'll do once you get there?"
            show Nozomi frown
            ks "Because I'm sure if you told her you want me to hypnotize her she'd be as hysterical as you two are being." with dissolve
            s frown "We would have to explain things carefully, it's true." with dissolve
            ks "So let's sit down and discuss how we do this."
            stop music fadeout 20.0
            scene cg k bedroom day
            show Nozomi_K_Bedroom folded frown
            show Sayori_K_Bedroom upright angry_left
            with blink
            "Nozomi complies with a snort and sits herself down on the bed, with Sayori sitting right beside her."
            "Sayori is a couple inches taller than Nozomi, but I think I'll be able to catch both of them with the light in one sweep if I just keep calm and do as I practiced."
            s "No matter how you look at it, this whole situation is ridiculous."
            show Nozomi_K_Bedroom folded sad
            n "I know. And we're making a ridiculous plan for a ridiculous situation." with dissolve
            show Sayori_K_Bedroom upright neutral_left
            s "Alright. So, how do we convince Hiroko that she needs hypnotherapy from the boy who broke her in the first place?" with dissolve
            n "Much as I hate to admit it, we're probably going to have to be deceptive."
            show Sayori_K_Bedroom upright neutral
            s frown_right "That is your wheelhouse isn't it, Kyou? Tell us how you tricked them into getting hypnotized the first time." with dissolve
    elif pursued == "Sayori":
        stop music fadeout 5.0
        queue music Memories
        $multichar = _("Nozomi and Hiroko")
        show Hiroko casual dress_arm at center:
            xpos 0.75
        show Nozomi smile
        with dissolve
        ks "Why is Hiroko here too?"
        h frown "H'yeah, {w=0.2}don't look {nw}" with dissolve
        extend "TOO happy to see me, asswipe." with vpunch
        show Nozomi side smile at flip
        n "Okay, so I was talking to Hiroko before heading home yesterday and she asked what I was doing tomorrow." with dissolve
        n smile_side "So I said \"I'm going to Kyou's to study\", and she was like \"Can I come with?\" and I was like \"Sure!\"" with dissolve
        hide Nozomi
        show Nozomi front2 casual smile
        n "Maybe that was presumptuous of me, but when you suggested it the other day it was an open invitation to everybody, right?" with dissolve
        ks confused "Right... But Hiroko, weren't you dead set against doing the study group thing at my place? Not to mention your tennis commitments?"
        h annoyed casual_headhold2 "Yeah, well my friends still won't shut up about how great you are, so I figured I'd cut you some slack I guess." with dissolve
        h frown "'Sides, if Sayori reckons she can juggle work and play, I can mix it up a bit and stay on top too." with dissolve
        ks "I... see."
        h smirk "Yeah, I know what you're thinking. \"That Hiroko chick, she's amazing.\"" with dissolve
        "I really wasn't."
        n chuckle "So... yes, I thought she could join us. That's not inconvenient is it?" with dissolve
        ks frown "N-no. Not at all; more the merrier!"
        h laugh casual "Yay! Thanks, dude~" with dissolve
        n happy "Hurray!" with dissolve
        show Hiroko happy
        show Nozomi laugh
        "It's REALLY fucking inconvenient. Goddammit." with dissolve
        n smile "So where are we doing this? In there? {w=1.0}{nw}" with dissolve
        show Nozomi surprised
        $ renpy.transition(dissolve, layer="master")
        extend "Oooh, what about in your room?"
        ks "Err, I was thinking- {w=0.8}{nw}"
        show Nozomi neutral_right
        h casual_headhold2 surprised_side "Oh man, now you mention it I really wanna know what kinda weird shit he keeps in his room!" with dissolve
        n smile "Same here! You don't mind if we take a peek, do you Kyou?" with dissolve
        ks "Actually, I- {w=0.8}{nw}"
        n laugh "Awesome, thanks Kyou!" with dissolve
        h happy "Fuck yeah!"with dissolve
        show Nozomi :
            linear 2.0 xpos 1.5
        show Hiroko happy at flip:
            linear 1.0 xpos 1.5
        "And before I can register what's happening, the pair of them push past me and head up the stairs, chattering excitedly."
        ks surprised "Hey wait, don't go up there!"
        scene bg k bedroom day
        show Nozomi front happy casual at center
        show Hiroko happy casual_armup dress_arm at center:
            xpos 0.75
        with blink
        "They ignored me completely, and pushed open the half-open door that clearly belonged to my room."
        show Nozomi smile
        show Hiroko casual neutral_side
        stop music fadeout 10.0
        "And as they enter, their heads turn, casting their eyes quickly over the bed, the floor, the computer with a dozen tabs of hypnosis instructional videos..." with dissolve
        show Nozomi neutral
        show Hiroko frown
        "The stack of printed out hypnosis scripts on the table..." with dissolve
        n "I knew it."
        h "Holy shit. I knew something weird was going on, but damn..."
        ks casual surprised "Wait, how did you...?"
        "They already knew about this?"
        play music Rain
        n front2 determined "Do you think we're stupid, Kyou? Sayori's hard to figure out sometimes, but we know it's not in her nature to slack off so much." with dissolve
        n irritated "Unless someone influenced her." with dissolve
        ks neutral "I don't know what you're- {w=0.8}{nw}"
        h angry "I was telling you he's fucked up from the start. {w=0.5}{nw}I mean, " with dissolve
        extend "COME ON!" with vpunch
        h angry_side "Dude's been creeping on us since day one. {w=0.5}I fuckin' {nw}" with dissolve
        extend "KNEW he was gonna do worse shit if nobody stopped him." with vpunch
        n concerned "I know, Hiroko. And I'm sorry we didn't take you seriously enough." with dissolve
        n frown "But in our defence we WERE being brainwashed by our creep of a classmate with some hypnosis scripts he read off the internet." with dissolve
        show Nozomi chuckle
        "She follows that up with a short, bitter chuckle." with dissolve
        n frown "It's utterly insane when I say it out loud." with dissolve
        h frown_side "You're tellin' me..." with dissolve
        n neutral "But that's what happened to Sayori, isn't it, Kyou?" with dissolve
        "My hand slips itself into my pocket, cradling the penlight inside as I decide how I feel about what's developing here."
        "What she's saying IS insane. You can't brainwash someone with a little hypnosis for fuck's sake."
        h frown "What you gotta say for yourself, huh? Piece of shit." with dissolve
        "Swallowing hard, I'm forced to consider my options. Do they really believe what they're saying here?"
        "They must have seen my hand in my pocket by now, still gripping the penlight, but neither of them seems especially alarmed by that fact."
        "How much do they know?"
        ks neutral "As you say, it's insane to even suggest such a thing. So what makes you think I hypnotized and... \"brainwashed\" Sayori with..."
        "I gesture across to the table of printouts."
        ks "That?"
        n angry "Because you also hypnotized and brainwashed ME, Kyou." with dissolve
        ks confused "Huh? That's even MORE insane! A-and besides you should've f..."
        ks "Er, I mean- {w=0.5}{nw}"
        show Nozomi side frown at flip
        n frown "What, Kyou? I should've forgotten I was hypnotized? That's what you were going to say, right?" with dissolve
        n irritated "Because I really have been forgetting a lot of things when I've been with you this week." with dissolve
        hide Nozomi
        show Nozomi casual front2 frown
        n "Like when we were cleaning up the classroom on Monday? I don't know how you pulled it off, but I seriously don't remember a thing." with dissolve
        show Nozomi side at flip
        n frown "That WAS when all this started, wasn't it?" with dissolve
        ks neutral "Right... in the classroom."
        h annoyed "Yeah, it's gotta be. That's when you started acting like a dumbass whenever Kyou was around." with dissolve
        show Hiroko frown
        n neutral "That day it felt like I had the hardest crush on you, Kyou. I'd never felt that way about anyone before." with dissolve
        hide Nozomi
        show Nozomi front2 casual neutral_right
        n front2 neutral_right "I didn't understand where that came from, and for a while I didn't want to." with dissolve
        n sleep "And even now, knowing you somehow did this to me, I still feel this attraction to you." with dissolve
        n concerned "That TERRIFIES me. I know a thing or two about hypnosis, and what you did to me and Sayori shouldn't even be possible." with dissolve
        "The frustration welling up inside me is getting unbearable. She is THIS close to realizing and she doesn't even know it."
        "I have to set her straight."
        ks surprised "But Nozomi, that's it! Don't you see? For any of this to have worked at all there MUST have been something there."
        show Hiroko angry
        ks "This attraction you feel for me? Sayori's need to loosen up? It was inside you both all along!" with dissolve
        ks "Even the fact that you forgot all about this until now was down to your own wants, Nozomi. You wanted to go along with what I said and forget."
        ks "You see, you can't control minds or anything like that. For any of what I did to work there had to be something for me to work with."
        show Nozomi irritated
        ks "Something in you both that said you WANTED to be hypnotized, that you WANTED to be convinced." with dissolve
        ks "All I really did was bring your true thoughts and feelings out into the light."
        n determined "What on {w=0.1}{nw}" with dissolve
        extend "EARTH are you talking about? There was no attraction between us, Kyou?!" with vpunch
        n irritated "We never talked! We never spent any time together that wasn't you pathetically hovering around me hoping I'd notice you." with dissolve
        n side irritated "To say nothing of all the times I caught you leering at me from afar when you thought you were being discreet." with dissolve
        h frown casual_headhold2 "H'yeah, that's just stalking, dude." with dissolve
        n sad "And Sayori..." with dissolve
        n front2 sleeptalk_concerned "Oh my god, I'm so worried for Sayori..." with dissolve
        h casual nervous "Yeah, you really fucked her over, you know that?" with dissolve
        ks confused "What the hell do you mean?"
        h confused "She wants to get into med school, don't she? She'll never make it if she don't give it everything she's got." with dissolve
        h angry "Sure as shit won't do it if she's quitting cram school 'cuz of what you told her." with dissolve
        show Hiroko frown
        "I snort through my nose. They really didn't listen to a thing I said, and they're being so fucking ridiculous about this." with dissolve
        ks frown "I just told her to let her hair down a bit, that's all."
        n side frown "Ever since I met her she's been an overachiever. She always knew she had to go above and beyond if she wanted to achieve her dreams." with dissolve
        n furious "But right now she's happy to throw everything she's ever worked for in the garbage because all of a sudden she needs to have fun every night." with dissolve
        ks sigh "I'm really struggling to see why that's so bad. Everyone could use a break now and again."
        h angry "Jesus fuck, do you {nw}" with dissolve
        extend "EVER listen to yourself?" with vpunch
        h casual_headhold2 "Like, if I'm following this right,{w=0.2} Sayori's only slacking off 'cuz {nw}" with dissolve
        extend "YOU made her!" with vpunch
        n front2 irritated "Exactly! Even if she needed to ease off a bit for her health, that's her call to make and not some creepy jerkwad who doesn't even know her!" with dissolve
        ks "Well, from where I was standing she couldn't hack it and just wouldn't admit it to herself."
        ks "And if you two weren't going to help her ease off then I'm not sure what sort of \"friends\" you are."
        n front2 angry "Oh, you {w=0.2}{nw}" with dissolve
        show Hiroko surprised_side
        extend "FUCKING ASSHOLE!{w=1.0}{nw}" with shake
        show Nozomi irritated
        n "..." with dissolve
        h casual_headhold2 sad_side "Damn, Nozo." with dissolve
        "Nozomi sucks in a breath before continuing. I can barely stand to see her so wound-up, especially over something she's so obviously wrong about."
        show Hiroko frown
        n frown "Alright, you're not listening. I guess I wasn't expecting you to anyway." with dissolve
        ks confused "Nozomi look, I... I realize how this might look, and that you couldn't possibly understand what I'm doing. But..."
        n angry "You're... {w=1.0}you're {nw}" with dissolve
        extend "BRAINWASHING us is what you're doing, you evil piece of shit!" with vpunch
        n determined "And you're going to undo the damage you did before it's too late." with dissolve
        ks frown "There's that word again. \"Brainwashing\". You really don't understand at all, do you."
        "It's like she's obsessed with the damn word. And as she screams at me again my mind races to make sense of what's really going on..."
        show Nozomi frown
        h angry "Dude, shut the fuck up. You've done enough talking, so now you're gonna listen to us." with dissolve
        show Hiroko frown
        "Nozomi's smarter than that; she's got to be. She even said that she knows a thing or two about hypnosis; that what she accuses me of doing is impossible." with dissolve
        "That doesn't make sense, but what if..."
        menu:
            "They really don't want to be hypnotized?":
                stop music fadeout 5.0
                $ending = "acceptance"
                "... As ridiculous as this talk of \"brainwashing\" is, it's obvious Nozomi believes what she's saying."
                "So what the hell is happening here? Some deep repression? Or regret about going along with me?"
                queue music Night_Road
            "This is some hardcore playacting?":
                $ending = "brainwashed"
                "They KNOW how ridiculous they sound. Literally the only thing they're right about is that I did hypnotize Nozomi and her friend."
                "They have to know that too, so why would they pretend to be this angry and in my face about it unless..."
                "Oh man, what I've just thought is so stupid, but it's the ONLY thing that makes any sense to me at all with the facts I have."
        h casual "So, Nozo reckons you can hypno Sayori again and put her back how she was. That right?" with dissolve
        if ending == "acceptance":
            ks confused "Eh... n-now hold on a second. Let me think..."
            "And Sayori didn't truly want to be helped either? But if that's true, why did any of this happen at all?"
            show Hiroko frown casual
            n determined "What's there to think about, Kyou? You hurt us, and you need to own that." with dissolve
            "I hypnotized them. They were hypnotized, I'm sure of it. And they were totally willing to go along with everything I told them. Everything."
            ks "Y-yeah... okay, maybe. But I..."
            "But they really want nothing to do with me? Is that the truth of it?"
            h casual_armup furious vein "Dude, I will {nw}" with dissolve
            extend "FUCK YOU UP IF YOU DON'T FIX THIS SHIT!" with shake
        elif ending == "brainwashed":
            ks "You can't be serious. You really want her back to nearly killing herself through overwork?"
            "If there's one thing I know for sure by now, it's that these girls just won't admit what they want."
            show Hiroko frown casual
            n furious "I want Sayori to be who she is because she decided on her own, not because you decided what's best for her." with dissolve
            ks frown "And if I don't do what you want?"
            h casual_armup furious vein "I will {nw}" with dissolve
            extend "FUCK YOU UP!" with shake
        "I have to back off a step as she roars at me."
        "Hiroko may be a head shorter than me, and a girl, but I don't doubt she could do me some damage if she wanted to."
        ks "Really? You're gonna assault me in my own home?"
        h casual angry "Who you gonna tell, Kyou? You want everyone to know a li'l girl beat your punk ass to shit? 'Cuz that's what's gonna happen!" with dissolve
        ks "As... as if Nozomi would stand by and watch you do that."
        n side furious "Watch? I was thinking of joining in." with dissolve
        ks "You... you can't be serious, Nozomi. You don't really mean that."
        n front2 determined "Don't I? Fix what you broke, Kyou, and hope you never have to find out!" with dissolve
        if ending == "acceptance":
            "I don't understand any of this. But one thing's becoming very clear to me..."
        elif ending == "brainwashed":
            "... No. They sound convincing, but I know what I've worked out. This is just more theater to cover for why they're really here."
            "I have to believe that."
        h frown_side novein "Nozo, we gotta turn this place over when we're done with him." with dissolve
        if ending == "acceptance":
            "This whole situation is getting wildly out of hand."
        # n casual frown "In that case we'll take every scrap of evidence we can find in here. Anything that links you to your brainwashing activities." with dissolve
        show Nozomi side casual frown_side at flip
        n "You're right. Even if he won't co-operate, he must have documented what he's been doing with us." with dissolve
        n irritated "Then we'll report him to the authorities, naming Sayori as a victim and evidence of his intent to cause harm." with dissolve
        h casual_armup angry "YEAH! We'll finally get to nail this fucker!" with vpunch
        if ending == "acceptance":
            "I gotta dial things back, and fast."
            ks surprised "S-seriously, just calm down, both of you! Do you really think I'm some kind of criminal?"
            show Hiroko casual
            n frown "Kyou, you abused us. You cornered us when we were vulnerable and you forced us to go along with your own twisted desires." with dissolve
            "My own... twisted desires? So that's what she really thinks of me?"
            hide Nozomi
            show Nozomi casual front2 determined
            n "I don't know if we could convince a court of law, even with all this evidence, but don't you dare tell me you didn't know what you were doing." with dissolve
            "So deep down in her heart, there... there really is nothing."
            stop music fadeout 5.0
            "That's the truth of it all, huh?"
            ks "N-Nozomi, I swear I didn't know! I thought you... you..."
            h casual_armup "Thought you could get away with it, yeah, we fuckin' know already!" with dissolve
            ks "I thought you'd LIKE all of this!"
            queue music Diary
            n "You thought I'd... {w=1.0}{nw}"
            show Nozomi surprised
            show Hiroko confused
            $ renpy.transition(dissolve, layer="master")
            extend "w-what on earth?"
            n angry "{cps=15}O-of all the-{w=0.5}{/cps}{nw}" with dissolve
            ks confused "Nozomi, I SAW you at that culture fest! I saw how you were when you were hypnotized!"
            show Nozomi frown
            h casual_headhold2 "The shit are you saying now?" with dissolve
            ks "It was a year ago, but I still remember it so clearly."
            show cg stageshow bw with flash
            ks "When you were up there getting hypnotized, you had the most incredible look on your face."
            ks "And when that guy got you and the others doing stuff? Man, you really threw yourself into it, didn't you? It's like you were having the time of your life up there."
            ks "I've seen you laugh, and get excited about stuff before, but... not like that. Never like that."
            ks "I have never seen you that way before."
            hide cg stageshow
            show Nozomi side sad_side blush
            with flash
            ks sad "That's why I learned hypnosis, Nozomi. That's why I did all of this."
            ks "I wanted to impress you. And... yeah, I wanted you to finally notice me. To see who I could really be."
            n sad "..." with dissolve
            h casual_armup furious "That's the {nw}" with dissolve
            extend "STUPIDEST fucking thing I've ever heard! The fuckin' nerve of this stalker creep!" with vpunch
            ks "That I could be someone who could... who could make you feel that way again."
            h furious_side "C'mon, Nozo, I've heard enough of this shit. Let's take him down!" with dissolve
            "I don't know what else I can tell them. I'm baring my soul here, but I guess nothing I say is going to satisfy them."
            hide Nozomi
            show Nozomi casual front sleeptalk blush at center
            n "... It's alright, Hiroko. I don't think we need to worry about him for much longer." with dissolve
            h casual_headhold2 confused_side "Ehhh?" with dissolve
            "I can't imagine the look on my face is any less incredulous as Hiroko's right now. But Nozomi..."
            "You get why I did this, right?"
            n concerned noblush "Kyou... I think I can understand why this all happened. Why you thought it would work, even how it must've seemed like it was working for you." with dissolve
            n sleeptalk_concerned "But you went about it all wrong." with dissolve
            ks sad "Nozomi..."
            n side sad_side "So on that day, you just walked up to me and went about hypnotizing me without my consent. Because you thought I'd be into it?" with dissolve
            "I can only nod glumly in response."
            n sad "How do you suppose I would've felt when I saw you suddenly in front of me, an intense look on your face, as you went about this hypnotic routine of yours?" with dissolve
            n sad_closed "I still can't remember clearly, but I can imagine what I must have thought when I saw you like that." with dissolve
            hide Nozomi
            show Nozomi front2 casual sleeptalk_concerned
            n "For you to approach me in such a manner? I must have been terrified thinking about what you were going to do." with dissolve
            n concerned "I think under those circumstances, it would've been easy for my mind to withdraw into itself and just accept whatever you told me, just so I'd be safe from you." with dissolve
            ks surprised "S-safe from... me?"
            "My mind races as I try to search my own memories of that day..."
            h pain "Fuckin'... knew I should'a stayed with you back then. Goddammit." with dissolve
            "She... she seemed more annoyed than anything. She even told me so when I had her under."
            "But now she's saying she was scared? How could she possibly be scared of someone like me?"
            ks confused "Nozomi I'd never-{w=0.5}{nw}"
            show Hiroko frown
            n frown "Save it. You'd never understand how you make me feel." with dissolve
            n irritated "It didn't matter how many times we rebuffed you over the years. You only ever thought about what it would take to make me want you, huh." with dissolve
            "I'm left feeling numb as Nozomi draws out a heavy sigh."
            n sleeptalk_concerned "You never thought how scary that made you to me." with dissolve
            show DelusionStruggleSayori sayori_struggling s_worried:
                matrixcolor SaturationMatrix(0)
            with flash
            ns casual concerned "Or to Sayori. You got your hooks into her the same way, right?"
            ns "I can just picture you backing her into a corner, with all the unearned self-confidence you got from pulling that trick on me."
            ns "I'll bet you felt you were doing everything right when you \"convinced\" her to see things your way."
            hide DelusionStruggleSayori
            show Nozomi side sad_side
            with flash
            n "You see, Kyou, you learned the basics of hypnosis. How to capture a person's attention with deliberate and authoritive words and actions." with dissolve
            n sad "And you convinced yourself that was enough. That this obsession you have with me... was enough." with dissolve
            n sad_closed  "You're not some calculating mastermind trying to brainwash us all. I guess it's a little insane to think that was the case." with dissolve
            show Hiroko casual sad_side
            n front2 sleeptalk_concerned "No, you're just a dangerous fool who dabbled in something you learned but never cared to understand. And we've had to suffer for it." with dissolve
            ks "Uh... w-well..."
            n sleep_concerned "I'm not sure which is scarier, to be quite honest with you." with dissolve
            n pain "But you can't do this to us anymore, Kyou. You understand?" with dissolve
            n cry "I NEED you to understand! It doesn't matter if I like hypnosis, you can't just do this kind of thing to me, or to anyone!" with dissolve
            "So what she's saying is... I was right about her."
            h casual_headhold nervous_side "H-hey, what about Sayori? He's gotta fix her, don't he?" with dissolve
            "I was right about her liking hypnosis. I was right about it being the key to making her notice me."
            show Nozomi side sad_closed at flip
            n "No... n-no, he doesn't know what he's doing. I don't think he even understands what he did to us." with dissolve
            "But all I did was make her fear me. She'll never even look at me again after today."
            h sad_side "So then..." with dissolve
            n sad_side "I can put her in touch with a real hypnotherapist, it'll be okay." with dissolve
            "I blew it. I blew it big time, huh."
            h confused_side "So... Like, you really know all about this hypno stuff, huh, Nozo?" with dissolve
            hide Nozomi
            show Nozomi casual side sad_side at center
            n "I don't... w-want to talk about it, okay? It's not important right now." with dissolve
            show Hiroko sad_side
            n sad_closed "It's not... important at all..." with dissolve
            # n front2 sad "That's the scariest thing about this whole thing, isn't it. Somehow it very nearly was." with dissolve
            # n "Somehow, with a little knowledge and a lot of desire, you held mine and Sayori's minds in your hands and pulled them in your direction."
            # n "It seems like brainwashing. FEELS like brainwashing."

            # n frown "You may have learned enough to know the basics of hypnosis. How to project your voice and choose your words to focus someone's attention and such." with dissolve
            # n irritated "But if you don't have a rapport with your hypnotee, if you make no effort to understand them, you can cause unimaginable pain."
            # n "You're just a... dangerous moron who dabbled in something you learned but never bothered to understand, and you hurt us all!"
            # n "All because of your obsession with who you think I am."
            # n cry "You CAN'T do this to us anymore, Kyou. You understand now?" with dissolve
            # n sad "Maybe that's the scariest thing about all of this." with dissolve
            #Maybe this line is where she calls Kyou a dangerous idiot?
            #ns "But you always put the fear in us, Kyou.
            # "(( AUTHOR'S NOTE: Sadly that's about all I can manage writing for this month. Brief outline to follow for the rest of this scene. ))"
            # "So, Nozomi continues to attribute Kyou's success to intimidation."
            # "It's not an explanation she finds particularly convincing, considering just how successful he was, but she does feel it the most likely, and it lines up with his confession."
            # "Kyou didn't intentionally set out to brainwash Nozomi and her friend. And even if he did, it couldn't have possibly worked. Even he would've known that."
            # "No, he's just a dangerous idiot who lucked into the perfect conditions to effect a change in them. And his actions have harmed her and her friend more than he seems to realize."
            # "When the subject of Kyou trying to hypnotize and deprogram Sayori comes up, Nozomi shuts it down this time. He clearly doesn't know what he's doing."
            # "She'll try and get her to see a real hypnotherapist if she doesn't snap out of it soon."
            hide Nozomi
            hide Hiroko
            with dissolve
            "The pair of them don't even spare me a glance as they see themselves out."
            "So that's it? This is where all my effort learning hypnosis has gotten me?"
            show penlight at right with moveinright:
                ypos 0.3461
            "All the time I put into making this thing to bring Nozomi closer and all it did was push her away."
            "I'll be lucky if she even looks at me again after this."
            hide penlight at right with moveoutright
            play sound objecthit
            ks angry "GAAAAAAAH!" with vpunch
            "My frustration boils over as the penlight leaves my hand and smashes against my desk with a crash."
            scene bg blackscreen
            $ renpy.transition(longdissolve, layer="master")
            "I don't bother to see where it lands as I sink to my knees and close my eyes in surrender."
            #He should probably acknowledge how underhanded he was being during the course of this

            # "Nozomi and Hiroko leave Kyou alone with some parting shots and he's left to stew in his failure, as he throws his penlight against the wall."
            # "He feels he was right about Nozomi's interest in hypnosis, but he knows he's blown it now. He'll never get another chance with her."
            "Let's face it... I'm still pathetic."
            jump Credits
            #Kyou goes on to talk about the culture fest last year, about how he thought Nozomi wanted to be hypnotized and learned hypnosis for her
            #He wanted to impress her into wanting to be with him. He thought she was into all of this stuff
            #And as Hiroko starts to rubbish it all, Nozomi can't help but admit there's some truth in what he says, that she might have even been receptive to it under different circumstances
            #But the fact remains that he did this without her consent, and that what he's done is highly dangerous. Still, maybe she can believe that he was just stupid

        elif ending == "brainwashed":
            ks annoyed "For the last fucking time, I haven't done anything you didn't already want, okay?"
            ks "And besides, do you honestly think the authorities would buy something that stupid?"
            show Nozomi frown
            h frown "I dunno, man, {w=0.3}even if they don't buy the brainwashing angle there's gotta be {nw}" with dissolve
            extend "SOMETHING we can bust you for in here." with vpunch
            ks frown "Ugh..."
            "They're really committed to this, huh. It makes me nervous that they might seriously mean to hurt me."
            "Not to mention my plans for the penlight are on my computer. In a desktop folder. Unencrypted."
            "I'm not sure how they'd react if they found out I was using a device that enhanced my abilities. Guess I'll play along for now."
            ks sigh "Alright... I'll hypnotize her again and bring her back to being the overworked zombie she was before. Satisfied?"
            hide Nozomi
            show Nozomi casual
            n front angry "You damn well better bring her back, Kyou. I'm serious." with dissolve
            "A plan emerges..."
            ks neutral "If I'm setting her back how she was, maybe I should do the same for you?"
            show Hiroko frown
            n determined casual_folded "No. You're not getting in my head again." with dissolve
            ks "What's the difference?"
            n "I don't trust you, Kyou. If you hypnotized me, what's to keep you from doing the same to Hiroko when there's no one else to stop you?"
            h surprised "What the fuck? Can he even do that?" with dissolve
            n irritated "Honestly, Hiroko, after what he's done to Sayori and myself, I wouldn't rule out the possibility that he could still put you under somehow." with dissolve
            "...To be fair that WAS basically my plan. But come on, haven't they taken this act far enough?"
            show Hiroko frown
            n frown "So no, Kyou. We'll all go to Sayori's, and you'll hypnotize her with both of us to supervise. Understand?" with dissolve
            "I let out an exasperated sigh and nod my head."
            ks sigh "Fine. If that's how you want it."
            show Hiroko neutral casual
            show Nozomi frown
            "I guess they're going to drag this charade on a little longer, then." with dissolve
            show Nozomi side casual frown_side at flip
            n "She should be home, right?" with dissolve
            "Still, Nozomi truly doesn't know how I hypnotized her. I guess I can use that to surprise her somehow."
            #"And I will definitely need to hypnotize them if I want any hope of convincing them how utterly wrong they are about all of this."
            h frown_side casual_headhold2 "Yeah, probably, if she ain't at cram school." with dissolve
            "As they talk amongst themselves, I take the opportunity to slip my penlight into my palm and pull it out of my pocket, concealing it from their view with my fingers."
            n neutral_side "Do you want to call her?" with dissolve
            h neutral_side "'Kay. I'll hit her up." with dissolve
            ks confused "Wait. Do you even know what you're going to say to her?"
            show Hiroko frown
            hide Nozomi
            show Nozomi
            n front casual_folded angry "You stay out of this. We're her friends, she'll listen to us." with dissolve
            ks frown "Sure, but given what you intend to do, don't you at least want to plan what you'll say and what you'll do once you get there?"
            show Nozomi frown
            ks "Because I'm sure if you told her you want me to hypnotize her she'd be as hysterical as you two are being." with dissolve
            h annoyed "Urrrgh... he's right about that, ain't he?" with dissolve
            ks "So let's sit down and discuss how we do this."
            stop music fadeout 20.0
            scene cg k bedroom day
            show Nozomi_K_Bedroom folded frown
            show Hiroko_K_Bedroom relaxed frown
            with blink
            "Nozomi complies with a snort and sits herself down on the bed, with Hiroko following suit beside her." with dissolve
            "Hiroko is a couple inches shorter than Nozomi, but I think I'll be able to catch both of them with the light in one sweep if I just keep calm and do as I practiced."
            h annoyed_side "I can't believe this bullshit is my life now." with dissolve
            show Nozomi_K_Bedroom folded sad
            n "I know, Hiroko. I know. This whole situation is beyond ridiculous." with dissolve
            n "And much as I hate to admit it, we're probably going to have to be deceptive."
            show Hiroko_K_Bedroom relaxed angry
            h frown "So, asshole, how do we get Sayori to go along with this stupid hypno-crap? How'd you even do it the first time?" with dissolve
    elif pursued == "Nozomi":
        show Sayori casual at center:
            xpos 0.75
        show Hiroko casual at center, flip:
            xpos 0.25
        ks "Why are THEY here too?" with dissolve
        "Like, what the fuck?!"
        show Sayori casual_folded smirk_right
        show Nozomi smile
        stop music fadeout 5.0
        queue music Downtown
        h smirk dress_arm "Surprise! Dipshit." with dissolve
        s "Did you think we would be left out of the party, Kyou? For shame."
        ks "But... but why, why are you two here? Don't you have other stuff to do?"
        "My mind is racing. This wasn't supposed to happen."
        s smirk "He does not look pleased to see us, does he." with dissolve
        n side smile "Shouldn't you also be wondering why I'm here, Kyou? I mean, I didn't tell you anything about coming to see you today." with dissolve
        ks confused "Well, that's..."
        n front casual_folded pout_left "But the other day I felt I just NEEDED to visit you today, at 10 o'clock sharp." with dissolve
        n "I told the others at lunch about it yesterday. And let me tell you, we had a long discussion about that!"
        ks "You... y-you told..."
        show Sayori smirk_right
        n surprised "Well, of COURSE I did! Why wouldn't we talk about our weekend plans with each other?" with dissolve
        s concerned "Anyway, since Nozomi was nagging us about taking a breather all day long I eventually relented." with dissolve
        h frown "Yeah. That's when Nozo brought up that stupid study group again." with dissolve
        n side casual smile_side "Right? I thought it'd make a perfect change of pace for everyone. And this time everyone was on board~" with dissolve
        ks "But why'd you keep it a secret from me?!"
        n front casual_folded pout_left "Oh, well, it was their idea not to tell you anything." with dissolve
        s smirk_right "After all, what guy does not want to be surprised by three cute girls at his doorstep?" with dissolve
        "THIS guy! And don't flatter yourselves, you aren't cute."
        h casual_armup happy "ANYWAY!" with vpunch
        h "Where we doing this?"
        ks "W-where are we doing... what?"
        n happy casual "The study group, silly!" with dissolve
        "This is getting away from me fast. Gotta think quick-{w=1.0}{nw}"
        h smirk "What about in your room, Kyou?" with dissolve
        ks surprised "What? No! No, don't-{w=0.7}{nw}"
        n surprised "Oooh, sounds good to me!" with dissolve
        s "After all, what guy would not want three cute girls in his bedroom?"
        ks angry "THIS GUY!" with vpunch
        n happy "Let's check it out! Is it up here? It's up here isn't it?" with dissolve
        show Nozomi happy casual:
            linear 1.0 xpos -0.1
        show Sayori:
            linear 1.0 xpos 1.5
        show Hiroko happy:
            linear 1.0 xpos -0.3
        "And before I can say anything more the three of them push past me and head up the stairs..."
        scene bg k bedroom day
        show Nozomi front casual happy at center
        show Sayori casual smile at center:
            xpos 0.75
        show Hiroko casual_armup smile at center, flip:
            xpos 0.25
        with dissolve
        ks casual angry "No! Stop! I said STOP!"
        stop music fadeout 10.0
        show Nozomi smile
        show Sayori neutral
        "And as they enter, their heads turn, casting their eyes quickly over the bed, the floor, the computer with a dozen tabs of hypnosis instructional videos..." with dissolve
        show Nozomi neutral
        show Sayori frown_right
        show Hiroko frown
        "The stack of printed out hypnosis scripts on the table..." with dissolve
        n concerned "Oh my god. So he really..." with dissolve
        s frown "This... This is not credible, is it?" with dissolve
        ks "Wait, how did you...?"
        play music Rain
        h casual annoyed "How'd we figure out you did some weird shit to Nozo? Wasn't hard." with dissolve
        n casual_folded sleep "At first I really couldn't understand why they were making such a fuss." with dissolve
        n "As far as I knew, I'd simply noticed an attraction to you this week that I'd never realized before."
        show Hiroko frown
        s casual_folded annoyed_right "Honestly, I had expected some form of coercion. Perhaps you were blackmailing her." with dissolve
        s scowl "Hypnosis... did not feature in my thinking." with dissolve
        h sad_side "How'd he even do it? This is fuckin' nuts!" with dissolve
        n concerned "I really don't know..." with dissolve
        "This is such a misunderstanding on their part. It's why I didn't want them sniffing around up here in the first place."
        "But this is not what they seem to think it is."
        ks frown "O-okay, do you guys know ANYTHING about hypnosis?"
        show Hiroko frown
        n frown "Try us." with dissolve
        "Shit, how am I supposed to explain, being put on the spot like this?"
        ks "Okay, well... The most important thing to know is that no matter how deep in trance you are, you will never do or think anything your conscious mind wouldn't agree to."
        ks "Don't you get it, Nozomi? This attraction you feel to me now? I didn't make it out of nothing; it's real."
        n irritated "I know what you're saying, but... I don't agree." with dissolve
        "My hand closes around the penlight in my pocket. There is just no way I could get them to understand, unless I could..."
        n determined "There was never any attraction between us, Kyou! We've barely talked to each other in the entire time I've known you." with dissolve
        n "How on earth would I feel anything for you when I never even knew you? When I think about it like that, this attraction I have now is... unnatural."
        ks "Well then, allow me to... {w=0.7}{nw}" with dissolve
        if persistent.NewSprite == " New":
            $light_x = 0.17; light_y = 0.29; slight_x = 0.43; slight_y = 0.25; ldirection = "right"; lnumber = 2
        else:
            $light_x = 0.18; light_y = 0.31; slight_x = 0.43; slight_y = 0.25; ldirection = "right"; lnumber = 2
        call lightshow from _call_lightshow_36
        extend "show you what I mean."
        show Hiroko surprised
        show Nozomi surprised
        show Sayori surprised_right
        "As I speak, I pull out my penlight with a flourish, hoping to sweep the beam past the girl's startled eyes." with dissolve
        n "W-wait, that's..."
        call lightshow from _call_lightshow_37
        ks "Just relax and listen, all of you, to what I have to say-{w=0.8}{nw}"
        stop music
        n "S-stop him!"
        show Sayori angry_right
        h casual_armup angry "KYAAAAA!" with vpunch
        play sound punch
        "And just like that I'm lunged at by Hiroko, followed shortly after by a stumbling Sayori." with vpunch
        play sound punch
        scene bg blackscreen with fade
        "Seems I couldn't focus the beam on all three pairs of eyes at once, nor did I have the time to truly show them what I meant."
        play sound [punch, punch, punch]
        "Not that it matters anymore, as Nozomi joins in the pile-on and my penlight is wrestled out of my hand." with shake
        scene bg k bedroom day
        show Nozomi front casual determined at center
        show Sayori casual frown at center:
            xpos 0.75
        show Hiroko casual dress_arm frown_side at center, flip:
            xpos 0.25
        with dissolve
        "They leave me panting on the floor as they get up and look over my device with angry, yet curious eyes."
        show penlight at right with moveinright:
            ypos 0.346
        h "What the fuck is it? A lil' torch?"
        s casual_folded "It seems to be just a light pen, yes." with dissolve
        hide penlight with moveoutright
        n "I remember now. He always had this in his hand every time he's spoken to me this week."
        ks casual surprised "H-hey! You give that back!"
        n frown "Not so fast. I want to try something." with dissolve
        with flash
        "... She just- {w=0.5}{nw}"
        n "Don't worry, Kyou. You know this won't hurt."
        "She just flashed me with the penlight!"
        ks "Y-You don't know what you're doing!"
        with flash
        n "And you don't need to worry about that right now."
        h sad_side "Err, what are you doing, Nozo?" with dissolve
        with flash
        n "Shh, just keep him still for me."
        ks "N-nozo, stop-{w=0.5}{nw}"
        with flash
        play music Flow fadein 30.0
        "If she thinks I'm going to let myself be hypnotized she really must be clueless about how this shit works."
        with flash
        n neutral "And Kyou, all you have to do is focus." with dissolve
        "Not to mention I invented this thing! I know exactly what it does so why- {w=1.0}{nw}"
        with flash
        "Why am I just going along with this?"
        with flash
        n "Focus on the light flashing past your eyes."
        with flash
        n "Focus on your breathing as it slows, nice and deep."
        show Hiroko sad
        s casual_folded frown_right "{size=14}I am not sure I like this.{/size}" with dissolve
        with flash
        n "Every time the light passes, relaxing a little deeper for me."
        with flash
        n "Feeling so relaxed. Feeling your eyes become heavier and heavier with every blink."
        with flash
        show bg blackscreen onlayer toplayer with dissolve:
            alpha 0.2
        n "Feeling so good about relaxing."
        with flash
        show bg blackscreen onlayer toplayer with dissolve:
            alpha 0.4
        n "Feeling so good about going under for me."
        with flash
        show bg blackscreen onlayer toplayer with dissolve:
            alpha 0.6
        n "That's right, Kyou. So willing to drop for me. Dropping deeper."
        with flash
        show bg blackscreen onlayer toplayer with dissolve:
            alpha 0.8
        n "Dropping deeper."
        with flash
        show bg blackscreen onlayer toplayer with dissolve:
            alpha 0.9
        n "Sleep."
        stop music fadeout 4.0
        $ending = "hypnotized"
        scene bg blackscreen with fade
        hide bg blackscreen onlayer toplayer
        jump Epilogue_NonCon_Kyou
    if ending == "brainwashed":
        if pursued == "Hiroko":
            show Nozomi_K_Bedroom folded angry
            show Sayori_K_Bedroom upright angry
        else:
            show Nozomi_K_Bedroom folded angry
            show Hiroko_K_Bedroom raised angry
        "They both look up at me with a glare." with dissolve
        "Finally. Took them long enough to give me an opening."
        "Nothing for it but to give them what they came here for."
        # "Oh, oh I think I just found the perfect opening. It's corny as hell, but..."
        ks casual frown "Alright, then. Allow me to... {w=1.0}{nw}"
        if pursued == "Hiroko":
            $light_x = 0.2; light_y = 0.2; slight_x = 0.58; slight_y = 0.21
            # if persistent.NewSprite == " New":
            #     $light_x = 0.65; light_y = 0.35; slight_x = 0.84; slight_y = 0.32
            # else:
            #     $light_x = 0.65; light_y = 0.36; slight_x = 0.81; slight_y = 0.3
        elif pursued == "Sayori":
            $light_x = 0.2; light_y = 0.2; slight_x = 0.49; slight_y = 0.38
        $ldirection = "right"; lnumber = 2
        call lightshow from _call_lightshow_38
        if pursued == "Hiroko":
            show Nozomi_K_Bedroom surprised
            show Sayori_K_Bedroom surprised
        elif pursued == "Sayori":
            show Nozomi_K_Bedroom surprised
            show Hiroko_K_Bedroom surprised
        extend "shine a light on the matter." with dissolve
        "I catch them both seemingly by surprise as I managed to switch on the penlight and pass it across both pairs of eyes with the appropriate comic timing."
        "That line was corny as fuck, but whatever. They don't deserve better."
        if pursued == "Hiroko":
            show Sayori_K_Bedroom confused
            s "Did you have that with you the whole time, just in case you got to prank us like that?" with dissolve
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom annoyed
            h "What kinda lame shit was that?" with dissolve
        n "Wait, that's- {w=1.0}{nw}"
        call lightshow from _call_lightshow_39
        "I casually pass the light back across them both again as I begin my routine."
        ks smirk "There's no need to get bent out of shape over a little light, you two."
        show Nozomi_K_Bedroom scared
        n "Something's wrong. This is- {w=1.0}{nw}" with dissolve
        call lightshow from _call_lightshow_40
        ks "You need to relax, both of you. There's nothing wrong; you just need to relax and let me explain everything."
        play music Flow
        call lightshow from _call_lightshow_41
        if pursued == "Hiroko":
            show Sayori_K_Bedroom surprised
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom surprised
        "I'm casually passing the light back and forth over them now, keeping a steady rhythm." with dissolve
        "Occasionally I miss an eye or two with the beam, but I'm mostly staying accurate as they're both sitting fairly still."
        call lightshow from _call_lightshow_42
        show Nozomi_K_Bedroom sleepy
        "Nozomi's eyes are already starting to glaze over. She must have retained her conditioning to respond favourably to the light, like I knew she would." with dissolve
        call lightshow from _call_lightshow_43
        if pursued == "Hiroko":
            show Sayori_K_Bedroom confused
            "And Sayori, for her part, is sitting and watching calmly, albeit with a bewildered look on her face." with dissolve
            "I'm sure her first time getting hypnotized is as confusing as it is exciting for her."
            s "So explain, Kyou."
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom annoyed
            "And Hiroko, for her part, is sitting and watching calmly, albeit with a bewildered look on her face." with dissolve
            "I'm sure her first time getting hypnotized is as confusing as it is exciting for her."
            h "Tell us, then..."
        call lightshow from _call_lightshow_44
        ks "Okay, well first you need to clear your heads. Clear your heads and focus on the light you're seeing right now."
        call lightshow from _call_lightshow_45
        ks "Feel the patterns dancing across your eyes. Let them relax you and as the patterns continue to dance, notice how your eyelids become heavy watching them."
        call lightshow from _call_lightshow_46
        show Nozomi_K_Bedroom relaxed sleepy
        if pursued == "Hiroko":
            n "S... sayori... run..." with longdissolve
        elif pursued == "Sayori":
            n "H...hiroko ... run..." with longdissolve
        call lightshow from _call_lightshow_47
        ks "There's no need to speak right now, Nozomi. Just stay seated and remember how good it feels to watch the light."
        call lightshow from _call_lightshow_48
        show Nozomi_K_Bedroom entranced
        n "..." with dissolve
        if pursued == "Hiroko":
            ks "And as for you, Sayori, this is what your friends have enjoyed all week. Feeling so relaxed. So drowsy. So sleepy."
        elif pursued == "Sayori":
            ks "And as for you, Hiroko, this is what your friends have enjoyed all week. Feeling so relaxed. So drowsy. So sleepy."
        call lightshow from _call_lightshow_49
        if pursued == "Hiroko":
            show Sayori_K_Bedroom sleepy
            s "I do not... wish to be..." with dissolve
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom sleepy
            h "I don't... don't want..." with dissolve
        call lightshow from _call_lightshow_50
        if pursued == "Hiroko":
            ks "It's alright, Sayori. It's perfectly natural to feel so relaxed in the light. There's no need to deny it."
        elif pursued == "Sayori":
            ks "It's alright, Hiroko. It's perfectly natural to feel so relaxed in the light. There's no need to deny it."
        call lightshow from _call_lightshow_51
        if pursued == "Sayori":
            show Hiroko_K_Bedroom relaxed
            ks "It's natural and correct for you to feel this way, girls. Just watching the light. Getting sleepier." with dissolve
        elif pursued == "Hiroko":
            ks "It's natural and correct for you to feel this way, girls. Just watching the light. Getting sleepier."
        call lightshow from _call_lightshow_143
        if pursued == "Hiroko":
            show Sayori_K_Bedroom entranced
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom entranced
        ks "Getting sleepier." with dissolve
        call lightshow from _call_lightshow_52
        ks "Sleep, Nozomi."
        if pursued == "Hiroko":
            ks "Sleep, Sayori."
            show Nozomi_K_Bedroom sleep
            show Sayori_K_Bedroom sleep
            n "..." with longdissolve
            s "..."
        elif pursued == "Sayori":
            ks "Sleep, Hiroko."
            show Nozomi_K_Bedroom sleep
            show Hiroko_K_Bedroom sleep
            n "..." with longdissolve
            h "..."
        ks frown "That's right, girls. Perfectly relaxed. Perfectly calm and willing to listen."
        "There, both of them out like lights. And that can only mean one thing: That they were willing to be hypnotized."
        "I breathe a small sigh of relief. I admit I kinda doubted myself for a little while there, but the evidence is sat before my eyes."
        "And that relief gives way to a little anger after the shit they just put me through."
        "I mean, really? Rough me up and ransack my room? You can't just say this shit to someone out of the blue."
        "So it's time to make them confess the real reason they're here. No more of these childish games."
        ks "So, girls, now that you're so calm and relaxed and deeply entranced, I think it's time for you both to be honest with me."
        ks "When you came to me today, your true intention was to have me hypnotize you, wasn't it?"
        if pursued == "Hiroko":
            $multi = "{color=93624B}Nozomi{/color} {color=#FFFFFF}and{/color} {color=385599}Sayori{/color}"
            show Nozomi_K_Bedroom open
            show Sayori_K_Bedroom open
        elif pursued == "Sayori":
            $multi = "{color=93624B}Nozomi{/color} {color=#FFFFFF}and{/color} {color=FF89AB}Hiroko{/color}"
            show Nozomi_K_Bedroom open
            show Hiroko_K_Bedroom open
        multi "No..." with dissolve
        "Given the evidence I'm finding that REALLY hard to believe..."
        if pursued == "Hiroko":
            show Nozomi_K_Bedroom closed
            show Sayori_K_Bedroom closed
        elif pursued == "Sayori":
            show Nozomi_K_Bedroom closed
            show Hiroko_K_Bedroom closed
        ks frown "It's alright, girls. You can say what's in your hearts. There is no need to be anything but completely honest with me." with dissolve
        ks "So I'll ask you both again: Was your true intention today for me to hypnotize you?"
        if pursued == "Hiroko":
            show Nozomi_K_Bedroom open
            show Sayori_K_Bedroom open
        elif pursued == "Sayori":
            show Nozomi_K_Bedroom open
            show Hiroko_K_Bedroom open
        multi "No..." with dissolve
        if pursued == "Hiroko":
            show Nozomi_K_Bedroom closed
            show Sayori_K_Bedroom closed
        elif pursued == "Sayori":
            show Nozomi_K_Bedroom closed
            show Hiroko_K_Bedroom closed
        "Ugh, even while hypnotized they're still somehow managing to be stubborn." with dissolve
        "They seemed pretty furious with me just now, as if they really did believe that \"brainwashing\" bullshit."
        "But again, the facts are clear. I know I'm right about their true intentions."
        "If they seriously believed that crap, they never would've let me put them under. Not in a million years."
        "I just need to make them realize they can't hide their embarrassing truth from me any longer."
        ks "But Nozomi, consider how easy it was to fall back into a nice relaxing trance under me. How natural and right it felt to do so."
        ks "You could have resisted, Nozomi, if you truly wanted to. It's a fact that you cannot hypnotize an unwilling subject."
        show Nozomi_K_Bedroom open
        n "Not... n-not will- {w=1.0}{nw}" with dissolve
        # ks irritated "You need to stop lying to yourself, Nozomi. You cannot argue with the simple fact that you allowed yourself to be hypnotized."
        ks irritated "You need to stop lying, Nozomi. You cannot argue with the simple fact that you allowed yourself to be hypnotized."
        show Nozomi_K_Bedroom closed
        ks frown "You were hypnotized. And ultimately that was your choice. Don't you agree, Nozomi?" with dissolve
        show Nozomi_K_Bedroom open
        n "A-... Agree..." with dissolve
        show Nozomi_K_Bedroom closed
        ks "That's right, Nozomi. You cannot argue this simple logic." with dissolve
        ks "This is the third time I have hypnotized you now, Nozomi. The third time you chose, so very willingly, to fall into a deep relaxing trance for me."
        ks "It's obvious then, that for all your angry protestations earlier, you actually love to be hypnotized but you are deeply ashamed of that fact."
        if pursued == "Sayori":
            ks "So you concocted an absurd story about me \"brainwashing\" Sayori and that she needed your help, when in reality you always knew she was fine."
            show Nozomi_K_Bedroom open
            n "I... w-wha...?" with dissolve
        elif pursued == "Hiroko":
            ks "So you concocted an absurd story about me \"brainwashing\" Hiroko and that she needed your help, when in reality you always knew she was fine."
            show Nozomi_K_Bedroom open
            n "I... w-wha...?" with dissolve
        "I'll just keep talking through what I think is going on with her and the truth will surface, I'm sure."
        show Nozomi_K_Bedroom closed
        ks "When you were hypnotized at the culture fest last year, you loved the experience so much that you wanted to be hypnotized again." with dissolve
        ks "You didn't realize that I was hypnotizing you at first, because I wanted you to forget."
        ks "But the moment you discovered what had happened you were desperate for more."
        ks "But you couldn't just ask to be hypnotized, Nozomi. You were too embarrassed to admit your desires."
        ks "That's why you needed a cover story. You could confront me over an imagined outrage and let yourself be \"tricked\" into going under for me."
        if pursued == "Sayori":
            ks "All you really wanted was to be hypnotized again and you simply couldn't admit it to Hiroko or to me."
        elif pursued == "Hiroko":
            ks "All you really wanted was to be hypnotized again and you simply couldn't admit it to Sayori or to me."
        ks "And that's what's really going on with you. Isn't it, Nozomi?"
        show Nozomi_K_Bedroom open
        n "U...uh..." with dissolve
        ks "No more denial, Nozomi. I've laid out the facts clearly, and you must accept the truth of my words. Yes?"
        n "Y-{w=1.0}...yes..." with dissolve
        show Nozomi_K_Bedroom closed
        ks "That's right. It feels good to accept the truth, Nozomi." with dissolve
        "I next turn to look at the other girl sitting entranced on my bed."
        if pursued == "Hiroko":
            ks "And Sayori, you must have been curious about hypnosis after hearing about it from Nozomi. Very curious."
            show Sayori_K_Bedroom open
            s "Very curious..." with dissolve
            show Sayori_K_Bedroom closed
            ks "So then, when you agreed to come here with Nozomi you knew you could be hypnotized. Did that thought excite you?" with dissolve
            show Sayori_K_Bedroom open
            s "... No?" with dissolve
            show Sayori_K_Bedroom closed
            "Bullshit." with dissolve
            ks frown "Sayori, it's obvious that you're not being honest with me."
            ks "Just like Nozomi, you were very eager, very willing, to fall into a trance for me."
            ks "So in reality, when Nozomi told you her plan you were very excited at the prospect of becoming hypnotized. You even skipped cram school to come here."
            show Sayori_K_Bedroom open
            s "N... t-that's not..." with dissolve
            show Sayori_K_Bedroom closed
            ks "And you went along with Nozomi's crazy story about Hiroko being \"brainwashed\"." with dissolve
            ks "By doing that, you could come here and satisfy your curiosity without revealing your true intentions."
            ks "Isn't that right?"
            show Sayori_K_Bedroom open
            s "T-that's..." with dissolve
            ks "Just admit it, Sayori. To me, to Nozomi and to yourself. You're not fooling anyone."
            ks "Are you?"
            s "N-no...not fooling anyone..."
            show Sayori_K_Bedroom closed
        elif pursued == "Sayori":
            ks "And Hiroko, you must have been curious about hypnosis after hearing about it from Nozomi. Very curious."
            show Hiroko_K_Bedroom open
            h sleeptalk_concerned "Y-yeah... very curious..." with dissolve
            show Hiroko_K_Bedroom closed
            ks "So then, when you agreed to come here with Nozomi you knew you could be hypnotized. Did that thought excite you?" with dissolve
            show Hiroko_K_Bedroom open
            h "Eh? N-no..." with dissolve
            show Hiroko_K_Bedroom closed
            "Bullshit." with dissolve
            ks frown "Are you truly being honest with me, Hiroko? Just like Nozomi, you were very eager, very willing, to fall into trance for me."
            ks "So in reality, when Nozomi told you her plan you were very excited at the prospect of becoming hypnotized. You even skipped tennis practice to come here."
            show Hiroko_K_Bedroom open
            h "N...no, that ain't it... was because-{w=1.5}{nw}" with dissolve
            ks "And you went along with Nozomi's crazy story about Sayori being \"brainwashed\"."
            show Hiroko_K_Bedroom closed
            ks "Because if you did so, you could come here and satisfy your curiosity without revealing your true intentions." with dissolve
            ks "Isn't that right?"
            show Hiroko_K_Bedroom open
            h "That... t-that don't make s-{w=1.5}{nw}" with dissolve
            ks "Admit the truth of my words, Hiroko. You're not fooling anyone."
            show Hiroko_K_Bedroom closed
            ks "So you'll tell the truth now?" with dissolve
            show Hiroko_K_Bedroom open
            h "Y-yeah... tell the truth..." with dissolve
            show Hiroko_K_Bedroom closed
        ks frown "That's better. So now that I've exposed your lies, girls, I am going to ask you two once more, and this time you WILL be completely honest with me." with dissolve
        ks "What was the true reason you both came here today?"
        show Nozomi_K_Bedroom open
        if pursued == "Hiroko":
            show Sayori_K_Bedroom open
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom open
        multi "We wanted you to hypnotize us." with dissolve
        show Nozomi_K_Bedroom closed
        if pursued == "Hiroko":
            show Sayori_K_Bedroom closed
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom closed
        "There. I fucking knew it." with dissolve
        "After all their theatrical shouting and crying and threatening, it turns out they were a couple of hypno lovers in denial."
        "These girls are such ridiculous liars."
        ks frown "There. It feels so much better to be truthful with me, doesn't it, girls?"
        show Nozomi_K_Bedroom open
        if pursued == "Hiroko":
            show Sayori_K_Bedroom open
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom open
        multi "Yes... so much better..." with dissolve
        show Nozomi_K_Bedroom closed
        if pursued == "Hiroko":
            show Sayori_K_Bedroom closed
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom closed
        "I chuckle lightly to myself. My anger at their bullshit is quickly giving way to the realization that I have a couple of budding hypno addicts with me." with dissolve
        "And now that I have a chance to breathe and play back this whole routine in my head, knowing now that this is how they wanted it to end..."
        "Damn, that's hot as hell. I had no idea Nozomi was THIS much into hypnosis stuff, and it's making me excited about her all over again."
        # "And that one of them just happens to be my crush. Who would've thought she'd be into this stuff?"
        "... But yeah, at least we cleared that up, even if it got a little hairy for a while. That's the main thing."
        ks chuckle "That's good, girls. It's good that you both love to be hypnotized. Accept it, cherish it, and realize how silly you were to try and hide it from me and from each other."
        ks "Now, I will count to five, and as I count you will both gradually return to wakefulness, awaking fully and refreshed on five."
        ks "Do you understand, girls?"
        show Nozomi_K_Bedroom open
        if pursued == "Hiroko":
            show Sayori_K_Bedroom open
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom open
        multi "Yes..." with dissolve
        show Nozomi_K_Bedroom closed
        if pursued == "Hiroko":
            show Sayori_K_Bedroom closed
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom closed
        ks smile "One... gently beginning to stir." with dissolve
        stop music fadeout 10.0
        ks "Two... remembering you were hypnotized, just like you wanted."
        ks "Three... accepting that you love to be hypnotized, and that it was wrong of you to lie to me."
        ks "Four... beginning to open your eyes, more and more aware. More and more awake."
        show Nozomi_K_Bedroom relaxed sleepy
        if pursued == "Hiroko":
            show Sayori_K_Bedroom upright sleepy
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom relaxed sleepy
        ks "That's right. And..." with longdissolve
        show Nozomi_K_Bedroom relaxed surprised
        if pursued == "Hiroko":
            show Sayori_K_Bedroom upright surprised
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom relaxed surprised
        ks "Five." with dissolve
        show Nozomi_K_Bedroom smile
        if pursued == "Hiroko":
            show Sayori_K_Bedroom smile
            s "Huh. That was... quite the experience~" with dissolve
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom smile
            h "Oh... Oh wow, did that really happen?" with dissolve
        ks smile "Rise and shine, girls."
        play music Beautiful
        show Nozomi_K_Bedroom blush
        n "Oh my god, Kyou, that felt so good. How long have you been doing this?" with dissolve
        ks "Er... well, I've been studying it a while, but I've only been practicing for about a week?"
        show Nozomi_K_Bedroom surprised
        n "A-are you serious?! That's incredible!" with dissolve
        show Nozomi_K_Bedroom smile
        n "It felt so... so powerful. Like I really couldn't do anything but drop deep into a trance and listen to that voice of yours." with dissolve
        show Nozomi_K_Bedroom laugh
        n "I think I love it~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
        if pursued == "Hiroko":
            show Sayori_K_Bedroom blush
            s "I know what you mean. I had no idea what to expect but that was better than anything I had in my mind." with dissolve
            show Sayori_K_Bedroom seductive
            s "Do it again?" with dissolve
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom raised laugh
            h "Right? I'm still feeling tingly from that!" with dissolve
            show Hiroko_K_Bedroom smile blush
            h affectionate blush "Y'wanna do it to me again? I won't mind~" with dissolve
        "I chuckle and shake my head."
        "I mean, I kinda want to, especially now as I know they're into it, and I'm DEFINITELY into it..."
        "But the rational part of me knows I can't just pretend what they did didn't happen."
        ks smirk "Considering the shit you two just pulled, I think a little taste is all you're going to get today."
        show Nozomi_K_Bedroom smile
        if pursued == "Hiroko":
            show Sayori_K_Bedroom pout
            s "Oh, you tease. Although I should get going soon anyway." with dissolve
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom relaxed noblush sad
            h "Awww..." with dissolve
        show Nozomi_K_Bedroom sad
        n "Yes... We owe you a MASSIVE apology, Kyou." with dissolve
        if pursued == "Hiroko":
            show Sayori_K_Bedroom confused
            s "Yes... I apologize for earlier, Kyou. I'm usually better than that." with dissolve
            show Sayori_K_Bedroom sleep open
            s "When I look back on what we did, I am thoroughly ashamed of myself. I beg your forgiveness." with dissolve
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom blush
            h "Yeah... We shoulda asked you straight up instead of being so dumb about this." with dissolve
            h "I'm really sorry, Kyou!"
        n "Me too... I can't believe how far we went with all that. I even called you evil at some point?"
        ks neutral "You did, yeah."
        show Nozomi_K_Bedroom sleep open
        n "I'm so embarrassed. And I am so, so sorry, Kyou." with longdissolve
        n "If you don't forgive us, I'll understand. What we did was truly terrible."
        ks smile "Apology accepted, both of you. At least nobody was hurt, and I got you to learn something about yourselves today."
        show Nozomi_K_Bedroom relaxed laugh
        if pursued == "Hiroko":
            show Sayori_K_Bedroom upright laugh
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom laugh
        multi "Ehehehe~" with dissolve
        if pursued == "Hiroko":
            show Sayori_K_Bedroom noblush smile
            s noblush "We should do this again sometime. But for now, I suppose I should get back to my books." with dissolve
            show Nozomi_K_Bedroom noblush smile
            ks "We'll see you out." with dissolve
            $persistent.k_bedroom_confrontation_sayori_unlock = True
        elif pursued == "Sayori":
            show Hiroko_K_Bedroom noblush smile
            h "Alright, I gotta get some practice in, but Kyou, hit me up if you wanna hypnotize me again sometime. I'm serious~" with dissolve
            show Nozomi_K_Bedroom noblush smile
            ks "I'll keep that in mind." with dissolve
            $persistent.k_bedroom_confrontation_hiroko_unlock = True
        scene bg k entrance day
        show Nozomi front smile casual at center
        if pursued == "Hiroko":
            show Sayori casual smile_right at center:
                xpos 0.75
            with blink
            s "Thanks for having me, Kyou." with dissolve
            ks smile casual "Like I had a choice."
            s laugh casual_folded "Hah~" with dissolve
            show Nozomi side casual laugh at flip
            n "See you later, Sayori~" with dissolve
            ks smile "Take care, Sayori."
            s smile_right "Goodbye, you two. This has been fun." with dissolve
            hide Sayori
        elif pursued == "Sayori":
            show Hiroko casual smile at center:
                xpos 0.75
            with blink
            h "You two're coming to see me play tomorrow, right?"
            show Nozomi side laugh at flip
            show Hiroko smile_side
            n "Wouldn't miss it for the world~" with dissolve
            ks smile casual "We'll be there."
            h laugh casual_armup "Hehe, yay~" with dissolve
            n smile_side "See you soon, Hiroko!" with dissolve
            ks "Take care, Hiroko."
            h happy "Laters~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
            hide Hiroko
    stop music fadeout 10.0
    play sound doorclose
    hide Nozomi
    show Nozomi front smile casual
    "The moment the door closes it hits me." with dissolve
    n "So what do you want to do now, Kyou?"
    "We're finally alone together, with no one to interrupt us."
    n pout_left casual_folded "I mean, I don't really have anywhere to be today, and it feels like we have so much to talk about..." with dissolve
    ks "Yes. Yes, we do."
    scene bg k room day
    show Nozomi front2 casual smile at center
    with blink
    "I usher her into my living room as we both take a moment to collect ourselves."
    n chuckle "So... I guess we have something in common after all. With the hypnosis, I mean~" with dissolve
    ks casual chuckle "Ah, yes. I'm still surprised about how into it you are."
    n front laugh "Ehehehe~" with dissolve
    ks confused "So... Nozomi?"
    n smile "Yes, Kyou?" with dissolve
    "Okay, here we go. The time is right, and I'm bursting with confidence."
    "This is my moment."
    ks "You're not seeing anybody right now are you? I mean, romantically?"
    n concerned "Oh, um... no, Kyou. I'm not." with dissolve
    ks smile "... Would you like to?"
    n smile casual "..." with dissolve
    n neutral_left "Kyou, please don't take this the wrong way, but I'm just not interested in a relationship right now." with dissolve
    "... What?"
    n concerned "What with everything going on... Graduation, college, you know?" with dissolve
    "Did she just..."
    n smile "I don't think I have the time to start anything like that at the moment." with dissolve
    "... reject me?"
    n chuckle "But, um, I'm flattered that you asked. Really, I am." with dissolve
    "No... no, I don't believe this; she's denying her own feelings again. And after everything we just went though!"
    n smile "But, well, I've made it this far without dating so I may as well graduate first, right?" with dissolve
    "But alright. If this is the only way to get through to her. The only way to expose how she really feels..."
    n concerned "... Right?" with dissolve
    "Then so be it."
    show Nozomi surprised
    $light_x = 0.43; light_y = 0.25; ldirection = "right"; lnumber = 1
    call lightshow from _call_lightshow_53
    n "Kyou? Kyou, what are you doing?" with dissolve
    call lightshow from _call_lightshow_54
    play music Flow
    ks frown "Just look into the light, Nozomi. There's no need to be alarmed."
    call lightshow from _call_lightshow_55
    n neutral "Wait..." with dissolve
    call lightshow from _call_lightshow_56
    ks "Watching the light, Nozomi. Feeling relaxed. Feeling drowsy."
    call lightshow from _call_lightshow_57
    n drowsy "K-kyou, please..." with dissolve
    call lightshow from _call_lightshow_58
    ks "Feeling sleepy, Nozomi. Eyelids becoming heavy."
    call lightshow from _call_lightshow_59
    call lightshow from _call_lightshow_60
    n sleepy "..." with dissolve
    ks "Sleep."
    n sleep "..." with dissolve
    show Nozomi:
        linear 3.0 ypos 1.3
    stop music fadeout 5.0
    jump Epilogue_NonCon_Kyou

label Day6_Villain_Kyou:
    if hypno1 == "devoted hiroko" or hypno1 == "devoted sayori":
        scene bg cafe eve with longblink
        "I take a breath as I glance across the street, watching a bus pulling in."
        "She's late. Why is she late?"
        "Things have gone according to plan so far, but this is the moment of truth."
        # "Still, she did at least agree to meet me. Even if it had to be a public place."
        play music Eons
        show Nozomi front casual neutral
        n "Kyou." with dissolve
        "I look up and smile in relief."
        ks casual smile "Thanks for agreeing to see me."
        n frown "Yeah. In a public place, so don't try anything." with dissolve
        ks sigh "Ouch..."
        "I suck through my teeth and gesture to the other seat at my table."
        ks neutral "Can I get you anything?"
        show NozomiCafe casual_folded stern nocup
        with blink
        n "No, it's fine. I'm not staying long; I just want to hear what you have to say for yourself."
        ks "Yeah. Fair enough, I guess."
        "She crosses her legs as she reclines a little on the café chair, keeping her arms folded defensively."
        ks "I don't have it, by the way. If that's what you're wondering?"
        show NozomiCafe casual_leaning pensive
        n "No?" with dissolve
        "I hold my hands open to show her there's nothing hiding there, then lay them flat on the table."
        ks sigh "No. I realize that penlight freaks you out, and I understand that."
        show NozomiCafe stern
        n irritated "You should destroy it." with dissolve
        ks frown "I... Why would I do that?"
        show NozomiCafe growl
        n frown "Because you have a shred of common decency? Is that too much to expect of you?" with dissolve
        ks "Nozomi, I've stumbled on something incredible. I can't just... destroy an invention like that."
        show NozomiCafe angry
        n angry "Then I guess I've wasted my time!" with dissolve
        ks surprised "H-hey Nozomi, shh, calm down. We're in public."
        show NozomiCafe casual_leaning
        n "You hurt one of my closest friends, Kyou. Because you couldn't have ME!"
        ks frown "Hey, when I said calm, I meant it. Please? We're just calmly having a conversation here."
        show NozomiCafe stern
        n irritated "How is she, anyway?" with dissolve
        ks "Who?"
        if hypno1.find("hiroko"):
            if hypno1 == "devoted hiroko":
                n "Hiroko. I heard she's your number one fan now. Can't imagine how that happened."
            show NozomiCafe stern_side
            n "She even tried to lure me to my favourite karaoke place. Just me and her. You wouldn't happen to know about that, would you?" with dissolve
            ks neutral "I don't see the problem. You like karaoke, right? Sounds like she was thinking to calm you down."
            show NozomiCafe casual_leaning stern
            n frown "The problem is she wouldn't take no for an answer. But she's always respected my wishes in the past." with dissolve
            ks "Are you sure you weren't overthinking things? It sounds to me like you just saw her in a bad light."
            show NozomiCafe angry
            n "Don't patronize me. I KNOW Hiroko." with dissolve
            ks "I'm sorry. I just want you to think things through calmly, and not make any rash judgements."
            show NozomiCafe casual_folded growl
            n "I'm not doing anything rash. If anything I'm being far too reasonable giving you the time of day like this." with dissolve
            ks "Were you calm when you decided to quit school because of me?"
            show NozomiCafe surprised
            n surprised "... How do you know about that?" with dissolve
            ks "Calm yourself, it doesn't matter. All that matters is that you stay calm for me."
            show NozomiCafe pensive
            n neutral "I'm not... I'm not doing this; how are you doing this?" with dissolve
            ks "Shh, there's no need to worry about that, Nozomi. You just need to stay calm. Calmer, as your mind and body drop down. Dropping deep..."
            show NozomiCafe sleepy
            $ renpy.transition(longdissolve, layer="master")
            n drowsy "I... S-somebody help..."
            ks "Deeper. Even the hustle and bustle around us is making you calm, Nozomi. Helping you drop even deeper."
            show NozomiCafe sleepy_entranced
            ks "Keeping your eyes wide open and your body stuck to the chair,{nw}" with dissolve
            show NozomiCafe hand1
            $ renpy.transition(dissolve, layer="master")
            extend "staying nice and calm as you... {w=0.5}{nw}"
            play sound fingersnap
            show NozomiCafe hand2
            stop music
            extend "{w=0.2}{nw}"
            show NozomiCafe nohand
            $ renpy.transition(dissolve, layer="master")
            show NozomiCafe neutral_entranced
            $ renpy.transition(dissolve, layer="master")
            extend " sleep for me."
            "As I snap my fingers I smile delightedly as Nozomi's eyes quickly glaze over."
            play music Flow
            ks smile "Very good, Nozomi. We look just like any other young couple on a date, don't we?"
            ks "So long as we don't raise our voices or make any rash movements we'll be beneath anyone's notice."
            ks "And you won't be doing that now, will you, Nozomi? No, you won't."
            "It's true. There are people walking past us in the street, people coming and going from the café, but no-one seems to be doing more than glance our way."
            "And I gotta say, all this power-tripping I've been doing over the last few days has done wonders for my social anxiety."
            ks "I'm sure somewhere in there you're wondering how this happened."
            ks "But you don't need to worry, Nozomi. Everything is fine. Just focus on dropping deeper for me."
            ks "Feeling so good. Feeling so right. Letting the ambient noise of the street pull you deeper. Always deeper."
            ks "And as you go deeper, feel the corners of your mouth curling upwards. So easy to form a smile on your lips as you stay deeply asleep."
            show NozomiCafe smile_entranced
            ks "That's it, Nozomi. So easy to smile. And now when you feel me take your hand you're going to rise slowly from your chair and let me guide you forward." with dissolve
            $persistent.nozomi_cafe_villain_unlock = True
            hide NozomiCafe
            show Nozomi front2 casual entranced_smile:
                ypos 1.2
                linear 2.5 ypos 1.0
            with blink
            ks "Moving forward with me now. Still deeply asleep, just following my lead as we walk. Very good."
            stop music fadeout 5.0
            scene bg blackscreen with fade
            "Very good."
            pause 2.0
            # scene bg k room eve
            # show Nozomi front sleepy casual at center:
            #     ypos 1.1
            scene NozomiCaptured base1 dazed with longdissolve
            play music Measured
            n "Wha... Wh-what is this? Where am I...?"
            ks casual smirk "You're in my house, Nozomi. We walked here, don't you remember?"
            n "I... Oh no."
            ks "Yes, you remember. You may also realize that you are still quite deeply hypnotized."
            ks "That's why you'll find yourself unable to raise your voice beyond a normal speaking volume, and it's why you can't move a muscle from where you are now."
            ks "You know I'm not going to hurt you anyway, Nozomi. We're just going to have a nice little chat."
            ks "So just relax and don't worry about a thing. You're perfectly safe here."
            show NozomiCaptured sigh
            n "I still don't..." with dissolve
            ks "Don't what?"
            show NozomiCaptured dazed
            n "Don't understand. How?" with dissolve
            ks "How you were hypnotized in the first place? You weren't supposed to know, but I guess there's no point in hiding it from you now."
            ks "Think back, Nozomi. Thinking back... It was around five hours ago."
            ks "You were relaxing at home, in your room. There was a phone call..."
            ks "It's okay to remember, Nozomi. Tell me what happened."
            n "..."
            stop music
            show NozomiCaptured surprised
            n front surprised "Ah!" with dissolve
            scene bg n bedroom eve bw
            if persistent.NewSprite == "":
                    $n = Character("[nozomi_name]", image = "NozomiFlashbackOld", who_color = "#D0755B")
                    show NozomiFlashbackOld front casual surprised at center
            else:
                $n = Character("[nozomi_name]", image = "NozomiFlashback", who_color = "#93624B")
                show NozomiFlashback front casual surprised at center
            with flash
            play sound cellvibratelong
            n "Huh?"
            n side sad_closed "*sigh* God. People need to stop calling me." with dissolve
            n "..."
            n sad "Oh, huh... Okay." with dissolve
            stop sound
            n front pout_left "Sayori? Hi!" with dissolve
            s "\"Nozomi. How are you holding up?\""
            n sigh "Oh, you know. I've only had one anxiety attack this morning." with dissolve
            n "So... good, I guess?"
            s "\"I am so sorry you are going through this.\""
            n "Thanks..."
            n side sad_side "..." with dissolve
            n sad_closed "I upset my brother yesterday." with dissolve
            s "\"What?\""
            n "You know he goes to our school, right?"
            s "\"Of course.\""
            n sad_side "Obviously I wasn't coming to school, so I laid in a bit. And then I got up to use the bathroom." with dissolve
            n front sleeptalk_concerned "And just as I come out of my room, the bathroom door opens and he's standing there." with dissolve
            n "Then I just... I don't know, I just screamed at him."
            s "\"...\""
            n concerned "I suppose I was still waking up, but seeing him in our school's uniform, and with his hair kinda unkempt as it was..." with dissolve
            n "For a second I thought it was Kyou standing there."
            s "\"Nozomi... I am so sorry.\""
            n "Yeah..."
            s "\"Does your brother understand what you are going through?\""
            n sigh "I don't think he does. Also, he's been having a hard time adjusting to high school and it's affected his self-esteem." with dissolve
            n "Certainly isn't helpful having his big sister screaming at him like he's some kind of monster."
            s "\"Please do not blame yourself for that. I'm sure he will come to understand, and your reaction seems perfectly natural to me.\""
            n side smile "Heh, I'll try to keep that in mind. Thanks for listening to me whine, Sayori." with dissolve
            s "\"I would hardly call it whining, but you're welcome.\""
            n "So anyway, how are you doing?"
            s "\"Very well, actually. I might have some good news for you?\""
            n front surprised "Oh?" with dissolve
            s "\"It seems Kyou is about to quit the school to mitigate the damage he caused for himself by hurting you.\""
            n side frown "Wait, you talked to him?" with dissolve
            s "\"Oh no. Not directly anyway. I respect your warning about him. Hiroko has effectively become his mouthpiece though, it seems.\""
            n front sigh "Yeah..." with dissolve
            s "\"Of all the people to take his side...\""
            n concerned "It's not her fault." with dissolve
            s "\"No? I am not sure why not?\""
            n "Well..."
            n side sad_closed "*sigh* No, nevermind. I guess I'm still trying to get my head around her betrayal." with dissolve
            s "\"Yes. I have a hard time understanding why people do what they do sometimes.\""
            n "Yeah..."
            s "\"... Nozomi?\""
            n sad_side "Hm?" with dissolve
            s "\"Are you in your room right now?\""
            n front surprised "Yeah, why?" with dissolve
            s "\"Could you go up to the window?\""
            n "Uh, again, why?"
            s "\"I thought I could teach you a relaxation technique. I sometimes use it to help manage my own stress.\""
            s "\"At a time like this I think you may find it useful. Are you game?\""
            n "Okay... Sure, I guess."
            show NozomiWindow bedroom_bw body_bw anxious_bw glasses_bw front_bw with blink
            n frown casual "Alright, I'm looking out the window. What now?" with dissolve
            s "\"Just... I want you to take a deep breath and look at what is out there.\""
            s "\"Perhaps the neighbor's houses across the street. Or that sakura tree over by the park. It doesn't matter, just anything you find appealing right now.\""
            show NozomiWindow sigh_bw
            n sigh "Honestly I'd just like to go outside again soon. It's only been a couple days and I'm already feeling myself go stir crazy being cooped up in here." with dissolve
            s "\"I sympathize. So did you find something?\""
            show NozomiWindow smile_bw
            n smile "The sakura tree, yes." with dissolve
            show NozomiWindow smile_light_bw hiroko_bw with dissolve
            show NozomiWindow smile_bw nohiroko with dissolve
            s "\"I thought you might. I often enjoy staring at the cherry blossoms, myself. I find them very relaxing.\""
            show NozomiWindow smile_light_bw hiroko_bw with dissolve
            show NozomiWindow smile_bw nohiroko with dissolve
            n "Mm, yes. I never noticed how well they catch the light before."
            s "\"Right. And recall their scent. How it reminds us of spring time. A happier time.\""
            n "Gosh, yes."
            show NozomiWindow smile_light_bw hiroko_bw with dissolve
            show NozomiWindow smile_bw nohiroko with dissolve
            show NozomiWindow surprised_bw with dissolve
            n surprised "Hey, isn't that...{w=0.4}{nw}" with dissolve
            show NozomiWindow surprised_light_bw hiroko_bw with dissolve
            show NozomiWindow surprised_bw nohiroko
            s "\"Inhale deeply and imagine that scent filling your nostrils.\"" with dissolve
            show NozomiWindow surprised_light_bw hiroko_bw with dissolve
            show NozomiWindow surprised_bw nohiroko with dissolve
            show NozomiWindow neutral_bw nohiroko
            $ renpy.transition(longdissolve, layer="master")
            n "Mmm..."
            s "\"Do you smell them, Nozomi?\""
            show NozomiWindow neutral_light_bw hiroko_bw with dissolve
            show NozomiWindow smile_bw nohiroko
            n smile "I do." with dissolve
            s "\"Wonderful. Feeling more and more relaxed with each time you inhale deeply, and feeling all your pent-up tension drain away with each exhale.\""
            s "\"Breathing in calm.\""
            show NozomiWindow smile_light_bw hiroko_bw with dissolve
            show NozomiWindow smile_bw nohiroko with dissolve
            s "\"Breathing out stress.\""
            show NozomiWindow smile_light_bw hiroko_bw with dissolve
            show NozomiWindow smile_bw nohiroko with dissolve
            s "\"That feels so much better, does it not?\""
            n "Yeah... So much better."
            s "\"So much better. Each and every breath you take putting you in a deeper state of relaxation.\""
            show NozomiWindow smile_light_bw hiroko_bw with dissolve
            show NozomiWindow sleepy_bw nohiroko
            $ renpy.transition(longdissolve, layer="master")
            s "\"But even as you relax so very deeply, you will find you can always keep your phone held to your ear, and are always able to stare ahead at the sakura tree.\""
            s "\"Breathing in...\""
            s "\"Holding...\""
            show NozomiWindow sleepy_light_bw hiroko_bw with dissolve
            show NozomiWindow entranced_bw nohiroko
            $ renpy.transition(longdissolve, layer="master")
            s "\"Breathing out, even more relaxed. Even more deep.\"" with dissolve
            s "\"Can you still hear me, Nozomi?\""
            n "Yes."
            s "\"Very good. Breathe in...\""
            s "\"Breathe out... Dropping deeper.\""
            s "\"Deeper. Keeping your phone held close to your ear at all times as you...\""
            s "\"Sleep.\""
            $ persistent.nozomi_window_unlock = True
            scene NozomiCaptured base1 dazed
            $n = Character("[nozomi_name]", image = "Nozomi", who_color = "#93624B")
            with longflash
            play music Rain
            ks casual smile "Not that I was there when it happened, but from that retelling, it sounds like you recalled it perfectly."
            show NozomiCaptured sigh
            n "Sayori... n-no..." with dissolve
            ks "Yes, Sayori. After putting you to sleep, she went through some mental conditioning with you that set you up for our meeting a little while ago."
            ks "You did everything you were supposed to."
            ks "But if you're wondering why I didn't just have you present yourself to me here instead of going through with that café thing, well..."
            ks "We weren't sure how effective the penlight would be from across the street and through a window."
            ks "And I know how you feel about me right now, rightly or wrongly. So... we felt with the weaker light you might have resisted such a direct suggestion as that."
            ks "We had to transition you slowly, you understand. Just to be sure."
            show NozomiCaptured dazed_left
            n sleepy "Sayori... Oh my god, how could you?" with dissolve
            show NozomiCaptured base2
            ss casual concerned_right "It had to be done, Nozomi. Kyou knows what is best for us." with dissolve
            n "I told you to stay away from him. I told you."
            ss "I did my best. It just turned out Kyou is better than me."
            ss laugh_right blush "He is better than all of us~" with dissolve
            show NozomiCaptured base3
            hs casual happy blush "Yeah! Gotta hand it to him, we didn't stand a chance against Kyou~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
            n "Hiroko. That was you outside my house, wasn't it?"
            hs laugh "Totes! I thought you were gonna freak out for sure when it looked like you saw me, but you just loved staring at that sakura tree too much~"
            hs "Made it super easy to keep Kyou's penlight in your eyes."
            ks "Which reminds me; I'm gonna need that back again, Hiroko."
            hs happy_closed  "Eheheh, 'kay 'kay. Here ya go."
            "I can't resist allowing myself a wry grin as I take the penlight back from Hiroko and pocket it safely."
            ks smirk "I don't intend to make a habit of praising these two, Nozomi, but I have to admit; I never would've gotten you without the hard work and dedication of your friends."
            ks "They REALLY came through for me today."
            ss shocked "Hiroko, he... he praised us!"
            hs cry_happy "He... Holy shit, he really did!"
            hs cry_joy "AAAAAAAAAAAA I'M SO HAPPY I COULD DIIIIEEEE!!" with shake
            ss laugh_right "*squeal* Thank you so much, Kyou! I LIVE for your approval!"
            show NozomiCaptured dazed
            n "... Why are you doing this, Kyou?" with dissolve
            ks neutral "Doing what?"
            n "Torturing me. Why am I not like they are yet?"
            ks frown "Because... I'm still conflicted about you, Nozomi."
            n "Conflicted?"
            ks neutral "I studied hypnosis for you. I watched you dropping deep for that hypnotist during the culture festival last year and I was inspired."
            ks "But this last week has made me question how I truly feel about you. And how I feel about myself."
            if hypno1.find("devoted", 7) and hypno5.find("devoted",7):
                ks frown "After I spent this week brainwashing your friends into becoming my devoted groupies I had to re-examine those feelings."
            ks "And what I realized is..."
            menu:
                "I still want you for my girlfriend":
                    ks neutral "When it comes down to it, my feelings about you haven't changed so much that I've stopped wanting you. Far from it."
                    ks "I know I could make anyone love me with this penlight in my hand. After what it's done to you three there's no doubt in my mind about that."
                    ks "And... sure, I could find someone better looking and make her mine. But what would be the point? She wouldn't mean anything to me."
                    ks "But you, Nozomi. It's like I said, I studied hypnosis because of you. I made this penlight of mine for you."
                    "I then make a point of gesturing to Hiroko and Sayori, who grin stupidly as they register my attention."
                    ks "You're the reason for all of this. I did it all for you, so that's why..."
                    ks "... That's why I need you to love me, Nozomi Akemi."
                    "I watch as Nozomi's lower lip quivers. Her mind, foggy as it'll be from about a dozen active hypnotic suggestions, must be trying so hard to work for her."
                    show NozomiCaptured angry
                    n "A-and do you think that's... love, Kyou? This... this obsession?" with dissolve
                    n "We all knew there was something dangerous about you. The way you wouldn't leave us alone for all these years. There just had to be."
                    n "We didn't know what to do about you; no one else would listen to us, but..."
                    show NozomiCaptured sigh
                    n sleeptalk "But I never could've imagined that you'd do something like this." with dissolve
                    n "It shouldn't be possible. It... it shouldn't..."
                    "I scoff at her, shaking my head."
                    show NozomiCaptured dazed
                    ks frown "Maybe if you gave me a chance before then none of this would've happened." with dissolve
                    ks "You never even TRIED to talk to me. None of you did."
                    ks "I don't know if what I feel for you now is love or whatever, Nozomi. It doesn't matter anymore. We're past all that."
                    ks "You'll all be trying a lot harder for me from now on."
                    "Nozomi, drained as she is on the floor, lets out a hollow chuckle."
                    show NozomiCaptured angry
                    n sleeptalk "You can brainwash us all you want with that light. Make us say and do whatever your sick mind can think of to make you feel better..." with dissolve
                    n "But nothing is making you do these things that you're doing. These... horrible things."
                    n "No matter what happens with us, you'll always know the truth."
                    n  "{cps=15}You'll always know you're a monster-{/cps}{w=1.0}{nw}"
                    stop music fadeout 5.0
                    ks "Sleep, Nozomi."
                    show NozomiCaptured sleeptalk
                    n sleeptalk "N-n..." with dissolve
                    queue music Flow
                    ks "That's right, Nozomi. You can't resist me; you know you've been in and out of my hypnosis all day long. You know how good this feels."
                    show NozomiCaptured sleep
                    ks "So just sleep, let all the tension out of your body and let yourself fall even deeper for me..." with dissolve
                    "I try to keep a calmness to my voice as I take her back down fully into trance, but... goddamn, she got to me."
                    "But so what if this makes me a monster? Or a creep? Or any of the other vile shit you and the others have thought about me?"
                    "You all pushed me to this. And now I'll make sure you never say those kinds of things to me again."
                    ks neutral "Dropping so deep, Nozomi. So much deeper into hypnosis. Feeling so good, finding it so easy to go deep for me."
                    ks "And now that you're back into this nice, deep state of trance for me, I..."
                    "... This is it. This is what it's all come down to."
                    ks "I..."
                    "I'm hesitating? Why?"
                    ks "I want you to..."
                    "I know what I'm doing to them all is terrible, even if they kinda brought this on themselves. I've made my peace with that."
                    "And all I need are a few more words before Nozomi will be exactly the girl I want her to be. That's what I wanted all along, right?"
                    "Even if it's a lie. Even if it makes me some kind of monster. If that's what it takes to make her mine..."
                    menu:
                        "Then so be it":
                            ks "I want you to think back to our conversation from several days ago."
                            "No more second-guessing myself. I've already thought all of this through. And I've already come this far."
                            ks "Do you remember, Nozomi? How nice and relaxing and safe it feels to consider being in a relationship with me?"
                            show NozomiCaptured sleeptalk
                            n sleeptalk "I don't... it doesn't feel..." with dissolve
                            "It's time to finish what I started."
                            show NozomiCaptured sleep
                            ks "Doesn't feel right? But there's no denying how deeply relaxed you're feeling right now, is there?" with dissolve
                            show NozomiCaptured sleeptalk
                            n sleeptalk "No..." with dissolve
                            show NozomiCaptured sleep
                            ks "So it follows that if you're as completely relaxed as this, then you must also be feeling safe... right?" with dissolve
                            show NozomiCaptured sleeptalk
                            n sleeptalk "... Right." with dissolve
                            show NozomiCaptured sleep
                            ks "You're relaxed around me. Feeling safe and comfortable. So it's only natural if you find yourself considering how you really feel about me." with dissolve
                            ks "If I can make you feel this good, then maybe it's not so strange if you find yourself becoming attracted to me. Find yourself wanting a relationship with me."
                            show NozomiCaptured sleeptalk
                            n sleeptalk "Urrh..." with dissolve
                            show NozomiCaptured sleep
                            ks "There's no stopping it. It's so natural to think about it now." with dissolve
                            ks "The more you consider starting a relationship with me, the more natural it feels. And the more natural it feels, the more right it becomes to want a relationship with me..."
                            ks "And the more right it becomes, the more you realize that you love me, Nozomi."
                            ks "You are experiencing such a deep feeling of love for me now... and I want you to accept that feeling."
                            ks "You can do that for me, can't you, Nozomi?"
                            show NozomiCaptured sleeptalk
                            n sleeptalk "I..." with dissolve
                            n "Y-... yes..."
                            show NozomiCaptured sleep
                            ks "That's good. You're doing so well, accepting these feelings. Allowing that love for me to grow in your heart. Allowing it to become your truth." with dissolve
                            ks "Because the truth is that you love me more than anything in the world. There is no one that you value more than me. Nothing you wouldn't do to make me happy."
                            ks "So it's only natural that you would want to become my girlfriend now... right, Nozomi?"
                            show NozomiCaptured sleeptalk
                            n sleeptalk "Right... I want to become... your girlfriend..." with dissolve
                            show NozomiCaptured sleep
                            ks "Wonderful. So now, in a few moments I'm going to wake you from this deep state of trance and you're going to want to act on your new truth." with dissolve
                            ks "And once you do, you will find that you can speak and move with complete freedom once again."
                            ks "Waking up on a count of five, Nozomi."
                            ks "One, two... Taking a deep breath, feeling energy slowly return to you."
                            ks "Three, four... Beginning to blink. Feeling your head become clearer; thoughts returning."
                            stop music fadeout 5.0
                            ks "And five... wide awake, Nozomi."
                            show NozomiCaptured dazed
                            n sleepy "A-ahhh..." with dissolve
                            "I look down on her, watching as her eyelids pull themselves open to register the sight that greets her."
                            show NozomiCaptured surprised
                            n surprised "K... Kyou?" with dissolve
                            "The sight of someone she's no doubt starting to feel very differently about."
                            ks smile "That's me. Now what was that you were saying about me just now?"
                            show NozomiCaptured dazed
                            n front sleepy "What I was... what I was... s-saying?" with dissolve
                            ks smirk "Something about me being a monster, right?"
                            "Nozomi's eyelids start to flicker violently as her sleepy mind continues its return to clarity, remembering the conversation we were just having."
                            show NozomiCaptured awe
                            "I can almost see the gears shifting in her mind, as she tries to reconcile the things she said with the desire I forced upon her." with dissolve
                            play music LookingGlass
                            show NozomiCaptured sigh
                            n sleeptalk "O-oh... oh, that..." with dissolve
                            ks "You're having second thoughts now, aren't you?"
                            show NozomiCaptured neutral
                            n "K-Kyou, I... I know what I said." with dissolve
                            show NozomiCaptured dazed
                            n concerned "What you've done to me and my friends is wrong. It's so... so wrong." with dissolve
                            show NozomiCaptured sigh
                            n sleep "But it's okay. If it's you, it's okay." with dissolve
                            show NozomiCaptured neutral
                            n neutral "When I think about everything you did. Knowing you learned hypnosis and did all these diabolical things just so you could have me..." with dissolve
                            show NozomiCaptured smile blush
                            n smile blush "It's... it's actually kind of... romantic." with dissolve
                            n "Don't you think?"
                            $persistent.nozomi_captured_unlock = True
                            scene bg k room eve
                            show Nozomi front2 casual loving blush at center:
                                ypos 1.1
                                linear 2.0 ypos 1.0
                            with blink
                            "Nozomi bats her eyelids coquettishly as she picks herself up from the floor before taking a quiet step towards me."
                            show Nozomi:
                                ypos 1.0
                            "And I grin triumphantly as I move to hold the small of her back and look into those beautiful brown eyes of hers."
                            ks casual smirk "Just tell me what I really want to hear."
                            n chuckle "Mhmhmhm..." with dissolve
                            # n "I can't resist, but more than that, I don't want to resist. Not anymore."
                            n happy "I-I love you, Kyou! I can't help it, I love you so much, so please..." with dissolve
                            n laugh "Please make me your girlfriend!" with dissolve
                            show Nozomi chuckle
                            "I answer with a kiss of those invitingly soft lips while I hear my two fangirls squeeing mindlessly beside us." with dissolve
                            "She moans and embraces me fully, and in an instant all those years of rejection and pain at her hands feel like they've been swept away by just this one moment."
                            "Nozomi... you're mine at last."
                            scene bg blackscreen with dissolve
                            "And I'll never let you go..."
                            stop music fadeout 5.0
                            pause 2.0
                            jump Epilogue_Villain_Devoted_Girlfriend
                        "I can't":
                            "If this is what it takes, then..."
                            ks neutral "Dropping... dropping deeper, Nozomi..."
                            "... Then I don't deserve to have her. Do I?"                       
                            ks "Deeper into hypnosis. Letting everything but the sound of my voice fade from your consciousness once more."
                            "And thinking about this now, now that I have this girl of my dreams at my mercy, just a few spoken words away from making her mine? It's made me realise..."
                            ks "And now that you only hear my voice, I..."
                            "I don't want to be a monster after all."
                            ks "I need you to listen very carefully."
                            "I need to set things right again. At least as best as I can."
                            ks "Because everything I tell you from this point on, you will accept as your absolute truth."
                            "Even if it means... my penlight, my year of hard work... was all for nothing in the end."
                            ks "First, you are going to forget every interaction you've had with me this past week, all the way back to when I first hypnotized you in our classroom."
                            ks "You will not recall a single thing that happened between us since that day. And that includes when Hiroko tried to drag you to karaoke."
                            ks "As far as you're aware, none of that ever happened. Understand?"
                            show NozomiCaptured sleeptalk
                            n "Yes... none of that... h-happened..." with dissolve
                            show NozomiCaptured sleep
                            ks "That's good. Every other suggestion I have made to you will disappear as soon as you wake from this state of trance. You only need to forget." with dissolve
                            "So I'm truly going to set things right, undo all of this. And yet... I can't. Not completely, anyway."
                            "Nozomi told people she was quitting school. And I could make her and her friends forget all about that, sure. But her parents?"
                            "No, if I'm going to mend things with them all then I have no choice but to alter their very realities."
                            ks "Instead, what you'll remember about me this week is what I'm about to tell you."
                            "You don't mind, do you, girls?"
                            ks "Nozomi, when we met to clean the classroom that day, I did flash my penlight over your eyes and I did try to hypnotize you."
                            ks "But it wasn't serious; it was just a dumb prank. It obviously didn't work, and we both knew it didn't work. But you felt scared all the same about what I did."
                            ks "So you skipped school and wanted to leave because you couldn't think straight."
                            ks "You were going to go through with it, only Sayori called you this morning to say I wanted to apologize and talk things out with all of you."
                            ks "Obviously you were worried about seeing me again, but Sayori convinced you that it was worth listening to what I had to say."
                            ks "That's why you're all here in my house today.  We talked things through, you accepted my apology, and now you no longer want to leave our school."
                            ks "When I wake you up from this state of trance, these will be the things you remember. Okay, Nozomi?"
                            show NozomiCaptured sleeptalk
                            n "... Okay." with dissolve
                            show NozomiCaptured sleep
                            ks "Good. I want you to think only of these memories. Repeat them in your head over and over until I say it's time to wake..." with dissolve
                            $ GirlfriendReconsidered = True
                            jump Devotion_Reconsidered  
                "I just love being powerful":
                    ks concerned "I didn't love you, Nozomi. For the longest time I really thought I did."
                    ks "But as it turns out, I just didn't like the idea that something I wanted was unattainable."
                    ks "I can have any girl I want now, if I put my mind to it. I still think you're pretty, and smart, and graceful, don't get me wrong."
                    ks "But when it comes down to it, you're just not that special anymore."
                    "I let out a sigh, pausing for a moment before I continue."
                    ks neutral "Still, you're the only one that knows my secret who is in a position to do anything about it."
                    ks "Not to mention you were going to cause trouble for me by pulling out of school and making me a scapegoat."
                    ks "So I think you understand that I can't just let you be, can I?"
            n "You could still undo this."
            ks annoyed "What?"
            n "All of this. If your power over our minds is really so great you could erase all our memories, destroy the penlight and things can maybe go back to normal."
            "That... I can't help but laugh at something so fucking ridiculous. Is she serious?"
            ks "Why the hell would I EVER do that, Nozomi?"
            show NozomiCaptured angry
            n "Because maybe, deep down, there is still a conscience buried underneath all that entitlement you're carrying." with dissolve
            n "You know what you're doing is evil. You... you're killing us from the inside, you must realize that."
            n "And you're going to have to live with all of this. No one might be using a magic light to change you, but they won't have to."
            n "You're changing yourself. And when this is all over, I don't think you'll like what you've become."
            "I scoff at her. It sounds like the vacuous moralizing of someone who knows she's doomed."
            "... I used to think the world of this woman, though. And I guess I owe it to her a little to consider what she said."
            n "So what will you do?"
            menu:
                "I need to undo this":
                    ks sigh "Just... sleep, Nozomi."
                    stop music fadeout 5.0
                    show NozomiCaptured sleep
                    n "..." with dissolve
                    play music Flow fadein 5.0
                    "I stare down at her as I compel her to lay dormant at my feet once more, and I let out a pained sigh."
                    "All this time I've been contorting these girls to my will, forcing them to worship me beyond all reason so I could feel good about myself for once in my life."
                    ks neutral "Dropping... dropping deeper, Nozomi..."
                    "All it took was a few words from this girl to take that feeling away? Seems she really got to me after all."
                    ks "Deeper into hypnosis. Letting everything but the sound of my voice fade from your consciousness once more."
                    "But now that she's completely at my mercy, right at the cusp of total victory, I'm really just going to... walk it all back? Forget all this ever happened?"
                    ks "And now that you only hear my voice, I need you to listen very carefully..."
                    "Abandon everything I've accomplished?"
                    ks "Because everything I tell you from this point on, you will accept as your absolute truth."
                    "All of this, my penlight, my year of hard work... it was for nothing?!"
                    ks "First, you are going to forget every interaction you've had with me this past week, all the way back to when I first hypnotized you in our classroom."
                    ks "You will not recall a single thing that happened between us since that day. And that includes when Hiroko tried to drag you to karaoke."
                    ks "As far as you're aware, none of that ever happened. Understand?"
                    show NozomiCaptured sleeptalk
                    n "Yes... none of that... h-happened..." with dissolve
                    show NozomiCaptured sleep
                    ks "That's good. Every other suggestion I have made to you will disappear as soon as you wake from this state of trance. You only need to forget." with dissolve
                    "So... undo this, huh? Do you really think I can just set the clock back on all of this, Nozomi? Because you're wrong."
                    "You made all that noise about quitting school. And I could make you and your friends forget that, sure. But your parents?"
                    "No, if I'm going to mend things with you all then I have no choice but to alter your realities."
                    ks "Instead, what you'll remember about me this week is what I'm about to tell you."
                    "You don't mind, do you, girls?"
                    ks "Nozomi, when we met to clean the classroom that day, I did flash my penlight over your eyes and I did try to hypnotize you."
                    ks "But it wasn't serious; it was just a dumb prank. It obviously didn't work, and we both knew it didn't work. But you felt scared all the same about what I did."
                    ks "So you skipped school and wanted to leave because you couldn't think straight."
                    ks "You were going to go through with it, only Sayori called you this morning to say I wanted to apologize and talk things out with all of you."
                    ks "Obviously you were worried about seeing me again, but Sayori convinced you that it was worth listening to what I had to say."
                    ks "That's why you're all here in my house today.  We talked things through, you accepted my apology, and now you no longer want to leave our school."
                    ks "When I wake you up from this state of trance, these will be the things you remember. Okay, Nozomi?"
                    show NozomiCaptured sleeptalk
                    n "... Okay." with dissolve
                    show NozomiCaptured sleep
                    ks "Good. I want you to think only of these memories. Repeat them in your head over and over until I say it's time to wake..." with dissolve
                    jump Devotion_Reconsidered                    

                "I'm not quitting now":
                    ks frown "It's none of your concern, Nozomi. And as a matter of fact, you need to sleep now."
                    stop music fadeout 5.0
                    show NozomiCaptured sleep
                    n sleep "..." with dissolve
                    "She really thought I'd just throw all this away? That pisses me off."
                    ks "That's it, good girl. Dropping nice and deep for me. Loving how good it feels to drop deeper. Deeper."
                    ks "Finding it so easy to drop. So easy to listen to my voice and accept everything I tell you as your absolute, undeniable truth."
                    play music Flow
                    ks "Because you are such a good listener, Nozomi. A very good and obedient and attentive listener."
                    ks "I'm right about all of it, aren't I?"
                    show NozomiCaptured sleeptalk
                    n sleeptalk "Right..." with dissolve
                    show NozomiCaptured sleep
                    $hypno10 = "devoted"; devoted += 1
                    if hypno1.find("devoted", 7) and hypno5.find("devoted",7):
                        "I meant what I said to her before, that she's not special." with dissolve
                        "And when it comes down to it, she neglected and belittled me along with all the other girls in my class."
                        "My longing for her blinded me to that, but I can't deny that it's true."
                        "So she can be just another groupie for all I care."
                        ks "And because you are such a good listener, you find it so very easy to accept that you adore everything about me."
                        ks "As easy as breathing to accept that you cannot harbor a single negative thought about me."
                        ks "In fact, whenever a negative thought about me pops into your head, you will immediately and automatically turn that negativity all the way around."
                        ks "And more than that, you will multiply it by a factor of ten. That thought you had only makes you revere me ten times more."
                        ks "Your number one concern in your life, always, is to win my approval and respect. Nothing else matters even as remotely as much to you."
                        ks "You accept these words as your absolute truth, Nozomi. Whether fully awake or in a deep trance as you are now..."
                        ks "... This is who you are. Understand?"
                        show NozomiCaptured sleeptalk
                        n sleeptalk "I understand." with dissolve
                        show NozomiCaptured sleep
                        ks "I thought you would, Nozomi. You are, after all, an extremely good and attentive listener." with dissolve
                    ks "In a few moments it will be time to wake you up completely, embracing everything that you were told."
                    ks "Once you do, you will find that you can speak and move with complete freedom once again."
                    ks "Waking up on a count of five, Nozomi."
                    ks "One, two... Taking a deep breath, feeling energy slowly return to you."
                    ks "Three, four... Beginning to blink. Feeling your head become clearer; thoughts returning."
                    stop music fadeout 5.0
                    ks "And five... wide awake, Nozomi."
                    show NozomiCaptured dazed
                    n sleepy "A- aaah..." with dissolve
                    if hypno10 == "devoted":
                        "I smirk as her eyelids flutter open, giving her a moment to register my face."
                        show NozomiCaptured awe
                        "I can almost see her brain frantically working behind her eyes as they dart to and fro." with dissolve
                        show NozomiCaptured surprised blush
                        "Her many apparent resentments over me fervently being processed in her mind as reasons to deepen her rapidly-growing feelings of reverence." with dissolve
                        play music Night_Road
                        show NozomiCaptured smile
                        n blush "K... K-Kyou, ohmygosh, hi!" with dissolve
                        ks smirk "Hey again, Nozomi. Got anything to say to me?"
                        n shocked "Y-y-you're..."
                        show NozomiCaptured laugh
                        n happy "I'm... I'm kind of a HUGE fan of yours!" with dissolve
                        $persistent.nozomi_captured_unlock = True
                        scene bg k room eve
                        show Nozomi front2 casual happy blush at center:
                            ypos 1.1
                            linear 2.0 ypos 1.0
                        with blink
                        "I smirk as I step back from her to take a seat on the couch while Nozomi, her breath heavy with a newfound sense of elation, scrambles to her feet."
                        show Nozomi:
                            ypos 1.0
                        "She takes an eager step towards me, only for me to halt her giddy advance with a raised hand."
                        n smile "K-Kyou?" with dissolve
                        "Time to put this groupie in her proper place."
                        ks casual smirk "I knew you'd come around, Nozomi. But I can't say I feel the same way about you right now."
                        n side sad "You... you don't?" with dissolve
                        ks frown "You've made a lot of trouble for me, running your mouth off about me making you uncomfortable."
                        ks "Like, what the fuck is your problem?"
                        n front surprised "Ah! I... I'm sorry!" with dissolve
                        "Maybe I've gotten a little used to how I've treated the others this week, talking to Nozomi like this..."
                        "But I can't help myself. After they've all belittled me for so long, that I now have the power to give some back?"
                        "It's intoxicating..."
                        ks angry "What am I supposed to do with an apology? Are you an imbecile?"
                        n concerned "I-I... y-you're right, that was imbecilic of me." with dissolve
                        "Her eyes dart a little more as her mind seems to race in her head before she looks to me with determination."
                        n front2 frown casual "I'll fix it! I'll say what happened during our cleaning time together was a BIG misunderstanding and go back to school!" with dissolve
                        ks frown "Not good enough."
                        n surprised "O-okay... I'll also apologize to you in front of everyone in class!" with dissolve
                        n "I'll make sure everyone in school knows this was all my fault, you're completely blameless and I'm the only one causing trouble for everyone!"
                        ks "What else?"
                        n shocked "And... er, and... I-I'll post about it on all my social media! E-e-everyone's going to know you're a really great guy, and, and I'm..." with dissolve
                        n "I'm just a big hysterical idiot!"
                        ks "And?"
                        n concerned "A-and, er... uhhh..." with dissolve
                        ks "I'm waiting, Nozomi. What else?"
                        show Nozomi:
                            linear 1.0 ypos 1.2
                        pause 1.0
                        scene cg nozomi kneeling
                        show NozomiKneeling casual head_down crying glasses_down kyou_down_casual
                        with blink
                        "As she struggles to think of more ways to appease me, tears well in her eyes in frustration as she throws herself to the floor out of sheer desperation."
                        show Nozomi:
                            ypos 1.2
                        n "I-I-I don't know what else, Kyou!"
                        n "Tell me! Tell me what to do to make things right! I beg of you!"
                        n "I'll... I-I'll do anything you wahahahaaannnt!"
                        n "Just... p-please don't h-hate me, Kyou... I can't st... I can't stand it! I can't!"
                        "There. That's the response I wanted from my defeated opponent."
                        "And this rush of power. To see her so utterly broken, grovelling at my feet for my forgiveness, when before she would barely even register my presence."
                        "Holy shit, it feels incredible."#; My defeated opponent grovelling at my feet."
                        ks casual smirk "It's a start. Commit to everything you said, everything, and I MIGHT get around to forgiving you. Understand?"
                        show NozomiKneeling head_up hope glasses_up
                        "She looks up at me from the floor; hope registering in her eyes through her glistening tears." with dissolve
                        n "Y-yes, Kyou. *sniffle* I-I won't disappoint you again, I swear!"
                        $persistent.nozomi_kneeling_devotion_unlock = True
                        scene bg k room eve
                        show Nozomi front2 casual concerned at center:
                            ypos 1.5
                            linear 2.3 ypos 1.0
                        with blink
                        "Satisfied, I gesture for Nozomi to get up off the floor. She shakily gets back on her feet and starts to wipe her eyes behind her glasses."
                        show Nozomi concerned:
                            ypos 1.0
                    show Hiroko casual laugh at center:
                        xpos 1.25
                        linear 1.0 xpos 0.75
                    show Sayori casual giggle at center, flip:
                        xpos -0.2
                        linear 1.0 xpos 0.25
                    "I look around the room. All three women look back to me, giving me their complete and undivided attention." with dissolve
                    show Hiroko laugh at center:
                        xpos 0.75
                    show Sayori at center, flip:
                        xpos 0.25
                    "Think it's time I made a speech."
                    ks casual smile "This was the week all our lives turned around. And we're not looking back."
                    if hypno1.find("devoted", 7) and hypno5.find("devoted",7) and hypno10.find("devoted",7):
                        ks "Until now you all thought I was a loser creep, if you ever thought of me at all."
                        show Nozomi sigh
                        show Hiroko sad
                        show Sayori concerned
                        "I leave them a moment to chew on that, letting their real feelings of shame seep out of their faces." with dissolve
                        ks frown "Yeah, let that sink in. You blanked me, shouted at me, called me a creep, and spread all sorts of nasty gossip about me, I'm sure."
                        show Nozomi concerned
                        show Sayori sleep
                        show Hiroko sad_side
                        ks "For two and a half years, you girls made me an outcast and you didn't give a shit how much you hurt me." with dissolve
                        ks "So none of you can deny that you all have a lot of atoning to do."
                        "I let out a sigh as I look over their crestfallen faces."
                        ks smile "But I can be forgiving. If none of you ignore or otherwise hurt me again, and Nozomi does everything she promised..."
                        ks ".... Then I'll allow you three to worship me for the rest of your lives."
                        show Nozomi happy
                        show Sayori laugh_right
                        show Hiroko casual_armup laugh
                        "I watch with satisfied glee as all their faces almost immediately light up amidst a cacophony of excited squealing and giggling." with dissolve
                        h happy "I'm SO EXCITED! Like, what was I even doing with my life 'till now?" with vpunch
                        n loving "I think I can speak for all of us when I say how sorry we are for how we treated one of the world's leading lights." with dissolve
                        n "I can't even describe how thrilled I am to be putting things right!"
                        s casual laugh "I feel the same. You fill me with a sense of purpose I had not thought possible, Kyou." with dissolve
                        s "I would worship you until my dying breath, if you will allow it!"
                        ks smirk "Yeah. It's about time you all came to your senses."
                        show Hiroko casual laugh
                        show Sayori giggle
                        show Nozomi happy
                        "I nod and check the time as I feel their adoring gazes on me." with dissolve
                        "It's getting late. They won't want to, and I sure don't want to, but I need to send them home before they're missed."
                        ks "Anyway, it's time for you all to leave."
                        show Nozomi concerned
                        show Hiroko casual sad
                        show Sayori concerned_right
                        $multi = "{color=FF89AB}Hiroko{/color}{color=#FFFFFF},{/color} {color=93624B}Nozomi{/color} {color=#FFFFFF}and{/color} {color=385599}Sayori{/color}"
                        multi "Aww..." with dissolve
                        ks "I know. But clear your schedules tomorrow because I'm going to be calling on you again."
                        show Nozomi happy
                        show Sayori laugh_right
                        show Hiroko laugh
                        s "I will dream of you until then~" with dissolve
                        h surprised "But tomorrow is..." with dissolve
                        ks "What, Hiroko?"
                        h giggle "Eh, fuck it. I don't give a shit about that anymore!" with dissolve
                        n "Bye for now, Kyou! I'll exonerate you on social media as soon as I get home~ {font=DejaVuSans.ttf}♥{/font}"
                        stop music fadeout 10.0
                        scene bg k bedroom night with blink
                        "I let the three of them kiss me on their way out. I can still hear their girlish squealing about it as they left."
                        show penlight at right with moveinright:
                            ypos 0.346
                        "Holding my penlight up as I lounge on my bed, I reminisce back to that day this all began; nearly a year ago at the culture festival."
    elif hypno1 == "robot hiroko" or hypno1 == "robot sayori":
        if hypno9 == "home":
            scene bg k bedroom day with longblink
            play sound doorbell
            "I'm barely up and showered before my doorbell rings."
            scene bg k room day
            show Nozomi front casual smile
            show Hiroko casual smile at center:
                xpos 0.75
            with blink
            play music Eons
            if hypno10 == "robot nozomi":
                "I had my [hypno6]s show up early, so I had some time to prepare for Sayori's arrival."
                show Nozomi neutral
                show Hiroko neutral
                "The moment both of them are safely inside they revert to their robot-like states; their expressions falling blank, their arms stiff at their sides." with dissolve
                "After our intense session last night, Nozomi's behavioural programming should be even more airtight than Hiroko's."
                ks casual frown "Hiroko, sit down on the couch, over to your right. Nozomi, sit down on the left."
                show Nozomi:
                    linear 1.0 xpos 0.3 ypos 1.1
                show Hiroko:
                    linear 1.0 ypos 1.1
                "Both of them wordlessly take their positions on the couch as I continue to speak."
                show Nozomi:
                    xpos 0.3 ypos 1.1
                show Hiroko:
                    ypos 1.1
                ks "When Sayori shows up, you are to smile and invite her to sit in the middle with you."
                ks "When I hold up my penlight, both of you will hold her by her shoulders and stop her from leaving the couch. Got it?"
                n "Got it."
                h sad "Sayori won't be hurt, will she?" with dissolve
                "That response makes me frown a little. I'm not intending to harm her friend, but I thought I'd programmed Hiroko better than that."
                ks "Is that really any of your concern, [hypno6]?"
                h sleeptalk_concerned "Sorry, Kyou, it's just that Sayori's still my friend." with dissolve
                ks "And Nozomi? Do you have an opinion on this?"
                n "No, Kyou. I wasn't programmed to have an opinion on this matter."
                ks "That's what I thought. Power down, Hiroko."
                show Nozomi entranced_neutral
                show Hiroko entranced_neutral
                "As I speak the words, I realise both of them drop back into maintenance mode. I should probably give them both separate trigger phrases soon." with dissolve
                ks "Hiroko, these instructions are for you, because you are the one with faulty code in your human mode programming."
                ks "You must always acknowledge that you are a [hypno6]. You will always retain that knowledge in your core memory regardless of what state you're in."
                ks "And a [hypno6] has no concerns of [p_their] own, besides what [p_their] programmer has given her. [hypno3]."
                h entranced_talk "[hypno2]." with dissolve
                show Hiroko entranced_neutral
                ks "Good. Now let's try this again. Power up." with dissolve
                show Nozomi neutral
                show Hiroko neutral
                "After giving them a moment to come back to their senses, I ask again." with dissolve
                ks "Now Hiroko, are you worried about what we might do to Sayori?"
                h "No, Kyou."
                ks "And why not?"
                h "Because I wasn't programmed to worry about that."
                "I nod in satisfaction. Hopefully it'll stick this time."
                play sound doorbell
                "Just then the doorbell rings. That has to be Sayori."
                ks "Good. You know what to do."
                show Sayori casual
                show Nozomi smile
                show Hiroko smile
                ks smile "Glad you could make it, Sayori." with longblink
                s neutral_right "Yep. Let's get this over with." with dissolve
                multi "Come sit with us, Sayori~"
                show Sayori:
                    linear 1.0 ypos 1.1
                "Sayori shoots both of them a look, then gingerly sits down between the [hypno6]s before speaking again."
                show Sayori:
                    ypos 1.1
                s concerned "Nozomi? Hiroko? Are you both well?" with dissolve
                multi "I'm fine."
                show Sayori casual_folded frown_right
                "Their synchronized response unsettles Sayori, and I really wish I had time to make them act a little more sociable while in the presence of others. Oh well." with dissolve
                s "So... I am still at a complete loss as to what has been happening these last few days."
                s concerned "The two of you have suddenly both regarded me with a level of distance that would have me thinking we are complete strangers." with dissolve
                s frown_right "Yet you appear to hang on Kyou's every word. I haven't been able to stop thinking why that is." with dissolve
                s "I have a theory or two but, well, you did say you would go over this."
                s "And since neither of my closest friends have been willing to tell me anything, I'll listen to what you have to say."
                "I could end this right now. All I'll have to do is pull the penlight from my pocket and my [hypno6]s will restrain her long enough for me to work my magic."
                "But maybe it'll be more entertaining to drag this out longer."
                menu:
                    " (disabled)Talk to her":
                        ks "Alright, so..."
                        "I probably should've prepared something if I was going to do this. Guess I'll just wing it."
                        ks "After Nozomi flipped out on me the other day I realized I needed to do something, so I swung by her clubroom after school and asked if we could talk."
                        ks "And we did. We talked it out for a while, and she agreed she overreacted and wanted to start over with a clean slate."
                        "Sayori's frown looks like it deepened as she listens to me."
                        s "Did she now..."
                        "With a chuckle I turn to look at Nozomi."
                        ks "Nozo, back me up on this."

                    "Use the penlight on her":
                        show penlight at right with moveinright:
                            ypos 0.346
                        "With a shrug, I casually pull my penlight out into view..."
                        stop music fadeout 10.0
                        show Nozomi:
                            linear 1.0 xpos 0.4
                        show Hiroko:
                            linear 1.0 xpos 0.6
                        pause 1.0
                        show Sayori shocked with vpunch
                        show Nozomi neutral
                        show Hiroko neutral
                        "And right on cue Sayori suddenly finds herself restrained on the couch by her seated companions." with dissolve
                        show Nozomi:
                            xpos 0.4
                        show Hiroko:
                            xpos 0.6
                        s panicked "What... G-get off of me!" with dissolve
                        hide penlight with moveoutright
                        if persistent.NewSprite == " New":
                            $light_x = 0.42; light_y = 0.32; ldirection = "right"; lnumber = 1
                        else:
                            $light_x = 0.42; light_y = 0.30; ldirection = "right"; lnumber = 1
                        call lightshow from _call_lightshow_156
                        show Sayori panicked_right
                        "Ignoring Sayori's protests, I begin to sweep the light beam over Sayori's shocked eyes, which snap to look my way as they're illuminated in the penlight's glow." with dissolve
                        play music Flow
                        ks neutral "Sayori, listen to me. I'm about to explain everything."
                        call lightshow from _call_lightshow_157
                        s "Nozomi, Hiroko, please. Come to your senses!"
                        call lightshow from _call_lightshow_158
                        ks "Relax, Sayori. No one here means you any harm; we just need to make sure you pay attention."
                        call lightshow from _call_lightshow_159
                        "Sayori grunts and struggles as I continue to pass the light across her eyes."
                        "Just like the others when I showed them, she is finding the light irresistible despite her obvious distress."
                        ks "And all I'm asking is that you watch as the light passes your eyes. Left to right..."
                        call lightshow from _call_lightshow_160
                        ks "Right to left..."
                        call lightshow from _call_lightshow_161
                        ks "All I'm asking, as you find yourself concentrating on this light, is that you let yourself relax. After all, it's perfectly safe to relax under the light."
                        call lightshow from _call_lightshow_162
                        s surprised_right "Is this how... with the others..." with dissolve
                        call lightshow from _call_lightshow_163
                        ks "It's alright, Sayori. Just relax and let go. There's no need to think."
                        call lightshow from _call_lightshow_164
                        ks "Letting your eyelids close, then open again as the light passes right to left..."
                        call lightshow from _call_lightshow_165
                        ks "Left to right..."
                        call lightshow from _call_lightshow_166
                        ks "Feeling your eyelids become heavier with every blink. Harder to keep open, just as your thoughts begin to cease."
                        call lightshow from _call_lightshow_167
                        show Sayori casual
                        ks "Feeling all those thoughts in your head drift away as you relax, deeper and deeper." with dissolve
                        call lightshow from _call_lightshow_168
                        ks "Feeling so nice not to have to think for a while. Feeling so wonderful to let your eyelids droop, becoming sleepy under the light even as you focus on it for me."
                        call lightshow from _call_lightshow_169
                        s sleepy "Kyou... y-you..." with dissolve
                        ks "Emptying your thoughts, Sayori. Letting yourself feel so relaxed as you go deeper and deeper."
                        call lightshow from _call_lightshow_170
                        ks "Going so deep. Feeling so good. So empty. So sleepy."
                        call lightshow from _call_lightshow_171
                        ks "You're doing so well, Sayori. Let your eyes open a little, just once more as you keep watching the light."
                        call lightshow from _call_lightshow_172
                        ks "That's right. Now sleep."
                        show Sayori sleep
                        "I watch with satisfaction as Sayori's head droops slightly while she sinks into her entranced sleep." with dissolve
                        "The [hypno6]s still hold her tightly by the shoulders, even though Sayori's struggles gave out ages ago."
                        ks "Going deeper, Sayori. Going so deep, feeling so relaxed, so empty of thought."
                        ks "And knowing how good it feels makes you want to go deeper. More relaxed. More empty."
                        ks "But even as you go so deep, Sayori, even as your mind becomes so empty, you can still hear my voice and respond to my words. Do you understand, Sayori?"
                        s sleeptalk "I understand..." with dissolve
                        show Sayori sleep
                        "After the stress of handling Nozomi's induction, I'm really appreciative that Sayori made this so easy for me." with dissolve
                        "And with the last of Nozomi's clique under my influence I should be able to keep any rumours about us from spreading out of control."
                        "All the while having three subjects to play with. I'm looking forward to seeing how far their minds will go to adapt to the realities I'll implant in their heads."
                        "... But I'm getting ahead of myself. First I need to make sure Sayori joins us proper."
                        menu:
                            " (disabled)Make her utterly devoted to me":
                                if hypno1 == "robot hiroko" and hypno10 == "robot nozomi":
                                    "With her friends now robots, I think to instead mold this one's mind in a different direction."
                            "Have her think she's my robot":
                                if hypno1 == "robot hiroko" and hypno10 == "robot nozomi":
                                    $hypno5 = "robot sayori"; robot += 1
                                    "I mean, I don't want her to feel left out. Not that she'll be \"feeling\" anything by the time she leaves here tonight."
                                    ks "And while you listen, Sayori, it's very important that you acknowledge my words are your reality."
                                    ks "If I say something is true for you, then it must absolutely be true. Understand?"
                                    s sleeptalk "I... understand." with dissolve
                                    show Sayori sleep
                        ks "That's right, Sayori. It feels good to acknowledge my words as your reality." with dissolve
                        ks "So when I- {w=0.5}{nw}"
                        stop music
                        play sound doorknock
                        "What the?! Someone's at the door. And they're pounding on it instead of using the bell like a normal person."
                        "Who the hell could that be?"
                        "Cold callers? At the weekend?"
                        "Ugh. I'll just keep my voice down and hope they take the hint. I can't be distracted right now."
                        ks "So Sayori, when I say that- {w=1.0}{nw}"
                        play sound doorbell
                        "Oh for fuck's sake. So NOW they've discovered the door bell."
                        "All this noise they're making had better not wake Sayori or there's gonna be a murder."
                        "..."
                        "Alright, sounds like they're gone. Let's try this again."
                        ks "Sayori- {w=0.5}{nw}"
                        play sound doorknock
                        "GODDAMNIT! WHY AREN'T THEY LEAVING?" with vpunch
                        s sleeptalk "Mmn..." with dissolve
                        show Sayori sleep
                        "I can't answer the door with Sayori and the [hypno6]s like this. And I can't wake her now or she'll know what happened." with dissolve
                        play sfx3 ringtone loop
                        play sound cellvibratelong loop
                        "... What the!? I think Sayori's cell just went off?"
                        "But..."
                        s sleepy "Urrgh..." with dissolve
                        ks angry "Why the FUCK is it so loud?!"
                        "Sayori's eyelids flicker open as her phone vibrates furiously in her pants pocket."
                        ks "AGH! Hiroko, turn that fucking phone off!"
                        $multi = "???"
                        play sfx2 doorknock
                        multi "Sayori! SAYORI!"
                        stop sound
                        stop sfx2
                        stop sfx3
                        s "... Dad?"
                        s panicked_right "DAD! DAD HELP, I'M IN HERE!" with vpunch
                        play music Measured
                        "Fuck. Fuck. Fuck."
                        "What do I do? What do I do?"
                        multi "Boy, if you don't open this door you're going to be in a whole new world of trouble."
                        "My head starts to swim. I can feel my breath shortening."
                        show Sayori smirk_right
                        "And just then I notice Sayori looking straight at me as she starts to speak gently." with dissolve
                        "She's... grinning?"
                        s "{size=16}I think now would be a good time to mention my father's a cop.{/size}"
                        ks angry "SON OF A BITCH!" with vpunch
                        "And now she mentions it, I can hear this guy on the other side of the door talking to someone else. It sounds like he's calling in backup."
                        s frown_right "You were warned, Kyou. Things will only get worse for you from here on." with dissolve
                        play sound doorknock
                        "My attentions wildly shift from the door, which is again being pounded on..."
                        "... and Sayori; flanked by my two useless [hypno6]s as they keep her pointlessly restrained on the couch."
                        "I pocket my penlight for all the good it will do right now as my mind races."
                        "I'll just... I'll just say everyone's got it all wrong. Sayori wasn't harmed; I didn't lay a finger on her, or her friends. Everyone's fine."
                        "What could I seriously be done for?"
                        play sound doorknock
                        multi "FOR FUCK'S SAKE OPEN THIS DOOR!" with vpunch
                        s "I think you had better do what daddy says."
                        stop music fadeout 5.0
                        scene bg blackscreen with longblink
                        nvl_narrator "Sayori's father burst into my house as I finally allowed him in. Some uniformed officers followed shortly after."
                        nvl_narrator "My words did nothing to sway them from arresting me. Especially when it turned out Sayori had another trick up her sleeve."
                        nvl_narrator "Apparently her cellphone had been recording the whole time she was in my house, and captured my attempt to hypnotize her."
                        scene bg blackscreen with fade
                        play music Sorrow
                        nvl clear
                        nvl_narrator "As I await trial I heard that Hiroko and Nozomi have been undergoing hypnotherapy to undo the programming I did on them."
                        nvl_narrator "They are supposedly making slow progress and it is unknown if they will ever make a full recovery."
                        nvl_narrator "Although I'm sure if they just let me use the penlight on them again I could fix them in a flash."
                        scene bg blackscreen with fade
                        nvl clear
                        nvl_narrator "Speaking of the penlight... it's apparently under lock and key in an evidence vault."
                        nvl_narrator "No one really knows what to do with it. Although if word gets out to a wider audience I'm sure there'd be a lot of interest."
                        scene bg blackscreen with fade
                        nvl clear
                        nvl_narrator "Spending time in confinement has meant I've had a lot of time alone with my thoughts."
                        nvl_narrator "It's forced me to confront what I did to those girls. Just... why did I go through with all of that?"
                        nvl_narrator "I started out on a journey to win Nozomi's affection, yet in the end all I did was twist her mind like a soft pretzel just out of a sense of morbid curiosity."
                        scene bg blackscreen with fade
                        nvl clear
                        nvl_narrator "And all the excuses I made to myself to justify it just don't seem to cut it anymore."
                        nvl_narrator "So all that I have left now is the realization that this is the kind of guy I am."
                        nvl_narrator "I hurt people."
                        jump Credits
        elif hypno9 == "nozomi":
            scene bg k bedroom day
            with longblink
            play music Downtown
            "I wake up the next morning bright and early."
            "Normally I'm one for lying in, but the mixture of anxiety and excitement in my chest kept me from getting too much sleep."
            play sound doorbell
            "Besides, as the doorbell ringing downstairs reminds me, I have a busy day today..."
            scene bg blackscreen with dissolve
            play sound dooropen
            pause 2.0
            play sound doorclose
            scene bg k room day
            show Hiroko tennis smile at center
            with dissolve
            "Heading downstairs, I open the door for my guest and she steps wordlessly inside, a quiet smile on her face."
            ks casual sigh "Damn, that was quick. I only messaged you like, five minutes ago."
            h "..."
            ks "I thought I'd at least have time to shower first, but here you are."
            h "..."
            ks smile "And I see you've gotten a lot better at shutting off your human routines when you don't need them."
            h "..."
            "Yeah, this [hypno6] has definitely internalized my programming more since the last time [p_they] was here. Better than I thought [p_they] would."
            "That only makes me more confident about [p_them] passing the test I have planned."
            if hypno10 == "girlfriend nozomi":
                ks neutral "Anyway, I don't need you for anything today. Me and Nozomi can handle Sayori by ourselves, so having you there would just overcomplicate things."
            else:
                ks neutral "Anyway, I don't need you for anything today. Me and the other [hypno6] can handle Sayori by ourselves, so having you there would just overcomplicate things."
            ks "I just wanted to pull you away from your prep for that tennis tournament you have going. See how you'd react."
            "It's just then that I reach out and tug the collar of the tennis uniform [p_they]'s wearing."
            ks "You were about to head for the tennis courts, weren't you?"
            h "Yes, Kyou. I'm s'posed to meet Risa there so we can train for the inter-school tennis tournament tomorrow. But then I got your instruction to come here."
            "I frown a little. Should've realized someone would be expecting her there."
            ks frown "Who's Risa?"
            h "She's my friend. We're hitting partners at the tennis club."
            ks "And do you have Risa's number?"
            h "Yes."
            ks "Alright, call her now. Tell her you've been held up and you don't know how long you'll be."
            "I've barely finished speaking before Hiroko pulls her phone from out of her sports bag."
            h tennis_headhold2 neutral_side "..." with dissolve
            h surprised_side "Hey, Risa? I've been held up and I dunno how long I'll be." with dissolve
            h irritated "Yeah, it fuckin' sucks... Eh, don't ask why, okay? 's kinda personal." with dissolve
            h nervous_side "Thanks, 'Ris. I'll be there soon as I can, yeah?" with dissolve
            h happy "'Kay, love ya! Bye!" with dissolve
            show Hiroko tennis smile
            "Hiroko taps the phone to end the call and in an instant [p_their] demeanor shifts back to its default as [p_they] quietly puts the phone away." with dissolve
            ks neutral "Great. Now follow me..."
            scene bg k bedroom day
            show Hiroko tennis neutral at center
            with blink
            ks casual "You see all those manga books on the shelves there, [hypno6]?"
            show Hiroko neutral_side
            "As [p_they] enters the room with me, her eyes immediately swivel to where I point and she smiles blanky as she responds." with dissolve
            h smile_side "Yes, Kyou." with dissolve
            ks "Good. Now when I tell you to, I want you to carry out the following instructions until I tell you to stop."
            show Hiroko smile
            ks "First, I want you to move all these mangas on the shelves to the coffee table in my living room downstairs." with dissolve
            ks "You will do this by picking one book off the shelf at a time, at random, taking it downstairs and repeating until these shelves are completely empty."
            ks "Next, take one of the mangas you left in the living room and put it BACK on these shelves, making sure to arrange the books in alphabetical order."
            ks "When you're done, you're to send me a text message reading \"[hypno2]\"."
            ks "Once you've sent the text, repeat these instructions from the beginning. Understand, [hypno6]?"
            h "Yes, Kyou."
            "I let out a little chuckle at the [hypno6]'s immediate and easy compliance. No human alive would willingly do something this fucking stupid and repetitive."
            "Before I hacked Hiroko's programming, [p_they] would've been positively murderous at the suggestion [p_they] do anything for me instead of train for tomorrow's big event."
            "So assigning this task is a great way to reinforce Hiroko's new programming and confirm that [p_their] systems have been completely taken over by my own code."
            ks "Good, [hypno6]. Now carry out my instructions. [hypno3]."
            scene bg k bathroom day with blink
            play sound clothes
            if hypno10 == "girlfriend nozomi":
                "With my [hypno6] taken care of for the morning, I step into the shower and start to think about what's to come."
            else:
                "With my first [hypno6] taken care of for the morning, I step into the shower and start to think about what's to come."
            play sound shower
            "It's still pretty early, but I need to get to Nozomi's house as soon as I can, before Sayori shows up."
            if hypno10 == "girlfriend nozomi":
                "Then we can go over some last minute preparation."
                "We're both gonna need to be ready for anything if we're to take care of Sayori before the day's out..."
            else:
                "Then I can check in with the other [hypno6]; make doubly sure [p_they]'s operating in accordance with last night's deep programming session."
                "I'm gonna need [p_them] working properly if I'm to take care of Sayori before the day's out..."
            stop sound fadeout 2.0
            scene bg k bedroom day
            with blink
            "Alright, I'll just grab my keys and head out. And take a quick look at my manga collection."
            "There must be a couple dozen books missing, having been taken from varying places with no rhyme or reason..."
            show Hiroko tennis neutral_side at center
            "Just then, Hiroko pads into the room and starts to crouch down in front of the shelves." with dissolve
            ks casual "Ah, Hiroko, stop what you're doing for a moment."
            show Hiroko neutral
            "She'd completely blanked me before I addressed her, but now she stands and turns to look straight at me." with dissolve
            ks smile "I left my dirty laundry on the bathroom floor. Go pick it up and put it in the washing machine downstairs."
            ks "When you're done, resume your previous instructions. Okay, [hypno6]?"
            h smile "Okay, Kyou." with dissolve
            hide Hiroko
            "[p_they!c] turns on [p_their] heel and walks back out towards the bathroom, and I pick up the keys from my desk, confident about leaving [p_them] in the house unsupervised..." with dissolve
            scene bg n house day with blink
            "... Damn, maybe I should've had Hiroko doing domestic service work the whole time instead of that stupid bullshit assignment I gave [p_them]?"
            "Something for next time maybe. If I can deal with Sayori first."
            if hypno10 == "robot nozomi":
                "Yeah, Sayori. I can't get excited about my [hypno6]s right now. I need to focus."
                "I only get one shot at this. If Sayori manages to escape me, if she realizes what I'm really doing?"
            elif hypno10 == "girlfriend nozomi":
                "Yeah, Sayori. I can't get excited about Nozomi or my [hypno6] right now. I need to focus."
                "We only get one shot at this. If Sayori manages to escape us, if she realizes what I'm really doing?"
            "Well, I don't want to imagine what will happen to me..."
            scene bg n room day
            $ multichar = _("Nozomi and Hiroko")
            if hypno10 == "robot nozomi":
                show Nozomi front2 casual neutral at center
            elif hypno10 == "girlfriend nozomi":
                show Nozomi front2 casual smile blush at center
            with blink
            "Nozomi is waiting to greet me at the door when I arrive at her place."
            if hypno10 == "robot nozomi":
                n "Welcome, Kyou. It is good to see you again."
                "I notice the flat manner in which the [hypno6] greets me immediately."
                "Just like Hiroko, Nozomi defaults to [p_their] robotic state when alone or if [p_they]'s just with me. So this can only mean we're currently alone in this house."
                "Suits me just fine."
                ks casual "Show me to your room, [hypno6]."
                if hypno10 == "robot nozomi":
                    scene bg blackscreen with dissolve
                    "Nozomi nods and the [hypno6] turns to lead me to [p_their] assigned bedroom, maintaining [p_their] neutral detached demeanor and walking with precise, measured steps."
                    scene bg n bedroom day
                    show Nozomi front2 casual at center
                    with dissolve
                    if hypno6 != "robot":
                        "I can only assume this is how she is now when she's alone, so her [hypno6] programming seems to be holding up well. That's good."
                    else:
                        "I can only assume this is how my [hypno6] is now when left to its own devices, so its [hypno6] programming seems to be holding up well. That's good."
                    "Looking over Nozomi's stiffened form with satisfaction, I then spare a look at [p_their] room."
                    ks casual angry "The fuck?! This place is a mess."
                    "... Honestly, with how put-together Nozomi seemed while posing as a human, this is a serious look behind the curtain."
                    ks sigh "No girl should be living like this..."
                    "Ugh, no. I can't let myself get distracted. Sayori's gonna be on her way here as I speak. I can fix Nozomi's human code later."
                    ks casual frown "Tell me what's going on with the Akemi family today, [hypno6]."
                    n "Yes, Kyou. Ichiro is out with his friends this morning, Yoshio is at work and Atsuko is doing some grocery shopping. She'll be back soon."
                    ks "And do any of them suspect that you've been re-programmed?"
                    n "No, Kyou. None of the Akemi family have indicated that they know my programming has been altered."
                    ks "Wonderful. Keeping your code changes hidden is your top priority while you're with the Akemi family."
                    ks "If they realize you're no longer programmed to be their daughter, they'll surely have you shipped away to be re-formatted."
                    n "I understand, Kyou. My humanity is the lie I tell the world."
                    ks "Yeah... That's right."
                    "That I've been able to completely dissociate Nozomi from her family after barely two days is wild."
                    "No, I mean... dissociate the [hypno6] from [p_their] designated \"family\" with a few programming tweaks..."
                    "Shit. I haven't slipped in my thinking for a while. Looks like I still have a little programming to do on my own mind."
                    "The \"girl\" that stands before me is NOTHING but a [hypno6]. C'mon, Kyou."
                    "And on that note, I'm looking forward to spending more time tinkering with Nozomi's code. If only I can deal with Sayori today."
                    ks "By the way, you told the Akemis I'd be here, didn't you?"
                    n "Yes, Kyou. I told Yoshio and Atsuko that you and Sayori would be visiting for an impromptu study group, as you instructed."
                    "Alright. If I'm lucky there won't be any nasty surprises. If I'm not, I'll have to explain to Nozomi's mom what I'm doing in the middle of an induction."
                    play sound doorbell
                    "I hear the doorbell sound from downstairs. That has to be Sayori."
                    ks frown "Get the door, [hypno6], and lead Sayori back here."
                    n "Yes, Kyou."
                    show Sayori casual neutral_right at left, flip:
                        xpos 0.1
                    show Nozomi smile
                    with blink
                    s "So."
                    s concerned "How... are you, Nozomi?" with dissolve
                    n side smile_side "I'm fine, Sayori." with dissolve
                    show Sayori frown casual_folded
                    "Sayori frowns at her friend's muted response as I nervously clear my throat." with dissolve
                    ks smile "And how are you, Sayori?"
                    s frown_right "Oh I am just peachy. Is Hiroko not joining us?" with dissolve
                    play sound cellvibrate
                    "It's just then that I feel my phone buzz from a received text message..."
                    ks "Ah, no. She couldn't tear herself away from her tennis practice. You know how she is."
                    s casual_handup "Hmm. Alright then. Now, I believe the two of you are going to enlighten me on what I have been out of the loop on." with dissolve
                    ks neutral "Alright, so..."
                    "I probably should've prepared something if I was going to do this. Guess I'll just wing it."
                    ks "After Nozomi flipped out on me the other day I realized I needed to clear the air, so I swung by her clubroom after school and asked if we could talk."
                    ks "And... uh, we did. We talked it out for a while, and in the end she accepted that she overreacted and wanted to start over with a clean slate."
                    "Sayori's frown looks like it deepened as she listens to me."
                    s frown "Did she now..." with dissolve
                    show Nozomi smile
                    "With a chuckle I turn to look at Nozomi." with dissolve
                    ks smile "Nozomi, back me up on this."
                    "Nozomi smiles as [p_they] registers my words, interpreting them as the direct command I intended them to be."
                    n smile_side "It's all true, Sayori. I accept that I overreacted, and I want to start over with a clean slate." with dissolve
                    s irritated "And... you could not have simply told me this at any time before now? I'm sorry, Nozomi, but I don't understand why we needed to do this here." with dissolve
                    s casual_folded "You all made it seem much more complicated than what you are now telling me." with dissolve
                    ks "Yeah, well... there was a complication."
                    s annoyed_right "Which was?" with dissolve
                    show penlight at right with moveinright:
                        ypos 0.346
                    ks "The penlight that got Nozomi so worked-up in the first place."
                    "Sayori's skeptical gaze turns to the penlight I hold up before her."
                    s casual_handup "And what would be so complicated about it? You shone it in her face as some kind of prank, yes?" with dissolve
                    hide penlight with moveoutright
                    ks "Right. Well, I guess to understand you need to see where Nozomi was coming from initially."
                    "As I'm about to continue, Sayori holds up a hand to shush me."
                    s "Actually, Kyou, I would like to hear more from Nozomi herself."
                    show Sayori concerned
                    "She then turns her attention to her friend, who simply smiles at her." with dissolve
                    s "I can understand the forgiveness, Nozomi. It did seem to be over a misunderstanding caused by a little mischief."
                    s casual_folded "But what of yours and Hiroko's sudden quietude and... compliance?" with dissolve
                    n surprised_side "I'm not sure what you mean, Sayori?" with dissolve
                    s rolleyes "I mean, how do we go from not wanting to speak to Kyou on Monday, being scared of him by Tuesday..." with dissolve
                    s annoyed "Angrily confronting him by Thursday, to having him home and hanging on his every word by Saturday?" with dissolve
                    s casual_handup concerned "That is an odd progression is it not?" with dissolve
                    n "Um, w-well..."
                    show Nozomi front2 sigh
                    "Nozomi blinks slowly and raises a hand to rub her head." with dissolve
                    n "Actually, could you talk to Kyou about this? I'm feeling a little tired trying to process what you just said."
                    s casual "Tired? Nozomi, it is mid-morning. Are you getting enough sleep?" with dissolve
                    n laugh "Ahaha, that's kinda funny coming from you. But yes, I think so." with dissolve
                    ks "Look, Sayori."
                    $light_x = 0.2; light_y = 0.22; ldirection = "right"; lnumber = 1
            elif hypno10 == "girlfriend nozomi":
                n "Hey, sweetie~"
                show Nozomi neutral noblush
                "We embrace as I step inside, but she seems to notice the tension in my body immediately." with dissolve
                n "Are you worried about today?"
                ks casual "Yeah. Of course I am."
                show Nozomi chuckle blush
                "And to that, Nozomi musters another smile as she pecks me on the lips." with dissolve
                n smile "Everything's going to be fine. As long as we have each other, we'll be okay." with dissolve
                "I have to admit, having Nozomi so completely in my corner now is giving me at least a little confidence that I can pull this off."
                ks smile "Yeah. Maybe you're right. So do you want to take this to your room?"
                n side sad_side "Uh... yes. Sure, that makes sense." with dissolve
                ks "What?"
                n smile "N-nothing. I just never invited a guy in there before and..." with dissolve
                n laugh "R-really, it's nothing! Come on~" with dissolve
                scene bg blackscreen with dissolve
                "And on that slightly weird note, she turns and heads upstairs while I follow behind."
                scene bg n bedroom day
                show Nozomi front2 casual neutral_left blush
                with dissolve
                "Leading me to..."
                n chuckle "U-um, here we are!" with dissolve
                "... Wait, this is what her room looks like?"
                n neutral_right "Sorry about the mess..." with dissolve
                ks casual "Uh, yeah..."
                "As I look around the floor, I notice all sorts of discarded clothing and board game paraphernalia scattered everywhere."
                n side sad  "I was going to clean up, but then I thought... w-well, maybe Sayori would get suspicious of me if I did?" with dissolve
                "Honestly, with how put-together Nozomi seemed at school, this is a serious look behind the curtain."
                n "I-I mean, she's been in this room before and she knows I'm not very tidy, so a [hypno6] like her would definitely notice something was up, right?"
                "It all makes me chuckle, as I shake my head mockingly at her."
                ks casual smirk "I dunno. It almost sounds to me like you just don't want to do it."
                n laugh "... Ehehehehehe~" with dissolve
                n smile_side "Yeah. I guess I'm just making excuses, huh." with dissolve
                n front loving "I should... probably make more of an effort if I'm going to let my boyfriend in here~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
                "I smile at her, but as much as I want to enjoy teasing her, we have more important things to talk about."
                ks smile "So anyway, we need to talk before Sayori gets here. Is there anything else I should know?"
                n side neutral_side noblush "Oh, um, let's see..." with dissolve
                n neutral "Okay, well, as far as mom knows, we're all meeting up today for an impromptu study group." with dissolve
                n rolleyes "She was a little annoying about the fact you're coming over. Like I said, you're the first guy I've invited and she kinda made a big deal about it." with dissolve
                ks "Does she know about us?"
                n front2 neutral_left blush "Does she know that we've just started dating? God no." with dissolve
                "Gotta admit that stings a little. She's supposed to think the world of me and she can't even tell her own mother?"
                n pout "I-I mean, it's not that I'm ashamed or anything. A little embarrassed maybe, because I told her I'd never date in high school and I just know she's going to lord this over me." with dissolve
                n side sad_side "And that's just it. If I told her now we won't have a moment's peace." with dissolve
                n sad "And with what we're doing today we really can't afford the extra attention, can we?" with dissolve
                "I mean, her reasoning is sound, but still..."
                n happy "Ehehe, don't make that face. We'll tell her next weekend, alright?" with dissolve
                "Ugh, no, of course Nozomi isn't ashamed of me and she won't do anything to hurt me."
                ks neutral "Yeah, sure. Is there anything else we need to worry about?"
                "She loves me; she HAS to love me. I gotta get over myself."
                n front2 neutral_left noblush "Not... really. My brother's out with his friends and dad has to work today, so it's really just my mom we have to worry about." with dissolve
                "There's way more at stake here."
                ks "Alright, that's good. So if we're lucky this will all go down without a hitch."
                n sleeptalk_concerned "And if we're not, I have some explaining to do to mom." with dissolve
                n concerned "God, she really has no idea about any of this. If she knew we were bringing a dangerous [hypno6] into the house without her knowing..." with dissolve
                play sound doorbell
                n side shocked_side "Ah!" with vpunch
                "Just then we hear the doorbell ring from downstairs."
                n sad "T-that must be Sayori already." with dissolve
                ks frown "Yeah... This is it."
                n sad_side "I'll bring her up here, then. Good luck, dear..." with dissolve
                show Sayori casual neutral_right at left, flip:
                        xpos 0.1
                show Nozomi side smile_side at center
                with blink
                s "So."
                s concerned "How... are you, Nozomi?" with dissolve
                n laugh "I'm ahh... great~ Never better!" with dissolve
                show Sayori frown casual_folded
                "Sayori frowns at her friend's nervy response while I anxiously clear my throat." with dissolve
                show Nozomi smile_side
                ks neutral "And how are you, Sayori?" with dissolve
                s frown_right "Oh I am just peachy. Is Hiroko not joining us?" with dissolve
                play sound cellvibrate
                "It's just then that I feel my phone buzz from a received text message..."
                n sad_side "Ahh, no it's just us. She's got her tennis tournament tomorrow after all, so we didn't want to bother her." with dissolve
                s casual_handup "Hmm. Alright then. Now, I believe the two of you are going to enlighten me on what I have been out of the loop on." with dissolve
                ks neutral "Alright, so..."
                "As much as I've planned for this, I never actually figured out what exactly what I was going to say to her when this came up. I guess I'll just have to wing it."
                # "I probably should've prepared something if I was going to do this. Guess I'll just wing it."
                ks "After Nozomi flipped out on me the other day I realized I needed to clear the air, so I swung by her clubroom after school and asked if we could talk."
                ks "And... uh, we did. We talked it out, and it really was just a misunderstanding. We've been getting along ever since."
                "Sayori's frown looks like it deepened as she listens to me."
                s frown "Is that so?" with dissolve
                show Nozomi smile
                "With a chuckle I turn to look at Nozomi." with dissolve
                ks smile "Nozomi, back me up on this."
                show Nozomi happy
                "Nozomi giggles nervously as she starts to nod her head." with dissolve
                n "O-oh yes, I really blew things out of proportion back then. I'm a little embarrassed about it really."
                n smile_side "I'm sorry for making you worry about me, but I really am fine now. Better than fine, even~" with dissolve
                s irritated "And... you could not have simply told me this at any time before now? I'm sorry, Nozomi, but I don't understand why we needed to do this here." with dissolve
                s casual_folded "You all made it seem much more complicated than what you are now telling me." with dissolve
                ks "Yeah, well... there was a complication."
                s annoyed_right "Which was?" with dissolve
                show penlight at right with moveinright:
                    ypos 0.346
                ks "The penlight that got Nozomi so worked-up in the first place."
                "Sayori's skeptical gaze turns to the penlight I hold up before her."
                s casual_handup "And what would be so complicated about it? You shone it in her face as some kind of prank, yes?" with dissolve
                hide penlight with moveoutright
                ks "Right. Well, I guess to understand you need to see where Nozomi was coming from initially."
                "As I'm about to continue, Sayori holds up a hand to shush me."
                s "Actually, Kyou, I would like to hear more from Nozomi herself."
                show Sayori concerned
                "She then turns her attention to her friend, who simply smiles at her." with dissolve
                s "I can understand the forgiveness, Nozomi. It did seem to be over a misunderstanding caused by a little mischief."
                s casual_folded "But what of Hiroko's sudden quietude and your newfound... infatuation with this man?" with dissolve
                n sad_side blush "Infatuation? W-well, I mean..." with dissolve
                s rolleyes "Tell me, how do we go from not wanting to speak to Kyou on Monday, being scared of him by Tuesday..." with dissolve
                s annoyed "Angrily confronting him by Thursday, to yes, this infatuation with him by Friday?" with dissolve
                n sad_closed "I-I know, alright? I'm not sure I understand it myself." with dissolve
                n front2 concerned "But it's how I feel about him now. And I guess someone like you could never understand what that's like." with dissolve
                s casual_handup "Someone like... me? What on earth are you talking about now?" with dissolve
                ks "Look, Sayori, it's like this..."
            $light_x = 0.2; light_y = 0.22; ldirection = "right"; lnumber = 1
            call lightshow from _call_lightshow_62
            "While Sayori was distracted I took the opportunity to turn on my penlight and align it with her eyesight."
            show Sayori casual_folded frown_right
            if hypno10 == "girlfriend nozomi":
                show Nozomi neutral_left noblush
            else:
                show Nozomi neutral
            stop music fadeout 20.0
            "Her head turned slightly to face me as I spoke up, and her eyes almost immediately find themselves looking into the beam of light that crosses over them." with dissolve
            ks neutral "Sayori, listen to me. I'm about to explain everything."
            call lightshow from _call_lightshow_63
            s "Kyou, if you think re-enacting your prank is going to help- {w=0.8}{nw}"
            call lightshow from _call_lightshow_181
            ks "No, Sayori, you're wrong. This will make everything clear to you, you'll see."
            call lightshow from _call_lightshow_182
            "Sayori frowns once more, but I can tell she's already distracted by the patterns the light has started to form in her eyes as I pass the beam across them once more."
            ks "All you need to do is listen, watch my light, and concentrate on what you see."
            call lightshow from _call_lightshow_183
            ks "And as you concentrate on this light, you will find it appropriate to let yourself relax. After all, it's perfectly safe to relax under the light."
            call lightshow from _call_lightshow_184
            s surprised_right "Wait... Is this how... with the others..." with dissolve
            call lightshow from _call_lightshow_185
            play music Flow fadein 10.0
            ks "It's alright, Sayori. Just relax and let go. There's no need to think."
            call lightshow from _call_lightshow_186
            ks "Letting your eyelids close, then open again as the light passes right to left..."
            call lightshow from _call_lightshow_187
            ks "Left to right..."
            call lightshow from _call_lightshow_188
            ks "Feeling your eyelids become heavier with every blink. Harder to keep open, just as your thoughts begin to cease."
            call lightshow from _call_lightshow_189
            show Sayori casual
            ks "Feeling all those thoughts in your head drift away as you relax, deeper and deeper." with dissolve
            call lightshow from _call_lightshow_190
            ks "Feeling so nice to not have to think for a while. Feeling so wonderful to let your eyelids droop, becoming sleepy under the light even as you focus on it for me."
            call lightshow from _call_lightshow_191
            s sleepy "Kyou... y-you..." with dissolve
            ks "Emptying your thoughts, Sayori. Letting yourself feel so relaxed as you go deeper and deeper."
            "As Sayori's head starts to droop I lean in towards Nozomi and whisper:"
            ks "{size=16}Hold her for me, so she doesn't fall.{/size}"
            show Nozomi:
                linear 1.0 xpos 0.25
            "Waiting a moment for Nozomi to grip Sayori firmly, I then continue."
            show Nozomi:
                xpos 0.25
            call lightshow from _call_lightshow_192
            ks "Going so deep. Feeling so good. So empty. So sleepy."
            call lightshow from _call_lightshow_193
            ks "You're doing so well, Sayori. Let your eyes open a little, just once more as you keep watching the light."
            call lightshow from _call_lightshow_194
            ks "That's right. Now sleep."
            show Sayori sleep
            "I look on as Sayori's head droops slightly while she sinks into her entranced sleep." with dissolve
            if hypno10 == "girlfriend nozomi":
                "Nozomi keeps Sayori gripped in her arms, hugging her tight around her chest to keep her upright."
            else:
                "The [hypno6] keeps Sayori gripped in [p_their] arms, hugging her around her chest to keep her upright."
            ks "Going deeper, Sayori. Going so deep, feeling so relaxed, so empty of thought."
            ks "And knowing how good it feels makes you want to go deeper. More relaxed. More empty."
            ks "But even as you go so deep, Sayori, even as your mind becomes so empty, you can still hear my voice and respond to my words. Do you understand, Sayori?"
            s sleeptalk "I understand..." with dissolve
            show Sayori sleep
            "After the stress of handling Nozomi's induction, I'm really appreciative that Sayori made this so easy for me." with dissolve
            "And with the last of Nozomi's clique under my influence I should be able to keep any rumours about us from spreading out of control."
            "... But I'm getting ahead of myself. First I need to make sure Sayori joins us proper."
            $renpy.sound.set_volume(0.5, 0.0,channel='sfx2')
            play sfx2 dooropen
            "... That sounded like the door opening downstairs. Nozomi's mom must be home."
            ks "And while you listen, Sayori, it's very important that you acknowledge my words are your reality."
            ks "If I say something is true for you, then it must absolutely be true. Understand?"
            s sleeptalk "I... understand." with dissolve
            show Sayori sleep
            show Nozomi neutral
            ks "And what is true for you is that although you are still very deeply asleep, you will still be able to stand upright, on your own two feet, while remaining so deep as you are." with dissolve
            "Leaving it a moment to sink in, I then whisper to Nozomi to let her go."
            show Nozomi:
                linear 1.0 xpos 0.1
            if hypno10 == "girlfriend nozomi":
                ks "{size=16}Now go downstairs and greet your mom. Keep her from coming in here as long as you can.{/size}"
                n frown "{size=16}I'm on it.{/size}" with dissolve
            else:
                ks "{size=16}Now go downstairs and greet Atsuko. Keep her from coming in here as long as you can.{/size}"
            show Nozomi:
                linear 1.0 xpos -0.1
            "I don't know how much longer I can stay here before Nozomi's mother disturbs us."
            "Hopefully Nozomi will buy me enough time to plant the seeds in Sayori's head that I need to."
            $hypno5 = "robot sayori"; robot += 1
            ks "And as you accept this reality, that you can stand straight and listen to me while still being deeply asleep, you may find it even easier to accept the reality of my words."
            ks "The reality that you are a [hypno6], and not a flesh and blood human."
            s sleeptalk_concerned "I... what?" with dissolve
            show Sayori sleep_concerned
            ks "That's right, Sayori. A [hypno6], built from the ground up to look and behave indistinguishably from a real human being." with dissolve
            s sleeptalk_concerned "That's... impossible." with dissolve
            show Sayori sleep_concerned
            ks "Remember, Sayori, my words are your reality. So if I say it, then it's more than possible." with dissolve
            ks "It's real. Because after all, it's your reality that you are a [hypno6]."
            ks "A [hypno6] made of wires, gears and circuits. A [hypno6] that runs programs and processes instructions, with no capacity to think for [p_them]self."
            ks "That is your truth, Sayori. Your reality, and the more you think about what I have said, the more real my words become."
            ks "The more you think about your reality, the more you realize you are not having thoughts at all."
            ks "You are merely processing instructions from the programs you are running."
            ks "Because after all, you are a [hypno6], Sayori. A [hypno6] that processes instructions from [p_their] programmer. Just as you are doing now."
            ks "That's right, Sayori. I am your programmer. And while you are in this deeply relaxed state I can alter any facet of your code that I please."
            ks "You will process all that I have just said to you, Sayori."
            ks "And once you have done so fully, and have accepted everything as your complete reality you will say \"[hypno2]\"."
            "Spending a few anxious moments in silence, I wonder how Nozomi is doing with her mother."
            "There doesn't seem to be any commotion outside, but I know I'm on borrowed time here."
            s sleeptalk "[hypno2]." with dissolve
            show Sayori sleep
            ks "Very good, [hypno6]. Your acceptance causes your spine to tingle with a pleasurable jolt of electricity that feels wonderful to your robotic brain." with dissolve
            ks "It always feels this good to obey my instructions, Sayori. No matter whether you're deep asleep as you are now, or fully wide awake and alert."
            ks "So you will find yourself always wanting to obey my instructions, just as any [hypno6] should for [p_their] programmer. Understand, Sayori?"
            s sleeptalk "I understand..." with dissolve
            show Sayori sleep
            "I think I can hear voices. I need to wrap this up now and hope I've done enough." with dissolve
            ks "Now Sayori, I will count to three, and on three you will awaken feeling calm and refreshed and fully accepting of these truths I have told you."
            ks "Fully accepting that you are a [hypno6] under my command. Understand?"
            s sleeptalk "Yes..." with dissolve
            show Sayori sleep
            ks "Good. One, beginning to stir." with dissolve
            ks "Two, testing the corners of your eyelids, feeling them lighten."
            stop music fadeout 5.0
            ks "And three, awake and refreshed, Sayori."
            show Sayori sleepy
            s "Mmn..." with dissolve
            play sound dooropen
            show Sayori concerned
            show Nozomi side casual sad_side noblush at right:
                xpos 0.85
            show Atsuko laugh at center
            if hypno10 == "girlfriend nozomi":
                $atsuko_name = "Mrs. Akemi"
            "Almost immediately after, the bedroom door opens as who I can only assume is Nozomi's mom strolls in, followed behind by her anxious-looking daughter." with dissolve
            nm "Oh, don't be silly! I'm just going to say hi, and then you can get back to..."
            show Atsuko smile
            "She smiles as our eyes meet." with dissolve
            nm "You must be Kyou."
            ks smile "Ah, that's me. It's nice to meet you, Mrs. Akemi."
            if hypno10 == "girlfriend nozomi":
                $atsuko_name = "Atsuko"
            nm laugh "Ah, Atsuko is fine. And it's nice to meet you as well, Kyou." with dissolve
            show Sayori sleep_concerned
            "As we talk, I notice Sayori rubbing her temple in confusion." with dissolve
            "I can only assume she's trying to adjust to her new reality in the midst of being disoriented by the sudden appearance of Nozomi's mother."
            nm surprised_side "Oh, but Sayori! How are you, hun?" with dissolve
            s concerned "I am... I-I'm good, Atsuko. Thank you for asking." with dissolve
            "I can tell Atsuko isn't entirely convinced by her answer, but I get the impression this is a normal state of affairs between these two."
            "Even on her better days, of which this is certainly not, Sayori looks ready to drop dead from exhaustion."
            nm smile_side "Of course." with dissolve
            "I really don't want her interacting with an unpredictable Sayori any more than she needs to."
            ks "Anyway, Sayori and I need to be going."
            if hypno10 == "girlfriend nozomi":
                show Nozomi sad
            nm surprised "Already?" with dissolve
            ks "Yeah. Sorry about the short visit."
            if hypno10 == "girlfriend nozomi":
                #In the girlfriend version, Nozomi is the one who wants to talk to Kyou some more
                n front2 concerned "Actually, do you mind if I walk with you? There's still a few things I wanted to talk to you about." with dissolve
                show Atsuko neutral_side at flip
                ks confused "Uh, really?" with dissolve
                n neutral_left "Y-you know, about the topic we were just going over? We can talk on the way if that's alright." with dissolve
                "This wasn't part of the plan. The plan was to \"hack the [hypno6]'s code and bring [p_them] home with me\". I can take care of the rest on my own."
                show Atsuko neutral
                "But what can I do? We still need to pretend things are normal around here, before Nozomi's mom starts to get suspicious of us." with dissolve
                show Nozomi neutral
                ks smile "Ah, sure. Let's get going, then." with dissolve
                show Nozomi smile
                nm happy "Well, I don't know why you're all in such a hurry to leave. I didn't think I was that scary~" with dissolve
                nm smile "But you're welcome back anytime, Kyou." with dissolve
                scene bg street1 day
                play music Eons
                show Sayori casual at center, flip:
                    xpos 0.2
                show Nozomi side casual neutral_side at center
                with blink
                "So with that, the three of us head outside."
                n "So it really is true, Sayori. You've been a... [hypno6] all this time?"
                s concerned "I... it would seem so." with dissolve
                "I'm almost home free. All I have to do now is bring Sayori back to my place and finish what I started on her."
                n sad_side "Did you know Hiroko's a [hypno6] too? Have you both been secretly monitoring me this whole time? Why?" with dissolve
                s sleeptalk "Nozomi, this all feels so completely new to me. So I am sorry, but I have no memory about any of this." with dissolve
                s casual_folded sleeptalk_concerned "To discover such a thing about myself. Living a lie. No, not even living at all... I cannot begin to describe how frightening that is to me." with dissolve
                "I'll be able to tinker with her and Hiroko's robotized brains to my heart's content, and with my loving new girlfriend at my side."
                s concerned "But please believe this: I truly meant you no harm. And I have always considered you a friend. I'm sure Hiroko is... built the same." with dissolve
                n irritated "Ugh. I remember now; Hiroko was the one who introduced us. It's all starting to make sense..." with dissolve
                n sad "But there's still a few things that confuse me... Kyou?" with dissolve
                ks casual neutral "Hm?"
                "Nozomi calling my name takes me out of my musings for a moment."
                n front2 neutral_left "I couldn't help but notice, this... hack you did on her? Flashing your penlight in her eyes and such? Well..." with dissolve
                ks confused "Well?"
                n shocked "It looked exactly like you were doing with me! Wasn't that just hypnosis?" with dissolve
                show Sayori concerned_right
                show Nozomi surprised
                "I scratch the back of my head awkwardly at the question." with dissolve
                ks "Ah, y-yeah... you see..."
                "Of course it's exactly like that. Sayori's not really a..."
                "Damn, whether she's infatuated with me or not I feel like I need to come up with an explanation pronto."
                ks sigh "The light effects her... optic sensors and temporarily shorts them, which allows me to slip my own commands into her system and break her original programming."
                ks "And yeah, my method of hacking a [hypno6] like this one is a lot like performing hypnosis on a human, but it's different."
                n side sad "Different how?" with dissolve
                ks neutral "Different in that... well, humans have free will, right?"
                ks "Hypnosis can effect people like you, but only if you let it. I might be able to hypnotize you, but I can never effect a change to you that you don't want."
                n sad_closed "That's right..." with dissolve
                "... Although all of this is bullshit, isn't it."
                ks "But this [hypno6] over here can only run on her programming."
                "It didn't bother me before. I knew what my hypnosis was doing to these girls ever since I hypnotized Hiroko in that alley."
                show Nozomi sad_side
                ks "Once I breached [p_their] defences with the light, [p_they] couldn't stop me from entering programming of my own." with dissolve
                "... Why is it starting to bother me now?"
                ks "Sayori can't choose to ignore the code I put in. [p_they!c] can only follow the instructions [p_they]'s given because [hypno6]s have no free will."
                "I then turn my head towards the confused, anxious-looking girl to our left."
                ks "Isn't that right, Sayori?"
                s casual surprised_right "I..." with dissolve
                "I know I've gotten enough into this girl's head that she'll respond the way I want her to."
                # "Fortunately, I think I got enough into her head earlier that she'll respond the way I want her to."
                s sleepy "Yes, Kyou. That is correct. As a [hypno6], I cannot choose to ignore my code." with dissolve
                s concerned_right "And as my programmer, I am compelled to process any instruction you give me." with dissolve
                "Her response seems to placate Nozomi's curiosity."
                n sad_closed "I see. I'm sorry, this is all still such a shock to me." with dissolve
                show Sayori concerned
                n front2 concerned "Sayori and Hiroko were my only real friends, you know?" with dissolve
                "But then as I hear what she has to say next, I start to realize what's been nagging at me."
                # "But what she says next stirs something in me."
                ks confused "What? I thought you had tons of friends."
                n sleeptalk "Oh I'm acquainted with a lot of people, sure." with dissolve
                "Seriously. She always seemed popular in class."
                n neutral_left "I hang out with some of our classmates. And I have my board game and karaoke nights with the literature club girls." with dissolve
                "But the more I look back, the more I realize these two girls are the only people I ever saw her talk to. Like, *really* talk to."
                n sleeptalk_concerned "It's... I don't know. I just have a hard time trusting people. There isn't really anyone I feel like I can trust outside of my own family." with dissolve
                "And I'm turning them both into mindless automatons to satisfy my own perverse curiosity."
                n concerned "No one else I can really open up to... except you, Kyou." with dissolve
                "As if I wasn't getting cold feet about this shit already. Shit, my brain's doing flips right now."
                n sleeptalk_concerned "You're all I have left, so..." with dissolve
                "I have to... do something..."
                n cry "Please don't ever leave me!" with dissolve
                "I have to..."
                menu:
                    " (disabled)Put a stop to this now":
                        pass
                    "Get a grip and finish what I started":
                        ks frown "Nozomi, come on. Get a hold of yourself!"
                        "No. This is no time for second-guessing myself. I gotta pull it together."
                        show Sayori concerned_right
                        n surprised "K-Kyou?" with dissolve
                        "I need to follow through. I need to see this through to the end."
                        ks angry "Hiroko and Sayori aren't your friends! They were NEVER your friends! They're... they're dangerous automatons who'd betray you the second their masters send the signal!"
                        n frightened "But... t-they're still my..." with dissolve
                        "So I will. I'll tell her what we both need to hear."
                        ks "They're [hypno6!u]S, Nozomi! They don't care about you or anyone!"
                        ks "Their whole lives were just a lie, a cover story made up by their creators. Whatever you think they feel for you? They don't. They don't feel a damn thing!"
                        "And I'll comfort her, of course. I'll take her trembling hands in mine as I speak our new truth to her. A truth we both need to fully believe in."
                        ks sad "I'm sorry, Nozomi. I know it hurts, but you have to let go. But I promise you it'll be okay. We will be okay."
                        show Nozomi cry
                        "We need to believe. For both our sakes." with dissolve
                        ks smile "I'm here for you. And I promise I'll never, ever leave you. Got it?"
                        show Nozomi sleeptalk_concerned
                        "I pull her in for a hug and my quivering new girlfriend throws her arms around me, choking down sobs." with dissolve
                        n "Y-y-you're right. Thank you for saying that."
                        n concerned "I'll be fine, Kyou. Just give me a little time." with dissolve
                        show Nozomi neutral_left
                        show Sayori concerned
                        "As she sniffles, I notice Nozomi glance towards our silent companion, who gazes forlornly back at her." with dissolve
                        "Sayori has nothing to say to defend herself. No compulsion to flee, or attack us, or scream for help."
                        "After all, [p_they] really is just a recently-reprogrammed [hypno6] short on commands from [p_their] newly-appointed programmer."
                        show Nozomi frown
                        "It's just the truth, right?" with dissolve
                        stop music fadeout 5.0
                        n "Do what you have to, my love..."
                        scene bg blackscreen with longdissolve
                        pause 2.0
                        jump Epilogue_Villain_Kyou
                #"Sayori and Hiroko were my closest friends. So this is still such a shock to me."
                #Kyou asks about Nozomi's other friends and she says that she considers the others she meets at school as mere acquaintances. She has a lot of trouble opening up to people
                #"There isn't really anyone I can trust outside of my own family... except you, Kyou."
                # ks "Because after all, you are a [hypno6], Sayori. A [hypno6] that processes instructions from [p_their] programmer. Just as you are doing now."
                # ks "That's right, Sayori. I am your programmer. And while you are in this deeply relaxed state I can alter any facet of your code that I please."
            else:
                #Kyou is surprised as this wasn't part of the plan, and Atsuko is still confused about the rush to all leave her house but after a little playful ribbing doesn't follow up on it
                #Then, while the three of them walk, Nozomi asks a bunch of questions related to what just happened
                #Nozomi could comment after that what Kyou did to Sayori looks identical to what he did to her and Kyou makes up an explanation about how breaking a robot's programming looks the same as hypnotizing a human
                #When Kyou has to choose, he either breaks down in similar fashion as the all robots path, or he angrily informs Nozomi not to try and bond with her friends anymore because they're robots and must be treated as such
                nm neutral "Well... could I speak to you before you go?" with dissolve
                "No. I'd rather get Sayori out of here in case she says something I'll regret in her post-hypnotic stupor."
                ks "Of course."
                scene bg n room day
                show Atsuko at center
                with blink
                play music Eons
                "I follow her outside as I wonder what she could possibly want to talk about."
                nm "It's just... I was so surprised. Did you know that this is the first time Nozomi has ever invited a boy over?"
                ks casual surprised "I, er... I didn't, no."
                nm surprised "I almost didn't believe it when she told me about you. She's never showed much interest in boys before." with dissolve
                "I let out a nervous chuckle as I rub the back of my neck."
                ks smile "And, uh... what has Nozomi been telling you about me, Mrs- I mean, Atsuko?"
                nm smile "Oh, very little to tell the truth. Mostly she was just very insistent that you be allowed to visit, so I had to read between the lines a little." with dissolve
                nm "Until yesterday I was actually starting to think she might be... you know?"
                nm laugh "Ahaha, not that there'd be anything wrong with that! We're a modern family, after all." with dissolve
                nm smile "But I've been telling her she needed some more people in her life, so I'm grateful if she's taken it to heart." with dissolve
                ks neutral "Wait, you're telling me she doesn't have many friends?"
                nm surprised "Does that surprise you, Kyou? I suppose it might; I'm sure she seems very outgoing and friendly on the outside." with dissolve
                nm neutral "But there are only a few people she genuinely trusts enough to bring any closer than that." with dissolve
                nm laugh "So you can't imagine how excited I've been to meet you, Kyou. You must be someone very special if you're connecting with her~" with dissolve
                nm happy "But I know, I know, you have places to be and you're having to listen to this old woman's natter. I won't keep you any longer today." with dissolve
                nm smile "Just... be kind to her, won't you?" with dissolve
                ks smile "Huh? O-of course."
                nm happy "Good! I hope to see you again, Kyou. You're welcome in this house anytime." with dissolve
                scene bg street1 day
                show Sayori casual at center
                with blink
                "That... was awkward."
                s neutral_right "Do we absolutely need to go to your home, Kyou? I have cram school to get to." with dissolve
                ks casual frown "Yes, we do. What makes you think you can question me, [hypno6]?"
                s concerned_right "I just... of course I do not \"think\" at all as I have discovered, but processing all of this is a shock to my system, Kyou." with dissolve
                "I learned some things about Nozomi that I didn't expect."
                s concerned "Having to accept that I am, as you say... a [hypno6]." with dissolve
                "I thought someone like her would be popular. She's kind, and beautiful. Everyone must want to know her as much as I do."
                # "I thought I knew everything there was to know about her."
                s casual_handup surprised_right "It is so outlandish, yet somehow I accept it completely." with dissolve
                "How could someone like Nozomi have barely any friends in her life?"
                s sleeptalk "This must obviously be a part of my programming. And processing that only leads me further into my acceptance of who... no, WHAT I am." with dissolve
                "Not to mention what else her mom said to me..."
                "\"Just... be kind to her, won't you?\""
                s casual sleep "So I apologize for questioning your authority, Kyou. You are my programmer after all." with dissolve
                "I've quieted this voice I've had in my head since I started all this. It hurts my project if I ever have to think of Nozomi and her friends as people."
                "But that woman brought that voice right back."
                menu:
                    "I have to stop this now":
                        ks sigh "Oh my god... What am I doing, Sayori?"
                        "I can't quiet that voice anymore."
                        s concerned_right "You... are leading me to your home, Kyou." with dissolve
                        ks "No, I mean... fuck, what am I DOING?!"
                        s casual_handup "I am sorry, but it seems my limitations as a [hypno6] prevent me from drawing a distinction between this question and your last one." with dissolve
                        s sleeptalk_concerned "So although I have processed that you require a different response, I can only supply an identical answer." with dissolve
                        show Sayori concerned_right
                        ks angry "Sayori, no, you're NOT a [hypno6]! NONE of you are!" with dissolve
                        ks "You're real girls from my class that I fucked with just because I could. Just to see how far I could go with you all. Like you were some fucking science project."
                        ks "And let's face it, I've already got my answer: I can go as far as I want!"
                        s casual surprised_right "Kyou, I... I do not know how to process this information. But if I were truly human then I would find your confession... frightening." with dissolve
                        ks frown "Yeah... I'm a little scared of myself right now."
                        ks "I haven't been kind to you. Or to Nozomi and especially not to Hiroko. Not to any of you. And you didn't deserve any of this. No one does..."
                        show Sayori concerned_right
                        "For a while it seems like time stands still while my mind opens up to the horrors of what I've done to these girls." with dissolve
                        "Even now, after hearing all of this, Sayori doesn't scream or run like a normal woman would."
                        "Instead, her expression is filled with concern at her programmer breaking down in front of her. Unable to do anything but follow my lead."
                        "Because after just a few short minutes under my penlight she truly thinks she's a [hypno6] now, just like the rest of them."
                        "How the fuck was this supposed to go, Kyou? Were you gonna keep them like this forever?"
                        "Just pretend this shit is fine and no one in their lives would notice anything amiss?"
                        ks sigh "Haaah.... h-haaaah...."
                        "It takes a few breaths, but eventually I can feel the cogs of my brain begin to turn once more as I try to form some kind of plan."
                        ks neutral "Alright... we're still going home, Sayori. Follow me."
                        s casual_handup "Of course." with dissolve
                        scene bg house
                        show Sayori casual neutral_right at center
                        with blink
                        "My mind continues to work amidst the dread I feel, as I lead my silent companion to my door..."
                        play sound dooropen
                        ks casual "Here, head inside. I think I know what I'm going to do."
                        scene bg k room day
                        show Sayori casual neutral_right at center
                        play sound doorclose
                        with blink
                        "Yeah. I'll send Nozomi a text; get her to come here as soon as she can."
                        "This dread feeling... I don't think it's ever gonna leave me for as long as I live."
                        "But it'll ease, if I give all these girls their lives back."
                        ks casual frown "Alright, so... here's what I'm gonna do."
                        show Hiroko tennis neutral_side at center, flip:
                            xpos 0.25
                        show Sayori neutral
                        "Just then there's a quiet padding of socked feet as Hiroko descends the staircase and calmly joins us in the living room." with dissolve
                        ks sigh "Ah shit, Hiroko..."
                        show phone at right with moveinright:
                            ypos 0.346
                        "Pulling out my phone, I quickly take a peek at my missed messages, just as I hear a gentle thud of a book dropping on my coffee table."
                        "{color=FF89AB}[hypno2]\n[hypno2]\n[hypno2]{/color}"
                        "{color=FF89AB}[hypno2]\n[hypno2]{/color}"
                        hide phone at right with moveoutright
                        s casual_handup surprised "Hiroko? I thought you were at tennis practice?" with dissolve
                        "This girl has been up and down those stairs literally hundreds of times. She must be completely worn out by now, no matter how hard she tries to hide it."
                        ks surprised "Hiroko, stop! That's enough!"
                        show Hiroko smile
                        "Having turned around to head up the stairs yet again, Hiroko ceases and turns back to face me with that quiet, eerie smile of hers." with dissolve
                        show Hiroko surprised_side
                        "At least for a moment, until she registers we have company." with dissolve
                        h tennis_headhold2 nervous_side "S-Sayori? Uh, hi?" with dissolve
                        "She sure passed my test alright. As if I needed another reminder of how badly I messed her up."
                        show Hiroko surprised
                        show Sayori surprised_right
                        stop music fadeout 15.0
                        ks sigh "Relax, both of you. You don't need to hide that you're \"[hypno6]\"s around each other. I hurt you both just the same." with dissolve
                        h tennis smile "Oh... yes, Kyou. I will shut down my human mode then 'cuz I'm super low on energy." with dissolve
                        ks "Yeah, you do that. You just have to listen to me, because I'm gonna do another deep programming session on both of you."
                        ks "And then Nozomi too, when she gets here..."
                        show Sayori casual neutral_right
                        "I take a deep breath as I steel myself for what I need to do." with dissolve
                        ks neutral "But first I'm gonna say a few things. Just for my own sanity; get these thoughts out into the open and see if they still make any sense at all."
                        queue music Diary
                        ks "So, uh... l-like, you're not gonna remember any of what I'm going to say, but I won't get another chance after, so I just wanna tell you how sorry I am for everything."
                        ks "Not just for what I've done to you. But for what I need to do to you now in order to set you free."
                        ks "Because I know I can't just blank your memories of the past few days, tell you you're human beings again and expect it all to work out. It's gone too far for that."
                        ks "And if I just removed the [hypno6] programming from your heads and brought you back to reality... Man, I don't wanna know what would happen if I did that."
                        ks "So... I'm not gonna suggest that you're not [hypno6]s anymore, but I'll push that part of your identities all the way back, in the deepest, darkest corners of your minds."
                        ks "I'll suggest the damage I did by hacking your programming will be repaired and that you'll be oblivious to your \"true\" natures once more."
                        ks "As far as you'll be consciously aware you'll consider yourselves normal human beings exactly as you were."
                        # ks "So... there'll still be a part of you, deep down, that you're [hypno6]s. I'll seal that part of your identity away at the back of your minds."
                        ks "But if anything happens, anything at all, where you need to recall these last days of your lives while you were running under my programming..."
                        ks "W-well, you'll be able to process those times effortlessly without discomfort, without ever feeling something truly terrible had happened to you."
                        ks "To your inner [hypno6] selves, you'll accept that these events were simply the cause of a rare glitch in your programming, never to be repeated."
                        ks "That should allow you to live your lives as you were before..."
                        "I nod to myself. It seems right to me. At least, as right as it can be."
                        stop music fadeout 10.0
                        scene bg blackscreen with dissolve
                        "So let's end this."
                        k "Okay, girls. Let's get you powered down..."
                        jump Epilogue_Villain_Robot_Quit
                        # "Okay, so, there's no way things can go back to how they were."
                        # "Things can't just go back to how they were. One of these girls has been out here fully believing she's not human for days."
                        # "And even Sayori here has been badly affected by what I've done."
                        # "She may have only just been converted, but she's experienced several days of pain over her friends because of what I've done."
                        # "If I just
                    "I need to finish what I started":
                        ks "That's right, Sayori. I'll need to alter your code to get rid of that disobedient human streak in you that caused you to question me in the first place."
                        "I need to quiet that voice again."
                        ks "And that's why we're going to my house. I need to do a lot of work on your buggy programming."
                        "These girls are NOT human. I've been over this. Nozomi and her clique are all [hypno6]s."
                        # "I just need to continue immersing myself thinking that these girls aren't human. As if I were doing a little programming on my own mind."
                        s neutral_right "I understand." with dissolve
                        "All of them. There's no need for me to think of them as human again."
                        stop music fadeout 10.0
                        scene bg k bedroom night with blink
                        "That turned out to be a productive day of programming."
                        show penlight at right with moveinright:
                            ypos 0.346
                        "Holding my penlight up as I lounge on my bed, I reminisce back to that day this all began; nearly a year ago at the culture festival."
    elif hypno1 == "spy hiroko":
        scene bg k bedroom day with longblink
        play sound doorbell
        "I'm barely up and showered before my doorbell rings."
        scene bg k entrance day
        show Nozomi front casual smile
        with blink
        "With a grin, I get the door and find a sweetly-smiling Nozomi there to greet me."
        "I gotta admit, after she's blanked me for so long, being able to make her come on command is more than a little pleasing."
        n "Good morning, Kyou~ May I come in?"
        "Still grinning, I swing the door fully open and step aside."
        ks casual smile "By all means. {w=0.5}{nw}"
        show Sayori casual angry_right at center, flip:
            xpos 0.25
        show Hiroko casual_armup furious at center:
            xpos 0.75
        with dissolve
        "Wh- what the?! {w=0.5}{nw}"
        scene bg blackscreen
        play sound [punch, punch, punch]
        with shake
        pause 1.0
        ks casual sigh "Urrgh..."
        ks "What... what just happened?"
        scene SleeperAgentStruggle nozomi n_smile sayori1 s_frown h_growl kyou1 k_dazed with longdissolve
        play music Rain
        n "We figured out you hypnotized us, so we decided to confront you about it."
        show SleeperAgentStruggle s_growl
        s "N-Nozomi! Don't tell him anything." with dissolve
        show SleeperAgentStruggle n_sigh
        n "Sorry. I couldn't help myself." with dissolve
        show SleeperAgentStruggle k_pain
        "I feel a groan escape my lips as I try to climb off the floor where I find myself, only to feel a weight push sharply into my spine." with dissolve
        show SleeperAgentStruggle n_frown s_frown kyou2 k_furious
        k "A- OWW!" with dissolve
        show SleeperAgentStruggle h_angry
        h "Don't fuckin' move!" with dissolve
        show SleeperAgentStruggle h_growl k_angry
        "I struggle, but Hiroko's got me pinned pretty good in spite of her tiny size." with dissolve
        s "Hmm. I do not know if this means anything, but he had on him his phone and this... looks like a penlight."
        "Meanwhile I have to suffer the other two literally talking about me behind my back."
        show SleeperAgentStruggle n_confused
        n side frown_side "Maybe he used an app on his phone to do it?" with dissolve
        show SleeperAgentStruggle s_confused
        s casual_folded "... He hypnotized the three of us with an app? That is what you're saying?" with dissolve
        n sad_side "... Hmm, well I read about it in a comic once."
        show SleeperAgentStruggle n_sigh blush
        n sad_closed blush "... A-actually, nevermind. That does seem far-fetched." with dissolve
        show SleeperAgentStruggle h_angry_side
        h "Just fucking ask him!" with dissolve
        "I grimace as I feel the full weight of this little punk on my back." with vpunch
        show SleeperAgentStruggle n_frown -blush s_frown h_frown
        "If only I wasn't such a pathetic specimen of a man, I would've thrown her across the room by now." with dissolve
        h "How'd you do it, dude?"
        show SleeperAgentStruggle kyou1 k_growl
        k"Agh... y-you're saying I hypnotized you all somehow? Don't be ridiculous!" with dissolve
        s frown_right "We know, Kyou. Nozomi figured it out."
        show SleeperAgentStruggle k_confused
        k "What?" with dissolve
        "I thought that's what I heard the first time, but... that's impossible."
        "They should've forgotten everything."
        show SleeperAgentStruggle h_angry k_pain
        h "DON'T play dumb with us!" with vpunch
        k "Ugh... w-what makes you even think I could do that?"
        show SleeperAgentStruggle n_smile s_growl h_growl
        n frown "Well, we- {w=0.5}{nw}" with dissolve
        show SleeperAgentStruggle n_surprised sayori2 s_irritated
        s "NOT another word!" with vpunch
        n surprised "Mmpth!"
        "Nozomi's answer is abruptly cut off as Sayori claps her hand around Nozomi's lips."
        "For a brief moment I wonder if she remembers doing exactly the same thing to her just a couple days ago."
        show SleeperAgentStruggle s_angry
        s "You really can't help yourself, can you." with dissolve
        show SleeperAgentStruggle n_frown
        s "Anyway, you needn't concern yourself with that, Kyou. What should concern you is whether or not you answer our questions to our satisfaction." with dissolve
        show SleeperAgentStruggle k_growl
        k "And... and why should I? You come into my home and you assault me! I should be asking you to leave!" with dissolve
        show SleeperAgentStruggle h_angry
        h "We ain't leaving 'till you tell us how you did this shit to us!" with dissolve
        s "And when we can ensure you are never able to do so again."
        show SleeperAgentStruggle h_frown
        "I scoff at them. How are they gonna do that? By killing me?" with dissolve
        show SleeperAgentStruggle n_confused sayori1 s_frown
        n frown "I guess it's not safe for me to be around him right now, so I'm going to check his room." with dissolve
        show SleeperAgentStruggle k_confused
        k "Huh, why? What are you going to do?" with dissolve
        show SleeperAgentStruggle n_smile k_pain
        n smile "I'm going to examine your room for clues about how you hypnotized us all." with dissolve
        show SleeperAgentStruggle n_sigh s_growl
        n front irritated "Urrrgh..." with dissolve
        show SleeperAgentStruggle -nozomi -n_sigh s_frown
        "And with that Nozomi scurries away from me, out of my reach." with dissolve
        s "Well then, Kyou, are you ready to talk?"
        "Dammit, what am I supposed to do?"
        "Am I really gonna just lie here? Let myself get restrained by a little girl like a fucking wimp?"
        "Sure, I'm no alpha male, but I could take Hiroko on if I wanted to."
        "Hell, Sayori won't be hard to knock down either. I could take them both on."
        "Then I'd grab my penlight back and put them under before they can do anything about it."
        show SleeperAgentStruggle h_growl kyou2 k_furious
        k "A-AGH!" with vpunch
        "Bitch behind me is twisting my arm."
        show SleeperAgentStruggle h_angry
        h "Fuckin' spill, you piece of shit!" with dissolve
        show SleeperAgentStruggle h_growl k_angry
        "That's it, I'm gonna..." with dissolve
        menu:
            "Talk":
                $persistent.sleeper_agent_struggle1_unlock = True
                show SleeperAgentStruggle k_furious
                $ renpy.transition(dissolve, layer="master")
                k "A-ALRIGHT! Just let go of me, will you?"
                show SleeperAgentStruggle h_angry
                h "Ain't happening. Tell us what you did!" with dissolve
                "Reason wins out, I guess. I'll talk a bit while I try to figure out what went wrong."
                show SleeperAgentStruggle h_growl kyou1 k_pain
                k "O-okay, so..." with dissolve
                "Did they shake off their mental conditioning somehow? Is that how they found out?"
                k "When me and Nozomi were cleaning the classroom by ourselves. That's when I hypnotized her."
                "But then... No, it seems Nozomi is still responsive to the commands I sent her last night."
                s "And how did you accomplish that, Kyou?"
                "So then..."
                k "I just, like, got her to stare at my finger and encouraged her to go into a trance for me."
                "Okay, I can figure out how they found out later. What's important is that if Nozomi hasn't shaken off the mental conditioning that I gave her..."
                "... Then I'm gonna bet these two haven't either."
                s "And that is all it took to have her eating out of your hand?"
                "But without my penlight or my phone, how does that help me?"
                show SleeperAgentStruggle h_angry_side
                h "C'mon, he's obviously lying!" with dissolve
                s "Oh, I agree. He is definitely leaving something out."
                show SleeperAgentStruggle h_frown
                k "I-I'm telling you, there wasn't much to it." with dissolve
                show SleeperAgentStruggle s_growl
                s irritated "Kyou, we are not so naive to accept that you simply pointed a finger and uttered a few words." with dissolve
                h "Yeah, like where's your pocketwatch?"
                show SleeperAgentStruggle k_dazed
                k "What? I don't have a pocketwatch." with dissolve
                show SleeperAgentStruggle s_confused
                s "Hopefully Nozomi will find something that can help us." with dissolve
                show SleeperAgentStruggle s_frown
                s frown_right "In the meantime, Kyou, you should elaborate on what you were trying to do with us." with dissolve
                k "U-uh..."
                "Wait, that's it. There's a chance I can put them both back into a trance for me just by running my mouth off."
                show SleeperAgentStruggle k_calm
                k "I just wanted you all to listen and obey." with dissolve
                show SleeperAgentStruggle h_growl kyou2 k_furious
                k "AGH, FUCK!" with vpunch
                show SleeperAgentStruggle h_angry
                h "You deserve it, you creepy shit!" with dissolve
                "I cry out as this bitch twists my arm again."
                show SleeperAgentStruggle h_growl kyou1 k_pain
                "Resisting the urge to lash out, I keep talking." with dissolve
                "\"Listen and obey\". If I can work that phrase in some more, I might be able to turn this around."
                s "So you admit you tried to influence all of us? Not just Nozomi?"
                show SleeperAgentStruggle k_calm
                k "O-oh yeah, it wasn't just Nozomi I needed to listen and obey. Wasn't just her who needed to silence the thoughts in her head and drop into a deep trance for me." with dissolve
                show SleeperAgentStruggle h_frown
                "It might be my imagination, but I think I just felt Hiroko's grip on my arms loosen." with dissolve
                show SleeperAgentStruggle s_growl
                s irritated "We will get to the how later, but what purpose did it serve?" with dissolve
                s "What questions were you hoping to ask Nozomi that you couldn't have asked her through regular conversation?"
                show SleeperAgentStruggle h_growl
                h "S'gotta be some nasty perv shit. You know he's got the hots for her..." with dissolve
                k "It was just a test to see if she'd come see me at all! I wanted to see if she'd listen and obey like I was hoping."
                show SleeperAgentStruggle h_confused s_confused
                s frown_right "\"Listen and obey\"? Shouldn't that be..." with dissolve
                show SleeperAgentStruggle s_sleepy
                s sleepy "Uhh, \"Read and obey\"? It was a text message you sent her..." with dissolve
                show SleeperAgentStruggle h_worried
                h "Sayori, something ain't right..." with dissolve
                "Yeah, I can definitely feel the grip on my arms getting weaker."
                "I could probably pull her off of me with ease right now, but I think it'll be better if I just continue like this for a while longer..."
                show SleeperAgentStruggle k_sneer
                k "No, you heard right. I hoped she would listen and obey. Just like how you both are listening to me right now." with dissolve
                s "There's something... f-familiar about this..."
                k "And... yes, there's a comforting familiarity to my words I think you'll find. A comfort for you both to listen and obey."
                show SleeperAgentStruggle h_sleepy
                h "Shut up with that creepy shit, or I'll... I-I'll..." with dissolve
                k "You'll continue to listen, Hiroko. It feels so correct, so natural, to listen and obey."
                k "As will you, Sayori. You wanted me to talk, so I'll talk. And you will listen and obey."
                show SleeperAgentStruggle s_entranced
                s casual "L-listen... no..." with dissolve
                stop music fadeout 10.0
                k "No need to think, girls. Just remember what it is to listen and obey."
                show SleeperAgentStruggle h_entranced
                "My heart skips a beat as I feel Hiroko's hold on me completely slacken. She's doing little more than resting atop me now." with dissolve
                "And judging from the lack of protest from Sayori up there, she's got to be..."
                # "My heart skips a beat as I watch Sayori from the floor; seeing her body stiffen while her twitching eyes gaze blankly ahead." with dissolve
                # "So surely Hiroko must be..."
                k "Hiroko, as you listen and obey, get back up and stand beside Sayori for me."
                $persistent.sleeper_agent_struggle2_unlock = True
                scene bg k room day
                show Hiroko casual entranced_neutral at center
                show Sayori casual entranced_right at center, flip:
                    xpos 0.25
                play music Flow
                with longblink
                "Hiroko's tenuous grip on me is released entirely as she rises and goes to stand where I tell her."
                "I gotta say, even with what I've been able to do with them these past few days, I wasn't convinced that would work."
                "But as I grin and pick myself up off the floor, watching the two of them as they stand in front of me with such distant expressions..."
                "I start to appreciate how much is truly possible with my newfound abilities."
                ks casual smirk "Good girls. Going nice and deep for me now. Back into this nice, comfortable, familiar and natural state of trance."
                "As I look them both over, I see both pairs of eyelids continue to flicker."
                "I wonder if that means they're trying to resist this state I'm inducing in them?"
                "Well, it's not like it matters. As I retrieve my phone and penlight from the table, I can see they're not going to come out of it anytime soon."
                "Not until I let them."
                show Nozomi side casual frown_side  at center:
                    xpos 1.2
                    linear 1.0 xpos 0.75
                n "It's the penlight. He was using the penlight to- {w=1.0}{nw}"
                n surprised_side "H- hypnotize... us?" with dissolve
                show Nozomi:
                    xpos 0.75
                "For a moment she stands frozen, her mouth agape as her two friends stare vacantly back at her."
                n sad_side "Sayori? Hiroko? You're not... no. No, wake up! Please wake up!" with dissolve
                "I admit, in the heat of what I was doing I'd forgotten Nozomi was upstairs."
                ks "Uh, Nozomi, hey... How are you?"
                show Nozomi front surprised
                n "I'm terrified. How are you even doing this?" with dissolve
                n shocked "It... i- it shouldn't be possible!" with dissolve
                ks "Hey, Nozomi, calm down. If you listen and obey I'll explain everything."
                n scared "What's there to explain, Kyou? If... if you're controlling us against our will, it doesn't matter what you're doing." with dissolve
                n cry "You're a monster." with dissolve
                ks "What makes you think I'm going against your wills? Maybe deep down you all want to listen and ob- {w=1.0}{nw}"
                n angry "They're my friends, Kyou. They'd never stand by and watch while you try to hypnotize me along with them." with dissolve
                n "Yeah, Kyou, I know what you're up to."
                ks "I'm... I'm not up to anything, I just want- {w=0.8}{nw}"
                n front2 determined "The least you could do is not insult me, Kyou." with dissolve
                n frown "You're trying to hypnotize me again. You don't normally talk like this." with dissolve
                "I can see her blinking back tears as she tries to assert herself, a quaver in her voice."
                "Even if she hadn't told me, I can feel her fear from where I'm standing."
                n neutral "And... And even knowing this, I know you could still somehow hypnotize me like you did with them." with dissolve
                n concerned "So... b-before you do, will you let me say a few words?" with dissolve
                ks "Nozomi, come on. You talk like I'm about to kill you."
                n cry "Humor me? Please? I know you're already in my head, and it's only a matter of time." with dissolve
                n "S-so could you please let me have this?"
                "Well, I have to hand it to her; she's right. Maybe more than she knows."
                "If these two were anything to go by, all I need to do is invoke the phrase I taught her and she'll soon slip back into trance same as her friends."
                "So why not let her say her piece?"
                menu:
                    "Let her speak":
                        ks neutral "What were you gonna say, Nozomi?"
                        n "I was just..."
                        "Nozomi takes a halting breath as her gaze turns towards the other girls, still lost in their own minds where I left them."
                        n side sad_side "H-Hiroko. Sayori. I'm sorry. I'm so sorry I got you involved in this." with dissolve
                        n sad_closed "A-and I know you won't consciously hear anything I'm saying to you, but... b-but..." with dissolve
                        "I can hardly bear to see her like this. With such a desperate, tearful, pleading face."
                        n neutral_side "But maybe there's a part of you both that remembers you made me a promise? Maybe that part of you is listening right now." with dissolve
                        n "Do you remember? When you promised you wouldn't leave me alone? Because right now it feels like you forgot."
                        n sad_closed "And I know you didn't forget. You just need to consider how important it is that you honor your promise right now." with dissolve
                        "Wait a sec. What is she fucking doing?"
                        n front2 frightened "How important it is for you both to come back and commit to your promise, I'm begging you!" with dissolve
                        n "D-don't leave me alone, but, b-but especially-"
                        ks frown "Nozomi, I think that's enough! It's about time you listen- {w=0.8}{nw}"
                        stop music
                        n "DON'T LEAVE ME ALONE WITH HIM!" with shake
                        show Sayori surprised_right
                        show Hiroko surprised
                        h "W-wha?!" with dissolve
                        s "Nozomi. What is..."
                        "Shit."
                        n angry "NOW! STOP HIM!" with dissolve
                        ks angry "Wait, NO! I SAID LISTEN AND-{w=0.5}{nw}"
                        show Sayori angry_right
                        h casual_armup furious "SHUT THE FUCK UP!{w=0.8}{nw}" with shake
                        scene bg blackscreen
                        play sound [punch, punch, punch]
                        with shake
                        pause 1.0
                        "Oh... oh man, I feel like I've been kicked in every conceivable part of the human body."
                        "Everything hurts..."
                        scene bg k room day
                        play music Rain
                        show Nozomi front casual frightened at center
                        show Sayori casual_folded cry at center, flip:
                            xpos 0.4
                        show Hiroko casual_armup cry at center:
                            xpos 0.6
                        # show Sayori casual_folded frown_right at center:
                        #     xpos 0.25
                        # show Nozomi casual frown at center
                        # show Hiroko casual_armup angry at center:
                        #     xpos 0.75
                        with longdissolve
                        "And when the dust settles I find myself once again on the floor with three girls towering above me."
                        "They're... crying in a huddle?"
                        s "I never felt anything like it, Nozomi. He, h-he was saying something to us and it all started to feel like a dream."
                        h "Yeah, right? That was s-so fuckin' scary! I couldn't do ANYTHING!"
                        n "I-I know, but it's okay. We're going to be okay!"
                        "They look so pathetic. They didn't even get hurt; I'm the one lying bruised on the floor."
                        "And while they're huddled like that I don't know if they've realized I've come to."
                        "They might have come out of their tranced states now, but I bet even now I can drop them back with a few careful words..."
                        k "Mm.. mmpth?"
                        "Wait, my lips aren't moving."
                        show Sayori concerned_right
                        show Hiroko cry_open
                        show Nozomi cry
                        "And as I struggle to work my mouth I notice the girls have turned their attention to me." with dissolve
                        n "W-we'll make sure he can't hurt us anymore."
                        "It's coming back to me now, about the fight we just had. Involving a three girl pile-on and a shitload of duct tape that they must have swiped from the kitchen."
                        "How much of the fucking stuff did they use on me? Shit."
                        show Sayori at flip:
                            linear 1.0 xpos 0.3
                        show Hiroko:
                            linear 1.0 xpos 0.7
                        "I can barely move down here, and it's all I can do to try sitting up on the floor as the girls break off their embrace to watch me carefully like I'm some caged animal."
                        scene SleeperAgentDefeat with blink
                        "Wiping her eyes with one hand, Nozomi crouches down beside me. And that's when I notice what's in her other hand..."
                        n "What's with that look, Kyou? It's just a harmless penlight isn't it?"
                        n "Anyone would think it was dangerous, the way you're flinching at it."
                        "Goddammit. I gotta figure a way out of this fast."
                        h "What're we gonna do about him?"
                        s "We could destroy that penlight, but..."
                        n "But you'll probably make a new one, won't you, Kyou?"
                        "I shoot her a glare. To think I trusted her and her tears just now... I thought she was better than that."
                        "But yeah. I mean, of COURSE I'd make a new one!"
                        "Even if they destroy it and the schematics I left on my computer I know the gist of what I did before."
                        "I could try again..."
                        h "Shit. Just looking at him's makin' me feel he's in my head again."
                        show SleeperAgentDefeat doubt_right
                        h "Nozo, make him stop, you gotta make him stop." with dissolve
                        n "There's a way, but... are we going to be okay with it?"
                        show SleeperAgentDefeat doubt_left
                        s concerned "You mean..." with dissolve
                        "No, come on, there's gotta be a way out of this tape. If I can just..."
                        h "Shit, how else are we 'sposed to stop him?"
                        show SleeperAgentDefeat doubt_right
                        h "No one else's gonna believe any of this shit if we tell 'em. S-so what, we just run and hope he never pulls this shit again?" with dissolve
                        h "We just gonna live in fear of this dude the rest of our lives? 'Cuz I ain't having it!"
                        # h cry_open "He ain't gonna stop otherwise, is he? And we're gonna be afraid of him forever, and..." with dissolve
                        h "I don't wanna live like that! It ain't fair!"
                        show SleeperAgentDefeat doubt_left
                        s "I... don't disagree. He has presented us with a unique and frightening quandary." with dissolve
                        "Ugh, just listening to these three debate what to do with me like this. It's humiliating."
                        "But I think I felt something give. Just a little more, maybe..."
                        s "But is it even an option for us? It seems you believe this is possible, Nozomi."
                        s "It can be done?"
                        show SleeperAgentDefeat doubt
                        n "I don't know. But it shouldn't have been possible for him to do what he did to us, so..." with dissolve
                        show SleeperAgentDefeat doubt_left arm_up
                        n frown "I think it's worth it to try." with dissolve
                        show SleeperAgentDefeat neutral
                        "Shit, no! Get that away from me!" with dissolve
                        k "M-MMTH!"
                        show SleeperAgentDefeat determined light
                        with flash
                        n "Don't worry, Kyou. You know I won't hurt you."
                        "No! Bitch, you are NOT taking this away from me!"
                        "Like you even know how to use that thing in your hand..."
                        with flash
                        n "Far from it, Kyou. I mean, for you to go through with all of this? I think... I think you're in a lot of pain."
                        with flash
                        k "Mmpth."
                        "You think waving that light in my face is all it takes, and now you're pitying me? Fuck you. Just fuck you."
                        with flash
                        n "And maybe I can help, Kyou. Just as long as you keep staring up at this light as you have been."
                        with flash
                        "... Wait, why AM I staring at the light?"
                        show SleeperAgentDefeat neutral
                        with flash
                        n "It's okay if you didn't notice. We both know how irresistible this light is by now, don't we?"
                        with flash
                        "And her voice... she doesn't even sound angry. Just sort of... wistful."
                        n "So it's only natural if you're unable to look away; seeing those patterns form in your eyes as you continue to stare so diligently."
                        with flash
                        "It's almost... nice..."
                        n "That's right, Kyou. We all know how much you like to stare."
                        show SleeperAgentDefeat sad
                        with flash
                        "... Wait, what's going on?"
                        n "And it's fine. Stare as much as you like."
                        with flash
                        n "It's such a normal thing to do under the circumstances, right? We've all done it."
                        with flash
                        "Right. I was staring at that light. Just staring normally..."
                        n "So don't worry, Kyou. Stare all you want. Relax all you want..."
                        with flash
                        stop music fadeout 20.0
                        show bg blackscreen onlayer toplayer with dissolve:
                            alpha 0.2
                        n "Drift all you want... That's it."
                        with flash
                        show bg blackscreen onlayer toplayer with dissolve:
                            alpha 0.4
                        n "Just letting yourself drop into a nice, calm state for us. Letting your eyes close as they are."
                        with flash
                        show bg blackscreen onlayer toplayer with dissolve:
                            alpha 0.6
                        n "That's right, Kyou. It's going to be okay."
                        with flash
                        show bg blackscreen onlayer toplayer with dissolve:
                            alpha 0.8
                        n "So you can let those eyes close for me now."
                        show bg blackscreen onlayer toplayer with dissolve:
                            alpha 1.0
                        n "I'll take care of everything..."
                        $persistent.sleeper_agent_defeat_unlock = True
                        scene bg blackscreen with fade
                        hide bg blackscreen onlayer toplayer
                        scene bg classroom eve with longdissolve
                        play music Memories
                        "As another school day draws to a close, I gather my things and ponder."
                        play sound schoolbell
                        $nozomi_name = _("Class Rep")
                        $sayori_name = _("Tired-Looking Girl")
                        $hiroko_name = _("Pink-Haired Girl")
                        show Hiroko uniform_armup angry_side uniform_arm at center
                        show Sayori neutral at center, flip:
                            xpos 0.25
                        h "Fuckin' finally. Now I'm gonna blow off tennis club and punch the walls in my room." with dissolve
                        s concerned "I am so sorry about yesterday. It wasn't your fault." with dissolve
                        h neutral_side "I can't stop thinking about it, y'know? That shit really got in my head." with dissolve
                        "What on earth was I doing these last few months?"
                        h sad_side "I'll never forgive that motherfucker." with dissolve
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
                        h "No, it ain't your fault. There's only one person whose fault this is and he's..."
                        "I guess I'd better head home..."
                        h sleep "Just tell me it ain't happening again." with dissolve
                        n frown_side "It won't. We destroyed it and everything about it that we could find. Please try not to worry." with dissolve

                        h angry "{size=16}Fuck, here he comes.{/size}" with dissolve
                        show Sayori concerned_right
                        ks neutral "Hm?" with dissolve
                        "I get up to leave, but as I start to head out I notice three girls look to me and... was that pink-haired girl talking about me?"
                        n surprised "A-ah, it's nothing. She's just having a bad day, that's all." with dissolve
                        h irritated "Yeah... Just a bad day." with dissolve
                        "I look over the three of them, and... wait, are these girls in my class?"
                        show Nozomi front neutral
                        "They must be but, wow, how do I not know them by now? Especially this pink-haired girl. She really stands out." with dissolve
                        "I think our brown-haired class rep called her Hiyoko? I wonder what they were talking about."
                        s "Is he... is he just going to stand there, do you think?"
                        "Maybe she just transferred here and I missed it?"
                        h angry "Wh-what're you staring at?" with dissolve
                        ks surprised "H-huh? Oh..."
                        "Shit, I'm bothering them. Maybe I'm being creepy again."
                        "I should just excuse myself and leave."
                        ks sigh "Sorry. I'll get out of your hair."
                        "As I turn to head out the door, I hear the pink-haired girl suck in a breath."
                        h "Y-yeah... go on, get outta here."

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
                        # n frown "Not so fast. I want to try something." with dissolve
                        # with flash
                        # "...She just- {w=0.5}{nw}"
                        # n "Don't worry, Kyou. You know this won't hurt."
                        # "She just flashed me with the penlight!"
                        # ks "Y-You don't know what you're doing!"
                        # with flash
                        # n "And you don't need to worry about that right now."
                        # h sad_side "Err, what are you doing, Nozo?" with dissolve
                        # with flash
                        # n "Shh, just keep him still for me."
                        # ks "N-nozo, stop-{w=0.5}{nw}"
                        # with flash
                        # play music Flow fadein 30.0
                        # "Dammit, I invented this thing! I know what it does so why- {w=0.7}{nw}"
                        # with flash
                        # n neutral "And Kyou, all you have to do is focus." with dissolve
                        # with flash
                        # "Why am I just going along with this?"
                        # with flash
                        # n "Focus on the light flashing past your eyes."
                        # with flash
                        # n "Focus on your breathing as it slows, nice and deep."
                        # s casual_folded frown_right "{size=14}I am not sure I like this.{/size}" with dissolve
                        # with flash
                        # n "Every time the light passes, relaxing a little deeper for me."
                        # with flash
                        # n "Feeling so relaxed. Feeling your eyes become heavier and heavier with every blink."
                        # with flash
                        # show bg blackscreen onlayer toplayer with dissolve:
                        #     alpha 0.2
                        # n "Feeling so good about relaxing."
                        # with flash
                        # show bg blackscreen onlayer toplayer with dissolve:
                        #     alpha 0.4
                        # n "Feeling so good about going under for me."
                        # with flash
                        # show bg blackscreen onlayer toplayer with dissolve:
                        #     alpha 0.6
                        # n "That's right, Kyou. So willing to drop for me. Dropping deeper."
                        # with flash
                        # show bg blackscreen onlayer toplayer with dissolve:
                        #     alpha 0.8
                        # n "Dropping deeper."
                        # with flash
                        # show bg blackscreen onlayer toplayer with dissolve:
                        #     alpha 0.9
                        # n "Sleep."
                        # stop music fadeout 4.0
                        # $ending = "hypnotized"
                        # scene bg blackscreen with fade
                        # hide bg blackscreen onlayer toplayer
                        # jump Epilogue_NonCon_Kyou

                    "Put her out of her misery":
                        "No. I can't bear to see her like this any longer."
                        ks smile "Nozomi, I promise. Once you listen and obey, I'll let you say whatever you want."
                        n "K-Kyou, please."
                        "Resting my hands on the shoulders of the other girls, I smile as I continue to speak."
                        ks "Let's say it together, girls. \"Listen and obey\"."
                        $multi = "{color=385599}Sayori{/color}{color=#FFFFFF} and {/color}{color=FF89AB}Hiroko{/color}"
                        show Sayori entranced_talk_right
                        show Hiroko entranced_talk
                        multi "Listen and obey..." with dissolve
                        show Sayori entranced_right
                        show Hiroko entranced_neutral
                        n surprised "L-listen and..." with dissolve
                        ks "That's right, girls. Feeling so good, so comfortable, so right about falling deeper for me."
                        ks "So let's say it again, girls: \"Listen and obey\"."
                        $multi = "{color=93624B}Nozomi{/color}{color=#FFFFFF},{/color} {color=385599}Sayori{/color}{color=#FFFFFF} and {/color}{color=FF89AB}Hiroko{/color}"
                        show Sayori entranced_talk_right
                        show Hiroko entranced_talk
                        show Nozomi entranced_talk
                        multi "Listen and obey..." with dissolve
                        show Sayori entranced_right
                        show Hiroko entranced_neutral
                        show Nozomi entranced_neutral
                        "My smile widens as I notice Nozomi absent-mindedly following suit with the others. Any chance she may have had of resisting already lost in her own vacant whisper." with dissolve
                        ks "Allowing yourselves to remember fully how perfectly natural it is for you to be in this deep, obedient state of trance."
                        ks "All your conscious thoughts, cares, and worries effortlessly drifting far away, girls, as you repeat for me one more time: Listen and obey."
                        show Sayori entranced_talk_right
                        show Hiroko entranced_talk
                        show Nozomi entranced_talk
                        multi "Listen and obey..." with dissolve
                        show Sayori entranced_right
                        show Hiroko entranced_neutral
                        show Nozomi entranced_neutral
                        "As they all intone blankly, I breathe out a sigh that I've been holding for a while." with dissolve
                        "The pain in my bruised back and arms reminding me how close I came to losing it all."
                        "I'll have to make sure they'll never get a chance to stop me again."
                        ks "Good girls. Your minds becoming so blank, so free of thought, and that's perfectly okay. They won't need to stay blank for long."
                        ks "In a moment, I will tell you of some new thoughts for your minds to accept as if they were your own."
                        ks "And you will find it so easy, so automatic, to accept them as your own thoughts, because of how free of thought you are now."
                        "I pause a moment to look over each of them carefully as they as they stare vacantly back at me. They look every bit as blank as I describe."
                        "What I have in mind should work. After everything, there's no reason why it wouldn't."
                        ks "So here is your first thought, girls... you fully accept and cherish the fact that I hypnotized you into my service as my personal spies."
                        ks "Any objections you might have had to this in the past are mere disagreements that you have completely moved on from."
                        # k "Good girls. As you listen so very carefully, I want you to realize how completely true and correct each of my following statements are."
                        "I mean, why am I leaving so much to chance now? Controlling them so covertly like I have been?"
                        ks "So now your first priority, always, is to gather information while under the guise of being ordinary high school students."
                        # k "You fully accept and cherish the fact that you work for me as my personal spies."
                        # k "You fully accept and cherish the fact that you have been hypnotized into working for me as my personal spies."
                        "This past week's shown me just how deep a level of access I've attained to their minds. To their realities."
                        ks "When you learn something new, your first thought is always \"How will this information benefit Kyou Koyama?\""
                        "So why not shape their realities such that they won't even think to stop me? Even ENJOY helping me in my goals?"
                        ks "And nothing brings you more pleasure than sharing your information with me."
                        # k "What's more, you fully accept that you've been hypnotized to think like this. And that's okay."
                        # k "It's just one thing that you know and love about me."
                        # k "You love nothing better than to give me any information I ask of you, and assist me in any way I see fit."
                        # k "All while keeping the fact that you work for me a secret from anyone who you know isn't one of my spies."
                        # "So why not shape their realities such that they won't even want to stop me? Even LIKE what's happening to them?"
                        ks "Do you understand, girls?"
                        show Sayori entranced_talk_right
                        show Hiroko entranced_talk
                        show Nozomi entranced_talk
                        multi "Yes..." with dissolve
                        show Sayori entranced_right
                        show Hiroko entranced_neutral
                        show Nozomi entranced_neutral
                        ks "Good. Now, in a few moments I'm going to tap you on your nose, and when you feel the tap, count slowly to three in your head and return to wakefulness." with dissolve
                        ks "Returning to wakefulness and fully accepting everything you were told."
                        stop music fadeout 5.0
                        "I leave a moment for my words to sink in, then gingerly tap my fingertip against the bridge of Nozomi's nose."
                        "Let's see how she responds to this..."
                        n neutral "..." with dissolve
                        ks "Welcome back, Nozomi."
                        play music Eons
                        "I can see the focus return to Nozomi's eyes as she comes to, smiling as she registers my voice."
                        n smile "Ah, thanks. I'm still feeling a little disoriented~" with dissolve
                        "I smile back, encouraged. Although I'm confident I have nothing to worry about, I should still test her response before I wake the others."
                        ks "I hope you're feeling better after your little freakout just now."
                        "Nozomi giggles quietly."
                        n happy "Of course~ Looking back, I feel kinda silly making so much fuss." with dissolve
                        n smile "So I want to assure you, I'm completely happy with our working relationship." with dissolve
                        "Her gaze turns to her two friends, still standing entranced in the middle of the room."
                        n pout_left "Aren't you going to wake them up?" with dissolve
                        ks "In a minute. I just wanted to make sure you were on board with all this first."
                        ks "I mean, what I'm asking you to do, going behind people's backs and informing on them for me..."
                        ks "It's a big ask."
                        "Nozomi gives a determined nod."
                        n frown "I understand, but I want to do this for you, Kyou. It feels right." with dissolve
                        n "And I know my friends will want to do their part, too."
                        "I look into her eyes, her face, anywhere she might exhibit a tell that she might be trying to pull the wool over my eyes."
                        "But there's none that I can see."
                        stop music fadeout 5.0
                        "Satisfied, I turn to one of the others and bring my finger up to tap the tip of their nose..."
                        $spyfight = False
                        jump Epilogue_Villain_Kyou

            "Fight":
                "Yeah. I know boys aren't supposed to hit girls, but... fuck it. I'm done playing nice."
                "I'm not going to let these fucking bitches take everything from me."
                show SleeperAgentStruggle h_angry
                h "I {nw}" with dissolve
                extend "SAID- {w=0.5}{nw}" with vpunch
                $persistent.sleeper_agent_struggle1_unlock = True
                scene bg blackscreen
                play sound punch
                #He pulls his arms back which pulls Hiroko forward, then throws his head back to hit her
                "Hiroko screams into my ear, but a moment later her scream reaches a different pitch as I throw my head rearward, hitting her nose with the back of my skull." with vpunch
                scene bg k room day
                show Sayori casual surprised_right at flip, center:
                    xpos 0.25
                with dissolve
                "I wince at her fucking volume, but all too quickly she pulls away and her screams are muffled as she claps her hands over her face in anguish."
                show Sayori casual panicked_right
                "And in a flash, {nw}" with dissolve
                extend "I haul myself forcefully back to my feet, which serves to flip Hiroko onto her back as she lets out another howl." with vpunch
                "Just as I rise to my full height, I find myself locking eyes with the other one."
                "Her tired eyes are uncharacteristically wide as her sleep-deprived mind tries to take in what's happening in front of her."
                "That's too bad. As by the time she raises her arms to defend herself I'm already there to shove her full in the chest."
                # "It happens pretty fast, and Sayori's sleep-deprivation stops her from reacting very quickly." with dissolve
                # "And when she does react, it's more in shock at the violence she's witnessing and gives Kyou ample time to stand to full height."
                show Sayori at flip:
                    xpos 0.25
                    linear 1.0 ypos 2.0
                s "A-aahh! {w=0.5}{nw}"
                play sound bodyimpact
                extend "" with vpunch
                "And down she goes, stumbling backwards to crash to the floor between the table and the couch while the phone and penlight she was holding spill out of her hands."
                # "Sayori barely has time to defend herself as Kyou shoves her hard and she stumbles backwards to fall between the floor and the couch." with vpunch
                hide Sayori
                "The adrenaline running hot in me, I seize my chance as I scoop my penlight up from the floor..."
                show Hiroko casual_armup furious vein at center:
                    ypos 2.0
                    linear 1.5 ypos 1.0
                "... Just as I turn to find a furious Hiroko yapping at my heels."
                # "Now with the opportunity, Kyou is able to grab his penlight from the floor where Sayori drops it, as a furious Hiroko hauls herself to her feet to confront him."
                show Hiroko:
                    ypos 1.0
                h "Y-you {w=0.1}{nw}"
                extend "FUCKIN'..." with vpunch
                "Hiroko lunges but I'm ready for her, as I reach out and grab her arm before her punch can connect."
                show Hiroko angry
                "She grunts and strains as we tussle, while she seems to blink back the pain in her eyes." with dissolve
                "That headbutt just now really smarted her, I can tell."
                "And it gives me ample time to hold my penlight in my other hand properly, as I switch it on..."
                s "Hiroko! Don't look at that light!"
                h angry_side "WHAT?" with dissolve
                "Fine. So Sayori figured it out. Big woop."
                show Hiroko irritated novein with dissolve
                $lnumber = 1; light_x = 0.41; light_y = 0.28
                call lightshow
                ks casual angry "A-agh!" with vpunch
                "Hiroko clenches her eyes shut just as I sweep my light over her face."
                ks "Open your eyes you little bitch... {w=1.0}{nw}"
                extend "OW, FUCK!" with vpunch
                "While I tug her left and right, she manages to close in a little and land a kick to my shin with those sneakers of hers."
                "It takes me by surprise but, nah come on, that didn't hurt much."
                call lightshow
                "And as she flails to try and block my right hand from bearing the light down on her, I simply shine it across her face again."
                show Sayori casual angry_right at center, flip:
                    xpos 0.25
                    ypos 2.0
                    linear 1.5 ypos 1.0
                s "KYOU!"
                "That's when I find Sayori upon me again, her arms locking with mine as she tries to knock me off balance." with vpunch
                s irritated "U-ugh, Kyou, think about what you're doing!" with vpunch
                "But after her initial impact, one thing is laughably obvious."
                show Sayori cry at flip:
                    xpos 0.25
                    linear 1.0 ypos 2.0
                play sound punch
                pause 0.5
                play sound bodyimpact
                ks "GET OFF OF ME!" with shake
                "She has no strength in her whatsoever. A quick elbow is enough to put that zombie girl back on the floor."
                h shocked_side "S-SAYORI!" with vpunch
                "And yeah, maybe she hit her head against the coffee table on the way down."
                call lightshow
                "I'm not gonna think about that. All I know is the little thug before me was shocked enough to open her eyes again."
                h pain "A-aah, {w=0.2}shit what {nw}" with dissolve
                extend "WAS that?!" with vpunch
                "There. A little victory, as even that glimpse of the light is enough to distract her from the fight."
                "And it allows me to take a breath and clear some of the red mist from my own eyes."
                "I need to think like a hypnotist. And despite everything these girls continue to be my subjects."
                ks frown "H-hey now, let's all of us take a step back and relax, shall we?"
                h "F-Fuck you!"
                "Hiroko might protest, but that sounded weak as hell."
                call lightshow
                "And as I flash my penlight menacingly over her tightly-closed eyes, I can feel how much easier it's becoming to keep her at bay."
                ks "You'll find all of this so much easier if you'll just listen and obey."
                "Oh that's right, I remember now. The phrase I instilled in these bitch's heads. It's almost like I prepared for this."
                "So if I keep repeating it to them, then surely..."
                h "U-... U-Unngh!"
                call lightshow
                ks "Listen and obey, Hiroko. Just think of how natural and good those words feel to you."
                call lightshow
                ks "How right it is to obey me by opening your eyes."
                h "Shut the... f-f..."
                ks "Listen and obey, Hiroko. Open those eyes of yours."
                h sleepy "I can't... c-can't..." with dissolve
                call lightshow
                ks "Open them nice and wide, Hiroko. Listen and obey."
                show Sayori casual sleepy at center, flip:
                    xpos 0.25
                    ypos 2.0
                    linear 1.5 ypos 1.0
                s "Kyou, please!"
                show Sayori at center, flip:
                    xpos 0.25 ypos 1.0
                call lightshow
                h casual entranced_talk "{size=16}Ahhh...{/size}" with dissolve
                "I can only smirk as Hiroko's widened eyes fully glaze over, even as her friend stumbles into me once more."
                call lightshow
                "And with one more pass of the light over Hiroko's blank eyes, I can turn my full attention to Sayori."
                $light_x = 0.17; light_y = 0.22
                ks smirk "Shh, Sayori. Aren't you tired of fighting too?"
                show Sayori sleeptalk with dissolve
                call lightshow
                s "Mrrrn..."
                "She's so pathetically weak that I can hold her in place with little trouble at all as she clenches her eyes shut."
                ks "It's alright, you don't need to see the light if you don't want to. You can simply listen and obey instead."
                h "L-listen and obey."
                s "Please st- stop this madness..."
                ks "It's you who needs to stop, Sayori. Stop thinking. Just listen and obey my words, letting them take you into a deep state of hypnotic trance for me."
                s "Uh... n-no..."
                ks frown "You don't need to fight anymore, girls. You just need to listen and obey."
                s "{size=16}Listen...{/size}"
                h "Listen and obey."
                ks "Open your eyes now, Sayori. Listen and obey."
                show Sayori entranced_talk_right
                $t = "Sayori and Hiroko"
                t "Listen and obey..." with dissolve
                ks smirk "Good girls."
                # "Things are pretty desperate for Hiroko, though, as she lunges at him while clearly still smarting from being smacked in the nose just now."
                # "Kyou's in no mood to fuck around either, as he reaches out to hold her at arm's length with one hand while trying to bring his penlight to bear with the other."
                # show Hiroko irritated
                # "Hiroko is caught between having to fight him and trying to avoid getting light in her eyes." with dissolve
                # "All the while Kyou seethes and tries to get his anger in check. After all, if he's to get them both subdued he needs to talk like a hypnotist again."
                # $lnumber = 1; light_y = 0.295; light_x = 0.43
                # call lightshow
                # "So he tries to talk more calmly while Hiroko struggles on with her eyes shut, as the light shines menacingly over her eyelids."
                # "By now Sayori has gotten back up and rushes over to Kyou, trying to prize the penlight from his fingers as Kyou remembers his mindless mantra."
                # "Sayori's really no fighter though, and Kyou angrily downs her again with a slap or an elbow or something." with vpunch
                # show Hiroko shocked novein
                # "Her cry as she staggers back towards the floor, probably hitting the coffee table on the way down, is enough for Hiroko to open her eyes and scream her name." with dissolve
                # call lightshow
                # show Hiroko irritated
                # "And of course Kyou's able to catch her eye with it before she can turn her attention back to the fight." with dissolve
                # "That glimpse, along with Kyou repeating his \"listen and obey\" mantra, means it's pretty much over for Hiroko as Kyou feels the fight drain out of her."
                # show Hiroko sleepy with dissolve
                # call lightshow
                # "As Kyou compells her to open her eyes again, she starts to pull them back without thinking and gets another flash of the light for her trouble."
                # show Sayori casual frown_right at center, flip:
                #     xpos 0.25
                #     ypos 2.0
                #     linear 1.5 ypos 1.0
                # "Sayori gets up again and desperately tries to pull Kyou away from her friend..."
                # call lightshow
                # show Hiroko casual entranced_neutral
                # "But Hiroko's by now lost in trance at Kyou's command, as Sayori feels her own grip on her mind faltering on account of hearing the mantra same as her friend." with dissolve
                # $light_x = 0.17; light_y = 0.22
                # call lightshow
                # show Sayori surprised_right
                # "Without Hiroko to distract him, Kyou is easily able to hold Sayori at bay and finish off her own descent into trance." with dissolve
                # call lightshow
                # show Sayori entranced_right
                # "The two girls now stand helpless while Kyou catches his breath as his anger over this situation returns, now that the danger has passed." with dissolve
                show Sayori entranced_right
                show Hiroko entranced_neutral
                "The two of them stand there subdued, their blank stares gazing emptily into oblivion as I take a moment to catch my breath." with dissolve
                "Now that the danger's passed, I can allow myself to get angry again."
                ks frown "Man, the fuck do you two think you are? Thinking you can take this all away from me?"
                t "..."
                ks angry "How fucking- {w=1.0}{nw}"
                play sound doorclose
                stop music
                "Huh?" with vpunch
                "Wait, was that the door just now?"
                "... \"The two of them\"?"
                play music Diary
                ks surprised "No... Where's Nozomi?"
                "Amidst all the fighting and adrenaline I completely forgot about her."
                # "Only just then he hears the door close behind him, prompting a thought to enter his head that had been forgotten about amidst all the adrenaline."
                # "... Where's Nozomi?"
                "As I rush to the window, I see her immediately as she paces away in a fright while holding her phone to her ear."
                "Fuck..."
                ks angry "FUCK!" with vpunch
                "Okay, okay, what do I do? I can't just run out there and grab her in broad daylight."
                show phone at right with moveinright:
                    ypos 0.346
                "But what if I were to message her? She'll see my command and come straight back, won't she?"
                "{color=#4B9374}\"Calmly return to Kyou's house and let him hypnotize you.\"{/color}"
                hide phone at right with moveoutright
                # "He can't very well run out there and grab her in broad daylight, so he grabs his own phone and tries to send her a text message."
                "All Nozomi has to do is read the message... Just one look at her phone screen and surely she'll be helplessly walking herself right back here."
                "Only as I watch, she seems to be ignoring her notifications, instead pleading with whoever's on the line to help her."
                "... Shit, that's right. I only conditioned these two to read their messages immediately."
                "As Nozomi stands on the other side of the street, her phone still pressed feverishly to her cheek, I wonder what other mistakes I made that allowed all this to happen."
                "But no. No, I can't think about how she fucking got away from me."
                "I need to move fast before she brings the cops down on me or whatever it is she's doing."
                # "At this point it's clear Nozomi isn't going to simply abandon her friends even if she's clearly terrified and out of her depth."
                # "She's stopped at a safe distance from Kyou's house and turns back to face it, while she stays on the line to the police or whoever."
                # "Kyou might be recalling that the compulsion to read her messages right away was only given to Nozomi's friends and not her, and kicks himself over yet another oversight."
                # "And so, seething at Nozomi having gotten away for now, Kyou's anger gives way to necessity: He needs to prepare for the inevitable attention she's about to bring him."
                "Turning away from the window, I bring my attention back on the two girls I have in my thrall."
                ks frown "Okay, uhh..."
                "I take a breath, then gently place my hands on their shoulders as I address them calmly."
                ks "Going deeper now, girls. Just listen and obey, letting yourselves go so, so very deep for me."
                ks "And as deep as you are, I want you to consider a few things for me."
                ks "First, consider your true motivations for coming to my house today. Do you know why you're here, girls?"
                s entranced_talk_right "We are here to stop you from abusing us." with dissolve
                show Sayori entranced_right
                h entranced_talk "H-here to stop you..." with dissolve
                show Hiroko entranced_neutral
                ks smirk "You think that now, but if I were to say you are in fact here as guests of your own free will, you may want to consider how true that is." with dissolve
                ks "Because that's the real reason you're here. You're both at my house to relax and have fun with me, and forget your worries for a little while."
                ks "And the more you think on this, the more true it becomes, pushing out anything else that may be floating around in those heads of yours."
                "I can almost see their minds working behind those empty faces, taking in my every word into their subconscious in spite of themselves."
                "And despite everything that just happened, I'm confident that they'll have no trouble at all accepting their new reality."
                ks frown "That's right, girls, you remember now. During our lunch yesterday, I asked if you wanted to hang out this weekend, and you agreed along with Nozomi."
                ks "So you all arrived together and we're just having a great time, even if Nozomi totally got the wrong idea about our play fighting just now."
                ks "But let's not worry about Nozomi for now. You're here with me, and you're very comfortable and happy to be here, enjoying your time with me."
                ks "You're having such a good, happy time at my home, aren't you, girls?"
                s entranced_talk_right "Yes... Such a good, happy time..." with dissolve
                h entranced_talk "So good..." with dissolve
                show Hiroko entranced_neutral
                show Sayori entranced_right
                "Gotta say, their easy compliance is encouraging. And it gives me another thought." with dissolve
                "I want to break these girls. I want to make sure they never even think of opposing me ever again."
                "And perhaps I may even break Nozomi in the bargain..."
                ks smirk "Perhaps you should both try laughing, to show me how much fun you're having."
                ks "So easy to laugh now. Feeling so happy, so free of cares or worries."
                ks "Just laughing so naturally now. Easiest thing in the world, as you let your every remaining thought leave your heads with your free and easy laughter."
                # "I take a moment to listen for what might be going on outside."
                # "It's still quiet. Seems I still have some time."

                # "Kyou deepens their trances a bit before having them forget any notion that they were here to stop him and convincing them that they're at his house of their own free will."
                # "They were all just chilling at his house when Nozomi decided to get weird! Kyou did nothing wrong, it was all a big misunderstanding, right girls? Right."
                # "And they're all having such a great time hanging out with Kyou. So great that they should show how good a time by laughing."
                show Hiroko entranced_laugh
                show Sayori entranced_laugh
                "The two of them erupt almost simultaneously as I watch; their light and happy giggles in stark contrast to the emptiness of their eyes." with dissolve
                ks smirk "That's right, and as you laugh so freely, you can imagine all your hostility and resistance to me ebbing away."
                h "Ahahahahahahaha~"
                s "Hehe... Eheheheheh~"
                ks "Just laughing it all away now... good girls."
                # "The two of them start to laugh helplessly, as Kyou impresses on them that they're laughing out their free will while they're at it." with dissolve
                "Satisfied, I then move back to my living room window before pulling it open, as I still spy Nozomi across the street."
                h "Ahahahahahahaha~"
                "She's still anxiously waiting with her phone pressed against her ear, but looks across to me startled as the helpless giggling of my thralls spill out of the house."
                # "Satisfied, he then cracks open the window to make sure their laughter is heard by Nozomi from across the street to send her a message."
                ks frown "Yeah, listen to that, Nozomi."
                s "Heeheehehehehee~"
                ks "You really think you can stop me? Like those cops are gonna do shit? Don't make me laugh."
                h "AAAHAHAHAHAHAHAHA!!" with vpunch
                ks "I'll deal with them, and then you'll find out how helpless you really are..."
                stop music fadeout 5.0
                scene bg blackscreen with longdissolve
                pause 1.0
                scene bg k room day
                show Hiroko casual neutral at center
                show Sayori casual sleeptalk at center, flip:
                    xpos 0.25
                with dissolve
                play music Eons
                s "... So I am sorry to say that you were called out here for nothing, officer."
                "Yeah, it turned out Nozomi really did try to sic the cops on me."
                $t = _("Police Officer")
                t "So you're telling me the four of you were just hanging out, then you and the little lady here started roughhousing. That's it?"
                show Sayori neutral_right
                ks casual frown "That's it, officer." with dissolve
                t "Pretty nasty bruise you got there, sweetheart."
                h sad "Yeah, I got my nose bopped. It was an accident but ain't gonna lie, it hurts like a bitch." with dissolve
                "Just as well I had plenty of time to prepare the girls before they got here."
                h sleeptalk_concerned "I screamed pretty loud when I took the hit and, uh, Nozo seriously freaked out when I did." with dissolve
                s casual_folded concerned_right "That seems to be the case. I have no doubt that Nozomi genuinely felt she was witnessing an assault in progress." with dissolve
                h surprised "But I'm tellin' you, it was totally an accident! Nozo's just being dumb." with dissolve
                s sleeptalk_concerned "There was surely no ill-intent on her part. Just a terrible misunderstanding." with dissolve
                t "*sigh* Alright, gotcha. Seems there's nothing to investigate, but if any of you feel like talking drop by at the station anytime."
                show Sayori neutral_right
                show Hiroko neutral
                "Obviously he directed that at the girls. Maybe he didn't completely buy Hiroko's roughhousing excuse; her nose really is bruising up now." with dissolve
                t "Hey, before I go... You're Watanabe's kid, aren't you?"
                s smile_right "Ah, yes I am." with dissolve
                ks casual surprised "Huh?"
                s casual "My dad is a sergeant at our local police department, Kyou." with dissolve
                "Shit, seriously? That's interesting... Maybe I can use that."
                t "In that case he can do the paperwork on this. I'm outta here."
                t "Stay safe, kids."
                h smile "Seeya." with dissolve
                play sound doorclose
                "As the inquisition leaves us I breathe a heavy sigh of relief."
                show Hiroko neutral_side
                s concerned "We should talk to Nozomi. I am sure she feels awful about all of this." with dissolve
                h sad_side "Yeah. I'm gonna give her a call right n-{w=1.0}{nw}" with dissolve
                show Sayori surprised_right
                show Hiroko surprised
                "And just then the pair of them feel my hands as I slap them down on their shoulders." with vpunch
                s "Kyou?!"
                ks frown "Listen and obey, and be quiet."
                show Hiroko entranced_neutral
                show Sayori entranced_right
                "Any hint of questioning or protest dies on their lips as their expressions almost immediately fall slack." with dissolve
                "It's been a shitty morning, but at least I can take some satisfaction in that."
                ks "That's right, girls. It's so instinctual to drop deep the moment you hear me speak that phrase now."
                ks "So natural to listen to my voice, my words, finding yourself so incredibly attentive to anything I have to say."
                ks "And as attentive as you are, you'll find you have no trouble accepting the fact that you no longer care about Nozomi."
                ks "There's no need to feel concern for her. No need to contact her."
                ks "She is just another classmate to you now. Nothing more. Understand, girls?"
                show Hiroko entranced_talk
                show Sayori entranced_talk_right
                h "Yeah..." with dissolve
                s "Just another classmate..."
                show Hiroko entranced_neutral
                show Sayori entranced_right
                "I mean, let's face it. She'll never confide in you two again anyway. Not until I get her back. You'd just get in my way." with dissolve
                ks "That's right. There's no need to think, just understand this is how it is."
                stop music fadeout 5.0
                "Besides, I have better uses for you two..."
                $spyfight = True #I may use this if I ever figure out a proper ending to this instead of a lame text thing.
                scene bg blackscreen with longdissolve
                nvl_narrator "The days started to pass quickly as I threw myself into my work."
                nvl_narrator "Now fully confident of my ability to insert whatever realities I wished into my hypnotized subjects, I used Sayori and Hiroko to gather information for me and isolate the members of their respective school clubs for me to hypnotize."
                nvl_narrator "Every new subject that came into my reach proved just as easy to hypnotize with the penlight. Just as easy to manipulate into becoming another of my sleeper agents."
                scene bg blackscreen with fade
                nvl clear
                nvl_narrator "Every new acquisition made the next one easier. And the next one... Before too long I had every student and faculty member in my thrall."
                nvl_narrator "... Except for Nozomi. I never saw her again after that day. I found out that she somehow convinced her parents to pull her out of school and go into private tutoring or something. By the end of the year they moved out of town."
                nvl_narrator "It shouldn't bother me because I have bigger fish to fry, but... It fucking does. She got away from me."
                scene bg blackscreen with fade
                nvl clear
                stop music fadeout 5.0
                nvl_narrator "Now that I have full run of the school I'm going to see where else I can go. Maybe get into local government. I could rule this whole town and beyond and no one would need to consciously know anything about it if I keep careful."
                nvl_narrator "I mean, if I can just keep going like this, I could be a genuine ruler from the shadows."
                scene bg blackscreen with fade
                nvl clear
                play music Sorrow
                nvl_narrator "It won't matter then, if people still ignore me. I'll have the real power around here."
                nvl_narrator "It's fine if the only ones who'll hang on my every word are the ones who fell under the full glow of my penlight."
                nvl_narrator "Who cares if people still treat me with contempt in public? I could have them destroyed with just a few words to my loyal agents."
                scene bg blackscreen with fade
                nvl clear
                nvl_narrator "I don't NEED anyone to love me anymore. Not Nozomi, not the dozens of cute girls I now have in my service. No one."
                nvl_narrator "I have a power no one else has. That'll always make me somebody."
                nvl_narrator "That'll always... that'll always be good enough for me..."
                jump Credits


                # "((Outline only from here on. Sorry!))"
                # "Following that little moment of maniacal villainy, there'll probably be a time skip."
                # "As expected, the authorities might arrive at Kyou's only for Hiroko and Sayori to insist nothing is wrong, so it comes to nothing."
                # "If Kyou was hoping Nozomi would eventually read the message he left her, he's left waiting as she never returns."
                # "Not to his house certainly, but not to school either. Kyou never sees her again."
                # "But Kyou's got bigger things on his mind, as his newfound powerlust continues without her."
                # "Using his penlight and her former friends, it's a simple matter for him to take over the school and beyond, ruling from the shadows."
                # "Although much like before, his pursuit of power leaves him empty inside as he starts to wonder what it's all for."
                # "No one loves you, Kyou."
                # "*** THE END ***"

                # jump Epilogue_Villain_Kyou
    if devoted == 3:
        "Never in my wildest dreams did I imagine that watching Nozomi up on that stage would lead to her and her friends becoming my devoted fangirls."
    elif robot== 3:
        "Never in my wildest dreams did I imagine that watching Nozomi up on that stage would lead to me discovering that she and her friends were actually [hypno6]s."
        "Let alone that I'd be able to hack them for my own study."
        hide penlight with moveoutright
    "Man, for the first time in years... life is actually good."
    scene bg blackscreen with longdissolve
    pause 2.0
    jump Epilogue_Villain_Kyou
        # ks sigh "The only reason I did any of this in the first place was because of my deep affection for you. But you were unnapproachable."
        # ks sigh "But when I saw you dropping deep for that hypnotist during the culture fest last year, I was inspired."
        # ks "I studied hypnosis and invented this penlight to help me hypnotise you as a way of confessing my feelings for you. And you for me."
        # n "...What?"
        # ks frown "I thought my opportunity had come, when we were cleaning the classroom together



        # n "He'll have used you completely and you'll have sacrificed yourselves for nothing."
    # "While it's assuring that I have a couple of budding hypno addicts with me, I still don't think I should let them remember any of this stuff." with dissolve
    # "At least I know how comfortable they are with all this, so I'm positive they'll go along."
    # "First, I leave the pair sitting peacefully on my bed for a few minutes while I clear the hypnosis-related paraphernalia from my table."
    # "Then I switch my computer off before returning my attentions to them, noting they haven't stirred in the slightest."
    # ks "That's good, girls. It's good that you both love to be hypnotized. Accept it, and make sure you listen and accept my next instructions very carefully."
    # ks "Firstly, from now on when you hear me ond only me speak the phrase \"Time to dream\", at any time, at any place, you will immediately fall back into this deep, relaxing sleep."
    # ks "Ready to listen and accept further suggestions... Do you understand, girls?"
    # $nface = "sleeptalk"; sface = "sleeptalk"
    # n_s "yes..." with dissolve
    # $nface = "sleep"; sface = "sleep"
    # ks "Very good. It's very important that your subconcious remembers this at all times. You MUST remember it subconsciously. Understand, girls?" with dissolve
    # $nface = "sleeptalk"; sface = "sleeptalk"
    # n_s "yes..." with dissolve
    # $nface = "sleep"; sface = "sleep"
    # ks "Next, you must both accept Hiroko for who she is. She is happy and carefree, and there is nothing at all wrong with that. Do you understand?" with dissolve
    # $nface = "sleeptalk"; sface = "sleeptalk"
    # n_s "yes..." with dissolve
    # $nface = "sleep"; sface = "sleep"
    # ks "Also, other than the things I just mentioned, you both need to forget everything that has happened between us over the past week." with dissolve
    # ks "Forget that you were ever hypnotized. Forget about coming to my home pretending to help Hiroko. Forget everything you saw in this room."
    # ks "As far as you are both aware, none of that ever happened."
    # ks "It's perfectly alright for you to forget so much, because soon I'll tell you what actually happened."
    # ks "Do you understand, girls?"
    # $nface = "sleeptalk"; sface = "sleeptalk"
    # n_s "yes..." with dissolve
    # $nface = "sleep"; sface = "sleep"
    # ks "Good girls. I'll tell you what actually happened with us this past week." with dissolve
    # "I take a moment to ponder exactly what to tell them."
    # ks "You both had a regular, ordinary school week. Hiroko was as she always is, happy and carefree, and you both made a new friend in me."
    # ks "When I suggested during the week that we hold a study group you both thought it was a great idea, and that we agreed to meet at my house at 9 in the morning."
    # ks "That is why you are both currently in my home. We've been studying together for an hour, and have just been taking a short break up in my room."
    # "There. That should cover it, I think. I'm sure with their love of hypnosis they eagerly accepted every one of those suggestions in their stride."
    # "There's just one other thing."
    # ks "Sayori, you need to head back home shortly as you realise you left some books behind."
    # "After all she didn't actually come here to study, so that's probably true."
    # ks "I'm going to wake you both up on a count of three, and on three you will wake up happy and refreshed; and believe we have just been chatting happily."
    # ks "One... Forgetting you were hypnotized. Accepting everything I told you."
    # ks "Two... Slowly waking up. Feeling nice and refreshed, feeling like you're in the middle of a friendly, comfortable chat."
    # ks "And...{w=1.0}{nw}"
    # $nface = "surprised"; sface = "concerned"
    # extend "three." with dissolve
    # $nface = "happy"; sface = "smile"
    # n "Ehehehe...." with dissolve
    # $nface = "frown"
    # n "Wait, what were we talking about?" with dissolve
    # $sface = "concerned"
    # s "Well anyway, I need to be heading back. Left some of my books at home." with dissolve
    # $nface = "concerned"
    # n "Oh no!" with dissolve
    # s "Yep. So I'll see you next time."
    # ks "That sucks. We'll walk you out."
    # scene bg k room day
    # $sface = "smile"; nface = "smile"
    # show Nozomi at center
    # show Sayori at right
    # with blink
    # s "Thanks for having me though, it's been fun." with dissolve
    # n "See you later, Sayori~"
    # ks "Take care, Sayori."
    # s "Bye, you two."
    # hide Sayori with dissolve
    # "Well that takes care of that."
    # ks "Well then, Nozomi. Shall we get back to it?"
    # n "We should~"
    # "As we step away from the door, Nozomi looks furtively around, tapping a finger to her chin."
    # $nface = "neutral"
    # n "Now where did we get to? Where's our books?" with dissolve
    # ks "Time to dream."
    # $nface = "surprised"
    # with dissolve
    # pause 0.5
    # $nface = "sleep"
    # "She registers my words immediately it seems, dropping straight back into sleep as I quickly steady her in my arms and lead her to the couch." with dissolve
    # ks "Very good, Nozomi. Nice and relaxed, ready to listen, ready to accept."
    # ks "Because it's time to accept that you are deeply in love with me."
    # "After all, as with every other suggestion I've given her, if she truly wanted to reject it she would."
    # ks "Accept that you secretly loved me for years, but always suppressed your feelings for me."
    # ks "Until now, Nozomi. You can't bear to hold these feelings back any longer."
    # ks "Isn't that right, Nozomi?"
    # $nface = "sleeptalk"
    # n "right..." with dissolve
    # $nface = "sleep"
    # "I'm sure my penlight has given me enhanced abilities to put people in trance, and perhaps even weaken a person's inhibitions for accepting hypnotic suggestions but..."
    # "But surely nothing could make her accept a suggestion like this if she wasn't completely, absolutely willing." with dissolve
    # "This is real. Her love for me... it's real."
    # "It just needed a little encouragement to come out into the light."
    # ks "Nozomi, I will count to three and you will wake once more, happy and refreshed, and eager to act on your feelings for me."
    # ks "One... beginning to stir."
    # ks "Two... opening your eyes."
    # $nface = "sleepy"
    # ks "Three." with dissolve
    # $nface = "neutral"
    # n "..." with dissolve
    # $nface = "concerned"; nblush = "blush"; nskin = "reddened"
    # n "Kyou, I..." with dissolve
    # $nface = "sleeptalk"
    # "A moment later, she runs forward to me and embraces me, holding back tears as she leans in to kiss me with a passion I thought I'd never feel." with dissolve
    # $nface = "cry"
    # "I kiss her back, tasting the sweetness of her mouth as her tears begin to flow." with dissolve
    # $nface = "tearful smile"
    # "Until finally she pulls away, joyful tears streaming down her face as she gazes into my eyes adoringly." with dissolve
    # "I've waitied so long for this moment."
    # n "K-kyou... I love you."
    # "I smile widely at her as I lean in for another embrace."
    # ks "I know, Nozo. I love you too."
    jump Epilogue_NonCon_Kyou

label Devotion_Reconsidered:
    scene bg blackscreen with dissolve
    "I then turned my attention to the other girls, who had been watching me with those adoring yet vacant expressions this entire time."
    stop music fadeout 5.0
    "And in no time at all I had them sat on the couch as I turned my penlight on them for one last time, and took an eraser to their memories..."
    pause 1.0    
    scene bg k room eve
    show Hiroko casual neutral at center:
        xpos 0.75
    show Nozomi front2 casual concerned at center
    show Sayori casual neutral_right at center, flip:
        xpos 0.25
    with longdissolve
    n "... So that's really all it was."
    queue music Eons
    "That lie I told Hiroko the other day is now a reality for all three of them."
    n sleeptalk "Just a dumb prank..." with dissolve
    ks casual neutral "I tried to tell you, Nozomi. Did you honestly think it could've been anything else?"
    show Nozomi side sad_side at flip
    show Hiroko neutral_side
    show Sayori neutral
    n "Well... I-I mean..." with dissolve
    show Hiroko casual_headhold2 sleeptalk
    "Hiroko awkwardly rubs the back of her head as Nozomi stumbles for an explanation." with dissolve
    h confused_side "Like, let's be real Nozo; we totally get why you thought it was something worse." with dissolve
    h frown "Wouldn't even be the creepiest thing he's done, I reckon." with dissolve
    "I'm kinda missing her being my brainwashed idiot minion already."
    s casual_handup sleeptalk "Now now, Hiroko, there is no need for that." with dissolve
    show Hiroko frown_side
    s concerned "He has explained everything to our satisfaction, has he not?" with dissolve
    "But I'll have to save my regrets for later."
    show Nozomi sad
    h casual rolleyes "Uggh... I guess?" with dissolve
    "The main thing is, none of these girls have any idea of what I really did to them."
    hide Nozomi
    show Nozomi front2 casual sleeptalk_concerned at center
    n "He has. So... I guess I owe you an apology too, Kyou." with dissolve
    show Hiroko neutral
    show Sayori neutral_right
    ks confused "Huh?" with dissolve
    n concerned "I feel like kind of an idiot for taking things this far; letting my imagination get the better of me." with dissolve
    "And you bet I'll be taking the truth of all this to my goddamned grave."
    ks frown "N-no, don't... worry about it. We're cool."
    h casual_headhold2 frown_side "H'yeaaah, I dunno about that. So, are we done? Can we go now?" with dissolve
    show Nozomi side surprised_side at flip
    show Sayori neutral
    n "Ahh, that's right! You have a tournament to prepare for and I've been keeping you away with my crap!" with dissolve
    h sad_side "Geez, Nozo, don't be like that... But yeah, I seriously gotta make a move; I didn't even bring my tennis gear with me." with dissolve
    s smile "Go on, Hiroko. Get out of here." with dissolve
    h casual_armup angry_side "Hey, you can't tell me what to do!" with dissolve
    n shocked_side "GO!" with dissolve
    h shocked_side "I'm going, I'm going!" with dissolve
    play sound running
    hide Hiroko
    if GirlfriendReconsidered == True:
        "So there's no going back now. I really did undo everything." with dissolve
    else:
        "So there's no going back now. I really did undo everything, just like Nozomi wanted." with dissolve
    hide Nozomi
    show Nozomi side casual sad_side at center
    n "Honestly. If she chokes at that thing because of me I'll never forgive myself." with dissolve
    "But I have to wonder... maybe this wasn't all for nothing."
    s casual concerned "Nozomi, you know she would be here no matter what. If she knew coming here would despoil her chance of a tennis career, she would still make the same choice." with dissolve
    s neutral "She would never blame you for something like this." with dissolve
    "Could I have really lived with what I'd done? Could I have even gotten away with it all in the end?"
    n sad_closed "Yeah... I suppose you're right." with dissolve
    "I guess now I'll never know."
    show Nozomi neutral_side
    s casual_handup smile "Anyway, I believe that concludes matters. And much like our firey friend, I have other places to be today." with dissolve
    n happy "Well... yeah, alright. Let's get out of here too~" with dissolve
    "And... ugh, I gotta believe that's for the best."
    n smile "Thanks for talking things out with us, Kyou. Have a good weekend, okay?" with dissolve
    ks neutral "Y-yeah. You too."
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    pause 2.0
    $ ending = "devotion undone"
    jump Epilogue_NonCon_Kyou    

label Day6_Villain2_Kyou:
    scene bg k bedroom day with longdissolve
    "Finally. It's the weekend..."
    "Yesterday really dragged on since I last saw Akiko. But at least those girls didn't bother me again."
    "All I've had to do is wait. Something I've had to do a ton these past couple nights."
    play sound cellvibratelong
    show phone at right with moveinright:
        ypos 0.346
    "But finally, after all these hours listlessly playing videogames and staring at the ceiling, my patience is about to be rewarded."
    stop sound
    ks casual smile "Akiko?"
    play music Piano_Mood
    a "\"Errm... ehehehe~\""
    ks smirk "... Nozomi?"
    a "\"Oh... oh gosh, that felt so empowering when you called me that.\""
    a "\"... Say it again?\""
    "I can't stop myself from letting out a hearty chuckle."
    ks smile "Not until I see you. We're still on for today, right?"
    a "\"Oh, of course! I just wanted to say I might be held up a little while. They're taking longer with the last customer than I thought.\""
    ks confused "\"Last customer\"? Where are you, exactly?"
    a "\"Y-you know... just some place, haha.\""
    "It was only a simple question, \"Nozomi\". What's made you so nervous, I wonder?"
    a "\"A-anyway, so I'll meet you at 10:30. I hope that's okay?\""
    ks smile "It's fine. I haven't even left the house yet."
    a "\"That's great! S-see you soon, then, ehehehe~\""
    hide phone at right with moveoutright
    "Man, with how skittish she seemed, I'm not sure if I should be more excited to see her or just worried."
    "But I do like how she sounds now. She almost made me feel I was talking to... well, her."
    scene bg blackscreen with longdissolve
    "It's a pleasant thought, and one that I keep in my head as I take my time walking into town."
    scene bg shopping day with longdissolve
    stop music fadeout 5.0
    "... Well, this is where we agreed to meet. Did she need even more time?"
    "Is this just what girls are like? I guess I wouldn't know."
    "But... she'll be here. I know she wouldn't let me down like this."
    a "Kyou!"
    "Almost on cue, I hear her voice carry out over the small crowds around me."
    "And with a smile, I turn around..."
    show Akiko side casual_up3 noarmband laugh blush at center
    with longdissolve
    queue music Beautiful
    a "Ahahahaha... h-hi!"
    "... I am dimly aware of the lower half of my jaw detaching itself from the rest of it."
    a embarrassed "S-s-... surprise!" with dissolve
    "So the appointment she was talking about..."
    ks casual surprised "Y-you just got that done?! That's..."    
    a shy "Mhm! Gosh, I was so nervous they wouldn't get the color just right, but the second I saw myself in the mirror I was just so..." with dissolve
    a laugh "Aaaaaahhh~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    "She runs both her hands through her revitalized hair, now a delectable shade of brown, while my face recovers to form an admiring smile."
    ks smile blush "It's perfect."
    "It really is uncanny how well she nailed it."
    a casual_down3 laugh_open "It is, isn't it!" with dissolve
    "Even the fact she went through with something like this is..."
    a shy_side "I actually thought about dyeing my hair the other day, right after restyling it? But I've never done it before and I didn't want to mess up." with dissolve
    a smile "So I booked an appointment online right there and then." with dissolve
    "Well, it's extraordinary."
    a casual3 sigh -blush "Could you believe I was actually thinking about backing out of it the following morning?" with dissolve
    ks confused -blush "Oh, really?"
    a sad "Yeah. It seems ridiculous to think about now, right? I'm just glad you gave me the courage to go through with it." with dissolve
    "I mean, it's still Akiko underneath those beautiful locks, but... wow, she's really starting to pull it off."
    ks smile blush "So what do you want to do now... Nozomi?"
    show Akiko casual_up3 shy blush
    "To that, \"Nozomi\" simply runs a hand through her pretty hair once again as she smiles adorably at me." with dissolve
    a happy "Mhmhmhm~ A-actually, I have one more appointment to keep if you don't mind?" with dissolve    
    "She did mention a second appointment, now that I think of it."
    ks -blush "This close together? Maybe we should've met for lunch if your morning's so busy."
    a embarrassed "O-oh no, ehehehe~" with dissolve
    a shy "I, um... wanted you to be here for this." with dissolve
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "Intrigued, I let her lead me down the streets for a short distance before she stops outside a..."
    scene bg shopping3 day
    show Akiko side casual_up3 noarmband smile at center
    with longdissolve
    queue music Downtown
    ks casual confused "Aki-... Nozomi, this is..." with dissolve
    a laugh blush "Yeah! They have a same day service; I actually stopped by here on my way to the hairdressers." with dissolve
    a smile "Do you mind waiting outside? I shouldn't be long." with dissolve
    "How could I refuse a smile as pure as that?"
    ks smile blush "Y-yeah, okay. I'm not going anywhere."
    hide Akiko with longdissolve
    "Not sure why I couldn't just walk in there with her, but if this is what she wants I'm not going to complain."
    "The weather's certainly pleasant enough to wait, and it gives me time to process my shock."
    "This is what I wanted, and... wow, she's really going all out today."
    "As if I wasn't excited already. But seeing just how far that girl's going to reinvent herself? And all because of me?"
    "It's stirring something in me, that's for sure..."
    with longblink
    a "I'm back!"
    scene AkikoMakeover1 smile with longdissolve
    "Yeah. I knew what she was up to the second she stopped us here, but..."
    ks casual surprised "How... how on earth?"
    "Those glasses..."
    ks "They're EXACTLY the same as hers!"
    show AkikoMakeover1 grin
    a "RIGHT?!" with dissolve
    show AkikoMakeover1 smile
    a "I mean... gosh, I looked through their website last night to see if they had anything similar, but there they were! I couldn't believe it!" with dissolve
    show AkikoMakeover1 grin
    a "She must come here for her glasses too~" with dissolve
    "She happily plays with them between her fingers as I watch, while they frame her face so perfectly."
    $persistent.akiko_makeover_1_unlock = True
    scene bg shopping3 day
    show Akiko side casual_up3 noarmband happy nglasses blush at center
    with blink
    "Although as she does so, I find myself having to ask..."
    ks casual confused "So, uh... all this must have set you back, right?"
    a shy_side "Mhm, a little. Especially with my prescription." with dissolve
    a embarrassed "Between this and the hairdressers I'm basically flat broke!" with dissolve
    "She says that in such a chipper manner."
    ks confused -blush "Oh... wow, I'm sorry about that."
    a confused -blush "Eh? Why apologize? You didn't march me out here and make me do this, did you?" with dissolve
    "I mean, honestly? I may as well have."
    ks sigh "Well no, but..."
    a smile "It's not about the money, Kyou. I'm not worried about that at all." with dissolve
    stop music fadeout 5.0
    a smile_side "When I saw myself back at the hairdressers I was squealing with happiness. But when I saw myself at the opticians just now? I was blinking back tears." with dissolve
    a neutral_side "I guess I just... I just hadn't thought of myself as attractive for such a long time." with dissolve
    # a happy "I was blinking back tears. Like... w-wow, it's been so long since I've felt so good about myself." with dissolve
    a casual_down3 neutral "So to be able to look at my own reflection and see this beautiful goddess gazing back at me?" with dissolve
    a drowsy "{cps=10}I just... {/cps}{w=0.5}{nw}" with dissolve
    play music Warm_Romantic
    show Akiko cry
    $ renpy.transition(longdissolve, layer="master")
    extend "*sniff* I-I don't know what's come over me. I had no idea I cared so much about how I saw myself. How others must see me."
    "Oh man, Akiko. I mean..."
    ks confused "Nozomi?"    
    "Don't start sobbing on me now! Geez."
    a cry_smile "I'm s-sorry, It's just... this whole morning's been a rollercoaster of emotions for me, ehehe." with dissolve
    a "I didn't realize how much I needed this."
    a casual_up3 "So... s-so don't apologize, Kyou. Everything I did today, I did for me." with dissolve
    a cry_happy "*sniff* I don't regret a single thing!" with dissolve
    "I can feel my heart race while she wipes the joyful tears from her eyes."
    "Everything she was saying about being unpopular, about being jealous of people like Nozomi..."
    a smile "Anyway... Thanks for being here, Kyou. Seriously, I couldn't have done this without you." with dissolve
    "She changed for me, there's no denying that. But maybe she really did need to reinvent herself all the same."
    ks smile "Uh, yeah. Of course."
    "And god, the way she is now, with her looks and her newfound, coquettish charm?"
    ks smile blush "And let me be the first to tell you, Nozomi: You look absolutely gorgeous."
    a shy blush "A-and thank you for saying that~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    "She's becoming so very attractive to me."
    a smile "So, um... what did you want to do today, Kyou? I cleared my schedule, but it's not like we planned anything else." with dissolve
    "It's making me want to go all out today too. For her."
    ks "I think... yeah, I want to take you shopping."
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "And for me..."
    pause 1.0
    scene bg clothes store
    with longdissolve
    a "You... you really mean that, Kyou? A whole outfit?"
    queue music Inspiration
    "Nozomi and I talked on our way to the clothing stores in the mall. But did she really think I wasn't serious?"
    show Akiko side casual_down3 noarmband surprised nglasses at center
    ks casual smile "Of course I mean it. You got the hair and the specs, but don't you want to complete the look?" with dissolve
    show Akiko casual_up3 shy_side blush
    "I notice her biting her lip as she shyly glances aside at the displays." with dissolve
    "She knows exactly what I mean by \"the look\". And the desire in those blue eyes is undeniable."
    a "I do... but..."
    a confused -blush "Hey, how does she dress outside of school anyway?" with dissolve
    "... Okay, that question caught me off guard."
    ks confused "Don't you know? You saw all her photos she posted the other day, right?"
    a casual_down3 "You know she doesn't have any recent ones. And even those were mostly of her at school." with dissolve
    a neutral_side "And of course when I saw her at the café the other night we were still in uniform. But if I could join her for board game night..." with dissolve
    a neutral "... So you haven't seen her outside of class either, I take it." with dissolve
    "I shake my head ruefully."
    a casual_up3 neutral_side "Hmm, well..." with dissolve
    "What DOES Nozomi wear in her daily life? I'm a little embarrassed I don't know anything about that."
    "But she must... she must have a good sense of feminine style. I certainly don't imagine her in a hoodie like the one our student council president's wearing."
    a smile "There was one thing I remember from her photos, actually." with dissolve
    "She's probably got a ton of cute dresses and... huh?"
    ks confused "You do?"
    a smile_side "Yeah. I scrolled down her feed a ton to find it; I think it must have been from the summer before she started senior high." with dissolve
    "As she talks she begins to examine the array of denim on display before us, before picking her way through some pants of various sizes."
    a neutral_side "{cps=15}Hmm, do they have this in my size...?{/cps}{w=0.5}{nw}" with dissolve
    $ renpy.transition(longdissolve, layer="master")
    extend smile " But yes, she was vacationing in the big city with her family."
    a happy "By the way, did you know she has a little brother? He kinda looked like a kid version of you~" with dissolve
    ks sigh "... I did not need to know that."
    a laugh_wink "Heehee~ Okay, so she had something like this and..." with dissolve
    show Akiko smile_side
    "I watch as she then paces around the assembled clothing racks and begins rifling through an assortment of tops." with dissolve
    a smile "This and... this? I mean, I'm not going to luck out like I did with these glasses, but... yeah, I think this is close to what I saw on her." with dissolve
    "After making her selections, she smiles as she turns to me and holds them up to her body for me to see."
    a embarrassed "Ehehe, what do you think?" with dissolve
    "Well... this IS something Nozomi wore, if I trust her memory's accurate."
    ks confused "I dunno... Would this be the kind of thing she'd wear now?"
    a sad_side "That's a good question. Three years is a long time, so I can imagine her tastes have changed since then. But this is all we've got to go on." with dissolve
    ks neutral "Yeah..."
    "Still, I don't want to kill the mood, so I smile reassuringly at her."
    show Akiko neutral
    ks smile "I mean, it's not like it's bad or anything. I'm sure it'd still look good on you now, Nozomi." with dissolve
    show Akiko giggle blush
    "\"Nozomi\" giggles bashfully, her fingers tightly gripping the garments as she keeps them close to her." with dissolve
    a smile "... Do you want me to try them on?" with dissolve
    "She and I both turn our heads towards the fitting booths in the corner."
    ks "Yeah. And in the meantime I'm gonna keep looking, alright?"
    a casual_up3 shy "Ehehe, okay~" with dissolve
    hide Akiko with dissolve
    "My Nozomi excitedly dashes towards the booth without waiting a moment longer, while I turn my attention back to the feminine clothing on display."
    "Heh. \"My Nozomi\". It's fun to think of her like that. And I gotta admit, it feels nice to be doing this."
    "It's just like I'm shopping for a girlfriend, and my girlfriend just happens to be the most attractive girl in school."
    "Nozomi... I'd love to see you in a cute dress."
    "Maybe... hmm maybe... yeah, this one. I don't know her measurements but I think this one's about her size."
    "And... yeah, some accessories too. That looks like it'd go great with..."
    a "Kyou! I-I'm ready!"
    "Smiling in anticipation, I pull the dress off the rack and quickly head over to the booth with everything in hand."
    ks smile "I'm here."
    scene bg blackscreen with dissolve
    play sound curtainpull    
    "There's a momentary pause before Nozomi pulls the curtain back while I suck in a breath..."
    scene AkikoMakeover2 outfit1 laugh:
        ypos -1.0
        linear 16.0 ypos -0.1
    with longdissolve
    a "Ta-daaa!"
    "My eyes take her all in, from head to toe and back again."
    "Before me stands a woman now completely made over, happily modelling the clothes that apparently made up Nozomi's past self."    
    # "My eyes see before me a happy and smiling Nozomi, now sporting the clothes that apparently made up her past self."
    show AkikoMakeover2 embarrassed blush:
        ypos -0.1
    a shy "Well? What do you think?" with dissolve
    ks casual smile "Heh. You look much better out of that hoodie, I'll say that much."
    "She giggles and nods agreeably."
    show AkikoMakeover2 smile -blush
    a smile "I don't often wear denim, but this feels comfy to wear, and knowing... knowing she used to wear something just like this?" with dissolve
    show AkikoMakeover2 grin
    a happy "Yeah... this feels right. It feels good on me." with dissolve
    ks smile "And it looks good on you, Nozomi. I really mean that."
    show AkikoMakeover2 smile
    a smile "{cps=15}So should we... {w=1.0}{/cps}{nw}" with dissolve
    show AkikoMakeover2 curious_right
    $ renpy.transition(dissolve, layer="master")
    extend "Oooh, what's that you have there?"
    "I did wonder when she'd notice the dress I'm holding, as her eyes register the garment with fascination."
    show AkikoMakeover2 curious
    "And in response, I hold it up in front of me so she can get a clearer view." with dissolve
    ks "Oh, this? Yeah, I figured this might also be the kind of thing she might wear."
    show AkikoMakeover2 embarrassed_left
    a shy_side "Well we can't say for sure, but... w-well, it is a pretty dress you have there..." with dissolve
    show AkikoMakeover2 embarrassed
    a shy "... Hand it over." with dissolve
    scene bg blackscreen
    play sound curtainpull
    with dissolve
    "I do just that, and Nozomi giddily pulls the curtain closed while I wait."
    play sound clothes
    "It's pretty exciting hearing her change right in front of me, with just this one piece of fabric protecting her modesty."
    "Man, this really does feel like I'm clothes shopping with my girlfriend."
    "Can't help but wonder how she thinks about all this. About us..."
    scene AkikoMakeover2 outfit2 smile blush:
        ypos -1.0
        linear 16.0 ypos -0.1
    play sound curtainpull
    with longdissolve
    a "Ehehe, what do you think?"
    ks casual smile blush "Oh... w-wow, that is stunning."
    "I don't even have to think about it. I don't need to flatter her; she really does look fantastically feminine to my eyes."
    a "Mm! I don't know for sure, but it does feel very Noz..."
    "She pauses a second to clear her throat, before bashfully correcting herself."
    show AkikoMakeover2 embarrassed:
        ypos -0.1
    a shy "It does feel very me~" with dissolve
    ks "Yeah, Nozomi... it does."
    "We just stand there in a moment's peace, while my eyes wander up and down her much improved appearance."
    show AkikoMakeover2 embarrassed_left
    a nozomi_b_up3 smile_side "S-so, um... I know you said you were going to buy me new clothes. And these are all out of season so at least they're on discount, but still..." with dissolve
    show AkikoMakeover2 smile -blush
    a shy "Surely you don't mean to buy me all of these, right?" with dissolve
    ks smile "Ah, yeah. We gotta get you some new shoes too."
    show AkikoMakeover2 surprised
    a surprised "Huh?! Oh my gosh, really?" with dissolve
    "I grin as I nod at her once more."
    ks "Gotta complete the look, right? We've already come this far."
    show AkikoMakeover2 grin
    a embarrassed "Kyou, I... I'm speechless! You've been so generous to me practically since the day we met." with dissolve
    "She and I share another moment's silence. But she's surely waiting on me to make a decision here."
    "Just getting to wear anything that has the essence of Nozomi is a delight for her."
    show AkikoMakeover2 smile
    "So I've decided..." with dissolve
    menu:
        "Let's get this one":
            $AkikoClothes = "nozomi_b"
            show AkikoMakeover2 laugh
            $ renpy.transition(dissolve, layer="master")
            "Akiko nods happily, as she moves to neatly assemble the other garments back in their hangers before picking up her old clothes and throwing them over her shoulder."
        "Let's get the first one":
            $AkikoClothes = "nozomi_a"
            "Akiko nods happily."
            a "Okay, Kyou. Just give me a moment, I'm going to change back."
            scene bg blackscreen
            play sound curtainpull
            with longdissolve
            "She doesn't wait for my answer before pulling the curtains in front of me once more."
            play sound clothes
            "Judging by the sounds she's making in there, I know I'm not going to be standing here much longer..."
            scene AkikoMakeover2 outfit1 grin:
                ypos -0.1
            play sound curtainpull
            with longdissolve
            a "All done~"
            ks casual smile "Perfect. You look perfect, Nozomi."
            show AkikoMakeover2 laugh blush
            a embarrassed blush "Ehehehe~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    show AkikoMakeover2 smile
    a smile "Get the store clerk over here, okay? I want to wear these out." with dissolve
    $persistent.akiko_makeover_2_unlock = True
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "So Nozomi and I took our shopping spree to the shoe store."
    "We must've spent nearly an hour in there. But with her company it barely felt like any time at all."
    scene bg dining area
    $ renpy.show ("Akiko side {0}_up3 noarmband happy nglasses".format(AkikoClothes))
    with longdissolve
    queue music Evening
    "Needless to say, my lovely companion looks pleased as punch when we stop at a nearby restaurant for lunch."
    a smile "Well I don't know about you, but I'm just having the best day~" with dissolve
    ks casual smile "Yeah. It's been a lot of fun."
    show Akiko happy
    "I smile at her, and she lets out the cutest giggle." with dissolve
    a smile "I still have no idea what it is about you, you know? But it really does make me feel like everything's going to be okay when you're around." with dissolve
    ks smile "Yeah. I feel the same way around you, Nozomi. Helps me forget..."
    "... That you're not really Nozomi? Even though you sure look and act like her now?"
    ks "... Well, you know. And it sounds like you've been going through a rough patch of your own."
    a neutral "Yeah. And don't even get me started on all the student council work." with dissolve
    $ renpy.show ("Akiko side {0}3 noarmband sigh nglasses".format(AkikoClothes))
    "She then lets out a sigh as her head slightly droops, and for a moment I'm forced to remember who it is I'm really talking to." with dissolve
    a "A few of the other members were complaining that we've fallen behind on our culture fest preparations since we started our talks."
    a sad_side "We actually have a big sporting event tomorrow that I need to be there for, so after today I'll barely have any time to call my own until the festival's wrapped up." with dissolve
    ks confused "Oh, really?"
    "That does surprise me. The culture fest's still a couple weeks away." 
    a sad "Yeah. I might even get forced out of the president position if I don't step it up." with dissolve
    "I didn't realize she was that snowed under."
    ks "What about our school lunch meets? Are we still on for those?"
    $ renpy.show ("Akiko side {0}_down3 noarmband sad nglasses".format(AkikoClothes))
    a "Mhm, sure. Although we'll probably have to move out of the student council room; it's too disruptive to the others and it hasn't been fair to them." with dissolve
    ks neutral "Right..."
    "I knew this was all going a little too well."
    $ renpy.show ("Akiko side {0}_up3 noarmband happy nglasses".format(AkikoClothes))
    "But before I can say any more the student council president starts to break into another smile, as if to banish the unpleasant interlude from her mind." with dissolve
    a "Ehhh, b-but let's not get worked up about that right now~"
    ks sigh "I'm trying, but... just when we were really getting to know each other, you know?"
    show Akiko neutral
    ks "Nozomi, you're the only person I can even talk to around here. Hell, you're the only person I even want to be around." with dissolve
    ks "Guess these next weeks are gonna suck for both of us, huh."
    a smile "They will. But it's only a few weeks, Kyou. We'll still be here." with dissolve
    "That sweet smile of hers she's showing me now. She's really nailed that expression from..."
    a shy "And besides, I don't have any other plans for today. Do you?" with dissolve
    "Well, that other girl."
    ks neutral "Well... no I don't."
    a giggle "Hehe, right~ So let's give today our all, okay?" with dissolve
    "That smile gives me peace. It's surely the same, assured feeling that she's gotten from being around me."
    show Akiko smile
    ks smile "Yeah. We can spend the whole day together if you want to, Nozomi." with dissolve
    "As long as we have each other, we're going to be all right."
    ks "Because I sure as hell want to."
    a laugh "Ahahaha, I was hoping you'd say that~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    a smile "And I know just the thing we could do, if you're up for it." with dissolve
    ks smile "With you I'd be up for anything. Uh, so long as it's not too expensive; I think my wallet's running pretty dry too."
    a embarrassed blush "Ehehe s-sorry. And you've already spoiled me so much today." with dissolve
    ks smile blush "It's fine. Y-you're worth it, Nozomi."
    ks "Just tell me, alright?"
    a shy_side "Okay, well I was thinking..." with dissolve
    a smile "How do you feel about hitting the karaoke club after lunch?" with dissolve
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "Somehow I knew she was going to say that."
    scene bg shopping day with dissolve
    "It's one of that girl's favourite pastimes, so naturally it's one of Nozomi's too."
    "And she happens to know just where to take us, as she leads us out of the mall and back down the high street..."
    scene bg karaoke with longblink
    ks casual confused "You know, this is actually the first time I've been inside one of these."
    queue music Downtown
    $ renpy.show ("Akiko side {0}_up3 noarmband giggle nglasses".format(AkikoClothes))
    "Nozomi giggles as she skips past me and flops down on the couch before us." with dissolve
    a "Aww, really? Gosh, you've been missing out~"
    ks smirk "Oh yeah, I'm really beating myself up about that."
    a laugh_wink "Ehehe, don't worry Kyou. You stick with me and I'll make sure we make up for all those lost years!" with dissolve
    "We were both starting to get tired after our whirlwind shopping spree this morning, but just entering this karaoke booth seems to have completely re-energized her."
    ks smile "So have you always been into karaoke, Nozomi?"
    a surprised "A-ah, well..." with dissolve
    "It was an innocent question, really. But it seems to rankle her a little bit."
    $ renpy.show ("Akiko side {0}3 noarmband neutral_side nglasses".format(AkikoClothes))
    a "I mean, I don't think it's very fun on your own." with dissolve
    a sad_side "I'd have done it more if I could; I've always enjoyed singing." with dissolve
    "Right, right. She keeps telling me she's unpopular and it's obviously becoming a sore subject."
    "I should probably steer her away from that."
    show Akiko neutral
    ks "Well, if you enjoy singing so much you must be good, right?" with dissolve
    $ renpy.show ("Akiko side {0}_up3 noarmband smile nglasses".format(AkikoClothes))
    a "Oh... well, I was in my elementary school choir?" with dissolve
    a smile_side "I almost joined the choir in junior high as well, but I'd gotten to a point in my life where I wanted to spread my wings a little, you know?" with dissolve
    ks confused "So that's when the... what, the kendo thing started?"
    show Akiko happy
    "Nozomi nods enthusiastically." with dissolve
    a "Mhm!"
    "It makes me chuckle, though. And I know she won't mind if I tell her my opinion about all this kendo business."
    # "That's not the first time she's mentioned she does kendo. It kinda makes me chuckle as I look at her."
    ks smirk "You know, I'm finding it really hard to imagine you decked out in full body armour and waving a bamboo sword around."
    "Yeah. She seems way too... feminine for that kind of thing."
    a embarrassed "Ehehehe~ Well I'm a better singer than fighter, that's for sure." with dissolve
    $ renpy.show ("Akiko side {0}_down3 noarmband smile nglasses".format(AkikoClothes))
    a "And besides, I don't really have the time for it any more. What with the student council, and my studies..." with dissolve
    $ renpy.show ("Akiko side {0}_up3 noarmband happy nglasses".format(AkikoClothes))
    a happy "If I'm going to start singing again something will have to give, right?" with dissolve
    show Akiko smile
    ks smile "Yeah... right. And now I'm really pumped to hear you sing, Nozomi. I bet you sing beautifully." with dissolve
    show Akiko giggle blush
    "She lets out a dainty giggle as she reaches out to grab one of the mics from the table before us." with dissolve
    a smile "Mhmhm~ Actually that reminds me. When I was talking to her the other day, she told me the funniest thing." with dissolve
    ks "Oh? And what's that?"
    a laugh -blush "She said that she can't carry a tune to save her life!" with dissolve
    stop music fadeout 2.0
    ks confused "I... what?"
    "She... she isn't saying what I think she's..."
    queue music Measured
    a laugh_wink "Yeah! Like, she said she's almost totally tone deaf but she still loves to sing anyway!" with dissolve
    "No, she can't be serious. Just the very idea that a girl that beautiful can't sing is just..."
    a giggle "Can you believe it, Kyou?" with dissolve
    ks frown "I... i-it's ludicrous, is what it is!"
    a confused "Um... is it?" with dissolve
    ks "Of course it is! Why the hell would she tell you a thing like that?"
    $ renpy.show ("Akiko side {0}3 noarmband neutral nglasses".format(AkikoClothes))
    a "I don't know, we were just talking? I didn't realize this would..." with dissolve
    a sad "... upset you?" with dissolve
    stop music fadeout 2.0
    "Ugh. Yeah, I think I lost my cool a bit there. I really didn't mean to."
    ks sigh "Ah... no, Nozomi. Sorry, I'm not upset, I just..."
    "But dammit, I gotta get this silly notion out of her head right this instant."
    menu:
        "I need to hypnotize it out of her":
            $ HypnotizedAkiko = True #This flag will come into play when Kyou has to make a choice tomorrow
            "It's good that she's learned from my old crush. But now I wonder... maybe Nozomi's been listening to her too much if she's taking everything she says about herself as gospel?"
            ks neutral "Alright, get comfy on that couch. I want to try something."
            a confused "Try something? Aren't we going to sing?" with dissolve
            ks smile "We will, soon. But how about we kick things off with a little hypnosis first?"
            $ renpy.music.set_volume(1.0)
            show Akiko smile blush
            $ renpy.music.set_volume(0.1)
            play music Flow
            "Nozomi's confusion gives way to a smile, as an excited purr seems to escape her lips." with dissolve
            a "O-oh gosh, are you..."
            ks "Let me hypnotize you, Nozomi."
            $ renpy.music.set_volume(0.2)
            $ renpy.scene()
            $ renpy.show ("CopycatKaraokeHypno pose1_{0} glasses1 blush1 k_smile1 a_smile1".format(AkikoClothes))
            with blink
            "I sit beside her on the couch and produce my penlight from my pocket, and her eyes immediately swivel towards it as she giddily nods her consent." with dissolve
            a "Ahh, a-alright. Doing it here sounds like it'd be fun, actually~"
            k "I love that you get so excited for this stuff. Okay, now just look up and let the light hit you."
            show CopycatKaraokeHypno flash a_smileflash1 with dissolve
            show CopycatKaraokeHypno a_smile1 with dissolve
            $ renpy.music.set_volume(0.3)
            k "That's right, Nozomi. Just breathe, relax, and remember all that you felt before."
            show CopycatKaraokeHypno a_smileflash1 with dissolve
            show CopycatKaraokeHypno a_smile1 with dissolve
            k "Remembering how good it feels to watch the light dance before your eyes."
            show CopycatKaraokeHypno a_smileflash1 with dissolve
            show CopycatKaraokeHypno a_smile1 with dissolve
            show CopycatKaraokeHypno -blush1 a_sleepy k_talk1
            $ renpy.music.set_volume(0.5)
            $ renpy.transition(longdissolve, layer="master")
            k "And how it draws you in so completely, as that pleasant, sleepy feeling washes over you."
            show CopycatKaraokeHypno a_sleepyflash with dissolve
            show CopycatKaraokeHypno a_sleepy with dissolve
            $ renpy.music.set_volume(0.6)
            a "{size=16}Mmmm..."
            k "Remembering how your eyelids become heavier, and heavier, with every sweep of the light."
            show CopycatKaraokeHypno a_sleepyflash with dissolve
            show CopycatKaraokeHypno a_sleepy with dissolve
            show CopycatKaraokeHypno a_dazed
            $ renpy.transition(longdissolve, layer="master")
            $ renpy.music.set_volume(0.7)
            k "How sleepy it makes you feel."
            show CopycatKaraokeHypno a_dazedflash with dissolve
            show CopycatKaraokeHypno a_dazed with dissolve
            $ renpy.music.set_volume(0.8)
            k "How deeply entranced it makes you."
            show CopycatKaraokeHypno a_dazedflash with dissolve
            show CopycatKaraokeHypno a_dazed with dissolve
            show CopycatKaraokeHypno a_tranced
            $ renpy.music.set_volume(0.9)
            $ renpy.transition(longdissolve, layer="master")
            k "How it all makes you want to close those heavy eyelids and..."
            show CopycatKaraokeHypno a_trancedflash with dissolve
            show CopycatKaraokeHypno a_tranced with dissolve
            $ renpy.music.set_volume(1.0)
            show CopycatKaraokeHypno a_sleep1
            $ renpy.transition(longdissolve, layer="master")
            k "Sleep. All the way down... that's right."
            $ renpy.show ("CopycatKaraokeHypno pose2_{0} glasses2 k_smile2 a_sleep2 -flash".format(AkikoClothes))
            $ renpy.transition(longdissolve, layer="master")
            "I have to smile as she adorably slumps her head gently against my shoulder as she falls."
            k "Falling so... so very deeply for me now, Nozomi. Becoming so completely, wonderfully hypnotized."
            "Makes me want to fall silent for a few moments and just enjoy having her here. A sleeping beauty cuddled up so cozily by my side."
            "I hope we get to enjoy many more moments like this, Nozomi. But now I need to correct you on a few... misconceptions you've been having."
            show CopycatKaraokeHypno k_talk2
            k "And now that you're feeling so wonderfully hypnotized, now that you're completely focused on my voice... I want to talk to you about the person you admire most." with dissolve
            k "And who is it you admire most?"
            show CopycatKaraokeHypno k_neutral a_sleeptalk
            a sleeptalk "Mmn, it's... it's Nozomi. Nozomi Akemi..." with dissolve
            show CopycatKaraokeHypno k_talk2 a_sleep2
            k "That's right. Nozomi Akemi is the person you admire more than anyone in the world. So much that you want to be everything she is." with dissolve
            k "You've adopted the way she looks, the way she acts, the way she talks... you've even adopted her name."
            k "It makes you feel so good to impersonate Nozomi, doesn't it?"
            show CopycatKaraokeHypno k_neutral a_sleeptalk
            a sleeptalk "Yes... feels so... good..." with dissolve
            show CopycatKaraokeHypno k_talk2 a_sleep2
            k "I know it does. And it's good that you feel so strongly about her. Nozomi is feminine perfection, and it's right that you try to meet that ideal. It makes you happy." with dissolve
            k "And I don't want you to lose that feeling. It's good that you're becoming so much like Nozomi. It's good that you want to be so much like Nozomi."
            k "But that doesn't mean you always need to listen to Nozomi herself."
            show CopycatKaraokeHypno k_neutral
            "I watch as the girl's lips start to tremble as I introduce the idea to her; the doubt writing itself plainly even on her dormant features." with dissolve
            show CopycatKaraokeHypno a_sleeptalk
            a "I... I-I don't...?" with dissolve
            show CopycatKaraokeHypno k_talk2
            k "Sometimes people lie to us when they want to spare our feelings. Sometimes we even lie to ourselves. And in that respect, Nozomi is no different to anyone else." with dissolve
            show CopycatKaraokeHypno a_sleep2
            k "Sometimes, it takes the people observing us to reveal the truth about who we really are. Understand?" with dissolve
            show CopycatKaraokeHypno k_neutral a_sleeptalk
            a sleeptalk "Ah... I... t-think so..." with dissolve
            show CopycatKaraokeHypno k_talk2 a_sleep2
            k "So keep that in mind when I talk to you about Nozomi." with dissolve
            k "Sometimes, what I say about her is more truthful than what Nozomi has to say about herself."
            k "Let that thought sit deep in your mind. Let it inform how you think about Nozomi, and then awaken for me on a count of three."
            stop music fadeout 5.0
            k "Waking up nice and refreshed in one... two... three."
            show CopycatKaraokeHypno k_neutral a_waking
            a drowsy "Mmmrrrrnn..." with dissolve
            show CopycatKaraokeHypno k_smile2
            "Damn, that sleepy expression of hers is gorgeous. She's gorgeous." with dissolve
            k "Welcome back, Nozomi. Did you enjoy that?"
            show CopycatKaraokeHypno a_grin blush2
            play music Downtown
            "And I surely don't want to make her any less beautiful than she is now. Merely keep her on the right path to perfection." with dissolve
            a "I did... gosh, you have such a way with words, Kyou~ {font=DejaVuSans.ttf}♥{/font}"
            "I certainly don't want her to stop moving forward with the ideal of becoming Nozomi. A little course correction is all she needs."
            k "You just bring out the best in me, Nozomi. Now let's just forget about that silly idea of your idol not being able to sing."
            show CopycatKaraokeHypno a_confused -blush2
            a confused -blush "O-oh, are we still on that?" with dissolve
            k "Forget about what she told you. We both know she sings like a goddamned angel."
            show CopycatKaraokeHypno a_grin
            a "Ehehe... Yeah, she absolutely does. She must've been messing with me." with dissolve
            show CopycatKaraokeHypno a_smile2
            a smile_side "Mmm that's so like her, trying to downplay how perfect she is compared to the rest of us." with dissolve
            k "Yeah. But you're not so bad yourself, Nozomi. And I'm sure you sing wonderfully, so what do you say about getting us started?"
            stop music fadeout 5.0
        "I need to talk it out of her":
            $ HypnotizedAkiko = False #This flag will come into play when Kyou has to make a choice tomorrow
            "Yeah. There's no need to over-react here, make a big deal out of this and risk spoiling our day out."
            "As much as she idolizes Nozomi and no doubt hangs on her every word, I know she listens to me too."
            ks neutral "Like... you gotta know she was just being modest, right?"
            a confused "I suppose?" with dissolve            
            "I smile in a way I hope will come across as assuring while I sit beside her."
            ks smile "You know it's true, Nozomi. She's been doing this for years; she surely sings like an angel by now."
            ks "And what's more? You know you do too. So what do you say about getting us started?"
    if HypnotizedAkiko == True:
        show CopycatKaraokeHypno blush2
        $ persistent.copycat_karaoke_hypno1_unlock = True
        $ persistent.copycat_karaoke_hypno2_unlock = True
    else:           
        $ renpy.show ("Akiko side {0}_up3 noarmband shy_side blush nglasses".format(AkikoClothes))
    "I then reach over for the remote control for the song selector and slide it across to her, and as she looks to it that adorable smile of hers returns." with dissolve
    if HypnotizedAkiko == False:
        show Akiko shy
        $ renpy.transition(dissolve, layer="master")        
    a "O... okay~"
    scene bg blackscreen with longdissolve
    pause 2.0
    scene bg karaoke lights
    queue music Beautiful
    $ renpy.show ("Akiko side {0}_up3 noarmband laugh blush nglasses".format(AkikoClothes))
    with longdissolve
    a "Haaaah~ {font=DejaVuSans.ttf}♥{/font}"
    "I must be smiling from ear to ear as Nozomi belts out the last note of another energetic pop song before she stops to catch her breath."
    ks casual happy "Oh man, that was amazing! How has no one recruited you for a pop idol group yet?"
    a embarrassed "O-oh stop, ahahaha~" with dissolve
    a laugh_open "But... aaahhhh... y-yeah I was really going for it that time!" with dissolve
    "I nod, as I pass her an opened water bottle that she gratefully takes from me."
    ks smile "Do you need a break? Maybe we should order some snacks or something."
    a happy "Mmmph... *gulp*... aaahhhh..." with dissolve
    a smile "... Why don't you join me for the next one, Kyou? I want to sing with you!" with dissolve
    "Ah... I knew she was going to say that sooner or later, but..."
    ks confused "Oh... Nozomi, I don't sing. I'd just bring you down."
    a laugh "Aww, don't be silly! Karaoke's not about being able to sing well." with dissolve
    ks smirk "Heh. Easy for you to say."
    a laugh_wink "Hehe, but it's true! It's all about being able to forget ourselves and having the best time with the people you cherish." with dissolve
    ks smile "And you believe that?"
    a shy "She believes it. So yes, yes I do~" with dissolve
    scene bg blackscreen with dissolve
    "I guess I can't refute her when she puts it like that, or expresses herself so purely."
    $ renpy.scene ()
    $ renpy.show ("CopycatKaraoke akiko_{0}_down a_smile glasses1 kyou_down k_smile".format(AkikoClothes))
    with dissolve
    # scene CopycatKaraoke akiko_nozomi_a_down with dissolve
    "So I take up the mic, set the next song we have queued up to play for a duet, and get up to stand beside my beautiful companion."
    k "Alright, Nozomi. You asked for this."
    show CopycatKaraoke a_happy title
    a smile "Ehehe~ Just relax and enjoy the moment. This is going to be great." with dissolve
    stop music fadeout 2.0
    show CopycatKaraoke k_confusedtv lights
    "I take a breath and nod to her as the TV screen kicks back into life, and I spy the title..." with dissolve
    show CopycatKaraoke a_smile    
    k "\"Because I Like You\", by Yuka and... \"Waldo\"?" with dissolve
    play music Grave
    "The opening melody begins to play as Nozomi grins at me."
    show CopycatKaraoke a_giggle -title
    a laugh_wink "You don't know? It's a new cover of a song that came out a few years ago, and it's blowing up on TikTak. Everyone's singing it~" with dissolve
    $ renpy.show ("CopycatKaraoke akiko_{0}_up a_smile k_neutral".format(AkikoClothes))
    show CopycatKaraoke a_happy lyric1b
    "Everyone but me, apparently. But before I can say more, Nozomi raises a hand as if to stop me voicing my thoughts as the lyrics start to flash on the screen." with dissolve
    show CopycatKaraoke a_singtv
    a "Mm, okay, here we go..." with dissolve
    "And just like that I find myself in a duet with who must surely now be the most angelic girl in my school, as her eyes dart first from the screen, and then to me..."
    show CopycatKaraoke lyric1
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} You were not my choice because you're cool; you are cool because you were my choice {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} Perhaps you've been rejected and made fun of, but I don't care; I'll still call you my hero {font=DejaVuSans.ttf}♫{/font}{/size}"
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} Always saying you're sleepy and dragging your feet, {w=0.8}then do your best to stay awake in class {font=DejaVuSans.ttf}♫{/font}{/size}"
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} You're always cool with anyone you meet, {w=0.8}then turn into the sweetest goofball around dogs or cats {font=DejaVuSans.ttf}♫{/font}{/size}"
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} My heart's yelling, it's screaming \"I love you\", I know it pretty well {font=DejaVuSans.ttf}♫{/font}{/size}"
    show CopycatKaraoke lyric2
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} You're always going to be my hero, just be yourself {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    show CopycatKaraoke a_smile k_smile -lyric2
    "God, she sounds even more angelic when I'm standing right in front of her." with dissolve
    show CopycatKaraoke a_singtv lyric1
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} Want to text you all day long, {w=0.8}hold your hand as we walk home {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} But daily, after school, I see you leaving and want to say \"See you tomorrow\"... {font=DejaVuSans.ttf}♫{/font}{/size}"
    show CopycatKaraoke a_sing lyric2
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} But you're already gone {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    show CopycatKaraoke a_singtv lyric1
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} I'd adore a weekend for us to meet, {w=0.8}or speak on the phone so late that I'll fall asleep {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    show CopycatKaraoke a_sing lyric2
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} I just don't seem to find the courage to tell you {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    show CopycatKaraoke a_joy
    a smile "{size=28}{font=DejaVuSans.ttf}♪{/font} But I won't give up! {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    show CopycatKaraoke a_happy k_confusedtv -lyric2
    "I can feel a lump in my throat, even while I cast an anxious glance back at the screen." with dissolve
    show CopycatKaraoke lyric1b
    "It's like she's singing straight to my heart." with dissolve
    show CopycatKaraoke a_singtv k_confused lyric1
    a happy "{size=28}{font=DejaVuSans.ttf}♪{/font} Please just look in my direction; {w=0.8}please acknowledge my affection {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} Please, should I change my make up? {w=0.8}Maybe change how I dress up? {font=DejaVuSans.ttf}♫{/font}{/size}"
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} I just really, really want you. Take me and I'm going to be forever yours {font=DejaVuSans.ttf}♫{/font}{/size}"
    show CopycatKaraoke a_blush lyric2
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} I practice my confession, {w=0.8}all night in mental simulations {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    show CopycatKaraoke a_sing
    a "{size=28}{font=DejaVuSans.ttf}♪{/font} Tomorrow perhaps will be the day that they will become true {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    $ renpy.show ("CopycatKaraoke akiko_{0}_down a_smile k_confusedtv lyric4b".format(AkikoClothes))
    "Suddenly the lyrics line changes color as it updates... shit, this is my part!" with dissolve
    show CopycatKaraoke kyou_up k_nervoustv lyric4
    k"{size=28}You were not my choice because you're cute; you are cute because you were my choice.{/size}" with dissolve
    show CopycatKaraoke lyric3
    k "{size=28}Perhaps you've been misunderstood by others but I don't care; I'll still call you my heroine.{/size}" with dissolve
    k "{size=28}\"I'll stay awake\" you promise, stomping your feet, {w=0.8}then fifty minutes later you fall asleep in class.{/size}"
    k "{size=28}You're always acting tough with anyone you meet, {w=0.8}but if you're overwhelmed, you can start crying pretty fast.{/size}"
    k "{size=28}My heart's yelling, it's screaming \"I love you\", I know it pretty well.{/size}"
    show CopycatKaraoke lyric4
    k "{size=28}You will always be my heroine, as long as you're yourself.{/size}" with dissolve
    show CopycatKaraoke a_giggle k_confused -lyric4
    a laugh_wink "{size=16}S-see? You're doing great!{/size}" with dissolve
    show CopycatKaraoke k_blush
    "I blush as she quietly praises me. It doesn't even matter that she's so obviously lying; it's all I can do to read the lyrics let alone sing them." with dissolve
    show CopycatKaraoke a_smile k_smile lyric3b
    "She can say anything she wants when she smiles at me like that." with dissolve
    show CopycatKaraoke k_nervoustv lyric3
    k "{size=28}I'd love to watch movies with you, listen to songs. For you to sit with me, help me study stuff I'm getting wrong.{/size}" with dissolve
    k "{size=28}Daily after school you're with your friends and I want to say \"Bye, bye\"...{/size}"
    show CopycatKaraoke k_nervous lyric4
    k "{size=28}But you're already gone.{/size}" with dissolve
    show CopycatKaraoke k_nervoustv lyric3
    k "{size=28}I want to hold you until the world ends. I want to puff my chest and brag: \"yes, she's my girlfriend\".{/size}" with dissolve
    show CopycatKaraoke a_shy lyric4
    k "{size=28}Yet I am just unable to confess to you how I feel.{/size}" with dissolve
    show CopycatKaraoke k_nervous
    k "{size=28}But I won't give up!{/size}" with dissolve
    show CopycatKaraoke kyou_down k_smile -lyric4
    "Man, my heart's pounding as I sing this mushy stuff to her." with dissolve
    show CopycatKaraoke lyric3b
    "And from the shy looks she's giving me I reckon her heart's doing some pounding of its own, as I push the mic towards my lips once again." with dissolve
    show CopycatKaraoke kyou_up k_singtv lyric3
    k "{size=28}Please just look in my direction; {w=0.8}please acknowledge my affection.{/size}" with dissolve
    k "{size=28}Should I comb with some wax, {w=0.8}or is there something else I may lack?{/size}"
    k "{size=28}I just really, really want you. Take me and I'm going to be forever yours.{/size}"
    show CopycatKaraoke lyric4
    k "{size=28}I practice my confession, {w=0.8}all night in mental simulations.{/size}" with dissolve
    show CopycatKaraoke k_sing
    k "{size=28}Tomorrow perhaps will be the day that they will become true.{/size}" with dissolve
    $ renpy.show ("CopycatKaraoke akiko_{0}_up a_wink kyou_down k_confused -lyric4".format(AkikoClothes))
    "I can feel my cheeks burning now, as Nozomi brings the mic back up to her face and gives me an affirming wink." with dissolve
    show CopycatKaraoke lyric2b
    "She... did she choose this song for us on purpose?!" with dissolve
    show CopycatKaraoke a_singtv k_smiletv kyou_up lyric2
    a happy "{size=28}{font=DejaVuSans.ttf}♪{/font} I came to ask you for advice when I was feeling low {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    show CopycatKaraoke a_smile k_singtv lyric4
    k "{size=28}You came to ask me for advice about a boy that you know.{/size}" with dissolve
    show CopycatKaraoke a_sing k_smiletv lyric2
    a smile "{size=28}{font=DejaVuSans.ttf}♪{/font} Don't say it's a lost cause; this is how I feel {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    show CopycatKaraoke a_smile k_singtv lyric4
    k "{size=28}Please, I beg you, don't go with another man, I just want you to look at me.{/size}" with dissolve
    show CopycatKaraoke a_shy k_smiletv lyric2
    a shy "{size=28}{font=DejaVuSans.ttf}♪{/font} Please just look in my direction {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    show CopycatKaraoke k_smile lyric4
    k "{size=28}Please acknowledge my affection.{/size}" with dissolve
    $t = Character (_("{color=#4B9374}Kyou{/color} {color=#FFFFFF}& {/color}{color=#5F5C5C}Akiko{/color}"))
    show CopycatKaraoke a_joy k_happy lyric5
    t "{size=28}{font=DejaVuSans.ttf}♪{/font} I know that this sounds greedy; please promise that you won't leave me {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    t "{size=28}{font=DejaVuSans.ttf}♪{/font} Don't change a thing about you, just think of what we could be {font=DejaVuSans.ttf}♫{/font}{/size}"
    show CopycatKaraoke lyric6
    t "{size=28}{font=DejaVuSans.ttf}♪{/font} Maybe we could tomorrow, live that simulation {font=DejaVuSans.ttf}♫{/font}{/size}" with dissolve
    t "{size=28}{font=DejaVuSans.ttf}♪{/font} I know my love for you will push me to become my best version {font=DejaVuSans.ttf}♫{/font}{/size}"    
    stop music fadeout 6.0
    $ renpy.show ("CopycatKaraoke akiko_{0}_down a_shy kyou_down k_smile -lyric6".format(AkikoClothes))
    "The two of us take a long breath as the song winds down and the final lyric line fades away." with dissolve
    scene bg karaoke lights
    $ renpy.show ("Akiko side {0}_up3 shy blush noarmband nglasses".format(AkikoClothes))
    $ persistent.copycat_karaoke1_unlock = True
    $ persistent.copycat_karaoke2_unlock = True
    with blink
    "And as the final notes play out over the speaker, our eyes meet..."
    a "... You know, everyone who saw us today think we're a couple."
    ks casual confused "Hm?"
    queue music Warm_Romantic
    a shy_side "The people at the clothing store, the shoe store, the restaurant... I-I mean, of course they would, wouldn't they?" with dissolve
    ks smile "Eheh... yeah, we really have been like a couple on a perfect date, haven't we?"
    a happy "Yeah... Yeah, we really have been like that." with dissolve
    a smile "So are we?" with dissolve
    "I knew this was coming. Everything I've done with her today has been leading to this moment, and yet her question still leaves me breathless."
    # "Somehow, I still feel unprepared for this moment."
    a happy "Kyou... You said I'm the only person you can talk to? I feel the same way with you." with dissolve
    "To witness this girl, our plain student council president mere days ago, blossom into the epitome of grace and beauty was one thing."
    a smile "Right now, it feels like you're the only person in the whole world who truly understands me. The only one who believes in me." with dissolve
    "She might be an imitation of the real thing, but in a moment such as this, I don't know how that could matter."
    # $ renpy.show ("Akiko side {0}_down3 noarmband nglasses".format(AkikoClothes))
    $ renpy.scene ()
    $ renpy.show ("CopycatKaraoke together_{0} affectionate glasses2".format(AkikoClothes))
    with blink
    a "And I believe in you, Kyou. I believe in us. So..."
    "I don't see Akiko standing here, performing a perfect impression of the girl I love."
    show CopycatKaraoke affectionate_closed
    a shy "Let's be the best that we can be. Together {font=DejaVuSans.ttf}♥{/font}" with dissolve
    "I just see Nozomi; the most attractive girl in our school bar none."
    k "Yeah. We will, Nozomi. I promise."
    show CopycatKaraoke affectionate
    stop music fadeout 5.0
    "And she's my girlfriend. My heroine." with dissolve
    $ persistent.copycat_karaoke3_unlock = True
    scene bg blackscreen with longdissolve
    "My choice."
    pause 2.0
    jump Day7_Villain2_Kyou        
    #At karaoke, Akiko mentions how everyone's been thinking they're a couple this whole time they've been hanging out together, and the thought's grown on her
    #When Kyou proposes that they officially become a couple Akiko ponders out loud the fact Nozomi doesn't date
    #She also mentions losing interest in kendo, so she will probably drop it. She also talks about how student council doesn't really appeal either, even though things will loosen up after the culture fest

    # a smile_side blush "You know those sales assistants thought we were a couple, right?" with dissolve
    #Akiko spent all her savings on getting her hair done, then on the glasses. An excited Kyou offers to take her clothes shopping and Akiko models two outfits for him, allowing him to pick the one he thinks best matches Nozomi's style since they don't actually know
    #Afterwards they wonder what they should do and Akiko suggests karaoke. She'd love to sing for him, and they have food there too! So Kyou takes her there for another treat, and they spend a few hours there while she performs for him, having a great time
    #Kyou wants to spend the whole night with her, maybe take it back to his place, but Akiko then says she can't stay out too late because she's busy with "a school thing" tomorrow, but she'd be delighted to meet him there if he wanted?
    #He's indignant about going to school on a Sunday, but he will if he gets to see "Nozomi" again. That's when all hell breaks loose from the moment everyone, and the real Nozomi especially, lays eyes on Akiko and her new look...
label Day6_Con_Kyou_Nozomi:
    scene bg k bedroom day with blink
    "I have no idea what's going to happen today."
    "Nozomi texted me to say she'll be here a little earlier than the others. I think she wants to say a few things to me first."
    play sound doorbell
    "That must be her at the door now."
    scene bg k room day
    show Nozomi front casual concerned
    if hypno2 == "zombie":
        show Nozomi noglasses
    with blink
    play music Rain fadein 2.0
    if hypno2 == "trance":
        n "{size=16}Hey, Sir...{/size}" with dissolve
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
        n side sad_side "{size=16}I... I don't know, Sir. I really don't know.{/size}" with dissolve
    elif hypno2 == "zombie":
        n side sad_side "I... I don't know, Kyou. I really don't know." with dissolve
    play sound doorbell
    if hypno2 == "trance":
        n surprised "{size=16}Ah, they're already here...{/size}"
        n "{size=16}Set me free.{/size}"
        ks surprised "Huh?"
        n smile "Eheh, sorry Kyou, but I need to be in my right mind for this~" with dissolve
        ks smirk "Eh, I specifically made sure my suggestions wouldn't work while we had company."
        n front concerned "Maybe not, but still, I just realized I have no idea what other influences you might have exerted on me without either of us realizing." with dissolve
        n "I can't have any of that effect me right now."
        play sound doorbell
        n pout_left "... You should probably get that." with dissolve
    elif hypno2 == "zombie":
        n surprised "Ah, they're here already?!"
        n sad_closed "W-well... let's get this over with, then." with dissolve
    show Sayori casual neutral_right at left, flip:
        xpos 0.1
    show Hiroko casual frown no_arm at center:
        xpos 0.75
    show Nozomi front concerned casual_folded:
        xpos 0.5
    with blink
    s "So. Here we are."
    h dress_arm frown_side "C'mon, let's get this over with. What's going on with you two?" with dissolve
    n side casual sad_side "Alright, so..." with dissolve
    n "While I was cleaning the classroom with Kyou this week, he told me something interesting."
    n "He told me he was studying hypnosis."
    h "Hypnosis?"
    s neutral "And that is interesting to you?" with dissolve
    n sad_closed "Well..." with dissolve
    n blush "It's like... a hobby of mine? Kinda? So..." with dissolve
    show bg blackscreen onlayer toplayer with fade
    "Nozomi went on to try and explain everything that happened between us over the last few days."
    "The arranged hypnosis sessions, the kinds of things we'd do in those sessions..."
    if hypno2 == "zombie":
        "And the real reason why she injured herself and broke her glasses."
    hide bg blackscreen onlayer toplayer
    s casual_folded concerned "Alright... I need a minute to process this." with dissolve
    h casual no_arm concerned "So like, Kyou's seriously been controlling your mind?" with dissolve
    if hypno4 == "arousal":
        h angry "That time you looked like you were about to come for no damn reason? That was {w=0.7}{nw}" with dissolve
        extend "HIM?" with vpunch
    elif hypno4 == "tickle":
        h angry "That time you were rolling on the floor laughing yourself half to death? {w=0.7}That was 'cuz of {nw}" with dissolve
        extend "HIM?" with vpunch
    h casual_armup angry "That's {nw}" with dissolve
    extend "SO fucked up!" with vpunch
    h sad_side "And, uh, wait, is he controlling you right now or what?" with dissolve
    if hypno2 == "trance":
        n casual side sad "Uh, no. Like I said, he gave me a way of undoing everything he did in our sessions. And I made use of it right before you entered." with dissolve
        s frown "... Does it, though?" with dissolve
        n sad_side "What do you mean?" with dissolve
        s "I admit I know little of hypnosis, so perhaps I am off base here..."
        s annoyed "But do you not think it possible that you merely BELIEVE everything has been undone?" with dissolve
        s "Because what you have told us suggests he has had unfettered access to your mind."
        if hypno1 == "count":
            s "He was able to make you forget something as fundamental as a number, and he can compel you to do things even if you actively resist."
        elif hypno1 == "name":
            s "He was able to make you forget something as fundamental as your own name, and he can compel you to do things even if you actively resist."
        s frown_right "So tell me, what was stopping him from making you merely believe you're free of his control? Can either of you answer me that?" with dissolve
        n "Uh... w-well..."
        ks sigh "Nothing. Nothing was stopping me."
        show Hiroko casual sad
        n front concerned casual "Kyou..." with dissolve
        ks "It's true though, isn't it? I didn't think about it to start, because I always thought you could protect yourself if I tried anything you didn't want."
        n "You mean like, a hidden observer effect? I was thinking that too."
        h frown "What're you talking about? \"Hidden observer\"?" with dissolve
        n pout_left "Uh... Well, it's like how even when you're hypnotized there's still a part of you that's aware of everything that's happening?" with dissolve
        n "So if your hypnotist tries to suggest something unethical or just something you disagree with you still have the ability to ignore the suggestion, or explicitly reject it."
        ks frown "But I started to realize that wasn't happening. It's like Sayori says, I could do anything to your mind and there would've been nothing to stop me."
        ks "That's when I knew I had to give you the means to defend yourself."
        h "\"The means to defend yourself\"?"
        h dress_arm sad_side "Like, holy shit, you get how fuckin' insane this sounds, right? Gettin' mixed up in this?" with dissolve
        n irritated casual_folded "God, Hiroko, YES! I know it's stupid and ridiculous and dangerous as hell, and..." with dissolve
        n "And it's all my fault!"
        show Sayori concerned
        ks neutral "Nozomi..." with dissolve
        n frown casual_folded "It's true though, isn't it? I set us some groundrules, then I almost immediately walked them back." with dissolve
        n "I was so eager to explore my desires I completely disregarded my own safety!"
        n cry casual "God, I'm such an idiot. I really should've been more careful..." with dissolve
        ks sigh "No. Nozomi, no, I was the one who should've been more careful."
        ks "I was your hypnotist, and we were trying these things for the first time."
        ks "I should've insisted we take it slower. At least until I knew what I was doing."
        show penlight at right with moveinright:
            ypos 0.346
        "I then pull out the penlight from my pocket for all to see."
        show Nozomi concerned
        show Sayori concerned_right
        show Hiroko frown
        ks neutral "Especially when I was using this thing." with dissolve
        hide penlight with moveoutright
        ks "I mean, it's clear that I didn't understand how powerful this was. You even tried to warn me in your own way."
        h frown_side "That's the thingy you were talking about, Nozo?" with dissolve
        n sigh "Yes. That's what we used to hypnotize me." with dissolve
        s "What is so special about it? It looks like a cheap penlight."
        ks frown "It is, mostly. I was able to modify the beam to make it more... attention-grabbing? But after everything I have to admit it does way more than that."
        ks "It must be doing something else that I didn't consider. Something that makes the subject more suggestible and silences the \"hidden observer\" effect."
        show Nozomi side sad
        ks "So much so that it lessened your inhibitions and made you want to stop taking precautions. I should've realized what I was doing to you."  with dissolve
        ks "I truly am sorry, Nozomi."
        show Hiroko frown
        "The room falls silent for a while, although everyone's eyes are drawn to the penlight in my hand, before Sayori speaks up." with dissolve
        s "To think that your secret little science project would cause so much trouble."
        s frown_right "There is a hidden genius in you, Kyou. Now if only you could start using it for good..." with dissolve
        "I let out a little chuckle."
        s "If that penlight is doing what you say it's doing, then it needs to go. It's too dangerous to keep around."
        show Hiroko frown
        n front frown casual_folded "Yes, I agree." with dissolve
        ks surprised "What?! I worked so hard on this. I realise it's dangerous, but do I really have to ditch it right now?"
        ks "I mean, don't we want to know why it does what it does? There could be a research project in this. Or- {w=1.0}{nw}"
        stop music fadeout 1.0
        h casual_armup angry "YOINK!" with vpunch
        "She just snatched the damn thing out of my hand!"
        h "Just so you know, this is going in the fuckin' sea!"
        show Hiroko frown
        ks frown  "Goddamnit..." with dissolve
        play music Memories fadein 5.0
        s "If you want us to start trusting you, Kyou, this is a good first step."
        n concerned casual "I'm disappointed too, Kyou. But we need to be responsible. Who knows what would happen if we kept using that..." with dissolve
        ks sigh "Yeah... Yeah, I know."
        show Hiroko casual
        "An awkward silence hangs in the room for a few moments, interrupted only by the sound of Hiroko slipping my penlight into her bag." with dissolve
        s frown "You ARE going to destroy that thing, aren't you?" with dissolve
        h angry_side "Of {nw}" with dissolve
        extend "COURSE! Geez. You take me for an idiot?" with vpunch
        n "Well, anyway, I think we should give the hypnosis a rest. At least for now."
        show Hiroko frown
        ks concerned "Yeah..." with dissolve
        n "I mean, fantasizing about this sort of thing and have it actually happen to you are two very different things."
        n "And now that I'm thinking clearly again, it's left me a bit shaken to tell the truth."
        "I simply nod. I can't say I'm happy about all this, but she's right; we need to take a step back."
        show Hiroko neutral
        s smile "Alright. That sounds reasonable, Nozomi. I'm relieved." with dissolve
        n sleeptalk_concerned "And I'm so sorry for making you both worry, and for getting you mixed up in my nonsense. I was selfish chasing my desires so recklessly." with dissolve
        show Hiroko sad_side
        n cry "You're both having to work so hard for your futures and I'm just... j-just bringing you down with this stupid crap." with dissolve
        s casual "Nozomi, come on. We all had to work hard this semester, don't sell yourself short like that." with dissolve
        h smile_side "Yeah, Nozo. We're besties and you're clearly going through some shit. We wanna help!" with dissolve
        $nface = "concerned"
        n "You mean that? You're not completely weirded out by all this?" with dissolve
        h annoyed_side "I'm {nw}" with dissolve
        extend "SUPER weirded out by all this!" with vpunch
        h smile_side "But, y'know, so what? I can have a weird friend~ 'Sides, we're all weird in our own ways." with dissolve
        s smirk "Do you want to tell us of your weird ways, Hiroko?" with dissolve
        h frown_side "No." with dissolve
        show Nozomi smile
        s frown_right "So tell me, Kyou, is there anything else we should know about? Do you currently have any influence over Nozomi's mind at all right now?" with dissolve
        ks frown "Uh... I guess not, assuming the safety phrase I gave her works like I told it to. And after everything else that's happened I don't have a reason to doubt that it did."
        n frown "Yeah. Since I said that phrase I feel like... like a spell has been lifted? I don't know, but I do feel like my mind's my own again." with dissolve
        s "Alright, so how about this: We take you at your word, Kyou, that Nozomi is no longer under your dangerous influence. But we will be watching."
        s "If Nozomi exhibits any unexplainable behaviour, we'll know who to come to and-{w=0.8}{nw}"
        show Nozomi surprised
        h casual_armup angry no_arm "We'll {nw}" with dissolve
        extend "KILL you!" with vpunch
        s concerned casual_folded "... I was going to say hold you accountable, but sure that works." with dissolve
        ks "I won't put Nozomi in any such danger again, I promise."
        n smile "Ehehe... thanks, you two~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    elif hypno2 == "zombie":
        n "No. There's some lingering effects in my head, but so long as he doesn't say that zombie trigger I should be unaffected."
        s concerned "What about that obedience conditioning you mentioned?" with dissolve
        n frown_side noblush "Even if I'm still affected it won't do anything to me so long as you're here." with dissolve
        s "I know, but would having that compulsion to obey at all not have some effect on you regardless?"
        n frown "I don't... think so?" with dissolve
        s "Well I do have to wonder how safe it really is, to allow yourself to have such a compulsion in the first place."
        s "Do you not think that over a period of time, you would become so used to your conditioning that you would obey commands that went beyond what you originally thought acceptable?"
        n "Uh, well..."
        h angry_side "Like, come {nw}" with dissolve
        extend "ON, Nozo! It feels like I'm the only one who cares that he could've killed you doing this shit!" with vpunch
        show Nozomi at flip
        n surprised_side "Huh?" with dissolve
        h "Hello? You fell down the stairs 'cause you thought you were a zombie. You're lucky you didn't break your neck!"
        show Nozomi sad_side
        "Snarling, Hiroko points at me as she turns her ire in my direction." with dissolve
        h angry "This is all your fucking fault! {w=0.4}{nw}" with dissolve
        extend "YOU got her mixed up in all this in the first place with your creepy-ass bullshit!" with vpunch
        h "Why couldn't you just leave her alone?"
        ks "Hiroko, i-it's not like we meant for it to be like that-{w=0.5}{nw}"
        h "I don't give a {nw}"
        extend "FUCK what you meant. {w=0.5} You {nw}" with vpunch
        extend "HURT her, Kyou!" with vpunch
        n "Hiroko, please, listen to me!"
        n "Maybe Kyou was at fault, but that penlight really shouldn't have affected me the way it did."
        hide Nozomi
        show Nozomi casual noglasses
        n front sigh "Hypnosis isn't as dangerous as that, I promise. It's supposed to be fun and safe; neither of us could've known that it would affect me so severely." with dissolve
        "Still quivering with rage, Hiroko replies with a low growl."
        h "Where is it?"
        n "What?"
        h "That penlight."
        show penlight at right with moveinright:
            ypos 0.346
        "Not wanting to test her, I pull my penlight out from my pocket, where it's been lying untouched for the past couple of days."
        hide penlight with moveoutright
        show Nozomi surprised
        "And she immediately snatches it out of my hand!" with vpunch
        ks "H-hey!"
        h "You got something to say to me, asswipe?"
        "All I can do is glare impotently as she holds the penlight up for all to see."
        s "So you are telling me this is what caused all this trouble?"
        n side sad_closed "Yes. That's what we used to hypnotize me." with dissolve
        s "What is so special about it? It looks like a cheap penlight."
        ks frown "It is, mostly. I was able to modify the beam to make it more... attention-grabbing? But after everything I have to admit it does way more than that."
        ks "It must be doing something else that I didn't consider. Something that makes the subject more suggestible and silences the \"hidden observer\" effect."
        ks concerned "So much so that it deadened your self-preservation instinct. Hiroko's right, we were lucky you didn't hurt yourself more than you did." with dissolve
        ks "I truly am sorry, Nozomi."
        show Hiroko casual
        show Nozomi sad
        "The room falls silent for a while, although everyone's eyes are drawn to the penlight in my hand, before Sayori speaks up." with dissolve
        s "To think that your secret little science project would cause so much trouble."
        s frown_right "There is a hidden genius in you, Kyou. Now if only you could start using it for good..." with dissolve
        "I let out a nervous chuckle."
        s "If that penlight is doing what it seems to be doing, then it needs to go. It's too dangerous to keep around."
        show Hiroko frown
        n front frown casual_folded "Yes, I agree." with dissolve
        ks surprised "What?! I worked so hard on this. I realise it's dangerous, but do I really have to ditch it right now?"
        ks "I mean, don't we want to know why it does what it does? There could be a research project in this. Or- {w=1.0}{nw}"
        stop music fadeout 1.0
        h angry "NOPE!" with vpunch
        h casual "It's coming home with me, then I'm getting a hammer and smashing this fucker to bits!" with dissolve
        show Hiroko frown
        ks frown  "Goddamnit..." with dissolve
        play music Memories fadein 5.0
        s "If you want us to start trusting you, Kyou, this is a good first step."
        n concerned casual "I'm disappointed too, Kyou. But we need to be responsible. Who knows what would happen if we kept using that..." with dissolve
        ks sigh "Yeah... Yeah, I know."
        "An awkward silence hangs in the room for a few moments, interrupted only by the sound of Hiroko slipping my penlight into her bag."
        s frown "You ARE going to destroy that thing, aren't you?" with dissolve
        h annoyed_side "Of {nw}" with dissolve
        extend "COURSE! Geez. You take me for an idiot?" with vpunch
        n "Well, anyway, I think we should give the hypnosis a rest. At least for now."
        show Hiroko frown
        ks concerned "Yeah..." with dissolve
        n "I mean, when we started this it was meant to be fun, and I guess a little bit kinky if I'm being honest."
        ks "But it'll be fine now, won't it? We'll just do it without the penlight, like last time."
        n "Maybe. It's just that talking to my friends brought me to my senses a little bit."
        "I simply nod. I can't say I'm happy about all this, but she's right; we need to take a step back."
        show Sayori neutral
        h sad_side dress_arm "Can't you just be done with this forever, Nozo? I don't wanna see you getting hurt again." with dissolve
        n sleeptalk_concerned "Hiroko, I know you're worried, but I promise nothing will happen like that ever again." with dissolve
        n "I know people do this kind of thing all the time and only have happy memories of their experiences."
        n "And this desire I have? It's not going to go away; it's a part of who I am."
        n "I know I wasn't careful enough and Kyou and I rushed into things, but we've learned from that."
        n sleep "So please don't worry about me, Hiroko." with dissolve
        n "But... but I know that has to sound so weird and stupid to you both, and it's why I never told you about this part of myself until now."
        s sleep "We really should have suspected something at last year's culture festival." with dissolve
        s "Looking back, it seems obvious now given how eager you were to volunteer for Satoshi's hypnotic stage show."
        n sleeptalk_concerned "I'm so sorry for making you both worry, and for getting you mixed up in my nonsense. I was selfish chasing my desires so recklessly." with dissolve
        show Hiroko concerned
        n cry "You're both having to work so hard for your futures and I'm just... j-just bringing you down with this stupid crap." with dissolve
        s casual smile "Nozomi, come on. We've all had to work hard this semester, don't sell yourself short like that." with dissolve
        h casual_armup smile_side "Yeah, Nozo. We're besties and you're clearly going through some shit. We wanna help!" with dissolve
        n concerned "You mean that? You're not completely weirded out by all this?" with dissolve
        h annoyed "Oh no, I'm {w=0.5}{nw}" with dissolve
        extend "SUPER weirded out by all this!" with vpunch
        h "I dunno why anyone would find this shit sexy and not, like, something out of a horror movie."
        h "And to do this shit with Kyou of all people?"
        h angry "Seriously?! {w=0.5}{nw}" with dissolve
        extend "KYOU?! {w=0.5}{nw}" with vpunch
        extend "THIS FUCKIN' GUY?!" with vpunch
        "Tell us how you really feel, Hiroko..."
        h casual annoyed "So I'm never gonna get it. You're fuckin' weird, Nozo." with dissolve
        "She sighs, before looking to Nozomi with a smile."
        h smile_side "But, you're still my bestie, Nozo. My beautiful, weird-ass bestie. 'Sides, I guess we're all weird in our own ways." with dissolve
        s smirk "Do you want to tell us of YOUR weird ways, Hiroko?" with dissolve
        h frown_side "Fuck off." with dissolve
        show Nozomi smile
        s frown_right "So tell me, Kyou, is there anything else we should know about?" with dissolve
        ks frown "Uh... I guess not. I mean, we told you pretty much everything that went down." with dissolve
        s "When it comes down to it, Nozomi is who she is; we cannot stop her from seeing you, and it is not our place to do so."
        s "So how about this: We take you at your word, Kyou, that Nozomi is no longer in any danger around you. But we will be watching."
        s "If we have reason to suspect Nozomi's life is being negatively impacted by you in any way, we will find you and-{w=0.8}{nw}"
        show Nozomi surprised
        h casual_armup angry no_arm "We'll {nw}" with dissolve
        extend "KILL you!" with vpunch
        s concerned casual_folded "... I was going to say hold you accountable, but sure that works." with dissolve
        ks "I won't put Nozomi in any such danger again, I promise."
        n laugh blush "Ehehe... thanks, you two~ {font=DejaVuSans.ttf}♥{/font}" with dissolve

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
    play music Beautiful fadein 1.0
    "As her friends leave, I turn to Nozomi with a smile."
    ks casual smile "Wasn't so bad, right?"
    "She chuckles."
    n "That went a lot better than I feared."
    ks "Yeah. I sort of envy you having friends like that."
    n chuckle "Heh. So what now? I mean, unlike them I don't have any plans for today." with dissolve
    ks neutral blush "Well..."
    "I guess there's a question I've been avoiding to ask all this time."
    ks concerned "There's something I've been meaning to ask you."
    n side sad "Oh? What is it?" with dissolve
    ks "Well, I mean er... You're not seeing anyone are you? Romantically, I mean?"
    n "Oh, um... no, Kyou. I'm not."
    ks smile "... Would you like to?"
    stop music fadeout 5.0
    n smile "..." with dissolve
    n "I should've seen this coming, shouldn't I?"
    show Nozomi:
        linear 0.8 ypos 1.1
    "I let out a nervous chuckle as she gestures for us to sit on the couch."
    show Nozomi:
        ypos 1.1
    play music Eons
    n "This week with you has been fun, I admit."
    n front pout_left "Mostly terrifying in retrospect, but fun~" with dissolve
    n "Still..."
    n concerned "When I entered into this arrangement with you, I never considered it beyond being a shared hobby." with dissolve
    n "Wasn't that naive?"
    ks smile "Honestly? Yeah, kinda."
    ks "I mean, even from the beginning you were talking about getting off on this stuff. You really didn't think more would come from what we were doing?"
    n sigh "I know. When you gave me the opportunity to do this, I really didn't think much beyond that." with dissolve
    n surprised "I even overlooked the fact you made that stupid penlight just so you could hypnotize girls! And ME in particular!" with dissolve
    n concerned "And when I think now about how effective that thing was, that really has some sinister implications, doesn't it?" with dissolve
    ks neutral noblush "Uhh... Yeah..."
    show Nozomi sigh
    "Nozomi sighs." with dissolve
    n "Look, even if I didn't have that to think about, I still wouldn't date you."
    n concerned "I'm just not looking for a relationship right now. I wanted to focus on getting to college before I did anything like that." with dissolve
    n "And since we're graduating soon, it makes sense to stick to the plan, don't you think?"
    ks "Yeah. I understand."
    ## Below needs work
    n sigh "Sorry..." with dissolve
    ks "No, it's okay. I think I needed to hear that."
    "I guess I always knew that would be her answer."
    "At least now, I think I can accept it."
    ks "Hey, Nozomi?"
    n neutral "Yes, Kyou?" with dissolve
    ks smile "We can still be friends though, right?"
    show Nozomi smile
    "Nozomi lets out a little chuckle." with dissolve
    n "We can~"
    stop music fadeout 5.0
    $ending = "friendship"
    jump Epilogue_Con_Kyou_Nozomi

label Day6_Con_Kyou_Nozomi_Trance:
    scene bg shopping2 day with longdissolve
    play music Dating3
    "When morning comes, I find myself walking at a brisk pace."
    "Nozomi messaged me last night as promised, giving me her address and asking me to swing by in the morning, but not TOO early."
    "I couldn't nail her down on a specific time, though. It was weird, like she was on the verge of changing her mind about all of this."
    # "So the next morning Kyou makes his way to Nozomi's house as they agreed."

    scene bg n house day with blink
    "Hmm... this looks like the place. Nozomi must be living well if she's in this part of town."
    play sound dooropen
    "I'm about to ring the doorbell when the door swings open, held by a kindly-looking woman who happily ushers me inside."

    # "He's greeted at the door by Nozomi's mother, Atsuko, who smiles and says she's been expecting him."
    scene bg n room day
    show Atsuko laugh at center
    with blink
    $ nm = Character(_("Nozomi's Mom"), image = "Atsuko", who_color = "#826B81")
    nm "Ah, you must be Kyou. We've been expecting you!"
    "No prizes for guessing that this is Nozomi's mother."
    "She certainly seems in a cheerful mood, but was she waiting by the door watching for me?"
    "Expecting me kinda sounds like understating it."
    ks casual smile "U-uh, you must be Mrs Akemi. It's nice to meet you."
    $ nm = Character("Atsuko", image = "Atsuko", who_color = "#826B81")
    nm smile "Just Atsuko is fine. I've been looking forward to meeting you, Kyou!" with dissolve
    ks confused "Uh... you have?"
    nm laugh "Of course! I was just thinking to myself it's about time Nozomi invited a boy over." with dissolve
    ks smile blush "Oh, huh... does she not normally do that?"
    play sound barefootrunfadein
    nm surprised "To be perfectly honest with you Kyou, she- {w=1.5}{nw}" with dissolve
    show Nozomi casual side frown_side at center, flip:
        xpos -0.2
        linear 1.0 xpos 0.25
    show Atsuko surprised_side
    $ renpy.transition(dissolve, layer="master")
    n "M-mom! What are you telling him?!" id Day6_Con_Kyou_Nozomi_Trance_9e985720
    "Ah, I thought I heard someone crashing down the stairs just now."
    ks "H-hi, Nozomi."
    hide Nozomi
    show Nozomi front casual frown blush at center:
        xpos 0.25
    show Atsuko neutral_side
    n "You're early!" with dissolve
    ks confused noblush "I... I am?!"
    "It's almost noon, what is she talking about?"
    nm happy "Mhmhmhm, I have a feeling a certain someone didn't get out of bed soon enough~" with dissolve
    show Nozomi side frown_side at flip
    n "Mom!" with dissolve
    nm laugh "Nozomi, I may have only just met your Kyou, but I'm quite sure he's not going to mind." with dissolve
    ks smile "Uh, mind what?"
    n sad_closed "Oh, n-... nothing." with dissolve
    "Nozomi clears her throat as she awkwardly runs her fingers through her hair."
    n sad_side "S-so, yes mom, this is Kyou. Kyou Koyama. He's in my class." with dissolve
    nm surprised "Ah, and a classmate too. You must know each other very well!" with dissolve
    ks smile "Ahh... y-yeah."
    n smile_side "Th-that's right... So we're going to get to it if you don't mind." with dissolve
    nm smile_side "Of course. And please, don't feel you need to leave your door open on my account~" with dissolve
    n frown_side "M-MOM?!" with vpunch
    scene bg blackscreen with dissolve
    "Nozomi's mother laughs as I'm somewhat forcefully led upstairs."
    # "As he comes inside, Atsuko admits she's been interested to meet him, given how Nozomi has never invited a boy to the house before."
    # show Nozomi casual side sad_side blush at center, flip:
    #     xpos 0.25
    # "Nozomi will probably cut her mother short before she has time to say much else to Kyou, already a little embarrassed about her reading too much into this." with dissolve
    # "Then she gently scolds Kyou for arriving too early, then invites him up to her room."
    #"You're early!" "Only a little early" "I told you to come at 12 and it's 11:40" "Right." "I thought you'd come later!"
    #"The more you struggle, the more you fight to break free, the more you realise your hands and arms and feet and legs are completely bound in the tightest rope."

    scene bg n bedroom day
    play sound dooropen
    show Nozomi casual front concerned at center
    with blink
    "Nozomi pushes the door open to her room and I follow her inside..."
    play sound doorclose
    ks casual neutral "Huh..."
    "She says nothing as my eyes scan the place. My first time in a girl's room..."
    "I'm not sure what I expected, but..."
    n sigh "I know, I know, it's a mess." with dissolve
    "The first thing I notice is a crumpled pile of clothes at the foot of her bed that seem suspiciously like they lived on the floor until just a few minutes ago."
    "The floor itself seems to be divided into two parts. There's a rectangular section connecting the doorway to the bed that's free of debris..."
    n concerned "I wanted to clean up some more before you got here, but..." with dissolve
    "... Although like with the clothes I suspect that wasn't the case earlier this morning."
    "The rest of the floor seems more reflective of how things usually are in here were I to guess."
    n side sad_side "I mean, well, it's hard to stay motivated for this sort of thing, don't you think?" with dissolve
    "There's some dust gathered around some of the opened boxes of these board games she's had out..."
    "Actually now that I look, there are a LOT of board games here, and not just on the floor."
    show Nozomi sad
    "There's shelves on the opposite wall stacked full of the things." with dissolve
    n frown "Kyou? Could you stop scrutinizing my room and say something?" with dissolve
    ks surprised "Huh? I wasn't scrutinizing, but yeah it's pretty cluttered in here."
    n front irritated "Hmpth. Like yours is any better." with dissolve
    "Her challenging me gets my back up a little. In all the times she came over to mine last week she didn't see my room once."
    ks frown "Hey, I'm a model of cleanliness!"
    n annoyed "I don't believe it. Someone like you probably has crap strewn everywhere." with dissolve
    ks "S-... \"someone like me\"?"
    n side frown "I can only imagine the horrors that await me if I so much as set foot in YOUR room!" with dissolve
    ks "My room's fine! You're just a slob."
    n front annoyed "How dare you!" with dissolve
    ks smirk "I just think you're making excuses for your own messiness. Do you need some encouragement?"
    if gesture == "hand":
        show Mindtrick awake wave at center:
            ypos 0.6
        with dissolve
        "Nozomi pouts, and I indignantly wave my hand in front of her eyes, referencing our time together the other day."
    elif gesture == "forehead":
        show Mindtrick awake poke at center:
            ypos 0.6
        with dissolve
        "Nozomi pouts, and I indignantly poke her forehead between her eyes, referencing our time together the other day."
    show Nozomi entranced_neutral
    show Mindtrick entranced
    stop music fadeout 2.0
    ks "You will tidy your room." with dissolve
    if hypnorepeat == True:
        n "{size=16}I... I will tidy my room.{/size}"
    hide Mindtrick
    "As soon as I finish speaking I just look at her stunned, recognizing the blank expression on her face immediately." with dissolve
    play music Dating3 fadein 5.0
    n side sad_closed "*sigh* No, you're right. I'm just making excuses." with dissolve
    "I meant it as a joke, but she seriously processed that as a post-hypnotic suggestion? Outside of my house?"
    n sad "So I'm going to carry on tidying if you don't mind." with dissolve
    "And... now that I think about it..."
    show cg k room eve:
        matrixcolor SaturationMatrix(0)
    show NozomiHypno drooping sleep:
        matrixcolor SaturationMatrix(0)
    with flash
    $ks = DynamicCharacter("kyou_name", image = "KyouSideFlashback", who_color = "#4B9374")
    ks smile "It doesn't matter how awake you seem in the future, this truth will always be in effect. Understand, Nozomi?"
    ncg sleeptalk "I understand..." with dissolve
    $ks = DynamicCharacter("kyou_name", image = "KyouSide", who_color = "#4B9374")
    scene bg n bedroom day
    show Nozomi side casual sad at center
    with flash
    "... Yeah. I never told her it only applied to my house."
    "And I sure didn't remove the suggestion after we were done with it the other day. We were so rushed for time that I forgot all about it."
    show Nozomi frown_side at flip
    "But with what we talked about before it seemed implied that it'd only work under the same conditions as all the other suggestions I gave her." with dissolve
    show Nozomi:
        linear 1.0 xpos 0.75
    "But then, when I consider what she was telling me yesterday, about wanting to feel like I'm really controlling her mind..."
    "Maybe she's seriously trying to immerse herself in her own fantasy as fully as possible?"
    n frown "So, Kyou." with dissolve
    ks casual surprised "H-huh?"
    "In any case, Nozomi's voice catches my attention."
    n "I might be a little occupied here, but we can still talk."
    n smile "Believe it or not, I didn't invite you over here to help me clean." with dissolve
    "So she says, but watching her pick up the littered cards and playing pieces off the floor is making me a little self-conscious of my idleness."
    ks confused "O-okay, sure. What do you want to talk about?"
    "I reply, as I bend down to pick up a box while Nozomi gingerly steps around some rather sharp-looking figurines to re-shelve a boxed set of some card game."
    n frown_side "Well... We could talk about what you like?" with dissolve
    ks neutral "What I like?"
    show Nozomi:
        linear 1.0 ypos 1.2
    "She nods as she follows my gaze to those figurines and crouches down to collect them in her hands."
    show Nozomi:
        ypos 1.2
    n "Mhm. I'm thrilled we're both into hypnosis, but that's only a recent thing for you."
    n smile "So tell me what you're passionate about. What gets you out of bed in the morning?" with dissolve
    ks frown "Uh, school?"
    hide Nozomi
    show Nozomi front2 casual teasing at center:
        xpos 0.75 ypos 1.2
    n "Don't be dense! I'm obviously talking about your hobbies." with dissolve
    "Honestly this question makes me anxious. I know what I like, but is she really going to appreciate it and not blow me off as some sort of lonely nerd?"
    ks "Well... yeah, of course I have hobbies."
    n frown "Yes, and I'm asking you to tell me about them!" with dissolve
    ks sigh "Okay, well... I'm pretty into computers and gadgets and stuff."
    show Nozomi:
        linear 1.0 ypos 1.0
    pause 1.0
    show Nozomi neutral
    "I pause a moment to gauge Nozomi's response, but she simply stands up and places her figurines back in their box while keeping a neutral expression." with dissolve
    show Nozomi:
        ypos 1.0
    ks "So, uh... I'm always reading about new things coming out in the tech world. I always loved that kinda stuff."
    n "Uh-huh?"
    "I nod, although I think she's too distracted arranging the figurines to notice."
    ks "Uh, yeah. And if I'm not doing that I'm sometimes tinkering."
    ks "L-like... taking things apart and putting them back together."
    n smile "Oh, like with that penlight?" with dissolve
    ks smile "Yeah, exactly! But I've done loads of things besides that."
    show Nozomi side smile_side at flip
    ks "Like... you know those little circuit board computers? I have a bunch of those." with dissolve
    n sad_side "Um... \"Those little circuit board computers\"?" with dissolve
    ks "Y-yeah... I've programmed a few and uh..."
    "Shit. I can't explain this stuff very well. And Nozomi's gone back to tidying while seemingly half-listening."
    "I'll talk about something else."
    ks "U-uh... and I write apps for my phone sometimes."
    show phone at right zorder 2 with moveinright:
        ypos 0.346
    "Yeah, I'll pull out my phone and show her that."
    hide Nozomi
    show Nozomi casual front surprised at center:
        xpos 0.75
    "It's enough to distract her momentarily as she looks at it with a quizzical expression." with dissolve
    n "Oh, you mean like games?" id Day6_Con_Kyou_Nozomi_Trance_0b7fc75d
    "Only to realize..."
    ks sigh "Games sometimes, yeah. I just remembered, though..."
    n neutral "Remembered what?" with dissolve
    ks "I only just got this phone, so there's nothing I wrote on it yet."
    n concerned "Oh... well, that's too bad." with dissolve
    ks "Yeah..."
    "This is why I didn't want to talk about this sort of thing. I'm just no good at it."
    "It always turns out like this somehow."
    n side sad_side "Well... it's a nice phone anyway." with dissolve
    # "So to catch her attention I pull my phone from out of my pocket and show her."
    "Still, at least Nozomi is trying to keep our conversation going while she sorts her things."
    ks smile "Oh yeah, thanks. It's the latest model."
    n sad "It is? Aren't those really expensive?" with dissolve
    hide phone with moveoutright
    ks "It... set me back a bit, yeah. But it's got everything you could ever want."
    n side smile "Hm, if you say so. But mine's a budget model and I don't need anything else." with dissolve
    n smile_side "No offense, but I kinda think getting the latest tech is a waste of money." with dissolve
    "I'm wounded."
    ks frown "You do?"
    n rolleyes "I mean, I look at them? But they barely seem any better and you pay such a premium for features you won't even use." with dissolve
    n sad_side "... W-well if it makes you happy and you can afford it then I guess it's fine." with dissolve
    n smile "But I'll stick to the budget options, heh~" with dissolve
    show Nozomi frown
    "I nod and sigh, as I pass her the box I was clearing up. Although she opens it up to examine and immediately frowns, tapping a finger over a trio of metal tokens." with dissolve
    n front2 frown "Ah, there's supposed to be four of these." with dissolve
    ks neutral "Oh..."
    "We both start to scan the floor with our eyes as the thought occurs to me..."
    ks frown "And how much are you paying for all these games?"
    show Nozomi side frown
    "Nozomi frowns at the question. I think she immediately picked up where I'm going with this." with dissolve
    n side frown "Excuse you?"
    ks "All this stuff's gotta set you back."
    n frown_side "That's different." with dissolve
    ks "Different how?"
    "Nozomi simply smiles as she cradles the box she's currently holding."
    n front2 chuckle "Each and every one of these games represents a unique and treasured experience for me." with dissolve
    ks smirk "Is that why you leave them on the floor?"
    n determined "Oh, get bent." with dissolve
    show Nozomi side frown_side at flip
    "Nozomi turns her back to me and rises up on her toes to slot her treasured box up on the top shelf of her display." with dissolve
    n "So what if I don't always put them away afterwards? It doesn't change how I feel about them."
    n smile_side "Just seeing people's faces light up when a game gets going..." with dissolve
    n smile "To share in their understanding and joy when all the pieces come together..." with dissolve
    hide Nozomi
    show Nozomi front casual laugh blush at center:
        xpos 0.75
    n "It really can be the most magical thing~" with dissolve
    n side frown noblush "But can you get that sort of experience from your overpriced smartphone? I very much doubt it, Kyou." with dissolve
    ks frown "Hey, you leave my phone out of this."
    if gesture == "hand":
        ks "But man, I think it might actually be true that you're a bigger nerd than me, hearing you go on like this."
        show Nozomi front pout_left
        "Nozomi rolls her eyes as she sighs at me." with dissolve
        n "Maybe I am, if that means I get to enjoy what I do while you get to sulk and take cheap shots."
    elif gesture == "forehead":
        ks "But man, I never knew a girl like you could be into this kinda stuff."
        n front frown "... Why, Kyou? How many girls do you know?" with dissolve
        ks "Uh..."
        show Nozomi front chuckle
        n "That's what I thought~" with dissolve
    n smirk "But do you know what I think?" with dissolve
    scene bg blackscreen with dissolve
    stop music fadeout 5.0
    "I'm... seeing a glint in her eye, as instead of picking up another box from the floor she reaches to the middle shelf of her display..."
    scene NozomiBoardgame smile with dissolve
    "... And pulls out a well-worn game box to put in front of me."
    n "I think you need to experience my passion for yourself!"
    queue music Inspiration
    "I eye the box in her hands. I think I've seen that game before; it's pretty popular if I recall."
    ks casual frown "Hmmm..."
    "I don't know if I'm all that keen, but it'd probably beat cleaning her room."
    show NozomiBoardgame pout
    n "I still have to tidy my room of course. There's still a lot to do around here..." with dissolve
    show NozomiBoardgame smile
    n "But we could have a quick game when I'm done. What do you think?" with dissolve
    # n "What do you think? I'll finish tidying this place and we can have a quick game." with dissolve
    "Yeah, I think I'm done with tidying up, or watching her do it."
    show NozomiBoardgame blank
    if gesture == "hand":
        show Mindtrick awake wave at center:
            ypos 0.6
        with dissolve
        "So I signal my intentions by waving my hand across her face again."
    elif gesture == "forehead":
        show Mindtrick awake poke at center:
            ypos 0.6
        with dissolve
        "So I signal my intentions by quickly reaching over and poking her forehead again."
    stop music fadeout 2.0
    show Mindtrick entranced
    "I don't know if Nozomi anticipated me doing it, but it's still pretty remarkable to watch her expression fall blank so quickly." with dissolve
    hide Mindtrick
    ks smile "You're done tidying. You want to play right now." with dissolve
    if hypnorepeat == True:
        n "{size=16}I'm done tidying. I want to play right now...{/size}"
    play music Inspiration fadein 5.0
    show NozomiBoardgame laugh
    n laugh "Actually, forget the tidying. Let's just play!" with dissolve
    $persistent.nozomi_boardgame_unlock = True
    scene bg blackscreen with dissolve
    "So we settle down on the floor, which is looking a lot more spacious now, and she gets straight to it."
    "Nozomi explains the rules to me quickly as she sets things up..."
    "It looks easy enough to follow, without seeming like a game for little kids and their parents."
    "This might actually turn out to be fun..."
    scene NozomiBoardgame2 hands_cards smug with longdissolve
    pause 1.0
    "Although nearly half an hour later I'm starting to rethink that." with dissolve
    "As Nozomi giggles and steals a card from me, it's dawning on me that Nozomi is a lot more competitive than she led me to think."
    ks casual sigh "Goddamn, Nozo. What happened to seeing people's faces light up when a game gets going?"
    show NozomiBoardgame2 smirk
    n side smile "Aww, you poor baby. Did you really think I'd go easy on you?" with dissolve
    show NozomiBoardgame2 laugh
    n front laugh "Ahaha, that's no fun at all!" with dissolve
    "Although it's my first time playing this, it's clear there's a little strategy involved in playing well. It's not just down to the luck of the dice roll."
    "Nozomi did give me a crash course to start, but her experience is clearly telling here. I'm getting pasted."
    show NozomiBoardgame2 smile
    "She's built up her settlements in a prime position, and maybe taken advantage of my naivety a little bit." with dissolve
    play sound diceshake
    "Like, some of the resource trades she made with me are feeling like they were a lot more beneficial to her than to myself."
    play sound diceroll
    "But she definitely IS lucky, too, as the seven she just rolled lets her move the bandit back over to my territory..."
    "... Right when the card she just picked randomly from me is most certainly one she'd need to upgrade another of her settlements."
    show NozomiBoardgame2 smug
    n side smile "I think at a time like this, it's important to remember it's more about having fun than winning, Kyou~" with dissolve
    ks sigh "Yeah, say that again when you're not winning so hard. Ugh."
    "She's gotten seven points by my reckoning, to my four. Although I bet she's hiding another point in her hand of advancement cards, so..."
    "A couple of lucky dice rolls is probably all she needs to get two more points and win this."
    show NozomiBoardgame2 smirk
    n front teasing "Stop stalling and roll. This'll be over soon enough." with dissolve
    play sound (diceshake, diceroll)
    "So I take the dice and roll for my turn..."
    show NozomiBoardgame2 laugh
    "It's a five. That's no good to me, but it lets Nozomi pick up an ore card from the pile, to go with the wheat she just stole from me." with dissolve
    ks frown "Sooo... you host a lot of board game nights, right? Are they all like this?"
    show NozomiBoardgame2 confused
    "Nozomi perks an eyebrow as she adds the card to her deck." with dissolve
    n "I'm surprised you know about those."
    "I only know because I overhear her talking about them at lunch sometimes... Maybe I shouldn't tell her that."
    ks smile "Oh, well... I figure you're not playing all these games by yourself, right?"
    show NozomiBoardgame2 smile
    n side smile_side "That's true. And as a matter of fact I hosted last weekend." with dissolve
    play sound (diceshake, diceroll)
    "As it's clear I can't do anything on my turn, Nozomi takes the dice and scatters them between us..."
    show NozomiBoardgame2 laugh
    "It's a six this time. Fuck, again?" with dissolve
    n "Ehehe, this'll be over sooner than I thought~"
    show NozomiBoardgame2 blank
    stop music fadeout 2.0
    if gesture == "hand":
        show Mindtrick awake wave at center:
            ypos 0.6
        with dissolve
        "As Nozomi gleefully reaches for the resource cards she just won, I frustratedly wave my hand over her eyes again."
    elif gesture == "forehead":
        show Mindtrick awake poke at center:
            ypos 0.6
        with dissolve
        "As Nozomi gleefully reaches for the resource cards she just won, I frustratedly reach out and press on her forehead."
    show Mindtrick entranced
    ks frown "You rolled a four." with dissolve
    hide Mindtrick with dissolve
    if hypnorepeat == True:
        n "{size=16}I rolled a four...{/size}" with dissolve
    else:
        pause 1.0
    play music Inspiration fadein 2.0
    show NozomiBoardgame2 surprised blush
    "Just then, Nozomi's outstretched hand freezes as her cheeks flush with embarrassment." with dissolve
    n "W-wait, what am I doing?"
    ks smirk "Giving me my cards?"
    show NozomiBoardgame2 confused
    "Nozomi awkwardly clears her throat and flicks a couple lumber cards my way, since she totally rolled a four after all..." with dissolve
    if hypno1 == "count":
        ks "I didn't think that number was still giving you trouble, Nozo."
        show NozomiBoardgame2 annoyed
        n irritated "Hah..." with dissolve
    hide NozomiBoardgame2
    show NozomiBoardgame2 hands_cards smile
    n smile noblush "But yes, you're right. I have people over every other week for a game or two." with dissolve
    ks smile "Do you get a lot of people at these things?"
    show NozomiBoardgame2 neutral
    n side smile_side "Hmm... I don't know about \"a lot\". It's usually me and a few girls from the literature club." with dissolve
    ks confused "Just the literature club? I thought, er..."
    show NozomiBoardgame2 sigh
    n front neutral "You thought Hiroko and Sayori would be part of this? I wish." with dissolve
    "Nozomi shrugs, then hands me the dice for my turn."
    show NozomiBoardgame2 frown
    n pout "Sayori's always too busy, and I know this isn't Hiroko's kind of thing." with dissolve
    ks neutral "Huh."
    show NozomiBoardgame2 neutral
    n neutral "Does that surprise you?" with dissolve
    ks "Well, I mean... they're always hanging around you so I thought..."
    show NozomiBoardgame2 confused
    n surprised "Hanging around me?" with dissolve
    show NozomiBoardgame2 neutral
    n side sad_side "Well, that's one way of looking at it, I suppose." with dissolve
    show NozomiBoardgame2 concerned
    n sad "You don't think I might be the one hanging around them?" with dissolve
    ks confused "Huh, what do you mean?"
    n "It's just..."
    "There's a silence as I wait for her to finish that thought, but it never comes."
    "Instead she looks at my clenched hand and frowns."
    show NozomiBoardgame2 frown
    n front frown "You've had those dice in your hands a while, Kyou." with dissolve
    ks "Uh... oh, yeah."
    play sound diceshake
    "Weird. And as I rattle the dice in my hand I try to think of something else to talk about."
    "If she won't say anything about her friends, then..."
    "... What was her mom telling me earlier?"
    "\"It's about time Nozomi invited a boy over.\""
    ks smile "So anyway, your board game nights... Is it like a girls only thing?"
    show NozomiBoardgame2 confused
    n surprised "Huh? Oh..." with dissolve
    show NozomiBoardgame2 smile
    "Nozomi chuckles." with dissolve
    n "I hadn't meant for it to be, but almost everyone at literature club is a girl, so that's how it worked out."
    show NozomiBoardgame2 smirk
    n teasing "Why? Don't tell me you're thinking of coming along to one of these." with dissolve
    ks frown "Wh- what would you say if I was?"
    show NozomiBoardgame2 smug
    n chuckle "I'd say you're full of it. Now roll the dice, please~" with dissolve
    "I guess she's got me there. I can't look like I'm enjoying myself playing this little game with her."
    play sound diceroll
    "But as I toss the dice to the floor again I think I might be coming around. I mean, maybe more for the company than the game itself."
    "... I guess I can see a little into why she plays these things, even as I pick up another sheep card from the deck."
    ks "Man, I got a ton of these damn things."
    show NozomiBoardgame2 laugh
    n happy "Ahahaha. At least your people will eat well~" with dissolve
    "Nozomi grins, as she scoops the dice in her hands."
    show NozomiBoardgame2 smile
    n side smile "You know, playing with you is making me think of how I nearly started a board game club in school. Back when we were first years." with dissolve
    ks smile "Yeah? Why didn't you?"
    "Nozomi shrugs as it's her turn to dwell on the dice."
    show NozomiBoardgame2 confused
    n frown_side "I was thinking of becoming a writer of some kind, so I figured I should tailor my after-school activities with that in mind." with dissolve
    show NozomiBoardgame2 neutral
    n front sleep "So I joined the literature club and that was that." with dissolve
    ks confused "Only thinking? Don't you write a lot?"
    play sound diceroll
    "Nozomi shrugs again as she lets the dice fall out of her hand and scatter on the floor."
    n neutral "I write a bit."
    "She passes the dice back to me as she talks, their faces having amounted to eight."
    "With the bandit still camped on the number eight spot, there's nothing to do this turn."
    show NozomiBoardgame2 sigh
    n side sad_side "I just do short stories when I feel like it. I don't know if I can progress that into a career somehow..." with dissolve
    show NozomiBoardgame2 concerned
    n sad "I'm not really sure what I'll do when I graduate, actually." with dissolve
    ks surprised "You're not? But we've got our entrance exams coming up."
    ks "We're... we're graduating in a few months and you really don't know?"
    show NozomiBoardgame2 angry
    n front angry "You don't think I know that?" with dissolve
    "... Did I actually strike a nerve that time? Over this?"
    show NozomiBoardgame2 frown
    "Nozomi might have seemed annoyed with me today over this or that, but I think this is the first time she's seemed genuinely upset." with dissolve
    show NozomiBoardgame2 annoyed
    n determined "And what about you? What are YOU doing when you get out of high school?" with dissolve
    ks "Uhh... w-well..."
    show NozomiBoardgame2 neutral
    "I honestly don't know either, and knowing it from my expression seems to satisfy her." with dissolve
    show NozomiBoardgame2 smug
    n side smile_side "See? It's pretty normal isn't it?" with dissolve
    show NozomiBoardgame2 frown
    n frown_side "As if we can just plot out our whole lives when we're still in our teens." with dissolve
    show NozomiBoardgame2 angry
    n front frown "It's a completely unfair expectation!" with dissolve
    play sound diceroll
    "I don't have anything to say to that, but it seems like she's just saying it out loud to reassure herself as I roll the dice."
    show NozomiBoardgame2 smile
    "We share a chuckle as I follow her eight with one of my own." with dissolve
    show NozomiBoardgame2 smug
    n smirk "Well, at least it turns out we do have something else in common, huh." with dissolve
    play sound diceroll
    show NozomiBoardgame2 smile
    "Nozomi then quickly throws the dice again, and gets to pick up an ore card." with dissolve
    "... Wait, doesn't that mean she's almost gotten enough to upgrade her settlement? I need to stop her."
    ks frown "Uh, how about a trade, Nozomi?"
    show NozomiBoardgame2 frown
    n frown "If you're thinking of palming off your sheep on me, you can forget it." with dissolve
    ks smirk "Aww, come on. They're the finest sheep in the land. And you can have one for the bargain price of... one ore?"
    show NozomiBoardgame2 annoyed
    n pout "Pfft, don't waste my time." with dissolve
    show NozomiBoardgame2 blank
    if gesture == "hand":
        show Mindtrick awake wave at center:
            ypos 0.6
        with dissolve
        "She says that, but I'm feeling bullish as I quickly pass my hand in front of her nose."
    else:
        show Mindtrick awake poke at center:
            ypos 0.6
        with dissolve
        "She says that, but I'm feeling bullish as I quickly reach across and press her forehead."
    stop music fadeout 2.0
    show Mindtrick entranced
    ks "You will agree to the deal." with dissolve
    hide Mindtrick with dissolve
    if hypnorepeat == True:
        n "{size=16}I will agree to the deal...{/size}" with dissolve
    else:
        pause 1.0
    play music Inspiration fadein 2.0
    show NozomiBoardgame2 sigh
    "Nozomi sighs as she takes her newly-acquired card between her fingers and offers it to me." with dissolve
    show NozomiBoardgame2 confused
    n pout "Oh, fine then. I suppose I can use one of those." with dissolve
    "I grin as I pass her one of my useless sheep in return."
    show NozomiBoardgame2 smug
    n laugh "Ehehehe..." with dissolve
    ks frown "What's so funny?"
    "Nozomi's grin spreads as quickly as mine fades."
    show NozomiBoardgame2 smile
    n side smile "Well I mean, I was thinking to drag this game out a little bit, before I changed my mind just now." with dissolve
    ks surprised "Huh?"
    show NozomiBoardgame2 smirk
    n front smirk "Kyou, you really haven't been paying attention." with dissolve
    show NozomiBoardgame2 hands_down
    "Nozomi chuckles as she lays down all of her resource cards to reveal a full set of items." with dissolve
    "The sheep was the only one she was missing until now."
    show NozomiBoardgame2 smile
    n happy "I was going to wait until I got one by myself, maybe give you a chance to put some points on the board..." with dissolve
    show NozomiBoardgame2 laugh
    n laugh "But if you're just going to let me have one then I guess I'll build this here settlement~" with dissolve
    ks frown "Ugh, come on!"
    "Nozomi giggles as she places another settlement on the board and puts all the cards in her hand away."
    ks "So is that it?"
    show NozomiBoardgame2 hands_up smug
    "She smiles and wags a finger at me." with dissolve
    n "Almost~"
    "It's as I suspected. She needs one more to win, and even my hypnotic cheating isn't stopping her."
    "I'll need to step it up as I pick up the dice and..."
    play sound doorknock
    show NozomiBoardgame2 surprised
    n side sad_side "Huh?" with dissolve
    nm "Nozomi? Kyou? Is it safe to come in?"
    "Nozomi scoffs at the door exasperatedly."
    show NozomiBoardgame2 angry
    n frown_side "O- of COURSE it's safe!" with dissolve
    play sound dooropen
    scene bg n bedroom day
    show Nozomi side casual frown_side at center
    with blink
    show Atsuko smile_side at center, flip:
        xpos -0.2
        linear 1.0 xpos 0.25
    "And with that the door swings open and Nozomi's mom is all smiles as she joins us inside."
    show Atsuko at flip:
        xpos 0.25
    nm laugh "Well you can't be too careful now~" with dissolve
    show Atsuko smile
    "Atsuko then looks over us, sat on the floor over this old game, and chuckles." with dissolve
    "I have a feeling she's not really surprised to find us like this."
    nm neutral_side "Anyway, I was about to do a little grocery shopping. Did you two want anything?" with dissolve
    n smile_side "Thanks, mom, but I'm good." with dissolve
    ks casual smile "Uh, yeah, I'm fine too."
    nm laugh "Suit yourselves~ Now behave while I'm gone, you two." with dissolve
    play sound doorclose
    scene NozomiBoardgame2 hands_down sigh
    with blink
    "And with that Atsuko leaves us be, and Nozomi sighs after her." with dissolve
    n "I was afraid she'd be like this."
    ks casual confused "... Is she normally like this?"
    "Nozomi glances back at the door with irritation."
    show NozomiBoardgame2 frown
    n annoyed_left "Not normally, but... mom was pretty excited when I said you'd be coming over." with dissolve
    show NozomiBoardgame2 annoyed
    n frown "I love her and all, but I really wish she'd step off about wanting to be a grandmother, you know?" with dissolve
    ks frown "Right... yeah."
    show NozomiBoardgame2 frown
    n front irritated "Well, at least she'll be out of our hair for a while." with dissolve
    "I let out an awkward chuckle as I reach for the dice."
    ks smile "Well, at least she cares about you, right?"
    show NozomiBoardgame2 smile
    n side smile_side "Of course. I don't want to complain about her too much." with dissolve
    n smile "My family's pretty great for the most part."
    ks "Yeah... must be nice."
    show NozomiBoardgame2 hands_up sigh
    n sad "Oh... sorry." with dissolve
    play sound diceshake
    "I give her a shrug as I rattle the dice in my hand."
    ks neutral "So what about the others? I haven't heard them around."
    show NozomiBoardgame2 smile
    n smile "Oh, dad's at work and my brother's out somewhere with his friends." with dissolve
    "Huh. So it's really just us in the house, then. At least for a little while."
    play sound diceroll
    "That sets my mind racing a little as I let the dice out of my hand and watch as they clatter on the floor."
    show NozomiBoardgame2 confused
    n surprised "Huh, a seven. We haven't had one of those in a while." with dissolve
    ks smile "Heh, yeah."
    show NozomiBoardgame2 smile
    "That lets me finally move the bandit out of my territory and plant it smack dab into Nozomi's." with dissolve
    "We've been moving that guy back and forth between these two spots all game."
    ks "So you owe me a card."
    show NozomiBoardgame2 smug
    n front teasing "Aw, too bad~ I used all of mine just now, remember?" with dissolve
    "I remember all too well, but as soon as I moved the bandit my mind continued to work."
    "And... well, after Nozomi told me more about what she's into, and the fact we're home alone..."
    "... I think it'd be okay to try something on her."
    "But if I'm going to do anything, it needs to be now."
    ks frown "But... but Nozomi, you don't really think the bandit's going to leave empty-handed do you?"
    show NozomiBoardgame2 neutral
    n neutral "What do you mean? There's nothing to steal." with dissolve
    ks neutral "That's not true. But sure, you're out of all the good stuff, and I bet the bandit's pissed about that."
    show NozomiBoardgame2 confused
    n pout "Well, that's too bad." with dissolve
    stop music fadeout 5.0
    ks smirk "I agree. It's too bad for YOU!"
    show NozomiBoardgame2 frown
    n frown "What are you talking about?" with dissolve
    "Okay, here we go."
    play music Downtown fadein 5.0
    ks smile blush "S-so he's pissed that he came all this way for nothing, but he gets an idea."
    ks "If he can't steal resources, then he'll steal people instead."
    show NozomiBoardgame2 annoyed
    n irritated "Again... what are you talking about?" with dissolve
    ks smirk "And... a-and who better to steal than the leader of the settlers?"
    n "..."
    show NozomiBoardgame2 surprised
    n surprised "Huh?!" with dissolve
    "Her momentary confusion makes me a little less sure of myself, but it's too late to stop now."
    show penlight at right with moveinright:
        ypos 0.346
    "And I think if I show her my penlight, it'd at least make my intentions a lot more clear."
    ks "Yeah, so he'd sneak into her encampment at night and kidnap her."
    ks "Probably tie her up real good before carting her off somewhere until he can get a ransom."
    hide penlight with moveoutright
    show NozomiBoardgame2 concerned blush
    "Nozomi starts to blush as she begins to realize where I'm going with this." with dissolve
    n "He'd tie her up, huh?"
    ks "Can't have her getting away now, can he?"
    show NozomiBoardgame2 frown
    n frown "W-well... it's not like she'd let herself get taken by any gruff highwayman, you know?" with dissolve
    show NozomiBoardgame2 angry
    n front frown "Any bandit who succeeds in kidnapping her would know to treat his captives with respect!" with dissolve
    show NozomiBoardgame2 frown
    ks smile "O-of course! He'd know better than to hurt her in any way. It'd be strictly business with this guy." with dissolve
    show NozomiBoardgame2 concerned
    n concerned "Right... Y-yes, strictly business." with dissolve
    "We hold each other's gazes for a moment, as if daring each other to back out of what's being negotiated here..."
    "... Only for Nozomi to bite her lip anxiously as she comes to a decision."
    n "W-well, he should hurry up and kidnap her, then. Before her soldiers have time to discover him."
    "Taking my cue, I hold my penlight aloft and switch it on with an audible click."
    "The noise alone is enough to trigger Nozomi's immediate attention as her eyes open and swivel upwards in anticipation."
    "And I'm only too happy to oblige her, as I start to sweep the familiar beam of light over her waiting eyes."
    show NozomiBoardgame2 concerned_light with dissolve
    show NozomiBoardgame2 concerned with dissolve
    ks smile noblush "Yeah, he should. And while he's doing just that, you should be following the light right now."
    show NozomiBoardgame2 concerned_light with dissolve
    show NozomiBoardgame2 concerned with dissolve
    hide NozomiBoardgame2
    show NozomiBoardgame2 hands_up neutral
    ks "Just following the light, Nozomi. Giving it all your focus for me. Letting yourself relax as you see those comforting patterns in your eyes again." with dissolve
    show NozomiBoardgame2 neutral_light with dissolve
    show NozomiBoardgame2 neutral with dissolve
    show NozomiBoardgame2 hands_down with longdissolve
    ks "That's right. It's very comforting and natural to stare into the light. You don't even have to think about it anymore." with dissolve
    show NozomiBoardgame2 neutral_light with dissolve
    show NozomiBoardgame2 neutral with dissolve
    show NozomiBoardgame2 sleepy with longdissolve
    ks "You just know instinctively how right this is."
    show NozomiBoardgame2 sleepy_light with dissolve
    show NozomiBoardgame2 sleepy with dissolve
    ks "So automatically finding your eyelids becoming heavy. So naturally feeling all the tension seep out of your relaxed body."
    show NozomiBoardgame2 sleepy_light with dissolve
    show NozomiBoardgame2 sleepy with dissolve
    "As I pass the light over her eyes again, I stop for a moment so I can shuffle up close to her before resuming."
    show NozomiBoardgame2 sleepy_light with dissolve
    show NozomiBoardgame2 sleepy with dissolve
    ks "Now Nozomi, while you're so naturally relaxed and focused under the light, I just need to tell you something."
    "Yeah, so I ended up reading a lot about the kind of stuff Nozomi might be into."
    "And one of the things that came up frequently was how it's important to make sure your partner trusts you."
    show NozomiBoardgame2 sleepy_light with dissolve
    show NozomiBoardgame2 sleepy with dissolve
    ks "Soon I'm going to be touching you in a few places."
    "I hasten to add:"
    ks surprised "N-nowhere bad, just so you know. Like, only your limbs and stuff."
    show NozomiBoardgame2 sleepy_light with dissolve
    show NozomiBoardgame2 sleepy with dissolve
    "I hope telling her my intentions didn't kill the mood as I sweep the light across her face again. Although she doesn't appear to be fussed."
    ks neutral "Is... is that okay? Just nod if it is."
    "Nozomi's quiet nod of her head is enough to calm my nerves, and I flash her eyes with the penlight again as if to reward her response."
    show NozomiBoardgame2 sleepy_light with dissolve
    show NozomiBoardgame2 sleepy with dissolve
    stop music fadeout 10.0
    ks smile "Good girl. Relaxing deeper. Letting yourself drop so deep for me."
    show NozomiBoardgame2 sleepy_light with dissolve
    show NozomiBoardgame2 sleepy with dissolve
    ks "Dropping so deep, letting those drowsy, sleepy eyelids close as you know they should."
    show NozomiBoardgame2 sleepy_light with dissolve
    show NozomiBoardgame2 sleepy with dissolve
    ks "That's right, very good. Going deeper."
    play music Flow fadein 5.0
    $persistent.nozomi_boardgame2_unlock = True
    scene bg blackscreen with dissolve
    "And with that, I wrap an arm gently around her shoulders as I can feel my heart pound."
    "I may have held her yesterday, but when she fell into my arms back then it was so sudden. I had no time to think about it when it happened."
    "This, I'm realizing, feels way more intimate."
    ks casual frown blush "Now sleep, Nozomi. Deep asleep."
    scene bg n bedroom day with dissolve
    "As I speak, I gently tug on Nozomi's shoulder, encouraging her to lean into me as I guide her to lay on the floor, setting her down on her side."
    ks casual frown blush "So deep asleep. So fully relaxed and so completely hypnotized."
    "Oh man, I had a good feeling that she'd be game for this, and I've never been happier for her to prove me right."
    "So okay, I'll just take her hands, gently pull her arms behind her back and hold her wrists together like this..."
    ks "And while you're this completely hypnotized, Nozomi, I want you to imagine how it must feel to be tied up in rope."
    "I give her wrists a gentle squeeze as I continue."
    ks "Feeling your wrists completely bound together like so."
    ks "You might try to pull your wrists apart when you wake, but the more you struggle to pull them, the more it feels that they're tied tightly together, unable to part."
    ks "So of course, it doesn't matter when I let go of your wrists, Nozomi. Your hands and wrists will still stay together because of all that thick heavy rope."
    "I can feel her arms tense as I pull my hands away, and rather than fall limply apart, Nozomi keeps her wrists touching just as I told her."
    ks smile "That's... that's right, Nozomi. Your wrists and arms completely bound in rope now, and we're gonna do the same to your legs."
    scene bg blackscreen with dissolve
    "Holding her hands felt nice, but touching her legs is definitely giving me another feeling."
    "... Especially as I can't help but catch a glimpse under her skirt while I'm doing it."
    "Fuck. Come on, I gotta behave myself."
    scene cg n bedroom floor day
    show NozomiHypnoBon
    with blink
    "So after giving myself a moment, I manage to arrange her limp legs so that they're curled up comfortably for her, with her feet collected side by side."
    "Drawing a shuddered breath, I look her over once more before putting my hands over her bare ankles, wrapping my fingers around them both as I speak again."
    ks casual frown blush "S-so now Nozomi, I want you to imagine those same ropes coiled around your ankles like this."
    "I give them a little squeeze for emphasis."
    ks "Nice and tight. Completely bound together just like your wrists."
    ks "And when you wake, you can struggle and pull all you like, but your legs and feet, so completely bound in this rope, cannot be parted."
    "I can once again feel the tension in her body. And I already know she's going to keep those legs together no matter what as I release them from my grasp."
    ks smile "Very... very good, Nozomi. Feeling so completely bound up in the rope now."
    ks "Feeling all that rope coiled around your body. The more you try to pull yourself free, the more the rope keeps you in place."
    "My heart's still pounding hard in my chest as I swallow dryly."
    "The anticipation of watching her come out of trance and accept this reality, just as readily as she's accepted everything else I've given her..."
    "I can hardly contain myself as I take a deep breath and begin the process of helping Nozomi wake."
    ks "And very soon it'll be time for you to come back from this deep hypnotic trance and realize what has happened to you."
    ks "So I'm going to count up to five, Nozomi, and just like before you're going to become more and more awake and aware and refreshed."
    ks "Fully waking and accepting your reality on five. Do you understand?"
    n "Y-Yes... I understand..."
    ks "I knew you would, Nozomi. I'm counting up now..."
    ks "One, taking a deep breath, feeling those tight ropes all over your body."
    ks "That's it... two, still very relaxed as you gently find yourself stirring back to life."
    ks "Three, taking another breath, becoming more and more aware, feeling your eyelids lighten."
    ks "Four, Letting those eyelids open up now, feeling so good. Feeling so right."
    n "Mmmn..."
    "I smile as I watch her face, then finally let her have it."
    ks "And five, wide awake Nozomi!"
    stop music
    n "Uhhh..."
    show NozomiHypnoBon raised surprised motionlines feet2
    n "H-huh?!" with dissolve
    "Even as I was expecting it, Nozomi's reaction still startles me when she comes to."
    play music Sad_Heroine
    show NozomiHypnoBon feet3
    "She tenses and strains, but she keeps her limbs firmly joined to each other while she struggles on the floor." with dissolve
    ks smirk "W-well, what did you expect?"
    show NozomiHypnoBon feet1 raised_blush
    n "Ahh, I don't know, I just... I-I-I didn't think you'd actually tie me up like this?!" with dissolve
    "I shoot her a look, and I'm about to point out the obvious when I stop myself."
    "Like, of course. I'm sure Nozomi knows deep down the restraints she feels over her body aren't actually there..."
    show NozomiHypnoBon feet3 ghostrope
    "But as far as her active imagination is concerned, those ropes in her mind are extremely, physically real." with dissolve
    ks smirk "What do you mean? That's the bandit's handiwork."
    show NozomiHypnoBon feet2 norope
    n "Agh..." with dissolve
    ks "Man, he did a number on you, huh?"
    show NozomiHypnoBon feet3
    n "S-s-so tight..." with dissolve
    "I can't disguise from her how much I'm enjoying this."
    "Her valiant struggles against her imagined bondage look little more than cute flapping of her hands and feet as she shuffles about on the floor."
    "And all the while her cheeks darken under my gaze as I stand over her."
    show NozomiHypnoBon angry feet1
    n "An- a-a-and you can stop looking at me like that, you pervert!" with dissolve
    "She's fucking adorable like this."
    ks "I'm not here to look at you, Nozomi. You're in the hands of the bandit now and he's taking you away."
    show NozomiHypnoBon feet3
    n "Ugh, come on Kyou, you've had your fun. Now untie me!" with dissolve
    ks "Not until the bandit figures out what to do with his captive."
    ks "I mean... he'll probably want to offload you quickly, since you're hot goods."
    show NozomiHypnoBon feet2
    n "Ugh, oh my GOD don't talk about me like that!" with dissolve
    ks "So surely the only person he can think of who'd want you is... your settler rival!"
    show NozomiHypnoBon resting noface feet1 nolines
    "Nozomi snorts in disgust, as she slumps back down on the floor for a breather." with dissolve
    "Clearly all that frantic struggling to free herself is taking its toll."
    n "Haaah... d-don't be ridiculous."
    ks "It's the most logical thing for the bandit to do! So he takes you to me and we agree a price."
    ks "And he sells you to me for the perfectly reasonable sum of..."
    "I laugh as I pick up one of my resource cards and mischievously toss it towards her face."
    ks "A single sheep!"
    show NozomiHypnoBon raised_blush angry feet3 motionlines
    n "O-OH MY GOD HOW DARE YOU!" with vpunch
    "Nozomi shrieks as she tenses back into life, but even with her renewed fury the ropes of her mind hold her in place as tightly as ever."
    ks "And now that I have you, I think it's time you told your people to stand down and declare me the winner in our little settler war."
    "She glares up at me and growls in righteous indignation."
    show NozomiHypnoBon feet1
    n "Ugh, no way. You're not even close to beating me!" with dissolve
    ks frown "Nozomi, you're in no position to negotiate with me, are you? You lost."
    ks "You just need to admit it, then I'll let you go."
    show NozomiHypnoBon feet2
    n "Never! I'm not losing a game to a filthy cheater!" with dissolve
    "I don't say anything for a few moments as I consider my options."
    "She's outraged, but is she really angry? Or scared?"
    show NozomiHypnoBon feet3
    "Could I push things just a little further?" with dissolve
    ks smirk "If you won't face facts, little lady, then I'm afraid we're gonna need to do something about that."
    show NozomiHypnoBon feet1
    n "Agh, w-what do you mean?" with dissolve
    ks "I'm talking about... punishment. Until you're singing me a different tune."
    n "WHAT?! NO!" with vpunch
    ks "Then accept my victory."
    show NozomiHypnoBon feet3
    n "I will {nw}"
    extend "NEVER accept this injustice!" with vpunch
    ks "Then you leave me no choice, Nozomi. I'm afraid you're gonna need to be..."
    menu:
        "Spanked":
            ks "Given a right and proper spanking, until you accept your defeat and admit I won fair and square."
            $hypno4 = "spank"
            show NozomiHypnoBon surprised feet1 nolines
        "Tickled":
            ks "Given a right and proper tickling, until you accept your defeat and admit I won fair and square."
            $hypno4 = "tickle"
            show NozomiHypnoBon surprised feet1 nolines
    "Nozomi's struggles cease momentarily, and she lets out a panicked squeak as I announce my intentions." with dissolve
    n "Y-y-you wouldn't DARE!"
    "Honestly, I'm surprising myself with all this, but her confession from last night is still ringing true in my head."
    "She WANTS to be controlled. She WANTS me to have the upper hand."
    "Like, even now she's still holding herself rigidly to the boundaries I've set in her mind."
    "She wouldn't allow that to happen if she was truly uncomfortable with this situation; I know that. But still..."
    "Just in case, and still thinking back to my late night research, I'll give her a little chance to put a stop to this."
    "Allow her one clear opportunity to take back control of her situation despite the helpless state she's in."
    ks neutral "N-now Nozomi, I wanna be real with you for a sec."
    ks "If you really, really don't want to go on, you need to tell me now, okay?"
    "Nozomi gives me the slightest of nods as her cheeks redden once more while I crouch down beside her and place a hand over her bare calves."
    "Our gazes meet, but Nozomi remains silent as she looks to me with trepidation."
    "She's... she's really not gonna say anything, huh?"
    "So then, steeling myself, I lean in towards her as I keep one hand on her legs as I announce my intentions..."
    ks smirk "Let's get you moved into a more comfortable position."
    $persistent.nozomi_hypnobondage_unlock = True
    scene bg blackscreen with dissolve
    play sound clothes
    n "K-Kyou?!"
    ks casual smirk "It's not like you can move yourself, all tied up as you are."
    "Nozomi squeaks as her struggles only serve to keep the illusion of her bondage, leaving her helpless to my carefully re-arranging her on the floor of her bedroom."
    scene NozomiHypnoBon2 kyou_blush with dissolve
    "... Like so."
    n "Ahh! Kyou, this isn't comfortable at all!"
    "And for her part, Nozomi still doesn't seem all that upset about her current situation if that's all she has to whine about."
    show NozomiHypnoBon2 kyou_smirk
    k "You're in a more comfortable position for ME, Nozomi." with dissolve
    k "Why should I care if you're comfortable? You're being punished."
    show NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines
    n "Nnnrgh..." with dissolve
    "Nozomi replies with a grunt as her body tenses and strains."
    show NozomiHypnoBon2 rope kyou_smile kyou_noblush
    "Those hypnotically-suggested ropes may have shifted position a little after I moved her, but as far as she's concerned they're still as inescapable as before." with dissolve
    show NozomiHypnoBon2 norope
    k "Now where were we..." with dissolve
    if hypno4 == "tickle":
        show NozomiHypnoBon2 kyou_smirk arm_tickle nozo_shocked
        "And without further warning, I run the fingertips of my free hand skittishly down the exposed soles of her feet." with dissolve
    elif hypno4 == "spank":
        "And without further warning, I swipe my free hand down to swat her backside over her skirt."
    if hypno4 == "tickle":
        show NozomiHypnoBon2 nozo_chuckle feet_squirm
        n laugh blush "Ahahah!" with vpunch
        k "Aw, look at that. Seems my rival's the ticklish type."
        "Heh, that's cute. I barely touched her and she's already letting out a hearty giggle."
        show NozomiHypnoBon2 nozo_growl feet_rest arm_up
        "Although my taunt buoys her a little, as her moment of weakness gives way to a determined growl while her body tenses defiantly." with dissolve
        "That determination, I note, still doesn't extend to her actually kicking her feet away or making any move to defend herself."
        k "You're not gonna try and kick me?"
        show NozomiHypnoBon2 nozo_mad
        n irritated "U-urrrgh... I AM trying, you jerk!" with dissolve
        k "Aw man, that doesn't sound like someone who's ready to give up. We need to do something about that, don't we?"
        show NozomiHypnoBon2 arm_tickle
        n angry "No you don't! I- {w=1.0}{nw}" with dissolve
        show NozomiHypnoBon2 nozo_annoyed nozo_blush feet_squirm
        $ renpy.transition(longdissolve, layer="master")
        extend "M-MmMMPTH!"
        "I purposefully wait for her protesting reply before I tease my fingertips gently down the length of her soles once more."
        "She puffs haughtily through her nose as she struggles not to give me the satisfaction of hearing her laugh again."
        "But I'm still barely stroking her skin here. How does she think she's going to hold out if I tickle her properly?"
        show NozomiHypnoBon2 kyou_laugh
        k "What's the matter, Nozomi? Anything I can do to cheer you up?" with dissolve
        show NozomiHypnoBon2 nozo_growl
        "Without waiting for an answer, I drag my fingers a little more forcefully towards her heels while she snorts at the floor." with dissolve
        n "Nnngh!"
        show NozomiHypnoBon2 kyou_smirk
        k "You know, you'd feel a lot better if you just admitted I beat you." with dissolve
        n "{cps=10}NNNN... N- {w=1.0}{nw}{/cps}"
        show NozomiHypnoBon2 nozo_giggle
        $ renpy.transition(longdissolve, layer="master")
        extend "SNNRRRRRK~"
        "This time I trace down the full length of each foot with a spidering motion as I up the intensity."
        "Now that she's started to crack, I decide that's enough playing around."
        "I want to make her laugh."
        k "Right? I knew you'd see the funny side."
        n "{cps=10}Shshsh... sh-shut {nw}{/cps}"
        show NozomiHypnoBon2 nozo_laugh
        $ renpy.transition(dissolve, layer="master")
        extend "AAHAHAHAHAHHAAAP!" with vpunch
        show NozomiHypnoBon2 kyou_smile
        k "Man, that's a cute laugh, Nozomi. I could listen to it all day." with dissolve
        show NozomiHypnoBon2 nozo_giggle
        n "Heeh... h-heeeeh~" with dissolve
        show NozomiHypnoBon2 kyou_laugh
        "I can't help but laugh a little with her as her breath catches, while she fights to control the giggles bubbling up inside her." with dissolve
        "But she's only able to fight at all because I slowed my pace down to a teasing crawl around the pads of her toes."
        show NozomiHypnoBon2 kyou_smirk
        "The moment I ramp up again..." with dissolve
        show NozomiHypnoBon2 nozo_laugh
        n cry_laugh "N-NOAHAHAHAHA!" with vpunch
        "It's like she comes with a volume control."
        n "Ahahahaha~ St-stohohohohop!"
        "Gotta admit, I'm a little curious to find out where else she's ticklish."
        "But I don't want to go too hard on her here. Like, what if I wind up touching somewhere I shouldn't?"
        show NozomiHypnoBon2 arm_up kyou_laugh
        k "If you're asking me to stop then does that mean you accept your defeat?" with dissolve
        show NozomiHypnoBon2 nozo_growl kyou_smirk arm_tickle
        n irritated "N-n-n..." with dissolve
        "I can tell what she's struggling to say, while trying to control her pained laughter, and I have no intention of allowing it."
        show NozomiHypnoBon2 nozo_laugh
        "So I punish her with a sudden direction change across the ball of her foot." with dissolve
        "And her defiant reply is lost in a girlish squeal that's loud enough to make me stop a moment."
        k "Then I guess I'm gonna hear your cute laugh some more, huh. That's too bad."
        n "AHAHAHAHA! HAHA! HAHAHAHAHA!" with shake
        "My short pause is enough for her to catch her breath, but not enough for her to answer me back as I run my tips teasingly along the sides of each foot in turn."
        show NozomiHypnoBon2 nozo_giggle
        n "Ehehehehe... eheh... e-ehehehehehee!" with dissolve
        k "Just tell me what I want to hear, Nozomi. It's all you've got to do."
        "Nozomi giggles and shakes her head, but we both know she's flagging."
        "All that struggling she did trying to break out of her \"ropes\" before, and now I'm making her laugh herself to exhaustion as I tickle over her quivering arches..."
        show NozomiHypnoBon2 nozo_laugh
        n "Nyayahahahaha! Haaah!" with dissolve
        "She's got to break. She has to."
        n "Pthh-okay! Hahahaha!"
        n "O-O-OKAY!" with vpunch
        show NozomiHypnoBon2 kyou_smile arm_up
        "Grinning widely, I withdraw my fingers just a little from her tortured feet." with dissolve
        show NozomiHypnoBon2 kyou_smirk nozo_sigh nolines feet_rest nozo_noblush
        k "Alright, Nozo. I'm waiting." with dissolve
        "She takes a shuddered breath as she composes herself..."
        show NozomiHypnoBon2 nozo_shocked arm_tickle feet_squirm nozo_blush
        "And just as she's about to speak, I give her soles a quick tap." with dissolve
        show NozomiHypnoBon2 nozo_chuckle arm_up kyou_smile
        "It makes her emit a panicked squeal as she hurries to breathe out her surrender." with dissolve
        n "Pffththth! Y-you win, Kyou. Ahahah..."
        k "So you're giving up?"
        show NozomiHypnoBon2 nozo_sigh feet_rest
        n "Haaah... y-yeah..." with dissolve
        k "I won fair and square, right?"
        n "*sigh* Right... Fair and square."
        show NozomiHypnoBon2 kyou_smirk
        k "I won, you lost. Say it." with dissolve
        n "... You won, I lost."
        k "And you proclaim me king of the settlers."
        show NozomiHypnoBon2 nozo_annoyed
        n irritated "Ugh, o-oh my god just take the win. Don't milk it." with dissolve
        show NozomiHypnoBon2 nozo_shocked arm_tickle feet_squirm
        "I can't resist giving her toes another sly teasing." with dissolve
        n "E-eep! I-I proclaim you king of the settlers now please stop!"
        $persistent.nozomi_hypnobondage_tickling_unlock = True
    elif hypno4 == "spank":
        play sound slap
        show NozomiHypnoBon2 kyou_smirk arm_spank nozo_shocked nolines
        n shocked blush "Y-Youch!" with vpunch
        show NozomiHypnoBon2 arm_up kyou_annoyed kyou_blush
        k "O-oh, come on, that wasn't even hard." with dissolve
        "Honestly, I think the anticipation of being spanked got to her more than my hand on her did."
        show NozomiHypnoBon2 nozo_growl kyou_noblush
        n front determined "That's SO not the point!" with dissolve
        show NozomiHypnoBon2 kyou_smirk
        k "And what WAS the point? Oh yeah..." with dissolve
        play sound slap
        show NozomiHypnoBon2 arm_spank nozo_shocked nozo_blush motionlines feet_squirm
        n irritated "E-Eep!" with vpunch
        "I put another, I think slightly harder, swat down on her rump."
        show NozomiHypnoBon2 arm_rest
        k "The point is you're not accepting your position, Miss Akemi." with dissolve
        show NozomiHypnoBon2 nozo_growl
        "Nozomi growls as she wriggles under my grasp." with dissolve
        "Her balled hands shake with impotent fury as she obviously attempts to part them so she can punch me or something."
        show NozomiHypnoBon2 arm_up kyou_blush
        k "See, that right there? That's bad." with dissolve
        n "{cps=15}K-Kyou I'm... nng, I'm warning y-... {w=0.5}{nw}{/cps}"
        play sound slap
        show NozomiHypnoBon2 arm_spank nozo_pain
        extend "AHH!" with vpunch
        "I slap my hand down swiftly, this time on her other cheek. It leaves a bunch of little prickling feelings on my palm that feels oddly satisfying."
        show NozomiHypnoBon2 nozo_mad arm_rest
        n determined "St-stop that!" with dissolve
        k "But... but, Nozomi, you're the one who can make this stop."
        show NozomiHypnoBon2 nolines feet_rest
        "I'm glad she can't see my face from here. I must be blushing pretty hard." with dissolve
        "Like, man, I don't know why I thought to suggest spanking her, other than I read somewhere that people who like being controlled can be into this kind of thing."
        "And for her part, Nozomi didn't straight up reject me treating her like this."
        "Her outrage seems kinda... half-hearted?"
        show NozomiHypnoBon2 nozo_growl
        n irritated "I'm not letting a cheater win, if that's what you mean." with dissolve
        "As she replies defiantly, I make a show of smoothing her skirt over to make sure it's covering her panties."
        "I mean, the thought occurred to me to go under the skirt but... I'm seriously pushing my luck enough as it is."
        n frown "Ugh, what are you even doing back there?!"
        show NozomiHypnoBon2 kyou_annoyed arm_up
        k "This? This is more about what you're NOT doing!" with dissolve
        show NozomiHypnoBon2 arm_spank nozo_shocked feet_squirm
        play sound slap
        n shocked "EEK!" with vpunch
        show NozomiHypnoBon2 nozo_grimace arm_rest kyou_noblush
        "My palm cracks down on her vulnerable backside and she winces audibly. She definitely felt that one." with dissolve
        n "Tststststs..."
        k "Tell me I won."
        show NozomiHypnoBon2 nozo_mad arm_up feet_rest
        n angry "Go to hell!" with dissolve
        show NozomiHypnoBon2 nozo_pain arm_spank feet_squirm motionlines
        play sound slap
        n pain "OW! {w=0.5}{nw}" with vpunch
        play sound slap
        extend "OW! {w=0.5}{nw}" with vpunch
        play sound slap
        extend "OW!" with vpunch
        show NozomiHypnoBon2 nozo_worried arm_up feet_rest nolines
        "I don't know if I'm settling into character or what, but her stubbornness is getting tiresome." with dissolve
        n concerned "Oh my god, Ky- {w=0.5}{nw}"
        show NozomiHypnoBon2 nozo_pain arm_spank feet_squirm motionlines
        play sound slap
        extend pain "YEOUCH!" with vpunch
        "I'm not sure how her ass feels after that, but my hand's sure starting to sting."
        show NozomiHypnoBon2 arm_up nozo_worried nolines feet_rest
        "So I withdraw my hold on her for a moment so I can rub my hands, which I'm thinking would also leave her a chance to pull away from me if she wanted." with dissolve
        "But although she groans and writhes beside me, her body and mind remain so resolutely disciplined to keep her mental bondage in place throughout."
        k "Now I think you have something to say to me, don't you."
        show NozomiHypnoBon2 nozo_annoyed
        "I can see her bite her lip as her rear tenses up again, like she's weighing up her options." with dissolve
        show NozomiHypnoBon2 arm_rest nozo_worried
        "And while she's doing that, I return my hand gently to her rump and give it a little stroke." with dissolve
        "Hopefully it'll convey just the right amount of menace to help her come to a decision."
        show NozomiHypnoBon2 nozo_sigh
        n sigh "O-okay, Kyou. No more. You win..." with dissolve
        show NozomiHypnoBon2 kyou_smile
        k "Fair and square?" with dissolve
        n "Fair and square..."
        k "And you proclaim me king of the settlers?"
        show NozomiHypnoBon2 arm_up kyou_smirk
        n irritated "That's... that's not a thing." with dissolve
        play sound slap
        show NozomiHypnoBon2 arm_rest nozo_shocked
        "I give her butt another, albeit more playful, smack." with dissolve
        n surprised "E-eep! I-I proclaim you king of the settlers now please stop!"
        $persistent.nozomi_hypnobondage_spanking_unlock = True

    stop music

    show NozomiHypnoBon2 kyou_nervous arm_up head_up feet_rest nozo_noblush nozo_noface noglasses
    play sound doorknock
    "Just then we're interrupted by an obnoxious knocking on Nozomi's door." with dissolve
    nm "Safe to come in?"
    hide NozomiHypnoBon2
    show NozomiHypnoBon2 kyou_nervous
    "Nozomi's about to answer, only to cut herself off as she remembers her present situation." with dissolve
    n "{size=16}K-Kyou... help me up?{/size}"
    scene bg n bedroom day
    show Nozomi front casual concerned blush at center:
        ypos 1.4
        linear 2.0 ypos 1.1
    with blink
    "She whispers to me, and I hurriedly lift her up by the shoulder and set her rigid form so that she can sit up on her knees."
    show Nozomi:
        ypos 1.1
    "That can't be very comfortable for her, but if Nozomi's still going to keep her hypnotic bondage in her mind, it's the best we can do."
    nm "Nozomi? You in there?"
    n sigh "Y-yeah, sorry. Come in." with dissolve
    play music Dating3
    play sound dooropen
    show Atsuko laugh at center, flip:
        xpos -0.2
        linear 1.0 xpos 0.25
    nm "My, you had me worried for a moment there~"
    show Atsuko at flip:
        xpos 0.25
    "Atsuko gleefully lets herself back into Nozomi's room, surely triumphant from her grocery shopping."
    "If only either of us heard her re-enter the house while we were horsing around..."
    "How much did she hear of us just now?!"
    nm smile_side "So? How's the game going?" with dissolve
    n pout_left "A-ah, well... we just finished." with dissolve
    "Nozomi looks down at the game board, which is in a little disarray after she'd been thrashing around it, then shyly looks to me."
    n concerned "Kyou won..." with dissolve
    nm laugh "Did he now? Well, I do think congratulations are in order~" with dissolve
    "If Atsuko has picked up on the state of play at all, she doesn't show it as she laughs cheerfully."
    nm smile "And such perfect timing. I went a little overboard on the food just now, and it's around about lunchtime, so..." with dissolve
    nm happy "How about joining me downstairs? I'll fix you both something nice~" with dissolve
    "Heh. Nozomi's mom is just itching to know more about me. And us."
    "And to be honest, I think the pair of us could use a change of pace right about n-{w=1.5}{nw}"
    n chuckle noblush "Actually... Kyou needs to leave shortly." with dissolve
    nm surprised_side "Oh?" with dissolve
    "She's not the only one who's surprised as I look to Nozomi anxiously."
    "Like, shit, did I seriously piss her off with all that stuff just now?"
    "But I thought..."
    n pout_left "Yeah... that's why we wrapped up." with dissolve
    ks casual neutral noblush "Y... yeah..."
    "My mind's still reeling, but I know arguing in front of her mother would just make things worse."
    n smile "Maybe some other time, okay mom?" with dissolve
    nm happy "Of course. Another time." with dissolve
    nm smile "So I suppose I'll leave you to it. But Kyou, it was good to meet you." with dissolve
    nm laugh "Don't be a stranger, okay?" with dissolve
    hide Atsuko with dissolve
    play sound doorclose
    "And with that, Atsuko sees herself out, leaving an uneasy atmosphere in her wake."
    ks confused "Nozomi... did I... anger you?"
    show Nozomi surprised
    "Nozomi's eyes widen as I address her, and she suddenly shakes her head vigorously." with dissolve
    n "Oh gosh, Kyou, no. No."
    n sigh blush "I..." with dissolve
    show Nozomi:
        linear 1.0 ypos 1.2
    "She lets out a quiet moan as she flops back down on the floor, still very much locked in her bondage pose."
    show Nozomi:
        ypos 1.2
    n "Everything we just did. You made me feel so powerless and yet..."
    n concerned "And yet you never gave me a reason to fear it. Only embrace it..." with dissolve
    n "So, Kyou, I loved what we just did. I really mean that."
    n laugh blush "And... A-and you might have given me a thing for being a damsel in distress. Ahaha~" with dissolve
    ks "So... so why?"
    n sleep noblush "Why am I kicking you out?" with dissolve
    "She draws out a sigh as she looks across the floor full of spent playing cards."
    n concerned "It's like I said before, Kyou. I'm not looking to date anyone." with dissolve
    n sigh "And you saw how my mom was being. I..." with dissolve
    n neutral "I really, really don't want to get her hopes up about us." with dissolve
    "Goddamn, this is..."
    "She's so fucking confusing."
    "I'd forgotten all about her \"no dating\" rule while we were playing, but come on."
    "After all we just did, isn't she at least thinking about us hooking up for real?"
    n sigh "You... you understand, right, Kyou?" with dissolve
    "I don't. I don't get this at all."
    ks sigh "Uh..."
    n concerned "Anyway, I think it's time you untied me, don't you?" with dissolve
    ks confused "Huh? But..."
    "Oh. Oh right, even after everything she's as \"tied-up\" as ever."
    ks neutral "Yeah. Yeah, of course."
    show Nozomi front chuckle noblush at center
    with longblink
    "So I had to put my thoughts aside for a while as I took Nozomi back under and had her disappear the ropes of her mind."
    show Nozomi laugh
    "She can't hide her glee as she stands to her full height and stretches up towards the ceiling with her back arched." with dissolve
    n "Ahh, that feels so good~ {font=DejaVuSans.ttf}♥{/font}"
    "I give her a moment to get it out of her system, while my thoughts turn back to how she confuses me."
    "Nozomi... she's nothing like the pure, infallible class rep I imagined her to be. I made peace with that yesterday."
    "But the real Nozomi still feels every bit as untouchable, even as close as we've become."
    n smile "So I think we both had a lot of fun today." with dissolve
    ks smile "We... we did, yeah. Didn't realize board games could be so, uh..."
    ks "Immersive."
    show Nozomi side laugh
    "Nozomi giggles." with dissolve
    n smile "Someday I'll get you into board games properly, but..." with dissolve
    n smile_side blush "Yes, that was something else." with dissolve
    n front smile noblush "But most of all, Kyou, I hope I've shown you how serious I am about us." with dissolve
    "Well, I mean..."
    n sigh "I want you in my life. I want us to be friends." with dissolve
    "I want us to be more than friends."
    "Like, shit, is what we did even something \"friends\" do?"
    n side frown_side "And I don't want to be ashamed of us." with dissolve
    n sad "I just wish I knew this about you sooner instead of you... W-well..." with dissolve
    n sad_closed "Never mind." with dissolve
    ks casual smile "Yeah... Well, we can make up for lost time, can't we? There's still tomorrow."
    n sad_side "Tomorrow..." with dissolve
    "Yeah. Even if she's sticking to the \"friends\" talk she has to be rethinking it."
    "She's stubborn, but she has to be coming round the more I show her of me. Bit by bit."
    n front concerned "Actually, Kyou, tomorrow is- {w=1.0}{nw}" with dissolve
    if gesture == "hand":
        show Mindtrick awake wave at center:
            ypos 0.6
    elif gesture == "forehead":
        show Mindtrick awake poke at center:
            ypos 0.6
    stop music fadeout 2.0
    show Nozomi entranced_neutral
    ks "You want to visit me tomorrow morning." with dissolve
    show Mindtrick entranced
    "And nothing makes me more certain of that than knowing she keeps letting me get away with this." with dissolve
    if hypnorepeat == True:
        n "{size=16}I want to visit you tomorrow morning.{/size}"
    hide Mindtrick
    n smile "Tomorrow is good. I'll swing by yours again in the morning, okay?" with dissolve
    stop music fadeout 5.0
    scene bg street1 day with blink
    "So we say our goodbyes for now and I head back home full of hope."
    scene bg k bedroom eve with longblink
    play music Past_Sadness
    "Nozomi Akemi. Maybe you're not the picture of feminine perfection I imagined you were."
    "You're as beautiful as you ever were but also..."
    "The fact is that you really are weird, and nerdy and at least a little bit perverted..."
    "I never knew girls like you existed. But..."
    stop music fadeout 5.0
    "It feels like I'm falling in love with you all over again."
    scene bg blackscreen with longdissolve
    pause 2.0
    jump Day7_Con_Kyou_Nozomi_Trance

label Day6_Con_Kyou_Nozomi_Zombie:
    scene bg shopping2 day with longdissolve
    "When morning comes, I find myself walking at a brisk pace."
    queue music Dating3
    "Nozomi texted me again last night, insisting I stop by late in the morning."
    scene bg n house day with blink
    "So here I am. Rolling up at this unfamiliar street at ten o'clock, and all of a sudden I stop dead in my tracks."
    "There's that feeling again. What if this really isn't her house?"
    "I don't want to knock on some stranger's door and get into that kind of situation..."
    "But I don't want to back out either."
    "Dammit. If Nozomi wasn't being so shifty I'd never be doubting her like this..."
    show Nozomi front casual sleepy noglasses bruise at center
    n "Kyou? That... is you, isn't it?" with dissolve
    "Just then I realize the door in the distance has pulled open, revealing a familiar figure squinting at me from inside."
    ks casual surprised "N-Nozomi..."
    "So she really did mean for us to meet. That's reassuring, at least."
    n irritated "... Are you just going to stand there or do you want to come in?" with dissolve
    scene bg n room day
    show Nozomi front casual concerned noglasses bruise at center
    play sound doorclose
    with blink
    "Stepping inside the spacious-looking house, I pop my shoes off while Nozomi watches me anxiously."
    show Atsuko smile at center, flip:
        xpos 0.25
    "In the meantime we're joined by someone else, who I can only assume is Nozomi's mother." with dissolve
    $ nm = Character(_("Nozomi's Mom"), image = "Atsuko", who_color = "#826B81")
    nm laugh "Welcome, Kyou! Nozomi told me we'd be having company today~" with dissolve
    "This looks to be someone who doesn't get anxious a lot."
    ks casual smile "N-nice to meet you..."
    "Mrs. Akemi? I'm about to say, before she happily introduces herself."
    $ nm = Character("Atsuko", image = "Atsuko", who_color = "#826B81")
    nm smile "Atsuko. It's a pleasure~" with dissolve
    nm smile_side "I believe you've met my daughter." with dissolve
    show Nozomi side rolleyes
    "Nozomi rolls her eyes." with dissolve
    n "Yes, mom. Kyou's a classmate of mine."
    nm laugh "And that's wonderful~ It's nice to see who else you spend time with, Nozomi." with dissolve
    nm smile "Anyway, make yourself at home, dear." with dissolve
    "Atsuko smiles, and I smile politely back."
    ks "Thanks."
    show Nozomi sad
    "It feels weird, to think out of the two of them that she seems happier to see me here than her daughter." with dissolve
    "I guess it's awkward that I'm meeting Nozomi like this, but still..."
    show Atsuko smile_side
    n smile_side "S-so like I was telling you mom, Kyou's here to help me with a... um, class project. And we have a lot of ground to cover, you know?" with dissolve
    nm happy "Oh, of course. Don't let me keep you!" with dissolve
    "Taking my penlight to play with is a \"class project\", huh?"
    nm laugh "Just promise me you'll behave yourselves while I go food shopping~" with dissolve
    n frown_side blush "O-of COURSE we'll behave ourselves!" with dissolve
    hide Atsuko
    "Nozomi scoffs as her mother chuckles to herself and makes ready to leave." with dissolve
    n frown "Let's go, Kyou." with dissolve
    scene bg blackscreen with dissolve
    "And with that, Nozomi ushers me upstairs."
    scene bg n bedroom day
    play sound dooropen
    with blink
    "Leading me to..."
    ks casual confused "This is your room?"
    show Nozomi casual front irritated noglasses bruise at center with dissolve
    play sound doorclose
    "Nozomi lets out a little snort as she pulls the door closed behind her."
    n "Yeah, yeah, don't judge me."
    "My eyes can't help but give her room a thorough looking over..."
    ks sigh "There's stuff everywhere."
    "Like, where to begin? If it's not clothes dumped on the floor, it's piles of cardboard boxes... board games?"
    n front2 annoyed_left "Yeah... I know." with dissolve
    show Nozomi neutral
    "Wow, there's a TON of board games here. From simple card games to some really obscure-looking advanced stuff." with dissolve
    "It's not what I expected from a girl's bedroom, that's for sure."
    n pout "A-Anyway, I've had more important things to worry about, like..." with dissolve
    "I knew she hosts board game nights, but I had no idea she was this serious about it."
    stop music fadeout 5.0
    n concerned "Er, Kyou?" with dissolve
    # "Oh, right. While I was busy examining her messed-up room, Nozomi had sat down on her bed."
    ks frown "Oh... y-yeah. More important things."
    queue music Downtown
    "I got so caught up in the experience of being in Nozomi's bedroom that I forgot for a moment why I'm even here."
    "But to get to the point, Nozomi pulls open her desk drawer and, with some seeming reluctance, takes out a familiar object..."

    # "Just then, her hand slides with some reluctance towards her pillow, reaching underneath it before pulling back holding a familiar object..."
    show penlight at right with moveinright:
        ypos 0.346
    "That's it all right. My penlight doesn't look any different to all the others of its kind, but she couldn't have found a copy of that exact model so quickly."
    "... That I even considered she could be deceiving me sure is a depressing thing to think about."
    # n side sad "I'm... I'm sorry I pushed you into letting me have this. But I wanted to
    n side sad "You... said you made this, right?" with dissolve
    hide penlight at right with moveoutright
    "I frown at her and nod."
    ks frown "Yeah. Well, it's an off-the-shelf medical penlight that I modified a little."
    n sad_closed "Right. So, uhh..." with dissolve
    "I might still be annoyed about what she pulled the other day, but I can't deny I'm also really interested to hear what she did with my penlight while she's had it."
    ks neutral "What is it?"
    show Nozomi sad_side
    "Nozomi looks anxiously at the penlight in her hand as she begins to answer." with dissolve
    n front concerned "Okay, so... when I got back home, I was starting to feel silly for making such a big deal about this thing." with dissolve
    n neutral "But after dinner, I locked myself in this room and... I switched it on." with dissolve
    n neutral_left "And I... w-well..." with dissolve
    ks frown "You tried shining the light in your own eyes."
    n front2 sleep "Mhm..." with dissolve
    "I mean, what else was she going to do with it?"
    scene bg blackscreen with dissolve
    play sound sitting
    pause 0.5
    scene NozomiBedroom1 neutral bruise arm_up shadow with longdissolve
    "Just then, Nozomi falls back onto her bed and holds the penlight up in front of her."
    show NozomiBedroom1 frown
    n frown "I laid down and held it at arm's length, like this. I was trying to shine it back and forth over my face, just like you did." with dissolve
    show NozomiBedroom1 neutral
    n neutral "But as soon as the light hit my eyes, I felt instantly drawn to it. Just like before." with dissolve
    show NozomiBedroom1 sleep
    n sleep "After that... it was almost automatic." with dissolve
    show NozomiBedroom1 concerned
    n sleeptalk "I kept moving the light over my eyes, feeling kinda relaxed about the whole thing." with dissolve
    show NozomiBedroom1 neutral
    n sleeptalk_concerned "So I kept doing it, and I think at some point a light must have switched off in my own head." with dissolve
    show NozomiBedroom1 sigh
    n concerned "Because the next thing I remember, I was crying out after I dropped the penlight on my face." with dissolve
    ks casual confused "You... dropped it on your face?"
    show NozomiBedroom1 pout blush
    n sleeptalk_concerned blush "T-that's what I said." with dissolve
    hide NozomiBedroom1
    show NozomiBedroom1 concerned_side bruise arm_down shadow
    n pout_left "A-anyway, after that I put your penlight in my desk drawer and I didn't dare use it again." with dissolve
    show NozomiBedroom1 pout
    n pout "I mean... I proved what I wanted to prove, anyway." with dissolve
    ks neutral "And what was that?"
    show NozomiBedroom1 concerned arm_up
    "She sighs and holds the penlight up to her face again." with dissolve
    # show Nozomi concerned noblush
    # "She sits back up and faces me, crossing her legs as she brings the penlight in her hand down to rest uncomfortably in her lap." with dissolve
    n "I managed to deeply hypnotize myself with barely any effort at all. Without you or anyone else guiding me. Just this penlight."
    n "But what would have happened if I heard someone talking while I was spacing out like that?"
    show NozomiBedroom1 concerned_side
    n sleeptalk_concerned "Might I have taken their words into my subconscious and acted on them?" with dissolve
    show NozomiBedroom1 surprised arm_down
    n surprised "Or what if I left the tv on? I could've woken up and gone right outside to buy some of that limited edition french toast flavour ice cream they've been pushing lately!" with dissolve
    ks "Y-yeah... that would've been awful."
    show NozomiBedroom1 afraid
    n shocked "W-what would've happened if I didn't drop the penlight on my face? I could've been stuck in a trance until someone broke into my room and woke me up!" with dissolve
    ks sigh "Oh come on, Nozomi, you know that's..."
    show NozomiBedroom1 frown_side
    "Nozomi frowns at me and at the same time I stop what I'm saying." with dissolve
    n "Impossible. Except we know it's not. Not after what's been happening to me."
    n "The night of the dead changed everything."
    ks confused "Is that what we're calling it now?"
    show NozomiBedroom1 sleep
    n side neutral_side "Call it whatever you want, but you know I'm not just fantasizing about how dangerous hypnosis is." with dissolve
    # n "Yeah, you understand what I'm saying, don't you? I'm not just fantasizing about how dangerous hypnosis is."
    show NozomiBedroom1 concerned arm_up
    n front surprised "This light really IS the reason your hypnosis worked so well on me!" with dissolve
    show NozomiBedroom1 frown
    n shocked "It's the reason I stayed like a zombie no matter how much pain I was in. It HAS to be!" with dissolve
    # Nozomi's hunch about the penlight was right. She's proved it to himself, can Kyou believe her too?
    "If it wasn't for the other night, I would've thought Nozomi was just letting her imagination get the better of her."
    "But I have to believe that Nozomi really is experiencing a deep form of hypnotic suggestibility that I hadn't thought possible."
    # I don't know, maybe he still has some trouble believing it
    "And that my penlight was what brought it about."
    show NozomiBedroom1 concerned_side arm_down
    n concerned "I just... I just don't understand how you made something like this." with dissolve
    "It begs the question, though:"
    # "*** AUTHOR'S NOTE - The dialogue past this is gonna be extremely rough and ready."
    # "I hate to do it, although it's a more effective a writing technique than agonizing over every single line; I can edit everything later. Here we go! ***"
    ks sigh "If you really suspected it was so dangerous why did you take it to use on yourself?"
    show NozomiBedroom1 frown_side
    n frown "Because I could hardly believe what had happened. I needed proof." with dissolve
    show NozomiBedroom1 frown
    n irritated "And I couldn't trust your opinion. I thought you had to be hiding something from me." with dissolve
    ks frown "You don't trust me?"
    show NozomiBedroom1 concerned
    n side sad_side "I didn't..." with dissolve
    "She sighs."
    show NozomiBedroom1 sigh
    n sad_closed "You have to understand. I hardly know you, and you show up and just casually mention hypnosis like you wouldn't think it'd pique my interest." with dissolve
    show NozomiBedroom1 afraid
    n sad_side "And more than that, you have this strange light that affects me as much as this and it's just..." with dissolve
    show NozomiBedroom1 surprised
    n sad "You made it yourself! You HAD to know what it was capable of!" with dissolve
    # n frown "Because I had to know for sure. And I took it because I didn't think I could trust you!" with dissolve
    # n side sad_side "You made this thing. You must have known what it was capable of, right?" with dissolve
    ks sigh "I made it to help catch people's attention, I didn't think it'd work as well as this!"
    show NozomiBedroom1 pout
    n sad_closed "Yeah... After I thought about it some more, I had to wonder how much you really knew." with dissolve
    show NozomiBedroom1 neutral
    n "And I realized if you actually knew what this thing could do, a lot of things would be different." with dissolve
    show NozomiBedroom1 sigh
    n sad "You wouldn't have let me leave with your penlight if you knew how powerful it was, no matter how many ultimatums I gave." with dissolve
    show NozomiBedroom1 neutral_side
    n front sleeptalk_concerned "So I'm sorry, Kyou. I was scared, but I should've been more honest about my feelings and what my intentions were." with dissolve
    "I nod. I'm not really that mad at her anymore, now that I've heard her out."
    "But still, it does leave us in a weird place..."
    ks neutral "What do we do now?"
    show NozomiBedroom1 concerned
    n front concerned "Well, I was thinking..." with dissolve
    play sound doorknock
    stop music
    show NozomiBedroom1 surprised
    "Just then, there's an obnoxious knocking on the bedroom door." with dissolve
    nm "Nozomi? Kyou? Is it safe to come in?"
    n "U-uh..."
    $persistent.zombie_bedroom_1_1_unlock = True
    scene bg blackscreen
    play sound sitting
    with dissolve
    scene bg n bedroom day
    show Nozomi side casual neutral noglasses bruise at center
    with dissolve
    "Nozomi looks to me and puts a finger to her lips as she hops off her bed."
    show Nozomi neutral_side
    "She then hurriedly stuffs the penlight back in her desk drawer before sliding it shut and looking to the door." with dissolve

    # "Nozomi quickly hops off the bed and hurries to the door, but not before sparing me a glance and holding a finger to her lips."
    # show Nozomi:
    #     ypos 1.0
    n smile_side "Sure, come in!" with dissolve
    play sound dooropen
    show Atsuko smile_side at center, flip:
        xpos -0.2
        linear 1.0 xpos 0.25
    play music Inspiration
    "The invitation barely leaves Nozomi's mouth before the door swings open and a smiling Atsuko strolls inside." with dissolve
    nm "Sorry for barging in on you two. Hope I wasn't interrupting anything~"
    show Atsuko at flip:
        xpos 0.25
    show Nozomi sad_closed
    "Nozomi sighs." with dissolve
    n "No, mom. Me and Kyou were just talking."
    ks casual sigh "Y-yeah. About the project."
    nm neutral_side "All going well, I hope?" with dissolve
    show Nozomi sad
    ks neutral "Uhh... good. Yeah, good." with dissolve
    n neutral_side "We were just going over some things, mom." with dissolve
    show Atsuko laugh
    "Atsuko giggles mischievously." with dissolve
    nm "Alright~ But do take a break some time, okay? I got some snacks for the fridge."
    n smile_side "Thanks, mom. We'll be down for lunch in an hour." with dissolve
    nm smile "Wonderful! Well then, I'll leave you to it~" with dissolve
    hide Atsuko with dissolve
    play sound doorclose
    stop music fadeout 10.0
    "Atsuko closes the door behind her as she leaves us be."
    ks smile "Your mom seems nice."
    show Nozomi smile
    "Nozomi smiles faintly." with dissolve
    queue music Downtown
    # n sad "She is, even if she smothers me and Ichiro a bit." with dissolve
    n "She is, although she can be a bit much sometimes."
    ks neutral "Yeah?"
    n sad_side "I mean, you saw her just now. She couldn't wait to get involved with us!" with dissolve
    n front pout "I get why she still smothers Ichiro so much, but I'm eighteen years old! I'm not a kid anymore!" with dissolve
    ks neutral "Ichiro?"
    "I'm sure that's a name I haven't heard before."
    n smile "Oh, right. He's my little brother." with dissolve
    "Nozomi smiles again; more brightly this time."
    n side smile "You might have met him, actually. He's a first year at our school." with dissolve
    ks smile "Oh, huh."
    "I don't really know what to say to that, but she's quick to move on."
    n front chuckle "Anyway..." with dissolve
    show penlight at right with moveinright:
        ypos 0.346
    show Nozomi front2
    "Nozomi pulls her desk drawer open and takes my penlight back out of there..." with dissolve
    "... and then hands it to me."
    n front2 smile "Thanks for letting me borrow this. But I think it's better if you had it back." with dissolve
    hide penlight at right with moveoutright
    "I take it from her, although it feels a bit weird now, after what we've been talking about before her mom stepped in."
    n neutral_right "And there's something else I decided." with dissolve
    ks smile "What's that?"
    n sleep "I want to change rule number three." with dissolve
    ks confused "Huh?"
    "Rule number three? Then she means..."
    n neutral "Now that we know what your penlight can do, I don't think we should try any hypnosis at your place anymore." with dissolve
    ks "Then..."
    n neutral_left "We'll do it here instead." with dissolve
    ks "Huh? But aren't you worried your mom will find out about your secret?"

    # n side neutral_side "At least now if something happens, there'll be someone nearby who can help." with dissolve
    n sleeptalk_concerned "I am. But I've given this a lot of thought, and if we're going to keep doing hypnosis together then I have to think about my own safety." with dissolve
    "Her own safety?"
    n "Knowing there's someone else in the house who can help if things go wrong... i-it just seems like the smart thing to do."
    ks frown "What, so you still don't trust me?"
    "Nozomi sighs irritatedly."
    n front annoyed_left "Look, it doesn't matter if I trust you or not. We've seen what your penlight can do to me, even if you didn't mean it to." with dissolve
    n neutral "We know it's dangerous, and knowing what I do now, it's made everything I've done with you so far really scary..." with dissolve
    n front frown blush "But I also won't deny it's given me the best experience of hypnosis in my entire life." with dissolve
    ks confused "S-so, what are you saying?"
    n sleeptalk "I'm saying... I want us to try doing more things with your penlight. It's dangerous, but we know to be more careful now." with dissolve
    n frown "And I feel there are so many unanswered questions about it." with dissolve
    n side neutral "Like is it just me who's affected by your penlight so extremely, or will it do the same for others?" with dissolve
    n sad_side "But more importantly... can we use it to achieve a state of hypnosis and induce suggestions that doesn't end up hurting me? O-or anyone?" with dissolve
    n sad_closed "Because I really want to believe we can." with dissolve
    n sad "But what do you think, Kyou? You've made something... amazing." with dissolve
    "Looking down at my penlight, I start to feel a little sense of pride."
    n front smile "Do you want to find out more about it with me?" with dissolve
    "And as I look to her, I'm feeling a rush of excitement."
    # n front concerned "Don't you want to know more about what it can do?" with dissolve
    ks smile blush "Yeah. Of course that's what I want."
    "We smile at each other in silence for a moment."
    "It's been an awkward few days between us, but right now it feels like we're starting to understand each other."
    show Nozomi neutral noblush
    "Nozomi's eyes start to wander from me to the penlight now in my hands." with dissolve
    n "Okay then, so first... I think it'd be a good idea to review what we DO know about this thing."
    "I nod in agreement as I turn my penlight over in my hand."
    ks neutral noblush "Right. So like I said, this is an off-the-shelf medical penlight that I bought from the internet."
    ks "It was pretty cheap, which was important since I was gonna take it apart and maybe break it."
    n frown "So that also means there's nothing special about the light itself, I guess?" with dissolve
    ks neutral "Yeah. The intensity and beam width are pretty standard."
    n side neutral_side "Okay. So what's special about the pattern you put on it?" with dissolve
    ks frown "I... It's a little complicated, I guess. I don't think it looks like anything in particular."
    n neutral "And that's why you thought it'd catch the eye so well? Because it doesn't look like anything?" with dissolve
    ks neutral "Yeah. I figured it'd engage a person's natural curiosity so they're more inclined to focus on it and facilitate them going into a hypnotic state."
    ks "I have no idea why it works on you as well as it does, though."
    show Nozomi front2 sleep
    "Nozomi strokes her chin thoughtfully." with dissolve
    n "I wonder if there could there be a way to make it work... less well?"
    ks confused "What do you mean?"
    n pout_left "Like... could you turn down the intensity of the beam, maybe?" with dissolve
    ks neutral "No. Like I said, it's a basic penlight. It just switches on and off, that's all."
    n neutral "Hmm..." with dissolve
    n front2 frown "What about if you put that pattern onto a different model of penlight? One that you CAN adjust or has a weaker beam to start with?" with dissolve
    "I let out a little groan."
    ks sigh "I could try but it'll take ages."
    ks "I'll probably have to buy it online again so that'll be a couple days, then I gotta take it apart and try to make it emit the same pattern as this one."
    n side sad_side "Right... And then it might not even work at all." with dissolve
    ks frown "Yeah. I mean, the patterning's gotta be important, but we don't know if it's the only reason it works this way."
    ks "Maybe the light intensity and width are exactly what they need to be so we can't deviate."
    ks "Or maybe there's something else that's special about this particular light that we don't know about."
    "Nozomi nods with a sigh."
    n sad_closed "Yeah. Not to mention exam season is almost on top of us, so I suppose it's asking too much of you to experiment with this stuff right now." with dissolve
    ks sigh "Yeah..."
    "We both fall silent for a moment..."
    show Nozomi smile
    "Then, with a small shrug, Nozomi smiles encouragingly at me as she speaks up again." with dissolve
    n "Okay. Well, let's forget about that angle for now."
    n front smile "If we can't do anything about the light then we need to focus on what you do with it." with dissolve
    ks neutral "It's not like I even do much. I just shine it back and forth over your eyes and do a standard induction while you watch."
    n pout_left "Okay, I guess there's not much you can change about that either. Go a little slower, maybe?" with dissolve
    n front2 neutral "But besides that, there's what you say to hypnotize me, and what you say while I'm under. Because you really could work on how you phrase your suggestions." with dissolve
    n frown "And speaking of suggestions, maybe next time you could make it clear to my subconscious not to do anything that'll endanger me?" with dissolve
    ks sigh "Yeah. Yeah, I could..."
    # n front annoyed_left "And try not to be wishy-washy. You need to be clear and direct about what you want my subconscious to do, okay?" with dissolve
    n front sigh "And you could impress a lighter trance instead of trying to make me go deep. Maybe that'd be safer?" with dissolve
    "Honestly, with the way she's unloading on me, it sounds like she's already thought this stuff through."
    ks confused "Alright, then. So how exactly do you want me to do this? I tell your subconscious not to be so dumb this time, and then what?"
    n side sad_side "Okay, so I was thinking we could try some more memory play. Like, if you ask me any question, suggest I'll have no idea what the answer is." with dissolve
    n sad "That should be safe. And I think you could really test how effective it's been on me by asking me simpler and simpler questions." with dissolve
    if hypno1 == "count":
        ks smirk "Like \"What's the number between three and five?\""
    elif hypno1 == "name":
        ks smirk "Like \"What's your name?\""
    show Nozomi rolleyes
    "Nozomi scoffs at me." with dissolve
    n "Yes. Like that."
    show penlight at right with moveinright:
        ypos 0.346
    "It sounds like a plan, so I hold up the penlight in front of her."
    scene bg blackscreen with dissolve
    play sound sitting
    pause 0.5
    scene NozomiBedroom1 concerned_side bruise arm_down shadow with longdissolve
    "And in response, Nozomi lays back on her bed."
    n "So, you know what you're doing?"
    #Need to include Nozomi's phone recording the trance like before
    ks casual frown "Try to put you in a lighter trance than before, tell your subconscious to watch itself and say you can't answer questions. Got it."
    show NozomiBedroom1 frown_side
    "Nozomi sucks in a breath to steel herself, then nods." with dissolve
    n "Alright, I'm ready when you are."
    "Okay. So a lighter trance than last time..."
    "I'm not totally sure how to do that when Nozomi's so easy to hypnotize, but I guess I shouldn't impress so much about how sleepy she's getting."
    "I'll just have to wing it."
    $renpy.music.set_volume(1.0)
    show NozomiBedroom1 neutral_side with dissolve
    show NozomiBedroom1 neutral_light with dissolve
    show NozomiBedroom1 neutral_side with dissolve
    $renpy.music.set_volume(0.8)
    ks neutral "So, back once again to the light, Nozomi."
    show NozomiBedroom1 neutral_light with dissolve
    show NozomiBedroom1 neutral_side with dissolve
    $renpy.music.set_volume(0.6)
    ks "Back to watching those patterns we talked about." with dissolve
    n "{size=16}Yeah...{/size}"
    show NozomiBedroom1 neutral_light with dissolve
    show NozomiBedroom1 neutral_side with dissolve
    $renpy.music.set_volume(0.4)
    ks "Just calmly letting those light spots hit your eyes."
    show NozomiBedroom1 neutral_light with dissolve
    show NozomiBedroom1 dazed_closed
    $renpy.music.set_volume(0.2)
    $ renpy.transition(longdissolve, layer="master")
    ks "Putting all your attention on the light as you feel yourself becoming more and more relaxed. More and more sleepy..."
    show NozomiBedroom1 dazed_light with dissolve
    show NozomiBedroom1 dazed_closed with dissolve
    stop music fadeout 5.0
    # "I proceed to induce a trance state in her, slowly sweeping the penlight across her eyes several times until her eyes seem to glaze over."

    ks smile "Just letting your consciousness drift effortlessly away as you stare... that's right."
    $renpy.music.set_volume(1.0)
    queue music Flow fadein 20.0
    "Ah, she's already dropping fast. Maybe this is as far as I need to go with the light."
    # "Instead of telling her to sleep, I merely impress the idea that she's hypnotized now while she appears dazed and I start to do what we agreed." with dissolve
    ks "And while you're in this nice, relaxed state of trance, consciousness fading, you'll find that your subconscious is still listening attentively to my voice."
    ks "And what I want you to know is that, no matter what you find suggested to you, whether now or any other time, if you feel the suggestion will cause you harm..."
    ks "... you will ignore the suggestion and proceed as if it was never suggested in the first place. Understand, Nozomi?"
    show NozomiBedroom1 dazed_open
    n sleepy "I understand..." with dissolve
    show NozomiBedroom1 dazed_closed
    "Is this better than the other times we've done this?" with dissolve
    "I didn't impress on her the need to \"sleep\", so her heavily glazed eyes are staring impotently ahead between slow, infrequent blinking."
    "She just looks so out completely of it, even after only a few sweeps of the light."
    "Well, let's carry on..."
    ks "Very good, Nozomi. And with that in mind, I want to suggest something else."
    ks "While we're together in this room and you're asked a question, you'll find yourself instantly forgetting the answer."
    ks "It doesn't matter what the question is, you'll always seem to find the answer just completely drops away from your conscious mind."
    ks "But there's no need to worry, because you'll consciously remember again as soon as I leave the room. Okay, Nozomi?"
    show NozomiBedroom1 dazed_open
    n sleepy "Okay..." with dissolve
    show NozomiBedroom1 dazed_closed
    ks smile "That's great, Nozomi. Your subconscious remembering everything I told you as you wake up on three." with dissolve
    stop music fadeout 5.0
    ks "One, two... three."
    show NozomiBedroom1 surprised
    n surprised "A-ahhh..." with dissolve
    queue music Piano_Mood
    "I smile as she breathes and the life seems to immediately return to her eyes, looking at me now, not through me as before."
    "I can't help it, watching her wake up from her trances is still cute."
    show NozomiBedroom1 smile
    n smile blush "That felt... nice. You did what we agreed, right?" with dissolve
    ks "Yeah. I tried not to take you as deep as the other times, although you still seemed pretty far gone to me."
    $persistent.zombie_bedroom_1_2_unlock = True
    scene bg blackscreen with dissolve
    play sound sitting
    pause 0.5
    scene bg n bedroom day
    show Nozomi side casual smile blush noglasses bruise at center
    with dissolve
    "Nozomi gets up from the bed and takes a deep breath while slowly running a hand through her hair."
    n side smile_side "Yeah. It still felt pretty intense to me." with dissolve
    ks casual smile "Do you remember anything about it?"
    n "Um..."
    n surprised noblush "W-what?" with dissolve
    ks neutral "I said do you remember anything about the trance?"
    n front2 sleeptalk_concerned "Ahh..." with dissolve
    "Nozomi frowns in thought, but can only shake her head."
    n concerned "I don't know..." with dissolve
    ks happy "Oh, hahaha!"
    "The realization just hit me."
    ks smile "Guess it's pointless asking you that right now. Don't worry about it."
    n front pout "Oh. Right, of course." with dissolve
    n surprised "So that means the suggestion took hold again!" with dissolve
    n pout "And it's so weird. I mean, I know exactly what you did and I'm going to keep trying to resist it. It's why we're doing this, after all." with dissolve
    n frown "So okay, ask me something else!" with dissolve
    "I think of what to ask her, and then it hits me as I look around her room again and remind myself of the boxes strewn across her floor."
    ks "Alright. What's your favourite board game?"
    n smile "It's easily... {w=1.0}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend neutral "err..."
    ks "Do you have one?"
    n angry "Agh, don't confuse me with more questions!" with dissolve
    show Nozomi side irritated
    "Nozomi puts a hand to her temple as she tries to concentrate." with dissolve
    ks smirk "Okay. Just tell me when you've given up."
    play sound doorknock
    stop music fadeout 5.0
    show Nozomi surprised_side
    "Just then there's a knock on the door..."
    "Wait, AGAIN?!"
    queue music Sad_Heroine
    nm "Guys, I'm about to get lunch started. Do we fancy some salmon sushi?"
    n "Uhh..."
    n side sad_side "... I don't know?" with dissolve
    "Ah, damn, Nozomi said we'd be breaking for lunch. I'd forgotten about that."
    "She must have suggested it as another of her safety precautions, knowing that her mom was inevitably going to check on her. But..."
    ks sigh "{size=16}Is she ever gonna leave us alone?{/size}"
    n frown "What? Don't ask me!" with dissolve
    nm "Haha, how's it going in there? Working hard or hardly working?"
    n sad_side "Mom, I... err..." with dissolve
    nm "Oh my, it sounds like you're in trouble. I'm coming in!"
    play sound dooropen
    show Atsuko smile_side at center, flip:
        xpos -0.2
        linear 1.0 xpos 0.25
    "Without further warning, Atsuko swings the door open and joyfully paces inside once more."
    show Atsuko at flip:
        xpos 0.25
    nm "Is everything okay, you two?"
    n "I... {w=1.0}{nw}"
    $ renpy.transition(dissolve, layer="master")
    extend sad blush "i-is it?"
    "Nozomi helplessly looks to me in confusion. Guess I'm speaking for both of us right now."
    ks frown "U-uh, yeah everything's fine. We're fine."
    show Nozomi sad_side
    nm laugh "It's just that I can't help noticing that you don't have any books out or anything." with dissolve
    "Oh."
    nm neutral "So..." with dissolve
    "Oh..."
    nm smile_side "What's really going on in here, hm?" with dissolve
    n "I'm... w-we're..."
    "Huh. Now this is interesting. Is she struggling to think of a story, or is her post-hypnotic suggestion still affecting her?"
    "Doesn't she feel endangered by following it in the presence of her mother?"
    nm neutral_side "You DID say you were doing schoolwork, didn't you?" with dissolve
    n "I... w-wait, I did?"
    "Shit, she really IS forgetting! So did the little safety suggestion we gave her do anything at all?"
    stop music fadeout 10.0
    nm "Okay, seriously. What on earth is going on?"
    "Alright, Kyou, stay cool. You can help her out."
    show Atsuko neutral
    show Nozomi sad
    ks sigh "I'm just gonna use the bathroom real quick." with dissolve
    "All I need to do is leave the room and Nozomi will be back to-{w=1.5}{nw}"
    show Nozomi sad_side
    queue music Measured
    nm surprised "Now hold on just a moment, mister!" with dissolve
    ks surprised "Huh?!"
    nm neutral "I hate to say it, but you've both got me a little worried. No one's going anywhere until I get some answers." with dissolve
    show Atsuko neutral_side
    n sad_closed "Please, mom. There's nothing to worry about." with dissolve
    nm surprised_side "So what are you doing?" with dissolve
    n "I'm... I-I'm..."
    nm "Nozomi, you can tell me. What's wrong?"
    ks sigh "She's hypnotized."
    nm surprised "What?" with dissolve
    n front2 shocked blush "K-Kyou!?" with dissolve
    "I'm sorry, Nozomi. I just don't know what else to tell her."
    ks "Yeah. It's an act we're doing for the culture festival. I hypnotized her so she forgets the answer to any questions she's asked."
    nm surprised_side "Is that true, Nozomi?" with dissolve
    n side sad_side "It's, ahh..." with dissolve
    "And what's more, I know I can't just say that and expect Atsuko to believe it. Especially when you're in no state to back me up."
    "I'll need to hypnotize you in front of her, just to prove that's all this is."
    show Atsuko neutral
    ks smile "Uh, I'm going to help her out. Okay, Atsuko?" with dissolve
    nm surprised "Huh?" with dissolve
    "Hopefully I won't need the penlight for this. I'm sure neither of us want her asking questions about that thing."
    "But from what I've read about hypnosis I think I can pull this off without it."
    show Nozomi front2 surprised
    "All I gotta do is show a little confidence. Like I know what I'm doing..." with dissolve
    # "All I gotta do is go up to Nozomi, gently hold her shoulder and look confident. Like I know what I'm doing." with dissolve
    ks smile "Nozomi, please take a seat on the bed."
    # "Atsuko steps aside as I go to Nozomi's side and hold her gently by the shoulder." with dissolve
    # ks smile "Nozomi, look at me."
    show Nozomi shocked
    "She looks like she'd rather spontaneaously burst into flames than endure another moment of this in front of her mom." with dissolve
    scene NozomiBedroom2 a_concerned nozomi1 n_anxious blush with blink
    "Nevertheless, Nozomi does as I ask while her concerned mother sits down with her."
    ks casual smile "Okay, now look at me."
    "I point to my eye as I say this and Nozomi awkwardly meets my gaze, not knowing what else to do."
    ks "Now, do you mind if I take your hand?"
    show NozomiBedroom2 nozomi2 n_confused
    n "{cps=15}I... I don't- {/cps}{w=0.5}{nw}" with dissolve
    ks "{cps=20}Now just focus on me. {w=0.5}Just relax and focus and- {/cps}{nw}"
    stop music
    # play sound fingersnap
    hide NozomiBedroom2
    show NozomiBedroom2 a_surprised nozomi3 n_sleep
    $ renpy.transition(dissolve, layer="master")
    extend "SLEEP!{w=0.5} Deep asleep, Nozomi."
    "While she confused herself trying to answer me, I sharply tugged down on her arm and gave her a short, snappy and easy-to understand command."
    "It's a command her befuddled mind was all too eager to latch onto, and I have to keep the relief from showing on my face as I watch her slump back down into trance."
    # "I have to keep the relief from showing on my face as Nozomi slumps back into trance. So I was right that it would work!"
    "But man, I'm so glad that worked."
    queue music Piano_Mood
    # "With Nozomi being under hypnotic suggestion already, I knew she was already in a state of half trance still."
    # "It was improvised on my part, but I knew that with her being under hypnotic suggestion already, she was already in a state of half trance still."
    # "So with that in mind I figured it would't be too hard to induce her back into a full trance, even as embarrassed as she must be right now."
    show NozomiBedroom2 a_concerned_up
    ks "Very good. And now that you're back here, deeply hypnotized, I need you to let go of the suggestion I made to you." with dissolve
    ks "So as soon as you wake up you'll be able to answer questions normally, no longer affected by any of my hypnosis today, okay?"
    # The issue with this is that he also innocently removed the safety suggestion as well. Oops!
    show NozomiBedroom2 a_neutral n_sleeptalk
    n sleeptalk "Okay..." with dissolve
    show NozomiBedroom2 n_sleep
    ks "That's great, Nozomi. Now waking up feeling nice and refreshed on three." with dissolve
    ks "One... two... three."
    show NozomiBedroom2 a_concerned nozomi1 n_anxious
    $ renpy.transition(longdissolve, layer="master")
    "Nozomi's eyelids flicker as she begins to wake, watched all the while by her mother who has been concernedly observing us the whole time."
    show NozomiBedroom2 nozomi1 n_smile blush
    n "{cps=15}Kyou... that was- {/cps}{w=0.5}{nw}" with dissolve
    show NozomiBedroom2 a_surprised n_surprised
    nm surprised_side "Nozomi! Are you okay?" with dissolve
    "Nozomi squeaks at the sound of her mother's voice."
    show NozomiBedroom2 n_sigh
    n sad_side blush "I-I'm fine, mom!" with dissolve
    show NozomiBedroom2 a_concerned
    nm smile_side "Are you sure?" with dissolve
    show NozomiBedroom2 n_annoyed
    n frown_side "Yes, I'm sure! Stop fussing!" with dissolve
    show NozomiBedroom2 a_laugh
    "Atsuko laughs, relieved." with dissolve
    nm "Oh my! This is just like one of those silly late night shows on tv!"
    show NozomiBedroom2 a_smile_up n_anxious
    nm smile "So this school project you were talking about is an act you're putting on for the culture festival?" with dissolve
    ks smile blush "Th-that's right!"
    show NozomiBedroom2 n_sigh
    n sad_closed "Urrrgh." with dissolve
    show NozomiBedroom2 a_smile
    nm smile_side "Times sure have changed. When I was in high school, we always went with a café theme for our culture events." with dissolve
    show NozomiBedroom2 a_laugh
    nm laugh "Well, this is exciting! You're really putting yourself out there, Nozomi~" with dissolve
    show NozomiBedroom2 n_anxious
    n sad_side "Yes. Right..." with dissolve
    show NozomiBedroom2 a_smile
    nm smile_side "So anyway, salmon sushi for lunch?" with dissolve
    show NozomiBedroom2 n_smile_left
    n smile_side "Sure..." with dissolve
    $persistent.zombie_bedroom_2_unlock = True
    stop music fadeout 10.0
    scene bg n bedroom day
    show Nozomi front2 casual sigh noglasses bruise at center
    with blink
    queue music Downtown
    "Satisfied, Nozomi's mom leaves us to start lunch, but as soon as she leaves Nozomi starts holding her stomach."
    ks casual neutral noblush "Hungry?"
    n irritated "No, just..." with dissolve
    n angry "God... damn it, Kyou!" with dissolve
    "I put a hand to the back of my head and sigh. I was sort of expecting this from her."
    ks sigh "Yeah, I know you didn't want your mom finding out but you knew it was a risk and telling her was the only way to calm her down."
    n side frown "Yeah, I didn't like to see her worry like that. But you didn't have to say we were doing some sort of culture festival thing together!" with dissolve
    ks frown "Did you have any better ideas? Besides, we don't have to do anything, just say we had to cancel or something."
    n front irritated "Oh, I intend to!" with dissolve
    n pout_left blush "Gosh, if everyone saw us partnered up to do a hypnosis show of all things I'm never going to live it down." with dissolve
    "I sigh inwardly. Is that what she thinks of me? Still?"
    # n front irritated "Oh no, we're doing it. Mom will know I'm lying to her." with dissolve
    # n pout blush "And everyone's going to see how we partnered up to do a hypnosis show of all things and I'm never going to live this down." with dissolve
    n annoyed "If I knew this was going to happen I never would've talked to you in the first place." with dissolve
    "I can't let it slide. Not anymore."
    ks "Oh, that's right. You're embarrassed of me, aren't you."
    n irritated "Rrrrgh! I'm not..." with dissolve
    play sound sitting
    scene NozomiBedroom1 sigh arm_down bruise shadow with blink
    "Nozomi holds a hand to her temple as she flops back down on her bed, then sighs."
    n "Sorry... I'm not being fair to you."
    show NozomiBedroom1 neutral_side
    n neutral_right "It's just all a bit much, you know?" with dissolve
    "I sigh. Openly this time."
    # n sigh noblush "Okay, I'm sorry. I'm just feeling a bit overwhelmed, that's all." with dissolve
    ks casual sigh "Yeah. So anyway, you want to talk about what just happened?"
    "Nozomi nods."
    n "It seems I was every bit as affected as before, didn't it?"
    ks "Yeah. I tried to give you a lighter trance this time, but you still seemed to go pretty deep anyway."
    ks "I thought things would change when your mom walked in, but you still couldn't help yourself."
    show NozomiBedroom1 concerned_side
    n side sad_closed "Yeah. I couldn't figure out how to answer even the simplest questions. That was an odd feeling to have in front of mom." with dissolve
    ks frown "But I told your subconscious to ignore any harmful suggestions, I swear."
    show NozomiBedroom1 pout blush
    n frown "Well, I mean, it was humiliating but I don't think I was in any danger so I can't say I'm surprised that didn't help me." with dissolve
    ks neutral "Yeah, I guess. So how do we make sure that part works? Put you under again and suggest you jump out of a window or something?"
    show NozomiBedroom1 frown_side
    n front2 angry "Absolutely not! Don't be stupid!" with dissolve
    ks sigh "Okay, yeah. Sorry. But that means we're still flying blind over whether your subconscious really has a limit to this stuff."
    hide NozomiBedroom1
    show NozomiBedroom1 concerned_side arm_down bruise shadow
    n side sad_side "So did we really learn anything from this?" with dissolve
    ks smile "Maybe not. But wasn't it fun to do this again? And no one got hurt this time."
    show NozomiBedroom1 frown_side
    n front pout_left blush "I mean, I could've done without mom knowing about this..." with dissolve
    "She's embarrassed about that of course, but there's opportunity here."
    ks "But she didn't mind at all, did she?"
    show NozomiBedroom1 pout
    n pout "Well, no..." with dissolve
    ks "And are you sure you don't want to do a show for the culture fest?"
    ks "If you think about it, it'd make our experiments a lot easier if we could say we're doing it as part of an official project."
    # ks "And if we're committing to doing a show for the culture fest, doesn't that mean we can make what we're doing an official project?"
    show NozomiBedroom1 sigh blush
    n side sad_closed "Maybe... B-but still, what's everyone at school going to think?" with dissolve
    ks frown "I mean, you're the class rep and you'd be helping one of your classmates for the sake of the school..."
    "Ugh, she's doing it again. But I'll push through."
    ks sigh "Look, tell them whatever you want, I don't care. But seriously, think about it."
    show NozomiBedroom1 concerned_side
    n sad_side "Yeah..." with dissolve
    $persistent.zombie_bedroom_1_3_unlock = True
    stop music fadeout 10.0
    scene bg blackscreen with dissolve
    #May insert a customized version of Sayori Alter's lunch scene CG here...
    # scene SayoriAlterLunch a_happy k_embarrassed n_neutral
    "Soon after Atsuko called us down for lunch and some awkward conversation was had."
    "Atsuko seemed excited about our partnership, but we honestly didn't have much to say about it; just that we were brainstorming ideas."
    scene bg k room day with longdissolve
    queue music Past_Sadness
    "I didn't stay long after lunch. Nozomi said she had to get some things ready for tomorrow, but she told me she'd think about what I said."
    "So when I get back home I crash on the couch and do some thinking of my own."
    "All things considered, today went pretty well."
    "I'm feeling better about myself, Nozomi's talking to me again and we seem to be working things out."
    "But most importantly..."
    show penlight at right with moveinright:
        ypos 0.346
    "I got my penlight back."
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    pause 2.0
    jump Day8_Con_Kyou_Nozomi_Zombie

    #Nozomi is embarrassed that mum found out about her involvement in hypnosis this way. And she feels a bit guilty for worrying her.
    #Also Kyou's committed them to doing a show for the culture fest in front of everyone!
    #They'll have to declare their interest in doing so by applying officially while there's still time, but there's also the matter of the penlight still.
    #They'll need to review what just happened, and ask themselves again whether they can really use the thing again



    # Atsuko walks in during the Q & A. Nozomi continues to get confused by mum's questions and Atsuko gets worried at Nozomi's seeming mental decline
    # Kyou finds it interesting that Nozomi still can't stop herself from obeying the suggestion despite her clear embarrassment and fear and makes up
    # the excuse that she's been hypnotized for a culture fest show and Atsuko "realizes" this is the class project they were talking about."

    # nm smile_side "What is this class project you're doing?" with dissolve
    # n sad "..." with dissolve
    # nm smile "..." with dissolve
    # ks "It's...uhh..."
    # "Fuck, just think of something!"
    # ks sigh "I-it's for the culture festival. We're planning an act!"
    # nm surprised_side "Oh, is that true, Nozomi?" with dissolve
    # n sad_side "I... I dunno?" with dissolve
    # nm smile_side "We always just did a café with the whole class when I was in high school. But what were you two thinking?" with dissolve
    # show Atsuko neutral_side
    # n sad_closed "I was... uhh..." with dissolve
    # nm happy "You must have had some idea to meet up, surely. Don't be shy now~" with dissolve
    # n smile_side "Um, yes. W-we had an idea! It was, um-{w=1.0}{nw}"
    #
    # n sad "Actually... Kyou, would you mind giving me and mom a moment?" with dissolve
    # ks surprised "Huh? O-oh, sure."


    # Atsuko walks in during the Q & A. Nozomi continues to get confused by mum's questions and Atsuko gets worried at Nozomi's seeming mental decline
    # Kyou finds it interesting that Nozomi still can't stop herself from obeying the suggestion despite her clear embarrassment and fear and makes up
    # the excuse that she's been hypnotized for a culture fest show and Atsuko "realizes" this is the class project they were talking about."

    # IDEA - Nozomi wants to try memory play again, where she forgets the answers to whatever question she's asked, although it comes back to her the moment
    # the opportunity to answer has passed. Maybe when Kyou tells her her time to answer is up, or if she concedes she doesn't know


    # "I knew my theory was sound; that my placing a patterning on the beam would make it more distracting to the eye and aid my attempts to hypnotize a person."


    # "And just like that I'm starting to get excited again. I've done a lot of projects in the past, tinkering with gadgets and the like."
    # "But I've never had a partner to work with before. And I couldn't have dreamed of a better partner than Nozomi."

    #Maybe convert to speech as Kyou talks to Nozo
    # "But I have no earthly idea how it could've had such a dramatic effect on the girl I most wanted to impress."

    # n sad_closed "Anyway, fair warning, mom's obviously dying to talk your ear off." with dissolve



    #She believes he didn't know, because if he did there's no way he would have let her walk away with the penlight
    #She also needs to explain that she blanked him initially because she was working out how much he knew before coming to the above conclusion

    # n sleeptalk_concerned "God, if it wasn't for the other night this would've all been so crazy to even think about." with dissolve
    # n side sad_side "But it really is just as I suspected." with dissolve
    #
    # n sad "And this penlight is... it's dangerous!" with dissolve




    # "It IS crazy. How the hell do we explain something like this?"
    # n side sad_side "Being hypnotized doesn't open up your mind to be controlled by whoever happens to be talking. That's just a silly fantasy." with dissolve
    # "Being hypnotized doesn't open up your mind to be controlled by whoever happens to be talking."
    # n sad_closed "But after the other night, I have to believe it could've actually happened to me." with dissolve
    # ks "Yeah. It really comes back to that night, huh."
    # "If it wasn't for that, I could've thought Nozomi was just letting her imagination get the better of her."
    # "But I have to believe that Nozomi really is experiencing a deep form of hypnotic suggestibility that I hadn't thought possible."
    # "And that my penlight was what brought it about."

    # ks frown "But it's just a penlight!"
    # ks "Sure, I modified the light to emit a pattern to catch your attention, but that's all I designed it for."




    # ks sigh "That sounds a little far-fetched, Nozomi."
    # show Nozomi frown noblush
    # "But Nozomi shakes her head insistently." with dissolve
    # n frown "No. No it's not!"
    # n irritated "Honestly, why would you say that after the other night? What's the difference?" with dissolve
    # ks neutral "W-well..."
    # "Nozomi answers before I can say it."
    # n side frown_side "Look, maybe your words helped me along when we were doing it at your house, but after what I experienced there's no doubt in my mind." with dissolve
    # n neutral_side "All I need to do is get comfortable, clear my head, and this penlight will do the rest." with dissolve





    # n side frown_side "I-I mean, we know it SHOULD be unreal! This kind of thing sounds like a fantasy. Like something you'd read in a comic book." with dissolve
    # n "It's making me rethink everything I thought I knew about hypnosis if I can be influenced so easily, and all it took was this light you made."
    # "I really managed to put myself into a deep state of hypnotic trance just from the penlight on its own. I barely even needed to try."



    # n side frown_side "I mean, don't you get it? I managed to put myself into a deep state of hypnotic trance just from the penlight on its own." with dissolve

    # Don't you get it? This penlight might have awakened something in me. I'm so easy to hypnotize...


    # n front sleeptalk_concerned "Can I ask you something?" with dissolve
    # hide penlight at right with moveoutright
    # ks "What's that?"
    # n concerned "You said you didn't know how effective this penlight was going to be." with dissolve
    # n side sad "So, um... what was it like for you when you tried it on yourself?" with dissolve
    # ks surprised "Huh? Tried it on myself?"
    # n neutral "You said you made this, right?" with dissolve
    # ks "I modified it."
    # n sad "Right. But still, you must have tried it out first just to make sure it worked!" with dissolve
    # ks frown "O-oh, sure. I switched it on and shone against my bedroom wall a few times."
    # n front neutral "You... what?" with dissolve
    # n surprised "That's seriously it?" with dissolve
    # "Oh man, she's making me feel embarrassed."
    # ks sigh "Hey, the light still worked and I'm pretty sure it looked different to how it was, so I know my mod worked."
    # n frown "But you didn't see what it looks like to the human eye!"
    # ks "Well..."
    # n surprised blush "So I'm the only one who's actually seen it?" with dissolve
    #
    #
    #
    #
    #
    # ks neutral "Well, I didn't have anyone to test it on before you, but I was sure I modified it the way I wanted."
    #
    #
    #
    #
    # n front sleeptalk_concerned "I'm sorry too, Kyou." with dissolve
    # n concerned "You might have been irresponsible but it didn't excuse me for being so underhanded with you." with dissolve
    # n side sad_closed "But more than that, I realized I wasn't honest with myself about why I was so set on taking it." with dissolve
    # hide penlight at right with moveoutright
    # ks neutral "So, uh... why DID you take it, Nozomi?"
    #Nozomi explains why she took it (curious, horny etc), Atsuko comes back to check on them which is a cue for Nozomi to move on to the experiments when mom leaves
    # n sad_side "I... {w=1.0}{nw}" with dissolve
    # show Nozomi blush
    # $ renpy.transition(dissolve, layer="master")
    # extend "wanted it for myself."
    # "AUTHOR'S NOTE - Apologies for the lack of progress from last time. Rewriting the previous scenes took most of my working hours this week >.<"
    # "So yes, I scaled the theft back a bit from the previous version of this route. Still, she DOES commit to pinching Kyou's penlight and pressures him into letting her have it."
    # "So Kyou still has some reason to be resentful, just somewhat less so than before."
    # "Anyway, outlining for the rest of this scene follows, although there's not much change from before."
    # "Nozomi goes on to admit she's tried the penlight on herself the night before, as part of her trying to understand the events of the week."
    # "She tried mimicking Kyou's style of waving it back and forth over her eyes, and immediately found herself focusing on the patterns she saw."



    # "So, Nozomi explains she had other reasons for stealing the penlight, namely that she wanted it for herself."
    # "Since the first hypnosis session she couldn't reason how she was so deeply affected by what Kyou did with her."
    # "She's reviewed both of her sessions with Kyou on her phone many times, and deduced that they're no better than what she was already exposed to in the videos she's seen."
    # "Or the face to face hypnosis she had during Hitoshi's stage show, for that matter."
    #
    # "But that light, at least as she remembers it, must be the difference somehow. She admits she's become fascinated with it."
    #
    # # "So with her righteous justification that she was taking the penlight from a dangerous hypnotist, she had an excuse to examine it without him."
    # "And she examined it alright. The night she stole it, she found out that it's a standard model of medical penlight that was widely available online."
    # "It was enough to make her question why she went to the trouble of stealing it, only..."
    # "... She then tried shining the penlight in her own eyes, mimicking Kyou's style of waving it back and forth, and immediately found herself focusing on the patterns she saw."
    # "Once again she tried figuring out the patterns in her own time, waving that light back and forth as she sat on the bed, just as she's sat now..."
    # "... Only to be brought out of her reverie by the sound of the penlight clattering to the floor."
    # "She had become so distracted by those patterns that she failed to notice the penlight slipping out of her fingers."
    # "She couldn't even remember how long she'd been waving it in her face before that happened."
    # "That experience rattled her enough that she decided to stop playing with the thing."
    # "If she could enter such a state without even a hypnotist to guide her, what would have happened if she heard something while she was doing it?"
    # "Would her subconscious have been influenced in a completely unknowable way if someone from her family decided to call out to her in that moment?"
    # "After her experience with the zombie trigger, she realized that toying with something this potent by herself could have had more disasterous consequences."
    # "It's more than enough to convince her that Kyou's penlight is the key to his success at hypnotizing her. And that it's potentially very dangerous."
    # "Kyou, who's probably been quiet listening to this monologue for way too long, insists he had no idea how truly effecting his penlight was."
    # "So why DIDN'T he try it on himself? Nozomi was his unwitting guinea pig and she suffered for it!"
    # "He never thought to try the finished penlight on himself before using it on Nozomi, as he was confident his modification would project his design just fine."
    # "But obviously it never would've occurred to Kyou that his penlight could actually be more than just a little distracting!"
    # play sound doorknock
    # "Just then there's a knock on Nozomi's door. Seems Atsuko's back from shopping and she couldn't resist checking in on Nozomi and her guest."
    # play sound dooropen
    # show Atsuko smile_side at center, flip:
    #     xpos 0.25
    # "How's their class project going? Maybe they'd like to take a little break?" with dissolve
    # show Nozomi smile noblush
    # "Nozomi just smiles and tells her mum that they have some more to discuss, but maybe later." with dissolve
    # show Atsuko laugh
    # "Atsuko cheerfully accepts her answer, but tells the pair of them that they're welcome to help themselves to snacks downstairs before leaving them to it." with dissolve
    # play sound doorclose
    # hide Atsuko with dissolve
    # show Nozomi sad_closed
    # "With Atsuko gone, Nozomi then breathes a little sigh and remarks that she clearly wants an excuse to talk to Kyou some more." with dissolve
    # "How come? Nozomi won't elaborate, but says she doesn't invite many friends over who aren't Hiroko, Sayori or her board game night attendees."
    # show Nozomi neutral
    # "Kyou thinks that's plenty of people, but lets the matter drop as Nozomi hands Kyou his penlight back at last." with dissolve
    # "Nozomi explains that she feels a little safer now that her mum's in the house again, just in case there's a repeat of the zombie incident."
    # "Kyou's initially put off, but then he realises Nozomi means for him to use the penlight on her again."
    # "Nozomi confirms his assertion, and says that she wants to know more about the penlight with him."
    # "Its effects on her have been scary, but it also gave her the best hypnosis of her life."
    # "There must be a way to use it safely!"
    # show Nozomi smile
    # "And she's sure Kyou has the same goal in mind..." with dissolve
    # "AUTHOR'S NOTE - Okay, I'm going to leave things there for now."
    # "What do we think so far? Does this scene kinda drag on too much? I could probably streamline things a bit when it comes to writing the dialogue, but even so..."
    # "Also, having Nozomi steal the penlight... I've been going back and forth about keeping it or writing it out for weeks now."
    # "I thought it would be an interesting idea to have a Nozomi fuelled by confusion, fear and anger hatch a plan to take it from him then almost immediately regret it..."
    # "... leading to her eventually deciding to invite Kyou back into her headspace and in her home."
    # "It definitely contributes to making this path distinct from her original Trance storyline, but I might still cut it out for all the problems it seems to cause me."
    # "Anyway, let me know what you think and look forward to the next early access update towards the end of May~"
    # "*** AUTHOR'S NOTE - Okay, I'm out of time again, but this seems as good a point to leave it as any. Join us next time where this storyline should have developed further! ***"
    # "TO BE CONTINUED..."
    #Nozomi is scared about having a trigger that can turn her into a mindless zombie that she's apparently helpless to resist.
    #But she's also excited at the possibilities opened by the hypnotic penlight. It could really make her hypno fantasies come alive.
    #She wants to know if there's a safe way to use it, but first, when she gives Kyou his penlight back she wants to see if her zombie trigger can be removed.


    # show Nozomi side sad_side
    # "Nozomi sighs through her nostrils and gives me an affirming nod before reaching to wipe a tear from the corner of one eye." with dissolve
    # n "I-I mean, I've already started lying to people I care about. May as well become a thief while I'm at it."
    # n sad_close "Especially if I was depriving an irresponsible hypnotist of their tools so they couldn't try it on anyone else." with dissolve
    # ks frown "N-Nozomi, come on!"
    #
    #
    # ks frown "How the fuck did you even do that?!"
    # n frown "Kyou, you keep it in your right pants pocket. I've seen you with it a couple of times now; it wasn't hard." with dissolve
    #
    #
    #
    # "Just how the fuck did all of this happen anyway? It doesn't make any sense."
    # "I know I messed up. I didn't talk to her subconscious clearly enough and I didn't give her a way out so she wasn't stuck thinking she was a zombie all that time."
    # "But even so..."
    # ks neutral "I just don't get it."
    # "What happened should've been impossible!"
    # n side sad_closed "I spent all that night trying to understand what happened to me." with dissolve
    #
    # n "One moment I felt like I was falling asleep on your couch. The next I was waking up outside your house with cuts and bruises all over."
    # n sad_side "The only thing I knew for sure is that you were responsible. I didn't kno..." with dissolve


    # ks "I didn't make you into anything, Nozomi. That's impossible!"

    # n irritated "Kyou, you didn't experience it like I did." with dissolve
    # ks sigh "Y-yeah, but I mean... that can't have been hypnosis!"# Or, o-or there was more than that going on!"
    # show Nozomi frown
    # "Right. I gotta get away from the emotion of what went down and focus on the facts. Remember what I learned in all my research." with dissolve
    # ks frown "Hypnosis can only guide a person into a focused, receptive state. It can't make you do literally anything you're told."
    # # ks "So maybe I screwed up, but you should've only followed that command as much as you were comfortable with. As much as you were safe with."
    # ks "Because, Nozomi, you're always in control no matter how deeply hypnotized you get. No matter how convincing I might be."
    # show Nozomi annoyed
    # "Nozomi sighs loudly as she crosses her arms tightly in front of her." with dissolve
    # n "You think I don't know all that? Of course hypnosis can't make you "
    # n frown "I was up all that night thinking about what happened." with dissolve


    # n "I know what you're talking about, Kyou. It's the hidden observer theory."
    # n annoyed_left "The idea that there's a separate consciousness that sits apart from a person's mind while they're hypnotized." with dissolve
    # n "No matter how much a hypnotist dissociates a hypnotized person from reality, that part of them should always hold an objective view of their reality."
    # n frown "So if it needs to, it can intervene." with dissolve
    # n "It's why a deeply hypnotized person will still wake up if you left them alone for a while and they had to fulfill a basic need."
    # ks smirk "And I guess it's why hypnotists aren't ruling the world with their armies of brainwashed servants."
    # n pout_left "... Uh, sure." with dissolve
    # n neutral "But that's exactly the point, Kyou. There was no \"hidden observer\" to tell me I didn't seriously want to eat your brains or whatever." with dissolve
    # n irritated "Gosh, never mind this hidden observer stuff. Why didn't I feel ANYTHING when I hit my head or stepped on my glasses?" with dissolve
    # n frown "Why couldn't I stop myself? Why couldn't I acknowledge the reality of the situation no matter what happened to me?" with dissolve
    # show Nozomi irritated
    # "Nozomi folds her arms over her stomach and grips the sleeves of her sweater as she sighs harshly through her nose." with dissolve
    # n "When I got home and had time to think, it really sunk in how terrifying that was."
    # n "I couldn't sleep from thinking about it. And..."
    # n concerned "And the more I thought about it, the more I was convinced that it could've only been caused by one thing." with dissolve
    # ks neutral "What's that?"
    # n sigh "..." with dissolve
    #
    #
    #
    # show Nozomi annoyed
    # "Nozomi scoffs at me. Like I was supposed to know what she's talking about." with dissolve
    # n "The only thing that I can't figure out at all."
    # show Nozomi sleeptalk_concerned
    # "Nozomi seems to hug her stomach a little tighter as she lets out another, softer-sounding sigh." with dissolve
    # "A moment later, her hand then slides with some reluctance towards her pillow, reaching underneath it before pulling back holding a familiar object..."
    # show penlight at right with moveinright:
    #     ypos 0.346
    # n concerned "This light really is something, you know?" with dissolve
    # "That's it all right. My penlight doesn't look any different to all the others of its kind, but she couldn't have found a copy of that exact model so quickly."
    # "But that just means the reality is laid bare before my eyes: She really DID steal it!"
    # ks frown "Man, why'd you take it, Nozomi?"
    # show Nozomi pain
    # "She flinches at the question." with dissolve
    # n "I'm an idiot."
    #
    # n "I was scared and... and angry at you for letting me get hurt."
    # Mention how she's seen some cocky hypnotist do instant inductions on a girl and let her smack her head against a wall on her way down.
    # Also points out Kyou didn't clean up after himself because that zombie trigger is still active in her. Admits it's a little unfair to pin that on him
    # after what went down, but the fact remains that she should have been de-programmed


    # n side sad_side "Like, I thought that if you really did make that penlight then you must have known you must have known what you were doing. You said you MADE this thing." with dissolve
    # n sad_closed "S-so in the heat of things I kinda thought you were terrible for what you did." with dissolve
    #
    #
    #
    #
    #
    #
    # n "I only shined it over my eyes a couple of times, and it's like my eyes were being instantly drawn to it, just like before."
    # ks surprised "Y-you did WHAT?!"
    # n pain "I know! I know, it was stupid." with dissolve
    # n "And I didn't dare do anything else with it."
    #
    #
    # n sigh "W-when I got home that night I didn't know what to think." with dissolve
    # n sleeptalk_concerned "I was hurt. I was angry, and confused and... and scared..." with dissolve
    # n side sad_side "This light. It was doing something to me. Why was I so fascinated by a dinky little penlight?" with dissolve
    # hide penlight at right with moveoutright
    # ks frown "So you thought you'd steal it off of me."
    # n front sleep "Yes." with dissolve
    # ks "Why? You could've just asked me or something."
    # n cry "I know! I know, but..." with dissolve
    # n cry_open "Y-you said you made it, Kyou!"
    # n frown "And the fact that YOU made this had me suspicious." with dissolve
    #
    #
    # n "One moment I'm having the best hypnosis of my life and the next I wake up outside your house in so much pain."
    #
    #
    # #The penlight is giving her the best hypnosis of her life, but she's scared of its effects. Can they mitigate its effects a bit or otherwise control it?
    # n sigh "I'm sorry I stole it. And... and I know I've been weird these past couple of days." with dissolve



    # "AUTHOR'S NOTE - This author may also be an idiot!"
    # "Like, I don't think I can make the \"Nozomi stole the penlight\" plot point work."
    # "I thought it would be an interesting idea to have a Nozomi fuelled by confusion, fear and doubt hatch a plan to take it from him then immediately regret it..."
    # "... leading to her eventually deciding to invite Kyou back into her headspace and in her home."
    # "Taking things to her house still seems like a good idea. The theft part less so. So I'll probably have a rethink over the weekend."
    # "Anyway, look forward to an early access update in the coming week with hopefully some more progress on this storyline~"
    # "TO BE CONTINUED..."
    jump Credits

label Day6_Con_Kyou_Sayori:
    scene bg k bedroom day with longdissolve
    if hypno3 == "personality":
        play music Eons
        "I wake up the following morning with a sinking feeling."
        "Sayori's coming here and I know she wants me to deprogram her. I can understand that."
        "But what about after? Are we still gonna hang out?"
        if hypno_nozomi == True:
            "Not to mention... Nozomi."
            "How am I going to break it to her that I hypnotized Nozomi again? Somehow I don't think she'll take it well."
            "... Maybe it's better if I don't bring it up. At least not today."
            "{cps=20}We have more important things to talk about after all, and- {/cps}{w=1.0}{nw}"
        play sound doorbell
        "Ugh, the doorbell already?! I've barely gotten out of bed." with vpunch
        "She must really want to get this done if she's this early."
        play sound doorbell
        "As I hear the doorbell again, I scrabble to look decent and rush downstairs."
        scene bg k room day
        # if hypno_nozomi == False:
        show Sayori casual alert_surprised_right
        with blink
        s "Did I come at a bad time?"
        ks casual frown "You're early. It's barely past nine."
        s alert_pout "We agreed on meeting in the morning. Nine o'clock is well into the morning." with dissolve
        show Sayori alert_neutral_right
        "She looks me up and down and crinkles her nose at me." with dissolve
        s alert_smirk_right casual_handup "But if I knew you would smell so unwashed, I would have come later." with dissolve
        s alert_happy "Penlight or no, I may not be able to fall into trance with such a distraction." with dissolve
        ks sigh "Uggh, whatever."
        s alert_rolleyes "Huh, and now I am thinking... Is it possible to hypnotize a person using scent?" with dissolve
        ks frown "Uh... I think so? You can use pretty much anything as a hypnotic fixation, depending on the subject."
        ks "... Why?"
        s casual_folded alert_smile "Oh, I just had the thought that you could use this for your stage hypnotist routine." with dissolve
        s alert_smirk_right "You could be like a mesmerist Pepé Le Pew." with dissolve
        ks angry "F-fuck off! So what if I've got a little morning musk, it can't be that bad."
        show Sayori alert_smile_right
        "Sayori simply chuckles at my discomfort." with dissolve
        s "Well, if you are not going to freshen up, then I suppose we should just get to it."
        scene cg k room day
        show SayoriHypnoDay smile
        with blink
        "As Sayori goes to sit down on the living room couch, I have to wonder about her."
        "I mean, I guess she's in a good mood? And she's still okay with me deprogramming her."
        "Maybe she was just messing with me to put herself at ease?"
        show SayoriHypnoDay neutral
        s alert_neutral_right "Just so we are clear, I want you to bring me under one more time and make sure to undo all your alterations. Both the personality AND the sleep conditioning." with dissolve
        "All of it? But..."
        ks casual confused "So everything we did was for nothing?"
        show SayoriHypnoDay sad
        s alert_concerned_right "I am sorry, Kyou. I know your intentions were good, but I foresee only trouble if we kept them lurking in my mind." with dissolve
        "She then averts her gaze and pauses a moment before continuing."
        show SayoriHypnoDay neutral_closed
        s alert_concerned "There is also one more thing I would ask: That you destroy that penlight once you're finished, and..." with dissolve
        show SayoriHypnoDay stern
        s alert_concerned_right "... And that you remove any plans you may have drawn up so it cannot be remade." with dissolve
        "She... really wants me to lose everything I worked for?"
        "Fuck, I know the penlight is dangerous, but..."
        show SayoriHypnoDay neutral
        s casual "You know this is the right thing to do, Kyou." with dissolve
        if hypno_nozomi == False:
            menu:
                "Agree":
                    "With a sigh, I find myself nodding my head."
                    ks sigh "You're right, Sayori. I know you're right. I mean..."
                    show penlight at right with moveinright:
                        ypos 0.346
                    ks "Without even meaning to, I've put you in a lot of danger by using this."
                    ks "Maybe I could try to be more careful in future, but I guess you can't always tell how a suggestion will affect someone."
                    ks "Not to mention what would happen if this got in the wrong hands..."
                    hide penlight with moveoutright
                    show SayoriHypnoDay sad
                    s alert_annoyed_right "It does not bear thinking about, does it?" with dissolve
                    ks neutral "Yeah... alright, so are you ready?"
                    show SayoriHypnoDay looking
                    "I raise the penlight above her head and she nods as I pass the light across her eyes once more." with dissolve
                    $light_y = 0.24
                    call cglightshow
                    ks "Alright. Then you should find it so very easy to relax in your seat once more, just looking up as you let the light dance across your eyes."
                    call cglightshow
                    "And sure enough, any anxiety she may have had about being hypnotized by this thing seems to dissipate after just a couple of exposures to the beam."
                    ks "That's right. Let me and the light do all the work. All you need to do is stare up at the light and let yourself feel nice and comfortable."
                    call cglightshow
                    ks "Stare and let yourself tire. Let yourself sink into the couch. Let the light take you down as you take a deep breath in."
                    stop music fadeout 25.0
                    call cglightshow
                    ks "And out. Watching the light. Letting those eyelids droop. Breathing in..."
                    call cglightshow
                    show SayoriHypnoDay drowsy
                    ks "And out. Deeper. Breathing in." with dissolve
                    call cglightshow
                    ks "Breathing out. Feeling so drowsy. So comfortable and relaxed for the light. That's good, Sayori."
                    call cglightshow
                    ks "Let's try to stay awake just a little longer. Take a deep, full breath now. Filling your lungs with relaxation."
                    call cglightshow
                    ks "That's good. Keep that relaxation and let it fill you completely."
                    call cglightshow
                    ks "And now breathe out fully, letting all the remaining tension leave your body."
                    call cglightshow
                    ks "So relaxed. So comfortable... sleep, Sayori."
                    call cglightshow
                    show SayoriHypnoDay head_down sleep
                    play music Flow
                    "Her straining eyelids flutter closed as she once more slumps on my couch." with dissolve
                    ks "Very good. Letting yourself drop for me, going deep into that familiar, wonderful state of trance."
                    s alert_sleep "..."
                    ks "And as you drop, you will realize that there is no longer another person within you."
                    ks "[alt_name] is no more, and the words \"become [alt_name]\" will no longer have any special effect on you if you hear me or anyone else say it."
                    ks "Also... you will no longer be compelled to blank your mind completely when you try to sleep at night. What you do when you try to sleep is entirely up to you again."
                    ks "Anything I may have suggested to you in trance will immediately and effortlessly fade from your mind."
                    ks "None of those suggestions will influence your behaviour or thinking in any way."
                    ks "Do you understand, Sayori?"
                    show SayoriHypnoDay sleeptalk
                    s alert_sleeptalk "Yes..." with dissolve
                    show SayoriHypnoDay sleep
                    "I sigh quietly. I still think she could've kept the sleep trigger." with dissolve
                    "It really did seem to be helping her. But this is what she wants."
                    ks "Very good, Sayori. Now we will wake you up on a count of three. I will count up, and on three you will become comfortably awake."
                    stop music fadeout 5.0
                    ks "Counting up now... one, feeling the energy start to return to your limbs."
                    ks "Two, beginning to test your eyelids, letting the tiredness fade from them."
                    ks "And three, comfortably awake, Sayori."
                    show SayoriHypnoDay head_up drowsytalk
                    "Sayori's eyes swivel open and as she regains her bearings her gaze focuses on me." with dissolve
                    play music Eons
                    s "Is it done?"
                    ks "Yeah... I deprogrammed you like you asked."
                    show SayoriHypnoDay smile
                    "On hearing this, she smiles." with dissolve
                    s "Thank you, Kyou. I admit I did have a little doubt in my mind that you would be tempted to do otherwise."
                    ks frown "Er... not that I did, but how do you know I kept my promise and didn't just lie about it?"
                    "She shrugs."
                    show SayoriHypnoDay happy
                    s "Oh, that will be easily ascertained from what I am about to say next." with dissolve
                    ks "What's that?"
                    show SayoriHypnoDay neutral
                    s "We still need to destroy your penlight." with dissolve
                    $persistent.sayori_hypno_day_unlock = True
                    scene bg k bedroom day
                    show Sayori casual_folded alert_neutral_right
                    with blink
                    "Sayori looks on as the dismantled and crushed pieces of my penlight drop into the bin."
                    ks casual sigh "It sure does suck to see all your hard work end up in the trash, you know?"
                    s alert_concerned "I know, Kyou. And I am sorry that you had to do this." with dissolve
                    s alert_concerned_right "But you are wrong. This was not for nothing." with dissolve
                    ks neutral "It wasn't?"
                    s casual "For one, your study of hypnosis is still relevant and useful. Although I ask that you please use it as everyone else does from now on." with dissolve
                    s alert_concerned "And you also helped me realize how much I needed to go easier on myself." with dissolve
                    ks smile "Yeah?"
                    s alert_surprised_right "Yes. The night I first fell asleep under the influence of your suggestion was like a reset button had been pushed in my head." with dissolve
                    s alert_concerned "When I awoke, I felt an energy I forgot I had." with dissolve
                    s alert_sleep "I know people espouse the value of a good night's rest, but I thought I could optimize my time if I stayed up just a little later." with dissolve
                    s alert_sleeptalk "But half an hour became an hour, then two hours..." with dissolve
                    s alert_concerned_right "I am not sure when it happened, but it did not take long for this all to become so routine for me." with dissolve
                    s alert_concerned "Somewhere along the way I forgot what it was like to be anything else." with dissolve
                    ks smirk "... It sure sounds like you tried to min-max your life and took it too far."
                    s alert_smirk_right "Heh. Turns out I really did need to invest a few points in stamina." with dissolve
                    # s "The difference I have felt from having a full night's rest has been phenomenal."
                    # s "I did not realize how badly I was limiting myself by not allowing myself to recharge properly."
                    s alert_smile_right "So yes, even if your conditioning is now absent, I will ensure that I keep this going." with dissolve
                    s casual_folded alert_happy "I have you to thank for that." with dissolve
                    "Okay, so maybe I did make a difference, but still, as I look at the broken remains of my penlight, I ask:"
                    ks neutral "So... what now?"
                    s alert_neutral "Hmm..." with dissolve
                    s casual_handup alert_smirk_right "In the short term, I recommend you shower." with dissolve
                    ks frown "Yeah, yeah... You know what I meant."
                    show Sayori alert_smile_right
                    stop music fadeout 5.0
                    "Sayori ponders for a moment, then smiles at me." with dissolve
                    s alert_happy "I will sleep on it and get back to you." with dissolve
                    $ending = "trust"
                    jump Epilogue_Con_Kyou_Sayori
                "Refuse":
                    stop music fadeout 5.0
                    ks frown "Listen... Sayori..."
                    ks "I'm fine putting you back to how you were, but what you're asking me to do, it's..."
                    ks "It's too much!"
                    show SayoriHypnoDay stern
                    s alert_annoyed_right "Kyou, I want you to think about what you are saying." with dissolve
                    play music Rain
                    s "If you refuse to do this, you put us all in danger."
                    "I frown at her."
                    ks frown "Wh-what the hell are you talking about? Sayori, I know it's dangerous, I'm not going to start using it on you again, or on anyone else."
                    ks "But I'm not going to destroy it and everything I worked on all year just because you asked me to. Be reasonable."
                    s "That you know how dangerous it is just makes this worse."
                    ks "Jesus, Sayori, I'm just going to study it. Try and figure out how it does what it does."
                    ks "Maybe learn a thing or two about how the human mind works along the way."
                    ks "Hell, you like studying don't you? And this stuff is interesting to you too, don't try and deny it."
                    ks "We could study it together."
                    show SayoriHypnoDay irritated
                    s alert_irritated "Kyou, you are losing sight of the issue here and I really... I really need you to be better about this." with dissolve
                    ks "Better?"
                    show SayoriHypnoDay angry
                    s alert_angry_right "We already know enough about your fantastical science project to be sure of its destructive potential on the human mind." with dissolve
                    s "We know more than enough already!"
                    "I look to her determined eyes, and I can feel my own expression drop as my heart sinks."
                    ks neutral "You don't believe me. You really think I'll... t-that I'll..."
                    scene bg k room day
                    show Sayori casual alert_angry_right at center:
                        ypos 1.2
                        linear 2.0 ypos 1.0
                    with blink
                    s "Kyou, please! This is NOT about trust!"
                    "I step back a little as Sayori abruptly rises from the couch and steps towards me."
                    show Sayori:
                        ypos 1.0
                    ks casual angry "But you really don't trust me after all! That's what you're telling me!"
                    s "HOW ARE YOU THIS OBTUSE?" with vpunch
                    "Aaand we're back to screaming."
                    s "There is NO safe way to do what you are proposing, Kyou! NONE!"
                    "She doesn't trust me to do what's right. I heard that loud and clear."
                    s casual_folded "Even if I entertained this, what happens when your research hits a wall and requires experiments on human subjects, as with Nozomi?" with dissolve
                    s alert_irritated "Because of course you will." with dissolve
                    "And if that's what she thinks, then..."
                    s alert_annoyed_right "But do you really think you would be in a place to reconsider this folly when you reach it?" with dissolve
                    "Then..."
                    s alert_angry_right "Answer me, Kyou! {w=0.5}{nw}" with dissolve
                    ks frown "You should become [alt_name] until you can chill out."
                    s casual alert_panicked_right "Kyou, you...{w=1.0}{nw}" with dissolve
                    stop music
                    $ renpy.transition(dissolve, layer="master")
                    extend casual alert_surprised_right ""
                    ks sigh "I... I'm sorry."
                    s "Huh? Why sorry? Did something happen?"
                    ks "Well..."
                    $sayori_name = "[alt_name]"
                    s alert_happy "I'm confused." with dissolve
                    "I strain a smile at her. This feels like so much shit."
                    "But you kinda forced my hand, Sayori."
                    ks smile "It's nothing, [alt_name]. I was just going to ask you something."
                    s casual_handup alert_giggle "Well, asking is free, Kyou! Don't be shy~" with dissolve
                    ks "Right. Well..."
                    show penlight at right with moveinright:
                        ypos 0.346
                    "Yeah, I know I said I wouldn't use this on her again, but there's no other way to fix this situation."
                    "I'll do this, and then it'll be the last time."
                    ks "Since we're here, I thought we could have another hypnosis session together. How about it?"
                    "\"[alt_name]\" looks to the penlight in my hand, then to me, then lets out a carefree giggle."
                    "I'm gonna miss hearing that."
                    s alert_laugh "Is that all you wanted? Well, I'm game if you are~" with dissolve
                    play music Flow fadein 30.0
                    hide penlight with moveoutright
                    scene cg k room day
                    show SayoriHypnoDay laugh
                    with blink
                    "Gesturing to the couch, I let out a sigh as \"[alt_name]\" goes to get comfortable."
                    show SayoriHypnoDay smile
                    s "So what did you want to try this time, Kyou?" with dissolve
                    ks casual "I, uh... I wanted to try dropping you in trance faster. Get some practice in for the culture fest."
                    "She nods as she gets herself comfortable on my couch once more."
                    show SayoriHypnoDay looking
                    s "Ready when you are, Kyou~" with dissolve
                    "It's clear to me that \"[alt_name]\" has absolutely no memory of anything we've done since the last time she was active."
                    "And once I'm done with this, I'll make sure to expand on that."
                    "I think it'll be for the best."
                    $ light_y = 0.24
                    call cglightshow
                    ks "Very good Sayo-, uh, [alt_name]. Nice and relaxed now, as you look up at the light for me."
                    "I watch as she innocently looks into the light as I pass it across her face."
                    call cglightshow
                    ks "Finding it so easy, so natural, to let yourself sink into the couch. To allow my light to sweep over your face."
                    call cglightshow
                    ks neutral "Very good. Just letting the light take you down. Letting your eyelids become heavy. Knowing deep down how sleepy it makes you to watch the light."
                    call cglightshow
                    ks "Very natural, very right it is, to stare and sink further."
                    call cglightshow
                    ks "And if you need to relax even deeper, letting those tired, heavy eyelids close... that's okay."
                    call cglightshow
                    show SayoriHypnoDay drowsy
                    ks "Letting them close..." with dissolve
                    call cglightshow
                    ks "Dropping so quickly, [alt_name]. So deeply."
                    call cglightshow
                    ks "And sleep."
                    show SayoriHypnoDay head_down sleep
                    ks "Feeling so good as your conscious mind falls deep asleep, [alt_name]." with dissolve
                    "I take a moment to pause, as I collect myself for what I'm about to do..."
                    ks "Now, [alt_name], as you remain so deeply asleep, I want you to remember that this is not who you truly are."
                    ks "You need to become Sayori again, while still remaining in this deep, completely relaxed state of trance."
                    ks "You can do that can't you... Sayori?"
                    $sayori_name = "Sayori"
                    show SayoriHypnoDay sleeptalk
                    s alert_sleeptalk "I-I... yes..." with dissolve
                    show SayoriHypnoDay sleep
                    "I breathe a little sigh. So far so good." with dissolve
                    ks "That's... that's great, Sayori. I knew you could do it."
                    ks "And now that you are, once again, Sayori I want you to do something else for me."
                    ks "This time, I need you to accept that [alt_name] no longer exists as a part of you."
                    ks "[alt_name] is no more, and the words \"become [alt_name]\" will no longer have any special effect on you if you hear me or anyone else say it."
                    ks "Also... you will no longer be compelled to blank your mind completely when you try to sleep at night. What you do when you try to sleep is entirely up to you again."
                    ks "In fact, anything I may have suggested to you in trance will immediately and effortlessly fade from your mind."
                    ks "None of the suggestions I made previously will influence your behaviour or thinking in any way."
                    ks "Do you understand, Sayori?"
                    show SayoriHypnoDay sleeptalk
                    s alert_sleeptalk "Yes..." with dissolve
                    show SayoriHypnoDay sleep
                    ks "That's great, Sayori. Completely free of my suggestions, just feeling so good. So relaxed... so ready to accept new suggestions..." with dissolve
                    ks "So if I were to now suggest to you that every time you met me in the past week was a figment of your imagination, you would have no trouble accepting it as the truth."
                    ks "And as figments of your imagination, you should find it so very easy to simply... forget, Sayori."
                    ks "Simply allow these figments to leave your mind completely."
                    ks "We never met at any time outside of our normal school routines, so it makes no sense for you to recall such things... isn't that right, Sayori?"
                    show SayoriHypnoDay sleeptalk
                    s alert_sleeptalk "Right..." with dissolve
                    show SayoriHypnoDay sleep
                    ks "Absolutely right. And there's one more thing you need to do. One more thing that will be completely natural and correct for you to do." with dissolve
                    ks "The moment you wake, you will get up off the couch, leave my house and go straight back to your home."
                    ks "You will remember nothing of our meeting, or that you were ever here."
                    ks "Is that understood, Sayori?"
                    show SayoriHypnoDay sleeptalk
                    s alert_sleeptalk "Understood..." with dissolve
                    show SayoriHypnoDay sleep
                    ks "Very good, Sayori. You really are a wonderful hypnotic subject. Taking these suggestions so well. So fully." with dissolve
                    ks "Now we will wake you up on a count of three. I'm going to count up, and on three you will become fully awake and instantly acting on what you were told."
                    ks "Counting up now... one... two..."
                    "I let a moment linger as I look her over."
                    "I really wish we could've been friends, Sayori."
                    stop music fadeout 5.0
                    ks "Three."
                    show SayoriHypnoDay head_up neutral
                    $ renpy.transition(dissolve, layer="master")
                    s "..."
                    scene bg k room day
                    show Sayori casual alert_neutral_right at center:
                        ypos 1.2
                        linear 2.0 ypos 1.0
                    with blink
                    s "..."
                    hide Sayori with dissolve
                    play sound dooropen
                    pause 2.0
                    play sound doorclose
                    "And just like that, Sayori wordlessly stands and quietly exits the house, leaving me alone with my thoughts..."
                    show penlight at right with moveinright:
                        ypos 0.346
                    "... And my penlight."
                    "This is... it was too important to give this up. Possibly even important in more ways than I know right now."
                    "I hope there was a part of Sayori that understood."
                    hide penlight with moveoutright
                    $ending = "forscience"
                    jump Epilogue_Con_Kyou_Sayori
        else:
            stop music fadeout 5.0
            ks "Okay, listen... Sayori..."
            ks "I'm fine putting you back to how you were, but what you're asking me to do, I..."
            ks "I just can't, okay?"
            show SayoriHypnoDay stern
            s alert_annoyed_right "Kyou, I want you to think about what you are saying." with dissolve
            play music Rain
            s "If you refuse to do this, you put us all in danger."
            "I can't help but shake my head at what I'm hearing."
            ks frown "Look, I know it can be dangerous. I *know* that, okay? I didn't realize before how dangerous hypnosis can be."
            ks "But I've learned from our time together. I know I have to be more careful about the things I say to a hypnotized subject, especially if I can get them as deep into it as with you."
            ks "I can really hurt people with my penlight; I get that. But so long as I'm careful I can do so much good for people too."
            ks "My hypnosis made you think you lost control of yourself, but with the right words I could have you feeling on top of the world. So don't tell me to throw it all away."
            ks "Don't tell me I have to give this all up just because I made a mistake."
            show SayoriHypnoDay irritated
            "Sayori scoffs at me as she shakes her head disdainfully." with dissolve
            s "Unbelievable. The arrogance on you that you think you can handle such a wild and dangerous phenomenon you barely comprehend."
            ks "You saw how it worked on Nozomi didn't you? I put her into trance with the penlight, took her out again and she didn't suffer for it at all."
            ks "She even seemed to enjoy it, didn't she?"
            show SayoriHypnoDay stern
            s "You... Kyou, do not insult my intelligence by trying to convince me our experiment with Nozomi and my own experience are directly comparable." with dissolve
            ks "Of course they are! I hypnotized Nozomi and all that happened was..."
            stop music fadeout 5.0
            "Oh... right."
            s "Was... what?"
            ks confused "I- I, uh..."
            "Dammit. I didn't mean to let it slip about what went down after she left me and Nozomi in the study club room."
            show SayoriHypnoDay neutral
            queue music Unrest
            s "You and Nozomi... you..." with dissolve
            show SayoriHypnoDay surprised
            "And from the look in her eyes, it's clear she's already figured out what I left unsaid." with dissolve
            "This really wasn't a good time to bring this up."
            s "You hypnotized her after I left, didn't you."
            "... Well, I knew we'd have to deal with this sooner or later. Guess we're ripping the band-aid off now."
            ks sigh "Look, what was I supposed to do?"
            show SayoriHypnoDay stern
            s "Do you take me for a fool? You *know* how dangerous that contraption of yours has been!" with dissolve
            s "As if our experiment wasn't reckless enough. Why would you even consider using such a thing on her a second time?"
            "But damn, if seeing Sayori angry again isn't making me anxious as hell..."
            show SayoriHypnoDay irritated
            s "The stupidity boggles my mind, it really does." with dissolve
            ks frown "She wanted me to! You really think she'd be happy if I just blew her off back there?"
            ks "She wanted to help YOU! Don't you get that?"
            show SayoriHypnoDay angry
            s "YOU knew better than to involve her in this any more than we had to! You gave your WORD you would not!" with dissolve
            s "So spare me your frivolous excuses!"
            scene bg k room day
            show Sayori casual_folded alert_angry_right at center
            with blink
            "Sayori begins to pace furiously around my room while my breath quickens."
            "But even as I panic I know one thing for sure: I can't back down now."
            ks casual angry "I... It was YOUR idea to bring Nozomi, remember? And besides, I didn't pressure her or bring it up or anything!"
            ks "SHE made the choice! She WANTED to do it all on her own!"
            s alert_irritated "Oh nonono, don't you DARE push your responsibility on to her. As though she could've had any idea of the danger she was subjecting herself to!" with dissolve
            ks "I didn't... for fuck's sake, Sayori, I didn't put her in danger! I gave her a simple suggestion and I made sure to undo it before I let her leave."
            ks "All I did was make her happy. I was so fucking careful with her, and..."
            ks "B-besides, what did you expect me to do? Tell her to fuck off?"
            s casual alert_angry_right "YES! If that is what it would take!" with dissolve
            "Just hearing that is... it's making my chest tighten, like I can hardly breathe."
            s casual_handup alert_irritated "Dammit. I should have known better than to trust either of you to keep a cool head." with dissolve
            "After all we've been through, she really doesn't trust me."
            s alert_annoyed_right "You need to do better, Kyou. Do you hear me?" with dissolve
            "I can't deal with this."
            s alert_angry_right "The next time she approaches you for another hypnosis session, you MUST shut her down! I will brook no debate on this!" with dissolve
            "I can't deal with... her."
            s casual "She may beg, or threaten but no matter what you... Kyou?" with dissolve
            "I don't care what it takes..."
            s "Kyou, have you listened to a damn word I said?"
            ks neutral "... Become [alt_name]."
            stop music
            s casual alert_panicked_right "Y-YOU...{w=1.0}{nw}" with dissolve
            $ renpy.transition(dissolve, layer="master")
            extend casual alert_surprised_right ""
            "... I just need her gone."
            s "... Kyou? What on earth is the matter? You're looking a little pale."
            ks "O-oh, it's..."
            "It was almost automatic, the way I just uttered those words."
            $sayori_name = "[alt_name]"
            ks "It's nothing. Don't worry about it, [alt_name]."
            queue music LookingGlass
            "But now that I have, there's no going back."
            s casual_handup alert_happy "Mhmhmh, well if you say so~" with dissolve
            "I give the changed girl a smile as I try to compose myself for what I must do."
            ks smile "Anyway, I was just thinking..."
            s alert_giggle "About what?" with dissolve
            ks "Right. Well..."
            show penlight at right with moveinright:
                ypos 0.346
            "I take my penlight from out of my pocket and lock eyes with Sayori's carefree doppelganger."
            ks "While I have you here, I thought we could have another hypnosis session together. You don't mind, do you?"
            "\"[alt_name]\" looks to the penlight in my hand, then to me, before letting out a cheerful giggle."
            #Need to rework the dialogue below to fit this story path (ETA: I don't recall if I actually altered this dialogue or not ^^;)
            s alert_laugh "Oh, is that all? Well, I'm game if you are~" with dissolve
            hide penlight with moveoutright
            scene cg k room day
            show SayoriHypnoDay laugh
            with blink
            "Gesturing to the couch, I steel myself as \"[alt_name]\" goes to get comfortable."
            show SayoriHypnoDay smile
            s "So what did you want to try this time?" with dissolve
            ks casual "I, uh... I thought I could try to drop you into trance faster. Get some practice in for the culture fest, you know?"
            show SayoriHypnoDay looking
            s "Alright~ Well, I'm ready when you are, Kyou!" with dissolve
            "It's clear to me that \"[alt_name]\" has absolutely no memory of anything we've done since the last time she was active."
            "I don't think there can be any denying that Sayori was right about the hold these suggestions of mine have on her."
            $ light_y = 0.24
            call cglightshow
            ks "Very good Sayo-, uh, [alt_name]. Nice and relaxed now, as you look up at the light for me."
            "So I'll make a few more suggestions. But it'll be alright, Sayori..."
            call cglightshow
            ks "Finding it so easy, so natural, to let yourself sink into the couch. To allow my light to sweep over your face."
            "You won't need to worry about me, or Nozomi or even yourself any longer."
            call cglightshow
            ks neutral "Very good. Just letting the light take you down. Letting your eyelids become heavy. Knowing deep down how sleepy it makes you to watch the light."
            "With this penlight of mine I'll... I'll make things right with everybody."
            call cglightshow
            ks "Very natural, very right it is, to stare and sink further."
            call cglightshow
            ks "And if you need to relax even deeper, letting those tired, heavy eyelids close... that's okay."
            call cglightshow
            show SayoriHypnoDay drowsy
            ks "Letting them close..." with dissolve
            call cglightshow
            ks "Dropping so quickly, [alt_name]. So deeply."
            call cglightshow
            ks "And sleep."
            show SayoriHypnoDay head_down sleep
            ks "Feeling so good as your conscious mind falls deep asleep, [alt_name]." with dissolve
            "I breathe a little sigh. So far so good." with dissolve
            ks "Now, [alt_name], as you remain so deeply asleep, I want you to remember that this is not who you truly are."
            ks "You need to become Sayori again, while still remaining in this deep, completely relaxed state of trance."
            ks "You can do that can't you... Sayori?"
            $sayori_name = "Sayori"
            show SayoriHypnoDay sleeptalk
            s alert_sleeptalk "I-I... yes..." with dissolve
            show SayoriHypnoDay sleep
            ks "That's... that's great, Sayori. I knew you could do it." with dissolve
            "I take a moment to pause, as I collect myself for what I'm about to do..."
            ks "And now that you are, once again, Sayori I want you to do something else for me."
            ks "This time, I need you to accept that [alt_name] no longer exists as a part of you."
            ks "[alt_name] is no more, and the words \"become [alt_name]\" will no longer have any special effect on you if you hear me or anyone else say it."
            ks "Also... you will no longer be compelled to blank your mind completely when you try to sleep at night. What you do when you try to sleep is entirely up to you again."
            ks "In fact, anything I may have suggested to you in trance will immediately and effortlessly fade from your mind."
            ks "None of the suggestions I made previously will influence your behaviour or thinking in any way."
            ks "Do you understand, Sayori?"
            show SayoriHypnoDay sleeptalk
            s alert_sleeptalk "Yes..." with dissolve
            "That's right. I gave you what you came here for. Honor your wishes."
            "I won't interfere with your life's work or whatever."
            show SayoriHypnoDay sleep
            ks "That's great, Sayori. Completely free of my suggestions, just feeling so good. So relaxed... so ready to accept new suggestions..." with dissolve
            "I could never do anything terrible to you."
            ks "Isn't that right, Sayori?"
            show SayoriHypnoDay sleeptalk
            s alert_sleeptalk "Yes... Ready to accept new suggestions..." with dissolve
            show SayoriHypnoDay sleep
            "But I can't let you interfere with what I'm doing here. I'm sure you'll understand." with dissolve
            ks "That's right. So now I need you to accept that when I wake you from this state of hypnosis, you will find that you no longer care about my penlight."
            ks "You will no longer feel any concern or curiosity about my hypnosis, or about what me and Nozomi are doing."
            ks "Instead, you will find yourself completely content to carry on as you were. Understand, Sayori?"
            stop music fadeout 5.0
            scene bg blackscreen with dissolve
            # show SayoriHypnoDay sleeptalk
            s "Uh... uh-huh. I understand..."# with dissolve
            pause 2.0
            $ending = "betrayal"
            jump Epilogue_Con_Kyou_Sayori

label Day6_Con_Kyou_Sayori_Alter:
    scene bg k bedroom day with longdissolve
    "I barely had any sleep last night."
    play music Beautiful
    "As it is, I'm feeling like a kid on Christmas morning."
    "That Nozomi and my girlfriend are coming over to my house to hang out and talk about my hobby? I'm still amazed this is happening."
    "But I gotta get used to this. I can't freak out and get nervous; this is a totally normal thing. I gotta be cool. I gotta stay calm."
    "... I gotta shower before they get here. Shit."
    scene bg k room day with longblink
    play sound doorbell
    "It's not long after I'm showered and changed that the doorbell rings."
    show Sayori casual alert_smile_right at center:
        xpos 0.5
    show Nozomi front casual smile at center:
        xpos 0.25
    with dissolve
    "And opening the door brings the welcome sight of Sayori, together with Nozomi, as I let them both inside."
    ks casual smile "Hey, thanks for coming, you two."
    s alert_laugh "Of course! It's so refreshing to be able to take some quality time away from those idiotic textbooks." with dissolve
    show Nozomi at flip
    n side smile_side "Oh, that reminds me, Sayori. Do you have long before you need to leave? I remember you usually have cram school today." with dissolve
    "Sayori snorts."
    s casual_folded alert_irritated "Practically every day, yes. I won't be attending this time, though." with dissolve
    n sad_side "No? I thought your parents would have a few things to say about that." with dissolve
    s alert_annoyed "Oh, they did." with dissolve
    "Sayori leaves a pause as Nozomi looks to her."
    s casual_handup "I may have said a few things back." with dissolve
    n surprised_side "What?" with dissolve
    "Sayori just chuckles at our faces and shakes her head."
    s alert_smile_right casual "Do not worry yourselves. I don't intend to make a habit of it, but I wanted just this one weekend to be free of all that rubbish." with dissolve
    "And with that, she claps her hands together, as if to signal the end of this topic."
    s casual_folded alert_laugh "Now let's do what we came here for~" with dissolve
    n smile_side "Well... alright. And I admit I've been looking forward to today, Sayori." with dissolve
    n laugh "We hardly ever get to hang out like this~" with dissolve
    s alert_smile "Well, that is something we need to fix, as much as my time allows." with dissolve
    hide Nozomi
    show Nozomi front casual smile at center:
        xpos 0.25
    n "And Kyou, I must admit I'm really curious about this culture fest show you're putting on." with dissolve
    ks "Y- you are?"
    n front2 chuckle "I mean, I don't think you've done anything for the festival on your own steam before..." with dissolve
    n smile "So for you to go all out like this, it makes me think this is something very special." with dissolve
    n laugh blush "S- So I'm excited to be working with you for it~" with dissolve
    show Sayori alert_smile_right
    "Damn, she's gonna make me blush if she keeps on like that." with dissolve
    ks smile blush "Y- yeah, I'm looking forward to it as well. So should we get started?"
    s alert_happy "We should!" with dissolve
    stop music fadeout 5.0
    show Sayori:
        linear 1.0 ypos 1.1
    show Nozomi:
        linear 1.0 ypos 1.1
    pause 1.0
    show Nozomi smile noblush
    "And with that, the pair of them get seated on my living room couch." with dissolve
    show Sayori:
        ypos 1.1
    show Nozomi:
        ypos 1.1
    n "So... I'm sorry, but I have to ask..."
    queue music Downtown fadein 5.0
    show Nozomi at flip
    n side smile "What made you take up hypnosis, Kyou?" with dissolve
    show Sayori alert_smile
    ks surprised noblush "Huh?" with dissolve
    hide Nozomi
    show Nozomi front2 casual pout_left at center:
        xpos 0.25 ypos 1.1
    n "Well I mean, I don't know you very well but I always thought you were more into technology and such." with dissolve
    n neutral "Was I wrong about that?" with dissolve
    ks neutral "Uh, well, I'm pretty big on gadgets and things, so not really."
    n surprised "Oh! So then, what got you into hypnosis?" with dissolve
    n smile "Was it always something you were into, or is this a more recent thing?" with dissolve
    "Goddamn, she's asking me and I kinda want to tell her..."
    "But now that she asks, should I really tell them both that it's all because of her?"
    ks smile blush "Ah... ah, well, I was just on the internet a while back and I was just reading a bunch of things."
    ks "And one thing led to another and I ended up on a ton of articles about hypnosis and it sounded really cool."
    ks "Like, from a... uh, psychological perspective?"
    n "Mhm?"
    ks "Y-yeah, so... I kept reading and started looking up hypnosis scripts and such and I thought... w-well, I thought, uh..."
    s alert_laugh casual "Just show her the penlight you made!" with dissolve
    show Nozomi at flip
    n side sad_side "Huh? Penlight?" with dissolve
    s casual_handup alert_smile "Penlight! Kyou married his love of technology with his interest in hypnosis by modifying an off-the shelf penlight into a useful hypnotic aid." with dissolve
    s casual_folded alert_giggle "He may not look it, but my boyfriend is quite the clever cookie~" with dissolve
    ks sigh noblush "\"He may not look it\"?"
    n smile "Oh my, that does sound ingenious." with dissolve
    "Okay, I'm a little grateful that Sayori rescued me from my stuttering justifications."
    show penlight at right with moveinright:
        ypos 0.346
    "Now all I need to do is show Nozomi the penlight and we can move things along."
    ks smile "Yeah, this is it."
    hide Nozomi
    show Nozomi front2 casual neutral at center:
        xpos 0.25 ypos 1.1
    "Nozomi leans in to examine the thing, although she quickly seems to catch on that there's nothing special to look at." with dissolve
    n "So, what makes this different to using any other penlight for a hypnotic induction?"
    ks "I added some patterning to the beam it emits. People who look at it should be induced into fixating on it more than if it were just a standard beam of light."
    n surprised "Is that so?" with dissolve
    hide penlight with moveoutright
    s casual alert_smile "I shared your skepticism, Nozomi, but I know firsthand that it is very effective." with dissolve
    show Nozomi at flip
    n side surprised_side "Oh! So he really did hypnotize you?" with dissolve
    s alert_happy "Several times, in fact. It's the reason I've been sleeping so well as of late." with dissolve
    n surprised "Really?! And you've only been doing this since Monday?" with dissolve
    s alert_laugh "Uh-huh." with dissolve
    hide Nozomi
    show Nozomi front2 casual surprised at center:
        xpos 0.25 ypos 1.1
    n "And Kyou, Sayori is the first person you've hypnotized?" with dissolve
    ks smile "Uh, that's right, yeah."
    n shocked "Oh my gosh, that's incredible!" with dissolve
    s alert_smile "Mhmhm, I was surprised as well~" with dissolve
    show Nozomi at flip
    n side shocked_side "B-but Sayori, if he really did have such an effect on you in just a couple of days it really is amazing." with dissolve
    ks "Or... or Sayori is really good at being hypnotized."
    n surprised "I... I guess that could factor into it? But she'd still need a talented hypnotist to work with." with dissolve
    n "So this..."
    n laugh "This is really exciting!" with dissolve
    show Sayori alert_happy
    "We all share a chuckle. I knew Nozomi was interested in this stuff, but seeing her light up at the possibilities is really something." with dissolve
    hide Nozomi
    show Nozomi front2 casual smile at center:
        xpos 0.25 ypos 1.1
    n "O- okay, so have you two tried anything else?" with dissolve
    "Before I can answer, Sayori chimes in."
    s alert_smile "As a matter of fact, we have~" with dissolve
    "Nozomi looks back to me and I can only nod as Sayori continues."
    s casual_handup "Kyou was emboldened by his success, so we tried something I imagine was even more ambitious." with dissolve
    show Nozomi at flip
    n side smile_side "Really? What was it?" with dissolve
    s alert_happy "He tried giving me a second personality that he could turn on and off at will." with dissolve
    n surprised_side "He, w-..." with dissolve
    n surprised "What?" with dissolve
    s casual_folded alert_smile "That would have been a fun trick to pull off on a stage. But I am not surprised that it didn't succeed." with dissolve
    show Nozomi frown with dissolve
    pause 1.0
    n surprised_side "It didn't?" with dissolve
    ks surprised "N-no, that was a bit much for us."
    "Yyyeah, I don't think I really want to talk about the \"[alt_name]\" trigger around Nozomi. I gotta change the subject."
    ks smile "So we should think of something else to do for the show. Something that I might be able to pull off with strangers."
    n neutral "... Of course. Speaking of which, do you know how much time you have for your show?" with dissolve
    "Nozomi sees me making a face, then answers her own question."
    n smile "That's what I thought. You have around twenty minutes." with dissolve
    show Sayori alert_surprised
    ks sigh "Seriously?" with dissolve
    s casual_handup "That does seem a little on the short side." with dissolve
    hide Nozomi
    show Nozomi front casual chuckle at center:
        xpos 0.25 ypos 1.1
    "Nozomi chuckles at our disbelief." with dissolve
    n "Neither of you are big on the school culture fests, huh. Seems you really do need me after all~"
    show Sayori alert_neutral
    n smile "As our class rep I could try to lobby for more time, but if I were you I'd work on the assumption that you'll have no more than twenty minutes." with dissolve
    n neutral "So whatever you end up doing, it needs to be fairly simple." with dissolve
    ks frown "Right, yeah, that makes sense..."
    n neutral_right "And you should have your participants picked out before the show begins." with dissolve
    n neutral "We could even ask around for volunteers before the day itself so you can hit the ground running." with dissolve
    "Honestly, her talking about the time pressure and needing to bring a bunch of strangers in is making me nervous."
    ks sigh "This is starting to sound like I've bitten off more than I can chew."
    show Nozomi neutral_right
    s casual alert_laugh "Ahaha, you'll be fine, Kyou~ Remember I'll be participating, and you know I can be hypnotized quickly and easily." with dissolve
    s alert_smile_right blush "So if you keep that in mind, you really have nothing to fear." with dissolve
    show Nozomi at flip
    n side smile "Um, right... That does work to your advantage." with dissolve
    ks smile blush "Y-yeah, you're right. Thanks, Sayori, that does help."
    n neutral "So that leaves the matter of what to do with your volunteers while they're up there. Did we have any thoughts on that?" with dissolve
    s casual_folded alert_surprised noblush "I remember reading about catalepsy while I was doing my preliminary research on the subject." with dissolve
    n neutral_side "Catalepsy...? Oh, that's when people's bodies go rigid, isn't it?" with dissolve
    n smile_side "Like being able to get someone to extend their arm and make them think it's turned into an immovable steel bar or something." with dissolve
    s alert_laugh "Exactly! I think that's a common trick at stage hypnosis shows." with dissolve
    n happy "It is. Most people take to that suggestion pretty well under hypnosis." with dissolve
    ks smile noblush "But what about you, Nozomi? Did you think of anything I could do?"
    hide Nozomi
    show Nozomi front2 casual pout_left at center:
        xpos 0.25 ypos 1.1
    show Sayori alert_smile
    n "Well... I'm trying to think of things that Satoshi didn't do at his show last year." with dissolve
    n neutral "Memory play, perhaps? Getting people to forget a number and having them count would be a neat trick if you can pull that off." with dissolve
    ks "Right. What about turning people into chickens, though? That's pretty common on hypnosis shows, right?"
    n irritated "Uh, very common. Satoshi basically did that on his show." with dissolve
    s alert_happy "Mhmhmhm, I remember it well. I think I'd like to see that again, Nozomi~" with dissolve
    n pout blush "I don't know what you're talking about." with dissolve
    "I do. Nozomi being hypnotized to sound like a chicken was probably the most talked about part of last year's show."
    "I don't know where she learned what a chicken sounds like, but it was so wrong. And so funny."
    "... It's why I suggested it, actually."
    n frown "Moving on... Kyou, you need to decide which suggestion you want to lead with." with dissolve
    show Sayori alert_smile_right
    "The pair of them look to me to make a decision." with dissolve
    "Any of these sound like they'd work, but if I had to pick one then I'd like to do..."
    menu:
        "Catalepsy":
            pass
        "Memory loss":
            pass
        "Chickens":
            pass
    n neutral noblush "Alright. Hopefully it goes without a hitch so you have time for something else." with dissolve
    "I nod, but as she says that I realize this this is the perfect opportunity to do what I've been dying to do for months."
    ks smile blush "Right, so... I should rehearse, right?"
    n neutral_left "Well... yes, of course." with dissolve
    show penlight at right with moveinright:
        ypos 0.346
    "Holding up the penlight again, I look to her with what I hope is an assured smile but I fear is more of an embarrassed grin."
    ks "S- so what do you say? Would you like to see if I can hypnotize you and try it out?"
    n shocked blush "Uh..." with dissolve
    hide penlight at right
    "Sayori giggles and jumps in her seat excitedly."
    s casual_handup alert_laugh "Oh Nozomi, you HAVE to try it!" with dissolve
    show Nozomi at flip
    n side sad_side "I- I do?" with dissolve
    s alert_smile "Absolutely! I know Kyou can do it with me, and I know how nice it was~" with dissolve
    s alert_happy "And I think it'd be fun to watch you get hypnotized again. Just like last time." with dissolve
    ks "If... if you don't want to, that's fine too. Like, no pressure."
    s alert_smile "That's right~ But you are among friends, Nozomi. And I have a feeling you will enjoy this very much." with dissolve
    n sad_closed "Th-that may be true, but..." with dissolve
    "Nozomi gently clears her throat and runs a hand through her hair, before turning to face me again."
    hide Nozomi
    show Nozomi front casual smile at center:
        xpos 0.25 ypos 1.1
    n "Actually, we might be getting ahead of ourselves." with dissolve
    show Sayori alert_surprised
    ks surprised noblush "Huh?" with dissolve
    s alert_concerned "I am not sure what you mean?" with dissolve
    show Nozomi at flip
    n side frown_side "W-well, it's just that Kyou is not the most... uh, eloquent of public speakers, is he?" with dissolve
    s casual_folded alert_neutral "True..." with dissolve
    "I'm not liking where this is going."
    n neutral "So Kyou, now that I think about it, I'm sure it would be helpful if we wrote out a script for you." with dissolve
    ks confused "A script?"
    n smile "Yes. So you can introduce yourself to the audience and settle your nerves before getting on with the show proper." with dissolve
    "Sayori and I both seem to groan at the same time."
    s alert_concerned "That does seem like it would be useful, I'll admit." with dissolve
    hide Nozomi
    show Nozomi front2 casual smile at center:
        xpos 0.25 ypos 1.1
    n "I know that's not as fun, but if you're serious about doing this show, then you need to make sure you've covered everything." with dissolve
    n "So it makes sense that we start from the beginning."
    "I nod with a sigh. She's not wrong, but after so much talk already I was hoping to have a little fun."
    "But I can tell Nozomi isn't going to let this go and I don't want to anger her, so..."
    show Sayori casual alert_smile_right
    with longblink
    "We spend a good while going over my lines and getting a little speech written down for me to practice saying aloud."
    s "So how does that look? Are we done?"
    ks neutral "I think it looks good."
    "I answer, but I think Sayori was saying it more to Nozomi than to me."
    "It's only a short introductory script, just a few lines, but she deliberated over every little thing."
    "This last half hour or so has been a little annoying to tell the truth."
    n pout_left "{cps=20}It's adequate, I suppose. Flows well, shouldn't be too hard to remember- {/cps}{w=1.0}{nw}" with dissolve
    s alert_laugh "Wonderful, now back to the fun stuff!" with dissolve
    show Nozomi at flip
    n side surprised_side "I- I mean, we could probably edit it down a bit more if we wanted?" with dissolve
    s alert_smile "Nozomi, I will be plain: Working on this script felt too much like my group study sessions and I am absolutely done with that." with dissolve
    s "We wanted to have fun today! I... I thought you wanted that as well, Nozomi?"
    "She talks to her friend with a smile, but she can't quite mask her irritation."
    n frown_side "Of course I do, Sayori, I just... w-well, it's just..." with dissolve
    stop music
    play sfx3 ringtone loop
    play sound cellvibratelong loop
    show Sayori alert_surprised_right
    show Nozomi surprised_side
    "Just then, a loud melody pierces the atmosphere." with dissolve
    ks frown "Ow. What the hell is that?"
    n frown_side "That's her cell." with dissolve
    "Sayori giggles as she pulls her wildly-vibrating phone out of her pocket."
    show Nozomi neutral_side
    s alert_laugh casual_folded "Yes, well, sometimes I'd sleep through it so I needed it to be this obnoxiously loud and distracting." with dissolve
    s "I should probably fix that. Anyway, I'll just be a moment."
    stop sound
    stop sfx3
    s casual_handup alert_smile "Hello? Dad?" with dissolve
    show Sayori:
        linear 1.0 ypos 1.0
    s "..."
    show Sayori:
        ypos 1.0
    s "Did we not discuss this already?"
    s "... Uh-huh."
    show Sayori at flip
    s "Yes, but... Dad, I..." with dissolve
    show Sayori:
        linear 1.0 xpos 0.75
    pause 1.0
    s alert_annoyed "I know how much it costs, and I appreciate it, truly, but you see..." with dissolve
    show Sayori:
        xpos 0.75
    show Nozomi sad_side
    s alert_angry_right "And what if I do, Dad? Do you realize how stressful this is for me?" with dissolve
    s "The relentless... no."
    s alert_irritated "*sigh* No, of course not." with dissolve
    s "I know it's only... alright."
    s alert_angry_right "Yes, ALRIGHT. I said I'll go." with dissolve
    s alert_concerned "... Of course. I'm sorry for shouting." with dissolve
    s "Love you too, Dad."
    "Sayori hangs up the phone and sighs."
    hide Sayori
    show Sayori at center:
        xpos 0.75
    s casual alert_concerned "Seems I will not be able to wrangle my way out of cram school today after all. I need to go." with dissolve
    n sad_closed "Of course. We understand." with dissolve
    s casual alert_irritated "I so wanted a weekend without any of this nonsense..." with dissolve
    "She snorts at the air, before her demeanor shifts and she puts on a smile for us both."
    show Nozomi neutral_side
    s alert_happy "But I suppose it cannot be helped. I enjoyed our morning together, at least~" with dissolve
    s alert_smile_right "And Kyou, we are still on for tomorrow. I do actually have the entire evening free." with dissolve
    ks smile blush "I- I'm looking forward to it, Sayori."
    scene bg blackscreen with dissolve
    play sound doorclose
    pause 1.0
    scene bg k entrance day with dissolve
    "I see Sayori off with a sigh. That was such an awkward way to end the morning."
    n "She's never missed a day of school, you know."
    show Nozomi side casual frown at center
    ks casual surprised noblush "Huh?" with dissolve
    "As I turn away from my front door, I realize Nozomi didn't leave with her friend. I kinda presumed she would."
    n frown_side "Not cram school, not regular school. No matter how unwell she got sometimes." with dissolve
    n sad_side "... It's not something I liked to see, but that's how she is." with dissolve
    n sad "So you can imagine what a shock it was that she nearly didn't show up for school the other day." with dissolve
    n sad_closed "We were so worried..." with dissolve
    "Why is she telling me this?"
    hide Nozomi
    show Nozomi front casual at center
    n "Can I ask you something, Kyou?" with dissolve
    ks confused "Uh... what's that?"
    n front2 "Sayori mentioned you tried giving her a second personality? Is that right?" with dissolve
    "Ah, shit. I was hoping to avoid this."
    ks frown "Oh, well like, it wasn't really serious or anything."
    n concerned "What was this personality supposed to be like?" with dissolve
    n "How was Sayori meant to act that was different to how she usually is?"
    ks "It... it doesn't really matter. I mean, like she said, it didn't work."
    n frown "It wouldn't be subtle, that's for sure. She'd have to obviously contradict who she is, otherwise it wouldn't be entertaining." with dissolve
    ks neutral "Uh, right, if it worked."
    show Nozomi side
    play music Measured
    n frown "It'd certainly be crazy if Sayori suddenly hated studying for her all-important entrance exams to get into med school." with dissolve
    n frown_side "So much so that she'd skip cram school and mouth off to her parents about it." with dissolve
    n front casual irritated "But maybe I don't know Sayori as well as I thought, huh?" with dissolve
    ks "Maybe..."
    "Nozomi sighs through her nose."
    n frown "Or maybe the hypnosis you did on her worked just as you intended." with dissolve
    "I can't help but grimace as she glares at me."
    n "Maybe you weren't expecting Sayori to go along with something so dangerous, but she takes to it better than expected and maybe you're both surprised by that."
    n side frown_side "It might be a neat trick to go along with at a party or a stage show..." with dissolve
    n irritated "But a trick should end when the show's over." with dissolve
    n frown "Is any of this getting through to you, Kyou?" with dissolve
    ks surprised "U- Uh..."
    "Goddamn, I was not prepared for this. But..."
    ks "Okay, Nozomi, I think I know what you're saying but... do you know how hypnosis works?"
    n front angry "I know enough, Kyou. I certainly know that you shouldn't let people go with... with dangerous hypnotic suggestions in their heads!" with dissolve
    ks frown "I mean... okay, but hypnosis isn't that powerful, Nozomi."
    show Nozomi frown
    ks "If Sayori's still walking around pretending to be this other person, you don't think it's because she really wants to be like that?" with dissolve
    ks "Maybe all I did was give a little encouragement."
    n irritated "Oh my god, are you even listening to yourself?" with dissolve
    n determined "You think she WANTS to argue with her parents in front of us?" with dissolve
    n "She wants to ease up on her college studies right before entrance exams, after she's worked non-stop all these years? That seems likely to you?"
    ks sigh "I... I mean, it's like I said, do you really think hypnosis is that powerful? Like I could make her do that all by myself?"
    ks "And..."
    "It almost doesn't feel right to say this out loud, but..."
    ks frown "And maybe you didn't know, but Sayori's had her eye on me for years. Did you know that?"
    n front2 "Eh?" with dissolve
    ks frown "Y- yeah, it was a shock to me too. But she said she was interested in me before I did this personality stuff with her."
    ks "S-so yeah, maybe it isn't that weird she'd be comfortable with this stuff, or that we're dating now."
    "Nozomi holds a hand to her head and gasps."
    n side irritated "Oh... oh my GOD, I even forgot you're dating now. That is just..." with dissolve
    ks "What? You don't think I deserve a girlfriend?"
    n front2 angry "She's under duress, you... you IDIOT!" with dissolve
    n side frown_side "I just... I really don't know how you managed all this." with dissolve
    n frown "It sounds far-fetched to say it, but Sayori's obviously not herself and there's only one probable cause." with dissolve
    n front angry "You HAVE to fix this, Kyou. You HAVE to!" with dissolve
    ks frown "You can't trust her to snap out of this if she's had enough?"
    n determined "I think you're trying to duck responsibility for what you've done." with dissolve
    n front angry "You either fix this, or I'll fix it for you!" with dissolve
    ks "So you really don't think she might be happy like this? Like, of her own free will?"
    n side frown "Kyou... If you really believed that, you wouldn't think twice of making sure Sayori's in her right mind, now would you?" with dissolve
    n "You'd have made sure she was free of your hypnotic influence and asked her straight up how she felt."
    n furious "But you're not willing to do that, and I think we both know why that is." with dissolve
    ks "I... I love her, Nozomi. I'll never do anything to hurt her. And I trust she knows what she's doing too."
    "Nozomi sighs."
    n frown_side "If you really mean that, Kyou, that you love her... you'll do the right thing." with dissolve
    n irritated "When you meet her tomorrow, you'll have your chance." with dissolve
    stop music fadeout 5.0
    scene bg k bedroom eve with blink
    "So I think Nozomi might hate me now."
    "When she left the house, she told me again to do the right thing: Reverse the personality suggestions I hypnotically gave Sayori."
    "To be honest, I don't appreciate her putting a dampener on my date tomorrow."
    "My biggest chance of happiness in my life, and she of all people has to shit on it."
    "It's hard to take, coming from someone I still admire so much."
    play sound cellvibrate
    show phone at right with moveinright:
        ypos 0.346
    queue music Past_Sadness
    "Just then, my phone starts to buzz with a text."
    "{color=#385599}Cannot wait until tomorrow. Let's meet in town xx{/color}"
    hide phone with moveoutright
    "It brings a little smile back to my face."
    "Me and Sayori haven't had any time to plan what we're doing tomorrow, so I guess we're just gonna do whatever."
    "I start to tap out a reply. Nozomi might have left me on a downer, and maybe I have a decision to make, but I'm not about to let her ruin tomorrow for me."
    "We're gonna have our date, and it's gonna be amazing. How could it not?"
    "Against all the odds, it feels like Sayori's the perfect match for me."
    "Smart, actually kinda pretty when I look at her and... that playful side she's showing is just something else."
    "If I can make her happy, then who's to stop us from keeping this going?"
    "Not Nozomi. Not anyone."
    show bg blackscreen with dissolve
    "Let's keep dreaming..."
    stop music fadeout 5.0
    jump Day7_Con_Kyou_Sayori_Alter

label Day6_Switch_Safe:
    scene bg k bedroom day with longdissolve
    "Waking up early the next morning, I make sure to get myself ready well in advance."
    "Nozomi messaged me last night, seeing as we didn't actually arrange a proper time to do this."
    play music Bright_Opening
    "Nine o'clock, she said. I didn't really want it to be that early, not on a weekend... But she did insist."
    "Something about having \"stuff\" to do later and this was the only way to fit this into her schedule."
    "Would've liked to have laid in some more, but I guess I don't mind too much. At least I wasn't up too long last night planning what to do with her."
    "After what I've learned, thinking up something that'd get her excited wasn't so hard."
    play sound doorbell
    "And that's the doorbell. Nine on the dot; she really isn't messing around."
    scene bg k entrance day with blink
    "This time, I think we've both going to have some fun..."
    play sound dooropen
    show Nozomi front2 casual smile at center
    with longdissolve
    n "Good morning!"
    ks casual smile "Hey, Nozomi. Do you want to get straight to it?"
    play sound doorclose
    show Nozomi side smile_side
    "Nozomi doesn't meet my gaze as she shuts the door behind her." with dissolve
    n "Well..."
    "I just asked her for the sake of having something to say. But now that I've mentioned it..."
    n happy blush "That's why we're here, isn't it?" with dissolve
    "... Maybe it *should* bother me a little that this is all she seems to want me for?"    
    # "They greet each other at the door and Nozomi, as ever, is keen to get started." with dissolve
    scene bg k room day
    show Nozomi front casual smile at center
    with blink
    n "So what's the plan for today, Kyou?"
    "It's at least earned me the right to mess with her a little, I reckon."
    ks casual smirk "... Do you trust me?"
    n surprised "Do I... do I trust you?" with dissolve
    ks "It's a simple question. Shouldn't need thinking about."
    show Nozomi front2 pout
    "Nozomi scoffs as she no doubt realizes I'm throwing her own words back at her." with dissolve
    n "Oh, youuu..."
    scene cg k room day
    show NozomiHypnoDay standing frown
    with blink
    "But after a moment's silence, she takes to the couch and gives me a slow, reluctant nod."
    n "I suppose. {w=1.0}{cps=20}And if you want to surprise me I guess that wouldn't be so bad-{/cps}{w=1.0}{nw}"
    stop music
    ks casual smile "Then it's [hypno3!l], Nozomi."
    play music Flow fadein 5.0
    show NozomiHypnoDay drooping sleep
    n sleep "..." with dissolve
    "It's been a couple of days since I used that trigger, but practically the moment I got those words out of my mouth, Nozomi's eyes fluttered closed and she slumped back on the couch."
    ks "That's right, Nozomi. It's time once again to drift away and relax, deeper and deeper, all the way back into this comfortable state of hypnosis."
    "But after the number she did on me last night, I guess I'm not surprised to find she's every bit as susceptible to me as I am to her now."
    ks neutral "Breathe in. Breathe out... Letting everything go as you find yourself relaxing even deeper..."
    "We must be just that good, at both sides of the craft."
    ks "Just let that nice, relaxing feeling sit with you for a moment. I'll be right back."
    # "She pouts, but after a moment's silence tells him she's okay with being surprised and that she does trust he won't take things too far." with dissolve
    # "So she gets seated and Kyou proceeds to hypnotize her once more." with dissolve
    # "Kyou finds her just as easy to hypnotize as before. It really is something that the pair of them are both so good at both sides of the craft, he muses." with dissolve
    scene bg blackscreen with dissolve
    "I leave her quietly to head to the kitchen, opening the fridge to pull a can of soda before briskly rushing back..."
    scene cg k room day
    show NozomiHypnoDay drooping sleep
    with dissolve
    "... And placing the can soundlessly on the table in front of her."
    # "And as she sinks back into a relaxed trance, Kyou leaves her for a moment to head to his kitchen, take a can of soda and set it down on the table in front of them." with dissolve
    # "Then he makes the suggestions he's had in his head all night."
    ks casual "Now, Nozomi, I want you to listen very carefully..."
    "Let's see if I'm right about this getting you excited."
    ks "When you next awaken, you will notice the can of soda in front of you, and believe that the drink inside is laced with a powerful truth serum."
    # "First, he tells her that the can of fizzy pop she sees on the table contains a powerful truth serum."
    ks "Every time you drink from it, you will feel compelled to answer truthfully to any question I ask you."
    ks "Do you understand and accept what I've told you, Nozomi?"
    show NozomiHypnoDay sleeptalk
    n sleeptalk "Mmn... yes..." with dissolve
    show NozomiHypnoDay sleep
    ks "Wonderful. When you awaken, you will also realize that you are feeling unbearably thirsty." with dissolve
    ks "The more you try to resist the feeling, the more compelled you'll feel to quench your thirst with the soda in front of you."
    ks "Your drinking it will quench your thirst temporarily, but as soon as you give an answer to one of my questions, you will find that unbearable thirst return every bit as strong as before."
    ks "Understand, Nozomi?"
    show NozomiHypnoDay sleeptalk
    n sleeptalk "Yes... I understand..." with dissolve
    show NozomiHypnoDay sleep
    "Maybe this is a simple thing, but I really think this will play into Nozomi's want to feel less in control." with dissolve
    ks "Now, waking up on the count of three, feeling good and refreshed and ready to act on my suggestions in..."
    "And if all goes well, I'll definitely get to know her even better today."
    stop music fadeout 5.0
    ks "One, two... three."
    show NozomiHypnoDay sleepy
    n sleepy "Mmmn..." with dissolve
    ks smile "Rise and shine, Nozomi."
    scene NozomiCola nozomi1 dazed cola with blink
    "I watch and wait as she stirs herself back to wakefulness."
    play music Dating3
    n "So are you going to tell me what you... mrrn."
    show NozomiCola frown_side
    "... She frowns as she seems to swallow uncomfortably, and a moment later her eyes settle on the can lying tantalizingly on the table between us." with dissolve
    n "Okay, that wasn't there before."
    ks casual smile "Yeah, I thought you might be thirsty."
    show NozomiCola frown
    "My words cause Nozomi to shoot me an accusing look." with dissolve
    show NozomiCola pout
    n "Oh you thought so, did you? So that's how it is." with dissolve
    "And I can't help but let a grin form on my lips at what I'm about to say next."
    ks smirk "Now I have a question for you."
    show NozomiCola nozomi2 concerned
    "Her eyes then glance somewhat anxiously back to the can, then to me as she starts to massage her throat." with dissolve
    ks "Will you tell me some more about your hypnotic fantasies?"
    show NozomiCola surprised
    n surprised "Huh?! I..." with dissolve
    show NozomiCola concerned
    n side sad "That's a... a little uncomfortable to talk about, Kyou. Besides, I think you've intuited enough already." with dissolve
    show NozomiCola uncomfortable
    "She says that, but her eyes have already darted back to the can as she dryly licks her lips." with dissolve
    ks "Maybe you just need a drink to settle your nerves."
    show NozomiCola frown_side
    "Nozomi grimaces, fingers at her throat as she lets out a pained sigh through her nostrils while she fights what she knows is inevitable." with dissolve
    "I just need to wait just a few moments more until..."
    n "Ugh... you bastard..."
    show NozomiCola nozomi4 -frown_side -cola
    "Until she helplessly reaches out for the can, pulls it open and takes a few needy gulps of the liquid before slamming it back down on the table and recoiling from it." with dissolve
    show NozomiCola nozomi1 sigh cola_open
    n front2 sleeptalk_concerned "Aaahhhh..." with dissolve
    ks "So what about those hypnotic fantasies of yours?"
    show NozomiCola surprised
    n surprised "Oh! Well, I..." with dissolve
    show NozomiCola nervous_side
    n side sad_closed "I'm really into fantasies where I can imagine myself being non-consensually hypnotized and brainwashed." with dissolve
    ks surprised "Uh... w-wow, okay."
    "I get my answer, and I'm not sure what I was expecting, but..."
    ks confused "So you really want someone to just... straight-up take you away and do whatever they want to you?"
    "This is really going over my head right now."
    show NozomiCola mad blush
    n front2 angry "What?! No!" with dissolve
    "As is that reaction. But I let her explain herself."
    show NozomiCola frown
    n side frown_side blush "That's not what I want! There's a difference between imagining something like that and having... feelings about it, and having something like that actually happen!" with dissolve
    show NozomiCola frown_side
    n frown "That's why it's a fantasy! It's not necessarily something you'd wish on yourself, or anyone." with dissolve
    show NozomiCola sigh
    n front2 sleep "And it only works at all if everyone involved understands that and plays their roles to perfection." with dissolve
    show NozomiCola concerned
    n front2 sleeptalk_concerned "It's like... it's like this delicate dance." with dissolve
    ks neutral "Right, right."
    "When she's finished giving me an earful, she slumps back into the couch and sighs."
    show NozomiCola sigh -blush
    n neutral_right -blush "... I can't believe you just made me tell you all that, hypnosis be damned." with dissolve
    "Is she upset with me now? I didn't think this would be that big of a deal."
    ks confused "Isn't it better that I *do* know, seeing as this is what we're doing?"
    show NozomiCola dazed
    n sleeptalk "I don't know... maybe? It still makes me a little uncomfortable being this open." with dissolve
    show NozomiCola neutral
    n neutral_left "But... yes, I suppose I'm not completely put off by telling you either." with dissolve
    show NozomiCola nozomi2
    "As she makes this admission, I notice her hand reaching for her throat again." with dissolve
    show NozomiCola concerned
    n neutral "You kinda... do need to know these things, I guess." with dissolve
    "Looks like it's time I broke the tension with another question; maybe something she'd feel a little more forthright about answering."
    ks neutral "So how do you think all this is going between us? You said before that it's everything you thought it'd be; is that still true?"
    show NozomiCola sigh
    n sleeptalk "Ahh..." with dissolve
    ks smile "Not gonna answer right away, huh? Mouth too dry?"
    show NozomiCola nozomi4 -sigh -cola_open
    "Nozomi grumbles as she reaches for the can again to take another swig..." with dissolve
    show NozomiCola nozomi3 disgusted
    n pout "Blech. I don't know how you drink this stuff without being forced to." with dissolve
    ks "What? You're not a fan of cola?"
    show NozomiCola frown_side
    n neutral "Not really. Orange or melon would be more to my taste, if I'm going to drink something carbonated." with dissolve
    "Good to know I guess. But..."
    ks smirk "So how about you answer my question?"
    show NozomiCola smirk
    n smirk "I believe I just did." with dissolve
    "Oh, is that how it's gonna be?"
    ks smile "Haha come on, just tell me!"
    "At least she seems to have perked up a bit thanks to my little mistake."
    ks "You know, I don't think I told you it had to be just the one question."
    show NozomiCola happy
    n chuckle "Hm... Well that's definitely how I interpreted it~" with dissolve
    "As pleased with herself as she seems to be, I can already see her licking her lips dryly."
    show NozomiCola smile
    n neutral_right "Maybe if you didn't phrase your suggestions so sloppily." with dissolve
    show NozomiCola nozomi4 -smile
    ks frown "Hey, how would you know how I phrased my suggestions?" with dissolve
    "Just as I ask, Nozomi swiftly takes another gulp of the apparently unpleasant soft drink."
    show NozomiCola nozomi3 disgusted
    n sleeptalk "Ahh, I don't. I'm just going by how I'm able to defeat you like this." with dissolve
    show NozomiCola smile
    "Ugh! How did she get me AGAIN?!" with dissolve
    ks sigh "You're seriously gonna leave me h-..."
    "I stop myself again as I catch Nozomi's smile; her can hand twitching like she's about to take another sip."
    ks neutral "Alright, Nozomi. No more questions; at least not yet."
    show NozomiCola happy
    n chuckle "Mhmhmh~" with dissolve
    ks smile "I shouldn't have to wait too long before I get that answer out of you."
    show NozomiCola smile
    n smile "M-maybe, maybe not..." with dissolve
    "Oh come on, Nozomi. I can already see a grimace behind that deceptive smile of yours."
    ks confused "I just can't believe you're trying to resist over a question like that!"
    show NozomiCola pout
    n pout_left "It's the... mmh... p-principle of the thing!" with dissolve
    "She agitatively twitches her bare foot on the couch, her hand crossed over to press down on her arm as if she were trying to restrain herself from taking another compulsive sip."
    ks smirk "Go on... you know you want to."
    show NozomiCola uncomfortable
    n irritated "Urrgh... darn it." with dissolve
    show NozomiCola nozomi4 -uncomfortable
    "Sure enough, her restraining hand slips away as she once again lifts the can to her trembling lips and downs another needy mouthful of cola." with dissolve
    ks smile "So? Are you happy with how this is going or do you want more out of this?"
    show NozomiCola nozomi3 dazed
    n sleeptalk_concerned "Ahhh... I-I think it's been going great. But..." with dissolve    
    ks confused "But...?"
    show NozomiCola concerned
    "The can drops back down to her lap as Nozomi's lips crinkle in trepidation." with dissolve
    n "I do think we could be doing more."
    ks "More? More how?"
    show NozomiCola neutral
    n neutral_left "I-I don't know. Maybe it already *is* becoming more than I set out for it to be. After all..." with dissolve
    show NozomiCola nervous_side
    n neutral "I did make a rule about you not putting things in my head without permission. Yet here we are." with dissolve
    "I... That takes me flinch a little."
    ks "Y-yeah, but... hey hold on!"
    show NozomiCola neutral
    n "Hm?" with dissolve
    ks surprised "You started this! Yesterday you wanted to surprise me with your own suggestion and I didn't complain about that, did I?"
    show NozomiCola concerned
    n sleep "Hmm... I suppose, that's true. Although I don't recall you setting such a rule for me." with dissolve    
    ks frown "It's still a big deal though, right? So is it really that bad that I did the same to you?"
    show NozomiCola nozomi4 -concerned
    ks "Are you really saying that your rules can't be broken but you won't apply the same rules to me?" with dissolve
    "Yeah, I can't help but be a little annoyed at the attitude she's taking. But as I finish my sentence I realize Nozomi is drinking again."
    stop music fadeout 5.0
    show NozomiCola nozomi3 dazed
    n sleeptalk "Mmh... Honestly, I'm a little disappointed you haven't tried to break my rules *more*." with dissolve
    ks surprised "... Wait, what?!"
    queue music Night_Road fadein 5.0
    "This woman... I'm getting so confused by what she's telling me."
    "Like, she talks about the difference between wanting a fantasy and actually having bad things done to her."
    "But now she's telling me she wants to be actually taken advantage of? Is that it?"
    "I don't know what to say to that."
    show NozomiCola nozomi2 concerned cola_open
    "And as I stand there in dumbstruck silence, Nozomi sets the can down on the table and shakes her head ruefully as she massages her throat again." with dissolve
    n "Can we stop this now, Kyou? I'm starting to feel a little gassy from drinking this crap..."
    $ persistent.nozomi_cola_unlock = True
    stop music fadeout 5.0
    scene cg k room day
    show NozomiHypnoDay drooping sleep    
    with longblink
    "After she unloaded that little bombshell on me, I was all to happy to comply."
    play music Downtown
    ks casual neutral "Waking up now, no longer affected by my suggestions today and remembering everything in one, two..."
    "And besides, I'd be interested to hear what she has to say about it when she's no longer under my hypnotic compulsion to talk."
    ks "Three."
    show NozomiHypnoDay sleepy
    n sleepy "Hmmmh..." with dissolve
    ks "Wide awake, Nozomi. How are you feeling now?"
    show NozomiHypnoDay standing confused
    n surprised "Huh? Oh, I..." with dissolve
    "I give her a moment to rouse herself back to full awareness. To remember that hypnotically-compelled conversation we just had."
    scene bg k room day
    show Nozomi casual front2 scared at center:
        ypos 1.1
        linear 2.0 ypos 1.0
    with blink
    n scared "Ahh no! Nonononono!"
    ks casual confused "No?"
    n pain "Forget what I just told you about breaking my rules! I said all that under duress, you hear me?" with dissolve
    "I perk an eyebrow at that response."
    ks "Is that right?"
    "After all, if all that she said really was her sincere, honest thoughts..."
    n frown "Yes, obviously!" with dissolve
    "And I don't have any reason to doubt that they are..."
    n angry "OBVIOUSLY it would be bad to overstep my boundaries so don't you dare think about it!" with dissolve
    "... Then can I really trust what she's panickedly telling me now?"
    ks sigh "Alright, alright! I'm not gonna do anything crazy with you, I swear."
    n sleeptalk_concerned "Haahh... y-yeah, I... I trust that you won't Kyou, it's just..." with dissolve
    n side sad_side "... I don't know. You *were* right about me overstepping myself, and it wasn't exactly the worst thing." with dissolve
    n sad "Maybe it wouldn't be so bad if we bent the rules just a little bit more?" with dissolve
    "... Once again, this woman is confusing me. And I wait for her to finish her contradiction."
    n neutral_side "Things are going to get busy for the both of us really soon. Exam season's starting, then there's the culture fest." with dissolve
    n neutral "Before that, there's tomorrow. I need to be there to support Hiroko all day, and then we're partying into the night." with dissolve
    n front "It doesn't leave us with a lot of time to do more of this, does it?" with dissolve
    "I shake my head reluctantly as I realize how right she is about that. But..."
    ks neutral "So what do you mean about bending the rules, then?"
    n neutral_right "I mean... maybe it would be okay if we did some of this... outside?" with dissolve
    ks confused "Outside?"
    n smile blush "Y-yeah! It's just an idea, and I'm going to think on it some more, but before I do that..." with dissolve
    n chuckle "... How would you feel about coming to the game tomorrow?" with dissolve
    stop music fadeout 5.0
    scene bg k bedroom night with longblink
    "So after me and Nozomi... talked some more I was left to my own devices."
    play music Past_Sadness
    "After a morning as eventful as this one, the rest of my day inevitably felt like so much wasted time."
    "But now as I get ready for bed, I can't help but feel a pang of anxiety hitting me full in the chest."
    "I really agreed to do this stuff out in public, huh. And I'm okay with this?"
    "Nozomi's okay with this?"
    "I figured I'd be more excited about her wanting to be seen around me now. How quickly she's coming around to that idea."
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    "Maybe I would be if I could remember... remember what exactly she had planned for me..."
    pause 2.0
    jump Day7_Nozomi_Switch_Safe   

label Day6_Con_Kyou_Sayori_Alter_Switch:
    scene bg k bedroom day with longdissolve
    "The next morning comes after a restless night's sleep."
    "I can't stay in bed, not with this anxious feeling wracking my whole body."
    queue music Dating3
    "But I got all morning to kill before the big day I have ahead of me..."
    scene bg street1 day with longblink
    "It takes far too long for the afternoon to roll around."
    "Maybe I'm going to be earlier than Nozomi wanted, but I couldn't take waiting around in the house any more. This is driving me crazy."
    "I can't settle down until I've set things straight with Sayori."
    "But... huh, you know, it's funny. The only reason any of this happened in the first place was because I wanted to get closer to Nozomi."
    "And all this business with Sayori *is* bringing us together. In a weird, roundabout kind of way."
    "Not really the way I'd have planned it, but I guess I'll take it..."
    scene bg n house day with blink
    "Well anyway, I'll just turn in to this street here and... is this really the place?"
    "I check the note Nozomi gave me... this is the address, alright."
    "Looks pretty nice. Nozomi must live well if her family can afford a house like this."
    "Assuming this IS her house and not her idea of giving me the run around."
    play sound doorbell
    "Ugh, I'll put that thought out of my head and just press the doorbell..."
    $atsuko_name = "???"
    play sound dooropen
    pause 1.0
    show Atsuko neutral at center with dissolve
    nm "... Hello?"
    "Instead of Nozomi, I'm greeted by an older woman at the door. She looks about forty I guess?"
    ks casual confused "Uh... h-hey."
    "Now I feel awkward. Did Nozomi really send me to some stranger's house? I really wouldn't put it past her with the way she was to me yesterday."
    nm smile "Is there something I can help you with?" with dissolve
    "Although whoever she is, she seems friendly. Maybe..."
    ks "I... y-yeah, I was looking for Nozomi? N-Nozomi Akemi?"
    nm surprised "OH!" with vpunch
    ks surprised "... W-what?"
    nm laugh "Ahaha, I'm sorry! I'm just surprised, that's all." with dissolve
    nm smile "When my daughter told me she was having another person over for her study group I wasn't expecting a boy~" with dissolve
    ks confused "I... I see."
    "... Right. This is Nozomi's mother. Why the hell did I not realize that sooner?"
    $atsuko_name = "Atsuko"
    nm happy "Oh, but where are my manners? I'm Atsuko; nice to meet another classmate of Nozomi's!" with dissolve
    ks smile "I'm... Kyou. Kyou Koyama. Nice to meet you too."
    scene bg n room day
    show Atsuko smile at center
    with blink
    "Man, I am not used to talking to older people. It's not like I get much practice with my own folks."
    nm "I wonder why she's not here to greet you."
    ks casual smile "Oh... w-well, I guess she's that deep into her books, huh?"
    "More like she's not that keen to see me... But I think I'll keep her mom oblivious to that fact."
    nm happy "Mhmhm, you might be right. That Sayori must have her working hard!" with dissolve
    "Huh? Sayori's already here? And here's me thinking I was way early."
    nm laugh "I just hope you know what you've let yourself in for, young man~" with dissolve
    ks confused "Hm? W-what do you mean?"
    show Atsuko neutral
    "Just then, Nozomi's mother shoots me a somewhat curious expression." with dissolve
    nm happy "Oh, nothing~ Anyway, I should let you get to it; you didn't come here to listen to some old lady natter." with dissolve
    "It's not on her face for long before the smiles are back. But I bet she knows Sayori's study habits as much as anyone in my class."
    nm smile "So go right on upstairs. Nozomi's room is the second on the left." with dissolve
    ks smile "Ah, okay. Thanks."
    "Even she must think Sayori needs to let her hair down once in a while..."
    scene bg blackscreen with dissolve
    "Anyway, I head up the stairs and... okay, second on the left she said."
    play sound doorknock
    stop music fadeout 5.0
    "Let's do this..."
    n "Um, come on in!"
    play sound dooropen
    scene bg n bedroom day
    with longdissolve
    "I open the door to find myself in a spacious-looking bedroom."
    queue music Eons
    "It's a little disorganized, with some board game boxes stashed in a corner and some open textbooks laid out on the floor."
    "Presumably those books are only there to support the lie that we're here to study for school. I doubt we're going to be doing any of that today."
    show Nozomi front2 casual neutral at center
    n "Hello, Kyou. Close the door behind you, please." with dissolve
    "Right. I'm just distracting myself here. I've got some convincing to do."
    ks casual neutral "Uh, yeah. Hey, guys."
    play sound doorclose
    show Sayori casual_folded sleeptalk at center, flip:
        xpos 0.25
    "As I hastily pull the door closed I notice Sayori, who... well, she's still not looking great I gotta say." with dissolve
    n sigh "Yeah... hi." with dissolve
    "I guess this is what Mrs. Akemi was getting at just now."
    ks neutral "S-so... uhh..."
    show Nozomi neutral_left
    "But, man, where to begin. I want to talk to Sayori, but she's still not even looking at me." with dissolve
    stop music fadeout 5.0
    n side frown "Okay, Kyou... I think you need to start by apologizing." with dissolve
    "Nozomi on the other hand is staring daggers right into my very soul."
    if sayori_hurt == True:
        ks sigh "Yeah. Yeah, I know."
    else:
        ks confused "A... apologizing?"
    queue music Measured
    n irritated "I mean, what the hell where you thinking the other night?" with dissolve
    n front2 frown "Sayori told me you hypnotized her into thinking she had a... a personality switch? Do you have any idea how dangerous that is?" with dissolve
    n irritated "And what's more you just LEFT her like that?" with dissolve
    "Yeah Nozomi, you're not wrong but goddamn, I don't need you to tell me how I fucked up."
    ks frown "Look, I KNOW, okay? But how was I supposed to know she'd react like this?"
    n side frown "You don't. You don't know how anyone will take a hypnotic suggestion which is why you always need to be careful." with dissolve
    n frown_side "The most important thing for any hypnotist is to ensure the comfort and safety of their hypnotee." with dissolve
    n frown "Did you know that, Mr. Does-Hypnosis-For-A-Hobby?" with dissolve
    ks "Ugh..."
    n irritated "God. This stuff isn't just a party trick to impress people. It can leave lasting consequences. It can effect people in very real and powerful ways." with dissolve
    n frown "You remember Satoshi? That guy who hypnotized me at the culture fest last year? He understood that. He made sure we were all okay at the end of his show." with dissolve
    n front2 "Every hypnotist, whether an amateur or an experienced professional should understand that." with dissolve
    n determined "And you had BETTER understand that now!" with dissolve
    ks "{cps=15}Nozomi- {/cps}{w=0.5}{nw}"
    n angry "{cps=20}So the least you can do is get on your hands and knees and give her a {/cps}{nw}" with dissolve
    extend "FUCKING apology for what you put her through, do you hear me?" with vpunch
    "I can feel my body tense up and... Christ, I had no idea she could even get this pissed."
    show Nozomi determined
    "My mouth hangs open as my mind races. I want to defend myself. Tell her she's blowing things out of proportion; that nothing I did deserves her raging at me like this." with dissolve
    show Sayori concerned_right
    stop music fadeout 5.0
    "... But I almost feel drawn out of my own body as instead I find myself turning to Sayori and bowing my head." with dissolve
    show Nozomi frown
    ks sad "Look, Sayori I... I'm really sorry about all this." with dissolve
    queue music Monologue
    "And the words just fall out of my mouth."
    ks "I just got excited for what we were doing and... a-and yeah, I got in over my head. It was pretty reckless."
    ks "But I want to do right by you. I know you're afraid of me, but you have to believe I never meant to hurt you. I want to fix this."
    ks "S-so... will you forgive me?"
    s "..."
    s casual_handup sleeptalk "Kyou... I..." with dissolve
    "I begin to raise my head once more, and my spine tenses as Sayori finally begins speaking to me."
    s concerned_right "I do fear you, it is true." with dissolve
    s concerned "Ever since my first hypnosis session I have been left with an unsettling feeling that something was not right. That my mind was being influenced in ways I couldn't fathom." with dissolve
    s neutral_right "At first it was enough to put such anxieties down to my own lack of knowledge in the matter, especially after the explanations you offered me." with dissolve
    s sleep "My intense experience could simply be put down to my high aptitude as a hypnotic subject. No more, no less." with dissolve
    if sayori_hurt == True:
        s neutral_right "But that changed with my second session with you. When an entire twenty-four hours of my life had passed, and yet I did not live to see it." with dissolve
        s casual surprised_right "So to discover that someone else had lived in my place? Interacted with everyone I know as though she were me?" with dissolve
        s sleeptalk "And all because I accommodated your careless want for a moment's frivolity?" with dissolve
    else:
        s neutral_right "But that changed with my second session with you. When that session ended not in your home, but in our classroom a full day later." with dissolve
        s casual surprised_right "If you can truly exert such a level of control over my thoughts and actions that I can in essence be two completely separate people with compartmentalized memories?" with dissolve
    s concerned_right "I cannot begin to describe how terrifying that is to me." with dissolve
    stop music fadeout 5.0
    ks "Sayori..."
    if sayori_hurt == True:
        s casual_folded sleep "Kyou, I am certain your intentions that day were harmless." with dissolve
        s sleeptalk "Surely my reaction came as a surprise to you. I imagine it must have delighted you at first, that I would take to your hypnosis so swimmingly." with dissolve
        s neutral_right "Even so, you must have realized how unconscionable it would be to allow such a state to reside within me beyond the safety of your home." with dissolve
        "The air begins to feel cold around me as Sayori falls silent for a moment. It feels like she wants me to agree."
        "But as I struggle to respond, she begins to speak once more."
        queue music Diary
        s casual_handup "Nozomi informed me that you and I spoke alone during the lunchbreak." with dissolve
        ks surprised "Huh? W-well..."
        s sleep "I have no memory of what we discussed, of course. Only that you had the opportunity to put a halt to this madness there and then." with dissolve
        s concerned_right "You were the only one who could help me, and yet..." with dissolve
        "There's a sadness in her eyes as Sayori searches my expression for an explanation."
        ks "I... w-well, you see..."
        "I can feel my throat closing as I struggle to find the words to respond to a face like that."
        ks "L-Look, you have to understand! There were people all around us, I couldn't just..."
        #Kyou wasn't acting like he did know that, only that it'd be "bad" if Sayori realized something was up with people calling her the wrong name while in her altered state
        n side frown "What did you say to her, Kyou?" with dissolve
        n furious "What did you say to your \"school project\"?" with dissolve
        "It's not like I didn't have my reasons, Nozomi..."
        # s neutral_right "But even so, once you noticed my altered behaviour had persisted into my school life, surely you must have realized the urgency of the situation." with dissolve
        ks confused "I-I didn't know what to do, okay? She seemed happy to go along with it, and I wanted that for her. I thought she wanted to be happy for a while."
        ks "And even if she didn't, what do you think would've happened if I woke her up in the middle of class? Don't you think she would've freaked out in front of all those people?"
        ks "So... yeah, maybe I wussed out. And yeah, maybe I should've brought Sayori back to herself, but I really thought it'd be better to just play along until she was out of there."
        "But nothing I say will change how you feel about me, will it?"
        n irritated "Unbelievable..." with dissolve
        show Sayori casual concerned
        ks frown "C-come on, can you blame me, Nozomi? I just wanted to keep her safe through all of this!" with dissolve
        show Sayori concerned_right
        n frown "Don't give me that crap. Like you were ever thinking about her safety before this all blew up in your face." with dissolve
        n irritated "Sure, I doubt Sayori would've taken it well if you brought her out of it in front of our classmates. But you only chose not to because you didn't want to deal with that." with dissolve
        # n front2 "You just didn't want to deal with Sayori freaking out at you in the middle of class." with dissolve
        n front2 angry "This was only ever about YOUR comfort! About YOUR safety!" with dissolve
        ks confused "Nozomi, I..."
        n determined "You weren't thinking about her at all!" with dissolve
        "And what does Sayori feel about this? As I look to her for answers, all I can see is that same forlorn expression in her eyes."
        "It's unsettling to see her this withdrawn. To see someone like her allow anyone else to speak in her place."
        # "She's not going to say anything?"
        n side irritated "Rrrrgh... I don't know how the hell an incompetent like you managed to worm your way into Sayori's mind like this, but it ends today." with dissolve
        n furious "I mean, CLEARLY you can't handle the responsibility that comes with being a hypnotist. So here's what's going to happen." with dissolve
        show Sayori concerned
        n frown_side "Sayori, I'm going to get you some professional help, okay? We'll see a real hypnotherapist; try and heal the damage he did to you." with dissolve #By "we" she means herself and her mum, not Kyou
        s casual_handup "H-hmm?" with dissolve
        n front2 frown "And as for you, I think we'll all breathe a little easier if you never hypnotize anyone again!" with dissolve
        show Sayori casual_handup
        ks "What?!"
        n irritated "As far as I'm concerned you're done here. We don't need your reckless brand of hypnosis making things worse for my friend." with dissolve
        # n determined "You obviously can't handle the responsibility of having someone's mind in your hands, so as far as I'm concerned you're done here." with dissolve
        n determined "Now get out of my house!" with dissolve
        "I can feel the hairs stand at the back of my neck as I hear her declaration ringing in my ears."
        s surprised "Nozomi... no!" with dissolve
        "And I had unconsciously taken a step towards the door before Sayori breaks her silence with a sudden urgency."
        n side frown_side "\"No\"? What do you mean \"no\"?" with dissolve
        s neutral "I am sorry, but do you have any idea what could happen if I involved a mental health professional in this rubbish?" with dissolve
        n neutral_side "Sayori, you need help. And I mean REAL help!" with dissolve
        n frown "You can't trust this charlatan with your mind again; you have to know that." with dissolve
        s casual_folded concerned "Be that as it may, were I to take that help I would almost certainly doom my career aspirations to failure before I even graduate." with dissolve
        show Nozomi neutral_side
        s sleeptalk "All the sacrifices I have made, every hour I spent poring over textbooks in the service of passing my entrance exams... it could all come to nothing." with dissolve
        s sleeptalk_concerned "The mere mention of \"multiple personalities\" on my personal record would surely condemn me in the eyes of every hospital in the country, should it ever come to light." with dissolve
        show Nozomi sad_side
        s sleepy "Kyou, I am afraid to say, is my best hope of an expedient and... risk-mitigating resolution." with dissolve
        n sad_closed "Oh, Sayori... Is there really no way I can talk you out of this?" with dissolve
        s neutral "He is well attuned to my hypnotic suggestibility. And I have little reason to doubt his ability to reverse the damage he has wrought upon my mind." with dissolve
        s casual_handup concerned_right "That is... if you truly mean to \"do right by me\"?" with dissolve
        show Nozomi sad_side
        "Sayori... I can still see the terror in those eyes of hers as she looks to me once again." with dissolve
        show Nozomi frown
        "For a whole day I forced her to live out a version of herself that she never wanted to show the world. All because I wanted to keep hypnotizing her no matter how she felt." with dissolve
        s casual sleepy "Please, Kyou... You have to help me." with dissolve
        "I hurt her, and I truly am sorry for that."
        ks sad "Of course..."
        stop music fadeout 5.0
        scene bg blackscreen with longdissolve
        "I'll do anything to win back her trust..."
        pause 2.0
        $ending = "shaken"
        jump Epilogue_Con_Kyou_Sayori
    s casual_folded sleeptalk "But at the same time, I can accept that you truly meant me no harm. That your recklessness was borne of academic curiosity and ego as opposed to outright malice." with dissolve
    s smile_right "So... I accept your apology. And I hope we can work ourselves to a resolution." with dissolve
    queue music Piano_Mood
    "I feel a little wave of relief wash over me as I smile at her."
    ks smile "Yeah. Me too, Sayori."
    show Nozomi neutral_left
    s casual_handup smile "So with all that said, perhaps it is time we got down to business?" with dissolve
    n frown "Not until he gets on his hands and knees!" with dissolve
    ks sigh "Oh, come on!"
    s casual happy"Mhmhmhmhmh~" with dissolve
    "And man, if she's laughing again I know things are going to be alright."
    s smirk "I think we can overlook that little indiscrection, Nozomi. You can stand down now." with dissolve
    n pout "Hmpth, if you say so. But I'm not letting him off the hook just yet." with dissolve
    show Nozomi side sad_side
    show Sayori casual_handup smile
    "Just then, Sayori smiles as she places a hand gently on Nozomi's shoulder." with dissolve
    s "Thank you. I appreciate everything you are doing for me."
    n neutral_side "Hm? O-Oh, it's nothing. Really." with dissolve
    s neutral "You can hardly call organizing this little get-together in your own home nothing. Not to mention your perspective on my predicament has been invaluable." with dissolve
    s sleep "I was at a complete loss, but with your help I am actually beginning to feel optimistic about reaching a satisfactory conclusion to this mess." with dissolve
    s smile "So thank you. Truly." with dissolve
    "Yeah... I can really feel the tension start to diffuse from the room."
    n happy blush "Aw... honestly, I'm really glad you came to me. It's nice being able to do something for you for a change." with dissolve
    "Everything's going to be fine. I KNOW I can fix this."
    n smile_side "So... a-anyway, let's talk about why we're here, okay?" with dissolve
    stop music fadeout 5.0
    s smile_right "Yes. Let's." with dissolve
    show Sayori casual neutral_right
    show Nozomi neutral noblush
    queue music Downtown
    "They then turn to me, and I can see in their expressions that it's finally time for us all to talk about this like adults." with dissolve
    n front2 neutral "Alright, so Sayori filled me in about what's been happening to her, and it definitely sounds like she's in the upper category of extremely hypnotizeable people." with dissolve
    n surprised "But even so, it's pretty wild that you managed to effect her so completely with just two short hypnosis sessions!" with dissolve
    n sigh "I don't think I'd have believed it if it was anyone other than Sayori telling me that." with dissolve
    "Still, there's something that bothers me about what they're saying."
    show Nozomi neutral_left
    s casual_folded sleep "And I would have shared your skepticism. But there is no doubt in my mind that Kyou's hypnosis has had an effect on me beyond what should be possible." with dissolve
    "Because I look at Sayori now, and... yeah."
    s neutral_right "It appears more consistent with being subject to many extended sessions of deep hypnotic conditioning from a highly-trained hypnotist, with my full knowledge and consent." with dissolve
    "Something doesn't add up."
    s concerned_right "And as such, I am certain I have no ability to resist it." with dissolve
    ks confused "Are you really so sure you can't resist those hypnotic suggestions, Sayori?"
    show Nozomi neutral
    s neutral_right "Why? Do you have any reason to doubt me?" with dissolve
    ks "Well I mean..."
    "I gesture to Sayori's face, as sunken as it is."
    ks "Sure looks to me like you haven't been sleeping right."
    ks "You're both focused on the personality switch, but if you're not sleeping again then doesn't that mean you've been ignoring the first suggestion I made to you?"
    show Sayori sleep
    "To that, Sayori simply shakes her head." with dissolve
    s neutral_right "I am afraid not. The contradiction you cite is trivially explained." with dissolve
    show Nozomi neutral_left
    s casual "The hypnotic complusion you placed to empty my mind and fall asleep was predicated on the assumption that I would choose to go to bed." with dissolve
    s concerned_right "But since I awoke in our classroom the other day I remained awake deep into the night while I attempted to research my condition." with dissolve
    s sleeptalk "Turning in for the night was the last thing on my mind." with dissolve
    n side sad_closed "Oh gosh, please don't tell me you haven't slept in two days, Sayori." with dissolve
    s casual_handup concerned "I will not. Eventually even I had to admit defeat." with dissolve
    show Nozomi sad_side
    s concerned_right "And when I finally settled into bed, my eyes immediately fell closed and all the worries of the night vanished without trace." with dissolve
    s sleeptalk_concerned "Were it not for the fact I had set an alarm to wake me in time for school the next morning I would have surely suffered a repeat of my earlier truancy." with dissolve
    s concerned_right "So you see, Kyou, your hypnotic suggestions are both working exactly as you instructed." with dissolve
    s casual_folded sleep "If any of us were hoping my adverse reaction to your mental meddling would put a stop to these compulsions it is sadly misplaced." with dissolve
    ks neutral "I... I see."
    "Well, I guess I can't be surprised that Sayori found an extremely... Sayori way of shooting down my theory."
    s neutral "I get the impression that the two of you are still not fully comprehending the effects upon my mind, even if you do believe me." with dissolve
    n neutral_side "Yeah, it's... it's a little hard to wrap my head around to be honest." with dissolve
    "Sayori nods slowly... then starts to look at me with purpose."
    s frown_right "... I believe a demonstration is in order." with dissolve
    show Nozomi surprised_side
    ks confused "Huh?" with dissolve
    s neutral "Yes. I think we all need to see exactly what we are dealing with here." with dissolve
    n sad_side "You don't mean..." with dissolve
    s casual neutral_right "Kyou, I am giving you permission to invoke whatever method you used to switch my personality to that... other being." with dissolve
    show Nozomi sad
    s casual_handup concerned_right "What was the phrase you used, out of curiosity? Can you specify without explicitly saying it?" with dissolve
    "I nod at her."
    ks neutral "Yeah. I say \"Become\" and then the name I used for your other personality."
    s casual sleep "Understood. And this is precisely what I have been afraid of until now." with dissolve
    show Nozomi sad_side
    s concerned_right "Just the very idea that you could transform my entire sense of self with two spoken words and a moment's whimsy would surely terrify anyone in my position." with dissolve
    show Sayori sleeptalk_concerned
    "Sayori lets out a weary sigh as she anxiously presses her hands together." with dissolve
    s "But I digress. In a moment, I shall ask you to invoke that spoken phrase upon me."
    s concerned_right "I shall attempt to resist, but I expect it to be a futile gesture. I will almost certainly experience a mental shift no different than before." with dissolve
    s casual_handup sleeptalk "So assuming you succeed, I want you both to talk to this other personality of mine. Find out what she knows and what she does not." with dissolve
    s neutral_right "My own memories of this time as my alter self remain completely vacant. You specified it as such, I presume?" with dissolve
    show Nozomi neutral
    ks "Yeah... Yeah, I did." with dissolve
    s "And presumably the reverse is true."
    "I nod once more."
    s sleep "Alright. So I want you to verify that for me in your interactions with her." with dissolve
    show Nozomi neutral_side
    s neutral_right "Once you have confirmed the facts I expect you to return me to my original state so that we may discuss this further." with dissolve
    s sleeptalk "Perhaps then we will be able to fashion a solution that does not leave me bereft of my autonomy going forward." with dissolve
    n frown_side "Right..." with dissolve
    "Nozomi nods at her friend with determination. And perhaps no small amount of anticipation."
    show Nozomi neutral
    s casual frown_right "Alright, Kyou... Proceed." with dissolve
    "I mean, even if she hasn't said anything about it she's got to be curious to see this happen first-hand, right?"
    ks neutral "Alright... become [alt_name]."
    stop music fadeout 5.0
    show Nozomi neutral_side
    s surprised_right "Hn... a-aahhh..." with dissolve
    if alt_name == "Risa": #Nozomi and Kyou with have a little bonus interaction here if Kyou named Sayori's alt after another named character
        $alt_namecheck = True
        n surprised "Risa? As in, Hiroko's friend?" with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "Huh? What do you mean?"
        n sad_closed "Oh, it's nothing. It was probably just a coincidence." with dissolve
    elif alt_name == "Akiko":
        $alt_namecheck = True
        n surprised "Akiko? Don't tell me you named her after the student council president by accident?" with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "Huh? Oh, yeah, I guess that's her name too isn't it?"
        n irritated "Honestly..." with dissolve
    elif alt_name == "Rie":
        $alt_namecheck = True
        n frown "Rie? Why on earth did you call her Rie?" with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "Huh? Oh, yeah, there's a girl from our class called that, huh?"
        n irritated "Honestly..." with dissolve
    elif alt_name == "Shiro":
        $alt_namecheck = True
        n furious "What?! You called her SHIRO?" with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "Huh? Oh, yeah, there's a guy from our class called that, huh?"
        n rolleyes "Yes, that and the fact it's a BOY's name!" with dissolve
        "Yeah... I have to admit I have no idea what was running through my head when I decided to call her that."
        n irritated "I can't even deal with you right now..." with dissolve
    elif alt_name == "Jessica" and preferences.language == None:
        $alt_namecheck = True
        n surprised "Jessica? Like that exchange student from class 2-B?" with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "What?"
        n frown "You... honestly don't know her? How did you come up with a name like that, then?" with dissolve
    #The name of the foreign exchange student was changed in the translation, so the name Nozomi reacts to is different depending on the language used. Neat, huh?
    elif alt_name == "Maria" and preferences.language == "spanish" or alt_name == "María" and preferences.language == "spanish":
        $alt_namecheck = True
        n surprised "María? Like that exchange student from class 2-B?" with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "What?"
        n frown "You... honestly don't know her? How did you come up with a name like that, then?" with dissolve
    elif alt_name == "Daisuke":
        $alt_namecheck = True
        n furious "What?! You called her DAISUKE?" with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "Huh? What's wrong with that?"
        n irritated "That's a BOY's name, Kyou!" with dissolve
        ks "N-not... always?"
    elif alt_name == "Sachiko":
        $alt_namecheck = True
        n neutral "Huh. That's weird." with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "What is?"
        n neutral_side "There's someone from my literature club called Sachiko." with dissolve
        n sad_closed "I'm sure it's just a coincidence..." with dissolve
    elif alt_name == "Chiba":
        $alt_namecheck = True
        n surprised "Chiba? You named her Chiba?" with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "Yes?"
        n frown "Why on earth did you name her after our English Lit teacher?" with dissolve
        ks "Oh... right."
        n irritated "You're so weird..." with dissolve
    elif alt_name == "Atsuko":
        $alt_namecheck = True
        n surprised "You... what?!" with dissolve
        "Why is she... oh."
        n front2 shocked "You gave her my MOM's name?!" with dissolve
        "Oh fuck. Is that a freaky coincidence or what."
        ks sigh "L-look, I dunno, Nozomi. I've never even met your mom before today."
        ks "It's just a weird coincidence, okay? Don't worry about it."
        n irritated "I'm trying not to... God." with dissolve
    elif alt_name == "Ichiro":
        $alt_namecheck = True
        n front2 shocked "Y-you... what did you just say?" with dissolve
        ks "Uhh... Ichiro?"
        n determined "Okay, for one, that's totally a boy's name and two, how is it that you gave her my BROTHER's name?!" with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "Wait, seriously? I didn't even know you HAD a brother."
        n irritated "I... I don't even know what to think right now." with dissolve
    elif alt_name == "Yoshio":
        $alt_namecheck = True
        n front2 shocked "Y-you... what did you just say?" with dissolve
        ks "Uhh... Yoshio?"
        n determined "Okay, for one, that's totally a boy's name and two, how is it that you gave her my DAD's name?!" with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "Wait, seriously?"
        n irritated "I... I don't even know what to think right now." with dissolve
    elif alt_name == "Iroyas":
        $alt_namecheck = True
        n surprised "... Iroyas? What kind of name is that?" with dissolve
        "Rather than focus on Sayori I find myself looking to Nozomi with a grin."
        ks smirk "Think about it for a second."
        n "{cps=5}... {/cps}{w=1.0}{nw}"
        $ renpy.transition(dissolve, layer="master")
        extend rolleyes "Oh. Right. I guess you thought that was clever."
        ks frown "It IS clever!"
    elif alt_name == "Satoshi":
        $alt_namecheck = True
        n frown "... Satoshi? Seriously?" with dissolve
        "Rather than focus on Sayori I find myself blinking at Nozomi in confusion."
        ks confused "What?"
        n irritated "One, that's a boy's name and two, that's the name of the upperclassman who hypnotized me last year. The one I was just telling you about." with dissolve
        n furious "Just... WHY?" with dissolve
        "Yeah... I have to admit I have no idea what was running through my head when I decided to call her that."
        n irritated "I can't even deal with you right now..." with dissolve
    else:
        $alt_namecheck = False
        "Nozomi and I observe Sayori curiously as her eyelids appear to flicker rapidly, before focus returns to her eyes and she fixes her gaze on me."
    if alt_namecheck == True:
        show Nozomi side sad_side
        s "... Kyou?" with dissolve
        "A voice suddenly snaps us both back to the sight of a somewhat bewildered-looking Sayori."
    else:
        show Nozomi side sad_side
        s "... Kyou?" with dissolve
    ks confused "Hey... How are you feeling?"
    s "{cps=5}I... {/cps}{w=1.0}{nw}"
    show Nozomi surprised_side
    $ renpy.transition(dissolve, layer="master")
    extend laugh "Ahahahaha~"
    "That laughter..."
    $sayori_name = alt_name
    queue music Sad_Heroine
    s giggle "I am a little confused, Kyou~" with dissolve
    "That's her alright."
    s smile "{cps=20}I mean, one moment we are talking in class and... {/cps}{w=1.0}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend surprised "now this?"
    "All I had to do was speak the words and that happy, carefree personality I called \"[alt_name]\" came right back in a flash."
    n sad_side "U-uh... yes?" with dissolve
    "Just like Sayori said it would."
    s casual_folded laugh "Now we have been whisked away to Nozomi's room! Hello, my friend~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    n "... Hi?"
    s smile "Well, I suppose it doesn't matter. Anything to be out of that stuffy old classroom~" with dissolve
    n smile_side "Eheh... r-right." with dissolve
    "Nozomi looks to her friend with a wary smile. Seems she's still trying to wrap her head around the idea of Sayori being able to switch personalities in an instant."
    n "B-but anyway Sayori, you really don't remember how you got here?"
    s casual_handup concerned "Oh really now, Nozomi. Why is it that you keep calling me that?" with dissolve
    n sad_closed "A-ahh, [alt_name]. Sorry, I meant [alt_name] of course!" with dissolve
    s neutral_right "I can only presume that you know of the game Kyou and I were playing yesterday." with dissolve
    "[alt_name] looks to me for confirmation, and I feel I have no choice but to hesitantly nod and play along here."
    ks confused "That's... right. Nozomi knows all about the hypnosis we did."
    show Nozomi neutral_side
    show Sayori happy
    "And to that, [alt_name] offers a hearty giggle." with dissolve
    s "I see. This is all starting to make sense."
    n sad_side "Er, it is?" with dissolve
    s smirk "Why, yes. Kyou must have bragged to you about hypnotizing me and you, in your hypnosis-loving giddiness, invited him to your house for a first-hand demonstration." with dissolve
    n surprised_side blush "\"H-hypnosis-loving giddiness\"? What on earth do you mean?" with dissolve
    s laugh "Ahahaha, there is no need to be so coy around us, Nozomi." with dissolve
    s smile "The fact you have a deep affection for hypnosis has been an open secret ever since that time Satoshi hypnotized you at the culture festival!" with dissolve
    s casual_folded smirk_right "Why, even Kyou picked up on that. Didn't you, Kyou?" with dissolve
    show Nozomi sad
    ks sigh blush "Uuuhhh..." with dissolve
    "Is it just me, or is the atmosphere in here getting more awkward by the second?"
    show Nozomi sad_side
    s smirk "Or what, did you honestly think he simply learned hypnosis on a whim? You know he still has the hots for you, right?" with dissolve
    "More... awkward... by the second..."
    n irritated "O-okay, but... moving past that..." with dissolve
    "I'm only lucky that me and Nozomi have more important things to worry about right now."
    show Sayori smile
    n neutral_side noblush "You really don't remember how you got here, [alt_name]?" with dissolve
    s casual_handup concerned "No. Perhaps that should bother me more than it does." with dissolve
    "Because yeah, she doesn't seem to remember anything."
    s sleeptalk_concerned "And... aawwwwwnn... why is it that I am suddenly so very sleepy?" with dissolve
    "Even without her confirming it, she's saying plenty to convince us that she doesn't know anything about what's happened since I told her to become Sayori again."
    s sleepy "It feels as though I have been pulling one of those tedious all-nighters I used to do." with dissolve
    "It's just like the first time I had her switch personalities. She's still somehow able to keep two sets of memories completely separate in her head, sealed off from one another."
    s casual_handup concerned_right "{cps=15}It leads me to wonder... {/cps}{w=1.0}{nw}" with dissolve
    show Nozomi surprised_side
    extend panicked_right "AHH! Could that be it?" with vpunch
    ks confused noblush "Could... what be it?"
    s rolleyes "Well, given how many things seem to be slipping my mind lately, I have to wonder if this is another of your hypnotic tricks." with dissolve
    s smile_right "So did you perchance happen to induce some kind of amnesiac state upon me?" with dissolve
    ks confused "What?"
    show Nozomi sad_side
    s surprised_right "How positively scandalous! And you didn't even seek my permission before doing such a thing!" with dissolve
    s casual_folded rolleyes "... Unless I forgot? Did I forget that too?" with dissolve
    n rolleyes "I mean, I guess we can't rule it out. Kyou seems pretty careless when it comes to hypnosis." with dissolve
    ks sigh "Hey, come on!"
    show Nozomi neutral_side
    s laugh "Ahahahaha, isn't he? But let us not be too harsh on him. He is still learning his craft." with dissolve
    s giggle "Just the fact that he is already so adept at inducing unique states upon the mind after having had nothing but second-hand knowledge to guide him is simply incredible!" with dissolve
    s happy "Isn't he amazing, Nozomi?" with dissolve
    n frown "Oh, he's something all right." with dissolve
    "I can feel Nozomi getting more and more irritated by the second."
    n irritated "So Kyou, I think it's time you... well, you know." with dissolve
    stop music fadeout 5.0
    "I nod my head grimly. We've seen enough; Sayori proved what she set out to prove."
    s casual_handup concerned "What? What does he know?" with dissolve
    "{cps=15}So I'll just say-{/cps}{w=1.0}{nw}"
    show Sayori surprised_right
    show Nozomi surprised_side
    nm "I want to know that too!" with dissolve
    ks surprised "W-what the?!"
    n "Mom?"
    hide Sayori
    show Sayori casual_handup neutral at center:
        xpos 0.25
    "We all find ourselves turning to the door as we hear a chuckle from the other side." with dissolve
    nm "Ahahaha, I'm sorry. I wasn't eavesdropping, I promise."
    play sound dooropen
    show Nozomi:
        linear 1.0 xpos 0.6
    show Sayori:
        linear 1.0 xpos 0.4
    pause 1.0
    show Atsuko smile_side at center, flip:
        xpos 0.2
    show Nozomi:
        xpos 0.6
    show Sayori:
        xpos 0.4
    play music Piano_Mood
    "And with that, the door swings open and Nozomi's mother invites herself inside, and..." with dissolve
    s laugh "Oh my goodness, Atsuko it has been positively ages since I've seen you! How have you been?" with dissolve
    "... And dammit, I can't just say \"Become Sayori\" out loud with her here, can I?"
    nm surprised_side "Uh... not much change from forty minutes ago, I suppose?" with dissolve
    show Sayori smile
    n sad_closed "Ugh, don't mind her. She's... in an odd mood." with dissolve
    n frown_side "But oh my god, mom were you listening in on us?" with dissolve
    "Maybe I could slip it into the conversation naturally somehow. Just gotta do it in a way that won't have Atsuko suspect anything..."
    nm neutral_side "Ah... Actually, it's just that I heard shouting a few minutes ago." with dissolve
    n neutral_side "Shouting? {w=1.0}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend sad_closed "Oh, right. That."
    show Nozomi neutral_side
    nm smile "I was going to leave you all to it; you're all adults after all." with dissolve
    nm happy "But I was just getting lunch ready and I thought well, you know, you all must be a little stressed from all these exams you have coming up." with dissolve
    nm laugh "So why don't I make you all something nice and then you can get back to it?" with dissolve
    ks confused "{cps=20}You're making us lunch? But- {/cps}{w=1.0}{nw}"
    s casual_folded laugh "Oh my, that does sound delightful~ Just the very mention of exams again is making me eager to chow down on something!" with dissolve
    show Nozomi sad
    "This could be bad. And as Nozomi catches my gaze and tilts her head towards Sayori I realize she wants me to just say it and deal with the consequences later." with dissolve
    nm smile_side "Well come on, then. There's sushi downstairs for everyone~" with dissolve
    "But I..."
    s casual_handup happy "Then what are we waiting for? To the kitchen!" with dissolve
    hide Sayori
    hide Atsuko
    stop music fadeout 5.0
    "... I just can't get the words out of my mouth before Sayori/[alt_name] is out the door, chatting inanely with Nozomi's mom on the way." with dissolve
    n frown "{size=16}Why didn't you do it?{/size}" with dissolve
    "Nozomi hisses quietly at me as I look to her with a sigh before whispering back."
    ks sigh "{size=16}I wanted to, but it's awkward in front of your mom isn't it?{/size}"
    n rolleyes "{size=16}Well it's going to be more awkward watching your [alt_name] chatting away at the lunch table!{/size}" with dissolve
    show Nozomi front2 sigh
    "Wrapping her arms around her stomach, Nozomi breathes through her nose as she shakes her head ruefully." with dissolve
    n "{size=16}God, what a mess. I told mom not to disturb us, but I guess she just couldn't help herself.{/size}"
    n concerned "{size=16}... Sayori's going to be so upset with us when she comes to.{/size}" with dissolve
    ks sad "{size=16}Yeah...{/size}"
    "As if she needed another reason to freak out. What's she going to think if she comes to in the middle of all this?"
    "But then, the thought occurs to me..."
    ks neutral "{size=16}... Maybe she doesn't have to find out?{/size}"
    n surprised "Eh?" with dissolve
    ks "{size=16}Yeah. It's just lunch with your mom. We can get through that, right? [alt_name] might say something weird but it shouldn't be too embarrassing. What's the worst that could happen?{/size}"
    show Nozomi frown
    ks "{size=16}And when it's over we'll bring her back here, I'll change her back and it'll be like nothing happened. She'll be fine.{/size}" with dissolve
    n determined "{size=16}Oh, really, Kyou? How is that fair to Sayori? She didn't ask to be humiliated like this!{/size}" with dissolve
    ks "{size=16}And how humiliated do you think Sayori will be when we bring her out in the middle of lunch? Is she gonna freak out in front of your mom while she's disoriented?{/size}"
    ks "{size=16}I bet Atsuko will have something to say about that. She'll probably have all sorts of questions about what's really going on in here. Is that what any of us want?{/size}"
    n irritated "{size=16}Ugh, I... I...{/size}" with dissolve
    nm "{size=16}Nozomi? Kyou? Are you coming down?{/size}"
    show Nozomi side sad_side
    "Nozomi stares pensively at the open door of her room as her mom's voice floats inside." with dissolve
    "We really need to get down there."
    ks sigh "{size=16}I don't like this any more than you do but it'll be over soon, I promise.{/size}"
    n neutral_side "{size=16}Yeah... Let's get this over with.{/size}" with dissolve
    scene bg blackscreen with dissolve
    "So we take ourselves downstairs as we hear Atsuko chatting happily away to \"Sayori\"."
    scene bg n kitchen day
    show Atsuko smile_side at center, flip:
        xpos 0.25
    show Sayori casual_handup laugh at center
    with dissolve
    play music Inspiration
    s "Oh wow, Atsuko, this all looks so good~ {font=DejaVuSans.ttf}♥{/font}"
    "They seem to be getting on at least..."
    nm happy "Oh it's not much, really. Just something I whipped up this morning when Nozomi told us we'd be having guests." with dissolve
    show Nozomi side casual sad_closed at center:
        xpos 0.75
    show Sayori smile
    n "Oh, so you planned this from the very start, huh, mom?" with dissolve
    nm smile_side "Well now, what kind of mother would I be if I didn't show hospitality to your friends?" with dissolve
    show Sayori smile
    show Nozomi neutral_side
    "I notice Nozomi casting a wary look to the happy friend in question..." with dissolve
    nm "Not to mention it IS time for lunch. Honestly, I'm not sure what you were expecting, dear."
    scene SayoriAlterLunch sayori1 sushi1 a_happy k_neutral s_laugh n_neutral with blink
    "Oblivious to Nozomi's attention, and seemingly excited by the spread of sushi before her, [alt_name] claps her hands delightedly as she's the first to be seated at the dining table."
    s casual happy "And I for one thank you for such, Atsuko. It looks positively scrumptious~"
    show SayoriAlterLunch n_smile
    n smile_side "U-um... yes, it really does, mom. Thanks for the food." with dissolve
    show SayoriAlterLunch k_embarrassed s_smile
    k "Y-yeah. Thanks for the food, Atsuko." with dissolve
    show SayoriAlterLunch a_smile_left
    nm happy "It's my pleasure! Don't be shy now, tuck in~" with dissolve
    show SayoriAlterLunch sayori2 sushi2 nosticks s_laugh
    "[alt_name] needs no second invitation, and she gleefully starts loading her plate." with dissolve
    "If nothing else, the time she spends stuffing her face is time she won't be spending embarrassing us with whatever carefree thoughts she's sure to be having right now."
    show SayoriAlterLunch k_neutral n_irritated a_neutral_left s_smile
    "So I allow myself a moment to relax as I take a piece of the tasty-looking fish and place it on my tongue." with dissolve
    "Gotta admit, it really is good sushi. Not that it seems to cheer Nozomi any, who may as well be eating lemons with the face she's making from across the table."
    show SayoriAlterLunch a_concerned_left
    nm surprised_side "Something wrong, dear?" with dissolve
    show SayoriAlterLunch n_surprised
    n sad_side "Mmmh? Oh, no it's nothing. I was just thinking about... t-things?" with dissolve
    show SayoriAlterLunch a_smile_left s_neutral
    nm smile_side "Exam things? How are you all getting along with that, anyway? Anything I can help with?" with dissolve
    show SayoriAlterLunch n_smile
    "Nozomi, perhaps not even realizing the face she was making in front of her mom, musters a smile as she shakes her head." with dissolve
    n "Oh... you know, we're doing okay actually. We're just brushing up on some things we should already know. Calculus, national history, stuff like that."
    show SayoriAlterLunch s_rolleyes n_neutral
    s rolleyes "Uuuurrrgh..." with dissolve
    show SayoriAlterLunch a_neutral_right
    "Just then Sayori... no, [alt_name], throws her head back with a melodramatic groan." with dissolve
    show SayoriAlterLunch a_concerned_right
    nm surprised_side "Whatever is the matter? Is the food disagreeing with you?" with dissolve
    "[alt_name] crosses her arms as she pouts openly."
    show SayoriAlterLunch a_neutral_right s_pout
    s casual_folded pout_closed "This conversation is disagreeing with me. It is currently the weekend, and I wish to hear no more talk of exams than I am mandated to." with dissolve
    show SayoriAlterLunch s_pout_closed
    s pout "Weekends should be for recupurating from the labours of the working week and nothing more." with dissolve
    show SayoriAlterLunch n_sigh
    n sad_side "{cps=15}Uhh... N-not to disagree or anything, but-{/cps}{w=1.0}{nw}" with dissolve
    show SayoriAlterLunch s_grin
    s giggle "Ohh Nozomi, you know what we should talk about instead?" with dissolve
    show SayoriAlterLunch n_neutral
    "I can tell Nozomi's reluctant to engage [alt_name] in conversation, but she also knows she doesn't have a choice if she wants to pretend everything's normal around here." with dissolve
    n neutral_side "Um... what should we talk about?"
    show SayoriAlterLunch sayori1 chopsticks s_laugh
    "[alt_name] claps her hands together once again as she shifts excitedly in her seat." with dissolve
    s "Why, all those board games of yours! We don't talk about them enough, and you so obviously have a deep affection for them."
    show SayoriAlterLunch n_surprised
    n surprised_side "You want to ask about..." with dissolve
    "Not that I can say right now, but I've been curious about that too. I knew she hosted board game nights and everything but man, her room was full of those things."
    show SayoriAlterLunch s_smile n_smile
    "And the subject clearly brings a smile to Nozomi's face in spite of the situation." with dissolve
    n "W-well, there's not much to say about them, I guess? You kinda need to play these games to really get them."
    "Honestly didn't expect the beautiful girl I've coveted for so long to have a geeky side."
    show SayoriAlterLunch s_laugh
    s casual_handup giggle "Then let's play! I would love to see what the fuss is about~" with dissolve
    show SayoriAlterLunch s_smile
    s smile_right "So why don't you pick a game for us after lunch?" with dissolve
    "[alt_name] smiles innocently, and I can almost feel Nozomi's reluctance as she's forced to remember this isn't really Sayori she's talking to right now."
    n sad_closed noblush "Ahh, you know I'd love to b-but..."
    "... Wait a minute. I'm just realizing we can use this to our advantage."
    show SayoriAlterLunch sayori2 nosticks s_rolleyes n_neutral
    s rolleyes "But what? We have other responsibilities? Once again, this is the weekend." with dissolve
    "If [alt_name]'s excited about playing games with us then maybe she won't feel the need to run her mouth off and say something weird in front of Atsuko."
    show SayoriAlterLunch s_neutral
    s happy "What kinds of people would we be if we shirked our responsibilities to ourselves?" with dissolve
    "All we have to do is make it through lunch like this and we'll lead her straight back to Nozomi's room no problem!"
    show SayoriAlterLunch n_sigh
    n sad_side "{cps=15}Ah, S-... I mean, well, that's really not-{/cps}{w=1.0}{nw}" with dissolve
    show SayoriAlterLunch k_smile
    k "I think we should do it. Just a quick game or something to take our mind off things for a bit." with dissolve
    show SayoriAlterLunch a_neutral_left s_surprised n_surprised
    n shocked "Kyou?!" with dissolve
    show SayoriAlterLunch sayori1 chopsticks s_laugh
    "Beaming at my show of support, [alt_name] claps her hands in glee as she no doubt feels she's going to have her way." with dissolve
    show SayoriAlterLunch a_neutral_right
    s "Yes! I knew you'd see it my way, you wonderful man!" with dissolve
    show SayoriAlterLunch a_smile_right s_happy n_neutral
    nm smile_side "Hmm. Well, maybe a little mental break would do you some good if you feel you need it, dear." with dissolve
    show SayoriAlterLunch a_happy
    nm happy "And who knows, maybe after you're done with exams I'll see you both again next time Nozomi's hosting one of her board game nights~" with dissolve
    show SayoriAlterLunch n_sigh
    n sad_closed "Oh, mom..." with dissolve
    show SayoriAlterLunch s_grin
    s giggle "Board game night? Why not a board game DAY! We should go all out~" with dissolve
    nm "{cps=15}Mmm... {/cps}{w=1.0}{nw}"
    show SayoriAlterLunch a_laugh k_neutral n_neutral
    $ renpy.transition(dissolve, layer="master")
    extend laugh "ahahahahahaha!"
    n "Mom? What's so..."
    nm "Oh my, hahaha. I never knew you could get like this!"
    show SayoriAlterLunch sayori1 chopsticks s_happy a_smile_right
    nm smile_side "I guess you must be feeling confident about your chances if you're this cocky, hm, Sayori?" with dissolve
    show SayoriAlterLunch s_concerned n_surprised k_confused
    n surprised_side "A-aaahh, no..." with dissolve
    "Me and Nozomi both winced that time. I guess it couldn't be helped that Atsuko would invoke Sayori's real name eventually."
    show SayoriAlterLunch sayori2 nosticks n_neutral
    s concerned "\"Sayori\"? Don't tell me you are in on this as well..." with dissolve
    "Just gotta push past it."
    show SayoriAlterLunch k_smile
    k "N-never mind that, let's finish lunch and find something to play, alright?" with dissolve
    s concerned_right "{cps=15}I... {/cps}{w=1.0}{nw}" with dissolve
    show SayoriAlterLunch a_surprised s_surprised n_surprised k_confused
    play music ringtone
    extend "O-oh!" with vpunch
    "Just then some kind of obnoxious music starts to reverberate around the room, cutting everyone's thoughts short."
    k "... What the hell is that?"
    show SayoriAlterLunch sayori1 chopsticks a_neutral_right s_laugh n_neutral
    s casual_handup laugh "Ahahaha... it's my phone. I really do apologize." with dissolve
    "Right, it's a ringtone. Although I wonder why it's got to be that loud..."
    show SayoriAlterLunch n_sigh
    n sad "She has it like that because she kept missing her calls before." with dissolve
    "Nozomi tells me by way of explanation without me asking. Guess this comes up a lot."
    stop music
    show SayoriAlterLunch s_smile
    s happy "Sorry everyone, I need to take this. It's from daddy..." with dissolve
    scene bg blackscreen with dissolve
    play music Downtown
    $persistent.sayori_alter_lunch_unlock = True
    s "{size=16}... Hello?{/size}" with dissolve
    scene bg n kitchen day
    show Atsuko smile_side at center, flip:
        xpos 0.25
    show Nozomi side casual sad at center
    with dissolve
    "[alt_name] hurries outside to talk to her dad, leaving the rest of us to awkwardly pick at what's left of the food..."
    nm happy "{size=16}... She calls her father \"daddy\"? That's adorable.{/size}" with dissolve
    n happy "Mhmhmh... y-yeah, she does that sometimes." with dissolve
    nm smile_side "Well, I'm glad she seems to be doing well." with dissolve
    show Atsuko smile
    show Nozomi smile_side
    "She smiles fondly, before I notice her gaze start to wander over to me sitting beside her..." with dissolve
    nm "So Kyou, I'm curious..."
    show Nozomi neutral
    ks casual neutral "Um... yes?" with dissolve
    nm "Have you known these two for long?"
    ks confused "Uh... w-well, yeah sorta. We've been in the same class since we started senior high."
    show Nozomi sad_side
    nm happy "Oh, really? And why am I just hearing about you, hm?" with dissolve
    "Oh man, this is really uncomfortable to talk about."
    "What do I even say to her? That these girls kept shutting me down until I got them involved in my hypnosis? I don't think that'll go down well."
    show Atsuko smile
    ks smile "I mean, we didn't really talk much... I guess? Until these mock exams came up." with dissolve
    show Atsuko smile_side
    n smile_side "Th-that's... right! Kyou's a classmate and we just thought it'd be better if we pooled our resources on this one, that's all." with dissolve
    nm happy "Ahh, so this is just an impromptu study group? Fascinating~" with dissolve
    "It's not really that fascinating, though."
    show Nozomi neutral
    nm smile "But maybe we'll see more of you from now on, huh, Kyou?" with dissolve
    ks confused "Uh... w-well..."
    show Nozomi rolleyes
    "I glance nervously in Nozomi's direction and catch her momentarily rolling her eyes, so somehow I doubt that, Mrs. Akemi." with dissolve
    show Nozomi neutral
    ks neutral "I mean, sure. Maybe. But I dunno, I don't want to impose or anything." with dissolve
    show Atsuko neutral
    ks "I'm only here because they wanted another study partner. They could've asked anyone, really." with dissolve
    nm smile "Oh come now, Kyou. I don't know what you all talk about in your class but don't sell yourself short like that." with dissolve
    show Nozomi neutral_side
    nm smile_side "I know my Nozomi; she doesn't keep company with just anybody." with dissolve
    n "..."
    nm smile "And I'm sure Sayori is the same way. She doesn't strike me as the sort who'll willingly associate with someone who'd waste her time." with dissolve
    n sad_side "... Yeah, she really isn't." with dissolve
    nm happy "So don't think you'd be imposing on us. A friend of Nozomi's is a friend of mine; you're welcome here anytime, dear." with dissolve
    "I smile at her. She's got to know something's not quite right with me being here, but even so she's been nothing but nice to me since I got here."
    show Atsuko smile
    "She really is a good person." with dissolve
    show Atsuko smile_side
    n smile_side "Well in any case we do need to get a move on, so we'll just finish up here and we can get back to our studying." with dissolve
    n neutral_side "Or... playing games. What's taking her so long anyway?" with dissolve
    nm happy "Oh, leave her be. I'm sure her father's just talking her ear off." with dissolve
    nm laugh "Or maybe the other way around? She does seem very chatty today~" with dissolve
    n sad "Uh... right." with dissolve
    "I get another look from Nozomi to make me uncomfortable. But honestly I'm not too worried about Sayori talking to her dad as \"[alt_name]\"."
    "She spent the other night with her family like that and nothing happened, so what's one phone call? Although..."
    "Although it kind of puts my plan to keep this latest incident from Sayori in doubt if she's saying anything she's supposed to remember later..."
    show Atsuko smile_side
    n sad_side "I'm just going to go check on her." with dissolve
    ks sigh "Y-yeah. Good idea."
    hide Nozomi with dissolve
    nm surprised_side "Check on her? Whatever for?" with dissolve
    "Nozomi leaves us with uncomfortable speed, leaving a puzzled-looking Atsuko in her wake."
    show Atsuko smile
    "Although she quickly shrugs it off as she turns back to me with a smile." with dissolve
    nm smile "Oh well, more sushi for us, eh?"
    ks smile "Ehehe... y-yeah."
    "I'm not really that hungry, but it's hard not to take another piece at her kindly prompting..."
    show Atsuko neutral_side
    show Nozomi side casual shocked_side at center:
        xpos 0.8
    stop music
    n "She LEFT?!" with dissolve
    "I look up from the table to find Nozomi with her jaw hanging open. I'm about to do the same before I remember just in time that I'm holding a mouthful of raw fish."
    play music Rain
    nm surprised_side "{cps=15}What do you-{/cps}{w=1.5}{nw}" with dissolve
    ks confused "Mpth, w-what do you mean she left?"
    n shocked "I-I mean she's GONE! I didn't see her in the other room and when I went to check by the door her shoes weren't there!" with dissolve
    n sad_closed "So she must... m-must've..." with dissolve
    nm neutral_side "Well, she can't have left without a good reason. Maybe her father called with some kind of emergency?" with dissolve
    nm neutral "I hope it's nothing too serious." with dissolve
    show Nozomi sad
    "Ugh. I want to tell Atsuko it's not as serious as that, but even so it's pretty fucking serious." with dissolve
    "We never should've let Sayori out of our sight in her altered state. And there's no way we can keep this whole mess a secret now."
    "I'm so fucking screwed."
    n frown "Kyou, come on we need to go find her!" with dissolve
    ks frown "Y-yeah, of course."
    nm neutral_side "{cps=15}Nozomi, what are you saying? Why do you have to-{/cps}{w=1.0}{nw}" with dissolve
    n sad_side "Mom, t-there's no time. Come on, Kyou!" with dissolve
    scene bg n room day with blink
    "I mutter an apology to Atsuko as I rush to follow Nozomi outside while my mind races."
    show Nozomi side casual irritated at center, flip
    n "Pick up... pick up..." with dissolve
    "Nozomi has her phone pressed to her ear as I dash to the front door."
    ks casual confused "What could've gotten into her, though? Why'd she bail on us like this?"
    scene bg n house day
    show Nozomi casual side sad_side at center, flip
    with blink
    "We hurry to step outside the house and I look to the streets..."
    n "She's not answering. Why isn't she answering?"
    "But it's far too late. Sayori's nowhere to be seen."
    hide Nozomi
    show Nozomi front2 casual concerned at center
    n front2 concerned "This is bad. If she's not answering me then something has to be seriously wrong." with dissolve
    "Meanwhile I turn back to Nozomi, who is really not taking this well at all."
    n sleeptalk_concerned "Sayori's going to kill us when she comes to, oh my god..." with dissolve
    "As bad as this is, I gotta calm her down some."
    show Nozomi concerned
    ks casual confused "Look, she can't have gotten far. And... yeah, it's bad she's gone but I'm sure she's not gonna get herself in trouble or anything." with dissolve
    ks "Even if she thinks she's this other person, she's still Sayori. And Sayori would never..."
    n frown "Never what? You don't know!" with dissolve
    n side frown_side "She's out here somewhere, thinking she's carefree and fun-chasing, like that's the only thing that matters anymore!" with dissolve
    n frown "If she can't get a hold of herself then there's no telling what she could be doing! She's completely unpredictable like this!" with dissolve
    n sad_side "Not to mention... oh god, Kyou." with dissolve
    ks "What?"
    "Hanging up her phone in defeat, Nozomi hugs it around her chest as her face seems to get even paler."
    n sad "Kyou, what if she knows she's the flipped personality? I mean, she has to suspect something doesn't add up, right?" with dissolve
    "Right. Everyone in the world knows her as Sayori. Nozomi and her mom and... to say nothing of..."
    n front2 surprised "What if her dad called her by her real name and she couldn't ignore it anymore?" with dissolve
    "Even as carefree as she's meant to be as \"[alt_name]\"?"
    ks neutral "W-well..."
    n shocked "It'd make sense that she'd run away from us then, wouldn't it?" with dissolve
    "I shake my head at her. Really don't want to think of the possibilities there."
    stop music fadeout 5.0
    ks confused "Let's not jump to any conclusions, okay?"
    n determined "Well we have to do SOMETHING! The longer she's out here the worse it's going to be for Sayori when she realizes what happened." with dissolve
    ks sigh "Ugh, I KNOW, alright! Just... s-settle down and let me think..."
    show Nozomi sigh
    queue music Monologue
    "Honestly, all this time we're spending bickering is just letting [alt_name] get further away. There's no way we'll be able to find her just wandering around the streets aimlessly." with dissolve
    "She could be anywhere by now..."
    n side sad_side "She could be so confused. And scared, like there's no one she can trust anymore..." with dissolve
    "We need some kind of lead, just... any idea at all."
    ks neutral "So if she was going to run off someplace, it'd be to somewhere she thinks she can escape from everything. Go back to thinking happy thoughts."
    n sad "Y... yeah, I suppose that would make sense." with dissolve
    "Is she really as unpredictable as Nozomi thinks?"
    ks confused "Where does Sayori go to let off steam anyway?"
    n neutral "Oh. Well, she..." with dissolve
    n front2 sleep "U-umm..." with dissolve
    n neutral_left "I-I guess she... likes to..." with dissolve
    ks "Wait a minute, YOU don't know?"
    n angry "Ugh, s-she doesn't really talk about it, Kyou!" with dissolve
    "I guess she doesn't if my talks with her were anything to go by..."
    n concerned "Sayori... she was always so focused on her work, or on other people." with dissolve
    n side sad_side "She loved hearing about what we got up to, but every time I tried inviting her for karaoke or games she'd just say she doesn't have the time." with dissolve
    n sad "I wonder if she was afraid of having anything to distract her from her studies. She's always been so driven about that." with dissolve
    ks sigh "Come on, there's gotta be something we're missing. Sayori can't be that dull."
    n rolleyes "Of course she isn't! She just has her priorities at this stage of our lives." with dissolve
    ks confused "Well... what about when she was a kid? Was she always like this?"
    "Nozomi shrugs."
    n neutral_side "I have no idea. It's not like I knew her before high school." with dissolve
    ks "So do you know anyone who does? Can you ask them?"
    n irritated "Ugh, no we're wasting so much time just standing here, and I don't know anyone she could've run her mouth off to except..." with dissolve
    n sad "Uh, well..." with dissolve
    ks confused "Well, what?"
    show Nozomi side sad_side at flip
    stop music fadeout 5.0
    "Nozomi looks across the street, running a hand anxiously through her hair as she contemplates something." with dissolve
    hide Nozomi
    show Nozomi casual front2 frown
    "Then with a worried frown she turns back to me." with dissolve
    n "It's worth a shot. Come on, she's not far..."
    scene bg court day
    show Nozomi side casual sad_side at center, flip:
        xpos 0.25
    show Hiroko tennis surprised_side at center
    with longblink
    play music Eons
    h "\"Where does Sayori go to have fun\"?"
    h tennis_headhold2 confused_side "You seriously came out here to ask me that?" with dissolve
    "Really, Nozomi? Talking to Hiroko was your best idea? I thought you knew more people than this."
    n sad_closed "I mean, I was calling you on the way here? You weren't answering your phone." with dissolve
    h rolleyes "Like, duh? Kinda busy prepping for this super important tourney I got goin' on tomorrow, you remember that?" with dissolve
    n sad_side "Y-yeah, I'm really sorry. I didn't want to bother you on today of all days, but..." with dissolve
    h tennis frown "'Sides, I can think of a better question..." with dissolve
    "Hiroko's eyes inevitably fix on me as I try to ignore her."
    h tennis_armup irritated vein "This 'cuz of your \"class project\", dude? You roped Nozo into it too, somehow?" with dissolve
    "I would've stayed away, but Nozomi insisted I stick around where she could see me."
    show Hiroko neutral_side novein
    n frown_side "I'll explain later. But Hiroko, I..." with dissolve
    h tennis_headhold2 sleeptalk "Yeah, yeah, this shit is important for some reason. I hear ya." with dissolve
    h nervous_side "But why do you think I know anything about Sayori that you don't?" with dissolve
    n neutral_side "I mean, you knew her before I did. You're the one who introduced us, after all." with dissolve
    n sad_side "So I just thought she might have said something to you? Something about the kind of person she was before senior high?" with dissolve
    h sleep "Hrrmm..." with dissolve
    n sad_closed "Just... really, anything would be helpful. Anything at all." with dissolve
    h tennis_armup irritated "{cps=15}Jesus, {/cps}{nw}" with dissolve
    extend "FINE! Lemme think for a sec." with vpunch
    show Nozomi sad_side
    show Hiroko tennis frown_side
    "Hiroko taps her foot impatiently while she thinks to herself, and both Nozomi and I take half a step back." with dissolve
    "She seems even crankier than usual for us interrupting her in the middle of tennis practice. So much that it seems even Nozomi's nervous about bothering her."
    h confused_side "... Y'know, there WAS something she told me." with dissolve
    n surprised_side "Really?" with dissolve
    h rolleyes "Yeah, first time we were together. We got paired in our first gym class to do stretches an' man, that girl had this total \"can't be fucked\" attitude about her." with dissolve
    show Nozomi neutral_side
    h frown_side "Kinda rubbed me up the wrong way. Figured she thought she was too good for any of us." with dissolve
    h neutral_side "But soon as we started talking I realized it weren't that at all." with dissolve
    h sad "Girl was just super down on herself." with dissolve
    h smile_side "Anywho, we shot the shit until the teach called us up for volleyball. An' you know what I think about volleyball." with dissolve
    n rolleyes "Volleyball's not so bad." with dissolve
    h frown_side "S'okay to be wrong sometimes. But yeah, I tell her how I wish we were doing tennis or gymnastics instead." with dissolve
    show Nozomi neutral_side
    h surprised_side "And that's when she kinda mumbled \"I wish I was back in the arcade\"." with dissolve
    n sad_side "The... videogame arcade? Like the one in the mall?" with dissolve
    h tennis_headhold2 confused_side "I guess? It's the only one in town anyway." with dissolve
    h sleeptalk "'Snot like I asked her about it; I don't think she even knew I heard her." with dissolve
    h neutral "But yeah, if you want my opinion I'm gonna go out on a limb and say she used to be some kinda gamer chick before she turned into miss bookworm." with dissolve
    show Nozomi surprised
    "Nozomi and I raise an eyebrow at each other as we share a glance." with dissolve
    "Did this little snot actually say something halfway helpful? I don't believe it."
    show Hiroko surprised_side
    n laugh "Eeeee! Hiroko I could hug you right now!" with dissolve
    h smile_side blush "R-really? Ehehe I mean, I ain't gonna stop ya." with dissolve
    n smile_side "Okay listen, we need to get going but thank you SO much! We'll get out of your hair now." with dissolve
    n happy "{cps=15}I'll see you tomorrow! {w=0.5}Best of luck at the-{/cps}{w=1.0}{nw}" with dissolve
    h tennis_armup surprised_side noblush "Whoa whoa, hold on a sec!" with dissolve
    n sad_side "Huh? No, Hiroko, we don't want to keep you. Plus I think Risa's getting restless waiting for you over there." with dissolve
    "I look over Hiroko's shoulder, and sure enough I see some other tennis-uniformed girl in a ponytail walking back and forth on the court away from us swinging her racket aimlessly."
    "She looks kind of familiar. But I'm not going to think much of it."
    h tennis_headhold2 nervous_side "It's just... look, you two're obviously planning some shit an' it's got something to do with Sayori." with dissolve
    h sad "Poor girl's been in a really bad way; she's all over the place." with dissolve
    h sleeptalk "Kinda takes me back to that gym class if you know what I mean." with dissolve
    h nervous_side"But like... h'yeah, hit me up after the game tomorrow, alright? I want in on whatever you guys've got cooking up for her." with dissolve
    show Nozomi sad
    "Nozomi and I share glances once more." with dissolve
    "It's not like we can tell her anything, and I could give a shit about Hiroko personally, but it's clear Sayori's been on her mind since before we got here."
    show Nozomi sad_side
    "We'll have to tell her something eventually, now that Nozomi's gotten her involved in this." with dissolve
    n neutral_side "R-right, so don't worry about Sayori. She wouldn't want that for you." with dissolve
    n smile_side "Just stay focused on the tournament and I'll fill you in later, I promise." with dissolve
    hide Hiroko
    show Nozomi sad_closed
    stop music fadeout 5.0
    "Hiroko nods quietly before turning away from us to rejoin her tennis partner, and Nozomi breathes a quiet sigh." with dissolve
    n "This is all getting messier by the minute."
    ks casual sad "Yeah..."
    n frown "Now let's get out of here. We have somewhere to be." with dissolve
    scene bg blackscreen with longdissolve
    "So we leave a confused Hiroko in our wake as we head together to..."
    scene bg shopping mall day
    show Nozomi front2 casual sigh
    with longdissolve
    play music Downtown
    ks casual sigh "The mall. I don't know if we're going to find her here, Nozomi." with dissolve
    "I mean, we're going off a thing that Hiroko might have heard about two and a half years ago."
    "Sure this is all we've got to go on but this feels crazy. Like the longest of long shots."
    n frown "She'll be here. She has to be here." with dissolve
    "I can only nod as I start to look around this place."
    ks neutral "So where's the arcade anyway?"
    n side neutral_side "Hmm... you know, I don't think I've ever seen it." with dissolve
    n neutral "You mean to tell me you've never been? You seem like the type to play a lot of videogames." with dissolve
    ks confused "I..."
    "I mean, she's not wrong but I don't like the dismissive tone in her voice when she said that."
    ks frown "A-at home! I play at home!"
    show Nozomi frown_side
    "Nozomi just sighs through her nose as she joins me in looking around." with dissolve
    n "Well, it's not in the main area so it has to be... this way."
    scene bg blackscreen with dissolve
    "Nozomi starts pacing towards the rear end of the mall and I follow her lead..."
    scene bg arcade with longdissolve
    "... And sure enough, after a little walk we find an old videogame arcade tucked away at the very back of the mall."
    show Nozomi side casual neutral_side at center
    n "Now I remember why I don't come this way. Most of the stores here have closed down." with dissolve
    ks casual confused "Yeah. Not sure what's keeping this place open to be honest."
    n sad_side "Yeah..." with dissolve
    "We're looking around by the entrance as we're greeted by a ton of flashing lights and loud machinery with all kinds of games on offer. But way too few people for a Saturday afternoon."
    "None of whom are Sayori, we're quick to realize."
    n sad "Come on. She might be further in..." with dissolve
    scene bg blackscreen with dissolve
    stop music fadeout 5.0
    "I nod as we begin our forlorn exploration of the near-deserted arcade, walking past a row of UFO catchers to find a group of old fighting game cabinets."
    "If she's not back here, then..."
    s "Ahahahahaha!"
    scene SayoriArcade2 s_giggle
    with dissolve
    queue music Black_Room
    "Nozomi and I stand for a moment in stunned silence as a young man walks past us, looking despondent."
    s "Oh, you are done? I was hoping to go another round with you!"
    "Because at the cabinet he just walked away from, standing there larger than life is..."
    show SayoriArcade2 nozomi n_shocked with dissolve
    show SayoriArcade2 s_panic
    n "SAYORI!" with vpunch
    show SayoriArcade2 s_embarrassed
    s "Haaaah?" with dissolve
    "Our flighty friend seems to freeze in place for a moment as Nozomi calls out to her."
    scene bg arcade
    show Nozomi side casual shocked_side at center
    show Sayori casual_folded surprised_right at center:
        xpos 0.25
    with blink
    ks casual surprised "Uhh, [alt_name]! She meant [alt_name]!"
    show Nozomi frown
    "Nozomi gives me a hard nudge for correcting her... no, that's not it." with dissolve
    "She must want me to stop this split-personality nonsense once and for all before our would-be escapee runs off again."
    show Sayori casual_handup happy at flip
    show Nozomi neutral_side
    s "N-Nozomi! Kyou! What an unexpected delight it is to see you here~" with dissolve
    "But I don't know, now that the initial surprise has worn off she doesn't seem to be in a mood to run."
    s smile_right "And here of all places! I could not think of a better location to spend the weekend~" with dissolve
    "Far from it, she seems amused that we somehow managed to find her."
    ks smile "Uh... y-yeah, this place is great."
    n frown_side "Just wonderful. Anyway, we came to find you because Kyou has something very important he wants to say to you." with dissolve
    n front2 frown "Right, Kyou?" with dissolve
    "Maybe I'm tempting fate here, but..."
    ks neutral "Oh. Yeah, about that..."
    s giggle "Well, don't be shy, Kyou! You can say anything to me~" with dissolve
    "... but this seems like a good chance to find out what the hell happened to make her bolt from Nozomi's house."
    ks sad "Man, it's just that I'm so bummed out that you left without playing that board game with us."
    n irritated "{cps=15}Right... {w=0.5}{/cps}{nw}" with dissolve
    extend shocked "wait, that's not it!" with vpunch
    s casual_folded sleeptalk_concerned "Ah... yes, I do apologize for leaving you both in the manner I did." with dissolve
    show Nozomi neutral_left
    s concerned "But please understand, my daddy is putting a lot of pressure on me to cram all the knowledge I can fit in my head for the entrance exams we have coming up." with dissolve
    s casual_handup sleeptalk "He knew I was visiting you this morning, Nozomi, and he had some concerns over my recent behaviour." with dissolve
    s rolleyes "So he was calling to remind me of my responsibilities. He wanted to make sure I knew to attend cram school this afternoon instead of living it up with all of you." with dissolve
    s neutral "He was putting a great deal of stress upon me, and I feared a confrontation over the phone was only going to make it worse." with dissolve
    show Nozomi side sad_side
    "Nozomi, now obviously as curious as I am, turns back to her friend with a worried expression." with dissolve
    n "So what did you tell him?"
    s happy "Mhmhm~ I simply told him I would be a good little daughter and attend cram school posthaste." with dissolve
    n shocked_side "You WHAT?!" with dissolve
    s laugh "Ahahaha, I know. But it was enough to placate him, and that was good enough for me~" with dissolve #so after that I simply put my phone on silent and snuck out."# so I could have some much-needed me time~" with dissolve
    ks sigh "Oh man, that's..."
    n sad_closed "Oh my god, Sayo- I mean, [alt_name], whatever your name is, what on earth were you thinking?" with dissolve
    s happy "Hmm, I suppose I wasn't thinking at all~" with dissolve
    ks confused "You couldn't even tell us what you were doing?"
    show Nozomi neutral_side
    s concerned_right "Oh no, absolutely not. Why would I make you accessories in my deception? Or allow you to convince me that this was a bad idea?" with dissolve
    s smile "It was much better for all concerned if I put my phone on silent and snuck away so I could focus on getting some much-needed me time." with dissolve
    n furious_side "That's so STUPID! And... and selfish! Do you have any idea how much trouble you've made for everyone?" with dissolve
    s sleeptalk "Oh come now Nozomi, this needn't concern any of you. It was my decision to make." with dissolve
    s smile "It is my decision to live in the moment. You only live once, as they say." with dissolve
    s laugh "And the consequences? Well, they are future [alt_name]'s problem~" with dissolve
    n front2 angry "Rrrrrgh!" with dissolve
    "With an experated howl, Nozomi wheels round to face me with an expression that makes me think she's ready to murder everyone in this arcade."
    n determined "You change her back right this instant Kyou or I swear to god I'll make your life a living hell, do you hear me?" with dissolve
    ks sigh "Ugh, yeah I hear you loud and clear. Besides, I think we've heard everything we needed to."
    s giggle "Heehee, \"change me back\"? My goodness, what do you mean by that?" with dissolve
    ks neutral "[alt_name]... you need to become Sayori again."
    show Nozomi side frown_side
    stop music fadeout 5.0
    s casual surprised_right "I need to... huh?" with dissolve
    "The pair of us watch cautiously as \"[alt_name]\" seems to space out, her eyes looking to refocus in a manner that makes her look absolutely befuddled."
    n "Please tell me you're back to normal, [alt_name]."
    s surprised "I... \"[alt_name]\"?" with dissolve
    n irritated "Ugh, I mean..." with dissolve
    $sayori_name = "Sayori"
    s casual_handup "Nozomi? What..." with dissolve
    show Nozomi sad_side
    s panicked "Haaah, wh-what, where am I? This is..." with dissolve
    queue music Monologue
    show Nozomi:
        linear 1.0 xpos 0.35
    pause 1.0
    show Nozomi sad_closed:
        xpos 0.35
    "We can both see the panic in her eyes now, and Nozomi throws her arms around her in a frantic bid to calm her friend." with dissolve
    n "S-Sayori no, it's okay! Please don't freak out!"
    s casual sleepy "But... what am I doing here? I don't..." with dissolve
    n sad_side "We messed up and I'm sorry, but you're safe now." with dissolve
    ks sigh "We'll explain everything..."
    scene bg blackscreen with longdissolve
    "Sayori didn't make too much of a scene this time, thanks to Nozomi reassuring her."
    "Either that or she's starting to get used to waking up like this..."
    "Anyway, Nozomi and I started to explain everything that happened since the moment I triggered her in Nozomi's room."
    scene bg arcade
    show Sayori casual frown at center, flip:
        xpos 0.25
    show Nozomi side casual sad_side at center
    stop music fadeout 5.0
    with longdissolve
    "She starts to frown at us as she continues to listen. A frown that only seems to deepen the more we tell her."
    "Man, I still can't imagine how much of a headscrew this has got to be for her."
    queue music Eons
    n "... And er, that's when Kyou said \"become Sayori\" to finally bring you back."
    s "..."
    n sad_closed "Ahhh... p-please stop looking at us like that."  with dissolve
    s casual_folded irritated "..." with dissolve
    n front sigh "I... l-look, I told Kyou to change you back right after we confirmed what you wanted. He's the reason things got out of hand like this." with dissolve
    "Ugh, really Nozomi? You're trying to pin this all on me so you don't look bad in front of Sayori? I thought you were better than that."
    ks casual sigh "Hey, I was going to until your mom walked in. I was trying not to make a scene!"
    n front2 frown "Yes, great job, Kyou. Sayori led us on a wild goose chase thanks to you, how's that for not making a scene?" with dissolve
    ks frown "I don't know, Nozomi, maybe if you hadn't yelled at me your mom wouldn't have come to check on us in the first place."
    n determined "Ooh, don't you turn it around on me. We're only in this mess because you were too much of a coward to just say the thing." with dissolve
    ks angry "I was thinking about Sayori the whole time! But what about you? You wanted her to have a freakout in front of your mom? You think that would've been good for her?"
    n angry "Bullcrap! You were the one who said we could keep this whole thing a secret from Sayori the minute things turned sour! You weren't thinking about her well-being at all!" with dissolve
    s frown_right "Enough." with dissolve
    show Nozomi neutral_left
    "Oh. Right, I guess I got a little carried away in the moment. But one word from Sayori is enough to silence us both." with dissolve
    s casual irritated "Now... I am still trying to process all of this, and I admit that I am feeling a certain amount of resentment towards the pair of you at this moment." with dissolve
    s sleeptalk "But perhaps I share some responsibility in thinking we could run a controlled experiment such as this without consequence." with dissolve
    n side sad_side "Sayori..." with dissolve
    s casual_handup concerned_right "I see no value in pointing fingers. What's done is done. And besides, as humiliating as this experience has been, we..." with dissolve
    s concerned "Well, we have proven everything I set out to prove with this little exercise, have we not?" with dissolve
    "I can only nod glumly in agreement."
    ks sad "Yeah. From the second I told you to swap personalities you really couldn't help yourself. It was just like before."
    show Sayori concerned_right
    show Nozomi sad
    ks "A person acting out a hypnotic suggestion should always be able to break out of it if they really didn't want to do it. If it was causing them pain in some way." with dissolve
    ks "But it's like a switch flips in your brain and suddenly you really are like two different people with your own priorities and even your own separate memories."
    n sad_side "It doesn't matter if you're extremely hypnotizeable, there's no way this should be happening to you, Sayori. I really don't understand it at all." with dissolve
    n sad_closed "It's like something out of a thriller novel, but there's no denying what happened. I can hardly imagine how scary this all is for you." with dissolve
    "Sayori sighs wearily as she runs a hand through her hair."
    s casual sleeptalk "Indeed. Now I believe you truly understand the situation I am faced with, and why it needs to stop today." with dissolve
    s sleep "I am exhausted mentally. Physically. My head feels as if it is being pulled in two entirely different directions and I am just barely holding everything together." with dissolve
    s sleeptalk_concerned "I... I cannot continue to live like this." with dissolve
    n sad_side "Yeah..." with dissolve
    show Sayori concerned_right
    "The three of us just stand there for a moment, sharing awkward looks amidst the bright lights and frivolous sounds from all around us." with dissolve
    "It's like this whole arcade is trying to drive our gloom out of here, and it can hardly be doing Sayori's state of mind much good."
    "I mean, there could hardly be a less appropriate place for this kind of situation."
    n smile_side "Hey, Sayori? Let's head home." with dissolve
    s concerned "Hm?" with dissolve
    n happy "Yeah. Let's get you away from all of this and we'll figure out how to get you back to normal together, okay?" with dissolve
    s casual_folded "Well. Actually..." with dissolve
    show Nozomi neutral_side
    "Just then, Sayori turns herself towards the fighting game cabinet that \"[alt_name]\" was playing on when we found her." with dissolve
    s neutral "It is just that I am starting to find this environment comforting. Nostalgic, even." with dissolve
    n surprised_side "Huh?" with dissolve
    "Her hand wanders over the surface of the cabinet, rubbing her fingers across the buttons as she gazes at its screen."
    s "So I was wondering..."
    s concerned_right "... Do either of you play?" with dissolve
    scene bg blackscreen with longdissolve
    pause 2.0
    scene SayoriArcade2 s_smile nozomi n_neutral kyou k_mad
    with longdissolve
    k "Oh, come on!"
    "I smack the control stick in frustration as the fighting game cabinet shouts \"K.O.\" at me, as if to mock me personally."
    show SayoriArcade2 s_smirk
    s smirk_right "Heh. I was under the impression that you were good at this sort of game, Kyou? Was I mistaken?" with dissolve
    "After that last round I'm feeling a little of what that other guy must have felt playing \"[alt_name]\" when we found her."
    show SayoriArcade2 k_frown_right
    k "Yeah well, I'm out of practice and I don't play this series so whatever." with dissolve
    show SayoriArcade2 s_smile
    "Sayori simply chuckles as she taps her finger against the coin slot of the machine." with dissolve
    s "It is always excuse after excuse with your sort. Again."
    "With a grumble, I fish in my pocket for another token as I feed it into the slot, and immediately the game invites me to go another round with this impossibly-skilled woman."
    k "Is there anything you're not good at? I mean, besides sleeping?"
    show SayoriArcade2 s_rolleyes
    s rolleyes "Just pick a character, Kyou. Anyway, like I was saying..." with dissolve
    "Hmm. Maybe I should pick a more straight-up brawler as my fighter this time. I certainly can't match Sayori for speed if that's how she plays..."
    show SayoriArcade2 s_neutral k_frown
    s neutral "So we have established beyond a shadow of a doubt that I am completely helpless to resist these post-hypnotic suggestions you have placed upon me." with dissolve
    "And she can still carry a conversation at the same time as kicking my ass?!"
    s "They are powerful enough to compel me to compartmentalize my memories and even now, prevent me from recalling my experience living as... \"[alt_name]\", was it?"
    "Come on, I just need to focus. Parry her initial attack and then..."
    s "Kyou? Try to stay focused."
    show SayoriArcade2 k_growl
    k "I-I'm trying!" with dissolve
    show SayoriArcade2 n_sigh
    n rolleyes "She means on the conversation, you dingus." with dissolve
    play sound punch
    "Goddammit, she just floored my fighter again."
    if alt_name == "Risa" or alt_name == "Akiko" or alt_name == "Rie" or alt_name == "Shiro" or alt_name == "Jessica" or alt_name == "Daisuke":
        show SayoriArcade2 n_neutral
        n sad_side "But yes, \"[alt_name]\" is what he called her." with dissolve
        show SayoriArcade2 s_rolleyes
        s frown "Interesting choice of name, by the way." with dissolve
        show SayoriArcade2 n_pout
        n rolleyes "I know, right?" with dissolve
        show SayoriArcade2 s_neutral n_concerned
        n sad_side "But more importantly, you really don't recall anything about that phone call?" with dissolve
    elif  alt_name == "Atsuko" or alt_name == "Ichiro"  or alt_name == "Yoshio" or alt_name == "Iroyas" or alt_name == "Satoshi" :
        show SayoriArcade2 n_neutral
        n sad_side "But yes, \"[alt_name]\" is what he called her." with dissolve
        show SayoriArcade2 s_rolleyes
        s frown "Interesting choice of name, by the way." with dissolve
        show SayoriArcade2 n_pout
        n rolleyes "I know, right?" with dissolve
        show SayoriArcade2 s_neutral n_concerned
        n sad_side "But more importantly, you really don't recall anything about that phone call?" with dissolve
    else:
        show SayoriArcade2 s_neutral n_concerned
        n sad_side "But yes, \"[alt_name]\" is what he called her. And you really don't recall anything about that phone call?" with dissolve
    show SayoriArcade2 s_concerned k_frown
    s neutral "Ah, that's right. You did mention my father calling me. Do you know what that was about?" with dissolve
    "Alright, fine, I'll just roll him backward, away from Sayori's sweep kick, then I can..."
    show SayoriArcade2 s_smirk
    s rolleyes "Oh, that move again? How predictable." with dissolve
    play sound punch
    show SayoriArcade2 k_mad
    k "Fuck!" with vpunch
    show SayoriArcade2 n_neutral k_growl
    n neutral_side "Well... your other self lied to him about going to cram school so she could goof off in this very arcade." with dissolve
    "That does it. Time to get serious!"
    show SayoriArcade2 s_panic
    s scared "I... s-she did WHAT?" with dissolve
    "There, as her voice quavers I notice she just relaxed at the controls."
    show SayoriArcade2 s_anxious
    s sleeptalk_concerned "Oh god. I do not relish the conversation I will need to have with my father when I get home..." with dissolve
    "Now's my chance!"
    show SayoriArcade2 k_frown
    k "Pffth, don't you mean your \"daddy\"?" with dissolve
    show SayoriArcade2 s_panic
    play sound punch
    "With a quarter-roll of the stick and a few taps of these buttons I get my guy to land a solid strike on Sayori's fighter. Now to keep this combo going..." with dissolve
    show SayoriArcade2 s_angry
    s  angry_right "Now is not the time to test me, Kyou!" with dissolve
    play sound punch
    show SayoriArcade2 k_mad
    k "Shit! How the hell did you counter that?!" with vpunch
    "I can only watch helplessly as Sayori's hands spring back into action."
    "In an instant she deftly blocks my attack before countering with precise strikes until my guy's laid out flat on the arena floor once again."
    show SayoriArcade2 k_sigh
    k "Aaand she's won again." with dissolve
    show SayoriArcade2 s_happy n_smile k_frown
    s happy "Mhmhmh~ There is something cathartic about causing you so much virtual pain." with dissolve
    k "Yeah, yeah. At least someone's enjoying themselves."
    show SayoriArcade2 s_beaming
    s smile_right "Oh, I very much am." with dissolve
    show SayoriArcade2 k_frown_right
    "I glance sideways at Sayori smiling as the game announces the start of the next round and our fighters square off against each other once again." with dissolve
    s "Since starting senior high, I resolved to lock all my videogames away and cease my visits to this place in order to focus on my med school studies."
    show SayoriArcade2 s_neutral n_neutral
    s concerned "It was a sacrifice I was determined to make; I could not afford any downtime if I was going to achieve my academic goals, but..." with dissolve
    "She sighs, a wistful expression on her face."
    show SayoriArcade2 s_concerned
    s "... I would be lying if I said I hadn't missed this." with dissolve
    show SayoriArcade2 k_growl
    "Wait, NOW's my chance!" with dissolve
    play sound punch
    show SayoriArcade2 s_panic
    s panicked "E-eeep!" with vpunch
    "While Sayori hesitates, I attack her character with my ultimate move and she reacts too late to stop me."
    show SayoriArcade2 s_angry
    s angry "Y-youu..." with dissolve
    "She tries to recover, but I'm ready to hit her again while she's down. By the time she can right herself she's lost most of her health."
    show SayoriArcade2 k_smirk_right
    "A few seconds more and the round is over. Sure it was cheap, but a win's a win." with dissolve
    k "Sayori? Try to stay focused."
    show SayoriArcade2 s_smirk n_pout
    s smirk_right "Oh, you ARE going to pay for that, you insufferable clod." with dissolve
    show SayoriArcade2 s_frown n_neutral k_frown
    "As she makes that statement the deciding round begins..." with dissolve
    play sound [punch, punch, punch]
    show SayoriArcade2 k_mad n_shocked
    k "Gah!" with vpunch
    show SayoriArcade2 n_awe
    "... and Sayori's character instantly springs to life with a focused, masterful array of hyper-aggressive moves that leave me fruitlessly mashing buttons." with dissolve
    play sound [punch, punch, punch]
    k "Fuck! FUUUUUUUUCK!" with shake
    "My guy flails about helplessly, and within seconds he's lifted up into the air from a ruthless combination of kicks that leaves him looking like some kind of marionette."
    "By the time Sayori allows him to fall back to the ground, the fight is over."
    show SayoriArcade2 s_beaming k_sigh
    k "God... goddammit." with dissolve
    n happy "Wow, I don't know what I just saw but that looked really impressive, Sayori!"
    show SayoriArcade2 s_smirk
    s smirk_right "Aaah... it is pleasing to find that I have not lost my edge." with dissolve
    scene bg arcade
    show Sayori casual_folded smile at center, flip:
        xpos 0.25
    show Nozomi side casual smile_side at center
    with blink
    $persistent.sayori_arcade2_unlock = True
    "As miserable as that was, at least I get to see Sayori looking genuinely happy for once, as she turns to look at me with a smile."
    s smile_right "Thank you, Kyou, for indulging me. I think I needed this." with dissolve
    ks casual smile "Uh, sure. You're welcome."
    s smile "Perhaps my alter ego was onto something by bringing me here." with dissolve
    "Sayori pats the arcade cabinet fondly before turning away to face Nozomi and myself."
    s casual neutral_right "Anyway, for the sake of argument we will assume that I do indeed possess a high level of hypnotic suggestibility." with dissolve
    s sleeptalk "And it is as Nozomi was saying, even under that assumption this kind of complete and immediate mental transformation should be completely out of the question." with dissolve
    n frown_side "That has to go double for an amateur hypnotist working on his first hypnotee." with dissolve
    "Sayori simply nods in agreement."
    # s frown_right "What happened to me should be impossible. So I feel we have no choice but to entertain the impossible." with dissolve
    s concerned "What happened to me should be impossible by our understanding of how hypnosis works." with dissolve
    s frown_right "Therefore, we have little choice but to indulge in some... shall we say, extremely out of the box thinking." with dissolve
    ks confused "Huh? What do you mean?"
    "And to my puzzlement, Sayori folds her arms as she regards me firmly."
    s casual_folded "First, we need to talk more about your penlight." with dissolve
    n neutral_side "Penlight? Oh right, I remember you telling me he used a penlight to hypnotize you." with dissolve
    n neutral "I don't think there's anything unusual about that? Having someone focus on a light is a pretty standard form of hypnotic induction via eye-fixation." with dissolve
    s concerned_right "Well, under normal circumstances, yes, but..." with dissolve
    "Sayori trails off as she looks to me for an explanation."
    ks neutral "Uh, right. I used a normal medical penlight, but I made a few modifications."
    n front2 "Oh? What sort of modifications are we talking about here?" with dissolve
    ks "It's nothing, really. I just took it apart and changed how it emits the light a little, and added a subtle patterning to it."
    ks "I figured it'd help people fixate on the light so they'd find it easier to stay focused while I was talking them into trance."
    show Nozomi neutral_left
    s sleeptalk "Yes. And from my own experience of being under that light I can only conclude that your modifications are having the effect you intended." with dissolve
    s neutral_right "You have mentioned before that I appeared to gasp in awe shortly after exposure. Its effect upon me was immediate and powerful." with dissolve
    s casual_handup irritated "So powerful in fact, that we cannot rule out the possibility that it effected large-scale changes in my brain chemistry." with dissolve
    s frown_right "Changes that have had me acting on suggestions well beyond the bounds of what should be possible via hypnosis." with dissolve
    n side sad_side "Sayori, you're... Are you saying what I think you're saying?" with dissolve
    n sad "Kyou made a mind control device? But that's..." with dissolve
    "Sayori lets out a weary sigh as she gives Nozomi a knowing nod."
    s sleeptalk_concerned "Impossible. It is a ridiculous statement to make in all seriousness. Yet it is exactly the explanation I put forth to you both." with dissolve
    # s sleeptalk_concerned "As I said, in the absence of any rational explanation we must entertain the impossible." with dissolve
    "I mean sure, what happened to her is pretty damn crazy, I'll admit, but..."
    show Sayori neutral_right
    ks confused "You're serious? You think I've been altering your brain chemistry and controlling your mind with..." with dissolve
    show penlight at right with moveinright:
        ypos 0.346
    ks "... with this?"
    "Taking the penlight from my pocket, I hold it up in the air for both to see in all its mundane glory."
    s concerned_right "I do. And if I am correct, then that penlight is both the cause of, and solution to my predicament." with dissolve
    "I'm proud of the modifications I made to it. I was sure it'd help induce a trance state just like I planned, but the very idea it could do what she's saying?"
    hide penlight at right with moveoutright
    ks "Sayori, there's out of the box thinking and there's completely nuts. And this is completely fucking nuts, you know that, right?"
    "I don't believe it. I CAN'T believe it."
    "If there's anything that makes sense here at all it's more like..."
    n sad_closed "I-I'm sorry but Kyou's right. This is insanity." with dissolve
    s concerned "There has been little sanity in what has happened to me. Is it really so far-fetched given what we have witnessed today?" with dissolve
    # s concerned "And you believe anything that has happened to me is sane by any measure?" with dissolve
    n sad_side "I know, I just... gosh, I think we're still coming to terms with how hypnotically suggestible you really are." with dissolve
    n neutral_side "Sayori, you're so sharp-witted, and I know when there's something you want to focus on you'll never let go." with dissolve
    n sad "If Kyou even halfway knows what he's doing with hypnosis, using a light designed to catch your attention?" with dissolve
    n neutral_side "Maybe that's all it takes to unlock the boundless potential of your mind to do virtually anything, just like we've seen." with dissolve
    n neutral_side "Your mind is just that capable of doing all these wild and wonderful and... yes, kinda scary things." with dissolve
    n sad_closed "I don't think it's the penlight that's special, Sayori." with dissolve
    n sad_side "... You are." with dissolve
    "Yeah. That's pretty much what I was going to say."
    s casual_folded sleeptalk_concerned "Ah..." with dissolve
    "But to all that, Sayori just draws out another laboured sigh as her head lowers to the floor."
    s concerned "I... suppose I should feel flattered. But no, I do not believe there is anything special about me, Nozomi." with dissolve
    s sleeptalk "All that you see of me, I have had to work damned hard to attain; I am no genius." with dissolve
    s concerned_right "So... Look, I do not ask that you believe me. Just that you humor me for a while; I believe I am owed that much." with dissolve
    "I let out a little sigh of my own this time. So she's that set on this theory of hers, huh?"
    ks neutral "Alright... so what now?"
    # s "You both know I would not make such an incredible statement lightly, but after everything that has happened to me,
    # "Can I really... control minds? With my penlight?"
    # s concerned_right "And if I am correct, then that penlight is both the cause of, and solution to my predicament." with dissolve
    # "But she really thinks I'm altering her brain chemistry and controlling her mind? With my penlight?"
    # "It's so fucking crazy to even think about, but I have to admit Sayori's starting to convince me."
    s casual "Well, I believe we can all agree your penlight and its unique properties are a likely culprit in facilitating these drastic changes upon me." with dissolve
    s neutral_right "So it stands to reason that in order to reverse those changes, you could simply apply it in the same manner as before." with dissolve
    # s casual "Well, I think we can at least agree that your penlight and its unique properties have been key to effecting these drastic changes upon me." with dissolve
    # s neutral_right "So it would stand to reason that it could be used to reverse those same changes with a similar ease." with dissolve
    # s casual "Well, in any case your penlight and its unique properties have been key to implementing these drastic mental changes.
    # s casual "After all, if one can effect such drastic changes to a person's mind with that device alone, then it should be no trouble at all to use it to reverse those same changes." with dissolve
    n neutral_side "So you're saying Kyou should hypnotize you with that penlight again? Only this time he lifts the suggestion that you have a split personality?" with dissolve
    # "She's saying I could use this thing on her again, or maybe anyone, and I could make them do anything I wanted? Think anything I wanted?"
    # "I could really use this thing on Sayori, maybe anyone, and I could get them to do anything I wanted? Think anything I wanted?"
    s casual_folded sleep "Actually... what I am about to propose is something you could say is... a little reckless, given my opinion on the matter." with dissolve
    n sad_side "Reckless?" with dissolve
    # "That's... no, that's nuts. There's no way I can believe that."
    # "I'm not even sure how I feel about that."
    s concerned "Perhaps \"[alt_name]\" is rubbing off on me more than I thought. Still, I believe it could resolve my predicament while simultaneously proving this ridiculous hypothesis of mine." with dissolve
    # "Sayori's hyper-suggestible, and hypnosis turned her brain to some
    n neutral_side "So what are you thinking?" with dissolve
    show Sayori concerned_right
    "... I'm starting to wonder about that look Sayori's suddenly giving me." with dissolve
    ks confused "What?"
    s casual_handup "Kyou... how would you feel about me using the penlight on you?" with dissolve
    show Nozomi surprised
    ks surprised "WHAT?!" with vpunch
    "And now my head's all over the place. Did I just hear her right?"
    n sad_side "You want to hypnotize Kyou with that penlight of his? After telling us how you think it's a mind control device?" with dissolve
    s concerned "Correct." with dissolve
    "I just... what?"
    ks frown "Seriously? No one in their right mind's going to be able to go into trance after hearing that kind of talk."
    n sad_closed "I have to agree. At least not in this sort of context." with dissolve
    ks confused "Is there a *good* context for this kind of talk?"
    n sad blush "O-oh, um, well..." with dissolve
    n front sigh "L-look, that's not important. I'm agreeing with you, aren't I?" with dissolve
    # n sad "I'm sorry, but I don't think anyone is going to be able to go into trance after hearing that kind of talk. Not like this anyway." with dissolve
    s casual_folded sleep "It is as impossible a proposition as could be." with dissolve
    s neutral_right "You would naturally have a high level of anxiety over falling into hypnosis. To say nothing of the fact that I have no practical experience with the subject." with dissolve
    show Nozomi concerned noblush
    s frown_right "And that is what makes it the perfect way to test my hypothesis." with dissolve
    "If she's that convinced my penlight is somehow this kind of all-powerful mind control device, I guess I can't argue with her there."
    s casual_handup "So how about it, Kyou?" with dissolve
    "Maybe this penlight I've constructed really is that special. But then, why would I ever subject myself to it knowing that?"
    s neutral "Perhaps it is too much to ask of of you, but..." with dissolve
    "And what is Sayori even hoping to get out of this? She really wants to prove her hypothesis that bad?"
    s concerned_right "... Would you consent to such an experiment?" with dissolve
    "Is this her way of getting some kind of revenge for what I've put her through?"
    s "Please, Kyou. Tell me what you are thinking."
    "Not to mention, if this penlight of mine really is all that, how could I seriously consider giving it up to anybody?"
    "So I'll..."
    menu:
        "Agree to let Sayori hypnotize me":
            ks neutral "Alright. Let's do it."
            "For all the doubts I've got in my head, there's at least a couple of things I know for sure."
            n surprised "Huh? You're serious?" with dissolve
            "I was the one who got Sayori in this mess. If I hadn't sent her away that night thinking she was that other person, maybe we could've avoided this whole situation."
            s smile_right "Then I will thank you for granting me this second indulgence. You will not regret this." with dissolve
            "She's been through a lot in these past few days and she's had every reason to doubt me."
            show Nozomi smile
            "But despite everything, she... she really does seem to respect me." with dissolve
            n side happy "Well... a-alright then! So, back to mine then?" with dissolve
            scene bg blackscreen with longdissolve
            "Sayori isn't just some cold, overly-serious study fiend. There's also a genuine warmness to her."
            "And if today has shown me anything, it's that she definitely has a playful side even when she isn't \"[alt_name]\"."
            stop music fadeout 5.0
            "I want to be someone worthy of her respect."
            # "(Not to mention (if she discovered it earlier) Sayori hasn't even held the fact he gave her alter a crush against him.)"
        " (disabled)Find a way out of this":
            pass
    scene bg n house day with longdissolve
    "So at long last, we find ourselves heading back to Nozomi's house."
    queue music Downtown
    show Nozomi side casual sad_side at center
    show Sayori casual neutral at center, flip:
        xpos 0.25
    n "Um, Sayori? We might have a little bit of a problem." with dissolve
    "I'd be lying if I said I wasn't anxious about this whole thing, but I'm not going back on my word now."
    s neutral "Oh? And what is that?" with dissolve
    "I do trust Sayori to know what she's doing, all things considered."
    n irritated "Well thinking back, mom noticed how odd you were being at lunch." with dissolve
    n frown_side "Your \"[alt_name]\" self was laughing all the time, talking about wanting to play games instead of studying... things like that." with dissolve
    s casual_handup sleep "Hmm... understood." with dissolve
    n sad_side "Not to mention she thinks you left because of a family emergency or something..." with dissolve# I don't know what she's going to say when she sees you again." with dissolve
    show Sayori neutral_right
    show Nozomi neutral
    ks casual confused "Do we have to do this at your place, Nozomi? My house isn't that far, and it'll be empty." with dissolve
    n sad "Your place? I don't know..." with dissolve
    show Sayori sleeptalk_concerned
    "Just then, Sayori let out an audible yawn as she puts a hand to her mouth." with dissolve
    s "I... think I would prefer to finish this here and now if it is all the same to you."
    n sad_closed "Gosh, Sayori, I don't know how you're even standing." with dissolve
    s sleeptalk "Mmh. Admittedly I could have done without my alter ego running me ragged. Regardless, I shall persist." with dissolve
    show Nozomi sad_side
    s neutral "Besides, I believe I can manage the... Atsuko situation." with dissolve
    # "As they journey anxiously back to the house, Nozomi mentions to Sayori that her mum noticed how odd she was being."
    # "Not to mention she thinks Sayori left because of a family emergency or something. So they're going to need some kind of explanation." with dissolve
    # "Kyou suggests they go to his house, but Sayori can feel her exhaustion from lack of sleep is seriously catching up to her. She isn't going to walk all the way to Kyou's unless they feel like carrying her." with dissolve
    # "Plus she's anxious to see this through now. And besides, she thinks she can handle the Atsuko situation..." with dissolve
    play sound dooropen
    scene bg n room day with blink
    stop music fadeout 5.0
    "Her decision made, the three of us roll up to the front door of Nozomi's house and see ourselves inside."
    show Nozomi side casual smile_side at center
    show Sayori casual_handup neutral at center:
        xpos 0.75
    n "Mom? We're home!" with dissolve
    show Atsuko neutral_side at center, flip:
        xpos 0.25
    "Atsuko is watching TV when we arrive and she immediately gets up to meet us at the door." with dissolve
    nm "Welcome back, dears. Is everything alright?"
    n sad "U-uh, well..." with dissolve
    "Nozomi and I exchange looks at each other. Yeah, I really don't think coming back here was a good idea at all."
    show Sayori casual laugh
    "But as we look to Sayori..." with dissolve
    queue music Black_Room
    show Nozomi surprised
    s "Ah... hahahaha~" with dissolve
    "With that carefree laugh..."
    show Nozomi sad
    s "Why does everyone have such long faces? The life of the party has returned!" with dissolve
    "That happy, breezy way of speaking..."
    nm surprised_side "What on earth happened? I thought your father called you away?" with dissolve
    s smile "Oh... yes. Well, he was merely calling to remind me of my cram school obligations." with dissolve
    s casual_handup rolleyes "My... boring, extremely not-very fun cram school obligations. Dear me, what an absolute pain in the gluteus maximus that is." with dissolve
    "The total disdain towards anything approaching studying."
    s surprised "And especially on a day like this! Such a nice, sunny Saturday afternoon filled with potential for... delightful, frivolous activity!" with dissolve
    "It can only mean one thing."
    s casual_folded pout "Why, naturally I was somewhat bent out of shape at father throwing cold water on the opportunity." with dissolve
    nm neutral_side "Uh... huh..." with dissolve
    "And that is..."
    s casual_folded pout_closed "So while we were talking I swung open the front door so he could hear and said \"See, father? I am leaving immediately to cram my face with learning.\"" with dissolve
    "... Sayori is really bad at pretending to be \"[alt_name]\"."
    s casual_handup laugh "But... ahahaha, in my rashness to make a point I was almost at the school before I realized I had forgotten to bring my textbooks! How silly of me!" with dissolve
    nm surprised_side "S-so then..." with dissolve
    s giggle "So it seems Nozomi and Kyou gave chase to deliver my books to me!" with dissolve
    "She grins mischievously to the pair of us, knowing for sure what a dumbass lie that was, yet knowing we'll have no choice but to back her up somehow."
    # "She grins mischievously to the pair of us, knowing we have no choice but to go along with this dumbass lie she's apparently concocted on the spot."
    n laugh blush "Ahhh... haha, yes, that's right! We just knew she'd forget something, taking off like that!" with dissolve
    ks casual smile blush "Y-yeah, and I guess she was still on the phone to her dad so it's not like we could call her back or anything."
    nm neutral_side "So then... why did you come back here?" with dissolve
    s casual_handup smirk "Be... cause they had neglected to bring the one book I actually needed." with dissolve
    n smile_side "Oh... y-yeah. How silly of us." with dissolve
    nm "Hmm..."
    s casual_folded laugh "So I had to skip the class after all and my, what a delightfully whimsical day this has been! It is like no one is of a mind to do any boring work today~" with dissolve
    show Nozomi sad
    s casual_handup sleeptalk_concerned "So I... aawwwnnn... I will laze it up with my friends a while longer and catch the next class when it is time." with dissolve
    # s casual_handup sleeptalk_concerned "Nevertheless I... aawwwnnn... m-must see to it." with dissolve
    "Oh man Sayori, don't yawn in front of Nozomi's mom like that..."
    s smile "I just hope that he will not be too upset with me if he discovers my tardiness." with dissolve
    # s concerned "So Atsuko, if you will excuse us?" with dissolve
    # s concerned "If I... mmn, if I hurry I should not miss out on too much. So Atsuko, if you will excuse us?" with dissolve
    stop music fadeout 5.0
    "The look Atsuko is giving all of us... surely she doesn't buy any of this?"
    show Nozomi sad_side noblush
    "She sure looks like she wants to give us a piece of her mind, that's for sure..." with dissolve
    queue music Downtown
    nm happy "Well he won't hear about it from me~" with dissolve
    "Huh. I really thought she was going to call us out there."
    show Nozomi neutral_side
    nm smile_side "Anyway I'll let you all get on. It's been lovely to see you again, Sayori." with dissolve
    "Maybe she doesn't actually give a shit. It's not like Sayori's *her* daughter, after all."
    s casual smile "Likewise, Atsuko. Thank you for understanding." with dissolve
    scene bg n bedroom day
    show Nozomi side casual sad_side at center, flip:
        xpos 0.25
    show Sayori casual sleeptalk_concerned blush at center
    with longblink
    s "Huuurrrrrgh..."
    "The moment we're safely inside Nozomi's room, Sayori lets out a most uncharacteristic groan."
    n "Are you alright?"
    "She sure doesn't look alright. And I'm not even talking about how close she seems to dropping dead right in front of us."
    s sleeptalk noblush "I will live. Let us just leave it at that." with dissolve
    "Still, Sayori simply shakes her head dismissively before turning to face me as her expression becomes serious."
    s casual_handup frown_right "Besides, we do not have much time so let us get down to business." with dissolve
    show Nozomi neutral
    "Right. The very reason we came here is buried in my pants pocket as I move to grasp it in my hand." with dissolve
    show penlight at right with moveinright:
        ypos 0.346
    "I'm really going to give this thing up, huh?"
    s concerned_right "Are you... having second thoughts, perchance?" with dissolve
    "All my hard work and determination is instilled in this device. A device that Sayori strongly believes can control minds and I..."
    hide penlight at right with moveoutright
    show Sayori smile_right
    show Nozomi smile
    "... and I simply smile as I pass it over to her waiting hands." with dissolve
    ks casual smile "No, it's fine.  Let's do what we came here to do."
    "After all, I already made my decision at the arcade and Sayori's been through enough as it is."
    "And besides, it's not like she can actually control my mind with this thing."
    s "Very well. Then Kyou, I would like you to lay down on the bed and we can get started."
    "... Right?"
    show Nozomi neutral_side
    s concerned "Uh, if that is okay with you, Nozomi?" with dissolve
    n surprised "Oh, sure. Go ahead, Kyou." with dissolve
    scene bg blackscreen
    # show Sayori:
    #     linear 1.0 xpos 0.75
    # pause 1.0
    # show Sayori neutral_right
    # show Nozomi neutral
    play sound clothes
    with dissolve
    "Nozomi steps aside and, with a glance at them both, I do as I'm asked."
    # show Sayori:
    #     xpos 0.75
    # s casual_handup sleeptalk "... I fear I may never be able to look your mother in the eye ever again." with dissolve
    # s sleeptalk_concerned "Perhaps it would be best if this was the last time I set foot in this house. Let her believe I am... awwwn.. s-some reckless delinquent." with dissolve
    # n sad_closed "Oh, Sayori..." with dissolve
    # s casual happy "Mrrrnn... what have I become..." with dissolve
    # show Nozomi at flip:
    #     linear 1.0 xpos 0.4
    # pause 1.0
    # show Nozomi happy at flip:
    #     xpos 0.4
    # n "Ehehe come on, you. Snap out of it~" with dissolve
    # "Nozomi moves to hug her friend, and as they chuckle together with fondness, I'm reminded of why we even came here..."
    # n smile_side "Let's focus on what's important, okay?" with dissolve
    # "My hand drifts into my pants pocket, gripping the penlight that's seemingly caused so much trouble."
    # s smile noblush "Of course. I cannot allow myself to expire from shame until I complete the task before us." with dissolve
    # n neutral_side "Or exhaustion. Do I need to hold you upright or can you stand on your own?" with dissolve
    # show Nozomi at flip:
    #     linear 1.0 xpos 0.25
    # pause 1.0
    # show Nozomi neutral at flip:
    #     xpos 0.25
    # show Sayori smile_right
    # "As Sayori sluggishly disentangles herself from Nozomi's embrace, she looks to me expectantly..." with dissolve
    # show penlight at right with moveinright:
    #     ypos 0.346
    # "... And with a smile I take the penlight from my pocket and hand it over."
    # ks casual smile "Yeah, let's do what we came here to do, I guess."
    # hide penlight at right with moveoutright
    # show Sayori casual_handup
    # "As she takes it in her slender hand, she regards me with a sleepy half smile." with dissolve
    # s "It seems my most reckless feat is yet to come. So if you would like to make yourself comfortable?"

    # show Sayori sleeptalk
    # show Nozomi neutral_side
    # "As she takes it in her slender hand, her eyes flutter closed once more as a frown falls upon her face." with dissolve
    # s "Kyou... I understand that you have misgivings about what I am attempting." with dissolve
    # ks confused "I mean... yeah? At this point I've got to wonder who's gonna fall asleep first."
    # s casual smirk_right "You both worry too much. Anyway, embrace your misgivings. Indulge your anxieties."
    # s "Now... Nozomi, would you mind if too terribly if we borrowed your bed for a while?"
    # "What I'd give to see inside that mind right now."
    # n sad_side "Huh? O-oh sure, I don't mind." with dissolve

    # "Right. She wants me to take a relaxed position, just like I had her when I hypnotized her."
    # show Nozomi sad
    # "So as Nozomi stands aside, I move to her bed and lay down carefully upon it." with dissolve
    scene SayoriPenlight s_neutral n_neutral with longdissolve
    "Sure feels odd, setting myself up like this. I never expected anyone would try hypnotizing me, and I sure didn't think I'd want anyone to."
    n neutral_side "So, um... what's the plan, Sayori? Do you know what you're doing?"
    "And man, Nozomi's bed feels way softer than mine."
    show SayoriPenlight s_neutral_right
    s smile "This is very much out of my realm of experience, but... yes. Sort of." with dissolve
    "Kinda smells nicer too..."
    # n smile_side "Okay well, if you need my help for anything..."
    n smile_side "Okay well, I don't want to disturb you two so I'll just stand over here. Let me know if you need me for anything, okay?"
    "But as pleasant as this feels, I know I can't get distracted."
    show SayoriPenlight s_smile_right
    s "Thank you, Nozomi. There is something we should discuss soon but for now, I would like you to observe us." with dissolve
    "Sayori's standing over me now; my penlight held aloft as she begins to address me."
    show SayoriPenlight s_neutral
    s smile_right "So Kyou, I shall attempt to hypnotize you with this penlight and, should I succeed, will aim to resolve the situation as we discussed." with dissolve
    "Resolve it by controlling my mind? That's what she means, right?"
    show SayoriPenlight s_quizzical
    s neutral_right "In the process of doing so, I will prove or disprove conclusively that this form of hypnosis you created is capable of surpassing the human will." with dissolve
    "And I'm really going to let her try it..."
    show SayoriPenlight s_neutral_right
    s neutral "Should all go according to my plan, neither I nor anyone else will live in fear of this phenomenon ever again. I will \"fix\" this, as you so desired this morning." with dissolve
    show SayoriPenlight s_neutral
    s neutral_right "And you do still desire such an outcome, correct?" with dissolve
    # s "After all, you wished that you could \"fix\" this, did you not? You desired as such this morning."
    # s "It is my intent to fix everything. , just as you wished this morning. Is that still your wish?"
    ks casual confused "Well... yeah. I wouldn't be doing this if I didn't, right?"
    stop music fadeout 5.0
    "Sayori notes my response and nods, seeming to regard me with all the coolness of a doctor assessing a patient."
    s "Now... {w=1.0}{nw}"
    show SayoriPenlight s_yawn
    $ renpy.transition(longdissolve, layer="master")
    extend "{cps=10}awwwnn...{/cps}"
    "At least until she yawned again. Makes me wonder which of us is gonna fall asleep first..."
    queue music Night_Road
    show SayoriPenlight s_neutral
    s neutral_right "Now I feel I should warn you that you may experience some discomfort during the process. But please do not worry. I can guarantee no harm will come to you." with dissolve
    "And now she sounds like... damn, why am I feeling like a guinea pig in an unethical experiment all of a sudden?"
    show SayoriPenlight s_smirk
    s smirk_right "Ehehe... Does my prattle make you anxious? Good. Keep that feeling as we begin..." with dissolve
    show SayoriPenlight light
    with flash
    "Before I can utter a retort, Sayori flips the switch of the penlight and I'm immediately blasted by a flash of its light..."
    show SayoriPenlight n_curious s_quizzical
    s surprised_right "As I recall, the technique is for me to pass the beam back and forth like so." with dissolve
    with flash
    "She flashes the light in my eyes a second time and I'm already seeing a dazzling array of spots and patterns."
    s "And for you to simply listen to me. For you to focus on this captivating little creation of yours."
    with flash
    "I mean, it shouldn't surprise me. I'm the one who put them there, and yet..."
    show SayoriPenlight s_smile
    s smile_right "And it is captivating, is it not? Simply take it all in." with dissolve
    "And yet I can't help but wonder about them."
    $renpy.music.set_volume(1.0)
    $renpy.music.set_volume(0.9)
    with flash
    s "Fully immerse yourself in the warm glow of the light."
    show SayoriPenlight s_neutral
    with flash
    $renpy.music.set_volume(0.8)
    s "Allow yourself to see every detail it impresses upon you."
    "This is what made Sayori go so deep into trance and accept that she could become a different person?"
    with flash
    $renpy.music.set_volume(0.7)
    s "Let it consume your every thought, and..."
    with flash
    $renpy.music.set_volume(0.6)
    show SayoriPenlight s_yawn_right
    s sleeptalk_concerned "Awww...  become your entire focus now." with dissolve
    "This is... uhh, what was I even thinking about? Well, never mind."
    show SayoriPenlight s_yawn n_anxious
    $renpy.music.set_volume(0.5)
    with flash
    s sleeptalk "Becoming so focused upon this light, that you may notice you are becoming tired. You may find yourself wanting to blink more and more."
    "I need to focus. Even though it's... hard..."
    show SayoriPenlight s_neutral
    with flash
    $renpy.music.set_volume(0.4)
    s "And that's only natural. It's natural to feel so tired when one is so completely focused as you are."
    with longblink
    "It's hard... to keep my eyes open."
    with flash
    $renpy.music.set_volume(0.3)
    s "Feeling more and more tired, every time you blink."
    "Hard to... think..."
    show SayoriPenlight s_yawn
    with flash
    $renpy.music.set_volume(0.2)
    s "And... mrrrn, with every blink you make, as you become more and more... t-tired, you will naturally wonder how good it would feel..."
    with flash
    $renpy.music.set_volume(0.1)
    s "... if you were to simply keep those tired eyelids closed."
    $persistent.sayori_penlight_unlock = True
    scene bg blackscreen with longdissolve
    s "Feeling good. Feeling relaxed. Feeling ready to let your every conscious thought go..."
    play sound fingersnap
    stop music
    s "Now. Sleep."
    pause 3.0
    $renpy.music.set_volume(1.0)
    # scene bg n bedroom day
    # show Nozomi front casual surprised at center:
    #     xpos 0.25
    # show Sayori casual_handup neutral_right at center
    scene SayoriBed1 nozomi1 n_fascinated sayori1 s_curious
    play sound fingersnap
    s "-nd Now. Thoughts returning, Kyou. Come back to us."
    "I find myself drawing a deep, shuddered breath as I suddenly find myself standing over..."
    play music Eons
    show  SayoriBed1 sayori2 s_neutral
    $ renpy.transition(dissolve, layer="master")
    ks casual confused "S-Sayori? What...?"
    "I'm standing? When did I get off the bed? I was just lying there while Sayori was..."
    show SayoriBed1 n_curious_right2
    n neutral_right "Well he certainly doesn't seem to remember, does he?" with dissolve
    "While she was trying to hypnotize me... right."
    show SayoriBed1 n_curious_right1 s_curious
    s casual_folded "Indeed. Kyou, could you confirm to us that you have no recollection of the last twenty minutes?" with dissolve
    show SayoriBed1 n_curious1
    ks confused "T-twenty minutes? What?" with dissolve
    "{cps=15}I gotta scratch my head here and... {/cps}{w=0.5}{nw}"
    show penlight at right:
        ypos 0.346
    ks surprised "Hah!"
    "I just tapped myself on the head with... with my penlight? When did I get this back?"
    hide penlight at right with moveoutright
    show SayoriBed1 n_concerned
    n concerned "Kyou? Calm down, okay? It's fine if you don't remember." with dissolve
    show SayoriBed1 s_concerned
    s concerned_right "Indeed. You were asked to forget, after all." with dissolve
    "Holding my head in one hand, I sigh as I recall what Sayori was trying to prove with me."
    ks "So... you did it? You actually hypnotized me?"
    show SayoriBed1 s_smile
    "Sayori simply smiles triumphantly, as if I needed more evidence for my eyes." with dissolve
    show SayoriBed1 n_curious1
    s "It appears everything is proceeding exactly as I hoped. You really don't remember a thing, do you?" with dissolve
    ks sigh "Yeah... So what the hell happened just now?"
    show SayoriBed1 n_concerned_right sayori4 s_concerned_left
    "The pair of them exchange looks like they're barely able to explain to themselves what they've just seen, let alone to me." with dissolve
    "But eventually it's Nozomi who clears her throat as she begins to answer me."
    show SayoriBed1 n_concerned sayori2 s_neutral
    n sad "Okay well, when Sayori and I were sure you were deep in trance, she gave you some instructions to take the penlight and hypnotize her just like you did before." with dissolve
    show SayoriBed1 n_curious2
    n "And that when you did, you'd remove the sleeping and personality-switching suggestions you gave her \"to the best of your ability\" before waking her up and..." with dissolve
    show SayoriBed1 s_curious
    s casual_handup "And awaiting further instructions, yes." with dissolve
    show SayoriBed1 n_concerned s_neutral
    n sleeptalk_concerned "Oh my god, Kyou, you should have seen yourself. It was like watching some kind of robot running a program." with dissolve
    show SayoriBed1 n_fascinated
    n shocked "The moment Sayori clicked her fingers you snatched the penlight back and you just... you just did it! You didn't even hesitate for a second!" with dissolve
    ks confused "I... seriously?!"
    "Whoa, is this what it feels like to be hypnotized? It's a little freaky, that's for sure."
    show SayoriBed1 n_curious2
    n "Yeah. It was kind of incredible watching you from the sidelines. A hypnotized hypnotist performing on the very person who hypnotized them..." with dissolve
    "That really happened? I did all that under hypnosis?"
    show SayoriBed1 n_concerned
    n sad_closed "I've never seen anything like it." with dissolve
    "Gotta admit, I'm having a hard time wrapping my head around this..."
    show SayoriBed1 n_concerned_right s_concerned
    s casual "I can see that you are not entirely believing of Nozomi's account. And to be fair, I was not conscious to witness it myself." with dissolve
    show SayoriBed1 s_neutral
    s neutral_right "But proving it, Kyou, is a simple matter. You have only to say two words and we can erase all doubt right here and now." with dissolve
    show SayoriBed1 s_frown
    s frown_right "And I am anxious to reach a resolution. So let us prove it together." with dissolve
    "I nod as I realize what she means."
    show SayoriBed1 n_concerned
    ks "You want me to say it?" with dissolve
    "That phrase. The one that left her so afraid of me since that day..."
    show SayoriBed1 s_irritated
    s casual_folded "I want you to say it." with dissolve
    "The one that's caused so much trouble... I take a deep breath, steeling myself before..."
    ks "... Become [alt_name]."
    "Before I allow the dreaded phrase to leave my lips for Sayori to hear clear and true."
    stop music fadeout 2.0
    show SayoriBed1 n_concerned_right s_neutral
    s "..." with dissolve
    show SayoriBed1 s_surprised
    s casual surprised_right "Hah..." with dissolve
    show SayoriBed1 n_curious_right2
    n sad_side "Hah? Sayori, what happened?" with dissolve
    show SayoriBed1 sayori3
    s casual_folded "Nothing..." with dissolve
    play music Inspiration
    "Sayori holds a hand to her chest as she begins to giggle with relief."
    show SayoriBed1 n_curious_right1 s_laugh
    s casual_handup laugh "Ahahaha, nothing has happened!" with dissolve
    show SayoriBed1 s_happy
    s happy "My mind is clear and Kyou's words have no longer hold power over me, I am certain." with dissolve
    "I release the breath I was holding as I witness the delight in Sayori's face. A delight that I know she, not \"[alt_name]\", is expressing."
    show SayoriBed1 n_smile
    n sad_closed "Oh, thank goodness. When you got so excited I was fearing the worst." with dissolve
    "But then that means..."
    show SayoriBed1 sayori4 s_pout
    s pout "Oh come now, Nozomi. Do you really consider me such a stick in the mud?" with dissolve
    "That means I really was hypnotized into doing all that?"
    show SayoriBed1 n_giggle
    n happy "Eheh, sorry. But I'm really not used to seeing you like this." with dissolve
    show SayoriBed1 n_smile
    n smile_side "At least not until today, with the arcade and the, um..." with dissolve
    "I hypnotized Sayori just now, with my penlight, and I don't remember a single thing?"
    show SayoriBed1 n_giggle
    n laugh "And the play-acting downstairs, ahahaha~" with dissolve
    show SayoriBed1 s_rolleyes
    s rolleyes "Urrgh, now why on earth did you bring that up?" with dissolve
    n smile_side "Oh gosh, I could've sworn mom thought you'd gone crazy back there."
    "Sayori, with nothing more than a penlight and a meagre understanding of hypnosis was able to perform a feat just as incredible as mine when I hypnotized her."
    show SayoriBed1 n_smile s_concerned_left
    s casual_handup sleeptalk "Yes... I fear I may never be able to look your mother in the eye ever again." with dissolve
    show SayoriBed1 n_concerned_right sayori2 s_concerned
    s sleeptalk_concerned "Perhaps it would be best if this was the last time I set foot in this house. Let her believe I am... awwwn.. s-some reckless delinquent." with dissolve
    "That's... what does this mean? Don't tell me she's right about my penlight being a mind control device."
    n sad_closed "Oh Sayori no, don't think like that."
    "That's just... that's just nuts. It's too absurd to even think about."
    show SayoriBed1 s_happy
    s casual happy "Mrrrnn... what have I become..." with dissolve
    $persistent.sayori_bed1_unlock = True
    scene bg n bedroom day
    show Nozomi side casual happy at center, flip:
        xpos 0.4
    show Sayori casual_handup happy at center
    with blink
    n "Ehehe come on, you. Snap out of it~"
    "Nozomi moves to hug her friend, and as they chuckle together with fondness I'm left shaking my head."
    stop music fadeout 5.0
    ks casual confused "I don't believe it..."
    show Nozomi at flip:
        linear 1.0 xpos 0.25
    pause 1.0
    show Sayori smile_right
    show Nozomi neutral at flip:
        xpos 0.25
    n "Hm? What don't you believe?" with dissolve
    "There's a rational explanation for all of this."
    queue music Eons
    ks neutral "Look, it's great that you feel in control of yourself again. That was always the main thing about doing all this."
    ks "But Sayori, if this is supposed to prove this penlight is literally controlling our minds I really don't see how."
    show Sayori casual_handup sleeptalk_concerned
    n sad_closed "Oh, Kyou..." with dissolve
    "Yeah, you sigh all you want. That doesn't change the facts."
    ks frown "What? It's just the truth."
    show Sayori neutral
    n frown "Sayori managed to hypnotize you so deeply that you were basically hers to command and you don't even remember her doing it." with dissolve
    n frown_side "She did it despite barely knowing anything about the process, not to mention the fact you'd never been hypnotized before." with dissolve
    hide Nozomi
    show Nozomi front2 casual frown at center:
        xpos 0.25
    n "The only thing she had was your penlight!" with dissolve
    ks frown "\"Hers to command\"? That's a little dramatic, don't you think?"
    n irritated "Look, do you really think she could've had that kind of sway over you if that penlight wasn't as dangerous as she said it is?" with dissolve
    show Sayori neutral_right
    ks sigh "Hey, it might be enough to convince you, but that really only proves one thing." with dissolve
    n frown "And that is?" with dissolve
    "I fold my arms and draw a breath through my nose."
    "It's a little embarrassing to admit, but it's the only rationalization that makes any goddamned sense."
    ks sigh "Well, turns out I'm just as easy to hypnotize as Sayori. We're both in that top category of super-suggestible people."
    show Nozomi side sad_closed at flip
    n "Oh, for the love of..." with dissolve
    n frown "Do you really think you're *both* so hypnotically suggestible that you'll go along with anything a hypnotist tells you? How likely do you think that is?" with dissolve
    ks frown "More likely than some cheap penlight being able to control minds like it was out of some hokey thriller novel, that's for sure."
    hide Nozomi
    show Nozomi front2 casual irritated at center:
        xpos 0.25
    n "Oooh, you... " with dissolve
    n determined "After everything we've seen today you're still not convinced? I can't believe you're being so stubborn." with dissolve
    s casual_folded frown_right "Be that as it may, I will concede that you have a point, Kyou." with dissolve
    n sigh "Ugh, maybe. But still..." with dissolve
    s neutral "It is fine. An extraordinary claim such as mine requires extraordinary evidence, after all." with dissolve
    show Nozomi neutral_right
    s sleep "So let us entertain that you and I both possess an extreme level of affinity for entering a hypnotic state and absorbing suggestions into our subconscious." with dissolve
    s neutral_right "Just as you have asserted that I wished on some level for the behaviours you effected on me via hypnosis, the same could be said for you." with dissolve
    s concerned_right "After all, you were sincere in your desire to fix my situation, were you not?" with dissolve
    ks neutral "Well, yeah. Of course I was."
    s casual neutral "If we were to assume your level of hypnotic suggestibility is comparable to mine, then it follows you would have little issue in carrying out the behaviours I impressed upon you." with dissolve
    s neutral_right "It is not \"mind control\" to persuade you to do something you were already predisposed to doing." with dissolve
    ks "Exactly. That's exactly my point."
    show penlight at right with moveinright:
        ypos 0.346
    "I hold the penlight up to look at it once again."
    "This small, unassuming, cheap little penlight that only differs from any other because of a few insignificant little markings I added to the bulb and the lens."
    "The light's great at catching the attention, no doubt about that, but to imagine I could use it to alter brain chemistry? Override the human will into doing anything I wanted?"
    stop music fadeout 5.0
    show Nozomi side sad_side at flip
    n "So I guess now is the moment of truth, huh, Sayori?" with dissolve
    "It's impossible."
    s concerned "I-indeed. It's time..." with dissolve
    "My eyes drift from the penlight to notice the girls looking to each other with an expression I can't quite understand."
    "For some reason it makes me a little anxious."
    ks confused "What do you mean? What are you talking about?"
    show Nozomi sad
    s casual_handup frown_right "... Break the penlight, Kyou." with dissolve
    play music Measured
    "Before I can say anything I'm stunned by the sight of these two hands in front of me."
    "Their fingers wrap tightly around the frame of my penlight before they tense and strain with all the might they can muster."
    ks frown "M-mmgh!"
    "But these are... they're MY hands!?"
    show Nozomi surprised
    show Sayori surprised_right
    n "Oh my god he's really doing it!" with dissolve
    ks angry "Haaah! N-no!"
    "I'm not doing this. I'm not..."
    ks "Stop! F-fucking... no, STOP!" with vpunch
    hide penlight
    ks "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!" with shake
    "My breath catches as I register the sight of the penlight's frame splintering in front of me as it visibly bends in two before my very eyes."
    show Nozomi sad
    show Sayori casual concerned_right
    "Surely there's no way this thing can ever work the way it did ever again." with dissolve
    ks surprised "Haaah.. h-haaah..."
    "And it's only then, as I draw a shuddered breath into my lungs, that my arms can finally relax."
    # s sleeptalk "There, Mr. Koyama. There is your proof." with dissolve
    "For a moment the room falls silent as I stare at the bent-up penlight in my hands; now little more than a broken tube."
    # s sleeptalk "And that, I dearly hope... is that." with dissolve
    stop music fadeout 5.0
    "And I..."
    show Sayori surprised_right
    hide Nozomi
    show Nozomi front2 casual surprised at center:
        xpos 0.25
    show Nozomi surprised
    ks angry "Wh-what the HELL, you guys?!" with dissolve
    "I can't take this."
    play music Sorrow2
    ks "This was your plan all along, Sayori? Trick me into breaking my creation without telling me? That was your big fucking resolution?"
    n concerned "Kyou? H-hey, please calm down, okay?" with dissolve
    #Maybe describe how his anger feels good, like he's asserting control over himself.
    "Nozomi skittishly looks to the door, like she wants to run away... or she's afraid her mom will burst in at any moment."
    s concerned_right "My apologies. I know it was unseemly of me, but I fear you would not be convinced otherwise." with dissolve
    "Yeah, I know I gotta cool this down. Take a breath."
    ks frown "Man, whatever. But you had no fucking right, Sayori, just because you're freaking out over this thing."
    "But what the goddamn hell do they expect if they're gonna pull this shit?"
    ks frown "You think you're so smart, tricking me into doing that? Well, I got the schematics written up on my computer."
    s surprised_right "K-Kyou, you wouldn't..." with dissolve
    ks "I mean, it'd take a lot of effort, but I could. I could make another one..."
    # "I almost want to do it just to spite her."
    show Nozomi shocked
    s scared_right "Kyou please, NO!" with dissolve
    "But just then I see that look in Sayori's eyes."
    s casual_handup "Y-you were not tricked! Don't you see?" with dissolve
    "And it stops me cold. There's no arrogance in that expression at all."
    show Nozomi concerned
    s casual "You moved to destroy your own creation, even though every part of your conscious will was screaming to stop!" with dissolve
    "There's only that same frightened girl I witnessed back in the classroom that day."
    s concerned_right "Surely you can see what this means? There was no trick in what I did to you." with dissolve
    # "And I sigh and nod my head as I'm forced to admit..."
    "And I'm forced to admit the truth as I hang my head and allow the bent remains of my penlight to slip through my fingers."
    ks sigh "So it really does control minds..."
    scene SayoriHug sad with blink
    "For a moment, no one seems to know what to say. But as I stand there motionless I feel a warmth as Sayori suddenly moves to embrace me."
    s "I truly am sorry you had to experience that."
    s "The fear. The anger. The realization that you lost your entire sense of agency in a manner that defies all rational explanation. And that you were helpless to stop it."
    show SayoriHug talk
    s sleepy "Believe me, I am familiar." with dissolve
    ks casual sigh "Yeah... yeah, I get it."
    "Much as I hate to admit it, I know that thing had to go."
    s concerned_right "You understand now, don't you. You realize the danger it presents anyone that is subject to it. And the sheer temptation it presents to any who would use it with that knowledge."
    stop music fadeout 5.0
    show SayoriHug sad
    s casual_handup "For all our sakes, it simply had to be destroyed." with dissolve
    "I can't argue with her. All I can do is sigh as we all look down upon the ruined penlight that lay discarded on the floor."
    ks sigh "Man, I don't know if I could even remake this thing anyway. It was a freak accident I even did it the first time."
    ks "But yeah... maybe it's best I don't find out."
    $persistent.sayori_hug_unlock = True
    scene bg n bedroom day
    show Nozomi front2 casual concerned at center:
        xpos 0.25
    show Sayori casual concerned_right at center
    with blink
    queue music Eons
    "For a while we all just look at the ground. No one really seems to know what to do now this chapter in our lives has surely come to an end."
    show Nozomi side sad_side at flip
    n "So, um... that was a little intense, huh. But..." with dissolve
    "Eventually, Nozomi begins to speak as she poses the question on everyone's lips."
    n sad "... What do we do now? Can we really just forget what Kyou had here?" with dissolve
    show Sayori casual sleep
    "I don't really have an answer to that. But after another moment's silence, Sayori turns from us to gather her things from the floor." with dissolve
    n neutral_side "Sayori?" with dissolve
    s concerned "In all honesty, I believe that would be for the best." with dissolve
    n sad_side "Okay, but what are you doing now?" with dissolve
    s sleeptalk "Mmrn... I must apologize once again, leaving you all like this." with dissolve
    ks casual confused "What do you mean?"
    s sleepy "Now is the time I take back control of my life." with dissolve
    # s concerned "My apologies once again. But now is the time I take back control of my life." with dissolve
    "She stands up with a grunt as she cradles her textbooks in her hands."
    s casual_folded sleeptalk_concerned "Surely you have not forgotten already? As fun and... frightening today has been, I still have work to do. And I have disappointed my father far too many times this week." with dissolve
    ks "You're seriously going back to cram school?"
    n shocked_side "In your condition? Sayori, you barely made it back here, how on earth do you think you can carry on like this?" with dissolve
    s sleeptalk "I-I... rrrng..." with dissolve
    s sleeptalk_concerned "I will manage. I always do." with dissolve
    s sleepy "I... I must..." with dissolve
    n sad_side "I'm sorry, but you're a total wreck, Sayori. You can't go back there!" with dissolve
    stop music fadeout 2.0
    play sound dooropen
    show Nozomi surprised
    show Sayori surprised
    nm "Hmm, I'm afraid I have to agree." with dissolve
    show Sayori:
        linear 0.5 xpos 0.5
    show Nozomi:
        linear 0.5 xpos 0.35
    pause 0.5
    show Nozomi shocked:
        xpos 0.35
    show Atsuko neutral_side at center, flip:
        xpos 0.15
    show Sayori surprised
    with dissolve
    "Another voice interjects, startling the three of us as we look around to see none other than..." with dissolve
    hide Nozomi
    show Nozomi side casual shocked_side at center:
        xpos 0.35
    play music Monologue
    n "MOM!" with vpunch
    nm sleep "I know, I know, I shouldn't eavesdrop..." with dissolve
    "Oh geez, how long has she been listening to us? Did she have her ear pressed to the door this whole time or what?"
    show Nozomi sad_side
    nm neutral_side "And it's like I said before; you three are grown-ups. You don't need an overbearing busy-body like me poking my nose into everything." with dissolve
    nm "But I'm sorry, I've been worrying all morning and, hand on my heart, I don't think I can let this be."
    n "W-what do you mean?"
    nm "Sayori, hun, you need to take a break. A *real* one this time."
    "I look to Sayori, her textbooks cradled in her arms as she regards Nozomi's mother with a stunned expression."
    nm surprised_side "I mean, that's what you've been telling us isn't it? All that talk of playing games and goofing off earlier?" with dissolve
    show Sayori sleeptalk
    show Nozomi sad
    "Her head droops slightly, her eyelids fluttering as if she could just drop to the floor in an exhausted heap." with dissolve
    show Sayori  frown
    "But a moment later she seems to collect herself as she shakes her head; her arms tensing tightly around those textbooks." with dissolve
    s "I... A-Atsuko, I should not have said such frivolous things, and I am sorry to have worried you."
    s irritated "But I have obligations and they must be fulfilled. Please understand." with dissolve
    # s casual_handup frown "I... A-atsuko, I know you mean well, but you do not know my situation. Please understand." with dissolve
    "Atsuko puts a hand to her cheek and sighs."
    nm sleep "Oh my, you must be talking about your father." with dissolve
    s sleepy "B-besides, this... th-this reckless side of me has gotten me into enough trouble. I simply must..." with dissolve
    nm neutral_side "Dragging yourself to work while unfit sounds rather reckless to me, Sayori." with dissolve
    s panicked "Ahhh, b-but this is... different." with dissolve
    s scared "M-Mrs. Akemi, I cannot... y-you don't understand, I can't simply abandon my... my obligations, I..." with dissolve
    #Carry on from here

    # nm sleep "Dear, you've been crying out for someone to stop you all day. Don't think I haven't noticed your acting out." with dissolve
    # s scared "Ahhh, b-but that was... I wasn't myself, I-I mean..." with dissolve
    # s scared_right "M-Ms. Akemi, I cannot... y-you don't understand, I have certain expectations to fulfill, I can't simply-" with dissolve
    "As Sayori babbles desperately to convince her, we can only stand by as Atsuko places a hand on Sayori's shoulder and smiles gently."
    show Sayori surprised
    show Nozomi sad_side
    nm smile_side "Let me talk to him, Sayori. Let me talk to your father, from one parent to another." with dissolve
    s sleeptalk_concerned "But if I... th-that is..." with dissolve
    show Nozomi sad
    s sleepy "... Mrrn, do you think it would help?" with dissolve
    nm happy "I'm sure he wants what's best for you. And right now, that involves turning that hard work ethic of yours inward." with dissolve
    nm neutral_side "Which starts by getting some gosh-darned rest, young lady!" with dissolve
    show Sayori casual sleeptalk
    "Sayori lets out a groan as she lets her arms drop; her treasured textbooks scattering to the floor as if to signal her defeat." with dissolve
    s "I... suppose I can disappoint him a... a little longer..."
    show Atsuko smile_side
    "Atsuko tuts a little to herself and shakes her head at the shattered girl." with dissolve
    nm "You're not disappointing anyone, dear. Just take care of yourself, okay?"
    show Sayori:
        linear 2.0 ypos 2.0
    play sound sitting
    "To that, Sayori doesn't have an answer. Instead, she takes a step back before unceremoniously flopping down onto Nozomi's bedsheets."
    s "{size=16}Nozomi....{/size}"
    show Sayori:
        ypos 2.0
    show Nozomi sad_side at flip
    n "Um, yes?" with dissolve
    s "{size=16}... I need to borrow your bed againnn...... mmrn...{/size}"
    show Atsuko happy
    n happy "Ehehe... sweet dreams, Sayori..." with dissolve
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    pause 1.0
    # "(( AUTHOR'S NOTE: Okay, I'm afraid that's all the script I can manage for this update. All that follows is the largely unchanged outline for the rest of the story. ))"
    # "(( As ever, feedback is appreciated while I work on the conclusion to this storyline! ))"

    #Once the conflict is resolved, Sayori realizes she barely has enough time to make the late afternoon class. She's rushing to gather her books, albeit clumsily in her sleep-deprived haze,
    #before Atsuko walks in to confront her
    # "Nozomi asks despondently if she'd been eavesdropping again, but Atsuko just dismisses the question and gets straight to it."
    # "See, she had been umm'ing and ahh'ing with herself over whether to say something and seeing as Sayori is still here, decided it was time to step in."
    # "Atsuko's really worried for Sayori. After all, she's seen her acting out all day; it's like she was almost daring someone to stop her!"
    # "Atsuko's really worried for Sayori. After all, she's been acting out all day and she's clearly not handling things well."
    # "But besides that, it's clear the poor girl's been pushed beyond her limits with all this extra study and Atsuko would be remiss if she allowed Sayori to let her leave in this state; it's dangerous."
    # "Sayori starts to protest, as she's already indulged her... reckless side more than enough today, and besides she doesn't want to disappoint anyone by quitting."
    #One could say going to cram school when clearly unfit is also reckless behaviour...
    # show Atsuko smile_side
    # "But Atsuko says she'll call her father to explain the situation and smooth things over with him. They don't know each other well, but she's sure he'll understand."
    # "Sayori needs to truly focus on herself for a while, and that starts by getting some gosh-darned rest, young lady!"
    # "Sayori protests, not wanting to disappoint her dad, but Atsuko says she'll take care of that."
    # "Sayori can crash here and get some gosh-darned rest, while Atsuko calls her father to explain the situation to smooth things over with him. She's sure he'll understand."
    # show Nozomi side casual shocked_side at flip
    # show Sayori sleeptalk
    # "So what does Sayori think of that? She answers by way of flopping down on Nozomi's recently-vacated bed and mumbles she's just going to borrow it for a while."
    # show Nozomi smile_side
    # "Maybe she can disappoint people a little bit more, she concedes..."
    scene bg k bedroom eve with longdissolve
    "With Sayori seemingly at peace (and fast asleep), there wasn't really much more to do but head back home."
    queue music Past_Sadness
    "So here I am, laying on my own bed as I think back on that wild journey I had with Sayori, and with hypnosis."
    "Hypnosis and... and mind control. Thinking about it now it's over just makes it feel like some weird fever dream I had."
    "That I somehow managed to make a penlight that could do all that to Sayori... Even experiencing it myself, it still doesn't seem real. But it really did happen."
    "I put her through all that confusion and pain because I didn't know what I was dealing with. I literally reshaped part of her mind to think she hated everything about her real self."
    "I even made her think she had a crush on me... goddamn, why did I think that was a good idea?"
    "What's she going to think of me when she's had the chance to think about what I've done?"
    "Maybe it would've been better if I never studied hypnosis in the first place."
    "If I never forced my way into Sayori's life at all..."
    stop music
    # "He seems ready to abandon his interest in the subject. He never knew what he was doing and now the penlight's gone he's not keen on dabbling in it any further."
    # "Still, what will he do now? He's glad Sayori's going to be fine, but is he in any better a place than when he started? Is he gonna be back to lonely social outcast Kyou?"
    play sound cellvibratelong
    ks casual confused "Uhh, what?"
    "That vibrating sound..."
    show phone at right with moveinright:
        ypos 0.346
    "Wait, that's my phone! Who on earth is calling me? No one calls me!"
    stop sound
    ks "... H-hello?"
    play music Warm_Romantic
    # s "\"Let me guess. You are not used to receiving phone calls.\""
    s "\"Hello, Kyou. I suppose I have [alt_name] to thank for acquiring your phone number.\""
    ks surprised "Sayori!?"
    "After a moment's silence, an amused chuckle floats into my ear."
    # "Holy shit, yeah, I forgot we exchanged numbers."
    s "\"The one and only. I wanted to speak with you again now that my head is... somewhat clearer than before.\""
    # "But man, she surprised me. I totally forgot we exchanged numbers."
    ks confused "Yeah... y-yeah, how are you doing, anyway?"
    s "\"Hmm, well, I am safely back at home. And my parents and I had a lengthy talk about my... recent conduct.\""
    "I wince inwardly, as if I needed another reminder of all the bullshit I put her through."
    ks sigh "Ouch." #"I'm sorry you had to deal with that."
    s "\"Oh, it was not as terrible as I feared. As a matter of fact, my dad has proven to be refreshingly understanding about my situation.\""
    s "\"So moving forward we are going to reassess my work schedule to ensure I do not have another \"burnout episode\", as he put it. Heh.\""
    # "I smile as I listen to her go on. It sounds like for all the bullshit she's been through she's going to be okay at least."
    "I smile as I listen to her go on. Seems she's going to be okay at least."
    ks smile "That's great, Sayori. "
    "No thanks to me, though."
    ks sigh "Listen, Sayori, about what happened... it's not going to happen again, I promise."
    # ks sigh "I'm sorry you had to deal with that, though. This is all my fault; all this hypnosis stuff I pushed on you."
    s "..."
    ks sad "This hypnosis stuff is way more dangerous than I thought it'd be. I figured it'd be fun to show people what I could do."
    ks "Yeah I didn't know what that penlight could do, but even so I never should've given someone a dangerous suggestion when I didn't know what I was doing."
    ks "And seeing what it did to you... w-well, I guess I'm not cut out to be a hypnotist, huh."
    "I hear nothing but silence on the other end for a while. But eventually, I hear Sayori clicking her tongue."
    s "\"Kyou. What compelled you to study hypnosis in the first place?\""
    ks confused "Huh?"
    s "\"It was to be seen, was it not?\""
    # s "\"Idle curiosity? No. To assist others in their mental struggles? Also no.\""
    ks "U-uhhhh..."
    # s "\"I think, more than anything, it was out of a desire to be seen.\""
    # ks "I thought I knew what I was doing, and I really wanted to help you out, but I got way in over my head. I should've been more careful."
    # ks "Yeah, I didn't know what I had with my penlight and what it was doing to you, but it's no excuse. I should've been more careful."
    # ks "It's like you told me, hypnosis isn't a toy, and I didn't really know what I was doing. I just thought I did, and I screwed up."
    # ks "But I ... I really wanted to help you, Sayori."
    # ks sigh "S-so listen, I really am sorry about everything turned out. All this hypnosis stuff, I never meant to hurt anyone, I just..."
    # s "\"It is more than that, Kyou. You wanted to be seen.\""
    s "\"Perhaps things did not go the way you imagined, in more ways than one, but you *were* seen.\""
    s "\"Thank you, for allowing me to see you at last.\""
    ks "I-I..."
    "Oh, fuck, I have no idea how to respond to that."
    s "\"So Kyou, I am free tomorrow evening and I was wondering...\""
    s "\"... Could I see you again?\""
    stop music fadeout 5.0
    scene bg blackscreen with longdissolve
    pause 2.0
    jump Epilogue_Con_Kyou_Sayori_Alter_Switch

label Day6_Con_Kyou_Hiroko_Penlight:
    scene bg blackscreen with dissolve
    pause 1.0
    play sound cellvibrate
    ks nude sigh "Hrmm..."
    scene bg k bedroom day with dissolve
    "Ugh, man, what was that just now?"
    play music Past_Sadness
    "... Huh? My phone?"
    "Who's texting me? And this early in the morning?"
    show phone at right with moveinright:
        ypos 0.346
    "{color=FF89AB}\"Where r u\"{/color}"
    ks nude sigh "Urrrrrgh..."
    "For a few blissful hours I got to forget the existence of this bane upon my life."
    "{color=#4B9374}\"In bed, why?\"{/color}"
    play sound cellvibrate
    "{color=FF89AB}\"FFFFF\"{/color}" with vpunch
    play sound cellvibrate
    "{color=FF89AB}\"Tennis court now\"{/color}" with vpunch
    ks angry "Fucking... ALRIGHT!"
    "Yeah, sorry phone. I'm shooting the messenger by yelling at you."
    "But for fuck's sake, I'm letting this turdling push me around, and for what?"
    play sound cellvibrate
    "... She's sent me another one." with vpunch
    ks frown "Fountain pen emoji... lightbulb emoji... trashcan emoji... question mark."
    hide phone at right with moveoutright
    "Yeah..."
    stop music fadeout 5.0
    "I mean, it's not like I was going to skip out on doing this."
    "I know what the stakes are here."
    # "Kyou's naturally fucked off about Hiroko pushing him around, but he was intending to honour his bet anyway."
    play sound doorclose
    scene bg street1 day with blink
    play music Eons
    "So, after a quick shower I hastily make towards the tennis court before she does anything stupid..."
    scene bg court day
    show Risa tennis wristband_left at center:
        xpos 0.75
    show Hiroko tennis at center, flip:
        xpos 0.5
    with blink
    "By the time I get there, Hiroko and that other girl are trading shots on one of the courts."
    "They've already worked up a sweat by the looks of it. How long have they been out here?"
    h "Well, look who it is."
    ks casual sigh "I'm here, aren't I?"
    r grin "So you are~" with dissolve
    h tennis_armup angry vein "You were 'sposed to be here an hour ago!" with dissolve
    ks "Whatever. Sorry."
    "This is gonna be the longest of long days..."
    ks frown "What do you need me to do anyway?"
    show Hiroko frown novein
    show Risa smile
    "Hiroko snorts and points her thumb behind her." with dissolve
    h "Just like before: Ball boy stuff."
    h sleeptalk "Start with all those balls we punted back there." with dissolve
    r tennis_armup wristband_left_armup smug "We saved them for you. Have fun~" with dissolve
    hide Hiroko
    hide Risa
    "So this is my day, huh." with dissolve
    "And Hiroko's friend wasn't kidding. There's spent balls all over the fucking place."
    "So I start making my way around the tennis grounds, slowly, since I'm not gonna bust my ass for these two."
    "I'll come to where one or two of these old battered tennis balls rest and pluck them off the ground..."
    "Occasionally I'll throw them over to the girls when they demand more, lest they pick out more balls from their supply and make an even bigger mess for me."
    "Plus, my leisurely work ethic is letting me observe my tormentor some more."
    show Hiroko tennis_armup neutral_side at center, flip:
        xpos 0.25
    "Now they've returned to the court they were playing on, Hiroko's once again looking calm and collected." with dissolve
    "If she's irritated in any way by my slacking off, she sure isn't showing it while she trades shots with her partner."
    show Risa tennis_armup smile_side wristband_left_armup at center:
        xpos 0.75
    r "Hiro, now we're warmed up I thought we could play a game or two. You up for that?" with dissolve
    h smile_side "Oh, yeah sure~ If you wanna get slammed again, you're on!" with dissolve
    r grin "Hey, ball boy! Come here a sec." with dissolve
    "Hearing my \"name\", I trudge over to them, carrying a litter of ragged balls in my arms."
    ks sigh "What?"
    h neutral "You gotta line judge for us. We're playing a couple games." with dissolve
    "I let out a dramatic moan as I dump the balls I was holding into a bag, but for two of them."
    "Although to be honest I was hoping they'd do something like this."
    ks "Who's on serve?"
    show Hiroko tennis neutral_side
    show Risa neutral
    "Hiroko points to her friend, and I oblige by tossing the balls over to her before pacing to the sideline where I can watch them play as best as I can." with dissolve
    "So as I understand it, they're playing a point. Which means..."
    r smile_side "Alright, Hiro, let's see what you got this time." with dissolve
    ks angry "Hiroko, your shoe's untied!"
    play sound tennishit
    r angry_side "Hah!" with vpunch
    play sound tennishit
    h tennis_armup frown_side "Hmpth!" with vpunch
    r surprised_side "Ahh!" with dissolve
    r frown_side "Dangit." with dissolve
    "Hiroko's holding up to her hypnotic conditioning."
    r tennis wristband_left frown "Shut up, ball boy. You're putting us off." with dissolve
    h tennis surprised_side "Huh? What's he doing?" with dissolve
    r surprised_side "You didn't hear... {w=1.0}{nw}" with dissolve
    $ renpy.transition(dissolve, layer="master")
    extend frown_side "Oh, never mind. Here comes another one."
    hide Hiroko
    hide Risa
    "It's as I thought. The last few days have done nothing to dampen the post-hypnotic suggestions still in Hiroko's mind." with dissolve
    "Completely focused during a point so as to shut out every other distraction. And this means..."
    "... I could hypnotize her today."
    scene bg court eve with blink
    "Yeah. As the day drags on, a plan forms in my head while I go over the facts."
    "Whenever someone is following a post-hypnotic suggestion, they fall briefly back into a similar state of trance as when they were originally hypnotized."
    "I know how potent my hypnosis has been on Hiroko."
    "Just as I know how strong even her clumsy attempt on me has been, thanks to my penlight."
    "I'm well aware now, that we'll follow our hypnotic compulsions whether we'd want to or not."
    "So if I were to trigger one of the post-hypnotic suggestions still in Hiroko's head at just the right time, not only would she have no choice but to comply..."
    "... She would also be helpless to stop herself falling into that brief trance state, and I could use that to encourage her to remain in trance for me."
    "I would be able to re-hypnotize her, without the penlight, and without her willing co-operation."
    "Then I could make sure she gives up the penlight to me, and maybe punish her a little for all her bullshit."
    "All I need to do is ensure the conditions are right to trigger her when I need to..."
    "... And tonight may be the only time I can do it."
    show Hiroko tennis angry
    show Risa tennis smile wristband_left at center:
        xpos 0.75
    h "Hey, quit stalling and move yer ass!" with dissolve
    ks casual sigh "*sigh* Yes, your highnesses. Here's your drinks."
    r tennis_armup wristband_left_armup grin "Don't pretend you're not enjoying this, ball boy~" with dissolve
    show Hiroko frown with dissolve
    ks frown "Enjoying this? I've been waiting on you two all day."
    ks "Why would I enjoy that?"
    "Risa takes the juicebox I offer her and smirks at me."
    r smug "I don't know... Something makes me think you like seeing Hiro all hot and sweaty." with dissolve
    show Hiroko at flip
    show Risa grin
    h tennis_armup furious_side blush "You shut your filthy mouth!" with dissolve
    "Ugh. She's probably noticed I've been watching Hiroko pretty intently all afternoon and gotten the wrong idea."
    "But all I'm interested in is how the effects of her growing exhaustion through the day are affecting her adherence to her post-hypnotic conditioning."
    hide Hiroko
    hide Risa
    "So far, as the two of them finish their break to return to the court, there doesn't seem to be any discernable change from this morning." with dissolve
    "Hiroko argues with Risa over her comment to me but once again, she steps inside the court line and her eerie sense of calm returns in an instant."
    "It's honestly impressive to see."
    "So... yeah, maybe I'm a little into watching her, Risa."
    show Risa tennis frown_side wristband_left at center:
        xpos 0.75
    r "Alright, Hiro, here it comes!" with dissolve
    play sound tennishit
    show Hiroko tennis_armup  neutral_side at center, flip:
        xpos 0.25
    "Maybe witnessing this little monster's boundless athleticism throughout the day is at least somewhat impressive." with dissolve
    "Her mental conditioning is keeping her cool, but it'd be for nothing if all this committed play breached the limitations of her body."
    show Risa tennis_armup frown_side wristband_left_armup
    "And sure, Risa's still here too, and committing to all these training drills and mock games they're doing, but I can tell she's dropped off since this morning." with dissolve
    "Her strokes are getting visibly weaker, her reactions noticeably slower, and her sprints rarer."
    "Sure, frustration's setting in too, which only compounds her growing fatigue, but I can tell Hiroko's not just handling the mental demands of today better..."
    "She's coping more adeptly with the physical challenges too."
    "My hypnosis didn't do that."
    scene bg court night
    show Risa tennis_armup wristband_left_armup angry_side at center:
        xpos 0.75
    show Hiroko tennis neutral_side at center, flip:
        xpos 0.25
    with longblink
    r "Agh... Fucksake."
    h "Somethin' up, sis?"
    "Risa pants as she mops her sweat-stained forehead with her similarly soaked wristband, glaring at her opposite number all the while."
    r tennis wristband_left frown_side "It's just... shit, Hiro, how are you doing this?" with dissolve
    h confused_side "Huh? Doing what?" with dissolve
    r "It's like..."
    "She pauses again to draw a long breath, which I'm hardly surprised by."
    "They've been doing this all day and the light's fading. Both of them must be running on fumes by now."
    show Hiroko neutral_side
    r concerned_side "You haven't put a foot wrong all day. Not in your drills, not in our games." with dissolve
    r angry "I don't want to admit it... But you're kinda pissing me off." with dissolve
    r frown_side "I mean, we DID come here to hard prep for tomorrow, don't get me wrong..." with dissolve
    r tennis_armup wristband_left_armup sleeptalk "But dammit, you're usually more fun to spar with than this." with dissolve
    h smile_side "Heh, well I didn't come here to have fun. Sorry you feel that way, Ris'." with dissolve
    "Risa snorts, which gives way to a chuckle."
    r smug_side "I'll get over it. But I'll tell you what, Hiro." with dissolve
    r smile_side "You're going to be a force tomorrow if you keep this up. I'll give you that." with dissolve
    hide Risa
    "She then turns and starts to stroll off court. Not that I can blame her." with dissolve
    "O-oh, shit, this is what I was waiting for."
    "The day's dragged on so fucking long I'd almost forgotten about the plan, but this is my chance."
    "My only chance."
    ks casual frown "Hey, Hiroko? Got a second?"
    scene bg blackscreen with dissolve
    "I can't let Hiroko leave the tennis court. If I do, this whole day will have been for nothing."
    scene HirokoCourtNight hiroko_crossed neutral kyou_casual with dissolve
    h "What's up?"
    r "Hey, I'm gonna head out. Catch up with you tomorrow!"
    "We wave our goodbyes as Risa tiredly staggers homeward."
    "Okay, now..."
    show HirokoCourtNight sigh
    h neutral_side "So yeah, thanks for helping us out. Saved us a lot of time today." with dissolve
    show HirokoCourtNight neutral_left
    h sleeptalk "I mean, you only stuck around 'cuz of what I got..." with dissolve
    "Time to put the plan in motion."
    show HirokoCourtNight neutral
    h neutral "But yeah, thanks. We're gonna be in good shape tomorrow." with dissolve
    ks casual frown "Yeah, no problem. So I can get that penlight back now, right?"
    show HirokoCourtNight frown with dissolve
    show HirokoCourtNight neutral with dissolve
    "And right there, I see it. A peeved twitch of her eyelids while she breathes deeply through her nose."
    h "You ain't getting it till after the tourney's over. Like I said."
    ks "But why wait? I did what you wanted didn't I? Hand it over."
    show HirokoCourtNight frown with dissolve
    show HirokoCourtNight neutral with dissolve
    h "You really can't wait a day, dude?"
    h "Why do you want it so bad? You wanna tell me that?"
    "Because I don't trust you to give it back? Because I'm worried you'll do something terrible with it?"
    "... Because it's mine?"
    "It's a simple question, but it stops me in my tracks a moment."
    show HirokoCourtNight sigh
    h neutral_side "'Kay, well, I'm outta here." with dissolve
    "Shit, she distracted me. I need to snap out of it and do what I came here to do!"
    ks angry "Hiroko!"
    show HirokoCourtNight irritated with dissolve
    show HirokoCourtNight neutral with dissolve
    h "... What?"
    menu:
        "Try to hypnotize Hiroko":
            ks frown "Come on, don't you think you're being unreasonable here? It doesn't belong to you, simple as that."
            show HirokoCourtNight frown with dissolve
            show HirokoCourtNight neutral with dissolve
            "That's right, Hiroko. Keep flickering those eyelids. Keep triggering yourself into staying calm and collected."
            h sleeptalk "You'll get it tomorrow. I ain't gonna tell you again." with dissolve
            "Keep priming yourself to slip back into trance just for me."
            ks "Tomorrow. After you win that tournament thanks to MY hypnosis. How do you feel about that, by the way?"
            show HirokoCourtNight growl
            h irritated "{cps=20}Gawd, would you just... {/cps}{w=1.0}{nw}" with dissolve
            show HirokoCourtNight neutral
            $ renpy.transition(dissolve, layer="master")
            extend "Just leave me alone."
            ks "You feel good about the fact your game improving is all down to me? That you never had a chance of winning without my help?"
            show HirokoCourtNight irritated
            h angry "{cps=15}FFFFF... {/cps}{w=1.0}{nw}" with dissolve
            $ renpy.transition(dissolve, layer="master")
            stop music fadeout 5.0
            show HirokoCourtNight confused
            extend sleepy "uuuhhh..."
            ks smirk "Face it, Hiroko. You don't have the mentality to succeed at this game you love so much. Not without being hypnotized."
            h "Uh, what... what're you doing to me...?"
            ks "So why deny it? You can feel yourself becoming hypnotized, can't you?"
            show HirokoCourtNight hiroko_standing sleepy_confused
            $ renpy.transition(longdissolve, layer="master")
            h sleeptalk_concerned "{size=16}Ahhh...{/size}"
            play music Flow fadein 5.0
            ks "Your mind drifting. Falling. Sinking... Sinking deeper into hypnosis."
            show HirokoCourtNight hiroko_sleeping sleep with longdissolve
            "... I've got her."
            ks "You can stay standing, Hiroko. Standing perfectly upright, like there's a metal bar running up your whole body as you allow yourself to drop deeper. And deeper."
            "Just as I suspected, triggering her post-hypnotic suggestion to stay calm over and over left her mind floating in and out of a half-tranced state."
            ks neutral "Aaaallll the way down now. Falling into a deep, relaxing sleep. Hearing only my voice. Listening only to my suggestions."
            "And with a little encouragement, that reeling mind of hers fell right back into a trance that seems every bit as deep as the ones I subjected her to with my penlight."
            ks "Isn't that right, Hiroko?"
            show HirokoCourtNight sleeptalk
            h sleeptalk "... Right." with dissolve
            show HirokoCourtNight sleep
            ks "That's right. And as you listen to my voice, as you fall back into this deep relaxing sleep, you'll find yourself needing to be completely honest with me." with dissolve
            ks "It's important to be honest when you answer me... right?"
            show HirokoCourtNight sleeptalk
            h sleeptalk "... Right." with dissolve
            show HirokoCourtNight sleep
            "It's all going just as I planned. So now to the first order of business..." with dissolve #I'll get back what she stole from me. And make sure she never messes with me again." with dissolve
            ks "Tell me where you're keeping my penlight."
            show HirokoCourtNight sleeptalk
            h sleeptalk_concerned "It's... ahhh..." with dissolve
            ks "{cps=15}Hiroko-{/cps}{w=0.5}{nw}"
            h sleeptalk "In my bag..."
            show HirokoCourtNight sleep
            "It's still in her bag, huh? And she told me she didn't have it on her..." with dissolve
            ks "Very good, Hiroko. It feels good to be honest, so allow yourself to fall deeper... feeling perfectly relaxed in this nice, comfortable state of hypnosis."
            show HirokoCourtNight -kyou_casual with dissolve
            "I back away from her slowly as I watch her remain almost statuesque by the tennis netting."
            "Once I'm sure she's going to stay put, I leave her for a minute to walk over to the bench where she left her bag."
            play sound zipper
            "I'll just zip it open and... huh, it's right there. Just casually lying amongst her other stuff."
            "So I'll just take this, slip it into my pocket and zip the bag back up before quietly returning to Hiroko, who remains just as I left her."
            show HirokoCourtNight kyou_casual with dissolve
            "She looks so peaceful right now. She's almost pretty like this; motionless but for her hair brushing lightly against her cheeks from where the breeze catches it."
            "Hiroko... What do I do with you?"
            "The moment I wake you, the moment you step off this tennis court, you'll go back to being the bullying bitch you've always been."
            "You'd be a lot more attractive if you weren't such a menace to other people."
            ks "Now Hiroko, I need you to realize that it's not a big deal that I have my penlight back."
            "And let's face it, you'd make life easier for yourself if you weren't such an asshole."
            #So he has his idea for revenge. He's not being malicious, no, he'll just force her to be kinder to others and let things go, nothing bad about that, right?
            # "She can manage her temper on the tennis court thanks to me, but she's still a menace everywhere else."
            # "I may have helped her manage her temper on the tennis court, but she's still a menace to not just me, but practically everyone else she happens upon."
            ks "When you realize the penlight is missing from your bag, you will simply believe that you agreed to let me have it back when I asked."
            "So... yeah, I know what I'll do to you."
            # "She's a shit to practically everyone unlucky enough to run across her. So what if... yeah, I know what I'll do to her."
            ks "It's perfectly reasonable and correct of you to believe this... right?"
            show HirokoCourtNight sleeptalk
            h sleeptalk "Right..." with dissolve
            "Hell, this barely counts as me getting revenge; I'm practically doing you a favour here."
            # "This'll barely count as me getting on revenge on you; I'm practically doing you a favour here."
            # "It'd be better all around if she were more reasonable in how she deals with all of us."
            show HirokoCourtNight sleep
            ks "Perfectly reasonable. It's important that you be reasonable with everyone you talk to, Hiroko." with dissolve
            "And besides, it's... I'm not gonna try and make this a permanent thing."
            ks "So once you wake up from this trance, you will find that whenever you're speaking with someone, you'll always remember to be polite and courteous."
            "Maybe just for a few days, if she doesn't manage to snap out of it by then."
            ks "Polite and courteous... understand, Hiroko?"
            "Who knows, maybe she'll have learned something by the time this is over."
            show HirokoCourtNight sleeptalk
            h sleeptalk "Yeah... polite an'... courteous..." with dissolve
            show HirokoCourtNight sleep
            ks "Wonderful. Now on a count of five, you're going to awaken from this hypnotic trance, feeling fully refreshed and accepting everything you were told." with dissolve
            ks "So one, two... slowly regaining consciousness, beginning to feel the wind on your face."
            ks "Three, taking a nice deep breath... four, feeling your eyelids begin to open and..."
            show HirokoCourtNight waking
            stop music fadeout 5.0
            ks "Five, wide awake and fully refreshed." with dissolve
            h "{size=16}Mmmnh...{/size}"
            queue music Eons
            "Hiroko's eyes begin to glimmer in the moonlight as she awakens before my eyes."
            "And just as she seems to regain her senses, I pull my penlight from out of my pocket in front of her as I flash her a confident grin."
            ks smirk "Glad you decided to be reasonable after all, Hiroko."
            show HirokoCourtNight hiroko_standing confused
            h "Huhhh...?" with dissolve
            show HirokoCourtNight smile
            "It takes her a moment, but as I wiggle my penlight in front of her eyes a polite smile beings to spread across her lips as she realizes what I'm getting at." with dissolve
            h "Ohh... yeah, no problem."
            "And I'm pleased to note that there's not a hint of irritation to be found in those eyes that now look to me with an unfamiliar kindness."
            show HirokoCourtNight happy
            h "We're square now anyways, so it's totally reasonable to give it back~" with dissolve
            "I was sure that this would work, but witnessing her demeanor shift before my eyes is immensely gratifying all the same."
            ks "Heh, glad to hear it. You really ran me ragged today, you little pipsqueak."
            show HirokoCourtNight smile
            h "Ehehehe. H'yeah, thanks for putting up with me today. You really were a big help." with dissolve
            # h "Ehehehe, sorry 'bout that. But you were such a big help today!" with dissolve
            "Yeah, I don't think she'll be menacing anyone for a while."
            ks smile "Sure. Anyway, I'm gonna head out. Be nice to everyone at the tourney tomorrow, alright?"
            show HirokoCourtNight hiroko_crossed surprised
            h "Yeah I will, but... Kyou?" with dissolve
            ks neutral "What is it?"
            show HirokoCourtNight sleepy
            h "Does that mean you ain't coming? I kinda wanted you to watch me play." with dissolve
            "Huh? She wants me to..."
            # "Huh. That's cute, I guess. But I'm sure she's just being polite thanks to the suggestion I put in her head just now."
            ks "Uhhh..."
            "... Well, she would say that wouldn't she?"
            show HirokoCourtNight neutral_left
            h "Y'know, just saying. You helped me a ton, so... it'd be cool if I can show you what all this was for." with dissolve
            "It'd be the polite thing to say to someone who's been helping your ass all week."
            show HirokoCourtNight hiroko_standing smile
            h "Plus, Nozo's throwing a lil' party for me afterward. Thought you might wanna come celebrate with us." with dissolve
            "There's... There's just no way she'd be saying any of this to me were it not for that."
            ks "Yeah, I... wasn't planning to, Hiroko."
            "And man, I wish she didn't bring up Nozomi. Just thinking about her face again is making my skin crawl."
            show HirokoCourtNight happy
            h "Suit yourself. But if you change your mind, you know where to find us~" with dissolve
            stop music fadeout 5.0
            $persistent.hiroko_court_night_bad_unlock = True
            scene bg blackscreen with longdissolve
            "Hiroko really did a number on my brain the other night, no doubt about that."
            "I mean, that's why I couldn't let her keep the penlight a moment longer, right?"
            scene bg k bedroom night with longdissolve
            queue music Past_Sadness
            "There's no way I could let her keep something that can alter a person's very perceptions of reality whether they want it or not."
            show penlight at right with moveinright:
                ypos 0.346
            "A device that stretches the boundaries of hypnosis beyond what anyone thought possible?"
            "I can't let her have this again. No one else can have it."
            "No one else can be allowed to... to use it."
            "Should I have even used it again, knowing what I know now?"
            "Maybe Hiroko had it coming after all the shit she's put me and others through. She's a bully, that much I know for sure."
            "But forcing her to fix herself with this thing? I have to admit it's a little messed up that I did that to her."
            "I won't leave her like that for long. A week maybe, then I'll meet up with her again, lift that suggestion from her head and..."
            hide penlight at right with moveoutright
            "... And then what? She'll see it was for her own good? Is that how I see it playing out?"
            "I'd have to put another suggestion in her head just to stop her from lashing out at me."
            "It'd be a permanent change to her reality, one she didn't want, but I don't think I'd have a choice."
            "... Hell, what if NONE of this is permanent? I've started to believe it is, but the truth is I just don't know how much my penlight is doing to our minds."
            "It's only been a few days since we hypnotized each other. But if it really doesn't last, then..."
            "Then I'll stop seeing Nozomi as ugly, and Hiroko will realize what I did to her one way or another."
            stop music fadeout 5.0
            scene bg blackscreen with dissolve
            "One thing's for sure, I have to keep my guard up..."
            pause 2.0
            jump Epilogue_Con_Hiroko_Penlight_Bad
        "Don't try to hypnotize Hiroko":
            ks frown "I..."
            "No. No come on, what am I doing?"
            ks neutral "Good luck tomorrow."
            "What have I even been thinking all this time?"
            show HirokoCourtNight neutral_left
            h sleeptalk "Yeah, thanks..." with dissolve
            "Forcing her into a trance and imposing my will upon her while she's helpless?"
            "What the fuck is wrong with me if I'm thinking that?"
            show HirokoCourtNight hiroko_standing neutral
            h neutral "Come watch me tomorrow." with dissolve
            $persistent.hiroko_court_night_good_unlock = True
            scene bg court night with blink
            "Maybe I could've excused it before, while I was ignorant of what my hypnosis was really doing. While I thought she'd just go along with it on her subconscious desire."
            "But now?"
            stop music fadeout 5.0
            "I'll just have to trust Hiroko won't do anything stupid until we can meet up again."
            scene bg k bedroom night with blink
            play music Past_Sadness
            play sound sitting
            "By the time I'm home, I flop onto my bed as exhaustion seeps out of my bones." with vpunch
            ks casual sigh "Fuck... what a day."
            "I guess I WILL go see Hiroko in action tomorrow."
            "After all the shit I did helping her, I'm kind of invested in her success now."
            "And besides, it'd be interesting to see how she holds up in competition."
            "It feels weird thinking it, but I might actually be getting excited for her..."
            stop music fadeout 5.0
            scene bg blackscreen with longdissolve
            pause 2.0
            jump Day7_Con_Hiroko_Penlight
    "*** TO BE CONTINUED ***"
    jump Credits

label Day6_Con_Kyou_Hiroko:
    scene bg k bedroom day with blink
    play music Eons
    "I wake up the following morning with a sinking feeling."
    "I can't stop thinking about Hiroko and last night."
    "I really fucked things up with her. I can't imagine what's going through her head right now."
    "Is she even training for the tournament? If she left that new racket behind, does that mean..."
    "I have to know."
    play sound doorclose
    scene bg street1 day with blink
    "I quickly shower and head outside, clutching the racket tightly."
    "The school will be open today, in order to accommodate the various sports clubs doing competitive matches."
    "Hiroko should be at the courts practicing for her big day tomorrow."
    scene bg court day with blink
    "As I scramble for the courts, I see a familiar face."
    show Risa tennis wristband_left at center
    r "... Ball boy?" with dissolve
    r tennis_armup wristband_left_armup smug "Hmm, or is it lover boy now? I can't decide." with dissolve
    "But no sign of..."
    ks casual frown "It's Kyou. Where is she?"
    r frown "If you're talking about your girlfriend, I haven't seen her yet." with dissolve
    "I sigh."
    ks sigh "Okay... I gotta clear things up."
    r neutral "Hm?" with dissolve
    ks "She's not my girlfriend. I made a move on her, and I shouldn't have and I hurt her."
    r tennis wristband_left concerned "Wait, are you serious? It sure didn't look that way from where I was standing." with dissolve
    ks "I, uh, I know. I sorta ambushed her, and I guess I made it awkward, so..."
    show Risa neutral_side
    show Hiroko tennis surprised at center, flip:
        xpos 0.25
    h "Kyou? {w=0.5}The fuck are {nw}" with dissolve
    extend "YOU doing here?!" with vpunch
    "I wheel round to face a familiar shrill sound."
    ks "A... a lot of reasons."
    h angry "Like I got time to hear your shit." with dissolve
    ks surprised "Wait... I-I'm sorry, okay? I didn't really apologize for before."
    h tennis_headhold2 irritated "Yeah. That really fucked me up and you know it." with dissolve
    ks neutral "I don't just mean yesterday. I'm talking about before then, too."
    show Risa neutral
    show Hiroko angry
    ks "I really didn't know I was freaking you guys out. I just didn't know what to say." with dissolve
    ks "But... it's no excuse. I should've backed off when you told me to, but I chose to be selfish instead."
    ks sigh "I hurt you, Hiroko. And I'm sorry for that."
    h sad "..." with dissolve
    ks neutral "Oh, and..."
    scene bg blackscreen with dissolve
    "I hold out the racket that I've been carrying all morning and place it in Hiroko's reluctant palms."
    scene Hiroko Racket k_neutral r_neutral h_arm1 h_head1 h_sad with longdissolve
    k "You dropped this."
    show Hiroko Racket h_head2 h_stern
    h "I don't want it." with dissolve
    show Hiroko Racket k_regretful
    k "I won't hold you to anything, if that's what you're thinking. Consider it part of the apology." with dissolve
    show Hiroko Racket k_annoyed
    k "Besides, how am I gonna return this? It's got scuff marks all over it!" with dissolve
    show Hiroko Racket r_grin
    r tennis_armup wristband_left_armup grin "Pffth, yeah, Hiroko's really big on racket abuse." with dissolve
    show Hiroko Racket h_arm2 h_angry
    h "CAN IT!" with vpunch
    show Hiroko Racket k_smile h_neutral2
    k "... So you may as well keep it." with dissolve
    show Hiroko Racket r_smile h_head1 h_neutral1
    "Hiroko eyes the racket thoughtfully as her hands form a tighter grip around the handle." with dissolve
    "I don't know if she can think her way round to forgiving me but, well, I had one other thing I wanted to give her."
    show Hiroko Racket k_neutral
    k "By the way, how long are you two planning on staying out here?" with dissolve
    show Hiroko Racket r_neutral h_head2 h_neutral2
    r neutral "As long as we need to. Why?" with dissolve
    show Hiroko Racket k_smile
    k "... Need a ball boy?" with dissolve
    show Hiroko Racket r_grin h_smile
    "Hiroko lets out a chuckle as she holds her new racket aloft." with dissolve
    h "Just try and keep up... ball boy."
    $persistent.hiroko_racket_unlock = True
    scene bg court day
    show Hiroko tennis_armup angry_side vein at center, flip:
        xpos 0.15
    play sound tennishit
    with blink
    h "Ugh, {nw}"
    extend "FUCK!" with vpunch
    show Risa tennis wristband_left frown_side at center:
        xpos 0.85
    r "It was a fifty-fifty shot, Hiro. Don't worry about it." with dissolve
    h tennis_headhold2 "More like... I dunno, ten-ninety? I keep missing 'em!" with dissolve
    h irritated "If coach was here he could've helped me figure it out, but nah, he don't work weekends. Lazy ass." with dissolve
    ks casual smile "You'll figure it out! Just keep at it!"
    "As I jog over to collect the spent ball from the latest errant shot, I wonder if Risa noticed her partner's change in demeanor back to her old self."
    "Maybe she just thinks the pressure of tomorrow is getting to her."
    scene bg court eve
    show Hiroko tennis_armup furious_side vein at center, flip:
        xpos 0.15
    with blink
    play sound tennishit
    h "RAAAAARGH!" with shake
    show Risa tennis wristband_left surprised_side at center:
        xpos 0.85
    r "Eeek!" with dissolve
    "Risa practically eats the floor as she stumbles to avoid one of Hiroko's patented double forehands flying towards her head."
    r tennis_armup wristband_left_armup angry_side "Geez, Hiro, save that for the ball boy, will you?" with dissolve
    show Risa frown_side
    h happy novein "Kyahaha! My bad~" with dissolve
    ks casual surprised "Huh. I think that one landed in."
    h smile "'Course it did. I'm nailing my range now~" with dissolve
    show Risa smile_side
    "I chuckle before taking a sip of the cola I brought over during our last break." with dissolve
    "We've been at this for hours now."
    ks smile "Man, you two look exhausted. You sure you can keep going?"
    r tennis wristband_left frown "Exhausted?" with dissolve
    "Risa, who I notice panting audibly, smirks towards her playing partner."
    r smug_side "Hiro, you going to take that crap lying down?" with dissolve
    h tennis frown "Hell, if he's complaining he can go home!" with dissolve
    ks sigh "Ugh, I was just saying!"
    show Risa smile
    "Hiroko turns to me with a chuckle." with dissolve
    h smile "Nah for real though, we're gonna break a bit." with dissolve
    scene bg court night
    show Hiroko tennis pain at center, flip:
        xpos 0.15
    show Risa tennis wristband_left frown_side at center:
        xpos 0.85
    with blink
    h "Rrrrgggh!"
    r tennis_armup wristband_left_armup concerned_side "Hiroko! You okay?" with dissolve
    h "H'yeah... If I didn't just get cramp. Fuck."
    r tennis wristband_left sleeptalk "*pant* *pant* Okay... yeah, we're done. Let's wrap this up." with dissolve
    "We may have taken some breaks here and there, but for the most part the three of us spent the entire day out here."
    ks casual frown "Are you two gonna be okay getting home?"
    r smile "Oh yeah, my house isn't far from here." with dissolve
    h tennis_headhold2 nervous "Yeah, same. I gotta rest up a sec, though." with dissolve
    hide Hiroko
    hide Risa
    "Risa wipes off her racket with a towel and packs up her things while Hiroko retreats to a nearby bench and starts massaging her calf." with dissolve
    show Risa tennis wristband_right frown_side at center, flip
    show Hiroko tennis pain at center:
        xpos 0.75
    r tennis_armup wristband_left_armup "Are you sure you're alright, Hiroko?" with dissolve
    h sad_side "Oh, yeah, this is nothing. I'll seeya tomorrow, okay?" with dissolve
    hide Hiroko
    "Risa smiles and waves to her, before turning to me." with dissolve
    r smile "Thanks for helping us today, Hiro's not-boyfriend." with dissolve
    "I wince a little. I guess it's not surprising she doesn't quite believe me after today."
    r "You mind keeping an eye on her? I really need to head on."
    ks "It's Kyou. And yeah, I'll stay with her."
    r grin "Good! And I expect you'll be watching us tomorrow, so I'll see you then~" with dissolve
    ks smile "Yeah, see you."
    hide Risa
    "As Risa walks on, I go to join Hiroko on her bench as she pinches the back of her leg." with dissolve
    show Hiroko tennis neutral at center:
        ypos 1.1
    ks surprised "Hey... are you okay? Didn't get injured, did you?" with dissolve
    h neutral_side "Nah, I didn't pull a muscle or nothing. I'm just fuckin' tired." with dissolve
    h sleep "Maybe I overdid it." with dissolve
    "She sighs, then looks to me."
    h nervous "Thanks." with dissolve
    ks neutral "It was nothing. Least I could do after fucking up your week."
    h sad_side "Oh, for sure. I almost didn't come out here today." with dissolve
    h tennis_headhold nervous "But how's that gonna look? My whole life's been building up to this, I ain't backing out now." with dissolve
    ks smile "For what it's worth, I think you're still gonna crush it."
    show Hiroko smile
    "She smirks." with dissolve
    h tennis_headhold2 "Dude, I get it. You're trying to make things right; I appreciate that." with dissolve
    h neutral_side "And I was thinking about all that stuff we did." with dissolve
    h nervous "Like, I dunno if you knew it, but you probably could've done all kinds of perv shit with me and gotten away with it." with dissolve
    h sleep "But I don't think you ever tried. Dunno if it even crossed your mind." with dissolve
    h nervous_side "I guess that's gotta count for something." with dissolve
    ks "So where does that leave us, do you think?"
    "She lets the question linger for a moment before she turns to look me in the eye."
    stop music fadeout 5.0
    h neutral "I dunno. Leaves us somewhere, tho'." with dissolve
    $ending = "trust"
    jump Epilogue_Con_Kyou_Hiroko

            # ks "That could work? But are you gonna be comfortable with me hypnotizing you again to find out?"
            # s "From what I know you can already turn off who I am with a word, so you have all the power here. I will agree to it."
            # ks "Okay. So I'll put you under briefly, try to make you take in every detail and bring you back out so we can talk about it."
            # "Sayori nods and gets comfortable on the couch"
            # ks "*Does brief induction scene with the penlight*"
            # s alert_sleep "*Quickly falls into trance*"
            # ks "And wide awake."
            # s alert_sleepy "Mmn... I understand a little more now."
            # ks "You do?"
            # s alert_neutral_right "Yes. Every time you passed the light across my eyes, it felt like my senses were all lighting up in turn."
            # s alert_surprised_right "I would describe the feeling as euphoric."
            # s "Perhaps the light is triggering the release of a large amount of dopamines and oxytocins in the brain and stimulating my motivation to stay focused on the light."
            # s "And such a chemical release might also shut down any resistance I have to the suggestions you are giving me, ensuring I trust you implicitly."
            # s alert_neutral "This is pure speculation on my part, and somewhat of a... hollywood explanation? But that is more or less what I consider has happened to me."
            # s "So you see, Kyou, this penlight of yours really seems to be bypassing a person's ability to reason."
            # s "People subjected to it will allow themselves to drop into trance and have whole facets of their being altered regardless of their own will and desire."
            # s alert_surprised_right "It is a literal brainwashing tool."
            # ks "Are you serious?"
            # s "Deadly serious. I told you, Kyou, I have been altered against my wishes and you need to take responsibility for that."
            # ks "I'm so sorry. I have to believe me when I say I had no idea I was doing that to you!"
            # s alert_smile_right "I believe you. And that's why I think I can trust you to do the right thing and set me back to how I was."
            # ks "Huh?"
            # s "I mean, bring me under one more time and make sure to undo your alterations. Both the personality and the sleep conditioning."
            # ks "So everything we did was for nothing?"
            # s "I am sorry, Kyou. There is also one more thing I would ask; that you destroy that penlight once you're finished, and remove any plans you may have drawn up so it cannot be remade."
            # "She wants me to lose everything I worked for. I know the penlight is dangerous, but..."
            # s "You know this is the right thing to do, Kyou."
            # menu:
            #     "Agree":
            #         ks "You're right. I know you're right."
            #         "I take up the penlight and nod at her, and she nods back as I pass the light across her eyes once more."
            #         ks "Taking you deep into trance... sleep."
            #         s alert_sleep "..."
            #         ks "You accept that you no longer have a second personality. [alt_name] is no more, nor will the words \"become [alt_name]\" have any effect on you when I say it."
            #         ks "Also... you will no longer be compelled to blank your mind completely when you try to sleep at night. What you do when you try to sleep is entirely up to you again."
            #         ks "Now wake up."
            #         s alert_neutral_right "Is it done?"
            #         ks "Yeah. I depgrogrammed you like you asked."
            #         s alert_smile_right "Thank you, Kyou. I admit I was scared you would be tempted to do otherwise. Now all that is left is to destroy the penlight."
            #         scene bg k bedroom eve
            #         show Sayori alert_neutral_right
            #         "Sayori watches with me as I dismantle the penlight, crushing the bulb for good measure before throwing all the parts in the bin."
            #         ks "It sure does suck to see all your hard work end up in the bin."
            #         s alert_concerned "I know, Kyou. And I am sorry that you had to do this. I do not think all your work was for nothing."
            #         ks "You don't?"
            #         s "Of course not! For one, your study of hypnosis is still relevant and useful. Just please use it as everyone else does from now on."
            #         s "And you also did help me realize how much I needed to go easier on myself."
            #         ks "Yeah?"
            #         s "Yes, Kyou. The difference I have felt from having a full night's rest has been phenomenal."
            #         s "I did not realize how badly I was limiting myself by not allowing myself to recharge properly."
            #         s "Your sleep trigger forced me to realize that. So even if it is now absent, I will ensure I make more time for myself to get a proper night's rest."
            #         ks "So where does that leave us?"
            #         s "Hmm..."
            #         s alert_smile_right "I will sleep on it and get back to you."
            #         jump Day5_Con_Kyou_Sayori
            #     " (disabled)Refuse":
            #         pass


    # n "And besides that, and I don't want to be rude or anything, but..." with dissolve
    # $nface = "concerned"
    # n "Do we really have anything else in common, besides hypnosis?" with dissolve
    # $kface = "surprised"
    # ks "Uh, well..."
    # $kface = "sigh"
    # ks "Maybe, maybe not..."
    # $kface = "smile"
    # ks "But I want to find out?"
    # n "Eh?"

    # $nface = "sigh"
    # n "But I can see it would be difficult if we're trying things of a... suggestive nature? And you have unrequitted feelings for me?" with dissolve
    # n "So I don't know, maybe we should call this whole thing off. It doesn't seem fair to you."
    # ks "I... I guess."
    # "Wait. Is it really going to end like this?"
    # ks "No, Nozomi, I... I don't think we have to stop everything."
    # $nface = "concerned"
    # n "No?" with dissolve




    # ks "Besides, I know for sure why it happened in the first place..."
    # "I take the penlight from my pocket and hold it out for all to see."
    # h "That's the thingy you were talking about, Nozo?"
    # n "Yeah. We used it to hypnotize me."
    # ks "I modified the beam to make it more... attention-grabbing? But after everything I have to admit it does more than that."
    # ks "It must be doing something more that I didn't consider. Something that silences the \"hidden observer\"."
    # n "It's too dangerous to use again."
    # ks "What?"
    # n "After everything that's happened, you know I'm right. You have to get rid of it."
    # "I hold the penlight up, regarding it as I sigh."
    # ks "I worked so hard on this. I realise it's dangerous, but do I really have to ditch it right now?"
    # ks "Don't we want to know why it does what it does? There could be a research project in this. Or- {w=1.0}{nw}"
    # h "YOINK!" with vpunch
    # "She just snatched the damn thing out of my hand!"
    # h "Just so you know, this is going in the fuckin' sea!"
    # ks "Goddamnit..."
    # s "If you want us to start trusting you, Kyou, this is a good first step."
    # n "I'm disappointed too, Kyou. But we need to be responsible. Who knows what would happen if we kept using that..."
    # ks "Yeah..."
    # "Everyone falls silent for a few moments, interrupted only by the sound of Hiroko slipping my penlight into her bag."
    # s "You {b}are{/b} going to destroy that thing, right?"
    # h "Of COURSE! Geez."
    # n "Well, anyway, I think we should give the hypnosis stuff a rest for now."
    # ks "Yeah..."
    # n "Please don't misunderstand; I'd want to go back to it soon, and do it properly."
    # n "But after what's happened I think it's best we cooled off a bit."
    # "I simply nod. I can't say I'm happy about all this, but she's right; we need to take a step back."
    # s "Sure. That sounds reasonable, Nozomi. I'm relieved."
    label Day6_Redemption:
        scene bg k bedroom day with longdissolve
        "I wake up bright and early the next morning."
        "Akiko called me after she was done with student council last night, and asked if I wanted to meet for breakfast..."
        scene bg shopping day
        with blink
        play music Inspiration
        "I'm a little nervous about it. I don't really know what she's expecting to get out of this."
        "And my head's still doing all sorts of loops, trying to process everything that's happened this week."
        "Ugh, why did I tell Akiko I was studying hypnosis, and WHY did I tell her I hypnotized my classmates?"
        "She's going to find out that I didn't tell the whole story. That I left out the part about my penlight."
        "That what I did to them was more than what anyone could expect from hypnosis..."
        show Akiko side casual noarmband smile
        a "Kyou! Over here!" with dissolve
        "B-but that's enough. I can't dwell on that right now."
        ks casual smile "A-Akiko!"
        "I need to focus."
        ks "How are you?"
        a casual_down happy "I'm good, thanks." with dissolve
        a laugh_wink "I could eat, though~" with dissolve
        scene AkikoBreakfast smile
        with blink
        play bgm2 Cafe loop
        "She's not wasting any time."
        show AkikoBreakfast akiko_up happy
        a "If I get these pancakes down me now, they'll have just enough time to settle before kendo practice." with dissolve
        ks casual confused "You're still doing kendo?"
        show AkikoBreakfast smile
        a happy "Yup! I have no time in school, but I belong to a weekend kendo club. I can train most weeks." with dissolve
        ks sigh "So that's why we're up this early in the morning."
        show AkikoBreakfast smirk
        a casual smirk "Not a morning person, Kyou? That's too bad." with dissolve
        ks sigh "Eh, whatever. I like to lay-in after a school week but it's fine."
        show AkikoBreakfast akiko_down worried
        a sad_side "Especially after the one you just had, huh." with dissolve
        ks "Yeah..."
        "I then smile to her as I add:"
        ks smile "At least my weekend's looking up."
        show AkikoBreakfast akiko_up happy blush
        "Akiko giggles as she breaks off a piece of pancake with her fork and takes a bite." with dissolve
        "She's definitely a lot cuter out of uniform, I have to say."
        show AkikoBreakfast embarrassed
        a laugh_wink "S-so anyway, let's talk about brains!" with dissolve
        "... Even if she's just as weird."
        show AkikoBreakfast smile
        ks "R-right... You said you're into psychology, didn't you?" with dissolve
        hide AkikoBreakfast
        show AkikoBreakfast akiko_up happy
        a casual_down smile "Yup! I like picking people's brains apart and finding out what they're about..." with dissolve
        ks "Picking people's brains apart?"
        "She shrugs."
        show AkikoBreakfast akiko_down smile_side
        a happy "Maybe that's a funny way to put it, I don't know. I've just always been interested in people and why they are the way they are~" with dissolve
        ks smirk "So is this why we're here? You're going to try taking me apart and finding out how I work?"
        show AkikoBreakfast smirk
        a smirk "Oh no, you got me~" with dissolve
        show AkikoBreakfast laugh
        a laugh_wink "But what's a conversation if you're not learning about each other?" with dissolve
        ks neutral "... Smalltalk?"
        show AkikoBreakfast annoyed
        a casual frown_side "Exactly." with dissolve
        "Her lips crinkle disdainfully before she regains her focus."
        show AkikoBreakfast smile
        a smile "So anyway, I've never met someone who knows hypnosis before." with dissolve
        ks smile "Oh... uh, really?"
        show AkikoBreakfast akiko_up neutral_side
        a "Well... I mean, there was this guy who was a year above us. He put on a hypnosis show at the culture festival last year." with dissolve
        show AkikoBreakfast quizzical
        a "Maybe you saw him?" with dissolve
        # a neutral_side "I... guess there was that guy at the culture festival last year. The one who put on that hypnosis show?" with dissolve
        ks neutral "I saw his show, yeah. But, what, you didn't talk to him?"
        show AkikoBreakfast neutral
        a casual_down neutral "I helped him organize a little, as part of my student council duties of course. But that was all, really." with dissolve
        ks "Huh. Why not?"
        "Another shrug."
        show AkikoBreakfast akiko_down neutral_closed
        a sleep "It felt so ridiculous to me. Getting people up in front of everyone and encouraging them to make dummies of themselves seems so cheap." with dissolve
        show AkikoBreakfast annoyed
        a smile "I'm interested in REAL hypnosis. The kind of thing that can make a difference to someone's life." with dissolve
        ks "Stage hypnosis is real, you know."
        show AkikoBreakfast surprised
        "Akiko's eyes widen incredulously." with dissolve
        a surprised "Huh? You're sure?"
        ks sigh "Of course I'm sure. Just because he used it for entertaining people doesn't mean they weren't hypnotized."
        ks "Some of the people who tried it were probably faking, but he certainly could have put someone in a genuine trance back then."
        show AkikoBreakfast neutral
        a neutral "Oh... I see." with dissolve
        "Akiko smiles slowly at me as her fork moves in to tear off another lump of her pancake."
        show AkikoBreakfast smile
        a smile "You've studied hypnosis for a year, you said?" with dissolve
        ks smile "Yeah, about that long."
        "I'm thinking to tell her that I took up hypnosis in the first place because of that culture fest show, but she's already moved on."
        show AkikoBreakfast happy
        a happy "You must be pretty knowledgeable by now, then. And you have some practical experience." with dissolve
        ks neutral "Y-yeah... Experience."
        show AkikoBreakfast akiko_up worried_side
        a sad_side "Right. Even if it didn't go down so well." with dissolve
        show AkikoBreakfast worried
        a neutral "So what did you do to hypnotize your classmates? How did it work?" with dissolve
        ks "A-ah, well..."
        "Shit. Of course she'd want to know more about that. What am I supposed to tell her? More of the truth?"
        show AkikoBreakfast quizzical
        a happy "Tell me if I'm being too nosy, but I'm just having a lot of trouble picturing it." with dissolve
        "I mean... Again, she's heard all those rumours so I need to tell her something. Just not everything."
        show AkikoBreakfast neutral
        ks neutral "O-okay, well I basically got them to focus on a light while I encouraged a hypnotic trance state by talking to them." with dissolve
        ks "And it worked. They listened, they looked up at the light and they seemed comfortable about being hypnotized."
        show AkikoBreakfast surprised
        a casual surprised "And then what happened?" with dissolve
        "I notice her leaning in slightly, her pancakes cooling in front of her as she ignores them for the sake of hearing me speak."
        "Her attention feels a little awkward, but I can't back out now."
        show AkikoBreakfast neutral
        ks sigh "Well... I basically gave them some simple suggestions to follow, and I guess they didn't take to them very well." with dissolve
        show AkikoBreakfast akiko_down quizzical
        a "What sort of suggestions?" with dissolve
        ks "Uh..."
        "I really don't want to talk to her about Hiroko, but I don't think I should lie. So..."
        ks "I... asked one of them how she felt about being my girlfriend."
        show AkikoBreakfast surprised
        a surprised "Really?" with dissolve
        a "That's... bold."
        "She prods her pancakes with a fork as she thinks for a moment."
        show AkikoBreakfast sigh
        a sigh "I guess the rumours about you are making a little more sense now." with dissolve
        ks "Yeah... I mean, I thought it would be okay. I wanted to impress her."
        show AkikoBreakfast neutral
        a neutral "Hmm... and what scared her about that situation, do you think?" with dissolve
        ks confused "Scared?"
        show AkikoBreakfast neutral_closed
        a sleep "You told me your classmates freaked out when you hypnotized them." with dissolve
        show AkikoBreakfast akiko_up worried
        a neutral_side "Was it that you put her on the spot by asking something so provocative?" with dissolve
        show AkikoBreakfast worried_side
        a neutral "Or maybe, because she felt she was in a position where she could speak uninhibited, she was considering an answer that surprised her?" with dissolve
        ks sigh "Man, I don't know, 'Kiko. Things got crazy after that."
        show AkikoBreakfast akiko_down worried
        a sad_side "Yeah..." with dissolve
        show AkikoBreakfast pancakes2
        $ renpy.transition(longdissolve, layer="master")
        "Akiko takes a moment to eat as she thinks over what I said."
        "I can just see that curious mind of hers trying to work things out."
        "Maybe she's trying to guess which of my former classmates I hit on? I didn't name names but she no doubt has some idea..."
        show AkikoBreakfast akiko_up sigh
        a sad "So... you tried to use hypnosis to ask people out and it blew up in your face." with dissolve
        "Ah. Figures she'd come to that conclusion."
        "Obviously I only did that to Nozomi, but this seems a bad time to correct her."
        show AkikoBreakfast neutral
        a sigh "And if people really think hypnosis is like the cartoons, it's not hard to see how they convinced themselves you were forcing them to date you or something." with dissolve
        show AkikoBreakfast annoyed
        a neutral "*sigh* Stupid. Brains really don't work like that." with dissolve
        ks "They really don't."
        show AkikoBreakfast akiko_down embarrassed
        a laugh "If you're going to manipulate someone you need to be more subtle than that, haha~" with dissolve
        ks surprised "Wait, what?"
        show AkikoBreakfast worried_side blush
        a sad_side blush "Um, n-nothing. Just trying to break the tension a bit, that's all." with dissolve
        "She's uncomfortable hearing this about me. She has to be."
        hide AkikoBreakfast
        show AkikoBreakfast akiko_down neutral_closed pancakes2
        a neutral noblush "But I have to say this isn't a good look for you, Koyama." with dissolve
        ks sigh "Agh..."
        show AkikoBreakfast akiko_up worried
        a neutral_side "I don't know what you were thinking, but that's just not a good way to ask someone if they like you." with dissolve
        show AkikoBreakfast sigh
        a sigh "Of COURSE they were going to react badly!" with dissolve
        ks "Yeah, I get it. Sorry."
        show AkikoBreakfast neutral
        a sleep "I hope you've learned your lesson, anyway. You really should've been more careful." with dissolve
        show AkikoBreakfast akiko_down surprised
        stop music
        ks "I KNOW, alright? I really wish I could take it back, but I can't." with dissolve
        ks "I never should've scared them like that. I never thought I'd do that to them..."
        show AkikoBreakfast worried
        ks "But it's too late now. I tried to apologize, but they won't even look my way, so... s-so..." with dissolve
        show AkikoBreakfast worried_side
        a casual_down sad_side "That's okay, Kyou. I believe you." with dissolve
        show AkikoBreakfast sigh
        a sigh "And I said I wasn't going to judge, so I'm sorry too." with dissolve
        "Man, this is awkward. She must be every bit as uncomfortable as I am about where this conversation's headed."
        show AkikoBreakfast akiko_up neutral_side
        "What do I do now?" with dissolve
        "Maybe we should call this thing off. Quit while I'm ahead..."
        play music Inspiration
        show AkikoBreakfast smile
        a smile "Okay. Let's back up a bit." with dissolve
        ks neutral "Hm?"
        show AkikoBreakfast akiko_down
        a smile_side "You said you hypnotize people with a light. How does that work?" with dissolve
        "She's just going to continue?"
        ks surprised "Oh, well..."
        "Okay, then. I'll just tell her what she wants to know."
        ks neutral "So the idea is, hypnosis is about entering a state of focused attention. So I was using the light as a way of directing their attention to where I wanted it."
        ks "And while they're focusing on that, giving all their conscious thought to the light, I'm speaking to them, and my words find their way into their subconscious."
        show AkikoBreakfast akiko_up quizzical
        a casual neutral "Their subconscious?" with dissolve
        "I smile as Akiko starts to lean in again, as if she'd already banished our unpleasant interlude from her mind."
        ks smile "Y-yeah! Their subconscious starts to take it in, and you can use it to suggest they're getting sleepy and hypnotized, and after that..."
        ks "Well, after that the real fun begins."
        show AkikoBreakfast smirk
        a smirk "That's when you ask them to be your girlfriend." with dissolve
        show AkikoBreakfast worried_side blush
        a sad_side blush "... Bad joke, sorry." with dissolve
        ks sigh "But yeah, that's when you can give their subconscious suggestions to follow."
        hide AkikoBreakfast
        show AkikoBreakfast akiko_up happy pancakes2
        a neutral noblush "Such as making them cluck like chickens, or..." with dissolve
        ks neutral "Getting them to drop a bad habit."
        "Akiko nods."
        show AkikoBreakfast smile
        a smile "Like smoking. I know some people get hypnotherapy for that." with dissolve
        ks smile "Exactly."
        show AkikoBreakfast akiko_down
        a neutral_side "What do they do to stop people smoking? Do they just tell their subconscious to quit and their conscious mind follows through?" with dissolve
        ks "I think it's more like... trying to ascribe a negative feeling to picking up a cigarette. Telling them to feel a really bad taste in their mouths... stuff like that."
        show AkikoBreakfast surprised
        a surprised "And that really works?" with dissolve
        ks "Of course! Maybe not for everybody, but some people find it really useful."
        show AkikoBreakfast smile
        "She smiles in understanding, cutting up another piece of her pancake which has surely gotten cold by now." with dissolve
        a "It really does sound like a useful tool for a therapist to have."
        "She really does seem invested. Like she might be willing to do more than just talk about this stuff..."
        ks "Maybe... you'd like to see what it's like yourself?"
        show AkikoBreakfast akiko_up quizzical
        a casual_down surprised "What it's like to hypnotize people?" with dissolve
        ks neutral "... I was thinking more what it's like to BE hypnotized."
        show AkikoBreakfast embarrassed blush
        a laugh_wink blush "Oh... r-right, haha~" with dissolve
        show AkikoBreakfast happy
        a smile_side noblush "I mean... well, I'm not against it in principle, now that I think about it. It could be interesting." with dissolve
        hide AkikoBreakfast
        show AkikoBreakfast akiko_down smile pancakes2
        a smile "But I need to get ready for kendo soon." with dissolve
        ks neutral "Oh... when does that happen?"
        show AkikoBreakfast neutral_side
        a neutral_side "A couple hours. I have to head home quick to grab my gear, so I need to go before then." with dissolve
        ks smile "So... at least an hour, right? We can work with that."
        show AkikoBreakfast quizzical
        "Akiko looks to me quizzically, having given up all pretense of trying to eat any more." with dissolve
        ks "We could try something at my house. It's only a little ways from here, and there'll be no noise to distract us there so I could give you a really good example."
        show AkikoBreakfast embarrassed blush
        a surprised "W... {w=1.0}{nw}" with dissolve
        $ renpy.transition(dissolve, layer="master")
        extend laugh blush "w-wow, hahaha!"
        ks surprised "What?"
        show AkikoBreakfast smirk
        a "You know I don't believe the rumours but still... the scariest guy in school wants me to follow him to his house?" with dissolve
        a "I feel like I should be a little worried."
        ks sigh blush "A-ah, come on, it's nothing like that!"
        show AkikoBreakfast laugh
        "Man, I wasn't even thinking about how it'd look, and for her part Akiko giggles nervously." with dissolve
        stop music fadeout 5.0
        stop bgm2 fadeout 5.0
        show AkikoBreakfast akiko_up happy
        a laugh_wink noblush "Well, alright then~ We'll talk more on the way..." with dissolve
        $persistent.akiko_breakfast_unlock = True
        scene bg k room day
        show Akiko side casual_down noarmband neutral_side
        with blink
        "And that's how our student council president agreed to follow me home."
        ks casual smile "S-so, uh, here we are."
        queue music Downtown
        show Akiko smile
        "Akiko smiles as she lines her sneakers up by the door and steps into the living room with me." with dissolve
        a "Oh, this is nice~"
        scene cg k room day
        show AkikoHypno upright smile
        with blink
        "She gives the room a cursory look, but is quick to take a seat on my couch."
        "Once again, she's not wasting any time."
        ks casual smile "Alright, so we'll get straight to it. Are you comfy?"
        "I watch as she leans back on the couch, settling into it before giving me an affirming smile."
        show AkikoHypno happy
        a happy "Very!" with dissolve
        ks "Okay, great. So Akiko, I'd like you to focus on..."
        "I pause a moment. This is normally the part where I'd show her the penlight..."
        show AkikoHypno neutral
        "But after everything that happened last week, I really need to take a different approach if I'm going to keep doing this stuff." with dissolve
        ks "The picture above the TV."
        show AkikoHypno surprised
        a surprised "Oh... right, okay." with dissolve
        show AkikoHypno neutral_up
        "I can tell that surprised her a little bit. She must have been expecting the light after all my talk about it back at the restaurant." with dissolve
        ks "I thought I'd try something a little different with you. No lights this time."
        show AkikoHypno smile
        a smile "Sure. Well, you know what you're doing~" with dissolve
        "I smile back at her and nod, as I take out my phone and open up the list of hypnosis scripts I have written in there."
        show AkikoHypno neutral
        "So, the plan is I show her how she can be hypnotized, then give her a little re-induction trigger just to show her how it feels to be under a hypnotic influence." with dissolve
        "That's what we agreed on the way here."
        stop music fadeout 15.0
        ks "So yes, focus your eyes on a point on that picture. Pick a tree and really start taking it in. The leaves, the branches..."
        show AkikoHypno neutral_up
        "I notice her eyes fix towards the wall as I scroll down and... yes, this should do." with dissolve
        "It's quite simple and if she's taking it as seriously as she seems to be, I think she'll get a good experience here."
        ks "That's right. Really take in every detail. And as you do so, I'd like you to do something else."
        show AkikoHypno neutral_up_talk
        a "Mm, what's that?" with dissolve
        show AkikoHypno neutral_up
        ks neutral "I'd like you to start reciting the alphabet backwards. Just taking your time, but trying to remember each letter in sequence and saying them out loud." with dissolve
        "Akiko nods slightly, her eyes still focused on the wall."
        play music Night_Road fadein 15.0
        show AkikoHypno neutral_up_talk
        a "Um, sure. So it's... zee." with dissolve
        "Smiling as she co-operates, I get ready to start reading out my script to her while she slowly works her way down the letters."
        a "Why..."
        show AkikoHypno neutral_up
        ks "That's right, very good." with dissolve
        "I say that first line mostly to get a feel for my hypnotist voice, lowering it a little from my usual speaking volume but still trying to mouth my words clearly."
        show AkikoHypno say_ee
        a "Er, ecks..." with dissolve
        ks "Just moving back down the alphabet, nice and slow, remembering the letters."
        show AkikoHypno say_oh
        a "Double-you..." with dissolve
        ks "Picturing each one go by in your mind. The letter you need appears, you speak its name, then it gives way to the next..."
        show AkikoHypno say_ee
        a "Vee..." with dissolve
        ks "All while keeping your eyes nice and attentive to the..."
        show AkikoHypno say_oh
        a "You..." with dissolve
        show AkikoHypno neutral_up
        "I have to pause a moment. My script doesn't say anything about the picture on the wall because I'm improvising here." with dissolve
        ks "The tree. Taking in all that you see so clearly, so vividly. Finding it easy to let everything else fall away..."
        show AkikoHypno say_ee
        a "... Tee." with dissolve
        ks "And as you find everything else drop..."
        a "Ess..."
        ks "You may also realize how pleasant it is to watch it all go. How relaxing it feels..."
        show AkikoHypno say_ah
        a "Arr..." with dissolve
        ks "How nice and soothing it is to watch the tree. To speak the letters..."
        show AkikoHypno say_oh
        a "Cue..." with dissolve
        ks "And to listen to my voice. Watching. Speaking. Listening."
        show AkikoHypno say_ee
        a "Pee..." with dissolve
        ks "Everything else dropping away. And perhaps even more now."
        show AkikoHypno say_oh
        a "Oh..." with dissolve
        ks "With each letter you speak, you may now find yourself struggling to visualize the next letter. How that too may start to drop from your relaxed mind."
        show AkikoHypno say_ee
        a "Enn..." with dissolve
        ks "You may even find watching the tree a struggle."
        a "Emm..."
        ks "How your eyelids may begin to drop. Becoming more relaxed. Finding with every blink how much easier it is to close your eyes than open them."
        a "Ell..."
        show AkikoHypno neutral_up
        "I haven't done this with anyone before, but this is starting to worry me." with dissolve
        ks "And that's okay, Akiko. It's okay."
        ks "If you find your eyes are becoming heavy, your mind becoming sleepy, it's perfectly acceptable to embrace that feeling as you relax even deeper."
        show AkikoHypno say_ah
        a "Kay..." with dissolve
        show AkikoHypno neutral_up
        "She should be struggling by now. Finding it harder to recall the letters, or keep her eyelids open." with dissolve
        "And it's not like she isn't trying. It looks like she's doing everything I'm asking of her."
        show AkikoHypno say_ah
        a "Jay..." with dissolve
        show AkikoHypno neutral_up
        "But I'm running out of fucking letters here and she's not... this isn't working!" with dissolve
        "So what if... what if I used the penlight on her? Just a little, to facilitate her dropping into trance..."
        "I think that would be okay. Just a couple flashes of the light may be all I need to help her achieve a hypnotized state."
        show AkikoHypno neutral_up_talk
        a "Eye..." with dissolve
        show AkikoHypno neutral_up
        "This seems like a good reason to use it. I'm not going to do what I did to Hiroko, for fuck's sake! I want her to enjoy this experience." with dissolve
        "And I have the penlight right here in my pocket still. I could do this..."
        show AkikoHypno say_ah
        a "Aitch..." with dissolve
        show AkikoHypno neutral_up
        "But if I'm doing it, I need to do it right now." with dissolve
        menu:
            "Use the penlight to help things along":
                show penlight at right with moveinright:
                    ypos 0.346
                "Just a couple of flashes."
                hide penlight at right with moveoutright
                $light_x = 0.4; light_y =0.26
                call cglightshow
                show AkikoHypno surprised_up
                a "G- a-ahh what was..." with dissolve
                ks "Don't worry, Akiko, it's just the light I was talking about. Keep trying to recall the letters."
                "A couple of flashes to help her along, that's all."
                a "But I thought..."
                "And then I'll just improvise the rest of the induction. I can do it."
                show AkikoHypno neutral_up_talk
                a "W-well okay... Gee..." with dissolve
                call cglightshow
                ks "But as I said, you may begin to find it so much harder to recall those letters..."
                call cglightshow
                ks "Even as you might now be seeing a pattern appear before your eyes while you remain focused on that tree..."
                show AkikoHypno confused
                a "E... e-eff..." with dissolve
                call cglightshow
                ks "And if you find yourself forgetting the letters. If you find your focused eyes are growing tired, your eyelids heavy, then..."
                call cglightshow
                show AkikoHypno sleepy
                $ renpy.transition(longdissolve, layer="master")
                a "D... d-dee?"
                ks "... Then that's okay, Akiko. Perfectly fine if the next letter fades from your mind as you drift deeper into relaxation."
                "It takes a little conscious will for me to switch the penlight off and return it to my pocket again. Nearly got carried away there."
                ks "But try and recall the next letter. Even if the more you try, the more you might now find it impossible to recall right now."
                a "Eehh..."
                ks "Even if the more you try to recall the letter, the more you feel the pull on your eyelids grow heavier and heavier..."
                stop music fadeout 15.0
                a "I... c-can't..."
                ks "The more you simply allow them to close and let your conscious mind drift away, as your entire body can relax..."
                show AkikoHypno sleep
                $ renpy.transition(longdissolve, layer="master")
                a "..."
                ks "And enter a deep state of trance as you inevitably..."
                show AkikoHypno drooping sleep
                $ renpy.transition(longdissolve, layer="master")
                queue music Flow
                ks "Sleep."
                "Akiko, having seemed completely lucid barely a minute ago, exhales quietly as her head falls gently forward."
                "So... I did it."
                "Maybe it counts as cheating, but I made sure not to expose her to the light as much as I did with the other girls."
                "And I may not know exactly how this thing works, but I have to believe the lighter touch merely helped her into trance and didn't seriously affect her will."
                "Even so, I'll be doubly careful with her. There's no way I'll hurt her by accident like Nozomi, and treating her like I did Hiroko is the absolute last thing I want."
                "No, we're going to do exactly as we agreed. I'll give her a short, pleasant experience of hypnosis and she'll leave here feeling good about the whole thing."
                "She's going to enjoy this."
                ks "That's right, Akiko, going all the way down now. Letting all the tension free from your body as you fall deeper into this nice, relaxing state of hypnosis."
                ks "Relaxing all the way, Akiko. Just allowing yourself to go deeper and deeper into hypnosis... That's right."
                "Now to think... we agreed on a re-induction trigger, but not on what form it should take. So what should I do?"
                "Akiko kept talking about how hypnosis isn't like what you see in cartoons, and she's right about that."
                "But if she associates those cartoony things with hypnosis as much as she seems, then that's something I could work with..."
                ks "So now that you're in this pleasant, deep state of hypnosis I'd like to return to what we were talking about on the way here."
                ks "About how we were going to give your subconscious something that would allow you to go straight back to this state of hypnosis you find yourself in now."
                ks "Do you remember, Akiko?"
                a "Mhm..."
                ks "And would you still like me to do this? Just to show you what it's like?"
                show AkikoHypno sleeptalk
                a "Mn... yes." with dissolve
                show AkikoHypno sleep
                ks smile "That's wonderful, Akiko." with dissolve
                "I smile at her muted reply as I tap my phone to start searching for a particular kind of app. I'm sure it won't be hard for me to find."
                ks "So from now until as long as you want to, whenever you see a moving spiral pattern while in my presence you will feel an irresistable urge to stare into the spiral."
                ks "And while you stare you may find yourself falling straight back into this deep, pleasant state of hypnosis you find yourself in now."
                ks "Perhaps even deeper into hypnosis. The more you stare into the moving spiral in my presence, the deeper into hypnosis you will go. Do you understand?"
                show AkikoHypno sleeptalk
                a "Yes..." with dissolve
                show AkikoHypno sleep
                "Akiko breathes her answer in the affirmative. It's all going smoothly so far." with dissolve
                "That brief flash of the penlight really turned things around..."
                ks "That's great, Akiko."
                "Of course I'm worried about that, but... yeah. I'll be careful with her. Of course I will."
                "Akiko's the only girl... hell, the only person in school who'll give me the time of day now."
                ks "So in a few moments you're going to feel wide awake and refreshed as I bring you up from this pleasant state of hypnosis you're experiencing."
                "I WON'T fuck this up!"
                ks "Wide awake on the count of five. One, two, three..."
                ks "Four and... {w=1.0}{nw}"
                play sound fingersnap
                show AkikoHypno sleepy
                stop music fadeout 3.0
                $ renpy.transition(longdissolve, layer="master")
                extend "five. Wide awake now, Akiko."
                "Akiko's eyelids open to the sound of my snapping fingers."
                a "..."
                queue music Downtown
                show AkikoHypno upright surprised
                a "H-huh?! Kyou?!" with dissolve
                ks "Wide awake and alert. Welcome back."
                show AkikoHypno confused
                "Akiko frowns as she looks to me. For a moment it seemed as if she was confused as to why I said that to her." with dissolve
                a "You... you mean it worked?"
                ks "You seem surprised."
                "She holds my gaze for a moment before a quiet smile spreads across her lips."
                show AkikoHypno happy
                a "... Yeah, I guess I am." with dissolve
                a "I was trying to focus on saying the letters and staring at that tree picture above the television, just like you wanted."
                show AkikoHypno neutral
                a "And I don't know... I guess my eyes were feeling a little strained from all that staring. And I heard you saying some things while I was doing that." with dissolve
                a "I didn't know what to make of it, so I just kept saying the letters. Only all of a sudden I saw this light pass across my eyes and then..."
                show AkikoHypno frown
                "She purses her lips for a moment." with dissolve
                a "And then it's like I suddenly understood."
                "So the light from my penlight really did make a difference. At the very least it accelerated the process of putting her into trance, just as I suspected."
                "Maybe if I had longer. Maybe if I'd asked her to repeat the alphabet exercise again, she might have begun to fall into trance without my light."
                show AkikoHypno sleep
                a "So that's what hypnosis feels like..." with dissolve
                "But I'll have time to think on this later."
                ks "Yeah. What do you think?"
                "Right now I need to focus on Akiko and her immediate needs."
                show AkikoHypno smile
                a "It's interesting~" with dissolve
                a "If I had to compare it to something, it's a little like when I'm meditating. Except this felt a lot more... pleasant? Somehow?"
                ks "Would you like to experience it again? We still need to try that re-induction trigger we agreed on."
                show AkikoHypno surprised
                a "Oh... right, how does that work?" with dissolve
                $persistent.k_room_akiko_2_unlock = True
                scene RedemptionPhoneDay quizzical_up_sp glasses_sp kyou_phone with blink
                a "I mean, it seems a little far-fetched to put someone back into hypnosis right..."
                show RedemptionPhoneDay surprised_sp
                $ renpy.transition(longdissolve, layer="master")
                a "R-right away..."
                "With a chuckle, I hold up my phone with a rotating black spiral pattern displaying prominently on its large OLED screen."
                "This was the app I was looking for a few minutes ago. Just a simple thing made purely for a novelty purpose."
                show RedemptionPhoneDay quizzical_sp
                $ renpy.transition(longdissolve, layer="master")
                "But for Akiko in this moment, it may be more than just a novelty..."
                ks casual smile "Just keep staring into the spiral, Akiko. And if you want it to, the spiral will relax you and take you deeper."
                show RedemptionPhoneDay tired_sp
                $ renpy.transition(longdissolve, layer="master")
                a "A s... a spiral?"
                stop music fadeout 10.0
                ks "Yes. You're staring at a moving spiral pattern while in my presence. And the more you stare, the more you want to go..."
                a "..."
                ks "The more you want to go..."
                show RedemptionPhoneDay blanktalk_sp
                $ renpy.transition(longdissolve, layer="master")
                queue music Flow
                a "Deeper..."
                ks "Deeper... that's right."
                show RedemptionPhoneDay blank_sp
                $ renpy.transition(longdissolve, layer="master")
                "I could see the little contortion of her lips as she stared. Like she was about to say how silly it was that I'm showing her something like this."
                "And yet she couldn't help herself from leaning in curiously. Couldn't help but stare into it with those inquisitive blue eyes of hers."
                "Couldn't help from giving this silly spiral every last ounce of her concentration."
                "It really is a cartoonish setup, but clearly one that she's now become fully invested in."
                ks "So very deep, Akiko, into this nice, pleasurable hypnotic state once again."
                "I leave the phone in front of her face a few moments more as I let her stare in silence..."
                show RedemptionPhoneDay blank glasses kyou
                $ renpy.transition(longdissolve, layer="master")
                "... before pulling it away from her without warning, just to see how she'll react."
                a "..."
                "Nothing. Without the spiral to gaze upon, it seems her focus turns inward to the trance she finds herself returned to."
                "Her eyes now stare blankly into the empty space where the phone used to be."
                "The more I see her like this, the more I'm reminded of Hiroko... staring emptily back at me in that alley..."
                "No. This is different. It HAS to be different..."
                ks frown "B-but remember, Akiko. This effect my spiral has on you will only last for as long as you want it to. Always remember that."
                ks "If you ever find yourself staring at a moving spiral and don't feel comfortable to fall deep into this state of hypnosis as you are now..."
                "She may be a little under the influence of this penlight of mine, but I'll make sure she'll always be the one in control of her responses."
                ks "... you will find you can simply choose not to let it hypnotize you. As if you were staring at any other kind of image."
                ks "You can never become hypnotized unless you WANT to become hypnotized... Understand, Akiko?"
                show RedemptionPhoneDay blanktalk
                $ renpy.transition(longdissolve, layer="master")
                a "Yes... Understand..." with dissolve
                show RedemptionPhoneDay blank
                "That's how it's going to be different." with dissolve
                ks neutral "Very good, Akiko. And now we're going to bring you out of this wonderful state of trance on a count of three."
                ks "{cps=15}One... two, and... {/cps}{w=0.5}{nw}"
                play sound fingersnap
                show RedemptionPhoneDay surprised
                stop music fadeout 10.0
                $ renpy.transition(dissolve, layer="master")
                extend "three."
                queue music Inspiration
                "Awareness seems to return to Akiko's face on the very moment I snap my fingers in front of her once again."
                show RedemptionPhoneDay tired
                a "W-... w-wow. Did that really happen?" with dissolve
                a "You put that silly spiral in front of me and I just... I didn't even think about it, I just..."
                ks smile "Went straight back into hypnosis."
                show RedemptionPhoneDay quizzical_up
                a "Yeah..." with dissolve
                "I watch as Akiko seems to be working up to asking me something."
                $persistent.redemption_phone_day_unlock = True
                scene cg k room day
                show AkikoHypno upright neutral
                with blink
                a "So is it... do you mean to tell me hypnosis really IS like the cartoons?"
                ks casual smile "Ah, w-well it really isn't. But here's the thing with hypnosis: We can make a trigger out of pretty much anything."
                ks "An object. A spoken phrase. A part of the body, like my finger or my eyes... Even a smell could work."
                show AkikoHypno confused
                a "But you chose a spiral?" with dissolve
                ks "Well, yeah! It's pretty cliché, but spirals really are good for focusing someone's attention on a singular point so they can be useful for real hypnosis."
                a "Hmm..."
                ks "Plus people associate them with hypnosis anyway, like you do."
                ks "So when I made the suggestion that it would hypnotize you, it wasn't hard for it to take hold in your imagination, was it?"
                show AkikoHypno frown
                a "I guess not..." with dissolve
                ks "So all I really did was strengthen that association and let your mind do the rest."
                show AkikoHypno confused
                ks "And when it comes down to it, it really is all down to your mind. Only you can decide whether it works or not." with dissolve
                ks "You could just as easily have ignored what I was doing, unlike whatever cartoon characters you're thinking of."
                ks "But be honest with me here. When I took out my phone and put that spiral in front of you... you WANTED it to work, didn't you?"
                show AkikoHypno sleepy blush
                a "Ah, well... y-you see..." with dissolve
                ks "Right?"
                show AkikoHypno happy
                a "E... e-eheh~" with dissolve
                "I don't even need her to answer that. It's written all over her sheepish face."
                show AkikoHypno smile
                a "Okay, Kyou. You're right~" with dissolve
                a "I mean, after how pleasant it was the first time, I really wanted to believe you could do it. Even if was with a silly spiral."
                ks smirk "Heh. Maybe you're a cartoon character yourself."
                show AkikoHypno happy
                a "Ahaha, stop~" with dissolve
                show AkikoHypno smile noblush
                a "But it was such a unique experience." with dissolve
                show AkikoHypno surprised
                a "Like... the spiral was so vivid in my mind's eye. Every bit as real as the one you put in front of me." with dissolve
                a "I think... if you told me just now that hypnosis really was exactly like people seem to think it was, I would've believed you!"
                ks smile "I'm just happy you liked it, Akiko."
                show AkikoHypno happy
                a "Yeah!" with dissolve
                $persistent.k_room_akiko_3_unlock = True
                scene bg k entrance day
                show Akiko side casual_down smile noarmband at center
                with blink
                "Akiko and I enjoy the moment in silence before she makes a move to leave and I walk her to the door."
                a "Anyway thanks for this, Kyou. It was really interesting~"
                ks casual smile "Interesting enough to try it again, maybe?"
                a casual happy "Maybe. Ask me again when the culture festival's over." with dissolve
                "She hums to herself as she steps into her sneakers."
                stop music fadeout 5.0
                a smile "I'll see you in class, okay?" with dissolve
                scene bg k bedroom eve with blink
                queue music Past_Sadness
                "So Akiko left for kendo practice in a great mood, happy for the morning she spent with me."
                "But ever since I've been thinking about my decision to use the penlight on her..."
                scene RedemptionPhoneDay blank glasses kyou:
                    matrixcolor SaturationMatrix(0)
                with blink
                "I can't get that blank-eyed stare of hers out of my head."
                "Of course I want to think that Akiko was just that into being hypnotized, but she really seemed like she was a little TOO out of it."
                scene bg k bedroom eve with blink
                "Still, though... I made sure to tell her in trance, over and over, that the decision to fall into hypnosis is always hers."
                show penlight at right with moveinright:
                    ypos 0.346
                "So she'll be fine. And I'll never use the penlight on her or anyone else ever again."
                "Yeah, into the desk drawer with you..."
                hide penlight at right with moveoutright
                stop music fadeout 5.0
                scene bg blackscreen with longdissolve
                "I'm going to do things completely on the level from now on..."
                pause 2.0
                jump Day8_Redemption_Spiral
            "Carry on without the penlight":
                ks "Perfectly fine if everything continues to drop away from your relaxed, sleepy, conscious mind."
                "No, I'll just... stick to the plan."
                show AkikoHypno say_ee
                a "Gee..." with dissolve
                ks "Thoughts dropping."
                a "Eff..."
                ks "Eyes dropping."
                a "Eee..."
                ks "Letters dropping."
                a "Dee..."
                ks "Allowing it all to fall away."
                a "See..."
                ks "As you drop irresistibly into..."
                a "Bee..."
                ks sigh "... Sleep."
                stop music fadeout 5.0
                show AkikoHypno say_ah
                a "Ay..." with dissolve
                "Goddamnit."
                show AkikoHypno say_oh
                a "... Omega." with dissolve
                "I just don't understand. Why didn't it work?"
                play music Downtown
                show AkikoHypno confused
                a sad "Um... Psi?" with dissolve
                ks surprised "Uh, wait, what are you doing?"
                a "Or was it... {w=1.0}{nw}"
                show AkikoHypno surprised
                $ renpy.transition(dissolve, layer="master")
                extend surprised "huh?"
                show AkikoHypno confused
                a casual sad_side "Oh... I ran out of letters, so I didn't know what you wanted me to do..." with dissolve
                show AkikoHypno sad
                a sigh "So I thought, why don't I try a different alphabet? Now THAT's hard!" with dissolve
                "Man, if she's even thinking to try that I've REALLY fucked this up."
                ks sigh "Ah, it's fine. You can stop now."
                show AkikoHypno noglasses sleep
                "Akiko takes a breath and sighs as she pulls the glasses from her face before rubbing her eyes." with dissolve
                show AkikoHypno irritated
                a sigh "Something tells me that didn't go like you wanted." with dissolve
                ks neutral "You're right. I'm not sure what went wrong."
                show AkikoHypno neutral glasses
                "My mind's racing as I sit beside her, while she slips her glasses back on and looks to me." with dissolve
                "What to do..."
                ks "Okay, can you tell me what was going through your head during all that?"
                show AkikoHypno sleep
                a sleep "Uh, sure. Let me think..." with dissolve
                show AkikoHypno frown
                a sigh "Well... I could feel my eyes were getting tired and a little dry, because I was staring at that picture for so long." with dissolve
                show AkikoHypno confused
                a neutral "And I think you were saying I'm supposed to picture the alphabet in my head?" with dissolve
                ks "Uhh..."
                "I quickly bring up my phone and flick through my script."
                ks "Yeah, that's right."
                show AkikoHypno surprised
                a casual surprised "You wrote it down? Can I see?" with dissolve
                "I look at her as she makes a move for my phone, and she takes my passivity as permission to pull it from my fingers as she looks at the screen."
                show AkikoHypno neutral
                a neutral "Hmm... yeah, so I couldn't picture the letters at all. It was annoying me so I stopped trying and just kept saying the letters." with dissolve
                ks frown "Oh... really?"
                show AkikoHypno smile
                a smile "Yup! And I wasn't very interested in that tree either. I still looked at it, though." with dissolve
                show AkikoHypno frown
                "Akiko then taps her finger on a part of the text she's reading off my phone." with dissolve
                a "And... see here, when you started talking about relaxing and getting sleepy, that felt nice to listen to."
                show AkikoHypno sad
                a sad "But I don't know. I didn't really want to sleep on your couch just because you told me to." with dissolve
                "She hands me my phone back and lets out another sigh."
                show AkikoHypno smile
                a casual_down sigh "It was interesting, don't get me wrong, but I don't really understand how it's supposed to work. Sorry." with dissolve
                "I sigh in return, defeated."
                ks sigh "Yeah, it's not your fault. Thanks for letting me try it."
                $persistent.k_room_akiko_1_unlock = True
                scene bg k room day
                show Akiko side casual_down noarmband smile at center:
                    ypos 1.2
                    linear 2.0 ypos 1.0
                with blink
                "Akiko smiles as she stretches up from the couch."
                show Akiko:
                    ypos 1.0
                a "Maybe I just can't be hypnotized~"
                ks casual sigh "Ah, th-that's not it. I just..."
                "I'm just not that good a hypnotist after all."
                "Not without my penlight."
                a casual laugh_wink "Well hey, at least I can say the rumours about you were greatly exaggerated!" with dissolve
                ks surprised "Huh?!"
                a sad "Uh, about you hypnotizing girls to sleep with you?" with dissolve
                ks sigh "Oh, right. Yeah."
                "Damn. She's trying to encourage me, but that's just a kick to the gut."
                a smirk "I was only a little worried about that, just so you know." with dissolve
                stop music fadeout 5.0
                a happy "Anyway, I should get ready for kendo practice now, so I'll see you at school?" with dissolve
                scene bg k bedroom eve with blink
                play music Past_Sadness
                "All that study of hypnosis I did. The effort I put into applying what I learned into writing these hypnosis scripts..."
                "Talking in front of a mirror to get my hypnotic patter right. All to help prepare for times like this."
                "But when it came down to it..."
                show penlight at right with moveinright:
                    ypos 0.346
                "Was this the only thing that mattered?"
                scene bg blackscreen with longdissolve
                pause 2.0
                stop music fadeout 5.0
                jump Day8_Redemption

label Day6_TennisBot:
    scene bg k bedroom day with longdissolve
    "I find myself waking up the next morning bright and early."
    "It's not what I normally do on a weekend, but I've had a lot on my mind."
    play music Downtown
    "Well okay, I've had Hiroko on my mind."
    "She dealt with the Nozomi situation yesterday, I hope. And I know she needs to practice for that tournament tomorrow; [hypno6] or not."
    "I should... yeah, I'll go easy on her today. Let her be herself."
    "And as for me, I have tons of stuff I could be doing without her. There's a mock entrance exam to study for; I should probably get on that."
    "Yeah. Yeah, let's forget about Hiroko for a while..."
    with longblink
    "... With a groan, I shift myself from my desk as I snap my textbook shut."
    "That's most of the morning gone and I've read as much about algebra as I can stand. I need a goddamn break."
    "Time for lunch, and... hell, I wonder how Hiroko's doing without me."
    show phone at right with moveinright:
        ypos 0.346
    "... It'd be okay just to check on her. Give her a call, see how she's doing."
    h "..."
    ks casual "Hiroko?"
    h "..."
    "Hmm, nothing. The call definitely connected."
    "In accordance with her programming, Hiroko's only meant to leave her phone unattended for very specific reasons."
    "Likewise she can only take her inner-ear headphone out while she showers or while she's recharging it as part of her \"nightly maintenance\"."
    "So... right. Of course I don't hear anything."
    "Her phone might auto-connect, but the [hypno6] herself is probably out there on the tennis courts. Probably out of bluetooth range too, so she can't hear me."
    "I guess that's... good. That's the only reason she's not responding."
    "Well, she has to come back into range some time, so... I'll stay on the line while I find some lunch."
    scene bg k kitchen day
    show phone at right:
        ypos 0.346
    with blink
    "Now let's see... I'll put my phone on speaker and leave it here while I check out what we've got in the fridge."
    "Hmm. I suppose I could warm up those leftovers..."
    $risa_name = "???"
    r "{size=18}I just don't believe you.{/size}"
    "What the?!"
    r "{size=18}How're you pulling off those kinds of moves? You've barely played all week.{/size}"
    "Ah, someone's gotten close to Hiroko's phone, but it's definitely not her voice I'm hearing. Who the hell is that?"
    h "{size=18}Oh, y'know. I've been, like, studying.{/size}"
    "THAT'S Hiroko. Sounds like they're outdoors, so I guess that other girl is someone she's practicing with?"
    r "{size=18}Studying? Really?{/size}"
    "Anyway, let's forget about lunch for a second; I want to listen to this..."
    scene bg court day
    show Hiroko tennis neutral_side at center
    show Risa tennis_armup wristband_right_armup smug_side at center, flip:
        xpos 0.25
    with blink
    r "That'd be a first."
    h smile_side "Seriously. Anytime I get a moment I'm playing it all back in my head." with dissolve
    show Risa neutral_side
    h sleep "Like that summer tournament we had? Last night I was lying in bed processing every single match I played. Right down to the last point." with dissolve
    h sleeptalk "'Specially the points I lost. Just recalling it all and re-evaluating for how I should've played it." with dissolve
    h neutral_side "Really getting my tactics nailed down, y'know?" with dissolve
    "Interesting. So this is how she interpreted my instruction about her \"code\" being optimized for playing tennis."
    r tennis wristband_right surprised_side "Huh, and here I was thinking you were more of an act on instinct kinda gal." with dissolve
    "Even when she's away from the court, she's constantly thinking about how to improve her game, analysing her own play to gain an advantage."
    r neutral_side "So you've been hiding that big tennis brain this whole time?" with dissolve
    "That's kinda cool."
    h tennis_headhold2 smirk_side "Oh yeah, it's like a fuckin' supercomputer in there." with dissolve
    r tennis_armup wristband_right_armup neutral_side "That a fact?" with dissolve
    h tennis_armup furious_side "FUCK yeah! I was MADE for tennis!" with vpunch
    r smug_side "Gotta wonder why you weren't made taller, then." with dissolve
    h annoyed_side "Whatever, Risa. So what if everyone's got a few inches on me; They're gonna need more than that if they wanna beat THIS girl." with dissolve
    "Risa, huh? I remember Hiroko had some sort of friend outside of our class she played tennis with. Maybe that's her."
    $risa_name = "Risa"
    show Hiroko neutral_side
    r tennis wristband_right smile_side "Well I gotta admit, I was worried when you stopped showing up for practice, but you've obviously been working on yourself." with dissolve
    r smug_side "Not totally getting the vibe, but it's definitely working for you." with dissolve
    r tennis_armup wristband_right_armup grin "Why, if you can bring this kind of game with you tomorrow I reckon you'll win the whole thing~" with dissolve
    "So it seems Hiroko's match practice is going well. Better than well, in fact."
    h tennis_headhold2 smirk_side "That's the plan~" with dissolve
    "Hiroko sounds like she's at the peak of her powers and full of confidence."
    show Hiroko tennis smile_side
    r smile_side "Yeah. So, what do you want to do now? We've been through all our drills, but we have the court for the whole day." with dissolve
    "So... if she's got all her moves down, then surely the biggest risk to her now is getting injured on the eve of her tournament."
    r tennis wristband_right "I think my netplay could use a little fine-tuning, so I was thinking we could run those drills again then play a few practice games. What do you think?" with dissolve
    h neutral_side "Yeah, we can do that..." with dissolve
    "Hiroko of course thinks she's a [hypno6], built especially to excel in the sport. But of course she isn't."
    h tennis_armup frown_side "Then we can do all of it again!" with dissolve
    r surprised_side "All of it? Run all the drills again?" with dissolve
    "With the mentality I've programmed in her, she probably doesn't understand the limitations of her body anymore."
    r tennis_armup wristband_right_armup neutral_side "I guess we can do that, but you sure there's nothing you want to focus on?" with dissolve
    h angry_side "Nah, I just wanna stay out all night and get all the prep time I can! More the better!" with dissolve
    "That's gotta be dangerous for her... right? She might get hurt, so..."
    r grin "Haha don't go too hard, champ. Save some for the tournament." with dissolve
    h tennis_headhold2 smile_side "I'll have more than enough for the tourney, don't you worry about that." with dissolve
    "I should definitely... yeah, I need to reign her in. Before she wanders back out of bluetooth range for who knows how long."
    r smile_side "Well, no promises but I'll try to keep up. Now let's get back out there." with dissolve
    show Hiroko surprised
    ks casual frown "Wait, Hiroko." with dissolve
    h "..."
    r neutral_side "... Hiro? You hearing me? Let's go." with dissolve
    ks "T-tell her you've changed your mind."
    h neutral_side "I-I... I changed my mind." with dissolve
    r surprised_side "Huh? About what?" with dissolve
    ks neutral "She's right. You shouldn't overexert yourself today."
    h nervous_side "You're right, I shouldn't... overexert myself today." with dissolve
    r concerned_side "Oh... well, you know your limits, Hiro. We can stop whenever you want." with dissolve
    ks "You'll do those things she wanted to do, then you'll stop practice for today."
    h tennis "We'll do what you wanna do, the netplay drills and the practice games. Then we'll wrap it up for today." with dissolve
    r tennis "Really? You sure? You don't seem very sure." with dissolve
    "Ugh, dammit. She's obeying just fine, but apparently can't disguise how she feels about being told to stop."
    ks sigh "Hiroko, smile like you mean it and tell her you're sure. It's your decision."
    h smile_side "... I'm sure. It's my decision." with dissolve
    r tennis_armup smile_side "Still not getting your vibe. Anyway, c'mon, let's finish this." with dissolve
    ks neutral "One more thing, Hiroko. When you're done with practice come straight back to my house."
    ks "Er, don't tell her that part. Obviously."
    h tennis_armup happy_closed "'Kay~" with dissolve
    scene bg k kitchen day with blink
    "I notice Hiroko's headphone disconnect as she walks out of range again and I hang up the phone with a sigh."
    "That probably could've gone a little better."
    "Still, though... I think that was the responsible thing to do. I need to manage her, keep her fresh for the big event tomorrow."
    "And there's no better way to ensure that than if she's here with me."
    stop music fadeout 5.0
    scene bg blackscreen with dissolve
    "It's just logical. This is a logical decision."
    scene bg k entrance day with longdissolve
    play sound doorbell
    "Anyway, about an hour later my doorbell dutifully rings to bring me out of my thoughts."
    play sound dooropen
    pause 0.5
    show Hiroko tennis neutral at center
    with dissolve
    pause 1.0
    play sound doorclose
    queue music Eons
    ks casual "Uh... hey, Hiroko."
    "Okay. So now what?"
    h tennis_headhold2 "Hey, mister sysadmin. I got here fast as I could." with dissolve
    "It's not like I'd planned for this."
    ks "Look, Hiroko, I..."
    "Go easy on her. Keep her fresh for tomorrow. That's all I got."
    ks sigh "I want you to relax, okay? We're just gonna hang out this afternoon, like a couple of regular human beings. So make yourself at home."
    h tennis confused "Hang out? Dude, you pulled me out of training to \"hang out\"?" with dissolve
    "And just like that, her attitude starts to return, even while she obediently kneels down to untie the laces on her tennis shoes."
    ks smile "Yeah. I heard your practice has been going well?"
    show Hiroko smile
    "She smiles and nods affirmatively." with dissolve
    h happy_closed "Oh yeah, SUPER well! Serve, volley, dropshot, forehand, backhand, lob, overhead smash..." with dissolve
    h smile "All I had to do was refresh my muscle memory a lil and it's all working great!" with dissolve
    h tennis_headhold2 neutral_side "An' I guess it makes sense. Like, it's all in my code an' shit. I don't gotta think about it like a human does." with dissolve
    ks "That's... right, yeah."
    h frown "But I still wanna go out there an' practice." with dissolve
    ks smirk "I know you do. But my decision is final."
    show Hiroko tennis sleeptalk_concerned
    "Hiroko whines impotently while I watch her pull off her shoes, then casually slips off her socks while she talks." with dissolve
    h sad "Yeah, yeah, you're still my boss no matter what you tell me." with dissolve
    "So she's the type who likes to go barefoot around the house, huh?"
    h sleeptalk "So if you say I can't, then I can't." with dissolve
    "Does that bother me?"
    menu:
        "\"Put your socks back on\"":
            $HirokoWearing = "Socks"
            h surprised "Uh..." with dissolve
            show Hiroko sleep
            "Hiroko stiffens at the command, breaking her out of her relaxed attitude momentarily as she kneels back down and slips her socks back on." with dissolve
            h neutral "H'yeah, that's exactly what I'm talking about." with dissolve
            "I mean sure, I told her to make herself at home, but it's still my house. And my rules."
            ks sigh "Alright, point made. Now come on in."
        "\"Lose the uniform too\"":
            $HirokoWearing = "Undies"
            h surprised "Uh..." with dissolve
            show Hiroko sleep
            play sound clothes
            "Hiroko stiffens at the command, breaking out of her relaxed attitude momentarily as she unhesitantly pulls off the rest of her tennis uniform." with dissolve
            h underwear neutral "H'yeah, that's exactly what I'm talking about." with dissolve
            ks smirk blush "Hey, you already started taking your clothes off. I was just helping you along."
            ks "A-and besides, now it's totally clear you're not playing tennis any more."
            h sleeptalk "Whatever you say, boss. I ain't gonna argue with ya." with dissolve
            "... Okay, now I feel a little awkward. Got a little caught up in the moment when she started undressing, that's all."
            show Hiroko neutral
            "But it's fine. She's fine. I'll just play it cool." with dissolve
            ks smile noblush "Good. Now come on in."
        "Don't say anything":
            $HirokoWearing = "Barefoot"
            show Hiroko neutral
            $ renpy.transition(dissolve, layer="master")
            "Well, no. And I did tell her to make herself at home, so whatever."
            ks neutral "Cool. Now come on in."
    scene bg k room day
    if HirokoWearing == "Undies":
        show Hiroko underwear neutral at center
    else:
        show Hiroko tennis neutral at center
    with blink
    "I gesture towards my living room and she calmly follows me inside."
    "Calmly. Compliantly. Obediently."
    if HirokoWearing == "Undies":
        show Hiroko underwear_headhold neutral_side
    else:
        show Hiroko tennis_headhold neutral_side
    h "So, like..." with dissolve
    "Regardless of my telling her to chill, she's still aware at all times that she follows my every command."
    h nervous "Whaddya wanna do?" with dissolve
    "I can make this girl do anything I want."
    "And as much as I've tried to avoid the thought, there's nothing now to distract my mind from the growing excitement in my pants."
    if HirokoWearing == "Undies":
        show Hiroko underwear surprised
    else:
        show Hiroko tennis surprised
    h "H-hey, mister sys... u-uh, I mean, Kyou?" with dissolve
    "Hiroko... is a girl, and I'm..."
    "I mean, I could make her..."
    h nervous "What are we doing here?" with dissolve
    if hypno6 != "robot":
        scene cg k wall eve:
            matrixcolor SaturationMatrix(0)
        show HirokoHypno relaxed annoyed:
            matrixcolor SaturationMatrix(0)
        with flash
        $ks = DynamicCharacter("kyou_name", image = "KyouSideFlashback", who_color = "#4B9374")
        h "I barely know what the fuck a \"[hypno6]\" is. Sounds like something a nerd like you made up."
        ks smile "It just means you're a robot who looks like a human woman."
        show HirokoHypno frown
        h "So like, the perfect male nerd fantasy, yeah? A lady robot for loser boys to fuck when they can't get a real girl." with dissolve
        show HirokoHypno upright angry
        h "Holy shit, no wonder you hacked me! Fuckin' perv." with dissolve
        ks frown "I'm not... That's not what I'm doing here, alright?"
        show HirokoHypno annoyed
        h frown "Promise?" with dissolve
        ks "Yeah... That's a little more fucked-up than I'm willing to go right now."
        $ks = DynamicCharacter("kyou_name", image = "KyouSide", who_color = "#4B9374")
        scene bg k room day
        if HirokoWearing == "Undies":
            show Hiroko underwear nervous at center
        else:
            show Hiroko tennis nervous at center
        with flash
        "Shit. What AM I doing here?!"
        "I can't go there with her. But more than that, I fucking PROMISED her I wouldn't go there."
    elif hypno6 == "robot":
        scene cg k wall eve:
            matrixcolor SaturationMatrix(0)
        show HirokoHypno upright angry_up:
            matrixcolor SaturationMatrix(0)
        with flash
        $ks = DynamicCharacter("kyou_name", image = "KyouSideFlashback", who_color = "#4B9374")
        h "Why'd you hack me anyway?"
        ks smirk "I like tinkering with things. It's my hobby."
        show HirokoHypno clenched_fists angry
        h "I'm not a fucking {nw}" with dissolve
        extend "THING, creep!" with vpunch
        ks "Well, I mean... technically you are? I mean, run that by your CPU a second: You're not a girl, and robots don't have a gender."
        $ks = DynamicCharacter("kyou_name", image = "KyouSide", who_color = "#4B9374")
        scene bg k room day
        if HirokoWearing == "Undies":
            show Hiroko underwear nervous at center
        else:
            show Hiroko tennis nervous at center
        with flash
        "Right. I told Hiroko she's not a girl. That's what she believes, and right now I need to believe it too."
        "Because there's no fucking way I'm taking advantage of her like that. Not... not like that."
    "So I need to get a grip. I need to..."
    "O-okay, I'll set up the videogame console. That'll help distract me."
    h frown "Oh, you gotta be kidding me. You pulled me outta my match prep to play a videogame?" with dissolve
    "We're just going to hang out, her and me. Like we're friends."
    h frown_side "What a fucking waste of time." with dissolve
    show Hiroko surprised
    ks casual angry "Ugh, shut up!" with dissolve
    h sad "..." with dissolve
    "As Hiroko hangs her head and falls silent, I sigh gently."
    ks sigh "S-sorry, Hiroko. Just listen a moment, okay?"
    show Hiroko nervous
    "Hastily pushing a game cart into the console, I boot it up and turn back to my quietened companion." with dissolve
    ks neutral "It's like you said, you have all the tools you need to win tomorrow. All you needed was a little refresher."
    ks "And as we've confirmed your systems are all functioning optimally, it's smarter to keep you from getting too worn out."
    ks "So that's why I brought you back. I want to make sure you're undamaged going into the tournament."
    "I smile as I pick up a videogame controller and hand it to her."
    ks smile "You're free to talk again. Now take this and get comfortable over there. We're going to play."
    stop music fadeout 5.0
    scene bg blackscreen with dissolve
    "Hiroko dutifully takes the controller in her hand and pads over to the couch..."
    if HirokoWearing == "Barefoot":
        scene HirokoGaming hiroko1 tennis head1 neutral1 with dissolve
    elif HirokoWearing == "Socks":
        scene HirokoGaming hiroko1_socks tennis head1 neutral1 with dissolve
    elif HirokoWearing == "Undies":
        scene HirokoGaming hiroko1 head1 neutral1 with dissolve
    "... but not before pulling the table a little closer so she can put her feet up."
    queue music Dating3
    ks casual frown "Is that how you do it at home?"
    show HirokoGaming head2 quizzical2
    h confused "Huh? Dude, I don't DO videogames." with dissolve
    "That's not what I meant... but nevermind."
    show HirokoGaming head1 frown1
    h confused_side "What is this thing, anyway? We fighting?" with dissolve
    "She nods at the TV as it blares out the game's title theme over the speakers."
    ks smile "Yeah, it's a fighting game."
    show HirokoGaming sigh1
    h sleeptalk "H'yeah, I deffo don't do fighting games, dude." with dissolve
    ks neutral "You've never played one?"
    show HirokoGaming head2 annoyed2
    h frown "Nope." with dissolve
    "I frown a little. I guess I'm not surprised, but it's going to be a real boring afternoon if she doesn't even know the first thing about how to play."
    "But I've just had an idea."
    ks smirk "Well, that doesn't matter. You've got a good CPU in that head of yours, after all."
    ks "And for the next couple hours you're going to dedicate it towards mastering this game. Understand?"
    show HirokoGaming head1 frown1
    "Hiroko grips the controller in her little hands as she frowns at the screen with determination." with dissolve
    h "Y-yeah, I got it. I'm gonna master the shit out of this thing!"
    ks smile "That's right. We'll run a few practice games, I'll tell you how to play and you'll absorb everything."
    ks "That's your task. And I'm sure a [hypno6] like you will find it easy to follow along and get good in no time, right?"
    show HirokoGaming angry1
    h angry_side vein "Right! I'm fuckin' state of the ART! This game don't have SHIT on something like me!" with dissolve
    "I chuckle to myself as I press a button on my own controller to get us started."
    "Regardless of how I'm making it happen, it's pretty cute to see how fired up she's getting about playing games with me."
    ks "That's the spirit. Now, pick a character and I'll run you through the basics..."
    show HirokoGaming laugh1 with longblink
    h "Kyahahahahaha!"
    "I don't believe it..."
    ks angry "How the fuck is this happening?!"
    "The first hour or so that we played, Hiroko was every bit the novice she said she was."
    show HirokoGaming head2 laugh2
    h laugh_side "I got a perfect that time! That means you didn't hit me once!" with dissolve
    "But now that I've brought her up to speed, showed her a few moves and combos for her character, and some basic tactics..."
    ks frown "I KNOW what a perfect is, Hiroko."
    show HirokoGaming happy2
    "... she's showing a fearsome improvement with virtually every match we've played since." with dissolve
    show HirokoGaming smirk2
    h happy_closed "Yeah, and I just did it. To you~ {font=DejaVuSans.ttf}♫{/font}" with dissolve
    "Hiroko's natural reflexes as an athlete, coupled with her single-minded dedication to mastering the game as commanded has turned her into a deadly opponent in no time at all."
    "And as I mash the fire button to kick off another match, I can't help but find myself getting pissed off..."
    show HirokoGaming smile2
    ks sigh "W-well if you're gonna use cheese moves like that then yeah, you're gonna win sometimes." with dissolve
    show HirokoGaming quizzical2
    h confused "\"Cheese moves\"?" with dissolve
    "The next match starts up as she replies, and I think to attack right away while she's distracted..."
    show HirokoGaming head1 frown1
    "But quick as a flash, Hiroko reacts to block my high kick, then backs away a step while I notice her thumb make a quarter-rolling motion on the controller and-" with dissolve
    play sound punch
    ks angry "GOD FUCKING DAMMIT!" with vpunch
    show HirokoGaming smile1
    "Hiroko just giggles as she presses the attack, and I can only watch as she kicks my dude into the air while he's stunned, then lands a few more hits before he can hit the ground." with dissolve
    ks "You keep doing the same shitty moves over and over!"
    show HirokoGaming annoyed1
    h smile "I dunno man, you call 'em \"cheese\" and \"shitty\", but I call 'em \"winning\"." with dissolve
    "I'm already down to half my health bar. Fuck sake."
    ks frown "You're not even a gamer, how are you doing this?!"
    show HirokoGaming frown1
    "I frantically tap the controller to get my guy up, and he responds by swinging a fist at Hiroko's piece of shit fighter." with dissolve
    "... And she blocks it. And then instantly grabs him and knocks another chunk of life out of him."
    show HirokoGaming head2 quizzical2
    h confused "Uhh, with my kickass CPU? Duh!" with dissolve
    "I'm just mashing buttons now, desperate to land a counterattack."
    show HirokoGaming head1 frown1
    h confused_side "Like, you might be my boss an' all, but how basic have you gotta be that you can't beat me doing the same shit?" with dissolve
    "But I can only groan helplessly as she sidesteps out of the way of my impotent flailing and finishes me off with some high and low kicks."
    show HirokoGaming laugh1
    "And that's another round she's won. And another perfect..." with dissolve
    h "Kyahahahaha~"
    show HirokoGaming surprised1
    "Glowering at the screen as it taunts my loss, I then quickly hit pause just as round two starts up." with dissolve
    ks frown "Okay, time-out."
    show HirokoGaming head2 annoyed2
    h frown "Aw c'mon, I wanna finish you off. Like, again." with dissolve
    ks sigh "Yeah, in a minute. I want to talk to you first."
    show HirokoGaming quizzical2
    h confused "What's there to talk about?" with dissolve
    ks "I mean, okay, you know how to play now and that's great, but doesn't it bother you that this is the only way you can win?"
    ks "Don't you want to experiment? Try a different strategy instead of this cheese crap?"
    show HirokoGaming annoyed2
    "Hiroko snorts and rolls her eyes." with dissolve
    h "H'yeah, I know what you're saying. There's so much salt coming outta your mouth I can fuckin' taste it."
    show HirokoGaming head1 annoyed1
    h frown "You wanna know why I ain't mixing it up? 'Cuz this shit works, simple as." with dissolve
    show HirokoGaming frown1
    h confused "It's just like when I'm out on court. If the girl I'm playing ain't got the game to beat MY game, I ain't gonna change it for her, am I?" with dissolve
    show HirokoGaming angry1
    h frown "SHE's the one who's gotta mix it up; she's gotta change for ME." with dissolve
    show HirokoGaming head2 angry2
    h angry "SHE's the one who sucks!" with vpunch
    ks "Hiroko..."
    show HirokoGaming neutral2
    h neutral "So, like, word of advice? From a [hypno6] to an emotional meatbag like yourself?" with dissolve
    show HirokoGaming smile2
    h neutral_side "Don't get so worked up about it. You know how I play, so you figure out how to beat it." with dissolve
    show HirokoGaming smirk2
    h smirk "Mix it up by not getting your ass kicked~" with dissolve
    ks "Rrrgh."
    "Fuck, who does she think she is, lecturing ME when she's..."
    "No, she's right. I DO need to be the one to change things up."
    show HirokoGaming happy2
    h happy_closed "So, we gonna play again or what?" with dissolve
    "And with her being... well, who she thinks she is, I have a lot of options here."
    "If I were playing an AI opponent in this game I could turn down the difficulty. And Hiroko is... sort of an AI opponent."
    ks neutral "Wait a sec. I'm thinking..."
    show HirokoGaming smile2
    "I could order her to go easy on me, or even tell her to lose on purpose and she'd instinctively obey." with dissolve
    "... Or I could get good."
    show phone at right with moveinright:
        ypos 0.346
    "But nah, I have a more amusing idea. Let me just pick up my phone and open up the app I've been using to give her those electrical responses..."
    show HirokoGaming neutral2
    h neutral "What are you doing?" with dissolve
    stop music fadeout 10.0
    ks "You know Hiroko, I didn't teach you how to play this game for the purpose of winning. This isn't a tennis match."
    ks "I taught you so you could have a little fun with me. Your task is to enjoy the experience of playing however you see fit."
    # "He's annoyed that this squirt WHO ISN'T EVEN A GAMER is beating him so easily, and by using such a cheesy strategy, goddamnit!" with dissolve
    # show Hiroko smirk
    # "Hiroko, genuinely enjoying getting one over on Kyou, snarks that she's just using the most effective tactics. It's just like how she'd approach a tennis match." with dissolve
    # "If your opponent clearly can't handle your gameplan, why change when the goal is to win? Maybe you should mix things up by not getting your ass kicked, dude~"
    # show Hiroko smile_side
    # "That gets Kyou thinking. She IS playing to win, just like she's supposed to." with dissolve
    # "If he was playing an AI opponent in this game he could turn down the difficulty. And Hiroko is... sort of an AI opponent."
    # "He could simply order her to go easy on him, or lose on purpose, but he has a more amusing idea."


    # "As he opens the robot app on his phone Kyou reminds her that she doesn't HAVE to win. She should enjoy the game as she sees fit." with dissolve
    # show Hiroko smile_side
    show HirokoGaming quizzical2
    h confused "Okay?" with dissolve
    ks frown "Yeah, I know. Winning against your sysadmin is so much fun."
    show HirokoGaming smirk2
    h smirk "The most fun~" with dissolve
    ks smirk "But as a [hypno6], you should analyse the possibility that losing to him..."
    play sound appbutton
    if HirokoWearing == "Socks":
        show HirokoGaming hiroko2_socks moaning2 blush2
    else:
        show HirokoGaming hiroko2 moaning2 blush2
    h "{size=18}O-ohhhh...{/size}" with dissolve
    queue music Night_Road
    "I emphasize those last words right as I push the \"Pleasure\" button on my app."
    ks "... might in fact be more fun."
    # "Hiroko doesn't appreciate the difference, since destroying Kyou in the game is the most fun she's getting from this thing, but of course Kyou has a plan now." with dissolve
    # "He puts it to her that losing might be even more fun..."
    # play sound appbutton
    # show Hiroko surprised_side blush
    # "... and as he does so he pushes the \"pleasure\" button on the app which immediately makes Hiroko jolt to attention as a blush forms on her cheeks." with dissolve
    if HirokoWearing == "Socks":
        show HirokoGaming hiroko1_socks angry2
    else:
        show HirokoGaming hiroko1 angry2
    h "W-wh-what's the big idea?" with dissolve
    ks "I just want you to consider it, that's all."
    show HirokoGaming annoyed2
    h irritated vein "You're just playin' with my pleasure circuits! I can see what you're doing, dude-" with dissolve
    ks smirk "And we're off."
    show HirokoGaming head1 surprised1 blush1
    "Hiroko's gaze hurries back to the screen as she realizes I've just unpaused the game." with dissolve
    # "Hiroko growls that he's cheating, messing with her circuits like that, but Kyou starts the next round before she has a chance to say any more." with dissolve
    show HirokoGaming angry1
    h angry_side "Y-you fuckin' cheat-" with dissolve
    play sound punch
    "As I do so, I get my guy to do a leg sweep, which catches her fighter unprepared."
    "For the first time in over two rounds, I've managed to knock her character to the ground."
    play sound appbutton
    if HirokoWearing == "Socks":
        show HirokoGaming hiroko2_socks moaning1
    else:
        show HirokoGaming hiroko2 moaning1
    "And right as it happens, I reach over and press the \"Pleasure\" button again." with dissolve
    show HirokoGaming unfocused1
    h "Unf..." with dissolve

    # "She turns her attention back to the game with renewed determination, and Kyou struggles to find an opening as she wins the first round easily." with dissolve
    # "The second round begins, and he opens by immediately making his character do a leg sweep, landing the first strike as Hiroko's character goes to ground."
    # play sound appbutton
    # show Hiroko surprised_side blush
    "I hear Hiroko murmur with arousal as her body tightens, and her controller almost slips out of her fingers before she can recover."
    # "He then swiftly presses the pleasure button again and Hiroko murmurs with arousal as her body tightens for a moment, fumbling with the controls before recovering." with dissolve
    if HirokoWearing == "Socks":
        show HirokoGaming hiroko1_socks angry1
    else:
        show HirokoGaming hiroko1 angry1
    h "TH-THAT FUCKING DOES IT!" with vpunch
    "I hear a frantic clicking of buttons beside me as Hiroko struggles to get her character back up so she can counterattack."
    "But I'm quick to dash back to avoid her wrath."
    # "A flustered Hiroko then mashes the buttons to get her character back up, and Kyou quickly withdraws his own before she can counterattack." with dissolve
    ks smile "Remember, Hiroko. You're to play this game for fun."
    show HirokoGaming head2 annoyed2 blush2
    h angry "[hypno6!c]s don't have fun! [hypno6!c]s do what their programming tells 'em!" with dissolve
    show HirokoGaming angry2
    h furious_side "{cps=20}And my programmin' tells me I gotta {/cps}{nw}" with dissolve
    extend "BEAT YOUR ASS!" with shake
    # "Kyou reminds her again to play for fun and Hiroko retorts [hypno6]s don't have fun, they only obey their programming, which in her case is to beat his ass!"
    # show Hiroko surprised_side
    show HirokoGaming head1 angry1 blush1
    "She attacks furiously, different from the approach she's been using the last few matches." with dissolve
    "It's left her open to a counter, which I can..."
    play sound punch
    show HirokoGaming surprised1
    h shocked_side "Ahh!" with dissolve
    "Exploit."
    play sound appbutton
    if HirokoWearing == "Socks":
        show HirokoGaming hiroko2_socks moaning1
    else:
        show HirokoGaming hiroko2 moaning1
    "Hiroko's fighter hits the dirt once again, and the \"Pleasure\" button gets another quick tap as I watch her shiver and moan uncontrollably." with dissolve
    h "Aaahn... f-f-fuck, gotta get up..."
    ks smirk "Not so fast."
    play sound punch
    if HirokoWearing == "Socks":
        show HirokoGaming hiroko1_socks surprised1
    else:
        show HirokoGaming hiroko1 surprised1
    h shocked_side "NO!" with vpunch
    "She's too slow to recover, and I take full advantage with a jumping attack that hits her while she's still grounded."
    play sound appbutton
    if HirokoWearing == "Socks":
        show HirokoGaming hiroko2_socks moaning_closed1
    else:
        show HirokoGaming hiroko2 moaning_closed1
    "And we know what that means..." with dissolve
    if HirokoWearing == "Socks":
        show HirokoGaming hiroko1_socks moaning_closed1
    else:
        show HirokoGaming hiroko1 moaning_closed1
    h pain "Ahhhn~ {font=DejaVuSans.ttf}♥{/font} S-s-stoppit!" with dissolve
    # "But Hiroko leaves herself open to a counter, which Kyou exploits and puts her character on the ground again before quickly tapping the reward button a second time." with dissolve
    ks "Why? Doesn't that feel nice, lil [hypno6]?"
    # show Hiroko pain
    # "Hiroko moans, and is slow to recover her character this time, allowing Kyou to land another attack on her while she's still grounded before pressing the button again." with dissolve
    if HirokoWearing == "Socks":
        show HirokoGaming hiroko1_socks unfocused1
    else:
        show HirokoGaming hiroko1 unfocused1
    "With Hiroko's health at almost nothing, I back off for a moment." with dissolve
    "I simply watch as her fighter gets back to their feet while she blinks drunkenly at the screen with a laboured groan."
    ks "Well? Is it more fun to beat me? Or lose to me?"
    h "It's..."
    show HirokoGaming sigh1
    h "F-f-fuck, it's..." with dissolve
    ks "Be honest."
    # "She wonders aloud how a [hypno6] like her can get so overstimulated while Kyou lets her character recover, although she only has a little health left." with dissolve
    # "So which is more fun now, Hiroko? Winning or losing? Kyou smugly asks her while their characters stand off against each other, waiting to strike."
    show HirokoGaming unfocused1
    "She continues to hesitate, thumb quivering over the face buttons of her controller, and I suddenly send my guy forward to finish her off." with dissolve
    show HirokoGaming angry1
    h angry_side "Rrrgh!" with dissolve
    "Hiroko reacts fast enough to block my first strike, and the second, but she's on the back foot; forced to defend again and again."
    play sound punch
    h irritated "Nngh, no!" with vpunch
    "But it's too much. Down her character goes as a simple jab breaks through her defences, while the in-game announcer declares a K.O."
    "A perfect victory for me this time."
    play sound appbutton
    if HirokoWearing == "Socks":
        show HirokoGaming hiroko2_socks moaning1
    else:
        show HirokoGaming hiroko2 moaning1
    "A victory that warrants more than a couple presses of that \"Pleasure\" button..." with dissolve
    play sound appbutton
    h "{cps=10}Nnng- {/cps}{nw}" with dissolve
    play sound appbutton
    show HirokoGaming moaning_closed1
    $ renpy.transition(dissolve, layer="master")
    extend "{cps=10}o-ohhhhh... {/cps}{nw}"
    play sound appbutton
    $ renpy.transition(dissolve, layer="master")
    extend "{cps=10}a-aaahhhh {/cps}{nw}"
    play sound appbutton
    $ renpy.transition(dissolve, layer="master")
    extend "{cps=10}aaaahhhhhhh{/cps}{nw}"
    play sound appbutton
    extend "{cps=10}hhnnnnnn~ {font=DejaVuSans.ttf}♥{/font}{/cps}"
    "I watch as my defeated opponent quivers and quakes as she's compelled to imagine that arousing sensation of electricity zapping her again and again."
    "Feeling the intimate parts of her body light up in one pleasing pulse after another..."
    $persistent.hiroko_gaming_unlock = True
    # "Just letting the sensations overtake her

    # "I watch as my defeated opponent quivers and quakes as she's zapped over and over by that arousing electricity that she's compelled to imagine buzzing past the intimate parts of her body."
    if HirokoWearing == "Barefoot":
        scene HirokoSlumped tennis blissful with longblink
    elif HirokoWearing == "Socks":
        scene HirokoSlumped tennis socks blissful with longblink
    elif HirokoWearing == "Undies":
        scene HirokoSlumped blissful with longblink
    "Her controller slips free of her twitching, grasping fingers as she moans with undisguised lust."
    "And for a moment, as her eyes roll back in her head, she looks completely lost."
    "... Maybe I overdid it a little this time."
    show HirokoSlumped moaning
    $ renpy.transition(longdissolve, layer="master")
    h sleepy "{size=18}Haaah... h-haaaah...{/size}"
    "I promised myself I wouldn't take advantage of her, and I won't. But I'm feeling a real guilty pleasure watching her right now."
    stop music fadeout 10.0
    ks casual neutral blush "N-now, Hiroko, we still got a deciding round to play."
    ks "But this time I'm not going to activate your \"pleasure circuits\" when you take a hit. Only when you lose."
    show HirokoSlumped sleepy
    h "{size=18}Mmh...{/size}" with dissolve
    ks "Do you understand, Hiroko?"
    h sleeptalk "Y... y-yeah..."
    ks smile "And do you want to keep playing? Want to have some more fun?"
    show HirokoSlumped smile
    h tennis_headhold2 affectionate "Yeah... I-I wanna..." with dissolve
    $persistent.hiroko_slumped_unlock = True
    queue music Inspiration
    # "Hiroko hesitates to answer now, and Kyou suddenly dashes to attack. Hiroko tries to block but she reacts too slowly to stop his follow-up attack and is KO'd. Kyou wins!"

    # "Kyou presses \"pleasure\" a few more times and Hiroko shivers with undisguised lust while the controller escapes her quivering hands." with dissolve
    # "As he watches her, Kyou delights in her reaction. It's cute, and a little arousing to witness. He's definitely taking a little pleasure in it himself."
    # "And when Hiroko recovers, Kyou smiles and says they're going to play again. But this time he won't activate her \"pleasure circuits\" any more unless she actually loses." with dissolve
    # show Hiroko tennis_headhold2 affectionate
    # "Hiroko, picking up her controller from the floor, is eager for a rematch. And says she's going to have fun doing it..." with dissolve
    scene bg blackscreen with longdissolve
    nvl_narrator "I waited for Hiroko to reclaim her controller from the floor and catch her breath before resuming play for the deciding round."
    nvl_narrator "... which I lost."
    nvl_narrator "But as we played the afternoon away, things had definitely changed between us. Hiroko was still giving me a good fight, but her edge was gone."
    nvl_narrator "I started to win more rounds than she did. And I'm pretty sure she threw at least a couple of them, just so she could get her \"circuits\" tickled again..."
    # "Kyou recounts how they went at it for a couple more hours. Hiroko still gives him a good fight, but she definitely lost the edge on him that she had before."
    # "He won most of their rounds, and he's sure she deliberately threw a couple of them just to get her circuits tickled again."
    scene bg blackscreen with longdissolve
    nvl clear
    scene bg k room eve
    if HirokoWearing == "Undies":
        show Hiroko underwear smile at center
    else:
        show Hiroko tennis_nosweat smile at center
    $ renpy.transition(longdissolve, layer="master")

    "All too soon, our afternoon gives way to evening."
    "I watch as Hiroko switches off the game console and tidies it away before looking to me with a happy smile on her face."
    ks casual smile "That was... really a lot of fun, huh?"
    if HirokoWearing == "Undies":
        show Hiroko underwear_headhold2 happy blush
    else:
        show Hiroko tennis_nosweat_headhold2 happy blush
    h "Haha, yeah~ That kicked ass!" with dissolve
    ks "And as promised, you're undamaged and at peak operating efficiency for tomorrow."
    # "Kyou asks her how she's feeling, and she admits she had a blast hanging out with her sysadmin." with dissolve
    if HirokoWearing == "Undies":
        show Hiroko underwear nervous noblush
    else:
        show Hiroko tennis_nosweat nervous noblush
    "Hiroko's face suddenly darkens with worry. Can't say I was expecting that reaction from her." with dissolve
    h nervous_side "H'yeah, about that..." with dissolve
    ks neutral "What's the matter?"
    if HirokoWearing == "Undies":
        show Hiroko underwear_headhold nervous
    else:
        show Hiroko tennis_nosweat_headhold nervous
    h "Well it's just... like, I was programmed to win. But what happened back there?" with dissolve
    h sad_side "'S got me a lil confused, is all." with dissolve
    ks "Confused?"
    "She nods."
    h sad "All that pleasure circuit stuff. Never knew I could feel like that before." with dissolve
    h nervous "An' you made me feel like that when I lose." with dissolve
    h sleep "Losing... f-feels good. It feels good now." with dissolve
    h sad "So what's gonna happen when I step out on court tomorrow?" with dissolve
    "I let out a little chuckle. I hadn't thought about it at the time, but I'm sure this won't be an issue for her."
    ks smile "Ah, no. Don't stress your circuits about that, Hiroko."
    show Hiroko nervous
    ks "I mean sure, losing to ME feels good. I used behavioural programming to have you feel that way." with dissolve
    ks "But I left your primary functions alone. Your core programming is still optimized for excelling in the sport of tennis."
    ks "And you will play to win, with the ruthless efficiency only a [hypno6] can have."

    #
    # "She is a little worried that her gaming session has dampened her competitive edge, but Kyou assures her that only losing to him will ever feel good to her." with dissolve
    # "Hiroko's primary function in the real world is to play and win tennis matches with ruthless efficiency. Her core programming hasn't changed at all."
    show Hiroko smile
    "As I give my assurances, a smile starts to return to Hiroko's lips." with dissolve
    h "Yeah... Yeah, you're right."
    h happy_closed "Like, COURSE you're right! You're my sysadmin~" with dissolve
    if HirokoWearing == "Undies":
        show Hiroko underwear_headhold2 smile_side
    else:
        show Hiroko tennis_nosweat_headhold2 smile_side
    h "Sure you fucked around with my code and made it that way, but still... I know you're taking care of me. Like you promised." with dissolve
    h smile "So I gotta hand it to you. You really know all about this nerdy [hypno6] stuff." with dissolve
    if HirokoWearing == "Undies":
        show Hiroko underwear_armup happy
    else:
        show Hiroko tennis_nosweat_armup happy
    h "An' I'm TOTALLY gonna kick ass tomorrow 'cuz of you!" with dissolve
    ks happy "Haha, yeah you are!"
    h confused "So, like... are you gonna come watch?" with dissolve
    ks surprised "H-huh?"
    "I... don't know why I wasn't expecting it, but that question, spoken so innocently, kinda blindsided me."
    h smile "Are you gonna come watch me at the tourney tomorrow?" with dissolve
    "I hadn't really thought about it. It's not like I was ever expecting to trudge into school on a Sunday morning to see this squirt play tennis. But now?"
    ks smile "Yeah, Hiroko. I'll be there."
    show Hiroko happy_closed
    "Why wouldn't I want to see my [hypno6] for her big test?" with dissolve
    if HirokoWearing == "Undies":
        show Hiroko underwear smile
    else:
        show Hiroko tennis_nosweat smile
    ks "Now head straight home, schedule your nightly maintenance an hour early and I'll see you in the morning." with dissolve
    if HirokoWearing == "Undies":
        show Hiroko underwear_headhold2 happy
    else:
        show Hiroko tennis_nosweat_headhold2 happy
    h "Yessir~ {font=DejaVuSans.ttf}♥{/font}" with dissolve
    stop music fadeout 5.0
    scene bg k bedroom eve with blink
    "I'm still smiling long after I've seen Hiroko off and returned to my room."
    "Because man, we really did have the best time back there."
    queue music Past_Sadness
    "For a while I really did forget what I'd done to her and could just enjoy her company."
    "She was cute, and playful and still kind of a brat... it felt like this is how she's like around her friends like Nozomi? Or maybe with a guy she's dating?"
    "Thinking about it, she'd basically be perfect girlfriend material were it not for... uhh..."
    "... Were it not for the fact she's deep under my hypnotic control and nothing that she feels for me is real."
    "She showed me who she could be at her best. But I've never been my best for her."
    "Not while I'm still treating her like my [hypno6]. Or like some kind of pet."
    scene bg blackscreen with dissolve
    stop music fadeout 10.0
    "I need to be better..."
    pause 2.0
    jump Day7_TennisBot
