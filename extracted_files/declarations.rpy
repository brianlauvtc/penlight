init:

    # define config.gl2 = True #Enables Ren'Py's new model-based renderer. Commented out because I think this is enabled by default on the more recent versions of Ren'Py
    #Going forward I'll be able to, among other things, perform b&w colour changes on image layers without having to make separate b&w objects
    #Add matrixcolor SaturationMatrix(0) to an image's property when showing it to make b&w
    #Example:
    # scene RedemptionPhoneDay blank glasses kyou:
    #     matrixcolor SaturationMatrix(0)

    define config.allow_underfull_grids = True #This allows the CG Gallery to function in the later versions of Ren'Py, as it typically has an underfull grid

    layeredimage Nozomi front:
        image_format "Sprites/Nozomi/Front/{image}.png"
        group back_hair:
            attribute longwavy "longwavy back" default
            attribute shortwavy "shortwavy back"
        group skin:
            attribute normal "normal" default
            attribute reddened "reddened"
        always:
            "front hair"
        group clothes:
            attribute casual "casual"
            attribute casual_folded "casual folded"
            attribute maid "maid"
            attribute uniform "uniform" default
            attribute uniform_folded "uniform folded"
            attribute underwear "underwear"
            attribute nude "null"
        group face:
            attribute angry "angry"
            attribute annoyed "annoyed"
            attribute annoyed_left "annoyed left"
            attribute chuckle "chuckle"
            attribute concerned "concerned"
            attribute confused "null" #Add non-existant expressions just to keep lint happy...
            attribute cry "cry"
            attribute cry_laugh "cry laugh"
            attribute cry_joy "cry joy"
            attribute cry_happy "cry happy"
            attribute determined "determined"
            attribute drowsy "drowsy"
            attribute entranced_neutral "entranced neutral"
            attribute entranced_talk "entranced neutral talk"
            attribute entranced_smile "entranced smile"
            attribute entranced_wideopen "entranced wideopen"
            attribute frightened "frightened"
            attribute frown "frown"
            attribute furious "furious"
            attribute happy "happy"
            attribute irritated "irritated"
            attribute laugh "laugh"
            attribute loving "loving"
            attribute neutral "neutral" default
            attribute neutral_left "neutral left"
            attribute neutral_right "neutral right"
            attribute pain "pain"
            attribute panicked "panicked"
            attribute pout_left "pout left"
            attribute pout "pout"
            attribute sad "null"
            attribute scared "scared"
            attribute shocked "shocked"
            attribute sigh "sigh"
            attribute sleep_concerned "sleep concerned"
            attribute sleeptalk "sleeptalk"
            attribute sleeptalk_concerned "sleeptalk concerned"
            attribute sleepy "sleepy"
            attribute sleep "sleep"
            attribute smile "smile"
            attribute smirk "smirk"
            attribute stern "null"
            attribute stern_closed "null"
            attribute surprised "surprised"
            attribute teasing "teasing"
        group blush:
            attribute blush "blush"
            attribute noblush "null" default
        group bruise:
            attribute bruise "bruise"
        group accessory:
            attribute glasses "glasses" default
            attribute noglasses "null"
            attribute mask "mask"

    layeredimage Nozomi front2:
        image_format "Sprites/Nozomi/Front/{image}.png"
        always:
            "body 2"
        group clothes:
            attribute casual "casual 2"
            attribute maid "maid 2"
            attribute uniform "uniform 2" default
            attribute uniform_folded "uniform 2" #A hangover from Nozomi's earliest sprite. Added here to ward off visual bugs
            attribute underwear "underwear 2"
            attribute nude "null"
        group face:
            attribute angry "angry"
            attribute annoyed "annoyed"
            attribute annoyed_left "annoyed left"
            attribute chuckle "chuckle"
            attribute concerned "concerned"
            attribute confused "null" #Add non-existant expressions just to keep lint happy...
            attribute cry "cry"
            attribute cry_laugh "cry laugh"
            attribute cry_joy "cry joy"
            attribute cry_happy "cry happy"
            attribute determined "determined"
            attribute drowsy "drowsy"
            attribute entranced_neutral "entranced neutral"
            attribute entranced_talk "entranced neutral talk"
            attribute entranced_smile "entranced smile"
            attribute entranced_wideopen "entranced wideopen"
            attribute frightened "frightened"
            attribute frown "frown"
            attribute furious "furious"
            attribute happy "happy"
            attribute irritated "irritated"
            attribute laugh "laugh"
            attribute loving "loving"
            attribute neutral "neutral" default
            attribute neutral_left "neutral left"
            attribute neutral_right "neutral right"
            attribute pain "pain"
            attribute panicked "panicked"
            attribute pout_left "pout left"
            attribute pout "pout"
            attribute sad "null"
            attribute scared "scared"
            attribute shocked "shocked"
            attribute sigh "sigh"
            attribute sleep_concerned "sleep concerned"
            attribute sleeptalk "sleeptalk"
            attribute sleeptalk_concerned "sleeptalk concerned"
            attribute sleepy "sleepy"
            attribute sleep "sleep"
            attribute smile "smile"
            attribute smirk "smirk"
            attribute stern "null"
            attribute stern_closed "null"
            attribute surprised "surprised"
            attribute teasing "teasing"
        group blush:
            attribute blush "blush"
            attribute noblush "null" default
        group bruise:
            attribute bruise "bruise"
        group accessory:
            attribute glasses "glasses" default
            attribute noglasses "null"
            attribute mask "mask"

    layeredimage Nozomi side:
        image_format "Sprites/Nozomi/Side/{image}.png"
        always:
            "body"
        group clothes:
            attribute casual "casual"
            attribute maid "maid"
            attribute uniform "uniform" default
            attribute underwear "underwear"
            attribute nude "null"
        group face:
            attribute anxious_side "anxious side"
            attribute anxious "anxious"
            attribute frown "frown"
            attribute frown_side "frown side"
            attribute furious_side "furious side"
            attribute furious "furious"
            attribute happy "happy"
            attribute laugh "laugh"
            attribute irritated "irritated"
            attribute neutral "neutral"
            attribute neutral_side "neutral side"
            attribute rolleyes "rolleyes"
            attribute sad "sad"
            attribute sad_side "sad side"
            attribute sad_closed "sad closed"
            attribute smile "smile"
            attribute smile_side "smile side"
            attribute surprised "surprised"
            attribute surprised_side "surprised side"
            attribute shocked "shocked"
            attribute shocked_side "shocked side"
        group blush:
            attribute blush "blush"
            attribute noblush "null" default
        group bruise:
            attribute bruise "bruise right"
            attribute bruise2 "bruise left"
        group accessory:
            attribute glasses "glasses" default
            attribute noglasses "null"
            attribute mask "mask"

    layeredimage side NozomiSide:
        image_format "Sprites/Nozomi Side/{image}.png"
        always:
            "body"
        group clothes:
            attribute casual "casual"
            attribute casual_folded "casual folded"
            attribute casual2 "casual2"
            attribute uniform "uniform" default
            attribute uniform_folded "uniform folded"
            attribute underwear "underwear"
            attribute nude "null"
        group face:
            attribute angry "angry"
            attribute annoyed "annoyed"
            attribute chuckle "chuckle"
            attribute concerned "concerned"
            attribute confused "null" #Add non-existant expressions just to keep lint happy...
            attribute cry "cry"
            attribute cry_laugh "cry laugh"
            attribute cry_joy "cry joy"
            attribute cry_happy "cry happy"
            attribute determined "determined"
            attribute drowsy "drowsy"
            attribute entranced_neutral "entranced neutral"
            attribute entranced_talk "entranced neutral talk"
            attribute entranced_smile "entranced smile"
            attribute entranced_wideopen "entranced wideopen"
            attribute frightened "frightened"
            attribute frown "frown"
            attribute furious "furious"
            attribute happy "happy"
            attribute irritated "irritated"
            attribute laugh "laugh"
            attribute loving "loving"
            attribute neutral "neutral" default
            attribute pain "pain"
            attribute panicked "panicked"
            attribute pout_left "pout left"
            attribute pout "pout"
            attribute sad "null"
            attribute scared "scared"
            attribute shocked "shocked"
            attribute sigh "sigh"
            attribute sleep_concerned "sleep concerned"
            attribute sleeptalk "sleeptalk"
            attribute sleeptalk_concerned "sleeptalk concerned"
            attribute sleepy "sleepy"
            attribute sleep "sleep"
            attribute smile "smile"
            attribute smirk "smirk"
            attribute stern "null"
            attribute stern_closed "null"
            attribute surprised "surprised"
            attribute teasing "teasing"
        group blush:
            attribute blush "blush"
            attribute noblush "null" default
        group glasses:
            attribute glasses "glasses" default
            attribute noglasses "null"

    layeredimage Atsuko:
        image_format "Sprites/Atsuko/{image}.png"
        always:
            "body"
        always:
            "hair"
        always:
            "clothes"
        group face:
            attribute angry "angry"
            attribute happy "happy"
            attribute laugh "laugh"
            attribute neutral "neutral"
            attribute neutral_side "neutral side"
            attribute sleep "sleep"
            attribute smile "smile" default
            attribute smile_side "smile side"
            attribute surprised "surprised"
            attribute surprised_side "surprised side"

    layeredimage side KyouSide:
        image_format "Sprites/Kyou/{image}.png"
        group back_hair:
            attribute back_hair "back hair" default
        group skin:
            attribute normal "body" default
        group front_hair:
            attribute front_hair "front hair" default
        group clothes:
            attribute uniform "uniform" default
            attribute butler "butler"
            attribute casual "casual"
            attribute nude "null"
        group face:
            attribute angry "angry"
            attribute annoyed "annoyed"
            attribute aroused "aroused"
            attribute chuckle "chuckle"
            attribute concerned "concerned"
            attribute confused "confused"
            attribute cry "cry"
            attribute entranced "entranced"
            attribute frown "frown"
            attribute happy "happy"
            attribute irritated "irritated"
            attribute neutral "neutral" default
            attribute sad "sad"
            attribute sigh "sigh"
            attribute sleep "sleep"
            attribute sleepy "sleepy"
            attribute smile "smile"
            attribute smirk "smirk"
            attribute surprised "surprised"
        group blush:
            attribute noblush "null" default
            attribute blush "blush"

    layeredimage side KyouSideFlashbackOld:
        always:
            im.Grayscale("Sprites/Kyou/back hair.png")
        always:
            im.Grayscale("Sprites/Kyou/body.png")
        always:
            im.Grayscale("Sprites/Kyou/front hair.png")
        group clothes:
            attribute uniform:
                im.Grayscale("Sprites/Kyou/uniform.png") default
            attribute casual:
                im.Grayscale("Sprites/Kyou/casual.png")
        group face:
            attribute confused:
                im.Grayscale("Sprites/Kyou/confused.png")
            attribute frown:
                im.Grayscale("Sprites/Kyou/frown.png")
            attribute neutral:
                im.Grayscale("Sprites/Kyou/neutral.png") default
            attribute smirk:
                im.Grayscale("Sprites/Kyou/smirk.png")
            attribute surprised:
                im.Grayscale("Sprites/Kyou/surprised.png")

    layeredimage side KyouSideFlashback:
        always:
            im.Grayscale("Sprites/Kyou/body.png")
        group clothes:
            attribute uniform:
                im.Grayscale("Sprites/Kyou/uniform.png") default
            attribute casual:
                im.Grayscale("Sprites/Kyou/casual.png")
        group face:
            attribute angry:
                im.Grayscale("Sprites/Kyou/angry.png")
            attribute confused:
                im.Grayscale("Sprites/Kyou/confused.png")
            attribute frown:
                im.Grayscale("Sprites/Kyou/frown.png")
            attribute neutral:
                im.Grayscale("Sprites/Kyou/neutral.png") default
            attribute sigh:
                im.Grayscale("Sprites/Kyou/sigh.png")
            attribute smile:
                im.Grayscale("Sprites/Kyou/smile.png")
            attribute smirk:
                im.Grayscale("Sprites/Kyou/smirk.png")
            attribute surprised:
                im.Grayscale("Sprites/Kyou/surprised.png")

    layeredimage HirokoTest:
        image_format "Sprites/Hiroko/{image}.png"
        # group back_hair:
        #     attribute long_back "long back" default
        group skin:
            attribute normal_headhold "body headhold"
            attribute normal_headhold2 "body headhold 2"
            attribute casual_headhold "body headhold"
            attribute casual_headhold2 "body headhold 2"
            attribute uniform_headhold "body headhold"
            attribute underwear_headhold "body headhold"
            attribute tennis_headhold "body headhold"
            attribute tennis_headhold2 "body headhold 2"
            attribute uniform_headhold2 "body headhold 2"
            attribute underwear_headhold2 "body headhold 2"
        # group front_hair:
        #     attribute long_front "long front" default
        group clothes:
            attribute casual_headhold "casual headhold"
            attribute casual_headhold2 "casual headhold 2"
            attribute tennis_headhold "tennis headhold"
            attribute tennis_headhold2 "tennis headhold 2"
            attribute underwear_headhold "underwear headhold"
            attribute underwear_headhold2 "underwear headhold 2"
            attribute uniform_headhold "uniform headhold"
            attribute uniform_headhold2 "uniform headhold 2"
        group face:
            attribute affectionate "affectionate"
            attribute confused "confused"
            attribute confused_side "confused side"
            attribute nervous "nervous"
            attribute nervous_side "nervous side"
            attribute scared "scared"
            attribute scared_side "scared side"

    layeredimage Hiroko:
        image_format "Sprites/Hiroko/{image}.png"
        group skin:
            attribute normal "body" default
            attribute casual2 "body2" #Adding a '2' to the first property here puts Hiroko in a different hairstyled body
            attribute maid_armup "body armup"
            attribute normal_armup "body armup"
            attribute uniform_armup "body armup"
            attribute casual_armup "body armup"
            attribute casual2_armup "body2 armup"
            attribute dungaree "body"
            attribute dungaree_armup "body armup"
            attribute dungaree2 "body2"
            attribute dungaree2_armup "body2 armup"
            attribute tennis_armup "body armup"
            attribute tennis_nosweat_armup "body armup"
            attribute underwear_armup "body armup"
            #New assets
            attribute normal_headhold "body headhold"
            attribute normal_headhold2 "body headhold 2"
            attribute casual_headhold "body headhold"
            attribute casual2_headhold "body2 headhold"
            attribute casual_headhold2 "body headhold 2"
            attribute casual2_headhold2 "body2 headhold 2"
            attribute dungaree_headhold "body headhold"
            attribute dungaree_headhold2 "body headhold 2"
            attribute dungaree2_headhold "body2 headhold"
            attribute dungaree2_headhold2 "body2 headhold 2"
            attribute maid_headhold "body headhold"
            attribute maid_headhold2 "body headhold 2"
            attribute uniform_headhold "body headhold"
            attribute underwear_headhold "body headhold"
            attribute tennis_headhold "body headhold"
            attribute tennis_nosweat_headhold "body headhold"
            attribute tennis_headhold2 "body headhold 2"
            attribute tennis_nosweat_headhold2 "body headhold 2"
            attribute uniform_headhold2 "body headhold 2"
            attribute underwear_headhold2 "body headhold 2"
        group clothes:
            attribute casual "casual"
            attribute casual2 "casual"
            attribute casual_armup "casual armup"
            attribute casual2_armup "casual armup"
            attribute dungaree "dungaree"
            attribute dungaree_armup "dungaree armup"
            attribute dungaree2 "dungaree"
            attribute dungaree2_armup "dungaree armup"
            attribute maid "maid"
            attribute maid_armup "maid armup"
            attribute gym "gym"
            attribute tennis "tennis"
            attribute tennis_nosweat "tennis nosweat"
            attribute tennis_armup "tennis armup"
            attribute tennis_nosweat_armup "tennis nosweat armup"
            attribute underwear "underwear"
            attribute underwear_armup "underwear armup"
            attribute uniform "uniform" default
            attribute uniform_armup "uniform armup"
            attribute nude "null"
            attribute nude "bare arm"
            #New assets
            attribute casual_headhold "casual headhold"
            attribute casual2_headhold "casual headhold"
            attribute casual_headhold2 "casual headhold 2"
            attribute casual2_headhold2 "casual headhold 2"
            attribute dungaree_headhold "dungaree headhold"
            attribute dungaree_headhold2 "dungaree headhold 2"
            attribute dungaree2_headhold "dungaree headhold"
            attribute dungaree2_headhold2 "dungaree headhold 2"
            attribute maid_headhold "maid headhold"
            attribute maid_headhold2 "maid headhold 2"
            attribute tennis_headhold "tennis headhold"
            attribute tennis_nosweat_headhold "tennis headhold nosweat"
            attribute tennis_headhold2 "tennis headhold 2"
            attribute tennis_nosweat_headhold2 "tennis headhold 2 nosweat"
            attribute underwear_headhold "underwear headhold"
            attribute underwear_headhold2 "underwear headhold 2"
            attribute uniform_headhold "uniform headhold"
            attribute uniform_headhold2 "uniform headhold 2"
            #Below is a bunch of bullshit definitions to keep lint from having a fit
            attribute relaxed "Null"
            attribute drooping "Null"
            attribute nofists "Null"
            attribute no_fists "Null"
            attribute upright "Null"
            attribute clenched_fists "Null"
            attribute clenched_fists_tennis "Null"
            attribute relaxed_fists "Null"
            attribute relaxed_fists_tennis "Null"
        group arm:
            #This entire group is obsolete, back when the old stock sprites were in use. All the attributes invoke blank pngs, but I'm not taking it out because
            #of all the bugfixing that would need to be done on the script if I did ._.
            attribute no_arm "null" default
            attribute tennis_arm "tennis arm"
            attribute dress_arm "dress arm"
            attribute uniform_arm "uniform arm"
            attribute nofists "Null"
            attribute clenched_fists_tennis "Null"
        group face:
            attribute affectionate "affectionate"
            attribute angry "angry"
            attribute angry_side "angry side"
            attribute annoyed "annoyed"
            attribute annoyed_side "annoyed side"
            attribute concerned "concerned"
            attribute confused "confused"
            attribute confused_side "confused side"
            attribute cry "cry"
            attribute cry_happy "cry happy"
            attribute cry_joy "cry joy"
            attribute cry_open "cry open"
            attribute embarrassed "embarrassed"
            attribute entranced_concerned "entranced concerned"
            attribute entranced_concerned_talk "entranced concerned talk"
            attribute entranced_neutral "entranced neutral"
            attribute entranced_laugh "entranced laughing"
            attribute entranced_talk "entranced talk"
            attribute frown "frown"
            attribute frown_side "frown side"
            attribute furious "furious"
            attribute furious_side "furious side"
            attribute giggle "giggle"
            attribute happy "happy"
            attribute happy_closed "happy closed"
            attribute happy_side "happy side"
            attribute irritated "irritated"
            attribute laugh "laugh"
            attribute laugh_side "laugh side"
            attribute nervous "nervous"
            attribute nervous_side "nervous side"
            attribute neutral "neutral" default
            attribute neutral_side "neutral side"
            attribute pain "pain"
            attribute pout "pout"
            attribute rolleyes "rolleyes"
            attribute sad "sad"
            attribute sad_talk "sad talk"
            attribute sad_side "sad side"
            attribute scared "scared"
            attribute scared_side "scared side"
            attribute shocked "shocked"
            attribute shocked_side "shocked side"
            attribute sleep_concerned "sleep concerned"
            attribute sleep "sleep"
            attribute sleeptalk_concerned "sleeptalk concerned"
            attribute sleeptalk "sleeptalk"
            attribute sleepy "sleepy"
            attribute smile "smile"
            attribute smile_side "smile side"
            attribute smirk "smirk"
            attribute smirk_side "smirk side"
            attribute surprised "surprised"
            attribute surprised_side "surprised side"

            #Bullshit to shut lint up
            attribute annoyed_up "Null"
            attribute angry_up "Null"
            attribute drowsy "Null"
            attribute scared "Null"
            attribute sleepy_up_open "Null"
            attribute sleepy_up_closed "Null"


        group blush:
            attribute noblush "null" default
            attribute blush "blush"
        group vein:
            attribute novein "null" default
            attribute vein "veins"
        group facemask:
            attribute mask "mask"

    layeredimage side HirokoSide:
        image_format "Sprites/Hiroko Side/{image}.png"
        group skin:
            attribute normal "body" default
            attribute casual2 "body2" #Adding a '2' to the first property here puts Hiroko in a different hairstyled body
            attribute dungaree "body"
            attribute dungaree2 "body2"
            #New assets
        group clothes:
            attribute casual "casual"
            attribute casual2 "casual"
            attribute dungaree "dungaree"
            attribute dungaree2 "dungaree"
            attribute maid "maid"
            attribute gym "gym"
            attribute tennis "tennis"
            attribute underwear "underwear"
            attribute uniform "uniform" default
            attribute nude "null"
            #New assets
            #Below is a bunch of bullshit definitions to keep lint from having a fit
            # attribute relaxed "Null"
            # attribute drooping "Null"
            # attribute nofists "Null"
            # attribute no_fists "Null"
            # attribute upright "Null"
            # attribute clenched_fists "Null"
            # attribute clenched_fists_tennis "Null"
            # attribute relaxed_fists "Null"
            # attribute relaxed_fists_tennis "Null"
        group face:
            attribute affectionate "affectionate"
            attribute angry "angry"
            attribute angry_side "angry side"
            attribute annoyed "annoyed"
            attribute annoyed_side "annoyed side"
            attribute concerned "concerned"
            attribute confused "confused"
            attribute confused_side "confused side"
            attribute cry "cry"
            attribute cry_happy "cry happy"
            attribute cry_joy "cry joy"
            attribute cry_open "cry open"
            attribute embarrassed "embarrassed"
            attribute entranced_concerned "entranced concerned"
            attribute entranced_concerned_talk "entranced concerned talk"
            attribute entranced_neutral "entranced neutral"
            attribute entranced_laugh "entranced laughing"
            attribute entranced_talk "entranced talk"
            attribute frown "frown"
            attribute frown_side "frown side"
            attribute furious "furious"
            attribute furious_side "furious side"
            attribute giggle "giggle"
            attribute happy "happy"
            attribute happy_closed "happy closed"
            attribute happy_side "happy side"
            attribute irritated "irritated"
            attribute laugh "laugh"
            attribute laugh_side "laugh side"
            attribute nervous "nervous"
            attribute nervous_side "nervous side"
            attribute neutral "neutral" default
            attribute neutral_side "neutral side"
            attribute pain "pain"
            attribute pout "pout"
            attribute rolleyes "rolleyes"
            attribute sad "sad"
            attribute sad_talk "sad talk"
            attribute sad_side "sad side"
            attribute scared "scared"
            attribute scared_side "scared side"
            attribute shocked "shocked"
            attribute shocked_side "shocked side"
            attribute sleep_concerned "sleep concerned"
            attribute sleep "sleep"
            attribute sleeptalk_concerned "sleeptalk concerned"
            attribute sleeptalk "sleeptalk"
            attribute sleepy "sleepy"
            attribute smile "smile"
            attribute smile_side "smile side"
            attribute smirk "smirk"
            attribute smirk_side "smirk side"
            attribute surprised "surprised"
            attribute surprised_side "surprised side"

            #Bullshit to shut lint up
            # attribute annoyed_up "Null"
            # attribute angry_up "Null"
            # attribute drowsy "Null"
            # attribute scared "Null"
            # attribute sleepy_up_open "Null"
            # attribute sleepy_up_closed "Null"
        group blush:
            attribute noblush "null" default
            attribute blush "blush"
        group vein:
            attribute novein "null" default
            attribute vein "veins"
        group facemask:
            attribute mask "mask"

    layeredimage Sayori:
        image_format "Sprites/Sayori/{image}.png"
        group back_hair:
            attribute long_back "long back" default
        group skin:
            attribute normal "body normal" default
            attribute normal_folded "body folded"
            attribute normal_handup "body handup" # Hand raised up to rest under her chin, with the other hand at her hip
            attribute normal_attention "body attention" # Standing to attention, which is the standard pose but with her left arm moved closer to the rest of her body
            attribute uniform_handup "body handup"
            attribute uniform_folded "body folded"
            attribute maid_handup "body handup"
            attribute maid_folded "body folded"
            attribute casual_handup "body handup"
            attribute casual_folded "body folded"
            attribute underwear_handup "body handup"
            attribute underwear_folded "body folded"
        group front_hair:
            attribute long_front "long front" default
        group clothes:
            attribute casual "casual"
            attribute casual_handup "casual handup"
            attribute casual_folded "casual folded"
            attribute maid "maid"
            attribute maid_handup "maid handup"
            attribute maid_folded "maid folded"
            attribute nude "null"
            attribute nude "bare arm"
            attribute underwear "underwear"
            attribute underwear_handup "underwear handup"
            attribute underwear_folded "underwear folded"
            attribute underwear "bare arm"
            attribute uniform "uniform" default
            attribute uniform_handup "uniform handup"
            attribute uniform_folded "uniform folded"
        group face:
            attribute angry "angry"
            attribute alert_angry "alert angry"
            attribute angry_right "angry right"
            attribute alert_angry_right "alert angry right"
            attribute alert_annoyed "alert annoyed"
            attribute alert_annoyed_right "alert annoyed right"
            attribute alert_concerned "alert concerned"
            attribute alert_concerned_right "alert concerned right"
            attribute alert_cry "alert cry"
            attribute alert_crysmile "alert crysmile"
            attribute alert_drowsy "alert drowsy"
            attribute alert_giggle "alert giggle"
            attribute alert_happy "alert happy"
            attribute alert_irritated "alert irritated"
            attribute alert_laugh "alert laugh"
            attribute alert_laugh_right "alert laugh right"
            attribute alert_neutral "alert neutral"
            attribute alert_neutral_right "alert neutral right"
            attribute alert_panicked "alert panicked"
            attribute alert_panicked_right "alert panicked right"
            attribute alert_panicked_blank_right "alert panicked blank right"
            attribute alert_pout "alert pout"
            attribute alert_pout_closed "alert pout closed"
            attribute alert_rolleyes "alert rolleyes"
            attribute alert_scared_right "alert scared right"
            attribute alert_scared "alert scared"
            attribute alert_sleep "alert sleep"
            attribute alert_sleep_concerned "alert sleep concerned"
            attribute alert_sleepy "alert sleepy"
            attribute alert_sleeptalk "alert sleeptalk"
            attribute alert_sleeptalk_concerned "alert sleeptalk concerned"
            attribute alert_smile "alert smile"
            attribute alert_smile_right "alert smile right"
            attribute alert_smirk "alert smirk"
            attribute alert_smirk_right "alert smirk right"
            attribute alert_surprised "alert surprised"
            attribute alert_surprised_right "alert surprised right"
            attribute alert_surprised_blank_right "alert surprised blank right"
            attribute alert_tranceroll "alert trance roll"
            attribute annoyed "annoyed"
            attribute annoyed_right "annoyed right"
            attribute blank "blank"
            attribute blank_right "blank right"
            attribute concerned_right "concerned right"
            attribute concerned "concerned"
            attribute cry "cry"
            attribute entranced_laugh "entranced laughing"
            attribute entranced_right "entranced right"
            attribute entranced_talk_right "entranced talk right"
            attribute frown_right "frown right"
            attribute frown "frown"
            attribute giggle "giggle"
            attribute happy "happy"
            attribute irritated "irritated"
            attribute laugh "laugh"
            attribute laugh_right "laugh right"
            attribute neutral_right "neutral right"
            attribute neutral "neutral" default
            attribute panicked "panicked"
            attribute panicked_right "panicked right"
            attribute pout "pout"
            attribute pout_closed "pout closed"
            attribute rolleyes "rolleyes"
            attribute scared_right "scared right"
            attribute scared "scared"
            attribute scowl "scowl"
            attribute shocked "shocked"
            attribute sleep_concerned "sleep concerned"
            attribute sleep "sleep"
            attribute sleeptalk_concerned "sleeptalk concerned"
            attribute sleeptalk "sleeptalk"
            attribute sleepy "sleepy"
            attribute smile_right "smile right"
            attribute smile "smile"
            attribute smirk_right "smirk right"
            attribute smirk "smirk"
            attribute surprised "surprised"
            attribute surprised_right "surprised right"
            attribute tranceroll "trance roll"
        group blush:
            attribute blush "blush"
            attribute noblush "null" default

    layeredimage side SayoriSide:
        image_format "Sprites/Sayori Side/{image}.png"
        group skin:
            attribute normal "body" default
        group clothes:
            attribute casual "casual"
            attribute nude "null"
            attribute underwear "underwear"
            attribute uniform "uniform" default
        group face:
            attribute angry "angry"
            attribute alert_angry "alert angry"
            attribute angry_right "angry right"
            attribute alert_angry_right "alert angry right"
            attribute alert_annoyed "alert annoyed"
            attribute alert_annoyed_right "alert annoyed right"
            attribute alert_concerned "alert concerned"
            attribute alert_concerned_right "alert concerned right"
            attribute alert_cry "alert cry"
            attribute alert_crysmile "alert crysmile"
            attribute alert_drowsy "alert drowsy"
            attribute alert_giggle "alert giggle"
            attribute alert_happy "alert happy"
            attribute alert_irritated "alert irritated"
            attribute alert_laugh "alert laugh"
            attribute alert_laugh_right "alert laugh right"
            attribute alert_neutral "alert neutral"
            attribute alert_neutral_right "alert neutral right"
            attribute alert_panicked "alert panicked"
            attribute alert_panicked_right "alert panicked right"
            attribute alert_pout "alert pout"
            attribute alert_pout_closed "alert pout closed"
            attribute alert_rolleyes "alert rolleyes"
            attribute alert_scared_right "alert scared right"
            attribute alert_scared "alert scared"
            attribute alert_sleep "alert sleep"
            attribute alert_sleep_concerned "alert sleep concerned"
            attribute alert_sleepy "alert sleepy"
            attribute alert_sleeptalk "alert sleeptalk"
            attribute alert_sleeptalk_concerned "alert sleeptalk concerned"
            attribute alert_smile "alert smile"
            attribute alert_smile_right "alert smile right"
            attribute alert_smirk "alert smirk"
            attribute alert_smirk_right "alert smirk right"
            attribute alert_surprised "alert surprised"
            attribute alert_surprised_right "alert surprised right"
            attribute annoyed "annoyed"
            attribute annoyed_right "annoyed right"
            attribute blank "blank"
            attribute blank_right "blank right"
            attribute concerned_right "concerned right"
            attribute concerned "concerned"
            attribute cry "cry"
            attribute entranced_laugh "entranced laughing"
            attribute entranced_right "entranced right"
            attribute entranced_talk_right "entranced talk right"
            attribute frown_right "frown right"
            attribute frown "frown"
            attribute giggle "giggle"
            attribute happy "happy"
            attribute irritated "irritated"
            attribute laugh "laugh"
            attribute laugh_right "laugh right"
            attribute neutral_right "neutral right"
            attribute neutral "neutral" default
            attribute panicked "panicked"
            attribute panicked_right "panicked right"
            attribute pout "pout"
            attribute pout_closed "pout closed"
            attribute rolleyes "rolleyes"
            attribute scared_right "scared right"
            attribute scared "scared"
            attribute scowl "scowl"
            attribute shocked "shocked"
            attribute sleep_concerned "sleep concerned"
            attribute sleep "sleep"
            attribute sleeptalk_concerned "sleeptalk concerned"
            attribute sleeptalk "sleeptalk"
            attribute sleepy "sleepy"
            attribute smile_right "smile right"
            attribute smile "smile"
            attribute smirk_right "smirk right"
            attribute smirk "smirk"
            attribute surprised "surprised"
            attribute surprised_right "surprised right"
        group blush:
            attribute blush "blush"
            attribute noblush "null" default

    layeredimage Risa:
        image_format "Sprites/Risa/Side/{image}.png"
        group skin:
            attribute body "body" default
            attribute body_armup "body armup"
            attribute uniform_armup "body armup"
            attribute casual_armup "body armup"
            attribute tennis_armup "body armup"
            attribute underwear_armup "body armup"
        group accessory:
            attribute wristband_left "tennis wristband left" #Show one wristband or the other depending which direction she's facing
            attribute wristband_left_armup "tennis wristband left armup" #Show one wristband or the other depending which direction she's facing
            attribute wristband_right "tennis wristband right" # She's meant to only have a wristband on her left wrist
            attribute wristband_right_armup "tennis wristband right armup" # She's meant to only have a wristband on her left wrist
        group clothes:
            attribute casual "casual"
            attribute casual_armup "casual armup"
            attribute tennis "tennis"
            attribute tennis_armup "tennis armup"
            attribute underwear "underwear"
            attribute underwear_armup "underwear armup"
            attribute uniform "uniform" default
            attribute uniform_armup "uniform armup"
            attribute nude "null"
        group face:
            attribute angry "angry"
            attribute angry_side "angry side"
            attribute concerned "concerned"
            attribute concerned_side "concerned side"
            attribute drowsy "drowsy"
            attribute entranced_side "entranced side"
            attribute frown "frown"
            attribute frown_side "frown side"
            attribute grin "grin"
            attribute neutral "neutral" default
            attribute neutral_side "neutral side"
            attribute sleep "sleep"
            attribute sleeptalk "sleeptalk"
            attribute smile "smile"
            attribute smile_side "smile side"
            attribute smug "smug"
            attribute smug_side "smug side"
            attribute surprised "surprised"
            attribute surprised_side "surprised side"
        group blush:
            attribute noblush "null" default
            attribute blush "blush"

    layeredimage Akiko side:
        image_format "Sprites/Akiko/Side/{image}.png"
        group body: #Body attributes 2, 3 and 4 correspond to the hairstyle Akiko's using
            attribute body "Body" default
            attribute body2 "Body 2"
            attribute body3 "Body 3"
            attribute body4 "Body 4"
            attribute body5 "Body 5"
            attribute body_down "Body Down"
            attribute body_down2 "Body Down 2"
            attribute body_down3 "Body Down 3"
            attribute body_down4 "Body Down 4"
            attribute body_down5 "Body Down 5"
            attribute body_up "Body Up"
            attribute body_up2 "Body Up 2"
            attribute body_up3 "Body Up 3"
            attribute body_up4 "Body Up 4"
            attribute casual "Body"
            attribute casual2 "Body 2"
            attribute casual3 "Body 3"
            attribute casual4 "Body 4"
            attribute nozomi_a3 "Body 3"
            attribute nozomi_b3 "Body 3"
            attribute nozomi_a4 "Body 4"
            attribute nozomi_b4 "Body 4"
            attribute casual_down "Body Down"
            attribute casual_down2 "Body Down 2"
            attribute casual_down3 "Body Down 3"
            attribute casual_down4 "Body Down 4"
            attribute nozomi_a_down3 "Body Down 3"
            attribute nozomi_b_down3 "Body Down 3"
            attribute nozomi_a_down4 "Body Down 4"
            attribute nozomi_b_down4 "Body Down 4"
            attribute casual_up "Body Up"
            attribute casual_up2 "Body Up 2"
            attribute casual_up3 "Body Up 3"
            attribute casual_up4 "Body Up 4"
            attribute nozomi_a_up3 "Body Up 3"
            attribute nozomi_b_up3 "Body Up 3"
            attribute nozomi_a_up4 "Body Up 4"
            attribute nozomi_b_up4 "Body Up 4"
            attribute underwear "Body"
            attribute underwear2 "Body 2"
            attribute underwear3 "Body 3"
            attribute underwear4 "Body 4"
            attribute underwear_down "Body Down"
            attribute underwear_down2 "Body Down 2"
            attribute underwear_down3 "Body Down 3"
            attribute underwear_down4 "Body Down 4"
            attribute uniform "Body"
            attribute uniform2 "Body 2"
            attribute uniform3 "Body 3"
            attribute uniform4 "Body 4"
            attribute uniform5 "Body 5"
            attribute uniform_down "Body Down"
            attribute uniform_down2 "Body Down 2"
            attribute uniform_down3 "Body Down 3"
            attribute uniform_down4 "Body Down 4"
            attribute uniform_down5 "Body Down 5"
            attribute uniform_up "Body Up"
            attribute uniform_up2 "Body Up 2"
            attribute uniform_up3 "Body Up 3"
            attribute uniform_up4 "Body Up 4"
            attribute shadow "Shadow"
        group clothes:
            attribute nude "Null"
            attribute casual "Casual"
            attribute casual2 "Casual 2"
            attribute casual3 "Casual 2"
            attribute casual_down "Casual Down"
            attribute casual_down2 "Casual Down 2"
            attribute casual_down3 "Casual Down 2"
            attribute nozomi_a_down3 "Nozomi A Down"
            attribute nozomi_b_down3 "Nozomi B Down"
            attribute nozomi_a_down4 "Nozomi A Down 4"
            attribute nozomi_b_down4 "Nozomi B Down 4"
            attribute casual_up "Casual Up"
            attribute casual_up2 "Casual Up"
            attribute casual_up3 "Casual Up"
            attribute nozomi_a_up3 "Nozomi A Up"
            attribute nozomi_b_up3 "Nozomi B Up"
            attribute nozomi_a_up4 "Nozomi A Up 4"
            attribute nozomi_b_up4 "Nozomi B Up 4"
            attribute nozomi_a3 "Nozomi A"
            attribute nozomi_b3 "Nozomi B"
            attribute nozomi_a4 "Nozomi A 4"
            attribute nozomi_b4 "Nozomi B 4"
            attribute underwear "Underwear"
            attribute underwear2 "Underwear"
            attribute underwear3 "Underwear"
            attribute underwear_down "Underwear Down"
            attribute underwear_down2 "Underwear Down"
            attribute underwear_down3 "Underwear Down"
            attribute underwear_up "Underwear Up"
            attribute underwear_up2 "Underwear Up"
            attribute underwear_up3 "Underwear Up"
            attribute uniform "Uniform" default
            attribute uniform2 "Uniform 2"
            attribute uniform3 "Uniform 2"
            attribute uniform4 "Uniform 4" #Hairstyle no.4 needs its own custom clothes drawing because the longer hair covers a part of them
            attribute uniform5 "Uniform"
            attribute uniform_down "Uniform Down"
            attribute uniform_down2 "Uniform Down 2"
            attribute uniform_down3 "Uniform Down 2"
            attribute uniform_down4 "Uniform Down 4"
            attribute uniform_down5 "Uniform Down"
            attribute uniform_up "Uniform Up"
            attribute uniform_up2 "Uniform Up"
            attribute uniform_up3 "Uniform Up"
            attribute uniform_up4 "Uniform Up 4"
        group face:
            attribute angry "Angry"
            attribute angry_side "Angry Side"
            attribute confused "Confused"
            attribute confused_side "Confused Side"
            attribute cry "Cry"
            attribute cry_happy "Cry Happy"
            attribute cry_happy_closed "Cry Happy Closed"
            attribute cry_smile "Cry Smile"
            attribute drowsy "Drowsy"
            attribute embarrassed "Embarrassed"
            attribute embarrassed_side "Embarrassed Side"
            attribute entranced_neutral "Entranced Neutral"
            attribute entranced_talk "Entranced Talk"
            attribute entranced_smile "Entranced Smile"
            attribute giggle "Giggle"
            attribute happy "Happy"
            attribute laugh "Laugh"
            attribute laugh_open "Laugh Open"
            attribute laugh_wink "Laugh Wink"
            attribute laugh_wink_side "Laugh Wink Side"
            attribute pain "Pain"
            attribute frown "Frown"
            attribute frown_side "Frown Side"
            attribute neutral "Neutral" default
            attribute neutral_side "Neutral Side"
            attribute sad "Sad"
            attribute sad2 "Sad 2"
            attribute sad_closed "Sad Closed"
            attribute sad_closed2 "Sad Closed 2"
            attribute sad_side "Sad Side"
            attribute sad_side2 "Sad Side 2"
            attribute shy "Shy"
            attribute shy_side "Shy Side"
            attribute sigh "Sigh"
            attribute smile "Smile"
            attribute smile_side "Smile Side"
            attribute sleep "Sleep"
            attribute sleeptalk "Sleeptalk"
            attribute smirk "Smirk"
            attribute smirk_side "Smirk Side"
            attribute surprised "Surprised"
            attribute surprised_side "Surprised Side"
        group blush:
            attribute blush "Blush"
            attribute noblush "Null" default
        group armband:
            attribute armband "Armband" default
            attribute armband_down "Armband Down"
            attribute armband_up "Armband Up"
            attribute noarmband "Null"
        group glasses:
            attribute glasses "Glasses" default
            attribute nglasses "Glasses Nozomi"
            attribute noglasses "Null"
        group shadow:
            attribute shadow "Shadow"    

    layeredimage NozomiFlashback front:
        group back_hair:
            attribute longwavy:
                im.Grayscale("Sprites/Nozomi/Front/longwavy back.png") default
        group skin:
            attribute normal:
                im.Grayscale("Sprites/Nozomi/Front/normal.png") default
            attribute reddened:
                im.Grayscale("Sprites/Nozomi/Front/reddened.png")
        always:
            im.Grayscale("Sprites/Nozomi/Front/front hair.png")
        group clothes:
            attribute uniform:
                im.Grayscale("Sprites/Nozomi/Front/uniform.png") default
            attribute uniform_folded:
                im.Grayscale("Sprites/Nozomi/Front/uniform folded.png")
            attribute casual:
                im.Grayscale("Sprites/Nozomi/Front/casual.png")
            attribute casual_folded:
                im.Grayscale("Sprites/Nozomi/Front/casual folded.png")
        group face:
            attribute annoyed_left:
                im.Grayscale("Sprites/Nozomi/Front/annoyed left.png")
            attribute concerned:
                im.Grayscale("Sprites/Nozomi/Front/concerned.png")
            attribute entranced_neutral:
                im.Grayscale("Sprites/Nozomi/Front/entranced neutral.png")
            attribute frown:
                im.Grayscale("Sprites/Nozomi/Front/frown.png")
            attribute laugh:
                im.Grayscale("Sprites/Nozomi/Front/laugh.png")
            attribute neutral:
                im.Grayscale("Sprites/Nozomi/Front/neutral.png")
            attribute pout_left:
                im.Grayscale("Sprites/Nozomi/Front/pout left.png")
            attribute pout:
                im.Grayscale("Sprites/Nozomi/Front/pout.png")
            attribute irritated:
                im.Grayscale("Sprites/Nozomi/Front/irritated.png")
            attribute shocked:
                im.Grayscale("Sprites/Nozomi/Front/shocked.png")
            attribute sigh:
                im.Grayscale("Sprites/Nozomi/Front/sigh.png")
            attribute sleep:
                im.Grayscale("Sprites/Nozomi/Front/sleep.png")
            attribute sleeptalk_concerned:
                im.Grayscale("Sprites/Nozomi/Front/sleeptalk concerned.png")
            attribute smile:
                im.Grayscale("Sprites/Nozomi/Front/smile.png")
            attribute surprised:
                im.Grayscale("Sprites/Nozomi/Front/surprised.png")
        group glasses:
            attribute glasses:
                im.Grayscale("Sprites/Nozomi/Front/glasses.png") default
            attribute noglasses:
                im.Grayscale("Sprites/Nozomi/Front/null.png")
        group blush:
            attribute blush:
                im.Grayscale("Sprites/Nozomi/Front/blush.png")
            attribute noblush:
                im.Grayscale("Sprites/Nozomi/Front/null.png") default

    layeredimage NozomiFlashback side:
        group skin:
            attribute normal:
                im.Grayscale("Sprites/Nozomi/Side/body.png") default
        group clothes:
            attribute uniform:
                im.Grayscale("Sprites/Nozomi/Side/uniform.png") default
            attribute casual:
                im.Grayscale("Sprites/Nozomi/Side/casual.png")
            attribute underwear:
                im.Grayscale("Sprites/Nozomi/Side/underwear.png")
        group face:
            attribute frown:
                im.Grayscale("Sprites/Nozomi/Side/frown.png")
            attribute frown_side:
                im.Grayscale("Sprites/Nozomi/Side/frown side.png")
            attribute shocked:
                im.Grayscale("Sprites/Nozomi/Side/shocked.png")
            attribute shocked_side:
                im.Grayscale("Sprites/Nozomi/Side/shocked side.png")
            attribute surprised:
                im.Grayscale("Sprites/Nozomi/Side/surprised.png")
            attribute surprised_side:
                im.Grayscale("Sprites/Nozomi/Side/surprised side.png")
            attribute sad:
                im.Grayscale("Sprites/Nozomi/Side/sad.png")
            attribute sad_side:
                im.Grayscale("Sprites/Nozomi/Side/sad side.png")
            attribute sad_closed:
                im.Grayscale("Sprites/Nozomi/Side/sad closed.png")
            attribute smile:
                im.Grayscale("Sprites/Nozomi/Side/smile.png")
            attribute smile_side:
                im.Grayscale("Sprites/Nozomi/Side/smile side.png")
        group blush:
            attribute blush:
                im.Grayscale("Sprites/Nozomi/Side/blush.png")
            attribute noblush:
                im.Grayscale("Sprites/Nozomi/Side/null.png") default
        group glasses:
            attribute glasses:
                im.Grayscale("Sprites/Nozomi/Side/glasses.png") default
            attribute noglasses:
                im.Grayscale("Sprites/Nozomi/Side/null.png")

    layeredimage SayoriFlashback:
        group skin:
            attribute normal:
                im.Grayscale ("Sprites/Sayori/body normal.png") default
            attribute normal_folded:
                im.Grayscale ("Sprites/Sayori/body folded.png")
            attribute uniform_folded:
                im.Grayscale ("Sprites/Sayori/body folded.png")
            attribute casual_folded:
                im.Grayscale ("Sprites/Sayori/body folded.png")
            attribute uniform_handup:
                im.Grayscale ("Sprites/Sayori/body handup.png")
        group clothes:
            attribute casual:
                im.Grayscale ("Sprites/Sayori/casual.png")
            attribute casual_folded:
                im.Grayscale ("Sprites/Sayori/casual folded.png")
            attribute nude "null"
            attribute uniform:
                im.Grayscale ("Sprites/Sayori/uniform.png") default
            attribute uniform_folded:
                im.Grayscale ("Sprites/Sayori/uniform folded.png")
            attribute uniform_handup:
                im.Grayscale ("Sprites/Sayori/uniform handup.png")
        group face:
            attribute alert_annoyed:
                im.Grayscale ("Sprites/Sayori/alert annoyed.png")
            attribute alert_concerned:
                im.Grayscale ("Sprites/Sayori/alert concerned.png")
            attribute alert_happy:
                im.Grayscale ("Sprites/Sayori/alert happy.png")
            attribute alert_sleeptalk:
                im.Grayscale ("Sprites/Sayori/alert sleeptalk.png")
            attribute alert_sleep:
                im.Grayscale ("Sprites/Sayori/alert sleep.png")
            attribute alert_smile:
                im.Grayscale ("Sprites/Sayori/alert smile.png")
            attribute alert_smile_right:
                im.Grayscale ("Sprites/Sayori/alert smile right.png")
            attribute alert_smirk:
                im.Grayscale ("Sprites/Sayori/alert smirk.png")
            attribute alert_smirk_right:
                im.Grayscale ("Sprites/Sayori/alert smirk right.png")
            attribute alert_laugh:
                im.Grayscale ("Sprites/Sayori/alert laugh.png")
            attribute alert_neutral:
                im.Grayscale ("Sprites/Sayori/alert neutral.png")
            attribute alert_neutral_right:
                im.Grayscale ("Sprites/Sayori/alert neutral right.png")

    layeredimage Mindtrick:
        #This is the close-up image panel that shows whenever Kyou's mind trick move is used during Nozomi's Trance route
        image_format "images/Mind Trick/{image}.png"
        group base:
            attribute base "Base" default
        group nozomi:
            attribute awake "Highlight" #Shows a couple white dots over Nozomi's eyes
            attribute entranced "Null" #Shows nothing, giving Nozomi's eyes a blank, entranced look
        group kyou_hand:
            attribute wave "Wave Hand"
            attribute wave_sleeve "Wave Hand"
            attribute poke "Poke Hand"
            attribute poke_sleeve "Poke Hand"
            #Found an additional use for this image, where I added Kyou's fingersnapping hand from the café scene in the Devoted path to convey its use in another scene
            attribute fingersnap "Fingersnap"
        group sleeve:
            attribute wave_sleeve "Wave Hand Sleeve"
            attribute poke_sleeve "Poke Hand Sleeve"
        always:
            "Border"

    layeredimage SpiralPhone:
        #This is the close-up image panel that's used to show Kyou nonconsenually hypnotizing Akiko with his phone
        image_format "images/Spiral Phone/{image}.png"
        group base:
            attribute base "Base" default
        group akiko:
            attribute angry "Angry"
            attribute entranced "Entranced"
            attribute sleepy "Sleepy"
            attribute surprised "Surprised"
        group glasses:
            attribute glasses "Glasses" default
        always:
            "Border"

    layeredimage SayoriFlashbackOld:
        group back_hair:
            attribute long_back:
                im.Grayscale ("Sprites/Sayori/long back.png") default
        group skin:
            attribute normal:
                im.Grayscale ("Sprites/Sayori/body normal.png") default
            attribute normal_folded:
                im.Grayscale ("Sprites/Sayori/body folded.png")
            attribute uniform_folded:
                im.Grayscale ("Sprites/Sayori/body folded.png")
            attribute casual_folded:
                im.Grayscale ("Sprites/Sayori/body folded.png")
        group front_hair:
            attribute front_hair:
                im.Grayscale ("Sprites/Sayori/long front.png") default
        group clothes:
            attribute casual:
                im.Grayscale ("Sprites/Sayori/casual.png")
            attribute casual_folded:
                im.Grayscale ("Sprites/Sayori/casual folded.png")
            attribute nude "null"
            attribute uniform:
                im.Grayscale ("Sprites/Sayori/uniform.png") default
            attribute uniform_folded:
                im.Grayscale ("Sprites/Sayori/uniform folded.png")
        group face:
            attribute alert_annoyed:
                im.Grayscale ("Sprites/Sayori/alert annoyed.png")
            attribute alert_happy:
                im.Grayscale ("Sprites/Sayori/alert happy.png")
            attribute alert_sleep:
                im.Grayscale ("Sprites/Sayori/alert sleep.png")
            attribute alert_smile:
                im.Grayscale ("Sprites/Sayori/alert smile.png")
            attribute alert_smile_right:
                im.Grayscale ("Sprites/Sayori/alert smile right.png")
            attribute alert_smirk:
                im.Grayscale ("Sprites/Sayori/alert smirk.png")
            attribute alert_smirk_right:
                im.Grayscale ("Sprites/Sayori/alert smirk right.png")
            attribute alert_laugh:
                im.Grayscale ("Sprites/Sayori/alert laugh.png")
            attribute alert_neutral:
                im.Grayscale ("Sprites/Sayori/alert neutral.png")
            attribute alert_neutral_right:
                im.Grayscale ("Sprites/Sayori/alert neutral right.png")

    layeredimage NozomiFlashbackOld front:
        group back_hair:
            attribute longwavy:
                im.Grayscale("Sprites/Nozomi/Front/longwavy back.png") default
        group skin:
            attribute normal:
                im.Grayscale("Sprites/Nozomi/Front/normal.png") default
            attribute reddened:
                im.Grayscale("Sprites/Nozomi/Front/reddened.png")
        always:
            im.Grayscale("Sprites/Nozomi/Front/front hair.png")
        group clothes:
            attribute uniform:
                im.Grayscale("Sprites/Nozomi/Front/uniform.png") default
            attribute uniform_folded:
                im.Grayscale("Sprites/Nozomi/Front/uniform folded.png")
            attribute casual:
                im.Grayscale("Sprites/Nozomi/Front/casual.png")
            attribute casual_folded:
                im.Grayscale("Sprites/Nozomi/Front/casual folded.png")
        group face:
            attribute annoyed_left:
                im.Grayscale("Sprites/Nozomi/Front/annoyed.png")
            attribute concerned:
                im.Grayscale("Sprites/Nozomi/Front/concerned.png")
            attribute entranced_neutral:
                im.Grayscale("Sprites/Nozomi/Front/entranced neutral.png")
            attribute frown:
                im.Grayscale("Sprites/Nozomi/Front/frown.png")
            attribute neutral:
                im.Grayscale("Sprites/Nozomi/Front/neutral.png")
            attribute laugh:
                im.Grayscale("Sprites/Nozomi/Front/laugh.png")
            attribute pout_left:
                im.Grayscale("Sprites/Nozomi/Front/pout left.png")
            attribute surprised:
                im.Grayscale("Sprites/Nozomi/Front/surprised.png")
            attribute pout:
                im.Grayscale("Sprites/Nozomi/Front/pout.png")
            attribute irritated:
                im.Grayscale("Sprites/Nozomi/Front/irritated.png")
            attribute shocked:
                im.Grayscale("Sprites/Nozomi/Front/shocked.png")
            attribute sigh:
                im.Grayscale("Sprites/Nozomi/Front/sigh.png")
            attribute sleep:
                im.Grayscale("Sprites/Nozomi/Front/sleep.png")
            attribute sleeptalk_concerned:
                im.Grayscale("Sprites/Nozomi/Front/sleeptalk concerned.png")
            attribute smile:
                im.Grayscale("Sprites/Nozomi/Front/smile.png")
        group blush:
            attribute blush:
                im.Grayscale("Sprites/Nozomi/Front/blush.png")
            attribute noblush:
                im.Grayscale("Sprites/Nozomi/Front/null.png") default
        group glasses:
            attribute glasses:
                im.Grayscale("Sprites/Nozomi/Front/glasses.png") default
            attribute none:
                im.Grayscale("Sprites/Nozomi/Front/null.png")

    layeredimage NozomiFlashbackOld side:
        group skin:
            attribute normal:
                im.Grayscale("Sprites/Nozomi/Side/body.png") default
        group clothes:
            attribute uniform:
                im.Grayscale("Sprites/Nozomi/Side/uniform.png") default
            attribute casual:
                im.Grayscale("Sprites/Nozomi/Side/casual.png")
            attribute underwear:
                im.Grayscale("Sprites/Nozomi/Side/underwear.png")
        group face:
            attribute frown:
                im.Grayscale("Sprites/Nozomi/Side/frown.png")
            attribute frown_side:
                im.Grayscale("Sprites/Nozomi/Side/frown side.png")
            attribute surprised:
                im.Grayscale("Sprites/Nozomi/Side/surprised.png")
            attribute surprised_side:
                im.Grayscale("Sprites/Nozomi/Side/surprised side.png")
            attribute sad:
                im.Grayscale("Sprites/Nozomi/Side/sad.png")
            attribute sad_side:
                im.Grayscale("Sprites/Nozomi/Side/sad side.png")
            attribute sad_closed:
                im.Grayscale("Sprites/Nozomi/Side/sad closed.png")
            attribute shocked_side:
                im.Grayscale("Sprites/Nozomi/Side/shocked side.png")
            attribute smile:
                im.Grayscale("Sprites/Nozomi/Side/smile.png")
            attribute smile_side:
                im.Grayscale("Sprites/Nozomi/Side/smile side.png")
        group blush:
            attribute blush:
                im.Grayscale("Sprites/Nozomi/Side/blush.png")
            attribute noblush:
                im.Grayscale("Sprites/Nozomi/Side/null.png") default
        group glasses:
            attribute glasses:
                im.Grayscale("Sprites/Nozomi/Side/glasses.png") default
            attribute noglasses:
                im.Grayscale("Sprites/Nozomi/Side/null.png")

    python:

        import math
        import random

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                        time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)

    transform flip:
        xzoom - 1

    transform tremble:
        alpha 1.0 xoffset 0
        choice:
            block:
                linear 0.05 xoffset 10
                linear 0.05 xoffset -10
                repeat 2
            block:
                choice:
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    repeat 2
                choice:
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    repeat 2
        choice:
            block:
                linear 0.05 xoffset -10
                linear 0.05 xoffset 10
                repeat 2
            block:
                choice:
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    repeat 2
                choice:
                    linear 0.05 xoffset -10
                    linear 0.05 xoffset 10
                    linear 0.05 xoffset -10
                    repeat 2
        linear 0.07 xoffset 0
