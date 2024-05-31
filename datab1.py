from pymongo import MongoClient
from datetime import datetime, timedelta
import random

client = MongoClient('mongodb://localhost:27017/')
db = client['RGR2']

groups = [
    {"_id":"1", "name": "Псих1", "direction": "Психология"},
    {"_id":"2", "name": "Псих2", "direction": "Психология"},
    {"_id":"3", "name": "Псих3", "direction": "Психология"},
    {"_id":"4", "name": "Фил1", "direction": "Философия"},
    {"_id":"5", "name": "Фил2", "direction": "Философия"},
    {"_id":"6", "name": "Фил3", "direction": "Философия"},
    {"_id":"7", "name": "Соц1", "direction": "Социология"},
    {"_id":"8", "name": "Соц2", "direction": "Социология"},
    {"_id":"9", "name": "Соц3", "direction": "Социология"}
]

db.groups.insert_many(groups)

students = [
    {
        "name": "Данилов Глеб Фёдорович",
        "birthday": "15/05/2003",
        "address": "Россия, г. Ставрополь, Совхозная ул., д. 9 кв.8",
        "phone": "+7(913)647-40-23",
        "email": "fudog_idofo15@mail.ru",
        "group_id": "1",
        "direction": "Психология",
        "budget": True
    },

    {
        "name": "Соловьев Макар Игоревич",
        "birthday": "19/03/2001",
        "address": "Россия, г. Пушкино, Полесская ул., д. 3 кв.90",
        "phone": "+7(913)411-10-50",
        "email": "mijib-ujuya59@mail.ru",
        "group_id": "1",
        "direction": "Психология",
        "budget": True
    },

    {
        "name": "Михайлов Александр Максимович",
        "birthday": "21/03/2003",
        "address": "Россия, г. Воронеж, Строителей ул., д. 23 кв.150",
        "phone": "+7(913)561-54-94",
        "email": "fixa_vaxiku13@mail.ru",
        "group_id": "1",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Иванова Варвара Эмировна",
        "birthday": "06/03/2001",
        "address": "Россия, г. Ставрополь, Майская ул., д. 15 кв.80",
        "phone": "+7(913)127-23-30",
        "email": "cogu_favapi40@mail.ru",
        "group_id": "1",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Федотова Антонина Кирилловна",
        "birthday": "12/09/2000",
        "address": "Россия, г. Сыктывкар, Заречный пер., д. 2 кв.172",
        "phone": "+7(913)784-80-84",
        "email": "hihezo_zilu38@mail.ru",
        "group_id": "1",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Кузнецова Полина Данииловна",
        "birthday": "30/12/2003",
        "address": "Россия, г. Москва, Солнечный пер., д. 12 кв.11",
        "phone": "+7(913)056-01-69",
        "email": "busox_omola40@mail.ru",
        "group_id": "1",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Малинин Андрей Даниилович",
        "birthday": "01/06/2001",
        "address": "Россия, г. Ноябрьск, Октябрьский пер., д. 22 кв.31",
        "phone": "+7(913)312-80-74",
        "email": "kecipu_poco36@mail.ru",
        "group_id": "1",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Иванов Георгий Дмитриевич",
        "birthday": "21/08/2000",
        "address": "Россия, г. Электросталь, Полесская ул., д. 11 кв.201",
        "phone": "+7(913)924-36-43",
        "email": "nina-tomuci37@mail.ru",
        "group_id": "2",
        "direction": "Психология",
        "budget": True
    },

    {
        "name": "Родионова Полина Максимовна",
        "birthday": "13/12/2003",
        "address": "Россия, г. Новый Уренгой, Юбилейная ул., д. 14 кв.75",
        "phone": "+7(913)382-36-79",
        "email": "gari_vikezu93@mail.ru",
        "group_id": "2",
        "direction": "Психология",
        "budget": True
    },

    {
        "name": "Исаев Михаил Захарович",
        "birthday": "17/03/2000",
        "address": "Россия, г. Владикавказ, Вокзальная ул., д. 15 кв.8",
        "phone": "+7(913)357-51-72",
        "email": "vijub_ahisu37@mail.ru",
        "group_id": "2",
        "direction": "Психология",
        "budget": True
    },

    {
        "name": "Горячева Фатима Дмитриевна",
        "birthday": "04/04/2000",
        "address": "Россия, г. Брянск, Первомайская ул., д. 19 кв.178",
        "phone": "+7(913)109-48-56",
        "email": "seyi-lutato71@mail.ru",
        "group_id": "2",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Голубева Мирослава Константиновна",
        "birthday": "04/08/2003",
        "address": "Россия, г. Санкт-Петербург, Заречный пер., д. 20 кв.102",
        "phone": "+7(913)466-60-00",
        "email": "cezefo_yuhi81@mail.ru",
        "group_id": "2",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Борисова Варвара Семёновна",
        "birthday": "30/07/2000",
        "address": "Россия, г. Находка, Речной пер., д. 19 кв.9",
        "phone": "+7(913)366-43-97",
        "email": "nuxoz_ugiha50@mail.ru",
        "group_id": "2",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Петухов Григорий Платонович",
        "birthday": "30/01/2002",
        "address": "Россия, г. Брянск, Калинина ул., д. 5 кв.78",
        "phone": "+79137650427",
        "email": "buba_mahazo52@mail.ru",
        "group_id": "2",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Горелов Андрей Иванович",
        "birthday": "10/11/2003",
        "address": "Россия, г. Саранск, Набережная ул., д. 4 кв.68",
        "phone": "+7(913)961-18-44",
        "email": "sufu-tupite15@mail.ru",
        "group_id": "2",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Анисимов Фёдор Евгеньевич",
        "birthday": "14/05/2001",
        "address": "Россия, г. Москва, Пионерская ул., д. 6 кв.2",
        "phone": "+7(913)099-04-94",
        "email": "vijobum_ofe73@mail.ru",
        "group_id": "3",
        "direction": "Психология",
        "budget": True
    },

    {
        "name": "Новикова Ольга Данииловна",
        "birthday": "05/06/2001",
        "address": "Россия, г. Чита, Мичурина ул., д. 15 кв.47",
        "phone": "+7(913)030-88-79",
        "email": "nemubam-ige88@mail.ru",
        "group_id": "3",
        "direction": "Психология",
        "budget": True
    },

    {
        "name": "Михеева Елизавета Семёновна",
        "birthday": "20/06/2000",
        "address": "Россия, г. Железногорск, Трудовая ул., д. 18 кв.170",
        "phone": "+7(913)164-56-81",
        "email": "vuni-feyiho99@mail.ru",
        "group_id": "3",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Колесникова Анна Артёмовна",
        "birthday": "29/03/2002",
        "address": "Россия, г. Калуга, Кирова ул., д. 14 кв.79",
        "phone": "+7(913)359-35-07",
        "email": "wimufu-vago7@mail.ru",
        "group_id": "3",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Лебедев Матвей Глебович",
        "birthday": "19/09/2002",
        "address": "Россия, г. Новочебоксарск, Коммунистическая ул., д. 10 кв.85",
        "phone": "+7(913)733-13-17",
        "email": "wanot-epizo35@mail.ru",
        "group_id": "3",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Акимова Мария Ибрагимовна",
        "birthday": "24/09/2003",
        "address": "Россия, г. Рубцовск, Пушкина ул., д. 19 кв.64",
        "phone": "+7(913)126-72-36",
        "email": "kelofa_xawo49@mail.ru",
        "group_id": "3",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Тимофеева Вера Ивановна",
        "birthday": "30/11/2003",
        "address": "Россия, г. Тольятти, Приозерная ул., д. 8 кв.67",
        "phone": "+7(913)125-09-53",
        "email": "det-ufujava63@mail.ru",
        "group_id": "3",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Зайцева Эвелина Кирилловна",
        "birthday": "01/02/2001",
        "address": "Россия, г. Хабаровск, Дорожная ул., д. 14 кв.184",
        "phone": "+7(913)860-11-38",
        "email": "ruti_xakise66@mail.ru",
        "group_id": "3",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Калинин Игорь Билалович",
        "birthday": "07/08/2001",
        "address": "Россия, г. Пермь, Березовая ул., д. 21 кв.188",
        "phone": "+7(913)078-76-62",
        "email": "jemuna-mare42@mail.ru",
        "group_id": "3",
        "direction": "Психология",
        "budget": False
    },

    {
        "name": "Хохлов Тимофей Ярославович",
        "birthday": "19/05/2002",
        "address": "Россия, г. Рубцовск, Дачная ул., д. 25 кв.137",
        "phone": "+7(913)006-31-87",
        "email": "gonuci-give99@mail.ru",
        "group_id": "4",
        "direction": "Философия",
        "budget": True
    },

    {
        "name": "Муравьева София Михайловна",
        "birthday": "28/01/2001",
        "address": "Россия, г. Сыктывкар, Полесская ул., д. 10 кв.140",
        "phone": "+7(913)842-94-95",
        "email": "zug_iyibote57@mail.ru",
        "group_id": "4",
        "direction": "Философия",
        "budget": True
    },

    {
        "name": "Рудакова Елизавета Тимофеевна",
        "birthday": "23/01/2003",
        "address": "Россия, г. Невинномысск, Заречный пер., д. 21 кв.117",
        "phone": "+7(913)313-10-22",
        "email": "paronoj-iwi47@mail.ru",
        "group_id": "4",
        "direction": "Философия",
        "budget": True
    },

    {
        "name": "Федосеев Георгий Романович",
        "birthday": "01/06/2003",
        "address": "Россия, г. Дербент, Юбилейная ул., д. 1 кв.179",
        "phone": "+7(913)773-07-30",
        "email": "gupog_izozo98@mail.ru",
        "group_id": "4",
        "direction": "Философия",
        "budget": False
    },

    {
        "name": "Агапова Злата Артёмовна",
        "birthday": "12/07/2001",
        "address": "Россия, г. Курган, Солнечный пер., д. 16 кв.164",
        "phone": "+7(913)470-65-85",
        "email": "xucix_ereri14@mail.ru",
        "group_id": "4",
        "direction": "Философия",
        "budget": False
    },

    {
        "name": "Григорьев Даниил Васильевич",
        "birthday": "12/04/2000",
        "address": "Россия, г. Белгород, Партизанская ул., д. 25 кв.11",
        "phone": "+7(913)374-77-98",
        "email": "gehus_ohaho59@mail.ru",
        "group_id": "4",
        "direction": "Философия",
        "budget": False
    },

    {
        "name": "Герасимова Полина Алексеевна",
        "birthday": "23/03/2001",
        "address": "Россия, г. Щёлково, Дружная ул., д. 24 кв.67",
        "phone": "+7(913)122-15-56",
        "email": "xac-etupiwo58@mail.ru",
        "group_id": "4",
        "direction": "Философия",
        "budget": False
    },

    {
        "name": "Кузнецова Екатерина Евгеньевна", 
        "birthday": "22/12/2002", 
        "address": "Россия, г. Дзержинск, Пролетарская ул., д. 6 кв.213",
        "phone": "+7(913)203-94-46", 
        "email": "dorela-disi99@mail.ru",
        "group_id": "5",
        "direction": "Философия",
        "budget": True
    },
    
    {
        "name": "Воробьева Ксения Дмитриевна", 
        "birthday": "29/01/2000", 
        "address": "Россия, г. Дзержинск, Пролетарская ул., д. 6 кв.213", 
        "phone": "+7(913)275-86-02",
        "email": "kic-uvuhuba80@mail.ru",
        "group_id": "5",
        "direction": "Философия",
        "budget": True
    },
    
    {
        "name": "Фокина Марта Кирилловна", 
        "birthday": "01/09/2002", 
        "address": "Россия, г. Псков, Комсомольская ул., д. 2 кв.110", 
        "phone": "+7(913)877-57-66",
        "email": "noyipey_oye90@mail.ru",
        "group_id": "5",
        "direction": "Философия", 
        "budget": False
    },
    
    {
        "name": "Суханов Николай Лукич", 
        "birthday": "29/07/2001", 
        "address": "Россия, г. Орск, Космонавтов ул., д. 17 кв.53", 
        "phone": "+7(913)669-63-88",
        "email": "vih_ipuhine62@mail.ru",
        "group_id": "5", 
        "direction": "Философия",
        "budget": False
    },
    
    {
        "name": "Медведева Мария Матвеевна", 
        "birthday": "14/08/2003", 
        "address": "Россия, г. Орск, Космонавтов ул., д. 17 кв.53", 
        "phone": "+7(913)694-99-28",
        "email": "kim-ikeraza43@mail.ru",
        "group_id": "5", 
        "direction": "Философия",
        "budget": False
    },
    
    {
        "name": "Филиппова Эмилия Дмитриевна", 
        "birthday": "14/07/2003", 
        "address": "Россия, г. Нефтекамск, Майская ул., д. 5 кв.150", 
        "phone": "+7(913)408-56-19",
        "email": "sez-ojunaka47@mail.ru",
        "group_id": "5", 
        "direction": "Философия",
        "budget": False
    },
    
    {
        "name": "Тарасов Никита Алексеевич", 
        "birthday": "12/03/2000", 
        "address": "Россия, г. Белгород, Западная ул., д. 4 кв.182", 
        "phone": "+7(913)391-24-61",
        "email": "mawa_macuva53@mail.ru",
        "group_id": "5", 
        "direction": "Философия",
        "budget": False
    },

    {
        "name": "Миронова Ольга Александровна", 
        "birthday": "22/09/2000", 
        "address": "Россия, г. Рыбинск, Чапаева ул., д. 23 кв.167", 
        "phone": "+7(913)298-55-17",
        "email": "nix-ecanonu31@mail.ru",
        "group_id": "5", 
        "direction": "Философия",
        "budget": False
    },

    {
        "name": "Андреев Роберт Максимович", 
        "birthday": "13/11/2002", 
        "address": "Россия, г. Москва, Красноармейская ул., д. 21 кв.21", 
        "phone": "+7(913)317-69-59",
        "email": "pox-ujadine80@mail.ru",
        "group_id": "6", 
        "direction": "Философия",
        "budget": True
    },
    
    {
        "name": "Беликов Даниил Елисеевич", 
        "birthday": "08/03/2000", 
        "address": "Россия, г. Томск, Ленина ул., д. 21 кв.121", 
        "phone": "+7(913)545-46-32",
        "email": "jafe_ribasi85@mail.ru",
        "group_id": "6", 
        "direction": "Философия",
        "budget": True
    },
    
    {
        "name": "Мальцева Василиса Степановна", 
        "birthday": "07/01/2001", 
        "address": "Россия, г. Владимир, Зеленая ул., д. 21 кв.105", 
        "phone": "+7(913)307-02-64",
        "email": "pisuw-axika28@mail.ru",
        "group_id": "6",
        "direction": "Философия",
        "budget": False
    },
    
    {
        "name": "Логинов Артемий Матвеевич", 
        "birthday": "07/12/2002", 
        "address": "Россия, г. Октябрьский, Полевой пер., д. 2 кв.149", 
        "phone": "+7(913)557-02-91",
        "email": "sazuy_eguxi16@mail.ru",
        "group_id": "6", 
        "direction": "Философия",
        "budget": False
    },
    
    {
        "name": "Орлов Михаил Лукич", 
        "birthday": "28/08/2003", 
        "address": "Россия, г. Новосибирск, Гагарина ул., д. 1 кв.2", 
        "phone": "+7(913)083-04-26",
        "email": "texe_gahajo81@mail.ru",
        "group_id": "6", 
        "direction": "Философия",
        "budget": False
    },
    
    {
        "name": "Головин Илья Дмитриевич", 
        "birthday": "05/05/2003", 
        "address": "Россия, г. Долгопрудный, ЯнкиКупалы ул., д. 9 кв.164", 
        "phone": "+7(913)615-34-74",
        "email": "gilafi_vozu90@mail.ru",
        "group_id": "6", 
        "direction": "Философия",
        "budget": False
    },
    
    {
        "name": "Андрианова Камила Арсентьевна", 
        "birthday": "07/03/2001", 
        "address": "Россия, г. Березники, Дзержинского ул., д. 24 кв.38", 
        "phone": "+7(913)294-94-04",
        "email": "yomiya-gebo55@mail.ru",
        "group_id": "6", 
        "direction": "Философия",
        "budget": False
    },

    {
        "name": "Петров Марсель Егорович", 
        "birthday": "05/11/2001", 
        "address": "Россия, г. Чебоксары, Западная ул., д. 22 кв.108", 
        "phone": "+7(913)553-01-97",
        "email": "cumor-uzuja10@mail.ru",
        "group_id": "6", 
        "direction": "Философия",
        "budget": False
    },

    {
        "name": "Осипов Андрей Ильич", 
        "birthday": "11/03/2000", 
        "address": "Россия, г. Пермь, Вокзальная ул., д. 21 кв.67", 
        "phone": "+7(913)805-28-03",
        "email": "dix-urorate8@mail.ru",
        "group_id": "6", 
        "direction": "Философия",
        "budget": False
    },

    {
        "name": "Колесникова Алиса Львовна", 
        "birthday": "26/03/2002", 
        "address": "Россия, г. Улан-Удэ, Вишневая ул., д. 16 кв.14", 
        "phone": "+7(913)940-97-42",
        "email": "tewu_najeke91@mail.ru",
        "group_id": "7", 
        "direction": "Социология",
        "budget": True
    },
    
    {
        "name": "Казаков Максим Мирославович", 
        "birthday": "03/05/2002", 
        "address": "Россия, г. Керчь, Железнодорожная ул., д. 23 кв.96", 
        "phone": "+7(913)355-43-96",
        "email": "naz_obafoko48@mail.ru",
        "group_id": "7",
        "direction": "Социология", 
        "budget": True
    },
    
    {
        "name": "Никифоров Артём Викторович", 
        "birthday": "31/01/2002", 
        "address": "Россия, г. Шахты, Юбилейная ул., д. 17 кв.18", 
        "phone": "+7(913)537-17-87",
        "email": "kizec_anuhu13@mail.ru",
        "group_id": "7", 
        "direction": "Социология",
        "budget": True
    },
    
    {
        "name": "Котова Кира Олеговна", 
        "birthday": "31/03/2003", 
        "address": "Россия, г. Находка, Мира ул., д. 15 кв.185", 
        "phone": "+7(913)819-22-45",
        "email": "fic-iworeme67@mail.ru",
        "group_id": "7", 
        "direction": "Социология",
        "budget": False
    },
    
    {
        "name": "Михеев Богдан Тимофеевич", 
        "birthday": "14/04/2000", 
        "address": "Россия, г. Ачинск, Восточная ул., д. 13 кв.104", 
        "phone": "+7(913)961-60-45",
        "email": "tek_onujeku11@mail.ru",
        "group_id": "7",
        "direction": "Социология", 
        "budget": False
    },
    
    {
        "name": "Иванова Мария Адамовна", 
        "birthday": "16/10/2003", 
        "address": "Россия, г. Южно-Сахалинск, Чкалова ул., д. 20 кв.87", 
        "phone": "+7(913)909-30-60",
        "email": "dok-itexina64@mail.ru",
        "group_id": "7", 
        "direction": "Социология",
        "budget": False
    },
    
    {
        "name": "Латышева Анастасия Макаровна", 
        "birthday": "06/10/2000", 
        "address": "Россия, г. Пенза, Песчаная ул., д. 18 кв.59", 
        "phone": "+7(913)076-75-47",
        "email": "pubafuv-efo7@mail.ru",
        "group_id": "7", 
        "direction": "Социология",
        "budget": False
    },

    {
        "name": "Фадеев Андрей Андреевич", 
        "birthday": "13/11/2003", 
        "address": "Россия, г. Йошкар-Ола, Зеленый пер., д. 20 кв.143", 
        "phone": "+7(913)666-81-10",
        "email": "jut-ibeyobe16@mail.ru",
        "group_id": "8", 
        "direction": "Социология",
        "budget": True
    },
    
    {
        "name": "Панкова Есения Михайловна", 
        "birthday": "06/11/2001", 
        "address": "Россия, г. Великий Новгород, Пушкина ул., д. 24 кв.77", 
        "phone": "+7(913)816-86-13",
        "email": "suj-oradozu29@mail.ru",
        "group_id": "8", 
        "direction": "Социология",
        "budget": True
    },
    
    {
        "name": "Лавров Алексей Ильич", 
        "birthday": "07/12/2001", 
        "address": "Россия, г. Пермь, Зеленая ул., д. 20 кв.47", 
        "phone": "+7(913)660-44-56",
        "email": "pon-buwaya82@mail.ru",
        "group_id": "8",
        "direction": "Социология", 
        "budget": False
    },
    
    {
        "name": "Новикова Ксения Никитична", 
        "birthday": "04/06/2003", 
        "address": "Россия, г. Южно-Сахалинск, Заводская ул., д. 25 кв.182", 
        "phone": "+7(913)963-74-46",
        "email": "xay_ikimufi68@mail.ru",
        "group_id": "8", 
        "direction": "Социология",
        "budget": False
    },
    
    {
        "name": "Блинова Таисия Фёдоровна", 
        "birthday": "13/06/2003", 
        "address": "Россия, г. Подольск, Мирная ул., д. 20 кв.30", 
        "phone": "+7(913)330-90-22",
        "email": "viruw_iwepe91@mail.ru",
        "group_id": "8", 
        "direction": "Социология",
        "budget": False
    },
    
    {
        "name": "Ефремов Михаил Максимович", 
        "birthday": "18/08/2003", 
        "address": "Россия, г. Саранск, Лесной пер., д. 9 кв.195", 
        "phone": "+7(913)988-81-96",
        "email": "cunuleb_evu49@mail.ru",
        "group_id": "8", 
        "direction": "Социология",
        "budget": False
    },
    
    {
        "name": "Сергеев Денис Фёдорович", 
        "birthday": "24/03/2003", 
        "address": "Россия, г. Красноярск, Совхозная ул., д. 25 кв.194", 
        "phone": "+7(913)508-04-51",
        "email": "koje-jabadu40@mail.ru",
        "group_id": "8", 
        "direction": "Социология",
        "budget": False
    },

    {
        "name": "Волкова Варвара Романовна", 
        "birthday": "22/09/2003", 
        "address": "Россия, г. Волжский, Колхозный пер., д. 11 кв.17", 
        "phone": "+7(913)845-01-33",
        "email": "yalu-wukuta88@mail.ru",
        "group_id": "8", 
        "direction": "Социология",
        "budget": False
    },
    
    {
        "name": "Малышев Егор Максимович", 
        "birthday": "02/10/2002", 
        "address": "Россия, г. Иваново, Пролетарская ул., д. 23 кв.15", 
        "phone": "+7(913)115-67-27",
        "email": "kimudu_ligi30@mail.ru",
        "group_id": "9", 
        "direction": "Социология",
        "budget": True
    },
    
    {
        "name": "Ефимов Семён Романович", 
        "birthday": "16/03/2003", 
        "address": "Россия, г. Красногорск, Калинина ул., д. 25 кв.22", 
        "phone": "+7(913)580-61-26",
        "email": "pal_apiraye80@mail.ru",
        "group_id": "9", 
        "direction": "Социология",
        "budget": True
    },
    
    {
        "name": "Шапошников Иван Елисеевич", 
        "birthday": "19/01/2001", 
        "address": "Россия, г. Волгоград, Минская ул., д. 13 кв.132", 
        "phone": "+7(913)149-24-64",
        "email": "paduha_lalu10@mail.ru",
        "group_id": "9",
        "direction": "Социология", 
        "budget": True
    },
    
    {
        "name": "Тихонов Григорий Максимович", 
        "birthday": "28/03/2003", 
        "address": "Россия, г. Петрозаводск, Рабочая ул., д. 9 кв.185", 
        "phone": "+7(913)620-18-13",
        "email": "miyut_axoco91@mail.ru",
        "group_id": "9", 
        "direction": "Социология",
        "budget": False
    },
    
    {
        "name": "Лобанов Михаил Никитич", 
        "birthday": "08/08/2003", 
        "address": "Россия, г. Орёл, 17 Сентября ул., д. 1 кв.146", 
        "phone": "+7(913)396-01-41",
        "email": "moceni_xave13@mail.ru",
        "group_id": "9", 
        "direction": "Социология",
        "budget": False
    },
    
    {
        "name": "Кулакова Марта Львовна", 
        "birthday": "31/07/2001", 
        "address": "Россия, г. Каменск - Уральский, Березовая ул., д. 25 кв.96", 
        "phone": "+7(913)918-24-29",
        "email": "ralux-etexo71@mail.ru",
        "group_id": "9", 
        "direction": "Социология",
        "budget": False
    },
    
    {
        "name": "Воронина Ариана Георгиевна", 
        "birthday": "31/03/2003", 
        "address": "Россия, г. Батайск, Победы ул., д. 10 кв.93", 
        "phone": "+7(913)543-06-08",
        "email": "xedoc-uzeki22@mail.ru",
        "group_id": "9",
        "direction": "Социология", 
        "budget": False
    },

    {
        "name": "Савин Артур Александрович", 
        "birthday": "19/03/2000", 
        "address": "Россия, г. Новочеркасск, Трудовая ул., д. 10 кв.79", 
        "phone": "+7(913)334-10-84",
        "email": "jom-ehumogu14@mail.ru",
        "group_id": "9",
        "direction": "Социология", 
        "budget": False
    },

    {
        "name": "Богданова Кира Данииловна", 
        "birthday": "21/02/2003", 
        "address": "Россия, г. Брянск, Октябрьский пер., д. 17 кв.109", 
        "phone": "+7(913)918-84-62",
        "email": "wolki_neba81@mail.ru",
        "group_id": "9",
        "direction": "Социология", 
        "budget": False
    }
]

