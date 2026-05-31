# The game starts here.

#TODO:
#Nozomi Route - Really want Nozomi to comment early on regarding the clichédness of Kyou using a penlight as a hypnosis tool, which Kyou is probably oblivious to
#Nozomi Route - Day 13 final dialogue could do with more reactions from Kyou to what Nozomi's saying

init python:
    renpy.add_layer("hilayer", above="master") # Add a layer above the default background layer so we can lay a darkening effect on top of it
    renpy.add_layer("toplayer", above="hilayer") # Add a layer above the high layer so we can keep some things undarkened
    renpy.music.register_channel("sfx2", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("sfx3", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("bgm2", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    if renpy.variant("small"):
        renpy.register_style_preference("text_background", "background_on", style.window, "background", "gui/phone/textbox.png")
    else:
        renpy.register_style_preference("text_background", "background_on", style.window, "background", "gui/textbox.png")
    renpy.register_style_preference("text_background", "background_off", style.window, "background", "gui/clear_textbox.png")
    credits = (_('Writing'), 'Angela DeMille'), (_('Sprite Art'), 'Armando Sionosa (Innovator123)'), (_('CG Art'), 'Armando Sionosa (Innovator123)'), \
    (_('Backgrounds'), 'minikle (dlsite.com)'), (_('Programming'), 'Angela DeMille'), (_('Spanish Translation'), 'Oswaldo B. (Waldo)'), \
    (_('Music'), 'Chris Collins (indiemusicbox.com)'), (_('Music'), 'Cristoph Rauch Music (CRM)'), \
    (_('Music'), 'Gowler Music'), (_('Music'), 'Kevin MacLeod (incompetech.com)'), (_('Music'), 'Ayato Sound Create'), (_('Music'), 'Alex Beroza (ccmixter.org/AlexBeroza)'), (_('Music'), 'wellman (ccmixter.org/wellman)'), (_('Sound'), 'www.soundbyter.com'), \
    (_('Sound'), 'www.zapsplat.com'), (_('Sound'), 'www.soundjay.com'), (_('Sound'), 'www.fesliyanstudios.com'), \
    (_('Sound'), 'Mike Koenig (soundbible.com)'), (_('Sound'), 'www.picturetosound.com'), (_('Sound'), 'benzix2 (freesound.com)'), (_('Sound'), 'ultradust (freesound.com)'), \
    (_('Angel Cake ($10) Backers'), "Mokou Moe"), (_('Angel Cake ($10) Backers'), "keikun99"), (_('Angel Cake ($10) Backers'), "Giovanni Bermeo"), (_('Angel Cake ($10) Backers'), "Sieth8989"), (_('Angel Cake ($10) Backers'), "Trinity"), \
    (_('Angel Cake ($10) Backers'), "DirectorBlack"), (_('Angel Cake ($10) Backers'), "Doa"), (_('Angel Cake ($10) Backers'), "Clants"), (_('Angel Cake ($10) Backers'), "JJS"), \
    (_('Angel Cake ($10) Backers'), "TheKayOne"), (_('Angel Cake ($10) Backers'), "Cristian C"), (_('Angel Cake ($10) Backers'), "HMfan"), (_('Angel Cake ($10) Backers'), "John Glenn"), \
    (_('Angel Cake ($10) Backers'), "Steven Swope"), (_('Angel Cake ($10) Backers'), "Kigo"), (_('Angel Cake ($10) Backers'), "Argo"), (_('Angel Cake ($10) Backers'), "Aaron Grey"), \
    (_('Angel Cake ($10) Backers'), "Erina Blaze"), (_('Angel Cake ($10) Backers'), "Matthew Codispoti"), (_('Angel Cake ($10) Backers'), "Marcel Weniger"), (_('Angel Cake ($10) Backers'), "Kris Van Gucht"), \
    (_('Angel Cake ($10) Backers'), "Thorbjørn Prochnow Sletten"), (_('Angel Cake ($10) Backers'), "ok"), (_('Angel Cake ($10) Backers'), "xstationo"), (_('Angel Cake ($10) Backers'), "Brian Bentley"), \
    (_('Angel Cake ($10) Backers'), "Darkos619"), (_('Angel Cake ($10) Backers'), "Niels van Leuken"), (_('Angel Cake ($10) Backers'), "Chiaki"), (_('Angel Cake ($10) Backers'), "Craig Kuhnert"), \
    (_('Angel Cake ($10) Backers'), "Cueballl"), (_('Angel Cake ($10) Backers'), "RayRay"), (_('Angel Cake ($10) Backers'), "Scythe"), (_('Angel Cake ($10) Backers'), "Okko Knuuttila"), \
    (_('Angel Cake ($10) Backers'), "Matthew Garbidor"), (_('Angel Cake ($10) Backers'), "Justin Hoyland"), (_('Angel Cake ($10) Backers'), "Kraz Master"), (_('Angel Cake ($10) Backers'), "MidnightCake"), \
    (_('Angel Cake ($10) Backers'), "G"), (_('Angel Cake ($10) Backers'), "chiobio"), (_('Angel Cake ($10) Backers'), "Lyaruil"), (_('Angel Cake ($10) Backers'), "Xinrui Zhang"), (_('Angel Cake ($10) Backers'), "MVB"), \
    (_('Angel Cake ($10) Backers'), "Slicknastyda2nd"), (_('Angel Cake ($10) Backers'), "Julian Edwards"), (_('Angel Cake ($10) Backers'), "Andre Seifert"), (_('Angel Cake ($10) Backers'), "Madibat"), \
    (_('Angel Cake ($10) Backers'), "Patrick Hattrick"), (_('Angel Cake ($10) Backers'), "Pat"), (_('Angel Cake ($10) Backers'), "Kevin Emerson"), (_('Angel Cake ($10) Backers'), "Gin"), \
    (_('Angel Cake ($10) Backers'), "Fukurou Yoru"), (_('Angel Cake ($10) Backers'), "konane"), (_('Angel Cake ($10) Backers'), "GH"), (_('Angel Cake ($10) Backers'), "hokkijek"), \
    (_('Angel Cake ($10) Backers'), "fred"), (_('Angel Cake ($10) Backers'), "Smartorpheus9"), (_('Angel Cake ($10) Backers'), "Parathese"), (_('Angel Cake ($10) Backers'), "Lander Wamsley"), \
    (_('Angel Cake ($10) Backers'), "Polyface"), (_('Angel Cake ($10) Backers'), "Daniel"), (_('Angel Cake ($10) Backers'), "Jedruben"), (_('Angel Cake ($10) Backers'), "Chimerable"), \
    (_('Angel Cake ($10) Backers'), "stardust crusader's overdrive"), (_('Angel Cake ($10) Backers'), "Andrew Morris"), (_('Angel Cake ($10) Backers'), "XXX"), (_('Angel Cake ($10) Backers'), "Ziggy J"), \
    (_('Angel Cake ($10) Backers'), "Lunar Circuit"), (_('Angel Cake ($10) Backers'), "Blessedbycows"), (_('Angel Cake ($10) Backers'), "Baris"), (_('Angel Cake ($10) Backers'), "Michael McNeir"), \
    (_('Angel Cake ($10) Backers'), "Wobben Buffet"), (_('Angel Cake ($10) Backers'), "Joshua Neff"), (_('Angel Cake ($10) Backers'), "Zandor"), \
    (_('Angel Cake ($10) Backers'), "doulomb"), (_('Angel Cake ($10) Backers'), "Mr.milkshake"), (_('Angel Cake ($10) Backers'), "15117083374"), \
    (_('Angel Cake ($10) Backers'), "CarDr"), (_('Angel Cake ($10) Backers'), "junkcron"), (_('Angel Cake ($10) Backers'), "omori fan"), (_('Angel Cake ($10) Backers'), "J"), (_('Angel Cake ($10) Backers'), "Terran Vaughn"), \
    (_('Angel Cake ($10) Backers'), "InverseSpirit27"), (_('Angel Cake ($10) Backers'), "Garry"), (_('Angel Cake ($10) Backers'), "Christopher Pajo"), (_('Angel Cake ($10) Backers'), "Dead Throne"), \
    (_('Angel Cake ($10) Backers'), "James"), (_('Angel Cake ($10) Backers'), "Reimann,Nico"), (_('Angel Cake ($10) Backers'), "OttoM4N-HlX"), (_('Angel Cake ($10) Backers'), "Brad the Lad"), \
    (_('Angel Cake ($10) Backers'), "Dream Searcher"), (_('Angel Cake ($10) Backers'), "Adrian Box"), (_('Angel Cake ($10) Backers'), "Marxster"), (_('Angel Cake ($10) Backers'), "Der Micha"), \
    (_('Angel Cake ($10) Backers'), "Peter O'Reilly"), (_('Angel Cake ($10) Backers'), "Throwawayprn1"), (_('Angel Cake ($10) Backers'), "All Might"), (_('Angel Cake ($10) Backers'), "Adam Gausemel"), \
    (_('Angel Cake ($10) Backers'), "sapphire eyes"), (_('Angel Cake ($10) Backers'), "Thrownaway"), (_('Angel Cake ($10) Backers'), "Robert Kay"), (_('Angel Cake ($10) Backers'), "loljav"), \
    (_('Angel Cake ($10) Backers'), "xyzzyzzyxxysym"), (_('Angel Cake ($10) Backers'), "Giorgio Galli"), (_('Angel Cake ($10) Backers'), "gler P"), (_('Angel Cake ($10) Backers'), "Ruuto"), \
    (_('Angel Cake ($10) Backers'), "Mr. D"), (_('Angel Cake ($10) Backers'), "Misken Basket"), (_('Angel Cake ($10) Backers'), "John Smith"), (_('Angel Cake ($10) Backers'), "Summer Silver"), \
    (_('Angel Cake ($10) Backers'), "MadKing"), (_('Angel Cake ($10) Backers'), "Qbuizzy"), (_('Angel Cake ($10) Backers'), "KaiserGor"), (_('Angel Cake ($10) Backers'), "Aiden Prucker"), \
    (_('Angel Cake ($10) Backers'), "shadow13"), (_('Angel Cake ($10) Backers'), "TerribleBurden"), (_('Angel Cake ($10) Backers'), "Op-Tron"), (_('Angel Cake ($10) Backers'), "Ethan Niedermeyer"), \
    (_('Angel Cake ($10) Backers'), "SomeRandomNamedBob"), (_('Angel Cake ($10) Backers'), "DS"), (_('Angel Cake ($10) Backers'), "ClimbX"), (_('Angel Cake ($10) Backers'), "Dynamite"), \
    (_('Angel Cake ($10) Backers'), "Daniel Matos"), (_('Angel Cake ($10) Backers'), "person1758"), (_('Angel Cake ($10) Backers'), "Corey Bova"), (_('Angel Cake ($10) Backers'), "Roy Cohen"), \
    (_('Angel Cake ($10) Backers'), "chen"), (_('Angel Cake ($10) Backers'), "Steven Murdoch"), (_('Angel Cake ($10) Backers'), "BSOB"), (_('Angel Cake ($10) Backers'), "Valentina"), (_('Angel Cake ($10) Backers'), "Takos"), \
    (_('Angel Cake ($10) Backers'), "Zack Culbreath"), (_('Angel Cake ($10) Backers'), "Garry"), (_('Angel Cake ($10) Backers'), "alex"), (_('Angel Cake ($10) Backers'), "Sothe Dain"), \
    (_('Angel Cake ($10) Backers'), "Nikhil Mohan"), (_('Angel Cake ($10) Backers'), "SentientStone"), (_('Angel Cake ($10) Backers'), "Chris Banas"), (_('Angel Cake ($10) Backers'), "Sleeping Cat Studios"), \
    (_('Angel Cake ($10) Backers'), "Tom Hull"), (_('Angel Cake ($10) Backers'), "Squid"), (_('Angel Cake ($10) Backers'), "LP247"), (_('Angel Cake ($10) Backers'), "steve llama"), \
    (_('Angel Cake ($10) Backers'), "Komogi"), (_('Angel Cake ($10) Backers'), "Noah Goldberg"), (_('Angel Cake ($10) Backers'), "CmderJeremy"), (_('Angel Cake ($10) Backers'), "PlaidX"), \
    (_('Angel Cake ($10) Backers'), "sleepyhead"), (_('Angel Cake ($10) Backers'), "Scott Healy"), (_('Angel Cake ($10) Backers'), "Alice Sysoyev"), (_('Angel Cake ($10) Backers'), "kprotty"),  \
    (_('Angel Cake ($10) Backers'), "Trent Walk"),  (_('Angel Cake ($10) Backers'), "Im Teqno"), (_('Angel Cake ($10) Backers'), "xGDHx"), (_('Angel Cake ($10) Backers'), "Lil Penpusher"), \
    (_('Angel Cake ($10) Backers'), "Melvin"),  (_('Angel Cake ($10) Backers'), "Komrad Nep"), (_('Angel Cake ($10) Backers'), "Pj Tie"), \
    (_('Angel Cake ($10) Backers'), "Andreas Hoem"),  (_('Angel Cake ($10) Backers'), "Ole Jakob Aarsand"), (_('Angel Cake ($10) Backers'), "FlyteKnight"), \
    (_('Angel Cake ($10) Backers'), "Jake"),  (_('Angel Cake ($10) Backers'), "H2Ooze"), (_('Angel Cake ($10) Backers'), "RCPTMOE"), (_('Angel Cake ($10) Backers'), "Valerus_Letarus"), \
    (_('Angel Cake ($10) Backers'), "RandomG"), (_('Angel Cake ($10) Backers'), "Isran Rosiles Sanchez"), (_('Angel Cake ($10) Backers'), "HacedorDeHistorias"), (_('Angel Cake ($10) Backers'), "Michael Domen"), \
    (_('Angel Cake ($10) Backers'), "Daniel Guevara"), (_('Angel Cake ($10) Backers'), "Bean"), (_('Angel Cake ($10) Backers'), "genghis khan"), (_('Angel Cake ($10) Backers'), "pjtie"), \
    (_('Angel Cake ($10) Backers'), "Kt1v3nus"), (_('Angel Cake ($10) Backers'), "FuzionEnderYT"), (_('Angel Cake ($10) Backers'), "FauxTrenchcoat123"), (_('Angel Cake ($10) Backers'), "Kadse Klo"), \
    (_('Angel Cake ($10) Backers'), "Leave me alone Don’t touch me"), (_('Angel Cake ($10) Backers'), "jack sock"), (_('Angel Cake ($10) Backers'), "Peg Leg Panda"), (_('Angel Cake ($10) Backers'), "VoidTime"), \
    (_('Angel Cake ($10) Backers'), "FrightKnight1031"), (_('Angel Cake ($10) Backers'), "qwertybsxq"), (_('Angel Cake ($10) Backers'), "John Smith"), (_('Angel Cake ($10) Backers'), "Chromm"), \
    (_('Angel Cake ($10) Backers'), "Farokjános"), (_('Angel Cake ($10) Backers'), "Miles Murray"), (_('Angel Cake ($10) Backers'), "relrelrel"), (_('Angel Cake ($10) Backers'), "xGDHx"), \
    (_('Angel Cake ($10) Backers'), "GAMEZILLA"), (_('Angel Cake ($10) Backers'), "Toast Butter"), (_('Angel Cake ($10) Backers'), "Over"), (_('Angel Cake ($10) Backers'), "digitama"), \
    (_('Cheesecake ($5) Backers'), "Armaan Babu"), (_('Cheesecake ($5) Backers'), "Sammich"), (_('Cheesecake ($5) Backers'), "Kyle"), (_('Cheesecake ($5) Backers'), "Paragoth"), (_('Cheesecake ($5) Backers'), "Byron Johnson"), \
    (_('Cheesecake ($5) Backers'), "WolfyLeo"), (_('Cheesecake ($5) Backers'), "retroactivefailure"), (_('Cheesecake ($5) Backers'), "Christopher Velez"), \
    (_('Cheesecake ($5) Backers'), "HolySin"), (_('Cheesecake ($5) Backers'), "Jefferson Gilligan"), (_('Cheesecake ($5) Backers'), "KOOLAID"), (_('Cheesecake ($5) Backers'), "littletimo"), \
    (_('Cheesecake ($5) Backers'), "Andrew"), (_('Cheesecake ($5) Backers'), "Johan"), (_('Cheesecake ($5) Backers'), "Arbiter"), (_('Cheesecake ($5) Backers'), "Gunzil"), \
    (_('Cheesecake ($5) Backers'), "Night Moon Entertainment"), (_('Cheesecake ($5) Backers'), "Starcplake"), (_('Cheesecake ($5) Backers'), "Gertt"), (_('Cheesecake ($5) Backers'), "Nictis"), \
    (_('Cheesecake ($5) Backers'), "Aurora"), (_('Cheesecake ($5) Backers'), "Golden Phoenix"), (_('Cheesecake ($5) Backers'), "AP"), \
    (_('Cheesecake ($5) Backers'), "Fernwei"), (_('Cheesecake ($5) Backers'), "Shou234"), (_('Cheesecake ($5) Backers'), "Jose Rios"), (_('Cheesecake ($5) Backers'), "generic.hybridity"), \
    (_('Cheesecake ($5) Backers'), "Antoine Domino"), (_('Cheesecake ($5) Backers'), "Gameknight21"), (_('Cheesecake ($5) Backers'), "Lufen"), (_('Cheesecake ($5) Backers'), "Jared B Kleinman"), \
    (_('Cheesecake ($5) Backers'), "Nathan Day"), (_('Cheesecake ($5) Backers'), "Shockmaster"), (_('Cheesecake ($5) Backers'), "Faelyia"), (_('Cheesecake ($5) Backers'), "Andrew Bryant"), \
    (_('Cheesecake ($5) Backers'), "Revhass"), (_('Cheesecake ($5) Backers'), "Jessie Cook"), (_('Cheesecake ($5) Backers'), "Navvana"), (_('Cheesecake ($5) Backers'), "Rena"), \
    (_('Cheesecake ($5) Backers'), "Jim S"), (_('Cheesecake ($5) Backers'), "Tim"), (_('Cheesecake ($5) Backers'), "Khinzaw"), (_('Cheesecake ($5) Backers'), "Jessie"), (_('Cheesecake ($5) Backers'), "Athaulfs"), \
    (_('Cheesecake ($5) Backers'), "M"), (_('Cheesecake ($5) Backers'), "Negativatron"), (_('Cheesecake ($5) Backers'), "Pax Bernhardt"), (_('Cheesecake ($5) Backers'), "Rolliepolie"), \
    (_('Cheesecake ($5) Backers'), "JJ Gray"), (_('Cheesecake ($5) Backers'), "hiro neko"), (_('Cheesecake ($5) Backers'), "John Steed"), (_('Cheesecake ($5) Backers'), "Eric Ramsey"), \
    (_('Cheesecake ($5) Backers'), "Sun Ce"), (_('Cheesecake ($5) Backers'), "Drew Wood"), \
    (_('Cheesecake ($5) Backers'), "Kaithral"), (_('Cheesecake ($5) Backers'), "JCamit"), (_('Cheesecake ($5) Backers'), "Remi Eikeland"), (_('Cheesecake ($5) Backers'), "Richard Jones"), \
    (_('Cheesecake ($5) Backers'), "BoatyMcBoatface"), (_('Cheesecake ($5) Backers'), "Jeke"), (_('Cheesecake ($5) Backers'), "charliehypno"), (_('Cheesecake ($5) Backers'), "Generic Name"), \
    (_('Cheesecake ($5) Backers'), "DaLertleShrimpie"), (_('Cheesecake ($5) Backers'), "Ceci"), (_('Cheesecake ($5) Backers'), "Ephemerous"), (_('Cheesecake ($5) Backers'), "Joshua Davis"), \
    (_('Cheesecake ($5) Backers'), "Jack Brucz"), (_('Cheesecake ($5) Backers'), "GTisSmoking "), (_('Cheesecake ($5) Backers'), "Adyen"), (_('Cheesecake ($5) Backers'), "Jasmine"), \
    (_('Cheesecake ($5) Backers'), "kolpob"), (_('Cheesecake ($5) Backers'), "Rashid García"), (_('Cheesecake ($5) Backers'), "RobertH"), \
    (_('Cheesecake ($5) Backers'), "James Smallridge"), (_('Cheesecake ($5) Backers'), "Luki Hypno"), (_('Cheesecake ($5) Backers'), "Joshua G."), (_('Cheesecake ($5) Backers'), "Sebastian Just"), \
    (_('Cheesecake ($5) Backers'), "Em Kijo"), (_('Cheesecake ($5) Backers'), "Ralkavi"), (_('Cheesecake ($5) Backers'), "Red Moose"), (_('Cheesecake ($5) Backers'), "V"), \
    (_('Cheesecake ($5) Backers'), "David John Edward Bowdish"), (_('Cheesecake ($5) Backers'), "R"), (_('Cheesecake ($5) Backers'), "Dracula6"), (_('Cheesecake ($5) Backers'), "Daehan Ji"), \
    (_('Cheesecake ($5) Backers'), "RollB"), (_('Cheesecake ($5) Backers'), "Aeryle"), (_('Cheesecake ($5) Backers'), "J C"), (_('Cheesecake ($5) Backers'), "Alex"), \
    (_('Cheesecake ($5) Backers'), "Nunya"), (_('Cheesecake ($5) Backers'), "Jack Henderson"), (_('Cheesecake ($5) Backers'), "Flluffie"), (_('Cheesecake ($5) Backers'), "Defier"), \
    (_('Cheesecake ($5) Backers'), "ProfessorMesmerize"), (_('Cheesecake ($5) Backers'), "Grif end"), (_('Cheesecake ($5) Backers'), "tonmix"), (_('Cheesecake ($5) Backers'), "Genesis"), \
    (_('Cheesecake ($5) Backers'), "yelop"), (_('Cheesecake ($5) Backers'), "Torrin"), (_('Cheesecake ($5) Backers'), "e3"), (_('Cheesecake ($5) Backers'), "D"), \
    (_('Cheesecake ($5) Backers'), "Paul Fischer"), (_('Cheesecake ($5) Backers'), "Kanin Wilson"), (_('Cheesecake ($5) Backers'), "Clowncringe"), (_('Cheesecake ($5) Backers'), "Nagmar"), \
    (_('Cheesecake ($5) Backers'), "silver Bowsman"), (_('Cheesecake ($5) Backers'), "Steve"), (_('Cheesecake ($5) Backers'), "Plasmabolt13 "), \
    (_('Cheesecake ($5) Backers'), "TDL"), (_('Cheesecake ($5) Backers'), "Resident"), (_('Cheesecake ($5) Backers'), "John Doe"), (_('Cheesecake ($5) Backers'), "Patrick DA SILVA FERREIRA"), \
    (_('Cheesecake ($5) Backers'), "Crispy in Spirit"), (_('Cheesecake ($5) Backers'), "Andrew Jackson"), (_('Cheesecake ($5) Backers'), "DarkVenom"), (_('Cheesecake ($5) Backers'), "Bill Bradley (H1Battle)"), \
    (_('Cheesecake ($5) Backers'), "Daidai"), (_('Cheesecake ($5) Backers'), "sunt"), (_('Cheesecake ($5) Backers'), "Hihi"), (_('Cheesecake ($5) Backers'), "Shin007"), \
    (_('Cheesecake ($5) Backers'), "Dani Buijen Van Weelderen"), (_('Cheesecake ($5) Backers'), "f4ngl1d3r"), (_('Cheesecake ($5) Backers'), "Marra"), (_('Cheesecake ($5) Backers'), "royaljelly"), \
    (_('Cheesecake ($5) Backers'), "Dibokucres"), (_('Cheesecake ($5) Backers'), "Jake Bean"), (_('Cheesecake ($5) Backers'), "Lisa Röther"), \
    (_('Cheesecake ($5) Backers'), "Xbit272"), (_('Cheesecake ($5) Backers'), "David Siegel"), (_('Cheesecake ($5) Backers'), "Shrek"), (_('Cheesecake ($5) Backers'), "W.Trickster"), \
    (_('Cheesecake ($5) Backers'), "effectD"), (_('Cheesecake ($5) Backers'), "Kevin M"), (_('Cheesecake ($5) Backers'), "Kaldimaar"), (_('Cheesecake ($5) Backers'), "ThePatron"), \
    (_('Cheesecake ($5) Backers'), "banno muramaro"), (_('Cheesecake ($5) Backers'), "Aaron Silverman"), (_('Cheesecake ($5) Backers'), "BR76"), \
    (_('Cheesecake ($5) Backers'), "Brandon"), (_('Cheesecake ($5) Backers'), "Anonimb0 _01"), (_('Cheesecake ($5) Backers'), "Thomas Barker"), (_('Cheesecake ($5) Backers'), "ekkse159951 ."), \
    (_('Cheesecake ($5) Backers'), "Zach"), (_('Cheesecake ($5) Backers'), "Sett Valentino"), (_('Cheesecake ($5) Backers'), "Skullever"), (_('Cheesecake ($5) Backers'), "Uwawa"), \
    (_('Cheesecake ($5) Backers'), "peter banner"), (_('Cheesecake ($5) Backers'), "Jose Juarez"), (_('Cheesecake ($5) Backers'), "William Christopher Andrews"), (_('Cheesecake ($5) Backers'), "Minerva T"), \
    (_('Cheesecake ($5) Backers'), "Craig"), (_('Cheesecake ($5) Backers'), "Nevercomingback"), (_('Cheesecake ($5) Backers'), "brad klein"), \
    (_('Cheesecake ($5) Backers'), "Ryan Nate"), (_('Cheesecake ($5) Backers'), "Zachary Charles"), (_('Cheesecake ($5) Backers'), "Sonrio12"), (_('Cheesecake ($5) Backers'), "Thomas Howe"), \
    (_('Cheesecake ($5) Backers'), "Honos"), (_('Cheesecake ($5) Backers'), "ODSThero"), (_('Cheesecake ($5) Backers'), "Steven Ross"), (_('Cheesecake ($5) Backers'), "Mycroft L."), \
    (_('Cheesecake ($5) Backers'), "ducks"), (_('Cheesecake ($5) Backers'), "Noah Romelien"), (_('Cheesecake ($5) Backers'), "Aria"), \
    (_('Cheesecake ($5) Backers'), "Jack Dawson"), (_('Cheesecake ($5) Backers'), "Anon"), (_('Cheesecake ($5) Backers'), "Pixelixels"), \
    (_('Cheesecake ($5) Backers'), "Reth"), (_('Cheesecake ($5) Backers'), "Ravenwing"), (_('Cheesecake ($5) Backers'), "Jack Phillips"), (_('Cheesecake ($5) Backers'), "safijieisqn1"), \
    (_('Cheesecake ($5) Backers'), "Parker Mann"), (_('Cheesecake ($5) Backers'), "Thom334"), (_('Cheesecake ($5) Backers'), "Genesis"), (_('Cheesecake ($5) Backers'), "Benjamin Kolarik"), \
    (_('Cheesecake ($5) Backers'), "Petra"), (_('Cheesecake ($5) Backers'), "robert story"), (_('Cheesecake ($5) Backers'), "Ian Trollinger"), (_('Cheesecake ($5) Backers'), "Michael Marinelli"), \
    (_('Cheesecake ($5) Backers'), "Twingo"), (_('Cheesecake ($5) Backers'), "Christopher Barnett"), (_('Cheesecake ($5) Backers'), "Lucas Davies"), (_('Cheesecake ($5) Backers'), "Tristan Casey"), \
    (_('Cheesecake ($5) Backers'), "Tk"), (_('Cheesecake ($5) Backers'), "UrsaMesmer"), (_('Cheesecake ($5) Backers'), "Tanman"), (_('Cheesecake ($5) Backers'), "Richard Blow"), \
    (_('Cheesecake ($5) Backers'), "Ashley Ledvark"), (_('Cheesecake ($5) Backers'), "Zoruko"), (_('Cheesecake ($5) Backers'), "Raphael"), (_('Cheesecake ($5) Backers'), "Kyle R Spinelli"), (_('Cheesecake ($5) Backers'), "beans"), \
    (_('Cheesecake ($5) Backers'), "Harrison J Jones"), (_('Cheesecake ($5) Backers'), "Bob Bob"), (_('Cheesecake ($5) Backers'), "Kade Radmall"), (_('Cheesecake ($5) Backers'), "Richard"), \
    (_('Cheesecake ($5) Backers'), "ilias abbasov"), (_('Cheesecake ($5) Backers'), "Yuno Gasai"), (_('Cheesecake ($5) Backers'), "Braden McClintock"), (_('Cheesecake ($5) Backers'), "Unseen Umpire"), \
    (_('Cheesecake ($5) Backers'), "Robert Dennis"), (_('Cheesecake ($5) Backers'), "Blake Gordon"), (_('Cheesecake ($5) Backers'), "High Moon"), (_('Cheesecake ($5) Backers'), "Uh-stuff"), \
    (_('Cheesecake ($5) Backers'), "RazzAzz"), (_('Cheesecake ($5) Backers'), "Ashley McCallum"), (_('Cheesecake ($5) Backers'), "mitch"), \
    (_('Cheesecake ($5) Backers'), "Hypnotised girl Shan"), (_('Cheesecake ($5) Backers'), "Anthony Hobbs"), (_('Cheesecake ($5) Backers'), "Will Bee"), \
    (_('Cheesecake ($5) Backers'), "Geoff Jolson"), (_('Cheesecake ($5) Backers'), "Michael"), (_('Cheesecake ($5) Backers'), "Gamemaster232"), (_('Cheesecake ($5) Backers'), "rth627"), \
    (_('Cheesecake ($5) Backers'), "Matthew Scott"), (_('Cheesecake ($5) Backers'), "Rick F Romero"), (_('Cheesecake ($5) Backers'), "Glu16"), (_('Cheesecake ($5) Backers'), "Dink"), \
    (_('Cheesecake ($5) Backers'), "Yodiak"), (_('Cheesecake ($5) Backers'), "Darrian Dragneel"), (_('Cheesecake ($5) Backers'), "Blue bone"), (_('Cheesecake ($5) Backers'), "KingGiddorrah"), \
    (_('Cheesecake ($5) Backers'), "Adiboy"), (_('Cheesecake ($5) Backers'), "Hray"), (_('Cheesecake ($5) Backers'), "Andrew Thompson"), (_('Cheesecake ($5) Backers'), "Snargle"), \
    (_('Cheesecake ($5) Backers'), "Cdender"), (_('Cheesecake ($5) Backers'), "Justin Anderson"), (_('Cheesecake ($5) Backers'), "Exoltair"), (_('Cheesecake ($5) Backers'), "Jasper Solt"), (_('Cheesecake ($5) Backers'), "Christopher Juy"),  \
    (_('Cheesecake ($5) Backers'), "Akary"), (_('Cheesecake ($5) Backers'), "Branek"), (_('Cheesecake ($5) Backers'), "Matthew G Hafner"), \
    (_('Cheesecake ($5) Backers'), "Saionji11"), (_('Cheesecake ($5) Backers'), "dylan dragonballsuperz"), (_('Cheesecake ($5) Backers'), "David"), \
    (_('Cheesecake ($5) Backers'), "Frank"), (_('Cheesecake ($5) Backers'), "symop123"), (_('Cheesecake ($5) Backers'), "Nemo Nadie"), (_('Cheesecake ($5) Backers'), "Daniel O'Brien"), (_('Cheesecake ($5) Backers'), "Jace the deck builder"), \
    (_('Cheesecake ($5) Backers'), "Randomnamebeep"), (_('Cheesecake ($5) Backers'), "Mr. Wood"), (_('Cheesecake ($5) Backers'), "teirai"), (_('Cheesecake ($5) Backers'), "Throw Away"), \
    (_('Cheesecake ($5) Backers'), "Timelord Omega"), (_('Cheesecake ($5) Backers'), "Cho Ice"), (_('Cheesecake ($5) Backers'), "DBZFan 531"), (_('Cheesecake ($5) Backers'), "Not a halo fan"), \
    (_('Cheesecake ($5) Backers'), "Sanic The Hodgeheg"), (_('Cheesecake ($5) Backers'), "Christine Ross"), (_('Cheesecake ($5) Backers'), "Hassen"), (_('Cheesecake ($5) Backers'), "tgva8889"), \
    (_('Cheesecake ($5) Backers'), "Linike"), (_('Cheesecake ($5) Backers'), "quyminh"), (_('Cheesecake ($5) Backers'), "Jora, The One Piece Spoiler"), (_('Cheesecake ($5) Backers'), "Ken Powers"), \
    (_('Cheesecake ($5) Backers'), "thehypnofish"), (_('Cheesecake ($5) Backers'), "Wallace"), (_('Cheesecake ($5) Backers'), "Mac mills"), (_('Cheesecake ($5) Backers'), "vahlok"), \
    (_('Cheesecake ($5) Backers'), "Ye Tony"), (_('Cheesecake ($5) Backers'), "shadowking135"), (_('Cheesecake ($5) Backers'), "Nalak"), (_('Cheesecake ($5) Backers'), "Whatthehec"), \
    (_('Cheesecake ($5) Backers'), "Ryan"), (_('Cheesecake ($5) Backers'), "john johna"), (_('Cheesecake ($5) Backers'), "Charles Fedler"), (_('Cheesecake ($5) Backers'), "NiKsplosion2003"), \
    (_('Cheesecake ($5) Backers'), "lazy_bot"), (_('Cheesecake ($5) Backers'), "Norseman"), (_('Cheesecake ($5) Backers'), "ng"), (_('Cheesecake ($5) Backers'), "allthegood"), \
    (_('Cheesecake ($5) Backers'), "Ben Arizona"), (_('Cheesecake ($5) Backers'), "Ashe"),  (_('Cheesecake ($5) Backers'), "Sigurd0812"), \
    (_('Cheesecake ($5) Backers'), "Julien Peter"), (_('Cheesecake ($5) Backers'), "Norman Riggis"),  (_('Cheesecake ($5) Backers'), "Tempest"), (_('Cheesecake ($5) Backers'), "gw1963"), \
    (_('Cheesecake ($5) Backers'), "QQwerty"), (_('Cheesecake ($5) Backers'), "Tyler Foster"), (_('Cheesecake ($5) Backers'), "Killidia"), (_('Cheesecake ($5) Backers'), "Pumpkin God"), \
    (_('Cheesecake ($5) Backers'), "William Xiong"),  (_('Cheesecake ($5) Backers'), "Bart Ligthart"),  (_('Cheesecake ($5) Backers'), "JustAOk"),  (_('Cheesecake ($5) Backers'), "Jacob"), \
    (_('Cheesecake ($5) Backers'), "NobleGryphon"), (_('Cheesecake ($5) Backers'), "Clayton Borkes"), (_('Cheesecake ($5) Backers'), "QuarianHips"), \
    (_('Cheesecake ($5) Backers'), "Doofenshmirtz Evil Incorporated Charity Outreach Program"), (_('Cheesecake ($5) Backers'), "Cammie Dawn"), (_('Cheesecake ($5) Backers'), "SoulTy"), (_('Cheesecake ($5) Backers'), "Darakkuu"), \
    (_('Cheesecake ($5) Backers'), "Teslakaine"), (_('Cheesecake ($5) Backers'), "James Copper"), (_('Cheesecake ($5) Backers'), "madnessoreilli "), (_('Cheesecake ($5) Backers'), "oliver plaman"), \
    (_('Cheesecake ($5) Backers'), "DEADSKULLZ"), (_('Cheesecake ($5) Backers'), "Alex Kelley"), (_('Cheesecake ($5) Backers'), "Akane Hashimi"), (_('Cheesecake ($5) Backers'), "Mako m"), \
    (_('Cheesecake ($5) Backers'), "Nicholas Harris"), (_('Cheesecake ($5) Backers'), "Jacob Barr"), (_('Cheesecake ($5) Backers'), "Manas Annugu"), (_('Cheesecake ($5) Backers'), "pastdark"), \
    (_('Cheesecake ($5) Backers'), "Christophe Pettus"), (_('Cheesecake ($5) Backers'), "Gimble"), (_('Cheesecake ($5) Backers'), "enji rickson"), (_('Cheesecake ($5) Backers'), "Thetacron"), \
    (_('Cheesecake ($5) Backers'), "Kristoffer Schuh"), (_('Cheesecake ($5) Backers'), "RD64"), (_('Cheesecake ($5) Backers'), "kie coo"), (_('Cheesecake ($5) Backers'), "Natasha"), \
    (_('Cheesecake ($5) Backers'), "Bastion"), (_('Cheesecake ($5) Backers'), "DrnNck1"), (_('Cheesecake ($5) Backers'), "William Becker"), (_('Cheesecake ($5) Backers'), "MegaZeroX"), \
    (_('Cheesecake ($5) Backers'), "Fandaniel"), (_('Cheesecake ($5) Backers'), "ddrfanboy"), (_('Cheesecake ($5) Backers'), "Luke Smith"), (_('Cheesecake ($5) Backers'), "joe manson"), \
    (_('Cheesecake ($5) Backers'), "xGDHx"), (_('Cheesecake ($5) Backers'), "Luis Esquivel"), (_('Cheesecake ($5) Backers'), "Alan Hernandez"), (_('Cheesecake ($5) Backers'), "Lucas"), \
    (_('Cheesecake ($5) Backers'), "ftg200"), (_('Cheesecake ($5) Backers'), "earthwormjim3"), (_('Cheesecake ($5) Backers'), "anonlv000"), (_('Cheesecake ($5) Backers'), "Lewy"), \
    (_('Cheesecake ($5) Backers'), "Saiminoko"), (_('Cheesecake ($5) Backers'), "Username1127"), (_('Cheesecake ($5) Backers'), "vngood"), (_('Cheesecake ($5) Backers'), "Caliber Cross"), \
    (_('Cheesecake ($5) Backers'), "musterybattel 33"), (_('Cheesecake ($5) Backers'), "Parker Barr"), (_('Cheesecake ($5) Backers'), "Jax"), (_('Cheesecake ($5) Backers'), "J"), \
    (_('Cheesecake ($5) Backers'), "Alejandro Castro"), (_('Cheesecake ($5) Backers'), "CAnon"), (_('Cheesecake ($5) Backers'), "Nova"), (_('Cheesecake ($5) Backers'), "Reaviar"), \
    (_('Cheesecake ($5) Backers'), "Papal"), (_('Cheesecake ($5) Backers'), "gideon smith"), (_('Cheesecake ($5) Backers'), "Holo M. Baby"), (_('Cheesecake ($5) Backers'), "Holo M. Baby"), \
    (_('Cheesecake ($5) Backers'), "Nick Gohmann"), (_('Cheesecake ($5) Backers'), "Niinix"), (_('Cheesecake ($5) Backers'), "HoldTightMalcolm"), (_('Cheesecake ($5) Backers'), "Medbread"), \
    (_('Cheesecake ($5) Backers'), "J H"), (_('Cheesecake ($5) Backers'), "Azanark"), (_('Cheesecake ($5) Backers'), "Carrie Lee"), (_('Cheesecake ($5) Backers'), "Severn Aiches Seven"), \
    (_('Cheesecake ($5) Backers'), "DB"), (_('Cheesecake ($5) Backers'), "Kazz"), (_('Cheesecake ($5) Backers'), "Robert Kay"), (_('Cheesecake ($5) Backers'), "kaine deahwalker"), (_('Cheesecake ($5) Backers'), "Rerte"), \
    (_('Cheesecake ($5) Backers'), "Alexander Padua"), (_('Cheesecake ($5) Backers'), "Nothings There"), (_('Cheesecake ($5) Backers'), "Justin Defer"), (_('Cheesecake ($5) Backers'), "lee"), \
    (_('Cheesecake ($5) Backers'), "qk"), (_('Cheesecake ($5) Backers'), "ztya1998"), (_('Cheesecake ($5) Backers'), "Zakry"), (_('Cheesecake ($5) Backers'), "Ralgor"), \
    (_('Cheesecake ($5) Backers'), "Alex Gigea"), (_('Cheesecake ($5) Backers'), "ninjaguy1111"), (_('Cheesecake ($5) Backers'), "Engel Bert"), (_('Cheesecake ($5) Backers'), "Roberto Bravo"), \
    (_('Cheesecake ($5) Backers'), "Romanian"), (_('Cheesecake ($5) Backers'), "Jessie A George"), (_('Cheesecake ($5) Backers'), "Rahasia"), (_('Cheesecake ($5) Backers'), "Samurainik"), \
    (_('Shortcake ($3) Backers'), "Oroan"), (_('Shortcake ($3) Backers'), "Broom11"), (_('Shortcake ($3) Backers'), "Galblater"), (_('Shortcake ($3) Backers'), "Engenh0s0"), \
    (_('Shortcake ($3) Backers'), "Samyul"), (_('Shortcake ($3) Backers'), "Bill Purcell"), \
    (_('Shortcake ($3) Backers'), "pentgrax"), (_('Shortcake ($3) Backers'), "me body"), (_('Shortcake ($3) Backers'), "Austin Baker"), (_('Shortcake ($3) Backers'), "themanwithsauce"), \
    (_('Shortcake ($3) Backers'), "Colin Lyon"), (_('Shortcake ($3) Backers'), "Mario Herrmann"), (_('Shortcake ($3) Backers'), "Levi VM"), (_('Shortcake ($3) Backers'), "redluc14n"), \
    (_('Shortcake ($3) Backers'), "Dan"), (_('Shortcake ($3) Backers'), "wang17eee"), (_('Shortcake ($3) Backers'), "No Name"), (_('Shortcake ($3) Backers'), "Philip Rosenquist"), \
    (_('Shortcake ($3) Backers'), "Mike Johnson"), (_('Shortcake ($3) Backers'), "Thomas Hardman"), (_('Shortcake ($3) Backers'), "Raphael"), (_('Shortcake ($3) Backers'), "Kethrocyte"), \
    (_('Shortcake ($3) Backers'), "Joanna B"), (_('Shortcake ($3) Backers'), "J"), (_('Shortcake ($3) Backers'), "Vadimsyr1"), (_('Shortcake ($3) Backers'), "GTF"), \
    (_('Shortcake ($3) Backers'), "Sébastien Guély"), (_('Shortcake ($3) Backers'), "Nathan Storm Rice"), (_('Shortcake ($3) Backers'), "Gamer Of Zero"), (_('Shortcake ($3) Backers'), "John Wright"), \
    (_('Shortcake ($3) Backers'), "binaural-histolog"), (_('Shortcake ($3) Backers'), "Maxwell Swenson"), (_('Shortcake ($3) Backers'), "KnightRosery"), (_('Shortcake ($3) Backers'), "Quinn Pepper"), \
    (_('Shortcake ($3) Backers'), "Swampfox"), (_('Shortcake ($3) Backers'), "Drim"), (_('Shortcake ($3) Backers'), "Sean M Harper"), (_('Shortcake ($3) Backers'), "goopyb00py"), (_('Shortcake ($3) Backers'), "CMaestro"), \
    (_('Shortcake ($3) Backers'), "kumari moira"), (_('Shortcake ($3) Backers'), "MadRaff"), (_('Shortcake ($3) Backers'), "Chance Beranek"), (_('Shortcake ($3) Backers'), "Johan Ottevanger"), \
    (_('Shortcake ($3) Backers'), "Tomson Chiou"), (_('Shortcake ($3) Backers'), "SnivGrits"), (_('Shortcake ($3) Backers'), "Bobby Cardosa"), (_('Shortcake ($3) Backers'), "cody raugh"), \
    (_('Shortcake ($3) Backers'), "ambering"), (_('Shortcake ($3) Backers'), "HypnoMindz"), (_('Shortcake ($3) Backers'), "Ticoderoga"), (_('Shortcake ($3) Backers'), "Brion Forget"), \
    (_('Cupcake ($1) Backers'), "Jonathon Ford"), (_('Cupcake ($1) Backers'), "David"), (_('Cupcake ($1) Backers'), "Tom Kain"), (_('Cupcake ($1) Backers'), "Akidnas"), \
    (_('Cupcake ($1) Backers'), "Blake"), (_('Cupcake ($1) Backers'), "Pingo"), (_('Cupcake ($1) Backers'), "AntiMyx"), (_('Cupcake ($1) Backers'), "Arne Sahlberg"), \
    (_('Cupcake ($1) Backers'), "Abby Royal"), (_('Cupcake ($1) Backers'), "Lunasticks"), (_('Cupcake ($1) Backers'), "Astrid"), \
    (_('Cupcake ($1) Backers'), "ELOricalcos Dragon"), (_('Cupcake ($1) Backers'), "Dawson"), (_('Cupcake ($1) Backers'), "August Murdock"), (_('Cupcake ($1) Backers'), "POLaris"), \
    (_('Cupcake ($1) Backers'), "Miragian"), (_('Cupcake ($1) Backers'), "lucasw89"),(_('Cupcake ($1) Backers'), "David"), (_('Cupcake ($1) Backers'), "tertin"), \
    (_('Cupcake ($1) Backers'), "kalabash"), (_('Cupcake ($1) Backers'), "Keitherian David"), (_('Cupcake ($1) Backers'), "Yinzer"), \
    (_('Cupcake ($1) Backers'), "Spooky"), (_('Cupcake ($1) Backers'), "anonlv000"), (_('Cupcake ($1) Backers'), "xiamingyuan"), \
    (_('Cupcake ($1) Backers'), "Justice Brown"), (_('Cupcake ($1) Backers'), "Wesley Cox"), (_('Cupcake ($1) Backers'), "Andrew Postol"), (_('Cupcake ($1) Backers'), "Gimmick"), \
    (_('Cupcake ($1) Backers'), "Gigant Blood"), (_('Cupcake ($1) Backers'), "Bill Armitage"), (_('Cupcake ($1) Backers'), "Red"), (_('Cupcake ($1) Backers'), "Michael Cummings"), \
    (_('Cupcake ($1) Backers'), "DG"), (_('Cupcake ($1) Backers'), "Sherman"), (_('Cupcake ($1) Backers'), "Jacob Henson"), (_('Cupcake ($1) Backers'), "Marty McLatex lover"), (_('Cupcake ($1) Backers'), "Serevo"), \
    (_('Cupcake ($1) Backers'), "Raul Torres Vargas"), (_('Cupcake ($1) Backers'), "Hypnoringzzz"), (_('Cupcake ($1) Backers'), "FishFish332"), (_('Cupcake ($1) Backers'), "Daniel Jensen"), \
    (_('Cupcake ($1) Backers'), "Dylan Wilson"), (_('Cupcake ($1) Backers'), "Katbug"), (_('Cupcake ($1) Backers'), "wombatdno"), (_('Cupcake ($1) Backers'), "Shady Canopy"), (_('Cupcake ($1) Backers'), "Hellen Kraig"), \
    (_('Cupcake ($1) Backers'), "Rankori"), (_('Cupcake ($1) Backers'), "Steve Wilcoff"), (_('Cupcake ($1) Backers'), "Erick Lorenzen"), (_('Cupcake ($1) Backers'), "David Lencioni"),\
    (_('Cupcake ($1) Backers'), "David de Germà i Mercer"), (_('Cupcake ($1) Backers'), "Thomas Ward"), (_('Cupcake ($1) Backers'), "Elise Fellas"),\
    (_('Cupcake ($1) Backers'), "Stormfox4251"), (_('Cupcake ($1) Backers'), "Chroma"), (_('Cupcake ($1) Backers'), "Ryan Towers"), (_('Cupcake ($1) Backers'), "KoolFashion"), \
    (_('Cupcake ($1) Backers'), "BedBall"), (_('Cupcake ($1) Backers'), "Particle Man"), (_('Cupcake ($1) Backers'), "Cool Guy"), (_('Cupcake ($1) Backers'), "Lucas Sullivan"), \
    (_('Cupcake ($1) Backers'), "Vilhelm3"), (_('Cupcake ($1) Backers'), "KrisP"), (_('Cupcake ($1) Backers'), "Tsusaku Cohenat"), (_('Cupcake ($1) Backers'), "AnAlternateEnding"), \
    (_('Cupcake ($1) Backers'), "derp man"), (_('Cupcake ($1) Backers'), "Ryaigne"), (_('Cupcake ($1) Backers'), "Kevin Zuker"), (_('Cupcake ($1) Backers'), "Larax99"), (_('Cupcake ($1) Backers'), "Shawn Fitzwater"), \
    (_('Cupcake ($1) Backers'), "Lynette"), (_('Cupcake ($1) Backers'), "Crinisen"), (_('Cupcake ($1) Backers'), "D4rkdestiny"), (_('Cupcake ($1) Backers'), "ShinyLatex"), (_('Cupcake ($1) Backers'), "Thorbjørn Prochnow Sletten"), \
    (_('Cupcake ($1) Backers'), "qxvw198"), (_('Cupcake ($1) Backers'), "Floria Estere"), (_('Cupcake ($1) Backers'), "Kaaaaaa"), (_('Cupcake ($1) Backers'), "Benjamin Knight"), \
    (_('Cupcake ($1) Backers'), "John Scoundrel"), (_('Cupcake ($1) Backers'), "Durán Ahumada Angel Roberto"), (_('Cupcake ($1) Backers'), "Julian"), (_('Cupcake ($1) Backers'), "Dylan the bi guy"), \
    (_('Cupcake ($1) Backers'), "RedJayWiz Channel"), (_('Cupcake ($1) Backers'), "deep-sheep"), \
    (_('Special Thanks'), "Sammich"), (_('Special Thanks'), "Doa"), (_('Special Thanks'), "Cristian C")

    credits_s = ""
    c1 = ''
    c2 = 0
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=20}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=20}Made with " + renpy.version()
    # credits_s += "\n{size=20}Made with Ren'py (7.5.0.22062402)" #Don't forget to set this to the current Ren'py version

    def replacement_show(*args, **kwargs):
        if renpy.transition():
            renpy.transition(dissolve)
        return

    mp = MultiPersistent("Penlight")


init:
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5, color="#FFFFFF")
    image theend = Text(_("{size=80}The end"), text_align=0.5)
    image thanks = Text(_("{size=80}Thank you for playing!"), text_align=0.5)
    $persistent.NewSprite = " New"

label splashscreen:
    if persistent.played_before is None:
        show text "Select your language" at center:
            ypos 0.1
        show second_text at center:
            ypos 0.85
        show third_text at center: #find definitions for these texts in declarations.rpy
            ypos 0.9
        menu:
            "English":
                $renpy.change_language(None)
            "Español":
                $renpy.change_language("spanish")
        $persistent.played_before = True
        hide text
        hide second_text
        hide third_text
        with longdissolve
        pause 1.0
    else:
        pass
    show text _("Penlight is a work of fiction.\n Some of the situations presented would be highly immoral to attempt in reality. \nWhile the characters in this work are fictitious and exploration is encouraged, \nplease do not attempt to recreate what you see in real life.") at truecenter with longdissolve
    pause 10.0
    hide text with longdissolve
    pause 1.0
    return

label start:
    jump Day1_Kyou
