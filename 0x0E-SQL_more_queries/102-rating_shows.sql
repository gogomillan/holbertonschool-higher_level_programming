-- Script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Select sum left join group by and order by
SELECT ts.title, Sum(tsr.rate) AS rating
FROM   tv_shows ts LEFT JOIN tv_show_ratings tsr
  ON   tsr.show_id = ts.id
GROUP BY ts.title
ORDER BY Sum(tsr.rate) DESC ;
