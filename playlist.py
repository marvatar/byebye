import streamlit as st
from PIL import Image


def main():
    st.title("So!")
    st.markdown(""" 
                Jetzt, wo wir unter uns sind, möchte ich mich noch einmal ein bisschen länger und wehmütiger verabschieden.
                Gleich vorweg: Wer auf sentimentales Gewäsch keine Lust hat, kann jetzt einfach die Seite wieder schließen. No worries!

                Die 19 Jahre bei Infratest, TNS und Kantar machen unschwer einen großen Teil meines Lebens aus.
                Große und wichtige Ereignisse sind irgendwann in dieser Zeit passiert, sowohl privat als auch beruflich.
                Die Welt hat sich ganz schön geändert, technologisch und auch sonst...
                
                Zum Abschied möchte ich noch einmal ein paar Gedanken mit Euch teilen, etwas wild und unkontrolliert vielleicht - aber das seid Ihr von mir so gewohnt.
                Damit es einigermaßen organisiert bleibt, hatte ich die Idee, eine kleine Playlist zusammenzustellen und dazu ein wenig zu sinnieren.
                Wer also Lust hat, startet die Playlist über den Link, klickt dann die passenden Felder unten an und liest sich die Texte durch.
                Vielleicht entlockt es noch einmal einen Schmunzler oder triggert eine schöne Erinnerung... würde mich freuen.
                """)

    st.markdown("https://open.spotify.com/playlist/5THCLsUU3qjKFxrLDF0mNe?si=443650e5306f446a")

    st.divider()
    st.markdown("<h1 style='text-align: center;'>Songs from the last 19 years</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>🎶🎶🎶🎶🎶😪🎶</h1>" , unsafe_allow_html=True)


    st.divider()

    track01 = Image.open('./assets/marvatar__I_Walk_the_line_b755c8dd-ac60-4c56-b0c4-2bd7978d1dd9.png')
    track02 = Image.open('./assets/schönheit_der_chance.jpeg')
    track03 = Image.open('./assets/b62.jpg')
    track04 = Image.open('./assets/marvatar__Fahrrad_fahren_8a602e0a-4a4a-4715-ae00-7178a19c0510.webp')
    track05 = Image.open('./assets/marvatar__Life_in_Mars_8aa6b3f2-d18e-4825-bb25-28d0349e9853.webp')
    track06 = Image.open('./assets/marvatar__den_sjalvslagne_ec6f353e-55c0-4be8-83a5-bc7a8eaa4f1b.webp')
    track07 = Image.open('./assets/unoptimiert.jpeg')
    track08 = Image.open('./assets/marvatar__pure_Vernunft_darf_niemals_siegen_0ed29476-99f3-4123-b39e-0cbf5b3fba32.webp')
    track09 = Image.open('./assets/marvatar__wenn_es_dunkel_und_kalt_wird_in_berlin_d7670f65-f981-427e-b321-8ce0a7a7ae88.png')
    track10 = Image.open('./assets/lache_welt.jpeg')
    track11 = Image.open('./assets/marvatar__apply_some_pressure_b13a686d-2ae3-4b4b-bb23-17aa69b1db2f.png')
    track12 = Image.open('./assets/komm_rueber.jpeg')
    track13 = Image.open('./assets/irgendein_tag.jpeg')
    track14 = Image.open('./assets/nixwirdbesser.jpeg')
    track15 = Image.open('./assets/feierabend.jpeg')
    track16 = Image.open('./assets/marvatar__These_days_71a15a60-21a7-4815-aed6-24c700f9df23.png')
    track17 = Image.open('./assets/marco.jpeg')
    track18 = Image.open('./assets/longandwindingroad.jpeg')
    track19 = Image.open('./assets/abenteuer.jpeg')

#############################

    with st.container():
        ycol1, ycol2 = st.columns(2)