db.students.insert_many(students)

timetable_data = [
    {"number_pair": 1, "start_time": "8:00", "end_time": "9:30"},
    {"number_pair": 2, "start_time": "9:40", "end_time": "11:20"},
    {"number_pair": 3, "start_time": "11:25", "end_time": "12:55"},
    {"number_pair": 4, "start_time": "15:05", "end_time": "16:35"},
    {"number_pair": 5, "start_time": "16:50", "end_time": "18:20"},
    {"number_pair": 6, "start_time": "18:30", "end_time": "20:00"},
    {"number_pair": 7, "start_time": "20:05", "end_time": "21:35"}
]

db.timetable.insert_many(timetable_data)

teachers = [
    {"name": "Сергеев Сергей Сергеевич", "subject": "Общая психология"},
    {"name": "Иванов Иван Иваныч", "subject": "Высшая математика"},
    {"name": "Петров Петр Петрович", "subject": "Всеобщая история"},
    {"name": "Игнатов Игнат Игнатович", "subject": "Физическая культура"},
    {"name": "Андреев Андрей Андреевич", "subject": "Безопасность жизнедеятельности"},
    {"name": "Афанасьев Афанасий Афанасьевич", "subject": "Этика"},
    {"name": "Васильев Василий Васильевич", "subject": "Логика"},
    {"name": "Григорьев Григорий Григорьевич", "subject": "Социология"}
]

