from difflib import SequenceMatcher

slovar_unsorted= {'Откладывание': 'формирование финансовой подушки безопасности, которая может стать спасением в случае непредвиденных обстоятельств',
     'Инвестирование': 'вложение денег с целью получить доход и сохранить капитал. Человек или юридическое лицо вкладывают свободные деньги туда, где они работают и преумножаются.',
     'Краткосрочное инвестирование': 'это вложение свободного капитала в инвестиционные проекты на период длительностью до 12 месяцев с целью быстро приумножить капитал. Краткросрочное инвестрование обычно приносит больший доход, но и риск выше, если сравнивать с долгосрочным инвестированием',
     'Долгосрочное инвестирование': 'это капиталовложения сроком от 1–5 лет и более. Одни и те же виды инвестиций могут быть как краткосрочными, так и долгосрочными. Например, сроки вкладов в облигации могут составлять от 1 года до 50 лет. Целесообразно инвестировать на срок от 1 года и более. На долгосрочном инвестировании меньше риск и меньше прибыль',
     'Банк': 'коммерческая финансовая организация, основные виды деятельности которой — привлечение и размещение денежных средств, а также проведение расчетов. С экономической точки зрения банки выступают на денежном рынке посредниками между теми, у кого есть свободные денежные средства, и теми, кто нуждается в дополнительных ресурсах. Наиболее распространенные продукты банков — расчетно-кассовое обслуживание физических и юридических лиц, вклады и депозиты, кредиты, в том числе ипотечные займы, автокредиты, потребительские кредиты, банковские карты и др.',
     'Заём': 'получение чего-либо взаймы, с условием возврата. В широком смысле этого слова занимать можно не только деньги, но и вещи.',
     'Кредитор': 'тот, кто предоставляет средства. Тот, кому будут возвращаться средства, взятые "взаймы".',
     'Заёмщик':'тот, кто берёт средства в долг и обязан их вернуть в обговоренный срок.',
     'Ипотека': 'это форма залога недвижимости. Ее оформляют, когда покупают квартиру в кредит: банк дает часть денег, покупатель получает право собственности с обременением. Если не погасить кредит вовремя, банк может продать квартиру и забрать деньги в счет долга. Чтобы купить квартиру в ипотеку, нужно правильно выбрать банк и собрать документы для оформления кредита и сделки.',
     'Кредит':'Предоставление товаров или денег в долг. Делится на долгосрочный и краткосрочный. Тем дольше срок кредита, тем больше составит переплата.',
     'Долгосрочный кредит': 'Кредит, выданный предоставленный на продолжительный срок.',
     'Краткосрочный кредит': 'Кредит, выданный предоставленный на продолжительный срок.',
     'Дебетовая карта': 'пластиковая карта, обычно привязанная к одному или нескольким расчетным счетам в банке. Банковские карты используются для безналичных платежей, в том числе и через Интернет, а также для снятия наличных или пополнения счета через банкомат.',
     'Кредитная карта': 'это банковский продукт, с помощью которого клиент может делать покупки, переводы и снимать наличные, даже если в данный момент не имеет собственных денег. Средства берут в долг у банка, расходуют в обычных торговых точках и интернет-магазинах или обналичивают.',
     'Вклад':'умма денег, которую банк принимает от клиента на определенный или неопределенный срок и обязуется возвратить сумму вклада и выплатить проценты на нее на условиях и в порядке, предусмотренных договором. Банки предлагают гражданам вклады до востребования (на неопределенный срок) и срочные депозиты (договором предусмотрен срок, на который банк принимает у вкладчика средства).',
     'Бюджет семьи':'совокупность доходов и расходов семьи за определенный период времени, например, один год или один месяц.',
     'Вексель':'письменное обязательство заемщика (векселедателя) выплатить в установленный срок определенную сумму предъявителю векселя или лицу, указанному в векселе.',
     'Пенсия':'регулярное (ежемесячное) денежное пособие, выплачиваемое лицам, которые достигли пенсионного возраста (пенсия по старости), имеют инвалидность (пенсия по инвалидности) или потеряли кормильца.',
     'Денежный перевод':'это перевод (движение) денежных средств от отправителя к получателю с помощью операторов платежных систем с целью зачисления денежных средств на счет получателя или выдачи ему их в наличной форме.',
     'Закон спроса и предложения':'экономический закон, устанавливающий зависимость величины спроса и предложения товаров на рынке от их цен. При прочих равных условиях, чем цена на товар ниже, тем больше величина спроса (готовность покупать) и тем меньше величина предложения (готовность продавать).',
     'Заработная плата':'вознаграждение за труд в зависимости от квалификации работника, сложности, количества, качества и условий выполняемой работы, а также компенсационные и стимулирующие выплаты.',
     'Микрокредит':' вид финансирования, заключающийся в выдаче небольших займов на небольшие сроки, как правило, под большие проценты, обычно людям, которые не имеют доступа к традиционным банкам в силу разных причин.',
     'Налог транспортный':'налог, взимаемый с владельцев зарегистрированных транспортных средств, который зависит от мощности двигателя и возраста транспортного средства.',
     'НДФЛ':'налог, который составляет 13% от суммарного дохода физического лица в Российской Федерации.',
     'Налог на доходы физических лиц':'налог, который составляет 13% от суммарного дохода физического лица в Российской Федерации.',
     'Налоговая ставка':'величина налоговых начислений на единицу измерения налоговой базы.',
     'Налоговый вычет':'сумма, на которую уменьшается размер дохода (налогооблагаемая база), с которого уплачивается налог.',
     'Торговая наценка':' разница между розничной и оптовой ценой товаров, необходимая для покрытия издержек и получения прибыли предприятиями торговли.',
     'Облигация':'ценная бумага, владелец которой имеет право получить от лица, ее выпустившего, номинальную стоимость облигации деньгами или в виде нового имущества.',
     'Предложение':'количество товара, которое производители готовы продать.',
     'Премия':'одна из форм поощрения за выдающиеся результаты, достигнутые в какой-либо области деятельности либо поощрительная плата работнику за высокую квалификацию, перевыполнение норм выработки, за качество работы в дополнение к окладу.',
     'Прибыль':'положительная разница между суммарными доходами (в которые входит выручка от реализации товаров и услуг, полученные штрафы и компенсации, процентные доходы и т. п.) и затратами на производство или приобретение, хранение, транспортировку, сбыт этих товаров и услуг. Прибыль = Доходы – Затраты (в денежном выражении).',
     'Простые проценты':'метод расчета процентов, при котором начисления происходят однократно на первоначальную сумму вклада (долга).',
     'Сложные проценты':'причисление процентов к сумме вклада, позволяет в дальнейшем осуществлять начисление процентов и на первоначальный вклад, и на пополнение.',
     'Равновесная цена':'цена, при которой объем спроса на рынке равен объему предложения.',
     'Рейтинг':'числовой или порядковый показатель, отображающий важность или значимость определенного объекта или явления.',
     'Рентабельность':'относительный показатель экономической эффективности.',
     'Рыночное равновесие':'ситуация на рынке, когда спрос на товар равен его предложению.',
     'Скидка':'сумма, на которую снижается продажная цена товара, предлагаемого покупателю.',
     'Спрос':'количество товара, который покупатели хотят приобрести за какое-то время (неделя, месяц и т. д.).',
     'Страхование':'финансовая услуга, покрывающая полностью или частично ущерб при наступлении страхового случая.',
     'Страхование жизни':'страхование, предусматривающее защиту имущественных интересов застрахованного лица, связанных с его жизнью и смертью.',
     'Страховая премия':'плата за страхование, которую страхователь обязан внести страховщику в соответствии с договором страхования или законом.',
     'Страховщик':'компания, оказывающая страховые услуги.',
     'Товар':'любая вещь, которая участвует в свободном обмене на другие вещи, или продукт, произведенный для продажи.',
     'Услуга':'результат одного или нескольких действий, осуществленных при взаимодействии поставщика и потребителя (услуги медицинские, образовательные, транспортные, аренда и др.).',
     'Функция спроса':'функция, определяющая спрос в зависимости от влияющих на него различных факторов.',
     'Штраф':'узаконенное наказание за правонарушение в виде определенной суммы денег, обязанность уплаты которой возлагается на нарушителя.',
     'Тело':'это те деньги, которые вы берете в долг у банка, если это тело кредита и деньги, которые вы вложили, если это тело вложения.',
     'Аванс':'Денежная сумма, выдаваемая в счет предстоящих платежей за материальные ценности, выполненные работы и оказанные услуги.',
     'Активы':'Имущество предприятий, в состав которого входят основные средства, другие долгосрочные вложения (включая нематериальные активы), оборотные средства, финансовые активы.',
     'Акциз':'Косвенный налог, включаемый в цену товара и оплачиваемый покупателем. Законом РФ установлен порядок обложения акцизами реализуемых винно-водочных изделий, этилового спирта и пищевого сырья (кроме отпускаемого для выработки ликероводочных изделий и винодельческой продукции, пива, табачных изделий, шин, легковых автомобилей, грузовых автомобилей грузоподъемностью до 1,25 тонн, ювелирных изделий, бриллиантов, изделий из хрусталя, ковров и ковровых изделий, меховых изделий, а также одежды из натуральной кожи).',
     'Банкротство':'Неспособность должника удовлетворить требования кредиторов по оплате товаров (работ, услуг), включая неспособность обеспечить обязательные платежи в бюджет и во внебюджетные фонды.',
     'Бартер':'Безвалютный, но оцененный и сбалансированный обмен товарами, оформляемый единым договором (контрактом).',
     'Товарная биржа':'Коммерческое предприятие, регулярно функционирующий рынок однородных товаров с определенными характеристиками.',
     'Фондовая биржа':'Организованный и регулярно функционирующий рынок по купле-продаже ценных бумаг. Основными функциями фондовой биржи являются мобилизация временно свободных денежных средств через продажу ценных бумаг и установление рыночной стоимости ценных бумаг.',
     'Дефицит':'это когда спрос на какой-то ресурс преобладает над предложением.',
     'Профицит':'Превышение доходов бюджета над его расходами',
     'Бюджетное регулирование':'Система перераспределения денежных средств, состоящая в передаче части ресурсов вышестоящего бюджета нижестоящему в целях сбалансированности. К механизму регулирования относятся: субсидии; субвенции; регулирующие доходные источники. Бюджетное регулирование является составной частью бюджетного процесса.',
     'Валюта':'Денежная единица, используемая для измерения величины стоимости товаров, понятие «валюта» применяется в значениях: денежная единица данной страны (доллар США, японская иена), денежные знаки иностранных государств, а также кредитные и платежные средства, используемые в международных расчетах, и международная (региональная) денежная расчетная единица и платежное средство (переводной рубль, ЕВРО).',
     'Валютный курс':'Цена денежной единицы данной национальной валюты, выраженная в денежных единицах валюты другой страны.',
     'Государственные займы':'Кредитные отношения между государством и юридическими и физическими лицами, в результате которых государство получает определенные суммы денежных средств на определенный срок за определенную плату, осуществляются в виде продажи государственных ценных бумаг, займов внебюджетных фондов и в порядке получения кредитов у банков.',
     'Девальвация':'Понижение курса национальной или международной (региональной) денежной единицы по отношению к валютам другой страны. Очень часто девальвация отражает обесценение валютных средств в результате инфляции.',
     'Инфляция':'Обесценивание денег из-за роста цен на товары и услуги',
     'Дефляция':'Изъятие государством из обращения части обращающихся избыточных денежных средств с целью снижения инфляции.',
     'Долг государственный внешний':'Долговые обязательства Правительства Российской Федерации перед иностранными государствами или международными организациями, выраженные в иностранной валюте.',
     'Долг государственный внутренний':'Долговые обязательства Правительства Российской Федерации, выраженные в валюте Российской Федерации, перед юридическими и физическими лицами, если иное не установлено нормативными актами Российской Федерации. Юридическими формами долговых обязательств являются кредиты, полученные правительством, государственные займы, полученные посредством выпуска ценных бумаг от имени Правительства Российской Федерации, других долговых обязательств, гарантированных Правительством Российской Федерации.',
     'Залог':'Имущество, которое выступает обеспечением по договору займа и гарантирует исполнение заемщиком своих обязательств перед заимодавцем.',
     'Инвестор':'лицо, которому ценные бумаги принадлежат на праве собственности (собственники) или ином вещном праве (владельцы).',
     'Исковая давность':'Срок для защиты права по иску лица. право которого нарушено. Общий срок исковой давности установлен в три года. Для отдельных видов требований законом могут устанавливаться специальные сроки исковой давности, сокращенные или более длительные по сравнению с общим сроком. Исковая давность, в частности, не распространяется на требования вкладчиков к банку о выдаче вкладов.',
     'Коммерческие банки':'Частные и государственные банки, осуществляющие универсальные операции по кредитованию промышленных, торговых и других предприятий, главным образом за счет тех денежных капиталов, которые они получают в виде вкладов.',
     'Лизинг':'Представляет собой специальную форму финансовых вложений на приобретение оборудования, товаров длительного пользования или недвижимого имущества. Участниками лизинговых операций являются, как правило, три стороны: предприятие - производитель объекта лизинга; лизинговая компания - арендодатель; а также предприятие - арендатор (лизингополучатель).',
     'Налог':'Обязательный, индивидуально безвозмездный платеж, взимаемый с организаций и физических лиц в форме отчуждения принадлежащих им на праве собственности, хозяйственного ведения или оперативного управления денежных средств, в целях финансового обеспечения деятельности государства и (или) муниципальных образований. Признаки налога: принудительный характер; безвозмездность; безэквивалентность.',
     'Овердрафт':'Отрицательный баланс на текущем счете клиента, приобретающий иногда статус кредита, т.е. форма краткосрочного кредита предоставление которого осуществляется списанием средств по счету клиента банком сверх остатка средств на счете, в результате чего образуется дебетовое сальдо. При овердрафте в погашение задолженности направляются все суммы зачисляемые на текущий счет клиента поэтому объем кредита изменяется по мере поступления средств, что отличает овердрафт от обычных ссуд. Проценты взимаются по существующим или согласованным ставкам.',
     'Опцион':'Право выбора способа исполнения обязательства предоставляемое одной из сторон договора, его условиями или право отказа от исполнения обязательства при определенных условиях.',
     'Опционный заём':'Заем с опционом форма займа или долгового обязательства при ко тором кредитору в определенных пределах предоставляется право выбора погашения.',
     'Оферта':'Формальное предложение определенному лицу заключить сделку с указанием всех необходимых для ее заключения условий.',
     'Пассивы':'Обязательства (за исключением субвенций дотации собственных средств и других источников) предприятия состоящие из заемных и привлеченных средств включая кредиторскую задолженность.',
     'Полис':'Документ страхового органа подтверждающий наличие заключенной сделки о страховании.',
     'Пошлины':'Денежные суммы которые взимаются специально уполномоченными учреждениями за совершенные действия в пользу пред приятии или частных лиц.',
     'Резервы':'Часть финансовых ресурсов которая предназначена для финансирования потребностей, возникающих непредвиденно и направленные как на простое, так и на расширенное воспроизводство и потребление. Страховые резервы - часть финансовых ресурсов направленная на возмещение ущерба по страховым случаям. Страховые финансовые резервы - финансовые резервы страховых компаний. Эти резервы необходимы когда текущих средств не хватает на выплаты.',
     'Рубль':'Валюта Российской Федерации, законное платежное средство обязательное к приему по нарицательной стоимости на всей территории Российской Федерации.',
     'Финансы':'Совокупность объективно обусловленных экономических отношений, имеющих распределительный характер, денежную форму выражения и материализуемых в денежных доходах и накоплениях, формируемых в руках государства и субъектов хозяйствования для целей расширенного воспроизводства, материального стимулирования работающих, удовлетворение социальных и других потребностей. Условием функционирования финансов является наличие денег, а причиной появления финансов служит потребность субъектов хозяйствования и государства в ресурсах, обеспечивающих их деятельность.',
     'Фьючерс':'Стандартный договор на поставку товара в будущем по цене, определенной сторонами при совершении сделки.',
     'Чек':'Ценная бумага, содержащая ничем не обусловленное распоряжение чекодателя банку произвести платеж указанной в нем суммы. В качестве плательщика по чеку может быть указан только банк, где чекодатель имеет средства, которыми он вправе распоряжаться путем выставления чеков. Отзыв чека до истечения срока для его предъявления не допускается. Выдача чека не погашает денежного обязательства, во исполнение которого он выдан. Форма чека и порядок его заполнения определяются законом и установленными в соответствии с ним банковскими правилами.',
     'Юридическое лицо':'Организация, которая имеет в собственности, хозяйственном ведении или оперативном управлении обособленное имущество и отвечает по своим обязательствам этим имуществом, может от своего имени приобретать и осуществлять имущественные и иные неимущественные права, нести обязанности, быть истцом и ответчиком в суде. Юридические лица должны иметь самостоятельный баланс или смету и быть зарегистрированы в качестве юридического лица. Юридическими лицами могут быть организации, преследующие извлечение прибыли в качестве основной цели своей деятельности (коммерческие организации) либо не ставящие извлечение прибыли в качестве такой цели и не распределяющие полученную прибыль между участниками (некоммерческие организации).',
     'Брокер':'Профессиональный участник рынка ценных бумаг, оказывающий услуги по исполнению поручения клиента (в том числе эмитента эмиссионных ценных бумаг при их размещении) на совершение гражданско-правовых сделок с ценными бумагами и (или) на заключение договоров, являющихся производными финансовыми инструментами.',
     'Волатильность':'Индикатор рынка ценных бумаг или валюты, показывающий уровень его изменчивости в определенный период.',
     'Дивиденды':'Часть прибыли акционерного общества, распределяемая между его участниками в соответствии с количеством и видом принадлежащих им обыкновенных и привилегированных акций.',
     'Ликвидность':'Способность активов быть быстро проданными с минимальными денежными потерями, связанными со скоростью реализации.',
     'Маржа':'Разница между ценой и себестоимостью (аналог понятия прибыль). Может быть выражена как в денежных единицах, так и в процентах, как отношение разницы между ценой и себестоимостью к цене (в отличие от торговой наценки, которая вычисляется как та же самая разница по отношению к себестоимости).',
     'Репо':'Договор купли-продажи ценных бумаг с обязательством обратного выкупа.',
     'Спот':'Условия расчетов, при которых оплата по сделке производится немедленно (как правило, в течение двух дней).',
     'Своп':'Финансовый контракт, по которому стороны соглашаются на обмен чистыми выплатами в течение определенного периода.',
     'Процентный своп':'обмен платежей по плавающей и фиксированной процентным ставкам',}

