```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen FROM women_stemDB GROUP BY Major ORDER BY SumTotal DESC LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=3649217, SumWomen=2196311), Row(Major='NURSING', SumTotal=2722122, SumWomen=2439073), Row(Major='COMPUTER SCIENCE', SumTotal=1668147, SumWomen=371488), Row(Major='MECHANICAL ENGINEERING', SumTotal=1185951, SumWomen=141791), Row(Major='ELECTRICAL ENGINEERING', SumTotal=1059851, SumWomen=208208), Row(Major='MATHEMATICS', SumTotal=941161, SumWomen=421733), Row(Major='CHEMISTRY', SumTotal=864890, SumWomen=436891), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=806676, SumWomen=455481), Row(Major='GENERAL ENGINEERING', SumTotal=794976, SumWomen=201097), Row(Major='CIVIL ENGINEERING', SumTotal=690989, SumWomen=156936)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen 
            FROM women_stemDB 
            GROUP BY Major 
            ORDER BY SumTotal DESC 
            LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=3929926, SumWomen=2365258), Row(Major='NURSING', SumTotal=2931516, SumWomen=2626694), Row(Major='COMPUTER SCIENCE', SumTotal=1796466, SumWomen=400064), Row(Major='MECHANICAL ENGINEERING', SumTotal=1277178, SumWomen=152698), Row(Major='ELECTRICAL ENGINEERING', SumTotal=1141378, SumWomen=224224), Row(Major='MATHEMATICS', SumTotal=1013558, SumWomen=454174), Row(Major='CHEMISTRY', SumTotal=931420, SumWomen=470498), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=868728, SumWomen=490518), Row(Major='GENERAL ENGINEERING', SumTotal=856128, SumWomen=216566), Row(Major='CIVIL ENGINEERING', SumTotal=744142, SumWomen=169008)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen 
            FROM women_stemDB 
            GROUP BY Major 
            ORDER BY SumTotal DESC 
            LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=4210635, SumWomen=2534205), Row(Major='NURSING', SumTotal=3140910, SumWomen=2814315), Row(Major='COMPUTER SCIENCE', SumTotal=1924785, SumWomen=428640), Row(Major='MECHANICAL ENGINEERING', SumTotal=1368405, SumWomen=163605), Row(Major='ELECTRICAL ENGINEERING', SumTotal=1222905, SumWomen=240240), Row(Major='MATHEMATICS', SumTotal=1085955, SumWomen=486615), Row(Major='CHEMISTRY', SumTotal=997950, SumWomen=504105), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=930780, SumWomen=525555), Row(Major='GENERAL ENGINEERING', SumTotal=917280, SumWomen=232035), Row(Major='CIVIL ENGINEERING', SumTotal=797295, SumWomen=181080)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen FROM women_stemDB GROUP BY Major ORDER BY SumTotal DESC LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=6175598, SumWomen=3716834), Row(Major='NURSING', SumTotal=4606668, SumWomen=4127662), Row(Major='COMPUTER SCIENCE', SumTotal=2823018, SumWomen=628672), Row(Major='MECHANICAL ENGINEERING', SumTotal=2006994, SumWomen=239954), Row(Major='ELECTRICAL ENGINEERING', SumTotal=1793594, SumWomen=352352), Row(Major='MATHEMATICS', SumTotal=1592734, SumWomen=713702), Row(Major='CHEMISTRY', SumTotal=1463660, SumWomen=739354), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=1365144, SumWomen=770814), Row(Major='GENERAL ENGINEERING', SumTotal=1345344, SumWomen=340318), Row(Major='CIVIL ENGINEERING', SumTotal=1169366, SumWomen=265584)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen 
            FROM women_stemDB 
            GROUP BY Major 
            ORDER BY SumTotal DESC 
            LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=6456307, SumWomen=3885781), Row(Major='NURSING', SumTotal=4816062, SumWomen=4315283), Row(Major='COMPUTER SCIENCE', SumTotal=2951337, SumWomen=657248), Row(Major='MECHANICAL ENGINEERING', SumTotal=2098221, SumWomen=250861), Row(Major='ELECTRICAL ENGINEERING', SumTotal=1875121, SumWomen=368368), Row(Major='MATHEMATICS', SumTotal=1665131, SumWomen=746143), Row(Major='CHEMISTRY', SumTotal=1530190, SumWomen=772961), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=1427196, SumWomen=805851), Row(Major='GENERAL ENGINEERING', SumTotal=1406496, SumWomen=355787), Row(Major='CIVIL ENGINEERING', SumTotal=1222519, SumWomen=277656)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen 
            FROM women_stemDB 
            GROUP BY Major 
            ORDER BY SumTotal DESC 
            LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=6737016, SumWomen=4054728), Row(Major='NURSING', SumTotal=5025456, SumWomen=4502904), Row(Major='COMPUTER SCIENCE', SumTotal=3079656, SumWomen=685824), Row(Major='MECHANICAL ENGINEERING', SumTotal=2189448, SumWomen=261768), Row(Major='ELECTRICAL ENGINEERING', SumTotal=1956648, SumWomen=384384), Row(Major='MATHEMATICS', SumTotal=1737528, SumWomen=778584), Row(Major='CHEMISTRY', SumTotal=1596720, SumWomen=806568), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=1489248, SumWomen=840888), Row(Major='GENERAL ENGINEERING', SumTotal=1467648, SumWomen=371256), Row(Major='CIVIL ENGINEERING', SumTotal=1275672, SumWomen=289728)]
```

