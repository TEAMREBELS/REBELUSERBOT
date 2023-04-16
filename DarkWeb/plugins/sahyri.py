import asyncio
import os
import sys
import random
from telethon import events
from DarkWeb import ALIVE_NAME, CMD_HELP
from Dark.utils import admin_cmd, edit_or_reply
from telethon import events
from DarkWeb.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK WEB"

@dark.on(admin_cmd(pattern=r"psad$", outgoing=True))
async def _(event):
    if event.fwd_from: 
        return
    h=(random.randrange(1,22))
    if h==1:
        await event.edit(f"Kithe miladi hai uhana akhan 👀 nu ninda,\njihana nu bevaphavam ne ruvaia 😭 hove..\n\n\n✍️{DEFAULTUSER}") 
    if h==2:
        await event.edit(f"Muhabata de anadaja vakhare-vakhare hude ne..\nKise ne ṭuṭa ke cahia te koi caha ke ṭuṭa gia..!!.\n\n\n✍️{DEFAULTUSER}")
    if h==3:
        await event.edit(f"Teri 👉narajagi 😔ika pala di vi dila❤️ sahida nai\nlaphaja ca nai dasa sakade kina tainu piara❤️ karade an\n\n\n✍️{DEFAULTUSER}")
    if h==4:
        await event.edit(f"Mohabbat dila vica kujha isa tarha di hoṇo cahidi hai,\nKi uha hasila bhavem kise duje nu hove..\nPara kami usanu zidagi bhara meri hoṇi cahidi hai..!\n\n\n✍️{DEFAULTUSER}") 
    if h==5:
        await event.edit(f"Tre kanan de vica gala kara pyra diam kara pyara dia,\nChaḍa sagana ni aja gala mana lai yara dia mana lai yara dia..😘😍\n\n\n✍️{DEFAULTUSER}") 
    if h==6:
        await event.edit(f"Aja kala di Love Story da ihi asul ai,\ntusi jisanu yada karake ro rahe ho uha kise hora nu Khush rakhaṇa ca Busy ai..\n\n\n✍️{DEFAULTUSER}") 
    if h==7:
        await event.edit(f"Phark ta bas soch da hai,\nnahi ta dosati vi pyar to ghaṭa nahin hund...\n\n\n✍️{DEFAULTUSER}") 
    if h==8:
        await event.edit(f"Jado tainu pahili vara vekhia ruhh ne avaza diti chala koi gunaha kar,\ntainu pata Mai muhabata kara lai..\n\n\n✍️{DEFAULTUSER}") 
    if h==9:
        await event.edit(f"Yaar badal ke vekho, tuhaade nawe yaara ch v ohna diyaa rooha jhalkdiyaa haungiyaa\npurane yaar bhulne v nahi te ohna di yaad v nahi auni\n\n\n✍️{DEFAULTUSER}") 
    if h==10:
        await event.edit(f"Tere pyaar waang saadhe iraade v kache nikale\nnaa chhadeyaa gya, ni dilo kadheyaa gyaa\n\n\n✍️{DEFAULTUSER}")  
    if h==11:
        await event.edit(f"Pyar v bahut azeeb aa\njis insaan nu paayea v na howe\nus nu v khohan da darr lageyaa rehnda\n\n\n✍️{DEFAULTUSER}") 
    if h==12:
        await event.edit(f"Tera door Jana seh na howe😒\nIshq enna naal tere ve🙈\nSathon hun reh na howe❤️..!!\n\n\n✍️{DEFAULTUSER}") 
    if h==13:
        await event.edit(f"Saah lain naam tera sajjna🙈\nBina pal vi kithe sarda😕..!!\nRabb vang tenu poojan akhiyan😇\nTe dil ibadat karda😍..!!\n\n\n✍️{DEFAULTUSER}") 
    if h==14:
        await event.edit(f"Tenu ki dassiye hun sajjna ve\nGhutt sabran vala kinjh pita e😣..!!\nAsa ikalleyan beh beh raatan nu\nTera naam har saah naal lita e❤️..!\nTenu khabran na khaure dil chandre diyan\nIshq tere de dhageyan naal sita e🙈..!!\nIkk jaan diwani hoyi teri e\nduja dil tere naawe kita e😍..!!\n\n\n✍️{DEFAULTUSER}") 
    if h==15:
        await event.edit(f"Ki kehne haal dilan de ve\nKoi puche na koi dasse na🙌..!!\nSathon rabb vi mukh fereya\nTe jagg ton pal vi russe na💔..!!\nAsi sab nu muskaunde firde haan\nTe sanu dekh koi hasse na☹️..!!\nSade hassde mukh dekh sawal karan\nTe udaas hoyia nu koi puche na😟..!!\n\n\n✍️{DEFAULTUSER}") 
    if h==16:
        await event.edit(f"Oh gaira de sang khul gaye hone aa\nnaweyaa de naal ghul gaye hone aa\ntu jinaa da khyaal dil cho ni kadhda\nArwinder O kadon de tainu bhulge hone a\n\n\n✍️{DEFAULTUSER}") 
    if h==17:
        await event.edit(f"Zaroori nahi ke jajhbaat kalam naal hi likhe jaan\nkhali panne v bahut byaan kar jande ne\n\n\n✍️{DEFAULTUSER}") 
    if h==18:
        await event.edit(f"Zindagi aini dukhi nahi aa ke marn nu jee kare\npar kujh lok dukh hi eaina dinde ne ke jeon da dil nahi karda\n\n\n✍️{DEFAULTUSER}") 
    if h==19:
        await event.edit(f"Saadhe ute aapna hak jataun wala koi nahi\ntu ruse taa tainu mna la ge\npar asi rusiye kive sanu manaun wal koi nahi\n\n\n✍️{DEFAULTUSER}") 
    if h==20:
        await event.edit(f"Bhull gaya jiona loka layi\nHun aapde khayal vas lainda e..!!\nShad k mehfilan duniya diyan\nIkalleyan ja kite behnda e..!!\nKhaure vigad gaya ja sudhar gaya\nPar nakhre na hun kise de sehnda e..!!\nHun nhi krda dil kise naal mohobbat nu\nBs time pass de zariye labbda rehnda e..!!✍️{DEFAULTUSER}")
    if h==21:
        await event.edit(f"Bekadri kar rukhe ho tur Jana\nEda nahio chahan hundiya..!!\nBefikre ho nhi saunde sajjna\nJinna nu parwahan hundiya..!!\n\n\n✍️{DEFAULTUSER}") 
    if h==22:
        await event.edit(f"Ajh v ohi chehra e\npar tera dil na mera e\npata ni kadon tak rehna\nmere dil vich naam jo tera e\n\n\n✍️{DEFAULTUSER}")  
    if h==22:
        await event.edit(f"Change hon ja maade sanu fark nhi painda\nO asi taan izzat rakhde aan dil ch\nSanu chahun valeyan layi vi te bhulaun valeyan layi vi..!!\nJee sadke aawe jihne auna\nTe jaan vala ja sakde\nKyunki aawdi zindagi de boohe khulle rakhne ne asi\nAun valeyan layi vi te jaan valeyan layi vi🙏😎..!!\n\n\n✍️{DEFAULTUSER}")
    if h==22:
        await event.edit(f"Sabh da dilo hi karida ae,\nkoi varte ja parkhe oh gal wakhri\n\n\n✍️{DEFAULTUSER}")

