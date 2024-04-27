import pandas as pd
#import pandas library and alias it as pd

file1 = pd.read_excel("excelfile.xlsx")
file2 = pd.read_excel("excelfile2.xlsx")
#i load 2 excel file(excelfile.xlsx and excelfile2.xlsx) using pd.read_excel() funtion.

file1_col = file1[['First Name', 'Last Name']]
file2_col = file2[['ID', 'Company ID']]
# i initilize file1_col and file2_col into there corresponding files(file1, file2) and index there columns[First Name, Last Name] and
#[ID, Company ID] when pertaining index its case sensitive so make sure that the column name is exactly called

file1_col.reset_index(drop= True, inplace= True)
file2_col.reset_index(drop= True, inplace= True)
# i use rest_index here with parameter drop= True and inplace =True. so i can reset index when i do the concatenation
# the index will not have duplicate indices.

con = pd.concat([file1_col, file2_col], axis=1)
# pd.concat() funtion is use to combine 2 DataFrame(file1_col, file2_col) axis=1 making them sort from top to bottom.
# and i initilize it to a new variable name(con)

a = pd.DataFrame(con)
# i can then now prin con here but instead i put it in a DataFrame() function to make it DataFrame and then initialize it
#to variable name (a)

print(a.to_string())
# i printed (a) here and added to_string() funtion to make the entire DataFrame show

# here is the final output of to file that i joined together they are from different columns:
# file1(excelfile.xlsx) with column [First Name, Last Name]
# file2(excelfile1.xlsx) with column [ID, Company ID]

