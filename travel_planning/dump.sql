--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: destination; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.destination (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    location character varying(150) NOT NULL,
    description text,
    likes integer,
    image character varying(255),
    user_id integer NOT NULL,
    "timestamp" timestamp without time zone NOT NULL
);


ALTER TABLE public.destination OWNER TO postgres;

--
-- Name: destination_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.destination_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.destination_id_seq OWNER TO postgres;

--
-- Name: destination_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.destination_id_seq OWNED BY public.destination.id;


--
-- Name: travel_package; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.travel_package (
    id integer NOT NULL,
    name character varying(100),
    description text,
    location character varying(150),
    hotel character varying(100),
    hotel_description text,
    duration character varying(100),
    package_price double precision,
    latitude character varying(50) NOT NULL,
    longitude character varying(50) NOT NULL
);


ALTER TABLE public.travel_package OWNER TO postgres;

--
-- Name: travel_package_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.travel_package_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.travel_package_id_seq OWNER TO postgres;

--
-- Name: travel_package_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.travel_package_id_seq OWNED BY public.travel_package.id;


--
-- Name: travel_package_image; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.travel_package_image (
    id integer NOT NULL,
    filename character varying(255),
    travel_package_id integer NOT NULL
);


ALTER TABLE public.travel_package_image OWNER TO postgres;

--
-- Name: travel_package_image_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.travel_package_image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.travel_package_image_id_seq OWNER TO postgres;

--
-- Name: travel_package_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.travel_package_image_id_seq OWNED BY public.travel_package_image.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(100) NOT NULL,
    email character varying(150) NOT NULL,
    password_hash character varying(255) NOT NULL
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_id_seq OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: user_image; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_image (
    id integer NOT NULL,
    user_id integer NOT NULL,
    image_path character varying(255) NOT NULL
);


ALTER TABLE public.user_image OWNER TO postgres;

--
-- Name: user_image_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_image_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_image_id_seq OWNER TO postgres;

--
-- Name: user_image_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_image_id_seq OWNED BY public.user_image.id;


--
-- Name: wished_holiday; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.wished_holiday (
    id integer NOT NULL,
    holiday_type character varying(50) NOT NULL,
    travel_duration integer NOT NULL,
    price_range character varying(100) NOT NULL,
    travel_time character varying(100) NOT NULL,
    departure_location character varying(100) NOT NULL,
    additional_info text,
    user_id integer NOT NULL
);


ALTER TABLE public.wished_holiday OWNER TO postgres;

--
-- Name: wished_holiday_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.wished_holiday_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.wished_holiday_id_seq OWNER TO postgres;

--
-- Name: wished_holiday_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.wished_holiday_id_seq OWNED BY public.wished_holiday.id;


--
-- Name: destination id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.destination ALTER COLUMN id SET DEFAULT nextval('public.destination_id_seq'::regclass);


--
-- Name: travel_package id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.travel_package ALTER COLUMN id SET DEFAULT nextval('public.travel_package_id_seq'::regclass);