## Track 1
        with ycol1:
            with st.expander(label="(1) Johnny Cash: I walk the line"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track01, width=200)
                with xcol2:
                    st.markdown("""
                        Die Anfangstakte dieses Lied markieren die ersten Jahre bei Infratest. 
                        Quasi täglich waren sie aus dem Nachbarbüro zu hören und läuteten, unabhängig von der Uhrzeit, "den gemütlichen Teil" des Tages ein.
                        
                        Es sind manchmal die kleinen Dinge, die einem die nötige Struktur geben, um in ein geregeltes Arbeitsleben zu finden. 
                        Feste Rituale wie das Treffen in der Mittagsrunde, gemeinsames Tischgrillen im Büro, Käsefondue in der Mittagspause oder auch der Spaziergang zum Döner holen.
                        Für mich war das ein idealer Einstieg ins Berufsleben. 
                        
                        Der Kollege von damals hat schon recht mit seiner Einschätzung: 
                        "Das muss man pflegen. Sowas ist schneller abgeschafft, als wieder eingeführt." 
                        """)

## Track 2
        with ycol2:
            with st.expander(label="(2) Tomte: Die Schönheit der Chance"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track02, width=200)
                with xcol2:
                    st.markdown("""
                        Ich hab länger ein Lied gesucht, dass ein wenig auf die Arbeit in der Statistik passt.
                        Ich hab mich für dieses Lied nicht nur entschieden, weil es einigermaßen nerdig im Titel auf unsere Stichprobenzieherei abzielt, 
                        sondern weil es mich auch an die Zeit damals erinnert, als ich kollegialen Hinweisen folgend relativ intensiv versucht habe, meinen musikalischen Horizont zu erweitern.
                            
                        Dass ich mal in einer Statistik-Abteilung lande, würde so manchen meiner Mathe-Lehrer*innen im Nachhinein wahrscheinlich noch in den Wahnsinn treiben.
                        Mehr sag ich vielleicht dazu nicht... Vielleicht doch kein Zufall, dass ich relativ schnell programmiertechnisch aufgerüstet habe,
                        um den Rechner das machen zu lassen, was ich selbst nicht konnte...

                        Die Arbeit auf der Konsole war im Kleinen, wie das Arbeiten im Infratest-Gebäude damals im Großen: nicht eben hübsch anzusehen, aber es hat wahnsinnig effektiv funktioniert.
                        Noch heute schrecke ich aus dem Schlaf manchmal auf und rufe: "ZUF!", "CID!", "CATICHECK!!!" Gelernt ist gelernt.
                        """)

#############################

    with st.container():
        ycol1, ycol2 = st.columns(2)

## Track 3
        with ycol1:
            with st.expander(label="(3) Gisbert Zu Knyphausen: Das Licht dieser Welt"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track03, width=200)
                with xcol2:
                    st.markdown("""
                        Beide meine Mädels sind während der Zeit mit Euch auf die Welt gekommen und inzwischen 
                        ziemlich groß geworden. Deshalb habe ich dieses Lied auf die Liste gesetzt, weil es so schön beschreibt, was man
                        sich als Vater so für die Kinder wünscht.
                      
                        Dass ich so einfach und unproblematisch in Teilzeit arbeiten konnte und so viel Zeit
                        mit meinen Kindern verbringen durfte, dafür bin ich unendlich dankbar und gebe diesen Dank unmittelbar an die Entscheider, 
                        Beteiligten und Betroffenen weiter.    
                        """)

# ## Track 4
        with ycol2:
            with st.expander(label="(4) Max Raabe: Fahrrad fahrn"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track04, width=200)
                with xcol2:
                    st.markdown("""
                        Ein krasser Vorteil war immer auch der extrem kurze Arbeitsweg, den ich sehr gerne mit dem Fahrrad am Schlosspark entlang zurückgelegt habe.
                        Im Sommer war es wie ein Mini-Urlaub, im Herbst durch den Morgennebel wie in einem verwunschenen Paradies, im Winter war ich oft steifgefroren, 
                        im Regen bis auf die Haut nass und dann strumpfsockend im Büro. Wir Radler sind schon verwegene Typen...
                        
                        Auf jeden Fall immer eine gute Gelegenheit noch einmal durchzuschnaufen, bevor es tagsüber rundgeht. Und um sich "freizustrampeln", 
                        nach einem stressigen Tag... 
                        """)