init -1: #Was getting "galscroll not defined" errors until I moved this declaration to an earlier init block
    transform galscroll(gal_top): #gal_top determines how far to scroll up the image, with 0.0 the very top, negative numbers lower down. A couple images have nothing but empty space so it's more useful to stop scrolling sooner
        ypos -1.0
        linear 12.0 ypos gal_top

    transform galtop(gal_top): #Sets the gallery image to the y axis position specified. Used to set vertical images to the top of the image, like Akiko's fitting room CG from Copycat
        ypos gal_top

    transform galzoomout(): #Zooms out a double-sized CG image so I can show the full image in the gallery
        zoom 0.5 xpos 0.0

    transform coinswing_n1:
        "HirokoCouch nozomi_up n_talk neutral_l coin_l"with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk neutral coin" with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk neutral_r coin_r" with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk neutral coin" with dissolve
        pause 0.7
        repeat

    transform coinswing_n2: #These multiple transitions I'm needing to use to facilitate a short animation for a single CG is so inelegant. Maybe I can figure out something better later...
        "HirokoCouch nozomi_up n_talk2 neutral_l coin_l"with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk2 neutral coin" with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk2 neutral_r coin_r" with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk2 neutral coin" with dissolve
        pause 0.7
        repeat

    transform coinswing_d1:
        "HirokoCouch nozomi_up n_neutral dazed_l coin_l"with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_neutral dazed coin" with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_neutral dazed_r coin_r" with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_neutral dazed coin" with dissolve
        pause 0.7
        repeat

    transform coinswing_d2:
        "HirokoCouch nozomi_up n_talk dazed_l coin_l"with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk dazed coin" with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk dazed_r coin_r" with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk dazed coin" with dissolve
        pause 0.7
        repeat

    transform coinswing_s1:
        "HirokoCouch nozomi_up n_talk sleepy_l coin_l"with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk sleepy coin" with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk sleepy_r coin_r" with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk sleepy coin" with dissolve
        pause 0.7
        repeat

    transform coinswing_s2:
        "HirokoCouch nozomi_up n_talk sleep coin_l"with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk sleep coin" with dissolve 
        pause 0.7
        "HirokoCouch nozomi_up n_talk sleep coin_r" with dissolve
        pause 0.7
        "HirokoCouch nozomi_up n_talk sleep coin" with dissolve
        pause 0.7
        repeat

    transform coinswing_hc2: #This one is for the second Hiroko Couch CG
        "HirokoCouch2 nozomi2 n_smile2 hiroko1 h_sleepyr1 coin_r"with dissolve
        pause 0.7
        "HirokoCouch2 nozomi2 n_smile2 hiroko1 h_sleepy1 coin"with dissolve
        pause 0.7
        "HirokoCouch2 nozomi2 n_smile2 hiroko1 h_sleepyl1 coin_l"with dissolve
        pause 0.7
        "HirokoCouch2 nozomi2 n_smile2 hiroko1 h_sleepy1 coin"with dissolve
        pause 0.7
        repeat

