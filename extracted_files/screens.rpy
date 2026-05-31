################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


##Added this style to be able to click anywhere on the screen to toggle the UI back on the CG Gallery. Waldo.
style empty_button is default:
    background None
    foreground None

##Made this style based off of the navigation button text style that's used in the title screen, but with different colors
style cg_viewer_button is gui_button 

style cg_viewer_button_text is gui_button: #Since this is for text buttons, it's going to affect the arrows (< and >)
    size 50
    color "#ffffff"
    insensitive_color "#676464"  #The < and > buttons are programmed to be insensitive if we're on the first and last image, respectively, and they'll look gray when so
    outlines [ (3, "#000000", 1, 1) ]
    kerning 1
    hover_color "#d9e80d"
    selected_color "#18dfe6"
    yalign 0.5

style cg_viewer_text is gui_text: #Since this is for text, it will affect the little sign that shows which image out of how many we're in.
    size 40
    color "#ffffff"
    outlines [ (3, "#000000", 1, 1) ]
    kerning 1
    yalign 0.5 #I'm giving them a different yalign because, for some reason, they don't match by default

style cg_viewer_mobile_button_text is cg_viewer_button_text: #This style, to use in the mobile version, takes the cg_viewer_button_style as a base, and adds modification. For now, just the font size.
    size 80

style cg_viewer_mobile_text is cg_viewer_text: #Sme thing here but for cg_viewer_text
    size 64

style quick_mobile_cg_viewer_button_text is quick_button_text: #Making this style for the cg viewer quick menu out of the quick style
    size 30


##Created this transform to make the CG thumbnails grow bigger when you hover over them. This is for the thumbnails of single image CGs, as I'm leaving the old code for them.
transform cg_hover_zoom:
    anchor (0.5, 0.5)

    on idle:
        zoom 1.0

    on hover:
        zoom ((thumbnail_x + 15.0) / thumbnail_x)



##CG Button function. This function is made to create the image buttons that open the CG sets in the CG gallery.
init python:
    def cg_button(name): #Where "name" is the name of the CG
        
        unlocked = getattr(persistent, f"{name.replace(' ', '_')}_unlock", False) #You should have a variable called "name_of_the_CG_unlock" (underscores included), which is checked here
        offset_to_the_left = -10
        if unlocked:
            return ImageButton(
                idle_image=im.Scale(ImageReference(f"{name} butt"), thumbnail_x, thumbnail_y),
                hover_image=im.Scale(ImageReference(f"{name} butt"), thumbnail_x+15, thumbnail_y+15),#Making the size a little bigger when hovering.
                xalign=0.5,
                yalign=0.5,
                xoffset = offset_to_the_left,
                #bottom_margin=24,
                action=[
                    SetVariable("cg_group_name", name),
                    SetVariable("cg_index", 0),
                    ShowMenu("cg_viewer", _transition=dissolve),
                ]
            )

        else:
            return At(g_cg.make_button(
                f"{name}",
                f"{name} butt",
                im.Scale("cg locked.png", thumbnail_x, thumbnail_y),
                xalign=0.5, yalign=0.5,
                idle_border=None,
                background=None,
                xoffset = offset_to_the_left,
                #bottom_margin=24
            ), cg_hover_zoom )



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                xpos 0.185 #0.205
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    # if not renpy.variant("small"):
    add SideImage() xalign 0.0 yalign 1.0


style window is default

style say_thought is say_dialogue:
    color "#1d97a4"
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style namebox is default:
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style namebox_label is default:
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style say_dialogue:
    properties gui.text_properties("dialogue")
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1
    xpos 242 #gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

### CHOICE SCREEN

# How long the player has to make a choice in timeout seconds.
default timeout = 10.0

# The label the player is sent to if they fail to make a choice in the time
# allotted. If None, the timeout is disabled.
default timeout_label = None

# A preference that enables or disables timed choices.
default persistent.timed_choices = True

# screen choice(items):
#     style_prefix "choice"
#
#     vbox:
#         for i in items:
#             textbutton i.caption action i.action
#
#     if (timeout_label is not None) and persistent.timed_choices:
#
#         bar:
#             xalign 0.5
#             ypos 400
#             xsize 740
#             value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)
#
#         timer timeout action Jump(timeout_label)

screen choice:
    style_prefix "choice"

    vbox:
        for i in items:
            if i.action:
                if " (disabled)" in i.caption:
                    textbutton i.caption.replace(" (disabled)", "") text_color("#606060") xsize 840
                else:
                    textbutton i.caption action i.action xsize 840
            else:
                textbutton i.caption xsize 840

# screen choice:
#
#     window:
#         style "menu_window"
#         xalign 0.5
#         yalign 0.5
#
#         vbox:
#             style "menu"
#             spacing 2
#
#             for caption, action, chosen in items:
#
#                 if action:
#
#                     if " (disabled)" in caption:
#                         $ caption = caption.replace(" (disabled)", "")
#                         button:
#                             action None
#                             style "menu_choice_button"
#
#                             text caption style "menu_choice"
#                     else:
#                         button:
#                             action action
#                             style "menu_choice_button"
#
#                             text caption style "menu_choice"
#
#                 else:
#                     text caption style "menu_caption"

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

style choice_button is default:
    properties gui.button_properties("choice_button")
    xsize 1280

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

### Choice screen ###############################################################
###
### This screen is used to display the in-game choices presented by the menu
### statement. The one parameter, items, is a list of objects, each with caption
### and action fields.
###
### http://www.renpy.org/doc/html/screen_special.html#choice

# screen choice(items):
#    style_prefix "choice"
#
#    vbox:
#        for i in items:
#            if i.chosen:
#                textbutton i.caption style "choice_chosen_button" action i.action
#            else:
#                textbutton i.caption action i.action

define config.menu_include_disabled = True


### When this is true, menu captions will be spoken by the narrator. When false,
### menu captions will be displayed as empty buttons.
#define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
   xalign 0.5
   ypos 270
   yanchor 0.5

   spacing gui.choice_spacing

style choice_button is default:
   properties gui.button_properties("choice_button")

style choice_button_text is default:
   properties gui.button_text_properties("choice_button")

style choice_chosen_button is choice_button

style choice_chosen_button_text is choice_button_text:
    color "#1d97a4"
    # color "#959292"

# style choice_chosen_button_text is choice_button_text:
    # outlines [ (3, "#000000", 1, 1) ]
    # color "#9999cc"

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

# GALLERIES START
    #CG Gallery
    g_cg = Gallery()

    g_cg.button("titlescreen")
    g_cg.image("titlescreen")

    g_cg.button("kyou intro single image")
    g_cg.condition("persistent.kyou_intro_unlock")
    g_cg.image("cg kyou intro")

    g_cg.button("stageshow")
    g_cg.condition("persistent.stageshow_unlock")
    #g_cg.image("cg stageshow bw")
    #g_cg.image("cg stageshow")


    g_cg.button("classroom nozomi")
    g_cg.condition("persistent.classroom_nozomi_unlock")
    g_cg.image("cg classroom eve", "NozomiHypno folded stern")
    g_cg.image("cg classroom eve", "NozomiHypno folded angry")
    g_cg.image("cg classroom eve", "NozomiHypno standing confused")
    g_cg.image("cg classroom eve", "NozomiHypno standing drowsy")
    g_cg.image("cg classroom eve", "NozomiHypno drooping sleepy")
    g_cg.image("cg classroom eve", "NozomiHypno drooping sleepy arm_uniform ")
    g_cg.image("cg classroom eve", "NozomiHypno drooping sleep arm_uniform")
    g_cg.image("cg classroom eve", "NozomiHypno drooping sleeptalk arm_uniform")

    g_cg.button("hiroko_tennis1 single image")
    g_cg.condition("persistent.hiroko_tennis1_unlock")
    g_cg.image("cg hiroko_tennis1")

    g_cg.button("sayori intro")
    g_cg.condition("persistent.sayori_intro_unlock")
    g_cg.image("cg study room2 eve", "SayoriIntro suspicious_open")
    g_cg.image("cg study room2 eve", "SayoriIntro suspicious_closed")
    g_cg.image("cg study room2 eve", "SayoriIntro sigh")

    g_cg.button("sayori study")
    g_cg.condition("persistent.sayori_study_unlock")
    g_cg.image("SayoriStudy sayori1 talking")
    g_cg.image("SayoriStudy sayori2 sleep")
    g_cg.image("SayoriStudy sayori2 waking")
    g_cg.image("SayoriStudy sayori1 smile_side")
    g_cg.image("SayoriStudy sayori1 smile")

    g_cg.button("rooftop day")
    g_cg.condition("persistent.rooftop_day_unlock")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown surprised", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown surprised blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek angry", "RoofNozomi handsdown surprised blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek angry", "RoofNozomi handsdown smile blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown smile blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown smile_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown smile_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown smile_left blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown smile_left blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown smile_left blush", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown smile noblush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown smile_left noblush", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown smile_left noblush", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown laugh noblush", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown neutral_left noblush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown neutral_left noblush", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown neutral_left noblush", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown smile noblush", "RoofSayori leanforward smirk")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown smile noblush", "RoofSayori leanforward smirk")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown laugh noblush", "RoofSayori leanforward laugh")

    g_cg.button("alley hiroko")
    g_cg.condition("persistent.alley_hiroko_unlock")
    g_cg.image("cg alley eve", "HirokoHypno upright angry clenched_fists")
    g_cg.image("cg alley eve", "HirokoHypno upright frown clenched_fists")
    g_cg.image("cg alley eve", "HirokoHypno upright angry_up clenched_fists")
    g_cg.image("cg alley eve", "HirokoHypno upright drowsy clenched_fists")
    g_cg.image("cg alley eve", "HirokoHypno upright straining relaxed_fists")
    g_cg.image("cg alley eve", "HirokoHypno upright straining nofists")
    g_cg.image("cg alley eve", "HirokoHypno relaxed drowsy no_arm")
    g_cg.image("cg alley eve", "HirokoHypno relaxed sleepy_up_open arm_uniform")
    g_cg.image("cg alley eve", "HirokoHypno relaxed sleep arm_uniform")
    g_cg.image("cg alley eve", "HirokoHypno drooping sleep arm_uniform")
    g_cg.image("cg alley eve", "HirokoHypno drooping sleeptalk arm_uniform")
    g_cg.image("cg alley eve", "HirokoHypno relaxed entranced_neutral arm_uniform")
    g_cg.image("cg alley eve", "HirokoHypno relaxed entranced_neutral no_arm")
    g_cg.image("cg alley eve", "HirokoHypno relaxed entranced_talk no_arm")
    g_cg.image("cg alley eve", "HirokoHypno relaxed entranced_concerned no_arm")
    g_cg.image("cg alley eve", "HirokoHypno relaxed entranced_concerned_talk no_arm")

    g_cg.button("akiko science")
    g_cg.condition("persistent.akiko_science_unlock")
    g_cg.image("AkikoScience akiko1 neutral kyou1")
    g_cg.image("AkikoScience akiko1 confused kyou1")
    g_cg.image("AkikoScience akiko1 concerned kyou1")
    g_cg.image("AkikoScience akiko1 peaceful kyou1")
    g_cg.image("AkikoScience akiko1 frown kyou1")
    g_cg.image("AkikoScience akiko1 sigh kyou1")
    g_cg.image("AkikoScience akiko1 concerned_left kyou1")
    g_cg.image("AkikoScience akiko1 surprised kyou1")
    g_cg.image("AkikoScience akiko1 neutral kyou2")
    g_cg.image("AkikoScience akiko1 neutral2 kyou2 light")
    g_cg.image("AkikoScience akiko1 confused kyou2 light")
    g_cg.image("AkikoScience akiko1 confused2 kyou2 light")
    g_cg.image("AkikoScience akiko1 concerned kyou2 light")
    g_cg.image("AkikoScience akiko1 concerned2 kyou2 light")
    g_cg.image("AkikoScience akiko1 sleepy kyou2 light")
    g_cg.image("AkikoScience akiko1 sleepy2 kyou2 light")
    g_cg.image("AkikoScience akiko1 peaceful kyou2 light")
    g_cg.image("AkikoScience akiko2 sleep kyou2 light")
    g_cg.image("AkikoScience akiko2 sleep kyou2")
    g_cg.image("AkikoScience akiko2 sleep kyou1")
    g_cg.image("AkikoScience akiko2 sleeptalk kyou1")
    g_cg.image("AkikoScience akiko2 waking kyou1")
    g_cg.image("AkikoScience akiko1 surprised kyou1")
    g_cg.image("AkikoScience akiko1 smile kyou1")
    g_cg.image("AkikoScience akiko1 laugh blush kyou1")
    g_cg.image("AkikoScience akiko1 smile blush kyou1")

    g_cg.button("delusion rooftop")
    g_cg.condition("persistent.delusion_rooftop_unlock")
    g_cg.image("DelusionRooftop head_up curious")
    g_cg.image("DelusionRooftop head_up curious penlight")
    g_cg.image("DelusionRooftop head_up curious_light penlight")
    g_cg.image("DelusionRooftop head_up confused penlight")
    g_cg.image("DelusionRooftop head_up confused_light penlight")
    g_cg.image("DelusionRooftop head_up surprised penlight")
    g_cg.image("DelusionRooftop head_up surprised_light penlight")
    g_cg.image("DelusionRooftop head_up sleepy penlight")
    g_cg.image("DelusionRooftop head_up sleepy_light penlight")
    g_cg.image("DelusionRooftop head_down sleep penlight")
    g_cg.image("DelusionRooftop head_down sleep")
    g_cg.image("DelusionRooftop head_down sleeptalk")
    g_cg.image("DelusionRooftop head_down waking")
    g_cg.image("DelusionRooftop head_up curious")
    g_cg.image("DelusionRooftop head_up smile")
    g_cg.image("DelusionRooftop head_up surprised")

    g_cg.button("classroom lunch2 delusion")
    g_cg.condition("persistent.classroom_lunch2_delusion_unlock")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile s_frown hiroko1 h_frown")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral_right s_frown hiroko1 h_frown_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral_right s_neutral_right hiroko1 h_frown_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_happy s_neutral_right hiroko1 h_frown_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_happy s_neutral_right hiroko1 h_rolleyes")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_right hiroko1 h_rolleyes")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral s_neutral hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral s_neutral hiroko1 h_neutral")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral s_irritated hiroko1 h_neutral")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_concerned_side s_neutral_left hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_concerned_side s_neutral_left hiroko1 h_sad")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_left hiroko1 h_sad")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_smile_side s_neutral_left hiroko1 h_sad")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_pout s_neutral_left hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_pout s_irritated hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_sigh s_irritated hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_neutral_side s_neutral_left hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral s_frown hiroko1 h_frown")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_curious_right s_frown hiroko1 h_frown")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_curious_right s_frown hiroko1 h_rolleyes")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral_right s_sleep hiroko1 h_rolleyes")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral s_neutral hiroko1 h_neutral")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral s_neutral hiroko1 h_frown")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral s_smile_right hiroko1 h_frown")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral s_smile_right hiroko1 h_pout")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_curious s_neutral hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_curious s_neutral hiroko1 h_growl")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_curious s_neutral hiroko2 h_mad")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko2 h_mad")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko2 h_growl")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_happy n_blush s_worried hiroko2 h_frown_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_happy n_blush s_sleep hiroko1 h_frown_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_concerned_side s_irritated hiroko1 h_worried_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_concerned s_irritated hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_left hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_smile_side s_neutral_left hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_smile_side s_smile_left hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_smile_side s_smile_left hiroko1 h_happy")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile n_blush s_smile_left hiroko1 h_happy")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_sigh n_blush s_smile_left hiroko1 h_happy")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_sigh n_blush s_smile_left hiroko1 h_smirk_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_pout n_blush s_smile_left hiroko1 h_smirk_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_pout n_blush s_smile_left hiroko1 h_happy")

    g_cg.button("sports shed night")
    g_cg.condition("persistent.sports_shed_night_unlock")
    g_cg.image("cg sports shed night", "HirokoHypno upright tennis annoyed nofists")
    g_cg.image("cg sports shed night", "HirokoHypno upright tennis frown")
    g_cg.image("cg sports shed night", "HirokoHypno upright tennis angry clenched_fists_tennis")
    g_cg.image("cg sports shed night", "HirokoHypno upright tennis angry_up clenched_fists_tennis")
    g_cg.image("cg sports shed night", "HirokoHypno upright tennis annoyed_up nofists")
    g_cg.image("cg sports shed night", "HirokoHypno upright tennis angry clenched_fists_tennis")
    g_cg.image("cg sports shed night", "HirokoHypno upright tennis annoyed_up clenched_fists_tennis")
    g_cg.image("cg sports shed night", "HirokoHypno upright tennis surprised relaxed_fists_tennis")
    g_cg.image("cg sports shed night", "HirokoHypno upright tennis drowsy nofists")
    g_cg.image("cg sports shed night", "HirokoHypno relaxed tennis drowsy")
    g_cg.image("cg sports shed night", "HirokoHypno relaxed tennis sleep")
    g_cg.image("cg sports shed night", "HirokoHypno drooping tennis sleep")
    g_cg.image("cg sports shed night", "HirokoHypno drooping tennis sleeptalk")
    g_cg.image("cg sports shed night", "HirokoHypno relaxed tennis neutral")

    g_cg.button("classroomlunch2 1")
    #Regular version
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_laugh n_armup n_smile_left glasses sayori s_smile_nozomi")
    g_cg.condition("persistent.classroomlunch2_1_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_neutral_sayori n_armup n_smile_right glasses sayori s_smirk_hiroko")
    g_cg.condition("persistent.classroomlunch2_1_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_grin_sayori n_armup n_smile_left glasses sayori s_smirk_hiroko")
    g_cg.condition("persistent.classroomlunch2_1_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_grin_sayori n_folded n_thinking glasses sayori s_smirk_hiroko")
    g_cg.condition("persistent.classroomlunch2_1_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_grin_sayori n_folded n_smile_left glasses sayori s_smirk_hiroko")
    g_cg.condition("persistent.classroomlunch2_1_unlock")
    #Villainous variant
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_neutral_nozomi n_folded n_nervous glasses sayori s_neutral_nozomi")
    g_cg.condition("persistent.classroomlunch2_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_neutral_nozomi n_folded n_nervous_left glasses sayori s_neutral_nozomi")
    g_cg.condition("persistent.classroomlunch2_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_sad_nozomi n_folded n_nervous_left glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch2_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_sad_nozomi n_folded n_sigh glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch2_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_sad_nozomi n_folded n_sigh glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch2_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_sad_nozomi n_folded n_nervous_left glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch2_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_sad_nozomi n_folded n_nervous_right glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch2_2_unlock")

    g_cg.button("devotion start")
    g_cg.condition("persistent.devotion_start_unlock")
    g_cg.image("DevotionStart grimace kyou")
    g_cg.image("DevotionStart head_up angry kyou")
    g_cg.image("DevotionStart head_up surprised kyou")
    g_cg.image("DevotionStart head_down grimace blush_down kyou")
    g_cg.image("DevotionStart head_up smile blush_up kyou")
    g_cg.image("DevotionStart head_up surprised blush_up kyou")
    g_cg.image("DevotionStart head_up shocked kyou")
    g_cg.image("DevotionStart head_down cry blush_down kyou")
    g_cg.image("DevotionStart head_up hopeful blush_up kyou")
    g_cg.image("DevotionStart head_up joyous blush_up kyou")
    g_cg.image("DevotionStart head_up smile blush_up kyou")
    g_cg.image("DevotionStart head_up happy blush_up kyou")
    g_cg.image("DevotionStart head_up laugh blush_up kyou")
    g_cg.condition("persistent.devotion_start2_unlock") #The last two frames are unlocked if Kyou commits to this route
    g_cg.image("DevotionStart head_up smile blush_up")
    g_cg.image("DevotionStart head_up laugh blush_up")

    g_cg.button("robot start")
    g_cg.condition("persistent.robot_start_unlock")
    g_cg.image("RobotStart hiroko1 terrified")
    g_cg.image("RobotStart hiroko1 pleading")
    g_cg.image("RobotStart hiroko1 crying")
    g_cg.image("RobotStart hiroko2 head_down sobbing")
    g_cg.image("RobotStart hiroko2 head_up nervous")
    g_cg.image("RobotStart hiroko2 head_up shocked")

    g_cg.button("sleeper agent start")
    g_cg.condition("persistent.sleeper_agent_start_unlock")
    g_cg.image("SleeperAgentStart hiroko_yell kyou_grimace")
    g_cg.image("SleeperAgentStart hiroko_yell kyou_pain")
    g_cg.image("SleeperAgentStart hiroko_growl kyou_yell")

    g_cg.button("hiro walk devotion")
    g_cg.condition("persistent.hiro_walk_devotion_unlock")
    g_cg.image("HirokoWalk blush smile neutral")
    g_cg.image("HirokoWalk blush smile stern")
    g_cg.image("HirokoWalk blush laugh stern")
    g_cg.image("HirokoWalk blush happy stern")
    g_cg.image("HirokoWalk blush happy neutral")
    g_cg.image("HirokoWalk sad neutral")
    g_cg.condition("persistent.hiro_walk_robot_unlock")
    g_cg.image("HirokoWalk anxious neutral")
    g_cg.condition("persistent.hiro_walk_robot_unlock")
    g_cg.image("HirokoWalk anxious smirk")
    g_cg.condition("persistent.hiro_walk_robot_unlock")
    g_cg.image("HirokoWalk sigh smirk")
    g_cg.condition("persistent.hiro_walk_robot_unlock")
    g_cg.image("HirokoWalk frown smirk")
    g_cg.condition("persistent.hiro_walk_robot_unlock")

    g_cg.button("redemption start")
    g_cg.condition("persistent.redemption_start_unlock")
    g_cg.image("RedemptionStart")
    g_cg.image("RedemptionStart arm_down cry")
    g_cg.image("RedemptionStart arm_down fear")
    g_cg.image("RedemptionStart arm_down sad")
    g_cg.image("RedemptionStart arm_down angry")

    g_cg.button("devotion bedroom day2")
    g_cg.condition("persistent.devotion_bedroom_day2_unlock")
    g_cg.image("DevotionBedroom head_up_blush uniform_armsdown smile")
    g_cg.image("DevotionBedroom head_up_blush uniform_armsdown happy")
    g_cg.image("DevotionBedroom head_up uniform_armsdown confused")
    g_cg.image("DevotionBedroom head_up uniform_armsdown neutral_right")
    g_cg.image("DevotionBedroom head_up uniform_armsdown smile")
    g_cg.image("DevotionBedroom head_up uniform_armsdown frown")
    g_cg.image("DevotionBedroom head_up uniform_armsup sad")
    g_cg.image("DevotionBedroom head_up uniform_armsup frown_right")
    g_cg.image("DevotionBedroom head_up uniform_armsup laugh")
    g_cg.image("DevotionBedroom head_up_blush uniform_armsup laugh")
    g_cg.image("DevotionBedroom head_up_blush uniform_armsup smile")
    g_cg.image("DevotionBedroom head_up_blush uniform_armsdown sad")

    g_cg.button("hiroko robot programming")
    g_cg.condition("persistent.hiroko_robot_programming_unlock")
    g_cg.image("HirokoRobotProgramming")
    g_cg.image("HirokoRobotProgramming kyou")
    g_cg.image("HirokoRobotProgramming trancetalk kyou")
    g_cg.image("HirokoRobotProgramming trance kyou")
    g_cg.image("HirokoRobotProgramming head_side sleepy kyou")
    g_cg.image("HirokoRobotProgramming head_side awake kyou")

    g_cg.button("k bedroom hiroko 1")
    g_cg.condition("persistent.k_bedroom_hiroko_1_unlock")
    g_cg.image("cg k wall eve", "HirokoHypno upright neutral")
    g_cg.image("cg k wall eve", "HirokoHypno upright frown")
    g_cg.image("cg k wall eve", "HirokoHypno upright angry")
    g_cg.image("cg k wall eve", "HirokoHypno upright annoyed")
    g_cg.image("cg k wall eve", "HirokoHypno upright angry_up")
    g_cg.image("cg k wall eve", "HirokoHypno relaxed frown")
    g_cg.image("cg k wall eve", "HirokoHypno upright angry clenched_fists")
    g_cg.image("cg k wall eve", "HirokoHypno upright concerned relaxed_fists")
    g_cg.image("cg k wall eve", "HirokoHypno upright entranced_concerned_talk relaxed_fists")
    g_cg.image("cg k wall eve", "HirokoHypno relaxed entranced_neutral")
    g_cg.image("cg k wall eve", "HirokoHypno relaxed uniform sad_closed")
    g_cg.condition("persistent.k_bedroom_hiroko_2_unlock")
    g_cg.image("cg k wall eve", "HirokoHypno relaxed uniform sad")
    g_cg.condition("persistent.k_bedroom_hiroko_2_unlock")
    g_cg.image("cg k wall eve", "HirokoHypno relaxed uniform blush sad_closed")
    g_cg.condition("persistent.k_bedroom_hiroko_2_unlock")
    g_cg.image("cg k wall eve", "HirokoHypno relaxed uniform blush sad")
    g_cg.condition("persistent.k_bedroom_hiroko_2_unlock")
    g_cg.image("cg k wall eve", "HirokoHypno relaxed uniform blush sleeptalk")
    g_cg.condition("persistent.k_bedroom_hiroko_2_unlock")
    g_cg.image("cg k wall eve", "HirokoHypno relaxed uniform blush smile")
    g_cg.condition("persistent.k_bedroom_hiroko_2_unlock")
    g_cg.image("cg k wall eve", "HirokoHypno relaxed uniform noblush drowsy")
    g_cg.condition("persistent.k_bedroom_hiroko_2_unlock")
    g_cg.image("cg k wall eve", "HirokoHypno relaxed uniform noblush sleep")
    g_cg.condition("persistent.k_bedroom_hiroko_2_unlock")
    g_cg.image("cg k wall eve", "HirokoHypno drooping uniform noblush sleep")
    g_cg.condition("persistent.k_bedroom_hiroko_2_unlock")
    g_cg.image("cg k wall eve", "HirokoHypno drooping uniform noblush sleeptalk")
    g_cg.condition("persistent.k_bedroom_hiroko_2_unlock")
    g_cg.image("cg k wall eve", "HirokoHypno upright uniform noblush scared")
    g_cg.condition("persistent.k_bedroom_hiroko_2_unlock")

    g_cg.button("hiroko vs risa")
    g_cg.condition("persistent.hiroko_vs_risa_unlock")
    g_cg.image("Hiroko_vs_Risa hiroko")
    g_cg.image("Hiroko_vs_Risa hiroko frown")

    g_cg.button("akiko intro")
    g_cg.condition("persistent.akiko_intro_unlock")
    g_cg.image("AkikoIntro akiko2 worried")
    g_cg.image("AkikoIntro akiko2 sigh")
    g_cg.image("AkikoIntro akiko1 frown")
    g_cg.image("AkikoIntro akiko1 happy")
    g_cg.image("AkikoIntro akiko1 cheerful")
    g_cg.image("AkikoIntro akiko1 frown")
    g_cg.image("AkikoIntro akiko1 awkward")
    g_cg.image("AkikoIntro akiko1 smile")

    g_cg.button("nozomi cafe")
    g_cg.condition("persistent.nozomi_cafe_unlock")
    g_cg.image("NozomiCafe uniform_leaning pensive")
    g_cg.image("NozomiCafe uniform_leaning pensive_side")
    g_cg.image("NozomiCafe uniform_leaning pensive_closed")
    g_cg.image("NozomiCafe uniform_leaning anxious")
    g_cg.image("NozomiCafe uniform_leaning anxious_closed")
    g_cg.image("NozomiCafe uniform_leaning neutral")
    g_cg.image("NozomiCafe uniform_leaning stern")
    g_cg.image("NozomiCafe uniform_leaning stern_side")
    g_cg.image("NozomiCafe uniform_leaning smile")
    g_cg.image("NozomiCafe uniform_leaning smile_closed")
    g_cg.image("NozomiCafe uniform_leaning smirk")
    g_cg.image("NozomiCafe uniform_leaning surprised")
    g_cg.image("NozomiCafe uniform_leaning angry")
    g_cg.image("NozomiCafe uniform_folded pensive")
    g_cg.image("NozomiCafe uniform_folded pensive_side")
    g_cg.image("NozomiCafe uniform_folded pensive_closed")
    g_cg.image("NozomiCafe uniform_folded anxious")
    g_cg.image("NozomiCafe uniform_folded anxious_closed")
    g_cg.image("NozomiCafe uniform_folded neutral")
    g_cg.image("NozomiCafe uniform_folded stern")
    g_cg.image("NozomiCafe uniform_folded stern_side")
    g_cg.image("NozomiCafe uniform_folded smile")
    g_cg.image("NozomiCafe uniform_folded smile_closed")
    g_cg.image("NozomiCafe uniform_folded smirk")
    g_cg.image("NozomiCafe uniform_folded surprised")
    g_cg.image("NozomiCafe uniform_folded angry")
    g_cg.image("NozomiCafe uniform_leaning pensive blush")
    g_cg.image("NozomiCafe uniform_leaning pensive_side blush")
    g_cg.image("NozomiCafe uniform_leaning pensive_closed blush")
    g_cg.image("NozomiCafe uniform_leaning anxious blush")
    g_cg.image("NozomiCafe uniform_leaning anxious_closed blush")
    g_cg.image("NozomiCafe uniform_leaning neutral blush")
    g_cg.image("NozomiCafe uniform_leaning stern blush")
    g_cg.image("NozomiCafe uniform_leaning stern_side blush")
    g_cg.image("NozomiCafe uniform_leaning smile blush")
    g_cg.image("NozomiCafe uniform_leaning smile_closed blush")
    g_cg.image("NozomiCafe uniform_leaning smirk blush")
    g_cg.image("NozomiCafe uniform_leaning surprised blush")
    g_cg.image("NozomiCafe uniform_leaning angry blush")
    g_cg.image("NozomiCafe uniform_folded pensive blush")
    g_cg.image("NozomiCafe uniform_folded pensive_side blush")
    g_cg.image("NozomiCafe uniform_folded pensive_closed blush")
    g_cg.image("NozomiCafe uniform_folded anxious blush")
    g_cg.image("NozomiCafe uniform_folded anxious_closed blush")
    g_cg.image("NozomiCafe uniform_folded neutral blush")
    g_cg.image("NozomiCafe uniform_folded stern blush")
    g_cg.image("NozomiCafe uniform_folded stern_side blush")
    g_cg.image("NozomiCafe uniform_folded smile blush")
    g_cg.image("NozomiCafe uniform_folded smile_closed blush")
    g_cg.image("NozomiCafe uniform_folded smirk blush")
    g_cg.image("NozomiCafe uniform_folded surprised blush")
    g_cg.image("NozomiCafe uniform_folded angry blush")

    g_cg.button("room hiroko 1")
    g_cg.condition("persistent.room_hiroko_1_unlock")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis annoyed nofists")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis frown nofists")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis annoyed_up nofists")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis drowsy nofists")
    g_cg.image("cg k room eve", "HirokoHypno relaxed tennis sleepy_up_closed")
    g_cg.image("cg k room eve", "HirokoHypno relaxed tennis sleepy_up_open")
    g_cg.image("cg k room eve", "HirokoHypno drooping tennis sleep")
    g_cg.image("cg k room eve", "HirokoHypno drooping tennis sleeptalk")
    g_cg.image("cg k room eve", "HirokoHypno relaxed tennis drowsy")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis blush annoyed")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis blush sleeptalk")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis blush angry clenched_fists_tennis")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis blush frown")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis blush neutral")
    g_cg.condition("persistent.room_hiroko_2_unlock")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis angry blush")
    g_cg.condition("persistent.room_hiroko_2_unlock")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis blush surprised relaxed_fists_tennis")
    g_cg.condition("persistent.room_hiroko_2_unlock")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis blush scared relaxed_fists_tennis")
    g_cg.condition("persistent.room_hiroko_2_unlock")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis sleeptalk")
    g_cg.condition("persistent.room_hiroko_2_unlock")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis angry")
    g_cg.condition("persistent.room_hiroko_2_unlock")
    g_cg.image("cg k room eve", "HirokoHypno upright tennis blush annoyed_up")
    g_cg.condition("persistent.room_hiroko_2_unlock")
    g_cg.image("cg k room eve", "HirokoHypno relaxed tennis sleep")
    g_cg.condition("persistent.room_hiroko_2_unlock")
    g_cg.image("cg k room eve", "HirokoHypno relaxed tennis neutral")
    g_cg.condition("persistent.room_hiroko_2_unlock")


    g_cg.button("classroomlunch3")
    #Sayori version
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_sayori nozo_lunch n_folded n_curious_right glasses sayori s_neutral_nozomi_alert")
    g_cg.condition("persistent.classroomlunch3_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_sayori nozo_lunch n_folded n_curious_right glasses sayori s_sigh_alert")
    g_cg.condition("persistent.classroomlunch3_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_annoyed_sayori nozo_lunch n_folded n_curious_right glasses sayori s_sigh_alert")
    g_cg.condition("persistent.classroomlunch3_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_annoyed_sayori nozo_lunch n_armup n_sigh glasses sayori s_neutral_nozomi_alert")
    g_cg.condition("persistent.classroomlunch3_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_sayori nozo_lunch n_armup n_sigh glasses sayori s_neutral_nozomi_alert")
    g_cg.condition("persistent.classroomlunch3_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_sayori nozo_lunch n_armup n_smile_right glasses sayori s_neutral_nozomi_alert")
    g_cg.condition("persistent.classroomlunch3_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_grin_sayori nozo_lunch n_armup n_smile_right glasses sayori s_neutral_nozomi_alert")
    g_cg.condition("persistent.classroomlunch3_2_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_grin_sayori nozo_lunch n_armup n_smile_right glasses sayori s_smile_hiroko_alert")
    g_cg.condition("persistent.classroomlunch3_2_unlock")
    #Hiroko version
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_folded n_thinking glasses sayori s_neutral_nozomi")
    g_cg.condition("persistent.classroomlunch3_3_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_folded n_thinking glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch3_3_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_armup n_smile_left glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch3_3_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_smile_nozomi nozo_lunch n_armup n_smile_right glasses sayori s_smile_hiroko")
    g_cg.condition("persistent.classroomlunch3_3_unlock")
    #Villain version
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_folded n_thinking glasses sayori s_neutral_nozomi")
    g_cg.condition("persistent.classroomlunch3_4_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_folded n_thinking glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch3_4_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_nozomi nozo_lunch n_folded n_thinking glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch3_4_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_nozomi nozo_lunch n_armup n_nervous_left glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch3_4_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_worried_nozomi nozo_lunch n_armup n_nervous_left glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch3_4_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_worried_nozomi nozo_lunch n_folded n_sigh glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch3_4_unlock")
    g_cg.image("ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_folded n_sigh glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch3_4_unlock")

    #Sleeper Agent Night (Where Hiroko is re-hypnotized on the tennis court at the start of Kyou's plan to nab Sayori
    g_cg.button("sleeper agent night")
    g_cg.condition("persistent.sleeper_agent_night_unlock")
    g_cg.image("HirokoCourtNight hiroko_phone surprised kyou_arm_uniform kyou_uniform")
    g_cg.image("HirokoCourtNight hiroko_phone surprised_light kyou_arm_uniform kyou_uniform")
    g_cg.image("HirokoCourtNight hiroko_phone sleepy kyou_arm_uniform kyou_uniform")
    g_cg.image("HirokoCourtNight hiroko_phone sleepy_light kyou_arm_uniform kyou_uniform")
    g_cg.image("HirokoCourtNight hiroko_standing entranced kyou_arm_uniform kyou_uniform")
    g_cg.image("HirokoCourtNight hiroko_standing entranced kyou_uniform")
    g_cg.image("HirokoCourtNight hiroko_standing entranced_talk kyou_uniform")

    g_cg.button("k room nozomi 1 1")
    g_cg.condition("persistent.k_room_nozomi_1_1_unlock")
    g_cg.image("cg k room eve", "NozomiHypno standing uniform neutral")
    g_cg.image("cg k room eve", "NozomiHypno standing uniform stern_closed")
    g_cg.image("cg k room eve", "NozomiHypno standing uniform smile")
    g_cg.image("cg k room eve", "NozomiHypno folded uniform annoyed")
    g_cg.image("cg k room eve", "NozomiHypno standing uniform angry")
    g_cg.image("cg k room eve", "NozomiHypno standing uniform lookup")
    g_cg.image("cg k room eve", "NozomiHypno standing uniform drowsy")
    g_cg.image("cg k room eve", "NozomiHypno drooping uniform sleepy")
    g_cg.image("cg k room eve", "NozomiHypno drooping uniform sleep")
    g_cg.image("cg k room eve", "NozomiHypno drooping uniform sleeptalk")
    g_cg.image("cg k room eve", "NozomiHypno standing uniform bruise sad noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno standing uniform bruise neutral noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno drooping uniform bruise sleeptalk noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno standing uniform bruise confused noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno standing uniform bruise stern noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno standing uniform bruise annoyed noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno folded uniform bruise stern_closed noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno folded uniform bruise stern noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno folded uniform bruise angry noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno folded uniform bruise surprised noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno folded uniform bruise annoyed noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno folded uniform bruise neutral noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")
    g_cg.image("cg k room eve", "NozomiHypno folded uniform bruise smile noglasses")
    g_cg.condition("persistent.k_room_nozomi_1_2_unlock")

    g_cg.button("hiroko trapped")
    g_cg.condition("persistent.hiroko_trapped_unlock")
    g_cg.image("cg k room eve2", "HirokoTrapped Struggling")
    g_cg.image("cg k room eve2", "HirokoTrapped Kyou Struggling")
    g_cg.image("cg k room eve2", "HirokoTrapped Kyou Surprised")

    g_cg.button("hiroko tickle")
    g_cg.condition("persistent.hiroko_tickle_unlock")
    g_cg.image("HirokoTickle tickle")
    g_cg.image("HirokoTickle tickle karm_one")
    g_cg.image("HirokoTickle tickle hface_grimace karm_one")
    g_cg.image("HirokoTickle tickle harmdown_twitch hface_grimace karm_one")
    g_cg.image("HirokoTickle tickle harmdown_twitch hface_laugh karm_one")
    g_cg.image("HirokoTickle tickle harmup harmdown_notwitch hbodytwitch hface_laugh karm_one")
    g_cg.image("HirokoTickle tickle harmup harmdown_notwitch hbodytwitch hface_laugh karm_one kface_smirk")
    g_cg.image("HirokoTickle tickle harmup harmdown_notwitch hbodytwitch hface_laugh karm_two kface_smirk")

    g_cg.button("creepy hiroko")
    g_cg.condition("persistent.creepy_hiroko_unlock")
    g_cg.image("CreepyHiroko girls nozo_worried glasses hiro_excited")
    g_cg.image("CreepyHiroko girls nozo_nervous glasses hiro_laugh")
    g_cg.image("CreepyHiroko girls nozo_frown glasses hiro_worried")
    g_cg.image("CreepyHiroko girls nozo_angry glasses hiro_shocked")
    g_cg.image("CreepyHiroko hiroko hiro_fearful")
    g_cg.image("CreepyHiroko hiroko hiro_tearful")

    g_cg.button("hiroko couch argument")
    g_cg.condition("persistent.hiroko_couch_argument_unlock")
    g_cg.image("HirokoCouchArgument")
    g_cg.image("HirokoCouchArgument kyou_glare")
    g_cg.image("HirokoCouchArgument kyou_glare hiro_frown")
    g_cg.image("HirokoCouchArgument kyou_angry hiro_frown")
    g_cg.image("HirokoCouchArgument kyou_angry hiro_angry")

    g_cg.button("k room hiroko tv1")
    g_cg.condition("persistent.k_room_hiroko_tv1_unlock")
    g_cg.image("cg k room tv eve", "HirokoHypno upright tennis2 frown2 clenched_fists_tennis2")
    g_cg.image("cg k room tv eve", "HirokoHypno upright tennis2 angry2 clenched_fists_tennis2")
    g_cg.image("cg k room tv eve", "HirokoHypno upright tennis2 angry2")
    g_cg.image("cg k room tv eve", "HirokoHypno upright tennis2 sleeptalk")
    g_cg.image("cg k room tv eve", "HirokoHypno upright tennis2 sleep")
    g_cg.image("cg k room tv eve", "HirokoHypno upright tennis2 annoyed_up2")
    g_cg.image("cg k room tv eve", "HirokoHypno upright tennis2 annoyed2")
    g_cg.image("cg k room tv eve", "HirokoHypno upright tennis2 smirk2")
    g_cg.image("cg k room tv eve", "HirokoHypno upright tennis2 frown2")
    g_cg.condition("persistent.k_room_hiroko_tv2_unlock")
    g_cg.image("cg k room tv eve", "HirokoHypno upright tennis2 frown2 relaxed_fists_tennis2")
    g_cg.condition("persistent.k_room_hiroko_tv2_unlock")
    g_cg.image("cg k room tv eve", "HirokoHypno upright tennis2 neutral2")
    g_cg.condition("persistent.k_room_hiroko_tv2_unlock")


    g_cg.button("sayori arm")
    g_cg.condition("persistent.sayori_arm_unlock")
    g_cg.image("CouchHypno sayori_sleeping_down sleep")
    g_cg.image("CouchHypno sayori_sleeping_up sleep kyou_up")
    g_cg.image("CouchHypno sayori_sleeping_up sleeptalk kyou_up")
    g_cg.image("CouchHypno sayori_sleeping_up sleep kyou_down")
    g_cg.image("CouchHypno sayori_waking_up thinking")
    g_cg.image("CouchHypno sayori_waking_up sleepy")
    g_cg.image("CouchHypno sayori_waking_up surprised")
    g_cg.image("CouchHypno sayori_waking_up puzzled")
    g_cg.image("CouchHypno sayori_struggling frown")
    g_cg.image("CouchHypno sayori_struggling thinking")
    g_cg.image("CouchHypno sayori_waking_up thinking")
    g_cg.image("CouchHypno sayori_waking_up concerned")
    g_cg.image("CouchHypno sayori_waking_up thinking")
    g_cg.image("CouchHypno sayori_sleeping_up sleep")
    g_cg.image("CouchHypno sayori_sleeping_up sleeptalk")
    g_cg.image("CouchHypno sayori_waking_up concerned")
    g_cg.image("CouchHypno sayori_waking_up puzzled")
    g_cg.image("CouchHypno sayori_waking_up chuckle")
    g_cg.image("CouchHypno sayori_waking_up smile")
    g_cg.image("CouchHypno sayori_struggling thinking")
    g_cg.image("CouchHypno sayori_waking_up puzzled")
    g_cg.image("CouchHypno sayori_waking_up shocked")
    g_cg.image("CouchHypno sayori_waking_up shocked kyou_up")
    g_cg.image("CouchHypno sayori_waking_up surprised kyou_up")
    g_cg.image("CouchHypno sayori_waking_up sleepy kyou_up")
    g_cg.image("CouchHypno sayori_waking_up thinking kyou_up")
    g_cg.image("CouchHypno sayori_sleeping_up sleep kyou_up")
    g_cg.image("CouchHypno sayori_sleeping_down sleep kyou_down")
    g_cg.image("CouchHypno sayori_waking_down thinking")
    g_cg.image("CouchHypno sayori_waking_down sleepy")
    g_cg.image("CouchHypno sayori_waking_down smile")

    g_cg.button("nozomi mindtrick")
    g_cg.condition("persistent.nozomi_mindtrick_unlock")
    g_cg.image("CouchHypno nozomi n_smile glasses kyou_down")
    g_cg.image("CouchHypno nozomi n_grumpy glasses kyou_down")
    g_cg.image("CouchHypno nozomi n_angry_open glasses kyou_down")
    g_cg.image("CouchHypno nozomi n_surprised glasses kyou_point")
    g_cg.image("CouchHypno nozomi n_dazed glasses kyou_point")
    g_cg.image("CouchHypno nozomi n_tranced glasses kyou_point")
    g_cg.image("CouchHypno nozomi n_neutral glasses kyou_down")
    g_cg.image("CouchHypno nozomi n_puzzled glasses kyou_down")
    g_cg.image("CouchHypno nozomi_blush n_laugh glasses kyou_down")
    g_cg.image("CouchHypno nozomi_blush n_surprised glasses kyou_down")
    g_cg.image("CouchHypno nozomi_blush n_angry_closed glasses kyou_down")
    g_cg.image("CouchHypno nozomi_headclutch_blush n_angry_open glasses nozomi_armsup kyou_down")
    g_cg.image("CouchHypno nozomi_headclutch_blush n_angry_closed glasses nozomi_armsup kyou_down")
    g_cg.image("CouchHypno nozomi n_angry_closed glasses kyou_down")
    g_cg.image("CouchHypno nozomi n_surprised glasses kyou_down")
    g_cg.image("CouchHypno nozomi n_surprised glasses kyou_wave")
    g_cg.image("CouchHypno nozomi n_dazed glasses kyou_wave")
    g_cg.image("CouchHypno nozomi n_tranced glasses kyou_wave")
    g_cg.image("CouchHypno nozomi n_tranced glasses kyou_down")
    g_cg.image("CouchHypno nozomi n_drool glasses kyou_down")
    g_cg.image("CouchHypno nozomi n_drool glasses kyou_point")
    g_cg.image("CouchHypno nozomi n_drool glasses kyou_wave")
    g_cg.image("CouchHypno nozomi_sleep kyou_down")

    g_cg.button("zombie beginning")
    g_cg.condition("persistent.zombie_beginning_unlock")
    g_cg.image("ZombieBeginning")
    g_cg.image("ZombieBeginning arms_up")
    g_cg.image("ZombieBeginning arms_up angry")

    g_cg.button("nozomi injured")
    g_cg.condition("persistent.nozomi_injured_unlock")
    g_cg.image("NozomiInjured pain")
    g_cg.image("NozomiInjured worried")
    g_cg.image("NozomiInjured worried kyou")
    g_cg.image("NozomiInjured sigh kyou")

    g_cg.button("nozomi hiroko hug")
    g_cg.condition("persistent.nozomi_hiroko_hug_unlock")
    g_cg.image("NozomiHirokoHug nozomi_worried bruise1 hiroko_worried")
    g_cg.image("NozomiHirokoHug nozomi_irritated bruise1 hiroko_worried")
    g_cg.image("NozomiHirokoHug nozomi_irritated bruise1 hiroko_neutral")
    g_cg.image("NozomiHirokoHug nozomi_annoyed bruise1 hiroko_neutral")
    g_cg.image("NozomiHirokoHug nozomi_annoyed bruise1 hiroko_worried")
    g_cg.image("NozomiHirokoHug nozomi_worried bruise1 hiroko_worried")
    g_cg.image("NozomiHirokoHug girls2 nozomi_uncomfortable bruise2 hiroko_cry")
    g_cg.image("NozomiHirokoHug girls2 nozomi_uncomfortable bruise2 nozomi_blush2 hiroko_cry")
    g_cg.image("NozomiHirokoHug girls2 nozomi_shy bruise2 nozomi_blush2 hiroko_cry")
    g_cg.image("NozomiHirokoHug girls1 nozomi_smile bruise1 nozomi_blush1 hiroko_grin")
    g_cg.image("NozomiHirokoHug girls1 nozomi_happy bruise1 nozomi_blush1 hiroko_grin")
    g_cg.image("NozomiHirokoHug girls1 nozomi_happy bruise1 nozomi_blush1 hiroko_laugh")
    g_cg.image("NozomiHirokoHug girls1 nozomi_surprised bruise1 hiroko_laugh")
    g_cg.image("NozomiHirokoHug girls1 nozomi_annoyed bruise1 hiroko_smile")
    g_cg.image("NozomiHirokoHug girls1 nozomi_annoyed bruise1 hiroko_laugh hiroko_blush")
    g_cg.image("NozomiHirokoHug girls1 nozomi_annoyed bruise1 hiroko_neutral hiroko_blush")
    g_cg.image("NozomiHirokoHug girls1 nozomi_irritated bruise1 hiroko_neutral hiroko_blush")
    g_cg.image("NozomiHirokoHug girls1 nozomi_smile bruise1 hiroko_smile")
    g_cg.image("NozomiHirokoHug girls1 nozomi_squint bruise1 hiroko_smile")
    g_cg.image("NozomiHirokoHug girls1 nozomi_worried bruise1 hiroko_smile")

    g_cg.button("sayori lunch")
    g_cg.condition("persistent.sayori_lunch_unlock")
    g_cg.image("SayoriLunch neutral")
    g_cg.image("SayoriLunch sleep")
    g_cg.image("SayoriLunch annoyed")
    g_cg.image("SayoriLunch irritated")
    g_cg.image("SayoriLunch concerned")
    g_cg.image("SayoriLunch concerned_side")
    g_cg.image("SayoriLunch puzzled")
    g_cg.image("SayoriLunch sleepy")
    g_cg.image("SayoriLunch rolleyes")

    g_cg.button("sayori walk")
    g_cg.condition("persistent.sayori_walk_unlock")
    g_cg.image("SayoriWalk kyou_surprised sayori_smile")
    g_cg.image("SayoriWalk kyou_surprised sayori_concerned")
    g_cg.image("SayoriWalk kyou_sigh sayori_concerned")
    g_cg.image("SayoriWalk kyou_sigh sayori_neutral")
    g_cg.image("SayoriWalk kyou_neutral sayori_smirk")
    g_cg.image("SayoriWalk kyou_annoyed sayori_smirk")
    g_cg.image("SayoriWalk kyou_annoyed sayori_happy")
    g_cg.image("SayoriWalk kyou_neutral sayori_happy")
    g_cg.image("SayoriWalk kyou_neutral sayori_neutral")
    g_cg.image("SayoriWalk kyou_neutral sayori_smile")

    g_cg.button ("nozomi argument")
    g_cg.condition("persistent.nozomi_argument_unlock")
    g_cg.image("NozomiArgument arms_up furious")
    g_cg.image("NozomiArgument arms_up angry")
    g_cg.image("NozomiArgument arms_up irritated")
    g_cg.image("NozomiArgument arms_up frown")
    g_cg.image("NozomiArgument arms_up angry")
    g_cg.image("NozomiArgument arms_up sleepy poke")
    g_cg.image("NozomiArgument arms_down entranced poke")
    g_cg.image("NozomiArgument arms_up sleepy wave")
    g_cg.image("NozomiArgument arms_down entranced wave")
    g_cg.image("NozomiArgument arms_down sleepy")
    g_cg.image("NozomiArgument arms_down calmtalk")
    g_cg.image("NozomiArgument arms_down calm")

    g_cg.button ("sayori fallen")
    g_cg.condition("persistent.sayori_fallen_unlock")
    g_cg.image("SayoriFallen head_up fear")
    g_cg.image("SayoriFallen head_down")
    g_cg.image("SayoriFallen head_down tears")
    g_cg.image("SayoriFallen head_up crying")
    g_cg.image("SayoriFallen head_up crying blush")
    g_cg.image("SayoriFallen head_up concerned_side_crying blush")
    g_cg.image("SayoriFallen head_up concerned_crying blush")
    g_cg.image("SayoriFallen head_up crying_closed blush")
    g_cg.image("SayoriFallen head_up concerned_crying")
    g_cg.image("SayoriFallen head_up confused")
    g_cg.image("SayoriFallen head_up sigh")
    g_cg.image("SayoriFallen head_up neutral")
    g_cg.image("SayoriFallen head_up neutral blush")
    g_cg.image("SayoriFallen head_up sigh blush")
    g_cg.image("SayoriFallen head_up confused blush")
    g_cg.image("SayoriFallen head_up fear blush")
    g_cg.image("SayoriFallen head_up concerned blush")
    g_cg.image("SayoriFallen head_up concerned_side blush")
    g_cg.image("SayoriFallen head_up sleepy blush")
    g_cg.image("SayoriFallen head_up sleep blush")
    g_cg.image("SayoriFallen head_up sleep")

    g_cg.button ("sayori sleep")
    g_cg.condition("persistent.sayori_sleep_unlock")
    g_cg.image("SayoriSleep sleep")
    g_cg.image("SayoriSleep sleep kyou")
    g_cg.image("SayoriSleep waking kyou")

    g_cg.button ("sayori sitting")
    g_cg.condition("persistent.sayori_sitting_unlock")
    g_cg.image("SayoriSitting right_arm_down left_arm_down sayori_hair_down confused")
    g_cg.image("SayoriSitting right_arm_up left_arm_down sayori_hair_down surprised")
    g_cg.image("SayoriSitting right_arm_up left_arm_up sayori_hair_up confused")
    g_cg.image("SayoriSitting right_arm_up left_arm_up sayori_hair_up smile")
    g_cg.image("SayoriSitting right_arm_up left_arm_up sayori_hair_up happy")

    g_cg.button("sayori sleeper capture")
    g_cg.condition("persistent.sayori_sleeper_capture_unlock")
    g_cg.image("SayoriSleeperCapture hiro_tired sayori_head_up sayori_stern")
    g_cg.image("SayoriSleeperCapture hiro_tired sayori_head_up sayori_stern_flash")
    g_cg.image("SayoriSleeperCapture hiro_tired sayori_head_up sayori_startled")
    g_cg.image("SayoriSleeperCapture hiro_tired_flash sayori_head_up sayori_startled")
    g_cg.image("SayoriSleeperCapture hiro_angry sayori_head_up sayori_startled")
    g_cg.image("SayoriSleeperCapture hiro_angry sayori_head_up sayori_startled_flash")
    g_cg.image("SayoriSleeperCapture hiro_angry sayori_head_up sayori_angry")
    g_cg.image("SayoriSleeperCapture hiro_angry sayori_head_up sayori_angry_flash")
    g_cg.image("SayoriSleeperCapture hiro_surprised sayori_head_up sayori_angry")
    g_cg.image("SayoriSleeperCapture hiro_surprised sayori_head_up sayori_confused")
    g_cg.image("SayoriSleeperCapture hiro_surprised_flash sayori_head_up sayori_confused")
    g_cg.image("SayoriSleeperCapture hiro_sleepy sayori_head_up sayori_confused")
    g_cg.image("SayoriSleeperCapture hiro_sleepy_flash sayori_head_up sayori_confused")
    g_cg.image("SayoriSleeperCapture hiro_blank sayori_head_up sayori_confused")
    g_cg.image("SayoriSleeperCapture hiro_blank sayori_head_up sayori_confused_flash")
    g_cg.image("SayoriSleeperCapture hiro_blank sayori_head_up sayori_anxious")
    g_cg.image("SayoriSleeperCapture hiro_blank sayori_head_up sayori_anxious_flash")
    g_cg.image("SayoriSleeperCapture hiro_blank sayori_head_up sayori_sleepy")
    g_cg.image("SayoriSleeperCapture hiro_blank sayori_head_up sayori_sleepy_flash")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_right kyou_neutral hiro_blank sayori_head_up sayori_anxious")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_right kyou_neutral hiro_blank sayori_head_down sayori_sleep")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_down kyou_neutral hiro_blank sayori_head_down sayori_sleep")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_down kyou_neutral hiro_blank sayori_head_down sayori_sleeptalk")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_down kyou_smile hiro_blank sayori_head_down sayori_sleep")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_down kyou_smile hiro_blank sayori_head_up sayori_blank")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_both kyou_smile hiro_blank sayori_head_up sayori_blank")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_both kyou_grin hiro_blank sayori_head_up sayori_blank")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_down kyou_smile hiro_blank sayori_head_up sayori_blank")
    g_cg.image("SayoriSleeperCapture kyou kyou_phone kyou_smile hiro_blank sayori_head_up sayori_blank")
    g_cg.image("SayoriSleeperCapture kyou kyou_phone kyou_smile hiro_blank sayori_head_up sayori_blank_talk")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_down kyou_smile hiro_blank sayori_head_up sayori_blank")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_left kyou_neutral hiro_blank sayori_head_up sayori_blank")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_both kyou_neutral hiro_blank sayori_head_up sayori_blank")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_both kyou_neutral hiro_blank_talk sayori_head_up sayori_blank_talk")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_both kyou_grin hiro_blank sayori_head_up sayori_blank")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_both kyou_grin hiro_blank_talk sayori_head_up sayori_blank_talk")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_both kyou_smile hiro_blank sayori_head_up sayori_blank")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_both kyou_smile hiro_blank_talk sayori_head_up sayori_blank_talk")
    g_cg.image("SayoriSleeperCapture kyou kyou_arm_down kyou_smile hiro_blank sayori_head_up sayori_blank")

    g_cg.button("akiko student council hypno")
    g_cg.condition("persistent.akiko_student_council_hypno_unlock")
    g_cg.image("AkikoSC akiko arms_up surprised1 kyou")
    g_cg.image("AkikoSC akiko arms_up surprised1 kyou penlight")
    g_cg.image("AkikoSC akiko arms_up surprised2 kyou penlight")
    g_cg.image("AkikoSC akiko arms_up confused1 kyou penlight")
    g_cg.image("AkikoSC akiko arms_up confused2 kyou penlight")
    g_cg.image("AkikoSC akiko arms_down sleepy1 kyou penlight")
    g_cg.image("AkikoSC akiko arms_down sleepy2 kyou penlight")
    g_cg.image("AkikoSC akiko arms_down sleep kyou penlight")
    g_cg.image("AkikoSC akiko arms_down sleep kyou")
    g_cg.image("AkikoSC akiko arms_down sleeptalk kyou")
    g_cg.image("AkikoSC akiko arms_down nozomi sleep kyou")
    g_cg.condition("persistent.akiko_student_council_hypno2_unlock") #The second part is unlocked when Kyou commits to the "turn Akiko into Nozomi" path
    g_cg.image("AkikoSC akiko arms_down nozomi sleeptalk kyou")
    g_cg.condition("persistent.akiko_student_council_hypno2_unlock")

    g_cg.button("akiko student council hypno2")
    g_cg.condition("persistent.akiko_student_council_hypno3_unlock")
    g_cg.image("AkikoSC akiko2 arms_down excited1")
    g_cg.image("AkikoSC akiko2 arms_down excited1 penlight")
    g_cg.image("AkikoSC akiko2 arms_down excited2 penlight")
    g_cg.image("AkikoSC akiko2 arms_down smile1 penlight")
    g_cg.image("AkikoSC akiko2 arms_down smile2 penlight")
    g_cg.image("AkikoSC akiko2 arms_down sleepy1 penlight")
    g_cg.image("AkikoSC akiko2 arms_down sleepy2 penlight")
    g_cg.image("AkikoSC akiko2 arms_down sleep penlight")
    g_cg.image("AkikoSC akiko2 arms_down sleep")
    g_cg.image("AkikoSC akiko2 arms_down sleeptalk")
    g_cg.image("AkikoSC akiko2 arms_down smile1")

    g_cg.button("k room nozomi 2 1")
    g_cg.condition("persistent.k_room_nozomi_2_1_unlock")
    g_cg.image("cg k room eve", "NozomiHypno standing casual neutral")
    g_cg.image("cg k room eve", "NozomiHypno standing casual stern")
    g_cg.image("cg k room eve", "NozomiHypno standing casual sad")
    g_cg.image("cg k room eve", "NozomiHypno standing casual lookup")
    g_cg.image("cg k room eve", "NozomiHypno standing casual annoyed")
    g_cg.image("cg k room eve", "NozomiHypno standing casual stern_closed")
    g_cg.image("cg k room eve", "NozomiHypno standing casual surprised")
    g_cg.image("cg k room eve", "NozomiHypno standing casual angry blush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual confused noblush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual laugh noblush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual smile noblush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual smile_closed noblush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual sad blush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual laugh blush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual smile blush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual stern_closed blush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual stern blush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual confused blush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual lookup noblush")
    g_cg.image("cg k room eve", "NozomiHypno standing casual drowsy noblush")
    g_cg.image("cg k room eve", "NozomiHypno drooping casual sleepy noblush")
    g_cg.image("cg k room eve", "NozomiHypno drooping casual sleep noblush")
    g_cg.image("cg k room eve", "NozomiHypno drooping casual sleeptalk noblush")
    g_cg.image("cg k room eve", "NozomiHypno drooping casual sleep arm_uniform noblush")
    g_cg.condition("persistent.k_room_nozomi_2_2_unlock")
    # g_cg.unlock_image("cg k room eve", "NozomiHypno drooping casual sleeptalk arm_uniform")

    g_cg.button("classroomlunch4 1")
    #Nozomi Trance version
    g_cg.image("ClassroomLunch boy2_lunch hiroko h_laugh n_armup n_smile_left glasses sayori s_smile_hiroko")
    g_cg.condition("persistent.classroomlunch4_1_unlock")
    g_cg.image("ClassroomLunch boy2_lunch hiroko h_laugh n_armup n_sigh glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch4_1_unlock")
    g_cg.image("ClassroomLunch boy2_lunch hiroko h_worried_nozomi n_armup n_sigh glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch4_1_unlock")
    g_cg.image("ClassroomLunch boy2_lunch hiroko h_worried_nozomi n_armup n_curious_right glasses sayori s_sigh")
    g_cg.condition("persistent.classroomlunch4_1_unlock")
    g_cg.image("ClassroomLunch boy2_lunch hiroko h_grin_sayori n_armup n_curious_right glasses sayori s_sigh")
    g_cg.condition("persistent.classroomlunch4_1_unlock")
    g_cg.image("ClassroomLunch boy2_lunch hiroko h_neutral_nozomi n_folded n_frown_left glasses sayori s_neutral_nozomi")
    g_cg.condition("persistent.classroomlunch4_1_unlock")
    g_cg.image("ClassroomLunch boy2_lunch hiroko h_annoyed_sayori n_folded n_frown_left glasses sayori s_neutral_nozomi")
    g_cg.condition("persistent.classroomlunch4_1_unlock")
    g_cg.image("ClassroomLunch boy2_lunch hiroko h_grin_sayori n_folded n_sigh glasses sayori s_neutral_nozomi")
    g_cg.condition("persistent.classroomlunch4_1_unlock")
    g_cg.image("ClassroomLunch boy2_lunch hiroko h_grin_sayori n_folded n_sigh glasses sayori s_smirk_hiroko")
    g_cg.condition("persistent.classroomlunch4_1_unlock")

    g_cg.button("k room nozomi reversal1")
    g_cg.condition("persistent.k_room_nozomi_reversal1_unlock")
    g_cg.image("cg k room reversal", "NozomiReversal penlight casual smile")
    g_cg.image("cg k room reversal", "NozomiReversal penlight casual neutral")
    g_cg.image("cg k room reversal", "NozomiReversal penlight casual laugh")
    g_cg.condition("persistent.k_room_nozomi_reversal2_unlock")
    g_cg.image("cg k room reversal", "NozomiReversal penlight uniform neutral")
    g_cg.condition("persistent.k_room_nozomi_reversal3_unlock")
    g_cg.image("cg k room reversal", "NozomiReversal penlight uniform smile")
    g_cg.condition("persistent.k_room_nozomi_reversal3_unlock")

    g_cg.button("k room nozomi tv1")
    g_cg.condition("persistent.k_room_nozomi_tv1_unlock")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 smile2")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 laugh")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 smile_closed")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 neutral2")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 annoyed")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 stern2")
    g_cg.condition("persistent.k_room_nozomi_tv2_unlock")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 smile2 blush2")
    g_cg.condition("persistent.k_room_nozomi_tv3_unlock")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 smile_closed blush2")
    g_cg.condition("persistent.k_room_nozomi_tv3_unlock")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 confused2 blush2")
    g_cg.condition("persistent.k_room_nozomi_tv3_unlock")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 surprised2 blush2")
    g_cg.condition("persistent.k_room_nozomi_tv3_unlock")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 stern2 blush2")
    g_cg.condition("persistent.k_room_nozomi_tv3_unlock")
    g_cg.image("cg k room tv eve", "NozomiHypno standing casual2 laugh blush2")
    g_cg.condition("persistent.k_room_nozomi_tv3_unlock")
    g_cg.image("cg k room tv eve")
    g_cg.condition("persistent.k_room_nozomi_tv4_unlock")

    g_cg.button("hiroko reversal")
    g_cg.condition("persistent.hiroko_reversal_unlock")
    g_cg.image("cg k room reversal","HirokoReversal nervous")
    g_cg.image("cg k room reversal","HirokoReversal body nervous_side")
    g_cg.image("cg k room reversal","HirokoReversal body_blush angry")
    g_cg.image("cg k room reversal","HirokoReversal body angry")
    g_cg.image("cg k room reversal","HirokoReversal body neutral")
    g_cg.image("cg k room reversal","HirokoReversal body smirk")

    g_cg.button("hiroko cat 1")
    g_cg.condition("persistent.hiroko_cat_1_unlock")
    g_cg.image("cg k room ground eve", "Hiroko Cat happy")
    g_cg.image("cg k room ground eve", "Hiroko Cat dazed")
    g_cg.image("cg k room ground eve", "Hiroko Cat lying sleep")
    g_cg.image("cg k room ground eve", "Hiroko Cat lying waking")

    g_cg.button("hiroko cat 2")
    g_cg.condition("persistent.hiroko_cat_2_unlock")
    g_cg.image("Hiroko Cat2 light1")
    g_cg.image("Hiroko Cat2 hiroko1 annoyed light1")
    g_cg.image("Hiroko Cat2 hiroko1 surprised light2")
    g_cg.image("Hiroko Cat2 hiroko2 angry light2")
    g_cg.image("Hiroko Cat2 hiroko2 angry")
    g_cg.image("Hiroko Cat2 hiroko2 curious")

    g_cg.button("hiroko racket")
    g_cg.condition("persistent.hiroko_racket_unlock")
    g_cg.image("Hiroko Racket k_neutral r_neutral h_arm1 h_head1 h_sad")
    g_cg.image("Hiroko Racket k_neutral r_neutral h_arm1 h_head2 h_stern")
    g_cg.image("Hiroko Racket k_regretful r_neutral h_arm1 h_head2 h_stern")
    g_cg.image("Hiroko Racket k_annoyed r_neutral h_arm1 h_head2 h_stern")
    g_cg.image("Hiroko Racket k_annoyed r_grin h_arm1 h_head2 h_stern")
    g_cg.image("Hiroko Racket k_annoyed r_grin h_arm2 h_head2 h_angry")
    g_cg.image("Hiroko Racket k_smile r_grin h_arm2 h_head2 h_angry")
    g_cg.image("Hiroko Racket k_smile r_grin h_arm2 h_head2 h_neutral2")
    g_cg.image("Hiroko Racket k_smile r_smile h_arm2 h_head1 h_neutral1")
    g_cg.image("Hiroko Racket k_neutral r_smile h_arm2 h_head1 h_neutral1")
    g_cg.image("Hiroko Racket k_neutral r_neutral h_arm2 h_head2 h_neutral2")
    g_cg.image("Hiroko Racket k_smile r_neutral h_arm2 h_head2 h_neutral2")
    g_cg.image("Hiroko Racket k_smile r_grin h_arm2 h_head2 h_smile")

    g_cg.button("study room sayori")
    g_cg.condition("persistent.study_room_sayori_unlock")
    g_cg.image("cg study room eve", "SayoriHypno standing")
    g_cg.image("cg study room eve", "SayoriHypno standing smile")
    g_cg.image("cg study room eve", "SayoriHypno standing uniform_handsout smile")
    g_cg.image("cg study room eve", "SayoriHypno standing uniform_handsout stern")
    g_cg.image("cg study room eve", "SayoriHypno standing uniform_handsout neutral")
    g_cg.image("cg study room eve", "SayoriHypno standing uniform_handsout looking")
    g_cg.image("cg study room eve", "SayoriHypno standing uniform_handsout surprised")
    g_cg.image("cg study room eve", "SayoriHypno standing uniform_handsout drowsytalk")
    g_cg.image("cg study room eve", "SayoriHypno standing uniform_handsout drowsy")
    g_cg.image("cg study room eve", "SayoriHypno standing uniform drowsy")
    g_cg.image("cg study room eve", "SayoriHypno drooping uniform sleep")
    g_cg.image("cg study room eve", "SayoriHypno drooping sleeptalk")
    g_cg.image("cg study room eve", "SayoriHypno standing uniform_slumped noface")

    g_cg.button("k room sayori")
    g_cg.condition("persistent.k_room_sayori_unlock")
    g_cg.image("cg k room eve", "SayoriHypno standing alert_smile")
    g_cg.image("cg k room eve", "SayoriHypno standing alert_smile blush")
    g_cg.image("cg k room eve", "SayoriHypno standing alert_looking")
    g_cg.image("cg k room eve", "SayoriHypno standing alert_surprised")
    g_cg.image("cg k room eve", "SayoriHypno standing alert_drowsytalk")
    g_cg.image("cg k room eve", "SayoriHypno standing alert_drowsy")
    g_cg.image("cg k room eve", "SayoriHypno standing alert_sleep")
    g_cg.image("cg k room eve", "SayoriHypno standing alert_sleep blush")
    g_cg.image("cg k room eve", "SayoriHypno drooping alert_sleep")
    g_cg.image("cg k room eve", "SayoriHypno drooping alert_sleeptalk")
    g_cg.image("cg k room eve", "SayoriHypno drooping alert_sleeptalk blush")

    g_cg.button("sayori alter start")
    g_cg.condition("persistent.sayori_alter_start_unlock")
    g_cg.image("cg k bedroom eve1", "Sayori_K_Bedroom happy")
    g_cg.image("cg k bedroom eve1", "Sayori_K_Bedroom happy blush")
    g_cg.image("cg k bedroom eve1", "Sayori_K_Bedroom shy smile_side")
    g_cg.image("cg k bedroom eve1", "Sayori_K_Bedroom shy blush smile_side")
    g_cg.image("cg k bedroom eve1", "Sayori_K_Bedroom shy smile_front")
    g_cg.image("cg k bedroom eve1", "Sayori_K_Bedroom shy blush smile_front")
    g_cg.image("cg k bedroom eve1", "Sayori_K_Bedroom shy surprised")
    g_cg.image("cg k bedroom eve1", "Sayori_K_Bedroom shy blush surprised")

    g_cg.button("sayori greeting")
    g_cg.condition("persistent.sayori_greeting_unlock")
    g_cg.image("SayoriGreeting laugh")
    g_cg.image("SayoriGreeting cheerful")
    g_cg.image("SayoriGreeting neutral")
    g_cg.image("SayoriGreeting smile")
    g_cg.image("SayoriGreeting smile blush")

    g_cg.button("nozomisleepercapture")
    g_cg.condition("persistent.nozomisleepercapture_unlock")
    g_cg.image ("NozomiSleeperCapture")
    g_cg.image ("NozomiSleeperCapture nozo_scream_light")
    g_cg.image ("NozomiSleeperCapture hiro_angry")
    g_cg.image ("NozomiSleeperCapture hiro_angry nozo_scream_light")
    g_cg.image ("NozomiSleeperCapture nozo_screamup_light")
    g_cg.image ("NozomiSleeperCapture nozo_screamup")
    g_cg.image ("NozomiSleeperCapture hiro_angry nozo_screamup")
    g_cg.image ("NozomiSleeperCapture hiro_angry nozo_screamup_light")
    g_cg.image ("NozomiSleeperCapture hiro_angry nozo_sleepy")
    g_cg.image ("NozomiSleeperCapture hiro_angry nozo_sleepy sayo_angry")
    g_cg.image ("NozomiSleeperCapture hiro_angry nozo_sleepy_light sayo_angry")
    g_cg.image ("NozomiSleeperCapture nozo_subdued sayo_subdued sayo_angry hiro_subdued hiro_angry2 nozo_sleepy")
    g_cg.image ("NozomiSleeperCapture nozo_subdued sayo_subdued sayo_angry hiro_subdued hiro_angry2 nozo_sleepy_light")
    g_cg.image ("NozomiSleeperCapture nozo_subdued sayo_subdued sayo_angry hiro_subdued hiro_angry2 nozo_sleep")
    g_cg.image ("NozomiSleeperCapture nozo_subdued sayo_subdued sayo_angry hiro_subdued hiro_growl2 nozo_sleep")
    g_cg.image ("NozomiSleeperCapture nozo_subdued sayo_subdued sayo_surprised hiro_subdued hiro_surprised nozo_sleep")
    g_cg.image ("NozomiSleeperCapture nozo_subdued sayo_subdued sayo_surprised_light hiro_subdued hiro_surprised_light nozo_sleep")
    g_cg.image ("NozomiSleeperCapture nozo_subdued sayo_subdued sayo_entranced hiro_subdued hiro_entranced nozo_sleep")
    g_cg.image ("NozomiSleeperCapture nozo_subdued sayo_subdued sayo_entranced hiro_subdued hiro_entranced nozo_entranced")
    g_cg.image ("NozomiSleeperCapture nozo_standing sayo_standing sayo_blank hiro_standing hiro_blank nozo_blank glasses_standing")
    g_cg.image ("NozomiSleeperCapture nozo_standing sayo_standing sayo_blank hiro_standing hiro_blank nozo_blanktalk glasses_standing")
    g_cg.image ("NozomiSleeperCapture nozo_standing sayo_standing sayo_blank hiro_standing hiro_blank nozo_blank glasses_standing")
    g_cg.image ("NozomiSleeperCapture nozo_standing sayo_standing sayo_blanktalk hiro_standing hiro_blanktalk nozo_blanktalk glasses_standing")

    g_cg.button("delusion struggle sayori")
    g_cg.condition("persistent.delusion_struggle_sayori_unlock")
    g_cg.image("DelusionStruggleSayori")
    g_cg.image("DelusionStruggleSayori sayori_struggling s_angry_up_flash")
    g_cg.image("DelusionStruggleSayori sayori_struggling s_angry")
    g_cg.image("DelusionStruggleSayori sayori_struggling s_angry_up_flash")
    g_cg.image("DelusionStruggleSayori sayori_struggling s_angry_up")
    g_cg.image("DelusionStruggleSayori sayori_struggling s_angry_up k_concerned")
    g_cg.image("DelusionStruggleSayori sayori_struggling s_angry_up_flash k_concerned")
    g_cg.image("DelusionStruggleSayori sayori_struggling s_worried k_concerned")
    g_cg.image("DelusionStruggleSayori sayori_struggling s_worried_flash k_concerned")
    g_cg.image("DelusionStruggleSayori sayori_struggling s_worried k_calm")
    g_cg.image("DelusionStruggleSayori sayori_struggling s_worried_flash k_calm")
    g_cg.image("DelusionStruggleSayori sayori_relaxing s_worried k_calm")
    g_cg.image("DelusionStruggleSayori sayori_relaxing s_worried_flash k_calm")
    g_cg.image("DelusionStruggleSayori sayori_relaxing s_sleepy k_calm")
    g_cg.image("DelusionStruggleSayori sayori_relaxing s_sleepy_flash k_calm")

    g_cg.button("devotion tennis")
    #There's four different variations of this scene. May need to break this up >.<
    g_cg.condition("persistent.devotion_tennis_unlock")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown neutral_right")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown happy")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown confused")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown smile")
    g_cg.image("DevotionBedroom head_up tennis_armsdown neutral_right")
    g_cg.image("DevotionBedroom head_up tennis_armsdown happy")
    g_cg.image("DevotionBedroom head_up tennis_armsdown smile")
    g_cg.image("DevotionBedroom head_up tennis_armsup frown_right")
    g_cg.image("DevotionBedroom head_up tennis_armsup confused")
    g_cg.image("DevotionBedroom head_up tennis_armsdown confused")
    g_cg.image("DevotionBedroom head_up tennis_armsup sad")
    g_cg.image("DevotionBedroom head_up tennis_armsup cry")
    g_cg.image("DevotionBedroom head_up tennis_armsup neutral kyou_arm")
    g_cg.image("DevotionBedroom head_up tennis_armsdown neutral kyou_arm")
    g_cg.image("DevotionBedroom head_up tennis_armsdown awe kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsup smile kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsup sultry kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsup confused kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsup laugh kyou")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsup smile kyou")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown smile_light kyou")
    g_cg.image("DevotionBedroom head_up tennis_armsdown smile_light")
    g_cg.image("DevotionBedroom head_up tennis_armsdown neutral_light")
    g_cg.image("DevotionBedroom head_up tennis_armsdown straining")
    g_cg.image("DevotionBedroom head_up tennis_armsdown straining_light")
    g_cg.image("DevotionBedroom head_down tennis_armsdown sleep")
    g_cg.image("DevotionBedroom head_down tennis_armsdown sleeptalk")
    g_cg.image("DevotionBedroom head_down tennis_armsdown sleepy")
    g_cg.image("DevotionBedroom head_down tennis_holding awe_down")
    g_cg.image("DevotionBedroom head_up_blush tennis_holding sultry")
    g_cg.image("DevotionBedroom head_up_blush tennis_holding confused")
    #Tennis sans wristbands and socks variant
    g_cg.button("devotion tennis partial")
    g_cg.condition("persistent.devotion_tennis_partial_unlock")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsup_partial sad")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown_partial neutral_right")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown_partial sad")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown_partial cry")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown_partial confused")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown_partial smile")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown_partial happy")
    g_cg.image("DevotionBedroom head_up tennis_armsdown_partial neutral_right")
    g_cg.image("DevotionBedroom head_up tennis_armsdown_partial happy")
    g_cg.image("DevotionBedroom head_up tennis_armsdown_partial smile")
    g_cg.image("DevotionBedroom head_up tennis_armsup_partial frown_right")
    g_cg.image("DevotionBedroom head_up tennis_armsup_partial confused")
    g_cg.image("DevotionBedroom head_up tennis_armsdown_partial confused")
    g_cg.image("DevotionBedroom head_up tennis_armsup_partial sad")
    g_cg.image("DevotionBedroom head_up tennis_armsup_partial cry")
    g_cg.image("DevotionBedroom head_up tennis_armsup_partial neutral kyou_arm")
    g_cg.image("DevotionBedroom head_up tennis_armsdown_partial neutral kyou_arm")
    g_cg.image("DevotionBedroom head_up tennis_armsdown_partial awe kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsup_partial smile kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsup_partial sultry kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsup_partial confused kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsup_partial laugh kyou")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsup_partial smile kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush tennis_armsdown_partial smile_light kyou")
    g_cg.image("DevotionBedroom head_up tennis_armsdown_partial smile_light")
    g_cg.image("DevotionBedroom head_up tennis_armsdown_partial neutral_light")
    g_cg.image("DevotionBedroom head_up tennis_armsdown_partial straining")
    g_cg.image("DevotionBedroom head_up tennis_armsdown_partial straining_light")
    g_cg.image("DevotionBedroom head_down tennis_armsdown_partial sleep")
    g_cg.image("DevotionBedroom head_down tennis_armsdown_partial sleeptalk")
    g_cg.image("DevotionBedroom head_down tennis_armsdown_partial sleepy")
    g_cg.image("DevotionBedroom head_down tennis_holding_partial awe_down")
    g_cg.image("DevotionBedroom head_up_blush tennis_holding_partial sultry")
    g_cg.image("DevotionBedroom head_up_blush tennis_holding_partial confused")
    #Underwear variant
    g_cg.button("devotion underwear")
    g_cg.condition("persistent.devotion_underwear_unlock")
    g_cg.image("DevotionBedroom head_up_blush underwear_armsdown smile")
    g_cg.image("DevotionBedroom head_up_blush underwear_armsdown happy")
    g_cg.image("DevotionBedroom head_up_blush underwear_armsdown confused")
    g_cg.image("DevotionBedroom head_up underwear_armsdown neutral_right")
    g_cg.image("DevotionBedroom head_up underwear_armsdown happy")
    g_cg.image("DevotionBedroom head_up underwear_armsdown smile")
    g_cg.image("DevotionBedroom head_up underwear_armsup frown_right")
    g_cg.image("DevotionBedroom head_up underwear_armsup confused")
    g_cg.image("DevotionBedroom head_up underwear_armsdown confused")
    g_cg.image("DevotionBedroom head_up underwear_armsup sad")
    g_cg.image("DevotionBedroom head_up underwear_armsup cry")
    g_cg.image("DevotionBedroom head_up underwear_armsup neutral kyou_arm")
    g_cg.image("DevotionBedroom head_up underwear_armsdown neutral kyou_arm")
    g_cg.image("DevotionBedroom head_up underwear_armsdown awe kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush underwear_armsup smile kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush underwear_armsup sultry kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush underwear_armsup confused kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush underwear_armsup laugh kyou")
    g_cg.image("DevotionBedroom head_up_blush underwear_armsup happy kyou")
    g_cg.image("DevotionBedroom head_up_blush underwear_armsup smile kyou")
    g_cg.image("DevotionBedroom head_up_blush underwear_armsdown smile_light kyou")
    g_cg.image("DevotionBedroom head_up underwear_armsdown smile_light")
    g_cg.image("DevotionBedroom head_up underwear_armsdown neutral_light")
    g_cg.image("DevotionBedroom head_up underwear_armsdown straining")
    g_cg.image("DevotionBedroom head_up underwear_armsdown straining_light")
    g_cg.image("DevotionBedroom head_down underwear_armsdown sleep")
    g_cg.image("DevotionBedroom head_down underwear_armsdown sleeptalk")
    g_cg.image("DevotionBedroom head_down underwear_armsdown sleepy")
    g_cg.image("DevotionBedroom head_down underwear_holding awe_down")
    g_cg.image("DevotionBedroom head_up_blush underwear_holding sultry")
    g_cg.image("DevotionBedroom head_up_blush underwear_holding confused")
    #Naked variant
    g_cg.button("devotion naked")
    g_cg.condition("persistent.devotion_naked_unlock")
    g_cg.image("DevotionBedroom head_up_blush bare_armsdown smile")
    g_cg.image("DevotionBedroom head_up_blush bare_armsdown happy")
    g_cg.image("DevotionBedroom head_up_blush bare_armsdown confused")
    g_cg.image("DevotionBedroom head_up bare_armsdown neutral_right")
    g_cg.image("DevotionBedroom head_up bare_armsdown happy")
    g_cg.image("DevotionBedroom head_up bare_armsdown smile")
    g_cg.image("DevotionBedroom head_up bare_armsup frown_right")
    g_cg.image("DevotionBedroom head_up bare_armsup confused")
    g_cg.image("DevotionBedroom head_up bare_armsdown confused")
    g_cg.image("DevotionBedroom head_up bare_armsup sad")
    g_cg.image("DevotionBedroom head_up bare_armsup cry")
    g_cg.image("DevotionBedroom head_up bare_armsup neutral kyou_arm")
    g_cg.image("DevotionBedroom head_up bare_armsdown neutral kyou_arm")
    g_cg.image("DevotionBedroom head_up bare_armsdown awe kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush bare_armsup smile kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush bare_armsup sultry kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush bare_armsup confused kyou_arm")
    g_cg.image("DevotionBedroom head_up_blush bare_armsup laugh kyou")
    g_cg.image("DevotionBedroom head_up_blush bare_armsup happy kyou")
    g_cg.image("DevotionBedroom head_up_blush bare_armsup smile kyou")
    g_cg.image("DevotionBedroom head_up_blush bare_armsdown smile_light kyou")
    g_cg.image("DevotionBedroom head_up bare_armsdown smile_light")
    g_cg.image("DevotionBedroom head_up bare_armsdown neutral_light")
    g_cg.image("DevotionBedroom head_up bare_armsdown straining")
    g_cg.image("DevotionBedroom head_up bare_armsdown straining_light")
    g_cg.image("DevotionBedroom head_down bare_armsdown sleep")
    g_cg.image("DevotionBedroom head_down bare_armsdown sleeptalk")
    g_cg.image("DevotionBedroom head_down bare_armsdown sleepy")
    g_cg.image("DevotionBedroom head_down bare_holding awe_down")
    g_cg.image("DevotionBedroom head_up_blush bare_holding sultry")
    g_cg.image("DevotionBedroom head_up_blush bare_holding confused")

    g_cg.button("study room hypno sayori")
    g_cg.condition("persistent.study_room_hypno_sayori_unlock")
    g_cg.image("StudyRoomHypno hiroko1 h_happy sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko1 h_grin sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko2 h_grin h_blush1 sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko2 h_cheerful h_blush1 sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko2 h_happy h_blush1 sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko3 h_smug sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko3 h_smug sayori2 s_sleeptalk")
    g_cg.image("StudyRoomHypno hiroko3 h_smile_right sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko3 h_talking sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko3 h_smile_right sayori2 s_sleeptalk")
    g_cg.image("StudyRoomHypno hiroko3 h_smile sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko3 h_smile_right sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko3 h_smile_closed h_blush2 sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko3 h_smile_closed h_blush2 sayori2 s_sleeptalk")
    g_cg.image("StudyRoomHypno hiroko3 h_talking h_blush2 sayori2 s_sleep")
    g_cg.image("StudyRoomHypno hiroko3 h_smile_right h_blush2 sayori2 s_sleeptalk")
    g_cg.image("StudyRoomHypno hiroko3 h_smile_right sayori2 s_waking")
    g_cg.image("StudyRoomHypno hiroko3 h_laugh h_blush2 sayori2 s_waking")
    g_cg.image("StudyRoomHypno hiroko3 h_laugh h_blush2 sayori2 s_startled s_blush")

    g_cg.button("k phone robot")
    g_cg.condition("persistent.k_phone_robot_unlock")
    g_cg.image("KyouPhone bedroom uniform nozomi_fear")
    g_cg.image("KyouPhone bedroom uniform nozomi_sleepy")
    g_cg.image("KyouPhone bedroom uniform nozomi_sleepy_hiroko")

    g_cg.button("nozomi robot kiss single image")
    g_cg.condition("persistent.nozomi_robot_kiss_unlock")
    g_cg.image("cg nozomi robot kiss")

    g_cg.button("hiroko shoe")
    g_cg.condition("persistent.hiroko_shoe_unlock")
    g_cg.image("HirokoShoe pose1")
    g_cg.image("HirokoShoe pose2")
    g_cg.image("HirokoShoe pose3 neutral")
    g_cg.image("HirokoShoe pose3 happy")

    g_cg.button("hiroko yawn day")
    g_cg.condition("persistent.hiroko_yawn_day_unlock")
    g_cg.image("HirokoYawn day n_listening h_sitting h_neutral")
    g_cg.image("HirokoYawn day n_listening h_sitting h_frown")
    g_cg.image("HirokoYawn day n_listening h_yawning h_sleepy")
    g_cg.image("HirokoYawn day n_concerned h_yawning h_angry")
    g_cg.image("HirokoYawn day n_listening h_sitting h_frown_left")
    g_cg.image("HirokoYawn day n_concerned h_sitting h_frown_left")

    g_cg.button("classroom lunch2 sleeper")
    g_cg.condition("persistent.classroom_lunch2_sleeper_unlock")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_smile")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_neutral")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_frown_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko2 h_growl")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko2 h_growl")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko2 h_frown")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_right hiroko2 h_frown")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_right hiroko2 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_right hiroko1 h_worried_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko1 h_worried_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko1 h_frown_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_frown_right s_worried hiroko1 h_frown_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_frown_right s_worried hiroko1 h_worried_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_worried_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_worried")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_worried h_blush")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_sad h_blush")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_sad h_blush")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral_right s_neutral_right hiroko1 h_neutral_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_curious s_neutral hiroko1 h_neutral")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_curious s_neutral hiroko1 h_smirk")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_frown_right s_angry hiroko1 h_smirk")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_frown_right s_angry hiroko1 h_worried_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_pout s_frown hiroko1 h_worried_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_pout s_frown hiroko1 h_sad")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_frown_right s_frown hiroko1 h_sad")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_sad")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_worried")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_concerned s_neutral hiroko1 h_worried")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral s_neutral hiroko1 h_neutral")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile s_neutral hiroko1 h_neutral")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_neutral")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_smirk_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_neutral_side s_smile_right hiroko1 h_smirk_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_smile_side s_smile_right hiroko1 h_smirk_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_smile_side s_neutral_left hiroko1 h_smirk_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_smile_side s_sleep hiroko1 h_smirk_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_concerned_side s_sleep hiroko1 h_worried_left")
    g_cg.image("ClassroomLunch2 kyou nozomi2 n_concerned_side s_smile hiroko1 h_worried_left")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_neutral s_smile hiroko1 h_neutral")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_neutral")
    g_cg.image("ClassroomLunch2 kyou nozomi1 n_concerned s_smile hiroko1 h_neutral_left")

    g_cg.button("rooftop devotion")
    g_cg.condition("persistent.rooftop_devotion_unlock")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated smile blush", "RoofSayori leanforward smile blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated happy blush", "RoofSayori leanforward smile blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward smile blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward awe blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated happy blush", "RoofSayori leanforward smirk blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated smile blush", "RoofSayori leanforward smirk blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated smile blush", "RoofSayori leanforward frown blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward frown blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward determined blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated concerned blush", "RoofSayori leanforward frown blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated determined blush", "RoofSayori leanforward frown blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated determined blush", "RoofSayori leanforward determined blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated confused blush", "RoofSayori leanforward determined blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated confused blush", "RoofSayori leanforward determined_side blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated sad blush", "RoofSayori leanforward frown blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward surprised blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward cry blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated concerned blush", "RoofSayori leanforward cry blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated sad blush", "RoofSayori leanforward cry blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated sad blush", "RoofSayori leanforward angrycry blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated concerned blush", "RoofSayori leanforward angrycry blush")
    g_cg.image("cg rooftop day", "RoofHiroko infatuated determined blush", "RoofSayori leanforward determined blush")

    g_cg.button("rooftop robot")
    g_cg.condition("persistent.rooftop_robot_unlock")
    g_cg.image("RoofRobot h_neutral n_sleepy")
    g_cg.image("RoofRobot h_neutral_left n_neutral")
    g_cg.image("RoofRobot h_smile_left n_neutral")
    g_cg.image("RoofRobot h_smile_left n_confused")
    g_cg.image("RoofRobot h_neutral n_sleepy sayori s_stern")
    g_cg.image("RoofRobot h_neutral n_confused_right sayori s_stern_left")
    g_cg.image("RoofRobot h_neutral_right n_surprised sayori s_stern_left")
    g_cg.image("RoofRobot h_neutral_right n_surprised sayori s_concerned_left")
    g_cg.image("RoofRobot h_neutral_right n_confused_right sayori s_concerned_left")
    g_cg.image("RoofRobot h_neutral_right n_confused_right sayori s_concerned")
    g_cg.image("RoofRobot h_neutral_right n_confused_right sayori s_stern_left")
    g_cg.image("RoofRobot h_neutral_right n_sleepy sayori s_stern_left")
    g_cg.image("RoofRobot h_neutral_right n_sleepy sayori s_angry_left")
    g_cg.image("RoofRobot h_smile n_sleepy sayori s_angry_left")
    g_cg.image("RoofRobot h_smile n_sleepy sayori s_concerned_left")
    g_cg.image("RoofRobot h_neutral n_sleepy sayori s_concerned_left")
    g_cg.image("RoofRobot h_neutral n_sleepy sayori s_angry")
    g_cg.image("RoofRobot h_neutral n_sleepy sayori s_stern_left")
    g_cg.image("RoofRobot h_neutral_left n_neutral sayori s_stern_left")
    g_cg.image("RoofRobot h_smile n_neutral sayori s_stern_left")
    g_cg.image("RoofRobot h_smile n_confused_right sayori s_angry_left")
    g_cg.image("RoofRobot h_neutral n_confused_right sayori s_angry")
    g_cg.image("RoofRobot h_neutral n_neutral sayori s_angry")
    g_cg.image("RoofRobot h_neutral n_neutral sayori s_irritated")
    g_cg.image("RoofRobot h_neutral n_sleepy sayori s_concerned")
    g_cg.image("RoofRobot h_neutral n_neutral sayori s_concerned_left")
    g_cg.image("RoofRobot h_neutral n_smile_left sayori s_concerned_left")
    g_cg.image("RoofRobot h_neutral n_smile_right sayori s_concerned_left")
    g_cg.image("RoofRobot h_neutral n_smile_right sayori s_concerned")
    g_cg.image("RoofRobot h_neutral n_sigh")
    g_cg.image("RoofRobot h_neutral n_neutral")
    g_cg.image("RoofRobot h_neutral n_smile_left")

    g_cg.button("rooftop robot  girlfriend")
    g_cg.condition("persistent.rooftop_robot__girlfriend_unlock")
    g_cg.image("RoofRobotGF nozomi1 k_surprised k_blush n_happy n_blush1 h_neutral")
    g_cg.image("RoofRobotGF nozomi1 k_surprised k_blush n_smile1 n_blush1 h_neutral")
    g_cg.image("RoofRobotGF nozomi1 k_smile k_blush n_smile1 n_blush1 h_neutral")
    g_cg.image("RoofRobotGF nozomi1 k_smile k_blush n_confused1 n_blush1 h_neutral")
    g_cg.image("RoofRobotGF nozomi1 k_smile n_confused1 n_blush1 h_neutral")
    g_cg.image("RoofRobotGF nozomi1 k_smile n_confused1 h_neutral")
    g_cg.image("RoofRobotGF nozomi1 sayori s_frown k_surprised n_confused1 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_furious k_surprised n_surprised n_blush2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_worried k_surprised n_surprised n_blush2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_worried k_surprised n_confused2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_worried k_neutral n_confused2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_worried k_neutral n_neutral2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_frown k_neutral n_neutral2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_frown k_neutral n_confused2 n_blush2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_growl k_neutral n_confused2 n_blush2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_growl k_neutral n_confused2 h_smile")
    g_cg.image("RoofRobotGF nozomi2 sayori s_worried k_neutral n_confused2 h_smile")
    g_cg.image("RoofRobotGF nozomi2 sayori s_worried k_sigh n_confused2 h_smile")
    g_cg.image("RoofRobotGF nozomi2 sayori s_growl k_sigh n_confused2 h_smile")
    g_cg.image("RoofRobotGF nozomi2 sayori s_frown k_neutral n_confused2 h_smile")
    g_cg.image("RoofRobotGF nozomi2 sayori s_frown k_neutral n_neutral_left h_neutral_left")
    g_cg.image("RoofRobotGF nozomi2 sayori s_frown k_neutral n_neutral2 h_smile")
    g_cg.image("RoofRobotGF nozomi2 sayori s_growl k_neutral n_neutral2 h_smile")
    g_cg.image("RoofRobotGF nozomi2 sayori s_furious k_neutral n_neutral2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_furious k_smirk n_neutral2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_irritated k_smirk n_neutral2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_worried k_neutral n_neutral2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_frown k_neutral n_confused2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_frown k_smile n_neutral_left h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_frown k_smile n_smile_left h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_frown k_smile n_smile2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 sayori s_worried k_smile n_smile2 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 k_neutral n_confused2 h_neutral")
    g_cg.image("RoofRobotGF nozomi1 k_neutral n_sigh h_neutral")
    g_cg.image("RoofRobotGF nozomi1 k_sigh n_neutral1 h_neutral")
    g_cg.image("RoofRobotGF nozomi1 k_confused n_smile1 h_neutral")
    g_cg.image("RoofRobotGF nozomi2 k_confused n_neutral_right h_neutral")
    g_cg.image("RoofRobotGF nozomi2 k_smile n_neutral_right h_neutral_left")
    g_cg.image("RoofRobotGF nozomi2 k_smile n_neutral_right h_smile_left")
    g_cg.image("RoofRobotGF nozomi2 k_confused n_neutral_right h_neutral")
    g_cg.image("RoofRobotGF nozomi2 k_confused n_neutral_left h_neutral")
    g_cg.image("RoofRobotGF nozomi2 k_sigh n_neutral_left h_neutral")
    g_cg.image("RoofRobotGF nozomi1 k_sigh n_sigh h_neutral")
    g_cg.image("RoofRobotGF nozomi1 k_smile n_sigh h_neutral")
    g_cg.image("RoofRobotGF nozomi1 k_smile n_smile1 h_neutral")

    g_cg.button("hiroko yawn eve")
    g_cg.condition("persistent.hiroko_yawn_eve_unlock")
    g_cg.image("HirokoYawn eve e_neutral n_listening h_sitting h_sleepy")
    g_cg.image("HirokoYawn eve e_neutral n_concerned h_sitting h_yawn")
    g_cg.image("HirokoYawn eve e_curious n_shocked h_sleeping h_sleep")
    g_cg.image("HirokoYawn eve e_curious n_shocked h_sleeping h_waking")
    g_cg.image("HirokoYawn eve e_curious n_shocked h_sitting_blush h_panic")
    g_cg.image("HirokoYawn eve e_laugh n_shocked h_sitting_blush h_panic")
    g_cg.image("HirokoYawn eve e_laugh n_shocked h_sitting_blush h_sorry")
    g_cg.image("HirokoYawn eve e_laugh n_shocked h_sitting_blush h_sleepy")
    g_cg.image("HirokoYawn eve e_laugh n_shocked h_sitting_blush h_yawn")
    g_cg.image("HirokoYawn eve e_laugh n_shocked h_sleeping_blush h_sleep")
    g_cg.image("HirokoYawn eve e_laugh n_shocked h_sleeping_blush h_waking")
    g_cg.image("HirokoYawn eve e_laugh n_shocked h_sleeping_blush h_sleeptalk")
    g_cg.image("HirokoYawn eve e_laugh n_shocked h_sleeping h_sleep")

    g_cg.button("classroomlunch5 1")
    # Nozomi Zombie version
    g_cg.image("ClassroomLunch boy1 boy2_missing hiroko h_laugh n_armup n_smile_left sayori s_smile_hiroko")
    g_cg.condition("persistent.classroomlunch5_1_unlock")
    #Hiroko Ticklish Hands version
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_smile_sayori n_armup n_smile_right glasses sayori s_smile_nozomi")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_worried_nozomi n_armup n_smile_right glasses sayori s_smile_nozomi")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_worried_nozomi n_armup n_smile_left glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_sad_nozomi n_armup n_smile_left glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_worried_nozomi n_armup n_smile_left glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_worried_nozomi n_folded n_neutral_left glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_sad_nozomi n_folded n_smile_left glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_sad_nozomi n_folded n_smile_left glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_sad_nozomi n_folded n_frown_left glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_neutral_nozomi n_folded n_frown_left glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_sad_nozomi n_armup n_thinking glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_grin_nozomi n_armup n_thinking glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_furious hiroko h_grin_nozomi n_armup n_thinking glasses sayori s_concerned_nozomi")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_furious hiroko h_grin_nozomi n_armup n_nervous_left glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_furious hiroko h_worried_nozomi n_armup n_nervous_left glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_furious hiroko h_grin_nozomi n_folded n_thinking glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_furious hiroko h_grin_nozomi n_folded n_thinking glasses sayori s_pout")
    g_cg.condition("persistent.classroomlunch5_2_unlock")
    g_cg.image("ClassroomLunch boy1 boy2_missing k_nervous hiroko h_grin_nozomi n_folded n_smile_left glasses sayori s_neutral_hiroko")
    g_cg.condition("persistent.classroomlunch5_2_unlock")

    g_cg.button("hiroko tennis kiss single image")
    g_cg.condition("persistent.hiroko_tennis_kiss_unlock")
    g_cg.image("cg hiroko tennis kiss")

    g_cg.button("nozomi collapse single image")
    g_cg.condition("persistent.nozomi_collapse_unlock")
    g_cg.image("cg nozomi collapse")

    g_cg.button("study room nozomi")
    g_cg.condition("persistent.study_room_nozomi_unlock")
    g_cg.image("cg study room eve", "NozomiHypno standing stern")
    g_cg.image("cg study room eve", "NozomiHypno standing lookup")
    g_cg.image("cg study room eve", "NozomiHypno standing drowsy")
    g_cg.image("cg study room eve", "NozomiHypno drooping sleep")

    g_cg.button("study room hypno nozomi")
    g_cg.condition("persistent.study_room_hypno_nozomi_unlock")
    g_cg.image("StudyRoomHypno sayori1 s_neutral_right nozomi1 n_sleep")
    g_cg.image("StudyRoomHypno sayori1 s_neutral nozomi1 n_sleep")
    g_cg.image("StudyRoomHypno sayori1 s_surprised nozomi1 n_sleep")
    g_cg.image("StudyRoomHypno sayori1 s_smirk nozomi1 n_sleep")
    g_cg.image("StudyRoomHypno sayori1 s_neutral_right nozomi1 n_sleeptalk")
    g_cg.image("StudyRoomHypno sayori1 s_stern nozomi1 n_sleep")
    g_cg.image("StudyRoomHypno sayori1 s_quizzical nozomi1 n_sleep")
    g_cg.image("StudyRoomHypno sayori1 s_stern_right nozomi1 n_sleep")
    g_cg.image("StudyRoomHypno sayori1 s_thoughtful nozomi1 n_sleep")
    g_cg.image("StudyRoomHypno sayori1 s_smile nozomi1 n_sleep")
    g_cg.image("StudyRoomHypno sayori1 s_neutral_right nozomi1 n_sleepysmile")
    g_cg.image("StudyRoomHypno sayori1 s_neutral_right nozomi1 n_sleepysmile n_blush_low")
    g_cg.image("StudyRoomHypno sayori1 s_neutral_right nozomi2 n_startled n_blush_high")
    g_cg.image("StudyRoomHypno sayori1 s_smile_right nozomi2 n_startled n_blush_high")
    g_cg.image("StudyRoomHypno sayori1 s_smile_right nozomi2 n_smile_left")
    g_cg.image("StudyRoomHypno sayori1 s_neutral nozomi2 n_smile")
    g_cg.image("StudyRoomHypno sayori1 s_neutral nozomi2 n_neutral")
    g_cg.image("StudyRoomHypno sayori1 s_neutral nozomi2 n_neutral_left")
    g_cg.image("StudyRoomHypno sayori1 s_smile_right nozomi2 n_neutral_left")

    g_cg.button("nozomi chocolate")
    g_cg.condition("persistent.nozomi_chocolate_unlock")
    g_cg.image("NozomiChocolate arm1 choc1 contemplating")
    g_cg.image("NozomiChocolate arm1 choc1 disgusted")
    g_cg.image("NozomiChocolate arm1 choc1 chewing_disgusted")
    g_cg.image("NozomiChocolate arm1 choc1 confused")
    g_cg.image("NozomiChocolate arm1 choc1 confused_down")
    g_cg.image("NozomiChocolate arm2 choc1 confused_down")
    g_cg.image("NozomiChocolate arm2 choc1 confused")
    g_cg.image("NozomiChocolate arm1 choc1 determined")
    g_cg.image("NozomiChocolate arm1 choc2 chewing_disgusted")
    g_cg.image("NozomiChocolate arm1 choc2 disgusted")
    g_cg.image("NozomiChocolate arm1 choc2 confused")
    g_cg.image("NozomiChocolate arm1 choc2 blank")
    g_cg.image("NozomiChocolate arm1 choc2 chewing")
    g_cg.image("NozomiChocolate arm1 choc2 happy blush")
    g_cg.image("NozomiChocolate arm2 choc2 happy blush")
    g_cg.image("NozomiChocolate arm2 choc2 laugh blush")
    g_cg.image("NozomiChocolate arm2 choc2 grin blush")
    g_cg.image("NozomiChocolate arm2 choc2 confused blush")

    g_cg.button("zombie bedroom 1 1")
    g_cg.condition("persistent.zombie_bedroom_1_1_unlock")
    g_cg.image("NozomiBedroom1 neutral bruise arm_up shadow")
    g_cg.image("NozomiBedroom1 frown bruise arm_up shadow")
    g_cg.image("NozomiBedroom1 sleep bruise arm_up shadow")
    g_cg.image("NozomiBedroom1 concerned bruise arm_up shadow")
    g_cg.image("NozomiBedroom1 sigh bruise arm_up shadow")
    g_cg.image("NozomiBedroom1 pout bruise blush arm_up shadow")
    g_cg.image("NozomiBedroom1 concerned_side bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 pout bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 concerned_side bruise arm_up shadow")
    g_cg.image("NozomiBedroom1 surprised bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 afraid bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 frown_side bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 sleep bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 frown bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 concerned bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 sigh bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 afraid bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 neutral bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 neutral_side bruise arm_down shadow")
    g_cg.image("NozomiBedroom1 neutral_light bruise arm_down shadow")
    g_cg.condition("persistent.zombie_bedroom_1_2_unlock")
    g_cg.image("NozomiBedroom1 dazed_closed bruise arm_down shadow")
    g_cg.condition("persistent.zombie_bedroom_1_2_unlock")
    g_cg.image("NozomiBedroom1 dazed_light bruise arm_down shadow")
    g_cg.condition("persistent.zombie_bedroom_1_2_unlock")
    g_cg.image("NozomiBedroom1 dazed_open bruise arm_down shadow")
    g_cg.condition("persistent.zombie_bedroom_1_2_unlock")
    g_cg.image("NozomiBedroom1 smile bruise arm_down shadow")
    g_cg.condition("persistent.zombie_bedroom_1_2_unlock")
    g_cg.image("NozomiBedroom1 pout bruise blush arm_down shadow")
    g_cg.condition("persistent.zombie_bedroom_1_3_unlock")
    g_cg.image("NozomiBedroom1 frown_side bruise blush arm_down shadow")
    g_cg.condition("persistent.zombie_bedroom_1_3_unlock")
    g_cg.image("NozomiBedroom1 sigh bruise blush arm_down shadow")
    g_cg.condition("persistent.zombie_bedroom_1_3_unlock")
    g_cg.image("NozomiBedroom1 concerned_side bruise blush arm_down shadow")
    g_cg.condition("persistent.zombie_bedroom_1_3_unlock")

    g_cg.button("zombie bedroom 2")
    g_cg.condition("persistent.zombie_bedroom_2_unlock")
    g_cg.image("NozomiBedroom2 a_concerned nozomi1 n_anxious blush")
    g_cg.image("NozomiBedroom2 a_concerned nozomi2 n_confused blush")
    g_cg.image("NozomiBedroom2 a_surprised nozomi3 n_sleep")
    g_cg.image("NozomiBedroom2 a_concerned_up nozomi3 n_sleep")
    g_cg.image("NozomiBedroom2 a_neutral nozomi3 n_sleeptalk")
    g_cg.image("NozomiBedroom2 a_concerned nozomi1 n_anxious")
    g_cg.image("NozomiBedroom2 a_concerned nozomi1 n_smile blush")
    g_cg.image("NozomiBedroom2 a_surprised nozomi1 n_surprised blush")
    g_cg.image("NozomiBedroom2 a_surprised nozomi1 n_sigh blush")
    g_cg.image("NozomiBedroom2 a_concerned nozomi1 n_sigh blush")
    g_cg.image("NozomiBedroom2 a_concerned nozomi1 n_annoyed blush")
    g_cg.image("NozomiBedroom2 a_laugh nozomi1 n_annoyed blush")
    g_cg.image("NozomiBedroom2 a_smile_up nozomi1 n_anxious blush")
    g_cg.image("NozomiBedroom2 a_smile_up nozomi1 n_sigh blush")
    g_cg.image("NozomiBedroom2 a_smile nozomi1 n_sigh blush")
    g_cg.image("NozomiBedroom2 a_laugh nozomi1 n_sigh blush")
    g_cg.image("NozomiBedroom2 a_laugh nozomi1 n_anxious blush")
    g_cg.image("NozomiBedroom2 a_smile nozomi1 n_anxious blush")
    g_cg.image("NozomiBedroom2 a_smile nozomi1 n_smile_left blush")

    g_cg.button("zombie bedroom 3")
    g_cg.condition("persistent.zombie_bedroom_3_unlock")
    g_cg.image("NozomiBedroom3 troubled")
    g_cg.image("NozomiBedroom3 troubledtalk")
    g_cg.image("NozomiBedroom3 sleeptalk")
    g_cg.image("NozomiBedroom3 sleep")

    g_cg.button("nozomi boardgame")
    g_cg.condition("persistent.nozomi_boardgame_unlock")
    g_cg.image("NozomiBoardgame smile")
    g_cg.image("NozomiBoardgame pout")
    g_cg.image("NozomiBoardgame blank")
    g_cg.image("NozomiBoardgame laugh")

    g_cg.button("nozomi boardgame2")
    g_cg.condition("persistent.nozomi_boardgame2_unlock")
    g_cg.image("NozomiBoardgame2 hands_cards smug")
    g_cg.image("NozomiBoardgame2 hands_cards smirk")
    g_cg.image("NozomiBoardgame2 hands_cards laugh")
    g_cg.image("NozomiBoardgame2 hands_cards smile")
    g_cg.image("NozomiBoardgame2 hands_cards confused")
    g_cg.image("NozomiBoardgame2 hands_cards blank")
    g_cg.image("NozomiBoardgame2 hands_cards surprised blush")
    g_cg.image("NozomiBoardgame2 hands_cards confused blush")
    g_cg.image("NozomiBoardgame2 hands_cards annoyed blush")
    g_cg.image("NozomiBoardgame2 hands_cards neutral")
    g_cg.image("NozomiBoardgame2 hands_cards sigh")
    g_cg.image("NozomiBoardgame2 hands_cards frown")
    g_cg.image("NozomiBoardgame2 hands_cards concerned")
    g_cg.image("NozomiBoardgame2 hands_cards angry")
    g_cg.image("NozomiBoardgame2 hands_down smirk")
    g_cg.image("NozomiBoardgame2 hands_down smile")
    g_cg.image("NozomiBoardgame2 hands_down laugh")
    g_cg.image("NozomiBoardgame2 hands_up smug")
    g_cg.image("NozomiBoardgame2 hands_up surprised")
    g_cg.image("NozomiBoardgame2 hands_up angry")
    g_cg.image("NozomiBoardgame2 hands_down sigh")
    g_cg.image("NozomiBoardgame2 hands_down annoyed")
    g_cg.image("NozomiBoardgame2 hands_up sigh")
    g_cg.image("NozomiBoardgame2 hands_up smile")
    g_cg.image("NozomiBoardgame2 hands_up confused")
    g_cg.image("NozomiBoardgame2 hands_up neutral")
    g_cg.image("NozomiBoardgame2 hands_up frown")
    g_cg.image("NozomiBoardgame2 hands_up annoyed")
    g_cg.image("NozomiBoardgame2 hands_up surprised")
    g_cg.image("NozomiBoardgame2 hands_up confused")
    g_cg.image("NozomiBoardgame2 hands_up concerned blush")
    g_cg.image("NozomiBoardgame2 hands_up frown blush")
    g_cg.image("NozomiBoardgame2 hands_up angry blush")
    g_cg.image("NozomiBoardgame2 hands_up concerned blush")
    g_cg.image("NozomiBoardgame2 hands_up concerned_light blush")
    g_cg.image("NozomiBoardgame2 hands_up neutral_light")
    g_cg.image("NozomiBoardgame2 hands_down neutral")
    g_cg.image("NozomiBoardgame2 hands_down neutral_light")
    g_cg.image("NozomiBoardgame2 hands_down sleepy")
    g_cg.image("NozomiBoardgame2 hands_down sleepy_light")

    g_cg.button("nozomi hypnobondage") #Formerly known as "n bedroom hypnobondage"
    g_cg.condition("persistent.nozomi_hypnobondage_unlock")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised surprised feet2 motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised surprised feet3 motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet1 motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet2 norope motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet3 norope motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet3 ghostrope motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised_blush angry feet1 norope motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised_blush angry feet2 norope motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised_blush angry feet3 norope motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon ghostrope")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet2 ghostrope motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised_blush angry feet3 ghostrope motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon fullrope")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet2 fullrope motionlines")
    g_cg.image("cg n bedroom floor day", "NozomiHypnoBon raised_blush angry feet3 fullrope motionlines")

    g_cg.button("nozomi hypnobondage tickling")
    g_cg.condition("persistent.nozomi_hypnobondage_tickling_unlock")
    g_cg.image("NozomiHypnoBon2 kyou_blush")
    g_cg.image("NozomiHypnoBon2 kyou_smirk kyou_blush")
    g_cg.image("NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smirk kyou_blush")
    g_cg.image("NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smile rope")
    g_cg.image("NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smile")
    #Tickle and Spank variants start here
    g_cg.image("NozomiHypnoBon2 nozo_shocked nozo_noblush motionlines kyou_smirk arm_tickle")
    g_cg.image("NozomiHypnoBon2 nozo_chuckle nozo_noblush motionlines kyou_smirk arm_tickle")
    g_cg.image("NozomiHypnoBon2 nozo_growl nozo_noblush motionlines kyou_smirk")
    g_cg.image("NozomiHypnoBon2 nozo_mad nozo_noblush motionlines kyou_smirk")
    g_cg.image("NozomiHypnoBon2 nozo_mad nozo_noblush motionlines kyou_smirk arm_tickle")
    g_cg.image("NozomiHypnoBon2 nozo_annoyed nozo_blush motionlines kyou_smirk arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_annoyed nozo_blush motionlines kyou_laugh arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_growl nozo_blush motionlines kyou_laugh arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_growl nozo_blush motionlines kyou_smirk arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_giggle nozo_blush motionlines kyou_smirk arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_laugh nozo_blush motionlines kyou_smirk arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_laugh nozo_blush motionlines kyou_smile arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_giggle nozo_blush motionlines kyou_smile arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_giggle nozo_blush motionlines kyou_laugh arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_growl nozo_blush motionlines kyou_smirk arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_laugh nozo_blush motionlines kyou_smirk arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_laugh nozo_blush motionlines kyou_smile arm_up feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_smirk arm_up feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_sigh nozo_noblush nolines kyou_smirk arm_up feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_shocked nozo_blush nolines kyou_smirk arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_chuckle nozo_blush nolines kyou_smile arm_up feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_smile arm_up feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_smirk arm_up feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_annoyed nozo_blush nolines kyou_smirk arm_up feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_shocked nozo_blush nolines kyou_smirk arm_tickle feet_squirm")
    g_cg.image("NozomiHypnoBon2 kyou_nervous arm_up head_up feet_rest nozo_noblush nozo_noface noglasses")


    g_cg.button("nozomi hypnobondage spanking")
    g_cg.condition("persistent.nozomi_hypnobondage_spanking_unlock")
    g_cg.image("NozomiHypnoBon2 kyou_blush")
    g_cg.image("NozomiHypnoBon2 kyou_smirk kyou_blush")
    g_cg.image("NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smirk kyou_blush")
    g_cg.image("NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smile rope")
    g_cg.image("NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smile")
    g_cg.image("NozomiHypnoBon2 nozo_shocked nozo_noblush nolines kyou_smirk arm_spank")
    g_cg.image("NozomiHypnoBon2 nozo_shocked nozo_noblush nolines kyou_annoyed kyou_blush arm_up")
    g_cg.image("NozomiHypnoBon2 nozo_growl nozo_noblush nolines kyou_annoyed kyou_noblush arm_up")
    g_cg.image("NozomiHypnoBon2 nozo_growl nozo_noblush nolines kyou_smirk arm_up")
    g_cg.image("NozomiHypnoBon2 nozo_shocked nozo_blush motionlines kyou_smirk arm_spank feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_shocked nozo_blush motionlines kyou_smirk arm_rest feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_growl nozo_blush motionlines kyou_smirk arm_rest feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_growl nozo_blush motionlines kyou_smirk kyou_blush arm_up feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_pain nozo_blush motionlines kyou_smirk kyou_blush arm_spank feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_mad nozo_blush motionlines kyou_smirk kyou_blush arm_rest feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_mad nozo_blush nolines kyou_smirk kyou_blush arm_rest feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_growl nozo_blush nolines kyou_smirk kyou_blush arm_rest feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_growl nozo_blush nolines kyou_annoyed kyou_blush arm_up feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_shocked nozo_blush nolines kyou_annoyed kyou_blush arm_spank feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_grimace nozo_blush nolines kyou_annoyed kyou_noblush arm_rest feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_mad nozo_blush nolines kyou_annoyed kyou_noblush arm_up feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_pain nozo_blush motionlines kyou_annoyed kyou_noblush arm_spank feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_worried nozo_blush nolines kyou_annoyed kyou_noblush arm_up feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_pain nozo_blush motionlines kyou_annoyed kyou_noblush arm_spank feet_squirm")
    g_cg.image("NozomiHypnoBon2 nozo_annoyed nozo_blush nolines kyou_annoyed kyou_noblush arm_up feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_worried nozo_blush nolines kyou_annoyed kyou_noblush arm_rest feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_annoyed kyou_noblush arm_rest feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_smile kyou_noblush arm_rest feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_smirk kyou_noblush arm_up feet_rest")
    g_cg.image("NozomiHypnoBon2 nozo_shocked nozo_blush nolines kyou_smirk kyou_noblush arm_rest feet_rest")
    g_cg.image("NozomiHypnoBon2 kyou_nervous arm_up head_up feet_rest nozo_noblush nozo_noface noglasses")

    g_cg.button("sayori alter lunch")
    g_cg.condition("persistent.sayori_alter_lunch_unlock")
    g_cg.image("SayoriAlterLunch sayori1 sushi1 chopsticks a_happy k_neutral s_laugh n_neutral")
    g_cg.image("SayoriAlterLunch sayori1 sushi1 chopsticks a_happy k_neutral s_laugh n_smile")
    g_cg.image("SayoriAlterLunch sayori1 sushi1 chopsticks a_happy k_embarrassed s_smile n_smile")
    g_cg.image("SayoriAlterLunch sayori1 sushi1 chopsticks a_smile_left k_embarrassed s_smile n_smile")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_smile_left k_embarrassed s_laugh n_smile")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_left k_neutral s_smile n_irritated")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_concerned_left k_neutral s_smile n_irritated")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_concerned_left k_neutral s_smile n_surprised")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_smile_left k_neutral s_neutral n_surprised")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_smile_left k_neutral s_neutral n_smile")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_smile_left k_neutral s_rolleyes n_neutral")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_rolleyes n_neutral")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_concerned_right k_neutral s_rolleyes n_neutral")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_pout n_neutral")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_pout_closed n_neutral")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_pout_closed n_sigh")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_grin n_sigh")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_grin n_neutral")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_neutral s_laugh n_neutral")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_neutral s_laugh n_surprised")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_neutral s_smile n_smile")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_neutral s_laugh n_smile")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_rolleyes n_neutral")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_neutral n_neutral")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_neutral n_sigh")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_smile s_neutral n_sigh")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_left k_smile s_surprised n_surprised")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_left k_smile s_laugh n_surprised")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_smile s_laugh n_surprised")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_smile_right k_smile s_happy n_neutral")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_happy k_smile s_happy n_neutral")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_happy k_smile s_happy n_sigh")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_happy k_smile s_grin n_sigh")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_laugh k_neutral s_grin n_neutral")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_smile_right k_neutral s_happy n_neutral")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_smile_right k_confused s_concerned n_surprised")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_smile_right k_confused s_concerned n_neutral")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_smile_right k_smile s_concerned n_neutral")
    g_cg.image("SayoriAlterLunch sayori2 sushi2 nosticks a_surprised k_confused s_surprised n_surprised")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_confused s_laugh n_neutral")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_confused s_laugh n_sigh")
    g_cg.image("SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_confused s_smile n_sigh")

    g_cg.button("sayori arcade2")
    g_cg.condition("persistent.sayori_arcade2_unlock")
    g_cg.image("SayoriArcade2 s_giggle")
    g_cg.image("SayoriArcade2 s_giggle nozomi n_shocked")
    g_cg.image("SayoriArcade2 s_panic nozomi n_shocked")
    g_cg.image("SayoriArcade2 s_embarrassed nozomi n_shocked")
    g_cg.image("SayoriArcade2 s_smile nozomi n_neutral kyou k_mad")
    g_cg.image("SayoriArcade2 s_smirk nozomi n_neutral kyou k_mad")
    g_cg.image("SayoriArcade2 s_smirk nozomi n_neutral kyou k_frown_right")
    g_cg.image("SayoriArcade2 s_smile nozomi n_neutral kyou k_frown_right")
    g_cg.image("SayoriArcade2 s_rolleyes nozomi n_neutral kyou k_frown_right")
    g_cg.image("SayoriArcade2 s_neutral nozomi n_neutral kyou k_frown")
    g_cg.image("SayoriArcade2 s_neutral nozomi n_neutral kyou k_growl")
    g_cg.image("SayoriArcade2 s_neutral nozomi n_sigh kyou k_growl")
    g_cg.image("SayoriArcade2 s_rolleyes nozomi n_neutral kyou k_growl")
    g_cg.image("SayoriArcade2 s_rolleyes nozomi n_pout kyou k_growl")
    g_cg.image("SayoriArcade2 s_neutral nozomi n_concerned kyou k_growl")
    g_cg.image("SayoriArcade2 s_concerned nozomi n_concerned kyou k_frown")
    g_cg.image("SayoriArcade2 s_smirk nozomi n_concerned kyou k_frown")
    g_cg.image("SayoriArcade2 s_smirk nozomi n_concerned kyou k_mad")
    g_cg.image("SayoriArcade2 s_smirk nozomi n_neutral kyou k_growl")
    g_cg.image("SayoriArcade2 s_panic nozomi n_neutral kyou k_growl")
    g_cg.image("SayoriArcade2 s_anxious nozomi n_neutral kyou k_growl")
    g_cg.image("SayoriArcade2 s_anxious nozomi n_neutral kyou k_frown")
    g_cg.image("SayoriArcade2 s_panic nozomi n_neutral kyou k_frown")
    g_cg.image("SayoriArcade2 s_angry nozomi n_neutral kyou k_frown")
    g_cg.image("SayoriArcade2 s_angry nozomi n_neutral kyou k_mad")
    g_cg.image("SayoriArcade2 s_angry nozomi n_neutral kyou k_sigh")
    g_cg.image("SayoriArcade2 s_happy nozomi n_smile kyou k_frown")
    g_cg.image("SayoriArcade2 s_beaming nozomi n_smile kyou k_frown_right")
    g_cg.image("SayoriArcade2 s_neutral nozomi n_neutral kyou k_frown_right")
    g_cg.image("SayoriArcade2 s_concerned nozomi n_neutral kyou k_frown_right")
    g_cg.image("SayoriArcade2 s_concerned nozomi n_neutral kyou k_growl")
    g_cg.image("SayoriArcade2 s_panic nozomi n_neutral kyou k_growl")
    g_cg.image("SayoriArcade2 s_angry nozomi n_neutral kyou k_growl")
    g_cg.image("SayoriArcade2 s_angry nozomi n_neutral kyou k_smirk_right")
    g_cg.image("SayoriArcade2 s_smirk nozomi n_pout kyou k_smirk_right")
    g_cg.image("SayoriArcade2 s_frown nozomi n_neutral kyou k_frown")
    g_cg.image("SayoriArcade2 s_frown nozomi n_shocked kyou k_mad")
    g_cg.image("SayoriArcade2 s_frown nozomi n_awe kyou k_mad")
    g_cg.image("SayoriArcade2 s_beaming nozomi n_awe kyou k_sigh")
    g_cg.image("SayoriArcade2 s_smirk nozomi n_awe kyou k_sigh")

    g_cg.button("sayori penlight")
    g_cg.condition("persistent.sayori_penlight_unlock")
    g_cg.image("SayoriPenlight n_neutral s_neutral")
    g_cg.image("SayoriPenlight n_neutral s_neutral_right")
    g_cg.image("SayoriPenlight n_neutral s_smile_right")
    g_cg.image("SayoriPenlight n_neutral s_quizzical")
    g_cg.image("SayoriPenlight n_neutral s_yawn")
    g_cg.image("SayoriPenlight n_neutral s_smirk")
    g_cg.image("SayoriPenlight n_neutral s_smirk light")
    g_cg.image("SayoriPenlight n_curious s_quizzical light")
    g_cg.image("SayoriPenlight n_curious s_smile light")
    g_cg.image("SayoriPenlight n_curious s_neutral light")
    g_cg.image("SayoriPenlight n_curious s_yawn_right light")
    g_cg.image("SayoriPenlight n_anxious s_yawn_right light")
    g_cg.image("SayoriPenlight n_anxious s_neutral light")
    g_cg.image("SayoriPenlight n_anxious s_yawn light")

    g_cg.button("sayori bed1")
    g_cg.condition("persistent.sayori_bed1_unlock")
    g_cg.image("SayoriBed1 nozomi1 n_fascinated sayori1 s_curious")
    g_cg.image("SayoriBed1 nozomi1 n_fascinated sayori2 s_neutral")
    g_cg.image("SayoriBed1 nozomi1 n_curious_right2 sayori2 s_neutral")
    g_cg.image("SayoriBed1 nozomi1 n_curious_right1 sayori2 s_curious")
    g_cg.image("SayoriBed1 nozomi1 n_curious1 sayori2 s_curious")
    g_cg.image("SayoriBed1 nozomi1 n_concerned sayori2 s_curious")
    g_cg.image("SayoriBed1 nozomi1 n_concerned sayori2 s_concerned")
    g_cg.image("SayoriBed1 nozomi1 n_concerned sayori2 s_smile")
    g_cg.image("SayoriBed1 nozomi1 n_curious1 sayori2 s_smile")
    g_cg.image("SayoriBed1 nozomi1 n_concerned_right sayori4 s_concerned_left")
    g_cg.image("SayoriBed1 nozomi1 n_concerned sayori2 s_neutral")
    g_cg.image("SayoriBed1 nozomi1 n_curious2 sayori2 s_neutral")
    g_cg.image("SayoriBed1 nozomi1 n_curious2 sayori2 s_curious")
    g_cg.image("SayoriBed1 nozomi1 n_fascinated sayori2 s_neutral")
    g_cg.image("SayoriBed1 nozomi1 n_concerned_right sayori2 s_concerned")
    g_cg.image("SayoriBed1 nozomi1 n_concerned_right sayori2 s_neutral")
    g_cg.image("SayoriBed1 nozomi1 n_concerned_right sayori2 s_frown")
    g_cg.image("SayoriBed1 nozomi1 n_concerned sayori2 s_frown")
    g_cg.image("SayoriBed1 nozomi1 n_concerned sayori2 s_irritated")
    g_cg.image("SayoriBed1 nozomi1 n_concerned_right sayori2 s_surprised")
    g_cg.image("SayoriBed1 nozomi1 n_curious_right2 sayori2 s_surprised")
    g_cg.image("SayoriBed1 nozomi1 n_curious_right2 sayori3 s_surprised")
    g_cg.image("SayoriBed1 nozomi1 n_curious_right1 sayori3 s_laugh")
    g_cg.image("SayoriBed1 nozomi1 n_curious_right1 sayori3 s_happy")
    g_cg.image("SayoriBed1 nozomi1 n_smile sayori3 s_happy")
    g_cg.image("SayoriBed1 nozomi1 n_smile sayori4 s_pout")
    g_cg.image("SayoriBed1 nozomi1 n_giggle sayori4 s_pout")
    g_cg.image("SayoriBed1 nozomi1 n_giggle sayori4 s_rolleyes")
    g_cg.image("SayoriBed1 nozomi1 n_smile sayori4 s_concerned_left")
    g_cg.image("SayoriBed1 nozomi1 n_concerned_right sayori2 s_concerned")
    g_cg.image("SayoriBed1 nozomi1 n_concerned_right sayori2 s_happy")

    g_cg.button("sayori hug")
    g_cg.condition("persistent.sayori_hug_unlock")
    g_cg.image("SayoriHug sad")
    g_cg.image("SayoriHug talk")

    g_cg.button("k room akiko 1")
    g_cg.condition("persistent.k_room_akiko_1_unlock")
    g_cg.image("cg k room day", "AkikoHypno upright smile")
    g_cg.image("cg k room day", "AkikoHypno upright happy")
    g_cg.image("cg k room day", "AkikoHypno upright neutral")
    g_cg.image("cg k room day", "AkikoHypno upright surprised")
    g_cg.image("cg k room day", "AkikoHypno upright neutral_up")
    g_cg.image("cg k room day", "AkikoHypno upright neutral_up_talk")
    g_cg.image("cg k room day", "AkikoHypno upright say_ee")
    g_cg.image("cg k room day", "AkikoHypno upright say_oh")
    g_cg.image("cg k room day", "AkikoHypno upright say_ah")
    g_cg.image("cg k room day", "AkikoHypno upright confused")
    g_cg.image("cg k room day", "AkikoHypno upright sad")
    g_cg.image("cg k room day", "AkikoHypno upright sleep noglasses")
    g_cg.image("cg k room day", "AkikoHypno upright irritated noglasses")
    g_cg.image("cg k room day", "AkikoHypno upright frown glasses")
    g_cg.image("cg k room day", "AkikoHypno upright surprised_up")
    g_cg.condition("persistent.k_room_akiko_2_unlock")
    g_cg.image("cg k room day", "AkikoHypno upright sleepy")
    g_cg.condition("persistent.k_room_akiko_2_unlock")
    g_cg.image("cg k room day", "AkikoHypno upright sleep")
    g_cg.condition("persistent.k_room_akiko_2_unlock")
    g_cg.image("cg k room day", "AkikoHypno drooping sleep")
    g_cg.condition("persistent.k_room_akiko_2_unlock")
    g_cg.image("cg k room day", "AkikoHypno drooping sleeptalk")
    g_cg.condition("persistent.k_room_akiko_2_unlock")
    g_cg.image("cg k room day", "AkikoHypno drooping sleepy")
    g_cg.condition("persistent.k_room_akiko_2_unlock")
    g_cg.image("cg k room day", "AkikoHypno upright sleepy blush")
    g_cg.condition("persistent.k_room_akiko_3_unlock")
    g_cg.image("cg k room day", "AkikoHypno upright happy blush")
    g_cg.condition("persistent.k_room_akiko_3_unlock")
    g_cg.image("cg k room day", "AkikoHypno upright smile blush")
    g_cg.condition("persistent.k_room_akiko_3_unlock")

    g_cg.button("sleeper agent struggle1")
    g_cg.condition("persistent.sleeper_agent_struggle1_unlock")
    g_cg.image("SleeperAgentStruggle nozomi n_smile sayori1 s_frown h_growl kyou1 k_dazed")
    g_cg.image("SleeperAgentStruggle nozomi n_smile sayori1 s_growl h_growl kyou1 k_dazed")
    g_cg.image("SleeperAgentStruggle nozomi n_sigh sayori1 s_growl h_growl kyou1 k_dazed")
    g_cg.image("SleeperAgentStruggle nozomi n_sigh sayori1 s_growl h_growl kyou1 k_pain")
    g_cg.image("SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_growl kyou2 k_furious")
    g_cg.image("SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_angry kyou2 k_furious")
    g_cg.image("SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_growl kyou2 k_angry")
    g_cg.image("SleeperAgentStruggle nozomi n_confused sayori1 s_frown h_growl kyou2 k_angry")
    g_cg.image("SleeperAgentStruggle nozomi n_confused sayori1 s_confused h_growl kyou2 k_angry")
    g_cg.image("SleeperAgentStruggle nozomi n_sigh blush sayori1 s_confused h_growl kyou2 k_angry")
    g_cg.image("SleeperAgentStruggle nozomi n_sigh blush sayori1 s_confused h_angry_side kyou2 k_angry")
    g_cg.image("SleeperAgentStruggle nozomi n_sigh blush sayori1 s_confused h_frown kyou2 k_angry")
    g_cg.image("SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_frown kyou1 k_growl")
    g_cg.image("SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_frown kyou1 k_confused")
    g_cg.image("SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_angry kyou1 k_pain")
    g_cg.image("SleeperAgentStruggle nozomi n_smile sayori1 s_growl h_growl kyou1 k_pain")
    g_cg.image("SleeperAgentStruggle nozomi n_surprised sayori2 s_irritated h_growl kyou1 k_pain")
    g_cg.image("SleeperAgentStruggle nozomi n_surprised sayori2 s_angry h_growl kyou1 k_pain")
    g_cg.image("SleeperAgentStruggle nozomi n_frown sayori2 s_angry h_growl kyou1 k_pain")
    g_cg.image("SleeperAgentStruggle nozomi n_frown sayori2 s_angry h_growl kyou1 k_growl")
    g_cg.image("SleeperAgentStruggle nozomi n_frown sayori2 s_angry h_angry kyou1 k_growl")
    g_cg.image("SleeperAgentStruggle nozomi n_frown sayori2 s_angry h_frown kyou1 k_growl")
    g_cg.image("SleeperAgentStruggle nozomi n_confused sayori1 s_frown h_frown kyou1 k_growl")
    g_cg.image("SleeperAgentStruggle nozomi n_confused sayori1 s_frown h_frown kyou1 k_confused")
    g_cg.image("SleeperAgentStruggle nozomi n_smile sayori1 s_frown h_frown kyou1 k_pain")
    g_cg.image("SleeperAgentStruggle nozomi n_sigh sayori1 s_growl h_frown kyou1 k_pain")
    g_cg.image("SleeperAgentStruggle sayori1 s_frown h_frown kyou1 k_pain")
    g_cg.image("SleeperAgentStruggle sayori1 s_frown h_growl kyou2 k_furious")
    g_cg.image("SleeperAgentStruggle sayori1 s_frown h_angry kyou2 k_furious")
    g_cg.image("SleeperAgentStruggle sayori1 s_frown h_growl kyou2 k_angry")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_frown h_growl kyou1 k_pain")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_frown h_angry_side kyou1 k_pain")
    # g_cg.image("SleeperAgentStruggle sayori1 s_frown h_frown kyou1 k_pain")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_growl h_frown kyou1 k_pain")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_growl h_frown kyou1 k_dazed")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_confused h_frown kyou1 k_dazed")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_frown h_frown kyou1 k_dazed")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_frown h_frown kyou1 k_calm")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    # g_cg.image("SleeperAgentStruggle sayori1 s_frown h_growl kyou2 k_furious")
    # g_cg.image("SleeperAgentStruggle sayori1 s_frown h_angry kyou2 k_furious")
    # g_cg.image("SleeperAgentStruggle sayori1 s_frown h_growl kyou1 k_pain")
    g_cg.image("SleeperAgentStruggle sayori1 s_frown h_growl kyou1 k_calm")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    # g_cg.image("SleeperAgentStruggle sayori1 s_frown h_frown kyou1 k_calm")
    g_cg.image("SleeperAgentStruggle sayori1 s_growl h_frown kyou1 k_calm")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_confused h_confused kyou1 k_calm")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_sleepy h_confused kyou1 k_calm")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_sleepy h_worried kyou1 k_calm")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_sleepy h_worried kyou1 k_sneer")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_sleepy h_sleepy kyou1 k_sneer")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_entranced h_sleepy kyou1 k_sneer")
    g_cg.condition("persistent.sleeper_agent_struggle2_unlock")
    g_cg.image("SleeperAgentStruggle sayori1 s_entranced h_entranced kyou1 k_sneer")

    g_cg.button("sleeper agent defeat")
    g_cg.condition("persistent.sleeper_agent_defeat_unlock")
    g_cg.image("SleeperAgentDefeat")
    g_cg.image("SleeperAgentDefeat doubt_right")
    g_cg.image("SleeperAgentDefeat doubt_left")
    g_cg.image("SleeperAgentDefeat doubt")
    g_cg.image("SleeperAgentDefeat arm_up doubt_left")
    g_cg.image("SleeperAgentDefeat arm_up neutral")
    g_cg.image("SleeperAgentDefeat arm_up determined light")
    g_cg.image("SleeperAgentDefeat arm_up neutral light")
    g_cg.image("SleeperAgentDefeat arm_up sad light")

    g_cg.button("k bedroom confrontation sayori")
    g_cg.condition("persistent.k_bedroom_confrontation_sayori_unlock")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded frown", "Sayori_K_Bedroom upright angry_left")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded sad", "Sayori_K_Bedroom upright angry_left")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded sad", "Sayori_K_Bedroom upright neutral_left")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded sad", "Sayori_K_Bedroom upright neutral")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded angry", "Sayori_K_Bedroom upright angry")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded surprised", "Sayori_K_Bedroom upright surprised")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded scared", "Sayori_K_Bedroom upright confused")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed sleepy", "Sayori_K_Bedroom upright sleepy")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed entranced", "Sayori_K_Bedroom upright entranced")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom sleep closed", "Sayori_K_Bedroom sleep closed")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom sleep open", "Sayori_K_Bedroom sleep open")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed smile", "Sayori_K_Bedroom upright smile")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush smile", "Sayori_K_Bedroom upright blush smile")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Sayori_K_Bedroom upright blush smile")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Sayori_K_Bedroom upright blush seductive")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush smile", "Sayori_K_Bedroom upright blush pout")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush sad", "Sayori_K_Bedroom upright blush pout")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush sad", "Sayori_K_Bedroom upright blush confused")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush sad", "Sayori_K_Bedroom sleep blush open")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom sleep blush open", "Sayori_K_Bedroom sleep blush open")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Sayori_K_Bedroom upright blush laugh")

    g_cg.button("k bedroom confrontation hiroko")
    g_cg.condition("persistent.k_bedroom_confrontation_hiroko_unlock")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded frown", "Hiroko_K_Bedroom relaxed frown")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded sad", "Hiroko_K_Bedroom relaxed frown")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded sad", "Hiroko_K_Bedroom relaxed angry")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded angry", "Hiroko_K_Bedroom raised angry")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded surprised", "Hiroko_K_Bedroom raised surprised")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded surprised", "Hiroko_K_Bedroom raised annoyed")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded scared", "Hiroko_K_Bedroom raised annoyed")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded scared", "Hiroko_K_Bedroom raised surprised")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded sleepy", "Hiroko_K_Bedroom raised surprised")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom folded sleepy", "Hiroko_K_Bedroom raised annoyed")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed sleepy", "Hiroko_K_Bedroom raised annoyed")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed entranced", "Hiroko_K_Bedroom raised sleepy")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed entranced", "Hiroko_K_Bedroom relaxed sleepy")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed entranced", "Hiroko_K_Bedroom relaxed entranced")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom sleep closed", "Hiroko_K_Bedroom sleep closed")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom sleep open", "Hiroko_K_Bedroom sleep open")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed smile", "Hiroko_K_Bedroom relaxed smile")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush surprised", "Hiroko_K_Bedroom relaxed smile")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Hiroko_K_Bedroom relaxed smile")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Hiroko_K_Bedroom raised laugh")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Hiroko_K_Bedroom raised blush smile")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush smile", "Hiroko_K_Bedroom relaxed sad")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush sad", "Hiroko_K_Bedroom relaxed blush sad")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom sleep blush open", "Hiroko_K_Bedroom relaxed blush sad")
    g_cg.image("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Hiroko_K_Bedroom relaxed blush laugh")

    g_cg.button("nozomi burglar")
    g_cg.condition("persistent.nozomi_burglar_unlock")
    g_cg.image("NozomiBurglar pose1 growling")
    g_cg.image("NozomiBurglar pose1 shouting")
    g_cg.image("NozomiBurglar pose1 shouting penlight")
    g_cg.image("NozomiBurglar pose1 confused penlight")
    g_cg.image("NozomiBurglar pose1 confused_light penlight")
    g_cg.image("NozomiBurglar pose1 worried penlight")
    g_cg.image("NozomiBurglar pose1 worried_light penlight")
    g_cg.image("NozomiBurglar pose1 sleepy penlight")
    g_cg.image("NozomiBurglar pose1 sleepy_light penlight")
    g_cg.image("NozomiBurglar pose1 sleeping penlight")
    g_cg.image("NozomiBurglar pose2 sleep")
    g_cg.image("NozomiBurglar pose2 sleeptalk")
    g_cg.image("NozomiBurglar pose2 waking")

    g_cg.button("nozomi burglar undressing")
    g_cg.condition("persistent.nozomi_burglar_undressing_unlock")
    g_cg.image("NozomiBurglarUndress")
    g_cg.image("NozomiBurglarUndress nozo_anxious glasses_anxious clothes_anxious confused")
    g_cg.image("NozomiBurglarUndress nozo_anxious glasses_anxious clothes_anxious shocked")
    g_cg.image("NozomiBurglarUndress nozo_giving noglasses clothes_giving offered_glasses")
    g_cg.image("NozomiBurglarUndress nozo_giving noglasses clothes_giving offered_none hand_up")
    g_cg.image("NozomiBurglarUndress nozo_anxious noglasses clothes_anxious ashamed_side hand_up")
    g_cg.image("NozomiBurglarUndress nozo_anxious noglasses clothes_anxious ashamed")
    g_cg.image("NozomiBurglarUndress nozo_anxious noglasses clothes_anxious confused")
    g_cg.image("NozomiBurglarUndress nozo_anxious noglasses clothes_anxious ashamed_side")
    g_cg.image("NozomiBurglarUndress nozo_anxious noglasses clothes_anxious shocked")
    g_cg.image("NozomiBurglarUndress nozo_anxious noglasses clothes_anxious blush_anxious shocked")
    g_cg.image("NozomiBurglarUndress nozo_undressing")
    g_cg.image("NozomiBurglarUndress nozo_giving noglasses blush_giving sweater offered_skirt")
    g_cg.image("NozomiBurglarUndress nozo_giving noglasses blush_giving sweater offered_none hand_up holding_skirt")
    g_cg.image("NozomiBurglarUndress nozo_giving noglasses blush_giving noclothes offered_sweater hand_up holding_skirt")
    g_cg.image("NozomiBurglarUndress nozo_giving noglasses blush_giving noclothes offered_none hand_up holding_sweater")
    g_cg.image("NozomiBurglarUndress nozo_giving noglasses blush_giving noclothes offered_none")
    g_cg.image("NozomiBurglarUndress nozo_begging noglasses blush_begging noclothes")
    g_cg.image("NozomiBurglarUndress nozo_anxious noglasses blush_anxious noclothes ashamed_side")
    g_cg.image("NozomiBurglarUndress nozo_anxious noglasses blush_anxious noclothes ashamed")

    g_cg.button("hiroko court night good")
    g_cg.condition("persistent.hiroko_court_night_good_unlock")
    g_cg.image("HirokoCourtNight hiroko_crossed neutral kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed sigh kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed neutral_left kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed frown kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed irritated kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed neutral_left kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_standing neutral kyou_casual")

    g_cg.button("hiroko court night bad")
    g_cg.condition("persistent.hiroko_court_night_bad_unlock")
    g_cg.image("HirokoCourtNight hiroko_crossed neutral kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed sigh kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed neutral_left kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed frown kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed irritated kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed growl kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed irritated kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed confused kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_standing sleepy_confused kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_sleeping sleep kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_sleeping sleeptalk kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_sleeping sleep")
    g_cg.image("HirokoCourtNight hiroko_standing confused kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_standing smile kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_standing happy kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed sleepy kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_crossed neutral_left kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_standing smile kyou_casual")
    g_cg.image("HirokoCourtNight hiroko_standing happy kyou_casual")

    g_cg.button("akiko makeover 1")
    g_cg.condition("persistent.akiko_makeover_1_unlock")
    g_cg.image("AkikoMakeover1 smile")
    g_cg.image("AkikoMakeover1 grin")

    g_cg.button("akiko makeover 2")
    g_cg.condition("persistent.akiko_makeover_2_unlock")
    g_cg.image("AkikoMakeover2 outfit1 laugh")
    g_cg.transform(galscroll(-0.1))
    g_cg.image("AkikoMakeover2 outfit1 embarrassed blush")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit1 smile")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit1 grin")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit1 curious_right")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit1 curious")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit1 embarrassed_left")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit1 embarrassed")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit2 smile blush")
    g_cg.transform(galscroll(-0.1))
    g_cg.image("AkikoMakeover2 outfit2 embarrassed blush")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit2 embarrassed_left blush")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit2 smile")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit2 surprised")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit2 grin")
    g_cg.transform(galtop(-0.1))
    g_cg.image("AkikoMakeover2 outfit2 laugh")
    g_cg.transform(galtop(-0.1))

    g_cg.button("copycat karaoke hypno1")
    g_cg.condition("persistent.copycat_karaoke_hypno1_unlock")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_a glasses1 blush1 k_smile1 a_smile1")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_a flash glasses1 blush1 k_smile1 a_smileflash1")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_a flash glasses1 blush1 k_smile1 a_smile1")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_a flash glasses1 blush1 k_smile1 a_smileflash1")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_sleepy")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_sleepyflash")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_dazed")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_dazedflash")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_tranced")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_trancedflash")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_sleep1")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_a glasses2 k_smile2 a_sleep2")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_a glasses2 k_talk2 a_sleep2")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_a glasses2 k_neutral a_sleeptalk")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_a glasses2 k_talk2 a_sleeptalk")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_a glasses2 k_neutral a_waking")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_a glasses2 k_smile2 a_waking")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_a glasses2 blush2 k_smile2 a_grin")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_a glasses2 k_smile2 a_confused")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_a glasses2 k_smile2 a_grin")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_a glasses2 k_smile2 a_smile2")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_a glasses2 blush2 k_smile2 a_smile2")
        
    g_cg.button("copycat karaoke hypno2")
    g_cg.condition("persistent.copycat_karaoke_hypno2_unlock")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_b glasses1 blush1 k_smile1 a_smile1")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_b flash glasses1 blush1 k_smile1 a_smileflash1")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_b flash glasses1 blush1 k_smile1 a_smile1")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_b flash glasses1 blush1 k_smile1 a_smileflash1")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_sleepy")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_sleepyflash")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_dazed")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_dazedflash")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_tranced")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_trancedflash")
    g_cg.image("CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_sleep1")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_b glasses2 k_smile2 a_sleep2")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_b glasses2 k_talk2 a_sleep2")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_b glasses2 k_neutral a_sleeptalk")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_b glasses2 k_talk2 a_sleeptalk")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_b glasses2 k_neutral a_waking")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_b glasses2 k_smile2 a_waking")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_b glasses2 blush2 k_smile2 a_grin")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_b glasses2 k_smile2 a_confused")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_b glasses2 k_smile2 a_grin")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_b glasses2 k_smile2 a_smile2")
    g_cg.image("CopycatKaraokeHypno pose2_nozomi_b glasses2 blush2 k_smile2 a_smile2")

    g_cg.button("copycat karaoke1")
    g_cg.condition("persistent.copycat_karaoke1_unlock")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_smile glasses1 kyou_down k_smile")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_happy glasses1 kyou_down k_smile title")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_happy glasses1 kyou_down k_confusedtv title lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_smile glasses1 kyou_down k_confusedtv title lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_giggle glasses1 kyou_down k_confusedtv lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_happy glasses1 kyou_down k_neutral lyric1b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_neutral lyric1b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_neutral lyric1 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_neutral lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_smile glasses1 kyou_down k_smile lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_smile lyric1 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_smile lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_sing glasses1 kyou_down k_smile lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_joy glasses1 kyou_down k_smile lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_happy glasses1 kyou_down k_confusedtv lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_happy glasses1 kyou_down k_confusedtv lyric1b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_confused lyric1 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_singtv a_blush glasses1 kyou_down k_confused lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_sing a_blush glasses1 kyou_down k_confused lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_down k_confusedtv lyric4b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_up k_nervoustv lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_up k_nervoustv lyric3 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_giggle a_blush glasses1 kyou_up k_confused lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_giggle a_blush glasses1 kyou_up k_confused k_blush lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_up k_smile k_blush lyric3b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_up k_nervoustv k_blush lyric3 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_up k_nervous k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_up k_nervoustv k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_down k_smile k_blush lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_down k_smile k_blush lyric3b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_up k_singtv k_blush lyric3 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_up k_sing k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_wink a_blush glasses1 kyou_down k_confused k_blush lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_wink a_blush glasses1 kyou_down k_confused k_blush lyric2b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_singtv a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_smile a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_sing a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_smile a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_shy a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_shy a_blush glasses1 kyou_up k_smile k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_joy a_blush glasses1 kyou_up k_happy k_blush lyric5 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_up a_joy a_blush glasses1 kyou_up k_happy k_blush lyric6 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_down k_smile k_blush lights")

    g_cg.button("copycat karaoke2")
    g_cg.condition("persistent.copycat_karaoke2_unlock")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_smile glasses1 kyou_down k_smile")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_happy glasses1 kyou_down k_smile title")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_happy glasses1 kyou_down k_confusedtv title lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_smile glasses1 kyou_down k_confusedtv title lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_giggle glasses1 kyou_down k_confusedtv lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_happy glasses1 kyou_down k_neutral lyric1b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_neutral lyric1b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_neutral lyric1 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_neutral lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_smile glasses1 kyou_down k_smile lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_smile lyric1 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_smile lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_sing glasses1 kyou_down k_smile lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_joy glasses1 kyou_down k_smile lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_happy glasses1 kyou_down k_confusedtv lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_happy glasses1 kyou_down k_confusedtv lyric1b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_confused lyric1 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_singtv a_blush glasses1 kyou_down k_confused lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_sing a_blush glasses1 kyou_down k_confused lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_down k_confusedtv lyric4b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_up k_nervoustv lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_up k_nervoustv lyric3 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_giggle a_blush glasses1 kyou_up k_confused lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_giggle a_blush glasses1 kyou_up k_confused k_blush lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_up k_smile k_blush lyric3b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_up k_nervoustv k_blush lyric3 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_up k_nervous k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_up k_nervoustv k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_down k_smile k_blush lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_down k_smile k_blush lyric3b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_up k_singtv k_blush lyric3 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_up k_sing k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_wink a_blush glasses1 kyou_down k_confused k_blush lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_wink a_blush glasses1 kyou_down k_confused k_blush lyric2b lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_singtv a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_smile a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_sing a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_smile a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_shy a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_shy a_blush glasses1 kyou_up k_smile k_blush lyric4 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_joy a_blush glasses1 kyou_up k_happy k_blush lyric5 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_up a_joy a_blush glasses1 kyou_up k_happy k_blush lyric6 lights")
    g_cg.image("CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_down k_smile k_blush lights")

    g_cg.button("copycat karaoke3")
    g_cg.condition("persistent.copycat_karaoke3_unlock")
    g_cg.image("CopycatKaraoke together_nozomi_a affectionate glasses2")
    g_cg.image("CopycatKaraoke together_nozomi_a affectionate_closed glasses2")
    g_cg.image("CopycatKaraoke together_nozomi_b affectionate glasses2")
    g_cg.image("CopycatKaraoke together_nozomi_b affectionate_closed glasses2")    

    g_cg.button("hiroko park sad")
    g_cg.condition("persistent.hiroko_park_sad_unlock")
    g_cg.image("HirokoParkSad")
    g_cg.image("HirokoParkSad frown_tears")
    g_cg.image("HirokoParkSad head2 angry_tears")
    g_cg.image("HirokoParkSad head2 stern_tears")
    g_cg.image("HirokoParkSad frown")
    g_cg.image("HirokoParkSad sad")
    g_cg.image("HirokoParkSad head2 stern")
    g_cg.image("HirokoParkSad head2 glare")
    g_cg.image("HirokoParkSad head2 surprised")
    g_cg.image("HirokoParkSad head2 angry")
    g_cg.image("HirokoParkSad head2 upset")
    g_cg.image("HirokoParkSad head2 upset_tears")
    g_cg.image("HirokoParkSad head1 sad_tears")
    g_cg.image("HirokoParkSad head1 arms_throw sad_tears")
    g_cg.image("HirokoParkSad head1 arms_down sad_tears")
    g_cg.image("HirokoParkSad head2 arms_down angry_tears")
    g_cg.image("HirokoParkSad head1 arms_down weeping")
    g_cg.image("HirokoParkSad head1 arms_down frown")
    g_cg.image("HirokoParkSad head2 arms_down stern")

    g_cg.button("hiroko won")
    g_cg.condition("persistent.hiroko_won_unlock")
    g_cg.image("HirokoWon shocked")
    g_cg.image("HirokoWon nozomi shocked")
    g_cg.image("HirokoWon nozomi crying")

    g_cg.button("nozomi cafe villain") #Formerly known as "nozomi cafe casual"
    g_cg.condition("persistent.nozomi_cafe_villain_unlock")
    g_cg.image("NozomiCafe casual_leaning pensive nocup")
    g_cg.image("NozomiCafe casual_folded stern nocup")
    g_cg.image("NozomiCafe casual_folded growl nocup")
    g_cg.image("NozomiCafe casual_folded angry nocup")
    g_cg.image("NozomiCafe casual_leaning angry nocup")
    g_cg.image("NozomiCafe casual_leaning stern nocup")
    g_cg.image("NozomiCafe casual_leaning stern_side nocup")
    g_cg.image("NozomiCafe casual_leaning stern nocup")
    g_cg.image("NozomiCafe casual_leaning angry nocup")
    g_cg.image("NozomiCafe casual_folded growl nocup")
    g_cg.image("NozomiCafe casual_folded surprised nocup")
    g_cg.image("NozomiCafe casual_folded pensive nocup")
    g_cg.image("NozomiCafe casual_folded sleepy nocup")
    g_cg.image("NozomiCafe casual_folded sleepy hand1 nocup")
    g_cg.image("NozomiCafe casual_folded sleepy_entranced hand1 nocup")
    g_cg.image("NozomiCafe casual_folded neutral_entranced hand2 nocup")
    g_cg.image("NozomiCafe casual_folded neutral_entranced nohand nocup")
    g_cg.image("NozomiCafe casual_folded smile_entranced nocup")

    g_cg.button("nozomi window")
    g_cg.condition("persistent.nozomi_window_unlock")
    g_cg.image("NozomiWindow bedroom_bw body_bw anxious_bw glasses_bw front_bw")
    g_cg.image("NozomiWindow bedroom_bw body_bw sigh_bw glasses_bw front_bw")
    g_cg.image("NozomiWindow bedroom_bw body_bw smile_bw glasses_bw front_bw")
    g_cg.image("NozomiWindow bedroom_bw body_bw smile_light_bw glasses_bw front_bw hiroko_bw")
    g_cg.image("NozomiWindow bedroom_bw body_bw surprised_bw glasses_bw front_bw")
    g_cg.image("NozomiWindow bedroom_bw body_bw surprised_light_bw glasses_bw front_bw hiroko_bw")
    g_cg.image("NozomiWindow bedroom_bw body_bw neutral_bw glasses_bw front_bw")
    g_cg.image("NozomiWindow bedroom_bw body_bw neutral_light_bw glasses_bw front_bw hiroko_bw")
    g_cg.image("NozomiWindow bedroom_bw body_bw sleepy_bw glasses_bw front_bw")
    g_cg.image("NozomiWindow bedroom_bw body_bw sleepy_light_bw glasses_bw front_bw hiroko_bw")
    g_cg.image("NozomiWindow bedroom_bw body_bw entranced_bw glasses_bw front_bw")
    #Colour version not seen during the main game
    g_cg.image("NozomiWindow bedroom body anxious glasses front")
    g_cg.image("NozomiWindow bedroom body sigh glasses front")
    g_cg.image("NozomiWindow bedroom body smile glasses front")
    g_cg.image("NozomiWindow bedroom body smile_light glasses front hiroko")
    g_cg.image("NozomiWindow bedroom body surprised glasses front")
    g_cg.image("NozomiWindow bedroom body surprised_light glasses front hiroko")
    g_cg.image("NozomiWindow bedroom body neutral glasses front")
    g_cg.image("NozomiWindow bedroom body neutral_light glasses front hiroko")
    g_cg.image("NozomiWindow bedroom body sleepy glasses front")
    g_cg.image("NozomiWindow bedroom body sleepy_light glasses front hiroko")
    g_cg.image("NozomiWindow bedroom body entranced glasses front")

    g_cg.button("nozomi captured")
    g_cg.condition("persistent.nozomi_captured_unlock")
    g_cg.image("NozomiCaptured base1 dazed")
    g_cg.image("NozomiCaptured base1 sigh")
    g_cg.image("NozomiCaptured base1 surprised")
    g_cg.image("NozomiCaptured base1 dazed_left")
    g_cg.image("NozomiCaptured base2 dazed_left")
    g_cg.image("NozomiCaptured base3 dazed_left")
    g_cg.image("NozomiCaptured base3 dazed")
    g_cg.image("NozomiCaptured base3 angry")
    g_cg.image("NozomiCaptured base3 sleep")
    g_cg.image("NozomiCaptured base3 sleeptalk")
    g_cg.image("NozomiCaptured base3 dazed")
    g_cg.image("NozomiCaptured base3 awe")
    g_cg.image("NozomiCaptured base3 surprised blush")
    g_cg.image("NozomiCaptured base3 smile blush")
    g_cg.image("NozomiCaptured base3 laugh blush")
    g_cg.image("NozomiCaptured base3 surprised")
    g_cg.image("NozomiCaptured base3 awe")
    g_cg.image("NozomiCaptured base3 sigh")
    g_cg.image("NozomiCaptured base3 neutral")
    g_cg.image("NozomiCaptured base3 smile blush")

    g_cg.button("nozomi kneeling trance1")
    g_cg.condition("persistent.nozomi_kneeling_trance1_unlock")
    g_cg.image("cg nozomi kneeling", "NozomiKneeling underwear head_down_blush pleasure glasses_down kyou_down_uniform")
    g_cg.image("cg nozomi kneeling", "NozomiKneeling underwear head_up_blush surprised glasses_up kyou_down_uniform")
    g_cg.image("cg nozomi kneeling", "NozomiKneeling underwear head_up_blush anxious glasses_up kyou_down_uniform")
    g_cg.image("cg nozomi kneeling", "NozomiKneeling underwear head_up_blush anxious glasses_up kyou_up_uniform")
    g_cg.image("cg nozomi kneeling", "NozomiKneeling underwear head_up surprised glasses_up kyou_down_uniform")
    g_cg.image("cg nozomi kneeling", "NozomiKneeling underwear head_up surprised glasses_up kyou_click_uniform")
    g_cg.condition("persistent.nozomi_kneeling_trance2_unlock")
    g_cg.image("cg nozomi kneeling", "NozomiKneeling underwear head_up falling glasses_up kyou_click_uniform")
    g_cg.condition("persistent.nozomi_kneeling_trance2_unlock")
    g_cg.image("cg nozomi kneeling", "NozomiKneeling underwear head_down blank glasses_down kyou_down_uniform")
    g_cg.condition("persistent.nozomi_kneeling_trance2_unlock")
    g_cg.image("cg nozomi kneeling", "NozomiKneeling underwear head_down blank glasses_down nokyou")
    g_cg.condition("persistent.nozomi_kneeling_trance2_unlock")
    
    g_cg.button("nozomi zombie walk")
    g_cg.condition("persistent.nozomi_zombie_walk_unlock")
    g_cg.image("NozomiZombieWalk nozomi1 neutral")
    g_cg.transform(galzoomout)
    g_cg.image("NozomiZombieWalk nozomi2 neutral")
    g_cg.transform(galzoomout)
    g_cg.image("NozomiZombieWalk nozomi_right")
    g_cg.transform(galzoomout)
    g_cg.image("NozomiZombieWalk nozomi_left neutral_left")
    g_cg.transform(galzoomout)
    g_cg.image("NozomiZombieWalk nozomi_left talk_left")
    g_cg.transform(galzoomout)

    g_cg.button("nozomi lying")
    g_cg.condition("persistent.nozomi_lying_unlock")
    g_cg.image("NozomiCaptured base4 entranced")
    g_cg.image("NozomiCaptured base4 entranced_dazed")
    g_cg.image("NozomiCaptured base4 sleep")
    g_cg.image("NozomiCaptured base4 sleeptalk")
    g_cg.image("NozomiCaptured base4 dazed")
    g_cg.image("NozomiCaptured base4 awe blush")
    g_cg.image("NozomiCaptured base4 scared blush")

    g_cg.button("nozomi kitchen single image")
    g_cg.condition("persistent.nozomi_kitchen_unlock")
    g_cg.image("cg nozomi kitchen")
    g_cg.transform(galscroll(-0.1))

    g_cg.button("nozomi omelette")
    g_cg.condition("persistent.nozomi_omelette_unlock")
    g_cg.image("NozomiOmelette head_down sigh omelette1")
    g_cg.image("NozomiOmelette head_down pout omelette1")
    g_cg.image("NozomiOmelette head_up neutral omelette1")
    g_cg.image("NozomiOmelette head_up pout_closed omelette1")
    g_cg.image("NozomiOmelette head_up dazed omelette1")
    g_cg.image("NozomiOmelette head_up surprised omelette1")
    g_cg.image("NozomiOmelette head_down shy_down omelette2")
    g_cg.image("NozomiOmelette head_down shy_up omelette2")
    g_cg.image("NozomiOmelette head_up smile omelette2")
    g_cg.image("NozomiOmelette head_up teasing omelette2")

    g_cg.button("nozomi kiss")
    g_cg.condition("persistent.nozomi_kiss_unlock")
    g_cg.image("NozomiKiss kissing")
    g_cg.image("NozomiKiss standing sleepy glasses")
    g_cg.image("NozomiKiss standing smile glasses")
    g_cg.image("NozomiKiss standing sleepysmile glasses")

    g_cg.button("nozomi kneeling devotion")
    g_cg.condition("persistent.nozomi_kneeling_devotion_unlock")
    g_cg.image("cg nozomi kneeling", "NozomiKneeling casual head_down crying glasses_down kyou_down_casual")
    g_cg.image("cg nozomi kneeling", "NozomiKneeling casual head_up hope glasses_up kyou_down_casual")

    g_cg.button("classroom hiroko 2 1") #Formerly known as "classroom 2 Hiroko"
    g_cg.condition("persistent.classroom_hiroko_2_1_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno upright uniform2 frown2")
    g_cg.image("cg classroom 2", "HirokoHypno upright uniform2 annoyed_up2")
    g_cg.image("cg classroom 2", "HirokoHypno upright uniform2 angry_up2")
    g_cg.image("cg classroom 2", "HirokoHypno upright uniform2 angry2")
    g_cg.image("cg classroom 2", "HirokoHypno upright uniform2 annoyed2")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 annoyed2")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 drowsy2")
    g_cg.image("cg classroom 2", "HirokoHypno drooping uniform2 sleep")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 sleep")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 entranced_neutral")
    g_cg.image("cg classroom 2", "HirokoHypno drooping uniform2 sleeptalk")
    g_cg.condition("persistent.classroom_hiroko_2_2_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 sad_closed2")
    g_cg.condition("persistent.classroom_hiroko_2_2_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 surprised2")
    g_cg.condition("persistent.classroom_hiroko_2_2_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno upright uniform2 angry2 clenched_fists2")
    g_cg.condition("persistent.classroom_hiroko_2_2_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno upright uniform2 angry_up2 clenched_fists2")
    g_cg.condition("persistent.classroom_hiroko_2_2_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno upright uniform2 blush2 sad_closed2")
    g_cg.condition("persistent.classroom_hiroko_2_3_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 blush2 angry2 arm_uniform")
    g_cg.condition("persistent.classroom_hiroko_2_3_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 blush2 angry_up2 arm_uniform")
    g_cg.condition("persistent.classroom_hiroko_2_3_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 blush2 annoyed_up2 arm_uniform")
    g_cg.condition("persistent.classroom_hiroko_2_3_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 blush2 annoyed_up2 no_arm")
    g_cg.condition("persistent.classroom_hiroko_2_3_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 blush2 frown2 no_arm")
    g_cg.condition("persistent.classroom_hiroko_2_3_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno drooping uniform2 sleep arm_uniform")
    g_cg.condition("persistent.classroom_hiroko_2_4_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno drooping uniform2 sleeptalk arm_uniform")
    g_cg.condition("persistent.classroom_hiroko_2_4_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno relaxed uniform2 drowsy2")
    g_cg.condition("persistent.classroom_hiroko_2_4_unlock")
    g_cg.image("cg classroom 2", "HirokoHypno upright uniform2 angry2 clenched_fists2")
    g_cg.condition("persistent.classroom_hiroko_2_4_unlock")

    g_cg.button("hiroko rehearsal") #Formerly known as hiroko classroom rehearsal
    g_cg.condition("persistent.hiroko_rehearsal_unlock")
    g_cg.image("HirokoRehearsal pose1 frown")
    g_cg.image("HirokoRehearsal pose1 angry")
    g_cg.image("HirokoRehearsal pose2")

    g_cg.button("sayori arcade")
    g_cg.condition("persistent.sayori_arcade_unlock")
    g_cg.image("cg arcade", "SayoriArcade standing happy")
    g_cg.image("cg arcade", "KyouArcade bemused", "SayoriArcade standing happy")
    g_cg.image("cg arcade", "KyouArcade bemused", "SayoriArcade standing smile")
    g_cg.image("cg arcade", "KyouArcade bemused", "SayoriArcade lookaside smile_left")
    g_cg.image("cg arcade", "KyouArcade smile", "SayoriArcade lookaside smile_left")
    g_cg.image("cg arcade", "KyouArcade smile", "SayoriArcade lookaside rolleyes")
    g_cg.image("cg arcade", "KyouArcade defeated", "SayoriArcade victory noface")

    g_cg.button("hiroko gaming")
    g_cg.condition("persistent.hiroko_gaming_unlock")
    g_cg.image("HirokoGaming hiroko1 tennis head1 neutral1")
    g_cg.image("HirokoGaming hiroko1 tennis head2 quizzical2")
    g_cg.image("HirokoGaming hiroko1 tennis head1 frown1")
    g_cg.image("HirokoGaming hiroko1 tennis head1 sigh1")
    g_cg.image("HirokoGaming hiroko1 tennis head2 annoyed2")
    g_cg.image("HirokoGaming hiroko1 tennis head1 angry1")
    g_cg.image("HirokoGaming hiroko1 tennis head1 laugh1")
    g_cg.image("HirokoGaming hiroko1 tennis head2 laugh2")
    g_cg.image("HirokoGaming hiroko1 tennis head2 happy2")
    g_cg.image("HirokoGaming hiroko1 tennis head2 smirk2")
    g_cg.image("HirokoGaming hiroko1 tennis head2 smile2")
    g_cg.image("HirokoGaming hiroko1 tennis head1 smile1")
    g_cg.image("HirokoGaming hiroko1 tennis head1 annoyed1")
    g_cg.image("HirokoGaming hiroko1 tennis head1 surprised1")
    g_cg.image("HirokoGaming hiroko1 tennis head2 angry2")
    g_cg.image("HirokoGaming hiroko1 tennis head2 neutral2")
    g_cg.image("HirokoGaming hiroko2 tennis head2 moaning2 blush2")
    g_cg.image("HirokoGaming hiroko1 tennis head2 angry2 blush2")
    g_cg.image("HirokoGaming hiroko1 tennis head2 annoyed2 blush2")
    g_cg.image("HirokoGaming hiroko1 tennis head1 surprised1 blush1")
    g_cg.image("HirokoGaming hiroko1 tennis head1 angry1 blush1")
    g_cg.image("HirokoGaming hiroko2 tennis head1 moaning1 blush1")
    g_cg.image("HirokoGaming hiroko2 tennis head1 unfocused1 blush1")
    g_cg.image("HirokoGaming hiroko1 tennis head2 angry2 blush2")
    g_cg.image("HirokoGaming hiroko2 tennis head1 moaning_closed1 blush1")
    g_cg.image("HirokoGaming hiroko1 tennis head1 moaning_closed1 blush1")
    g_cg.image("HirokoGaming hiroko1 tennis head1 sigh1 blush1")
    #Socks
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 neutral1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head2 quizzical2")
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 frown1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 sigh1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head2 annoyed2")
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 angry1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 laugh1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head2 laugh2")
    g_cg.image("HirokoGaming hiroko1_socks tennis head2 happy2")
    g_cg.image("HirokoGaming hiroko1_socks tennis head2 smirk2")
    g_cg.image("HirokoGaming hiroko1_socks tennis head2 smile2")
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 smile1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 annoyed1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 surprised1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head2 angry2")
    g_cg.image("HirokoGaming hiroko1_socks tennis head2 neutral2")
    g_cg.image("HirokoGaming hiroko2_socks tennis head2 moaning2 blush2")
    g_cg.image("HirokoGaming hiroko1_socks tennis head2 angry2 blush2")
    g_cg.image("HirokoGaming hiroko1_socks tennis head2 annoyed2 blush2")
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 surprised1 blush1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 angry1 blush1")
    g_cg.image("HirokoGaming hiroko2_socks tennis head1 moaning1 blush1")
    g_cg.image("HirokoGaming hiroko2_socks tennis head1 unfocused1 blush1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head2 angry2 blush2")
    g_cg.image("HirokoGaming hiroko2_socks tennis head1 moaning_closed1 blush1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 moaning_closed1 blush1")
    g_cg.image("HirokoGaming hiroko1_socks tennis head1 sigh1 blush1")
    #Undies
    g_cg.image("HirokoGaming hiroko1 head1 neutral1")
    g_cg.image("HirokoGaming hiroko1 head2 quizzical2")
    g_cg.image("HirokoGaming hiroko1 head1 frown1")
    g_cg.image("HirokoGaming hiroko1 head1 sigh1")
    g_cg.image("HirokoGaming hiroko1 head2 annoyed2")
    g_cg.image("HirokoGaming hiroko1 head1 angry1")
    g_cg.image("HirokoGaming hiroko1 head1 laugh1")
    g_cg.image("HirokoGaming hiroko1 head2 laugh2")
    g_cg.image("HirokoGaming hiroko1 head2 happy2")
    g_cg.image("HirokoGaming hiroko1 head2 smirk2")
    g_cg.image("HirokoGaming hiroko1 head2 smile2")
    g_cg.image("HirokoGaming hiroko1 head1 smile1")
    g_cg.image("HirokoGaming hiroko1 head1 annoyed1")
    g_cg.image("HirokoGaming hiroko1 head1 surprised1")
    g_cg.image("HirokoGaming hiroko1 head2 angry2")
    g_cg.image("HirokoGaming hiroko1 head2 neutral2")
    g_cg.image("HirokoGaming hiroko2 head2 moaning2 blush2")
    g_cg.image("HirokoGaming hiroko1 head2 angry2 blush2")
    g_cg.image("HirokoGaming hiroko1 head2 annoyed2 blush2")
    g_cg.image("HirokoGaming hiroko1 head1 surprised1 blush1")
    g_cg.image("HirokoGaming hiroko1 head1 angry1 blush1")
    g_cg.image("HirokoGaming hiroko2 head1 moaning1 blush1")
    g_cg.image("HirokoGaming hiroko2 head1 unfocused1 blush1")
    g_cg.image("HirokoGaming hiroko1 head2 angry2 blush2")
    g_cg.image("HirokoGaming hiroko2 head1 moaning_closed1 blush1")
    g_cg.image("HirokoGaming hiroko1 head1 moaning_closed1 blush1")
    g_cg.image("HirokoGaming hiroko1 head1 sigh1 blush1")

    g_cg.button("hiroko slumped")
    g_cg.condition("persistent.hiroko_slumped_unlock")
    g_cg.image("HirokoSlumped tennis blissful")
    g_cg.image("HirokoSlumped tennis moaning")
    g_cg.image("HirokoSlumped tennis sleepy")
    g_cg.image("HirokoSlumped tennis smile")
    #Socks
    g_cg.image("HirokoSlumped tennis socks blissful")
    g_cg.image("HirokoSlumped tennis socks moaning")
    g_cg.image("HirokoSlumped tennis socks sleepy")
    g_cg.image("HirokoSlumped tennis socks smile")
    #Undies
    g_cg.image("HirokoSlumped blissful")
    g_cg.image("HirokoSlumped moaning")
    g_cg.image("HirokoSlumped sleepy")
    g_cg.image("HirokoSlumped smile")

    g_cg.button("nozomi karaoke group")
    g_cg.condition("persistent.nozomi_karaoke_group_unlock")
    g_cg.image("NozomiKaraokeGroup")
    g_cg.image("NozomiKaraokeGroup nozo_annoyed hiro_irritated risa_uncertain")
    g_cg.image("NozomiKaraokeGroup nozo_worried hiroko_armsup hiro_furious risa_disgruntled")
    g_cg.image("NozomiKaraokeGroup nozo_cry hiroko_armsup hiro_pain risa_pain")

    g_cg.button("nozomi threatening")
    g_cg.condition("persistent.nozomi_threatening_unlock")
    g_cg.image("NozomiThreatening arm_up frown scared")
    g_cg.image("NozomiThreatening arm_up neutral scared")
    g_cg.image("NozomiThreatening arm_up arrogant scared")
    g_cg.image("NozomiThreatening arm_up growl scared")
    g_cg.image("NozomiThreatening arm_up growl blush scared")
    g_cg.image("NozomiThreatening arm_up smirk blush scared")
    g_cg.image("NozomiThreatening arm_up smirk blush relaxed")
    g_cg.image("NozomiThreatening arm_up angry blush relaxed")
    g_cg.image("NozomiThreatening arm_up neutral relaxed")
    g_cg.image("NozomiThreatening arm_up fearful relaxed")
    g_cg.image("NozomiThreatening arm_down cry relaxed")
    g_cg.image("NozomiThreatening arm_down cry surprised")
    g_cg.image("NozomiThreatening arm_down fearful surprised")

    g_cg.button("nozomi sorry")
    g_cg.condition("persistent.nozomi_sorry_unlock")
    g_cg.image("NozomiSorry closed")
    g_cg.image("NozomiSorry open")

    g_cg.button("nozomi couch hypno")
    g_cg.condition("persistent.nozomi_couch_hypno_unlock")
    g_cg.image("NozomiCouchHypno k_hand_down n_hand_down neutral")
    g_cg.image("NozomiCouchHypno k_hand_down n_hand_down smile")
    g_cg.image("NozomiCouchHypno k_hand_down n_hand_down sad")
    g_cg.image("NozomiCouchHypno k_hand_down n_hand_down frown")
    g_cg.image("NozomiCouchHypno k_hand_down n_hand_forehead frown")
    g_cg.image("NozomiCouchHypno k_hand_down n_hand_down happy")
    g_cg.image("NozomiCouchHypno k_hand_down n_hand_down sigh")
    g_cg.image("NozomiCouchHypno k_hand_down n_hand_down surprised")
    g_cg.image("NozomiCouchHypno k_hand_down n_hand_down angry")
    g_cg.image("NozomiCouchHypno k_hand_down n_hand_down glare")

    g_cg.button("nozomi tortured tickle")
    g_cg.condition("persistent.nozomi_tortured_tickle_unlock")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi1 k1_neutral n1_sleepy")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi1 k1_neutral n1_waking")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_neutral n2_grimace")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_neutral n2_pain")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_neutral n2_worried")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_worried")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_fear")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_fear blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_worried blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_smirk n2_worried blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_smirk n2_sigh blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_smirk n2_surprised blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_smirk n2_fear blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_fright blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_angry blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_surprised n2_angry blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_neutral n2_grimace blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_frown n2_grimace blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_frown n2_fear blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_frown n2_worried blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2 k1_smirk n2_fright blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2_tickle k1_smirk n2_fright blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2_tickle lines2 k1_smirk n2_grimace blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2_tickle lines2 k1_smirk n2_fear blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2_tickle lines2 k1_neutral n2_pain blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2_tickle k1_frown n2_pain blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi2_tickle k1_frown n2_sigh blush2")
    g_cg.image("NozomiTortured_Tickle feet_socks nozomi1_tickle k1_frown n1_waking blush1")
    g_cg.image("NozomiTortured_Tickle feet_rest nozomi1_tickle k1_frown n1_waking blush1")
    g_cg.image("NozomiTortured_Tickle feet_rest nozomi2_tickle  k1_frown n2_worried blush2")
    g_cg.image("NozomiTortured_Tickle feet_rest nozomi2_tickle k1_smug n2_worried blush2")
    g_cg.image("NozomiTortured_Tickle feet_clenched nozomi2_tickle lines2 k1_smug n2_pain blush2")
    g_cg.image("NozomiTortured_Tickle feet_clenched nozomi2_tickle lines2 k1_smug n2_grin blush2")
    g_cg.image("NozomiTortured_Tickle feet_clenched nozomi2_tickle k1_surprised n2_fright blush2")
    g_cg.image("NozomiTortured_Tickle feet_rest nozomi2 k1_neutral n2_worried blush2")
    g_cg.image("NozomiTortured_Tickle feet_rest nozomi2 k1_frown n2_worried blush2")
    g_cg.image("NozomiTortured_Tickle feet_rest nozomi2 k1_growl n2_worried blush2")
    g_cg.image("NozomiTortured_Tickle feet_rest nozomi3 k2_growl n2_fright blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_growl n2_grimace blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_growl n2_pain blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_growl n2_grin blush2")
    g_cg.image("NozomiTortured_Tickle feet_clenched nozomi3 lines3 k2_growl n2_laugh_happy blush2")
    g_cg.image("NozomiTortured_Tickle feet_clenched nozomi3 lines3 k2_growl n2_pain blush2")
    g_cg.image("NozomiTortured_Tickle feet_clenched nozomi3 k2_talk n2_pain blush2")
    g_cg.image("NozomiTortured_Tickle feet_clenched nozomi3 k2_talk n2_fright blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_frown n2_pain blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_frown n2_grin blush2")
    g_cg.image("NozomiTortured_Tickle feet_clenched nozomi3 lines3 k2_frown n2_laugh blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_frown n2_laugh blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_growl n2_laugh blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_growl n2_laugh_mad blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_frown n2_laugh_mad blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 sweat3 lines3 k2_frown n2_laugh_mad blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 sweat3 lines3 k2_smirk n2_laugh_mad blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smug n2_laugh_mad blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smug n2_laugh_cry blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smirk n2_laugh_cry blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smirk n2_laugh_mad blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smirk n2_laugh_insane blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smirk n2_laugh_tranced blush2")
    g_cg.image("NozomiTortured_Tickle feet_squirm nozomi3 sweat3 lines3 k2_smirk n2_laugh_tranced blush2")
    g_cg.image("NozomiTortured_Tickle feet_rest nozomi1 sweat1 k1_smug n1_mindless blush1")
    g_cg.image("NozomiTortured_Tickle feet_rest nozomi1 sweat1 k1_smile n1_mindless blush1")
    g_cg.image("NozomiTortured_Tickle feet_rest nozomi1 sweat1 k1_smile n1_bliss blush1")

    g_cg.button("nozomi tortured spank")
    g_cg.condition("persistent.nozomi_tortured_spank_unlock")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi1 underwear1_up n1_sleepy k_neutral")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi1 underwear1_up n1_waking k_neutral")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2 underwear2_up n2_anxious k_neutral")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2 underwear2_up lines n2_grimace k_neutral")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up lines n2_grimace k_neutral")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_worried k_neutral")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_worried k_smug")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_worried k_smug blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fear k_smug blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_worried k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_sigh k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi2_rub underwear2_up n2_surprised k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi2_rub underwear2_up n2_worried k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fear k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fear k_wicked blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fright k_wicked blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_angry k_smug blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_angry k_surprised blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_anxious k_neutral blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_anxious k_frown blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fear k_frown blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_worried k_frown blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fright k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_raised underwear2_up n2_fright k_wicked blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_spank underwear2_up n2_fright k_wicked blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up lines n2_grimace k_smug blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_raised underwear2_up lines n2_fear k_smug blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_up lines n2_grimace k_smug blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised underwear2_up lines n2_fear k_smug blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_up lines n2_anxious k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi2_raised underwear2_up lines n2_anxious k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi2_raised underwear2_up lines n2_fear k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi2_raised underwear2_up lines n2_fear k_talk blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_up lines n2_shout k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_grimace k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi1_rub underwear1_up n1_worried k_smirk blush1")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi1_rub underwear1_down n1_worried k_smirk blush1")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_down lines n2_fright k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_raised underwear2_down n2_worried k_talk blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_down lines n2_shout k_talk blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_rub underwear2_down n2_anxious k_smug blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_down n2_anxious k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_raised underwear2_down n2_fear k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_down lines n2_scream k_surprised blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_down n2_fright k_neutral blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_rub underwear2_down n2_fright k_frown blush2")
    g_cg.image("NozomiTortured_Spank feet_tense nozomi2_raised underwear2_down n2_fear k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_down lines n2_shout k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised underwear2_down lines n2_shout k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised underwear2_down lines n2_fright k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red2 underwear2_down lines n2_scream k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_rub red2 underwear2_down lines n2_scream k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised red2 underwear2_down lines n2_scream k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red2 underwear2_down lines n2_grimace k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised red2 underwear2_down lines n2_grimace k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red2 underwear2_down lines n2_sigh k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_rub red2 underwear2_down lines n2_fear k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_rub red2 underwear2_down lines n2_fright k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised red2 underwear2_down lines n2_fright k_talk blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down lines n2_shout k_talk blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down lines n2_pain k_talk blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down lines n2_pain k_frown blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down lines n2_crying k_frown blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down lines n2_pain k_frown blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down lines n2_agony k_frown blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down lines n2_agony k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down lines n2_agony k_growl blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down lines n2_agony k_frown blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down sweat2 lines n2_agony k_frown blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down sweat2 lines n2_agony k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down sweat2 lines n2_agony k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down sweat2 lines n2_pain k_smirk blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down sweat2 lines n2_pain k_wicked blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down sweat2 lines n2_insane k_wicked blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down sweat2 lines n2_insane k_wicked blush2")
    g_cg.image("NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down sweat2 lines n2_tranced k_wicked blush2")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi1_rub red1 underwear1_down sweat1 n1_mindless k_wicked blush1")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi1_rub red1 underwear1_down sweat1 n1_bliss k_smirk blush1")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi1_rub red1 underwear1_down sweat1 n1_bliss k_smug blush1")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi1_rub red1 underwear1_down sweat1 n1_bliss k_smile blush1")
    g_cg.image("NozomiTortured_Spank feet_rest nozomi1_rub red1 underwear1_down sweat1 n1_smile k_smile blush1")

    g_cg.button("reversal good end")
    g_cg.condition("persistent.reversal_good_end_unlock")
    g_cg.image("ReversalGoodEnd bg1 sayori s_smile nozomi n_smile kyou k_smile hiroko h_smile risa r_neutral")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_smile nozomi n_smile kyou k_smile hiroko h_smile risa r_sigh")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_neutral hiroko h_concerned risa r_sigh")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_neutral hiroko h_surprised risa r_neutral_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_smirk nozomi n_neutral_side kyou k_neutral hiroko h_surprised risa r_neutral_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_smirk nozomi n_neutral_side kyou k_neutral hiroko h_angry risa r_neutral_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_happy nozomi n_neutral_side kyou k_neutral hiroko h_angry risa r_neutral_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_happy nozomi n_neutral_side kyou k_neutral hiroko h_angry h_blush risa r_neutral_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_happy nozomi n_neutral_side kyou k_neutral hiroko h_angry h_blush risa r_neutral")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_neutral hiroko h_concerned h_blush risa r_neutral")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_neutral hiroko h_concerned h_blush risa r_smug")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_concerned hiroko h_concerned h_blush risa r_smug")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_concerned hiroko h_concerned risa r_smile_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg2 sayori s_neutral nozomi n_nervous kyou k_neutral_side hiroko h_smile risa r_smile_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg2 sayori s_neutral nozomi n_nervous kyou k_smile hiroko h_smile risa r_smile_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg2 sayori s_neutral nozomi n_neutral_side kyou k_smile hiroko h_smile risa r_smile_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg2 sayori s_neutral nozomi n_neutral_side kyou k_smug hiroko h_smile risa r_smile_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg2 sayori s_curious nozomi n_neutral_side kyou k_smug hiroko h_smile risa r_smile_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg2 sayori s_curious nozomi n_smile kyou k_smile hiroko h_smile risa r_smile_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg2 sayori s_smirk nozomi n_smile kyou k_smile hiroko h_smile risa r_smile_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg2 sayori s_smirk nozomi n_happy n_blush kyou k_smile hiroko h_smile risa r_smile_side")
    g_cg.transform(galzoomout)
    g_cg.image("ReversalGoodEnd bg2 sayori s_smile nozomi n_smile n_blush kyou k_smile hiroko h_smile risa r_smile")
    g_cg.transform(galzoomout)

    g_cg.button("reversal bad end")
    g_cg.condition("persistent.reversal_bad_end_unlock")
    g_cg.image("ReversalBadEnd neutral")
    g_cg.image("ReversalBadEnd worried")
    g_cg.image("ReversalBadEnd curious")
    g_cg.image("ReversalBadEnd smile")
    g_cg.image("ReversalBadEnd wicked")

    g_cg.button("sayori room tickle")
    g_cg.condition("persistent.sayori_room_tickle_unlock")
    g_cg.image("SayoriRoom Tickle")
    g_cg.image("SayoriRoom Tickle sayoriback_sleepy")
    g_cg.image("SayoriRoom Tickle sayoriback_surprised_protag")
    g_cg.image("SayoriRoom Tickle sayoriback_quizzical_feet")
    g_cg.image("SayoriRoom Tickle sayoriback_quizzical_protag")
    g_cg.image("SayoriRoom Tickle kyouback_laugh sayoriback_quizzical_protag")
    g_cg.image("SayoriRoom Tickle kyouback_laugh sayoriback_annoyed_closed")
    g_cg.image("SayoriRoom Tickle kyouback_smile sayoriback_quizzical_protag")
    g_cg.image("SayoriRoom Tickle kyouback_smile sayoriback_surprised_feet sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyouback_smile sayoriback_anxious_feet sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyouback_smile sayoriback_annoyed_closed")
    g_cg.image("SayoriRoom Tickle kyouback_smirk sayoriback_annoyed_closed")
    g_cg.image("SayoriRoom Tickle kyouback_smirk sayoriback_anxious_protag")
    g_cg.image("SayoriRoom Tickle kyouback_smirk sayoriback_sleep")
    g_cg.image("SayoriRoom Tickle kyouback_smirk sayoriback_quizzical_protag")
    g_cg.image("SayoriRoom Tickle kyouback_smile sayoriback_quizzical_feet")
    g_cg.image("SayoriRoom Tickle kyouback_smile sayoriback_sleep")
    g_cg.image("SayoriRoom Tickle kyouback_smile sayoriback_sleep")
    g_cg.image("SayoriRoom Tickle kyouback_neutral sayoriback_sleep")
    g_cg.image("SayoriRoom Tickle kyougone kyounoface sayoriback_quizzical_protag")
    g_cg.image("SayoriRoom Tickle kyougone kyounoface sayoriback_surprised_protag")
    g_cg.image("SayoriRoom Tickle kyougone kyounoface sayoriback_angry")
    g_cg.image("SayoriRoom Tickle kyouback_neutral sayoriback_angry_protag")
    g_cg.image("SayoriRoom Tickle kyouback_neutral sayoriback_quizzical_protag")
    g_cg.image("SayoriRoom Tickle kyouback_neutral kyouback_blush sayoriback_quizzical_protag")
    g_cg.image("SayoriRoom Tickle kyouback_neutral kyouback_blush sayoriback_anxious_protag sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyouback_neutral kyouback_blush sayoriback_anxious_feet sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyouback_neutral sayoriback_anxious_protag sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyouback_neutral sayoriback_angry_protag sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyouback_neutral sayoriback_annoyed_closed sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_annoyed_closed sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_sleep")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_angry_protag")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_surprised_feet sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_smile sayoriback_surprised_feet sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_smirk sayoriback_surprised_feet sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_smirk sayoriback_giggle sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyouback_smirk Sayori_Front sayorifront_giggle sayorifront_blush sayori_nofoot")
    g_cg.image("SayoriRoom Tickle kyouback_smirk Sayori_Front sayorifront_pout sayorifront_blush sayori_nofoot")
    g_cg.image("SayoriRoom Tickle kyouback_laugh Sayori_Front sayorifront_pout sayorifront_blush sayori_nofoot")
    g_cg.image("SayoriRoom Tickle kyouback_smile Sayori_Front sayorifront_neutral sayorifront_blush sayori_nofoot")
    g_cg.image("SayoriRoom Tickle kyouback_smile Sayori_Front sayorifront_anxious sayori_nofoot")
    g_cg.image("SayoriRoom Tickle kyouback_smile sayoriback_sleep")
    g_cg.image("SayoriRoom Tickle kyouback_smile sayoriback_anxious_feet sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_anxious_feet sayoriback_blush")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_surprised_feet")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_smirk sayoriback_surprised_feet")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_smirk sayoriback_anxious_protag")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_smirk sayoriback_quizzical_protag")
    g_cg.image("SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_quizzical_protag")
    g_cg.image("SayoriRoom Tickle kyouback_neutral sayoriback_quizzical_protag")
    g_cg.image("SayoriRoom Tickle kyouback_neutral Sayori_Front sayorifront_neutral sayori_nofoot")
    g_cg.image("SayoriRoom Tickle kyouback_neutral Sayori_Front sayorifront_irritated sayori_nofoot")
    g_cg.image("SayoriRoom Tickle kyouback_neutral Sayori_Front sayorifront_anxious sayori_nofoot")
    g_cg.image("SayoriRoom Tickle kyouback_neutral Sayori_Front sayorifront_pout sayori_nofoot")
    g_cg.image("SayoriRoom Tickle kyouback_neutral Sayori_Front sayorifront_smirk sayori_nofoot")
    g_cg.image("SayoriRoom Tickle sayoriback_neutral kyougone kyounoface")
    g_cg.image("SayoriRoom Tickle sayoriback_smile kyougone kyounoface")
    g_cg.image("SayoriRoom Tickle sayoriback_happy kyougone kyounoface")

    g_cg.button("sayori dinner")
    g_cg.condition("persistent.sayori_dinner_unlock")
    g_cg.image("SayoriDinner nosayori")
    g_cg.image("SayoriDinner sayori_armsup laugh")
    g_cg.image("SayoriDinner sayori_armsup smile")
    g_cg.image("SayoriDinner sayori_armsup smile_side")
    g_cg.image("SayoriDinner sayori_armsup smile_closed")
    g_cg.image("SayoriDinner sayori_armsup neutral")
    g_cg.image("SayoriDinner sayori_armsup neutral_side")
    g_cg.image("SayoriDinner sayori_armsup smirk")
    g_cg.image("SayoriDinner sayori_armsup concerned")
    g_cg.image("SayoriDinner sayori_armsup concerned_closed")
    g_cg.image("SayoriDinner sayori_armsup surprised")
    g_cg.image("SayoriDinner sayori_armsup stern")
    g_cg.image("SayoriDinner sayori_armsup stern_side")
    g_cg.image("SayoriDinner sayori_armsup angry")
    g_cg.image("SayoriDinner sayori_armsup cry_open1")
    g_cg.image("SayoriDinner sayori_armsup cry_closed")
    g_cg.image("SayoriDinner sayori laugh")
    g_cg.image("SayoriDinner sayori smile")
    g_cg.image("SayoriDinner sayori smile_side")
    g_cg.image("SayoriDinner sayori smile_closed")
    g_cg.image("SayoriDinner sayori neutral")
    g_cg.image("SayoriDinner sayori neutral_side")
    g_cg.image("SayoriDinner sayori smirk")
    g_cg.image("SayoriDinner sayori concerned")
    g_cg.image("SayoriDinner sayori concerned_closed")
    g_cg.image("SayoriDinner sayori surprised")
    g_cg.image("SayoriDinner sayori stern")
    g_cg.image("SayoriDinner sayori stern_side")
    g_cg.image("SayoriDinner sayori angry")
    g_cg.image("SayoriDinner sayori cry_open1")
    g_cg.image("SayoriDinner sayori cry_closed")
    g_cg.image("SayoriDinner sayori laugh_cry")
    g_cg.image("SayoriDinner sayori cry_open2")
    g_cg.image("SayoriDinner sayori cry_smile")
    g_cg.image("SayoriDinner sayori_armsup_blush laugh")
    g_cg.image("SayoriDinner sayori_armsup_blush smile")
    g_cg.image("SayoriDinner sayori_armsup_blush smile_side")
    g_cg.image("SayoriDinner sayori_armsup_blush smile_closed")
    g_cg.image("SayoriDinner sayori_armsup_blush neutral")
    g_cg.image("SayoriDinner sayori_armsup_blush neutral_side")
    g_cg.image("SayoriDinner sayori_armsup_blush smirk")
    g_cg.image("SayoriDinner sayori_armsup_blush concerned")
    g_cg.image("SayoriDinner sayori_armsup_blush concerned_closed")
    g_cg.image("SayoriDinner sayori_armsup_blush surprised")
    g_cg.image("SayoriDinner sayori_armsup_blush stern")
    g_cg.image("SayoriDinner sayori_armsup_blush stern_side")
    g_cg.image("SayoriDinner sayori_armsup_blush angry")
    g_cg.image("SayoriDinner sayori_armsup_blush cry_open1")
    g_cg.image("SayoriDinner sayori_armsup_blush cry_closed")
    g_cg.image("SayoriDinner sayori_blush laugh")
    g_cg.image("SayoriDinner sayori_blush smile")
    g_cg.image("SayoriDinner sayori_blush smile_side")
    g_cg.image("SayoriDinner sayori_blush smile_closed")
    g_cg.image("SayoriDinner sayori_blush neutral")
    g_cg.image("SayoriDinner sayori_blush neutral_side")
    g_cg.image("SayoriDinner sayori_blush smirk")
    g_cg.image("SayoriDinner sayori_blush concerned")
    g_cg.image("SayoriDinner sayori_blush concerned_closed")
    g_cg.image("SayoriDinner sayori_blush surprised")
    g_cg.image("SayoriDinner sayori_blush stern")
    g_cg.image("SayoriDinner sayori_blush stern_side")
    g_cg.image("SayoriDinner sayori_blush angry")
    g_cg.image("SayoriDinner sayori_blush cry_open1")
    g_cg.image("SayoriDinner sayori_blush cry_closed")
    g_cg.image("SayoriDinner sayori_blush laugh_cry")
    g_cg.image("SayoriDinner sayori_blush cry_open2")
    g_cg.image("SayoriDinner sayori_blush cry_smile")

    g_cg.button("hiroko cam 1 1")
    g_cg.condition("persistent.hiroko_cam_1_1_unlock")
    g_cg.image("HirokoCam1 sleep_armdown sleep")
    g_cg.image("HirokoCam1 sleep_armdown sleeptalk")
    g_cg.image("HirokoCam1 sleep_armdown sleep")
    g_cg.image("HirokoCam1 sleep_armmid sleep")
    g_cg.image("HirokoCam1 sleep_armup sleep")
    g_cg.image("HirokoCam1 sleep_penlight sleep")
    g_cg.image("HirokoCam1 sleep_penlight sleeptalk")
    g_cg.image("HirokoCam1 sleep_penlight waking")
    g_cg.image("HirokoCam1 awake1 surprised")
    g_cg.image("HirokoCam1 awake1 happy")
    g_cg.image("HirokoCam1 awake2 cheerful sweat2")
    g_cg.condition("persistent.hiroko_cam_1_2_unlock")
    g_cg.image("HirokoCam1 awake2 smile sweat2")
    g_cg.condition("persistent.hiroko_cam_1_2_unlock")
    g_cg.image("HirokoCam1 sleep_armdown sleeptalk blush sweat1")
    g_cg.condition("persistent.hiroko_cam_1_2_unlock")
    g_cg.image("HirokoCam1 sleep_armdown sleep blush sweat1")
    g_cg.condition("persistent.hiroko_cam_1_2_unlock")

    g_cg.button("hiroko cam 2")
    g_cg.condition("persistent.hiroko_cam_2_unlock")
    g_cg.image("HirokoCam2 standing")
    g_cg.transform(galscroll(-0.2))
    g_cg.image("HirokoCam2 jumping")
    g_cg.transform(galscroll(-0.2))

    g_cg.button("hiroko karaoke bed 2")
    g_cg.condition("persistent.hiroko_cam_3_unlock")
    g_cg.image("cg hiroko karaoke bed 2")

    g_cg.button("hiroko bed")
    g_cg.condition("persistent.hiroko_bed_unlock")
    g_cg.image("HirokoBed sleeptalk")
    g_cg.image("HirokoBed sleep")
    g_cg.image("HirokoBed sleep_concerned")
    g_cg.image("HirokoBed waking")
    g_cg.image("HirokoBed sleeptalk_concerned")
    g_cg.image("HirokoBed sleepy")
    g_cg.image("HirokoBed nervous")
    g_cg.image("HirokoBed smile blush")
    g_cg.image("HirokoBed happy blush")
    g_cg.image("HirokoBed sleeptalk_concerned blush")

    g_cg.button("hiroko couch")
    g_cg.condition("persistent.hiroko_couch_unlock")
    g_cg.image("HirokoCouch neutral_l")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch sleeptalk")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch confused")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch frown")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_down n_frown frown")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_neutral neutral coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_neutral anxious coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk2 anxious coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk anxious coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_smile anxious coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_smile neutral coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk neutral_r coin_r")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk neutral coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk neutral_l coin_l")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk2 neutral_r coin_r")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk2 neutral coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk2 neutral_l coin_l")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_neutral dazed_r coin_r")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_neutral dazed coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_neutral dazed_l coin_l")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk dazed_r coin_r")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk dazed coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk dazed_l coin_l")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk sleepy_r coin_r")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk sleepy coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk sleepy_l coin_l")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk sleep coin_r")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk sleep coin")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_up n_talk sleep coin_l")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_down n_neutral sleep")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_down n_talk sleep")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_down n_talk2 sleep")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_down n_talk2 sleeptalk")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_down n_smile sleep")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_down n_neutral sleeptalk")
    g_cg.transform(galzoomout)
    g_cg.image("HirokoCouch nozomi_down n_smile sleepy")
    g_cg.transform(galzoomout)

    g_cg.button("hiroko couch2")
    g_cg.condition("persistent.hiroko_couch2_unlock")
    g_cg.image("HirokoCouch2 hiroko1 h_sleepy1")
    g_cg.image("HirokoCouch2 nozomi1a n_smile1 hiroko1 h_sleepyl1")
    g_cg.image("HirokoCouch2 nozomi1b n_smile1 hiroko2 h_sleep2")
    g_cg.image("HirokoCouch2 nozomi1b n_smile1 hiroko2 h_smile2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_frown2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_sleep2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_sleep2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_frownl2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_neutral2")
    g_cg.image("HirokoCouch2 nozomi1b n_sad1 hiroko2 h_neutral2")
    g_cg.image("HirokoCouch2 nozomi1b n_sad1 hiroko2 h_confused2")
    g_cg.image("HirokoCouch2 nozomi1b n_sad1 hiroko2 h_smile2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_smile2")
    g_cg.image("HirokoCouch2 nozomi1b n_happy1 hiroko2 h_smile2")
    g_cg.image("HirokoCouch2 nozomi1b n_smile1 hiroko2 h_smile2")
    g_cg.image("HirokoCouch2 nozomi2 n_grin2 hiroko1 h_surprised1 coin")
    g_cg.image("HirokoCouch2 nozomi2 n_happy2 hiroko1 h_surprised1 coin")
    g_cg.image("HirokoCouch2 nozomi2 n_smile2 hiroko1 h_sleepyr1 coin_r")
    g_cg.transform(coinswing_hc2)
    g_cg.image("HirokoCouch2 both n_surprisedd3 n_blush3 h_sleep3")
    g_cg.image("HirokoCouch2 both n_surprised3 n_blush3 h_sleep3")
    g_cg.image("HirokoCouch2 both n_smile3 h_sleep3")
    g_cg.image("HirokoCouch2 both n_neutral3 h_sleep3")
    g_cg.image("HirokoCouch2 both n_smile3 h_sleeptalk3")
    g_cg.image("HirokoCouch2 both n_happy3 h_sleepy3")
    g_cg.image("HirokoCouch2 both n_smile3 h_surprised3 h_blush3")
    g_cg.image("HirokoCouch2 both n_smile3 h_smile3 h_blush3")
    g_cg.image("HirokoCouch2 both n_happy3 n_blush3 h_smile3 h_blush3")
    g_cg.image("HirokoCouch2 nozomi1b n_happy1 n_blush1 hiroko2 h_happy2 h_blush2")
    g_cg.image("HirokoCouch2 nozomi1b n_smile1 n_blush1 hiroko2 h_smile2 h_blush2")
    g_cg.image("HirokoCouch2 nozomi1b n_smile1 n_blush1 hiroko2 h_confused2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_sigh2")
    g_cg.image("HirokoCouch2 nozomi1b n_happy1 hiroko2 h_sigh2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_neutrall2")
    g_cg.image("HirokoCouch2 nozomi1b n_smile1 hiroko2 h_neutrall2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_neutrall2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_neutral2")
    g_cg.image("HirokoCouch2 nozomi1b n_sad1 hiroko2 h_neutral2")
    g_cg.image("HirokoCouch2 nozomi1b n_frown1 hiroko2 h_neutral2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_neutral2")
    g_cg.image("HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_sad2")

    g_cg.button("hiroko cam 3")
    g_cg.condition("persistent.hiroko_cam_3_unlock")
    g_cg.image("HirokoCam3 pose1 n_neutral h_smile")
    g_cg.image("HirokoCam3 pose1 n_surprised h_smile")
    g_cg.image("HirokoCam3 pose1 n_neutral h_smile_light")
    g_cg.image("HirokoCam3 pose1 n_neutral h_dazed")
    g_cg.image("HirokoCam3 pose1 n_neutral h_dazed_light")
    g_cg.image("HirokoCam3 pose1 n_neutral h_sleepy")
    g_cg.image("HirokoCam3 pose1 n_neutral h_sleepy_light")
    g_cg.image("HirokoCam3 pose1 n_neutral h_sleep")
    g_cg.image("HirokoCam3 pose2 n_neutral")
    g_cg.image("HirokoCam3 pose3")
    g_cg.image("HirokoCam3 pose4")
    g_cg.image("HirokoCam3 pose1 n_awe h_sleep")
    g_cg.image("HirokoCam3 pose1 n_concerned h_sleep")
    g_cg.image("HirokoCam3 pose1 n_surprised h_sleep")
    g_cg.image("HirokoCam3 pose1 n_anxious blush h_sleep")
    g_cg.image("HirokoCam3 pose1 n_concerned blush h_sleep")

    g_cg.button("hiroko cam 4")
    g_cg.condition("persistent.hiroko_cam_4_unlock")
    g_cg.image("HirokoCam4 h1 h_neutral h_mask n1 n_neutral n_mask")
    g_cg.image("HirokoCam4 h1 h_smile h_mask n1 n_smile n_mask")
    g_cg.image("HirokoCam4 h2 h_happy h_mask n1 n_smile n_mask")
    g_cg.image("HirokoCam4 h2 h_happy h_mask n1 n_happy n_mask")
    g_cg.image("HirokoCam4 h2 h_happy h_mask n1 n_confused n_mask")
    g_cg.image("HirokoCam4 h1 h_worried h_mask n2 n_irritated n_mask")
    g_cg.image("HirokoCam4 h1 h_worried h_mask n2 n_rolleyes n_mask")
    g_cg.image("HirokoCam4 h1 h_neutral h_mask n2 n_neutral n_mask")
    g_cg.image("HirokoCam4 h1 h_smile h_mask n2 n_neutral n_mask")
    g_cg.image("HirokoCam4 h1 h_sleep h_mask n1 n_sleep n_mask")
    g_cg.image("HirokoCam4 h1 h_sleep h_mask n1 n_sleeptalk n_mask")
    g_cg.image("HirokoCam4 h1 h_sleep h_mask n1 n_irritated n_mask")
    g_cg.image("HirokoCam4 h1 h_sleep h_mask n1 n_sleeptalk_concerned n_mask")
    g_cg.image("HirokoCam4 h1 h_sleep h_mask n1 n_happy n_mask")
    g_cg.image("HirokoCam4 h1 h_sleeptalk h_mask n1 n_happy n_mask")
    g_cg.image("HirokoCam4 h1 h_waking h_mask n1 n_waking n_mask")
    g_cg.image("HirokoCam4 h1 h_smile n1 n_smile")
    g_cg.image("HirokoCam4 h1 h_smile n1 n_happy")
    g_cg.image("HirokoCam4 h1 h_smile n1 n_laugh n_blush1")
    g_cg.image("HirokoCam4 h1 h_smile n1 n_smile n_blush1")
    g_cg.image("HirokoCam4 h2 h_laugh h_blush1 n1 n_smile n_blush1")
    g_cg.image("HirokoCam4 h2 h_happy h_blush1 n1 n_smile n_blush1")
    g_cg.image("HirokoCam4 h1 h_sleep n1 n_sleep")
    g_cg.image("HirokoCam4 h1 h_sleeptalk n1 n_sleeptalk")
    g_cg.image("HirokoCam4 h1 h_waking n1 n_waking")
    g_cg.image("HirokoCam4 h1 h_waking n1 n_confused")
    g_cg.image("HirokoCam4 h1 h_confused n1 n_confused")
    g_cg.image("HirokoCam4 h1 h_worried n1 n_confused")
    g_cg.image("HirokoCam4 h3 n1 n_confused")
    g_cg.image("HirokoCam4 h3 n3")
    g_cg.image("HirokoCam4 h3 h_blush2 n3 n_blush2")
    g_cg.image("HirokoCam4 h1 h_scream h_blush1 n1 n_scream n_blush1")
    g_cg.image("HirokoCam4 h1 h_scream h_blush1 n1 n_angry n_blush1")
    g_cg.image("HirokoCam4 h1 h_sleeptalk n1 n_sleeptalk")
    g_cg.image("HirokoCam4 h1 h_sleep n1 n_sleep")
    g_cg.image("HirokoCam4 h1 h_sleep h_mask n1 n_sleep n_mask")
    g_cg.image("HirokoCam4 h1 h_sleeptalk h_mask n1 n_sleeptalk n_mask")
    g_cg.image("HirokoCam4 h1 h_waking h_mask n1 n_waking n_mask")
    g_cg.image("HirokoCam4 h1 h_smile h_mask n1 n_smile n_mask")
    g_cg.image("HirokoCam4 h1 h_smile h_mask n1 n_happy n_mask")
    g_cg.image("HirokoCam4 h1 h_laugh h_mask n1 n_happy n_mask")

    g_cg.button("hiroko cam 5")
    g_cg.condition("persistent.hiroko_cam_5_unlock")
    g_cg.image("HirokoCam5 h1 hm1 h_smile1 n1 nm1 n_pout1")
    g_cg.image("HirokoCam5 h1 hm1 h_smile1 n1 nm1 n_confused1")
    g_cg.image("HirokoCam5 h2 hm2 h_confused2 n1 nm1 n_frown1")
    g_cg.image("HirokoCam5 h2 hm2 h_frown2 n1 nm1 n_frown1")
    g_cg.image("HirokoCam5 h2 hm2 h_frown2 n1 nm1 n_surprised1")
    g_cg.image("HirokoCam5 h2 hm2 h_frown2 n1 nm1 n_derp1")
    g_cg.image("HirokoCam5 h2 hm2 h_confused2 n1 nm1 n_derp1")
    g_cg.image("HirokoCam5 h1 hm1 h_confused1 n1 nm1 n_derp1")
    g_cg.image("HirokoCam5 h2 hm2 h_smile2 n1 nm1 n_derp1")
    g_cg.image("HirokoCam5 h2 hm2 h_laugh2 n1 nm1 n_derp1")
    g_cg.image("HirokoCam5 h2 hm2 h_smirk2 n1 nm1 n_derp1")
    g_cg.image("HirokoCam5 h4 hm4 h_smirk4 nm1 n_derp1")
    g_cg.image("HirokoCam5 h4 hm4 h_laugh4 nm1 n_derp1")
    g_cg.image("HirokoCam5 h2 hm2 h_laugh2 n3 nm1 n_derp1")
    g_cg.image("HirokoCam5 h2 hm2 h_smile2 n3 nm1 n_derp1")
    g_cg.image("HirokoCam5 h2 hm2 h_smile2 n3 nm1 n_disgust1")
    g_cg.image("HirokoCam5 h2 hm2 h_smile2 n1 nm1 n_disgust1")
    g_cg.image("HirokoCam5 h2 hm2 h_laugh2 n1 nm1 n_disgust1")
    g_cg.image("HirokoCam5 h2 hm2 h_smile2 n2 nm2 n_confused2")
    g_cg.image("HirokoCam5 h2 hm2 h_smirk2 n2 nm2 n_confused2")
    g_cg.image("HirokoCam5 h2 hm2 h_smirk2 n2 nm2 n_frown2")
    g_cg.image("HirokoCam5 h2 hm2 h_surprised2 n2 nm2 n_frown2")
    g_cg.image("HirokoCam5 h2 hm2 h_derp2 n2 nm2 n_frown2")
    g_cg.image("HirokoCam5 h2 hm2 h_derp2 n2 nm2 n_smirk2")
    g_cg.image("HirokoCam5 h2 hm2 h_derp2 n4 nm2 n_smirk2")
    g_cg.image("HirokoCam5 h3 hm3 h_derp3 n4 nm2 n_smirk2")
    g_cg.image("HirokoCam5 h3 hm3 h_derp3 n2 nm2 n_happy2")
    g_cg.image("HirokoCam5 h3 hm3 h_derp3 n2 nm2 n_laugh2")
    g_cg.image("HirokoCam5 h3 hm3 h_derp3 n1 nm1 n_frown1")
    g_cg.image("HirokoCam5 h3 hm3 h_derp3 n1 nm1 n_pout1")
    g_cg.image("HirokoCam5 h1 hm1 h_disgust1 n2 nm2 n_happy2")
    g_cg.image("HirokoCam5 h1 hm1 h_disgust1 n2 nm2 n_laugh2")
    g_cg.image("HirokoCam5 h2 hm2 h_angry2 n2 nm2 n_laugh2")
    g_cg.image("HirokoCam5 h2 hm2 h_angry2 n2 nm2 n_derp2")
    g_cg.image("HirokoCam5 h2 hm2 h_smirk2 n2 nm2 n_derp2")
    g_cg.image("HirokoCam5 h2 hm2 h_smirk2 n1 nm1 n_frown1")
    g_cg.image("HirokoCam5 h2 hm2 h_frown2 n1 nm1 n_frown1")
    g_cg.image("HirokoCam5 h2 hm2 h_frown2 n2 nm2 n_frown2")
    g_cg.image("HirokoCam5 h2 hm2 h_derp2 n2 nm2 n_derp2")
    g_cg.image("HirokoCam5 h3 hm3 h_derp3 n3 nm1 n_derp1")
    g_cg.image("HirokoCam5 h1 hm1 h_sleep1 n1 nm1 n_sleep1")
    g_cg.image("HirokoCam5 h1 hm1 h_waking1 n1 nm1 n_waking1")
    g_cg.image("HirokoCam5 h1 hm1 h_happy1 n1 nm1 n_happy1")
    g_cg.image("HirokoCam5 h1 hm1 h_happy1 n1 nm1 n_smile1")
    g_cg.image("HirokoCam5 h1 hm1 h_smile1 n1 nm1 n_smile1")
    g_cg.image("HirokoCam5 h1 hm1 h_entrancedtalk1 n1 nm1 n_entrancedtalk1")
    g_cg.image("HirokoCam5 h1 hm1 h_entranced1 n1 nm1 n_entranced1")
    g_cg.image("HirokoCam5 h1 h_smile1 n1 n_confused1")
    g_cg.image("HirokoCam5 h2 h_laugh2 n1 n_confused1")
    g_cg.image("HirokoCam5 h2 h_laugh2 n2 n_happy2")
    g_cg.image("HirokoCam5 h2 h_smirk2 n2 n_happy2")
    g_cg.image("HirokoCam5 h2 h_smirk2 n1 n_pout1")
    g_cg.image("HirokoCam5 h2 h_smirk2 n1 n_neutral1")
    g_cg.image("HirokoCam5 h1 h_smile1 n1 n_neutral1")
    g_cg.image("HirokoCam5 h1 h_smile1 n1 n_frown1")
    g_cg.image("HirokoCam5 h1 h_smile1 n1 n_smile1")
    g_cg.image("HirokoCam5 h1 h_smile1 n1 n_disgust1")
    g_cg.image("HirokoCam5 h1 h_confused1 n1 n_smile1")
    g_cg.image("HirokoCam5 h1 h_disgust1 n1 n_smile1")
    g_cg.image("HirokoCam5 h1 h_happy1 n1 n_neutral1")
    g_cg.image("HirokoCam5 h1 h_happy1 n2 n_confused2")
    g_cg.image("HirokoCam5 h2 h_confused2 n2 n_confused2")
    g_cg.image("HirokoCam5 h2 h_confused2 n2 n_worried2")
    g_cg.image("HirokoCam5 h2 h_smile2 n2 n_worried2")
    g_cg.image("HirokoCam5 h2 h_smile2 n2 n_smile2")

    g_cg.button("nozo cam hypno") #Formerly known as "nozomi cam hypno"
    g_cg.condition("persistent.nozo_cam_hypno_unlock")
    g_cg.image("NozoCamHypno h_sleep head_down")
    g_cg.image("NozoCamHypno h_sleep head_up n_anxious")
    g_cg.image("NozoCamHypno h_sleep head_up n_curious")
    g_cg.image("NozoCamHypno h_sleep head_up n_anxious hand")
    g_cg.image("NozoCamHypno h_sleep head_up n_anxious_light hand")
    g_cg.image("NozoCamHypno h_sleep head_up n_awe hand")
    g_cg.image("NozoCamHypno h_sleep head_up n_awe_light hand")
    g_cg.image("NozoCamHypno h_sleep head_up n_curious hand")
    g_cg.image("NozoCamHypno h_sleep head_up n_curious_light hand")
    g_cg.image("NozoCamHypno h_sleep head_up n_anxious hand")
    g_cg.image("NozoCamHypno h_sleep head_up n_anxious_light hand")
    g_cg.image("NozoCamHypno h_sleep head_up n_sleepysmile hand")
    g_cg.image("NozoCamHypno h_sleep head_up n_sleepysmile_light hand")
    g_cg.image("NozoCamHypno h_sleep head_up n_sleep hand")
    g_cg.image("NozoCamHypno h_sleep head_up n_sleep")
    g_cg.image("NozoCamHypno h_sleeptalk head_up n_sleeptalk")
    g_cg.image("NozoCamHypno h_sleep head_up n_sleep")
    g_cg.image("NozoCamHypno h_waking head_up n_sleepy")
    g_cg.image("NozoCamHypno h_waking head_up n_curious")
    g_cg.image("NozoCamHypno h_curious head_up n_curious")


    g_cg.button("hiroko cam kiss")
    g_cg.condition("persistent.hiroko_cam_kiss_unlock")
    g_cg.image("HirokoCamKiss pose1")
    g_cg.image("HirokoCamKiss pose2 kissing")
    g_cg.image("HirokoCamKiss pose2 waking")
    g_cg.image("HirokoCamKiss pose3")

    g_cg.button("hiroko nozomi phone")
    g_cg.condition("persistent.hiroko_nozomi_phone_unlock")
    g_cg.image("HirokoNozomiPhone h_shocked n_shocked")
    g_cg.image("HirokoNozomiPhone h_worried n_shocked")
    g_cg.image("HirokoNozomiPhone h_worried n_scared")

    g_cg.button("sayori alter hug single image")
    g_cg.condition("persistent.sayori_alter_hug_unlock")
    g_cg.image("cg sayori alter hug")

    g_cg.button("sayori alter confrontation") #Formerly known as "sayori alter confrontation 1"
    g_cg.condition("persistent.sayori_alter_confrontation_unlock")
    g_cg.image("Sayori_Alter_Confrontation1")
    g_cg.image("Sayori_Alter_Confrontation1 sigh")
    g_cg.image("Sayori_Alter_Confrontation1 girls2 sad sigh")
    g_cg.image("Sayori_Alter_Confrontation1 girls2 sad smile")

    g_cg.button("rooftop reversal")
    g_cg.condition("persistent.rooftop_reversal_unlock")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek neutral", "RoofNozomi handsdown smile", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek surprised", "RoofNozomi handsdown panicked_right", "RoofSayori leanforward awe")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback surprised", "RoofNozomi handsdown panicked_right", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback smile", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback rolleyes", "RoofHiroko leanback smile", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback frown_left", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback rolleyes", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback sigh", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback sigh", "RoofHiroko leanback neutral", "RoofNozomi handsdown worried_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback rolleyes", "RoofHiroko leanback neutral", "RoofNozomi handsdown worried_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback rolleyes", "RoofNozomi handsdown worried_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback concerned_left", "RoofHiroko leanback rolleyes", "RoofNozomi handsdown worried_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral", "RoofHiroko leanback rolleyes", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback smirk", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback smirk", "RoofHiroko handcheek neutral", "RoofNozomi handsdown neutral", "RoofSayori leanforward smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback smirk", "RoofHiroko handcheek neutral", "RoofNozomi handsdown sigh", "RoofSayori leanforward smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback grin", "RoofHiroko handcheek neutral", "RoofNozomi handsdown sigh", "RoofSayori leanforward smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback grin", "RoofHiroko leanback neutral", "RoofNozomi handsdown worried_right", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko leanback neutral", "RoofNozomi handsdown worried_right", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko leanback rolleyes", "RoofNozomi handsdown worried_right", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko handcheek neutral", "RoofNozomi handsdown worried_right", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko handcheek neutral", "RoofNozomi handsdown panicked_right", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback grin", "RoofHiroko handcheek neutral", "RoofNozomi handsdown panicked_right blush", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown worried_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko handcheek worried", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown neutral_left blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback smirk", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback smirk", "RoofHiroko handcheek neutral", "RoofNozomi handsdown neutral blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko handcheek neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofRisa leanback surprised", "RoofHiroko leanback neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral", "RoofHiroko leanback neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko leanback neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback grin", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile", "RoofHiroko handcheek neutral", "RoofNozomi handsdown irritated blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko handcheek neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko handcheek neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback worried_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofRisa leanback concerned", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofRisa leanback grin", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofRisa leanback smile", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown growl blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback worried_left", "RoofNozomi handsdown growl blush", "RoofSayori leanback shocked")
    g_cg.image("cg rooftop day", "RoofRisa leanback frown_left", "RoofHiroko leanback worried_left", "RoofNozomi handsdown growl blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback frown_left", "RoofHiroko leanback worried_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback frown_left", "RoofHiroko leanback worried_left", "RoofNozomi handsdown angry_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback growl", "RoofHiroko leanback worried_left", "RoofNozomi handsdown angry_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback growl", "RoofHiroko leanback worried_left", "RoofNozomi handsdown growl_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback growl", "RoofHiroko leanback worried_right", "RoofNozomi handsdown growl_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback frown_left", "RoofHiroko leanback worried_right", "RoofNozomi handsdown growl_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofRisa leanback growl", "RoofHiroko leanback worried_right", "RoofNozomi handsdown growl_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko leanback surprised", "RoofNozomi handsdown worried_right", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko leanback worried_left", "RoofNozomi handsdown frown", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko leanback worried_left", "RoofNozomi handsdown regretful", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofNozomi handsdown regretful", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofNozomi handsdown regretful", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofNozomi handsdown crying", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofNozomi handsdown crying", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofNozomi handsdown crying", "RoofSayori leanforward frown")
    g_cg.image("cg rooftop day", "RoofNozomi handsdown crying")
    g_cg.image("cg rooftop day", "RoofNozomi handsdown frown")    

    g_cg.button("akiko intro2")
    g_cg.condition("persistent.akiko_intro2_unlock")
    g_cg.image("AkikoIntro2 confused")
    g_cg.image("AkikoIntro2 surprised")
    g_cg.image("AkikoIntro2 happy")

    g_cg.button("sayori alter bad end 3")
    g_cg.condition("persistent.sayori_alter_bad_end_3_unlock")
    g_cg.image("SayoriAlterBadEnd3 wink")
    g_cg.image("SayoriAlterBadEnd3 smile blink")

    g_cg.button("hiroko rooftop 1 1") #Formerly known as "hiroko rooftop 1-1" (with a hyphen)
    g_cg.condition("persistent.hiroko_rooftop_1_1_unlock")
    g_cg.image("HirokoRooftop1 h1 sleep_side")
    g_cg.image("HirokoRooftop1 h1 sad_side")
    g_cg.image("HirokoRooftop1 h1 neutral_side")
    g_cg.image("HirokoRooftop1 h2 neutral")
    g_cg.image("HirokoRooftop1 h2 frown")
    g_cg.image("HirokoRooftop1 h2 irritated")
    g_cg.image("HirokoRooftop1 h2 curious")
    g_cg.image("HirokoRooftop1 h2 smile")
    g_cg.image("HirokoRooftop1 h2 giggle")
    g_cg.image("HirokoRooftop1 h3 laugh")
    g_cg.image("HirokoRooftop1 h3 giggle")
    g_cg.image("HirokoRooftop1 h2 sleep")
    g_cg.image("HirokoRooftop1 h2 sadtalk_left")
    g_cg.image("HirokoRooftop1 h2 sad")
    g_cg.image("HirokoRooftop1 h2 sadtalk")
    g_cg.image("HirokoRooftop1 h2 nervous")
    g_cg.image("HirokoRooftop1 h2 sad_left")
    g_cg.image("HirokoRooftop1 h2 sad")
    g_cg.image("HirokoRooftop1 h2 growl")
    g_cg.image("HirokoRooftop1 h3 passionate")
    g_cg.image("HirokoRooftop1 h3 passionate_closed")
    g_cg.image("HirokoRooftop1 h3 sadtalk")
    g_cg.image("HirokoRooftop1 h2 surprised")
    g_cg.image("HirokoRooftop1 h2 surprised blush")
    g_cg.image("HirokoRooftop1 h3 passionate_closed blush")
    g_cg.image("HirokoRooftop1 h1 frown_side")
    g_cg.image("HirokoRooftop1 h2 neutral_left")
    g_cg.image("HirokoRooftop1 h3 furious")
    g_cg.image("HirokoRooftop1 h3 frown")
    g_cg.image("HirokoRooftop1 h2 kind")
    g_cg.image("HirokoRooftop1 h1 shocked_side")
    g_cg.image("HirokoRooftop1 h1 surprised_side")
    g_cg.image("HirokoRooftop1 h1 surprised_side2")
    g_cg.image("HirokoRooftop1 h3 furious")

    g_cg.button("hiroko rooftop 1 2") #Formerly known as "hiroko rooftop 1-2" (with a hyphen)
    g_cg.condition("persistent.hiroko_rooftop_1_2_unlock")
    g_cg.image("HirokoRooftop1 h1 sleep_side")
    g_cg.image("HirokoRooftop1 h1 surprised_side2")
    g_cg.image("HirokoRooftop1 h3 afraid")
    g_cg.image("HirokoRooftop1 h3 afraid_light")
    g_cg.image("HirokoRooftop1 h2 afraid")
    g_cg.image("HirokoRooftop1 h2 afraid_light")
    g_cg.image("HirokoRooftop1 h2 sleepy")
    g_cg.image("HirokoRooftop1 h2 sleepy_light")
    g_cg.image("HirokoRooftop1 h4 sleepy2")
    g_cg.image("HirokoRooftop1 h4 sleepy_light2")
    g_cg.image("HirokoRooftop1 h4 sleep2")
    g_cg.image("HirokoRooftop1 h4 sleeptalk2")

    g_cg.button("hiroko rooftop 2")
    g_cg.condition("persistent.hiroko_rooftop_2_unlock")
    g_cg.image("HirokoRooftop2 kyou_glare hiroko_glare")
    g_cg.image("HirokoRooftop2 kyou_surprised hiroko_glare")
    g_cg.image("HirokoRooftop2 kyou_laugh hiroko_smirk")
    g_cg.image("HirokoRooftop2 kyou_laugh hiroko_laugh")

    g_cg.button("penlight broken")
    g_cg.condition("persistent.penlight_broken_unlock")
    g_cg.image("PenlightBroken kyou1")
    g_cg.image("PenlightBroken kyou2")
    g_cg.image("PenlightBroken kyou3")

    g_cg.button("nozomi rooftop tickled") #Formerly known as "rooftop nozomi_tickled"
    g_cg.condition("persistent.nozomi_rooftop_tickled_unlock")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown strainedsmile", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown strainedsmile", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown strainedsmile", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown strainedsmile_left", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown strainedsmile_left", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown strainedsmile_left", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown strainedsmile", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown strainedsmile", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown strainedsmile_left blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown strainedsmile_left blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown panicked_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown laugh blush motionlines", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown laugh blush motionlines", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown laugh blush motionlines", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown panicked_left blush motionlines", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek shocked", "RoofNozomi laughing", "RoofSayori leanback shocked")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek shocked", "RoofNozomi laughing", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi laughing", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi laughing", "RoofSayori leanback angry")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek angry", "RoofNozomi laughing", "RoofSayori leanback angry")

    g_cg.button("nozomi rooftop spanked") #Formerly known as "rooftop nozomi_spanked"
    g_cg.condition("persistent.nozomi_rooftop_spanked_unlock")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown frown", "RoofSayori leanback smile")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown frown", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown frown", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown pain_left", "RoofSayori leanback sleep")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown pain_left", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown pain_left", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown pain_right", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown pain_right", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown smile_left blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown smile_left blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown panicked_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek surprised", "RoofNozomi handsdown grimace blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek surprised", "RoofNozomi handsdown pain_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek surprised", "RoofNozomi handsdown pain_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek surprised", "RoofNozomi handsdown grimace blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown grimace blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown pain_right blush", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown pain_right blush", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown grimace blush motionlines", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown frown motionlines", "RoofSayori leanback neutral")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown frown motionlines", "RoofSayori leanback worried")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek shocked", "RoofNozomi screaming", "RoofSayori leanback shocked")
    g_cg.image("cg rooftop day", "RoofHiroko handcheek shocked", "RoofNozomi screaming", "RoofSayori leanback worried blush")

    g_cg.button("nozomi rooftop tickle2")
    g_cg.condition("persistent.nozomi_rooftop_tickle2_unlock")
    g_cg.image("RoofNozomi2 nozomi_tickled lines_tickled hardlaugh blush")
    g_cg.image("RoofNozomi2 nozomi_tickled weaklaugh blush")

    g_cg.button("nozomi rooftop spank2")
    g_cg.condition("persistent.nozomi_rooftop_spank2_unlock")
    g_cg.image("RoofNozomi2 lines_spanked")
    g_cg.image("RoofNozomi2 lines_spanked scream")
    g_cg.image("RoofNozomi2")

    g_cg.button("nozomi provoke")
    g_cg.condition("persistent.nozomi_provoke_unlock")
    g_cg.image("NozomiProvoke angry blush arms1 kyou1")
    g_cg.image("NozomiProvoke frown blush arms1 kyou1")
    g_cg.image("NozomiProvoke scared blush arms1 kyou2")
    g_cg.image("NozomiProvoke scared_light blush arms1 kyou2")
    g_cg.image("NozomiProvoke dazed blush arms2 kyou2")
    g_cg.image("NozomiProvoke dazed_light blush arms2 kyou2")
    g_cg.image("NozomiProvoke sleepy arms2 kyou2")
    g_cg.image("NozomiProvoke sleepy_light arms2 kyou2")

    g_cg.button("nozomi couch strip")
    g_cg.condition("persistent.nozomi_couch_strip_unlock")
    g_cg.image("NozomiCouchStrip nozomi1 armdown nervous blush1 glasses1")
    g_cg.image("NozomiCouchStrip nozomi1 armup nervous blush1 glasses1")
    g_cg.image("NozomiCouchStrip nozomi1 armup disbelief blush1 glasses1")
    g_cg.image("NozomiCouchStrip nozomi2 frustrated blush2 glasses2")
    g_cg.image("NozomiCouchStrip nozomi3 frustrated blush2 glasses2")
    g_cg.image("NozomiCouchStrip nozomi4 pleading blush2 glasses2")
    g_cg.image("NozomiCouchStrip nozomi5")
    g_cg.image("NozomiCouchStrip nozomi6")

    g_cg.button("hypno rehearsal") #Formerly known as "hypno rehearsal 1"
    g_cg.condition("persistent.hypno_rehearsal_unlock")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_grumpy atsuko_sitting_socks a_confused nozomi_sitting_socks n_smile")
    g_cg.image("HypnoRehearsal1Gal kyou_left hiroko_sitting_socks h_growl h_hand1 atsuko_sitting_socks a_confused nozomi_sitting_socks n_smile")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_grumpy_light atsuko_sitting_socks a_confused_light nozomi_sitting_socks n_smile_light")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_relaxed")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed_light atsuko_sitting_socks a_relaxed_light nozomi_sitting_socks n_relaxed_light")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed_closed atsuko_sitting_socks a_relaxed_closed nozomi_sitting_socks n_relaxed_closed")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_irritated atsuko_sitting_socks a_irritated nozomi_sitting_socks n_irritated")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed_closed atsuko_laying_socks a_sleep nozomi_laying_socks n_sleep")
    g_cg.image("HypnoRehearsal1Gal hiroko_laying_socks h_sleep atsuko_laying_socks a_sleep nozomi_laying_socks n_sleep")
    g_cg.image("HypnoRehearsal1Gal hiroko_laying_socks h_wakingtalk atsuko_laying_socks a_waking nozomi_laying_socks n_waking")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_embarrassed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_relaxed")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_grumpy atsuko_sitting_socks a_neutral nozomi_sitting_socks n_neutral")
    g_cg.image("HypnoRehearsal1Gal kyou_left hiroko_sitting_socks h_grumpy h_hand1 atsuko_sitting_socks a_neutral nozomi_sitting_socks n_neutral")
    g_cg.image("HypnoRehearsal1Gal kyou_left hiroko_sitting_socks h_relaxed_closed h_hand1 atsuko_sitting_socks a_neutral nozomi_sitting_socks n_neutral")
    g_cg.image("HypnoRehearsal1Gal kyou_right_right hiroko_sitting_socks h_relaxed_closed atsuko_laying_socks a_sleep a_hand nozomi_sitting_socks n_neutral")
    g_cg.image("HypnoRehearsal1Gal kyou_right hiroko_sitting_socks h_relaxed_closed atsuko_laying_socks a_sleep a_hand nozomi_laying_socks n_sleep n_hand")
    g_cg.image("HypnoRehearsal1Gal kyou_right_left hiroko_laying_socks h_sleep atsuko_laying_socks a_sleep nozomi_laying_socks n_sleep n_hand")
    g_cg.image("HypnoRehearsal1Gal kyou_right_right hiroko_laying_socks h_sleep atsuko_laying_socks a_sleep a_hand nozomi_laying_socks n_sleep")
    g_cg.image("HypnoRehearsal1Gal kyou_left hiroko_laying_socks h_sleep h_hand2 atsuko_laying_socks a_sleep nozomi_laying_socks n_sleep")
    g_cg.image("HypnoRehearsal1Gal kyou_left hiroko_laying_socks h_sleeptalk h_hand2 atsuko_laying_socks a_sleep nozomi_laying_socks n_sleep")
    g_cg.image("HypnoRehearsal1Gal kyou_right hiroko_laying_socks h_sleep atsuko_laying_socks a_sleep a_hand nozomi_laying_socks n_sleep n_hand")
    g_cg.image("HypnoRehearsal1Gal atsuko_laying_socks a_sleep hiroko_laying_socks h_sleep nozomi_laying_socks n_sleep")
    g_cg.image("HypnoRehearsal1Gal atsuko_laying_socks a_waking hiroko_laying_socks h_waking nozomi_laying_socks n_waking")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_embarrassed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_relaxed")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_relaxed")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_smile")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_angry atsuko_sitting_socks a_neutral nozomi_sitting_socks n_neutral_left")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_neutral atsuko_sitting_socks a_happy nozomi_sitting_socks n_neutral_left")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_socks a_laugh nozomi_sitting_socks n_annoyed_left")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_socks a_smile nozomi_sitting_socks n_annoyed_left")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_socks a_smile_right nozomi_sitting_socks n_annoyed_left")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_socks a_smile_right nozomi_sitting_socks n_annoyed")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_socks a_neutral_right nozomi_sitting_socks n_annoyed_left")
    g_cg.image("HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_confused nozomi_sitting_socks n_annoyed_left")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_smug atsuko_sitting_onesock a_confused nozomi_sitting_socks n_neutral_left")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_smug atsuko_sitting_onesock a_neutral nozomi_sitting_socks n_neutral")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_smug atsuko_sitting_onesock a_neutral nozomi_laying_socks n_sleep")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_smug atsuko_sitting_onesock a_smile_right nozomi_laying_socks n_sleep")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile_right nozomi_protesting_socks n_growl_left")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile nozomi_sitting_socks n_neutral")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_growl atsuko_sitting_onesock a_smile nozomi_sitting_socks n_neutral")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_angry atsuko_sitting_onesock a_smile nozomi_sitting_socks n_neutral")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_laugh nozomi_sitting_socks n_irritated")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_laugh nozomi_protesting_socks n_angry_left")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile_right nozomi_protesting_socks n_angry_left")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile_right nozomi_protesting_socks n_angry")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile_right nozomi_protesting_socks n_growl")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile_right nozomi_protesting_socks n_angry")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_laugh nozomi_protesting_socks n_angry_left")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_laugh nozomi_protesting_socks n_angry")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_thieving_socks atsuko_sitting_onesock a_neutral_right nozomi_protesting_onesock n_confused")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_thieving_socks atsuko_sitting_onesock a_laugh nozomi_protesting_onesock n_growl_left")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_thieving_socks atsuko_sitting_onesock a_laugh nozomi_protesting_onesock n_angry_left")
    g_cg.image("HypnoRehearsal1Gal onesock hiroko_thieving_socks atsuko_sitting_onesock a_laugh nozomi_protesting_onesock n_angry")
    g_cg.image("HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_smug atsuko_sitting_onesock a_happy nozomi_sitting_onesock n_embarrassed")
    g_cg.image("HypnoRehearsal1Gal kyou_right_right twosocks hiroko_sitting_socks h_neutral_right atsuko_laying_onesock a_sleep nozomi_sitting_onesock n_neutral_left")
    g_cg.image("HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_laying_onesock a_waking nozomi_sitting_onesock n_neutral_left")
    g_cg.image("HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_confused nozomi_sitting_onesock n_neutral_left")
    g_cg.image("HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_neutral nozomi_sitting_onesock n_neutral_left")
    g_cg.image("HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_relaxed nozomi_sitting_onesock n_neutral_left")
    g_cg.image("HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_irritated nozomi_sitting_onesock n_neutral_left")
    g_cg.image("HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_angry nozomi_sitting_onesock n_neutral_left")

    g_cg.button("hypno rehearsal 2")
    g_cg.condition("persistent.hypno_rehearsal_2_unlock")
    g_cg.image("HypnoRehearsal2 neutral")
    g_cg.image("HypnoRehearsal2 smirk")
    g_cg.image("HypnoRehearsal2 thoughtful")
    g_cg.image("HypnoRehearsal2 concerned")
    g_cg.image("HypnoRehearsal2 laugh")
    g_cg.image("HypnoRehearsal2 grin")

    g_cg.button("sayori room hypno2")
    g_cg.condition("persistent.sayori_room_hypno2_unlock")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_neutral")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_neutral s_confused")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_confused s_confused")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_confused s_neutral")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_confused s_confused_closed")
    g_cg.image ("SayoriRoomHypno2 kyou k_frown s_confused_closed")
    g_cg.image ("SayoriRoomHypno2 kyou k_frown s_frown")
    g_cg.image ("SayoriRoomHypno2 kyou k_frown s_neutral")
    g_cg.image ("SayoriRoomHypno2 kyou k_smile s_neutral")
    g_cg.image ("SayoriRoomHypno2 kyou k_smile s_chuckle")
    g_cg.image ("SayoriRoomHypno2 kyou k_smile s_smile")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_smile light s_smile")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_smile light s_smile_flash")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_neutral light s_neutral")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_neutral light s_neutral_flash")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_neutral light s_drowsy")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_neutral light s_drowsy_flash")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_neutral light s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno2 kyou_penlight k2_neutral s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno2 kyou k_neutral s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno2 kyou k_neutral s_headdown s_sleeptalk")
    g_cg.image ("SayoriRoomHypno2 kyou k_frown s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno2 kyou k_smile s_headdown s_sleep")

    g_cg.button("sayori room hypno")
    g_cg.condition("persistent.sayori_room_hypno_unlock")
    g_cg.image ("SayoriRoomHypno")
    g_cg.image ("SayoriRoomHypno s_closed")
    g_cg.image ("SayoriRoomHypno s_closed_talk")
    g_cg.image ("SayoriRoomHypno s_neutral")
    g_cg.image ("SayoriRoomHypno s_confused_closed")
    g_cg.image ("SayoriRoomHypno k_handup s_confused_closed")
    g_cg.image ("SayoriRoomHypno k_handup s_confused")
    g_cg.image ("SayoriRoomHypno k_handup s_surprised_up")
    g_cg.image ("SayoriRoomHypno s_confused_closed")
    g_cg.image ("SayoriRoomHypno k_handup s_confused_up")
    g_cg.image ("SayoriRoomHypno s_confused_closed")
    g_cg.image ("SayoriRoomHypno s_confused_up")
    g_cg.image ("SayoriRoomHypno s_drowsy")
    g_cg.image ("SayoriRoomHypno s_confused_closed")
    g_cg.image ("SayoriRoomHypno s_sleepy")
    g_cg.image ("SayoriRoomHypno k_handsnap k_frown s_sleepy")
    g_cg.image ("SayoriRoomHypno k_handsnap k_frown s_armdown2 s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno k_frown s_armdown2 s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno k_handhold s_armup k_frown s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno s_armlap k_frown s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno s_armlap k_frown s_headdown s_sleeptalk")
    g_cg.image ("SayoriRoomHypno s_armlap s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno k_handshoulder s_armlap s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno k_handshoulder s_armlap s_headdown s_sleeptalk")
    g_cg.image ("SayoriRoomHypno s_armlap s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno k_frown s_armlap s_headdown s_sleep")
    g_cg.image ("SayoriRoomHypno s_armlap s_headdown s_waking")
    g_cg.image ("SayoriRoomHypno s_armlap2 s_surprised")
    g_cg.image ("SayoriRoomHypno s_armlap2 s_drowsy")
    g_cg.image ("SayoriRoomHypno s_armlap2 s_chuckle")
    g_cg.image ("SayoriRoomHypno s_armlap2 s_smile")
    g_cg.image ("SayoriRoomHypno s_armlap2 s_neutral")
    g_cg.image ("SayoriRoomHypno s_armlap2 s_closed_talk")
    g_cg.image ("SayoriRoomHypno s_armlap2 s_smile")

    g_cg.button("sayori doll pose1")
    g_cg.condition("persistent.sayori_doll_pose1_unlock")
    g_cg.image("SayoriDollPose1")
    g_cg.image("SayoriDollPose1 blush1")
    g_cg.image("SayoriDollPose1 pose2")
    g_cg.image("SayoriDollPose1 pose3 embarrassed_left blush3")
    g_cg.image("SayoriDollPose1 pose3_solo puzzled")
    g_cg.image("SayoriDollPose1 pose3_solo puzzled blush3")
    g_cg.image("SayoriDollPose1 pose3_solo annoyed blush3")
    g_cg.image("SayoriDollPose1 pose3_solo annoyed")
    g_cg.image("SayoriDollPose1 pose3_solo smile")
    g_cg.image("SayoriDollPose1 pose3_solo happy")
    g_cg.image("SayoriDollPose1 pose3_solo embarrassed_closed blush3")
    g_cg.image("SayoriDollPose1 pose3_solo embarrassed blush3")
    g_cg.image("SayoriDollPose1 pose3_solo embarrassed_left blush3")
    g_cg.image("SayoriDollPose1 pose3_solo embarrassed blush3")
    g_cg.image("SayoriDollPose1 pose3_solo puzzled blush3")
    g_cg.image("SayoriDollPose1 pose3_solo smirk blush3")

    g_cg.button("sayori doll pose2")
    g_cg.condition("persistent.sayori_doll_pose2_unlock")
    g_cg.image("SayoriDollPose2 couple1 head_up kyou_grin kyou_blush sayo_smirk sayo_blush")
    g_cg.image("SayoriDollPose2 couple1 head_up kyou_grin kyou_blush sayo_dazed sayo_blush")
    g_cg.image("SayoriDollPose2 couple1 head_up kyou_grin kyou_blush sayo_sleep")
    g_cg.image("SayoriDollPose2 couple1 head_down kyou_grin kyou_blush")
    g_cg.image("SayoriDollPose2 couple1 head_down kyou_smile")
    g_cg.image("SayoriDollPose2 couple2 kyou_neutral sayo_sleep")
    g_cg.image("SayoriDollPose2 couple2 kyou_neutral sayo_smile")
    g_cg.image("SayoriDollPose2 couple2 kyou_smile sayo_smile")
    g_cg.image("SayoriDollPose2 couple2 kyou_happy sayo_smile")
    g_cg.image("SayoriDollPose2 sayori sayo_smile")
    g_cg.image("SayoriDollPose2 couple3 sayo_smile")

    g_cg.button("sayori doll scene climax")
    g_cg.condition("persistent.sayori_doll_climax_unlock")
    g_cg.image("SayoriDollSceneClimax")

    g_cg.button("yikes end") #Formerly known as "hiroko yikes end"
    g_cg.condition("persistent.yikes_end_unlock")
    g_cg.image("Hiroko YikesEnd1 arms_out surprised blush")
    g_cg.image("Hiroko YikesEnd1 arms_in calm blush")
    g_cg.image("Hiroko YikesEnd1 couple2")
    g_cg.image("Hiroko YikesEnd1 couple3 smile")
    g_cg.image("Hiroko YikesEnd1 couple3 laugh")

    g_cg.button("alter good end 2") #Formerly known as "sayori alter good end 2"
    g_cg.condition("persistent.alter_good_end_2_unlock")
    g_cg.image ("Sayori AlterEnd3 n_confused h1 h_fists h_mad s1 s_surprised")
    g_cg.image ("Sayori AlterEnd3 n_neutral h1 h_fists h_growl s1 s_neutral")
    g_cg.image ("Sayori AlterEnd3 n_neutral h1 h_lowered h_frown s1 s_neutral")
    g_cg.image ("Sayori AlterEnd3 n_neutral h1 h_lowered h_growl s1 s_neutral")
    g_cg.image ("Sayori AlterEnd3 n_neutral h1 h_lowered h_rolleyes s1 s_neutral")
    g_cg.image ("Sayori AlterEnd3 n_neutral h1 h_lowered h_irritated s1 s_neutral")
    g_cg.image ("Sayori AlterEnd3 n_neutral h1 h_fists h_mad s1 s_neutral")
    g_cg.image ("Sayori AlterEnd3 n_confused h1 h_fists h_growl s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_confused h1 h_fists h_irritated s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_confused h1 h_fists h_pout s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral_right h2 h_fists h_frown_side s2 s_calm")
    g_cg.image ("Sayori AlterEnd3 n_neutral_right h2 h_fists h_frown_side s2 s_smile_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral_left h2 h_lowered h_smile_side s2 s_smile_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral_left h2 h_lowered h_smile_side s2 s_rolleyes")
    g_cg.image ("Sayori AlterEnd3 n_neutral h2 h_lowered h_smile_side s2 s_rolleyes")
    g_cg.image ("Sayori AlterEnd3 n_smile h2 h_lowered h_smile_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_glare h2 h_lowered h_neutral_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_glare h2 h_lowered h_frown_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_confused h2 h_lowered h_frown_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_confused h2 h_lowered h_pout_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral_right h2 h_lowered h_pout_side s2 s_calm")
    g_cg.image ("Sayori AlterEnd3 n_happy h2 h_lowered h_pout_side s2 s_calm")
    g_cg.image ("Sayori AlterEnd3 n_happy h2 h_lowered h_neutral_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_smile h2 h_lowered h_neutral_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_smile h2 h_fists h_frown_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_smile h2 h_fists h_frown_side s2 s_calm")
    g_cg.image ("Sayori AlterEnd3 n_glare h2 h_lowered h_frown_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_glare h2 h_lowered h_pout_side s2 s_rolleyes")
    g_cg.image ("Sayori AlterEnd3 n_pout h2 h_lowered h_pout_side s2 s_rolleyes")
    g_cg.image ("Sayori AlterEnd3 n_sad h2 h_lowered h_pout_side s2 s_rolleyes")
    g_cg.image ("Sayori AlterEnd3 n_sad h2 h_lowered h_smile_side s2 s_smile_side")
    g_cg.image ("Sayori AlterEnd3 n_sad h2 h_lowered h_pout_side s2 s_smile_side")
    g_cg.image ("Sayori AlterEnd3 n_happy h2 h_lowered h_pout_side s2 s_smirk_side")
    g_cg.image ("Sayori AlterEnd3 n_smile h1 h_lowered h_neutral s1 s_smirk")
    g_cg.image ("Sayori AlterEnd3 n_smile h1 h_lowered h_neutral s1 s_smile")
    g_cg.image ("Sayori AlterEnd3 n_happy h1 h_lowered h_neutral s1 s_smile")
    g_cg.image ("Sayori AlterEnd3 n_neutral_left h2 h_rolling h_neutral_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_smirk h2 h_rolling h_neutral_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_smirk h2 h_rolling h_pout_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_smirk h2 h_rolling h_pout_side s2 s_smirk_side")
    g_cg.image ("Sayori AlterEnd3 n_smirk h2 h_lowered h_pout_side s2 s_smirk_side")
    g_cg.image ("Sayori AlterEnd3 n_smile h2 h_lowered h_smile_side s2 s_smile_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral_right h2 h_lowered h_smile_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral_right h2 h_lowered h_smile_side s1 s_neutral")
    g_cg.image ("Sayori AlterEnd3 n_neutral h1 h_lowered h_neutral s1 s_neutral")
    g_cg.image ("Sayori AlterEnd3 n_neutral h1 h_lowered h_neutral s2 s_smile_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral h1 h_lowered h_neutral s1 s_smile")
    g_cg.image ("Sayori AlterEnd3 n_neutral h1 h_lowered h_awe s1 s_smile")
    g_cg.image ("Sayori AlterEnd3 n_neutral_right h1 h_lowered h_awe s2 s_smile_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral_right h2 h_lowered h_neutral_side s2 s_smile_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral_right h2 h_lowered h_neutral_side s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral_left h1 h_lowered h_neutral s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral_left h1 h_lowered h_confused s2 s_neutral_side")
    g_cg.image ("Sayori AlterEnd3 n_neutral h1 h_lowered h_neutral s1 s_neutral")
    g_cg.image ("Sayori AlterEnd3 n_smile h1 h_lowered h_smile s1 s_smile")
    g_cg.image ("Sayori AlterEnd3 n_smile h1 h_lowered h_laugh s1 s_smile")
    g_cg.image ("Sayori AlterEnd3 n_smile h1 h_lowered h_grin s1 s_smile")
    g_cg.image ("Sayori AlterEnd3 n_smile h2 h_lowered h_smile_side s2 s_smile_side")
    g_cg.image ("Sayori AlterEnd3 n_smile h2 h_lowered h_smile_side s2 s_rolleyes")
    g_cg.image ("Sayori AlterEnd3 n_smile h2 h_lowered h_smile_side s2 s_laugh")
    g_cg.image ("Sayori AlterEnd3 n_laugh h1 h_rolling h_laugh s2 s_laugh")
    g_cg.image ("Sayori AlterEnd3 n_laugh h1 h_rolling h_laugh s1 s_smile")

    g_cg.button("devotion end 1 single image")
    g_cg.condition("persistent.devotion_end_1_unlock")
    g_cg.image("cg devotion end 1")

    g_cg.button("devotion end 2")
    g_cg.condition("persistent.devotion_end_2_unlock")
    g_cg.image ("DevotionEnd2 nozomi1 arm_up n_smile n_blush k_smirk k_blush")
    g_cg.image ("DevotionEnd2 nozomi1 arm_up n_grin n_blush k_smirk k_blush")
    g_cg.image ("DevotionEnd2 nozomi2 arm_up n_grin n_blush k_surprised")
    g_cg.image ("DevotionEnd2 nozomi2 arm_up n_grin n_blush k_surprised_light")
    g_cg.image ("DevotionEnd2 nozomi2 arm_up n_giggle k_surprised")
    g_cg.image ("DevotionEnd2 nozomi2 arm_up n_giggle k_surprised_light")
    g_cg.image ("DevotionEnd2 nozomi2 arm_up n_giggle k_struggle")
    g_cg.image ("DevotionEnd2 nozomi2 arm_up n_giggle k_struggle_light")
    g_cg.image ("DevotionEnd2 nozomi2 arm_up n_giggle k_sleepy")
    g_cg.image ("DevotionEnd2 nozomi2 arm_up n_giggle k_sleepy_light")
    g_cg.image ("DevotionEnd2 nozomi2 arm_down n_giggle k_sleepy")
    g_cg.image ("DevotionEnd2 nozomi2 arm_down n_giggle k_sleepy_light")
    g_cg.image ("DevotionEnd2 nozomi2 arm_down n_grin k_sleepy")
    g_cg.image ("DevotionEnd2 nozomi2 arm_down n_grin k_sleepy_light")

    g_cg.button("nozomi interrogation")
    g_cg.condition("persistent.nozomi_interrogation_unlock")

    g_cg.button("trance stop end")
    g_cg.condition("persistent.trance_stop_end_unlock")
    g_cg.image("TranceStopEnd unsure")
    g_cg.image("TranceStopEnd smile")
    g_cg.image("TranceStopEnd happy")
    g_cg.image("TranceStopEnd laugh")

    g_cg.button("nozomi robot programming")
    g_cg.condition("persistent.nozomi_robot_programming_unlock")
    g_cg.image("NozomiRobotProgramming open")
    g_cg.image("NozomiRobotProgramming open kyou")
    g_cg.image("NozomiRobotProgramming closed kyou")

    g_cg.button("sayori grab")
    g_cg.condition("persistent.sayori_grab_unlock")
    g_cg.image("SayoriGrab sayori1 scared")
    g_cg.image("SayoriGrab sayori2 scared")
    g_cg.image("SayoriGrab sayori2 sad")

    g_cg.button("sayori x kyou")
    g_cg.condition("persistent.sayori_x_kyou_unlock")
    g_cg.image("cg sayori x kyou", "Sayori x Kyou surprised")
    g_cg.image("cg sayori x kyou", "Sayori x Kyou relaxed")

    g_cg.button("akiko breakfast")
    g_cg.condition("persistent.akiko_breakfast_unlock")
    g_cg.image("AkikoBreakfast smile")
    g_cg.image("AkikoBreakfast akiko_up smile")
    g_cg.image("AkikoBreakfast akiko_up smirk")
    g_cg.image("AkikoBreakfast akiko_down worried")
    g_cg.image("AkikoBreakfast akiko_up happy blush")
    g_cg.image("AkikoBreakfast akiko_up embarrassed blush")
    g_cg.image("AkikoBreakfast akiko_up smile blush")
    g_cg.image("AkikoBreakfast akiko_up happy")
    g_cg.image("AkikoBreakfast akiko_down smile_side")
    g_cg.image("AkikoBreakfast akiko_down smirk")
    g_cg.image("AkikoBreakfast akiko_down laugh")
    g_cg.image("AkikoBreakfast akiko_down annoyed")
    g_cg.image("AkikoBreakfast akiko_down smile")
    g_cg.image("AkikoBreakfast akiko_up neutral_side")
    g_cg.image("AkikoBreakfast akiko_up quizzical")
    g_cg.image("AkikoBreakfast akiko_up neutral")
    g_cg.image("AkikoBreakfast akiko_down neutral_closed")
    g_cg.image("AkikoBreakfast akiko_down annoyed")
    g_cg.image("AkikoBreakfast akiko_down surprised")
    g_cg.image("AkikoBreakfast akiko_down neutral")
    g_cg.image("AkikoBreakfast akiko_down smile")
    g_cg.image("AkikoBreakfast akiko_down happy")
    g_cg.image("AkikoBreakfast akiko_up worried_side")
    g_cg.image("AkikoBreakfast akiko_up neutral")
    g_cg.image("AkikoBreakfast akiko_up surprised")
    g_cg.image("AkikoBreakfast akiko_down quizzical")
    g_cg.image("AkikoBreakfast akiko_down surprised")
    g_cg.image("AkikoBreakfast akiko_down sigh")
    g_cg.image("AkikoBreakfast akiko_down neutral")
    g_cg.image("AkikoBreakfast akiko_down neutral_closed")
    g_cg.image("AkikoBreakfast akiko_up worried")
    g_cg.image("AkikoBreakfast akiko_up worried_side")
    g_cg.image("AkikoBreakfast akiko_down worried")
    g_cg.image("AkikoBreakfast akiko_down worried pancakes2")
    g_cg.image("AkikoBreakfast akiko_up sigh pancakes2")
    g_cg.image("AkikoBreakfast akiko_up neutral pancakes2")
    g_cg.image("AkikoBreakfast akiko_up annoyed pancakes2")
    g_cg.image("AkikoBreakfast akiko_down embarrassed pancakes2")
    g_cg.image("AkikoBreakfast akiko_down worried_side blush pancakes2")
    g_cg.image("AkikoBreakfast akiko_down neutral_closed pancakes2")
    g_cg.image("AkikoBreakfast akiko_up worried pancakes2")
    g_cg.image("AkikoBreakfast akiko_up sigh pancakes2")
    g_cg.image("AkikoBreakfast akiko_up neutral pancakes2")
    g_cg.image("AkikoBreakfast akiko_down surprised pancakes2")
    g_cg.image("AkikoBreakfast akiko_down worried pancakes2")
    g_cg.image("AkikoBreakfast akiko_down worried_side pancakes2")
    g_cg.image("AkikoBreakfast akiko_down sigh pancakes2")
    g_cg.image("AkikoBreakfast akiko_up neutral_side pancakes2")
    g_cg.image("AkikoBreakfast akiko_up smile pancakes2")
    g_cg.image("AkikoBreakfast akiko_down smile pancakes2")
    g_cg.image("AkikoBreakfast akiko_up quizzical pancakes2")
    g_cg.image("AkikoBreakfast akiko_up smirk pancakes2")
    g_cg.image("AkikoBreakfast akiko_up worried_side blush pancakes2")
    g_cg.image("AkikoBreakfast akiko_up happy pancakes2")
    g_cg.image("AkikoBreakfast akiko_up smile pancakes2")
    g_cg.image("AkikoBreakfast akiko_down smile pancakes2")
    g_cg.image("AkikoBreakfast akiko_down surprised pancakes2")
    g_cg.image("AkikoBreakfast akiko_up quizzical pancakes2")
    g_cg.image("AkikoBreakfast akiko_up embarrassed blush pancakes2")
    g_cg.image("AkikoBreakfast akiko_up happy blush pancakes2")
    g_cg.image("AkikoBreakfast akiko_down smile pancakes2")
    g_cg.image("AkikoBreakfast akiko_down neutral_side pancakes2")
    g_cg.image("AkikoBreakfast akiko_down quizzical pancakes2")
    g_cg.image("AkikoBreakfast akiko_down embarrassed blush pancakes2")
    g_cg.image("AkikoBreakfast akiko_down smirk blush pancakes2")
    g_cg.image("AkikoBreakfast akiko_down laugh blush pancakes2")
    g_cg.image("AkikoBreakfast akiko_up happy blush pancakes2")

    g_cg.button("redemption phone day")
    g_cg.condition("persistent.redemption_phone_day_unlock")
    g_cg.image("RedemptionPhoneDay quizzical_up_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneDay surprised_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneDay quizzical_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneDay tired_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneDay blanktalk_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneDay blank_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneDay blank glasses kyou")
    g_cg.image("RedemptionPhoneDay blanktalk glasses kyou")
    g_cg.image("RedemptionPhoneDay blank glasses kyou")
    g_cg.image("RedemptionPhoneDay surprised glasses kyou")
    g_cg.image("RedemptionPhoneDay tired glasses kyou")
    g_cg.image("RedemptionPhoneDay quizzical_up glasses kyou")

    g_cg.button("akiko slapped")
    g_cg.condition("persistent.akiko_slapped_unlock")
    g_cg.image("AkikoSlapped slapped")
    g_cg.image("AkikoSlapped sorry")

    g_cg.button("redemption phone eve")
    g_cg.condition("persistent.redemption_phone_eve_unlock")
    g_cg.image("RedemptionPhoneEve sleep glasses kyou")
    g_cg.image("RedemptionPhoneEve frown glasses kyou")
    g_cg.image("RedemptionPhoneEve sleep glasses kyou")
    g_cg.image("RedemptionPhoneEve sleep glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneEve frown_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneEve quizzical_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneEve tired_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneEve blanktalk_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneEve blank_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneEve sleep glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneEve sleep glasses kyou")
    g_cg.image("RedemptionPhoneEve happy glasses kyou")
    g_cg.image("RedemptionPhoneEve giggle glasses kyou")
    g_cg.image("RedemptionPhoneEve laugh glasses kyou")
    g_cg.image("RedemptionPhoneEve smile glasses kyou")
    g_cg.image("RedemptionPhoneEve laugh glasses kyou")
    g_cg.image("RedemptionPhoneEve quizzical_up glasses kyou")
    g_cg.image("RedemptionPhoneEve quizzical glasses kyou")
    g_cg.image("RedemptionPhoneEve happy blush glasses kyou")
    g_cg.image("RedemptionPhoneEve smile blush glasses kyou")
    g_cg.image("RedemptionPhoneEve laugh blush glasses kyou")
    g_cg.image("RedemptionPhoneEve quizzical_up blush glasses kyou")
    g_cg.image("RedemptionPhoneEve smile blush glasses kyou_phone")
    g_cg.image("RedemptionPhoneEve quizzical blush glasses kyou_phone")
    g_cg.image("RedemptionPhoneEve quizzical_up blush glasses kyou_phone")
    g_cg.image("RedemptionPhoneEve happy blush glasses kyou_phone")
    g_cg.image("RedemptionPhoneEve quizzical_sp blush glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneEve quizzical_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneEve blank_sp glasses_sp kyou_phone")
    g_cg.image("RedemptionPhoneEve blank glasses kyou")
    g_cg.image("RedemptionPhoneEve tired blush glasses kyou")
    g_cg.image("RedemptionPhoneEve giggle blush glasses kyou")

    g_cg.button("akiko kendo")
    g_cg.condition("persistent.akiko_kendo_unlock")
    g_cg.image("AkikoKendo akiko1 frown")
    g_cg.image("AkikoKendo akiko1 calm")
    g_cg.image("AkikoKendo akiko1 shout")
    g_cg.image("AkikoKendo akiko1 angry")
    g_cg.image("AkikoKendo akiko1 smirk")
    g_cg.image("AkikoKendo akiko1 confused")
    g_cg.image("AkikoKendo akiko1 nervous")
    g_cg.image("AkikoKendo akiko2 nervous")

    g_cg.button("sword strike single image")
    g_cg.condition("persistent.sword_strike_unlock")
    g_cg.image("cg sword strike")

    g_cg.button("akiko cornered")
    g_cg.condition("persistent.akiko_cornered_unlock")
    g_cg.image("AkikoCornered nervous")
    g_cg.image("AkikoCornered nervous_light")
    g_cg.image("AkikoCornered sleepy")
    g_cg.image("AkikoCornered sleepy_light")
    g_cg.image("AkikoCornered tranced")
    g_cg.image("AkikoCornered tranced_light")
    g_cg.image("AkikoCornered sleep")

    g_cg.button("voodoo phone")
    g_cg.condition("persistent.voodoo_phone_unlock")
    g_cg.image("VoodooPhone akiko1_uniform_socks surprised phone index_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks surprised blush1 phone index_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks shy_left blush1 phone index_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks shy_closed blush1 phone index_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks giggle blush1 phone index_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks shy blush1 phone index_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks shy blush1 phone index_up")
    g_cg.image("VoodooPhone akiko2_uniform_socks happy blush2 phone index_up")
    g_cg.image("VoodooPhone akiko2_uniform_socks wink blush2 phone index_up")
    g_cg.image("VoodooPhone akiko2_uniform_socks sheepish_left blush2 phone index_up")
    g_cg.image("VoodooPhone akiko2_uniform_socks sheepish blush2 phone index_down")
    g_cg.image("VoodooPhone akiko2_uniform_socks sheepish blush2 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks shocked blush1 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks giggle blush1 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko3_uniform_socks straining blush3 quivering1 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko3_uniform_socks laugh blush3 quivering1 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko3_uniform_socks laugh blush3 quivering1")
    g_cg.image("VoodooPhone akiko4_uniform_socks straining blush3 quivering2")
    g_cg.image("VoodooPhone akiko4_uniform_socks laugh blush3 quivering2")
    g_cg.image("VoodooPhone akiko4_uniform_socks laugh blush3 quivering2 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko4_uniform_socks grin blush3 quivering2 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko3_uniform_socks laugh blush3 quivering1 phone index_down")
    g_cg.image("VoodooPhone akiko4_uniform_socks grin blush3 phone index_down")
    g_cg.image("VoodooPhone akiko4_uniform_socks smile blush3")
    g_cg.image("VoodooPhone akiko1_uniform_socks shy blush1")
    g_cg.image("VoodooPhone akiko1_uniform_socks shy_left blush1")
    g_cg.image("VoodooPhone akiko2_uniform_socks sheepish blush2")
    g_cg.image("VoodooPhone akiko1_uniform_socks giggle blush1")
    g_cg.image("VoodooPhone akiko1_uniform_socks surprised blush1")
    g_cg.image("VoodooPhone akiko1_uniform_socks surprised blush1 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko2_uniform_socks happy blush2 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko2_uniform_socks sheepish blush2 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks giggle blush1 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko2_uniform_socks wink blush2 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks shy_closed blush1 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks shy blush1 phone index_down hand_down")
    g_cg.image("VoodooPhone akiko2_uniform_socks sheepish blush2 phone index_down hand_up")
    g_cg.image("VoodooPhone akiko1_uniform_socks shocked blush1deep phone index_down hand_up")
    g_cg.image("VoodooPhone akiko2_uniform_socks uncomfortable blush2deep phone index_down hand_up")
    g_cg.image("VoodooPhone akiko2_uniform_socks uncomfortable_left blush2deep phone index_down hand_up")
    g_cg.image("VoodooPhone akiko2_uniform_socks uncomfortable blush2deep phone index_down")
    g_cg.image("VoodooPhone akiko1_uniform_socks shy_left blush1 phone index_down")

    g_cg.button("hiroko scared single image")
    g_cg.condition("persistent.hiroko_scared_unlock")
    g_cg.image("cg hiroko scared")

    g_cg.button("bathroom ambush")
    g_cg.condition("persistent.bathroom_ambush_unlock")
    g_cg.image("BathroomAmbush akiko_up surprised glasses_sp kyou_up")
    g_cg.image("BathroomAmbush akiko_up furious glasses_sp kyou_up")
    g_cg.image("BathroomAmbush akiko_up angry glasses_sp kyou_up")
    g_cg.image("BathroomAmbush akiko_up anxious glasses_sp kyou_up")
    g_cg.image("BathroomAmbush akiko_down anxious glasses_sp kyou_up")
    g_cg.image("BathroomAmbush akiko_down sleepytalk glasses_sp kyou_up")
    g_cg.image("BathroomAmbush akiko_down sleepy glasses_sp kyou_up")
    g_cg.image("BathroomAmbush akiko_down sleepytalk glasses_sp kyou_down")
    g_cg.image("BathroomAmbush akiko_down sleepytalk blush glasses_sp kyou_down")
    g_cg.image("BathroomAmbush akiko_down entrancedtalk_sp glasses_sp kyou_down")
    g_cg.image("BathroomAmbush akiko_down entranced_sp glasses_sp kyou_down")
    g_cg.image("BathroomAmbush akiko_down entranced glasses")
    g_cg.image("BathroomAmbush akiko_down entrancedtalk glasses")

    g_cg.button("voodoo phone2")
    g_cg.condition("persistent.voodoo_phone2_unlock")
    g_cg.image("VoodooPhone akiko1_underwear giggle blush1")
    g_cg.image("VoodooPhone akiko2_underwear sheepish_left blush2")
    g_cg.image("VoodooPhone akiko1_underwear shy_closed blush1")
    g_cg.image("VoodooPhone akiko2_underwear uncomfortable blush2")
    g_cg.image("VoodooPhone akiko1_underwear surprised blush1")
    g_cg.image("VoodooPhone akiko1_underwear shy_left blush1")
    g_cg.image("VoodooPhone akiko2_underwear sheepish blush2")
    g_cg.image("VoodooPhone akiko1_underwear shy blush1")
    g_cg.image("VoodooPhone akiko2_underwear happy blush2")
    g_cg.image("VoodooPhone akiko2_underwear wink blush2")
    g_cg.image("VoodooPhone akiko1_underwear shy_closed2 blush1")
    g_cg.image("VoodooPhone akiko2_underwear uncomfortable_left blush2")
    g_cg.image("VoodooPhone akiko1_underwear shy")
    g_cg.image("VoodooPhone akiko2_underwear sheepish_left")
    g_cg.image("VoodooPhone akiko1_underwear shy_closed")
    g_cg.image("VoodooPhone akiko2_underwear sheepish")
    g_cg.image("VoodooPhone akiko2_underwear happy")
    g_cg.image("VoodooPhone akiko2_underwear uncomfortable")
    g_cg.image("VoodooPhone akiko1_underwear shy_left")
    g_cg.image("VoodooPhone akiko1_underwear giggle")
    g_cg.image("VoodooPhone akiko2_underwear uncomfortable_left")
    g_cg.image("VoodooPhone akiko1_underwear surprised")
    g_cg.image("VoodooPhone akiko1_underwear shy_closed2")
    g_cg.image("VoodooPhone akiko1_underwear neutral")
    g_cg.image("VoodooPhone akiko1_underwear talking")

    g_cg.button ("akiko kiss")
    g_cg.condition("persistent.akiko_kiss_unlock")
    g_cg.image("AkikoKiss climbing nervous blush1")
    g_cg.transform(galzoomout)
    g_cg.image("AkikoKiss climbing smile blush1")
    g_cg.transform(galzoomout)
    g_cg.image("AkikoKiss kissing blush2")
    g_cg.transform(galzoomout)
    g_cg.image("AkikoKiss climbing disoriented")
    g_cg.transform(galzoomout)
    g_cg.image("AkikoKiss kissing")
    g_cg.transform(galzoomout)

    g_cg.button("spiral ending")
    g_cg.condition("persistent.spiral_ending_unlock")
    g_cg.image("SpiralEnding furious scared")
    g_cg.image("SpiralEnding furious choking")
    g_cg.image("SpiralEnding calm scared")
    g_cg.image("SpiralEnding calm choking")

    g_cg.button("sayori hypno day") #Formerly known as "k room sayori day"
    g_cg.condition("persistent.sayori_hypno_day_unlock")
    g_cg.image("cg k room day", "SayoriHypnoDay smile")
    g_cg.image("cg k room day", "SayoriHypnoDay neutral")
    g_cg.image("cg k room day", "SayoriHypnoDay sad")
    g_cg.image("cg k room day", "SayoriHypnoDay neutral_closed")
    g_cg.image("cg k room day", "SayoriHypnoDay neutral")
    g_cg.image("cg k room day", "SayoriHypnoDay stern")
    g_cg.image("cg k room day", "SayoriHypnoDay looking")
    g_cg.image("cg k room day", "SayoriHypnoDay drowsy")
    g_cg.image("cg k room day", "SayoriHypnoDay head_down sleep")
    g_cg.image("cg k room day", "SayoriHypnoDay head_down sleeptalk")
    g_cg.image("cg k room day", "SayoriHypnoDay head_up drowsytalk")
    g_cg.image("cg k room day", "SayoriHypnoDay head_up happy")
    g_cg.image("cg k room day", "SayoriHypnoDay angry")

    g_cg.button("nozomi cola")
    g_cg.condition("persistent.nozomi_cola_unlock")

    g_cg.button("delusion end 1 single image")
    g_cg.condition("persistent.delusion_end_1_unlock")
    g_cg.image("cg delusion end 1")

    g_cg.button("robot karaoke end")
    g_cg.condition("persistent.robot_karaoke_end_unlock")
    g_cg.image("RobotKaraoke nozomi1 n_happy h_happy")
    g_cg.image("RobotKaraoke nozomi1 n_smile h_happy lyric1")
    g_cg.image("RobotKaraoke nozomi1 n_neutral h_happy lyric2")
    g_cg.image("RobotKaraoke nozomi1 n_neutral h_sing lyric2")
    g_cg.image("RobotKaraoke nozomi1 n_unsure h_sing lyric2")
    g_cg.image("RobotKaraoke nozomi1 n_unsure h_sing_n lyric1")
    g_cg.image("RobotKaraoke nozomi1 n_unsure h_sing_n")
    g_cg.image("RobotKaraoke nozomi1 n_unsure_closed h_sing lyric1")
    g_cg.image("RobotKaraoke nozomi1 n_unsure_closed h_happy lyric2")
    g_cg.image("RobotKaraoke nozomi1 n_tearful h_sing lyric2")
    g_cg.image("RobotKaraoke nozomi1 n_cry h_sing lyric1")
    g_cg.image("RobotKaraoke nozomi1 n_cry h_peaceful lyric1")
    g_cg.image("RobotKaraoke nozomi2 h_smile")

    g_cg.button("k bedroom robot nozomi")
    g_cg.condition("persistent.k_bedroom_robot_nozomi_unlock")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo upper")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo robot closed")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo robot open")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo upper", "Nozomi_K_Bedroom_Robo robot closed")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo confused")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo panicked")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo lower", "Nozomi_K_Bedroom_Robo panicked blush")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo panicked neutral")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo robot closed")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo upper")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo robot noglasses closed")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo robot noglasses open")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo upper", "Nozomi_K_Bedroom_Robo robot noglasses closed")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo confused noglasses")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo panicked noglasses")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo lower", "Nozomi_K_Bedroom_Robo panicked blush noglasses")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo panicked noglasses neutral")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo robot noglasses closed")

    g_cg.button("k bedroom robot hiroko")
    g_cg.condition("persistent.k_bedroom_robot_hiroko_unlock")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo upper")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo robot closed")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo robot open")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo upper", "Hiroko_K_Bedroom_Robo robot closed")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo confused")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo panicked body")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo lower", "Hiroko_K_Bedroom_Robo panicked blush")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo panicked body neutral")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo robot closed")

    g_cg.button("k bedroom robot sayori")
    g_cg.condition("persistent.k_bedroom_robot_sayori_unlock")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo upper")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo robot closed")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo robot open")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo upper", "Sayori_K_Bedroom_Robo robot closed")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo confused")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo panicked body")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo lower", "Sayori_K_Bedroom_Robo panicked blush ")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo panicked body neutral")
    g_cg.image("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo robot closed")

    g_cg.button("sayori alter confrontation2")
    g_cg.condition("persistent.sayori_alter_confrontation2_unlock")
    g_cg.image("Sayori_Alter_Confrontation2")
    g_cg.image("Sayori_Alter_Confrontation2 nozomi_bw")
    g_cg.image("Sayori_Alter_Confrontation2 nozomi_bw worried_bw")
    g_cg.image("Sayori_Alter_Confrontation2 nozomi_bw scared_bw")
    g_cg.image("Sayori_Alter_Confrontation2 nozomi_bw grin_bw scared_bw")
    g_cg.image("Sayori_Alter_Confrontation2 grin_bw scared_bw")
    g_cg.image("Sayori_Alter_Confrontation2 bg shadow nozomi_blush sayori smirk angry glasses")
    g_cg.image("Sayori_Alter_Confrontation2 bg shadow nozomi sayori smirk angry glasses")
    g_cg.image("Sayori_Alter_Confrontation2 bg shadow nozomi sayori smirk worried glasses")
    g_cg.image("Sayori_Alter_Confrontation2 bg shadow nozomi sayori smirk scared glasses")
    g_cg.image("Sayori_Alter_Confrontation2 bg shadow nozomi sayori grin scared glasses")
    g_cg.image("Sayori_Alter_Confrontation2 bg shadow nozomi_blush sayori grin scared glasses")

    g_cg.button("sayori alter coop end")
    g_cg.condition("persistent.alter_coop_end_1_unlock")
    g_cg.image("cg sayori alter coop end")

    g_cg.button("alter bad end 1") #Formerly known as "sayori alter bad end 1"
    g_cg.condition("persistent.alter_bad_end_1_unlock")
    g_cg.image("Sayori AlterEnd2")
    g_cg.image("Sayori AlterEnd2 side_open")
    g_cg.image("Sayori AlterEnd2 body_facing_down facing_open")
    g_cg.image("Sayori AlterEnd2 body_facing_down facing_closed")
    g_cg.image("Sayori AlterEnd2 body_facing_down facing_open")
    g_cg.image("Sayori AlterEnd2 bg body_facing_up facing_open")
    g_cg.image("Sayori AlterEnd2 bg body_side side_open")
    g_cg.image("Sayori AlterEnd2")
    g_cg.image("Sayori AlterEnd2 bg body_none eyes_none")

    g_cg.button("sayori alter bad end 2")
    g_cg.condition("persistent.alter_bad_end_2_unlock")
    g_cg.image("cg sayori alter bad end 2")

    g_cg.button("alter good end 1") #Formerly known as "sayori alter good end 1"
    g_cg.condition("persistent.alter_good_end_1_unlock")
    g_cg.image ("cg sayori alter good end 1", "Sayori AlterEnd1 concerned")
    g_cg.image ("cg sayori alter good end 1", "Sayori AlterEnd1 blush happy")

    g_cg.button("trance abuse end")
    g_cg.condition("persistent.trance_abuse_end_unlock")
    g_cg.image("TranceAbuseEnd smile")
    g_cg.image("TranceAbuseEnd shy_left")
    g_cg.image("TranceAbuseEnd shy blush")
    g_cg.image("TranceAbuseEnd shy_left blush")
    g_cg.image("TranceAbuseEnd shy blush hand")
    g_cg.image("TranceAbuseEnd excited blush hand")
    g_cg.image("TranceAbuseEnd smirk blush hand")
    g_cg.image("TranceAbuseEnd manic blush hand")
    g_cg.image("TranceAbuseEnd perverted blush hand nozomi_hand")

    g_cg.button("school cafe 1 single image")
    g_cg.condition("persistent.school_cafe_1_unlock")
    g_cg.image("cg school cafe")

    g_cg.button("zombie ending 1")
    g_cg.condition("persistent.zombie_ending_1_unlock")
    g_cg.image("ZombieEnding1 kyou k_smile point fingers_apart nozomi1 n_irritated")
    g_cg.image("ZombieEnding1 kyou k_smile point fingers_apart nozomi1 n_frown")
    g_cg.image("ZombieEnding1 kyou k_smile point fingers_apart nozomi1 n_straining blush1")
    g_cg.image("ZombieEnding1 kyou k_smile point fingers_closing nozomi1 n_straining blush1")
    g_cg.image("ZombieEnding1 kyou k_neutral rest fingers_closing nozomi1 n_focused")
    g_cg.image("ZombieEnding1 kyou k_neutral rest fingers_touch nozomi1 n_focused")
    g_cg.image("ZombieEnding1 kyou k_neutral snap fingers_touch nozomi1 n_focused")
    g_cg.image("ZombieEnding1 kyou k_neutral snap fingers_touch nozomi1 n_relaxed")
    g_cg.image("ZombieEnding1 kyou k_neutral rest nozomi2 n_sleep")
    g_cg.image("ZombieEnding1 kyou k_neutral rest nozomi2 n_sleeptalk")
    g_cg.image("ZombieEnding1 kyou k_smile rest nozomi2 n_sleep")
    g_cg.image("ZombieEnding1 kyou k_smile rest nozomi2 n_sleeptalk")
    g_cg.image("ZombieEnding1 kyou k_smile snap nozomi2 n_waking")
    g_cg.image("ZombieEnding1 kyou k_smile rest nozomi2 n_waking")
    g_cg.image("ZombieEnding1 kyou k_smile rest nozomi3 n_surprised")
    g_cg.image("ZombieEnding1 kyou k_smile rest nozomi3 n_smile")
    g_cg.image("ZombieEnding1 kyou k_smile rest nozomi3 n_smile blush3")
    g_cg.image("ZombieEnding1 kyou k_laugh rest nozomi3 n_smile blush3")
    g_cg.image("ZombieEnding1 kyou k_laugh rest nozomi3 n_laugh blush3")
    g_cg.image("ZombieEnding1 kyou k_laugh rest nozomi3 n_happy blush3")
    g_cg.image("ZombieEnding1")

    g_cg.button("hiroko stageshow good")
    g_cg.condition("persistent.hiroko_stageshow_good_unlock")
    g_cg.image("Hiroko StageShow bg_s kyou_s k_armup_s k_smile_s chairs_s male1_s female1_s hiroko_s male2_s nozomi_s")
    g_cg.image("Hiroko StageShow bg_s kyou_s k_armdown_s k_smile_s chairs_s male1_s female1_s hiroko_s h_hands_s male2_s nozomi_s")
    g_cg.image("Hiroko StageShow bg_s kyou_s k_armup_s k_smile_s chairs_s female1_s male2_s nozomi_s")

    g_cg.button("hiroko stageshow cat")
    g_cg.condition("persistent.hiroko_stageshow_cat_unlock")
    g_cg.image("Hiroko StageShow_Cat")
    g_cg.image("Hiroko StageShow_Cat licking_side guy")
    g_cg.image("Hiroko StageShow_Cat arm_down annoyed guy")
    g_cg.image("Hiroko StageShow_Cat hiroko_angry guy")
    g_cg.image("Hiroko StageShow_Cat hiroko_angry guy sweatdrops")

    g_cg.button("sayori stageshow catalepsy")
    g_cg.condition("persistent.sayori_stageshow_catalepsy_unlock")
    g_cg.image ("Sayori StageShow_Catalepsy")
    g_cg.image ("Sayori StageShow_Catalepsy arm_up")

    g_cg.button("sayori chicken1")
    g_cg.condition("persistent.sayori_chicken1_unlock")
    g_cg.image ("SayoriChicken1 kyou1 k_smile sayori2 s_sleep")
    g_cg.image ("SayoriChicken1 kyou1 k_smile_side sayori2 s_sleep")
    g_cg.image ("SayoriChicken1 kyou1 k_neutral_side sayori2 s_sleep")
    g_cg.image ("SayoriChicken1 kyou2 k_neutral_side sayori2 s_sleep")
    g_cg.image ("SayoriChicken1 kyou2 k_neutral sayori2 s_sleep")
    g_cg.image ("SayoriChicken1 kyou2 k_smile_side sayori2 s_sleep")
    g_cg.image ("SayoriChicken1 kyou1 k_smile sayori2 s_sleeptalk")
    g_cg.image ("SayoriChicken1 kyou1 k_smile sayori2 s_waking")
    g_cg.image ("SayoriChicken1 kyou2 k_laugh sayori3 s_shock blush")
    g_cg.image ("SayoriChicken1 kyou2 k_smirk sayori3 s_struggling blush")
    g_cg.image ("SayoriChicken1 kyou2 k_smirk sayori3 s_shock blush")
    g_cg.image ("SayoriChicken1 kyou3 k_smile sayori3 s_struggling blush")
    g_cg.image ("SayoriChicken1 kyou3 k_smile sayori3 s_chicken")

    g_cg.button("sayori chicken2")
    g_cg.condition("persistent.sayori_chicken2_unlock")
    g_cg.image ("SayoriChicken2 head_down dazed kyou")
    g_cg.image ("SayoriChicken2 head_down surprised")
    g_cg.image ("SayoriChicken2 head_up embarrassed")
    g_cg.image ("SayoriChicken2 head_up embarrassed_side")

    g_cg.button("sayori doll bad end single image")
    g_cg.condition("persistent.sayori_doll_bad_end_unlock")
    g_cg.image("cg sayori doll bad end")
    g_cg.transform(galscroll(0.0))

    g_cg.button("sayori doll good end")
    g_cg.condition("persistent.sayori_doll_good_end_unlock")
    g_cg.image ("SayoriDollEnd1")
    g_cg.image ("SayoriDollEnd1 sleep_down")
    g_cg.image ("SayoriDollEnd1 kyou_arms arms_down sleep_down")
    g_cg.image ("SayoriDollEnd1 kyou_chin arms_down head_up sleep_up")
    g_cg.image ("SayoriDollEnd1 kyou_back arms_down head_up sleep_up")
    g_cg.image ("SayoriDollEnd1 arms_down head_up smile")

    g_cg.button("hiroko good end 1")
    g_cg.condition("persistent.hiroko_good_end_1_unlock")
    g_cg.image ("cg school ext night", "Hiroko GoodEnd1 body smile")
    g_cg.image ("cg school ext night", "Hiroko GoodEnd1 blush smile")
    g_cg.image ("cg school ext night", "Hiroko GoodEnd1 blush laugh")

    g_cg.button("hiroko betrayal")
    g_cg.condition("persistent.hiroko_betrayal_unlock")
    g_cg.image ("HirokoBetrayal hiroko happy")
    g_cg.image ("HirokoBetrayal hiroko neutral")
    g_cg.image ("HirokoBetrayal hiroko curious")
    g_cg.image ("HirokoBetrayal hiroko awe")
    g_cg.image ("HirokoBetrayal hiroko smile")
    g_cg.image ("HirokoBetrayal hiroko grin")
    g_cg.image ("HirokoBetrayal hiroko concerned")
    g_cg.image ("HirokoBetrayal hiroko sad")
    g_cg.image ("HirokoBetrayal")

    g_cg.button("copycat ending 1 single image")
    g_cg.condition("persistent.copycat_ending_1_unlock")
    g_cg.image ("cg copycat ending 1")

    g_cg.button("copycat ending 2_1")
    g_cg.condition("persistent.copycat_ending_2_1_unlock")
    g_cg.image ("CopycatEnd2 blanktalk akiko_a smile")
    g_cg.image ("CopycatEnd2 blank akiko_a happy")
    g_cg.image ("CopycatEnd2 blank akiko_a grin")
    g_cg.image ("CopycatEnd2 blank akiko_a confused")
    g_cg.image ("CopycatEnd2 blanktalk akiko_a confused")
    g_cg.image ("CopycatEnd2 blank akiko_a happy blush")
    g_cg.image ("CopycatEnd2 blank akiko_a smile blush")

    g_cg.button("copycat ending 2_2")
    g_cg.condition("persistent.copycat_ending_2_2_unlock")
    g_cg.image ("CopycatEnd2 blanktalk akiko_b smile")
    g_cg.image ("CopycatEnd2 blank akiko_b happy")
    g_cg.image ("CopycatEnd2 blank akiko_b grin")
    g_cg.image ("CopycatEnd2 blank akiko_b confused")
    g_cg.image ("CopycatEnd2 blanktalk akiko_b confused")
    g_cg.image ("CopycatEnd2 blank akiko_b happy blush")
    g_cg.image ("CopycatEnd2 blank akiko_b smile blush")

    g_cg.button("redemption ending 1_1")
    g_cg.condition("persistent.redemption_ending_1_1_unlock")
    g_cg.image ("Redemption_Ending_1-1 kyou_room_s akiko_s quizzical_s glasses_s")
    g_cg.image ("Redemption_Ending_1-1 kyou_room_s akiko_s embarrassed_s blush_s glasses_s nokyou")
    g_cg.image ("Redemption_Ending_1-1 kyou_room_s akiko_s neutral_s glasses_s")
    g_cg.image ("Redemption_Ending_1-1 kyou_room_s akiko_s neutral_s kyou_s glasses_s")
    g_cg.image ("Redemption_Ending_1-1 kyou_room_s akiko_s sleep_s kyou_s glasses_s")
    g_cg.image ("Redemption_Ending_1-1 kyou_room_s akiko_s sleeptalk_s kyou_s glasses_s")
    g_cg.image ("Redemption_Ending_1-1 kyou_room_s akiko_s sleep_s kyou_s glasses_s")
    g_cg.image ("Redemption_Ending_1-1 kyou_room_s akiko_s sleep_s glasses_s")
    g_cg.image ("Redemption_Ending_1-1 kyou_room_s akiko_s waking_s glasses_s")
    g_cg.image ("Redemption_Ending_1-1 kyou_room_s akiko_s smile_s glasses_s")

    g_cg.button("redemption ending 1_2")
    g_cg.condition("persistent.redemption_ending_1_2_unlock")
    g_cg.image ("Redemption_Ending_1-2")
    g_cg.image ("Redemption_Ending_1-2 laugh")
    g_cg.image ("Redemption_Ending_1-2 talk")
    g_cg.image ("Redemption_Ending_1-2 arms_up smile")
    g_cg.image ("Redemption_Ending_1-2 arms_up talk")

    g_cg.button("hiroko park hypno")
    g_cg.condition("persistent.hiroko_park_hypno_unlock")
    g_cg.image ("HirokoParkHypno")
    g_cg.image ("HirokoParkHypno hiroko_arms_out")
    g_cg.image ("HirokoParkHypno hiroko_arms_out kyou_holding")
    g_cg.image ("HirokoParkHypno hiroko_arms_out kyou_pointing")
    g_cg.image ("HirokoParkHypno hiroko_arms_out frown_open kyou_pointing")
    g_cg.image ("HirokoParkHypno hiroko_arms_out frown_open_talk kyou_pointing")
    g_cg.image ("HirokoParkHypno hiroko_arms_out frown_closed kyou_pointing")
    g_cg.image ("HirokoParkHypno hiroko_arms_out frown_closed")
    g_cg.image ("HirokoParkHypno hiroko_arms_out frown_closed_talk")
    g_cg.image ("HirokoParkHypno hiroko_arms_out frown_closed")
    g_cg.image ("HirokoParkHypno hiroko_arms_close frown_closed")
    g_cg.image ("HirokoParkHypno hiroko_arms_closer frown_closed")
    g_cg.image ("HirokoParkHypno hiroko_arms_closer frown_closed kyou_clapping")
    g_cg.image ("HirokoParkHypno hiroko_slumped noface")
    g_cg.image ("HirokoParkHypno hiroko_sleep sleep")
    g_cg.image ("HirokoParkHypno hiroko_sleep sleeptalk")
    g_cg.image ("HirokoParkHypno")
    g_cg.image ("HirokoParkHypno laugh")
    g_cg.image ("HirokoParkHypno hiroko_sitting_blush")

    g_cg.button("hiroko park ending 1 single image")
    g_cg.condition("persistent.hiroko_park_ending_1_unlock")
    g_cg.image("cg hiroko park ending 1")

    g_cg.button("hiroko cafe")
    g_cg.condition("persistent.hiroko_cafe_unlock")
    g_cg.image("HirokoCafe worried")
    g_cg.image("HirokoCafe sigh")
    g_cg.image("HirokoCafe frown")
    g_cg.image("HirokoCafe scared_closed")
    g_cg.image("HirokoCafe scared")
    g_cg.image("HirokoCafe worried_left")
    g_cg.image("HirokoCafe frown")
    g_cg.image("HirokoCafe neutral_left")
    g_cg.image("HirokoCafe neutral")
    g_cg.image("HirokoCafe smile")
    g_cg.image("HirokoCafe smile_tears")

    g_cg.button("forced girlfriend ending")
    g_cg.condition("persistent.forced_girlfriend_ending_unlock")
    g_cg.image ("NozomiForcedGF smile_up")
    g_cg.image ("NozomiForcedGF smile_down")

    g_cg.button("nozomi good end 1")
    g_cg.condition("persistent.nozomi_good_end_1_unlock")
    g_cg.image ("cg nozomi good end 1", "Nozomi GoodEnd1 smile")
    g_cg.image ("cg nozomi good end 1", "Nozomi GoodEnd1 kiss")

    g_cg.button("tennis bot end 3")
    g_cg.condition("persistent.tennis_bot_end_1_unlock")
    g_cg.image("cg tennis bot end 3")


    g_cg.transition = dissolve

    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3

    gal_page = 1
    #thumbnail size in pixels:
    thumbnail_x = 267
    thumbnail_y = 150

#CG Gallery button image declarations
init +1 python:
    renpy.image ("titlescreen butt", im.Scale(ImageReference("titlescreen"), thumbnail_x, thumbnail_y))
    renpy.image ("kyou intro single image butt", im.Scale(ImageReference("cg kyou intro"), thumbnail_x, thumbnail_y))
    renpy.image ("stageshow butt", im.Scale(ImageReference("cg stageshow bw"), thumbnail_x, thumbnail_y))
    renpy.image ("classroom nozomi butt", im.Scale(ImageReference("cgt classroom nozomi"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko_tennis1 single image butt", im.Scale(ImageReference("cg hiroko_tennis1"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori intro butt", im.Scale(ImageReference("cgt sayori intro"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori study butt", im.Scale(ImageReference("cgt sayori study"), thumbnail_x, thumbnail_y))
    renpy.image ("sports shed night butt", im.Scale(ImageReference("cgt sports shed night"), thumbnail_x, thumbnail_y))
    renpy.image ("classroomlunch2 1 butt", im.Scale(ImageReference("cgt classroom lunch day2"), thumbnail_x, thumbnail_y))
    renpy.image ("rooftop day butt", im.Scale(ImageReference("cgt rooftop day"), thumbnail_x, thumbnail_y))
    renpy.image ("delusion rooftop butt", im.Scale(ImageReference("cgt delusion rooftop"), thumbnail_x, thumbnail_y))
    renpy.image ("k bedroom hiroko 1 butt", im.Scale(ImageReference("cgt k bedroom hiroko"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko vs risa butt", im.Scale(ImageReference("cgt hiroko vs risa"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko intro butt", im.Scale(ImageReference("cgt akiko intro"), thumbnail_x, thumbnail_y))
    renpy.image ("alley hiroko butt", im.Scale(ImageReference("cgt alley hiroko"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko science butt", im.Scale(ImageReference("cgt akiko science"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi cafe butt", im.Scale(ImageReference("cgt nozomi cafe uniform"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko trapped butt", im.Scale(ImageReference("cgt hiroko trapped"), thumbnail_x, thumbnail_y))
    renpy.image ("classroomlunch3 butt", im.Scale(ImageReference("cgt classroom lunch day3"), thumbnail_x, thumbnail_y))
    renpy.image ("sleeper agent night butt", im.Scale(ImageReference("cgt sleeper agent night"), thumbnail_x, thumbnail_y))
    renpy.image ("classroom lunch2 delusion butt", im.Scale(ImageReference("cgt classroom lunch 2 delusion"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko student council hypno butt", im.Scale(ImageReference("cgt akiko student council"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko student council hypno2 butt", im.Scale(ImageReference("cgt akiko student council2"), thumbnail_x, thumbnail_y))
    renpy.image ("devotion start butt", im.Scale(ImageReference("cgt devotion start"), thumbnail_x, thumbnail_y))
    renpy.image ("robot start butt", im.Scale(ImageReference("cgt robot start"), thumbnail_x, thumbnail_y))
    renpy.image ("sleeper agent start butt", im.Scale(ImageReference("cgt sleeper agent start"), thumbnail_x, thumbnail_y))
    renpy.image ("hiro walk devotion butt", im.Scale(ImageReference("cgt hiroko walk"), thumbnail_x, thumbnail_y))
    renpy.image ("redemption start butt", im.Scale(ImageReference("cgt redemption start"), thumbnail_x, thumbnail_y))
    renpy.image ("devotion bedroom day2 butt", im.Scale(ImageReference("cgt devotion bedroom day2"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko robot programming butt", im.Scale(ImageReference("cgt hiroko robot programming"), thumbnail_x, thumbnail_y))
    renpy.image ("creepy hiroko butt", im.Scale(ImageReference("cgt creepy hiroko"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko tickle butt", im.Scale(ImageReference("cgt hiroko tickle"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko couch argument butt", im.Scale(ImageReference("cgt hiroko couch argument"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori arm butt", im.Scale(ImageReference("cgt sayori arm"), thumbnail_x, thumbnail_y))
    renpy.image ("k room nozomi 1 1 butt", im.Scale(ImageReference("cgt k room nozomi"), thumbnail_x, thumbnail_y))
    renpy.image ("zombie beginning butt", im.Scale(ImageReference("cgt zombie beginning"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi injured butt", im.Scale(ImageReference("cgt nozomi injured"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi hiroko hug butt", im.Scale(ImageReference("cgt nozomi hiroko hug"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori lunch butt", im.Scale(ImageReference("cgt sayori lunch"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori walk butt", im.Scale(ImageReference("cgt sayori walk"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi argument butt", im.Scale(ImageReference("cgt nozomi argument"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori fallen butt", im.Scale(ImageReference("cgt sayori fallen"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori sleep butt", im.Scale(ImageReference("cgt sayori sleep"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori sitting butt", im.Scale(ImageReference("cgt sayori sitting"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori sleeper capture butt", im.Scale(ImageReference("cgt sayori sleeper capture"), thumbnail_x, thumbnail_y))
    renpy.image ("room hiroko 1 butt", im.Scale(ImageReference("cgt k room hiroko"), thumbnail_x, thumbnail_y))
    renpy.image ("k room nozomi 2 1 butt", im.Scale(ImageReference("cgt k room nozomi2"), thumbnail_x, thumbnail_y))
    renpy.image ("classroomlunch4 1 butt", im.Scale(ImageReference("cgt classroom lunch day4"), thumbnail_x, thumbnail_y))
    renpy.image ("k room nozomi reversal1 butt", im.Scale(ImageReference("cgt k room nozomireversal casual"), thumbnail_x, thumbnail_y))
    renpy.image ("k room nozomi tv1 butt", im.Scale(ImageReference("cgt k room nozomi tv"), thumbnail_x, thumbnail_y))
    renpy.image ("k room hiroko tv1 butt", im.Scale(ImageReference("cgt k room hiroko tv"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko reversal butt", im.Scale(ImageReference("cgt k room hirokoreversal"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko cat 1 butt", im.Scale(ImageReference("cgt hiroko cat 1"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko cat 2 butt", im.Scale(ImageReference("cgt hiroko cat 2"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko racket butt", im.Scale(ImageReference("cgt hiroko racket"), thumbnail_x, thumbnail_y))
    renpy.image ("study room sayori butt", im.Scale(ImageReference("cgt study room sayori"), thumbnail_x, thumbnail_y))
    renpy.image ("k room sayori butt", im.Scale(ImageReference("cgt k room sayori"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori alter start butt", im.Scale(ImageReference("cgt k bedroom sayori"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori greeting butt", im.Scale(ImageReference("cgt sayori greeting"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko shoe butt", im.Scale(ImageReference("cgt hiroko shoe"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko yawn day butt", im.Scale(ImageReference("cgt hiroko yawn day"), thumbnail_x, thumbnail_y))
    renpy.image ("classroom lunch2 sleeper butt", im.Scale(ImageReference("cgt classroom lunch 2 sleeper"), thumbnail_x, thumbnail_y))
    renpy.image ("rooftop devotion butt", im.Scale(ImageReference("cgt rooftop devotion"), thumbnail_x, thumbnail_y))
    renpy.image ("rooftop robot butt", im.Scale(ImageReference("cgt rooftop robot"), thumbnail_x, thumbnail_y))
    renpy.image ("rooftop robot  girlfriend butt", im.Scale(ImageReference("cgt rooftop robot girlfriend"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko yawn eve butt", im.Scale(ImageReference("cgt hiroko yawn eve"), thumbnail_x, thumbnail_y))
    renpy.image ("classroomlunch5 1 butt", im.Scale(ImageReference("cgt classroom lunch day5"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko tennis kiss single image butt", im.Scale(ImageReference("cg hiroko tennis kiss"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi collapse single image butt", im.Scale(ImageReference("cg nozomi collapse"), thumbnail_x, thumbnail_y))
    renpy.image ("study room nozomi butt", im.Scale(ImageReference("cgt study room nozomi"), thumbnail_x, thumbnail_y))
    renpy.image ("study room hypno nozomi butt", im.Scale(ImageReference("cgt study room hypno nozomi"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi chocolate butt", im.Scale(ImageReference("cgt nozomi chocolate"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomisleepercapture butt", im.Scale(ImageReference("cgt nozomi sleeper capture"), thumbnail_x, thumbnail_y))
    renpy.image ("delusion struggle sayori butt", im.Scale(ImageReference("cgt delusion struggle sayori"), thumbnail_x, thumbnail_y))
    renpy.image ("devotion tennis butt", im.Scale(ImageReference("cgt devotion bedroom day4_1"), thumbnail_x, thumbnail_y)) #Fromerly devotion tennis day 4_1
    renpy.image ("devotion tennis partial butt", im.Scale(ImageReference("cgt devotion bedroom day4_2"), thumbnail_x, thumbnail_y)) #Formerly devotion bedroom day4_2
    renpy.image ("devotion underwear butt", im.Scale(ImageReference("cgt devotion bedroom day4_3"), thumbnail_x, thumbnail_y)) #Formerly devotion bedroom day4_3
    renpy.image ("devotion naked butt", im.Scale(ImageReference("cgt devotion bedroom day4_4"), thumbnail_x, thumbnail_y)) #Formerly devotion bedroomtennis day4_4
    renpy.image ("study room hypno sayori butt", im.Scale(ImageReference("cgt study room hypno sayori"), thumbnail_x, thumbnail_y))
    renpy.image ("k phone robot butt", im.Scale(ImageReference("cgt k phone robot"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi robot kiss single image butt", im.Scale(ImageReference("cg nozomi robot kiss"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi mindtrick butt", im.Scale(ImageReference("cgt nozomi mindtrick"), thumbnail_x, thumbnail_y))
    renpy.image ("zombie bedroom 1 1 butt", im.Scale(ImageReference("cgt zombie bedroom 1"), thumbnail_x, thumbnail_y))
    renpy.image ("zombie bedroom 2 butt", im.Scale(ImageReference("cgt zombie bedroom 2"), thumbnail_x, thumbnail_y))
    renpy.image ("zombie bedroom 3 butt", im.Scale(ImageReference("cgt zombie bedroom 3"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi boardgame butt", im.Scale(ImageReference("cgt n boardgame"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi boardgame2 butt", im.Scale(ImageReference("cgt n boardgame 2"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi hypnobondage butt", im.Scale(ImageReference("cgt n bedroom hypnobondage"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi hypnobondage tickling butt", im.Scale(ImageReference("cgt n bedroom hypnobondage tickling"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi hypnobondage spanking butt", im.Scale(ImageReference("cgt n bedroom hypnobondage spanking"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori alter lunch butt", im.Scale(ImageReference("cgt sayori alter lunch"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori arcade2 butt", im.Scale(ImageReference("cgt sayori arcade 2"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori penlight butt", im.Scale(ImageReference("cgt sayori penlight"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori bed1 butt", im.Scale(ImageReference("cgt sayori bed 1"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori hug butt", im.Scale(ImageReference("cgt sayori hug"), thumbnail_x, thumbnail_y))
    renpy.image ("k room akiko 1 butt", im.Scale(ImageReference("cgt k room akiko"), thumbnail_x, thumbnail_y))
    renpy.image ("sleeper agent struggle1 butt", im.Scale(ImageReference("cgt sleeper agent struggle"), thumbnail_x, thumbnail_y))
    renpy.image ("sleeper agent defeat butt", im.Scale(ImageReference("cgt sleeper agent defeat"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi burglar butt", im.Scale(ImageReference("cgt n burglar"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi burglar undressing butt", im.Scale(ImageReference("cgt n burglar undressing"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko court night good butt", im.Scale(ImageReference("cgt hiroko court night good"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko court night bad butt", im.Scale(ImageReference("cgt hiroko court night bad"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko park sad butt", im.Scale(ImageReference("cgt hiroko park sad"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko won butt", im.Scale(ImageReference("cgt hiroko won"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi interrogation butt", im.Scale(ImageReference("cgt nozomi interrogation"), thumbnail_x, thumbnail_y))
    renpy.image ("trance stop end butt", im.Scale(ImageReference("cgt trance stop ending"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi robot programming butt", im.Scale(ImageReference("cgt nozomi robot programming"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori x kyou butt", im.Scale(ImageReference("cgt sayori x kyou"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori grab butt", im.Scale(ImageReference("cgt sayori grab"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko breakfast butt", im.Scale(ImageReference("cgt akiko breakfast"), thumbnail_x, thumbnail_y))
    renpy.image ("redemption phone day butt", im.Scale(ImageReference("cgt redemption phone day"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko slapped butt", im.Scale(ImageReference("cgt akiko slapped"), thumbnail_x, thumbnail_y))
    renpy.image ("redemption phone eve butt", im.Scale(ImageReference("cgt redemption phone eve"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko kendo butt", im.Scale(ImageReference("cgt akiko kendo"), thumbnail_x, thumbnail_y))    
    renpy.image ("sword strike single image butt", im.Scale(ImageReference("cg sword strike"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko cornered butt", im.Scale(ImageReference("cgt akiko cornered"), thumbnail_x, thumbnail_y))
    renpy.image ("voodoo phone butt", im.Scale(ImageReference("cgt voodoo phone"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko scared single image butt", im.Scale(ImageReference("cg hiroko scared"), thumbnail_x, thumbnail_y))
    renpy.image ("bathroom ambush butt", im.Scale(ImageReference("cgt bathroom ambush"), thumbnail_x, thumbnail_y))
    renpy.image ("voodoo phone2 butt", im.Scale(ImageReference("cgt voodoo phone 2"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko kiss butt", im.Scale(ImageReference("cgt akiko kiss"), thumbnail_x, thumbnail_y))
    renpy.image ("spiral ending butt", im.Scale(ImageReference("cgt spiral ending"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori hypno day butt", im.Scale(ImageReference("cgt kyou room sayori day"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi cola butt", im.Scale(ImageReference("cgt nozomi cola"), thumbnail_x, thumbnail_y))
    renpy.image ("k bedroom confrontation sayori butt", im.Scale(ImageReference("cgt k bedroom confrontation sayori"), thumbnail_x, thumbnail_y))
    renpy.image ("k bedroom confrontation hiroko butt", im.Scale(ImageReference("cgt k bedroom confrontation hiroko"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko makeover 1 butt", im.Scale(ImageReference("cgt akiko makeover 1"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko makeover 2 butt", im.Scale(ImageReference("cgt akiko makeover 2"), thumbnail_x, thumbnail_y))
    renpy.image ("copycat karaoke hypno1 butt", im.Scale(ImageReference("cgt copycat karaoke hypno 1"), thumbnail_x, thumbnail_y))
    renpy.image ("copycat karaoke hypno2 butt", im.Scale(ImageReference("cgt copycat karaoke hypno 2"), thumbnail_x, thumbnail_y))
    renpy.image ("copycat karaoke1 butt", im.Scale(ImageReference("cgt copycat karaoke 1"), thumbnail_x, thumbnail_y))
    renpy.image ("copycat karaoke2 butt", im.Scale(ImageReference("cgt copycat karaoke 2"), thumbnail_x, thumbnail_y))
    renpy.image ("copycat karaoke3 butt", im.Scale(ImageReference("cgt copycat karaoke 3"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi cafe villain butt", im.Scale(ImageReference("cgt nozomi cafe casual"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi window butt", im.Scale(ImageReference("cgt nozomi window"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi captured butt", im.Scale(ImageReference("cgt nozomi captured"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi kneeling trance1 butt", im.Scale(ImageReference("cgt nozomi kneeling trance"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi zombie walk butt", im.Scale(ImageReference("cgt nozomi zombie walk"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi lying butt", im.Scale(ImageReference("cgt nozomi lying"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi kitchen single image butt", im.Scale(ImageReference("cgt nozomi kitchen"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi omelette butt", im.Scale(ImageReference("cgt nozomi omelette"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi kiss butt", im.Scale(ImageReference("cgt nozomi kiss"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi kneeling devotion butt", im.Scale(ImageReference("cgt nozomi kneeling devotion"), thumbnail_x, thumbnail_y))
    renpy.image ("classroom hiroko 2 1 butt", im.Scale(ImageReference("cgt classroom 2 hiroko"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko rehearsal butt", im.Scale(ImageReference("cgt hiroko classroom rehearsal"), thumbnail_x, thumbnail_y))
    renpy.image ("yikes end butt", im.Scale(ImageReference("cgt hiroko yikes end"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko betrayal butt", im.Scale(ImageReference("cgt hiroko betrayal"), thumbnail_x, thumbnail_y))
    renpy.image ("alter good end 2 butt", im.Scale(ImageReference("cgt sayori alter good end 2"), thumbnail_x, thumbnail_y))
    renpy.image ("devotion end 1 single image butt", im.Scale(ImageReference("cg devotion end 1"), thumbnail_x, thumbnail_y))
    renpy.image ("devotion end 2 butt", im.Scale(ImageReference("cgt devotion end 2"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi karaoke group butt", im.Scale(ImageReference("cgt nozomi karaoke group"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi threatening butt", im.Scale(ImageReference("cgt nozomi threatening"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi sorry butt", im.Scale(ImageReference("cgt nozomi sorry"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi couch hypno butt", im.Scale(ImageReference("cgt nozomi couch hypno"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi tortured tickle butt", im.Scale(ImageReference("cgt nozomi tortured tickle"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi tortured spank butt", im.Scale(ImageReference("cgt nozomi tortured spank"), thumbnail_x, thumbnail_y))
    renpy.image ("reversal bad end butt", im.Scale(ImageReference("cgt reversal bad ending"), thumbnail_x, thumbnail_y))
    renpy.image ("reversal good end butt", im.Scale(ImageReference("cgt reversal good ending"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori arcade butt", im.Scale(ImageReference("cgt sayori arcade"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko gaming butt", im.Scale(ImageReference("cgt hiroko gaming"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko slumped butt", im.Scale(ImageReference("cgt hiroko slumped"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori room tickle butt", im.Scale(ImageReference("cgt sayori room tickle"), thumbnail_x, thumbnail_y))
    renpy.image ("rooftop reversal butt", im.Scale(ImageReference("cgt rooftop reversal"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko cam 1 1 butt", im.Scale(ImageReference("cgt hiroko cam 1"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko cam 2 butt", im.Scale(ImageReference("cgt hiroko cam 2"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko cam 3 butt", im.Scale(ImageReference("cgt hiroko cam 3"), thumbnail_x, thumbnail_y))
    renpy.image ("nozo cam hypno butt", im.Scale(ImageReference("cgt nozomi cam hypno"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko cam 4 butt", im.Scale(ImageReference("cgt hiroko cam 4"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko cam 5 butt", im.Scale(ImageReference("cgt hiroko cam 5"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko cam kiss butt", im.Scale(ImageReference("cgt hiroko cam kiss"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko nozomi phone butt", im.Scale(ImageReference("cgt hiroko nozomi phone"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko bed butt", im.Scale(ImageReference("cgt hiroko bed"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko couch butt", im.Scale(ImageReference("cgt hiroko couch"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko couch2 butt", im.Scale(ImageReference("cgt hiroko couch 2"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko karaoke bed 2 butt", im.Scale(ImageReference("cg hiroko karaoke bed 2"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori dinner butt", im.Scale(ImageReference("cgt sayori dinner"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori alter hug single image butt", im.Scale(ImageReference("cg sayori alter hug"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori alter confrontation butt", im.Scale(ImageReference("cgt sayori alter confrontation 1"), thumbnail_x, thumbnail_y))
    renpy.image ("akiko intro2 butt", im.Scale(ImageReference("cgt akiko intro 2"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori alter bad end 3 butt", im.Scale(ImageReference("cgt sayori alter bad end 3"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko rooftop 1 1 butt", im.Scale(ImageReference("cgt hiroko rooftop 1-1"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko rooftop 1 2 butt", im.Scale(ImageReference("cgt hiroko rooftop 1-2"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko rooftop 2 butt", im.Scale(ImageReference("cgt hiroko rooftop 2"), thumbnail_x, thumbnail_y))
    renpy.image ("penlight broken butt", im.Scale(ImageReference("cgt penlight broken"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi rooftop tickled butt", im.Scale(ImageReference("cgt nozomi rooftop_tickle"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi rooftop spanked butt", im.Scale(ImageReference("cgt nozomi rooftop_spanked"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi rooftop tickle2 butt", im.Scale(ImageReference("cgt nozomi rooftop tickle2"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi rooftop spank2 butt", im.Scale(ImageReference("cgt nozomi rooftop spank2"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi provoke butt", im.Scale(ImageReference("cgt nozomi provoke"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi couch strip butt", im.Scale(ImageReference("cgt nozomi couch strip"), thumbnail_x, thumbnail_y))
    renpy.image ("hypno rehearsal butt", im.Scale(ImageReference("cgt hypno rehearsal 1"), thumbnail_x, thumbnail_y))
    renpy.image ("hypno rehearsal 2 butt", im.Scale(ImageReference("cgt hypno rehearsal 2"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori room hypno butt", im.Scale(ImageReference("cgt sayori room hypno"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori room hypno2 butt", im.Scale(ImageReference("cgt sayori room hypno 2"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori doll pose1 butt", im.Scale(ImageReference("cgt sayori doll pose 1"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori doll pose2 butt", im.Scale(ImageReference("cgt sayori doll pose 2"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori doll scene climax butt", im.Scale(ImageReference("cg sayori doll climax"), thumbnail_x, thumbnail_y))
    renpy.image ("delusion end 1 single image butt", im.Scale(ImageReference("cg delusion end 1"), thumbnail_x, thumbnail_y))
    renpy.image ("robot karaoke end butt", im.Scale(ImageReference("cgt robot karaoke end"), thumbnail_x, thumbnail_y))
    renpy.image ("k bedroom robot nozomi butt", im.Scale(ImageReference("cgt k bedroom robot nozomi"), thumbnail_x, thumbnail_y))
    renpy.image ("k bedroom robot sayori butt", im.Scale(ImageReference("cgt k bedroom robot sayori"), thumbnail_x, thumbnail_y))
    renpy.image ("k bedroom robot hiroko butt", im.Scale(ImageReference("cgt k bedroom robot hiroko"), thumbnail_x, thumbnail_y))
    renpy.image ("school cafe 1 single image butt", im.Scale(ImageReference("cg school cafe"), thumbnail_x, thumbnail_y))
    renpy.image ("trance abuse end butt", im.Scale(ImageReference("cgt trance abuse ending"), thumbnail_x, thumbnail_y))
    renpy.image ("zombie ending 1 butt", im.Scale(ImageReference("cgt zombie ending 1"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko stageshow good butt", im.Scale(ImageReference("cgt hiroko stageshow good"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko stageshow cat butt", im.Scale(ImageReference("cgt hiroko stageshow cat"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori stageshow catalepsy butt", im.Scale(ImageReference("cgt sayori stageshow catalepsy"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori chicken1 butt", im.Scale(ImageReference("cgt sayori chicken 1"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori chicken2 butt", im.Scale(ImageReference("cgt sayori chicken 2"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori doll bad end single image butt", im.Scale(ImageReference("cgt sayori doll bad end"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori doll good end butt", im.Scale(ImageReference("cgt sayori doll good end"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko good end 1 butt", im.Scale(ImageReference("cgt hiroko good end 1"), thumbnail_x, thumbnail_y))
    renpy.image ("copycat ending 1 single image butt", im.Scale(ImageReference("cg copycat ending 1"), thumbnail_x, thumbnail_y))
    renpy.image ("copycat ending 2_1 butt", im.Scale(ImageReference("cgt copycat ending 2_1"), thumbnail_x, thumbnail_y))
    renpy.image ("copycat ending 2_2 butt", im.Scale(ImageReference("cgt copycat ending 2_2"), thumbnail_x, thumbnail_y))
    renpy.image ("redemption ending 1_1 butt", im.Scale(ImageReference("cgt redemption ending 1_1"), thumbnail_x, thumbnail_y))
    renpy.image ("redemption ending 1_2 butt", im.Scale(ImageReference("cgt redemption ending 1_2"), thumbnail_x, thumbnail_y))
    renpy.image ("forced girlfriend ending butt", im.Scale(ImageReference("cgt forced girlfriend ending"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko park hypno butt", im.Scale(ImageReference("cgt hiroko park hypno"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko park ending 1 single image butt", im.Scale(ImageReference("cg hiroko park ending 1"), thumbnail_x, thumbnail_y))
    renpy.image ("hiroko cafe butt", im.Scale(ImageReference("cgt hiroko cafe"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori alter confrontation2 butt", im.Scale(ImageReference("cgt sayori alter confrontation 2"), thumbnail_x, thumbnail_y))
    renpy.image ("alter good end 1 butt", im.Scale(ImageReference("cgt sayori alter good end 1"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori alter coop end butt", im.Scale(ImageReference("cg sayori alter coop end"), thumbnail_x, thumbnail_y))
    renpy.image ("alter bad end 1 butt", im.Scale(ImageReference("cgt sayori alter bad end 1"), thumbnail_x, thumbnail_y))
    renpy.image ("sayori alter bad end 2 butt", im.Scale(ImageReference("cg sayori alter bad end 2"), thumbnail_x, thumbnail_y))
    renpy.image ("tennis bot end 3 butt", im.Scale(ImageReference("cg tennis bot end 3"), thumbnail_x, thumbnail_y))
    renpy.image ("nozomi good end 1 butt", im.Scale(ImageReference("cgt nozomi good end 1"), thumbnail_x, thumbnail_y))


#This function checks an unlock variable and returns a given image name if it's true, and "cg locked.png" if it's false
init python:
    def unlockable_image(unlock_variable, image_name): 
        return ConditionSwitch( unlock_variable, image_name, "True", "cg locked.png" )

#This other function takes a list of several images and runs them through the unlockable_image function above under the same unlock variable
#This is used in CG Groups when there are sevaral images in a row that require a (shared) additional unlock flag to be seen in adition to the one that unlocks the button in the CG Galley
init python:
    def unlockable_image_list(unlock_variable, image_names):
        return [unlockable_image(unlock_variable, i) for i in image_names] #Where i is is a counter for every image within the image list

#This functiuon allows to overlap images, used in the CG Groups for old CGs that use the old styled multi-image declaration format
init python:
    def overlap_images(*images):
        return Fixed(*[ImageReference(i) for i in images])


##CG Grups, the groups of images that contain each CG set, each being an entry for the CG gallery
init python:
    cg_groups = {
        #Page 1
        "kyou intro single image":[], #Some "groups" like this one are going to be empty because they're a single image, so they don't require a UI (or the UI can't be implemented at the moment for whatever reason). The group name is purpusfully inconsistant with the unlock variable so that the code of the cg_button function doesn't find a true unlock variable and, as a result, calls the old method with cg.make_button
        "stageshow": [
            "cg stageshow bw",
            "cg stageshow"
        ],
        "classroom nozomi":[ #The overlap_images function is used here because this CG is in the old fashioned multiple-image declaration styele.
            overlap_images("cg classroom eve", "NozomiHypno folded stern"), #Here, for example, it will combine the "cg classroom eve" background and the "NozomiHypno folded stern" sprite into a single element of this group, showing them together in the cg_viewer
            overlap_images("cg classroom eve", "NozomiHypno folded angry"),
            overlap_images("cg classroom eve", "NozomiHypno standing confused"),
            overlap_images("cg classroom eve", "NozomiHypno standing drowsy"),
            overlap_images("cg classroom eve", "NozomiHypno drooping sleepy"),
            overlap_images("cg classroom eve", "NozomiHypno drooping sleepy arm_uniform "),
            overlap_images("cg classroom eve", "NozomiHypno drooping sleep arm_uniform"),
            overlap_images("cg classroom eve", "NozomiHypno drooping sleeptalk arm_uniform"),  
        ],   
        "hiroko_tennis1 single image": [
            #This one is a single image
        ],
        "alley hiroko": [
            overlap_images("cg alley eve", "HirokoHypno upright angry clenched_fists"),
            overlap_images("cg alley eve", "HirokoHypno upright frown clenched_fists"),
            overlap_images("cg alley eve", "HirokoHypno upright angry_up clenched_fists"),
            overlap_images("cg alley eve", "HirokoHypno upright drowsy clenched_fists"),
            overlap_images("cg alley eve", "HirokoHypno upright straining relaxed_fists"),
            overlap_images("cg alley eve", "HirokoHypno upright straining nofists"),
            overlap_images("cg alley eve", "HirokoHypno relaxed drowsy no_arm"),
            overlap_images("cg alley eve", "HirokoHypno relaxed sleepy_up_open arm_uniform"),
            overlap_images("cg alley eve", "HirokoHypno relaxed sleep arm_uniform"),
            overlap_images("cg alley eve", "HirokoHypno drooping sleep arm_uniform"),
            overlap_images("cg alley eve", "HirokoHypno drooping sleeptalk arm_uniform"),
            overlap_images("cg alley eve", "HirokoHypno relaxed entranced_neutral arm_uniform"),
            overlap_images("cg alley eve", "HirokoHypno relaxed entranced_neutral no_arm"),
            overlap_images("cg alley eve", "HirokoHypno relaxed entranced_talk no_arm"),
            overlap_images("cg alley eve", "HirokoHypno relaxed entranced_concerned no_arm"),
            overlap_images("cg alley eve", "HirokoHypno relaxed entranced_concerned_talk no_arm"),            
        ],
        "akiko science": [
            "AkikoScience akiko1 neutral kyou1",
            "AkikoScience akiko1 confused kyou1",
            "AkikoScience akiko1 concerned kyou1",
            "AkikoScience akiko1 peaceful kyou1",
            "AkikoScience akiko1 frown kyou1",
            "AkikoScience akiko1 sigh kyou1",
            "AkikoScience akiko1 concerned_left kyou1",
            "AkikoScience akiko1 surprised kyou1",
            "AkikoScience akiko1 neutral kyou2",
            "AkikoScience akiko1 neutral2 kyou2 light",
            "AkikoScience akiko1 confused kyou2 light",
            "AkikoScience akiko1 confused2 kyou2 light",
            "AkikoScience akiko1 concerned kyou2 light",
            "AkikoScience akiko1 concerned2 kyou2 light",
            "AkikoScience akiko1 sleepy kyou2 light",
            "AkikoScience akiko1 sleepy2 kyou2 light",
            "AkikoScience akiko1 peaceful kyou2 light",
            "AkikoScience akiko2 sleep kyou2 light",
            "AkikoScience akiko2 sleep kyou2",
            "AkikoScience akiko2 sleep kyou1",
            "AkikoScience akiko2 sleeptalk kyou1",
            "AkikoScience akiko2 waking kyou1",
            "AkikoScience akiko1 surprised kyou1",
            "AkikoScience akiko1 smile kyou1",
            "AkikoScience akiko1 laugh blush kyou1",
            "AkikoScience akiko1 smile blush kyou1",
        ],
        "sayori intro":[
            overlap_images("cg study room2 eve", "SayoriIntro suspicious_open"),
            overlap_images("cg study room2 eve", "SayoriIntro suspicious_closed"),
            overlap_images("cg study room2 eve", "SayoriIntro sigh"),
        ],
        "sayori study": [
            "SayoriStudy sayori1 talking",
            "SayoriStudy sayori2 sleep",
            "SayoriStudy sayori2 waking",
            "SayoriStudy sayori1 smile_side",
            "SayoriStudy sayori1 smile",
        ],
        "sports shed night": [
            overlap_images("cg sports shed night", "HirokoHypno upright tennis annoyed nofists"),
            overlap_images("cg sports shed night", "HirokoHypno upright tennis frown"),
            overlap_images("cg sports shed night", "HirokoHypno upright tennis angry clenched_fists_tennis"),
            overlap_images("cg sports shed night", "HirokoHypno upright tennis angry_up clenched_fists_tennis"),
            overlap_images("cg sports shed night", "HirokoHypno upright tennis annoyed_up nofists"),
            overlap_images("cg sports shed night", "HirokoHypno upright tennis angry clenched_fists_tennis"),
            overlap_images("cg sports shed night", "HirokoHypno upright tennis annoyed_up clenched_fists_tennis"),
            overlap_images("cg sports shed night", "HirokoHypno upright tennis surprised relaxed_fists_tennis"),
            overlap_images("cg sports shed night", "HirokoHypno upright tennis drowsy nofists"),
            overlap_images("cg sports shed night", "HirokoHypno relaxed tennis drowsy"),
            overlap_images("cg sports shed night", "HirokoHypno relaxed tennis sleep"),
            overlap_images("cg sports shed night", "HirokoHypno drooping tennis sleep"),
            overlap_images("cg sports shed night", "HirokoHypno drooping tennis sleeptalk"),
            overlap_images("cg sports shed night", "HirokoHypno relaxed tennis neutral"),
        ],
        "classroomlunch2 1":[
            "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_laugh n_armup n_smile_left glasses sayori s_smile_nozomi",
            "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_neutral_sayori n_armup n_smile_right glasses sayori s_smirk_hiroko",
            "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_grin_sayori n_armup n_smile_left glasses sayori s_smirk_hiroko",
            "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_grin_sayori n_folded n_thinking glasses sayori s_smirk_hiroko",
            "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_grin_sayori n_folded n_smile_left glasses sayori s_smirk_hiroko",
            #Villainous variant
            ConditionSwitch( #Here there's a ConditionSwitch because, even after unlocking the first images of this CG and becoming able to open it from the CG Gallery, these later images within the group get unlocked in a later scene
                "persistent.classroomlunch2_2_unlock", "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_neutral_nozomi n_folded n_nervous glasses sayori s_neutral_nozomi",
                "True", "cg locked.png" #When the aditional flag classroomlunch2_2_unlock is found to be false, the cg_viewer will just show the "cg locked.png" image
            ),
            ConditionSwitch(
                "persistent.classroomlunch2_2_unlock", "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_neutral_nozomi n_folded n_nervous_left glasses sayori s_neutral_nozomi",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch2_2_unlock", "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_sad_nozomi n_folded n_nervous_left glasses sayori s_neutral_hiroko",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch2_2_unlock", "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_sad_nozomi n_folded n_sigh glasses sayori s_neutral_hiroko",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch2_2_unlock", "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_sad_nozomi n_folded n_sigh glasses sayori s_concerned_nozomi",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch2_2_unlock", "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_sad_nozomi n_folded n_nervous_left glasses sayori s_concerned_nozomi",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch2_2_unlock", "ClassroomLunch boy1 girl1 boy2_missing boy3 girl3_missing hiroko h_sad_nozomi n_folded n_nervous_right glasses sayori s_concerned_nozomi",
                "True", "cg locked.png"
            ),                          
        ],
        #Page 2
        "rooftop day": [
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown surprised", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown surprised blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek angry", "RoofNozomi handsdown surprised blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek angry", "RoofNozomi handsdown smile blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown smile blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown smile_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown smile_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown smile_left blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown smile_left blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown smile_left blush", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown smile noblush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown smile_left noblush", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown smile_left noblush", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown laugh noblush", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown neutral_left noblush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown neutral_left noblush", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown neutral_left noblush", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown smile_right noblush", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown smile noblush", "RoofSayori leanforward smirk"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown smile noblush", "RoofSayori leanforward smirk"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown laugh noblush", "RoofSayori leanforward laugh"),
        ],
        "delusion rooftop": [
            "DelusionRooftop head_up curious",
            "DelusionRooftop head_up curious penlight",
            "DelusionRooftop head_up curious_light penlight",
            "DelusionRooftop head_up confused penlight",
            "DelusionRooftop head_up confused_light penlight",
            "DelusionRooftop head_up surprised penlight",
            "DelusionRooftop head_up surprised_light penlight",
            "DelusionRooftop head_up sleepy penlight",
            "DelusionRooftop head_up sleepy_light penlight",
            "DelusionRooftop head_down sleep penlight",
            "DelusionRooftop head_down sleep",
            "DelusionRooftop head_down sleeptalk",
            "DelusionRooftop head_down waking",
            "DelusionRooftop head_up curious",
            "DelusionRooftop head_up smile",
            "DelusionRooftop head_up surprised",
        ],
        "devotion start":[
            "DevotionStart grimace kyou",
            "DevotionStart head_up angry kyou",
            "DevotionStart head_up surprised kyou",
            "DevotionStart head_down grimace blush_down kyou",
            "DevotionStart head_up smile blush_up kyou",
            "DevotionStart head_up surprised blush_up kyou",
            "DevotionStart head_up shocked kyou",
            "DevotionStart head_down cry blush_down kyou",
            "DevotionStart head_up hopeful blush_up kyou",
            "DevotionStart head_up joyous blush_up kyou",
            "DevotionStart head_up smile blush_up kyou",
            "DevotionStart head_up happy blush_up kyou",
            "DevotionStart head_up laugh blush_up kyou",
            ConditionSwitch(
                "persistent.devotion_start2_unlock", "DevotionStart head_up smile blush_up", #The last two frames are unlocked if Kyou commits to this route
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.devotion_start2_unlock", "DevotionStart head_up laugh blush_up", #The last two frames are unlocked if Kyou commits to this route
                "True", "cg locked.png"
            ),
        ],
        "robot start": [
            "RobotStart hiroko1 terrified",
            "RobotStart hiroko1 pleading",
            "RobotStart hiroko1 crying",
            "RobotStart hiroko2 head_down sobbing",
            "RobotStart hiroko2 head_up nervous",
            "RobotStart hiroko2 head_up shocked",

        ],
        "sleeper agent start":[
            "SleeperAgentStart hiroko_yell kyou_grimace",
            "SleeperAgentStart hiroko_yell kyou_pain",
            "SleeperAgentStart hiroko_growl kyou_yell",
        ],
        "hiro walk devotion":[
            "HirokoWalk blush smile neutral",
            "HirokoWalk blush smile stern",
            "HirokoWalk blush laugh stern",
            "HirokoWalk blush happy stern",
            "HirokoWalk blush happy neutral",
            ConditionSwitch(
                "persistent.hiro_walk_robot_unlock", "HirokoWalk sad neutral",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.hiro_walk_robot_unlock", "HirokoWalk anxious neutral",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.hiro_walk_robot_unlock", "HirokoWalk anxious smirk",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.hiro_walk_robot_unlock", "HirokoWalk sigh smirk",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.hiro_walk_robot_unlock", "HirokoWalk frown smirk",
                "True", "cg locked.png"
            ),
        ],
        "k bedroom hiroko 1": [
            overlap_images("cg k wall eve", "HirokoHypno upright neutral"),
            overlap_images("cg k wall eve", "HirokoHypno upright frown"),
            overlap_images("cg k wall eve", "HirokoHypno upright angry"),
            overlap_images("cg k wall eve", "HirokoHypno upright annoyed"),
            overlap_images("cg k wall eve", "HirokoHypno upright angry_up"),
            overlap_images("cg k wall eve", "HirokoHypno relaxed frown"),
            overlap_images("cg k wall eve", "HirokoHypno upright angry clenched_fists"),
            overlap_images("cg k wall eve", "HirokoHypno upright concerned relaxed_fists"),
            overlap_images("cg k wall eve", "HirokoHypno upright entranced_concerned_talk relaxed_fists"),
            overlap_images("cg k wall eve", "HirokoHypno relaxed entranced_neutral"),
        ] + unlockable_image_list("persistent.k_bedroom_hiroko_2_unlock", [ #Here the unlockable_image_list function is used because multiple images in a row depend on the same unlock variable.
            overlap_images("cg k wall eve", "HirokoHypno relaxed uniform sad_closed"), #You can also find this being solved with the use of a bunch of ConditionSwitch'es because I hadn't made this function by the time I declared those        
            overlap_images("cg k wall eve", "HirokoHypno relaxed uniform sad"),        
            overlap_images("cg k wall eve", "HirokoHypno relaxed uniform blush sad_closed"),       
            overlap_images("cg k wall eve", "HirokoHypno relaxed uniform blush sad"),        
            overlap_images("cg k wall eve", "HirokoHypno relaxed uniform blush sleeptalk"),        
            overlap_images("cg k wall eve", "HirokoHypno relaxed uniform blush smile"),           
            overlap_images("cg k wall eve", "HirokoHypno relaxed uniform noblush drowsy"),           
            overlap_images("cg k wall eve", "HirokoHypno relaxed uniform noblush sleep"),            
            overlap_images("cg k wall eve", "HirokoHypno drooping uniform noblush sleep"),            
            overlap_images("cg k wall eve", "HirokoHypno drooping uniform noblush sleeptalk"),            
            overlap_images("cg k wall eve", "HirokoHypno upright uniform noblush scared"),
        ]),
        #Page 3
        "redemption start": [
            "RedemptionStart",
            "RedemptionStart arm_down cry",
            "RedemptionStart arm_down fear",
            "RedemptionStart arm_down sad",
            "RedemptionStart arm_down angry",
        ],
        "devotion bedroom day2": [
            "DevotionBedroom head_up_blush uniform_armsdown smile",
            "DevotionBedroom head_up_blush uniform_armsdown happy",
            "DevotionBedroom head_up uniform_armsdown confused",
            "DevotionBedroom head_up uniform_armsdown neutral_right",
            "DevotionBedroom head_up uniform_armsdown smile",
            "DevotionBedroom head_up uniform_armsdown frown",
            "DevotionBedroom head_up uniform_armsup sad",
            "DevotionBedroom head_up uniform_armsup frown_right",
            "DevotionBedroom head_up uniform_armsup laugh",
            "DevotionBedroom head_up_blush uniform_armsup laugh",
            "DevotionBedroom head_up_blush uniform_armsup smile",
            "DevotionBedroom head_up_blush uniform_armsdown sad",
        ],
        "hiroko robot programming": [
            "HirokoRobotProgramming",
            "HirokoRobotProgramming kyou",
            "HirokoRobotProgramming trancetalk kyou",
            "HirokoRobotProgramming trance kyou",
            "HirokoRobotProgramming head_side sleepy kyou",
            "HirokoRobotProgramming head_side awake kyou",
        ],
        "study room sayori": [
            overlap_images("cg study room eve", "SayoriHypno standing"),
            overlap_images("cg study room eve", "SayoriHypno standing smile"),
            overlap_images("cg study room eve", "SayoriHypno standing uniform_handsout smile"),
            overlap_images("cg study room eve", "SayoriHypno standing uniform_handsout stern"),
            overlap_images("cg study room eve", "SayoriHypno standing uniform_handsout neutral"),
            overlap_images("cg study room eve", "SayoriHypno standing uniform_handsout looking"),
            overlap_images("cg study room eve", "SayoriHypno standing uniform_handsout surprised"),
            overlap_images("cg study room eve", "SayoriHypno standing uniform_handsout drowsytalk"),
            overlap_images("cg study room eve", "SayoriHypno standing uniform_handsout drowsy"),
            overlap_images("cg study room eve", "SayoriHypno standing uniform drowsy"),
            overlap_images("cg study room eve", "SayoriHypno drooping uniform sleep"),
            overlap_images("cg study room eve", "SayoriHypno drooping sleeptalk"),
            overlap_images("cg study room eve", "SayoriHypno standing uniform_slumped noface"),
        ],
        "hiroko vs risa": [
            "Hiroko_vs_Risa hiroko",
            "Hiroko_vs_Risa hiroko frown",
        ],
        "nozomi cafe": [
            "NozomiCafe uniform_leaning pensive",
            "NozomiCafe uniform_leaning pensive_side",
            "NozomiCafe uniform_leaning pensive_closed",
            "NozomiCafe uniform_leaning anxious",
            "NozomiCafe uniform_leaning anxious_closed",
            "NozomiCafe uniform_leaning neutral",
            "NozomiCafe uniform_leaning stern",
            "NozomiCafe uniform_leaning stern_side",
            "NozomiCafe uniform_leaning smile",
            "NozomiCafe uniform_leaning smile_closed",
            "NozomiCafe uniform_leaning smirk",
            "NozomiCafe uniform_leaning surprised",
            "NozomiCafe uniform_leaning angry",
            "NozomiCafe uniform_folded pensive",
            "NozomiCafe uniform_folded pensive_side",
            "NozomiCafe uniform_folded pensive_closed",
            "NozomiCafe uniform_folded anxious",
            "NozomiCafe uniform_folded anxious_closed",
            "NozomiCafe uniform_folded neutral",
            "NozomiCafe uniform_folded stern",
            "NozomiCafe uniform_folded stern_side",
            "NozomiCafe uniform_folded smile",
            "NozomiCafe uniform_folded smile_closed",
            "NozomiCafe uniform_folded smirk",
            "NozomiCafe uniform_folded surprised",
            "NozomiCafe uniform_folded angry",
            "NozomiCafe uniform_leaning pensive blush",
            "NozomiCafe uniform_leaning pensive_side blush",
            "NozomiCafe uniform_leaning pensive_closed blush",
            "NozomiCafe uniform_leaning anxious blush",
            "NozomiCafe uniform_leaning anxious_closed blush",
            "NozomiCafe uniform_leaning neutral blush",
            "NozomiCafe uniform_leaning stern blush",
            "NozomiCafe uniform_leaning stern_side blush",
            "NozomiCafe uniform_leaning smile blush",
            "NozomiCafe uniform_leaning smile_closed blush",
            "NozomiCafe uniform_leaning smirk blush",
            "NozomiCafe uniform_leaning surprised blush",
            "NozomiCafe uniform_leaning angry blush",
            "NozomiCafe uniform_folded pensive blush",
            "NozomiCafe uniform_folded pensive_side blush",
            "NozomiCafe uniform_folded pensive_closed blush",
            "NozomiCafe uniform_folded anxious blush",
            "NozomiCafe uniform_folded anxious_closed blush",
            "NozomiCafe uniform_folded neutral blush",
            "NozomiCafe uniform_folded stern blush",
            "NozomiCafe uniform_folded stern_side blush",
            "NozomiCafe uniform_folded smile blush",
            "NozomiCafe uniform_folded smile_closed blush",
            "NozomiCafe uniform_folded smirk blush",
            "NozomiCafe uniform_folded surprised blush",
            "NozomiCafe uniform_folded angry blush",
        ],
        "k room nozomi 1 1":[
            overlap_images("cg k room eve", "NozomiHypno standing uniform neutral"),
            overlap_images("cg k room eve", "NozomiHypno standing uniform stern_closed"),
            overlap_images("cg k room eve", "NozomiHypno standing uniform smile"),
            overlap_images("cg k room eve", "NozomiHypno folded uniform annoyed"),
            overlap_images("cg k room eve", "NozomiHypno standing uniform angry"),
            overlap_images("cg k room eve", "NozomiHypno standing uniform lookup"),
            overlap_images("cg k room eve", "NozomiHypno standing uniform drowsy"),
            overlap_images("cg k room eve", "NozomiHypno drooping uniform sleepy"),
            overlap_images("cg k room eve", "NozomiHypno drooping uniform sleep"),
            overlap_images("cg k room eve", "NozomiHypno drooping uniform sleeptalk"),

        ] + unlockable_image_list("persistent.k_room_nozomi_1_2_unlock", [
            overlap_images("cg k room eve", "NozomiHypno standing uniform bruise sad noglasses"),           
            overlap_images("cg k room eve", "NozomiHypno standing uniform bruise neutral noglasses"),            
            overlap_images("cg k room eve", "NozomiHypno drooping uniform bruise sleeptalk noglasses"),            
            overlap_images("cg k room eve", "NozomiHypno standing uniform bruise confused noglasses"),           
            overlap_images("cg k room eve", "NozomiHypno standing uniform bruise stern noglasses"),          
            overlap_images("cg k room eve", "NozomiHypno standing uniform bruise annoyed noglasses"),           
            overlap_images("cg k room eve", "NozomiHypno folded uniform bruise stern_closed noglasses"),            
            overlap_images("cg k room eve", "NozomiHypno folded uniform bruise stern noglasses"),           
            overlap_images("cg k room eve", "NozomiHypno folded uniform bruise angry noglasses"),           
            overlap_images("cg k room eve", "NozomiHypno folded uniform bruise surprised noglasses"),            
            overlap_images("cg k room eve", "NozomiHypno folded uniform bruise annoyed noglasses"),            
            overlap_images("cg k room eve", "NozomiHypno folded uniform bruise neutral noglasses"),            
            overlap_images("cg k room eve", "NozomiHypno folded uniform bruise smile noglasses"),
        ]),
        "room hiroko 1": [
            overlap_images("cg k room eve", "HirokoHypno upright tennis annoyed nofists"),
            overlap_images("cg k room eve", "HirokoHypno upright tennis frown nofists"),
            overlap_images("cg k room eve", "HirokoHypno upright tennis annoyed_up nofists"),
            overlap_images("cg k room eve", "HirokoHypno upright tennis drowsy nofists"),
            overlap_images("cg k room eve", "HirokoHypno relaxed tennis sleepy_up_closed"),
            overlap_images("cg k room eve", "HirokoHypno relaxed tennis sleepy_up_open"),
            overlap_images("cg k room eve", "HirokoHypno drooping tennis sleep"),
            overlap_images("cg k room eve", "HirokoHypno drooping tennis sleeptalk"),
            overlap_images("cg k room eve", "HirokoHypno relaxed tennis drowsy"),
            overlap_images("cg k room eve", "HirokoHypno upright tennis blush annoyed"),
            overlap_images("cg k room eve", "HirokoHypno upright tennis blush sleeptalk"),
            overlap_images("cg k room eve", "HirokoHypno upright tennis blush angry clenched_fists_tennis"),
            overlap_images("cg k room eve", "HirokoHypno upright tennis blush frown"),
        ] + unlockable_image_list("persistent.room_hiroko_2_unlock", [
            overlap_images("cg k room eve", "HirokoHypno upright tennis blush neutral"),          
            overlap_images("cg k room eve", "HirokoHypno upright tennis angry blush"),           
            overlap_images("cg k room eve", "HirokoHypno upright tennis blush surprised relaxed_fists_tennis"),          
            overlap_images("cg k room eve", "HirokoHypno upright tennis blush scared relaxed_fists_tennis"),          
            overlap_images("cg k room eve", "HirokoHypno upright tennis sleeptalk"),          
            overlap_images("cg k room eve", "HirokoHypno upright tennis angry"),          
            overlap_images("cg k room eve", "HirokoHypno upright tennis blush annoyed_up"),          
            overlap_images("cg k room eve", "HirokoHypno relaxed tennis sleep"),           
            overlap_images("cg k room eve", "HirokoHypno relaxed tennis neutral"),
        ]),
        "classroomlunch3": [

        ] + unlockable_image_list("persistent.classroomlunch3_2_unlock", [ #Sayori version
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_sayori nozo_lunch n_folded n_curious_right glasses sayori s_neutral_nozomi_alert",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_sayori nozo_lunch n_folded n_curious_right glasses sayori s_sigh_alert",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_annoyed_sayori nozo_lunch n_folded n_curious_right glasses sayori s_sigh_alert",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_annoyed_sayori nozo_lunch n_armup n_sigh glasses sayori s_neutral_nozomi_alert",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_sayori nozo_lunch n_armup n_sigh glasses sayori s_neutral_nozomi_alert",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_sayori nozo_lunch n_armup n_smile_right glasses sayori s_neutral_nozomi_alert",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_grin_sayori nozo_lunch n_armup n_smile_right glasses sayori s_neutral_nozomi_alert",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_grin_sayori nozo_lunch n_armup n_smile_right glasses sayori s_smile_hiroko_alert",
        ]) + unlockable_image_list("persistent.classroomlunch3_3_unlock", [ #Hiroko version
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_folded n_thinking glasses sayori s_neutral_nozomi",            
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_folded n_thinking glasses sayori s_neutral_hiroko",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_armup n_smile_left glasses sayori s_neutral_hiroko",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_smile_nozomi nozo_lunch n_armup n_smile_right glasses sayori s_smile_hiroko",
        ]) + unlockable_image_list("persistent.classroomlunch3_4_unlock", [ #Villain version
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_folded n_thinking glasses sayori s_neutral_nozomi",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_folded n_thinking glasses sayori s_neutral_hiroko",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_nozomi nozo_lunch n_folded n_thinking glasses sayori s_neutral_hiroko",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_neutral_nozomi nozo_lunch n_armup n_nervous_left glasses sayori s_neutral_hiroko",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_worried_nozomi nozo_lunch n_armup n_nervous_left glasses sayori s_concerned_nozomi",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_worried_nozomi nozo_lunch n_folded n_sigh glasses sayori s_concerned_nozomi",
            "ClassroomLunch boy1 girl1 girl2 boy2_lunch boy3 hiroko h_sad_nozomi nozo_lunch n_folded n_sigh glasses sayori s_concerned_nozomi",
        ]),
        #Page 4
        "classroom lunch2 delusion": [
            "ClassroomLunch2 kyou nozomi1 n_smile s_frown hiroko1 h_frown",
            "ClassroomLunch2 kyou nozomi1 n_neutral_right s_frown hiroko1 h_frown_left",
            "ClassroomLunch2 kyou nozomi1 n_neutral_right s_neutral_right hiroko1 h_frown_left",
            "ClassroomLunch2 kyou nozomi1 n_happy s_neutral_right hiroko1 h_frown_left",
            "ClassroomLunch2 kyou nozomi1 n_happy s_neutral_right hiroko1 h_rolleyes",
            "ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_right hiroko1 h_rolleyes",
            "ClassroomLunch2 kyou nozomi1 n_neutral s_neutral hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi1 n_neutral s_neutral hiroko1 h_neutral",
            "ClassroomLunch2 kyou nozomi1 n_neutral s_irritated hiroko1 h_neutral",
            "ClassroomLunch2 kyou nozomi2 n_concerned_side s_neutral_left hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi2 n_concerned_side s_neutral_left hiroko1 h_sad",
            "ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_left hiroko1 h_sad",
            "ClassroomLunch2 kyou nozomi2 n_smile_side s_neutral_left hiroko1 h_sad",
            "ClassroomLunch2 kyou nozomi1 n_pout s_neutral_left hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi1 n_pout s_irritated hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi1 n_sigh s_irritated hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi2 n_neutral_side s_neutral_left hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi1 n_neutral s_frown hiroko1 h_frown",
            "ClassroomLunch2 kyou nozomi1 n_curious_right s_frown hiroko1 h_frown",
            "ClassroomLunch2 kyou nozomi1 n_curious_right s_frown hiroko1 h_rolleyes",
            "ClassroomLunch2 kyou nozomi1 n_neutral_right s_sleep hiroko1 h_rolleyes",
            "ClassroomLunch2 kyou nozomi1 n_neutral s_neutral hiroko1 h_neutral",
            "ClassroomLunch2 kyou nozomi1 n_neutral s_neutral hiroko1 h_frown",
            "ClassroomLunch2 kyou nozomi1 n_neutral s_smile_right hiroko1 h_frown",
            "ClassroomLunch2 kyou nozomi1 n_neutral s_smile_right hiroko1 h_pout",
            "ClassroomLunch2 kyou nozomi1 n_curious s_neutral hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi1 n_curious s_neutral hiroko1 h_growl",
            "ClassroomLunch2 kyou nozomi1 n_curious s_neutral hiroko2 h_mad",
            "ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko2 h_mad",
            "ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko2 h_growl",
            "ClassroomLunch2 kyou nozomi1 n_happy n_blush s_worried hiroko2 h_frown_left",
            "ClassroomLunch2 kyou nozomi1 n_happy n_blush s_sleep hiroko1 h_frown_left",
            "ClassroomLunch2 kyou nozomi2 n_concerned_side s_irritated hiroko1 h_worried_left",
            "ClassroomLunch2 kyou nozomi1 n_concerned s_irritated hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_left hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi2 n_smile_side s_neutral_left hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi2 n_smile_side s_smile_left hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi2 n_smile_side s_smile_left hiroko1 h_happy",
            "ClassroomLunch2 kyou nozomi1 n_smile n_blush s_smile_left hiroko1 h_happy",
            "ClassroomLunch2 kyou nozomi1 n_sigh n_blush s_smile_left hiroko1 h_happy",
            "ClassroomLunch2 kyou nozomi1 n_sigh n_blush s_smile_left hiroko1 h_smirk_left",
            "ClassroomLunch2 kyou nozomi1 n_pout n_blush s_smile_left hiroko1 h_smirk_left",
            "ClassroomLunch2 kyou nozomi1 n_pout n_blush s_smile_left hiroko1 h_happy",
        ],
        "akiko student council hypno": [
            "AkikoSC akiko arms_up surprised1 kyou",
            "AkikoSC akiko arms_up surprised1 kyou penlight",
            "AkikoSC akiko arms_up surprised2 kyou penlight",
            "AkikoSC akiko arms_up confused1 kyou penlight",
            "AkikoSC akiko arms_up confused2 kyou penlight",
            "AkikoSC akiko arms_down sleepy1 kyou penlight",
            "AkikoSC akiko arms_down sleepy2 kyou penlight",
            "AkikoSC akiko arms_down sleep kyou penlight",
            "AkikoSC akiko arms_down sleep kyou",
            "AkikoSC akiko arms_down sleeptalk kyou",
            ConditionSwitch(
                "persistent.akiko_student_council_hypno2_unlock", "AkikoSC akiko arms_down nozomi sleep kyou", #The second part is unlocked when Kyou commits to the "turn Akiko into Nozomi" path
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.akiko_student_council_hypno2_unlock", "AkikoSC akiko arms_down nozomi sleeptalk kyou",
                "True", "cg locked.png"
            ),
        ],
        "sleeper agent night": [
            "HirokoCourtNight hiroko_phone surprised kyou_arm_uniform kyou_uniform",
            "HirokoCourtNight hiroko_phone surprised_light kyou_arm_uniform kyou_uniform",
            "HirokoCourtNight hiroko_phone sleepy kyou_arm_uniform kyou_uniform",
            "HirokoCourtNight hiroko_phone sleepy_light kyou_arm_uniform kyou_uniform",
            "HirokoCourtNight hiroko_standing entranced kyou_arm_uniform kyou_uniform",
            "HirokoCourtNight hiroko_standing entranced kyou_uniform",
            "HirokoCourtNight hiroko_standing entranced_talk kyou_uniform",
        ],
        "akiko student council hypno2": [
            "AkikoSC akiko2 arms_down excited1",
            "AkikoSC akiko2 arms_down excited1 penlight",
            "AkikoSC akiko2 arms_down excited2 penlight",
            "AkikoSC akiko2 arms_down smile1 penlight",
            "AkikoSC akiko2 arms_down smile2 penlight",
            "AkikoSC akiko2 arms_down sleepy1 penlight",
            "AkikoSC akiko2 arms_down sleepy2 penlight",
            "AkikoSC akiko2 arms_down sleep penlight",
            "AkikoSC akiko2 arms_down sleep",
            "AkikoSC akiko2 arms_down sleeptalk",
            "AkikoSC akiko2 arms_down smile1",
        ],
        "hiroko trapped": [
            overlap_images("cg k room eve2", "HirokoTrapped Struggling"),
            overlap_images("cg k room eve2", "HirokoTrapped Kyou Struggling"),
            overlap_images("cg k room eve2", "HirokoTrapped Kyou Surprised"),
        ],
        "creepy hiroko": [
            "CreepyHiroko girls nozo_worried glasses hiro_excited",
            "CreepyHiroko girls nozo_nervous glasses hiro_laugh",
            "CreepyHiroko girls nozo_frown glasses hiro_worried",
            "CreepyHiroko girls nozo_angry glasses hiro_shocked",
            "CreepyHiroko hiroko hiro_fearful",
            "CreepyHiroko hiroko hiro_tearful",
        ],
        "hiroko tickle": [
            "HirokoTickle tickle",
            "HirokoTickle tickle karm_one",
            "HirokoTickle tickle hface_grimace karm_one",
            "HirokoTickle tickle harmdown_twitch hface_grimace karm_one",
            "HirokoTickle tickle harmdown_twitch hface_laugh karm_one",
            "HirokoTickle tickle harmup harmdown_notwitch hbodytwitch hface_laugh karm_one",
            "HirokoTickle tickle harmup harmdown_notwitch hbodytwitch hface_laugh karm_one kface_smirk",
            "HirokoTickle tickle harmup harmdown_notwitch hbodytwitch hface_laugh karm_two kface_smirk",
        ],
        "hiroko couch argument": [
            "HirokoCouchArgument",
            "HirokoCouchArgument kyou_glare",
            "HirokoCouchArgument kyou_glare hiro_frown",
            "HirokoCouchArgument kyou_angry hiro_frown",
            "HirokoCouchArgument kyou_angry hiro_angry",
        ],
        #Page 5
        "k room nozomi 2 1":[
            overlap_images("cg k room eve", "NozomiHypno standing casual neutral"),
            overlap_images("cg k room eve", "NozomiHypno standing casual stern"),
            overlap_images("cg k room eve", "NozomiHypno standing casual sad"),
            overlap_images("cg k room eve", "NozomiHypno standing casual lookup"),
            overlap_images("cg k room eve", "NozomiHypno standing casual annoyed"),
            overlap_images("cg k room eve", "NozomiHypno standing casual stern_closed"),
            overlap_images("cg k room eve", "NozomiHypno standing casual surprised"),
            overlap_images("cg k room eve", "NozomiHypno standing casual angry blush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual confused noblush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual laugh noblush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual smile noblush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual smile_closed noblush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual sad blush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual laugh blush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual smile blush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual stern_closed blush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual stern blush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual confused blush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual lookup noblush"),
            overlap_images("cg k room eve", "NozomiHypno standing casual drowsy noblush"),
            overlap_images("cg k room eve", "NozomiHypno drooping casual sleepy noblush"),
            overlap_images("cg k room eve", "NozomiHypno drooping casual sleep noblush"),
            overlap_images("cg k room eve", "NozomiHypno drooping casual sleeptalk noblush"),
            ConditionSwitch(
                "persistent.k_room_nozomi_2_2_unlock", overlap_images("cg k room eve", "NozomiHypno drooping casual sleep arm_uniform noblush"),
                "True", "cg locked.png"
            ),
        ],
        "zombie beginning": [
            "ZombieBeginning",
            "ZombieBeginning arms_up",
            "ZombieBeginning arms_up angry",
        ],
        "nozomi injured": [
            "NozomiInjured pain",
            "NozomiInjured worried",
            "NozomiInjured worried kyou",
            "NozomiInjured sigh kyou",
        ],
        "sayori arm": [
            "CouchHypno sayori_sleeping_down sleep",
            "CouchHypno sayori_sleeping_up sleep kyou_up",
            "CouchHypno sayori_sleeping_up sleeptalk kyou_up",
            "CouchHypno sayori_sleeping_up sleep kyou_down",
            "CouchHypno sayori_waking_up thinking",
            "CouchHypno sayori_waking_up sleepy",
            "CouchHypno sayori_waking_up surprised",
            "CouchHypno sayori_waking_up puzzled",
            "CouchHypno sayori_struggling frown",
            "CouchHypno sayori_struggling thinking",
            "CouchHypno sayori_waking_up thinking",
            "CouchHypno sayori_waking_up concerned",
            "CouchHypno sayori_waking_up thinking",
            "CouchHypno sayori_sleeping_up sleep",
            "CouchHypno sayori_sleeping_up sleeptalk",
            "CouchHypno sayori_waking_up concerned",
            "CouchHypno sayori_waking_up puzzled",
            "CouchHypno sayori_waking_up chuckle",
            "CouchHypno sayori_waking_up smile",
            "CouchHypno sayori_struggling thinking",
            "CouchHypno sayori_waking_up puzzled",
            "CouchHypno sayori_waking_up shocked",
            "CouchHypno sayori_waking_up shocked kyou_up",
            "CouchHypno sayori_waking_up surprised kyou_up",
            "CouchHypno sayori_waking_up sleepy kyou_up",
            "CouchHypno sayori_waking_up thinking kyou_up",
            "CouchHypno sayori_sleeping_up sleep kyou_up",
            "CouchHypno sayori_sleeping_down sleep kyou_down",
            "CouchHypno sayori_waking_down thinking",
            "CouchHypno sayori_waking_down sleepy",
            "CouchHypno sayori_waking_down smile",
        ],
        "sayori sleeper capture": [
            "SayoriSleeperCapture hiro_tired sayori_head_up sayori_stern",
            "SayoriSleeperCapture hiro_tired sayori_head_up sayori_stern_flash",
            "SayoriSleeperCapture hiro_tired sayori_head_up sayori_startled",
            "SayoriSleeperCapture hiro_tired_flash sayori_head_up sayori_startled",
            "SayoriSleeperCapture hiro_angry sayori_head_up sayori_startled",
            "SayoriSleeperCapture hiro_angry sayori_head_up sayori_startled_flash",
            "SayoriSleeperCapture hiro_angry sayori_head_up sayori_angry",
            "SayoriSleeperCapture hiro_angry sayori_head_up sayori_angry_flash",
            "SayoriSleeperCapture hiro_surprised sayori_head_up sayori_angry",
            "SayoriSleeperCapture hiro_surprised sayori_head_up sayori_confused",
            "SayoriSleeperCapture hiro_surprised_flash sayori_head_up sayori_confused",
            "SayoriSleeperCapture hiro_sleepy sayori_head_up sayori_confused",
            "SayoriSleeperCapture hiro_sleepy_flash sayori_head_up sayori_confused",
            "SayoriSleeperCapture hiro_blank sayori_head_up sayori_confused",
            "SayoriSleeperCapture hiro_blank sayori_head_up sayori_confused_flash",
            "SayoriSleeperCapture hiro_blank sayori_head_up sayori_anxious",
            "SayoriSleeperCapture hiro_blank sayori_head_up sayori_anxious_flash",
            "SayoriSleeperCapture hiro_blank sayori_head_up sayori_sleepy",
            "SayoriSleeperCapture hiro_blank sayori_head_up sayori_sleepy_flash",
            "SayoriSleeperCapture kyou kyou_arm_right kyou_neutral hiro_blank sayori_head_up sayori_anxious",
            "SayoriSleeperCapture kyou kyou_arm_right kyou_neutral hiro_blank sayori_head_down sayori_sleep",
            "SayoriSleeperCapture kyou kyou_arm_down kyou_neutral hiro_blank sayori_head_down sayori_sleep",
            "SayoriSleeperCapture kyou kyou_arm_down kyou_neutral hiro_blank sayori_head_down sayori_sleeptalk",
            "SayoriSleeperCapture kyou kyou_arm_down kyou_smile hiro_blank sayori_head_down sayori_sleep",
            "SayoriSleeperCapture kyou kyou_arm_down kyou_smile hiro_blank sayori_head_up sayori_blank",
            "SayoriSleeperCapture kyou kyou_arm_both kyou_smile hiro_blank sayori_head_up sayori_blank",
            "SayoriSleeperCapture kyou kyou_arm_both kyou_grin hiro_blank sayori_head_up sayori_blank",
            "SayoriSleeperCapture kyou kyou_arm_down kyou_smile hiro_blank sayori_head_up sayori_blank",
            "SayoriSleeperCapture kyou kyou_phone kyou_smile hiro_blank sayori_head_up sayori_blank",
            "SayoriSleeperCapture kyou kyou_phone kyou_smile hiro_blank sayori_head_up sayori_blank_talk",
            "SayoriSleeperCapture kyou kyou_arm_down kyou_smile hiro_blank sayori_head_up sayori_blank",
            "SayoriSleeperCapture kyou kyou_arm_left kyou_neutral hiro_blank sayori_head_up sayori_blank",
            "SayoriSleeperCapture kyou kyou_arm_both kyou_neutral hiro_blank sayori_head_up sayori_blank",
            "SayoriSleeperCapture kyou kyou_arm_both kyou_neutral hiro_blank_talk sayori_head_up sayori_blank_talk",
            "SayoriSleeperCapture kyou kyou_arm_both kyou_grin hiro_blank sayori_head_up sayori_blank",
            "SayoriSleeperCapture kyou kyou_arm_both kyou_grin hiro_blank_talk sayori_head_up sayori_blank_talk",
            "SayoriSleeperCapture kyou kyou_arm_both kyou_smile hiro_blank sayori_head_up sayori_blank",
            "SayoriSleeperCapture kyou kyou_arm_both kyou_smile hiro_blank_talk sayori_head_up sayori_blank_talk",
            "SayoriSleeperCapture kyou kyou_arm_down kyou_smile hiro_blank sayori_head_up sayori_blank",
        ],
        "classroomlunch4 1":[
            "ClassroomLunch boy2_lunch hiroko h_laugh n_armup n_smile_left glasses sayori s_smile_hiroko",
            "ClassroomLunch boy2_lunch hiroko h_laugh n_armup n_sigh glasses sayori s_neutral_hiroko",
            "ClassroomLunch boy2_lunch hiroko h_worried_nozomi n_armup n_sigh glasses sayori s_neutral_hiroko",
            "ClassroomLunch boy2_lunch hiroko h_worried_nozomi n_armup n_curious_right glasses sayori s_sigh",
            "ClassroomLunch boy2_lunch hiroko h_grin_sayori n_armup n_curious_right glasses sayori s_sigh",
            "ClassroomLunch boy2_lunch hiroko h_neutral_nozomi n_folded n_frown_left glasses sayori s_neutral_nozomi",
            "ClassroomLunch boy2_lunch hiroko h_annoyed_sayori n_folded n_frown_left glasses sayori s_neutral_nozomi",
            "ClassroomLunch boy2_lunch hiroko h_grin_sayori n_folded n_sigh glasses sayori s_neutral_nozomi",
            "ClassroomLunch boy2_lunch hiroko h_grin_sayori n_folded n_sigh glasses sayori s_smirk_hiroko",
        ],
        "akiko intro": [
            "AkikoIntro akiko2 worried",
            "AkikoIntro akiko2 sigh",
            "AkikoIntro akiko1 frown",
            "AkikoIntro akiko1 happy",
            "AkikoIntro akiko1 cheerful",
            "AkikoIntro akiko1 frown",
            "AkikoIntro akiko1 awkward",
            "AkikoIntro akiko1 smile",
        ],
        "k room nozomi reversal1": [
            overlap_images("cg k room reversal", "NozomiReversal penlight casual smile"),
            overlap_images("cg k room reversal", "NozomiReversal penlight casual neutral"),
            ConditionSwitch(
                "persistent.k_room_nozomi_reversal2_unlock", overlap_images("cg k room reversal", "NozomiReversal penlight casual laugh"),
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.k_room_nozomi_reversal3_unlock", overlap_images("cg k room reversal", "NozomiReversal penlight uniform neutral"),
                "True", "cg locked.png"
            ),   
            ConditionSwitch(
                "persistent.k_room_nozomi_reversal3_unlock", overlap_images("cg k room reversal", "NozomiReversal penlight uniform smile"),
                "True", "cg locked.png"
            ),
        ],
        "k room nozomi tv1": [ #This is a tricky one. So first, we start with the first few images that get unlocked from the first time we see Nozomi sitting with the tv behind her.
            overlap_images("cg k room tv eve", "NozomiHypno standing casual2 smile2"), #With the overlap functions because this one's in the old fashined multi-image declaration format
            overlap_images("cg k room tv eve", "NozomiHypno standing casual2 laugh"),
            overlap_images("cg k room tv eve", "NozomiHypno standing casual2 smile_closed"),
            overlap_images("cg k room tv eve", "NozomiHypno standing casual2 neutral2"),
            overlap_images("cg k room tv eve", "NozomiHypno standing casual2 annoyed"),
            ConditionSwitch( #Then we add a condition switch, because only one image depends on the k_room_nozomi_tv2_unlock variable
                "persistent.k_room_nozomi_tv2_unlock", overlap_images("cg k room tv eve", "NozomiHypno standing casual2 stern2"),
                "True", "cg locked.png"
            ),
        ] + unlockable_image_list("persistent.k_room_nozomi_tv4_unlock", [ #Then we close the square brackets, without comma, and use the unlockable_image_list function, because multiple images stringed together depend on k_room_nozomi_tv4_unlock.
            overlap_images("cg k room tv eve", "NozomiHypno standing casual2 smile2 blush2"),
            overlap_images("cg k room tv eve", "NozomiHypno standing casual2 smile_closed blush2"),
            overlap_images("cg k room tv eve", "NozomiHypno standing casual2 confused2 blush2"),
            overlap_images("cg k room tv eve", "NozomiHypno standing casual2 surprised2 blush2"),
            overlap_images("cg k room tv eve", "NozomiHypno standing casual2 stern2 blush2"),
            overlap_images("cg k room tv eve", "NozomiHypno standing casual2 laugh blush2"),
        ]) + [ #There's no need to put the function itself between square brackets. Then we write + and open square brackets again...
            ConditionSwitch( #... and add another ConditionSwitch because, once again, there's a single image depending on the k_room_nozomi_tv4_unlock variable
                "persistent.k_room_nozomi_tv4_unlock", overlap_images("cg k room tv eve"),
                "True", "cg locked.png"
            )
        ], #Then we finally close these last square brackets and add a comma, marking the end of this CG group.
        "k room hiroko tv1": [
            overlap_images("cg k room tv eve", "HirokoHypno upright tennis2 frown2 clenched_fists_tennis2"),
            overlap_images("cg k room tv eve", "HirokoHypno upright tennis2 angry2 clenched_fists_tennis2"),
            overlap_images("cg k room tv eve", "HirokoHypno upright tennis2 angry2"),
            overlap_images("cg k room tv eve", "HirokoHypno upright tennis2 sleeptalk"),
            overlap_images("cg k room tv eve", "HirokoHypno upright tennis2 sleep"),
            overlap_images("cg k room tv eve", "HirokoHypno upright tennis2 annoyed_up2"),
            overlap_images("cg k room tv eve", "HirokoHypno upright tennis2 annoyed2"),
            overlap_images("cg k room tv eve", "HirokoHypno upright tennis2 smirk2"),
        ] + unlockable_image_list("persistent.k_room_hiroko_tv2_unlock", [
            overlap_images("cg k room tv eve", "HirokoHypno upright tennis2 frown2"),
            overlap_images("cg k room tv eve", "HirokoHypno upright tennis2 frown2 relaxed_fists_tennis2"),
            overlap_images("cg k room tv eve", "HirokoHypno upright tennis2 neutral2"),
        ]),
        #Page 6
        "hiroko reversal": [
            overlap_images("cg k room reversal","HirokoReversal nervous"),
            overlap_images("cg k room reversal","HirokoReversal body nervous_side"),
            overlap_images("cg k room reversal","HirokoReversal body_blush angry"),
            overlap_images("cg k room reversal","HirokoReversal body angry"),
            overlap_images("cg k room reversal","HirokoReversal body neutral"),
            overlap_images("cg k room reversal","HirokoReversal body smirk"),
        ],
        "hiroko cat 2": [
            "Hiroko Cat2 light1",
            "Hiroko Cat2 hiroko1 annoyed light1",
            "Hiroko Cat2 hiroko1 surprised light2",
            "Hiroko Cat2 hiroko2 angry light2",
            "Hiroko Cat2 hiroko2 angry",
            "Hiroko Cat2 hiroko2 curious",
        ],
        "hiroko cat 1": [
            overlap_images("cg k room ground eve", "Hiroko Cat happy"),
            overlap_images("cg k room ground eve", "Hiroko Cat dazed"),
            overlap_images("cg k room ground eve", "Hiroko Cat lying sleep"),
            overlap_images("cg k room ground eve", "Hiroko Cat lying waking"),
        ],
        "k room sayori": [
            overlap_images("cg k room eve", "SayoriHypno standing alert_smile"),
            overlap_images("cg k room eve", "SayoriHypno standing alert_smile blush"),
            overlap_images("cg k room eve", "SayoriHypno standing alert_looking"),
            overlap_images("cg k room eve", "SayoriHypno standing alert_surprised"),
            overlap_images("cg k room eve", "SayoriHypno standing alert_drowsytalk"),
            overlap_images("cg k room eve", "SayoriHypno standing alert_drowsy"),
            overlap_images("cg k room eve", "SayoriHypno standing alert_sleep"),
            overlap_images("cg k room eve", "SayoriHypno standing alert_sleep blush"),
            overlap_images("cg k room eve", "SayoriHypno drooping alert_sleep"),
            overlap_images("cg k room eve", "SayoriHypno drooping alert_sleeptalk"),
            overlap_images("cg k room eve", "SayoriHypno drooping alert_sleeptalk blush"),
        ],
        "sayori alter start": [
            overlap_images("cg k bedroom eve1", "Sayori_K_Bedroom happy"),
            overlap_images("cg k bedroom eve1", "Sayori_K_Bedroom happy blush"),
            overlap_images("cg k bedroom eve1", "Sayori_K_Bedroom shy smile_side"),
            overlap_images("cg k bedroom eve1", "Sayori_K_Bedroom shy blush smile_side"),
            overlap_images("cg k bedroom eve1", "Sayori_K_Bedroom shy smile_front"),
            overlap_images("cg k bedroom eve1", "Sayori_K_Bedroom shy blush smile_front"),
            overlap_images("cg k bedroom eve1", "Sayori_K_Bedroom shy surprised"),
            overlap_images("cg k bedroom eve1", "Sayori_K_Bedroom shy blush surprised"),
        ],
        "sayori greeting": [
            "SayoriGreeting laugh",
            "SayoriGreeting cheerful",
            "SayoriGreeting neutral",
            "SayoriGreeting smile",
            "SayoriGreeting smile blush",
        ],
        "nozomisleepercapture": [
            "NozomiSleeperCapture",
            "NozomiSleeperCapture nozo_scream_light",
            "NozomiSleeperCapture hiro_angry",
            "NozomiSleeperCapture hiro_angry nozo_scream_light",
            "NozomiSleeperCapture nozo_screamup_light",
            "NozomiSleeperCapture nozo_screamup",
            "NozomiSleeperCapture hiro_angry nozo_screamup",
            "NozomiSleeperCapture hiro_angry nozo_screamup_light",
            "NozomiSleeperCapture hiro_angry nozo_sleepy",
            "NozomiSleeperCapture hiro_angry nozo_sleepy sayo_angry",
            "NozomiSleeperCapture hiro_angry nozo_sleepy_light sayo_angry",
            "NozomiSleeperCapture nozo_subdued sayo_subdued sayo_angry hiro_subdued hiro_angry2 nozo_sleepy",
            "NozomiSleeperCapture nozo_subdued sayo_subdued sayo_angry hiro_subdued hiro_angry2 nozo_sleepy_light",
            "NozomiSleeperCapture nozo_subdued sayo_subdued sayo_angry hiro_subdued hiro_angry2 nozo_sleep",
            "NozomiSleeperCapture nozo_subdued sayo_subdued sayo_angry hiro_subdued hiro_growl2 nozo_sleep",
            "NozomiSleeperCapture nozo_subdued sayo_subdued sayo_surprised hiro_subdued hiro_surprised nozo_sleep",
            "NozomiSleeperCapture nozo_subdued sayo_subdued sayo_surprised_light hiro_subdued hiro_surprised_light nozo_sleep",
            "NozomiSleeperCapture nozo_subdued sayo_subdued sayo_entranced hiro_subdued hiro_entranced nozo_sleep",
            "NozomiSleeperCapture nozo_subdued sayo_subdued sayo_entranced hiro_subdued hiro_entranced nozo_entranced",
            "NozomiSleeperCapture nozo_standing sayo_standing sayo_blank hiro_standing hiro_blank nozo_blank glasses_standing",
            "NozomiSleeperCapture nozo_standing sayo_standing sayo_blank hiro_standing hiro_blank nozo_blanktalk glasses_standing",
            "NozomiSleeperCapture nozo_standing sayo_standing sayo_blank hiro_standing hiro_blank nozo_blank glasses_standing",
            "NozomiSleeperCapture nozo_standing sayo_standing sayo_blanktalk hiro_standing hiro_blanktalk nozo_blanktalk glasses_standing",
        ],
        "delusion struggle sayori": [
            "DelusionStruggleSayori",
            "DelusionStruggleSayori sayori_struggling s_angry_up_flash",
            "DelusionStruggleSayori sayori_struggling s_angry",
            "DelusionStruggleSayori sayori_struggling s_angry_up_flash",
            "DelusionStruggleSayori sayori_struggling s_angry_up",
            "DelusionStruggleSayori sayori_struggling s_angry_up k_concerned",
            "DelusionStruggleSayori sayori_struggling s_angry_up_flash k_concerned",
            "DelusionStruggleSayori sayori_struggling s_worried k_concerned",
            "DelusionStruggleSayori sayori_struggling s_worried_flash k_concerned",
            "DelusionStruggleSayori sayori_struggling s_worried k_calm",
            "DelusionStruggleSayori sayori_struggling s_worried_flash k_calm",
            "DelusionStruggleSayori sayori_relaxing s_worried k_calm",
            "DelusionStruggleSayori sayori_relaxing s_worried_flash k_calm",
            "DelusionStruggleSayori sayori_relaxing s_sleepy k_calm",
            "DelusionStruggleSayori sayori_relaxing s_sleepy_flash k_calm",
        ],
        "devotion tennis": [ #Devotion bedroom day4_1
            "DevotionBedroom head_up_blush tennis_armsdown neutral_right",
            "DevotionBedroom head_up_blush tennis_armsdown happy",
            "DevotionBedroom head_up_blush tennis_armsdown confused",
            "DevotionBedroom head_up_blush tennis_armsdown smile",
            "DevotionBedroom head_up tennis_armsdown neutral_right",
            "DevotionBedroom head_up tennis_armsdown happy",
            "DevotionBedroom head_up tennis_armsdown smile",
            "DevotionBedroom head_up tennis_armsup frown_right",
            "DevotionBedroom head_up tennis_armsup confused",
            "DevotionBedroom head_up tennis_armsdown confused",
            "DevotionBedroom head_up tennis_armsup sad",
            "DevotionBedroom head_up tennis_armsup cry",
            "DevotionBedroom head_up tennis_armsup neutral kyou_arm",
            "DevotionBedroom head_up tennis_armsdown neutral kyou_arm",
            "DevotionBedroom head_up tennis_armsdown awe kyou_arm",
            "DevotionBedroom head_up_blush tennis_armsup smile kyou_arm",
            "DevotionBedroom head_up_blush tennis_armsup sultry kyou_arm",
            "DevotionBedroom head_up_blush tennis_armsup confused kyou_arm",
            "DevotionBedroom head_up_blush tennis_armsup laugh kyou",
            "DevotionBedroom head_up_blush tennis_armsup smile kyou",
            "DevotionBedroom head_up_blush tennis_armsdown smile_light kyou",
            "DevotionBedroom head_up tennis_armsdown smile_light",
            "DevotionBedroom head_up tennis_armsdown neutral_light",
            "DevotionBedroom head_up tennis_armsdown straining",
            "DevotionBedroom head_up tennis_armsdown straining_light",
            "DevotionBedroom head_down tennis_armsdown sleep",
            "DevotionBedroom head_down tennis_armsdown sleeptalk",
            "DevotionBedroom head_down tennis_armsdown sleepy",
            "DevotionBedroom head_down tennis_holding awe_down",
            "DevotionBedroom head_up_blush tennis_holding sultry",
            "DevotionBedroom head_up_blush tennis_holding confused",
        ],
        #Page 7
        "devotion tennis partial":[ #devotion bedroom day4_2
            "DevotionBedroom head_up_blush tennis_armsup_partial sad",
            "DevotionBedroom head_up_blush tennis_armsdown_partial neutral_right",
            "DevotionBedroom head_up_blush tennis_armsdown_partial sad",
            "DevotionBedroom head_up_blush tennis_armsdown_partial cry",
            "DevotionBedroom head_up_blush tennis_armsdown_partial confused",
            "DevotionBedroom head_up_blush tennis_armsdown_partial smile",
            "DevotionBedroom head_up_blush tennis_armsdown_partial happy",
            "DevotionBedroom head_up tennis_armsdown_partial neutral_right",
            "DevotionBedroom head_up tennis_armsdown_partial happy",
            "DevotionBedroom head_up tennis_armsdown_partial smile",
            "DevotionBedroom head_up tennis_armsup_partial frown_right",
            "DevotionBedroom head_up tennis_armsup_partial confused",
            "DevotionBedroom head_up tennis_armsdown_partial confused",
            "DevotionBedroom head_up tennis_armsup_partial sad",
            "DevotionBedroom head_up tennis_armsup_partial cry",
            "DevotionBedroom head_up tennis_armsup_partial neutral kyou_arm",
            "DevotionBedroom head_up tennis_armsdown_partial neutral kyou_arm",
            "DevotionBedroom head_up tennis_armsdown_partial awe kyou_arm",
            "DevotionBedroom head_up_blush tennis_armsup_partial smile kyou_arm",
            "DevotionBedroom head_up_blush tennis_armsup_partial sultry kyou_arm",
            "DevotionBedroom head_up_blush tennis_armsup_partial confused kyou_arm",
            "DevotionBedroom head_up_blush tennis_armsup_partial laugh kyou",
            "DevotionBedroom head_up_blush tennis_armsup_partial smile kyou_arm",
            "DevotionBedroom head_up_blush tennis_armsdown_partial smile_light kyou",
            "DevotionBedroom head_up tennis_armsdown_partial smile_light",
            "DevotionBedroom head_up tennis_armsdown_partial neutral_light",
            "DevotionBedroom head_up tennis_armsdown_partial straining",
            "DevotionBedroom head_up tennis_armsdown_partial straining_light",
            "DevotionBedroom head_down tennis_armsdown_partial sleep",
            "DevotionBedroom head_down tennis_armsdown_partial sleeptalk",
            "DevotionBedroom head_down tennis_armsdown_partial sleepy",
            "DevotionBedroom head_down tennis_holding_partial awe_down",
            "DevotionBedroom head_up_blush tennis_holding_partial sultry",
            "DevotionBedroom head_up_blush tennis_holding_partial confused",
        ],
        "devotion underwear": [
            "DevotionBedroom head_up_blush underwear_armsdown smile",
            "DevotionBedroom head_up_blush underwear_armsdown happy",
            "DevotionBedroom head_up_blush underwear_armsdown confused",
            "DevotionBedroom head_up underwear_armsdown neutral_right",
            "DevotionBedroom head_up underwear_armsdown happy",
            "DevotionBedroom head_up underwear_armsdown smile",
            "DevotionBedroom head_up underwear_armsup frown_right",
            "DevotionBedroom head_up underwear_armsup confused",
            "DevotionBedroom head_up underwear_armsdown confused",
            "DevotionBedroom head_up underwear_armsup sad",
            "DevotionBedroom head_up underwear_armsup cry",
            "DevotionBedroom head_up underwear_armsup neutral kyou_arm",
            "DevotionBedroom head_up underwear_armsdown neutral kyou_arm",
            "DevotionBedroom head_up underwear_armsdown awe kyou_arm",
            "DevotionBedroom head_up_blush underwear_armsup smile kyou_arm",
            "DevotionBedroom head_up_blush underwear_armsup sultry kyou_arm",
            "DevotionBedroom head_up_blush underwear_armsup confused kyou_arm",
            "DevotionBedroom head_up_blush underwear_armsup laugh kyou",
            "DevotionBedroom head_up_blush underwear_armsup happy kyou",
            "DevotionBedroom head_up_blush underwear_armsup smile kyou",
            "DevotionBedroom head_up_blush underwear_armsdown smile_light kyou",
            "DevotionBedroom head_up underwear_armsdown smile_light",
            "DevotionBedroom head_up underwear_armsdown neutral_light",
            "DevotionBedroom head_up underwear_armsdown straining",
            "DevotionBedroom head_up underwear_armsdown straining_light",
            "DevotionBedroom head_down underwear_armsdown sleep",
            "DevotionBedroom head_down underwear_armsdown sleeptalk",
            "DevotionBedroom head_down underwear_armsdown sleepy",
            "DevotionBedroom head_down underwear_holding awe_down",
            "DevotionBedroom head_up_blush underwear_holding sultry",
            "DevotionBedroom head_up_blush underwear_holding confused",
        ],
        "devotion naked": [
            "DevotionBedroom head_up_blush bare_armsdown smile",
            "DevotionBedroom head_up_blush bare_armsdown happy",
            "DevotionBedroom head_up_blush bare_armsdown confused",
            "DevotionBedroom head_up bare_armsdown neutral_right",
            "DevotionBedroom head_up bare_armsdown happy",
            "DevotionBedroom head_up bare_armsdown smile",
            "DevotionBedroom head_up bare_armsup frown_right",
            "DevotionBedroom head_up bare_armsup confused",
            "DevotionBedroom head_up bare_armsdown confused",
            "DevotionBedroom head_up bare_armsup sad",
            "DevotionBedroom head_up bare_armsup cry",
            "DevotionBedroom head_up bare_armsup neutral kyou_arm",
            "DevotionBedroom head_up bare_armsdown neutral kyou_arm",
            "DevotionBedroom head_up bare_armsdown awe kyou_arm",
            "DevotionBedroom head_up_blush bare_armsup smile kyou_arm",
            "DevotionBedroom head_up_blush bare_armsup sultry kyou_arm",
            "DevotionBedroom head_up_blush bare_armsup confused kyou_arm",
            "DevotionBedroom head_up_blush bare_armsup laugh kyou",
            "DevotionBedroom head_up_blush bare_armsup happy kyou",
            "DevotionBedroom head_up_blush bare_armsup smile kyou",
            "DevotionBedroom head_up_blush bare_armsdown smile_light kyou",
            "DevotionBedroom head_up bare_armsdown smile_light",
            "DevotionBedroom head_up bare_armsdown neutral_light",
            "DevotionBedroom head_up bare_armsdown straining",
            "DevotionBedroom head_up bare_armsdown straining_light",
            "DevotionBedroom head_down bare_armsdown sleep",
            "DevotionBedroom head_down bare_armsdown sleeptalk",
            "DevotionBedroom head_down bare_armsdown sleepy",
            "DevotionBedroom head_down bare_holding awe_down",
            "DevotionBedroom head_up_blush bare_holding sultry",
            "DevotionBedroom head_up_blush bare_holding confused",
        ],
        "study room hypno sayori": [
            "StudyRoomHypno hiroko1 h_happy sayori2 s_sleep",
            "StudyRoomHypno hiroko1 h_grin sayori2 s_sleep",
            "StudyRoomHypno hiroko2 h_grin h_blush1 sayori2 s_sleep",
            "StudyRoomHypno hiroko2 h_cheerful h_blush1 sayori2 s_sleep",
            "StudyRoomHypno hiroko2 h_happy h_blush1 sayori2 s_sleep",
            "StudyRoomHypno hiroko3 h_smug sayori2 s_sleep",
            "StudyRoomHypno hiroko3 h_smug sayori2 s_sleeptalk",
            "StudyRoomHypno hiroko3 h_smile_right sayori2 s_sleep",
            "StudyRoomHypno hiroko3 h_talking sayori2 s_sleep",
            "StudyRoomHypno hiroko3 h_smile_right sayori2 s_sleeptalk",
            "StudyRoomHypno hiroko3 h_smile sayori2 s_sleep",
            "StudyRoomHypno hiroko3 h_smile_right sayori2 s_sleep",
            "StudyRoomHypno hiroko3 h_smile_closed h_blush2 sayori2 s_sleep",
            "StudyRoomHypno hiroko3 h_smile_closed h_blush2 sayori2 s_sleeptalk",
            "StudyRoomHypno hiroko3 h_talking h_blush2 sayori2 s_sleep",
            "StudyRoomHypno hiroko3 h_smile_right h_blush2 sayori2 s_sleeptalk",
            "StudyRoomHypno hiroko3 h_smile_right sayori2 s_waking",
            "StudyRoomHypno hiroko3 h_laugh h_blush2 sayori2 s_waking",
            "StudyRoomHypno hiroko3 h_laugh h_blush2 sayori2 s_startled s_blush",
        ],
        "k phone robot": [
            "KyouPhone bedroom uniform nozomi_fear",
            "KyouPhone bedroom uniform nozomi_sleepy",
            "KyouPhone bedroom uniform nozomi_sleepy_hiroko",
        ],
        "nozomi robot kiss single image":[
            #This one is a single image
        ],
        "nozomi mindtrick": [
            "CouchHypno nozomi n_smile glasses kyou_down",
            "CouchHypno nozomi n_grumpy glasses kyou_down",
            "CouchHypno nozomi n_angry_open glasses kyou_down",
            "CouchHypno nozomi n_surprised glasses kyou_point",
            "CouchHypno nozomi n_dazed glasses kyou_point",
            "CouchHypno nozomi n_tranced glasses kyou_point",
            "CouchHypno nozomi n_neutral glasses kyou_down",
            "CouchHypno nozomi n_puzzled glasses kyou_down",
            "CouchHypno nozomi_blush n_laugh glasses kyou_down",
            "CouchHypno nozomi_blush n_surprised glasses kyou_down",
            "CouchHypno nozomi_blush n_angry_closed glasses kyou_down",
            "CouchHypno nozomi_headclutch_blush n_angry_open glasses nozomi_armsup kyou_down",
            "CouchHypno nozomi_headclutch_blush n_angry_closed glasses nozomi_armsup kyou_down",
            "CouchHypno nozomi n_angry_closed glasses kyou_down",
            "CouchHypno nozomi n_surprised glasses kyou_down",
            "CouchHypno nozomi n_surprised glasses kyou_wave",
            "CouchHypno nozomi n_dazed glasses kyou_wave",
            "CouchHypno nozomi n_tranced glasses kyou_wave",
            "CouchHypno nozomi n_tranced glasses kyou_down",
            "CouchHypno nozomi n_drool glasses kyou_down",
            "CouchHypno nozomi n_drool glasses kyou_point",
            "CouchHypno nozomi n_drool glasses kyou_wave",
            "CouchHypno nozomi_sleep kyou_down",
        ],
        "nozomi hiroko hug": [
            "NozomiHirokoHug nozomi_worried bruise1 hiroko_worried",
            "NozomiHirokoHug nozomi_irritated bruise1 hiroko_worried",
            "NozomiHirokoHug nozomi_irritated bruise1 hiroko_neutral",
            "NozomiHirokoHug nozomi_annoyed bruise1 hiroko_neutral",
            "NozomiHirokoHug nozomi_annoyed bruise1 hiroko_worried",
            "NozomiHirokoHug nozomi_worried bruise1 hiroko_worried",
            "NozomiHirokoHug girls2 nozomi_uncomfortable bruise2 hiroko_cry",
            "NozomiHirokoHug girls2 nozomi_uncomfortable bruise2 nozomi_blush2 hiroko_cry",
            "NozomiHirokoHug girls2 nozomi_shy bruise2 nozomi_blush2 hiroko_cry",
            "NozomiHirokoHug girls1 nozomi_smile bruise1 nozomi_blush1 hiroko_grin",
            "NozomiHirokoHug girls1 nozomi_happy bruise1 nozomi_blush1 hiroko_grin",
            "NozomiHirokoHug girls1 nozomi_happy bruise1 nozomi_blush1 hiroko_laugh",
            "NozomiHirokoHug girls1 nozomi_surprised bruise1 hiroko_laugh",
            "NozomiHirokoHug girls1 nozomi_annoyed bruise1 hiroko_smile",
            "NozomiHirokoHug girls1 nozomi_annoyed bruise1 hiroko_laugh hiroko_blush",
            "NozomiHirokoHug girls1 nozomi_annoyed bruise1 hiroko_neutral hiroko_blush",
            "NozomiHirokoHug girls1 nozomi_irritated bruise1 hiroko_neutral hiroko_blush",
            "NozomiHirokoHug girls1 nozomi_smile bruise1 hiroko_smile",
            "NozomiHirokoHug girls1 nozomi_squint bruise1 hiroko_smile",
            "NozomiHirokoHug girls1 nozomi_worried bruise1 hiroko_smile",
        ],
        "sayori lunch": [
            "SayoriLunch neutral",
            "SayoriLunch sleep",
            "SayoriLunch annoyed",
            "SayoriLunch irritated",
            "SayoriLunch concerned",
            "SayoriLunch concerned_side",
            "SayoriLunch puzzled",
            "SayoriLunch sleepy",
            "SayoriLunch rolleyes",
        ],
        #Page 8
        "sayori grab": [
            "SayoriGrab sayori1 scared",
            "SayoriGrab sayori2 scared",
            "SayoriGrab sayori2 sad",
        ],
        "sayori x kyou": [
            overlap_images("cg sayori x kyou", "Sayori x Kyou surprised"),
            overlap_images("cg sayori x kyou", "Sayori x Kyou relaxed"),
        ],
        "sayori walk": [
            "SayoriWalk kyou_surprised sayori_smile",
            "SayoriWalk kyou_surprised sayori_concerned",
            "SayoriWalk kyou_sigh sayori_concerned",
            "SayoriWalk kyou_sigh sayori_neutral",
            "SayoriWalk kyou_neutral sayori_smirk",
            "SayoriWalk kyou_annoyed sayori_smirk",
            "SayoriWalk kyou_annoyed sayori_happy",
            "SayoriWalk kyou_neutral sayori_happy",
            "SayoriWalk kyou_neutral sayori_neutral",
            "SayoriWalk kyou_neutral sayori_smile",
        ],
        "hiroko shoe": [
                "HirokoShoe pose1",
                "HirokoShoe pose2",
                "HirokoShoe pose3 neutral",
                "HirokoShoe pose3 happy",
        ],
        "hiroko yawn day": [
            "HirokoYawn day n_listening h_sitting h_neutral",
            "HirokoYawn day n_listening h_sitting h_frown",
            "HirokoYawn day n_listening h_yawning h_sleepy",
            "HirokoYawn day n_concerned h_yawning h_angry",
            "HirokoYawn day n_listening h_sitting h_frown_left",
            "HirokoYawn day n_concerned h_sitting h_frown_left",
        ],
        "classroomlunch5 1":[
            "ClassroomLunch boy1 boy2_missing hiroko h_laugh n_armup n_smile_left sayori s_smile_hiroko",
            #Hiroko Ticklish Hands version
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_smile_sayori n_armup n_smile_right glasses sayori s_smile_nozomi",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_worried_nozomi n_armup n_smile_right glasses sayori s_smile_nozomi",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_worried_nozomi n_armup n_smile_left glasses sayori s_neutral_hiroko",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_sad_nozomi n_armup n_smile_left glasses sayori s_neutral_hiroko",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_worried_nozomi n_armup n_smile_left glasses sayori s_neutral_hiroko",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_worried_nozomi n_folded n_neutral_left glasses sayori s_neutral_hiroko",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_sad_nozomi n_folded n_smile_left glasses sayori s_neutral_hiroko",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_sad_nozomi n_folded n_smile_left glasses sayori s_concerned_nozomi",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_sad_nozomi n_folded n_frown_left glasses sayori s_concerned_nozomi",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_neutral_nozomi n_folded n_frown_left glasses sayori s_concerned_nozomi",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_sad_nozomi n_armup n_thinking glasses sayori s_concerned_nozomi",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_uncomfortable hiroko h_grin_nozomi n_armup n_thinking glasses sayori s_concerned_nozomi",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_furious hiroko h_grin_nozomi n_armup n_thinking glasses sayori s_concerned_nozomi",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_furious hiroko h_grin_nozomi n_armup n_nervous_left glasses sayori s_neutral_hiroko",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_furious hiroko h_worried_nozomi n_armup n_nervous_left glasses sayori s_neutral_hiroko",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_furious hiroko h_grin_nozomi n_folded n_thinking glasses sayori s_neutral_hiroko",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_furious hiroko h_grin_nozomi n_folded n_thinking glasses sayori s_pout",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.classroomlunch5_2_unlock", "ClassroomLunch boy1 boy2_missing k_nervous hiroko h_grin_nozomi n_folded n_smile_left glasses sayori s_neutral_hiroko",
                "True", "cg locked.png"
            ),
        ],
        "classroom lunch2 sleeper": [
            "ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_smile",
            "ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_neutral",
            "ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_frown_left",
            "ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko2 h_growl",
            "ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko2 h_growl",
            "ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko2 h_frown",
            "ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_right hiroko2 h_frown",
            "ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_right hiroko2 h_neutral_left",
            "ClassroomLunch2 kyou nozomi1 n_concerned s_neutral_right hiroko1 h_worried_left",
            "ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko1 h_worried_left",
            "ClassroomLunch2 kyou nozomi1 n_surprised s_worried hiroko1 h_frown_left",
            "ClassroomLunch2 kyou nozomi1 n_frown_right s_worried hiroko1 h_frown_left",
            "ClassroomLunch2 kyou nozomi1 n_frown_right s_worried hiroko1 h_worried_left",
            "ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_worried_left",
            "ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_worried",
            "ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_worried h_blush",
            "ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_sad h_blush",
            "ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_sad h_blush",
            "ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi1 n_neutral_right s_neutral_right hiroko1 h_neutral_left",
            "ClassroomLunch2 kyou nozomi1 n_curious s_neutral hiroko1 h_neutral",
            "ClassroomLunch2 kyou nozomi1 n_curious s_neutral hiroko1 h_smirk",
            "ClassroomLunch2 kyou nozomi1 n_frown_right s_angry hiroko1 h_smirk",
            "ClassroomLunch2 kyou nozomi1 n_frown_right s_angry hiroko1 h_worried_left",
            "ClassroomLunch2 kyou nozomi1 n_pout s_frown hiroko1 h_worried_left",
            "ClassroomLunch2 kyou nozomi1 n_pout s_frown hiroko1 h_sad",
            "ClassroomLunch2 kyou nozomi1 n_frown_right s_frown hiroko1 h_sad",
            "ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_sad",
            "ClassroomLunch2 kyou nozomi1 n_frown_right s_irritated hiroko1 h_worried",
            "ClassroomLunch2 kyou nozomi1 n_concerned s_neutral hiroko1 h_worried",
            "ClassroomLunch2 kyou nozomi1 n_neutral s_neutral hiroko1 h_neutral",
            "ClassroomLunch2 kyou nozomi1 n_smile s_neutral hiroko1 h_neutral",
            "ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_neutral",
            "ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_smirk_left",
            "ClassroomLunch2 kyou nozomi2 n_neutral_side s_smile_right hiroko1 h_smirk_left",
            "ClassroomLunch2 kyou nozomi2 n_smile_side s_smile_right hiroko1 h_smirk_left",
            "ClassroomLunch2 kyou nozomi2 n_smile_side s_neutral_left hiroko1 h_smirk_left",
            "ClassroomLunch2 kyou nozomi2 n_smile_side s_sleep hiroko1 h_smirk_left",
            "ClassroomLunch2 kyou nozomi2 n_concerned_side s_sleep hiroko1 h_worried_left",
            "ClassroomLunch2 kyou nozomi2 n_concerned_side s_smile hiroko1 h_worried_left",
            "ClassroomLunch2 kyou nozomi1 n_neutral s_smile hiroko1 h_neutral",
            "ClassroomLunch2 kyou nozomi1 n_smile s_smile hiroko1 h_neutral",
            "ClassroomLunch2 kyou nozomi1 n_concerned s_smile hiroko1 h_neutral_left",
        ],
        "rooftop devotion":[
            overlap_images("cg rooftop day", "RoofHiroko infatuated smile blush", "RoofSayori leanforward smile blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated happy blush", "RoofSayori leanforward smile blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward smile blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward awe blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated happy blush", "RoofSayori leanforward smirk blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated smile blush", "RoofSayori leanforward smirk blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated smile blush", "RoofSayori leanforward frown blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward frown blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward determined blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated concerned blush", "RoofSayori leanforward frown blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated determined blush", "RoofSayori leanforward frown blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated determined blush", "RoofSayori leanforward determined blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated confused blush", "RoofSayori leanforward determined blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated confused blush", "RoofSayori leanforward determined_side blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated sad blush", "RoofSayori leanforward frown blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward surprised blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated awe blush", "RoofSayori leanforward cry blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated concerned blush", "RoofSayori leanforward cry blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated sad blush", "RoofSayori leanforward cry blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated sad blush", "RoofSayori leanforward angrycry blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated concerned blush", "RoofSayori leanforward angrycry blush"),
            overlap_images("cg rooftop day", "RoofHiroko infatuated determined blush", "RoofSayori leanforward determined blush"),
        ],
        "rooftop robot":[
            "RoofRobot h_neutral n_sleepy",
            "RoofRobot h_neutral_left n_neutral",
            "RoofRobot h_smile_left n_neutral",
            "RoofRobot h_smile_left n_confused",
            "RoofRobot h_neutral n_sleepy sayori s_stern",
            "RoofRobot h_neutral n_confused_right sayori s_stern_left",
            "RoofRobot h_neutral_right n_surprised sayori s_stern_left",
            "RoofRobot h_neutral_right n_surprised sayori s_concerned_left",
            "RoofRobot h_neutral_right n_confused_right sayori s_concerned_left",
            "RoofRobot h_neutral_right n_confused_right sayori s_concerned",
            "RoofRobot h_neutral_right n_confused_right sayori s_stern_left",
            "RoofRobot h_neutral_right n_sleepy sayori s_stern_left",
            "RoofRobot h_neutral_right n_sleepy sayori s_angry_left",
            "RoofRobot h_smile n_sleepy sayori s_angry_left",
            "RoofRobot h_smile n_sleepy sayori s_concerned_left",
            "RoofRobot h_neutral n_sleepy sayori s_concerned_left",
            "RoofRobot h_neutral n_sleepy sayori s_angry",
            "RoofRobot h_neutral n_sleepy sayori s_stern_left",
            "RoofRobot h_neutral_left n_neutral sayori s_stern_left",
            "RoofRobot h_smile n_neutral sayori s_stern_left",
            "RoofRobot h_smile n_confused_right sayori s_angry_left",
            "RoofRobot h_neutral n_confused_right sayori s_angry",
            "RoofRobot h_neutral n_neutral sayori s_angry",
            "RoofRobot h_neutral n_neutral sayori s_irritated",
            "RoofRobot h_neutral n_sleepy sayori s_concerned",
            "RoofRobot h_neutral n_neutral sayori s_concerned_left",
            "RoofRobot h_neutral n_smile_left sayori s_concerned_left",
            "RoofRobot h_neutral n_smile_right sayori s_concerned_left",
            "RoofRobot h_neutral n_smile_right sayori s_concerned",
            "RoofRobot h_neutral n_sigh",
            "RoofRobot h_neutral n_neutral",
            "RoofRobot h_neutral n_smile_left",
        ],
        #Page 9
        "rooftop robot  girlfriend": [
            "RoofRobotGF nozomi1 k_surprised k_blush n_happy n_blush1 h_neutral",
            "RoofRobotGF nozomi1 k_surprised k_blush n_smile1 n_blush1 h_neutral",
            "RoofRobotGF nozomi1 k_smile k_blush n_smile1 n_blush1 h_neutral",
            "RoofRobotGF nozomi1 k_smile k_blush n_confused1 n_blush1 h_neutral",
            "RoofRobotGF nozomi1 k_smile n_confused1 n_blush1 h_neutral",
            "RoofRobotGF nozomi1 k_smile n_confused1 h_neutral",
            "RoofRobotGF nozomi1 sayori s_frown k_surprised n_confused1 h_neutral",
            "RoofRobotGF nozomi2 sayori s_furious k_surprised n_surprised n_blush2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_worried k_surprised n_surprised n_blush2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_worried k_surprised n_confused2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_worried k_neutral n_confused2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_worried k_neutral n_neutral2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_frown k_neutral n_neutral2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_frown k_neutral n_confused2 n_blush2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_growl k_neutral n_confused2 n_blush2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_growl k_neutral n_confused2 h_smile",
            "RoofRobotGF nozomi2 sayori s_worried k_neutral n_confused2 h_smile",
            "RoofRobotGF nozomi2 sayori s_worried k_sigh n_confused2 h_smile",
            "RoofRobotGF nozomi2 sayori s_growl k_sigh n_confused2 h_smile",
            "RoofRobotGF nozomi2 sayori s_frown k_neutral n_confused2 h_smile",
            "RoofRobotGF nozomi2 sayori s_frown k_neutral n_neutral_left h_neutral_left",
            "RoofRobotGF nozomi2 sayori s_frown k_neutral n_neutral2 h_smile",
            "RoofRobotGF nozomi2 sayori s_growl k_neutral n_neutral2 h_smile",
            "RoofRobotGF nozomi2 sayori s_furious k_neutral n_neutral2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_furious k_smirk n_neutral2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_irritated k_smirk n_neutral2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_worried k_neutral n_neutral2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_frown k_neutral n_confused2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_frown k_smile n_neutral_left h_neutral",
            "RoofRobotGF nozomi2 sayori s_frown k_smile n_smile_left h_neutral",
            "RoofRobotGF nozomi2 sayori s_frown k_smile n_smile2 h_neutral",
            "RoofRobotGF nozomi2 sayori s_worried k_smile n_smile2 h_neutral",
            "RoofRobotGF nozomi2 k_neutral n_confused2 h_neutral",
            "RoofRobotGF nozomi1 k_neutral n_sigh h_neutral",
            "RoofRobotGF nozomi1 k_sigh n_neutral1 h_neutral",
            "RoofRobotGF nozomi1 k_confused n_smile1 h_neutral",
            "RoofRobotGF nozomi2 k_confused n_neutral_right h_neutral",
            "RoofRobotGF nozomi2 k_smile n_neutral_right h_neutral_left",
            "RoofRobotGF nozomi2 k_smile n_neutral_right h_smile_left",
            "RoofRobotGF nozomi2 k_confused n_neutral_right h_neutral",
            "RoofRobotGF nozomi2 k_confused n_neutral_left h_neutral",
            "RoofRobotGF nozomi2 k_sigh n_neutral_left h_neutral",
            "RoofRobotGF nozomi1 k_sigh n_sigh h_neutral",
            "RoofRobotGF nozomi1 k_smile n_sigh h_neutral",
            "RoofRobotGF nozomi1 k_smile n_smile1 h_neutral",
        ],
        "hiroko yawn eve": [
            "HirokoYawn eve e_neutral n_listening h_sitting h_sleepy",
            "HirokoYawn eve e_neutral n_concerned h_sitting h_yawn",
            "HirokoYawn eve e_curious n_shocked h_sleeping h_sleep",
            "HirokoYawn eve e_curious n_shocked h_sleeping h_waking",
            "HirokoYawn eve e_curious n_shocked h_sitting_blush h_panic",
            "HirokoYawn eve e_laugh n_shocked h_sitting_blush h_panic",
            "HirokoYawn eve e_laugh n_shocked h_sitting_blush h_sorry",
            "HirokoYawn eve e_laugh n_shocked h_sitting_blush h_sleepy",
            "HirokoYawn eve e_laugh n_shocked h_sitting_blush h_yawn",
            "HirokoYawn eve e_laugh n_shocked h_sleeping_blush h_sleep",
            "HirokoYawn eve e_laugh n_shocked h_sleeping_blush h_waking",
            "HirokoYawn eve e_laugh n_shocked h_sleeping_blush h_sleeptalk",
            "HirokoYawn eve e_laugh n_shocked h_sleeping h_sleep",
        ],
        "hiroko tennis kiss single image": [
            #This one is a single image
        ],
        "nozomi collapse single image": [
            #This one is a single image
        ],
        "nozomi interrogation":[
        "NozomiInterro nozomi1 n_neutral1 kyou2 k_disgust2",
        "NozomiInterro nozomi1 n_frown1 kyou1 k_frown1",
        "NozomiInterro nozomi1 n_annoyed1 kyou1 k_frown1",
        "NozomiInterro nozomi1 n_neutral1 kyou1 k_frown1",
        "NozomiInterro nozomi1 n_frown1 kyou1 k_growl1",
        "NozomiInterro nozomi1 n_neutral1 kyou2 k_disgust2",
        "NozomiInterro nozomi1 n_annoyed1 kyou2 k_disgust2",        
        "NozomiInterro nozomi1 n_smile1 kyou1 k_frown1",
        "NozomiInterro nozomi1 n_smile1 kyou1 k_angry1",
        "NozomiInterro nozomi1 n_happy1 kyou1 k_angry1",
        "NozomiInterro nozomi1 n_smile1 kyou1 k_growl1",
        "NozomiInterro nozomi1 n_smile1 kyou1 k_confused1",
        "NozomiInterro nozomi1 n_neutral1 kyou2 k_concerned2",
        "NozomiInterro nozomi1 n_confused1 kyou2 k_concerned2",
        "NozomiInterro nozomi1 n_confused1 kyou2 k_sigh2",
        "NozomiInterro nozomi1 n_neutral1 kyou2 k_sigh2",
        "NozomiInterro nozomi1 n_neutral1 kyou2 k_smile2",
        "NozomiInterro nozomi1 n_smile1 kyou2 k_smile2",
        "NozomiInterro nozomi1 n_smile1 kyou2 k_disgust2",
        "NozomiInterro nozomi1 n_surprised1 kyou3 k_angry3",
        "NozomiInterro nozomi1 n_confused1 kyou1 k_frown1",
        "NozomiInterro nozomi1 n_surprised1 kyou1 k_growl1",
        "NozomiInterro nozomi1 n_surprised1 kyou1 k_angry1",
        "NozomiInterro nozomi1 n_confused1 kyou2 k_disgust2",
        "NozomiInterro nozomi1 n_frown1 kyou2 k_disgust2",
        "NozomiInterro nozomi1 n_frown1 kyou2 k_concerned2",
        "NozomiInterro nozomi1 n_neutral1 kyou2 k_concerned2",
        "NozomiInterro nozomi1 n_frown1 kyou2 k_sigh2",
        "NozomiInterro nozomi1 n_neutral1 kyou2 k_smile2",
        "NozomiInterro nozomi1 n_happy1 kyou2 k_smile2",
        "NozomiInterro nozomi1 n_annoyed1 kyou2 k_smile2",
        "NozomiInterro nozomi2 n_shocked2 kyou3 k_angry3",
        "NozomiInterro nozomi2 n_frown2 kyou3 k_growl3",
        "NozomiInterro nozomi1 n_angry1 kyou1 k_frown1",
        "NozomiInterro nozomi2 n_worried2 kyou3 k_angry3",
        "NozomiInterro nozomi2 n_neutral2 kyou3 k_angry3",
        "NozomiInterro nozomi2 n_neutral2 kyou3 k_growl3",
        "NozomiInterro nozomi2 n_frown2 kyou3 k_growl3",
        "NozomiInterro nozomi2 n_nervous2 n_blush2 kyou3 k_growl3",
        "NozomiInterro nozomi2 n_worried_l2 n_blush2 kyou3 k_growl3",
        "NozomiInterro nozomi2 n_worried_l2 n_blush2 kyou1 k_smirk1",
        "NozomiInterro nozomi2 n_nervous2 n_blush2 kyou1 k_smirk1",
        "NozomiInterro nozomi2 n_nervous2 n_blush2 kyou1 k_confused1",
        "NozomiInterro nozomi2 n_sigh2 n_blush2 kyou1 k_confused1",
        "NozomiInterro nozomi2 n_laugh2 n_blush2 kyou1 k_confused1",
        "NozomiInterro nozomi2 n_smile2 kyou2 k_neutral2",
        "NozomiInterro nozomi2 n_smile2 kyou2 k_concerned2",
        "NozomiInterro nozomi2 n_smile2 kyou2 k_disgust2",
        "NozomiInterro nozomi1 n_happy1 kyou2 k_disgust2",
        "NozomiInterro nozomi1 n_smile1 kyou2 k_concerned2",
        "NozomiInterro nozomi2 n_laugh2 kyou2 k_concerned2",
        "NozomiInterro nozomi2 n_laugh2 kyou2 k_disgust2",
        "NozomiInterro nozomi1 n_smirk1 kyou2 k_disgust2",
        "NozomiInterro nozomi1 n_smirk1 kyou2 k_smile2",
        "NozomiInterro nozomi1 n_smile1 kyou2 k_neutral2",
        "NozomiInterro nozomi1 n_happy1 kyou2 k_neutral2",
        "NozomiInterro nozomi1 n_happy1 kyou1 k_confused1",
        "NozomiInterro nozomi2 n_worried_l2 kyou1 k_confused1",
        "NozomiInterro nozomi2 n_nervous2 kyou1 k_confused1",
        "NozomiInterro nozomi2 n_sigh2 kyou1 k_confused1",
        "NozomiInterro nozomi2 n_sigh2 kyou1 k_neutral1",
        "NozomiInterro nozomi2 n_nervous2 kyou1 k_neutral1",
        "NozomiInterro nozomi2 n_laugh2 n_blush2 kyou1 k_neutral1",
        ],
        "trance stop end":[
        "TranceStopEnd unsure",
        "TranceStopEnd smile",
        "TranceStopEnd happy",
        "TranceStopEnd laugh",
        ],
        "nozomi robot programming":[
            "NozomiRobotProgramming open",
            "NozomiRobotProgramming open kyou",
            "NozomiRobotProgramming closed kyou",
        ],
        "study room nozomi": [
            overlap_images("cg study room eve", "NozomiHypno standing stern"),
            overlap_images("cg study room eve", "NozomiHypno standing lookup"),
            overlap_images("cg study room eve", "NozomiHypno standing drowsy"),
            overlap_images("cg study room eve", "NozomiHypno drooping sleep"),
        ],
        "study room hypno nozomi":[
            "StudyRoomHypno sayori1 s_neutral_right nozomi1 n_sleep",
            "StudyRoomHypno sayori1 s_neutral nozomi1 n_sleep",
            "StudyRoomHypno sayori1 s_surprised nozomi1 n_sleep",
            "StudyRoomHypno sayori1 s_smirk nozomi1 n_sleep",
            "StudyRoomHypno sayori1 s_neutral_right nozomi1 n_sleeptalk",
            "StudyRoomHypno sayori1 s_stern nozomi1 n_sleep",
            "StudyRoomHypno sayori1 s_quizzical nozomi1 n_sleep",
            "StudyRoomHypno sayori1 s_stern_right nozomi1 n_sleep",
            "StudyRoomHypno sayori1 s_thoughtful nozomi1 n_sleep",
            "StudyRoomHypno sayori1 s_smile nozomi1 n_sleep",
            "StudyRoomHypno sayori1 s_neutral_right nozomi1 n_sleepysmile",
            "StudyRoomHypno sayori1 s_neutral_right nozomi1 n_sleepysmile n_blush_low",
            "StudyRoomHypno sayori1 s_neutral_right nozomi2 n_startled n_blush_high",
            "StudyRoomHypno sayori1 s_smile_right nozomi2 n_startled n_blush_high",
            "StudyRoomHypno sayori1 s_smile_right nozomi2 n_smile_left",
            "StudyRoomHypno sayori1 s_neutral nozomi2 n_smile",
            "StudyRoomHypno sayori1 s_neutral nozomi2 n_neutral",
            "StudyRoomHypno sayori1 s_neutral nozomi2 n_neutral_left",
            "StudyRoomHypno sayori1 s_smile_right nozomi2 n_neutral_left",
        ],
        "nozomi chocolate":[
            "NozomiChocolate arm1 choc1 contemplating",
            "NozomiChocolate arm1 choc1 disgusted",
            "NozomiChocolate arm1 choc1 chewing_disgusted",
            "NozomiChocolate arm1 choc1 confused",
            "NozomiChocolate arm1 choc1 confused_down",
            "NozomiChocolate arm2 choc1 confused_down",
            "NozomiChocolate arm2 choc1 confused",
            "NozomiChocolate arm1 choc1 determined",
            "NozomiChocolate arm1 choc2 chewing_disgusted",
            "NozomiChocolate arm1 choc2 disgusted",
            "NozomiChocolate arm1 choc2 confused",
            "NozomiChocolate arm1 choc2 blank",
            "NozomiChocolate arm1 choc2 chewing",
            "NozomiChocolate arm1 choc2 happy blush",
            "NozomiChocolate arm2 choc2 happy blush",
            "NozomiChocolate arm2 choc2 laugh blush",
            "NozomiChocolate arm2 choc2 grin blush",
            "NozomiChocolate arm2 choc2 confused blush",
        ],
        #Page 10
        "akiko breakfast": [
            "AkikoBreakfast smile",
            "AkikoBreakfast akiko_up smile",
            "AkikoBreakfast akiko_up smirk",
            "AkikoBreakfast akiko_down worried",
            "AkikoBreakfast akiko_up happy blush",
            "AkikoBreakfast akiko_up embarrassed blush",
            "AkikoBreakfast akiko_up smile blush",
            "AkikoBreakfast akiko_up happy",
            "AkikoBreakfast akiko_down smile_side",
            "AkikoBreakfast akiko_down smirk",
            "AkikoBreakfast akiko_down laugh",
            "AkikoBreakfast akiko_down annoyed",
            "AkikoBreakfast akiko_down smile",
            "AkikoBreakfast akiko_up neutral_side",
            "AkikoBreakfast akiko_up quizzical",
            "AkikoBreakfast akiko_up neutral",
            "AkikoBreakfast akiko_down neutral_closed",
            "AkikoBreakfast akiko_down annoyed",
            "AkikoBreakfast akiko_down surprised",
            "AkikoBreakfast akiko_down neutral",
            "AkikoBreakfast akiko_down smile",
            "AkikoBreakfast akiko_down happy",
            "AkikoBreakfast akiko_up worried_side",
            "AkikoBreakfast akiko_up neutral",
            "AkikoBreakfast akiko_up surprised",
            "AkikoBreakfast akiko_down quizzical",
            "AkikoBreakfast akiko_down surprised",
            "AkikoBreakfast akiko_down sigh",
            "AkikoBreakfast akiko_down neutral",
            "AkikoBreakfast akiko_down neutral_closed",
            "AkikoBreakfast akiko_up worried",
            "AkikoBreakfast akiko_up worried_side",
            "AkikoBreakfast akiko_down worried",
            "AkikoBreakfast akiko_down worried pancakes2",
            "AkikoBreakfast akiko_up sigh pancakes2",
            "AkikoBreakfast akiko_up neutral pancakes2",
            "AkikoBreakfast akiko_up annoyed pancakes2",
            "AkikoBreakfast akiko_down embarrassed pancakes2",
            "AkikoBreakfast akiko_down worried_side blush pancakes2",
            "AkikoBreakfast akiko_down neutral_closed pancakes2",
            "AkikoBreakfast akiko_up worried pancakes2",
            "AkikoBreakfast akiko_up sigh pancakes2",
            "AkikoBreakfast akiko_up neutral pancakes2",
            "AkikoBreakfast akiko_down surprised pancakes2",
            "AkikoBreakfast akiko_down worried pancakes2",
            "AkikoBreakfast akiko_down worried_side pancakes2",
            "AkikoBreakfast akiko_down sigh pancakes2",
            "AkikoBreakfast akiko_up neutral_side pancakes2",
            "AkikoBreakfast akiko_up smile pancakes2",
            "AkikoBreakfast akiko_down smile pancakes2",
            "AkikoBreakfast akiko_up quizzical pancakes2",
            "AkikoBreakfast akiko_up smirk pancakes2",
            "AkikoBreakfast akiko_up worried_side blush pancakes2",
            "AkikoBreakfast akiko_up happy pancakes2",
            "AkikoBreakfast akiko_up smile pancakes2",
            "AkikoBreakfast akiko_down smile pancakes2",
            "AkikoBreakfast akiko_down surprised pancakes2",
            "AkikoBreakfast akiko_up quizzical pancakes2",
            "AkikoBreakfast akiko_up embarrassed blush pancakes2",
            "AkikoBreakfast akiko_up happy blush pancakes2",
            "AkikoBreakfast akiko_down smile pancakes2",
            "AkikoBreakfast akiko_down neutral_side pancakes2",
            "AkikoBreakfast akiko_down quizzical pancakes2",
            "AkikoBreakfast akiko_down embarrassed blush pancakes2",
            "AkikoBreakfast akiko_down smirk blush pancakes2",
            "AkikoBreakfast akiko_down laugh blush pancakes2",
            "AkikoBreakfast akiko_up happy blush pancakes2",
        ],
        "hiroko racket": [
            "Hiroko Racket k_neutral r_neutral h_arm1 h_head1 h_sad",
            "Hiroko Racket k_neutral r_neutral h_arm1 h_head2 h_stern",
            "Hiroko Racket k_regretful r_neutral h_arm1 h_head2 h_stern",
            "Hiroko Racket k_annoyed r_neutral h_arm1 h_head2 h_stern",
            "Hiroko Racket k_annoyed r_grin h_arm1 h_head2 h_stern",
            "Hiroko Racket k_annoyed r_grin h_arm2 h_head2 h_angry",
            "Hiroko Racket k_smile r_grin h_arm2 h_head2 h_angry",
            "Hiroko Racket k_smile r_grin h_arm2 h_head2 h_neutral2",
            "Hiroko Racket k_smile r_smile h_arm2 h_head1 h_neutral1",
            "Hiroko Racket k_neutral r_smile h_arm2 h_head1 h_neutral1",
            "Hiroko Racket k_neutral r_neutral h_arm2 h_head2 h_neutral2",
            "Hiroko Racket k_smile r_neutral h_arm2 h_head2 h_neutral2",
            "Hiroko Racket k_smile r_grin h_arm2 h_head2 h_smile",
        ],
        "k room akiko 1": [
            overlap_images("cg k room day", "AkikoHypno upright smile"),
            overlap_images("cg k room day", "AkikoHypno upright happy"),
            overlap_images("cg k room day", "AkikoHypno upright neutral"),
            overlap_images("cg k room day", "AkikoHypno upright surprised"),
            overlap_images("cg k room day", "AkikoHypno upright neutral_up"),
            overlap_images("cg k room day", "AkikoHypno upright neutral_up_talk"),
            overlap_images("cg k room day", "AkikoHypno upright say_ee"),
            overlap_images("cg k room day", "AkikoHypno upright say_oh"),
            overlap_images("cg k room day", "AkikoHypno upright say_ah"),
            overlap_images("cg k room day", "AkikoHypno upright confused"),
            overlap_images("cg k room day", "AkikoHypno upright sad"),
            overlap_images("cg k room day", "AkikoHypno upright sleep noglasses"),
            overlap_images("cg k room day", "AkikoHypno upright irritated noglasses"),
            overlap_images("cg k room day", "AkikoHypno upright frown glasses"),
        ] + unlockable_image_list("persistent.k_room_akiko_2_unlock", [
            overlap_images("cg k room day", "AkikoHypno upright surprised_up"),
            overlap_images("cg k room day", "AkikoHypno upright sleepy"),
            overlap_images("cg k room day", "AkikoHypno upright sleep"),
            overlap_images("cg k room day", "AkikoHypno drooping sleep"),
            overlap_images("cg k room day", "AkikoHypno drooping sleeptalk"),
            overlap_images("cg k room day", "AkikoHypno drooping sleepy"),
        ]) + unlockable_image_list("persistent.k_room_akiko_3_unlock", [
            overlap_images("cg k room day", "AkikoHypno upright sleepy blush"),
            overlap_images("cg k room day", "AkikoHypno upright happy blush"),
            overlap_images("cg k room day", "AkikoHypno upright smile blush"),
        ]),
        "redemption phone day": [
            "RedemptionPhoneDay quizzical_up_sp glasses_sp kyou_phone",
            "RedemptionPhoneDay surprised_sp glasses_sp kyou_phone",
            "RedemptionPhoneDay quizzical_sp glasses_sp kyou_phone",
            "RedemptionPhoneDay tired_sp glasses_sp kyou_phone",
            "RedemptionPhoneDay blanktalk_sp glasses_sp kyou_phone",
            "RedemptionPhoneDay blank_sp glasses_sp kyou_phone",
            "RedemptionPhoneDay blank glasses kyou",
            "RedemptionPhoneDay blanktalk glasses kyou",
            "RedemptionPhoneDay blank glasses kyou",
            "RedemptionPhoneDay surprised glasses kyou",
            "RedemptionPhoneDay tired glasses kyou",
            "RedemptionPhoneDay quizzical_up glasses kyou",
        ],
        "sayori hypno day": [
            overlap_images("cg k room day", "SayoriHypnoDay smile"),
            overlap_images("cg k room day", "SayoriHypnoDay neutral"),
            overlap_images("cg k room day", "SayoriHypnoDay sad"),
            overlap_images("cg k room day", "SayoriHypnoDay neutral_closed"),
            overlap_images("cg k room day", "SayoriHypnoDay neutral"),
            overlap_images("cg k room day", "SayoriHypnoDay stern"),
            overlap_images("cg k room day", "SayoriHypnoDay looking"),
            overlap_images("cg k room day", "SayoriHypnoDay drowsy"),
            overlap_images("cg k room day", "SayoriHypnoDay head_down sleep"),
            overlap_images("cg k room day", "SayoriHypnoDay head_down sleeptalk"),
            overlap_images("cg k room day", "SayoriHypnoDay head_up drowsytalk"),
            overlap_images("cg k room day", "SayoriHypnoDay head_up happy"),
            overlap_images("cg k room day", "SayoriHypnoDay angry"),
        ],
        "nozomi cola": [
            "NozomiCola nozomi1 dazed cola",
            "NozomiCola nozomi1 frown_side cola",
            "NozomiCola nozomi1 frown cola",
            "NozomiCola nozomi1 pout cola",
            "NozomiCola nozomi2 concerned cola",
            "NozomiCola nozomi2 surprised cola",
            "NozomiCola nozomi2 uncomfortable cola",
            "NozomiCola nozomi2 frown_side cola",
            "NozomiCola nozomi4",
            "NozomiCola nozomi1 sigh cola_open",
            "NozomiCola nozomi1 surprised cola_open",
            "NozomiCola nozomi1 nervous_side cola_open",
            "NozomiCola nozomi1 mad blush cola_open",
            "NozomiCola nozomi1 frown blush cola_open",
            "NozomiCola nozomi1 frown_side blush cola_open",
            "NozomiCola nozomi1 sigh blush cola_open",
            "NozomiCola nozomi1 concerned blush cola_open",
            "NozomiCola nozomi1 sigh cola_open",
            "NozomiCola nozomi1 dazed cola_open",
            "NozomiCola nozomi1 neutral cola_open",
            "NozomiCola nozomi2 neutral cola_open",
            "NozomiCola nozomi2 neutral sigh cola_open",
            "NozomiCola nozomi4",
            "NozomiCola nozomi3 disgusted",
            "NozomiCola nozomi3 frown_side",
            "NozomiCola nozomi3 smirk",
            "NozomiCola nozomi3 happy",
            "NozomiCola nozomi3 smile",
            "NozomiCola nozomi3 pout",
            "NozomiCola nozomi3 uncomfortable",
            "NozomiCola nozomi4",
            "NozomiCola nozomi3 dazed",
            "NozomiCola nozomi3 concerned",
            "NozomiCola nozomi3 neutral",
            "NozomiCola nozomi3 nervous_side", 
            "NozomiCola nozomi2 concerned cola_open",
        ],
        "zombie bedroom 1 1": [
            "NozomiBedroom1 neutral bruise arm_up shadow",
            "NozomiBedroom1 frown bruise arm_up shadow",
            "NozomiBedroom1 sleep bruise arm_up shadow",
            "NozomiBedroom1 concerned bruise arm_up shadow",
            "NozomiBedroom1 sigh bruise arm_up shadow",
            "NozomiBedroom1 pout bruise blush arm_up shadow",
            "NozomiBedroom1 concerned_side bruise arm_down shadow",
            "NozomiBedroom1 pout bruise arm_down shadow",
            "NozomiBedroom1 concerned_side bruise arm_up shadow",
            "NozomiBedroom1 surprised bruise arm_down shadow",
            "NozomiBedroom1 afraid bruise arm_down shadow",
            "NozomiBedroom1 frown_side bruise arm_down shadow",
            "NozomiBedroom1 sleep bruise arm_down shadow",
            "NozomiBedroom1 frown bruise arm_down shadow",
            "NozomiBedroom1 concerned bruise arm_down shadow",
            "NozomiBedroom1 sigh bruise arm_down shadow",
            "NozomiBedroom1 afraid bruise arm_down shadow",
            "NozomiBedroom1 neutral bruise arm_down shadow",
            "NozomiBedroom1 neutral_side bruise arm_down shadow",
            ConditionSwitch(
                "persistent.zombie_bedroom_1_2_unlock", "NozomiBedroom1 neutral_light bruise arm_down shadow",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.zombie_bedroom_1_2_unlock", "NozomiBedroom1 dazed_closed bruise arm_down shadow",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.zombie_bedroom_1_2_unlock", "NozomiBedroom1 dazed_light bruise arm_down shadow",
                "True", "cg locked.png"
            ),            
            ConditionSwitch(
                "persistent.zombie_bedroom_1_2_unlock", "NozomiBedroom1 dazed_open bruise arm_down shadow",
                "True", "cg locked.png"
            ),  
            ConditionSwitch(
                "persistent.zombie_bedroom_1_2_unlock", "NozomiBedroom1 smile bruise arm_down shadow",
                "True", "cg locked.png"
            ), 
            ConditionSwitch(
                "persistent.zombie_bedroom_1_3_unlock", "NozomiBedroom1 pout bruise blush arm_down shadow",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.zombie_bedroom_1_3_unlock", "NozomiBedroom1 frown_side bruise blush arm_down shadow",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.zombie_bedroom_1_3_unlock", "NozomiBedroom1 sigh bruise blush arm_down shadow",
                "True", "cg locked.png"
            ),
            ConditionSwitch(
                "persistent.zombie_bedroom_1_3_unlock", "NozomiBedroom1 concerned_side bruise blush arm_down shadow",
                "True", "cg locked.png"
            ),
        ],
        "zombie bedroom 2": [
            "NozomiBedroom2 a_concerned nozomi1 n_anxious blush",
            "NozomiBedroom2 a_concerned nozomi2 n_confused blush",
            "NozomiBedroom2 a_surprised nozomi3 n_sleep",
            "NozomiBedroom2 a_concerned_up nozomi3 n_sleep",
            "NozomiBedroom2 a_neutral nozomi3 n_sleeptalk",
            "NozomiBedroom2 a_concerned nozomi1 n_anxious",
            "NozomiBedroom2 a_concerned nozomi1 n_smile blush",
            "NozomiBedroom2 a_surprised nozomi1 n_surprised blush",
            "NozomiBedroom2 a_surprised nozomi1 n_sigh blush",
            "NozomiBedroom2 a_concerned nozomi1 n_sigh blush",
            "NozomiBedroom2 a_concerned nozomi1 n_annoyed blush",
            "NozomiBedroom2 a_laugh nozomi1 n_annoyed blush",
            "NozomiBedroom2 a_smile_up nozomi1 n_anxious blush",
            "NozomiBedroom2 a_smile_up nozomi1 n_sigh blush",
            "NozomiBedroom2 a_smile nozomi1 n_sigh blush",
            "NozomiBedroom2 a_laugh nozomi1 n_sigh blush",
            "NozomiBedroom2 a_laugh nozomi1 n_anxious blush",
            "NozomiBedroom2 a_smile nozomi1 n_anxious blush",
            "NozomiBedroom2 a_smile nozomi1 n_smile_left blush",
        ],
        "nozomi boardgame": [
            "NozomiBoardgame smile",
            "NozomiBoardgame pout",
            "NozomiBoardgame blank",
            "NozomiBoardgame laugh",
        ],
        "nozomi boardgame2": [
            "NozomiBoardgame2 hands_cards smug",
            "NozomiBoardgame2 hands_cards smirk",
            "NozomiBoardgame2 hands_cards laugh",
            "NozomiBoardgame2 hands_cards smile",
            "NozomiBoardgame2 hands_cards confused",
            "NozomiBoardgame2 hands_cards blank",
            "NozomiBoardgame2 hands_cards surprised blush",
            "NozomiBoardgame2 hands_cards confused blush",
            "NozomiBoardgame2 hands_cards annoyed blush",
            "NozomiBoardgame2 hands_cards neutral",
            "NozomiBoardgame2 hands_cards sigh",
            "NozomiBoardgame2 hands_cards frown",
            "NozomiBoardgame2 hands_cards concerned",
            "NozomiBoardgame2 hands_cards angry",
            "NozomiBoardgame2 hands_down smirk",
            "NozomiBoardgame2 hands_down smile",
            "NozomiBoardgame2 hands_down laugh",
            "NozomiBoardgame2 hands_up smug",
            "NozomiBoardgame2 hands_up surprised",
            "NozomiBoardgame2 hands_up angry",
            "NozomiBoardgame2 hands_down sigh",
            "NozomiBoardgame2 hands_down annoyed",
            "NozomiBoardgame2 hands_up sigh",
            "NozomiBoardgame2 hands_up smile",
            "NozomiBoardgame2 hands_up confused",
            "NozomiBoardgame2 hands_up neutral",
            "NozomiBoardgame2 hands_up frown",
            "NozomiBoardgame2 hands_up annoyed",
            "NozomiBoardgame2 hands_up surprised",
            "NozomiBoardgame2 hands_up confused",
            "NozomiBoardgame2 hands_up concerned blush",
            "NozomiBoardgame2 hands_up frown blush",
            "NozomiBoardgame2 hands_up angry blush",
            "NozomiBoardgame2 hands_up concerned blush",
            "NozomiBoardgame2 hands_up concerned_light blush",
            "NozomiBoardgame2 hands_up neutral_light",
            "NozomiBoardgame2 hands_down neutral",
            "NozomiBoardgame2 hands_down neutral_light",
            "NozomiBoardgame2 hands_down sleepy",
            "NozomiBoardgame2 hands_down sleepy_light",

        ],
        #Page 11
        "nozomi hypnobondage": [
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised surprised feet2 motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised surprised feet3 motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet1 motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet2 norope motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet3 norope motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet3 ghostrope motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised_blush angry feet1 norope motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised_blush angry feet2 norope motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised_blush angry feet3 norope motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon ghostrope"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet2 ghostrope motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised_blush angry feet3 ghostrope motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon fullrope"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised_blush surprised feet2 fullrope motionlines"),
            overlap_images("cg n bedroom floor day", "NozomiHypnoBon raised_blush angry feet3 fullrope motionlines"),
        ],
        "nozomi hypnobondage tickling": [
            "NozomiHypnoBon2 kyou_blush",
            "NozomiHypnoBon2 kyou_smirk kyou_blush",
            "NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smirk kyou_blush",
            "NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smile rope",
            "NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smile",
            #Tickle and Spank variants start here
            "NozomiHypnoBon2 nozo_shocked nozo_noblush motionlines kyou_smirk arm_tickle",
            "NozomiHypnoBon2 nozo_chuckle nozo_noblush motionlines kyou_smirk arm_tickle",
            "NozomiHypnoBon2 nozo_growl nozo_noblush motionlines kyou_smirk",
            "NozomiHypnoBon2 nozo_mad nozo_noblush motionlines kyou_smirk",
            "NozomiHypnoBon2 nozo_mad nozo_noblush motionlines kyou_smirk arm_tickle",
            "NozomiHypnoBon2 nozo_annoyed nozo_blush motionlines kyou_smirk arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_annoyed nozo_blush motionlines kyou_laugh arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_growl nozo_blush motionlines kyou_laugh arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_growl nozo_blush motionlines kyou_smirk arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_giggle nozo_blush motionlines kyou_smirk arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_laugh nozo_blush motionlines kyou_smirk arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_laugh nozo_blush motionlines kyou_smile arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_giggle nozo_blush motionlines kyou_smile arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_giggle nozo_blush motionlines kyou_laugh arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_growl nozo_blush motionlines kyou_smirk arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_laugh nozo_blush motionlines kyou_smirk arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_laugh nozo_blush motionlines kyou_smile arm_up feet_squirm",
            "NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_smirk arm_up feet_squirm",
            "NozomiHypnoBon2 nozo_sigh nozo_noblush nolines kyou_smirk arm_up feet_rest",
            "NozomiHypnoBon2 nozo_shocked nozo_blush nolines kyou_smirk arm_tickle feet_squirm",
            "NozomiHypnoBon2 nozo_chuckle nozo_blush nolines kyou_smile arm_up feet_squirm",
            "NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_smile arm_up feet_rest",
            "NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_smirk arm_up feet_rest",
            "NozomiHypnoBon2 nozo_annoyed nozo_blush nolines kyou_smirk arm_up feet_rest",
            "NozomiHypnoBon2 nozo_shocked nozo_blush nolines kyou_smirk arm_tickle feet_squirm",
            "NozomiHypnoBon2 kyou_nervous arm_up head_up feet_rest nozo_noblush nozo_noface noglasses",            
        ],
        "nozomi hypnobondage spanking": [
            "NozomiHypnoBon2 kyou_blush",
            "NozomiHypnoBon2 kyou_smirk kyou_blush",
            "NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smirk kyou_blush",
            "NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smile rope",
            "NozomiHypnoBon2 nozo_annoyed nozo_noblush motionlines kyou_smile",
            "NozomiHypnoBon2 nozo_shocked nozo_noblush nolines kyou_smirk arm_spank",
            "NozomiHypnoBon2 nozo_shocked nozo_noblush nolines kyou_annoyed kyou_blush arm_up",
            "NozomiHypnoBon2 nozo_growl nozo_noblush nolines kyou_annoyed kyou_noblush arm_up",
            "NozomiHypnoBon2 nozo_growl nozo_noblush nolines kyou_smirk arm_up",
            "NozomiHypnoBon2 nozo_shocked nozo_blush motionlines kyou_smirk arm_spank feet_squirm",
            "NozomiHypnoBon2 nozo_shocked nozo_blush motionlines kyou_smirk arm_rest feet_squirm",
            "NozomiHypnoBon2 nozo_growl nozo_blush motionlines kyou_smirk arm_rest feet_squirm",
            "NozomiHypnoBon2 nozo_growl nozo_blush motionlines kyou_smirk kyou_blush arm_up feet_squirm",
            "NozomiHypnoBon2 nozo_pain nozo_blush motionlines kyou_smirk kyou_blush arm_spank feet_squirm",
            "NozomiHypnoBon2 nozo_mad nozo_blush motionlines kyou_smirk kyou_blush arm_rest feet_squirm",
            "NozomiHypnoBon2 nozo_mad nozo_blush nolines kyou_smirk kyou_blush arm_rest feet_rest",
            "NozomiHypnoBon2 nozo_growl nozo_blush nolines kyou_smirk kyou_blush arm_rest feet_rest",
            "NozomiHypnoBon2 nozo_growl nozo_blush nolines kyou_annoyed kyou_blush arm_up feet_rest",
            "NozomiHypnoBon2 nozo_shocked nozo_blush nolines kyou_annoyed kyou_blush arm_spank feet_squirm",
            "NozomiHypnoBon2 nozo_grimace nozo_blush nolines kyou_annoyed kyou_noblush arm_rest feet_squirm",
            "NozomiHypnoBon2 nozo_mad nozo_blush nolines kyou_annoyed kyou_noblush arm_up feet_rest",
            "NozomiHypnoBon2 nozo_pain nozo_blush motionlines kyou_annoyed kyou_noblush arm_spank feet_squirm",
            "NozomiHypnoBon2 nozo_worried nozo_blush nolines kyou_annoyed kyou_noblush arm_up feet_rest",
            "NozomiHypnoBon2 nozo_pain nozo_blush motionlines kyou_annoyed kyou_noblush arm_spank feet_squirm",
            "NozomiHypnoBon2 nozo_annoyed nozo_blush nolines kyou_annoyed kyou_noblush arm_up feet_rest",
            "NozomiHypnoBon2 nozo_worried nozo_blush nolines kyou_annoyed kyou_noblush arm_rest feet_rest",
            "NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_annoyed kyou_noblush arm_rest feet_rest",
            "NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_smile kyou_noblush arm_rest feet_rest",
            "NozomiHypnoBon2 nozo_sigh nozo_blush nolines kyou_smirk kyou_noblush arm_up feet_rest",
            "NozomiHypnoBon2 nozo_shocked nozo_blush nolines kyou_smirk kyou_noblush arm_rest feet_rest",
            "NozomiHypnoBon2 kyou_nervous arm_up head_up feet_rest nozo_noblush nozo_noface noglasses",
        ],
        "sayori alter lunch": [
            "SayoriAlterLunch sayori1 sushi1 chopsticks a_happy k_neutral s_laugh n_neutral",
            "SayoriAlterLunch sayori1 sushi1 chopsticks a_happy k_neutral s_laugh n_smile",
            "SayoriAlterLunch sayori1 sushi1 chopsticks a_happy k_embarrassed s_smile n_smile",
            "SayoriAlterLunch sayori1 sushi1 chopsticks a_smile_left k_embarrassed s_smile n_smile",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_smile_left k_embarrassed s_laugh n_smile",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_left k_neutral s_smile n_irritated",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_concerned_left k_neutral s_smile n_irritated",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_concerned_left k_neutral s_smile n_surprised",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_smile_left k_neutral s_neutral n_surprised",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_smile_left k_neutral s_neutral n_smile",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_smile_left k_neutral s_rolleyes n_neutral",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_rolleyes n_neutral",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_concerned_right k_neutral s_rolleyes n_neutral",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_pout n_neutral",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_pout_closed n_neutral",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_pout_closed n_sigh",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_grin n_sigh",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_grin n_neutral",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_neutral s_laugh n_neutral",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_neutral s_laugh n_surprised",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_neutral s_smile n_smile",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_neutral s_laugh n_smile",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_rolleyes n_neutral",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_neutral n_neutral",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_neutral s_neutral n_sigh",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_right k_smile s_neutral n_sigh",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_neutral_left k_smile s_surprised n_surprised",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_left k_smile s_laugh n_surprised",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_smile s_laugh n_surprised",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_smile_right k_smile s_happy n_neutral",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_happy k_smile s_happy n_neutral",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_happy k_smile s_happy n_sigh",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_happy k_smile s_grin n_sigh",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_laugh k_neutral s_grin n_neutral",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_smile_right k_neutral s_happy n_neutral",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_smile_right k_confused s_concerned n_surprised",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_smile_right k_confused s_concerned n_neutral",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_smile_right k_smile s_concerned n_neutral",
            "SayoriAlterLunch sayori2 sushi2 nosticks a_surprised k_confused s_surprised n_surprised",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_confused s_laugh n_neutral",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_confused s_laugh n_sigh",
            "SayoriAlterLunch sayori1 sushi2 chopsticks a_neutral_right k_confused s_smile n_sigh",
        ],
        "sayori arcade2": [
            "SayoriArcade2 s_giggle",
            "SayoriArcade2 s_giggle nozomi n_shocked",
            "SayoriArcade2 s_panic nozomi n_shocked",
            "SayoriArcade2 s_embarrassed nozomi n_shocked",
            "SayoriArcade2 s_smile nozomi n_neutral kyou k_mad",
            "SayoriArcade2 s_smirk nozomi n_neutral kyou k_mad",
            "SayoriArcade2 s_smirk nozomi n_neutral kyou k_frown_right",
            "SayoriArcade2 s_smile nozomi n_neutral kyou k_frown_right",
            "SayoriArcade2 s_rolleyes nozomi n_neutral kyou k_frown_right",
            "SayoriArcade2 s_neutral nozomi n_neutral kyou k_frown",
            "SayoriArcade2 s_neutral nozomi n_neutral kyou k_growl",
            "SayoriArcade2 s_neutral nozomi n_sigh kyou k_growl",
            "SayoriArcade2 s_rolleyes nozomi n_neutral kyou k_growl",
            "SayoriArcade2 s_rolleyes nozomi n_pout kyou k_growl",
            "SayoriArcade2 s_neutral nozomi n_concerned kyou k_growl",
            "SayoriArcade2 s_concerned nozomi n_concerned kyou k_frown",
            "SayoriArcade2 s_smirk nozomi n_concerned kyou k_frown",
            "SayoriArcade2 s_smirk nozomi n_concerned kyou k_mad",
            "SayoriArcade2 s_smirk nozomi n_neutral kyou k_growl",
            "SayoriArcade2 s_panic nozomi n_neutral kyou k_growl",
            "SayoriArcade2 s_anxious nozomi n_neutral kyou k_growl",
            "SayoriArcade2 s_anxious nozomi n_neutral kyou k_frown",
            "SayoriArcade2 s_panic nozomi n_neutral kyou k_frown",
            "SayoriArcade2 s_angry nozomi n_neutral kyou k_frown",
            "SayoriArcade2 s_angry nozomi n_neutral kyou k_mad",
            "SayoriArcade2 s_angry nozomi n_neutral kyou k_sigh",
            "SayoriArcade2 s_happy nozomi n_smile kyou k_frown",
            "SayoriArcade2 s_beaming nozomi n_smile kyou k_frown_right",
            "SayoriArcade2 s_neutral nozomi n_neutral kyou k_frown_right",
            "SayoriArcade2 s_concerned nozomi n_neutral kyou k_frown_right",
            "SayoriArcade2 s_concerned nozomi n_neutral kyou k_growl",
            "SayoriArcade2 s_panic nozomi n_neutral kyou k_growl",
            "SayoriArcade2 s_angry nozomi n_neutral kyou k_growl",
            "SayoriArcade2 s_angry nozomi n_neutral kyou k_smirk_right",
            "SayoriArcade2 s_smirk nozomi n_pout kyou k_smirk_right",
            "SayoriArcade2 s_frown nozomi n_neutral kyou k_frown",
            "SayoriArcade2 s_frown nozomi n_shocked kyou k_mad",
            "SayoriArcade2 s_frown nozomi n_awe kyou k_mad",
            "SayoriArcade2 s_beaming nozomi n_awe kyou k_sigh",
            "SayoriArcade2 s_smirk nozomi n_awe kyou k_sigh",            
        ],
        "sayori penlight": [
            "SayoriPenlight n_neutral s_neutral",
            "SayoriPenlight n_neutral s_neutral_right",
            "SayoriPenlight n_neutral s_smile_right",
            "SayoriPenlight n_neutral s_quizzical",
            "SayoriPenlight n_neutral s_yawn",
            "SayoriPenlight n_neutral s_smirk",
            "SayoriPenlight n_neutral s_smirk light",
            "SayoriPenlight n_curious s_quizzical light",
            "SayoriPenlight n_curious s_smile light",
            "SayoriPenlight n_curious s_neutral light",
            "SayoriPenlight n_curious s_yawn_right light",
            "SayoriPenlight n_anxious s_yawn_right light",
            "SayoriPenlight n_anxious s_neutral light",
            "SayoriPenlight n_anxious s_yawn light",            
        ],
        "sayori bed1": [
            "SayoriBed1 nozomi1 n_fascinated sayori1 s_curious",
            "SayoriBed1 nozomi1 n_fascinated sayori2 s_neutral",
            "SayoriBed1 nozomi1 n_curious_right2 sayori2 s_neutral",
            "SayoriBed1 nozomi1 n_curious_right1 sayori2 s_curious",
            "SayoriBed1 nozomi1 n_curious1 sayori2 s_curious",
            "SayoriBed1 nozomi1 n_concerned sayori2 s_curious",
            "SayoriBed1 nozomi1 n_concerned sayori2 s_concerned",
            "SayoriBed1 nozomi1 n_concerned sayori2 s_smile",
            "SayoriBed1 nozomi1 n_curious1 sayori2 s_smile",
            "SayoriBed1 nozomi1 n_concerned_right sayori4 s_concerned_left",
            "SayoriBed1 nozomi1 n_concerned sayori2 s_neutral",
            "SayoriBed1 nozomi1 n_curious2 sayori2 s_neutral",
            "SayoriBed1 nozomi1 n_curious2 sayori2 s_curious",
            "SayoriBed1 nozomi1 n_fascinated sayori2 s_neutral",
            "SayoriBed1 nozomi1 n_concerned_right sayori2 s_concerned",
            "SayoriBed1 nozomi1 n_concerned_right sayori2 s_neutral",
            "SayoriBed1 nozomi1 n_concerned_right sayori2 s_frown",
            "SayoriBed1 nozomi1 n_concerned sayori2 s_frown",
            "SayoriBed1 nozomi1 n_concerned sayori2 s_irritated",
            "SayoriBed1 nozomi1 n_concerned_right sayori2 s_surprised",
            "SayoriBed1 nozomi1 n_curious_right2 sayori2 s_surprised",
            "SayoriBed1 nozomi1 n_curious_right2 sayori3 s_surprised",
            "SayoriBed1 nozomi1 n_curious_right1 sayori3 s_laugh",
            "SayoriBed1 nozomi1 n_curious_right1 sayori3 s_happy",
            "SayoriBed1 nozomi1 n_smile sayori3 s_happy",
            "SayoriBed1 nozomi1 n_smile sayori4 s_pout",
            "SayoriBed1 nozomi1 n_giggle sayori4 s_pout",
            "SayoriBed1 nozomi1 n_giggle sayori4 s_rolleyes",
            "SayoriBed1 nozomi1 n_smile sayori4 s_concerned_left",
            "SayoriBed1 nozomi1 n_concerned_right sayori2 s_concerned",
            "SayoriBed1 nozomi1 n_concerned_right sayori2 s_happy",            
        ],
        "sayori hug":[
            "SayoriHug sad",
            "SayoriHug talk",
        ],
        "k bedroom confrontation sayori": [
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded frown", "Sayori_K_Bedroom upright angry_left"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded sad", "Sayori_K_Bedroom upright angry_left"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded sad", "Sayori_K_Bedroom upright neutral_left"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded sad", "Sayori_K_Bedroom upright neutral"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded angry", "Sayori_K_Bedroom upright angry"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded surprised", "Sayori_K_Bedroom upright surprised"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded scared", "Sayori_K_Bedroom upright confused"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed sleepy", "Sayori_K_Bedroom upright sleepy"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed entranced", "Sayori_K_Bedroom upright entranced"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom sleep closed", "Sayori_K_Bedroom sleep closed"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom sleep open", "Sayori_K_Bedroom sleep open"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed smile", "Sayori_K_Bedroom upright smile"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush smile", "Sayori_K_Bedroom upright blush smile"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Sayori_K_Bedroom upright blush smile"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Sayori_K_Bedroom upright blush seductive"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush smile", "Sayori_K_Bedroom upright blush pout"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush sad", "Sayori_K_Bedroom upright blush pout"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush sad", "Sayori_K_Bedroom upright blush confused"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush sad", "Sayori_K_Bedroom sleep blush open"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom sleep blush open", "Sayori_K_Bedroom sleep blush open"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Sayori_K_Bedroom upright blush laugh"),            
        ],
        #Page 12
        "k bedroom confrontation hiroko": [
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded frown", "Hiroko_K_Bedroom relaxed frown"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded sad", "Hiroko_K_Bedroom relaxed frown"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded sad", "Hiroko_K_Bedroom relaxed angry"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded angry", "Hiroko_K_Bedroom raised angry"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded surprised", "Hiroko_K_Bedroom raised surprised"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded surprised", "Hiroko_K_Bedroom raised annoyed"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded scared", "Hiroko_K_Bedroom raised annoyed"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded scared", "Hiroko_K_Bedroom raised surprised"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded sleepy", "Hiroko_K_Bedroom raised surprised"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom folded sleepy", "Hiroko_K_Bedroom raised annoyed"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed sleepy", "Hiroko_K_Bedroom raised annoyed"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed entranced", "Hiroko_K_Bedroom raised sleepy"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed entranced", "Hiroko_K_Bedroom relaxed sleepy"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed entranced", "Hiroko_K_Bedroom relaxed entranced"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom sleep closed", "Hiroko_K_Bedroom sleep closed"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom sleep open", "Hiroko_K_Bedroom sleep open"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed smile", "Hiroko_K_Bedroom relaxed smile"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush surprised", "Hiroko_K_Bedroom relaxed smile"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Hiroko_K_Bedroom relaxed smile"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Hiroko_K_Bedroom raised laugh"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Hiroko_K_Bedroom raised blush smile"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush smile", "Hiroko_K_Bedroom relaxed sad"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush sad", "Hiroko_K_Bedroom relaxed blush sad"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom sleep blush open", "Hiroko_K_Bedroom relaxed blush sad"),
            overlap_images("cg k bedroom day", "Nozomi_K_Bedroom relaxed blush laugh", "Hiroko_K_Bedroom relaxed blush laugh"),
        ],
        "sleeper agent struggle1":[
            "SleeperAgentStruggle nozomi n_smile sayori1 s_frown h_growl kyou1 k_dazed",
            "SleeperAgentStruggle nozomi n_smile sayori1 s_growl h_growl kyou1 k_dazed",
            "SleeperAgentStruggle nozomi n_sigh sayori1 s_growl h_growl kyou1 k_dazed",
            "SleeperAgentStruggle nozomi n_sigh sayori1 s_growl h_growl kyou1 k_pain",
            "SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_growl kyou2 k_furious",
            "SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_angry kyou2 k_furious",
            "SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_growl kyou2 k_angry",
            "SleeperAgentStruggle nozomi n_confused sayori1 s_frown h_growl kyou2 k_angry",
            "SleeperAgentStruggle nozomi n_confused sayori1 s_confused h_growl kyou2 k_angry",
            "SleeperAgentStruggle nozomi n_sigh blush sayori1 s_confused h_growl kyou2 k_angry",
            "SleeperAgentStruggle nozomi n_sigh blush sayori1 s_confused h_angry_side kyou2 k_angry",
            "SleeperAgentStruggle nozomi n_sigh blush sayori1 s_confused h_frown kyou2 k_angry",
            "SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_frown kyou1 k_growl",
            "SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_frown kyou1 k_confused",
            "SleeperAgentStruggle nozomi n_frown sayori1 s_frown h_angry kyou1 k_pain",
            "SleeperAgentStruggle nozomi n_smile sayori1 s_growl h_growl kyou1 k_pain",
            "SleeperAgentStruggle nozomi n_surprised sayori2 s_irritated h_growl kyou1 k_pain",
            "SleeperAgentStruggle nozomi n_surprised sayori2 s_angry h_growl kyou1 k_pain",
            "SleeperAgentStruggle nozomi n_frown sayori2 s_angry h_growl kyou1 k_pain",
            "SleeperAgentStruggle nozomi n_frown sayori2 s_angry h_growl kyou1 k_growl",
            "SleeperAgentStruggle nozomi n_frown sayori2 s_angry h_angry kyou1 k_growl",
            "SleeperAgentStruggle nozomi n_frown sayori2 s_angry h_frown kyou1 k_growl",
            "SleeperAgentStruggle nozomi n_confused sayori1 s_frown h_frown kyou1 k_growl",
            "SleeperAgentStruggle nozomi n_confused sayori1 s_frown h_frown kyou1 k_confused",
            "SleeperAgentStruggle nozomi n_smile sayori1 s_frown h_frown kyou1 k_pain",
            "SleeperAgentStruggle nozomi n_sigh sayori1 s_growl h_frown kyou1 k_pain",
            "SleeperAgentStruggle sayori1 s_frown h_frown kyou1 k_pain",
            "SleeperAgentStruggle sayori1 s_frown h_growl kyou2 k_furious",
            "SleeperAgentStruggle sayori1 s_frown h_angry kyou2 k_furious",
            "SleeperAgentStruggle sayori1 s_frown h_growl kyou2 k_angry",
        ] + unlockable_image_list("persistent.sleeper_agent_struggle2_unlock", [
            "SleeperAgentStruggle sayori1 s_frown h_growl kyou1 k_pain",
            "SleeperAgentStruggle sayori1 s_frown h_angry_side kyou1 k_pain",
            "SleeperAgentStruggle sayori1 s_growl h_frown kyou1 k_pain",
            "SleeperAgentStruggle sayori1 s_growl h_frown kyou1 k_dazed",
            "SleeperAgentStruggle sayori1 s_confused h_frown kyou1 k_dazed",
            "SleeperAgentStruggle sayori1 s_frown h_frown kyou1 k_dazed",
            "SleeperAgentStruggle sayori1 s_frown h_frown kyou1 k_calm",
            "SleeperAgentStruggle sayori1 s_frown h_growl kyou1 k_calm",
            "SleeperAgentStruggle sayori1 s_growl h_frown kyou1 k_calm",
            "SleeperAgentStruggle sayori1 s_confused h_confused kyou1 k_calm",
            "SleeperAgentStruggle sayori1 s_sleepy h_confused kyou1 k_calm",
            "SleeperAgentStruggle sayori1 s_sleepy h_worried kyou1 k_calm",
            "SleeperAgentStruggle sayori1 s_sleepy h_worried kyou1 k_sneer",
            "SleeperAgentStruggle sayori1 s_sleepy h_sleepy kyou1 k_sneer",
            "SleeperAgentStruggle sayori1 s_entranced h_sleepy kyou1 k_sneer",
            "SleeperAgentStruggle sayori1 s_entranced h_entranced kyou1 k_sneer",
        ]),
        "sleeper agent defeat":[
            "SleeperAgentDefeat",
            "SleeperAgentDefeat doubt_right",
            "SleeperAgentDefeat doubt_left",
            "SleeperAgentDefeat doubt",
            "SleeperAgentDefeat arm_up doubt_left",
            "SleeperAgentDefeat arm_up neutral",
            "SleeperAgentDefeat arm_up determined light",
            "SleeperAgentDefeat arm_up neutral light",
            "SleeperAgentDefeat arm_up sad light",            
        ],
        "nozomi burglar": [
            "NozomiBurglar pose1 growling",
            "NozomiBurglar pose1 shouting",
            "NozomiBurglar pose1 shouting penlight",
            "NozomiBurglar pose1 confused penlight",
            "NozomiBurglar pose1 confused_light penlight",
            "NozomiBurglar pose1 worried penlight",
            "NozomiBurglar pose1 worried_light penlight",
            "NozomiBurglar pose1 sleepy penlight",
            "NozomiBurglar pose1 sleepy_light penlight",
            "NozomiBurglar pose1 sleeping penlight",
            "NozomiBurglar pose2 sleep",
            "NozomiBurglar pose2 sleeptalk",
            "NozomiBurglar pose2 waking",            
        ],
        "nozomi burglar undressing": [
            "NozomiBurglarUndress",
            "NozomiBurglarUndress nozo_anxious glasses_anxious clothes_anxious confused",
            "NozomiBurglarUndress nozo_anxious glasses_anxious clothes_anxious shocked",
            "NozomiBurglarUndress nozo_giving noglasses clothes_giving offered_glasses",
            "NozomiBurglarUndress nozo_giving noglasses clothes_giving offered_none hand_up",
            "NozomiBurglarUndress nozo_anxious noglasses clothes_anxious ashamed_side hand_up",
            "NozomiBurglarUndress nozo_anxious noglasses clothes_anxious ashamed",
            "NozomiBurglarUndress nozo_anxious noglasses clothes_anxious confused",
            "NozomiBurglarUndress nozo_anxious noglasses clothes_anxious ashamed_side",
            "NozomiBurglarUndress nozo_anxious noglasses clothes_anxious shocked",
            "NozomiBurglarUndress nozo_anxious noglasses clothes_anxious blush_anxious shocked",
            "NozomiBurglarUndress nozo_undressing",
            "NozomiBurglarUndress nozo_giving noglasses blush_giving sweater offered_skirt",
            "NozomiBurglarUndress nozo_giving noglasses blush_giving sweater offered_none hand_up holding_skirt",
            "NozomiBurglarUndress nozo_giving noglasses blush_giving noclothes offered_sweater hand_up holding_skirt",
            "NozomiBurglarUndress nozo_giving noglasses blush_giving noclothes offered_none hand_up holding_sweater",
            "NozomiBurglarUndress nozo_giving noglasses blush_giving noclothes offered_none",
            "NozomiBurglarUndress nozo_begging noglasses blush_begging noclothes",
            "NozomiBurglarUndress nozo_anxious noglasses blush_anxious noclothes ashamed_side",
            "NozomiBurglarUndress nozo_anxious noglasses blush_anxious noclothes ashamed",            
        ],
        "akiko makeover 1": [
            "AkikoMakeover1 smile",
            "AkikoMakeover1 grin",           
        ],
        "akiko makeover 2": [
            At("AkikoMakeover2 outfit1 laugh", galscroll(-0.1)),
            At("AkikoMakeover2 outfit1 embarrassed blush", galtop(-0.1)),
            At("AkikoMakeover2 outfit1 smile", galtop(-0.1)),
            At("AkikoMakeover2 outfit1 grin", galtop(-0.1)),
            At("AkikoMakeover2 outfit1 curious_right", galtop(-0.1)),
            At("AkikoMakeover2 outfit1 curious", galtop(-0.1)),
            At("AkikoMakeover2 outfit1 embarrassed_left", galtop(-0.1)),
            At("AkikoMakeover2 outfit1 embarrassed", galtop(-0.1)),
            At("AkikoMakeover2 outfit2 smile blush", galtop(-0.1)),
            At("AkikoMakeover2 outfit2 embarrassed blush", galtop(-0.1)),
            At("AkikoMakeover2 outfit2 embarrassed_left blush", galtop(-0.1)),
            At("AkikoMakeover2 outfit2 smile", galtop(-0.1)),
            At("AkikoMakeover2 outfit2 surprised", galtop(-0.1)),
            At("AkikoMakeover2 outfit2 grin", galtop(-0.1)),
            At("AkikoMakeover2 outfit2 laugh", galtop(-0.1)),

        ],
        "copycat karaoke hypno1": [
            "CopycatKaraokeHypno pose1_nozomi_a glasses1 blush1 k_smile1 a_smile1",
            "CopycatKaraokeHypno pose1_nozomi_a flash glasses1 blush1 k_smile1 a_smileflash1",
            "CopycatKaraokeHypno pose1_nozomi_a flash glasses1 blush1 k_smile1 a_smile1",
            "CopycatKaraokeHypno pose1_nozomi_a flash glasses1 blush1 k_smile1 a_smileflash1",
            "CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_sleepy",
            "CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_sleepyflash",
            "CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_dazed",
            "CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_dazedflash",
            "CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_tranced",
            "CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_trancedflash",
            "CopycatKaraokeHypno pose1_nozomi_a flash glasses1 k_talk1 a_sleep1",
            "CopycatKaraokeHypno pose2_nozomi_a glasses2 k_smile2 a_sleep2",
            "CopycatKaraokeHypno pose2_nozomi_a glasses2 k_talk2 a_sleep2",
            "CopycatKaraokeHypno pose2_nozomi_a glasses2 k_neutral a_sleeptalk",
            "CopycatKaraokeHypno pose2_nozomi_a glasses2 k_talk2 a_sleeptalk",
            "CopycatKaraokeHypno pose2_nozomi_a glasses2 k_neutral a_waking",
            "CopycatKaraokeHypno pose2_nozomi_a glasses2 k_smile2 a_waking",
            "CopycatKaraokeHypno pose2_nozomi_a glasses2 blush2 k_smile2 a_grin",
            "CopycatKaraokeHypno pose2_nozomi_a glasses2 k_smile2 a_confused",
            "CopycatKaraokeHypno pose2_nozomi_a glasses2 k_smile2 a_grin",
            "CopycatKaraokeHypno pose2_nozomi_a glasses2 k_smile2 a_smile2",
            "CopycatKaraokeHypno pose2_nozomi_a glasses2 blush2 k_smile2 a_smile2",
        ],
        "copycat karaoke hypno2": [
            "CopycatKaraokeHypno pose1_nozomi_b glasses1 blush1 k_smile1 a_smile1",
            "CopycatKaraokeHypno pose1_nozomi_b flash glasses1 blush1 k_smile1 a_smileflash1",
            "CopycatKaraokeHypno pose1_nozomi_b flash glasses1 blush1 k_smile1 a_smile1",
            "CopycatKaraokeHypno pose1_nozomi_b flash glasses1 blush1 k_smile1 a_smileflash1",
            "CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_sleepy",
            "CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_sleepyflash",
            "CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_dazed",
            "CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_dazedflash",
            "CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_tranced",
            "CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_trancedflash",
            "CopycatKaraokeHypno pose1_nozomi_b flash glasses1 k_talk1 a_sleep1",
            "CopycatKaraokeHypno pose2_nozomi_b glasses2 k_smile2 a_sleep2",
            "CopycatKaraokeHypno pose2_nozomi_b glasses2 k_talk2 a_sleep2",
            "CopycatKaraokeHypno pose2_nozomi_b glasses2 k_neutral a_sleeptalk",
            "CopycatKaraokeHypno pose2_nozomi_b glasses2 k_talk2 a_sleeptalk",
            "CopycatKaraokeHypno pose2_nozomi_b glasses2 k_neutral a_waking",
            "CopycatKaraokeHypno pose2_nozomi_b glasses2 k_smile2 a_waking",
            "CopycatKaraokeHypno pose2_nozomi_b glasses2 blush2 k_smile2 a_grin",
            "CopycatKaraokeHypno pose2_nozomi_b glasses2 k_smile2 a_confused",
            "CopycatKaraokeHypno pose2_nozomi_b glasses2 k_smile2 a_grin",
            "CopycatKaraokeHypno pose2_nozomi_b glasses2 k_smile2 a_smile2",
            "CopycatKaraokeHypno pose2_nozomi_b glasses2 blush2 k_smile2 a_smile2",
        ],
        #Page 13
        "copycat karaoke1": [
            "CopycatKaraoke akiko_nozomi_a_down a_smile glasses1 kyou_down k_smile",
            "CopycatKaraoke akiko_nozomi_a_down a_happy glasses1 kyou_down k_smile title",
            "CopycatKaraoke akiko_nozomi_a_down a_happy glasses1 kyou_down k_confusedtv title lights",
            "CopycatKaraoke akiko_nozomi_a_down a_smile glasses1 kyou_down k_confusedtv title lights",
            "CopycatKaraoke akiko_nozomi_a_down a_giggle glasses1 kyou_down k_confusedtv lights",
            "CopycatKaraoke akiko_nozomi_a_up a_happy glasses1 kyou_down k_neutral lyric1b lights",
            "CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_neutral lyric1b lights",
            "CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_neutral lyric1 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_neutral lyric2 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_smile glasses1 kyou_down k_smile lights",
            "CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_smile lyric1 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_smile lyric2 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_sing glasses1 kyou_down k_smile lyric2 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_joy glasses1 kyou_down k_smile lyric2 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_happy glasses1 kyou_down k_confusedtv lights",
            "CopycatKaraoke akiko_nozomi_a_up a_happy glasses1 kyou_down k_confusedtv lyric1b lights",
            "CopycatKaraoke akiko_nozomi_a_up a_singtv glasses1 kyou_down k_confused lyric1 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_singtv a_blush glasses1 kyou_down k_confused lyric2 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_sing a_blush glasses1 kyou_down k_confused lyric2 lights",
            "CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_down k_confusedtv lyric4b lights",
            "CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_up k_nervoustv lyric4 lights",
            "CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_up k_nervoustv lyric3 lights",
            "CopycatKaraoke akiko_nozomi_a_down a_giggle a_blush glasses1 kyou_up k_confused lights",
            "CopycatKaraoke akiko_nozomi_a_down a_giggle a_blush glasses1 kyou_up k_confused k_blush lights",
            "CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_up k_smile k_blush lyric3b lights",
            "CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_up k_nervoustv k_blush lyric3 lights",
            "CopycatKaraoke akiko_nozomi_a_down a_smile a_blush glasses1 kyou_up k_nervous k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_up k_nervoustv k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_down k_smile k_blush lights",
            "CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_down k_smile k_blush lyric3b lights",
            "CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_up k_singtv k_blush lyric3 lights",
            "CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_up k_sing k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_wink a_blush glasses1 kyou_down k_confused k_blush lights",
            "CopycatKaraoke akiko_nozomi_a_up a_wink a_blush glasses1 kyou_down k_confused k_blush lyric2b lights",
            "CopycatKaraoke akiko_nozomi_a_up a_singtv a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_smile a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_sing a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_smile a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_shy a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_shy a_blush glasses1 kyou_up k_smile k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_joy a_blush glasses1 kyou_up k_happy k_blush lyric5 lights",
            "CopycatKaraoke akiko_nozomi_a_up a_joy a_blush glasses1 kyou_up k_happy k_blush lyric6 lights",
            "CopycatKaraoke akiko_nozomi_a_down a_shy a_blush glasses1 kyou_down k_smile k_blush lights",
        ],
        "copycat karaoke2": [
            "CopycatKaraoke akiko_nozomi_b_down a_smile glasses1 kyou_down k_smile",
            "CopycatKaraoke akiko_nozomi_b_down a_happy glasses1 kyou_down k_smile title",
            "CopycatKaraoke akiko_nozomi_b_down a_happy glasses1 kyou_down k_confusedtv title lights",
            "CopycatKaraoke akiko_nozomi_b_down a_smile glasses1 kyou_down k_confusedtv title lights",
            "CopycatKaraoke akiko_nozomi_b_down a_giggle glasses1 kyou_down k_confusedtv lights",
            "CopycatKaraoke akiko_nozomi_b_up a_happy glasses1 kyou_down k_neutral lyric1b lights",
            "CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_neutral lyric1b lights",
            "CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_neutral lyric1 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_neutral lyric2 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_smile glasses1 kyou_down k_smile lights",
            "CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_smile lyric1 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_smile lyric2 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_sing glasses1 kyou_down k_smile lyric2 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_joy glasses1 kyou_down k_smile lyric2 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_happy glasses1 kyou_down k_confusedtv lights",
            "CopycatKaraoke akiko_nozomi_b_up a_happy glasses1 kyou_down k_confusedtv lyric1b lights",
            "CopycatKaraoke akiko_nozomi_b_up a_singtv glasses1 kyou_down k_confused lyric1 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_singtv a_blush glasses1 kyou_down k_confused lyric2 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_sing a_blush glasses1 kyou_down k_confused lyric2 lights",
            "CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_down k_confusedtv lyric4b lights",
            "CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_up k_nervoustv lyric4 lights",
            "CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_up k_nervoustv lyric3 lights",
            "CopycatKaraoke akiko_nozomi_b_down a_giggle a_blush glasses1 kyou_up k_confused lights",
            "CopycatKaraoke akiko_nozomi_b_down a_giggle a_blush glasses1 kyou_up k_confused k_blush lights",
            "CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_up k_smile k_blush lyric3b lights",
            "CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_up k_nervoustv k_blush lyric3 lights",
            "CopycatKaraoke akiko_nozomi_b_down a_smile a_blush glasses1 kyou_up k_nervous k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_up k_nervoustv k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_down k_smile k_blush lights",
            "CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_down k_smile k_blush lyric3b lights",
            "CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_up k_singtv k_blush lyric3 lights",
            "CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_up k_sing k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_wink a_blush glasses1 kyou_down k_confused k_blush lights",
            "CopycatKaraoke akiko_nozomi_b_up a_wink a_blush glasses1 kyou_down k_confused k_blush lyric2b lights",
            "CopycatKaraoke akiko_nozomi_b_up a_singtv a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_smile a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_sing a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_smile a_blush glasses1 kyou_up k_singtv k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_shy a_blush glasses1 kyou_up k_smiletv k_blush lyric2 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_shy a_blush glasses1 kyou_up k_smile k_blush lyric4 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_joy a_blush glasses1 kyou_up k_happy k_blush lyric5 lights",
            "CopycatKaraoke akiko_nozomi_b_up a_joy a_blush glasses1 kyou_up k_happy k_blush lyric6 lights",
            "CopycatKaraoke akiko_nozomi_b_down a_shy a_blush glasses1 kyou_down k_smile k_blush lights",
        ],
        "copycat karaoke3": [
            "CopycatKaraoke together_nozomi_a affectionate glasses2",
            "CopycatKaraoke together_nozomi_a affectionate_closed glasses2",
            "CopycatKaraoke together_nozomi_b affectionate glasses2",
            "CopycatKaraoke together_nozomi_b affectionate_closed glasses2", 
        ],
        "nozomi cafe villain": [
            "NozomiCafe casual_leaning pensive nocup",
            "NozomiCafe casual_folded stern nocup",
            "NozomiCafe casual_folded growl nocup",
            "NozomiCafe casual_folded angry nocup",
            "NozomiCafe casual_leaning angry nocup",
            "NozomiCafe casual_leaning stern nocup",
            "NozomiCafe casual_leaning stern_side nocup",
            "NozomiCafe casual_leaning stern nocup",
            "NozomiCafe casual_leaning angry nocup",
            "NozomiCafe casual_folded growl nocup",
            "NozomiCafe casual_folded surprised nocup",
            "NozomiCafe casual_folded pensive nocup",
            "NozomiCafe casual_folded sleepy nocup",
            "NozomiCafe casual_folded sleepy hand1 nocup",
            "NozomiCafe casual_folded sleepy_entranced hand1 nocup",
            "NozomiCafe casual_folded neutral_entranced hand2 nocup",
            "NozomiCafe casual_folded neutral_entranced nohand nocup",
            "NozomiCafe casual_folded smile_entranced nocup",
        ],
        "nozomi captured": [
            "NozomiCaptured base1 dazed",
            "NozomiCaptured base1 sigh",
            "NozomiCaptured base1 surprised",
            "NozomiCaptured base1 dazed_left",
            "NozomiCaptured base2 dazed_left",
            "NozomiCaptured base3 dazed_left",
            "NozomiCaptured base3 dazed",
            "NozomiCaptured base3 angry",
            "NozomiCaptured base3 sleep",
            "NozomiCaptured base3 sleeptalk",
            "NozomiCaptured base3 dazed",
            "NozomiCaptured base3 awe",
            "NozomiCaptured base3 surprised blush",
            "NozomiCaptured base3 smile blush",
            "NozomiCaptured base3 laugh blush",
            "NozomiCaptured base3 surprised",
            "NozomiCaptured base3 awe",
            "NozomiCaptured base3 sigh",
            "NozomiCaptured base3 neutral",
            "NozomiCaptured base3 smile blush",
        ],
        "nozomi window": [
            "NozomiWindow bedroom_bw body_bw anxious_bw glasses_bw front_bw",
            "NozomiWindow bedroom_bw body_bw sigh_bw glasses_bw front_bw",
            "NozomiWindow bedroom_bw body_bw smile_bw glasses_bw front_bw",
            "NozomiWindow bedroom_bw body_bw smile_light_bw glasses_bw front_bw hiroko_bw",
            "NozomiWindow bedroom_bw body_bw surprised_bw glasses_bw front_bw",
            "NozomiWindow bedroom_bw body_bw surprised_light_bw glasses_bw front_bw hiroko_bw",
            "NozomiWindow bedroom_bw body_bw neutral_bw glasses_bw front_bw",
            "NozomiWindow bedroom_bw body_bw neutral_light_bw glasses_bw front_bw hiroko_bw",
            "NozomiWindow bedroom_bw body_bw sleepy_bw glasses_bw front_bw",
            "NozomiWindow bedroom_bw body_bw sleepy_light_bw glasses_bw front_bw hiroko_bw",
            "NozomiWindow bedroom_bw body_bw entranced_bw glasses_bw front_bw",
        ],
        "nozomi argument": [
            "NozomiArgument arms_up furious",
            "NozomiArgument arms_up angry",
            "NozomiArgument arms_up irritated",
            "NozomiArgument arms_up frown",
            "NozomiArgument arms_up angry",
            "NozomiArgument arms_up sleepy poke",
            "NozomiArgument arms_down entranced poke",
            "NozomiArgument arms_up sleepy wave",
            "NozomiArgument arms_down entranced wave",
            "NozomiArgument arms_down sleepy",
            "NozomiArgument arms_down calmtalk",
            "NozomiArgument arms_down calm",
        ],
        "sayori fallen": [
            "SayoriFallen head_up fear",
            "SayoriFallen head_down",
            "SayoriFallen head_down tears",
            "SayoriFallen head_up crying",
            "SayoriFallen head_up crying blush",
            "SayoriFallen head_up concerned_side_crying blush",
            "SayoriFallen head_up concerned_crying blush",
            "SayoriFallen head_up crying_closed blush",
            "SayoriFallen head_up concerned_crying",
            "SayoriFallen head_up confused",
            "SayoriFallen head_up sigh",
            "SayoriFallen head_up neutral",
            "SayoriFallen head_up neutral blush",
            "SayoriFallen head_up sigh blush",
            "SayoriFallen head_up confused blush",
            "SayoriFallen head_up fear blush",
            "SayoriFallen head_up concerned blush",
            "SayoriFallen head_up concerned_side blush",
            "SayoriFallen head_up sleepy blush",
            "SayoriFallen head_up sleep blush",
            "SayoriFallen head_up sleep",
        ],
        "sayori sleep": [
            "SayoriSleep sleep",
            "SayoriSleep sleep kyou",
            "SayoriSleep waking kyou",
        ],
        #Page 14
        "sayori sitting": [
            "SayoriSitting right_arm_down left_arm_down sayori_hair_down confused",
            "SayoriSitting right_arm_up left_arm_down sayori_hair_down surprised",
            "SayoriSitting right_arm_up left_arm_up sayori_hair_up confused",
            "SayoriSitting right_arm_up left_arm_up sayori_hair_up smile",
            "SayoriSitting right_arm_up left_arm_up sayori_hair_up happy",
        ],
        "nozomi kneeling devotion": [
            overlap_images("cg nozomi kneeling", "NozomiKneeling casual head_down crying glasses_down kyou_down_casual"),
            overlap_images("cg nozomi kneeling", "NozomiKneeling casual head_up hope glasses_up kyou_down_casual"),
        ],
        "classroom hiroko 2 1":[
            overlap_images("cg classroom 2", "HirokoHypno upright uniform2 frown2"),
            overlap_images("cg classroom 2", "HirokoHypno upright uniform2 annoyed_up2"),
            overlap_images("cg classroom 2", "HirokoHypno upright uniform2 angry_up2"),
            overlap_images("cg classroom 2", "HirokoHypno upright uniform2 angry2"),
            overlap_images("cg classroom 2", "HirokoHypno upright uniform2 annoyed2"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 annoyed2"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 drowsy2"),
            overlap_images("cg classroom 2", "HirokoHypno drooping uniform2 sleep"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 sleep"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 entranced_neutral"),
        ] + unlockable_image_list("persistent.classroom_hiroko_2_2_unlock", [
            overlap_images("cg classroom 2", "HirokoHypno drooping uniform2 sleeptalk"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 sad_closed2"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 surprised2"),
            overlap_images("cg classroom 2", "HirokoHypno upright uniform2 angry2 clenched_fists2"),
            overlap_images("cg classroom 2", "HirokoHypno upright uniform2 angry_up2 clenched_fists2"),
        ]) + unlockable_image_list("persistent.classroom_hiroko_2_3_unlock", [
            overlap_images("cg classroom 2", "HirokoHypno upright uniform2 blush2 sad_closed2"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 blush2 angry2 arm_uniform"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 blush2 angry_up2 arm_uniform"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 blush2 annoyed_up2 arm_uniform"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 blush2 annoyed_up2 no_arm"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 blush2 frown2 no_arm"),
        ]) + unlockable_image_list("persistent.classroom_hiroko_2_4_unlock", [
            overlap_images("cg classroom 2", "HirokoHypno drooping uniform2 sleep arm_uniform"),
            overlap_images("cg classroom 2", "HirokoHypno drooping uniform2 sleeptalk arm_uniform"),
            overlap_images("cg classroom 2", "HirokoHypno relaxed uniform2 drowsy2"),
            overlap_images("cg classroom 2", "HirokoHypno upright uniform2 angry2 clenched_fists2"),            
        ]),
        "hiroko rehearsal": [
            "HirokoRehearsal pose1 frown",
            "HirokoRehearsal pose1 angry",
            "HirokoRehearsal pose2",
        ],
        "sayori arcade": [
            overlap_images("cg arcade", "SayoriArcade standing happy"),
            overlap_images("cg arcade", "KyouArcade bemused", "SayoriArcade standing happy"),
            overlap_images("cg arcade", "KyouArcade bemused", "SayoriArcade standing smile"),
            overlap_images("cg arcade", "KyouArcade bemused", "SayoriArcade lookaside smile_left"),
            overlap_images("cg arcade", "KyouArcade smile", "SayoriArcade lookaside smile_left"),
            overlap_images("cg arcade", "KyouArcade smile", "SayoriArcade lookaside rolleyes"),
            overlap_images("cg arcade", "KyouArcade defeated", "SayoriArcade victory noface"),
        ],
        "sayori room hypno2": [
            "SayoriRoomHypno2 kyou_penlight k2_neutral",
            "SayoriRoomHypno2 kyou_penlight k2_neutral s_confused",
            "SayoriRoomHypno2 kyou_penlight k2_confused s_confused",
            "SayoriRoomHypno2 kyou_penlight k2_confused s_neutral",
            "SayoriRoomHypno2 kyou_penlight k2_confused s_confused_closed",
            "SayoriRoomHypno2 kyou k_frown s_confused_closed",
            "SayoriRoomHypno2 kyou k_frown s_frown",
            "SayoriRoomHypno2 kyou k_frown s_neutral",
            "SayoriRoomHypno2 kyou k_smile s_neutral",
            "SayoriRoomHypno2 kyou k_smile s_chuckle",
            "SayoriRoomHypno2 kyou k_smile s_smile",
            "SayoriRoomHypno2 kyou_penlight k2_smile light s_smile",
            "SayoriRoomHypno2 kyou_penlight k2_smile light s_smile_flash",
            "SayoriRoomHypno2 kyou_penlight k2_neutral light s_neutral",
            "SayoriRoomHypno2 kyou_penlight k2_neutral light s_neutral_flash",
            "SayoriRoomHypno2 kyou_penlight k2_neutral light s_drowsy",
            "SayoriRoomHypno2 kyou_penlight k2_neutral light s_drowsy_flash",
            "SayoriRoomHypno2 kyou_penlight k2_neutral light s_headdown s_sleep",
            "SayoriRoomHypno2 kyou_penlight k2_neutral s_headdown s_sleep",
            "SayoriRoomHypno2 kyou k_neutral s_headdown s_sleep",
            "SayoriRoomHypno2 kyou k_neutral s_headdown s_sleeptalk",
            "SayoriRoomHypno2 kyou k_frown s_headdown s_sleep",
            "SayoriRoomHypno2 kyou k_smile s_headdown s_sleep",
        ],
        "sayori room tickle": [
            "SayoriRoom Tickle",
            "SayoriRoom Tickle sayoriback_sleepy",
            "SayoriRoom Tickle sayoriback_surprised_protag",
            "SayoriRoom Tickle sayoriback_quizzical_feet",
            "SayoriRoom Tickle sayoriback_quizzical_protag",
            "SayoriRoom Tickle kyouback_laugh sayoriback_quizzical_protag",
            "SayoriRoom Tickle kyouback_laugh sayoriback_annoyed_closed",
            "SayoriRoom Tickle kyouback_smile sayoriback_quizzical_protag",
            "SayoriRoom Tickle kyouback_smile sayoriback_surprised_feet sayoriback_blush",
            "SayoriRoom Tickle kyouback_smile sayoriback_anxious_feet sayoriback_blush",
            "SayoriRoom Tickle kyouback_smile sayoriback_annoyed_closed",
            "SayoriRoom Tickle kyouback_smirk sayoriback_annoyed_closed",
            "SayoriRoom Tickle kyouback_smirk sayoriback_anxious_protag",
            "SayoriRoom Tickle kyouback_smirk sayoriback_sleep",
            "SayoriRoom Tickle kyouback_smirk sayoriback_quizzical_protag",
            "SayoriRoom Tickle kyouback_smile sayoriback_quizzical_feet",
            "SayoriRoom Tickle kyouback_smile sayoriback_sleep",
            "SayoriRoom Tickle kyouback_smile sayoriback_sleep",
            "SayoriRoom Tickle kyouback_neutral sayoriback_sleep",
            "SayoriRoom Tickle kyougone kyounoface sayoriback_quizzical_protag",
            "SayoriRoom Tickle kyougone kyounoface sayoriback_surprised_protag",
            "SayoriRoom Tickle kyougone kyounoface sayoriback_angry",
            "SayoriRoom Tickle kyouback_neutral sayoriback_angry_protag",
            "SayoriRoom Tickle kyouback_neutral sayoriback_quizzical_protag",
            "SayoriRoom Tickle kyouback_neutral kyouback_blush sayoriback_quizzical_protag",
            "SayoriRoom Tickle kyouback_neutral kyouback_blush sayoriback_anxious_protag sayoriback_blush",
            "SayoriRoom Tickle kyouback_neutral kyouback_blush sayoriback_anxious_feet sayoriback_blush",
            "SayoriRoom Tickle kyouback_neutral sayoriback_anxious_protag sayoriback_blush",
            "SayoriRoom Tickle kyouback_neutral sayoriback_angry_protag sayoriback_blush",
            "SayoriRoom Tickle kyouback_neutral sayoriback_annoyed_closed sayoriback_blush",
            "SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_annoyed_closed sayoriback_blush",
            "SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_sleep",
            "SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_angry_protag",
            "SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_surprised_feet sayoriback_blush",
            "SayoriRoom Tickle kyoufront kyoufront_smile sayoriback_surprised_feet sayoriback_blush",
            "SayoriRoom Tickle kyoufront kyoufront_smirk sayoriback_surprised_feet sayoriback_blush",
            "SayoriRoom Tickle kyoufront kyoufront_smirk sayoriback_giggle sayoriback_blush",
            "SayoriRoom Tickle kyouback_smirk Sayori_Front sayorifront_giggle sayorifront_blush sayori_nofoot",
            "SayoriRoom Tickle kyouback_smirk Sayori_Front sayorifront_pout sayorifront_blush sayori_nofoot",
            "SayoriRoom Tickle kyouback_laugh Sayori_Front sayorifront_pout sayorifront_blush sayori_nofoot",
            "SayoriRoom Tickle kyouback_smile Sayori_Front sayorifront_neutral sayorifront_blush sayori_nofoot",
            "SayoriRoom Tickle kyouback_smile Sayori_Front sayorifront_anxious sayori_nofoot",
            "SayoriRoom Tickle kyouback_smile sayoriback_sleep",
            "SayoriRoom Tickle kyouback_smile sayoriback_anxious_feet sayoriback_blush",
            "SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_anxious_feet sayoriback_blush",
            "SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_surprised_feet",
            "SayoriRoom Tickle kyoufront kyoufront_smirk sayoriback_surprised_feet",
            "SayoriRoom Tickle kyoufront kyoufront_smirk sayoriback_anxious_protag",
            "SayoriRoom Tickle kyoufront kyoufront_smirk sayoriback_quizzical_protag",
            "SayoriRoom Tickle kyoufront kyoufront_neutral sayoriback_quizzical_protag",
            "SayoriRoom Tickle kyouback_neutral sayoriback_quizzical_protag",
            "SayoriRoom Tickle kyouback_neutral Sayori_Front sayorifront_neutral sayori_nofoot",
            "SayoriRoom Tickle kyouback_neutral Sayori_Front sayorifront_irritated sayori_nofoot",
            "SayoriRoom Tickle kyouback_neutral Sayori_Front sayorifront_anxious sayori_nofoot",
            "SayoriRoom Tickle kyouback_neutral Sayori_Front sayorifront_pout sayori_nofoot",
            "SayoriRoom Tickle kyouback_neutral Sayori_Front sayorifront_smirk sayori_nofoot",
            "SayoriRoom Tickle sayoriback_neutral kyougone kyounoface",
            "SayoriRoom Tickle sayoriback_smile kyougone kyounoface",
            "SayoriRoom Tickle sayoriback_happy kyougone kyounoface",
        ],
        "hiroko gaming": [
            "HirokoGaming hiroko1 tennis head1 neutral1",
            "HirokoGaming hiroko1 tennis head2 quizzical2",
            "HirokoGaming hiroko1 tennis head1 frown1",
            "HirokoGaming hiroko1 tennis head1 sigh1",
            "HirokoGaming hiroko1 tennis head2 annoyed2",
            "HirokoGaming hiroko1 tennis head1 angry1",
            "HirokoGaming hiroko1 tennis head1 laugh1",
            "HirokoGaming hiroko1 tennis head2 laugh2",
            "HirokoGaming hiroko1 tennis head2 happy2",
            "HirokoGaming hiroko1 tennis head2 smirk2",
            "HirokoGaming hiroko1 tennis head2 smile2",
            "HirokoGaming hiroko1 tennis head1 smile1",
            "HirokoGaming hiroko1 tennis head1 annoyed1",
            "HirokoGaming hiroko1 tennis head1 surprised1",
            "HirokoGaming hiroko1 tennis head2 angry2",
            "HirokoGaming hiroko1 tennis head2 neutral2",
            "HirokoGaming hiroko2 tennis head2 moaning2 blush2",
            "HirokoGaming hiroko1 tennis head2 angry2 blush2",
            "HirokoGaming hiroko1 tennis head2 annoyed2 blush2",
            "HirokoGaming hiroko1 tennis head1 surprised1 blush1",
            "HirokoGaming hiroko1 tennis head1 angry1 blush1",
            "HirokoGaming hiroko2 tennis head1 moaning1 blush1",
            "HirokoGaming hiroko2 tennis head1 unfocused1 blush1",
            "HirokoGaming hiroko1 tennis head2 angry2 blush2",
            "HirokoGaming hiroko2 tennis head1 moaning_closed1 blush1",
            "HirokoGaming hiroko1 tennis head1 moaning_closed1 blush1",
            "HirokoGaming hiroko1 tennis head1 sigh1 blush1",
            #Socks
            "HirokoGaming hiroko1_socks tennis head1 neutral1",
            "HirokoGaming hiroko1_socks tennis head2 quizzical2",
            "HirokoGaming hiroko1_socks tennis head1 frown1",
            "HirokoGaming hiroko1_socks tennis head1 sigh1",
            "HirokoGaming hiroko1_socks tennis head2 annoyed2",
            "HirokoGaming hiroko1_socks tennis head1 angry1",
            "HirokoGaming hiroko1_socks tennis head1 laugh1",
            "HirokoGaming hiroko1_socks tennis head2 laugh2",
            "HirokoGaming hiroko1_socks tennis head2 happy2",
            "HirokoGaming hiroko1_socks tennis head2 smirk2",
            "HirokoGaming hiroko1_socks tennis head2 smile2",
            "HirokoGaming hiroko1_socks tennis head1 smile1",
            "HirokoGaming hiroko1_socks tennis head1 annoyed1",
            "HirokoGaming hiroko1_socks tennis head1 surprised1",
            "HirokoGaming hiroko1_socks tennis head2 angry2",
            "HirokoGaming hiroko1_socks tennis head2 neutral2",
            "HirokoGaming hiroko2_socks tennis head2 moaning2 blush2",
            "HirokoGaming hiroko1_socks tennis head2 angry2 blush2",
            "HirokoGaming hiroko1_socks tennis head2 annoyed2 blush2",
            "HirokoGaming hiroko1_socks tennis head1 surprised1 blush1",
            "HirokoGaming hiroko1_socks tennis head1 angry1 blush1",
            "HirokoGaming hiroko2_socks tennis head1 moaning1 blush1",
            "HirokoGaming hiroko2_socks tennis head1 unfocused1 blush1",
            "HirokoGaming hiroko1_socks tennis head2 angry2 blush2",
            "HirokoGaming hiroko2_socks tennis head1 moaning_closed1 blush1",
            "HirokoGaming hiroko1_socks tennis head1 moaning_closed1 blush1",
            "HirokoGaming hiroko1_socks tennis head1 sigh1 blush1",
            #Undies
            "HirokoGaming hiroko1 head1 neutral1",
            "HirokoGaming hiroko1 head2 quizzical2",
            "HirokoGaming hiroko1 head1 frown1",
            "HirokoGaming hiroko1 head1 sigh1",
            "HirokoGaming hiroko1 head2 annoyed2",
            "HirokoGaming hiroko1 head1 angry1",
            "HirokoGaming hiroko1 head1 laugh1",
            "HirokoGaming hiroko1 head2 laugh2",
            "HirokoGaming hiroko1 head2 happy2",
            "HirokoGaming hiroko1 head2 smirk2",
            "HirokoGaming hiroko1 head2 smile2",
            "HirokoGaming hiroko1 head1 smile1",
            "HirokoGaming hiroko1 head1 annoyed1",
            "HirokoGaming hiroko1 head1 surprised1",
            "HirokoGaming hiroko1 head2 angry2",
            "HirokoGaming hiroko1 head2 neutral2",
            "HirokoGaming hiroko2 head2 moaning2 blush2",
            "HirokoGaming hiroko1 head2 angry2 blush2",
            "HirokoGaming hiroko1 head2 annoyed2 blush2",
            "HirokoGaming hiroko1 head1 surprised1 blush1",
            "HirokoGaming hiroko1 head1 angry1 blush1",
            "HirokoGaming hiroko2 head1 moaning1 blush1",
            "HirokoGaming hiroko2 head1 unfocused1 blush1",
            "HirokoGaming hiroko1 head2 angry2 blush2",
            "HirokoGaming hiroko2 head1 moaning_closed1 blush1",
            "HirokoGaming hiroko1 head1 moaning_closed1 blush1",
            "HirokoGaming hiroko1 head1 sigh1 blush1",
        ],
        "hiroko slumped": [
            "HirokoSlumped tennis blissful",
            "HirokoSlumped tennis moaning",
            "HirokoSlumped tennis sleepy",
            "HirokoSlumped tennis smile",
            #Socks
            "HirokoSlumped tennis socks blissful",
            "HirokoSlumped tennis socks moaning",
            "HirokoSlumped tennis socks sleepy",
            "HirokoSlumped tennis socks smile",
            #Undies
            "HirokoSlumped blissful",
            "HirokoSlumped moaning",
            "HirokoSlumped sleepy",
            "HirokoSlumped smile",
        ],
        #Page 15
        "hiroko court night good": [
            "HirokoCourtNight hiroko_crossed neutral kyou_casual",
            "HirokoCourtNight hiroko_crossed sigh kyou_casual",
            "HirokoCourtNight hiroko_crossed neutral_left kyou_casual",
            "HirokoCourtNight hiroko_crossed frown kyou_casual",
            "HirokoCourtNight hiroko_crossed irritated kyou_casual",
            "HirokoCourtNight hiroko_crossed neutral_left kyou_casual",
            "HirokoCourtNight hiroko_standing neutral kyou_casual",
        ],
        "hiroko court night bad": [
            "HirokoCourtNight hiroko_crossed neutral kyou_casual",
            "HirokoCourtNight hiroko_crossed sigh kyou_casual",
            "HirokoCourtNight hiroko_crossed neutral_left kyou_casual",
            "HirokoCourtNight hiroko_crossed frown kyou_casual",
            "HirokoCourtNight hiroko_crossed irritated kyou_casual",
            "HirokoCourtNight hiroko_crossed growl kyou_casual",
            "HirokoCourtNight hiroko_crossed irritated kyou_casual",
            "HirokoCourtNight hiroko_crossed confused kyou_casual",
            "HirokoCourtNight hiroko_standing sleepy_confused kyou_casual",
            "HirokoCourtNight hiroko_sleeping sleep kyou_casual",
            "HirokoCourtNight hiroko_sleeping sleeptalk kyou_casual",
            "HirokoCourtNight hiroko_sleeping sleep",
            "HirokoCourtNight hiroko_standing confused kyou_casual",
            "HirokoCourtNight hiroko_standing smile kyou_casual",
            "HirokoCourtNight hiroko_standing happy kyou_casual",
            "HirokoCourtNight hiroko_crossed sleepy kyou_casual",
            "HirokoCourtNight hiroko_crossed neutral_left kyou_casual",
            "HirokoCourtNight hiroko_standing smile kyou_casual",
            "HirokoCourtNight hiroko_standing happy kyou_casual",
        ],
        "hiroko park sad": [
            "HirokoParkSad",
            "HirokoParkSad frown_tears",
            "HirokoParkSad head2 angry_tears",
            "HirokoParkSad head2 stern_tears",
            "HirokoParkSad frown",
            "HirokoParkSad sad",
            "HirokoParkSad head2 stern",
            "HirokoParkSad head2 glare",
            "HirokoParkSad head2 surprised",
            "HirokoParkSad head2 angry",
            "HirokoParkSad head2 upset",
            "HirokoParkSad head2 upset_tears",
            "HirokoParkSad head1 sad_tears",
            "HirokoParkSad head1 arms_throw sad_tears",
            "HirokoParkSad head1 arms_down sad_tears",
            "HirokoParkSad head2 arms_down angry_tears",
            "HirokoParkSad head1 arms_down weeping",
            "HirokoParkSad head1 arms_down frown",
            "HirokoParkSad head2 arms_down stern",
        ],
        "hiroko won": [
            "HirokoWon shocked",
            "HirokoWon nozomi shocked",
            "HirokoWon nozomi crying",
        ],
        "hiroko cam 1 1": [
            "HirokoCam1 sleep_armdown sleep",
            "HirokoCam1 sleep_armdown sleeptalk",
            "HirokoCam1 sleep_armdown sleep",
            "HirokoCam1 sleep_armmid sleep",
            "HirokoCam1 sleep_armup sleep",
            "HirokoCam1 sleep_penlight sleep",
            "HirokoCam1 sleep_penlight sleeptalk",
            "HirokoCam1 sleep_penlight waking",
            "HirokoCam1 awake1 surprised",
            "HirokoCam1 awake1 happy",
        ] + unlockable_image_list("persistent.hiroko_cam_1_2_unlock", [
            "HirokoCam1 awake2 cheerful sweat2",
            "HirokoCam1 awake2 smile sweat2",
            "HirokoCam1 sleep_armdown sleeptalk blush sweat1",
            "HirokoCam1 sleep_armdown sleep blush sweat1",            
        ]),
        "hiroko cam 2": [
            At("HirokoCam2 standing",galscroll(-0.2 )),
            At("HirokoCam2 jumping", galscroll(-0.2)),
        ],
        "hiroko karaoke bed 2": [
            #This is a single image
        ],
        "hiroko bed": [
            "HirokoBed sleeptalk",
            "HirokoBed sleep",
            "HirokoBed sleep_concerned",
            "HirokoBed waking",
            "HirokoBed sleeptalk_concerned",
            "HirokoBed sleepy",
            "HirokoBed nervous",
            "HirokoBed smile blush",
            "HirokoBed happy blush",
            "HirokoBed sleeptalk_concerned blush",
        ],
        "hiroko couch": [
            At("HirokoCouch neutral_l", galzoomout),
            At("HirokoCouch sleeptalk", galzoomout),
            At("HirokoCouch confused", galzoomout),
            At("HirokoCouch frown", galzoomout),
            At("HirokoCouch nozomi_down n_frown frown", galzoomout),
            At("HirokoCouch nozomi_up n_neutral neutral coin", galzoomout),
            At("HirokoCouch nozomi_up n_neutral anxious coin", galzoomout),
            At("HirokoCouch nozomi_up n_talk2 anxious coin", galzoomout),
            At("HirokoCouch nozomi_up n_talk anxious coin", galzoomout),
            At("HirokoCouch nozomi_up n_smile anxious coin", galzoomout),
            At("HirokoCouch nozomi_up n_smile neutral coin", galzoomout),
            At("HirokoCouch nozomi_up n_talk neutral_r coin_r", galzoomout),
            At("HirokoCouch nozomi_up n_talk neutral coin", galzoomout),
            At("HirokoCouch nozomi_up n_talk neutral_l coin_l", galzoomout),
            At("HirokoCouch nozomi_up n_talk2 neutral_r coin_r", galzoomout),
            At("HirokoCouch nozomi_up n_talk2 neutral coin", galzoomout),
            At("HirokoCouch nozomi_up n_talk2 neutral_l coin_l", galzoomout),
            At("HirokoCouch nozomi_up n_neutral dazed_r coin_r", galzoomout),
            At("HirokoCouch nozomi_up n_neutral dazed coin", galzoomout),
            At("HirokoCouch nozomi_up n_neutral dazed_l coin_l", galzoomout),
            At("HirokoCouch nozomi_up n_talk dazed_r coin_r", galzoomout),
            At("HirokoCouch nozomi_up n_talk dazed coin", galzoomout),
            At("HirokoCouch nozomi_up n_talk dazed_l coin_l", galzoomout),
            At("HirokoCouch nozomi_up n_talk sleepy_r coin_r", galzoomout),
            At("HirokoCouch nozomi_up n_talk sleepy coin", galzoomout),
            At("HirokoCouch nozomi_up n_talk sleepy_l coin_l", galzoomout),
            At("HirokoCouch nozomi_up n_talk sleep coin_r", galzoomout),
            At("HirokoCouch nozomi_up n_talk sleep coin", galzoomout),
            At("HirokoCouch nozomi_up n_talk sleep coin_l", galzoomout),
            At("HirokoCouch nozomi_down n_neutral sleep", galzoomout),
            At("HirokoCouch nozomi_down n_talk sleep", galzoomout),
            At("HirokoCouch nozomi_down n_talk2 sleep", galzoomout),
            At("HirokoCouch nozomi_down n_talk2 sleeptalk", galzoomout),
            At("HirokoCouch nozomi_down n_smile sleep", galzoomout),
            At("HirokoCouch nozomi_down n_neutral sleeptalk", galzoomout),
            At("HirokoCouch nozomi_down n_smile sleepy", galzoomout),
        ],
        #Page 16
        "hiroko couch2": [
            "HirokoCouch2 hiroko1 h_sleepy1",
            "HirokoCouch2 nozomi1a n_smile1 hiroko1 h_sleepyl1",
            "HirokoCouch2 nozomi1b n_smile1 hiroko2 h_sleep2",
            "HirokoCouch2 nozomi1b n_smile1 hiroko2 h_smile2",
            "HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_frown2",
            "HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_sleep2",
            "HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_sleep2",
            "HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_frownl2",
            "HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_neutral2",
            "HirokoCouch2 nozomi1b n_sad1 hiroko2 h_neutral2",
            "HirokoCouch2 nozomi1b n_sad1 hiroko2 h_confused2",
            "HirokoCouch2 nozomi1b n_sad1 hiroko2 h_smile2",
            "HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_smile2",
            "HirokoCouch2 nozomi1b n_happy1 hiroko2 h_smile2",
            "HirokoCouch2 nozomi1b n_smile1 hiroko2 h_smile2",
            "HirokoCouch2 nozomi2 n_grin2 hiroko1 h_surprised1 coin",
            "HirokoCouch2 nozomi2 n_happy2 hiroko1 h_surprised1 coin",
            At("HirokoCouch2 nozomi2 n_smile2 hiroko1 h_sleepyr1 coin_r", coinswing_hc2),
            "HirokoCouch2 both n_surprisedd3 n_blush3 h_sleep3",
            "HirokoCouch2 both n_surprised3 n_blush3 h_sleep3",
            "HirokoCouch2 both n_smile3 h_sleep3",
            "HirokoCouch2 both n_neutral3 h_sleep3",
            "HirokoCouch2 both n_smile3 h_sleeptalk3",
            "HirokoCouch2 both n_happy3 h_sleepy3",
            "HirokoCouch2 both n_smile3 h_surprised3 h_blush3",
            "HirokoCouch2 both n_smile3 h_smile3 h_blush3",
            "HirokoCouch2 both n_happy3 n_blush3 h_smile3 h_blush3",
            "HirokoCouch2 nozomi1b n_happy1 n_blush1 hiroko2 h_happy2 h_blush2",
            "HirokoCouch2 nozomi1b n_smile1 n_blush1 hiroko2 h_smile2 h_blush2",
            "HirokoCouch2 nozomi1b n_smile1 n_blush1 hiroko2 h_confused2",
            "HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_sigh2",
            "HirokoCouch2 nozomi1b n_happy1 hiroko2 h_sigh2",
            "HirokoCouch2 nozomi1b n_neutralr1 hiroko2 h_neutrall2",
            "HirokoCouch2 nozomi1b n_smile1 hiroko2 h_neutrall2",
            "HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_neutrall2",
            "HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_neutral2",
            "HirokoCouch2 nozomi1b n_sad1 hiroko2 h_neutral2",
            "HirokoCouch2 nozomi1b n_frown1 hiroko2 h_neutral2",
            "HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_neutral2",
            "HirokoCouch2 nozomi1b n_neutral1 hiroko2 h_sad2",
        ],
        "nozomi karaoke group": [
            "NozomiKaraokeGroup",
            "NozomiKaraokeGroup nozo_annoyed hiro_irritated risa_uncertain",
            "NozomiKaraokeGroup nozo_worried hiroko_armsup hiro_furious risa_disgruntled",
            "NozomiKaraokeGroup nozo_cry hiroko_armsup hiro_pain risa_pain",
        ],
        "sayori dinner": [
            "SayoriDinner nosayori",
            "SayoriDinner sayori_armsup laugh",
            "SayoriDinner sayori_armsup smile",
            "SayoriDinner sayori_armsup smile_side",
            "SayoriDinner sayori_armsup smile_closed",
            "SayoriDinner sayori_armsup neutral",
            "SayoriDinner sayori_armsup neutral_side",
            "SayoriDinner sayori_armsup smirk",
            "SayoriDinner sayori_armsup concerned",
            "SayoriDinner sayori_armsup concerned_closed",
            "SayoriDinner sayori_armsup surprised",
            "SayoriDinner sayori_armsup stern",
            "SayoriDinner sayori_armsup stern_side",
            "SayoriDinner sayori_armsup angry",
            "SayoriDinner sayori_armsup cry_open1",
            "SayoriDinner sayori_armsup cry_closed",
            "SayoriDinner sayori laugh",
            "SayoriDinner sayori smile",
            "SayoriDinner sayori smile_side",
            "SayoriDinner sayori smile_closed",
            "SayoriDinner sayori neutral",
            "SayoriDinner sayori neutral_side",
            "SayoriDinner sayori smirk",
            "SayoriDinner sayori concerned",
            "SayoriDinner sayori concerned_closed",
            "SayoriDinner sayori surprised",
            "SayoriDinner sayori stern",
            "SayoriDinner sayori stern_side",
            "SayoriDinner sayori angry",
            "SayoriDinner sayori cry_open1",
            "SayoriDinner sayori cry_closed",
            "SayoriDinner sayori laugh_cry",
            "SayoriDinner sayori cry_open2",
            "SayoriDinner sayori cry_smile",
            "SayoriDinner sayori_armsup_blush laugh",
            "SayoriDinner sayori_armsup_blush smile",
            "SayoriDinner sayori_armsup_blush smile_side",
            "SayoriDinner sayori_armsup_blush smile_closed",
            "SayoriDinner sayori_armsup_blush neutral",
            "SayoriDinner sayori_armsup_blush neutral_side",
            "SayoriDinner sayori_armsup_blush smirk",
            "SayoriDinner sayori_armsup_blush concerned",
            "SayoriDinner sayori_armsup_blush concerned_closed",
            "SayoriDinner sayori_armsup_blush surprised",
            "SayoriDinner sayori_armsup_blush stern",
            "SayoriDinner sayori_armsup_blush stern_side",
            "SayoriDinner sayori_armsup_blush angry",
            "SayoriDinner sayori_armsup_blush cry_open1",
            "SayoriDinner sayori_armsup_blush cry_closed",
            "SayoriDinner sayori_blush laugh",
            "SayoriDinner sayori_blush smile",
            "SayoriDinner sayori_blush smile_side",
            "SayoriDinner sayori_blush smile_closed",
            "SayoriDinner sayori_blush neutral",
            "SayoriDinner sayori_blush neutral_side",
            "SayoriDinner sayori_blush smirk",
            "SayoriDinner sayori_blush concerned",
            "SayoriDinner sayori_blush concerned_closed",
            "SayoriDinner sayori_blush surprised",
            "SayoriDinner sayori_blush stern",
            "SayoriDinner sayori_blush stern_side",
            "SayoriDinner sayori_blush angry",
            "SayoriDinner sayori_blush cry_open1",
            "SayoriDinner sayori_blush cry_closed",
            "SayoriDinner sayori_blush laugh_cry",
            "SayoriDinner sayori_blush cry_open2",
            "SayoriDinner sayori_blush cry_smile",
        ],
        "sayori alter hug single image": [
            #This is a single image CG
        ],
        "akiko slapped": [
            "AkikoSlapped slapped",
            "AkikoSlapped sorry",
        ],
        "rooftop reversal": [
            overlap_images("cg rooftop day", "RoofHiroko handcheek neutral", "RoofNozomi handsdown smile", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek surprised", "RoofNozomi handsdown panicked_right", "RoofSayori leanforward awe"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback surprised", "RoofNozomi handsdown panicked_right", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback smile", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback rolleyes", "RoofHiroko leanback smile", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback frown_left", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback rolleyes", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback sigh", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback sigh", "RoofHiroko leanback neutral", "RoofNozomi handsdown worried_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback rolleyes", "RoofHiroko leanback neutral", "RoofNozomi handsdown worried_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback rolleyes", "RoofNozomi handsdown worried_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback concerned_left", "RoofHiroko leanback rolleyes", "RoofNozomi handsdown worried_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral", "RoofHiroko leanback rolleyes", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback smirk", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral_right", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback smirk", "RoofHiroko handcheek neutral", "RoofNozomi handsdown neutral", "RoofSayori leanforward smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback smirk", "RoofHiroko handcheek neutral", "RoofNozomi handsdown sigh", "RoofSayori leanforward smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback grin", "RoofHiroko handcheek neutral", "RoofNozomi handsdown sigh", "RoofSayori leanforward smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback grin", "RoofHiroko leanback neutral", "RoofNozomi handsdown worried_right", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko leanback neutral", "RoofNozomi handsdown worried_right", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko leanback rolleyes", "RoofNozomi handsdown worried_right", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko handcheek neutral", "RoofNozomi handsdown worried_right", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko handcheek neutral", "RoofNozomi handsdown panicked_right", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback grin", "RoofHiroko handcheek neutral", "RoofNozomi handsdown panicked_right blush", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown worried_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko handcheek worried", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown neutral_left blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback smirk", "RoofHiroko leanback neutral", "RoofNozomi handsdown neutral blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback smirk", "RoofHiroko handcheek neutral", "RoofNozomi handsdown neutral blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko handcheek neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofRisa leanback surprised", "RoofHiroko leanback neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral", "RoofHiroko leanback neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko leanback neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback smirk_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback grin", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile", "RoofHiroko handcheek neutral", "RoofNozomi handsdown irritated blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko handcheek neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko handcheek neutral", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile_left", "RoofHiroko leanback worried_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_left blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofRisa leanback concerned", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofRisa leanback grin", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofRisa leanback smile", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown irritated blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback neutral_left", "RoofNozomi handsdown growl blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofRisa leanback neutral_left", "RoofHiroko leanback worried_left", "RoofNozomi handsdown growl blush", "RoofSayori leanback shocked"),
            overlap_images("cg rooftop day", "RoofRisa leanback frown_left", "RoofHiroko leanback worried_left", "RoofNozomi handsdown growl blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback frown_left", "RoofHiroko leanback worried_left", "RoofNozomi handsdown frown_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback frown_left", "RoofHiroko leanback worried_left", "RoofNozomi handsdown angry_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback growl", "RoofHiroko leanback worried_left", "RoofNozomi handsdown angry_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback growl", "RoofHiroko leanback worried_left", "RoofNozomi handsdown growl_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback growl", "RoofHiroko leanback worried_right", "RoofNozomi handsdown growl_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback frown_left", "RoofHiroko leanback worried_right", "RoofNozomi handsdown growl_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofRisa leanback growl", "RoofHiroko leanback worried_right", "RoofNozomi handsdown growl_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko leanback surprised", "RoofNozomi handsdown worried_right", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko leanback worried_left", "RoofNozomi handsdown frown", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko leanback worried_left", "RoofNozomi handsdown regretful", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofNozomi handsdown regretful", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofNozomi handsdown regretful", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofNozomi handsdown crying", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofNozomi handsdown crying", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofNozomi handsdown crying", "RoofSayori leanforward frown"),
            overlap_images("cg rooftop day", "RoofNozomi handsdown crying"),
            overlap_images("cg rooftop day", "RoofNozomi handsdown frown"), 
        ],
        "nozomi threatening": [
            "NozomiThreatening arm_up frown scared",
            "NozomiThreatening arm_up neutral scared",
            "NozomiThreatening arm_up arrogant scared",
            "NozomiThreatening arm_up growl scared",
            "NozomiThreatening arm_up growl blush scared",
            "NozomiThreatening arm_up smirk blush scared",
            "NozomiThreatening arm_up smirk blush relaxed",
            "NozomiThreatening arm_up angry blush relaxed",
            "NozomiThreatening arm_up neutral relaxed",
            "NozomiThreatening arm_up fearful relaxed",
            "NozomiThreatening arm_down cry relaxed",
            "NozomiThreatening arm_down cry surprised",
            "NozomiThreatening arm_down fearful surprised",
        ],
        "nozomi sorry": [
            "NozomiSorry closed",
            "NozomiSorry open",
        ],
        "nozomi couch hypno": [
            "NozomiCouchHypno k_hand_down n_hand_down neutral",
            "NozomiCouchHypno k_hand_down n_hand_down smile",
            "NozomiCouchHypno k_hand_down n_hand_down sad",
            "NozomiCouchHypno k_hand_down n_hand_down frown",
            "NozomiCouchHypno k_hand_down n_hand_forehead frown",
            "NozomiCouchHypno k_hand_down n_hand_down happy",
            "NozomiCouchHypno k_hand_down n_hand_down sigh",
            "NozomiCouchHypno k_hand_down n_hand_down surprised",
            "NozomiCouchHypno k_hand_down n_hand_down angry",
            "NozomiCouchHypno k_hand_down n_hand_down glare",
        ],
        #Page 17
        "nozomi tortured tickle": [
            "NozomiTortured_Tickle feet_socks nozomi1 k1_neutral n1_sleepy",
            "NozomiTortured_Tickle feet_socks nozomi1 k1_neutral n1_waking",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_neutral n2_grimace",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_neutral n2_pain",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_neutral n2_worried",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_worried",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_fear",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_fear blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_worried blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_smirk n2_worried blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_smirk n2_sigh blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_smirk n2_surprised blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_smirk n2_fear blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_fright blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_smug n2_angry blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_surprised n2_angry blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_neutral n2_grimace blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_frown n2_grimace blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_frown n2_fear blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_frown n2_worried blush2",
            "NozomiTortured_Tickle feet_socks nozomi2 k1_smirk n2_fright blush2",
            "NozomiTortured_Tickle feet_socks nozomi2_tickle k1_smirk n2_fright blush2",
            "NozomiTortured_Tickle feet_socks nozomi2_tickle lines2 k1_smirk n2_grimace blush2",
            "NozomiTortured_Tickle feet_socks nozomi2_tickle lines2 k1_smirk n2_fear blush2",
            "NozomiTortured_Tickle feet_socks nozomi2_tickle lines2 k1_neutral n2_pain blush2",
            "NozomiTortured_Tickle feet_socks nozomi2_tickle k1_frown n2_pain blush2",
            "NozomiTortured_Tickle feet_socks nozomi2_tickle k1_frown n2_sigh blush2",
            "NozomiTortured_Tickle feet_socks nozomi1_tickle k1_frown n1_waking blush1",
            "NozomiTortured_Tickle feet_rest nozomi1_tickle k1_frown n1_waking blush1",
            "NozomiTortured_Tickle feet_rest nozomi2_tickle  k1_frown n2_worried blush2",
            "NozomiTortured_Tickle feet_rest nozomi2_tickle k1_smug n2_worried blush2",
            "NozomiTortured_Tickle feet_clenched nozomi2_tickle lines2 k1_smug n2_pain blush2",
            "NozomiTortured_Tickle feet_clenched nozomi2_tickle lines2 k1_smug n2_grin blush2",
            "NozomiTortured_Tickle feet_clenched nozomi2_tickle k1_surprised n2_fright blush2",
            "NozomiTortured_Tickle feet_rest nozomi2 k1_neutral n2_worried blush2",
            "NozomiTortured_Tickle feet_rest nozomi2 k1_frown n2_worried blush2",
            "NozomiTortured_Tickle feet_rest nozomi2 k1_growl n2_worried blush2",
            "NozomiTortured_Tickle feet_rest nozomi3 k2_growl n2_fright blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_growl n2_grimace blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_growl n2_pain blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_growl n2_grin blush2",
            "NozomiTortured_Tickle feet_clenched nozomi3 lines3 k2_growl n2_laugh_happy blush2",
            "NozomiTortured_Tickle feet_clenched nozomi3 lines3 k2_growl n2_pain blush2",
            "NozomiTortured_Tickle feet_clenched nozomi3 k2_talk n2_pain blush2",
            "NozomiTortured_Tickle feet_clenched nozomi3 k2_talk n2_fright blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_frown n2_pain blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_frown n2_grin blush2",
            "NozomiTortured_Tickle feet_clenched nozomi3 lines3 k2_frown n2_laugh blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_frown n2_laugh blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_growl n2_laugh blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_growl n2_laugh_mad blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 lines3 k2_frown n2_laugh_mad blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 sweat3 lines3 k2_frown n2_laugh_mad blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 sweat3 lines3 k2_smirk n2_laugh_mad blush2",
            "NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smug n2_laugh_mad blush2",
            "NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smug n2_laugh_cry blush2",
            "NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smirk n2_laugh_cry blush2",
            "NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smirk n2_laugh_mad blush2",
            "NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smirk n2_laugh_insane blush2",
            "NozomiTortured_Tickle feet_squirm nozomi2_tickle sweat2 lines2 k1_smirk n2_laugh_tranced blush2",
            "NozomiTortured_Tickle feet_squirm nozomi3 sweat3 lines3 k2_smirk n2_laugh_tranced blush2",
            "NozomiTortured_Tickle feet_rest nozomi1 sweat1 k1_smug n1_mindless blush1",
            "NozomiTortured_Tickle feet_rest nozomi1 sweat1 k1_smile n1_mindless blush1",
            "NozomiTortured_Tickle feet_rest nozomi1 sweat1 k1_smile n1_bliss blush1",
        ],
        "nozomi tortured spank": [
            "NozomiTortured_Spank feet_rest nozomi1 underwear1_up n1_sleepy k_neutral",
            "NozomiTortured_Spank feet_rest nozomi1 underwear1_up n1_waking k_neutral",
            "NozomiTortured_Spank feet_tense nozomi2 underwear2_up n2_anxious k_neutral",
            "NozomiTortured_Spank feet_tense nozomi2 underwear2_up lines n2_grimace k_neutral",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up lines n2_grimace k_neutral",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_worried k_neutral",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_worried k_smug",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_worried k_smug blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fear k_smug blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_worried k_smirk blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_sigh k_smirk blush2",
            "NozomiTortured_Spank feet_rest nozomi2_rub underwear2_up n2_surprised k_smirk blush2",
            "NozomiTortured_Spank feet_rest nozomi2_rub underwear2_up n2_worried k_smirk blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fear k_smirk blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fear k_wicked blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fright k_wicked blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_angry k_smug blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_angry k_surprised blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_anxious k_neutral blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_anxious k_frown blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fear k_frown blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_worried k_frown blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_fright k_smirk blush2",
            "NozomiTortured_Spank feet_tense nozomi2_raised underwear2_up n2_fright k_wicked blush2",
            "NozomiTortured_Spank feet_tense nozomi2_spank underwear2_up n2_fright k_wicked blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up lines n2_grimace k_smug blush2",
            "NozomiTortured_Spank feet_tense nozomi2_raised underwear2_up lines n2_fear k_smug blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_up lines n2_grimace k_smug blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised underwear2_up lines n2_fear k_smug blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_up lines n2_anxious k_smirk blush2",
            "NozomiTortured_Spank feet_rest nozomi2_raised underwear2_up lines n2_anxious k_smirk blush2",
            "NozomiTortured_Spank feet_rest nozomi2_raised underwear2_up lines n2_fear k_smirk blush2",
            "NozomiTortured_Spank feet_rest nozomi2_raised underwear2_up lines n2_fear k_talk blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_up lines n2_shout k_smirk blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_up n2_grimace k_smirk blush2",
            "NozomiTortured_Spank feet_rest nozomi1_rub underwear1_up n1_worried k_smirk blush1",
            "NozomiTortured_Spank feet_rest nozomi1_rub underwear1_down n1_worried k_smirk blush1",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_down lines n2_fright k_smirk blush2",
            "NozomiTortured_Spank feet_tense nozomi2_raised underwear2_down n2_worried k_talk blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_down lines n2_shout k_talk blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_rub underwear2_down n2_anxious k_smug blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_down n2_anxious k_smirk blush2",
            "NozomiTortured_Spank feet_tense nozomi2_raised underwear2_down n2_fear k_smirk blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_down lines n2_scream k_surprised blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_down n2_fright k_neutral blush2",
            "NozomiTortured_Spank feet_tense nozomi2_rub underwear2_down n2_fright k_frown blush2",
            "NozomiTortured_Spank feet_tense nozomi2_raised underwear2_down n2_fear k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank underwear2_down lines n2_shout k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised underwear2_down lines n2_shout k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised underwear2_down lines n2_fright k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red2 underwear2_down lines n2_scream k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_rub red2 underwear2_down lines n2_scream k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised red2 underwear2_down lines n2_scream k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red2 underwear2_down lines n2_grimace k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised red2 underwear2_down lines n2_grimace k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red2 underwear2_down lines n2_sigh k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_rub red2 underwear2_down lines n2_fear k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_rub red2 underwear2_down lines n2_fright k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised red2 underwear2_down lines n2_fright k_talk blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down lines n2_shout k_talk blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down lines n2_pain k_talk blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down lines n2_pain k_frown blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down lines n2_crying k_frown blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down lines n2_pain k_frown blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down lines n2_agony k_frown blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down lines n2_agony k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down lines n2_agony k_growl blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down lines n2_agony k_frown blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down sweat2 lines n2_agony k_frown blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down sweat2 lines n2_agony k_smirk blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down sweat2 lines n2_agony k_smirk blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down sweat2 lines n2_pain k_smirk blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down sweat2 lines n2_pain k_wicked blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down sweat2 lines n2_insane k_wicked blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_raised red3 underwear2_down sweat2 lines n2_insane k_wicked blush2",
            "NozomiTortured_Spank feet_squirm nozomi2_spank red3 underwear2_down sweat2 lines n2_tranced k_wicked blush2",
            "NozomiTortured_Spank feet_rest nozomi1_rub red1 underwear1_down sweat1 n1_mindless k_wicked blush1",
            "NozomiTortured_Spank feet_rest nozomi1_rub red1 underwear1_down sweat1 n1_bliss k_smirk blush1",
            "NozomiTortured_Spank feet_rest nozomi1_rub red1 underwear1_down sweat1 n1_bliss k_smug blush1",
            "NozomiTortured_Spank feet_rest nozomi1_rub red1 underwear1_down sweat1 n1_bliss k_smile blush1",
            "NozomiTortured_Spank feet_rest nozomi1_rub red1 underwear1_down sweat1 n1_smile k_smile blush1",
        ],
        "hiroko cam 4": [
            "HirokoCam4 h1 h_neutral h_mask n1 n_neutral n_mask",
            "HirokoCam4 h1 h_smile h_mask n1 n_smile n_mask",
            "HirokoCam4 h2 h_happy h_mask n1 n_smile n_mask",
            "HirokoCam4 h2 h_happy h_mask n1 n_happy n_mask",
            "HirokoCam4 h2 h_happy h_mask n1 n_confused n_mask",
            "HirokoCam4 h1 h_worried h_mask n2 n_irritated n_mask",
            "HirokoCam4 h1 h_worried h_mask n2 n_rolleyes n_mask",
            "HirokoCam4 h1 h_neutral h_mask n2 n_neutral n_mask",
            "HirokoCam4 h1 h_smile h_mask n2 n_neutral n_mask",
            "HirokoCam4 h1 h_sleep h_mask n1 n_sleep n_mask",
            "HirokoCam4 h1 h_sleep h_mask n1 n_sleeptalk n_mask",
            "HirokoCam4 h1 h_sleep h_mask n1 n_irritated n_mask",
            "HirokoCam4 h1 h_sleep h_mask n1 n_sleeptalk_concerned n_mask",
            "HirokoCam4 h1 h_sleep h_mask n1 n_happy n_mask",
            "HirokoCam4 h1 h_sleeptalk h_mask n1 n_happy n_mask",
            "HirokoCam4 h1 h_waking h_mask n1 n_waking n_mask",
            "HirokoCam4 h1 h_smile n1 n_smile",
            "HirokoCam4 h1 h_smile n1 n_happy",
            "HirokoCam4 h1 h_smile n1 n_laugh n_blush1",
            "HirokoCam4 h1 h_smile n1 n_smile n_blush1",
            "HirokoCam4 h2 h_laugh h_blush1 n1 n_smile n_blush1",
            "HirokoCam4 h2 h_happy h_blush1 n1 n_smile n_blush1",
            "HirokoCam4 h1 h_sleep n1 n_sleep",
            "HirokoCam4 h1 h_sleeptalk n1 n_sleeptalk",
            "HirokoCam4 h1 h_waking n1 n_waking",
            "HirokoCam4 h1 h_waking n1 n_confused",
            "HirokoCam4 h1 h_confused n1 n_confused",
            "HirokoCam4 h1 h_worried n1 n_confused",
            "HirokoCam4 h3 n1 n_confused",
            "HirokoCam4 h3 n3",
            "HirokoCam4 h3 h_blush2 n3 n_blush2",
            "HirokoCam4 h1 h_scream h_blush1 n1 n_scream n_blush1",
            "HirokoCam4 h1 h_scream h_blush1 n1 n_angry n_blush1",
            "HirokoCam4 h1 h_sleeptalk n1 n_sleeptalk",
            "HirokoCam4 h1 h_sleep n1 n_sleep",
            "HirokoCam4 h1 h_sleep h_mask n1 n_sleep n_mask",
            "HirokoCam4 h1 h_sleeptalk h_mask n1 n_sleeptalk n_mask",
            "HirokoCam4 h1 h_waking h_mask n1 n_waking n_mask",
            "HirokoCam4 h1 h_smile h_mask n1 n_smile n_mask",
            "HirokoCam4 h1 h_smile h_mask n1 n_happy n_mask",
            "HirokoCam4 h1 h_laugh h_mask n1 n_happy n_mask",
        ],
        "hiroko cam 3": [
            "HirokoCam3 pose1 n_neutral h_smile",
            "HirokoCam3 pose1 n_surprised h_smile",
            "HirokoCam3 pose1 n_neutral h_smile_light",
            "HirokoCam3 pose1 n_neutral h_dazed",
            "HirokoCam3 pose1 n_neutral h_dazed_light",
            "HirokoCam3 pose1 n_neutral h_sleepy",
            "HirokoCam3 pose1 n_neutral h_sleepy_light",
            "HirokoCam3 pose1 n_neutral h_sleep",
            "HirokoCam3 pose2 n_neutral",
            "HirokoCam3 pose3",
            "HirokoCam3 pose4",
            "HirokoCam3 pose1 n_awe h_sleep",
            "HirokoCam3 pose1 n_concerned h_sleep",
            "HirokoCam3 pose1 n_surprised h_sleep",
            "HirokoCam3 pose1 n_anxious blush h_sleep",
            "HirokoCam3 pose1 n_concerned blush h_sleep",
        ],
        "nozo cam hypno": [
            "NozoCamHypno h_sleep head_down",
            "NozoCamHypno h_sleep head_up n_anxious",
            "NozoCamHypno h_sleep head_up n_curious",
            "NozoCamHypno h_sleep head_up n_anxious hand",
            "NozoCamHypno h_sleep head_up n_anxious_light hand",
            "NozoCamHypno h_sleep head_up n_awe hand",
            "NozoCamHypno h_sleep head_up n_awe_light hand",
            "NozoCamHypno h_sleep head_up n_curious hand",
            "NozoCamHypno h_sleep head_up n_curious_light hand",
            "NozoCamHypno h_sleep head_up n_anxious hand",
            "NozoCamHypno h_sleep head_up n_anxious_light hand",
            "NozoCamHypno h_sleep head_up n_sleepysmile hand",
            "NozoCamHypno h_sleep head_up n_sleepysmile_light hand",
            "NozoCamHypno h_sleep head_up n_sleep hand",
            "NozoCamHypno h_sleep head_up n_sleep",
            "NozoCamHypno h_sleeptalk head_up n_sleeptalk",
            "NozoCamHypno h_sleep head_up n_sleep",
            "NozoCamHypno h_waking head_up n_sleepy",
            "NozoCamHypno h_waking head_up n_curious",
            "NozoCamHypno h_curious head_up n_curious",
        ],
        "hiroko cam kiss": [
            "HirokoCamKiss pose1",
            "HirokoCamKiss pose2 kissing",
            "HirokoCamKiss pose2 waking",
            "HirokoCamKiss pose3",
        ],
        "hiroko cam 5": [
            "HirokoCam5 h1 hm1 h_smile1 n1 nm1 n_pout1",
            "HirokoCam5 h1 hm1 h_smile1 n1 nm1 n_confused1",
            "HirokoCam5 h2 hm2 h_confused2 n1 nm1 n_frown1",
            "HirokoCam5 h2 hm2 h_frown2 n1 nm1 n_frown1",
            "HirokoCam5 h2 hm2 h_frown2 n1 nm1 n_surprised1",
            "HirokoCam5 h2 hm2 h_frown2 n1 nm1 n_derp1",
            "HirokoCam5 h2 hm2 h_confused2 n1 nm1 n_derp1",
            "HirokoCam5 h1 hm1 h_confused1 n1 nm1 n_derp1",
            "HirokoCam5 h2 hm2 h_smile2 n1 nm1 n_derp1",
            "HirokoCam5 h2 hm2 h_laugh2 n1 nm1 n_derp1",
            "HirokoCam5 h2 hm2 h_smirk2 n1 nm1 n_derp1",
            "HirokoCam5 h4 hm4 h_smirk4 nm1 n_derp1",
            "HirokoCam5 h4 hm4 h_laugh4 nm1 n_derp1",
            "HirokoCam5 h2 hm2 h_laugh2 n3 nm1 n_derp1",
            "HirokoCam5 h2 hm2 h_smile2 n3 nm1 n_derp1",
            "HirokoCam5 h2 hm2 h_smile2 n3 nm1 n_disgust1",
            "HirokoCam5 h2 hm2 h_smile2 n1 nm1 n_disgust1",
            "HirokoCam5 h2 hm2 h_laugh2 n1 nm1 n_disgust1",
            "HirokoCam5 h2 hm2 h_smile2 n2 nm2 n_confused2",
            "HirokoCam5 h2 hm2 h_smirk2 n2 nm2 n_confused2",
            "HirokoCam5 h2 hm2 h_smirk2 n2 nm2 n_frown2",
            "HirokoCam5 h2 hm2 h_surprised2 n2 nm2 n_frown2",
            "HirokoCam5 h2 hm2 h_derp2 n2 nm2 n_frown2",
            "HirokoCam5 h2 hm2 h_derp2 n2 nm2 n_smirk2",
            "HirokoCam5 h2 hm2 h_derp2 n4 nm2 n_smirk2",
            "HirokoCam5 h3 hm3 h_derp3 n4 nm2 n_smirk2",
            "HirokoCam5 h3 hm3 h_derp3 n2 nm2 n_happy2",
            "HirokoCam5 h3 hm3 h_derp3 n2 nm2 n_laugh2",
            "HirokoCam5 h3 hm3 h_derp3 n1 nm1 n_frown1",
            "HirokoCam5 h3 hm3 h_derp3 n1 nm1 n_pout1",
            "HirokoCam5 h1 hm1 h_disgust1 n2 nm2 n_happy2",
            "HirokoCam5 h1 hm1 h_disgust1 n2 nm2 n_laugh2",
            "HirokoCam5 h2 hm2 h_angry2 n2 nm2 n_laugh2",
            "HirokoCam5 h2 hm2 h_angry2 n2 nm2 n_derp2",
            "HirokoCam5 h2 hm2 h_smirk2 n2 nm2 n_derp2",
            "HirokoCam5 h2 hm2 h_smirk2 n1 nm1 n_frown1",
            "HirokoCam5 h2 hm2 h_frown2 n1 nm1 n_frown1",
            "HirokoCam5 h2 hm2 h_frown2 n2 nm2 n_frown2",
            "HirokoCam5 h2 hm2 h_derp2 n2 nm2 n_derp2",
            "HirokoCam5 h3 hm3 h_derp3 n3 nm1 n_derp1",
            "HirokoCam5 h1 hm1 h_sleep1 n1 nm1 n_sleep1",
            "HirokoCam5 h1 hm1 h_waking1 n1 nm1 n_waking1",
            "HirokoCam5 h1 hm1 h_happy1 n1 nm1 n_happy1",
            "HirokoCam5 h1 hm1 h_happy1 n1 nm1 n_smile1",
            "HirokoCam5 h1 hm1 h_smile1 n1 nm1 n_smile1",
            "HirokoCam5 h1 hm1 h_entrancedtalk1 n1 nm1 n_entrancedtalk1",
            "HirokoCam5 h1 hm1 h_entranced1 n1 nm1 n_entranced1",
            "HirokoCam5 h1 h_smile1 n1 n_confused1",
            "HirokoCam5 h2 h_laugh2 n1 n_confused1",
            "HirokoCam5 h2 h_laugh2 n2 n_happy2",
            "HirokoCam5 h2 h_smirk2 n2 n_happy2",
            "HirokoCam5 h2 h_smirk2 n1 n_pout1",
            "HirokoCam5 h2 h_smirk2 n1 n_neutral1",
            "HirokoCam5 h1 h_smile1 n1 n_neutral1",
            "HirokoCam5 h1 h_smile1 n1 n_frown1",
            "HirokoCam5 h1 h_smile1 n1 n_smile1",
            "HirokoCam5 h1 h_smile1 n1 n_disgust1",
            "HirokoCam5 h1 h_confused1 n1 n_smile1",
            "HirokoCam5 h1 h_disgust1 n1 n_smile1",
            "HirokoCam5 h1 h_happy1 n1 n_neutral1",
            "HirokoCam5 h1 h_happy1 n2 n_confused2",
            "HirokoCam5 h2 h_confused2 n2 n_confused2",
            "HirokoCam5 h2 h_confused2 n2 n_worried2",
            "HirokoCam5 h2 h_smile2 n2 n_worried2",
            "HirokoCam5 h2 h_smile2 n2 n_smile2",
        ],
        "hiroko nozomi phone": [
            "HirokoNozomiPhone h_shocked n_shocked",
            "HirokoNozomiPhone h_worried n_shocked",
            "HirokoNozomiPhone h_worried n_scared",
        ],
        "reversal bad end": [
            "ReversalBadEnd neutral",
            "ReversalBadEnd worried",
            "ReversalBadEnd curious",
            "ReversalBadEnd smile",
            "ReversalBadEnd wicked",
        ],
        "reversal good end": [
            At("ReversalGoodEnd bg1 sayori s_smile nozomi n_smile kyou k_smile hiroko h_smile risa r_neutral", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_smile nozomi n_smile kyou k_smile hiroko h_smile risa r_sigh", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_neutral hiroko h_concerned risa r_sigh", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_neutral hiroko h_surprised risa r_neutral_side", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_smirk nozomi n_neutral_side kyou k_neutral hiroko h_surprised risa r_neutral_side", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_smirk nozomi n_neutral_side kyou k_neutral hiroko h_angry risa r_neutral_side", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_happy nozomi n_neutral_side kyou k_neutral hiroko h_angry risa r_neutral_side", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_happy nozomi n_neutral_side kyou k_neutral hiroko h_angry h_blush risa r_neutral_side", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_happy nozomi n_neutral_side kyou k_neutral hiroko h_angry h_blush risa r_neutral", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_neutral hiroko h_concerned h_blush risa r_neutral", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_neutral hiroko h_concerned h_blush risa r_smug", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_concerned hiroko h_concerned h_blush risa r_smug", galzoomout),
            At("ReversalGoodEnd bg1 sayori s_neutral nozomi n_neutral_side kyou k_concerned hiroko h_concerned risa r_smile_side", galzoomout),
            At("ReversalGoodEnd bg2 sayori s_neutral nozomi n_nervous kyou k_neutral_side hiroko h_smile risa r_smile_side", galzoomout),
            At("ReversalGoodEnd bg2 sayori s_neutral nozomi n_nervous kyou k_smile hiroko h_smile risa r_smile_side", galzoomout),
            At("ReversalGoodEnd bg2 sayori s_neutral nozomi n_neutral_side kyou k_smile hiroko h_smile risa r_smile_side", galzoomout),
            At("ReversalGoodEnd bg2 sayori s_neutral nozomi n_neutral_side kyou k_smug hiroko h_smile risa r_smile_side", galzoomout),
            At("ReversalGoodEnd bg2 sayori s_curious nozomi n_neutral_side kyou k_smug hiroko h_smile risa r_smile_side", galzoomout),
            At("ReversalGoodEnd bg2 sayori s_curious nozomi n_smile kyou k_smile hiroko h_smile risa r_smile_side", galzoomout),
            At("ReversalGoodEnd bg2 sayori s_smirk nozomi n_smile kyou k_smile hiroko h_smile risa r_smile_side", galzoomout),
            At("ReversalGoodEnd bg2 sayori s_smirk nozomi n_happy n_blush kyou k_smile hiroko h_smile risa r_smile_side", galzoomout),
            At("ReversalGoodEnd bg2 sayori s_smile nozomi n_smile n_blush kyou k_smile hiroko h_smile risa r_smile", galzoomout),
        ],
        #Page 18
        "sayori alter confrontation": [
            "Sayori_Alter_Confrontation1",
            "Sayori_Alter_Confrontation1 sigh",
            "Sayori_Alter_Confrontation1 girls2 sad sigh",
            "Sayori_Alter_Confrontation1 girls2 sad smile",
        ],
        "akiko intro2": [
            "AkikoIntro2 confused",
            "AkikoIntro2 surprised",
            "AkikoIntro2 happy",
        ],
        "akiko kendo": [
            "AkikoKendo akiko1 frown",
            "AkikoKendo akiko1 calm",
            "AkikoKendo akiko1 shout",
            "AkikoKendo akiko1 angry",
            "AkikoKendo akiko1 smirk",
            "AkikoKendo akiko1 confused",
            "AkikoKendo akiko1 nervous",
            "AkikoKendo akiko2 nervous",
        ],
        "sword strike single image": [
            #This one is a single image
        ],
        "akiko cornered": [
            "AkikoCornered nervous",
            "AkikoCornered nervous_light",
            "AkikoCornered sleepy",
            "AkikoCornered sleepy_light",
            "AkikoCornered tranced",
            "AkikoCornered tranced_light",
            "AkikoCornered sleep",
        ],
        "redemption phone eve": [
            "RedemptionPhoneEve sleep glasses kyou",
            "RedemptionPhoneEve frown glasses kyou",
            "RedemptionPhoneEve sleep glasses kyou",
            "RedemptionPhoneEve sleep glasses_sp kyou_phone",
            "RedemptionPhoneEve frown_sp glasses_sp kyou_phone",
            "RedemptionPhoneEve quizzical_sp glasses_sp kyou_phone",
            "RedemptionPhoneEve tired_sp glasses_sp kyou_phone",
            "RedemptionPhoneEve blanktalk_sp glasses_sp kyou_phone",
            "RedemptionPhoneEve blank_sp glasses_sp kyou_phone",
            "RedemptionPhoneEve sleep glasses_sp kyou_phone",
            "RedemptionPhoneEve sleep glasses kyou",
            "RedemptionPhoneEve happy glasses kyou",
            "RedemptionPhoneEve giggle glasses kyou",
            "RedemptionPhoneEve laugh glasses kyou",
            "RedemptionPhoneEve smile glasses kyou",
            "RedemptionPhoneEve laugh glasses kyou",
            "RedemptionPhoneEve quizzical_up glasses kyou",
            "RedemptionPhoneEve quizzical glasses kyou",
            "RedemptionPhoneEve happy blush glasses kyou",
            "RedemptionPhoneEve smile blush glasses kyou",
            "RedemptionPhoneEve laugh blush glasses kyou",
            "RedemptionPhoneEve quizzical_up blush glasses kyou",
            "RedemptionPhoneEve smile blush glasses kyou_phone",
            "RedemptionPhoneEve quizzical blush glasses kyou_phone",
            "RedemptionPhoneEve quizzical_up blush glasses kyou_phone",
            "RedemptionPhoneEve happy blush glasses kyou_phone",
            "RedemptionPhoneEve quizzical_sp blush glasses_sp kyou_phone",
            "RedemptionPhoneEve quizzical_sp glasses_sp kyou_phone",
            "RedemptionPhoneEve blank_sp glasses_sp kyou_phone",
            "RedemptionPhoneEve blank glasses kyou",
            "RedemptionPhoneEve tired blush glasses kyou",
            "RedemptionPhoneEve giggle blush glasses kyou",
        ],
        "voodoo phone": [
            "VoodooPhone akiko1_uniform_socks surprised phone index_down",
            "VoodooPhone akiko1_uniform_socks surprised blush1 phone index_down",
            "VoodooPhone akiko1_uniform_socks shy_left blush1 phone index_down",
            "VoodooPhone akiko1_uniform_socks shy_closed blush1 phone index_down",
            "VoodooPhone akiko1_uniform_socks giggle blush1 phone index_down",
            "VoodooPhone akiko1_uniform_socks shy blush1 phone index_down",
            "VoodooPhone akiko1_uniform_socks shy blush1 phone index_up",
            "VoodooPhone akiko2_uniform_socks happy blush2 phone index_up",
            "VoodooPhone akiko2_uniform_socks wink blush2 phone index_up",
            "VoodooPhone akiko2_uniform_socks sheepish_left blush2 phone index_up",
            "VoodooPhone akiko2_uniform_socks sheepish blush2 phone index_down",
            "VoodooPhone akiko2_uniform_socks sheepish blush2 phone index_down hand_down",
            "VoodooPhone akiko1_uniform_socks shocked blush1 phone index_down hand_down",
            "VoodooPhone akiko1_uniform_socks giggle blush1 phone index_down hand_down",
            "VoodooPhone akiko3_uniform_socks straining blush3 quivering1 phone index_down hand_down",
            "VoodooPhone akiko3_uniform_socks laugh blush3 quivering1 phone index_down hand_down",
            "VoodooPhone akiko3_uniform_socks laugh blush3 quivering1",
            "VoodooPhone akiko4_uniform_socks straining blush3 quivering2",
            "VoodooPhone akiko4_uniform_socks laugh blush3 quivering2",
            "VoodooPhone akiko4_uniform_socks laugh blush3 quivering2 phone index_down hand_down",
            "VoodooPhone akiko4_uniform_socks grin blush3 quivering2 phone index_down hand_down",
            "VoodooPhone akiko3_uniform_socks laugh blush3 quivering1 phone index_down",
            "VoodooPhone akiko4_uniform_socks grin blush3 phone index_down",
            "VoodooPhone akiko4_uniform_socks smile blush3",
            "VoodooPhone akiko1_uniform_socks shy blush1",
            "VoodooPhone akiko1_uniform_socks shy_left blush1",
            "VoodooPhone akiko2_uniform_socks sheepish blush2",
            "VoodooPhone akiko1_uniform_socks giggle blush1",
            "VoodooPhone akiko1_uniform_socks surprised blush1",
            "VoodooPhone akiko1_uniform_socks surprised blush1 phone index_down hand_down",
            "VoodooPhone akiko2_uniform_socks happy blush2 phone index_down hand_down",
            "VoodooPhone akiko2_uniform_socks sheepish blush2 phone index_down hand_down",
            "VoodooPhone akiko1_uniform_socks giggle blush1 phone index_down hand_down",
            "VoodooPhone akiko2_uniform_socks wink blush2 phone index_down hand_down",
            "VoodooPhone akiko1_uniform_socks shy_closed blush1 phone index_down hand_down",
            "VoodooPhone akiko1_uniform_socks shy blush1 phone index_down hand_down",
            "VoodooPhone akiko2_uniform_socks sheepish blush2 phone index_down hand_up",
            "VoodooPhone akiko1_uniform_socks shocked blush1deep phone index_down hand_up",
            "VoodooPhone akiko2_uniform_socks uncomfortable blush2deep phone index_down hand_up",
            "VoodooPhone akiko2_uniform_socks uncomfortable_left blush2deep phone index_down hand_up",
            "VoodooPhone akiko2_uniform_socks uncomfortable blush2deep phone index_down",
            "VoodooPhone akiko1_uniform_socks shy_left blush1 phone index_down",
        ],
        "hiroko scared single image": [
            #This one is a single image
        ],
        "bathroom ambush": [
            "BathroomAmbush akiko_up surprised glasses_sp kyou_up",
            "BathroomAmbush akiko_up furious glasses_sp kyou_up",
            "BathroomAmbush akiko_up angry glasses_sp kyou_up",
            "BathroomAmbush akiko_up anxious glasses_sp kyou_up",
            "BathroomAmbush akiko_down anxious glasses_sp kyou_up",
            "BathroomAmbush akiko_down sleepytalk glasses_sp kyou_up",
            "BathroomAmbush akiko_down sleepy glasses_sp kyou_up",
            "BathroomAmbush akiko_down sleepytalk glasses_sp kyou_down",
            "BathroomAmbush akiko_down sleepytalk blush glasses_sp kyou_down",
            "BathroomAmbush akiko_down entrancedtalk_sp glasses_sp kyou_down",
            "BathroomAmbush akiko_down entranced_sp glasses_sp kyou_down",
            "BathroomAmbush akiko_down entranced glasses",
            "BathroomAmbush akiko_down entrancedtalk glasses",
        ],
        #Page 19
        "voodoo phone2": [
            "VoodooPhone akiko1_underwear giggle blush1",
            "VoodooPhone akiko2_underwear sheepish_left blush2",
            "VoodooPhone akiko1_underwear shy_closed blush1",
            "VoodooPhone akiko2_underwear uncomfortable blush2",
            "VoodooPhone akiko1_underwear surprised blush1",
            "VoodooPhone akiko1_underwear shy_left blush1",
            "VoodooPhone akiko2_underwear sheepish blush2",
            "VoodooPhone akiko1_underwear shy blush1",
            "VoodooPhone akiko2_underwear happy blush2",
            "VoodooPhone akiko2_underwear wink blush2",
            "VoodooPhone akiko1_underwear shy_closed2 blush1",
            "VoodooPhone akiko2_underwear uncomfortable_left blush2",
            "VoodooPhone akiko1_underwear shy",
            "VoodooPhone akiko2_underwear sheepish_left",
            "VoodooPhone akiko1_underwear shy_closed",
            "VoodooPhone akiko2_underwear sheepish",
            "VoodooPhone akiko2_underwear happy",
            "VoodooPhone akiko2_underwear uncomfortable",
            "VoodooPhone akiko1_underwear shy_left",
            "VoodooPhone akiko1_underwear giggle",
            "VoodooPhone akiko2_underwear uncomfortable_left",
            "VoodooPhone akiko1_underwear surprised",
            "VoodooPhone akiko1_underwear shy_closed2",
            "VoodooPhone akiko1_underwear neutral",
            "VoodooPhone akiko1_underwear talking",
        ],
        "akiko kiss": [
            At("AkikoKiss climbing nervous blush1", galzoomout),
            At("AkikoKiss climbing smile blush1", galzoomout),
            At("AkikoKiss kissing blush2", galzoomout),
            At("AkikoKiss climbing disoriented", galzoomout),
            At("AkikoKiss kissing", galzoomout),
        ],
        "spiral ending": [
            "SpiralEnding furious scared",
            "SpiralEnding furious choking",
            "SpiralEnding calm scared",
            "SpiralEnding calm choking",
        ],
        "sayori alter bad end 3": [
        "SayoriAlterBadEnd3 wink",
        "SayoriAlterBadEnd3 smile blink",
        ],
        "hiroko rooftop 1 1": [
            "HirokoRooftop1 h1 sleep_side",
            "HirokoRooftop1 h1 sad_side",
            "HirokoRooftop1 h1 neutral_side",
            "HirokoRooftop1 h2 neutral",
            "HirokoRooftop1 h2 frown",
            "HirokoRooftop1 h2 irritated",
            "HirokoRooftop1 h2 curious",
            "HirokoRooftop1 h2 smile",
            "HirokoRooftop1 h2 giggle",
            "HirokoRooftop1 h3 laugh",
            "HirokoRooftop1 h3 giggle",
            "HirokoRooftop1 h2 sleep",
            "HirokoRooftop1 h2 sadtalk_left",
            "HirokoRooftop1 h2 sad",
            "HirokoRooftop1 h2 sadtalk",
            "HirokoRooftop1 h2 nervous",
            "HirokoRooftop1 h2 sad_left",
            "HirokoRooftop1 h2 sad",
            "HirokoRooftop1 h2 growl",
            "HirokoRooftop1 h3 passionate",
            "HirokoRooftop1 h3 passionate_closed",
            "HirokoRooftop1 h3 sadtalk",
            "HirokoRooftop1 h2 surprised",
            "HirokoRooftop1 h2 surprised blush",
            "HirokoRooftop1 h3 passionate_closed blush",
            "HirokoRooftop1 h1 frown_side",
            "HirokoRooftop1 h2 neutral_left",
            "HirokoRooftop1 h3 furious",
            "HirokoRooftop1 h3 frown",
            "HirokoRooftop1 h2 kind",
            "HirokoRooftop1 h1 shocked_side",
            "HirokoRooftop1 h1 surprised_side",
            "HirokoRooftop1 h1 surprised_side2",
            "HirokoRooftop1 h3 furious",
        ],
        "hiroko rooftop 1 2": [
            "HirokoRooftop1 h1 sleep_side",
            "HirokoRooftop1 h1 surprised_side2",
            "HirokoRooftop1 h3 afraid",
            "HirokoRooftop1 h3 afraid_light",
            "HirokoRooftop1 h2 afraid",
            "HirokoRooftop1 h2 afraid_light",
            "HirokoRooftop1 h2 sleepy",
            "HirokoRooftop1 h2 sleepy_light",
            "HirokoRooftop1 h4 sleepy2",
            "HirokoRooftop1 h4 sleepy_light2",
            "HirokoRooftop1 h4 sleep2",
            "HirokoRooftop1 h4 sleeptalk2",
        ],
        "hiroko rooftop 2": [
            "HirokoRooftop2 kyou_glare hiroko_glare",
            "HirokoRooftop2 kyou_surprised hiroko_glare",
            "HirokoRooftop2 kyou_laugh hiroko_smirk",
            "HirokoRooftop2 kyou_laugh hiroko_laugh",
        ],
        "penlight broken": [
            "PenlightBroken kyou1",
            "PenlightBroken kyou2",
            "PenlightBroken kyou3",
        ],
        "nozomi rooftop tickled": [
            overlap_images("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown strainedsmile", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown strainedsmile", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown strainedsmile", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown strainedsmile_left", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown strainedsmile_left", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown strainedsmile_left", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown strainedsmile", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown strainedsmile", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown strainedsmile_left blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown strainedsmile_left blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown panicked_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown laugh blush motionlines", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown laugh blush motionlines", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown laugh blush motionlines", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek laugh", "RoofNozomi handsdown panicked_left blush motionlines", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek shocked", "RoofNozomi laughing", "RoofSayori leanback shocked"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek shocked", "RoofNozomi laughing", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi laughing", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi laughing", "RoofSayori leanback angry"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek angry", "RoofNozomi laughing", "RoofSayori leanback angry"),
        ],
        #Page 20
        "nozomi rooftop spanked": [
            overlap_images("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown frown", "RoofSayori leanback smile"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek irritated", "RoofNozomi handsdown frown", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown frown", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown pain_left", "RoofSayori leanback sleep"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek annoyed", "RoofNozomi handsdown pain_left", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown pain_left", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown pain_right", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown pain_right", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown smile_left blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown smile_left blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek smile", "RoofNozomi handsdown panicked_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek surprised", "RoofNozomi handsdown grimace blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek surprised", "RoofNozomi handsdown pain_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek surprised", "RoofNozomi handsdown pain_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek surprised", "RoofNozomi handsdown grimace blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown grimace blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown pain_right blush", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown pain_right blush", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown grimace blush motionlines", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown frown motionlines", "RoofSayori leanback neutral"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek worried", "RoofNozomi handsdown frown motionlines", "RoofSayori leanback worried"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek shocked", "RoofNozomi screaming", "RoofSayori leanback shocked"),
            overlap_images("cg rooftop day", "RoofHiroko handcheek shocked", "RoofNozomi screaming", "RoofSayori leanback worried blush"),
        ],
        "nozomi rooftop tickle2": [
            "RoofNozomi2 nozomi_tickled lines_tickled hardlaugh blush",
            "RoofNozomi2 nozomi_tickled weaklaugh blush",
        ],
        "nozomi rooftop spank2": [
            "RoofNozomi2 lines_spanked",
            "RoofNozomi2 lines_spanked scream",
            "RoofNozomi2",
        ],
        "nozomi provoke": [
            "NozomiProvoke angry blush arms1 kyou1",
            "NozomiProvoke frown blush arms1 kyou1",
            "NozomiProvoke scared blush arms1 kyou2",
            "NozomiProvoke scared_light blush arms1 kyou2",
            "NozomiProvoke dazed blush arms2 kyou2",
            "NozomiProvoke dazed_light blush arms2 kyou2",
            "NozomiProvoke sleepy arms2 kyou2",
            "NozomiProvoke sleepy_light arms2 kyou2",
        ],
        "nozomi couch strip": [
            "NozomiCouchStrip nozomi1 armdown nervous blush1 glasses1",
            "NozomiCouchStrip nozomi1 armup nervous blush1 glasses1",
            "NozomiCouchStrip nozomi1 armup disbelief blush1 glasses1",
            "NozomiCouchStrip nozomi2 frustrated blush2 glasses2",
            "NozomiCouchStrip nozomi3 frustrated blush2 glasses2",
            "NozomiCouchStrip nozomi4 pleading blush2 glasses2",
            "NozomiCouchStrip nozomi5",
            "NozomiCouchStrip nozomi6",
        ],
        "nozomi kneeling trance1": [
            overlap_images("cg nozomi kneeling", "NozomiKneeling underwear head_down_blush pleasure glasses_down kyou_down_uniform"),
            overlap_images("cg nozomi kneeling", "NozomiKneeling underwear head_up_blush surprised glasses_up kyou_down_uniform"),
            overlap_images("cg nozomi kneeling", "NozomiKneeling underwear head_up_blush anxious glasses_up kyou_down_uniform"),
            overlap_images("cg nozomi kneeling", "NozomiKneeling underwear head_up_blush anxious glasses_up kyou_up_uniform"),
            overlap_images("cg nozomi kneeling", "NozomiKneeling underwear head_up surprised glasses_up kyou_down_uniform"),
        ] + unlockable_image_list("persistent.nozomi_kneeling_trance2_unlock", [
            overlap_images("cg nozomi kneeling", "NozomiKneeling underwear head_up surprised glasses_up kyou_click_uniform"),
            overlap_images("cg nozomi kneeling", "NozomiKneeling underwear head_up falling glasses_up kyou_click_uniform"),
            overlap_images("cg nozomi kneeling", "NozomiKneeling underwear head_down blank glasses_down kyou_down_uniform"),
            overlap_images("cg nozomi kneeling", "NozomiKneeling underwear head_down blank glasses_down nokyou"),            
        ]),
        "nozomi zombie walk": [
            At("NozomiZombieWalk nozomi1 neutral", galzoomout),
            At("NozomiZombieWalk nozomi2 neutral", galzoomout),
            At("NozomiZombieWalk nozomi_right", galzoomout),
            At("NozomiZombieWalk nozomi_left neutral_left", galzoomout),
            At("NozomiZombieWalk nozomi_left talk_left", galzoomout),
        ],
        "nozomi lying": [
            "NozomiCaptured base4 entranced",
            "NozomiCaptured base4 entranced_dazed",
            "NozomiCaptured base4 sleep",
            "NozomiCaptured base4 sleeptalk",
            "NozomiCaptured base4 dazed",
            "NozomiCaptured base4 awe blush",
            "NozomiCaptured base4 scared blush",
        ],
        "nozomi kitchen single image": [
            #This one is a single image
        ],
        #Page 21
        "nozomi omelette": [
            "NozomiOmelette head_down sigh omelette1",
            "NozomiOmelette head_down pout omelette1",
            "NozomiOmelette head_up neutral omelette1",
            "NozomiOmelette head_up pout_closed omelette1",
            "NozomiOmelette head_up dazed omelette1",
            "NozomiOmelette head_up surprised omelette1",
            "NozomiOmelette head_down shy_down omelette2",
            "NozomiOmelette head_down shy_up omelette2",
            "NozomiOmelette head_up smile omelette2",
            "NozomiOmelette head_up teasing omelette2",
        ],
        "nozomi kiss": [
            "NozomiKiss kissing",
            "NozomiKiss standing sleepy glasses",
            "NozomiKiss standing smile glasses",
            "NozomiKiss standing sleepysmile glasses",
        ],
        "hypno rehearsal": [ #This one requires a fix in the unlock variable
            "HypnoRehearsal1Gal hiroko_sitting_socks h_grumpy atsuko_sitting_socks a_confused nozomi_sitting_socks n_smile",
            "HypnoRehearsal1Gal kyou_left hiroko_sitting_socks h_growl h_hand1 atsuko_sitting_socks a_confused nozomi_sitting_socks n_smile",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_grumpy_light atsuko_sitting_socks a_confused_light nozomi_sitting_socks n_smile_light",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_relaxed",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed_light atsuko_sitting_socks a_relaxed_light nozomi_sitting_socks n_relaxed_light",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed_closed atsuko_sitting_socks a_relaxed_closed nozomi_sitting_socks n_relaxed_closed",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_irritated atsuko_sitting_socks a_irritated nozomi_sitting_socks n_irritated",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed_closed atsuko_laying_socks a_sleep nozomi_laying_socks n_sleep",
            "HypnoRehearsal1Gal hiroko_laying_socks h_sleep atsuko_laying_socks a_sleep nozomi_laying_socks n_sleep",
            "HypnoRehearsal1Gal hiroko_laying_socks h_wakingtalk atsuko_laying_socks a_waking nozomi_laying_socks n_waking",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_embarrassed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_relaxed",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_grumpy atsuko_sitting_socks a_neutral nozomi_sitting_socks n_neutral",
            "HypnoRehearsal1Gal kyou_left hiroko_sitting_socks h_grumpy h_hand1 atsuko_sitting_socks a_neutral nozomi_sitting_socks n_neutral",
            "HypnoRehearsal1Gal kyou_left hiroko_sitting_socks h_relaxed_closed h_hand1 atsuko_sitting_socks a_neutral nozomi_sitting_socks n_neutral",
            "HypnoRehearsal1Gal kyou_right_right hiroko_sitting_socks h_relaxed_closed atsuko_laying_socks a_sleep a_hand nozomi_sitting_socks n_neutral",
            "HypnoRehearsal1Gal kyou_right hiroko_sitting_socks h_relaxed_closed atsuko_laying_socks a_sleep a_hand nozomi_laying_socks n_sleep n_hand",
            "HypnoRehearsal1Gal kyou_right_left hiroko_laying_socks h_sleep atsuko_laying_socks a_sleep nozomi_laying_socks n_sleep n_hand",
            "HypnoRehearsal1Gal kyou_right_right hiroko_laying_socks h_sleep atsuko_laying_socks a_sleep a_hand nozomi_laying_socks n_sleep",
            "HypnoRehearsal1Gal kyou_left hiroko_laying_socks h_sleep h_hand2 atsuko_laying_socks a_sleep nozomi_laying_socks n_sleep",
            "HypnoRehearsal1Gal kyou_left hiroko_laying_socks h_sleeptalk h_hand2 atsuko_laying_socks a_sleep nozomi_laying_socks n_sleep",
            "HypnoRehearsal1Gal kyou_right hiroko_laying_socks h_sleep atsuko_laying_socks a_sleep a_hand nozomi_laying_socks n_sleep n_hand",
            "HypnoRehearsal1Gal atsuko_laying_socks a_sleep hiroko_laying_socks h_sleep nozomi_laying_socks n_sleep",
            "HypnoRehearsal1Gal atsuko_laying_socks a_waking hiroko_laying_socks h_waking nozomi_laying_socks n_waking",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_embarrassed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_relaxed",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_relaxed",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_relaxed atsuko_sitting_socks a_relaxed nozomi_sitting_socks n_smile",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_angry atsuko_sitting_socks a_neutral nozomi_sitting_socks n_neutral_left",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_neutral atsuko_sitting_socks a_happy nozomi_sitting_socks n_neutral_left",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_socks a_laugh nozomi_sitting_socks n_annoyed_left",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_socks a_smile nozomi_sitting_socks n_annoyed_left",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_socks a_smile_right nozomi_sitting_socks n_annoyed_left",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_socks a_smile_right nozomi_sitting_socks n_annoyed",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_socks a_neutral_right nozomi_sitting_socks n_annoyed_left",
            "HypnoRehearsal1Gal hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_confused nozomi_sitting_socks n_annoyed_left",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_smug atsuko_sitting_onesock a_confused nozomi_sitting_socks n_neutral_left",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_smug atsuko_sitting_onesock a_neutral nozomi_sitting_socks n_neutral",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_smug atsuko_sitting_onesock a_neutral nozomi_laying_socks n_sleep",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_smug atsuko_sitting_onesock a_smile_right nozomi_laying_socks n_sleep",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile_right nozomi_protesting_socks n_growl_left",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile nozomi_sitting_socks n_neutral",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_growl atsuko_sitting_onesock a_smile nozomi_sitting_socks n_neutral",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_angry atsuko_sitting_onesock a_smile nozomi_sitting_socks n_neutral",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_laugh nozomi_sitting_socks n_irritated",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_laugh nozomi_protesting_socks n_angry_left",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile_right nozomi_protesting_socks n_angry_left",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile_right nozomi_protesting_socks n_angry",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile_right nozomi_protesting_socks n_growl",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_smile_right nozomi_protesting_socks n_angry",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_laugh nozomi_protesting_socks n_angry_left",
            "HypnoRehearsal1Gal onesock hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_laugh nozomi_protesting_socks n_angry",
            "HypnoRehearsal1Gal onesock hiroko_thieving_socks atsuko_sitting_onesock a_neutral_right nozomi_protesting_onesock n_confused",
            "HypnoRehearsal1Gal onesock hiroko_thieving_socks atsuko_sitting_onesock a_laugh nozomi_protesting_onesock n_growl_left",
            "HypnoRehearsal1Gal onesock hiroko_thieving_socks atsuko_sitting_onesock a_laugh nozomi_protesting_onesock n_angry_left",
            "HypnoRehearsal1Gal onesock hiroko_thieving_socks atsuko_sitting_onesock a_laugh nozomi_protesting_onesock n_angry",
            "HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_smug atsuko_sitting_onesock a_happy nozomi_sitting_onesock n_embarrassed",
            "HypnoRehearsal1Gal kyou_right_right twosocks hiroko_sitting_socks h_neutral_right atsuko_laying_onesock a_sleep nozomi_sitting_onesock n_neutral_left",
            "HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_laying_onesock a_waking nozomi_sitting_onesock n_neutral_left",
            "HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_confused nozomi_sitting_onesock n_neutral_left",
            "HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_neutral nozomi_sitting_onesock n_neutral_left",
            "HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_relaxed nozomi_sitting_onesock n_neutral_left",
            "HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_irritated nozomi_sitting_onesock n_neutral_left",
            "HypnoRehearsal1Gal twosocks hiroko_sitting_socks h_neutral_right atsuko_sitting_onesock a_angry nozomi_sitting_onesock n_neutral_left",
        ],
        "hypno rehearsal 2": [ #This one requires a fix in the unlock variable
            "HypnoRehearsal2 neutral",
            "HypnoRehearsal2 smirk",
            "HypnoRehearsal2 thoughtful",
            "HypnoRehearsal2 concerned",
            "HypnoRehearsal2 laugh",
            "HypnoRehearsal2 grin",
        ],
        "zombie bedroom 3": [
            "NozomiBedroom3 troubled",
            "NozomiBedroom3 troubledtalk",
            "NozomiBedroom3 sleeptalk",
            "NozomiBedroom3 sleep",
        ],
        "sayori room hypno": [
            "SayoriRoomHypno",
            "SayoriRoomHypno s_closed",
            "SayoriRoomHypno s_closed_talk",
            "SayoriRoomHypno s_neutral",
            "SayoriRoomHypno s_confused_closed",
            "SayoriRoomHypno k_handup s_confused_closed",
            "SayoriRoomHypno k_handup s_confused",
            "SayoriRoomHypno k_handup s_surprised_up",
            "SayoriRoomHypno s_confused_closed",
            "SayoriRoomHypno k_handup s_confused_up",
            "SayoriRoomHypno s_confused_closed",
            "SayoriRoomHypno s_confused_up",
            "SayoriRoomHypno s_drowsy",
            "SayoriRoomHypno s_confused_closed",
            "SayoriRoomHypno s_sleepy",
            "SayoriRoomHypno k_handsnap k_frown s_sleepy",
            "SayoriRoomHypno k_handsnap k_frown s_armdown2 s_headdown s_sleep",
            "SayoriRoomHypno k_frown s_armdown2 s_headdown s_sleep",
            "SayoriRoomHypno k_handhold s_armup k_frown s_headdown s_sleep",
            "SayoriRoomHypno s_armlap k_frown s_headdown s_sleep",
            "SayoriRoomHypno s_armlap k_frown s_headdown s_sleeptalk",
            "SayoriRoomHypno s_armlap s_headdown s_sleep",
            "SayoriRoomHypno k_handshoulder s_armlap s_headdown s_sleep",
            "SayoriRoomHypno k_handshoulder s_armlap s_headdown s_sleeptalk",
            "SayoriRoomHypno s_armlap s_headdown s_sleep",
            "SayoriRoomHypno k_frown s_armlap s_headdown s_sleep",
            "SayoriRoomHypno s_armlap s_headdown s_waking",
            "SayoriRoomHypno s_armlap2 s_surprised",
            "SayoriRoomHypno s_armlap2 s_drowsy",
            "SayoriRoomHypno s_armlap2 s_chuckle",
            "SayoriRoomHypno s_armlap2 s_smile",
            "SayoriRoomHypno s_armlap2 s_neutral",
            "SayoriRoomHypno s_armlap2 s_closed_talk",
            "SayoriRoomHypno s_armlap2 s_smile",
        ],
        "sayori doll pose1": [
            "SayoriDollPose1",
            "SayoriDollPose1 blush1",
            "SayoriDollPose1 pose2",
            "SayoriDollPose1 pose3 embarrassed_left blush3",
            "SayoriDollPose1 pose3_solo puzzled",
            "SayoriDollPose1 pose3_solo puzzled blush3",
            "SayoriDollPose1 pose3_solo annoyed blush3",
            "SayoriDollPose1 pose3_solo annoyed",
            "SayoriDollPose1 pose3_solo smile",
            "SayoriDollPose1 pose3_solo happy",
            "SayoriDollPose1 pose3_solo embarrassed_closed blush3",
            "SayoriDollPose1 pose3_solo embarrassed blush3",
            "SayoriDollPose1 pose3_solo embarrassed_left blush3",
            "SayoriDollPose1 pose3_solo embarrassed blush3",
            "SayoriDollPose1 pose3_solo puzzled blush3",
            "SayoriDollPose1 pose3_solo smirk blush3",
        ],
        "sayori doll pose2": [
            "SayoriDollPose2 couple1 head_up kyou_grin kyou_blush sayo_smirk sayo_blush",
            "SayoriDollPose2 couple1 head_up kyou_grin kyou_blush sayo_dazed sayo_blush",
            "SayoriDollPose2 couple1 head_up kyou_grin kyou_blush sayo_sleep",
            "SayoriDollPose2 couple1 head_down kyou_grin kyou_blush",
            "SayoriDollPose2 couple1 head_down kyou_smile",
            "SayoriDollPose2 couple2 kyou_neutral sayo_sleep",
            "SayoriDollPose2 couple2 kyou_neutral sayo_smile",
            "SayoriDollPose2 couple2 kyou_smile sayo_smile",
            "SayoriDollPose2 couple2 kyou_happy sayo_smile",
            "SayoriDollPose2 sayori sayo_smile",
            "SayoriDollPose2 couple3 sayo_smile",
        ],
        "sayori doll scene climax": [
            #This one is a single image
        ],
        #Page 22
        "yikes end": [
            "Hiroko YikesEnd1 arms_out surprised blush",
            "Hiroko YikesEnd1 arms_in calm blush",
            "Hiroko YikesEnd1 couple2",
            "Hiroko YikesEnd1 couple3 smile",
            "Hiroko YikesEnd1 couple3 laugh",
        ],
        "hiroko betrayal": [
            "HirokoBetrayal hiroko happy",
            "HirokoBetrayal hiroko neutral",
            "HirokoBetrayal hiroko curious",
            "HirokoBetrayal hiroko awe",
            "HirokoBetrayal hiroko smile",
            "HirokoBetrayal hiroko grin",
            "HirokoBetrayal hiroko concerned",
            "HirokoBetrayal hiroko sad",
            "HirokoBetrayal",
        ],
        "alter good end 2": [
            "Sayori AlterEnd3 n_confused h1 h_fists h_mad s1 s_surprised",
            "Sayori AlterEnd3 n_neutral h1 h_fists h_growl s1 s_neutral",
            "Sayori AlterEnd3 n_neutral h1 h_lowered h_frown s1 s_neutral",
            "Sayori AlterEnd3 n_neutral h1 h_lowered h_growl s1 s_neutral",
            "Sayori AlterEnd3 n_neutral h1 h_lowered h_rolleyes s1 s_neutral",
            "Sayori AlterEnd3 n_neutral h1 h_lowered h_irritated s1 s_neutral",
            "Sayori AlterEnd3 n_neutral h1 h_fists h_mad s1 s_neutral",
            "Sayori AlterEnd3 n_confused h1 h_fists h_growl s2 s_neutral_side",
            "Sayori AlterEnd3 n_confused h1 h_fists h_irritated s2 s_neutral_side",
            "Sayori AlterEnd3 n_confused h1 h_fists h_pout s2 s_neutral_side",
            "Sayori AlterEnd3 n_neutral_right h2 h_fists h_frown_side s2 s_calm",
            "Sayori AlterEnd3 n_neutral_right h2 h_fists h_frown_side s2 s_smile_side",
            "Sayori AlterEnd3 n_neutral_left h2 h_lowered h_smile_side s2 s_smile_side",
            "Sayori AlterEnd3 n_neutral_left h2 h_lowered h_smile_side s2 s_rolleyes",
            "Sayori AlterEnd3 n_neutral h2 h_lowered h_smile_side s2 s_rolleyes",
            "Sayori AlterEnd3 n_smile h2 h_lowered h_smile_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_glare h2 h_lowered h_neutral_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_glare h2 h_lowered h_frown_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_confused h2 h_lowered h_frown_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_confused h2 h_lowered h_pout_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_neutral_right h2 h_lowered h_pout_side s2 s_calm",
            "Sayori AlterEnd3 n_happy h2 h_lowered h_pout_side s2 s_calm",
            "Sayori AlterEnd3 n_happy h2 h_lowered h_neutral_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_smile h2 h_lowered h_neutral_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_smile h2 h_fists h_frown_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_smile h2 h_fists h_frown_side s2 s_calm",
            "Sayori AlterEnd3 n_glare h2 h_lowered h_frown_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_glare h2 h_lowered h_pout_side s2 s_rolleyes",
            "Sayori AlterEnd3 n_pout h2 h_lowered h_pout_side s2 s_rolleyes",
            "Sayori AlterEnd3 n_sad h2 h_lowered h_pout_side s2 s_rolleyes",
            "Sayori AlterEnd3 n_sad h2 h_lowered h_smile_side s2 s_smile_side",
            "Sayori AlterEnd3 n_sad h2 h_lowered h_pout_side s2 s_smile_side",
            "Sayori AlterEnd3 n_happy h2 h_lowered h_pout_side s2 s_smirk_side",
            "Sayori AlterEnd3 n_smile h1 h_lowered h_neutral s1 s_smirk",
            "Sayori AlterEnd3 n_smile h1 h_lowered h_neutral s1 s_smile",
            "Sayori AlterEnd3 n_happy h1 h_lowered h_neutral s1 s_smile",
            "Sayori AlterEnd3 n_neutral_left h2 h_rolling h_neutral_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_smirk h2 h_rolling h_neutral_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_smirk h2 h_rolling h_pout_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_smirk h2 h_rolling h_pout_side s2 s_smirk_side",
            "Sayori AlterEnd3 n_smirk h2 h_lowered h_pout_side s2 s_smirk_side",
            "Sayori AlterEnd3 n_smile h2 h_lowered h_smile_side s2 s_smile_side",
            "Sayori AlterEnd3 n_neutral_right h2 h_lowered h_smile_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_neutral_right h2 h_lowered h_smile_side s1 s_neutral",
            "Sayori AlterEnd3 n_neutral h1 h_lowered h_neutral s1 s_neutral",
            "Sayori AlterEnd3 n_neutral h1 h_lowered h_neutral s2 s_smile_side",
            "Sayori AlterEnd3 n_neutral h1 h_lowered h_neutral s1 s_smile",
            "Sayori AlterEnd3 n_neutral h1 h_lowered h_awe s1 s_smile",
            "Sayori AlterEnd3 n_neutral_right h1 h_lowered h_awe s2 s_smile_side",
            "Sayori AlterEnd3 n_neutral_right h2 h_lowered h_neutral_side s2 s_smile_side",
            "Sayori AlterEnd3 n_neutral_right h2 h_lowered h_neutral_side s2 s_neutral_side",
            "Sayori AlterEnd3 n_neutral_left h1 h_lowered h_neutral s2 s_neutral_side",
            "Sayori AlterEnd3 n_neutral_left h1 h_lowered h_confused s2 s_neutral_side",
            "Sayori AlterEnd3 n_neutral h1 h_lowered h_neutral s1 s_neutral",
            "Sayori AlterEnd3 n_smile h1 h_lowered h_smile s1 s_smile",
            "Sayori AlterEnd3 n_smile h1 h_lowered h_laugh s1 s_smile",
            "Sayori AlterEnd3 n_smile h1 h_lowered h_grin s1 s_smile",
            "Sayori AlterEnd3 n_smile h2 h_lowered h_smile_side s2 s_smile_side",
            "Sayori AlterEnd3 n_smile h2 h_lowered h_smile_side s2 s_rolleyes",
            "Sayori AlterEnd3 n_smile h2 h_lowered h_smile_side s2 s_laugh",
            "Sayori AlterEnd3 n_laugh h1 h_rolling h_laugh s2 s_laugh",
            "Sayori AlterEnd3 n_laugh h1 h_rolling h_laugh s1 s_smile",
        ],
        "devotion end 1 single image": [
            #This one is a single image
        ],
        "devotion end 2": [
            "DevotionEnd2 nozomi1 arm_up n_smile n_blush k_smirk k_blush",
            "DevotionEnd2 nozomi1 arm_up n_grin n_blush k_smirk k_blush",
            "DevotionEnd2 nozomi2 arm_up n_grin n_blush k_surprised",
            "DevotionEnd2 nozomi2 arm_up n_grin n_blush k_surprised_light",
            "DevotionEnd2 nozomi2 arm_up n_giggle k_surprised",
            "DevotionEnd2 nozomi2 arm_up n_giggle k_surprised_light",
            "DevotionEnd2 nozomi2 arm_up n_giggle k_struggle",
            "DevotionEnd2 nozomi2 arm_up n_giggle k_struggle_light",
            "DevotionEnd2 nozomi2 arm_up n_giggle k_sleepy",
            "DevotionEnd2 nozomi2 arm_up n_giggle k_sleepy_light",
            "DevotionEnd2 nozomi2 arm_down n_giggle k_sleepy",
            "DevotionEnd2 nozomi2 arm_down n_giggle k_sleepy_light",
            "DevotionEnd2 nozomi2 arm_down n_grin k_sleepy",
            "DevotionEnd2 nozomi2 arm_down n_grin k_sleepy_light",
        ],
        "delusion end 1 single image": [
            #This one is a single image
        ],
        "trance abuse end": [
            "TranceAbuseEnd smile",
            "TranceAbuseEnd shy_left",
            "TranceAbuseEnd shy blush",
            "TranceAbuseEnd shy_left blush",
            "TranceAbuseEnd shy blush hand",
            "TranceAbuseEnd excited blush hand",
            "TranceAbuseEnd smirk blush hand",
            "TranceAbuseEnd manic blush hand",
            "TranceAbuseEnd perverted blush hand nozomi_hand",
        ],
        "school cafe 1 single image": [
            #This one is a single image
        ],
        "zombie ending 1": [
            "ZombieEnding1 kyou k_smile point fingers_apart nozomi1 n_irritated",
            "ZombieEnding1 kyou k_smile point fingers_apart nozomi1 n_frown",
            "ZombieEnding1 kyou k_smile point fingers_apart nozomi1 n_straining blush1",
            "ZombieEnding1 kyou k_smile point fingers_closing nozomi1 n_straining blush1",
            "ZombieEnding1 kyou k_neutral rest fingers_closing nozomi1 n_focused",
            "ZombieEnding1 kyou k_neutral rest fingers_touch nozomi1 n_focused",
            "ZombieEnding1 kyou k_neutral snap fingers_touch nozomi1 n_focused",
            "ZombieEnding1 kyou k_neutral snap fingers_touch nozomi1 n_relaxed",
            "ZombieEnding1 kyou k_neutral rest nozomi2 n_sleep",
            "ZombieEnding1 kyou k_neutral rest nozomi2 n_sleeptalk",
            "ZombieEnding1 kyou k_smile rest nozomi2 n_sleep",
            "ZombieEnding1 kyou k_smile rest nozomi2 n_sleeptalk",
            "ZombieEnding1 kyou k_smile snap nozomi2 n_waking",
            "ZombieEnding1 kyou k_smile rest nozomi2 n_waking",
            "ZombieEnding1 kyou k_smile rest nozomi3 n_surprised",
            "ZombieEnding1 kyou k_smile rest nozomi3 n_smile",
            "ZombieEnding1 kyou k_smile rest nozomi3 n_smile blush3",
            "ZombieEnding1 kyou k_laugh rest nozomi3 n_smile blush3",
            "ZombieEnding1 kyou k_laugh rest nozomi3 n_laugh blush3",
            "ZombieEnding1 kyou k_laugh rest nozomi3 n_happy blush3",
            "ZombieEnding1",
        ],
        #Page 23
        "hiroko stageshow good": [
            "Hiroko StageShow bg_s kyou_s k_armup_s k_smile_s chairs_s male1_s female1_s hiroko_s male2_s nozomi_s",
            "Hiroko StageShow bg_s kyou_s k_armdown_s k_smile_s chairs_s male1_s female1_s hiroko_s h_hands_s male2_s nozomi_s",
            "Hiroko StageShow bg_s kyou_s k_armup_s k_smile_s chairs_s female1_s male2_s nozomi_s",
        ],
        "hiroko stageshow cat": [
            "Hiroko StageShow_Cat",
            "Hiroko StageShow_Cat licking_side guy",
            "Hiroko StageShow_Cat arm_down annoyed guy",
            "Hiroko StageShow_Cat hiroko_angry guy",
            "Hiroko StageShow_Cat hiroko_angry guy sweatdrops",
        ],
        "sayori stageshow catalepsy": [
            "Sayori StageShow_Catalepsy",
            "Sayori StageShow_Catalepsy arm_up",
        ],
        "sayori chicken1": [
            "SayoriChicken1 kyou1 k_smile sayori2 s_sleep",
            "SayoriChicken1 kyou1 k_smile_side sayori2 s_sleep",
            "SayoriChicken1 kyou1 k_neutral_side sayori2 s_sleep",
            "SayoriChicken1 kyou2 k_neutral_side sayori2 s_sleep",
            "SayoriChicken1 kyou2 k_neutral sayori2 s_sleep",
            "SayoriChicken1 kyou2 k_smile_side sayori2 s_sleep",
            "SayoriChicken1 kyou1 k_smile sayori2 s_sleeptalk",
            "SayoriChicken1 kyou1 k_smile sayori2 s_waking",
            "SayoriChicken1 kyou2 k_laugh sayori3 s_shock blush",
            "SayoriChicken1 kyou2 k_smirk sayori3 s_struggling blush",
            "SayoriChicken1 kyou2 k_smirk sayori3 s_shock blush",
            "SayoriChicken1 kyou3 k_smile sayori3 s_struggling blush",
            "SayoriChicken1 kyou3 k_smile sayori3 s_chicken",
        ],
        "sayori chicken2": [
            "SayoriChicken2 head_down dazed kyou",
            "SayoriChicken2 head_down surprised",
            "SayoriChicken2 head_up embarrassed",
            "SayoriChicken2 head_up embarrassed_side",
        ],
        "sayori doll bad end single image": [
            #This one is a single image
        ],
        "sayori doll good end": [
            "SayoriDollEnd1",
            "SayoriDollEnd1 sleep_down",
            "SayoriDollEnd1 kyou_arms arms_down sleep_down",
            "SayoriDollEnd1 kyou_chin arms_down head_up sleep_up",
            "SayoriDollEnd1 kyou_back arms_down head_up sleep_up",
            "SayoriDollEnd1 arms_down head_up smile",
        ],
        "hiroko good end 1": [
            overlap_images("cg school ext night", "Hiroko GoodEnd1 body smile"),
            overlap_images("cg school ext night", "Hiroko GoodEnd1 blush smile"),
            overlap_images("cg school ext night", "Hiroko GoodEnd1 blush laugh"),
        ],
        "copycat ending 1 single image": [
            #This one is a single image
        ],
        #Page 24
        "copycat ending 2_1": [
            "CopycatEnd2 blanktalk akiko_a smile",
            "CopycatEnd2 blank akiko_a happy",
            "CopycatEnd2 blank akiko_a grin",
            "CopycatEnd2 blank akiko_a confused",
            "CopycatEnd2 blanktalk akiko_a confused",
            "CopycatEnd2 blank akiko_a happy blush",
            "CopycatEnd2 blank akiko_a smile blush",
        ],
        "copycat ending 2_2": [
            "CopycatEnd2 blanktalk akiko_b smile",
            "CopycatEnd2 blank akiko_b happy",
            "CopycatEnd2 blank akiko_b grin",
            "CopycatEnd2 blank akiko_b confused",
            "CopycatEnd2 blanktalk akiko_b confused",
            "CopycatEnd2 blank akiko_b happy blush",
            "CopycatEnd2 blank akiko_b smile blush",
        ],
        "redemption ending 1_1": [
            "Redemption_Ending_1-1 kyou_room_s akiko_s quizzical_s glasses_s",
            "Redemption_Ending_1-1 kyou_room_s akiko_s embarrassed_s blush_s glasses_s nokyou",
            "Redemption_Ending_1-1 kyou_room_s akiko_s neutral_s glasses_s",
            "Redemption_Ending_1-1 kyou_room_s akiko_s neutral_s kyou_s glasses_s",
            "Redemption_Ending_1-1 kyou_room_s akiko_s sleep_s kyou_s glasses_s",
            "Redemption_Ending_1-1 kyou_room_s akiko_s sleeptalk_s kyou_s glasses_s",
            "Redemption_Ending_1-1 kyou_room_s akiko_s sleep_s kyou_s glasses_s",
            "Redemption_Ending_1-1 kyou_room_s akiko_s sleep_s glasses_s",
            "Redemption_Ending_1-1 kyou_room_s akiko_s waking_s glasses_s",
            "Redemption_Ending_1-1 kyou_room_s akiko_s smile_s glasses_s",
        ],
        "redemption ending 1_2": [ 
            "Redemption_Ending_1-2",
            "Redemption_Ending_1-2 laugh",
            "Redemption_Ending_1-2 talk",
            "Redemption_Ending_1-2 arms_up smile",
            "Redemption_Ending_1-2 arms_up talk",
        ],
        "forced girlfriend ending": [
            "NozomiForcedGF smile_up",
            "NozomiForcedGF smile_down",
        ],
        "hiroko park hypno": [
            "HirokoParkHypno",
            "HirokoParkHypno hiroko_arms_out",
            "HirokoParkHypno hiroko_arms_out kyou_holding",
            "HirokoParkHypno hiroko_arms_out kyou_pointing",
            "HirokoParkHypno hiroko_arms_out frown_open kyou_pointing",
            "HirokoParkHypno hiroko_arms_out frown_open_talk kyou_pointing",
            "HirokoParkHypno hiroko_arms_out frown_closed kyou_pointing",
            "HirokoParkHypno hiroko_arms_out frown_closed",
            "HirokoParkHypno hiroko_arms_out frown_closed_talk",
            "HirokoParkHypno hiroko_arms_out frown_closed",
            "HirokoParkHypno hiroko_arms_close frown_closed",
            "HirokoParkHypno hiroko_arms_closer frown_closed",
            "HirokoParkHypno hiroko_arms_closer frown_closed kyou_clapping",
            "HirokoParkHypno hiroko_slumped noface",
            "HirokoParkHypno hiroko_sleep sleep",
            "HirokoParkHypno hiroko_sleep sleeptalk",
            "HirokoParkHypno",
            "HirokoParkHypno laugh",
            "HirokoParkHypno hiroko_sitting_blush",
        ],
        "hiroko park ending 1 single image": [
            #This one is a single image
        ],
        "hiroko cafe": [
            "HirokoCafe worried",
            "HirokoCafe sigh",
            "HirokoCafe frown",
            "HirokoCafe scared_closed",
            "HirokoCafe scared",
            "HirokoCafe worried_left",
            "HirokoCafe frown",
            "HirokoCafe neutral_left",
            "HirokoCafe neutral",
            "HirokoCafe smile",
            "HirokoCafe smile_tears",
        ],
        "robot karaoke end": [
            "RobotKaraoke nozomi1 n_happy h_happy",
            "RobotKaraoke nozomi1 n_smile h_happy lyric1",
            "RobotKaraoke nozomi1 n_neutral h_happy lyric2",
            "RobotKaraoke nozomi1 n_neutral h_sing lyric2",
            "RobotKaraoke nozomi1 n_unsure h_sing lyric2",
            "RobotKaraoke nozomi1 n_unsure h_sing_n lyric1",
            "RobotKaraoke nozomi1 n_unsure h_sing_n",
            "RobotKaraoke nozomi1 n_unsure_closed h_sing lyric1",
            "RobotKaraoke nozomi1 n_unsure_closed h_happy lyric2",
            "RobotKaraoke nozomi1 n_tearful h_sing lyric2",
            "RobotKaraoke nozomi1 n_cry h_sing lyric1",
            "RobotKaraoke nozomi1 n_cry h_peaceful lyric1",
            "RobotKaraoke nozomi2 h_smile",
        ],
        #Page 25
        "k bedroom robot nozomi": [
            overlap_images("cg k bedroom eve2", "Kyou_Robo upper"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo robot closed"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo robot open"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo upper", "Nozomi_K_Bedroom_Robo robot closed"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo confused"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo panicked"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo lower", "Nozomi_K_Bedroom_Robo panicked blush"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo panicked neutral"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Nozomi_K_Bedroom_Robo robot closed"),
        ],
        "k bedroom robot sayori": [
            overlap_images("cg k bedroom eve2", "Kyou_Robo upper"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo robot closed"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo robot open"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo upper", "Sayori_K_Bedroom_Robo robot closed"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo confused"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo panicked body"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo lower", "Sayori_K_Bedroom_Robo panicked blush "),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo panicked body neutral"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Sayori_K_Bedroom_Robo robot closed"),
        ],
        "k bedroom robot hiroko": [
            overlap_images("cg k bedroom eve2", "Kyou_Robo upper"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo robot closed"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo robot open"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo upper", "Hiroko_K_Bedroom_Robo robot closed"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo confused"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo panicked body"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo lower", "Hiroko_K_Bedroom_Robo panicked blush"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo panicked body neutral"),
            overlap_images("cg k bedroom eve2", "Kyou_Robo rest", "Hiroko_K_Bedroom_Robo robot closed"),
        ],
        "sayori alter confrontation2": [
            "Sayori_Alter_Confrontation2",
            "Sayori_Alter_Confrontation2 nozomi_bw",
            "Sayori_Alter_Confrontation2 nozomi_bw worried_bw",
            "Sayori_Alter_Confrontation2 nozomi_bw scared_bw",
            "Sayori_Alter_Confrontation2 nozomi_bw grin_bw scared_bw",
            "Sayori_Alter_Confrontation2 grin_bw scared_bw",
            "Sayori_Alter_Confrontation2 bg shadow nozomi_blush sayori smirk angry glasses",
            "Sayori_Alter_Confrontation2 bg shadow nozomi sayori smirk angry glasses",
            "Sayori_Alter_Confrontation2 bg shadow nozomi sayori smirk worried glasses",
            "Sayori_Alter_Confrontation2 bg shadow nozomi sayori smirk scared glasses",
            "Sayori_Alter_Confrontation2 bg shadow nozomi sayori grin scared glasses",
            "Sayori_Alter_Confrontation2 bg shadow nozomi_blush sayori grin scared glasses",
        ],
        "sayori alter coop end": [
            #This one is a single image
        ],
        "alter bad end 1": [
            "Sayori AlterEnd2",
            "Sayori AlterEnd2 side_open",
            "Sayori AlterEnd2 body_facing_down facing_open",
            "Sayori AlterEnd2 body_facing_down facing_closed",
            "Sayori AlterEnd2 body_facing_down facing_open",
            "Sayori AlterEnd2 bg body_facing_up facing_open",
            "Sayori AlterEnd2 bg body_side side_open",
            "Sayori AlterEnd2",
            "Sayori AlterEnd2 bg body_none eyes_none",
        ],
        "sayori alter bad end 2": [
            #This one is a single image
        ],
        "alter good end 1": [
            overlap_images("cg sayori alter good end 1", "Sayori AlterEnd1 concerned"),
            overlap_images("cg sayori alter good end 1", "Sayori AlterEnd1 blush happy"),
        ],
        "tennis bot end 3": [
            #This one is a single image
        ],
        #Page 26
        "nozomi good end 1": [
            overlap_images("cg nozomi good end 1", "Nozomi GoodEnd1 smile"),
            overlap_images("cg nozomi good end 1", "Nozomi GoodEnd1 kiss"),
        ],
    }
#END OF CG GROUPS

##List of tags used to filter CGs. 1 equals positive filter (must have), -1 equals negative (must not have) filter and 0 equals no filter
default cg_tags = {
    "k": 0, #Kyou
    "n": 0, #Nozomi
    "h": 0, #Hiroko
    "s": 0, #Sayori
    "nm": 0, #Atsuko
    "r": 0, #Risa
    "a": 0, # Akiko
}

##CG group tags. The tags that each CG has from the "cg_tags" list above
init python:
    cg_group_tags = {
    #Page 1
    "titlescreen": ["n", "k",],
    "kyou intro single image": ["k"],
    "stageshow": ["n"],
    "classroom nozomi": ["n"],
    "hiroko_tennis1 single image": ["h"],
    "alley hiroko": ["h"],
    "akiko science": ["a", "k"],
    "sayori intro": ["s"],
    "sayori study": ["s", "k"],
    "sports shed night": ["h"],
    "classroomlunch2 1": ["s", "h", "n", "k"],
    #Page 2
    "rooftop day": ["n", "h", "s"],
    "delusion rooftop": ["n"],
    "devotion start": ["h", "k"],
    "robot start": ["h", "k"],
    "sleeper agent start": ["h", "k"],
    "hiro walk devotion": ["h", "k"],
    "k bedroom hiroko 1": ["h"],
    #Page 3
    "redemption start": ["h", "k"],
    "devotion bedroom day2": ["h", "k"],
    "hiroko robot programming": ["h", "k"],
    "study room sayori": ["s"],
    "hiroko vs risa": ["h", "r"],
    "nozomi cafe": ["n"],
    "k room nozomi 1 1": ["n"],
    "room hiroko 1": ["h"],
    "classroomlunch3": ["h", "n", "s", "k"],
    #Page 4
    "classroom lunch2 delusion": ["h", "n", "s", "k"],
    "akiko student council hypno": ["a"],
    "sleeper agent night": ["h", "k"],
    "akiko student council hypno2": ["a"],
    "hiroko trapped": ["h", "k"],
    "creepy hiroko": ["n","h"],
    "hiroko tickle": ["h", "k"],
    "hiroko couch argument": ["h", "k"],
    #Page 5
    "k room nozomi 2 1": ["n"],
    "zombie beginning": ["n"],
    "nozomi injured": ["n"],
    "sayori arm": ["s", "k"],
    "sayori sleeper capture": ["h", "k", "s"],
    "classroomlunch4 1": ["h", "n", "s", "k"],
    "akiko intro": ["a"],
    "k room nozomi reversal1": ["n"],
    "k room nozomi tv1": ["n"],
    "k room hiroko tv1": ["h"],
    #Page 6
    "hiroko reversal": ["h"],
    "hiroko cat 2": ["h"],
    "hiroko cat 1": ["h"],
    "k room sayori": ["s"],
    "sayori alter start": ["s"],
    "sayori greeting": ["s"],
    "nozomisleepercapture": ["h", "n", "s"],
    "delusion struggle sayori": ["s", "k"],
    "devotion tennis": ["h", "k"],
    #Page 7
    "devotion tennis partial": ["h", "k"],
    "devotion underwear": ["h", "k"],
    "devotion naked": ["h", "k"],
    "study room hypno sayori": ["h", "s"],
    "k phone robot": ["n", "k"],
    "nozomi robot kiss single image": ["n", "k"],
    "nozomi mindtrick": ["n", "k"],
    "nozomi hiroko hug": ["n", "h"],
    "sayori lunch": ["s"],
    #Page 8
    "sayori grab": ["s", "k"],
    "sayori x kyou": ["s", "k"],
    "sayori walk": ["s", "k"],
    "hiroko shoe": ["h"],
    "hiroko yawn day": ["h", "n"],
    "classroomlunch5 1": ["h", "n", "s", "k"],
    "classroom lunch2 sleeper": ["h", "n", "s", "k"],
    "rooftop devotion": ["s", "h"],
    "rooftop robot": ["h", "n", "s"],
    #Page 9
    "rooftop robot  girlfriend": ["k", "n", "h", "s"],
    "hiroko yawn eve": ["h", "n"],
    "hiroko tennis kiss single image": ["k", "h", "r"],
    "nozomi collapse single image": ["k", "n"],
    "nozomi interrogation": ["n", "k"],
    "trance stop end": ["n", "k"],
    "nozomi robot programming": ["n", "k"],
    "study room nozomi": ["n"],
    "study room hypno nozomi": ["s", "n"],
    "nozomi chocolate": ["n"],
    #Page 10
    "akiko breakfast": ["a"],
    "hiroko racket": ["k", "r", "h"],
    "k room akiko 1": ["a"],
    "redemption phone day": ["a", "k"],
    "sayori hypno day": ["s"],
    "nozomi cola": ["n"],
    "zombie bedroom 1 1": ["n"],
    "zombie bedroom 2": ["nm", "n"],
    "nozomi boardgame": ["n", "k"],
    "nozomi boardgame2": ["n"],
    #Page 11
    "nozomi hypnobondage": ["n"],
    "nozomi hypnobondage tickling": ["n", "k"],
    "nozomi hypnobondage spanking": ["n", "k"],
    "sayori alter lunch": ["k", "nm", "s", "n"],
    "sayori arcade2": ["n", "k", "s"],
    "sayori penlight": ["s", "n"],
    "sayori bed1": ["n", "s"],
    "sayori hug": ["k", "s"],
    "k bedroom confrontation sayori": ["n", "s"],
    #Page 12
    "k bedroom confrontation hiroko": ["n", "h"],
    "sleeper agent struggle1": ["h", "n", "s", "k"],
    "sleeper agent defeat": ["s", "n", "h"],
    "nozomi burglar": ["n", "k"],
    "nozomi burglar undressing": ["n", "k"],
    "akiko makeover 1": ["a"],
    "akiko makeover 2": ["a"],
    "copycat karaoke hypno1": ["k", "a"],
    "copycat karaoke hypno2": ["k", "a"],
    #Page 13
    "copycat karaoke1": ["a", "k"],
    "copycat karaoke2": ["a", "k"],
    "copycat karaoke3": ["a", "k"],
    "nozomi cafe villain": ["n"],
    "nozomi captured": ["n"],
    "nozomi window": ["n"],
    "nozomi argument": ["k", "n"],
    "sayori fallen": ["s"],
    "sayori sleep": ["s", "k"],
    #Page 14
    "sayori sitting": ["s", "k"],
    "nozomi kneeling devotion": ["n", "k"],
    "classroom hiroko 2 1": ["h"],
    "hiroko rehearsal": ["k", "h"],
    "sayori arcade": ["k", "s"],
    "sayori room hypno2": ["k", "s"],
    "sayori room tickle": ["k", "s"],
    "hiroko gaming": ["h"],
    "hiroko slumped": ["h"],
    #Page 15
    "hiroko court night good": ["h", "k"],
    "hiroko court night bad": ["h", "k"],
    "hiroko park sad": ["h"],
    "hiroko won": ["n", "h"],
    "hiroko cam 1 1": ["h"],
    "hiroko cam 2": ["h"],
    "hiroko karaoke bed 2": ["h"],
    "hiroko bed": ["h"],
    "hiroko couch": ["n", "h"],
    #Page 16
    "hiroko couch2": ["h", "n"],
    "nozomi karaoke group": ["k", "r", "h", "n"],
    "sayori dinner": ["s"],
    "sayori alter hug single image": ["n", "s"],
    "akiko slapped": ["a", "r"],
    "rooftop reversal": ["s", "n", "h", "r"],
    "nozomi threatening": ["n", "k"],
    "nozomi sorry": ["n", "k"],
    "nozomi couch hypno": ["n", "k"],
    #Page 17
    "nozomi tortured tickle": ["n", "k"],
    "nozomi tortured spank": ["n", "k"],
    "hiroko cam 4": ["h", "n"],
    "hiroko cam 3": ["h", "n"],
    "nozo cam hypno": ["h", "n"],
    "hiroko cam kiss": ["h", "n"],
    "hiroko cam 5": ["h", "n"],
    "hiroko nozomi phone": ["h", "n"],
    "reversal bad end": ["n"],
    "reversal good end": ["s", "n", "k", "h", "r"],
    #Page 18
    "sayori alter confrontation": ["n", "s"],
    "akiko intro2": ["a"],
    "akiko kendo": ["a"],
    "sword strike single image": ["a", "k"],
    "akiko cornered": ["a", "k"],
    "redemption phone eve": ["a", "k"],
    "voodoo phone": ["a", "k"],
    "hiroko scared single image": ["h"],
    "bathroom ambush": ["k", "a"],
    #Page 19
    "voodoo phone2": ["a"],
    "akiko kiss": ["a", "k"],
    "spiral ending": ["s", "r", "a", "n", "h"],
    "sayori alter bad end 3": ["s"],
    "hiroko rooftop 1 1": ["h"],
    "hiroko rooftop 1 2": ["h"],
    "hiroko rooftop 2": ["h", "k"],
    "penlight broken": ["k"],
    "nozomi rooftop tickled": ["s", "n", "h"],
    #Page 20
    "nozomi rooftop spanked": ["s", "n", "h"],
    "nozomi rooftop tickle2": ["s", "n", "h"],
    "nozomi rooftop spank2": ["s", "n", "h"],
    "nozomi provoke": ["n", "k"],
    "nozomi couch strip": ["n"],
    "nozomi kneeling trance1": ["n", "k"],
    "nozomi zombie walk": ["n"],
    "nozomi lying": ["n"],
    "nozomi kitchen single image": ["n"],
    #Page 21
    "nozomi omelette": ["n"],
    "nozomi kiss": ["k", "n"],
    "hypno rehearsal": ["k", "h", "nm", "n"],
    "hypno rehearsal 2": ["s"],
    "zombie bedroom 3": ["k", "n"],
    "sayori room hypno": ["k", "s"],
    "sayori doll pose1": ["s", "k"],
    "sayori doll pose2": ["k", "s"],
    "sayori doll scene climax": ["s"],
    #Page 22
    "yikes end": ["k", "h"],
    "hiroko betrayal": ["h"],
    "alter good end 2": ["h", "n", "s"],
    "devotion end 1 single image": ["s", "h", "n"],
    "devotion end 2": ["n", "k"],
    "delusion end 1 single image": ["n"],
    "trance abuse end": ["n"],
    "school cafe 1 single image": ["h", "n", "k" "s"],
    "zombie ending 1": ["k", "n"],
    #Page 23
    "hiroko stageshow good": ["h", "k", "n"],
    "hiroko stageshow cat": ["h"],
    "sayori stageshow catalepsy": ["k", "s", "n"],
    "sayori chicken1": ["k", "s"],
    "sayori chicken2": ["k", "s"],
    "sayori doll bad end single image": ["s"],
    "sayori doll good end": ["k", "s"],
    "hiroko good end 1": ["k", "h"],
    "copycat ending 1 single image": ["h", "n", "a", "s", "k"],
    #Page 24
    "copycat ending 2_1": ["k", "a"],
    "copycat ending 2_2": ["k", "a"],
    "redemption ending 1_1": ["k", "a"],
    "redemption ending 1_2": ["k", "a"],
    "forced girlfriend ending": ["n", "k"],
    "hiroko park hypno": ["h"],
    "hiroko park ending 1 single image": ["h", "k"],
    "hiroko cafe": ["h"],
    "robot karaoke end": ["n", "h"],
    #Page 25
    "k bedroom robot nozomi": ["k","n"],
    "k bedroom robot sayori": ["k", "s"],
    "k bedroom robot hiroko": ["k", "h"],
    "sayori alter confrontation2": ["n", "s"],
    "sayori alter coop end": ["s", "k"],
    "alter bad end 1": ["s"],
    "sayori alter bad end 2": ["s", "k"],
    "alter good end 1": ["s"],
    "tennis bot end 3": ["h", "k"],
    #Page 26
    "nozomi good end 1": ["n", "k"],
}

##A function to check whether the tags are all at 0 (no filters applied)
init python:
    def all_filters_off(cg_tags):
        result = True #First the tag "result" is set to True by defualt
        for tag in cg_tags: #Then it goes over all the tags. 
            if cg_tags[tag] != 0: #If it finds that any of them is not zero; not all fitlers are off. Otherwise, it will remain as True in the end.
                result = False 
        return result #Then we return the result. 

##A function to check whether a given CG passes the filters of the cg tags
init python:
    def group_passes_filter(group_name, filters): #"Group name" would be the name of a CG from the list cg_groups, while "filters" is the list of tags used for filtering. Here we'd input "cg_tags"
        tags = cg_group_tags.get(group_name, []) #We extract the tags a CG has assigned on the cg_group_tags list. For example, if group_name = "rooftop day", it will extract "n", "h", "s".

        for tag, state in filters.items():
            if state == 1 and tag not in tags: #If a tag from cg_tags is set to 1 (positive filter) and it's NOT present on the CG, return False
                return False
            if state == -1 and tag in tags: #If a tag from cg_tags  is set to -1 (negative filter) and it IS present on the CG, return False
                return False

        return True #If the previous for cycle concluded without triggering any "return False", then the CG passed all the fitlers, and thus we return True

##A screen basically used as a function for the filter buttons that allow you to mark any given tag as positive or negative filter
screen filter_button(tag, label, name_color): #"tag" would be the tag the button is for. "label" is the name attached, such as "Kyou" for "k", and "name_color" is there to colorcode, such as pink for Hiroko
    $ bg_check = "#4CAF50" #Color for the check button
    $ bg_check_hover = "#92ff98" #Color for the check button when the cursor is hovering on it
    $ bg_x = "#F44336" #Color for the X button
    $ bg_x_hover = "#E57373" #Color for the X button when the cursor is hovering on it
    $ bg_disabled = "#444" #Color for either button when they're disabled
    $ bg_disabled_hover = "#909090" #Color for either button when they're disabled and the cursor is hovering on them

    hbox:
        spacing 8
        text "[label]": #The name of the filter being displayed
            drop_shadow [(3,3)]
            kerning 1
            outlines [(2.8, name_color, 1, 1), (1.0, "#000000ff", 1, 1)]
            if renpy.mobile: #If we're on mobile, make stuff bigger
                size 40
        textbutton "✔": #When you click on this button, it will set the tag to 1, with the goal of allowing only CGs that do have this tag
            if renpy.mobile:
                text_size 35
                ysize 50
                xsize 50
                text_xalign 0.5
            if cg_tags[tag] == 1:
                background bg_check
                hover_background bg_check_hover
            else:
                background bg_disabled
                hover_background bg_disabled_hover
            action SetDict(cg_tags, tag,
            0 if cg_tags[tag] == 1 else #If the tag is already set to 1, the button will set it back to 0 (click again to disable)
            1) #Otherwise (either if it's at 0 or -1), clicking it will set it to 1, its main goal.
        textbutton "✖": #When you click on this button, it will set the tag to -1, with the goal of allowing only CGs that do not have this tag
            if renpy.mobile:
                text_size 40
                ysize 50
                xsize 50
                text_xalign 0.5
            if cg_tags[tag] == -1:
                background bg_x
                hover_background bg_x_hover
            else:
                background bg_disabled
                hover_background bg_disabled_hover
            action SetDict(cg_tags, tag,
            0 if cg_tags[tag] == -1 else #If the tag is already set to -1, the button will set it back to 0 (click again to disable)
            -1) #Otherwise (either if it's at 0 or 1), clicking it will set it to -1, its main goal.
        

init python:
    def reset_cg_filters(): #This function that clears all filters by going over all tags in cg_tags and sets them to 0
        for tag in cg_tags:
            cg_tags[tag] = 0

## A little pop up window to edit the filters
screen tag_filter_popup():
    
    modal True
    zorder 100
    
    button: #A full screen button that closes the filter popup so that clicking anywhere (except the popup itself, since it will be on top) will close the popup
        style "empty" 
        xysize (config.screen_width, config.screen_height)
        action Hide("tag_filter_popup")

    frame:
        align (0.5, 0.5)
        padding (20, 20)
        modal True

        vbox:
            spacing 10

            text "Filter CGs by characters featured or absent": #Text at the top of the popup
                xalign 0.5
                if renpy.mobile:
                    size 35

            hbox: #Putting on row of tags on one hbox and another row on a second hbox, so that they're not all in one line
                spacing 40
                xalign 0.5

                use filter_button("k", "Kyou", "#4B9374")
                use filter_button("n", "Nozomi", "#93624B")
                use filter_button("h", "Hiroko", "#FF89AB")
                use filter_button("s", "Sayori", "#385599")
            
            hbox: 
                spacing 40
                xalign 0.5
                use filter_button("nm", "Atsuko", "#826B81")
                use filter_button("r", "Risa", "#FF9545")
                use filter_button("a", "Akiko", "#5F5C5C")

            null height 15
            if renpy.mobile: #Adding an extra vertical space if we're on mobile so that the "Clear" and "Close" buttons aren't as close to the filter buttons
                null height 30
            hbox:
                spacing 10
                textbutton "Clear": #A button to clear all the filters, calling the reset_cg_filters fucntion that sets all the tags to 0
                    action Function(reset_cg_filters)
                    at Transform(alpha=(0.0 if all_filters_off(cg_tags) else 1.0)) #If all filters are off (all tags set to 0), the "Clear" button will be invisible
                    if renpy.mobile:
                        text_size 35
                
                null width 650
                if renpy.mobile: #Adding an extra empty horizontal space if we're on mobile to ensure the "Close" button is at the edge of the larger popup
                    null width 230

                textbutton "Close": #A button that closes the popup
                    action Hide("tag_filter_popup")
                    xalign 1.0
                    if renpy.mobile:
                        text_size 35


    key "K_ESCAPE" action Hide("tag_filter_popup") #Pressing the ESC key will also close the popup

##Variables for the CG groups
default cg_group_name = None #The name of a given CG
default cg_index = 0 #A counter for members within a given CG group

##CG viewer screen. The screen with the sub menu that should appear when opening a CG set to be able to navigate it
screen cg_viewer():
    #variant "touch" #Keeping this to turn this screen into the touch variant so that I can test the actual mobile version on desktop
    modal True
    zorder 200
    default arrow_width = 50 #This is the width the clickable square shapped area around the arrows will have
    default gallery_ui_visible = True #This variable controls whether the UI is visible.
    default skipping_gallery = False #This is to add a skip mode to go through a CG set quickly
    default rollbacking_gallery = False #This is to add a rollback mode to go backwards through a CG set quickly
    

    add cg_groups[cg_group_name][cg_index] #This is the line that shows the image. cg_group_name is the name of the CG from CG Groups, and cg_index is the number assigned to each image



    if gallery_ui_visible:
        
        #A full screen button that, if either the skip or the rollback mode is active, turns them off. Otherwise moves forward if we're not on the last image, and closes the CG viewer if we are on the last image
        button:
            xfill True
            yfill True
            style "empty_button"
            action If(skipping_gallery or rollbacking_gallery, [ 
                SetScreenVariable("skipping_gallery", False),
                SetScreenVariable("rollbacking_gallery", False),
            ], If(
                cg_index < len(cg_groups[cg_group_name]) - 1,
                [ SetVariable("cg_index", cg_index + 1), Function(renpy.transition, dissolve) ],
                Hide("cg_viewer", transition=dissolve)
            ))
        
        #The CG viewer navigation buttons, with arrow buttons to move back and forth and showing which image out of how many we're on
        hbox:
            style_prefix "cg_viewer" #This is a style I created for the CG viewer
            spacing 10
            xpos 0.5
            ypos 0.85
            xanchor 0.5
            yanchor 0.5

            textbutton "<":
                xsize arrow_width
                ysize arrow_width
                text_xalign 0.5
                text_yalign 0.5
                xoffset 8
                action If(
                    cg_index > 0,
                    [ SetVariable("cg_index", cg_index - 1),
                    Function(renpy.transition, dissolve) ], #If we're not on the first image, move to the previous image with dissolve
                )
                sensitive cg_index > 0 #Make the button sensitive to hover when we're not on the first image

            frame: #Putting this text within a frame to give it a fixed space so that the arrows don't move around when what's display changes in size, for example, when going from 9/N to 10/N
                background None
                xsize arrow_width
                ysize arrow_width
                text "[cg_index + 1]": #This numbers the image we're currently looking at, from 1 to however many there are
                    xalign 0.5
                    yalign 0.5
            frame: 
                background None
                xsize 1 #Giving it 1 point of space, as so that the nubmers are close to each side of the slash
                ysize arrow_width
                text "/": 
                    xalign 0.5
                    yalign 0.5
            frame: 
                background None
                xsize arrow_width
                ysize arrow_width
                text "[len(cg_groups[cg_group_name])]": #This shows how many images there are in total in the CG
                    xalign 0.5
                    yalign 0.5

            textbutton ">":
                xsize arrow_width
                ysize arrow_width            
                action If(
                    cg_index < len(cg_groups[cg_group_name]) - 1, #If we're not on the last image, move to the next image with dissolve
                    [ SetVariable("cg_index", cg_index + 1),
                    Function(renpy.transition, dissolve) ], #This gives it the dissolve animation

                )
                sensitive cg_index < len(cg_groups[cg_group_name]) - 1 #Make the button sensitive to hover when we're not on the last image

        
        hbox: #These buttons appear at the bottom, and are in the style of the quick menu you see in game
            style_prefix "quick"
            spacing 20
            xpos 0.5
            ypos 0.95
            xanchor 0.5
            yanchor 1.0


            textbutton "Return":
                action Hide("cg_viewer", transition=dissolve) #Closing the CG viewer with dissolve
            
            textbutton "Hide UI":
                action SetScreenVariable("gallery_ui_visible", not gallery_ui_visible) #This hides the UI, this way the CG can be seen without obstructions
            
            textbutton "Rollback":
                action [
                    ToggleScreenVariable("rollbacking_gallery"),  #This toggles the rollback mode
                    If(skipping_gallery, SetScreenVariable("skipping_gallery", False)), #If skip mode is on, it will turn it off. These should be mutually exclusive, after all.
                ]
                sensitive cg_index > 0 #Make the button sensitive to hover when we're not on the first image
            
            textbutton "Skip":
                action [
                    ToggleScreenVariable("skipping_gallery"),  #This toggles the skip mode
                    If(rollbacking_gallery, SetScreenVariable("rollbacking_gallery", False)), #If rollback mode is on, it will turn it off. These should be mutually exclusive, after all.
                ]
                sensitive cg_index < len(cg_groups[cg_group_name]) - 1 #Make the button sensitive to hover when we're not on the last image

    else:
        button:  #Here, when the UI is hidden, we make a big button that covers the entire screen to be able to bring it back
            xfill True
            yfill True
            style "empty_button"
            action ToggleScreenVariable("gallery_ui_visible")
    
    #This is to be able to navigate the CG viewer with the keyboard. H to hide and unhide the UI, left and right keys to go back and forth,
    #space bar to move forwarth or close the image if it's the last, and escape to close the CG viewer
    key "K_h" action ToggleScreenVariable("gallery_ui_visible")
    key "K_LEFT" action If(cg_index > 0, [ SetVariable("cg_index", cg_index - 1), Function(renpy.transition, dissolve) ])
    key "K_RIGHT" action If(cg_index < len(cg_groups[cg_group_name]) - 1, [ SetVariable("cg_index", cg_index + 1), Function(renpy.transition, dissolve) ])
    key "K_SPACE" action If(
        cg_index < len(cg_groups[cg_group_name]) - 1,
        [ SetVariable("cg_index", cg_index + 1), Function(renpy.transition, dissolve) ],
        Hide("cg_viewer", transition=dissolve)
    )
    key "K_ESCAPE" action Hide("cg_viewer", transition=dissolve)

    key "K_LCTRL" action [
        ToggleScreenVariable("skipping_gallery"),  #Pressing Ctrl will turn on the skip mode
        If(rollbacking_gallery, SetScreenVariable("rollbacking_gallery", False)), #If rollback mode is on, it will turn it off. These should be mutually exclusive, after all.        
    ] 
    key "keyup_K_LCTRL" action SetScreenVariable("skipping_gallery", False) #Releasing Ctrl will turn off the skip mode

    key "mouseup_4" action If(cg_index > 0, [ SetVariable("cg_index", cg_index - 1)]) #Moving the mousewheel up should also move to the previous image, but WITHOUT the dissolve animation
    key "mouseup_5" action If(cg_index < len(cg_groups[cg_group_name]) - 1, [ SetVariable("cg_index", cg_index + 1)]) #Moving the mousewheel down should also move to the next image, but WITHOUT the dissolve animation

    #Here are the actions of the skip and rollback modes
    timer 0.05 repeat True action If( #When skip mode is on and we're not on the last image, it will move to the next image every 0.05s (20 per second)
        skipping_gallery and cg_index < len(cg_groups[cg_group_name]) - 1,
        SetVariable("cg_index", cg_index + 1)
    )
    
    timer 0.05 repeat True action If( #When skip mode is on and we're on the last image, it will turn off skip mode. At first I made it close the cg viewer, but I think this will give more control
        skipping_gallery and cg_index >= len(cg_groups[cg_group_name]) - 1,
        SetScreenVariable("skipping_gallery", False)
    )

    timer 0.05 repeat True action If( #When rollback mode is on and we're not on the first image, it will move to the previous image every 0.05s (20 per second)
        rollbacking_gallery and cg_index > 0,
        SetVariable("cg_index", cg_index - 1)
    )
    timer 0.05 repeat True action If( #When rollback mode is on and we're on the first image, it will turn off rollback mode
        rollbacking_gallery and cg_index == 0,
        SetScreenVariable("rollbacking_gallery", False)
    )

#A copy of the CG viewer screen with the flag variant "touch" which should make the buttons in the "quick" style bigger on phone
screen cg_viewer():

    variant "touch"
    modal True
    zorder 200
    default arrow_width = 90 #This is the width the clickable square shapped area around the arrows will have
    default gallery_ui_visible = True #This variable controls whether the UI is visible.
    default skipping_gallery = False #This is to add a skip mode to go through a CG set quickly
    default rollbacking_gallery = False #This is to add a rollback mode to go backwards through a CG set quickly
    

    add cg_groups[cg_group_name][cg_index] #This is the line that shows the image. cg_group_name is the name of the CG from CG Groups, and cg_index is the number assigned to each image



    if gallery_ui_visible:
        
        #A full screen button that, if either the skip or the rollback mode is active, turns them off. Otherwise moves forward if we're not on the last image, and closes the CG viewer if we are on the last image
        button:
            xfill True
            yfill True
            style "empty_button"
            action If(skipping_gallery or rollbacking_gallery, [ 
                SetScreenVariable("skipping_gallery", False),
                SetScreenVariable("rollbacking_gallery", False),
            ], If(
                cg_index < len(cg_groups[cg_group_name]) - 1,
                [ SetVariable("cg_index", cg_index + 1), With(dissolve)],
                Hide("cg_viewer", transition=dissolve)
            ))

        #The CG viewer navigation buttons, with arrow buttons to move back and forth and showing which image out of how many we're on
        hbox:
            style_prefix "cg_viewer_mobile" #This is a style I created for the mobile version of the CG viewer
            spacing 10
            xpos 0.5
            ypos 0.80
            xanchor 0.5
            yanchor 0.5
            
            textbutton "<<": #On mobile, I'm moving the Rollback button to this navigation menu
                xsize arrow_width
                ysize arrow_width
                action [
                    ToggleScreenVariable("rollbacking_gallery"),  #This toggles the rollback mode
                    If(skipping_gallery, SetScreenVariable("skipping_gallery", False)), #If skip mode is on, it will turn it off. These should be mutually exclusive, after all.
                ]
                sensitive cg_index > 0 #Make the button sensitive to hover when we're not on the first image
            
            textbutton "<":
                xsize arrow_width
                ysize arrow_width
                text_xalign 0.5
                text_yalign 0.5
                xoffset 20
                action If(
                    cg_index > 0,
                    [ SetVariable("cg_index", cg_index - 1),
                    Function(renpy.transition, dissolve) ], #If we're not on the first image, move to the previous image with dissolve
                )
                sensitive cg_index > 0 #Make the button sensitive to hover when we're not on the first image

            frame: #Putting this text within a frame to give it a fixed space so that the arrows don't move around when what's display changes in size, for example, when going from 9/N to 10/N
                background None
                xsize arrow_width
                ysize arrow_width
                text "[cg_index + 1]": #This numbers the image we're currently looking at, from 1 to however many there are
                    xalign 0.5
                    yalign 0.5
            frame: 
                background None
                xsize 1 #Giving it 1 point of space, as so that the nubmers are close to each side of the slash
                ysize arrow_width
                text "/": 
                    xalign 0.5
                    yalign 0.5
            frame: 
                background None
                xsize arrow_width #Giving it 50 points of space
                ysize arrow_width
                text "[len(cg_groups[cg_group_name])]": #This shows how many images there are in total in the CG
                    xalign 0.5
                    yalign 0.5

            textbutton ">":
                #text_size mobile_buttons_text_size
                xsize arrow_width
                ysize arrow_width            
                action If(
                    cg_index < len(cg_groups[cg_group_name]) - 1, #If we're not on the last image, move to the next image with dissolve
                    [ SetVariable("cg_index", cg_index + 1),
                    Function(renpy.transition, dissolve) ], #This gives it the dissolve animation

                )
                sensitive cg_index < len(cg_groups[cg_group_name]) - 1 #Make the button sensitive to hover when we're not on the last image

            textbutton ">>": #On mobile, I'm moving the skip button to the navigation menu
                xsize arrow_width
                ysize arrow_width 
                action [
                    ToggleScreenVariable("skipping_gallery"),  #This toggles the skip mode
                    If(rollbacking_gallery, SetScreenVariable("rollbacking_gallery", False)), #If rollback mode is on, it will turn it off. These should be mutually exclusive, after all.
                ]
                sensitive cg_index < len(cg_groups[cg_group_name]) - 1 #Make the button sensitive to hover when we're not on the last image
        
        hbox: #These buttons appear at the bottom
            style_prefix "quick_mobile_cg_viewer" #A style like the quick menu style but with a bigger font size
            spacing 20
            xpos 0.5
            ypos 0.95
            xanchor 0.5
            yanchor 1.0

            textbutton "Return":
                action Hide("cg_viewer", transition=dissolve) #Closing the CG viewer with dissolve
            
            textbutton "Hide UI":
                action SetScreenVariable("gallery_ui_visible", not gallery_ui_visible) #This hides the UI, this way the CG can be seen without obstructions

    else:
        button:  #Here, when the UI is hidden, we make a big button that covers the entire screen to be able to bring it back
            xfill True
            yfill True
            style "empty_button"
            action ToggleScreenVariable("gallery_ui_visible")
    
    #Navigation with keyboard won't be necesary on mobile


     
    #Here are the actions of the skip and rollback modes
    timer 0.05 repeat True action If( #When skip mode is on and we're not on the last image, it will move to the next image every 0.05s (20 per second)
        skipping_gallery and cg_index < len(cg_groups[cg_group_name]) - 1,
        SetVariable("cg_index", cg_index + 1)
    )
    
    timer 0.05 repeat True action If( #When skip mode is on and we're on the last image, it will turn off skip mode. At first I made it close the cg viewer, but I think this will give more control
        skipping_gallery and cg_index >= len(cg_groups[cg_group_name]) - 1,
        SetScreenVariable("skipping_gallery", False)
    )

    timer 0.05 repeat True action If( #When rollback mode is on and we're not on the first image, it will move to the previous image every 0.05s (20 per second)
        rollbacking_gallery and cg_index > 0,
        SetVariable("cg_index", cg_index - 1)
    )
    timer 0.05 repeat True action If( #When rollback mode is on and we're on the first image, it will turn off rollback mode
        rollbacking_gallery and cg_index == 0,
        SetScreenVariable("rollbacking_gallery", False)
    )



screen cg_gallery():

    tag menu
    default hover_broom = False
    use navigation
    use game_menu(_("CG Gallery")):

        hbox:
            spacing 10
            #ypos -5
            ypos -20
            xpos -10
            ysize 100
            #xpos 750
            #fixed:
                #ysize 60
            textbutton "Filters":
                text_color "#4C9369"
                text_hover_color "#d9e80d"
                text_selected_color "#ffffff"
                if renpy.mobile:
                    text_size 35
                    ypadding 50
                    xpadding 50
                    ysize 100
                    xpos 715
                    ypos -80
                else:
                    text_size 25
                action Show("tag_filter_popup")
                text_outlines ([ (3, "#d9e80d", 1, 1), (2, "#000000", 1, 1) ] if not all_filters_off(cg_tags) else [ (3, "#000000", 1, 1), (2, "#0000", 1, 1) ])

            if not all_filters_off(cg_tags):
                button:
                    if renpy.mobile:
                        xsize 60
                        ysize 60
                        xpos 450
                        ypos -60
                        hover_background "#ffffff87"
                    else:
                        xsize 25
                        ysize 25
                    hovered SetScreenVariable("hover_broom", True)
                    unhovered SetScreenVariable("hover_broom", False)
                    text "🧹":
                        xalign 0.5
                        yalign 1
                        if renpy.mobile:
                            size (40 if hover_broom else 35)
                        else:
                            size (25 if hover_broom else 20)
                    action [Function(reset_cg_filters), SetScreenVariable("hover_broom", False)]

        vbox:
            ypos 26
            spacing 0

            frame background None ypos 10:
                vpgrid:
                    style "gallery_window"
                    cols gal_cols
                    ypos -20 #xspacing 10
                    xspacing 0
                    draggable True
                    mousewheel True
                    spacing 24
                    xalign 0.0
                    #yoffset -35

                    scrollbars "vertical"
                    xoffset -20
                    #add g_cg.make_button("titlescreen", "titlescreen butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24) at cg_hover_zoom
                    if group_passes_filter("titlescreen", cg_tags):
                        fixed:
                            xsize thumbnail_x
                            ysize thumbnail_y

                            add g_cg.make_button(
                                "titlescreen",
                                "titlescreen butt",
                                im.Scale("cg locked.png", thumbnail_x, thumbnail_y),
                                xalign=0.53,
                                yalign=0.5,
                                idle_border=None,
                                background=None
                            ) at cg_hover_zoom

                    for group_name in cg_groups: #This cycle goes over all the CGs in the list of CG groups and creates a button for each of them
                        if group_passes_filter(group_name, cg_tags):
                            add cg_button(group_name)                
                #(There's no need to denote pages as such in the current CG Gallery code, but keeping this format is still useful for me visually when looking for a particular CG
                #Page 1
                
                #add g_cg.make_button("kyou intro", "kyou intro butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24) #at cg_hover_zoom
                #add g_cg.make_button("stageshow", "stageshow butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("stageshow")
                #add g_cg.make_button("classroom nozomi", "classroom nozomi butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko_tennis1", "hiroko_tennis1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24) #at cg_hover_zoom
                #add g_cg.make_button("sayori intro", "sayori intro butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori study", "sayori study butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #if getattr(persistent, "sayori_study_unlock", False):
                #    imagebutton:
                #        idle "sayori study butt"
                #        action [
                #            SetVariable("cg_group_name", "sayori study"),
                #            SetVariable("cg_index", 0),
                #            ShowMenu("cg_viewer", _transition=dissolve)
                #        ]
                #else:
                #    add g_cg.make_button("sayori study", "sayori study button", "sayori study locked button")

                #add cg_button("sayori study")

                #add g_cg.make_button("sports shed night", "sports shed night butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("classroom lunch day2", "classroom lunch day2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 2
                #add g_cg.make_button("rooftop day", "rooftop day butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("delusion rooftop", "delusion rooftop butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("delusion rooftop")

                #add g_cg.make_button("alley hiroko", "alley hiroko butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("akiko science", "akiko science butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("akiko science")
                
                #add g_cg.make_button("devotion start", "devotion start butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("devotion start")
                
                #add g_cg.make_button("robot start", "robot start butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("robot start")
                
                #add g_cg.make_button("sleeper agent start", "sleeper agent start butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sleeper agent start")
                #add g_cg.make_button("hiroko walk", "hiroko walk butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                ##add cg_button("hiroko walk")
                
                #add g_cg.make_button("k bedroom hiroko", "k bedroom hiroko butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 3
                #add g_cg.make_button("redemption start", "redemption start butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("redemption start")

                #add g_cg.make_button("devotion bedroom day2", "devotion bedroom day2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("devotion bedroom day2")
                
                #add g_cg.make_button("hiroko robot programming", "hiroko robot programming butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("hiroko robot programming")

                #add g_cg.make_button("study room sayori", "study room sayori butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko vs risa", "hiroko vs risa butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("hiroko vs risa")
                
                #add g_cg.make_button("nozomi cafe uniform", "nozomi cafe uniform butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomi cafe")

                #add g_cg.make_button("k room nozomi", "k room nozomi butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("k room hiroko", "k room hiroko butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("classroom lunch day3", "classroom lunch day3 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 4
                #add g_cg.make_button("classroom lunch 2 delusion", "classroom lunch 2 delusion butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("classroom lunch2 delusion")

                #add g_cg.make_button("akiko student council hypno", "akiko student council hypno butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("akiko student council hypno")
                
                #add g_cg.make_button("sleeper agent night", "sleeper agent night butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sleeper agent night")
                
                #add g_cg.make_button("akiko student council hypno2", "akiko student council hypno2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("akiko student council hypno2")

                #add g_cg.make_button("hiroko trapped", "hiroko trapped butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("creepy hiroko", "creepy hiroko butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("creepy hiroko")
                
                #add g_cg.make_button("hiroko tickle", "hiroko tickle butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("hiroko tickle")

                #add g_cg.make_button("hiroko couch argument", "hiroko couch argument butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("hiroko couch argument")

                #add g_cg.make_button("sayori arm", "sayori arm butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sayori arm")
                #Page 5
                #add g_cg.make_button("k room nozomi2", "k room nozomi2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("zombie beginning", "zombie beginning butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("zombie beginning")

                #add g_cg.make_button("nozomi injured", "nozomi injured butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomi injured")

                #add g_cg.make_button("sayori sleeper capture", "sayori sleeper capture butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sayori sleeper capture")

                #add g_cg.make_button("classroom lunch day4", "classroom lunch day4 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("akiko intro", "akiko intro butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("akiko intro")
                
                #add g_cg.make_button("k room nozomi reversal1", "k room nozomi reversal1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                ##add cg_button("k room nozomi reversal1")

                #add g_cg.make_button("k room nozomi tv", "k room nozomi tv butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("k room hiroko tv", "k room hiroko tv butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 6
                #add g_cg.make_button("k room hiroko reversal", "k room hiroko reversal butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko cat 2", "hiroko cat 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("hiroko cat 2")
                
                #add g_cg.make_button("hiroko cat 1", "hiroko cat 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("k room sayori", "k room sayori butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("k bedroom sayori", "k bedroom sayori butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori greeting", "sayori greeting butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sayori greeting")

                #add g_cg.make_button("nozomi sleeper capture", "nozomi sleeper capture butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomisleepercapture")
                
                #add g_cg.make_button("delusion struggle sayori", "delusion struggle sayori butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("delusion struggle sayori")
                
                #add g_cg.make_button("devotion bedroom day4_1", "devotion bedroom day4_1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("devotion tennis")

                #Page 7
                #add g_cg.make_button("devotion bedroom day4_2", "devotion bedroom day4_2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("devotion tennis partial")

                #add g_cg.make_button("devotion bedroom day4_3", "devotion bedroom day4_3 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("devotion underwear")

                #add g_cg.make_button("devotion bedroom day4_4", "devotion bedroom day4_4 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("devotion naked")
                
                #add g_cg.make_button("study room hypno sayori", "study room hypno sayori butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("study room hypno sayori")

                #add g_cg.make_button("k phone robot", "k phone robot butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("k phone robot")
                
                #add g_cg.make_button("nozomi robot kiss", "nozomi robot kiss butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24) #at cg_hover_zoom
                #add g_cg.make_button("nozomi mindtrick", "nozomi mindtrick butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomi mindtrick")

                #add g_cg.make_button("nozomi hiroko hug", "nozomi hiroko hug butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomi hiroko hug")

                #add g_cg.make_button("sayori lunch", "sayori lunch butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sayori lunch")

                #Page 8
                #add g_cg.make_button("sayori grab", "sayori grab butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sayori grab")

                #add g_cg.make_button("sayori x kyou", "sayori x kyou butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori walk", "sayori walk butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sayori walk")

                #add g_cg.make_button("hiroko shoe", "hiroko shoe butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("hiroko shoe")
                
                #add g_cg.make_button("hiroko yawn day", "hiroko yawn day butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("hiroko yawn day")
                
                #add g_cg.make_button("classroom lunch day5", "classroom lunch day5 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("classroom lunch 2 sleeper", "classroom lunch 2 sleeper butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("rooftop devotion", "rooftop devotion butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("rooftop robot", "rooftop robot butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("rooftop robot")
                
                #Page 9
                #add g_cg.make_button("rooftop robot girlfriend", "rooftop robot girlfriend butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("rooftop robot  girlfriend")
                
                #add g_cg.make_button("hiroko yawn eve", "hiroko yawn eve butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("hiroko yawn eve")
                
                #add g_cg.make_button("hiroko tennis kiss", "hiroko tennis kiss butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi collapse", "nozomi collapse butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("trance stop end", "trance stop end butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("trance stop end")
                
                #add g_cg.make_button("nozomi robot programming", "nozomi robot programming butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomi robot programming")

                #add g_cg.make_button("study room nozomi", "study room nozomi butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("study room hypno nozomi", "study room hypno nozomi butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("study room hypno nozomi")
                
                #add g_cg.make_button("nozomi chocolate", "nozomi chocolate butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomi chocolate")
                
                #Page 10
                #add g_cg.make_button("akiko breakfast", "akiko breakfast butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("akiko breakfast")
                
                #add g_cg.make_button("hiroko racket", "hiroko racket butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("hiroko racket")

                #add g_cg.make_button("k room akiko", "k room akiko butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("redemption phone day", "redemption phone day butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("redemption phone day")
                
                #add g_cg.make_button("k room sayori day", "k room sayori day butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("zombie bedroom 1", "zombie bedroom 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("zombie bedroom 1 1")

                #add g_cg.make_button("zombie bedroom 2", "zombie bedroom 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("zombie bedroom 2")
                
                #add g_cg.make_button("nozomi boardgame", "nozomi boardgame butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomi boardgame")

                #add g_cg.make_button("nozomi boardgame 2", "nozomi boardgame 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomi boardgame2")
                
                #Page 11
                #add g_cg.make_button("n bedroom hypnobondage", "n bedroom hypnobondage butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("n bedroom hypnobondage tickling", "n bedroom hypnobondage tickling butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomi hypnobondage tickling")
                
                #add g_cg.make_button("n bedroom hypnobondage spanking", "n bedroom hypnobondage spanking butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomi hypnobondage spanking")
                
                #add g_cg.make_button("sayori alter lunch", "sayori alter lunch butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sayori alter lunch")

                #add g_cg.make_button("sayori arcade 2", "sayori arcade 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sayori arcade2")

                #add g_cg.make_button("sayori penlight", "sayori penlight butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sayori penlight")
                
                #add g_cg.make_button("sayori bed 1", "sayori bed 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sayori bed1")
                
                #add g_cg.make_button("sayori hug", "sayori hug butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("sayori hug")

                #add g_cg.make_button("k bedroom confrontation sayori", "k bedroom confrontation sayori butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 12
                #add g_cg.make_button("k bedroom confrontation hiroko", "k bedroom confrontation hiroko butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sleeper agent struggle", "sleeper agent struggle butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sleeper agent defeat", "sleeper agent defeat butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("n burglar", "n burglarbutt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("n burglar undressing", "n burglar undressing butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("akiko makeover 1", "akiko makeover 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("akiko makeover 2", "akiko makeover 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("copycat karaoke hypno 1", "copycat karaoke hypno 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("copycat karaoke hypno 2", "copycat karaoke hypno 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 13
                #add g_cg.make_button("copycat karaoke 1", "copycat karaoke 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("copycat karaoke2", "copycat karaoke 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("copycat karaoke 3", "copycat karaoke 3 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi cafe casual", "nozomi cafe casual butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi captured", "nozomi captured butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi window", "nozomi window butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi argument", "nozomi argument butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori fallen", "sayori fallen butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori sleep", "sayori sleep butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 14
                #add g_cg.make_button("sayori sitting", "sayori sitting butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi kneeling devotion", "nozomi kneeling devotion butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("classroom 2 hiroko", "classroom 2 hiroko butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko classroom rehearsal", "hiroko classroom rehearsal butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori arcade", "sayori arcade butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori room hypno 2", "sayori room hypno 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori room tickle", "sayori room tickle butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko gaming", "hiroko gaming butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko slumped", "hiroko slumped butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 15
                #add g_cg.make_button("hiroko court night good", "hiroko court night good butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko court night bad", "hiroko court night bad butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko park sad", "hiroko park sad butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko won", "hiroko won butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko cam 1", "hiroko cam 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko cam 2", "hiroko cam 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko karaoke bed 2", "hiroko karaoke bed 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko bed", "hiroko bed butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko couch", "hiroko couch butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 16
                #add g_cg.make_button("hiroko couch 2", "hiroko couch 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("hiroko couch2")
                #add g_cg.make_button("nozomi karaoke group", "nozomi karaoke group butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori dinner", "sayori dinner butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori alter hug", "sayori alter hug butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("akiko slapped", "akiko slapped butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("rooftop reversal", "rooftop reversal butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi threatening", "nozomi threatening butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi sorry", "nozomi sorry butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi couch hypno", "nozomi couch hypno butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 17
                #add g_cg.make_button("nozomi tortured tickle", "nozomi tortured tickle butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi tortured spank", "nozomi tortured spank butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko cam 4", "hiroko cam 4 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko cam 3", "hiroko cam 3 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi cam hypno", "nozomi cam hypno butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko cam kiss", "hiroko cam kiss butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko cam 5", "hiroko cam 5 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko nozomi phone", "hiroko nozomi phone butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("reversal bad end", "reversal bad end butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("reversal good end", "reversal good end butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 18
                #add g_cg.make_button("sayori alter confrontation 1", "sayori alter confrontation 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("akiko intro 2", "akiko intro 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("akiko kendo", "akiko kendo butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sword strike", "sword strike butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("akiko cornered", "akiko cornered butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("redemption phone eve", "redemption phone eve butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("voodoo phone", "voodoo phone butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko scared", "hiroko scared butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("bathroom ambush", "bathroom ambush butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 19
                #add g_cg.make_button("voodoo phone 2", "voodoo phone 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("akiko kiss", "akiko kiss butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("spiral ending", "spiral ending butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori alter bad end 3", "sayori alter bad end 3 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko rooftop 1-1", "hiroko rooftop 1-1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko rooftop 1-2", "hiroko rooftop 1-2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko rooftop 2", "hiroko rooftop 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("penlight broken", "penlight broken butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("rooftop nozomi_tickled", "rooftop nozomi_tickled butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 20
                #add g_cg.make_button("rooftop nozomi_spanked", "rooftop nozomi_spanked butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi rooftop tickle2", "nozomi rooftop tickle2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi rooftop spank2", "nozomi rooftop spank2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi provoke", "nozomi provoke butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi couch strip", "nozomi couch strip butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi kneeling trance", "nozomi kneeling trance butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi zombie walk", "nozomi zombie walk butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add cg_button("nozomi zombie walk")                
                #add g_cg.make_button("nozomi lying", "nozomi lying butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi kitchen", "nozomi kitchen butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 21
                #add g_cg.make_button("nozomi omelette", "nozomi omelette butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("nozomi kiss", "nozomi kiss butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hypno rehearsal 1", "hypno rehearsal 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hypno rehearsal 2", "hypno rehearsal 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("zombie bedroom 3", "zombie bedroom 3 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori room hypno", "sayori room hypno butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)                
                #add g_cg.make_button("sayori doll pose 1", "sayori doll pose 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori doll pose 2", "sayori doll pose 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori doll scene climax", "sayori doll scene climax butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 22
                #add g_cg.make_button("hiroko yikes end", "hiroko yikes end butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko betrayal", "hiroko betrayal butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori alter good end 2", "sayori alter good end 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("devotion end 1", "devotion end 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("devotion end 2", "devotion end 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("delusion end 1", "delusion end 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("trance abuse end", "trance abuse end butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("school cafe 1", "school cafe 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("zombie ending 1", "zombie ending 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 23
                #add g_cg.make_button("hiroko stageshow good", "hiroko stageshow good butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko stageshow cat", "hiroko stageshow cat butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori stageshow catalepsy", "sayori stageshow catalepsy butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori chicken 1", "sayori chicken 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori chicken 2", "sayori chicken 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori doll bad end", "sayori doll bad end butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori doll good end", "sayori doll good end butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko good end 1", "hiroko good end 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("copycat ending 1", "copycat ending 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 24
                #add g_cg.make_button("copycat ending 2_1", "copycat ending 2_1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("copycat ending 2_2", "copycat ending 2_2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("redemption ending 1_1", "redemption ending 1_1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("redemption ending 1_2", "redemption ending 1_2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("forced girlfriend ending", "forced girlfriend ending butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko park hypno", "hiroko park hypno butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko park ending 1", "hiroko park ending 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("hiroko cafe", "hiroko cafe butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("robot karaoke end", "robot karaoke end butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 25
                #add g_cg.make_button("k bedroom robot nozomi", "k bedroom robot nozomi butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("k bedroom robot sayori", "k bedroom robot sayori butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("k bedroom robot hiroko", "k bedroom robot hiroko butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori alter confrontation 2", "sayori alter confrontation 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori alter coop end", "sayori alter coop end butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori alter bad end 1", "sayori alter bad end 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori alter bad end 2", "sayori alter bad end 2 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("sayori alter good end 1", "sayori alter good end 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #add g_cg.make_button("tennis bot end 3", "tennis bot end 3 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
                #Page 26
                #add g_cg.make_button("nozomi good end 1", "nozomi good end 1 butt", im.Scale("cg locked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)

#GALLERIES END

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    hover_color "#d9e80d"
    outlines [ (2.3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style gallery_window:
    bar_invert True
    bar_vertical True
    xsize 900
    ysize 550
    idle_color "#4C9369"
    hover_color "#d9e80d"
    selected_color "#ffffff"


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():
    python:
        if not persistent.set_volumes:
            _preferences.volumes['music'] *= 0.65
            _preferences.volumes['sfx'] *= 0.65
            persistent.set_volumes = True
    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("CG Gallery") action ShowMenu("cg_gallery")

        textbutton _("Patreon") action Confirm(_("This will open a window in your web browser. Are you sure?"), OpenURL("https://www.patreon.com/angelademille"))

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text:
    size 26
    idle_color "#4C9369"
    hover_color "#d9e80d"
    selected_color "#ffffff"
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    imagemap:
        ground "title.png"
        # hover "title secret.png"
        # hotspot (1028,289,0,0) action Confirm(_("This will open a window in your web browser. Are you sure?"), OpenURL("http://www.patreon.com/angelademille"))
        hotspot (1008,320,28,30) action If(cheat_count == 3, Confirm(_("Do you want to unlock all CGs?"), (Call("cg_cheat")), (SetVariable("cheat_count",0))), SetVariable("cheat_count",cheat_count+1))

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            # text "[config.name!t]":
            #     style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text:
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    size 20
    color '#d9e80d'

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 0 #Originally 10
    ysize 590 #Originally not present

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    # color gui.accent_color
    color "#4C9369"
    yalign 0.5
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text:
    color "#4C9369"
style about_text is gui_text:
    selected_idle_color "#4C9369"

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text:
    color "#4C9369"
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1
style page_button is gui_button
style page_button_text is gui_button_text:
    hover_color "#d9e80d"
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text:
    hover_color "#d9e80d"
    outlines [ (2.3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
            hbox:
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton _("English") action Language(None)
                    textbutton _("Spanish") action Language("spanish")

                vbox:
                    style_prefix "radio"
                    label _("Text Background")
                    textbutton _("Disabled") action StylePreference("text_background", "background_off"), SetVariable ('persistent.text_background','clear'), style.rebuild
                    textbutton _("Enabled") action StylePreference("text_background", "background_on"), SetVariable ('persistent.text_background','opaque'), style.rebuild


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text:
    color "#4C9369"
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1
style radio_button is gui_button
style radio_button_text is gui_button_text:
    hover_color "#d9e80d"
    selected_color "#ffffff"
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text:
    color "#4C9369"
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1
style check_button is gui_button
style check_button_text is gui_button_text:
    hover_color "#d9e80d"
    selected_color "#ffffff"
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text:
    color "#4C9369"
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text:
    color "#4C9369"
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text:
    hover_color "#d9e80d"
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1
    # selected_color "#ffffff"

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style pref_vbox:
    xsize 275

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]
    kerning 1

style slider_vbox:
    xsize 450


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    outlines [ (3, "#000000", 1, 1) ]
    drop_shadow [(3,3)]

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text:
    hover_color "#d9e80d"
    selected_color "#ffffff"
style help_label is gui_label
style help_label_text is gui_label_text:
    color "#4C9369"
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text:
    hover_color "#4C9369"

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
    color "#1d97a4"

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()
        textbutton _("Hide") action HideInterface()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