#############################

    with st.container():
        ycol1, ycol2 = st.columns(2)

## Track 5
        with ycol1:
            with st.expander(label="(5) Seu Jorge: Life on Mars"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track05, width=200)
                with xcol2:
                    st.markdown("""
                        Ach ja, mit dem Lied verbindet sich auch so viel: Wes Anderson-Filme, Weltraum-Themen...
                        Da kann ich mich ja stundenlang verlieren - natürlich nur außerhalb der Arbeitszeit.
                        
                        Aber auch während der Arbeitszeit gab es immer was zu entdecken und das ist auch im Rückblick grandios: 
                        Ich hatte immer, wirklich immer, die Freiheit rechts und links zu blicken und Dinge auszuprobieren.
                        Und manchmal ist sogar was dabei rausgekommen. Manchmal aber auch nur, von den abstrusen Neu-Entdeckungen mit Begeisterung in aller Ausführlichkeit zu erzählen.
                        Keine Ahnung, ob ich es irgendwann nochmal schaffe, schneller auf den Punkt zu kommen. 
                        
                        Diese Seite hier ist nicht gerade ein gutes Omen dafür...
                        """)

## Track 6
        with ycol2:
            with st.expander(label="(6) Mando Diao: Den Självslagne"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track06, width=200)
                with xcol2:
                    st.markdown("""
                        Auf so einer Liste darf natürlich ein Lied von meiner meistgehörten Platte in den letzten 19 Jahren nicht fehlen.
                        Überraschend unerreicht in meiner Playlist: Mando Diao "Infruset".
                        Während der Arbeit Musik zu finden, die man gut anhören kann, ohne immer laut mitsingen zu müssen und deswegen aus dem Arbeitstrott zu geraten, ist für mich sehr schwierig.
                        Noch sehr viel schwieriger ist es allerdings alt-schwedische Lyrik mitzusingen. 
                        Passt also perfekt als Begleitmusik und war und ist es immer wieder, immer wieder.
                        (Dummerweise hab ich es jetzt so oft gehört, dass ich mittlerweile doch mitsinge...)

                        Mindestens genauso schön: Alle Dota-Lieder mit den Texten von Mascha Kaléko. Wunderbar! Ausprobieren!
                        """)

#############################

    with st.container():
        ycol1, ycol2 = st.columns(2)

## Track 7
        with ycol1:
            with st.expander(label="(7) Bernd Begemann: Unoptimiert"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track07, width=200)
                with xcol2:
                    st.markdown("""
                        Optimierung und Automatisierung sind natürlich die Super-Schlagworte der modernen Arbeitswelt und treiben mich ja auch immer um.
                        
                        Was ich lernen durfte, ist, dass man immer "ganzheitlich" an die Sache rangehen sollte. Es geht darum, den wirklichen, den realen Bedarf
                        zu entdecken. Ein super optimierter Prozess, den keiner anwendet bringt nichts. Eine minimale Veränderung, die einem im Alltag
                        ein paar Sekunden nervige Klickerei spart, ist Gold wert.
                        
                        Und was jetzt langsam bewiesen ist - die ständige Einführung neuer, noch besserer Tools mit steilen Lernkurven bringt nicht immer den gewünschten 
                        Produktivitätsschub. Da gibt es leider keine Automatismen...
                        
                        **Wichtig**: Macht es mit Python! :smile:
                        """)