'''
      First Name    Last Name   ID  Company ID
0        Lindsay       Holden  111          17
1        Anushka       Wilcox  222          11
2        Bernard     Gonzalez  333         214
3           Jody      Bentley    4           7
4        Theresa      Sampson    5          12
5        Killian       Irvine    6           7
6           Siya      Murillo    7          14
7          T-Jay    Blackmore    8          16
8         Andrea         Adam    9           2
9          Macey      Harrell   10           5
10         Nigel         Kane   11           5
11         Falak         Diaz   12           6
12         Karen      Watkins   13           5
13        Sachin        Curry   14           8
14        Kelsie       Pearce   15          12
15       Areebah       Morris   16          16
16         Mared   Pennington   17          10
17     Kristofer     Portillo   18           9
18         Rhona        Heath   19          13
19          Roan        Joyce   20           7
20        Verity      Simmons   21          15
21        Jasper      Francis   22          11
22         Lilly       Mcleod   23          18
23          Jobe       Wooten   24           6
24           Mac     Christie   25          17
25          Toni       Kramer   26          10
26        Gracie    Pemberton   27          16
27         Angel        Giles   28           6
28          Sade        Povey   29          13
29        Daphne        Lynch   30          12
30          Zaki       Finney   31          11
31       Faizaan      Sanchez   32           4
32         Lubna      Vazquez   33          20
33         Traci     Whiteley   34           2
34         Pippa    Velasquez   35           1
35       Alessio      Lindsey   36           7
36        Caolan        Knott   37          19
37            Zi     Calderon   38          12
38        Hallie     Mcarthur   39           8
39          Glen         Long   40           7
40         Bodhi       Gamble   41          14
41          Sean        Bloom   42          13
42        Haidar   Strickland   43           8
43         Keith        Munro   44           9
44        Kishan       Patton   45           1
45        Carrie       Waller   46           8
46       Suleman     Delacruz   47           9
47          Reef         Howe   48           6
48        Damien      Ellwood   49          16
49          Elif      Wiggins   50          19
50       Lincoln      Mueller   51          10
51      Veronica      Ventura   52          19
52          Cali      Richard   53          18
53    Franciszek    Underwood   54          16
54         Fahad      Chester   55           1
55        Jadine      Dejesus   56           9
56           Dev      Bernard   57          19
57      Anoushka      Justice   58          14
58          Elle       Franks   59          17
59         Izzie         Phan   60           9
60         Ferne       Jordan   61          13
61        Gloria       Dunlop   62          15
62      Annabell        Miles   63          18
63          Reem         Peck   64          14
64       Izabela       Howell   65          12
65          Alec     Driscoll   66           4
66        Arisha        Whyte   67           3
67           Eva         Cote   68          13
68      Abigayle        Berry   69          13
69         Elora      Mullins   70           3
70         Kelsi          Guy   71          18
71        Harlan      Medrano   72          12
72          Taya       Golden   73          19
73        Aniyah        Regan   74           6
74        Emelia    Donaldson   75          18
75       Jessica         Cobb   76          19
76         Mario        Stein   77           2
77         Luisa      Dunkley   78          20
78       Chelsea        Young   79           5
79      Muhammed      Pollard   80           5
80        Shanay        Reyna   81           5
81        Caelan    Mcdonnell   82           7
82         Tayla         Nava   83          20
83         Mehdi         Frey   84          16
84        Elysia       Miller   85           5
85         Drake       Macias   86           3
86        Ebonie       George   87           1
87        Israel     Cottrell   88           9
88      Vladimir        Trejo   89           9
89       Dainton       Palmer   90          11
90       Mitchel      Randall   91          11
91       Timothy      Coulson   92           2
92      Cataleya       Forbes   93           8
93        Amelia       Bowler   94          17
94         Anand         Soto   95          11
95         Kaine         Bell   96           7
96     Lilly-Ann     Drummond   97          10
97        Kellie     Atkinson   98           1
98        Juliet    Mccaffrey   99           8
99      Zakariah       OBrien  100           3
100      Luciano     Jennings  101          10
101       Reegan         Chen  102          20
102        Garin      Terrell  103           7
103       Romana       Tucker  104           7
104       Everly     Gonzales  105           3
105         Eren        Short  106           9
106        Ruari    Ratcliffe  107          19
107          Sid      Mendoza  108           7
108        Denis      Russell  109           2
109         Jean        Ayers  110          10
110        Pawel         Dyer  111          11
111         Clay       Ramsay  112           4
112         Sila        Klein  113           7
113       Harris       Mccann  114           6
114       Zander        Curry  115           4
115        Sadia       Lister  116          14
116     Dominick       Flores  117           9
117        Gwion         Kerr  118          10
118        Paddy      Mueller  119          14
119       Melisa        Marsh  120           6
120         Roan     Copeland  121           2
121         Hina   Farrington  122          13
122          Kay       Morris  123           7
123       Zainab     Finnegan  124           4
124      Natalya       Mcphee  125          13
125         Olly        Avila  126           1
126        Tadhg     Mcarthur  127          16
127        Willa        Hayes  128           5
128        Khloe        Byers  129          10
129         Saim       Turner  130          13
130      Ava-Mai      Simpson  131           6
131        Damon        Ponce  132          18
132        Anish    Mcdonnell  133          20
133      Roberta       Newman  134          13
134        Chris       Walker  135           7
135     Angelina         Wong  136          19
136        Inaya      Mcbride  137          18
137         Gino    Mcfarlane  138           8
138         Ifan      Aguirre  139          16
139        Arnas      Krueger  140           5
140       Calvin    Humphries  141           5
141      Clarice   Williamson  142          16
142         Sara          Ray  143          16
143         Noel     Saunders  144           5
144        Benas       Morrow  145           2
145        Abiha        Hawes  146           9
146        Anais    Goldsmith  147          16
147          Jak        Sykes  148           5
148      Tatiana      Buckner  149           9
149         Tess       Butler  150           4
150        Rocco      Herrera  151           9
151     Jeanette     Randolph  152          16
152       Eloisa       Ibarra  153          12
153        Rehan      Emerson  154          19
154      Mikaela     Trujillo  155          19
155        Drake       Rhodes  156           9
156        Homer      Hayward  157           3
157   Jayden-Lee        Brock  158          13
158        Loren   Wainwright  159          16
159       Haroon        Olson  160           7
160        Darci        Pratt  161          20
161          Ria       Ritter  162           2
162       Jerome    Dickinson  163           2
163      Russell        Cline  164           8
164         Lila       Easton  165          16
165         Rudy         Soto  166           9
166      Indiana        Nairn  167          18
167       Jenson  Worthington  168           3
168        Phebe       Cannon  169          20
169        Tiana      Mansell  170           7
170       Lauren        Ortiz  171           4
171       Sanaya       Obrien  172           3
172        Imaan   Pennington  173          20
173      Kirstin     Gardiner  174           3
174       Mollie          May  175           2
175         Amin       Bonner  176          11
176       Horace        Hicks  177          20
177      Herbert    Rasmussen  178          13
178        Tamia     Mcgregor  179          19
179        Taryn      Camacho  180          14
180       Hester         Carr  181          19
181        Alyce         Horn  182           8
182       Elicia        Davie  183           9
183       Arslan   Valenzuela  184           9
184        Elina       Acosta  185           8
185        Tylor       Fowler  186           5
186        Aariz      Vickers  187           7
187       Kirsty         Hume  188          17
188        Cosmo        Reese  189           9
189      Tristan      Morales  190          19
190      Leilani           Yu  191          14
191        Lynda          Lin  192           4
192        Chyna        Busby  193          14
193        Ailsa       Hayden  194           4
194      Crystal         Boyd  195           3
195         Kobe        Costa  196          13
196         Anil       Bolton  197           6
197       Marcia       Heaton  198          16
198       Kacper       Thomas  199           1
199      Adaline      Mohamed  200          18
200      Lindsay       Holden  201           7
201      Anushka       Wilcox  202          11
202      Bernard     Gonzalez  203          11
203         Jody      Bentley  204          10
204      Theresa      Sampson  205           1
205      Killian       Irvine  206          13
206         Siya      Murillo  207          16
207        T-Jay    Blackmore  208           2
208       Andrea         Adam  209           7
209        Macey      Harrell  210          11
210        Nigel         Kane  211          11
211        Falak         Diaz  212          10
212        Karen      Watkins  213           8
213       Sachin        Curry  214          14
214       Kelsie       Pearce  215           7
215      Areebah       Morris  216           6
216        Mared   Pennington  217           1
217    Kristofer     Portillo  218          17
218        Rhona        Heath  219          11
219         Roan        Joyce  220           6
220       Verity      Simmons  221          20
221       Jasper      Francis  222           3
222        Lilly       Mcleod  223           4
223         Jobe       Wooten  224          14
224          Mac     Christie  225           8
225         Toni       Kramer  226          13
226       Gracie    Pemberton  227          19
227        Angel        Giles  228          12
228         Sade        Povey  229          12
229       Daphne        Lynch  230           1
230         Zaki       Finney  231           9
231      Faizaan      Sanchez  232          12
232        Lubna      Vazquez  233          12
233        Traci     Whiteley  234          11
234        Pippa    Velasquez  235          12
235      Alessio      Lindsey  236          16
236       Caolan        Knott  237           8
237           Zi     Calderon  238          10
238       Hallie     Mcarthur  239          15
239         Glen         Long  240           9
240        Bodhi       Gamble  241          19
241         Sean        Bloom  242          15
242       Haidar   Strickland  243          13
243        Keith        Munro  244          14
244       Kishan       Patton  245          13
245       Carrie       Waller  246          13
246      Suleman     Delacruz  247           2
247         Reef         Howe  248           8
248       Damien      Ellwood  249           8
249         Elif      Wiggins  250           9
250      Lincoln      Mueller  251           2
251     Veronica      Ventura  252          11
252         Cali      Richard  253          11
253   Franciszek    Underwood  254           3
254        Fahad      Chester  255           1
255       Jadine      Dejesus  256          17
256          Dev      Bernard  257          14
257     Anoushka      Justice  258          19
258         Elle       Franks  259           3
259        Izzie         Phan  260          19
260        Ferne       Jordan  261          15
261       Gloria       Dunlop  262           2
262     Annabell        Miles  263          13
263         Reem         Peck  264          20
264      Izabela       Howell  265           7
265         Alec     Driscoll  266          19
266       Arisha        Whyte  267           9
267          Eva         Cote  268           9
268     Abigayle        Berry  269           5
269        Elora      Mullins  270          15
270        Kelsi          Guy  271          10
271       Harlan      Medrano  272           2
272         Taya       Golden  273           2
273       Aniyah        Regan  274           4
274       Emelia    Donaldson  275           3
275      Jessica         Cobb  276           1
276        Mario        Stein  277          13
277        Luisa      Dunkley  278           2
278      Chelsea        Young  279          20
279     Muhammed      Pollard  280          19
280       Shanay        Reyna  281           9
281       Caelan    Mcdonnell  282          12
282        Tayla         Nava  283           9
283        Mehdi         Frey  284           2
284       Elysia       Miller  285          14
285        Drake       Macias  286           5
286       Ebonie       George  287           3
287       Israel     Cottrell  288          14
288     Vladimir        Trejo  289           1
289      Dainton       Palmer  290           6
290      Mitchel      Randall  291          14
291      Timothy      Coulson  292           3
292     Cataleya       Forbes  293           1
293       Amelia       Bowler  294          20
294        Anand         Soto  295          18
295        Kaine         Bell  296          13
296    Lilly-Ann     Drummond  297           4
297       Kellie     Atkinson  298          19
298       Juliet    Mccaffrey  299          12
299     Zakariah       OBrien  300           4
300      Luciano     Jennings  301           2
301       Reegan         Chen  302          11
302        Garin      Terrell  303          17
303       Romana       Tucker  304          17
304       Everly     Gonzales  305          10
305         Eren        Short  306          20
306        Ruari    Ratcliffe  307          18
307          Sid      Mendoza  308          14
308        Denis      Russell  309          12
309         Jean        Ayers  310           7
310        Pawel         Dyer  311           6
311         Clay       Ramsay  312           7
312         Sila        Klein  313           6
313       Harris       Mccann  314          16
314       Zander        Curry  315          14
315        Sadia       Lister  316          20
316     Dominick       Flores  317          16
317        Gwion         Kerr  318          11
318        Paddy      Mueller  319          15
319       Melisa        Marsh  320           5
320         Roan     Copeland  321          16
321         Hina   Farrington  322           4
322          Kay       Morris  323          14
323       Zainab     Finnegan  324           6
324      Natalya       Mcphee  325          12
325         Olly        Avila  326          18
326        Tadhg     Mcarthur  327           4
327        Willa        Hayes  328          18
328        Khloe        Byers  329          14
329         Saim       Turner  330          12
330      Ava-Mai      Simpson  331           8
331        Damon        Ponce  332           7
332        Anish    Mcdonnell  333           7
333      Roberta       Newman  334          19
334        Chris       Walker  335          13
335     Angelina         Wong  336           7
336        Inaya      Mcbride  337          16
337         Gino    Mcfarlane  338           1
338         Ifan      Aguirre  339          15
339        Arnas      Krueger  340          20
340       Calvin    Humphries  341           5
341      Clarice   Williamson  342          12
342         Sara          Ray  343          10
343         Noel     Saunders  344           4
344        Benas       Morrow  345           3
345        Abiha        Hawes  346           9
346        Anais    Goldsmith  347          15
347          Jak        Sykes  348           5
348      Tatiana      Buckner  349          19
349         Tess       Butler  350          19
350        Rocco      Herrera  351          13
351     Jeanette     Randolph  352          14
352       Eloisa       Ibarra  353           1
353        Rehan      Emerson  354           8
354      Mikaela     Trujillo  355           4
355        Drake       Rhodes  356           4
356        Homer      Hayward  357          11
357   Jayden-Lee        Brock  358           2
358        Loren   Wainwright  359           7
359       Haroon        Olson  360          13
360        Darci        Pratt  361          18
361          Ria       Ritter  362           3
362       Jerome    Dickinson  363          12
363      Russell        Cline  364           1
364         Lila       Easton  365          19
365         Rudy         Soto  366          17
366      Indiana        Nairn  367          20
367       Jenson  Worthington  368           8
368        Phebe       Cannon  369           5
369        Tiana      Mansell  370           6
370       Lauren        Ortiz  371           1
371       Sanaya       Obrien  372          15
372        Imaan   Pennington  373           6
373      Kirstin     Gardiner  374          20
374       Mollie          May  375           8
375         Amin       Bonner  376           6
376       Horace        Hicks  377           3
377      Herbert    Rasmussen  378          14
378        Tamia     Mcgregor  379          11
379        Taryn      Camacho  380          12
380       Hester         Carr  381          11
381        Alyce         Horn  382          20
382       Elicia        Davie  383           1
383       Arslan   Valenzuela  384           5
384        Elina       Acosta  385           1
385        Tylor       Fowler  386           6
386        Aariz      Vickers  387           1
387       Kirsty         Hume  388           9
388        Cosmo        Reese  389          18
389      Tristan      Morales  390          15
390      Leilani           Yu  391          14
391        Lynda          Lin  392           6
392        Chyna        Busby  393           7
393        Ailsa       Hayden  394           9
394      Crystal         Boyd  395           8
395         Kobe        Costa  396          14
396         Anil       Bolton  397          10
397       Marcia       Heaton  398           5
398       Kacper       Thomas  399           4
399      Adaline      Mohamed  400          15
400       Finbar      Keeling  401           7
401        Ryker       Krause  402           3
402         Izzy         Reed  403           6
403        Rohan         Mair  404           2
404      Camille      Britton  405           5
405        Chyna       Jacobs  406          10
406       Parker      Hartley  407           6
407         Ayla   Cunningham  408           7
408        Karim     Friedman  409          12
409        Denis       Juarez  410          14
410          Mea        Wolfe  411          11
411       Yannis       Orozco  412           2
412        Baran      Brookes  413          11
413         Iman     Matthams  414          12
414   Harvey-Lee     Drummond  415           9
415     Cristina       Turner  416          14
416      Savanna        Morse  417          10
417      Ellesha     Mcdaniel  418           7
418        Shola         Meza  419           9
419      Theresa     Calderon  420          17
420         Zakk       Romero  421           4
421        Meera      Vasquez  422           5
422         Alba       Rivers  423          14
423      Theodor       Harvey  424          17
424     Isla-Mae       OBrien  425          15
425      Ishmael      Markham  426          19
426        Derek       Sutton  427           8
427        Damon       Duncan  428          16
428       Saarah        Kirby  429           5
429         Rubi    Bannister  430          13
430       Aarron      Hampton  431          13
431     Gurpreet       Wooten  432          14
432          Ian     Galloway  433           5
433       Blaine    Christian  434           2
434       Tyrone        Hicks  435           8
435        Dante  Worthington  436          16
436       Teegan       Holder  437           9
437       Alanah     Anderson  438           3
438        Irfan      Redmond  439           1
439         Nico      Schultz  440          13
440        Chaim        Hagan  441           5
441      Eleanor         Hyde  442           1
442        Wayne      Frazier  443           9
443        Kiran       Hollis  444           3
444     Virginia     Marriott  445          14
445     Christos       Taylor  446           6
446         Gaia       Bright  447          18
447      Levison     Rawlings  448           9
448       Dulcie      Carlson  449          11
449      Caitlyn        Avery  450          17
450      Aaminah       Galvan  451          12
451      Ellenor       Osborn  452           6
452         Isla    Lancaster  453          19
453        Danny          Kim  454           3
454        Kenya       Conner  455          18
455       Luther      Barrett  456           4
456       Idrees         Rich  457           4
457      Chester        Dolan  458          17
458  Amelia-Lily      Vazquez  459           4
459        Sofie        Nixon  460           2
460        Mamie        Baker  461          16
461         Abby      Kaufman  462           1
462      Shelley       Feeney  463          12
463      Faizaan         Luna  464          16
464        Kanye        Wilde  465          20
465        Kylie          Bob  466          10
466        Menna     Sharples  467           7
467    Danielius        Reese  468           8
468         Kobi    Frederick  469           9
469         Maud       Barton  470          14
470       Tillie       Keller  471          19
471    Tymoteusz         Rosa  472           2
472       Akshay         Pope  473           6
473       Lynsey       Madden  474           7
474        Roxie       Alford  475           6
475        Umayr      Goddard  476           3
476       Jazmyn        Lewis  477           8
477       Raheel     Marshall  478           9
478        Maddy     Reynolds  479           4
479       Leonie        Wiley  480           4
480       Ignacy      Manning  481          10
481        Kayla        Haley  482          20
482     Rafferty        Hamer  483           4
483        Esmai       Lennon  484          13
484        Korey         Noel  485          15
485       Emilis       Hooper  486          13
486      Candice        Flynn  487           7
487    Nathaniel      Fuentes  488          14
488      Gregory        Yoder  489           3
489      Ammarah        Lyons  490           1
490       Murphy        Sweet  491          19
491      Cassidy        Short  492          12
492     Brittany       Larson  493          15
493         Rian         Mays  494          10
494        Emmie       Alcock  495          20
495       Mikail      Beasley  496          14
496        Diogo      Bradley  497           4
497        Layan       Ashley  498          19
498          Dua     Cisneros  499           5
499      Danyaal    Tomlinson  500          16

Process finished with exit code 0

'''