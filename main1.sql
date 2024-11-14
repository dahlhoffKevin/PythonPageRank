USE MediaWiki;

SELECT page_title, COUNT(pagelinks.pl_from)
  FROM 
    page
  JOIN pagelinks ON page_id = pl_from
  GROUP BY 
    pl_from;

SELECT page_title, COUNT(pagelinks.pl_from)
  FROM 
    pagelinks
  GROUP BY 
    pl_from;

SELECT page_title AS Quelle, pagelinks.pl_title AS Ziel
  FROM page
  JOIN pagelinks ON page_id = pl_from
  ORDER BY page_title;