## Track 8
        with ycol2:
            with st.expander(label="(8) Tocotronic: Pure Vernunft darf niemals siegen"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track08, width=200)
                with xcol2:
                    st.markdown("""
                        Hier noch ein typisches Arbeitsproblem aus meiner Zeit in der Medienforschung. Nicht, was man denken könnte bei dem Titel...
                        Netzwerken ist nicht so meine Stärke, ich war aber doch immer wieder mal "am Kunden". Im Smalltalk stellte sich heraus, dass 
                        die Person "Tocotronic" schätzt. Ja, sehr gut, hab ich mir gedacht. Da hab ich auch schon davon gehört. Da "relaten" wir jetzt mal.
                        "Ja," hab ich gesagt, "die find ich auch total super! Absolute Lieblingsband!" Tja...
                        
                        Leider hat sich mein angelesenes, halbes Dreiviertel-Wissen nicht ansatzweise als tragfähig für die sich einseitig erhoffte 
                        Buddy-Konversation erwiesen und ich stand innerhalb von Sekunden als anbiedernder Schleimer da, der nicht einmal ein Lied oder eine Platte der Band
                        benennen konnte. Tja, again what learned - authentisch bleiben... 
                        (Hab das mit Tocotronic natürlich nachbereitet.)
                        """)

#############################

    with st.container():
        ycol1, ycol2 = st.columns(2)

## Track 9
        with ycol1:
            with st.expander(label="(9) Element of Crime: Wenn es dunkel und kalt wird in Berlin"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track09, width=200)
                with xcol2:
                    st.markdown("""
                        Berlin im Dezember und Januar war zusammen mit Parchim und Güstrow das wichtigste und häufigste Reiseziel: Zur Kundenveranstaltung oder zur Schulung ins Telefonstudio.
                        Aber eigentlich immer im Winter, im Dunkeln und oft ziemlich allein - und zum Teil sehr hungrig (<- niemals in Güstrow!!!!).
                    
                        Zwei wichtige Erkenntnisse: 
                        * Die Häppchen im Soho House ersetzen kein Abendessen. 
                        * Und die Butterbrezeln (!) im Berliner CATI-Studio bekamen die Butter injiziert: Die Brezn vom Bahnhof Zoo?
                        
                        Viel, viel schöner war es, im Team herumzureisen. Ich funktioniere wohl am besten, wenn ich starke Kolleginnen an meiner Seite habe.
                        Da war ich dann auf der Heimfahrt heiser vom Ratschen und nicht vom Einweisen... 
                        """)

## Track 10
        with ycol2:
            with st.expander(label="(10) Jacques Palminger, 440hz Trio: Lache und die Welt ist mir Dir"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track10, width=200)
                with xcol2:
                    st.markdown("""
                        Lustig war's oft, als die KoFo-Truppe noch beisammen war. 
                        
                        Wir durften über Minuten hinweg lernen, 
                        dass wohl gerade besonders kurze Namen am Telefon nicht verstanden werden.
                        So mancher Spruch hat es zum Klassiker gebracht, aber eines war klar: immer einen Schritt vor den anderen...
                        
                        Das Soziale, der Zusammenhalt ist so wichtig: Mal Ratschen, mal Dampf ablassen, selbst sich übereinander lauthals ärgern, weil es so laut ist...
                        Geteiltes Leid ist halbes Leid. Geteilte Freude ist doppelt so viel wert. Ohne Team ist alles nichts.
                        
                        Wichtig für mich aber auch und eindrucksvoll in diesem Lied demonstriert: Da waren dann auch schon oft recht blöde Sprüche von mir dabei, 
                        die mir im Rückblick das kalte Grausen über den Rücken jagen. Hoffentlich lern ich mindestens da noch dazu.
                        """)

#############################

    with st.container():
        ycol1, ycol2 = st.columns(2)

## Track 11
        with ycol1:
            with st.expander(label="(11) Maximo Park: Apply Some Pressure"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track11, width=200)
                with xcol2:
                    st.markdown("""
                        Nach all dem Lachen etwas ernster: Es ist frappierend, wie sich die Situation einer Firma in der 
                        stetigen Transition verändert und was das für Konsequenzen auf allen Ebenen hat. Wie so oft führen manche Entscheidungen (oder nicht getroffene)
                        kaskadenartig zu Zwangsläufigkeiten, die über kurz oder lang das Gesamtgemenge komplett auf den Kopf stellen. 
                        
                        Ich habe für mich gelernt, wie wichtig für mich Klarheit, authentisches Auftreten und Zugewandtheit sind -  
                        und zum Glück im persönlichen Umgang auch immer wieder erleben durfte. 
                        
                        Die Resilienz bei Kantar ist, glaub ich, unerreicht. Da wird mir auch für die Zukunft nicht allzu bang.
                        """)

