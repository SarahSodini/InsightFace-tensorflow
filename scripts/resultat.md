Vår significance level är alpha = 0.05 (säger vi). 
För KS-test beräknar vi vårt critical value C med detta alpha, och om KS-statistic blir större än C bör vi avfärda nullhypotesen. Om p-värdet är mindre än vårt alpha stödjer det också att vi bör avfärda nullhypotesen. 

# KS:
### All:
    * Statistic = 0.2
    * pvalue = 0.9383310279844598
    * statistic_location = 0.87013
    * statistic_sign = -1
	* critical value = 0.5540860454230366 @ alpha = 0.02

### Mixed
	* statistic = 0.4
	* pvalue = 0.873015873015873
	* statistic_location = 0.87013
    * statistic_sign = -1
	* critical value = 0.9597051824376163 @ alpha = 0.02
  
### Uniform 1
	* statistic = 1.0, 
	* pvalue = 0.007936507936507936, 
	* statistic_location = 0.86171, 
	* statistic_sign = -1
	* critical value = 0.9597051824376163 @ alpha = 0.02

### Uniform 3
    * statistic = 1.0
    * pvalue = 0.007936507936507936
    * statistic_location = 0.85829
	* statistic_sign = 1
	* critical value = 0.9597051824376163 @ alpha = 0.02


# Hedges G
### Uniform 1
	* g = 2.979063288207087
  
### Uniform 3
	* g = 3.536677750778214


# Friedman: 
### Unbalanced:
    * statistic = 10.0
	* pvalue = 0.006737946999085469

## Balanced:
	* statistic = 8.400000000000006
	* pvalue = 0.01499557682047766

# Frågor

KS:
- Är det korrekt tänkt?
- Vi kan utläsa att för 'all' jämförelsen som görs mellan samtliga resultat av respektive dataset har en 93.8% chans att komma från samma distribution, vilket vi anser antagligen tyder på att modellerna inte skiljer sig speciellt mycket beroende på vilket dataset de är tränade på. 
- utvärderar man standardavvikelsena på samma sätt eller behöver vi göra ett annat statistiskt test?
- Vad innebär alfa, och hur väljer man alfa?
- På wikipedia står det att nollhypotesen avfärdas om följande gäller för stora n och m: ![alt text](image.png) Vad gills som stora n och m?

Friedman:
- är det korrekt tänkt att samples för varje test är de olika resultaten från mixed, uniform 1 och 3?
- Utifrån pvalue som är < 0.05, borde nullhypotesen rejectas att mean F1 score är samma för alla evaluationsdataseten. Dvs vi har tillräckligt mycket bevis för att datat som vi evaluerar dataseten på har en påverkan på modellens accuracy, dvs modellen presterar olika bra på de olika evalueringsdataseten. 

Kommentar under tabell 3.2.3:
- Vi har sett till att varje person bara finns med i antingen traininng, validation eller test dataseten. Det är dock så att i test och validation datasetten finns det personer som både är med i mixed och i uniform1/uniform3. Är detta ett stort problem? Vi kommer nog inte hinna ändra på det, utan får väll skriva om det som en felkälla isåfall. 

Om CNN-delen (2.2.1.1) under background:
- Behöver vi ens ha med den delen. Vi har typ bara med den delen för att ArcFace är en CNN och vi refererar till att ArcFace är ett CNN. Hur djupt behöver vi gå in på ArcFace, hur den funkar etc.?
- Svar: Vad är egenskaperna hos cnn som gör den bra för facial recognition/bilder i allmänhet. 


Cohens d, mäter skillnaden mellan de som har pvärde < 0.05, dvs ska göras bara på uniform 1 och 3
Pvärde är bra för att om det finns en skillnad, cohens d mäter om det är en stor skillnad eller inte. Får man ett litet cohens d, typ 0.1, så kan man säga att skillnaden inte är signifikant. 