#define n = Character("Nozomi", image = "Nozomi", who_color = "#D0755B") #Nozomi Akemi
define k = DynamicCharacter("kyou_name", who_color = "#4B9374") #Kyou Koyama
define nm = DynamicCharacter("atsuko_name", image = "Atsuko", who_color = "#826B81") #Atsuko Akemi (Nozomi's mum)
define ks = DynamicCharacter("kyou_name", image = "KyouSide", who_color = "#4B9374") #Kyou Koyama (side portrait version)
define a = DynamicCharacter("akiko_name", image = "Akiko", who_color = "#5F5C5C") #Akiko Tsushima
define an = DynamicCharacter("nozomi_name", image = "Akiko", who_color = "#93624B") #Akiko Tsushima (masquerading as Nozomi)
define n = DynamicCharacter("nozomi_name", image = "Nozomi", who_color = "#93624B") #Nozomi Akemi
define ncg = DynamicCharacter("nozomi_name", image = "NozomiHypno", who_color = "#93624B")
define ns = DynamicCharacter("nozomi_name", image = "NozomiSide", who_color = "#93624B") #Nozomi Akemi (side portrait version)

define r = DynamicCharacter("risa_name", image = "Risa", who_color = "#FF9545") #Risa Tachibana
define s = DynamicCharacter("sayori_name", image = "Sayori", who_color = "#385599") #Sayori Watanabe #235F70
define ss = DynamicCharacter("sayori_name", image = "SayoriSide", who_color = "#385599") #Sayori Watanabe (side portrait version)
define scg = Character("sayori_name", layeredimage = "SayoriHypno", who_color = "#385599") #Sayori Watanabe #235F70