## Track 12
        with ycol2:
            with st.expander(label="(12) Von Wegen Lisbeth: Komm mal rüber bitte"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track12, width=200)
                with xcol2:
                    st.markdown("""
                        Wichtiges Lied! Entscheidend sind hier die paar wenigen Takte ab Minute 2:22:
                        ***"Excel, Excel! Yeah! Tabelle!"***
                    
                        Dazu nur kurz die wichtigsten Regeln, die auch noch lange nach meinem Abschied gelten:
                        * Excel ist ein Ar***loch! (manchmal)
                        * Excel ist keine Datenbank! (niemals)
                        * Ein Excel-Sheet für dutzende oder gar hunderte Mitarbeiterinnen zur Bearbeitung freizugeben ist eine fragwürdige Entscheidung! (immer)

                        **UND**: Macht es mit Python! 
                        """)

#############################

    with st.container():
        ycol1, ycol2 = st.columns(2)

## Track 13
        with ycol1:
            with st.expander(label="(13) Kapelle Petra: An irgendeinem Tag wird die Welt untergehen"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track13, width=200)
                with xcol2:
                    st.markdown("""
                        Das Trostlied während Corona. Aber irgendwie immer noch schön und immer noch tröstend. Und leider passend für so viele aktuelle Gelegenheiten.
                        Aber eigentlich stimmt's doch auch: Es wird schon, wenn wir uns zusammenreißen und zusammenhalten. Das hat das Arbeiten hier immer wieder ausgemacht. 
                        
                        Corona hat uns ziemlich zerstreut und vereinzelt und so ganz haben wir noch nicht wieder zusammengefunden. Ich wünsche mir für Euch,
                        dass das bald wieder besser gelingt und Ihr, egal was noch so kommt, weiter so zusammenhaltet.                        
                        """)


## Track 14
        with ycol2:
            with st.expander(label="(14) Worried Man & Worried Boy: Von gschissn auf oasch"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track14, width=200)
                with xcol2:
                    st.markdown("""
                        Hoj? Wie kommt denn dieses Lied an dieser Stelle auf die Liste? Ich hab keine Ahnung... :sunglasses:
                        Aber manchmal muss man auch schimpfen und Dampf ablassen - klar! Und dann wird wieder weiterghackelt...
                        """)

#############################

    with st.container():
        ycol1, ycol2 = st.columns(2)

## Track 15
        with ycol1:
            with st.expander(label="(15) Grossstadtgeflüster: Feierabend"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track15, width=200)
                with xcol2:
                    st.markdown("""
                        Dieses Lied hat natürlich auch wieder mehrere Ebenen...
                        
                        Zum Ende meiner Zeit durfte ich bei Dx nochmal so richtig qualitativ denken. 
                        Erstes Thema: "Feierabend" für Menschen aus aller Welt erklären.
                        Im Endeffekt hat das wohl ganz gut funktioniert und auch durch die anderen Analysen wurde ich vorbildlich durchgesteuert, aber eins bleibt:
                        
                        der Wunsch "Schönen Feierabend" wird nie mehr die gleiche, unschuldige Bedeutung haben :laughing:
                        """)

## Track 16
    with ycol2:
        with st.expander(label="(16) Nico: These days"):
            xcol1, xcol2 = st.columns([1,3])
            with xcol1:
                st.image(track16, width=200)
            with xcol2:
                st.markdown("""
                        Oje, jetzt wird es zum Schluss doch noch einmal sehr wehmütig.
                        Aber eigentlich geht es mir hier um meinen wichtigsten Vorsatz für die Zukunft:
                        Ich möchte dann doch lieber nicht die Person werden, die "vom Krieg erzählt", zu allem eine Anekdote aus besseren Tagen weiß und 
                        im Zweifel "nix wird besser!" ruft. Zumindest nicht zu oft.
                          
                        Das wird mir, glaub ich, wenn ich das hier so sehe, sehr schwer fallen... Die armen, neuen Kolleg*innen...
                        """)

