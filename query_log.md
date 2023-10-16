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