define st = DynamicCharacter("sayori_name", image = "SayoriTest", who_color = "#385599") #Sayori Watanabe
define h = DynamicCharacter("hiroko_name", image = "Hiroko", who_color = "#FF89AB") #Hiroko Homura
define hs = DynamicCharacter("hiroko_name", image = "HirokoSide", who_color = "#FF89AB") #Hiroko Homura (side portrait version)
define hcg = DynamicCharacter("hiroko_name", image = "HirokoHypno", who_color = "#FF89AB") #Hiroko Homura
define bot_image = "Sayori"
define bot = DynamicCharacter("bot_name", image = "bot_image") #For use during robot ending

define test = Character ("Nozomi", image = "Test", who_color = "#D0755B") #Nozomi Akemi

define t = Character(_("Mr. Kobayashi"))
define tg = Character(_("Tennis Girl"))
define ta = Character(_("Student #1"))
define tb = Character(_("Student #2"))
define tc = Character(_("Student #3"))
define td = Character(_("Student #4"))
define te = Character("Kasumi")

default persistent.NewSprite = " New"

define k_nvl =  Character('Kyou', kind=nvl, color="#c8c8ff")

define multi = DynamicCharacter("multichar")

init:
    image bg classroom day = "BG/classroom day.jpg"
    image bg classroom eve = "BG/classroom eve.jpg"
    image bg classroom night = "BG/classroom night.jpg"
    image bg classroom2 day = "BG/classroom2 day.jpg"
    image bg classroom2 eve = "BG/classroom2 eve.jpg"
    image bg scienceclass eve = "BG/science class eve.jpg"
    image bg street1 day = "BG/street 1 day.jpg"
    image bg street1 eve = "BG/street 1 eve.jpg"
    image bg street1 night = "BG/street 1 night.jpg"
    image bg street2 eve = "BG/street 2 eve.jpg"
    image bg street3 night = "BG/street 3 night.jpg"
    image bg street4 night = "BG/street 4 night.jpg"
    image bg corridor day = "BG/corridor day.jpg"
    image bg corridor eve = "BG/corridor eve.jpg"
    image bg studentcouncil day = "BG/student council day.jpg"
    image bg studentcouncil eve = "BG/student council eve.jpg"
    image bg rooftop = "BG/rooftop day.jpg"
    image bg bathroom = "BG/bathroom.jpg"
    image bg house = "BG/kyou house day.jpg"
    image bg entrance = "BG/school entrance day.jpg"
    image bg entrance eve = "BG/school entrance eve.jpg"
    image bg k entrance day = "BG/kyou entrance day.jpg"
    image bg k entrance eve = "BG/kyou entrance eve.jpg"
    image bg k bedroom day = "BG/kyou bedroom day.jpg"
    image bg k bedroom eve = "BG/kyou bedroom evening.jpg"
    image bg k bedroom night = "BG/kyou bedroom night.jpg"
    image bg k room day = "BG/kyou room day.jpg"
    image bg k room eve = "BG/kyou room eve.jpg"
    image bg k room eve bw = im.Grayscale("BG/kyou room eve.jpg")
    image bg k house eve = "BG/kyou house eve.jpg"
    image bg n room day = "BG/nozomi room day.jpg"
    image bg n room eve = "BG/nozomi room eve.jpg"
    image bg n room night = "BG/nozomi room night.jpg"
    image bg n bedroom day = "BG/nozomi bedroom day.jpg"
    image bg n bedroom eve = "BG/nozomi bedroom eve.jpg"
    image bg n bedroom eve bw = im.Grayscale("BG/nozomi bedroom eve.jpg")
    image bg n kitchen day = "BG/nozomi kitchen day.jpg"
    image bg n kitchen eve = "BG/nozomi kitchen eve.jpg"
    image bg k kitchen eve = "BG/kyou kitchen eve.jpg"
    image bg k kitchen day = "BG/kyou kitchen day.jpg"
    image bg k bathroom day = "BG/kyou bathroom day.jpg"

    image bg ext school day = "BG/ext school day.jpg"
    image bg ext school eve = "BG/ext school eve.jpg"
    image bg ext school night = "BG/ext school night.jpg"
    image bg school outdoors day = "BG/school outdoors day.jpg"
    image bg school side eve = "BG/school side eve.jpg"
    image bg school side day = "BG/school side day.jpg"
    image bg park day = "BG/park day.jpg"
    image bg park eve = "BG/park eve.jpg"
    image bg library = "BG/library.jpg"
    image bg study room eve = "BG/study room eve.jpg"
    image bg study room eve bw = im.Grayscale("BG/study room eve.jpg")
    image bg study room night = "BG/study room night.jpg"
    image bg principals office day = "BG/principal's office day.jpg"
    image bg principals office eve = "BG/principal's office eve.jpg"
    image bg court day = "BG/court day.jpg"
    image bg court eve = "BG/court eve.jpg"
    image bg court night = "BG/court night.jpg"
    image bg track day = "BG/track day.jpg"
    image bg track eve = "BG/track eve.jpg"
    image bg sports storage = "BG/sports storage.jpg"
    image bg shopping eve = "BG/shopping street eve.jpg"
    image bg shopping day = "BG/shopping street day.jpg"
    image bg shopping night = "BG/shopping street night.jpg"
    image bg shopping2 day = "BG/shopping street 2 day.jpg"
    image bg shopping2 eve = "BG/shopping street 2 eve.jpg"
    image bg shopping3 day = "BG/shopping street 3 day.jpg"
    image bg cafe eve = "BG/cafe eve.jpg"
    image bg cafe eve bw = im.Grayscale("BG/cafe eve.jpg")

    image bg n house day = "BG/nozomi house day.jpg"
    image bg n house eve = "BG/nozomi house eve.jpg"
    image bg s house eve = "BG/sayori house eve.jpg"
    image bg s bedroom eve = "BG/sayori bedroom eve.jpg"

    image bg arcade = "BG/arcade.jpg"
    image bg shopping mall day = "BG/shopping mall day.jpg"
    image bg clothes store = "BG/clothes store.jpg"
    image bg dining area = "BG/dining area.jpg"
    image bg dining area night = "BG/dining area night.jpg"
    image bg karaoke = "BG/karaoke.jpg"
    image bg karaoke lights = "BG/karaoke lights.jpg"
    image bg fast food day = "BG/fast food day.jpg"
    image bg apartment day = "BG/apartment day.jpg"

    image phonetext = "images/text.png"

    image NozomiShadow = im.MatrixColor(
    "Sprites/Nozomi/Front/normal.png",
    im.matrix.colorize("#0000", "#0000"))

    image AkikoShadow = im.MatrixColor(
    "Sprites/Akiko/Side/Body 3.png",
    im.matrix.colorize("#0000", "#0000"))