#############################

    with st.container():
        ycol1, ycol2 = st.columns(2)

## Track 17
        with ycol1:
            with st.expander(label="(17) Gitti und Erika: Ciao, Marco, ciao"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track17, width=200)
                with xcol2:
                    st.markdown("""
                        Da muss man natürlich sofort gegensteuern. Hat eigentlich nix mit Kantar zu tun, aber naja... 
                        Hier mal kurz eine Kinderserie, die mich weniger inhaltlich beeindruckt hat, aber ziemlich verwirrt,
                        weil der kleine Marco nicht nur seeehr ähnlich heißt, sondern quasi eine Manga-Version von mir als Kind im Fernsehen war.
                        WTF??? würden wir heute sagen... Frappierend!!! :laughing:
                        
                        Und natürlich passt es inhaltlich super gut hier ans Ende der Liste.
                        (... äh, und, nein, ich hatte leider keinen Affen... das war dann wohl künstlerische Freiheit der Japaner)                                
                        """)

## Track 18
        with ycol2:
            with st.expander(label="(18) The Beatles: The Long and Winding Road"):
                xcol1, xcol2 = st.columns([1,3])
                with xcol1:
                    st.image(track18, width=200)
                with xcol2:
                    st.markdown("""
                        Tja, und das war's dann wohl. Als Kind hatte ich neben kurzen Lederhosen, mit denen ich im Winter 30km durch hüfthohen Schnee zur Schule
                        gelaufen bin, nicht viel. Aber irgendwann das rote und das blaue Best-of der Beatles auf Kassette.
                        Wie das damals so war, habe ich das sehr, sehr, sehr oft gehört. Und immer von vorn bis hinten durch, weil das quasi ja nur so ging.
                        "The Long and Winding Road" war (bis vor kurzem) immer das letzte Stück und es gibt mir immer noch das Gefühl, dass sich ein Kreis schließt und dass es gut ist.
                        
                        Ob Stichproben ziehen, Stichproben gewichten, Projekte managen und Daten verwurschteln, SINs der Radiosender auswendig lernen, Fernseher suchen, Datenschutzfolgeabschätzungen entwerfen 
                        und schließlich Storytelling - mann-oh-mann, da hab ich viel gelernt und lernen müssen. 
                        
                        Aber ich hatte zum Glück immer Euch Kolleg*innen, die mir das ganz geduldig erklärt haben und ohne zu Zögern geholfen haben, wenns bei mir nicht mehr weiterging: 
                        
                        **Von ganzem Herzen vielen Dank dafür!**
                    """)

#############################


## Track 19
    with st.container():
        with st.expander(label="(19) Vicky Leandros: Ich liebe das Leben"):
            xcol1, xcol2 = st.columns([1,3])
            with xcol1:
                st.image(track19, width=200)
            with xcol2:
                st.markdown("""
                Ja, ja, ja, ist ja gut... einen hab ich noch. Muss ja auch die 19 voll machen...
                
                Ist ja wohl klar, dass man nun wirklich keine Beziehung ohne dieses Lied beenden darf - auch keine Arbeitsbeziehung. 
                            
                Grundgesetz. Basta! :laughing:
                """)


    st.divider()

    st.markdown("""
                *Jetzt reicht's aber wirklich...*
                Ist aber ja mal wieder eine krude Mischung geworden. :smile:

                ### Macht's gut, passt auf Euch auf und bleibt gesund! 
                ### Euer Markus

                P.S.: Diese Seite wurde natürlich zu 100% mit Python erstellt :smile: :smile: :smile: 
                Die Bilder sind bis auf die zwei Ausnahmen von einer KI generiert. Ich komme einfach nicht aus meiner Haut...
                """)

if __name__ == "__main__":
    st.set_page_config(
    page_title="Bye Bye Playlist",
    page_icon="👋",
    layout="wide",

    )
    main()