--
-- Name: travel_package_image id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.travel_package_image ALTER COLUMN id SET DEFAULT nextval('public.travel_package_image_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: user_image id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_image ALTER COLUMN id SET DEFAULT nextval('public.user_image_id_seq'::regclass);


--
-- Name: wished_holiday id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wished_holiday ALTER COLUMN id SET DEFAULT nextval('public.wished_holiday_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
89eb4d278caa
\.


--
-- Data for Name: destination; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.destination (id, name, location, description, likes, image, user_id, "timestamp") FROM stdin;
1	potobelo gym	london ,portebello area	i was fun and busy but great staff	0	static/images\\destinations\\be9d04092510e3f6ae4cf1e5a3369b40OIG.VZF.jpeg	1	2024-02-21 13:05:09.880599
\.


--
-- Data for Name: travel_package; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.travel_package (id, name, description, location, hotel, hotel_description, duration, package_price, latitude, longitude) FROM stdin;
1	a romantic city	"The City of Lights offers iconic landmarks like the Eiffel Tower, the Louvre Museum, and the Notre Dame Cathedral. Indulge in delicious cuisine, charming cafes, and a romantic atmosphere. // Paris is renowned for its rich cultural heritage, boasting world-class art collections and historical monuments at every turn. Take a leisurely stroll along the Seine River and admire the elegant bridges that adorn its banks. Explore the vibrant neighborhoods of Montmartre, Marais, and Saint-Germain-des-Prés, each with its own unique charm and character. Don't miss the opportunity to experience the lively atmosphere of a traditional Parisian market, where you can sample fresh produce, artisanal cheeses, and fragrant flowers. Venture beyond the city center to discover hidden gems like the enchanting gardens of Versailles or the quaint village of Montmartre, immortalized by artists like Picasso and Van Gogh. Whether you're a history buff, a food enthusiast, or simply a lover of beauty, Paris offers something to enchant and delight every visitor."	Paris, France 	Le Royal Monceau - Raffles Paris (5*)	Step inside a masterpiece at the heart of the City of Light. Poised majestically in the shadow of the Arc de Triomphe, Le Royal Monceau is not just a luxury hotel but a legend that has played host to the greats of history. Daringly redesigned by Philippe Starck, this Parisian icon is just a stone's throw from the world's most famous avenue, the Champs Elysées. We invite you to experience an oasis of refinement and unrivalled service.	4 nights	700	48.8566	2.3522
2	a Historic Experiance	"Immerse yourself in history and culture with the Colosseum, the Trevi Fountain, and the Vatican City. Savor authentic Italian pasta, pizza, and gelato. // Explore the charming streets of Rome, adorned with ancient ruins and Renaissance architecture. Marvel at the grandeur of St. Peter's Basilica and the intricate artwork of the Sistine Chapel. Indulge in the vibrant atmosphere of lively piazzas and bustling markets. Discover the rich heritage and iconic landmarks that make Rome a timeless destination for travelers from around the world."	Rome, Italy 	Hotel Hassler Roma (5*)	Historic hotel with rooftop terrace overlooking Piazza Trinità dei Monti and Spanish Steps // Hassler Roma is the perfect residence of choice for those seeking the best place to stay in Rome's City Center, near the Spanish Steps, Piazza di Spagna and the Trevi Fountain. Our 87 individually decorated rooms and suites offer city or garden views as well as many other amenities including high speed Internet connection, Wi Fi access and much more at our luxury Rome hotel.	5 nights	500	41.9028	12.4964
3	greatest cosmopolitan city	"Experience Buckingham Palace, Big Ben, and the Tower of London. Enjoy classic afternoon tea, explore vibrant neighborhoods, and catch a West End show. // Dive into the rich history of London with visits to iconic landmarks such as Westminster Abbey and the British Museum. Wander along the banks of the River Thames and marvel at the modern architecture of the Shard. Delve into London's diverse culinary scene, from traditional fish and chips to Michelin-starred fine dining. Immerse yourself in the city's cultural tapestry, with world-class museums, galleries, and theaters at every turn. Discover the unique blend of old-world charm and contemporary innovation that makes London one of the most dynamic cities in the world."	London, England	The Savoy (5*)	Renowned luxury hotel with iconic Art Deco design, steps from Covent Garden, The Savoy is perfectly located on the River Thames, in the heart of all that London has to offer. At the forefront of the luxury hotel scene for over 130 years, The Savoy offers guests an experience that continuously evolves to meet the desires of the modern traveller.	5 nights	1200	51.5074	0.1278
4	Broadway Shows and landmarks	"The Big Apple boasts Times Square, the Statue of Liberty, and Central Park. Witness Broadway musicals, sample diverse cuisines, and soak in the city's energy.// Explore the vibrant neighborhoods of Manhattan, Brooklyn, and Queens, each with its own unique character and charm. Take a stroll along the High Line, an elevated park offering stunning views of the city skyline. Discover world-class art at the Metropolitan Museum of Art and the Museum of Modern Art. Indulge in New York's legendary food scene, from classic New York-style pizza to trendy rooftop bars. Experience the city's rich cultural diversity through festivals, parades, and street performances. From the iconic skyscrapers of Midtown to the historic brownstones of Greenwich Village, New York offers endless opportunities for exploration and adventure."	New York City, USA 	The Plaza (5*)	Iconic hotel with Central Park views, known for its Eloise Suite and afternoon tea, Since its debut on October 1, 1907, The Plaza Hotel has remained a New York icon hosting world leaders, dignitaries, captains of industry, Broadway legends, and Hollywood royalty. As an established staple for lavish society affairs and blockbuster films, The Plaza has welcomed guests from around the world to enjoy its magic at the castle on Central Park South for more than 100 years. Ideally situated on Fifth Avenue, The Plaza’s prestigious address continues to define elegance with unmatched service and an ever-evolving modern sensibility.	4 nights	1100	40.7128	74.0060
5	Festivals and Street Parties	"Marvel at Antoni Gaudí's architectural masterpieces like Sagrada Familia and Park Güell. Relax on Barceloneta beach, explore the Picasso Museum, and savor tapas. Wander through the enchanting streets of the Gothic Quarter, where medieval history meets modern flair. // Take in panoramic views of the city from Montjuïc Hill or Tibidabo Mountain. Dive into Barcelona's vibrant nightlife scene, with trendy bars and clubs lining the streets of El Raval and El Born. Experience the passion of flamenco at a traditional tablao or catch a live music performance at one of the city's many venues. Immerse yourself in Catalan culture with visits to local markets, where you can sample regional delicacies and browse handmade crafts. From the bustling Ramblas to the serene gardens of Park de la Ciutadella, Barcelona offers a perfect blend of history, culture, and Mediterranean charm."	Barcelona, Spain	Hotel Arts Barcelona (5*)	Overlooking Barceloneta Beach and Barcelona city center, this design hotel has 2 outdoor pools and luxury spa with city views. Hotel Arts offers art collection and a restaurant with 2 Michelin stars. The Arts is located next to Barcelona’s Olympic Port and surrounded by shops and lively bars. Barceloneta Beach is 820 feet away, while Ciutadella Park is 984 feet away. The Arts Hotel’s rooms include a flat-screen TV and sound system. The bathrooms have a separate bath and a shower. The hotel’s Enoteca restaurant, awarded 2 Michelin stars, serves fine Mediterranean cuisine. The property includes a number of other bars and restaurants, including a pool-side bar serving light meals in the summer. Hotel Arts has a hair salon and various luxury fashion boutiques. The hotel also offers a multilingual concierge team and a fully equipped business center.	5 nights	500	41.3883	2.1683
6	 Discover Japan	"Discover ancient temples like Senso-ji, experience the vibrant pop culture scene in Akihabara, and enjoy delicious sushi and ramen. Dive into Tokyo's bustling street markets, where you can find everything from traditional handicrafts to cutting-edge gadgets. // Explore the serene gardens of the Imperial Palace and witness the contrast between the city's modern skyscrapers and historic landmarks. Indulge in a sensory overload at Robot Restaurant in Shinjuku, where futuristic performances and neon lights mesmerize audiences. Take a leisurely stroll through the charming streets of Asakusa or Yanaka, where old-world charm meets contemporary trends. Experience the tranquility of traditional tea ceremonies and the thrill of karaoke nights in lively entertainment districts. From the iconic Tokyo Tower to the tranquil shores of Odaiba Beach, Tokyo offers an unforgettable mix of tradition, innovation, and boundless energy."	Tokyo, Japan	Mandarin Oriental, Tokyo (5*)	Mandarin Oriental, Tokyo’s visionary design and award-winning service have been recognized as the epitome of sophisticated luxury in the city. Perfectly situated in Tokyo's prestigious financial district, the first Mandarin Oriental Hotel Group in Japan combines contemporary and time-honoured architectural splendour. The site offers stunning city skyline views and convenient access to banquet and conference facilities in the nearby Mitsui Main Building, a Japanese cultural-heritage property.	5 nights	1000	35.6895	139.6917
7	Maldives Island Paradise	Immerse yourself in luxury and crystal-clear waters on this 7-day escape to the Maldives. Relax on pristine beaches, snorkel vibrant coral reefs, and enjoy overwater bungalows with stunning views.	Maldives (multiple islands)	Soneva Jani (5*)	Luxurious resort with private plunge pools, underwater restaurants, and personalized service.	7 days	6000	4.175	73.508
8	Mountain Retreat	Escape to the serene beauty of the mountains, where majestic peaks and tranquil valleys await. From scenic hikes to cozy fireside chats, immerse yourself in the peace and tranquility of nature.//	 "Mountain Getaways"	Alpine Lodge Retreat	"Experience alpine serenity at Alpine Lodge Retreat. Nestled amidst towering peaks, our lodge offers rustic charm, panoramic views, and warm hospitality that will make you feel right at home."	5 days	1300	47.6062	122.3321
9	Grand Canyon National Park Explorer	Experience the awe-inspiring beauty of the Grand Canyon on this 5-day adventure. Hike along scenic trails, learn about the geology and history, and enjoy breathtaking views.	Grand Canyon National Park, Arizona, USA	El Tovar Hotel (4*)	Historic hotel with stunning canyon views, comfortable rooms, and excellent dining options.	5 days	2000	36.114	-112.111
10	Bora Bora Honeymoon Escape	Escape to paradise on this romantic 7-day getaway to Bora Bora. Stay in luxurious overwater bungalows, relax on white-sand beaches, and enjoy unforgettable experiences like swimming with stingrays and exploring coral gardens.	Bora Bora, French Polynesia	Conrad Bora Bora Nui (5*)	Luxurious resort with private plunge pools, overwater bungalows, and stunning lagoon views.	7 days	3800	-16.519	-151.733
11	Safari Adventure	Embark on an exhilarating safari adventure into the heart of Africa's wilderness. Encounter majestic wildlife, traverse rugged landscapes, and immerse yourself in the timeless allure of the savannah.	African Safari Camps, South Africa	Savannah Lodge	Experience the thrill of the wild at Savannah Lodge. Our luxury tented camp offers unparalleled safari experiences, including guided game drives, bush walks, and evenings under the African stars.	12 days	2000	-28.557661	29.782084
12	Panama Canal Expedition	Embark on an extraordinary journey through the engineering marvel that is the Panama Canal. Witness colossal ships navigate through the locks, explore lush rainforests teeming with biodiversity, and delve into Panama's rich cultural heritage.	Panama Canal and Surrounding Areas	Canal View Resort	Experience unparalleled luxury and breathtaking views at Canal View Resort. Nestled along the Panama Canal, our resort offers elegant accommodations, world-class amenities, and unrivaled access to one of the world's most iconic waterways.	14 days	2200	9.1018	79.4029
\.


--
-- Data for Name: travel_package_image; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.travel_package_image (id, filename, travel_package_id) FROM stdin;
1	/static/images\\travel_packages\\ef1616c5ecdf178eparis11.jpg	1
2	/static/images\\travel_packages\\06cb2d65b0320bdcparislouvr.jpg	1
3	/static/images\\travel_packages\\b4b72d47e15062e2hotel-le-royal-monceau-raffles-paris.jpg	1
4	/static/images\\travel_packages\\724616b31f2b705dColosseum-Rome-600x400.jpg	2
5	/static/images\\travel_packages\\b328fb6ede554e15Rome_view12.jpg	2
6	/static/images\\travel_packages\\52f748f19e57a896Presidential_suite_Trinita_de_monti_living.jpg	2
7	/static/images\\travel_packages\\17242d75414bfd81london11.jpg	3
8	/static/images\\travel_packages\\8d82f885d135e995london12.jpg	3
9	/static/images\\travel_packages\\8e63b5826f24f610the-savoy-iconic-sign.jpg	3
10	/static/images\\travel_packages\\a057b942af9a3d95nwyork11.jpg	4
11	/static/images\\travel_packages\\23ec4c27c934aee7nwyork12.jpg	4
12	/static/images\\travel_packages\\d17300597d8b8b31the_plaza.jpeg	4
13	/static/images\\travel_packages\\c23ea0d7d5842974barca11.jpg	5
14	/static/images\\travel_packages\\0266159bfbb70287barca12.jpg	5
15	/static/images\\travel_packages\\23beb2bd8414fbeabarca_hotel.jpg	5
16	/static/images\\travel_packages\\cbeb6222a3a2bf6etokyo11.jpg	6
17	/static/images\\travel_packages\\428de400b71012bctokyo12.jpg	6
18	/static/images\\travel_packages\\331b0be671d8cad6tokyo_hotel.jpg	6
19	/static/images\\travel_packages\\3e234c1612820c1cmaldiv11.jpg	7
20	/static/images\\travel_packages\\ad21979f33f89d11maldiv12.jpg	7
21	/static/images\\travel_packages\\c156fb5a92b7b265maldiv13.webp	7
22	/static/images\\travel_packages\\8ad201abb50f5ff8AlpineZLodge11.jpg	8
23	/static/images\\travel_packages\\1839be59df28b8dbAlpineZLodge12.jpg	8
24	/static/images\\travel_packages\\2c5f600b54349b31AlpineZLodge13.jpg	8
25	/static/images\\travel_packages\\b44fe0cf91717e72grandcan11.jpg	9
26	/static/images\\travel_packages\\adbf59761431b308grandcan12.jpg	9
27	/static/images\\travel_packages\\f7937b9b87c913adgrandcan13.webp	9
28	/static/images\\travel_packages\\9e9e15fdb919d359borabora11.jpg	10
29	/static/images\\travel_packages\\3feb5b4e7d348afbborabora12.jpg	10
30	/static/images\\travel_packages\\a5be077ee024eccaborabora13.jpg	10
31	/static/images\\travel_packages\\57e62d339ad3f84asafari11.webp	11
32	/static/images\\travel_packages\\cabac901e2fd8b07safari12.jpg	11
33	/static/images\\travel_packages\\1abf2fb1920ab1acsafari13.jpg	11
34	/static/images\\travel_packages\\6822591ef372626ePanamaCanal11.jpg	12
35	/static/images\\travel_packages\\c26a2a5c9a8cf759PanamaCanal13.jpg	12
36	/static/images\\travel_packages\\d5756bb18d688d0dPanamaCanal12.jpg	12
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."user" (id, username, email, password_hash) FROM stdin;
1	maisam2004	maisam2004@googlemail.com	$2b$12$c/79rSPuonkjkeYeBqg3hOtV.dviIdtU6B6bz6Wg932bUK0b/EQvy
2	maisam2005	bestman_co2003@hotmail.com	$2b$12$R/5HqBvsQs1PfZOCmlYbt.k70qpLPd6iewfUXo1R7jU/9vSSH2vOO
\.


--
-- Data for Name: user_image; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_image (id, user_id, image_path) FROM stdin;
1	1	E:\\learned\\code_instute\\projects\\travel_planning_project\\travel_planning\\static\\images\\IMG_20230628_220501.jpg
\.


--
-- Data for Name: wished_holiday; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.wished_holiday (id, holiday_type, travel_duration, price_range, travel_time, departure_location, additional_info, user_id) FROM stdin;
2	cultural	5	budget	flexible dates	london	please be so luxury	1
4	beach	9	moderate	jan 2024	london	just cheepest possible	1
\.


--
-- Name: destination_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.destination_id_seq', 1, true);


--
-- Name: travel_package_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.travel_package_id_seq', 12, true);


--
-- Name: travel_package_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.travel_package_image_id_seq', 36, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 2, true);


--
-- Name: user_image_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_image_id_seq', 1, true);


--
-- Name: wished_holiday_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.wished_holiday_id_seq', 4, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: destination destination_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.destination
    ADD CONSTRAINT destination_pkey PRIMARY KEY (id);


--
-- Name: travel_package_image travel_package_image_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.travel_package_image
    ADD CONSTRAINT travel_package_image_pkey PRIMARY KEY (id);


--
-- Name: travel_package travel_package_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.travel_package
    ADD CONSTRAINT travel_package_pkey PRIMARY KEY (id);


--
-- Name: user user_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user_image user_image_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_image
    ADD CONSTRAINT user_image_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- Name: wished_holiday wished_holiday_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wished_holiday
    ADD CONSTRAINT wished_holiday_pkey PRIMARY KEY (id);


--
-- Name: destination destination_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.destination
    ADD CONSTRAINT destination_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: travel_package_image travel_package_image_travel_package_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.travel_package_image
    ADD CONSTRAINT travel_package_image_travel_package_id_fkey FOREIGN KEY (travel_package_id) REFERENCES public.travel_package(id);


--
-- Name: user_image user_image_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_image
    ADD CONSTRAINT user_image_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: wished_holiday wished_holiday_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.wished_holiday
    ADD CONSTRAINT wished_holiday_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- PostgreSQL database dump complete
--