image bg blackscreen = Solid ((0,0,0))
image bg redscreen = Solid ("DE0000")
image bg yellowscreen = Solid ("FEF600")
image bg greenscreen = Solid ("00BC00")
image bg indigo = Solid ("000084")

image black = Solid ((0,0,0,255))

image penlight = "images/penlight.png"
image phone = "images/smartphone.png"

image second_text = Text("This can be changed later in the Preferences menu")
image third_text = Text("Esto se puede cambiar más tarde en el menú de opciones")


image plight = "Sprites/light.png"
image plight bw = im.Grayscale("Sprites/light.png")
transform light_right: #"Shines" a light to the right over head-sized location
    xpos light_x
    ypos light_y
    linear 0.35 xalign light_x +0.12

transform dlight_right: #Double lights. "Shines" a light to the right over two head-sized locations
    xpos light_x
    ypos light_y
    linear 0.35 xalign light_x +0.12
    xpos slight_x
    ypos slight_y
    linear 0.35 xalign slight_x +0.12

transform light_left: #"Shines" a light to the left over head-sized location
    xpos light_x + 0.12
    ypos light_y
    linear 0.35 xalign light_x

transform dlight_left: #Double lights. "Shines" a light to the left over two head-sized locations
    xpos slight_x +0.12
    ypos slight_y
    linear 0.35 xalign slight_x
    xpos light_x +0.12
    ypos light_y
    linear 0.35 xalign light_x
