STAR_5 = [
    "apple","amazon","microsoft","disney","berkshire hathaway","starbucks","google","jpmorgan chase","costco","salesforce","southwest airlines",
    "coca cola","nike","american express","fedex","netflix","marriott","walmart","delta airlines","nordstrom","home depot","target","procter & gamble","usaa",
    "blackrock","johnson & johnson","goldman sachs","singapore airlines","3m","toyota","unilever","bmw","ups","accenture","ibm","visa","charles schwab",
    "cvs health","nestlé","adidas","mcdonal's","mastercard","pepsico","caterpillar","l'oréal","lockhead martin","adobe","publix super markets","merck","exxon mobil"]

STAR_4 = [
    "Reliance","Indian Oil Corporation","Oil & Natural Gas Corporation","State Bank of India","tata",
    "Bharat Petroleum Corporation","Rajesh Exports","Coal India","Larsen & Toubro","ICICI","Hindalco Industries","hdfc","mahindra","ntpc",
    "vedanta","maruti","suzuki","nayara","airtel","infosys","jsw steel","gail","grasim","axis","motherson sumi","wipro","hcl","canara","baroda",
    "itc","jindal steel","kotak","general insurance corporation","hyundai","bajaj","vodafone","idea","union","ultratech","power grid","hero",
    "ashok leyland","Bharat Heavy Electricals","Sun Pharmaceuticals","NABARD","Interglobe Aviation","IFFCO","IndusInd","honda","ambuja","adani power",
    "idbi","syndicate","future retail","avenue","andhra","upl","sundaram clayton","titan","oriental","aurobindo pharma","tvs motor","asian paints",
    "max financial","Hindustan Aeronautics","allahabad","apollo","eid party","lic","lupin","mrf","cipla","indiabulls","cipla","honda",
    "dr reddys","uco bank","nirma","shriram transport","aditya birla","ptc","citibank","acc","exide","jindal stainless","piramal","cadila",
    "torrent power","l&t","siemens","idfc","bosch","federal bank","dewan housing","ncc","shree cement","nmdc","jindal saw","rain industries",
    "maharashtra","bharat electronics","standard chartered","adani ports","varroc","bombay burmah","hsbc","national aluminium","nlc india",
    "nestle","cesc","britannia","kec international","chambal chemicals","edelweiss","kalpatarau","nhpc","sidbi","jk tyre","bharat forge",
    "eicher","godrej","jaiprakash associates","hindustan","m&m","rail vikas nigam","havells","glenmark","nbcc","dalmia","macrotech","rashtriya",
    "jsw energy","gujarat","dilip buildcon","adani","united spirits","jain irrigation","hubli","spicejet","gsfc","parle","dlf","jubliant life",
    "welspun corp","graphite india","pc jeweller","dabur","zuari agro","sterling & wilson","aditya birla","gmr","bharti infratel","dcm shriram",
    "marico","polycab india","apar industries","uflex","mphasis","srf","rbl","bandhan","torrent","muthoot","voltas","endurance technologies","alkem","pidilite",
    "arvind","apl","ceat","hfg","seciurity & intelligence","mindtree","cholamandalam","vardham textiles","abb india","raymond",
    "amara raja","allcargo","karnataka","irb","prestige","future lifestyle","deutsche","deepak fertilizers","karur vysya","thomas cook",
    "whirlpool","birla","united breweries","escorts","srei","future","basf","prism","berger","simplex","dish tv","gnfc","thermax","shriram",
    "cummins","biocon","gfl","minda","renault","surya roshni","zee","tube","the india","supreme","nerolac","aegis","hudco","sadbhav","balkrishna",
    "divi's","jk cement","igsec","trident","gsk","sterlite","shree renuka","iifl","varun beverages","ircon","the ramco","oracle","blue star",
    "suzlon energy","philips","fortis","ashoka","schaeffler","balrampur","hinduja","sintex","polyplex","himachal","aarti","cyient","hatsun",
    "hexaware","sundram","indian hotels","joyalukkas","colgate","crompton","bombay","jayaswal","team lease","krbl","atul","gvk","kei",
    "shoppers","jk lakshmi","city union","sundaram","skoda","century","kesoram","ge t&d","manappuram","fullerton","wockhardt","electrotherm",
    "jaiprakash","castrol","zensar","alembic","sun","shipping corporation","ambuja","prakash","lt foods","ipca","jindal","firstsource","great eastern",
    "pnc","Sobha","Abbott India","Mukand","Triveni Engineering and Industries","Force Motors","NIIT","Ballarpur","Brigade","Kirloskar","Tamilnad Mercantile Bank",
    "Time Technoplast","Jubilant","Gokul Agro","Strides","Avanti","Gayatri Projects","KPR Mill","Wheels India","Dhampur Sugar Mills","Garden Silk Mills",
    "BEML","Kirloskar","Persistent Systems","GHCL","Godawari Power","aia","Sintex","monnet","finolex","tafe","bgr","honeywell","america",
    "blue dart","cochin","mangalore chemicals","skf","nava bharat","ifci","pvr","venkys","sjvn","lakshmi vilas","bata","oberoi realty",
    "trent","infinite computer","page","sia","p&g","kajaria","asahi","jbf","sonata","akzo","dixon","rswm","mep","wabco","forbes","sanofi",
    "konkan","narayana","filatex","shirpur","pi industries","j kumar infra","himatsingka seide","nectar","electrosteel","ratnamani",
    "redington","va tech","galaxy","carborundum","essel","amber","hsil","emami","canon","bayer","mahanagar","rane holdings","orient","godfrey",
    "prime focus","v-guard","shankara building","birlasoft","vindhya","southern petrochemical","sutlej textiles","heritage","usha",
    "brightcom","dhunseri","astral poly","wall street","itd","avadh","bnp","magma","db corp","motilal oswal","montecarlo","siyaram",
    "solar","jayant arg","himadri","granules","ht media","dalmia bharat","nilkamal","parag milk","jagran prakashan","religare","Huhtamaki",
    "sarda energy","knr","relaxo","hitachi","equitas","phoenix mills","nahar spinning","asian star","sandhar techologies","rites","sunflag iron",
    "laurus labs","pfizer","century plyboards","omaxe","savita oil","power mech","mcleod russle","natco pharma","kirloskar","hil","meghmani",
    "jamna auto","linde india","sheela foam","heildelberg","kirloskar ferrous","rolta","pennar","cosmo","ttk"]

class rating:

    def get_rating(self, company_name):
        rating = 3
        for i in STAR_5:
            if i.lower() in company_name.lower():
                rating = 5
                break
        for i in STAR_4:
            if i.lower() in company_name.lower():
                rating = 4
                break

        return rating