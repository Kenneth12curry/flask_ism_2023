articles = [
    {
        "id": 1,
        "title": "Hp EliteBook Folio 104...",
        "img_url": "https://i.roamcdn.net/hz/ed/listing-thumb-360w/232b736215194c80f58f0ea55aa8c2df/-/horizon-files-prod/ed/picture/q0gg54vk/968f60e2fb703130fa410fee52c341ac82d742fd.jpg",
        "prix": "235 000 F Cfa",
    },
    {
        "id": 2,
        "title": "Imac 2015",
        "img_url": "https://i.roamcdn.net/hz/ed/listing-thumb-360w/33ccb595c254f74a6bb546c4fbb7c214/-/horizon-files-prod/ed/picture/q0gg5qew/22b4c82e3957672687c1a66ed8620a8c60bf17a7.jpg",
        "prix": "300 000 F Cfa",
    },
    {
        "id": 3,
        "title": "HP ELITEBOOK 840 G2..",
        "img_url": "https://i.roamcdn.net/hz/ed/listing-thumb-360w/02550547f790550baf07bd458745da87/-/horizon-files-prod/ed/picture/q788gm78/37efe9607da6d9fbb41b67457b7a15db79a525ed.jpg",
        "prix": "175 000 F Cfa",
    },
    {
        "id": 4,
        "title": "De superbes appartem..",
        "img_url": "https://i.roamcdn.net/hz/ed/listing-thumb-360w/e1726bd40cd0e2802a9c11ef4367d0ea/-/horizon-files-prod/ed/picture/q5669wk2/2ebacfc1e5958d91dbbcd6817fc8eb946559b4d4.jpg",
        "prix": "70 000 000 F Cfa",
    },
    {
        "id": 5,
        "title": "Dell Latitude 3379 Tact..",
        "img_url": "https://i.roamcdn.net/hz/ed/listing-thumb-360w/63dbaf00ae0560fe6daeb1aa8bed61b7/-/horizon-files-prod/ed/picture/q4447e8m/e0e8df02b67370056d05f0648cb756796e0ea122.jpg",
        "prix": "150 000 F Cfa",
    },

]

boutiques = [

    {
        "id": 1,
        "nom": "Hp EliteBook Folio 104...",
        "img_url": "https://i.roamcdn.net/hz/ed/listing-thumb-360w/232b736215194c80f58f0ea55aa8c2df/-/horizon-files-prod/ed/picture/q0gg54vk/968f60e2fb703130fa410fee52c341ac82d742fd.jpg",

    },
    {
        "id": 2,
        "nom": "Hp EliteBook Folio 104...",
        "img_url": "https://i.roamcdn.net/hz/ed/listing-thumb-360w/1701000eaf501a21f8629a503f7a1161/-/horizon-files-prod/ed/logo/q9mmn0x6/b38f6c5cc2919926a9d3d742c20bad7bd06bb61e.jpg",

    },
    {
        "id": 3,
        "nom": "Hp EliteBook Folio 104...",
        "img_url": "https://i.roamcdn.net/hz/ed/listing-thumb-360w/ed9b63d6e9a6e0177b16d21b9f3a1711/-/horizon-files-prod/ed/logo/qrzzrxej/43279de2acc1581e01799d5e151bd61b251015bd.jpg",

    },
    {
        "id": 4,
        "nom": "Hp EliteBook Folio 104...",
        "img_url": "https://i.roamcdn.net/hz/ed/listing-thumb-360w/6d3d3bd634848ad27e6c054c2e6611d3/-/horizon-files-prod/ed/logo/q6jq826/d4a363cf207b92d794c9f3af36cb7a4b55b338e3.png",

    },
    {
        "id": 5,
        "nom": "Hp EliteBook Folio 104...",
        "img_url": "https://i.roamcdn.net/hz/ed/listing-thumb-360w/2823bb935cc9d1053b3788eacc865162/-/horizon-files-prod/ed/logo/qz5vj4r/7c013e4e54403a5de3498685cc77e3e1be2f09b3.jpg",

    },

]


def getAllArticles():
    return articles


def findArticleById(id_article):
    for a in articles:
        if a["id"] == id_article:
            return a
    return None


def getAllShops():
    return boutiques