init:
    transform zoomout:
        xalign 0.0
        yalign 0.0
        # zoom 0.5


define rflash = Fade(0.1, 0.0, 0.4, color="#DE0000") #This is the flash of light when the laser pen is shined in the protag's face (red)
define oflash = Fade(0.1, 0.0, 0.4, color="#FE622C") #This is the flash of light when the laser pen is shined in the protag's face (orange)
define yflash = Fade(0.1, 0.0, 0.4, color="#FEF600") #This is the flash of light when the laser pen is shined in the protag's face (yellow)
define yflashlong = Fade(0.1, 3.0, 0.4, color="#FEF600") #This is the flash of light when the laser pen is shined in the protag's face (yellow)
define gflash = Fade(0.1, 0.0, 0.4, color="#00BC00") #This is the flash of light when the laser pen is shined in the protag's face (green)
define gflashlong = Fade(0.1, 3.0, 0.4, color="#00BC00") #This is the flash of light when the laser pen is shined in the protag's face (green)
define bflash = Fade(0.1, 0.0, 0.4, color="#009CFE") #This is the flash of light when the laser pen is shined in the protag's face (blue)
define iflash = Fade(0.1, 0.0, 0.4, color="#000084") #This is the flash of light when the laser pen is shined in the protag's face (indigo)
define vflash = Fade(0.1, 0.0, 0.4, color="#2C009C") #This is the flash of light when the laser pen is shined in the protag's face (violet)
define flash = Fade(0.3, 0.1, 0.3, color="#F7FFFF") #This is a white flash
define longflash = Fade(0.3, 2.0, 0.6, color="#F7FFFF") #This is a white long flash
define blink = Fade(0.5, 1.0, 0.4, color="#000000") #This is a black flash that shows when the protag is snapping back from trance
define longblink = Fade(2.0, 1.0, 1.0, color="#000000") #This is a black flash that shows when the protag is snapping back from trance
define longdissolve = Dissolve(1.5) #Longer dissolve effect, useful for CGs
define textwithdis =  { "master" : None } #Allows a transition to occur without hiding the dialogue box