slovar_temp = sorted(slovar_unsorted.items())
slovar = dict(slovar_temp) #отсортированый словарь
books = ['«Девушка с деньгами. Книга о финансах и здравом смысле», Анастасия Веселко',
        '«Сам себе финансист. Как тратить с умом и копить правильно», Анастасия Тарасова',
        '«Любить. Считать. Как построить крепкие и здоровые отношения на основе финансовой независимости», Светлана Шишкин',
        '«Правила инвестирования Уоррена Баффетта», Джереми Миллер',
        '«Разумный инвестор», Бенджамин Грэм',
        '«Глобальное распределение активов», Меб Фабер',
        '«Деньги без дураков», Александр Силаев',
        '«Из ряда вон! Как зарабатывать на альтернативных инвестициях», Жеральд Отье',
        '«Рыночные циклы. Как выявлять и использовать закономерности для успешного инвестирования», Говард Маркс',
        '«Когда плохо — это хорошо. Как зарабатывать на инвестиционных идеях», Исаак Беккер',
        '«Богатый Папа, бедный Папа»,Роберт Кийосаки',
        '«Думай и богатей», Наполеон Хилл',
        '«Азбука финансовой грамотности», Владимир Авденин',
        '«Как составить личный финансовый план и как его реализовать», Владимир Савенок',
        '«Правила инвестирования Уоррена Баффетта», Джереми Миллер']

vvod = None
key_slovar = None
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
similar(vvod, key_slovar)  # сравнивает ввод пользователя с ключом словаря и выводит десятичное число
similar("Apple", "Appel")  # выдаст 0.8 - 80% схожести 2 строк.