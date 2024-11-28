USE MediaWiki;

-- AUSGEHENDE LINKS FÜR JEDE SEITE
SELECT page_title, COUNT(page_title) ausgehendeLinks
FROM page p
JOIN pagelinks pl ON p.page_id = pl.pl_from
GROUP BY page_title;

-- EINGEHENDE LINKS FÜR JEDE SEITE
SELECT pl_title, COUNT(pl_title) eingehendeLinks
FROM pagelinks pl, page p
WHERE pl.pl_from=p.page_id
GROUP BY pl.pl_title
ORDER BY eingehendelinks DESC;