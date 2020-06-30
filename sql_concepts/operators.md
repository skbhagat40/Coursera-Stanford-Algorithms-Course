SQL OVER clause - 
Return a running count, 
can be used when I need total count of items after a group by query.
It supports partition also, 
example - 
```
 """
            SELECT a.#{col_name}, a.count, SUM(a.count) OVER() as total_count FROM
            (
            SELECT CAST(#{col_name} AS DATE), COUNT(*) AS
            count
            FROM #{table_name}
            WHERE #{col_name} BETWEEN '#{start_date}' AND '#{end_date}'
            AND #{secondary_col_name} = #{aff_id}
            GROUP BY CAST(#{col_name} AS DATE)
            )  a
            """
```
Concepts used here - getting results from another query and getting addional data on top of it, use subqueries FROM(subquery) alias.
Here, after I get the results after group by , I am using SUM(a.count) OVER() to get the running total of sum of counts returned by group by.

# I guess it's called window function in sql??
# learn about self joins in sql.

links - https://stackoverflow.com/questions/6218902/the-sql-over-clause-when-and-why-is-it-useful
https://stackoverflow.com/questions/39579224/using-group-by-and-over