@dark.on(admin_cmd(pattern=r"sdirty$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    s=(random.randrange(1,19)) 

    if s==1:
        await event.edit("हमारी एक मुस्कुराहट पर वो हमसे सेक्स कर बैठे...😁 \nवाह वाह...😅\nहमारी एक मुस्कुराहट पर वो हमसे सेक्स कर बैठे,\nवो घर जाने वाली थी कि हम फिर से मुस्कुरा बैठे..!!.😂😂😂")
    if s==2:
        await event.edit("तुम आरजू तो करो मोहब्बत की, हम इतने भी गरीब नहीं कि...\nतुम आरजू तो करो मोहब्बत की, हम इतने भी गरीब नहीं कि…\nकमरे का जुगाड़ भी ना कर सकें!")
    if s==3:
        await event.edit("Ishq k sahare jiya nahi karte,\nGum k pyalo ko piya nahi karte,\nkuch Dost bhos#i k aise bhi hote hai...\nJinke jab tak ungli na karo,yaad bhi nahi karte hai..😅😅😅😅..")
    if s==4:
        await event.edit("रात होगी तो कंडोम भी दुहाई देगा,\nटांगो के बीच सारा जहां दिखाई देगा,\nये काम है जानी, जरा संभलकर करना,\nएक कतरा भी गिरा तो 9 महीने बाद सुनाई देगा...")
    if s==5:
        await event.edit("ये काली-काली आँखें, ये गोरे-गोरे गाल,\nये काली-काली आँखें, ये गोरे-गोरे गाल,\nऔर बताओ कैसे हो?  lu*d के बाल.")
    if s==6:
        await event.edit("अर्ज़ किया है...\nरजवाड़े में उड़ रहे हैं घोड़े,\nरजवाड़े में उड़ रहे हैं घोड़े,\nध्यान से क्या पढ़ रहा है बे  lode\n,कभी देखा है क्या उड़ते हुए घोड़े.")
    if s==7:
        await event.edit("Kuchh to thaa unke labon par jo wo hume dekhkar itna badbadati thi,Fir pata chala ek din ki wo to gutkha chabaati thi")
    if s==8:
        await event.edit("Tangon Ko Utha, Kuchh Ch**T Dikha,\nMere L*Nd Par Zara Haath Fira\nYeh Ch**T Khushi Mein Hansti Hai,\nL*Nd Bhi Hilta Hai Masti Mein,")
    if s==9:
        await event.edit("Heela Heela Ke Chalti Ho\nKya Mardalogi…\nHeela Heela Ke Chalti Ho\nKya Mardalogi…\n\nHamko Nahi Dogi Tho Kya Aachar Daalogi…..")
    if s==10:
        await event.edit("Unki Aankhon Mein Ansu Aur Chehre Par Hasi Hai;\nWah Wah! Wah Wah!\nUnki Aankhon Mein Ansu Aur Chehre Par Hasi Hai;\nAisa Lagta Hai Ki Unki Lulli Zip Mein Fasi Hai!")
    if s==11:
        await event.edit("Sex Karo Daily,\nAgar Woh Mil Jaye Akeli.\nAgar Na Mile Akeli\nToh Pakad Lo Uski Saheli,\nAgar Na Mile Saheli\nToh Jindabaad Hatheli.\nBut Do Sex Daily!!!!!.")
    if s==12:
        await event.edit("Roye Hum Iss Kadar Unke Sine Se Lipat Kar;\nWah Wah!\nRoye Hum Iss Kadar Unke Sine Se Lipat Kar;\nKi Woh Khud Apni Kameez Utarkar Boli;\nDaba Le Kamine, Faltu Mein Natak Mat Kar!")
    if s==13:
        await event.edit("Pyar Kismat Hai Koi Khwab Nahi\nYe Wo Khel Hai Jisme Sab Kamiyab Nahi\nJinhe Ishq Ki Panah Mili Wo Kch Log H\nOr\n\nJinki Maa Ch*d Gayi Unka Hisab Nahi")
    if s==14:
        await event.edit("Pati Biwi Ka Boob Daba Kar Bola-\nAagr Ye Khde Hote To Bra Ki Jarurt Nahi Hoti\nBiwi Pati Ka Popt Pakdh Ke Boli:\nYe Thoda Aur Mota Hota To Padhosi Ki Jarurt Nahi Hoti.")
    if s==15:
        await event.edit("Unki Gali Se Guzre, To Chaubara Nazar Aaya;\nUnki Gali Se Guzre, To Chaubara Nazar Aaya;\nUski Maa Bahar Aa Kar Boli:\nGaand Faad Dungi Bhosdi Ke, Jo Dobara Nazar Aaya!")
    if s==16:
        await event.edit("कुछ तो बाकी है तेरे मेरे दरमियाँ ऐ जानेमन;\nयूँ ही नही तेरी याद में मेरा लंड खड़ा हो जाता।")
    if s==17:
        await event.edit("क्या कशिश थी उस की आँखों में मत पूछो;\nमुझ से मेरा दिल लड़ पड़ा मुझे यही चूत चाहिए।")
    if s==18:
        await event.edit("चाँद देखकर सितारे बने;\n आसमान देखकर बादल बने;\n नदी देखकर किनारे बने;\n आपके कारनामे देखकर कंडोम के कारखाने बने।")
    if s==19:
        await event.edit("अर्ज़ किया है… ज़िन्दगी लवडों का पुलिंदा है, चूत आजकल चुनिंदा है… कभी याद कर लिया करो इस नाचीज़ को भी, ये शख्स सिर्फ आपकी गां# मारने के लिए जिंदा है।")

@dark.on(admin_cmd(pattern=r"plove$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    h=(random.randrange(1,9))
    if h==1:
        await event.edit(f" Meri Kisi Gal Te Naraj Na Hovi,\nAkhian Nu Hanjua Nal Na Dhovi,\nMildi Ae Khushi Tenu Hasde Dekh Ke.\nSanu Maut Vi Aa Jave Ta Vi Na Rovi.\n\n\n✍️ {DEFAULTUSER}")
    if h==2:
        await event.edit(f"Dil Karda Ae Tere Kol Aa Ke Ruk Jaava,\nTeri Bukkal Wich Rakh Ke Sir Muk Jaava.\nHanju Ban Ke Digga Teriya Aakhaa Da,\nTere Bulla De Kol Aa Ke Sukk Jaava.\n\n\n✍️ {DEFAULTUSER}")
    if h==3:
        await event.edit(f"Tussi Hasde o sanu hasaan vaaste Tussi rone yo saanu rovaan vaaste Ek vaar rus ke ta vekho sohneyo Marr javange tuhanu manaan vaaste.\n\n\n✍️{DEFAULTUSER}")
    if h==4:
        await event.edit(f"Jo pani wang paviter, pyar tan unu kehnde ne.\n\njo ikk di ho ke reh je, naar tan unu kehnde ne.\n\n\n✍️{DEFAULTUSER}")
    if h==5:
        await event.edit(f"Khushboo teri yaari di saanu mehka jaandi hai,\n Teri har ik kitti hoyi gal saanu behka jaandi hai,\n Saah taan bahut der lagaande ne aun -jaan vich, \nHar saah ton pehle teri yaad aa jaandi hai.\n\n\n✍️{DEFAULTUSER}")
    if h==6:
        await event.edit(f"Yaadan tereiya nu bhullna hun okha ho gaya...... \nJo detey ne tu Gum ohna nu sehna okha ho geya..... \nTu jaan lagey keh deta bhull ja mainu....... \nHun unna gallan nu bhullana okha ho gaya......\n\n\n✍️{DEFAULTUSER}")
    if h==7:
        await event.edit(f"Ae chand chamkna chad vii de \nTeri chandni saanu staandi ae \nTera varga hai usda chehra \nTenu vekh ke usdi yaad aandi ae.\n\n\n✍️{DEFAULTUSER}  ")    
    if h==8:
        await event.edit(f"Tutte hoye Pemane ch jaam nahi aunda, \nIshq de mariz nu araam nahi aunda, \nO Dil todan walya tu e te sochya hunda,\n Tutya hoya Dil kisi de kamm nahi aunda.\n\n\n✍️{DEFAULTUSER}")
    if h==9:
        await event.edit(f"Meri kisi gal te naraj na hovi, \nAkhian nu hanjua nal na dhovi, \nMildi a khushi tenu hasde dekh ke\n Sanu maut v aa jave ta v na rovi…\n\n\n✍️{DEFAULTUSER}")  

@dark.on(admin_cmd(pattern="byeq ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    g=(random.randrange(1,18))
    if g==1:
        await event.edit(" जिंदगी में तन्हा रहना तो मुमकिन नहीं,\nतेरे साथ चलना दुनिया को गवारा भी नहीं,\nइसलिए, तेरा-मेरा दूर जाना ही बेहतर है।")
    if g==2:
        await event.edit("कुछ दिन साथ चलने वाले,\nथोड़ा और साथ चलने की तमन्ना थी,\nमजबूरी है कहना ही पड़ेगा अलविदा।")#creadit to kraken,sawan
    if g==3:
        await event.edit("न कहा न कुछ सुना, बस चुपके से चल दिए,\nमोहब्बत के उन्होंने सारे मायने बदल दिए,\अब तो तन्हा गलियों में गुजरेगी हर शाम,\nमर भी गए, तो भी नहीं भूलेंगे उनका नाम।")
    if g==4:
        await event.edit("पास थे, तो रोने की वजह बनते थे,\nदूर जाकर शायद मुस्कुराना सीख लें आप।")
    if g==5:
        await event.edit("दोबारा मिलें जिंदगी में यह दुआ करेंगे,\nदूर रहकर भी नजदीक होने की चाह करेंगे।")#creadit to kraken,sawan
    if g==6:
        await event.edit("माफ करना मुझे दूर तो जाना पड़ेगा,\nपास होकर भी तुम्हे अब भूल जाना पड़ेगा।")#creadit to kraken,sawan
    if g==7:
        await event.edit("वो शाम सुहानी थी जो गुजरी तेरे साथ,\nबिन तेरे अब कैसे कटेगी सारी रात,\nसमझ लो तुम भी यह मजबूरी है दिल की,\nनहीं गए, तो कैसे कल फिर होगी मुलाकात।")#creadit to kraken,sawan
    if g==8:
        await eventt.edit("तेरे साथ मुस्कुराना और ठोकरों से संभलना सीखा है,\nआता नहीं अलविदा कहना बस रोकर जताना सीखा है।")
    if g==9:
        await event.edit("यार तेरी दोस्ती को सलाम है,\nअलविदा कहकर भी हंसा दिया,\nयह बस तेरी यारी का कमाल है।")#creadit to kraken,sawan
    if g==10:
        await event.edit("ताउम्र तेरे साथ बीती रातों को फिर याद करेंगे,\nकह सकें अलविदा तुझसे इसलिए मेरे यार,\nआंसू का एक भी कतरा बहाए बिना बात करेंगे।")#creadit to kraken,sawan
    if g==11:
        await event.edit("रूठा जमाना जिंदगी भी रूठी,\nतभी तो तेरे-मेरे बीच ये दूरी छूटी,\nसमझ लेना तुम है ये मेरी मजबूरी,\nवरना न आने देता तेरे-मेरे बीच यह दूरी।")#creadit to kraken,sawan
    if g==12:
        await event.edit("करीब आते-आते तू कुछ दूर सा हो गया है,\nशाम को अलविदा कह तू कहीं गुम सा गया है,\nचाहता हूं मैं करीब होने का एहसास तेरे पर,\nखुशी के खातिर तेरी तुझे अलविदा कह गया हूं।")
    if g==13:
        await event.edit("खुश हूं फिर भी ये आंखे नम हैं,\nन चाहते हुए भी दूर जाने का गम है।")
    if g==14:
        await event.edit("दूर जाने की खबर सुनकर ये धड़कने रुक जाती हैं,\nअलविदा कहने के वक्त यार मेरी आंखें भर आती हैं।")#creadit to kraken,sawan
    if g==15:
        await event.edit(" अब हर लम्हा तुम्हारे बिना सूना सा लगेगा,\nअलविदा कहकर तुम्हारी यादों में जीना पड़ेगा।")
    if g==16:
        await event.edit("अब हलचल है दिल में नई उम्मीद की तलाश के लिए,\nकहना पड़ेगा अलविदा नई मंजिल की तलाश के लिए")
    if g==17:
        await event.edit(" जब तुम जाते हो, तो गुलिस्तां के सभी फूल झड़ जाते हैं,\nसंभलकर कहो अलविदा जाते-जाते पेड़ों से क्यों टकरा जाते हो।")
    if g==18:
        await event.edit("14. तिरछी निगाहों से जो देखा उन्होंने,\nतो हम मदहोश हो चले,\nजब पता चला कि वो अलविदा कहने आए,\nतो हम बेहोश हो चले।")

@dark.on(admin_cmd(pattern=r"sadstatusr$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    s=(random.randrange(1,15)) 
    if s==1:
        await event.edit("HAMNE TOH BSS DOST KO HI BEWAFA SAMJHA THHA...\nYAHAAN SACCHA PYAAR V SAATH NHI DIYA🥱🥱")
    if s==2:
        await event.edit("Love leads to death 🥱🥱\nOr to a living dead 🥱🥱")
    if s==3:
        await event.edit("BAATEN TU KABHI YE NA BHULNA.....\nKOI TERE KAARANN HAI..MRR RHA 🥱🥱🥱🥱")
    if s==4:
        await event.edit("Ae dost Tere jaise log ko kaat k fekk dange hm\nMeri taraf aae her toofan ko Teri taraff bhej dange hm...\nLekhin tune Jo saath chorrda hamara ......\nKsm SE badnaam krke tujhe nya dost....\n dhoondh lange hum🥱🥱🥱🥱")
    if s==5:
        await event.edit("Bde ajeeb Hain ye Zindagi k raaste.........\nAnjaane modd pe log Mill jaate Hain...khhud ko apna BTA k.....chorrrd jaate Hain...\n. KRTE hai. H baat (Zindagi bhar saath rahenge) interest khtm hone prr......zinda LAASH BNA jaate h🥱🥱🥱")
    if s==6:
        await event.edit("Dill jaisa thha waisa hi reh jaata......\nJitne dard thhey UTNE kaafi thhey.......\nZindagi aap me aake aur tadpaa diya.........\nMillla kya u badnaam krke ....zinda LAASh...... DIYA🙃🙃")
    if s==7:
        await event.edit("DARD SE IS KADAR DOSTI HO GYI.......\nZINDAGI BEDARD SI HO GYI.......\nJALL  GAY WO ASHIYANA.......JO KABHI BNA HI NHI THHA......\nROSHNI TOH CHORRDO..........\nGHAR MEIN JO MOMABATTIE  THHI WO V KHTM HO GYI.........🥱🥱")
    if s==8:
        await event.edit("Zindagi barbaad hai...... Zindagi SE pyaar na Karo.......\nHo raat toh Dinn ka intezaar na Karo.......\nWo Pall v aaega....jiss pal ka INTEZAAR na  ho aako.....\nPRRR uspe kabhi aitbaar na Karo........🥱🥱")
    if s==9:
        await event.edit("Dard k saath rhte hue v dosti nhi Hui\nZindagi bedard si hote hue v nhi Hui\nAashiyana toh jall gya\nPrr  Roshni nhi Hui ..........❤️")
    if s==10:
        await event.edit("ME: DUNIYA ME AISI KYA CHEEZ HAI JO FREE MEI MILTI HAI............\nMAH HEART : DHOKHA ")
    if s==11:
        await event.edit("JO INSAAN AAPKO TADAPTA HUA ....ROTA CHORRD DE NA.......... TOH SAMAJH LENA WO KABHI AAPSE \nPYAAR NHI KRR SKTA.....AGAR KOI PYAAR KAREGA NA......\nTOH WO KABHI AAPKO AISEY NHI CHORRDEGA.......🥱🥱")
    if s==12:
        await event.edit("TOOTE HAIN.....ES TARAH DILL ......\nAWAAZ TKK NA AAI....\nHUM JAISEY JEE RHE H.....\nKOI JEE K TOH BTAAE....🙃🙃")
    if s==13:
        await event.edit("AANKHON ME AANSU LEKE........\nHOTHON SE MUSKURAAE................\nHUM JAISEY JEE RHE HAIN.......\nKLI JEE K TOH BTAAE...🙃🙃")
    if s==14:
        await event.edit("TUJHE KAISEY PTA NA CHALAA.................\nK MAIN TENU PYAAR KRR Di AAN...........\nTUJHE KAISEY PTA NA CHALAA......\nK TERA INTEZAAR KRR DI AAN........🙃")
    if s==15:
        await event.edit("MTT CHORRDNA KISIKO USKE HAAL PE.......\nHO SKTA H.......\nAAPKE ALAWA  USKE PAAS AUR KOI NA HO.......🙃🙃")
     

CmdHelp("sadsahyri").add_command(
  "psad", "<sad sahyri>", "sad sahyri"
).add_command(
  "sdirty", "<dirty sahyri>", "dirty sahyri"
).add_command(
  "plove", "<love sahyri>", "love sahyri"
).add_command(
  "byeq", "<goodbye sahyri>", "goodbye sahyri"
).add_command(
  "sadstatusr", "<sadstatus>", "sadstatus"
).add()
