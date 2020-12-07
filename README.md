# Market Basket Analysis
> *Market basket analysis is a key technique of Association rule mining used by large retailers to uncover associations between items in transactions. Example customer who purchased bread are also likely to purchase jam, customers who purchased laptop were likelihood to purchase laptop bag as well. In short it is technique where different items are revealed from others that which items are bought together. <br>
So that marketing and sales tactics can be improvised.*<br>

**Frequent Pattern in Market Basket Analysis**<br>
It is of two types Itemsets and Sequential Pattern <br>
**Itemsets** : is where items are purchased may be in irregular order but in repetitive order, e.g milk & bread. So the salesmen can arrange these two items nearby or with the great offers to target audience. <br>
**Sequential Pattern** : is where the items are purchased in regular order, e.g Laptop & Laptop bag or Computer & Antivirus here the order does matter because customer will not purchase antivirus first then Computer so salesmen can arrange these two product far from other and use this space to place other exciting offers. <br>

Association rule mining has three main matrices - Support, Confidence, Lift
Suppose A is item and B is another item ;   <br>
A -> B [Support = 20%, Confidence = 60%, Lift = 1.8]; <br>
implies “if” A is bought “then” B is also bought. <br>

**Support** : <ins>Supp(AUB)</ins><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N  <br>
It is frequency of the items bought from all given records. It can filter out items that are bought less frequently.
For the above instance it can be considered as items A & B are purchased together in 20% of all the transactions.<br>

**Confidence** : <ins>Supp(AUB)</ins><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Supp(A)  <br>
It tells us how often product A,B bought together given number times A  occurs, with the help of this we can filter out the products are barely purchased alone like it was unable to filter out in “Support”.
For the above instance it can be considered as transactions in 60% of product A is bought, product B is also bought.<br>

**Lift** : &nbsp;&nbsp;<ins>Supp(AUB)</ins><br>
&nbsp;&nbsp;&nbsp;&nbsp;Supp(A) x Supp(B)  <br>
It finds the independent occurence probability of A & B (also A->B & B->A) and not like "Support" where direction is one (A->B) as the confidence may vary between two.
For the above instance lift = 1.5 indicates the value that product B is more likely get to be purchased when product A is bought. Lift value more than 1 indicates more likely the product B is to be purchased and vice versa.

**Apriori Algorithm** :<br>
It is used to find frequent individual items in database and extending them to larger item sets.
Strong or weak trend with objects/items which are associated with each other can be identified using appropriate threshold for support and confidence.<br>
Features - it is easy to understand and can be parallelized <br>
Limitations - it may need to find large number of rules which can be computationally expensive as it has to go through whole dataset.