#Game States
default pursued = ""
default light_x = 0.43
default light_y = 0.26
default cheat_count = 0
default cheat_state = False
default accepted_terms = True
default sayori_hurt = False
default ending = ""
default ldirection = "right" #Direction of travel for the penlight sweep animation
default lnumber = 1 #Number of light effects involved in the penlight sweep animation
default hypno1 = "" #Recording the hypno-related decisions made during the playthrough
default devoted = 0 #The number of brainwashed "devoted" people (Villain Route)
default robot = 0 #The number of brainwashed "robotized" people (Villain Route)
default sayorifaith = True
default hirokoinfluenced = False
default AkikoClothes = "nozomi_a"
default HypnotizedAkiko = False
default HirokoDeal = False
default GirlfriendReconsidered = False

define nozomi_name = "Nozomi"
define alt_name = ""
define kyou_name = "Kyou"
define akiko_name = "Akiko"
define hiroko_name = "Hiroko"
define sayori_name = "Sayori"
define risa_name = "Risa"
default atsuko_name = "Atsuko"
define multichar = "Nozomi and Sayori"

# default selectable = False


#Music

define audio.Rain = "BGM/Rain.ogg"
define audio.Measured = "BGM/MeasuredPaces.ogg"
define audio.Memories = "BGM/Memories.ogg"
define audio.Bright_Opening = "BGM/Bright Opening.ogg"
define audio.Flow = "BGM/The Flow of Time.ogg"
define audio.Peaceful = "BGM/Peaceful Piano.ogg"
define audio.Eons = "BGM/Eons Later.ogg"
define audio.Downtown = "BGM/Downtown.ogg"
define audio.Sorrow = "BGM/Sorrow.ogg"
define audio.Past_Sadness = "BGM/Past Sadness.ogg"
define audio.Machine = "BGM/The Machine Thinks.ogg"
define audio.Tennis = "BGM/Tennis.ogg"
define audio.Audience = "BGM/Audience.ogg"
define audio.LoudAudience = "BGM/Loud Audience.ogg"
define audio.Beautiful = "BGM/Beautiful Day.ogg"
define audio.Warm_Romantic = "BGM/Warm Romantic Mood (Looped).ogg"
define audio.Inspiration = "BGM/Inspiration_looped(Piano and Strings Version).ogg"
define audio.Dating3 = "BGM/Dating 3.ogg"
define audio.Sad_Heroine = "BGM/Sad Heroine.ogg"
define audio.Monologue = "BGM/Monologue.ogg"
define audio.Night_Road = "BGM/Immorality 01 - Night Road.ogg"
define audio.Clumsy_Two = "BGM/Clumsy Two.ogg"
define audio.Luminous_Rain = "BGM/Luminous Rain.ogg"
define audio.OnMyWay = "BGM/AlexBeroza_-_On_My_Way (short).ogg"
define audio.Park = "BGM/Park.ogg"
define audio.Diary = "BGM/Event - Old Diary.ogg"
define audio.Black_Room = "BGM/Immorality 06 - Black Room.ogg"
define audio.Piano_Mood = "BGM/Piano Mood.ogg"
define audio.Cafe = "BGM/cafe.ogg"
define audio.LookingGlass = "BGM/Looking Glass.ogg"
define audio.Unrest = "BGM/Unrest.ogg"
define audio.Sorrow2 = "BGM/Sorrow 2.ogg"
define audio.Dark_Piano = "BGM/piece-for-disaffected-piano-two-by-kevin-macleod.ogg"
define audio.Evening = "BGM/Evening Stroll.ogg"
define audio.Grave = "BGM/wellman (feat Queenie & RadioZero) - On Your Grave.ogg"

#Sound

define audio.schoolbell = "SFX/School Chime.mp3"
define audio.doorbell = "SFX/Door Bell.mp3"
define audio.cellvibrate = "SFX/Cell Vibrate Short.mp3"
define audio.cellvibratelong = "SFX/cell-vibrate.mp3"
define audio.dooropen = "SFX/Door Open.mp3"
define audio.doorclose = "SFX/Door Close.mp3"
define audio.classdoor = "SFX/Classroom Door Slide.mp3"
define audio.punch = "SFX/Jab.mp3"
define audio.clothes = "SFX/Clothes.mp3"
define audio.clothesstrip = "SFX/Rubbing-clothes-together-foley-3-www.FesliyanStudios.com.mp3"
define audio.fingersnap = "SFX/Finger snap.mp3"
define audio.doorknock = "SFX/Doorknocking.mp3"
define audio.doorknockslow = "SFX/Doorknocking Slow.mp3"
define audio.ringtone = "SFX/Ringtone.mp3"
define audio.doorbang = "SFX/Door bang.mp3"
define audio.appbutton = "SFX/Button.mp3"
define audio.tennisbounce = "SFX/Tennis Bounce.mp3"
define audio.tennishit = "SFX/Tennis Hit.mp3"
define audio.running = "SFX/Running.mp3"
define audio.applause = "SFX/Applause.mp3"
define audio.AudienceClapping = "SFX/Audience Clapping.mp3"
define audio.AudienceLaughter = "SFX/Audience Laughter.mp3"
define audio.AudienceLaughterLoud = "SFX/Audience Laughter (loud).mp3"
define audio.CrowdGasp = "SFX/Crowd Gasp.mp3"
define audio.footsteps = "SFX/footsteps.mp3"
define audio.barefootrunfadein = "SFX/footsteps barefoot running fadein.mp3"
define audio.runningshoes = "SFX/footsteps running shoes.mp3"
define audio.clap = "SFX/clap.mp3"
define audio.bodyimpact = "SFX/Body Impact.mp3"
define audio.papers = "SFX/Papers.mp3"
define audio.objecthit = "SFX/Object Hit.mp3"
define audio.racketdrop = "SFX/tennis racket placed down on hard surface.mp3"
define audio.sitting = "SFX/sitting.mp3"
define audio.shower = "SFX/shower-1.mp3"
define audio.telephone = "SFX/telephone.mp3"
define audio.zipper = "SFX/zipper.mp3"
define audio.curtainpull = "SFX/curtain pull.mp3"


define audio.diceshake = "SFX/Dice Shake.mp3"
define audio.diceroll = "SFX/Dice Roll.mp3"
define audio.slap = "SFX/Slap.mp3"
define audio.spank = "SFX/slaps_06.mp3"
define audio.sword = "SFX/Bamboo Sword Swing.mp3"

#Screen Shake
define shake = Shake((0, 0, 0, 0), 3.0, dist=15)

label lightshow:
    if ldirection == "right":
        if lnumber == 1:
            show plight at light_right, zorder 20
            hide plight with dissolve
        elif lnumber == 2:
            show plight at dlight_right, zorder 20
            pause 0.4
            hide plight with dissolve
        $ldirection = "left"
    else:
        if lnumber == 1:
            show plight at light_left, zorder 20
            hide plight with dissolve
        elif lnumber == 2:
            show plight at dlight_left, zorder 20
            pause 0.4
            hide plight with dissolve
        $ldirection = "right"
    return

label lightshow_bw:
    if ldirection == "right":
        if lnumber == 1:
            show plight bw at light_right, zorder 20
            hide plight bw with dissolve
        elif lnumber == 2:
            show plight bw at dlight_right, zorder 20
            pause 0.4
            hide plight bw with dissolve
        $ldirection = "left"
    else:
        if lnumber == 1:
            show plight bw at light_left, zorder 20
            hide plight bw with dissolve
        elif lnumber == 2:
            show plight bw at dlight_left, zorder 20
            pause 0.4
            hide plight bw with dissolve
        $ldirection = "right"
    return

label robotalk(char, type, face):
    if char == "hiroko":
        if type == "cg":
            if face == "entranced_talk":
                show HirokoHypno entranced_talk
            elif face == "entranced_neutral":
                show HirokoHypno entranced_neutral
            elif face == "neutral":
                show HirokoHypno neutral
        elif type == "sprite":
            if face == "entranced_talk":
                show Hiroko entranced_talk
            elif face == "entranced_neutral":
                show Hiroko entranced_neutral
            elif face == "neutral":
                show Hiroko neutral