db.teachers.insert_many(teachers)

subject_teacher = [
    ["Общая психология", "Сергеев Сергей Сергеевич"],
    ["Высшая математика", "Иванов Иван Иваныч"],
    ["Всеобщая история", "Петров Петр Петрович"],
    ["Физическая культура", "Игнатов Игнат Игнатович"],
    ["Безопасность жизнедеятельности", "Андреев Андрей Андреевич"],
    ["Этика", "Афанасьев Афанасий Афанасьевич"],
    ["Логика", "Васильев Василий Васильевич"],
    ["Социология", "Григорьев Григорий Григорьевич"]
]

sc_date = datetime(2024, 1, 1)
for gr in db.groups.find():
    sc_date += timedelta(days=1)
    for pair_num in range(1, 4):
        random_index = random.randint(0, len(subject_teacher) - 1)
        db.schedule.insert_one({
            "group": gr["_id"],
            "number_pair": pair_num,
            "subject": subject_teacher[random_index][0],
            "teacher": subject_teacher[random_index][1],
            "date": sc_date
        })

def random_int_from_interval(min_val, max_val):
    return random.randint(min_val, max_val)

for st in db.students.find():
    for sem in range(1, 5):
        for subj_teach in subject_teacher:
            db.marks.insert_one({
                "student": st["_id"],
                "semestr": sem,
                "subject": subj_teach[0],
                "teacher": subj_teach[1],
                "mark": random_int_from_interval(2, 5)
            })
    
for s in db.schedule.find():
    for st in db.students.find({"group_id":s["group"]}):
        db.attendence.insert_one({
            "schedule": s["_id"],
            "student": st["_id"],
            "attendence": random.random() < 0.5
        })

print("Данные успешно добавлены в MongoDB.")