label cg_cheat:
    #Calling this function should set every "seen it" state in the CG gallery to true, ensuring the whole gallery is unlocked.
    $ persistent.kyou_intro_unlock = True
    $ persistent.stageshow_unlock = True
    $ persistent.classroom_nozomi_unlock = True
    $ persistent.hiroko_tennis1_unlock = True
    $ persistent.sayori_intro_unlock = True
    $ persistent.sayori_study_unlock = True
    $ persistent.sports_shed_night_unlock = True
    $ persistent.hiroko_vs_risa_unlock = True
    $ persistent.delusion_rooftop_unlock = True
    $ persistent.classroom_lunch2_delusion_unlock = True
    $ persistent.classroom_lunch2_sleeper_unlock = True
    $ persistent.akiko_intro_unlock = True
    $ persistent.study_room_sayori_unlock = True
    $ persistent.room_hiroko_1_unlock = True
    $ persistent.room_hiroko_2_unlock = True
    $ persistent.k_room_sayori_unlock = True
    $ persistent.sayori_alter_start_unlock = True
    $ persistent.sayori_greeting_unlock = True
    $ persistent.sayori_arm_unlock = True
    $ persistent.sayori_lunch_unlock = True
    $ persistent.sayori_arcade2_unlock = True
    $ persistent.sayori_penlight_unlock = True
    $ persistent.sayori_bed1_unlock = True
    $ persistent.sayori_hug_unlock = True
    $ persistent.sayori_walk_unlock = True
    $ persistent.hiroko_trapped_unlock = True
    $ persistent.hiroko_tickle_unlock = True
    $ persistent.hiroko_cat_1_unlock = True
    $ persistent.hiroko_cat_2_unlock = True
    $ persistent.hiroko_racket_unlock = True
    $ persistent.hiroko_couch_argument_unlock = True
    $ persistent.k_room_hiroko_tv1_unlock = True
    $ persistent.hiroko_reversal_unlock = True
    $ persistent.hiroko_shoe_unlock = True
    $ persistent.hiroko_gaming_unlock = True
    $ persistent.hiroko_slumped_unlock = True
    $ persistent.tennis_bot_end_1_unlock = True
    $ persistent.hiroko_cafe_unlock = True
    $ persistent.hiroko_yawn_day_unlock = True
    $ persistent.hiroko_yawn_eve_unlock = True
    $ persistent.hiroko_cam_1_1_unlock = True
    $ persistent.hiroko_cam_1_2_unlock = True
    $ persistent.hiroko_cam_2_unlock = True
    $ persistent.hiroko_cam_3_unlock = True
    $ persistent.hiroko_cam_4_unlock = True
    $ persistent.hiroko_cam_5_unlock = True
    $ persistent.nozo_cam_hypno_unlock = True
    $ persistent.hiroko_cam_kiss_unlock = True
    $ persistent.hiroko_nozomi_phone_unlock = True
    $ persistent.hiroko_bed_unlock = True
    $ persistent.hiroko_couch_unlock = True
    $ persistent.hiroko_couch2_unlock = True
    $ persistent.hiroko_tennis_kiss_unlock = True
    $ persistent.sayori_room_hypno2_unlock = True
    $ persistent.sayori_room_tickle_unlock = True
    $ persistent.sayori_grab_unlock = True
    $ persistent.sayori_x_kyou_unlock = True
    $ persistent.sayori_arcade_unlock = True
    $ persistent.sayori_dinner_unlock = True
    $ persistent.sayori_alter_confrontation_unlock = True
    $ persistent.sayori_alter_confrontation2_unlock = True
    $ persistent.akiko_intro2_unlock = True
    $ persistent.sayori_alter_hug_unlock = True
    $ persistent.alter_bad_end_1_unlock = True
    $ persistent.alter_bad_end_2_unlock = True
    $ persistent.alter_coop_end_1_unlock = True
    $ persistent.hiroko_park_sad_unlock = True
    $ persistent.hiroko_won_unlock = True
    $ persistent.k_room_hiroko_tv2_unlock = True
    $ persistent.sayori_alter_bad_end_3_unlock = True
    $ persistent.hiroko_rooftop_1_1_unlock = True
    $ persistent.hiroko_rooftop_1_2_unlock = True
    $ persistent.hiroko_rooftop_2_unlock = True
    $ persistent.penlight_broken_unlock = True
    $ persistent.hiroko_stageshow_good_unlock = True
    $ persistent.hiroko_stageshow_cat_unlock = True
    $ persistent.hiroko_park_hypno_unlock = True
    $ persistent.hiroko_park_ending_1_unlock = True
    $ persistent.yikes_end_unlock = True
    $ persistent.hiroko_good_end_1_unlock = True
    $ persistent.classroomlunch2_1_unlock = True
    $ persistent.classroomlunch2_2_unlock = True
    $ persistent.classroomlunch3_unlock = True
    $ persistent.classroomlunch3_2_unlock = True
    $ persistent.classroomlunch3_3_unlock = True
    $ persistent.classroomlunch3_4_unlock = True
    $ persistent.classroomlunch4_1_unlock = True
    $ persistent.classroomlunch5_1_unlock = True
    $ persistent.classroomlunch5_2_unlock = True
    $ persistent.sleeper_agent_night_unlock = True
    $ persistent.nozomi_cafe_unlock = True
    $ persistent.k_room_nozomi_1_1_unlock = True
    $ persistent.k_room_nozomi_1_2_unlock = True
    $ persistent.k_room_nozomi_2_1_unlock = True
    $ persistent.k_room_nozomi_2_2_unlock = True
    $ persistent.study_room_nozomi_unlock = True
    $ persistent.study_room_hypno_nozomi_unlock = True
    $ persistent.nozomi_chocolate_unlock = True
    $ persistent.nozomi_mindtrick_unlock = True
    $ persistent.nozomi_collapse_unlock = True
    $ persistent.trance_stop_end_unlock = True
    $ persistent.nozomi_boardgame_unlock = True
    $ persistent.nozomi_boardgame2_unlock = True
    $ persistent.nozomi_hypnobondage_unlock = True
    $ persistent.nozomi_hypnobondage_spanking_unlock = True
    $ persistent.nozomi_hypnobondage_tickling_unlock = True
    $ persistent.sayori_alter_lunch_unlock = True
    $ persistent.sayori_hypno_day_unlock = True
    $ persistent.nozomi_cola_unlock = True
    $ persistent.nozomi_burglar_unlock = True
    $ persistent.nozomi_burglar_undressing_unlock = True
    $ persistent.hiroko_court_night_good_unlock = True
    $ persistent.hiroko_court_night_bad_unlock = True
    $ persistent.nozomi_rooftop_spanked_unlock = True
    $ persistent.nozomi_rooftop_tickled_unlock = True
    $ persistent.nozomi_rooftop_spank2_unlock = True
    $ persistent.nozomi_rooftop_tickle2_unlock = True
    $ persistent.nozomi_provoke_unlock = True
    $ persistent.nozomi_couch_strip_unlock = True
    $ persistent.nozomi_kneeling_trance1_unlock = True
    $ persistent.nozomi_kneeling_trance2_unlock = True
    $ persistent.nozomi_zombie_walk_unlock = True
    $ persistent.nozomi_lying_unlock = True
    $ persistent.nozomi_kitchen_unlock = True
    $ persistent.nozomi_omelette_unlock = True
    $ persistent.nozomi_kiss_unlock = True
    $ persistent.forced_girlfriend_ending_unlock = True
    $ persistent.nozomi_good_end_1_unlock = True
    $ persistent.k_room_nozomi_reversal1_unlock = True
    $ persistent.k_room_nozomi_reversal2_unlock = True
    $ persistent.k_room_nozomi_reversal3_unlock = True
    $ persistent.k_room_nozomi_tv1_unlock = True
    $ persistent.k_room_nozomi_tv2_unlock = True
    $ persistent.k_room_nozomi_tv3_unlock = True
    $ persistent.k_room_nozomi_tv4_unlock = True
    $ persistent.nozomi_karaoke_group_unlock = True
    $ persistent.nozomi_threatening_unlock = True
    $ persistent.nozomi_sorry_unlock = True
    $ persistent.nozomi_couch_hypno_unlock = True
    $ persistent.nozomi_tortured_tickle_unlock = True
    $ persistent.nozomi_tortured_spank_unlock = True
    $ persistent.reversal_bad_end_unlock = True
    $ persistent.reversal_good_end_unlock = True
    $ persistent.alter_good_end_1_unlock = True
    $ persistent.alter_good_end_2_unlock = True
    $ persistent.hiroko_betrayal_unlock = True
    $ persistent.zombie_beginning_unlock = True
    $ persistent.nozomi_injured_unlock = True
    $ persistent.nozomi_hiroko_hug_unlock = True
    $ persistent.zombie_bedroom_1_1_unlock = True
    $ persistent.zombie_bedroom_1_2_unlock = True
    $ persistent.zombie_bedroom_1_3_unlock = True
    $ persistent.zombie_bedroom_2_unlock = True
    $ persistent.zombie_bedroom_3_unlock = True
    $ persistent.classroom_hiroko_2_1_unlock = True
    $ persistent.classroom_hiroko_2_2_unlock = True
    $ persistent.classroom_hiroko_2_3_unlock = True
    $ persistent.classroom_hiroko_2_4_unlock = True
    $ persistent.sayori_room_hypno_unlock = True
    $ persistent.sayori_doll_pose1_unlock = True
    $ persistent.sayori_doll_pose2_unlock = True
    $ persistent.sayori_doll_climax_unlock = True
    $ persistent.hiroko_rehearsal_unlock = True
    $ persistent.hypno_rehearsal_unlock = True
    $ persistent.hypno_rehearsal_2_unlock = True
    $ persistent.trance_abuse_end_unlock = True
    $ persistent.school_cafe_1_unlock = True
    $ persistent.zombie_ending_1_unlock = True
    $ persistent.sayori_stageshow_catalepsy_unlock = True
    $ persistent.sayori_doll_good_end_unlock = True
    $ persistent.rooftop_day_unlock = True
    $ persistent.sports_shed_night_unlock = True
    $ persistent.delusion_struggle_sayori_unlock = True
    $ persistent.k_bedroom_confrontation_sayori_unlock = True
    $ persistent.k_bedroom_confrontation_hiroko_unlock = True
    $ persistent.akiko_makeover_1_unlock = True
    $ persistent.akiko_makeover_2_unlock = True
    $ persistent.copycat_karaoke_hypno1_unlock = True
    $ persistent.copycat_karaoke_hypno2_unlock = True
    $ persistent.copycat_karaoke1_unlock = True
    $ persistent.copycat_karaoke2_unlock = True
    $ persistent.copycat_karaoke3_unlock = True
    $ persistent.delusion_end_1_unlock = True
    $ persistent.alley_hiroko_unlock = True
    $ persistent.akiko_science_unlock = True
    $ persistent.devotion_start_unlock = True
    $ persistent.devotion_start2_unlock = True
    $ persistent.robot_start_unlock = True
    $ persistent.sleeper_agent_start_unlock = True
    $ persistent.hiro_walk_devotion_unlock = True
    $ persistent.hiro_walk_robot_unlock = True
    $ persistent.k_bedroom_hiroko_1_unlock = True
    $ persistent.k_bedroom_hiroko_2_unlock = True
    $ persistent.k_bedroom_hiroko_3_unlock = True
    $ persistent.redemption_start_unlock = True
    $ persistent.hiroko_robot_programming_unlock = True
    $ persistent.sayori_sleeper_capture_unlock = True
    $ persistent.k_phone_robot_unlock = True
    $ persistent.nozomi_robot_kiss_unlock = True
    $ persistent.rooftop_robot_unlock = True
    $ persistent.rooftop_robot__girlfriend_unlock = True
    $ persistent.nozomisleepercapture_unlock = True
    $ persistent.nozomi_interrogation_unlock = True
    $ persistent.nozomi_robot_programming_unlock = True
    $ persistent.robot_karaoke_end_unlock = True
    $ persistent.k_bedroom_robot_hiroko_unlock = True
    $ persistent.k_bedroom_robot_nozomi_unlock = True
    $ persistent.k_bedroom_robot_sayori_unlock = True
    $ persistent.devotion_bedroom_day2_unlock = True
    $ persistent.creepy_hiroko_unlock = True
    $ persistent.devotion_tennis_unlock = True
    $ persistent.devotion_tennis_partial_unlock = True
    $ persistent.devotion_underwear_unlock = True
    $ persistent.devotion_naked_unlock = True
    $ persistent.study_room_hypno_sayori_unlock = True
    $ persistent.rooftop_devotion_unlock = True
    $ persistent.sleeper_agent_struggle1_unlock = True
    $ persistent.sleeper_agent_struggle2_unlock = True
    $ persistent.sleeper_agent_defeat_unlock = True
    $ persistent.akiko_student_council_hypno_unlock = True
    $ persistent.akiko_student_council_hypno2_unlock = True
    $ persistent.akiko_student_council_hypno3_unlock = True
    $ persistent.nozomi_cafe_villain_unlock = True
    $ persistent.nozomi_captured_unlock = True
    $ persistent.nozomi_window_unlock = True
    $ persistent.nozomi_kneeling_devotion_unlock = True
    $ persistent.devotion_end_1_unlock = True
    $ persistent.devotion_end_2_unlock = True
    $ persistent.akiko_breakfast_unlock = True
    $ persistent.k_room_akiko_1_unlock = True
    $ persistent.k_room_akiko_2_unlock = True
    $ persistent.k_room_akiko_3_unlock = True
    $ persistent.redemption_phone_day_unlock = True
    $ persistent.akiko_slapped_unlock = True
    $ persistent.rooftop_reversal_unlock = True
    $ persistent.voodoo_phone_unlock = True
    $ persistent.hiroko_scared_unlock = True
    $ persistent.bathroom_ambush_unlock = True
    $ persistent.voodoo_phone1_unlock = True
    $ persistent.voodoo_phone2_unlock = True
    $ persistent.akiko_kiss_unlock = True
    $ persistent.spiral_ending_unlock = True
    $ persistent.redemption_phone_eve_unlock = True
    $ persistent.akiko_kendo_unlock = True
    $ persistent.copycat_ending_1_unlock = True
    $ persistent.copycat_ending_2_1_unlock = True
    $ persistent.copycat_ending_2_2_unlock = True
    $ persistent.sword_strike_unlock = True
    $ persistent.akiko_cornered_unlock = True
    $ persistent.redemption_ending_1_1_unlock = True
    $ persistent.redemption_ending_1_2_unlock = True
    $ persistent.sayori_lunch_unlock = True
    $ persistent.sayori_room_tickle_unlock = True
    $ persistent.nozomi_argument_unlock = True
    $ persistent.sayori_fallen_unlock = True
    $ persistent.sayori_sleep_unlock = True
    $ persistent.sayori_sitting_unlock = True
    $ persistent.sayori_chicken1_unlock = True
    $ persistent.sayori_chicken2_unlock = True
    $ persistent.sayori_doll_bad_end_unlock = True

    $cheat_count = 4 #This makes sure the cheat cannot be activated again (no need) until the game is restarted
    call screen main_menu
